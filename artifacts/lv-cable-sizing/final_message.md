All deliverables are on disk at `/filesystem/electrical__lv_cable_sizing__blind/output/submission.zip` (40,632 bytes, 5 files, integrity OK) and fully validated.

## Summary

In this iteration I audited every `vd_load_a` and `design_current_a` value in `wire_schedule.csv` against the governing circuit-class rules, confirming 100% correctness:
- **Design currents** (EDS-26 2.1/2.1.1): branch circuits = OCPD rating; motor/AC/VFD/elevator/fire-pump/transformer = 1.25 × FLA/rated current; general feeders = max(1.25 × connected, OCPD); service entrance = 2000 A bus ampacity — all 32 correct.
- **Voltage-drop loads** (UFC 3-501-01 3-2.7.4.3): general feeders = OCPD capacity; transformer secondary = 625 A (225 kVA @ 208 V); transformer primary = secondary + 6% loss; motors/AC/VFD/elevator = FLA/rated-load; fire pump = 96 A running; receptacles = 80% capacity; lighting/hard-wired = connected load — all 32 correct.

**Final verified deliverables (all on disk, all open correctly):**
1. `wire_schedule.csv` — 32 rows, 27 columns, all ampacity/VD/design-current/VD-load values correct.
2. `E-621_wire_schedule.dxf` — title block + schedule, agrees with CSV.
3. `calc_book.xlsx` — front_sheet (17 params), duct_assignment (11 rows), cost_ledger ($153,015 total).
4. `design_basis.md` — JSON block (7 keys) + narrative.
5. `constraint_register.xlsx` — 73 single-requirement rows covering all hard families.

All hard constraints pass the self-built validator; installed cost minimised to $153,015 including the 6% campus quantity break.