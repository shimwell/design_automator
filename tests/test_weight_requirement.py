from design_automator import my_custom_design
import json


def test_vessel_weight_against_requirement():
    """Checks that the weight passes the requirement"""

    with open('design_proposed.json') as f:
        proposed_inputs = json.load(f)
    test_design = my_custom_design(**proposed_inputs)
    proposed = test_design.weight()['vessel']

    with open('design_requirements.json') as f:
        design_requirements = json.load(f)
    
    requirement = design_requirements["weight_of_vessel"]

    assert proposed < requirement
