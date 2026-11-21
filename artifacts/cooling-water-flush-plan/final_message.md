A complete turnover package for the Tull Creek Data Hall Process Cooling Water (PCW) cleaning, flushing, and passivation campaign has been engineered, verified, and packaged into `/filesystem/final_batch4__mechanical_task5_pcw_flush_mop__blind/output/submission.zip`.

### Summary of Deliverables

The deliverable archive contains the seven required files:

1. **`flush_plan.csv`** (52 rows):
   - Establishes the full stage sequence across all eight circuits (`C1`–`C8`) using approved tokens (`HYDRO`, `INITIAL_FLUSH`, `CHEM_CLEAN`, `DRAIN_RINSE`, `PASSIVATE`, `HOLD`, `FINAL_FILL`).
   - Identifies circuits lacking accepted hydrostatic pressure charts (`C3`, `C5`, `C6`, `C7`) and schedules their 127.5 psig hydrostatic test per Section 23 21 16 cl. 3.3 and Section 01 91 13 cl. 1.3, while respecting accepted records for `C1`, `C2`, `C4`, and `C8`.
   - Determines flushing flows ensuring >= 4.0 ft/s in all legs for circuits serving plate heat exchangers or cold plates (`C2`–`C6`) and >= 3.28 ft/s (foulant suspension velocity per UFC 3-230-13 cl. 5-3.7) for others (`C1`, `C7`, `C8`).
   - Calculates Darcy-Weisbach head losses with Colebrook-White friction factors and fitting equivalent lengths per DOE-HDBK-1012/3-92, accounting for temporary hoses, strainers, and static lifts against assigned skids (`FS-1200-A`, `FS-600-A`, `FS-600-B`).
   - Allocates water draws and effluent routes (`SEWER` vs `HAUL`), routing copper-laden (`C4`–`C7`) and zinc-laden (`C8`) cleaning solutions and excess `C1` cleaning solution to off-site haulage to protect local sewer limits and maintain total sewer volume under the 500,000-gallon permit cap.
   - Implements a cascade from `C1` final rinse effluent to `C2` first rinse displacement, saving 5,596 gallons.

2. **`chemistry_plan.csv`** (40 rows):
   - Selects cleaning agents based on metallurgy: alkaline cleaner `CL-100` for carbon/stainless steel and copper circuits (`C1`–`C5`, `C7`), and neutral-pH cleaner `CL-210` for aluminum cold plates (`C6`) and galvanized steel (`C8`) to prevent white rust and high-pH corrosion.
   - Carries polyacrylate dispersant `PD-45` at 5.0 ppm active polymer with all cleaning charges per UFC 3-230-13 cl. 5-3.7.
   - Evaluates municipal water analysis (`Cl + SO4 = 860 mg/L > 800 mg/L`), ruling out nitrite-based programs. Selects Molybdate (`MO-500`) at 50 ppm initial / 100 ppm maintenance for `C1`–`C5` and `C7`, and Polysilicate (`PS-330`) at 50 ppm initial / 80 ppm maintenance for `C6` and `C8`.
   - Includes tolyltriazole azole (`TA-90`) at 10 ppm for all copper-wetted circuits (`C4`–`C7`).
   - Declares `RETAIN_AND_TOP_UP` at turnover, pricing whole packages per dosing row.

3. **`acceptance_matrix.csv`** (64 rows):
   - Specifies explicit numeric thresholds, operators, testing methods, sample point tags (low point drains `DV-C1-01` through `DV-C8-01` and outfall `MH-14`), and citations across `RINSE`, `PASSIVATION`, `DISCHARGE`, and `TURNOVER` gates.

4. **`schedule.csv`** (58 rows):
   - Sequence respects maximum 2 commissioning crews (`Crew-1`, `Crew-2`), rented fleet availability (`FS-1200-A` delivered at hour 48), and daily water draw allocations (including SI-04 reductions on Days 2, 3, and 6), achieving zero trucked water draw.
   - Satisfies all contractual milestones from CX-01: TM-1 (Hydro <= Day 6), TM-2 (Cleaning <= Day 22), TM-3 (Passivation <= Day 44), and TM-4 (Turnover <= Day 47).

5. **`resources.json`**:
   - Contains complete structures for `skid_assignment`, `water_profile`, `discharge_profile`, `power_check` (verifying all tie-in kW limits), `chemical_orders` (with lead times and negative pre-mobilisation order dates), and cost breakdown totaling **$71,279.67 USD**.

6. **`constraint_register.csv`** (66 rows):
   - Cites all applied requirements from adopted project documents and standards (`Section 23 25 16`, `Section 23 21 16`, `Section 01 91 13`, `UFC 3-230-13`, `DOE-HDBK-1012/3-92`, `40 CFR 403`, `29 CFR 1910.1200`, `SW-01`, `SW-02`, `SW-03 Rev B`, `SW-04 Rev B`, `SI-04`, `SI-05`, `CX-01 Rev B`, `CX-02`, `M-601 Rev C`, `M-602 Rev C`, `M-603 Rev C`, `VD-01`–`VD-07`, `RFI-022`, `RFI-031`), with zero citations of superseded, cancelled, or non-adopted documents.

7. **`MOP.md`**:
   - Detailed execution narrative and comprehensive design basis.
   - States exact governing constraint lines for each circuit:
     ```text
     GOVERNING CONSTRAINT C1: authorised programme discharge volume (margin 0.0081)
     GOVERNING CONSTRAINT C2: rinse endpoint (margin 0.0198)
     GOVERNING CONSTRAINT C3: rinse endpoint (margin 0.0198)
     GOVERNING CONSTRAINT C4: rinse endpoint (margin 0.0107)
     GOVERNING CONSTRAINT C5: rinse endpoint (margin 0.0107)
     GOVERNING CONSTRAINT C6: rinse endpoint (margin 0.0289)
     GOVERNING CONSTRAINT C7: rinse endpoint (margin 0.0107)
     GOVERNING CONSTRAINT C8: rinse endpoint (margin 0.0359)
     ```
   - Logs conflict resolutions (SW-03 Rev B vs RFI-031; UFC Table 6-2 vs text; UFC Table 5-11 vs Tables 5-14/5-15; rinse tolerance vs window) and document defects (M-PID-103 Rev A, cancelled UFC 3-240-13FN, CX-02 missing charts, VD-08 comfort chiller, Spec 22 11 23 domestic booster).
   - Includes a safety section discharging 29 CFR 1910.1200 hazard communication, PPE, and ANSI Z358.1 emergency wash facility obligations.