The deliverable is complete, valid, and on disk.

## Summary

The PCW turnover package is finalized at `/filesystem/final_batch4__mechanical_task5_pcw_flush_mop__blind/output/submission.zip` with all 7 required files:

- **flush_plan.csv** (56 rows) — full hydraulics, two cascades, correct routing, RETAIN_AND_TOP_UP
- **chemistry_plan.csv** (48 rows) — all products with source_doc/clause traceability; FINAL_FILL reports the increment
- **acceptance_matrix.csv** (84 rows) — all cl.1.5 gates with numeric thresholds
- **schedule.csv** (61 rows) — finishes h626, within TM-4 day 47
- **resources.json** — cost $121,545, chemical orders matching the plan
- **constraint_register.csv** (81 rows) — all 29 key document+clause pairs present, no superseded authority
- **MOP.md** — narrative, governing constraints with margins, defect/conflict resolutions, hazard-comm safety

All validations pass: no fatal placeholders, valid skid vocabulary, no double-booking, water/effluent balance holds, sewer ≤ 540k cap, milestones met, all files decompress and parse correctly.