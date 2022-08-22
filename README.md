# Current design
Parameter | Value | Units |
|---|---|---|
| blanket offset from source | 10 | m |
| blanket thickness | 10 | m |
| vessel offset from blanket |10 | m |
| blanket material | 10 | |
| blanket Li6 enrichment | 10 | percent |

![latest image](current_design.png)
# Model checks
| Check | Requirement | Current design value | Status |
|---|---|---|---|
| Weight of vacuum vessel | lt 30000000.0kg | 1000000000000.0 |[![test vessel weight requirement](https://github.com/shimwell/design_automator/actions/workflows/test_vessel_weight_requirement.yml/badge.svg)](https://github.com/shimwell/design_automator/actions/workflows/test_vessel_weight_requirement.yml)|
| Radius of vessel | lt 200m | 10000000.0 | [![radius requirement](https://github.com/shimwell/design_automator/actions/workflows/radius_requirements.yml/badge.svg)](https://github.com/shimwell/design_automator/actions/workflows/radius_requirements.yml)
# Neutronics checks
| Check | Requirement | Current design value | Status |
|---|---|---|---|
| Tritium breeding Ratio | ge 1.1 | 0 | [![TBR requirements](https://github.com/shimwell/design_automator/actions/workflows/tbr_requirements.yml/badge.svg)](https://github.com/shimwell/design_automator/actions/workflows/tbr_requirements.yml) |
| Tritium breeding Ratio | lt 3 | 0 | [![TBR requirements](https://github.com/shimwell/design_automator/actions/workflows/tbr_requirements.yml/badge.svg)](https://github.com/shimwell/design_automator/actions/workflows/tbr_requirements.yml) |
| Heating of the blanket | > 1GJ | @BlanketHeating | |

![parameters](./design_parameters.png)
![parameters](./neutron_flux_xy.png)
