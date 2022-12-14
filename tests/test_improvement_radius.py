from design_automator import my_custom_design
import json


def test_vessel_radius_improvement_against_previous():
    """Checks that the radius improves on the last version"""

    with open("design_proposed.json") as f:
        proposed_inputs = json.load(f)

    test_design = my_custom_design(**proposed_inputs)
    proposed = test_design.radius()["vessel"]

    with open("design_successful.json") as f:
        successful_designs = json.load(f)
    previous = successful_designs[-1]["radius_of_vessel"]

    assert proposed <= previous
