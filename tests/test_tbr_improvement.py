from design_automator import my_custom_design
import json


def test_tbr_improvement_against_previous():
    """Checks that the tbr improves on the last version"""

    with open('design_proposed.json') as f:
        proposed_inputs = json.load(f)

    test_design = my_custom_design(**proposed_inputs)
    proposed = test_design.tbr()

    with open('design_successfull.json') as f:
        successfull_designs = json.load(f)

    previous = successfull_designs[-1]["outputs"]["tritium_breeding_ratio"]

    assert proposed > previous
