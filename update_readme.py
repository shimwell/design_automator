import json



# includes TBR, heating, radius, weight etc
with open('design_successfull.json') as f:
    proposed_design = json.load(f)[-1]


with open('README.md', 'w') as readme:
    readme.write('# Current design\n')
    readme.write('Parameter | Value | Units |\n')
    readme.write('|---|---|---|\n')
    readme.write(f'| blanket offset from source | {proposed_design["inputs"]["blanket_offset_from_source"]} | m |\n')
    readme.write(f'| blanket thickness | {proposed_design["inputs"]["blanket_thickness"]} | m |\n')
    readme.write(f'| vessel offset from blanket |{proposed_design["inputs"]["vessel_offset_from_blanket"]} | m |\n')
    readme.write(f'| blanket material | {proposed_design["inputs"]["blanket_material"]} | |\n')
    readme.write(f'| blanket Li6 enrichment | {proposed_design["inputs"]["blanket_li6_enrichment"]} | percent |\n')

    # TODO include image

    readme.write('# Model checks\n')
    readme.write('| Check | Requirement | Current design value | Status |\n')
    readme.write('|---|---|---|---|\n')
    readme.write('| Weight of vacuum vessel | < 1000kg | @vesselweight |[![test vessel weight requirement](https://github.com/shimwell/example_automated_design_checker/actions/workflows/test_vessel_weight_requirement.yml/badge.svg)](https://github.com/shimwell/example_automated_design_checker/actions/workflows/test_vessel_weight_requirement.yml)|\n')
    readme.write('| Radius of vessel | < 10m | @vesselradius |\n')
    readme.write('| Estimated cost | < £100 | @cost |\n')

    readme.write('![latest image](https://github.com/shimwell/example_automated_design_checker/blob/main/current_design.png)\n')

    readme.write('# Neutronics checks\n')
    readme.write('| Check | Requirement | Current design value | Status |\n')
    readme.write('|---|---|---|---|\n')
    readme.write('| Tritium breeding Ratio | > 1.1 | @TBR | [![TBR requirements](https://github.com/shimwell/example_automated_design_checker/actions/workflows/tbr_requirements.yml/badge.svg)](https://github.com/shimwell/example_automated_design_checker/actions/workflows/tbr_requirements.yml) |\n')
    readme.write('| Heating of the blanket | > 1GJ | @BlanketHeating | |\n')
    readme.write('| DPA lifetime limit of vessel | > 50 | @NeutronShieldingVessel | |\n')

    readme.write('![latest image](https://github.com/shimwell/example_automated_design_checker/blob/main/neutron_flux_xy.png)\n')

    readme.write('# Software stack\n')
    readme.write('Requirements tests are run with this software stack\n')

    readme.write('| Name | version |\n')
    readme.write('|---|---|\n')
    readme.write('| OpenMC | 0.13.1 |\n')
    readme.write('| DAGMC | 3.2.2 |\n')
    readme.write('| Paramak | 0.8.3 |\n')
    readme.write('| TENDL nuclear data | 2020 |\n')
