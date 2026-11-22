All deliverables are complete and verified on disk.

## Summary

Delivered at `/app/files/dc_model__hall_seed005_d100__mep_routing/output/`:
- **`solution.py`** — self-contained IFC4 build script (ifcopenshell + numpy only, millimetre units / metre placements, headless, deterministic, ~1.4 s, no network, no PNG re-read).
- **`model.ifc`** — IFC4, 328 products, **0 express-rule errors**, **0 clashes** (self AABB check).
- **`reconciliation.json`** — drawing-note reconciliation log with per-service length splits.

The model rebuilds the ~27×24 m hall exactly as drawn (94 racks with cold-aisle facings, 6 perimeter CRAHs, 4 PDUs, 12 columns on the 7200 mm grid offset 150 mm, 104 sprinkler heads, raised access floor, cold-aisle containment with no roofs) and routes the three services clash-free: tray & busway overhead in separate lanes that never cross (≥800 mm in Y, 1400 mm busway supports ≤1500 max), and chilled water in the under-floor plenum (clear of columns, sprinklers, and the 1800 mm PDU reserved space) reaching every CRAH within 2500 mm. Verified: 94 racks, 104 sprinklers, 12 columns, 6 CRAHs, 4 PDUs; tray 81400 mm overhead, busway 109600 mm overhead, CHW 3860 mm overhead + 85700 mm under-floor.