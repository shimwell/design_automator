class my_custom_design:
    def __init__(
        self,
        blanket_offset_from_source,
        blanket_thickness,
        vessel_offset_from_blanket,
        blanket_material,
        blanket_li6_enrichment,
    ):

        self.blanket_offset_from_source = blanket_offset_from_source
        self.blanket_thickness = blanket_thickness
        self.vessel_offset_from_blanket = vessel_offset_from_blanket
        self.blanket_material = blanket_material
        self.blanket_li6_enrichment = blanket_li6_enrichment
        self.vessel_thickness = 10
        self.blanket_vessel_gap = 5

    def create_cad_model(self):
        import paramak

        blanket = paramak.CenterColumnShieldCylinder(
            name="mat_blanket",
            rotation_angle=360,
            height=500,
            inner_radius=self.blanket_offset_from_source,
            outer_radius=self.blanket_offset_from_source + self.blanket_thickness,
        )
        vessel = paramak.CenterColumnShieldCylinder(
            name="mat_vessel",
            rotation_angle=360,
            height=500,
            inner_radius=self.blanket_offset_from_source + self.blanket_thickness + self.blanket_vessel_gap,
            outer_radius=self.blanket_offset_from_source
            + self.blanket_thickness
            + self.blanket_vessel_gap
            + self.vessel_thickness,
        )
        model = paramak.Reactor([blanket, vessel])
        self.cad_model = model
        return model

    def radius(self):
        radius = {}
        radius["blanket"] = self.blanket_offset_from_source + self.blanket_thickness
        radius["vessel"] = radius["blanket"] + self.blanket_vessel_gap + self.vessel_thickness
        return radius

    def weight(self):
        self.create_cad_model()
        # these could be found from a materials database but are
        # hardcoded for this demonstration project
        vessel_density = 7.7  # g/cm
        blanket_density = 2.1  # g/cm

        volumes = self.cad_model.volume()

        weights = {
            "blanket": volumes[0] * blanket_density,
            "vessel": volumes[1] * vessel_density,
        }
        return weights

    def create_dagmc(self):
        model = self.create_cad_model()
        model.export_dagmc_h5m()
        return "dagmc.h5m"

    def create_neutronics_model(self, dagmc_filename=None):
        if not dagmc_filename:
            dagmc_filename = self.create_dagmc()

        import openmc
        import neutronics_material_maker as nmm
        import openmc_data_downloader as odd

        mat_blanket = nmm.Material.from_library(
            name=self.blanket_material,
            temperature=500,
            enrichment=self.blanket_li6_enrichment,
            enrichment_type="ao",
            enrichment_target="Li6",
        ).openmc_material
        mat_blanket.name = "mat_blanket"
        mat_blanket.temperature = None

        mat_vessel = nmm.Material.from_library(name="P91").openmc_material
        mat_vessel.name = "mat_vessel"

        my_materials = openmc.Materials([mat_blanket, mat_vessel])

        odd.just_in_time_library_generator(libraries=["TENDL-2019"], materials=my_materials)

        # bound_dag_univ = openmc.DAGMCUniverse(filename=dagmc_filename, auto_geom_ids=True).bounded_universe()
        # my_geometry = openmc.Geometry(root=bound_dag_univ)

        # makes use of the dagmc geometry
        dag_univ = openmc.DAGMCUniverse(dagmc_filename)

        # creates an edge of universe boundary at a large radius
        vac_surf = openmc.Sphere(r=10000, surface_id=9999, boundary_type="vacuum")

        # specifies the region as below the universe boundary
        region = -vac_surf

        # creates a cell from the region and fills the cell with the dagmc geometry
        containing_cell = openmc.Cell(cell_id=9999, region=region, fill=dag_univ)

        my_geometry = openmc.Geometry(root=[containing_cell])

        my_source = openmc.Source()
        my_source.space = openmc.stats.Point((0, 0, 0))
        my_source.angle = openmc.stats.Isotropic()
        my_source.energy = openmc.stats.Discrete([14e6], [1])

        my_settings = openmc.Settings(run_mode="fixed source", batches=10, particles=1000, source=my_source)

        my_model = openmc.Model(
            materials=my_materials,
            geometry=my_geometry,
            settings=my_settings,
        )

        return my_model

    def tbr(self, dagmc_filename=None):
        import openmc

        my_model = self.create_neutronics_model(dagmc_filename=dagmc_filename)

        mat_blanket = my_model.materials[0]  # assumes blanket is first material

        my_tallies = openmc.Tallies()
        mat_filter = openmc.MaterialFilter(mat_blanket)
        tbr_tally = openmc.Tally(name="TBR")
        tbr_tally.filters = [mat_filter]
        tbr_tally.scores = ["(n,Xt)"]  # Where X is a wildcard character, this catches any tritium production
        my_tallies.append(tbr_tally)

        my_model.tallies = my_tallies
        import os

        os.system("rm summary.h5")
        os.system("rm statepoint.*.h5")
        statepoint_file = my_model.run()

        sp = openmc.StatePoint(statepoint_file)

        tbr_tally = sp.get_tally(name="TBR")
        df = tbr_tally.get_pandas_dataframe()
        tbr_tally_result = df["mean"].sum()

        return tbr_tally_result

    def heating(self, dagmc_filename=None):
        import openmc

        my_model = self.create_neutronics_model(dagmc_filename=dagmc_filename)

        # Create mesh which will be used for tally
        mesh = openmc.RegularMesh()
        mesh_height = 100  # number of cells in the X and Z dimensions
        mesh_width = mesh_height
        mesh.dimension = [mesh_width, mesh_height, 1]  # only 1 cell in the Y dimension
        mesh.lower_left = [-100, -100, -100]  # physical limits (corners) of the mesh
        mesh.upper_right = [100, 100, 100]

        my_tallies = openmc.Tallies()
        mesh_filter = openmc.MeshFilter(mesh)
        heating_mesh_tally = openmc.Tally(name="heating_mesh")
        heating_mesh_tally.filters = [mesh_filter]
        heating_mesh_tally.scores = ["heating"]
        my_tallies.append(heating_mesh_tally)

        my_model.tallies = my_tallies
        import os

        os.system("rm summary.h5")
        os.system("rm statepoint.*.h5")
        statepoint_file = my_model.run()

        sp = openmc.StatePoint(statepoint_file)

        # access the flux tally
        my_tally = sp.get_tally(name="heating_mesh")
        my_slice = my_tally.get_slice(scores=["heating"])
        my_slice.mean.shape = (mesh_width, mesh_height)

        import matplotlib.pyplot as plt

        fig = plt.subplot()

        # when plotting the 2d data, added the extent is required.
        # otherwise the plot uses the index of the 2d data arrays
        # as the x y axis
        fig.imshow(my_slice.mean, extent=[-100, 100, -100, 100])
        plt.title("neutron heating on xy slice of geometry")
        plt.xlabel("Distance on x axis [cm]")
        plt.ylabel("Distance on y axis [cm]")
        plt.savefig("neutron_heating_xy.png")
