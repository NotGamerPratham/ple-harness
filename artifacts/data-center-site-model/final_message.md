I have completed the schematic site layout and 3D BIM model for instance `p6_002` on the wetland-divided parcel in accordance with all standards, conditions of approval, and the IFC4 deliverable contract.

### Summary of Design and Placement

- **Developable Zones & Phasing:**
  - **Phase 1 (Southern Area & Corridor):**
    - `DH_P1` (Data Hall 1): Footprint 75 m × 60 m (4,500 m²), 2 storeys (elevations 0.0 m, 4.5 m), height 9.0 m, GFA 9,000 m² (>= 7,200 m²), aspect ratio 1.25. Located at $[80, 20] \times [155, 80]$.
    - `SUB` (Substation): Footprint 40 m × 25 m (1,000 m²), height 6.0 m. Located at $[188, 175] \times [228, 200]$.
    - `CTP` (Cooling Plant): Footprint 32 m × 25 m (800 m²), height 4.0 m. Located at $[195, 235] \times [227, 260]$.
    - `GEN` (Generator Yard): Footprint 25 m × 20 m (500 m²), height 2.5 m. Located at $[260, 235] \times [285, 255]$.
    - `BRM` (Landscape Berm): Footprint 1,080 m², height 6.0 m, L-shaped configuration positioned along the south and west of the mechanical yard ($[185, 224] \dots [290, 262]$), completely screening `GEN` from viewpoints `R1` and `R2`, and providing 10 dB insertion loss.
    - `RET` (Stormwater Retention Basin): Footprint 45 m × 40 m (1,800 m²), extruded below grade ($[-0.3, 0.0]$ m) with above-grade height 0.0 m. Sized to satisfy the 11.8% impervious surface requirement for both Phase 1 and full campus buildout.
  - **Phase 2 (Northern Area):**
    - `DH_P2` (Data Hall 2): Footprint 75 m × 60 m (4,500 m²), 2 storeys (elevations 0.0 m, 4.5 m), height 9.0 m, GFA 9,000 m² (>= 7,200 m²), aspect ratio 1.25. Located at $[40, 195] \times [115, 255]$.

- **Networks and Connectivity:**
  - **Roads:** Single continuous network entering at the south frontage $[172, 0]$ (edge 0), routing north through the upland corridor between `WET1` and `WET2` without crossing either wetland. Serves `DH_P1`, `SUB`, `CTP`, and `GEN` in Phase 1 (length 343 m), and branches to `DH_P2` in Phase 2 (length 42 m, total road length 385 m). All occupied and hazardous structures are within 18 m of a conforming road.
  - **Medium Voltage:** Linear utility routing connecting Point of Interconnection (POI at $[320, 195]$) to `SUB` (92 m), `SUB` to `DH_P1` (110.1 m), and in Phase 2 `SUB` to `DH_P2` (78.9 m). Total MV length: 281.0 m.
  - **Cost Caps:**
    - Phase 1: $1.0 \times 202.06\text{ m (MV)} + 0.3 \times 343\text{ m (Road)} = 304.96 \le 314.0$.
    - Total Campus: $1.0 \times 280.98\text{ m (MV)} + 0.3 \times 385\text{ m (Road)} = 396.49 \le 473.0$ (well below reference cost of 454.7).

### Verification of the 17 Binding Conditions

1. **Setbacks ($\ge 18$ m):** Min setback = 20.0 m (PASS)
2. **Wetland Buffers ($\ge 8$ m):** Min buffer = 10.0 m (PASS)
3. **Wetland Road Crossings:** None (PASS)
4. **Lot Coverage ($\le 15.1\%$):** 11,300 m² / 89,600 m² = 12.61% $\le$ 15.1% (PASS)
5. **Program Footprint Minimums:** All 7 buildings meet/exceed required areas (PASS)
6. **Data Hall Aspect Ratio ($\le 2.5$):** Both halls are 1.25 (PASS)
7. **Gross Floor Area ($\ge 7,200$ m²):** Both halls provide 9,000 m² GFA (PASS)
8. **Structure Height ($\le 13.8$ m):** Max building height = 9.0 m (PASS)
9. **Floor-to-Floor Height (3.2 m – 5.5 m):** 4.5 m (PASS)
10. **Hazard Separation ($\ge 28$ m):** GEN separation to nearest occupied structure is 33.0 m (PASS)
11. **Apparatus Access ($\le 18$ m):** All occupied and hazardous structures within 13 m – 17 m of road in Phase 1 & Phase 2 (PASS)
12. **Site Entrance:** On south frontage ($y = 0$, edge 0) (PASS)
13. **Stormwater Retention ($\ge 11.8\%$ impervious):** Basin area 1,800 m² $\ge$ required 1,606 m² (PASS)
14. **Noise Limits ($\le 42.35$ dB(A)):** Cumulative sound power at $R_1$: Phase 1 = 36.97 dB, Total = 37.77 dB; at $R_2$: Phase 1 = 38.28 dB, Total = 38.44 dB (PASS)
15. **Visual Screening:** GEN sightlines from $R_1$ and $R_2$ 100% intercepted by berm (PASS)
16. **Medium-Voltage System:** Continuous routing POI $\to$ SUB $\to$ Data Halls within 5 m of served structures (PASS)
17. **Cost Caps:** Phase 1 = 304.96 $\le$ 314; Total = 396.49 $\le$ 473 (PASS)

### Deliverable

The IFC4 model has been written to:
- `submission/model.ifc`