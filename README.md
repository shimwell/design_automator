# Design Parameters
- blanket material: string
- blanket Li6 enrichment: float between 0. and 100.
- vessel offset from blanket: float above 0.
- blanket thickness: float above 0.
- blanket offset from source: float above 0.
![parameters](./design_parameters.png)

# Current design
Parameter | Value | Units |
|---|---|---|
| blanket offset from source | 30 | m |
| blanket thickness | 60 | m |
| vessel offset from blanket |5 | m |
| blanket material | Lithium | |
| blanket Li6 enrichment | 10 | percent |

![latest image](current_design.png)
# Model checks
| Check | Requirement | Current design value | Status |
|---|---|---|---|
| Weight of vacuum vessel | lt 30000000.0kg | 24190263.43264143 |[![test vessel weight requirement](https://github.com/shimwell/design_automator/actions/workflows/test_vessel_weight_requirement.yml/badge.svg)](https://github.com/shimwell/design_automator/actions/workflows/test_vessel_weight_requirement.yml)|
| Radius of vessel | lt 200m | 105 | [![radius requirement](https://github.com/shimwell/design_automator/actions/workflows/radius_requirements.yml/badge.svg)](https://github.com/shimwell/design_automator/actions/workflows/radius_requirements.yml)
# Neutronics checks
| Check | Requirement | Current design value | Status |
|---|---|---|---|
| Tritium breeding Ratio | ge 1.1 | 1.3059808923280056 | [![TBR requirements](https://github.com/shimwell/design_automator/actions/workflows/tbr_requirements.yml/badge.svg)](https://github.com/shimwell/design_automator/actions/workflows/tbr_requirements.yml) |
| Tritium breeding Ratio | lt 3 | 1.3059808923280056 | [![TBR requirements](https://github.com/shimwell/design_automator/actions/workflows/tbr_requirements.yml/badge.svg)](https://github.com/shimwell/design_automator/actions/workflows/tbr_requirements.yml) |

![parameters](./neutron_heating_xy.png)
