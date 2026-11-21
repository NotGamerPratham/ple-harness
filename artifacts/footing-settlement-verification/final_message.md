A verification memorandum for **Item 051** of the Package A Verification Register has been issued in accordance with the project record, contractual specifications, and the project memorandum template.

The completed deliverable is saved at:
`/filesystem/Thelbridge_Verification_Memo_Item051_BlockC.docx`

---

### Executive Summary of the Verification Memorandum

* **To:** Adrian Vance, Project Engineer (Structural/Geotechnical), Thelbridge Project Management Services  
* **From:** Rahul Nimkar, Geotechnical Reviewer, Thelbridge Project Management Services  
* **Cc:** Rachel Marlbeck, University Program Director, Thornbury State University  
* **Date:** July 20, 2026  
* **Subject:** Package A Verification Register — Item 051: Block C Spread Footings and Long-Term Clay Settlement Verification  
* **Disposition:** **REJECTED / OPEN — ACTION REQUIRED** (Item cannot be verified or closed)

---

### Key Technical Findings and Working

1. **Fatal Omission in EOR Calculation CB-GEO-007 (Rev.0):**
   * Structural Engineer of Record Gregory Nash, PE (Calloway Braddock) evaluated only immediate elastic settlement in the upper sand using the Schmertmann strain-influence factor method ($S_i = 0.70\text{ to }0.90\text{ in}$, differential $\Delta S_i = 0.20\text{ in}$).
   * On **Sheet 4** (*Consolidation — Long-Term Settlement Contribution — Stratum 2 CL Clay*), the EOR left all consolidation parameters blank and explicitly stated: *"Not computed. Serviceability taken from the immediate settlement result on Sheet 3."*
   * On **Sheet 5**, laboratory consolidation parameters from Vantree Report `VMT-2025-0109-CON` ($C_c = 0.28$, $C_r = 0.045$, $e_0 = 0.92$, $\sigma'_p = 1,900\text{ psf}$) were acknowledged but dismissed as non-governing. This violates direct design instructions in Kelbrook Geotechnical Investigation Report Rev.2 (§8.1 & §9.1) and the Design Basis Memorandum Rev.2 (§7.3).

2. **Independent Geotechnical Consolidation Settlement Analysis:**
   * **Stratum 2 CL Clay Aquitard:** Elevation 738.0 to 720.0 ($H = 18.0\text{ ft} = 216\text{ in}$); in-situ effective overburden at mid-layer (El. 729.0) $\sigma'_0 = 1,850\text{ psf}$; preconsolidation pressure $\sigma'_p = 1,900\text{ psf}$ ($\text{OCR} \approx 1.03$, normally consolidated); compression index $C_c = 0.28$; recompression index $C_r = 0.045$; initial void ratio $e_0 = 0.92$.
   * **Stress Increase:** Applied footing service load stress increase at mid-clay $\Delta\sigma = 900\text{ psf}$ (CB-GEO-007 Sheet 2); final effective stress $\sigma'_f = 2,750\text{ psf} \gg \sigma'_p$.
   * **Primary Consolidation Working ($S_c$):**
     * Standard Virgin Formula (Kelbrook §8.1):  
       $$S_c = \frac{C_c \cdot H}{1 + e_0} \log_{10}\left(\frac{\sigma'_0 + \Delta\sigma}{\sigma'_0}\right) = \frac{0.28 \cdot 216}{1.92} \log_{10}\left(\frac{2,750}{1,850}\right) = 31.50 \cdot 0.17216 = \mathbf{5.42\text{ inches}}$$
     * Two-Part Formula (Recompression + Virgin Compression):  
       $$S_{c,\text{recomp}} = \frac{0.045 \cdot 216}{1.92} \log_{10}\left(\frac{1,900}{1,850}\right) = 0.059\text{ in}$$  
       $$S_{c,\text{virgin}} = \frac{0.28 \cdot 216}{1.92} \log_{10}\left(\frac{2,750}{1,900}\right) = 5.058\text{ in}$$  
       $$S_c = 0.059 + 5.058 = \mathbf{5.12\text{ inches}}$$
   * **Total Settlement:**  
     $$S_{\text{total}} = S_i + S_c = 0.90\text{ in} + 5.12\text{ to }5.42\text{ in} = \mathbf{6.02\text{ to }6.32\text{ inches}}$$  
     *Exceeds the Specification Section 31 20 00 Article 3.6.A total settlement tolerance of **1.0 inch** by over 5 inches (utilization ratio 602% to 632%).*
   * **Differential Settlement and Angular Distortion:**  
     * Perimeter footings experience lower net stress increase ($\Delta\sigma \approx 400\text{ to }500\text{ psf}$), yielding $S_{\text{total}} \approx 3.4\text{ to }4.0\text{ in}$.  
     * Differential settlement $\Delta S_{\text{total}} = \mathbf{1.7\text{ to }2.3\text{ inches}}$, exceeding the contractual tolerance of **0.5 inch over 30 ft** by 240% to 360%.  
     * Angular distortion $\theta \approx 2.0 / (26 \times 12) = \mathbf{1/156}$, more than three times steeper than the AISC Design Guide 3 / Bjerrum structural damage threshold of **1/500**.

3. **Time-Rate of Consolidation:**
   * Double drainage through upper sand and deep aquifer ($H_{dr} = 9.0\text{ ft}$); $c_v = 4.5 \times 10^{-4}\text{ cm}^2/\text{s} = 0.04185\text{ ft}^2/\text{day}$.
   * Time to 50% consolidation: $t_{50} = 381\text{ days}\;(\approx 1.04\text{ years})$.
   * Time to 90% consolidation: $t_{90} = 1,641\text{ days}\;(\approx 4.50\text{ years})$.
   * Settlement will persist well into building occupancy, refuting any assertion that settlement is transient.

4. **Reconciliation with Field Monitoring (Document SM-BLKC-2026-Rev14):**
   * Survey records through Round 15 (06/26/2026, Dennis Halloran, PLS) demonstrate cumulative vertical settlement of **0.61 inches** at interior column footing MP-7 (FTG-C7), and up to **0.30 inches** differential settlement across the footprint.
   * Incremental 14-day settlement rates have not decelerated; the rate has more than doubled from $0.03\text{ in}/14\text{ days}$ during pedestal casting to $0.07\text{ in}/14\text{ days}$ during podium slab-on-grade placement.
   * At 196 days post-baseline, the observed 0.61 in represents immediate elastic movement plus approximately 20% to 25% of primary consolidation developed under staged dead load. The foundation has consumed **61% of total allowable tolerance** before architectural finishes, partitions (Spec 09 21 16), MEP, facade, and occupancy live loads are applied.

---

### Contractual Action Matrix (Requirements Prior to Closing Item 051)

| Action ID | Required Deliverable / Site Action | Scope & Technical Criteria | Responsible Party | Target Date |
| :---: | :--- | :--- | :--- | :---: |
| **A-1** | **Written Notice & Serviceability Disposition** | Formal notification under Spec 31 20 00 Article 3.6.B acknowledging settlement exceedance and providing interim structural safety assessment. | Gregory Nash, PE (Calloway Braddock) | 07/24/2026 |
| **A-2** | **Work Hold Enforcement on Block C** | Site freeze on all permanent work adding structural dead load, CMU/drywall partitions, or finishes to Block C. | Marcus Whitfield / S. Kendrow (Rowan Bay) | Immediate (07/20/2026) |
| **A-3** | **Revised Calculation CB-GEO-007 (Rev.1)** | Re-issue CB-GEO-007 with complete 1D clay consolidation calculations on Sheet 4 for all 12 footings using VMT laboratory test parameters. | Gregory Nash, PE (Calloway Braddock) | 07/31/2026 |
| **A-4** | **Accelerated Monitoring & Crack Gauges** | Increase survey cadence from 14 days to 7 days (Leica LS15); install optical tell-tale crack gauges across partition joints; weekly certified transmittals. | Dennis Halloran, PLS (Rowan Bay Survey) | Weekly (next 07/24/2026) |
| **A-5** | **Block C Foundation Remediation Plan** | Sealed remediation design evaluating underpinning (micropiles through clay to dense aquifer below El. 720.0), stiffened mat with jacking points, or ground improvement. | Gregory Nash, PE (Calloway Braddock) | 08/07/2026 |
| **A-6** | **Geotechnical Review & Concurrence** | Independent geotechnical review and formal concurrence on revised calculations and remediation design. | Alden Roscombe, PE (Kelbrook Geotechnical) | 08/14/2026 |
| **A-7** | **Thelbridge Final Verification & Closeout** | Engineering review of remediation submittals and survey verification to disposition and close Register Item 051. | Rahul Nimkar / Adrian Vance (Thelbridge) | Following A-1 to A-6 |

### Hold-Point Release Clarification (07/22/2026 Level-3 Placement)
The Level-3 concrete placement on July 22, 2026 is located at **Blocks A and B**. Blocks A and B are founded on a continuous 3.0-ft thick reinforced concrete basement mat (underside El. 731.5) and 48 deep driven steel pipe piles bearing in the dense sand and gravel aquifer below El. 720.0, completely decoupled from the Block C spread footings. Therefore, the rejection of Item 051 **does not hold up the Level-3 pour at Blocks A and B** (which depends on materials items 052, 053, 057 and structural items 050, 055). However, **permanent work and additional loading on Block C must remain frozen** until Item 051 is resolved.