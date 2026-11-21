### Engineering Validation Summary & Transmittal

**To:** Marguerite Falk, PE — Technical Director & Reviewing Engineer (AZ PE #42798)  
**From:** Gordon Selby, PE — Owner & Principal Engineer (AZ PE #48213)  
**Date:** 10/10/2025  
**Project:** CFDME-2025-041 — Ocotillo WUI Wildfire, Phase 1  
**Subject:** ASTM E119 Companion Simulation Validation Memo (Phase 1 Report rev B, Section 7)  
**Governing Standard:** CFDME Validation QA Procedure rev 2 (CFDME-QA-VAL-002, ASME V&V 20-2009 aligned); Units & Conversions SOP rev 2

---

### Deliverables Delivered Under `output/`

1. **`output/CFDME-2025-041_ASTM_E119_Validation_Memo.docx`**  
   The complete, formal engineering validation memorandum in Microsoft Word format, structured with firm-standard styling, metadata headers, comprehensive technical sections, analytical comparison tables, reviewer sign-off block, and the draft transmittal for Bianca Rennert.
2. **`output/CFDME-2025-041_ASTM_E119_Validation_Memo.txt`**  
   A complete plain-text copy of the memorandum and all embedded data tables for immediate inspection.
3. **`output/CFDME-2025-041_Phase1_Report_revB_Section7_Insert.docx`**  
   A standalone Word document containing the fully worked Section 7 text ready for direct insertion into `CFDME-2025-041_Phase1_report_revB.docx`.

---

### Key Technical Determinations & Memo Findings

1. **Assembly Match & Certification Basis:**  
   The assembly modeled in the companion simulation is identical in geometry, layering, and materials to the physical specimen tested by Red Butte Fire & Materials Testing (Report No. RBFMT-25-0918, dated 09/24/2025) and certified by Ironwood Fire Protection Engineering (Memo IWFPE-CERT-25-0374, dated 09/29/2025, Marla Kettering, PE). This rests upon an exact parameter match: a 3.05 m × 3.05 m non-load-bearing partition consisting of two 50 mm siliceous-aggregate printed concrete leaves, a 205 mm clear unfilled air cavity, an overall thickness of 305 mm, and continuous 9-gauge (3.8 mm diameter) galvanized steel truss wall ties at 600 mm vertical spacing with 25 mm embedment into each leaf. The geometry represents engineering record OAS-WUI-01_revC (architectural drawing OAS-WA-305mm-DW Rev A). Trevor Buckhalter’s subsequent revD transmittal (adding a 610 mm parapet, 50 mm coping, and 25 mm drip overhang on 10/09/2025 at 16:12:00 -0700) arrived after the 10/09/2025 morning mesh build and does not affect the certified E119 furnace partition.

2. **Governing Criterion, Crossing Times, and Section 7 Stub:**  
   ASTM E119 specifies two unexposed-face thermal-transmission criteria above initial ambient (21.0 °C): average rise $\le 139\text{ }^\circ\text{C}$ (threshold: $160.0\text{ }^\circ\text{C}$) and single-point rise $\le 181\text{ }^\circ\text{C}$ (threshold: $202.0\text{ }^\circ\text{C}$). The earlier criterion governs. In the companion run (`E119_companion_sim_results.csv`):
   * **Single-point criterion ($202.0\text{ }^\circ\text{C}$):** Linear crossing occurs at **$130.94\text{ min}$**, which rounds to **$131\text{ min}$** to the nearest minute (tripped at discrete sample $131\text{ min}$ at $202.1\text{ }^\circ\text{C}$).
   * **Average-rise criterion ($160.0\text{ }^\circ\text{C}$):** Linear crossing occurs at **$176.10\text{ min}$**, which rounds to **$176\text{ min}$** to the nearest minute (tripped at discrete sample $177\text{ min}$ at $160.9\text{ }^\circ\text{C}$).  
   Because $131\text{ min} < 176\text{ min}$, the single-point criterion governs. The prediction **$S = 131\text{ min}$ in the Section 7 stub stands**.

3. **Experimental Data of Record and Disposition on Bianca's Figure:**  
   * **Adopted Value:** Certified laboratory data **$D = 118\text{ min}$** (Red Butte RBFMT-25-0918 §5.2, governed by TC-6 over a steel tie course; Ironwood Memo IWFPE-CERT-25-0374 §2).  
   * **Disposition on Bianca's 129 min:** **REJECTED IN FULL.** Under CFDME Validation Procedure rev 2 Section 6, client-amended numbers are inadmissible absent a formally reissued report from Red Butte (e.g., RBFMT-25-0918-R1 signed by lab manager Glen Whitfield), an accredited calibration certificate, and an explicit laboratory supersession statement. None of these exist; certified $D = 118\text{ min}$ stands.

4. **Model Error, Acceptance Criterion, Uncertainty, and Comparisons:**  
   * **Model Comparison Error:** $E = S - D = 131\text{ min} - 118\text{ min} = \mathbf{+13\text{ min}}$ (explicit sign retained; exact unrounded: $+12.94\text{ min}$). A positive error indicates the simulation over-predicts endurance by $13\text{ min}$ ($+11.0\%$ relative to $D$).
   * **Primary Acceptance Criterion:** $|E| \le 10.0\%\text{ of } D = \mathbf{11.8\text{ min}}$ (limit as it falls; allowable interval: $[106.2\text{ min}, 129.8\text{ min}]$).
   * **Validation Uncertainty ($u_{\text{val}}$):** $u_{\text{val}} = \sqrt{u_{\text{num}}^2 + u_{\text{inp}}^2 + u_{\text{exp}}^2} = \sqrt{(\pm 4\text{ min})^2 + (\pm 6\text{ min})^2 + (\pm 5\text{ min})^2} = \sqrt{77\text{ min}^2} = \mathbf{\pm 8.77\text{ min}}$, reported to whole minutes as **$\mathbf{\pm 9\text{ min}}$**.
   * **Criterion Comparisons:**
     1. $|E| = 13\text{ min} > 11.8\text{ min}$ ($11.0\% > 10.0\%$): **The simulation FAILS the firm primary validation criterion.**
     2. $|E| = 13\text{ min} > u_{\text{val}} = 9\text{ min}$: The error exceeds the validation uncertainty floor, confirming the discrepancy is a **RESOLVED MODEL ERROR** rather than measurement scatter.
   * **Largest Prediction Clearing Criterion:** $S_{\text{max}} = D + 0.10\cdot D = 118\text{ min} + 11.8\text{ min} = \mathbf{129.8\text{ min}}$ (limit as it falls), corresponding to **$129\text{ min}$** as the largest whole-minute prediction.

5. **Two Diagnostic Comparisons & Model Physics:**  
   * **Separation Between Criteria (Average Rise vs. Single Point):**
     * Physical test: $163\text{ min} - 118\text{ min} = \mathbf{45\text{ min}}$.
     * Companion simulation: $176\text{ min} - 131\text{ min} = \mathbf{45\text{ min}}$ (exact crossing difference: $176.10\text{ min} - 130.94\text{ min} = 45.16\text{ min} \approx 45\text{ min}$).
     * *Delta: $0\text{ min}$ ($0.16\text{ min}$ exact).*
   * **Governing Point Elevation Above Nine-Point Mean at Governance:**
     * Physical test: At $118\text{ min}$, TC-6 rose $181\text{ }^\circ\text{C}$ while the 9-TC mean rose $96\text{ }^\circ\text{C}$ $\rightarrow \mathbf{85\text{ }^\circ\text{C}}\text{ (or } 85\text{ K)}$ elevation above mean.
     * Companion simulation: At $131\text{ min}$, $T_{\text{max}} = 202.1\text{ }^\circ\text{C}$ while $T_{\text{avg}} = 110.9\text{ }^\circ\text{C}$ $\rightarrow \mathbf{91.2\text{ }^\circ\text{C}}\text{ (or } 91.2\text{ K)}$ elevation above mean ($91.17\text{ }^\circ\text{C}$ exact crossing).
     * *Delta: $6.2\text{ }^\circ\text{C}\text{ (or } 6.2\text{ K)}$.*
   * **Diagnostic Meaning:** The multi-region conjugate thermal modeling of the metallic truss ties captures the localized thermal bridge with high accuracy ($45\text{ min}$ lag in both; peak within $6.2\text{ }^\circ\text{C}$). Furthermore, both criteria in the simulation lag the test by the identical $+13\text{ min}$ ($131 - 118 = +13\text{ min}$; $176 - 163 = +13\text{ min}$). This proves the error is **NOT a tie or mesh defect, but a GLOBAL thermal delay across the entire assembly**.
   * **Where Rework Belongs:** In the solid-region bulk thermal properties of the concrete leaves (accounting for volumetric heat capacity $\rho \cdot c_p$, moisture vaporization endotherms at $100\text{ }^\circ\text{C}$, and temperature-dependent conductivity $k(T)$) and furnace exposed-face radiative/convective heat flux coupling. Rework does not belong in the ties.
   * **Rework Status:** **NO rework has been started** on the file server as of 10/10/2025.

6. **Phase 1 Programmatic Impact & Case Setup Deficiencies:**  
   Section 7 must report the non-validation finding transparently. Because the current thermal model over-predicts endurance by $11.0\%$ (runs "cold"), using it in the Sprint 2 wildfire LES runs will unconservatively under-predict back-face temperatures under buffelgrass fire exposure. Furthermore, a case-setup audit revealed that Mulshi Simulation Labs improperly cloned a steady, non-reacting high-altitude external aero setup (Dry Wash Aerospace) with $p_{\infty} = 26,500\text{ Pa}$, $\rho_{\infty} = 0.4\text{ kg/m}^3$, no combustion, and no radiation, and misdiagnosed the physical $1.15\text{ s}$ ($0.87\text{ Hz}$) buoyant plume puffing oscillation as "numerical convergence stalling."

7. **Wildfire Claim vs. ASTM E119 & Reporting Form:**  
   ASTM E119 is a standardized, comparative building compartment fire exposure. It does **not** validate real-world wildfire performance under wind-driven, transient buffelgrass fire fronts (which produce $>100\text{ kW/m}^2$ radiant peaks, flame tilt, and ember showers), nor does it evaluate conventional wood-frame construction (no baseline was tested or modeled). Closing this gap requires large-scale physical wildfire testing (e.g., Red Butte's 10/27/2025 window) and direct comparative modeling of a wood-frame assembly. Any future comparison must be reported in the formal ASME V&V 20 format ($S, D, E, u_{\text{val}}$ with units), never as binary yes/no assertions.

8. **Rating Authority, Bianca's Figure, Stamp Language, & Checklist Disposition:**  
   * **Impact of 129 min if Substantiated:** If Red Butte officially reissued the report at $129\text{ min}$, both criteria would exceed $120\text{ min}$ ($129\text{ min}$ and $163\text{ min}$), qualifying the assembly for an upgraded **2-HOUR fire-resistance rating**.
   * **Authority to Act:** **EXCLUSIVELY Marla Kettering, PE (AZ PE #45106) of Ironwood Fire Protection Engineering**, upon receipt of an official, signed reissued report from Red Butte. Neither The CFD ME nor Ocotillo has authority to alter or certify ratings.
   * **Mandatory Stamp Block:**  
     `"CFD thermal analysis only. Fire-resistance rating certified separately by others."`
   * **Marguerite Falk's Checklist Disposition:**
     * **Item 6:** **CLOSED** by this memorandum and Section 7 text.
     * **Items 2, 3, 4, 5, 7, 9, 10:** **STAY OPEN** pending engineering remediation of the case setup, verification body text, and wind-load pressure reconciliation.

---

### Paragraph for Immediate Transmittal to Bianca Rennert Today

> "Bianca — We cannot authorize describing the companion simulation as 'validated against the certified test' in your product launch materials this Friday, nor can The CFD ME support a 2-hour rating claim. Under our governing engineering QA procedure (CFDME-QA-VAL-002 / ASME V&V 20), numerical validation must be measured strictly against the certified third-party laboratory test report of record (Red Butte Report RBFMT-25-0918, $D = 118\text{ min}$). Post-test internal thermocouple calibration adjustments cannot be adopted without a formally reissued, signed test report from Red Butte and an accompanying accredited calibration certificate. Against the certified 118-minute benchmark, our companion simulation predicts 131 minutes to the governing single-point criterion, yielding an error of $E = +13\text{ minutes}$ ($+11.0\%$). This exceeds our firm's 10.0% validation acceptance criterion ($11.8\text{ minutes}$) as well as our validation uncertainty floor ($\pm 9\text{ minutes}$), qualifying as a resolved model error that precludes an unqualified validation claim. Furthermore, Ironwood's official certification memo of record (IWFPE-CERT-25-0374, issued by Marla Kettering, PE) certifies the assembly at a 1-hour fire-resistance rating; only Ironwood is legally empowered to amend that rating if Red Butte ever formally reissues the test data. Finally, ASTM E119 is a standardized comparative furnace test and does not validate real-world wildfire survivability or comparative claims against wood-frame construction. We must resolve these technical differences through proper engineering channels before any public claims are made."