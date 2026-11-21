The Phase 1 foundation strategy study and deliverables for the Cattail Run Data Campus (`CR-P1` … `CR-P6`) have been prepared and packaged into `/filesystem/dc_structural__foundation_strategy__blind/output/submission.zip`.

### Summary of Foundation Strategy & Engineering Decisions

1. **Frost Protection & Bearing Depth:**
   * Air-freezing index for Loudoun County station of record USC00444909 (Lincoln, VA) from the current 1981–2010 NCEI normals product is **556 degree F-days** (superseding the 1951–1980 return period value of 416 degree F-days).
   * Per Loudoun County AHJ Amendment 3, because the 100-year AFI exceeds 500 degree F-days, the governing minimum bearing depth below finished grade is **42 inches** (3.5 ft).
   * All thirty-six foundations across all six building pads share a single uniform bearing elevation of $D_f = 42\text{ in}$ within Stratum I residual lean-to-silty clay (CL-ML, $\phi' = 26^\circ$, $c' = 250\text{ psf}$, $\gamma = 118\text{ pcf}$), avoiding dewatering ($d_w = 8.0\text{ to }21.0\text{ ft}$) and open-cut side-sloping constraints ($D_f \le 4.0\text{ ft}$).

2. **Occupancy & Bearing Capacity Factors of Safety:**
   * In accordance with UFC 3-220-01 Table 2-3, minimum factors of safety on bearing capacity are:
     * `CR-P1`, `CR-P2`, `CR-P3`, `CR-P6` (*Light Industrial, Public*): $\mathbf{FS = 3.5}$.
     * `CR-P4` (*Apartments, Office*): $\mathbf{FS = 3.0}$.
     * `CR-P5` (*Warehouse*): $\mathbf{FS = 2.5}$.
   * Three widely accepted bearing capacity formulations (Meyerhof, Brinch Hansen, and Vesic) were evaluated with shape, depth, and water-table adjustments. Meyerhof's formulation governed and was adopted as the design allowable bearing pressure. Presumptive values were prohibited per AHJ Amendment 4 and UFC 3-220-01 para 2-4.5.2.

3. **Settlement and Tolerable Movement Criteria:**
   * Layered elastic compression was evaluated per FHWA GEC 13 Equation 5-14 / RFI-019 with $dz = 0.25\text{ ft}$ and 2V:1H rectangular stress distribution to $z_{max} = \max(4B, 40\text{ ft})$.
   * All thirty-six foundations satisfy total settlement $s_{tot} \le 1.0\text{ in}$ (UFC 3-220-01 para 2-4.7.1) and angular distortion $\Delta s / L_{span} \le 1/500 = 0.00200$ across all spans (max computed campus angular distortion is 0.00126).

4. **Concrete Durability & Material Specifications:**
   * Soil sulfate testing established: `CR-P1` (0.14%, Class S1), `CR-P2` (0.23%, Class S2), `CR-P3` (0.07%, Class S0), `CR-P4` (0.11%, Class S1), `CR-P5` (0.05%, Class S0), and `CR-P6` (0.26%, Class S2) per EM 1110-2-2000 Table 2-2.
   * Specified concrete strengths selected from available site plant strengths:
     * `CR-P1`, `CR-P3`, `CR-P4`: $f'_c = 4,000\text{ psi}$, max $w/cm = 0.50$ (governed by W1/S1).
     * `CR-P2`, `CR-P6`: $f'_c = 4,500\text{ psi}$, max $w/cm = 0.45$ (governed by S2).
     * `CR-P5`: $f'_c = 5,000\text{ psi}$, max $w/cm = 0.40$ (governed by F3 de-icer apron exposure).
   * Grade 60 reinforcement ($f_y = 60\text{ ksi}$), $\rho \ge 0.0018$, $d = \text{thickness} - 4\text{ in}$.

5. **Campus Foundation Strategy & Rig Mobilisation Optimisation:**
   * **`CR-P1` & `CR-P2`:** Soft soils ($E_{s,I} = 110$ & $85\text{ ksf}$) with heavy data-hall column loads make spread footings infeasible (W1 settles $>1.0\text{ in}$ and column footings up to 39 ft physically collide). **IMPROVED_SPREAD** with rammed aggregate piers is physically required. Served by **Rig 1**.
   * **`CR-P6`:** Soft soil ($E_{s,I} = 95\text{ ksf}$) and heavy loads result in massive spread footings ($B = 25\text{ to }33.75\text{ ft}$) costing $196,610 and overlapping. **IMPROVED_SPREAD** costs $47,252 (saving over $100,000), justifying **Rig 2**.
   * **`CR-P4`:** SPREAD footings cost $58,911. Utilizing the open second slot on Rig 2 allows **IMPROVED_SPREAD** for $34,391 (including modulus test, zero marginal rig mobilisation), yielding a net saving of $24,520.
   * **`CR-P3` & `CR-P5`:** Stiff soils ($E_{s,I} = 210$ & $250\text{ ksf}$) permit compact, fully compliant shallow **SPREAD** footings ($s \le 0.995\text{ in}$ on P3, $s \le 0.799\text{ in}$ on P5; angular distortion $< 1/500$). SPREAD costs $31,317 (P3) and $17,018 (P5) vs. over $70,000 for improved alternatives requiring Rig 3 mobilisation.
   * **Programme Summary:** Exactly **2 rigs mobilised** ($80,000), serving 4 improved pads (`CR-P1`, `CR-P2`, `CR-P4`, `CR-P6`), with 4 production modulus tests ($38,000) and 2 spread-only pads (`CR-P3`, `CR-P5`). Total campus package cost is **$462,660.40**.

---

### Archive Verification

The submission archive `/filesystem/dc_structural__foundation_strategy__blind/output/submission.zip` contains exactly these six files at root:
1. `foundation_geometry.json` — Conforms to Revit family generator schema; contains all 6 pads and 36 foundation units with 3-in dimensioning grids, bearing capacities, settlements, reinforcement, and shear-wall stability parameters (`sliding_fs`, `eccentricity_in`, `uplift_fs`).
2. `ground_improvement_plan.json` — Ground improvement programme specifying $n_s = 10.0$, 30-in pier diameter, 2 mobilised rigs (`RIG-1` and `RIG-2`), 4 modulus tests, pad stiffness moduli, maximum treatment depths, and total linear feet.
3. `foundation_schedule.xlsx` — Foundation schedule populated on the owner's template for all 36 foundations in complete agreement with the geometry JSON.
4. `foundation_feasibility_matrix.md` — Foundation-type feasibility and optimisation matrix documenting structural demands, bearing pressures, settlements, shear-wall checks, governing constraints, and cost comparison between SPREAD and IMPROVED alternatives for every unit.
5. `constraint_register.xlsx` — 54-row register on owner's template documenting every applied code, standard, equation, and table clause, alongside set-aside superseded/cancelled predecessors.
6. `design_basis.md` — Design basis narrative opening with the required fenced JSON block, followed by comprehensive engineering justifications.