The lateral engineering package for Building A2 at the Northern Divide Data Campus has been completed, fully checked, and packaged into the required archive:

**Deliverable Location:**  
`/filesystem/final_batch4__structural_task5_wind_diaphragm_shear__blind/output/submission.zip`

### Deliverable Contents

The zip archive contains exactly the five required deliverable files:

1. **`lateral_schedule.xlsx`** — Complete workbook containing all nine required worksheets:
   * `DeckZones`: 12 zones with selected deck profiles (`D22-36/4-2`, `D22-36/7-2`, `D22-36/7-4`), tabulated shear stiffnesses ($G'$ adjusted by 1.15 in mechanical bay Z22 for 4 ft joist spacing), ASD capacities, areas, and costs.
   * `ChordSchedule`: 12 boundary chord and collector lines with scheduled plate sections (`PL4x3/8` on Line C-E2, `PL3x3/8` on all other lines), lengths, and erected costs.
   * `Piers`: 73 cantilever piers derived from the 2026 federated model and scan, recording wall line, extents ($s_0, s_1$), thickness, top elevation, Timoshenko cantilever stiffness $k$, scheduled Type E1 deck-to-panel embeds (146 total), and Type T1 base tie-down requirement (`yes`/`no`, 17 panels requiring tie-down).
   * `ShearWalls`: 72 rows reporting ASD roof-level line loads and shear wall reactions across all 12 wind scenarios (W01–W12) and 6 wall lines (S, E, N1, W, N2, E2).
   * `Diaphragm`: 216 rows reporting recovered ASD unit shears at quarter-point stations (0.25, 0.50, 0.75) for all scenarios and lines.
   * `Chords`: 144 rows reporting peak ASD axial forces for all chord and collector lines across all scenarios.
   * `Drift`: 24 rows reporting relative diaphragm deflections along global X and Y (peak $0.2820\text{ in}$ along X, $0.5187\text{ in}$ along Y, meeting the $0.55\text{ in}$ campus limit).
   * `Convergence`: 3 mesh refinement levels (L1 $H=10\text{ ft}$, L2 $H=5\text{ ft}$, L3 $H=2.5\text{ ft}$), demonstrating a 0.17% relative change between L2 and L3 in the reaction of wall line W under scenario W01 (well within the 5% acceptance limit).
   * `Cost`: Itemized bill of quantities summing to a certified installed package cost of **$224,030.94** (compliant with the $310,000 cap).

2. **`diaphragm_plan.dxf`** — Plan view drawings on the building grid in feet, containing both the **TRANSVERSE** and **LONGITUDINAL** directions, stating on its face that all loads shown are ASD, and carrying all required layers: `S-DIAP-SHEAR`, `S-DIAP-ZONE`, `S-WALL-REAC`, `S-CHRD`, `S-COLL`, `S-ANNO-TEXT`, and `S-GRID`.

3. **`constraint_register.xlsx`** — Sheet `Register` containing 111 verified requirement rows citing only current, non-superseded project documents (`EOR-NDDC-A2-S01` Rev 2, `WT-2026-07`, `TS-2026-02`, `NDDC-AHJ-014`, `ALTA-2025-77`, `SR-2026-118`, `OBD-NDDC-A2`, `Spec 01 33 00`, `CDS-B36`, `KRS-CH`, `KRS-CN`, `SJ-201`), matching exact clauses, values, and units.

4. **`calculations.pdf`** — A 3-page 8-1/2 x 11 portrait calculation package covering: executive summary; ASCE 7-16 wind parameters ($V = 115\text{ mph}$, Exposure C, $K_{zt} = 1.19$, $K_e = 0.8671$, $q_h = 28.75\text{ psf}$, $q_p = 29.37 / 30.31\text{ psf}$); parapet simple-beam cantilever lever action; DIAPH-MT 1.0 semi-rigid FE formulation and exact reproduction of benchmark VE-1; L1/L2/L3 mesh convergence study; deck zone shears; chord/collector member designs; shear wall reactions and overturning stability; deflection/drift checks; and cost summary.

5. **`design_basis.md`** — Design basis narrative carrying:
   * Required Parameter Table 1 (`Kzt`: 1.19, `Ke`: 0.8671, `q_h_psf`: 28.75, `screen_wall_top_ft`: 36.00, `asbuilt_opening_panel`: S14, `asd_combination`: 0.6W, `omega_d`: 2.35, `analysis_method`: DIAPH-MT 1.0 semi-rigid finite element model, `mesh_level`: L2).
   * Required Governing Scenario Table 2 (Line S: W05; Line E: W03; Line N1: W01; Line W: W07; Line N2: W01; Line E2: W07).
   * Detailed prose resolving all document conflicts (115 mph / Risk Category III vs preliminary 105 mph; $K_{zt} = 1.19$ vs 1.00; $K_e = 0.8671$ vs 1.00; north screen wall elevation +36.00 ft vs 2024 shop schedule +31.00 ft; field-cut opening S14-O1 with 1.5 ft leg neglected; and semi-rigid FE model required vs flexible/rigid distributions).