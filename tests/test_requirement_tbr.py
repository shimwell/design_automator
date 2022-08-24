from design_automator import my_custom_design, requirements
import json


def test_tbr_against_requirement():
    """Checks that the tbr passes the requirement"""

    with open("design_proposed.json") as f:
        proposed_inputs = json.load(f)
    test_design = my_custom_design(**proposed_inputs)
    proposed = test_design.tbr(dagmc_filename="dagmc.h5m")

    for requirement in requirements["tritium_breeding_ratio"]:
        operator = requirement[0]
        truth_val = requirement[1]
        assert operator(proposed, truth_val)
