from design_automator import my_custom_design
import json


with open("design_proposed.json") as f:
    design = json.load(f)

example_design = my_custom_design(**design)

tbr = example_design.tbr()
heating = example_design.heating()

radius = example_design.radius()["vessel"]
vessel_weight = example_design.weight()["vessel"]

# makes a picture and cad mode l of the design
example_design.cad_model.export_svg("current_design.png")
example_design.cad_model.export_stp("current_design.stp")

# opens
with open("design_successful.json") as f:
    previous_designs = json.load(f)
    print(previous_designs)

design["weight_of_vessel"] = vessel_weight
design["radius_of_vessel"] = radius
design["tritium_breeding_ratio"] = tbr

previous_designs.append(design)

with open("design_successful.json", "w") as f:
    json.dump(previous_designs, f, indent=2)
