The 95% construction document deliverables for the condenser water heat rejection replacement at the Papago Federal Center in Phoenix, Arizona have been engineered, calculated, validated, and packaged into `/filesystem/final_batch4__mechanical_task3_ct_heat_lcc__blind/output/submission.zip`.

### Summary of Selections & Deliverables

1. **Equipment Selections & Operating Basis**:
   - **CUP (Courthouse Central Utility Plant)**:
     - Configuration: 4 cells of CTX-0600-S (1,800.0 gpm total, 450.0 gpm/cell; normal WFR = 0.750, redundant WFR = 1.000).
     - Construction: SS-304 basin and casing, DE-2 drift eliminator (0.002%), premium efficiency TEFC 20 hp motor (91.7% nominal efficiency, 6-pole, NEMA Design B) with VFD.
     - Setpoints & Chemistry: CWSMIN = 75.0 °F, CWSOFFSET = 10.0 °F, scheduled CWSDESIGN = 86.0 °F; COC = 4.14 (Puckorius Scaling Index PSI = 5.60 at design CWR = 96.76 °F).
     - Financials: Investment = $786,200.00, LCC = $5,611,202.31 vs Basic Design $5,776,778.67 (**Net Savings = $165,576.36**).
     - Governing Constraint: `structural capacity` (relative margin 0.0250) against the 120 psf allowable superimposed load in framing zone CUP-S2 (operating weight = 117.0 psf).
   - **ANNEX (Data Annex Condenser Water Plant)**:
     - Configuration: 4 cells of CTX-0600-S (1,800.0 gpm total, 450.0 gpm/cell; normal WFR = 0.750, redundant WFR = 1.000).
     - Construction: SS-304 basin and casing, DE-2 drift eliminator (0.002%), premium efficiency TEFC 20 hp motor (91.7% efficiency, 6-pole) with VFD.
     - Setpoints & Chemistry: CWSMIN = 77.0 °F (respecting chiller min entering rating of 75.0 °F), CWSOFFSET = 11.0 °F, scheduled CWSDESIGN = 86.5 °F; COC = 4.00 (PSI = 5.60 at design CWR = 97.98 °F).
     - Financials: Investment = $786,200.00, LCC = $7,521,498.97 vs Basic Design $7,748,722.15 (**Net Savings = $227,223.17**).
     - Governing Constraint: `electrical capacity` (relative margin 0.0355), with peak coincident demand of 569.06 kW against MCC-R2 spare capacity of 590.0 kW.
   - **LAB (Laboratory Wing Condenser Water Plant)**:
     - Configuration: 3 cells of CTX-0900-H (2,025.0 gpm total, 675.0 gpm/cell; normal WFR = 0.750, redundant WFR = 1.125).
     - Construction: SS-304 basin and casing, DE-2 drift eliminator (0.002%), premium efficiency TEFC 20 hp motor (91.7% efficiency, 6-pole) with VFD.
     - Setpoints & Chemistry: CWSMIN = 61.0 °F, CWSOFFSET = 9.0 °F, scheduled CWSDESIGN = 87.0 °F; COC = 3.87 (PSI = 5.60 at design CWR = 99.07 °F).
     - Financials: Investment = $926,220.00, LCC = $7,742,277.58 vs Basic Design $7,935,639.70 (**Net Savings = $193,362.13**).
     - Governing Constraint: `electrical capacity` (relative margin 0.0093), with peak coincident demand of 635.17 kW against net MCC-R3 spare capacity of 641.14 kW (after deducting 18.86 kW for continuous exhaust fans EF-L7/L8/L9 per RFI-034).

2. **Package Files Delivered in `output/submission.zip`**:
   - `CT_SCHEDULE_CUP.dxf`, `CT_SCHEDULE_ANNEX.dxf`, `CT_SCHEDULE_LAB.dxf`: DXF sheets carrying scheduled fields on `M-CTWR-SCHD`, closed polyline frame outlines on `M-CTWR-PLAN`, and title blocks on `G-TBLK`.
   - `CT_CALC_CUP.xlsx`, `CT_CALC_ANNEX.xlsx`, `CT_CALC_LAB.xlsx`: Five sheets each (`DesignPoint`, `OffDesign` with 180 annual scenario bins summing to 8,760 hours, `WaterBalance`, `Energy`, and `LifeCycleCost`).
   - `constraint_register.csv`: 75 comprehensive constraint citations covering life-cycle costing, climate, configuration, equipment envelopes, chemistry, allocations, electrical distribution, and structural limits without citing any superseded or cancelled documents.
   - `design_basis.md`: Formal design basis recording the governing constraints, the required conflict resolution lines, engineering methodology, and margins.