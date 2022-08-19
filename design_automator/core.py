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

    def create_cad_model(self):
        import paramak

        blanket = paramak.CenterColumnShieldCylinder(
            name="mat_blanket",
            rotation_angle=360,
            height=500,
            inner_radius=self.blanket_offset_from_source,
            outer_radius=self.blanket_offset_from_source + self.blanket_thickness,
        )
        gap = 50
        vessel_thickness = 10
        vessel = paramak.CenterColumnShieldCylinder(
            name="mat_vessel",
            rotation_angle=360,
            height=500,
            inner_radius=self.blanket_offset_from_source + self.blanket_thickness + gap,
            outer_radius=self.blanket_offset_from_source
            + self.blanket_thickness
            + gap
            + vessel_thickness,
        )
        model = paramak.Reactor([blanket, vessel])
        self.cad_model = model
        return model

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

    def tbr(self, dagmc_filename=None):
        if not dagmc_filename:
            dagmc_filename = self.create_dagmc()

        import openmc
        import neutronics_material_maker as nmm

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

        bound_dag_univ = openmc.DAGMCUniverse(filename=dagmc_filename, auto_geom_ids=True).bounded_universe()
        my_geometry = openmc.Geometry(root=bound_dag_univ)

        my_source = openmc.Source()
        my_source.space = openmc.stats.Point((0, 0, 0))
        my_source.angle = openmc.stats.Isotropic()
        my_source.energy = openmc.stats.Discrete([14e6], [1])

        my_settings = openmc.Settings(
            run_mode="fixed source", batches=10, particles=1000, source=my_source
        )

        my_tallies = openmc.Tallies()
        mat_filter = openmc.MaterialFilter(mat_blanket)
        tbr_tally = openmc.Tally(name="TBR")
        tbr_tally.filters = [mat_filter]
        tbr_tally.scores = [
            "(n,Xt)"
        ]  # Where X is a wildcard character, this catches any tritium production
        my_tallies.append(tbr_tally)

        my_model = openmc.Model(
            materials=my_materials,
            geometry=my_geometry,
            settings=my_settings,
            tallies=my_tallies,
        )
        import os
        os.system('rm summary.h5')
        os.system('rm statepoint.*.h5')
        statepoint_file = my_model.run()

        sp = openmc.StatePoint(statepoint_file)

        tbr_tally = sp.get_tally(name="TBR")
        df = tbr_tally.get_pandas_dataframe()
        tbr_tally_result = df["mean"].sum()

        return tbr_tally_result

    def heating(self):
        self.create_dagmc_model()
