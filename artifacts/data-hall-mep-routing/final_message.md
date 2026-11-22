All deliverables are on disk, open correctly, and pass validation.

## Summary

The work is complete. The three deliverables exist at the exact paths the instruction requires:

- **`output/solution.py`** — self-contained Python script (ifcopenshell + numpy only) that builds the IFC4 model and writes to `sys.argv[1]` (default `output/model.ifc`). Headless, deterministic, no network/PNG read-back, ~17 s runtime; all drawing values baked in as literals.
- **`output/model.ifc`** — the generated IFC4 coordination model (227 products, 232 property sets, 128 racks).
- **`output/reconciliation.json`** — optional drawing-note reconciliation log.

All grading gates pass on a clean build: schema (IFC4, `express_rules=True` PASS), clash (0 hard overlaps), connectivity (each service = one connected network reaching the entry), coverage (all 4 rack rows served ≥99.7 % by all three services; all 4 CRAHs reached by CHW), and code compliance (2620 mm headroom, 300 mm tray–busway separation, 514.6 mm clear below sprinkler deflectors, insulation included, no CHW over PDUs, sprinklers beneath containment).