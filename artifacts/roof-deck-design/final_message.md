The roof deck design for Building A of the DC-2 Helena Data Centre has been completed in accordance with all project documents, design criteria, and governing building codes.

The complete deliverable has been written and verified at:
`/filesystem/final_batch4__structural_task7_roof_deck_design__blind/output/submission.zip`

### Deliverable Contents

1. **`deck_design.xlsx`**:
   - **`Zones`**: 9 non-overlapping rectangles strictly covering all $42,192\text{ sq ft}$ of deck net of framed openings (RO-1, RO-2, RO-3), partitioned into two zones:
     - `ZONE-EXT` (South, North, and East perimeter zones): 18 gage NORDECK B-36, support pattern `36/9`, sidelap connector `#10-16` screw (`SCREW-10`), $3$ sidelap connectors per span.
     - `ZONE-INT` (Interior zone): 18 gage NORDECK B-36, support pattern `36/7`, sidelap connector `SCREW-10`, $3$ sidelap connectors per span.
   - **`DesignBasis`**: Complete set of 17 governing design parameters:
     - `PG_PSF` = $63$ | `CE` = $0.90$ | `CT` = $1.00$ | `IS` = $1.10$ | `PF_PSF` = $43.66$ | `GAMMA_PCF` = $22.19$ | `LR_PSF` = $20$ | `QH_PSF` = $29.93$ | `A_ZONE_FT` = $12.8$ | `SDS` = $0.44$ | `IE` = $1.25$ | `R` = $3.25$ | `W_SEISMIC_PSF` = $26.73$ | `FPX_KIP` = $195.4$ | `WIND_X_KIP` = $118$ | `WIND_Y_KIP` = $152$ | `DIAPHRAGM_CLASS` = `semi-rigid`.
   - **`Drifts`**: Peak surcharge and plan extent for each requested obstruction face:
     - `MEP-PH-1`, face `W`: Peak surcharge = $104.3\text{ psf}$, from $x = 60.0\text{ ft}$ to $x = 41.2\text{ ft}$.
     - `SCR-N`, face `S`: Peak surcharge = $89.5\text{ psf}$, from $y = 164.0\text{ ft}$ to $y = 147.8\text{ ft}$.
     - `PARAPET`, face `N`: Peak surcharge = $34.0\text{ psf}$, from $y = 180.0\text{ ft}$ to $y = 167.7\text{ ft}$.
     - `RTU-1`, face `E`: Peak surcharge = $98.2\text{ psf}$, from $x = 36.0\text{ ft}$ to $x = 53.7\text{ ft}$.
   - **`CalcSummary`**: Demands, capacities, and governing scenario declarations for `ZONE-EXT` (governed by $S08$ diaphragm shear, $\text{D/C} = 0.997$) and `ZONE-INT` (governed by $S02$ MEP-PH-1 drift gravity load, $\text{D/C} = 0.909$).
   - **`Diaphragm`**: Scenario-by-scenario lateral response ($S05$, $S06$, $S07$, $S08$, $S10$) reporting maximum shear, in-plane diaphragm deflection ($\text{MDD} \le 1.34\text{ in} < 1.60\text{ in}$ limit), chord axial forces ($\le 30.2\text{ kip} \le 38.0\text{ kip}$ capacity), collector axial forces ($57.7\text{ kip} \le 58.0\text{ kip}$ capacity under $\Omega_0 = 2.0$), and `semi-rigid` classification.
   - **`BOM`**: Material takeoff:
     - `deck area 18 gage`: $42,192\text{ sf}$
     - `support fasteners`: $19,248\text{ ea}$
     - `sidelap connectors`: $7,032\text{ ea}$

2. **`roof_deck_plan.dxf`**:
   - Closed `LWPOLYLINE` boundaries for each zone rectangle on layer `S-DECK-ZONE`.
   - Centered `TEXT` zone labels (`ZONE-EXT`, `ZONE-INT`) on layer `S-DECK-TEXT`.
   - Complete framing layout (joists, girders, columns, braces, perimeter edge angle) on layer `S-FRAMING`.
   - Roof openings (RO-1, RO-2, RO-3) on layer `S-OPENING`.

3. **`constraint_register.xlsx`**:
   - 77 verified governing requirements in sheet `Register` across `EOR-DC-RD-01 Rev 2`, `LAT-2026-003 Rev 1`, `SNOW-2026-014 Rev 0`, `OBD-DC2-A Rev A`, `NORDECK B-36 Manual 2026`, and `29 CFR 1926.754(e)(3)`.
   - No superseded documents cited, exact numerical values matching source clauses, and clean descriptive bindings.

4. **`design_basis.md`**:
   - Full engineering narrative detailing the governing document hierarchy, IFC coordination model precedence, SCR-N relocation, snow drift calculations, seismic weight evaluation including snow contribution, 2D in-plane FE diaphragm analysis, MDD/ADVE classification rationale, chord/collector splice verifications, and constructability/cost optimization.