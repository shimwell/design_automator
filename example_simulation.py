from design_automator import my_custom_design
import json


with open("design_proposed.json") as f:
    proposed_inputs = json.load(f)

example_design = my_custom_design(**proposed_inputs)

tbr = example_design.tbr()
heating = example_design.heating()

radius = example_design.radius()["vessel"]
vessel_weight = example_design.weight()["vessel"]

# makes a picture and cad mode l of the design
example_design.cad_model.export_svg('current_design.png')
example_design.cad_model.export_stp('current_design.stp')

# opens 
with open("design_successful.json") as f:
    previous_designs = json.load(f)
    print(previous_designs)

previous_designs.append(
    {
        "inputs": proposed_inputs,
        "outputs": {
            "weight_of_vessel": vessel_weight,
            "radius_of_vessel": radius,
            "tritium_breeding_ratio": tbr,
        }
    }
)

with open("design_successful.json", "w") as f:
    json.dump(previous_designs, f, indent=2)
