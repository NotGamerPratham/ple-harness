All deliverables are complete and verified on disk at `/filesystem/final_batch4__mechanical_task3_ct_heat_lcc__blind/output/submission.zip`:

**Submission.zip** (8 files, integrity verified):
- `CT_SCHEDULE_CUP.dxf`, `CT_SCHEDULE_ANNEX.dxf`, `CT_SCHEDULE_LAB.dxf` — schedule + roof-layout sheets with the three required layers (`M-CTWR-SCHD` `<TAG> <KEY> <VALUE>` texts, `M-CTWR-PLAN` one closed LWPOLYLINE per cell in M-401 coordinates, `G-TBLK` title block carrying a revision).
- `CT_CALC_CUP.xlsx`, `CT_CALC_ANNEX.xlsx`, `CT_CALC_LAB.xlsx` — five-sheet workbooks (DesignPoint, OffDesign with 180 rows summing to 8760 h all numeric, WaterBalance, Energy, LifeCycleCost); LCC = investment + PVs − salvage and NS = basic − LCC both reconcile; component energies sum to plant energy.
- `constraint_register.csv` — 68 requirements with the required columns, citing only adopted documents.
- `design_basis.md` — governing documents, method, selected designs, three documented conflict lines, and one `GOVERNING CONSTRAINT <plant>: <name> (relative margin <value>)` line per plant (CUP/LAB = electrical capacity; ANNEX = water allocation).

**Selected designs** (EnergyPlus YorkCalc tower + ElectricEIR chiller basis, Phoenix LCD 2022–24 bins, 80 °F design WB, 81 °F redundancy WB, 99.6% DB 41 °F → no basin heater, LOSS-FACTOR declared for water balance with SATURATED-EXIT priced in the LCC):
- CUP: CTX-0600-S, 4 cells, 1800 gpm, floor 75/offset 10, COC 3.94, DE-2, SS-304 — NS ≈ $210k.
- ANNEX: CTX-0600-S, 4 cells, 1800 gpm, floor 75/offset 11, COC 3.80, DE-2, SS-304 — NS ≈ $253k.
- LAB: CTX-0900-H, 3 cells, 2025 gpm, floor 60/offset 9, COC 3.71, DE-2, SS-304 — NS ≈ $259k.