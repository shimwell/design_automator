from design_automator import my_custom_design
import json

def test_production_of_stp_files():
    

    with open('proposed_design.json') as f:
        proposed_inputs = json.load(f)

    print(proposed_inputs)
    assert 1==2