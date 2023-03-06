[video explain](https://www.youtube.com/watch?v=UcV1SxdXLqs)

# Design Parameters
- blanket material: string
- blanket Li6 enrichment: float gt 0. and lt 100.
- vessel offset from blanket: float gt 0.
- blanket thickness: float gt 0.
- blanket offset from source: float gt 0.

![parameters](./design_parameters.png)

# Current design
Parameter | Value | Units |
|---|---|---|
| blanket offset from source | 30 | m |
| blanket thickness | 60 | m |
| vessel offset from blanket |5 | m |
| blanket material | Lithium | |
| blanket Li6 enrichment | 15 | percent |

![latest image](current_design.png)
# Model checks
| Check | Requirement | Current design value | Status |
|---|---|---|---|
| Weight of vacuum vessel | lt 30000000.0kg | 24190263.43264143 | [![vessel weight requirement](https://github.com/shimwell/design_automator/actions/workflows/requirement_vessel_weight.yml/badge.svg)](https://github.com/shimwell/design_automator/actions/workflows/requirement_vessel_weight.yml) |
| Radius of vessel | lt 200m | 105 | [![radius requirement](https://github.com/shimwell/design_automator/actions/workflows/requirements_radius.yml/badge.svg)](https://github.com/shimwell/design_automator/actions/workflows/requirements_radius.yml) 
# Neutronics checks
| Check | Requirement | Current design value | Status |
|---|---|---|---|
| Tritium breeding Ratio | ge 1.1 | 1.32566240631087 | [![TBR requirements](https://github.com/shimwell/design_automator/actions/workflows/requirements_tbr.yml/badge.svg)](https://github.com/shimwell/design_automator/actions/workflows/requirements_tbr.yml) |
| Tritium breeding Ratio | lt 3 | 1.32566240631087 | [![TBR requirements](https://github.com/shimwell/design_automator/actions/workflows/requirements_tbr.yml/badge.svg)](https://github.com/shimwell/design_automator/actions/workflows/requirements_tbr.yml) |

![parameters](./neutron_heating_xy.png)

# Improvement tracking![parameters](./improvement_tritium_breeding_ratio.png)
![parameters](./improvement_radius_of_vessel.png)
![parameters](./improvement_weight_of_vessel.png)
