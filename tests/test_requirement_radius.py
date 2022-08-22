from design_automator import my_custom_design, requirements
import json


def test_vessel_radius_against_requirement():
    """Checks that the radius passes the requirement"""

    with open('design_proposed.json') as f:
        proposed_inputs = json.load(f)
    test_design = my_custom_design(**proposed_inputs)
    proposed = test_design.radius()['vessel']

    for requirement in requirements["radius_of_vessel"]:
        operator = requirement[0]
        truth_val = requirement[1]
        assert operator(proposed, truth_val)
