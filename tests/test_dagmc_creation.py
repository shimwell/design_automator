from design_automator import my_custom_design
import json
from pathlib import Path
import os


# def test_dagmc_file_creation():
#     """Checks that the dagmc file can be made"""

#     os.system('rm dagmc.h5m')

with open('design_proposed.json') as f:
    proposed_inputs = json.load(f)
test_design = my_custom_design(**proposed_inputs)

test_design.create_dagmc()

test_design.cad_model.export_image_3d()

assert Path("dagmc.h5m").is_file()
