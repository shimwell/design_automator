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
| Weight of vacuum vessel | < 1000kg | 1000000000000.0 |[![test vessel weight requirement](https://github.com/shimwell/design_automator/actions/workflows/test_vessel_weight_requirement.yml/badge.svg)](https://github.com/shimwell/design_automator/actions/workflows/test_vessel_weight_requirement.yml)|
| Radius of vessel | < 10m | 10000000.0 | [![radius requirement](https://github.com/shimwell/design_automator/actions/workflows/radius_requirements.yml/badge.svg)](https://github.com/shimwell/design_automator/actions/workflows/radius_requirements.yml)
# Neutronics checks
| Check | Requirement | Current design value | Status |
|---|---|---|---|
| Tritium breeding Ratio | > 1.1 | @TBR | [![TBR requirements](https://github.com/shimwell/design_automator/actions/workflows/tbr_requirements.yml/badge.svg)](https://github.com/shimwell/design_automator/actions/workflows/tbr_requirements.yml) |
| Heating of the blanket | > 1GJ | @BlanketHeating | |
![latest image](https://github.com/shimwell/design_automator/blob/main/neutron_flux_xy.png)
