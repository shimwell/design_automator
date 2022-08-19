from design_automator import my_custom_design
import json


with open("design_proposed.json") as f:
    proposed_inputs = json.load(f)

example_design = my_custom_design(**proposed_inputs)

tbr = example_design.tbr(dagmc_filename="dagmc.h5m")

with open("design_successfull_temp.json") as f:
    cad_results = json.load(f)
    print(cad_results)

with open("design_successfull.json") as f:
    previous_designs = json.load(f)
    print(previous_designs)

previous_designs.append(
    {
        "inputs": proposed_inputs,
        "outputs": {
            "weight_of_vessel": cad_results['vessel_weight'],
            "radius_of_vessel": cad_results['radius'],
            "tritium_breeding_ratio": tbr,
            "heating_ of_the_blanket": 10e6,
        }
    }
)

with open("design_successfull2.json", "w") as f:
    json.dump(previous_designs, f, indent=2)
