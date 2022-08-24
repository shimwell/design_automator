import json
from design_automator import requirements


# includes TBR, heating, radius, weight etc
with open('design_successful.json') as f:
    latest_design = json.load(f)[-1]


with open('README.md', 'w') as readme:
    readme.write('# Design Parameters\n')
    readme.write('- blanket material: string\n')
    readme.write('- blanket Li6 enrichment: float gt 0. and lt 100.\n')
    readme.write('- vessel offset from blanket: float gt 0.\n')
    readme.write('- blanket thickness: float gt 0.\n')
    readme.write('- blanket offset from source: float gt 0.\n')
    readme.write('\n')
    readme.write('![parameters](./design_parameters.png)\n')

    readme.write('\n')

    readme.write('# Current design\n')
    readme.write('Parameter | Value | Units |\n')
    readme.write('|---|---|---|\n')
    readme.write(f'| blanket offset from source | {latest_design["inputs"]["blanket_offset_from_source"]} | m |\n')
    readme.write(f'| blanket thickness | {latest_design["inputs"]["blanket_thickness"]} | m |\n')
    readme.write(f'| vessel offset from blanket |{latest_design["inputs"]["vessel_offset_from_blanket"]} | m |\n')
    readme.write(f'| blanket material | {latest_design["inputs"]["blanket_material"]} | |\n')
    readme.write(f'| blanket Li6 enrichment | {latest_design["inputs"]["blanket_li6_enrichment"]} | percent |\n')
    readme.write('\n')
    readme.write('![latest image](current_design.png)\n')

    readme.write('# Model checks\n')
    readme.write('| Check | Requirement | Current design value | Status |\n')
    readme.write('|---|---|---|---|\n')

    op = requirements["weight_of_vessel"][0][0].__name__
    val = requirements["weight_of_vessel"][0][1]
    readme.write(f'| Weight of vacuum vessel | {op} {val}kg | {latest_design["outputs"]["weight_of_vessel"]} | [![vessel weight requirement](https://github.com/shimwell/design_automator/actions/workflows/requirement_vessel_weight.yml/badge.svg)](https://github.com/shimwell/design_automator/actions/workflows/requirement_vessel_weight.yml) |\n')

    op = requirements["radius_of_vessel"][0][0].__name__
    val = requirements["radius_of_vessel"][0][1]
    readme.write(f'| Radius of vessel | {op} {val}m | {latest_design["outputs"]["radius_of_vessel"]} | [![radius requirement](https://github.com/shimwell/design_automator/actions/workflows/requirements_radius.yml/badge.svg)](https://github.com/shimwell/design_automator/actions/workflows/requirements_radius.yml) \n')
    # readme.write('| Estimated cost | < £100 | @cost |\n')

    readme.write('# Neutronics checks\n')
    readme.write('| Check | Requirement | Current design value | Status |\n')
    readme.write('|---|---|---|---|\n')

    op = requirements["tritium_breeding_ratio"][0][0].__name__
    val = requirements["tritium_breeding_ratio"][0][1]
    readme.write(f'| Tritium breeding Ratio | {op} {val} | {latest_design["outputs"]["tritium_breeding_ratio"]} | [![TBR requirements](https://github.com/shimwell/design_automator/actions/workflows/requirements_tbr.yml/badge.svg)](https://github.com/shimwell/design_automator/actions/workflows/requirements_tbr.yml) |\n')
    
    op = requirements["tritium_breeding_ratio"][1][0].__name__
    val = requirements["tritium_breeding_ratio"][1][1]
    readme.write(f'| Tritium breeding Ratio | {op} {val} | {latest_design["outputs"]["tritium_breeding_ratio"]} | [![TBR requirements](https://github.com/shimwell/design_automator/actions/workflows/requirements_tbr.yml/badge.svg)](https://github.com/shimwell/design_automator/actions/workflows/requirements_tbr.yml) |\n')

    # readme.write(f'| Heating of the blanket | > 1GJ | @BlanketHeating | |\n')
    # readme.write('| DPA lifetime limit of vessel | > 50 | @NeutronShieldingVessel | |\n')
    readme.write('\n')

    readme.write('![parameters](./neutron_heating_xy.png)\n')

    # readme.write('# Software stack\n')
    # readme.write('Requirements tests are run with this software stack\n')

    # readme.write('| Name | version |\n')
    # readme.write('|---|---|\n')
    # readme.write('| OpenMC | 0.13.1 |\n')
    # readme.write('| DAGMC | 3.2.2 |\n')
    # readme.write('| Paramak | 0.8.3 |\n')
    # readme.write('| TENDL nuclear data | 2020 |\n')
