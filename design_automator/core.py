
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
        pass
        # import paramak

        # blanket = CenterColumnShieldCylinder(
        #     rotation_angle= 360,
        #     height = 500, 
        #     inner_radius = blanket_offset_from_source
        #     outer_radius = blanket_offset_from_source + blanket_thickness
        # )
        # gap = 50
        # vessel_thickness = 10
        # vessel = CenterColumnShieldCylinder(
        #     rotation_angle= 360,
        #     height = 500, 
        #     inner_radius = blanket_offset_from_source + blanket_thickness + gap
        #     outer_radius = blanket_offset_from_source + blanket_thickness + gap + vessel_thickness
        # )
        # model = paramak.Reactor(blanket, vessel)
        # self.cad_model = model
        # return model

    def create_dagmc_model(self):
        pass

    def simulate_tbr(self):
        pass

    def simulate_dpa(self):
        pass

    def simulate_heating(self):
        pass

