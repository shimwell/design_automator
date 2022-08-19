

# Current design

| Parameter | Value | Units |
|---|---|---|
| blanket offset from source | @blanketoffset | m |
| blanket thickness | @blanketoffset | m |
| vessel offset from blanket | @vesseloffset | m |
| blanket material | @blanketmaterial | |
| blanket Li6 enrichment | @blanketenrichment | percent |


# Model checks
| Check | Requirement | Current design value | Status |
|---|---|---|---|
| Weight of vacuum vessel | < 1000kg | @vesselweight |[![test vessel weight requirement](https://github.com/shimwell/example_automated_design_checker/actions/workflows/test_vessel_weight_requirement.yml/badge.svg)](https://github.com/shimwell/example_automated_design_checker/actions/workflows/test_vessel_weight_requirement.yml)|
| Radius of vessel | < 10m | @vesselradius |
| Estimated cost | < £100 | @cost |

![latest image](https://github.com/shimwell/example_automated_design_checker/blob/main/current_design.png)

# Neutronics checks
| Check | Requirement | Current design value | Status |
|---|---|---|---|
| Tritium breeding Ratio | > 1.1 | @TBR | [![TBR requirements](https://github.com/shimwell/example_automated_design_checker/actions/workflows/tbr_requirements.yml/badge.svg)](https://github.com/shimwell/example_automated_design_checker/actions/workflows/tbr_requirements.yml) |
| Heating of the blanket | > 1GJ | @BlanketHeating | |
| DPA lifetime limit of vessel | > 50 | @NeutronShieldingVessel | |

![latest image](https://github.com/shimwell/example_automated_design_checker/blob/main/neutron_flux_xy.png)

# Software stack
Requirements tests are run with this software stack

| Name | version |
|---|---|
| OpenMC | 0.13.1 |
| DAGMC | 3.2.2 |
| Paramak | 0.8.3 |
| TENDL nuclear data | 2020 |