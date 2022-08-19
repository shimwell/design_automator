from design_automator import my_custom_design
import json


with open("design_proposed.json") as f:
    proposed_inputs = json.load(f)

example_design = my_custom_design(**proposed_inputs)

radius = example_design.radius()["vessel"]
vessel_weight = example_design.weight()["vessel"]

example_design.cad_model.export_svg('current_design.png')

results = {
    "weight_of_vessel": vessel_weight,
    "radius_of_vessel": radius,
    }


with open("design_successfull_temp.json", "w") as f:
    json.dump(results, f, indent=2)
