from design_automator import my_custom_design, requirements
import json


def test_vessel_weight_against_requirement():
    """Checks that the weight passes the requirement"""

    with open("design_proposed.json") as f:
        proposed_inputs = json.load(f)
    test_design = my_custom_design(**proposed_inputs)
    proposed = test_design.weight()["vessel"]

    for requirement in requirements["weight_of_vessel"]:
        operator = requirement[0]
        truth_val = requirement[1]
        assert operator(proposed, truth_val)
