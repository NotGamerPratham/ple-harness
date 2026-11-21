### Engineering Verification Summary — Package A Register Item 048

**Deliverable Location:** `/filesystem/Thelbridge_Verification_Memo_Item048_BlockB.docx`  
**Addressed To:** Rachel Marlbeck, University Program Director, Thornbury State University, Office of Capital Programs  
**Author:** Adrian Vance, Project Engineer (Structural/Geotechnical), Thelbridge Project Management Services — Owner's Representative  
**Date:** 07/20/2026  
**Subject:** Package A Verification Register Item 048 — Block B Plant-Room Support of Excavation (Submittal 31-SH-B Rev.1 & Rev.2 Supplement KE-L-2026-0713) — Technical Verification Review and Disposition  

---

### Executive Determination & Register Disposition

1. **Verification Determination:** **DISAPPROVED / REJECTED (NOT VERIFIED)**.
2. **Register Status:** **OPEN** (Closure Denied; Revise and Resubmit). In accordance with the Owner’s Written Verification Directive dated 07/06/2026, the item cannot be closed because it has not been verified.
3. **Impact on Planned 08/10/2026 Excavation Start:** **POSTPONED / CANNOT PROCEED**. The contractual hold-point cannot be released. Excavation mobilization for 08/10/2026 is suspended pending redesign, regulatory discharge permitting, EOR foundation impact review, and resubmission.

---

### Key Technical Findings and Engineering Working

#### 1. Scope of Dewatering and Invalidation of Submittal 31-DW-A Reliance
Kesterline’s Rev.2 supplement formally withdrew the Rev.1 dry-excavation assumption, acknowledging that Rowan Bay’s approved Dewatering Plan (*Submittal 31-DW-A Rev.1*) is explicitly restricted to the Block A basement excavation and excludes Block B (*Submittal 31-DW-A Rev.1 §1.2*). However, Kesterline’s conceptual proposal to pump four 8-in relief wells (*RW-B1 through RW-B4*) in its shoring letter does not constitute an approved, engineered, and permitted construction dewatering plan under *Specification Section 31 23 19*. No well hydraulics, pumping test data, drawdown cone analysis, $N+1$ standby generator backup, or Ohio EPA NPDES discharge permits exist in the project record for Block B.

#### 2. Excavation Base Heave Stability Under Artesian Head
* Final excavation subgrade: **El. 726.0 ft**; top of confined dense sand and gravel aquifer: **El. 720.0 ft**; clay plug thickness: $t_{\text{plug}} = 6.0\text{ ft}$.
* Saturated clay unit weight: $\gamma = 120\text{ pcf}$. Total unfactored plug weight: $W = 6.0\text{ ft} \times 120\text{ pcf} = 720\text{ psf}$.
* Per *Design Basis Memorandum CB-DBM-001 Rev.2 §6.2* and *ASCE 7-16 §2.3.1*, counteracting permanent soil weight is factored by $0.90$: $0.9W = 648\text{ psf}$.
* **Controlled Pumped Condition (Head at El. 726.5 ft):** $h_w = 6.5\text{ ft}$, uplift pressure $u = 6.5 \times 62.4 = 405.6\text{ psf}$. $\text{FS}_{\text{heave}} = 648 / 405.6 = 1.60 \ge 1.50$ (adequate *only if continuous pumping is guaranteed*).
* **Ambient Unpumped Condition (Head at El. 738.0 ft logged across 19 monitoring rounds):** $h_w = 18.0\text{ ft}$, artesian uplift pressure $u_{\text{ambient}} = 18.0 \times 62.4 = 1,123.2\text{ psf}$.
  $$\text{Factored Factor of Safety: } \text{FS}_{\text{factored}} = \frac{648\text{ psf}}{1,123.2\text{ psf}} = 0.58 \ll 1.50 \quad (\text{Severe Failure})$$
  $$\text{Unfactored Factor of Safety: } \text{FS}_{\text{unfactored}} = \frac{720\text{ psf}}{1,123.2\text{ psf}} = 0.64 \ll 1.00 \quad (\text{Catastrophic Blow-out})$$
  Net upward burst pressure: $\Delta u_{\text{net}} = 1,123.2 - 648 = 475.2\text{ psf}$ factored ($403.2\text{ psf}$ unfactored). Without active depressurization, instantaneous hydraulic base heave and complete pit flooding will occur upon reaching subgrade. Furthermore, Kesterline's proposed stop-work trigger in §R2.7 (El. 727.0 ft) allows $u = 436.8\text{ psf}$ and $\text{FS} = 1.48 < 1.50$, violating the mandatory project safety margin (*DBM §6.2*).

#### 3. Sheet-Pile Toe Embedment and Unsubstantiated Clay Shear Strength
* Kesterline assumed undrained shear strength $s_u = 1,400\text{ psf}$ to obtain net passive resistance $p_n = 4s_u - \sigma_{v0} = 4(1,400) - 3,106 = 2,494.0\text{ psf}$, passive force $P_p = 16,211\text{ lb/ft}$ over $D = 6.5\text{ ft}$, resisting moment $M_R = 368,800\text{ ft-lb/ft}$, and rotational safety factor $\text{FS}_{\text{toe}} = 1.55$.
* **Audit Discrepancy:** The *Geotechnical Investigation Report KGI-2024-0417 Rev.2 §6.3* explicitly establishes that the undrained shear strength of the CL clay aquitard is $s_u = 900\text{ to } 1,100\text{ psf}$ (mean $1,000\text{ psf}$). Kesterline's $1,400\text{ psf}$ value is an arbitrary, unconservative overstatement by 27% to 56%.
* **Re-analysis with Logged Geotechnical Strength:**
  * Upper-bound ($s_u = 1,100\text{ psf}$): $p_n = 4(1,100) - 3,106 = 1,294.0\text{ psf}$; $P_p = 8,411\text{ lb/ft}$; $M_R = 191,350\text{ ft-lb/ft}$;
    $$\text{FS}_{\text{toe}} = \frac{191,350}{237,293} = 0.81 \ll 1.50 \quad (\text{Rotational Failure})$$
  * Lower-bound ($s_u = 900\text{ psf}$): $p_n = 4(900) - 3,106 = 494.0\text{ psf}$; $P_p = 3,211\text{ lb/ft}$; $M_R = 73,050\text{ ft-lb/ft}$;
    $$\text{FS}_{\text{toe}} = \frac{73,050}{237,293} = 0.31 \ll 1.50 \quad (\text{Gross Failure / Collapse})$$
  * Mean ($s_u = 1,000\text{ psf}$): $p_n = 894.0\text{ psf}$; $P_p = 5,811\text{ lb/ft}$; $M_R = 132,200\text{ ft-lb/ft}$; $\text{FS}_{\text{toe}} = 0.56 \ll 1.50$.
  The sheet-pile toe will kick inward into the excavation, triggering wall collapse.

#### 4. Breach of Confining Aquitard
Lowering the sheet-pile toe to El. 719.5 ft penetrates $0.5\text{ ft}$ into the confined dense sand and gravel aquifer (top at El. 720.0 ft), puncturing the clay aquitard. Hard driving into gravel will declutch and distort interlocks, creating continuous vertical conduits for artesian water (initial head El. 738.0 ft) to discharge into the subgrade (El. 726.0 ft), causing high-velocity piping, sand boils, and ground loss, directly violating *GIR §9.6*.

#### 5. Tieback Ground Anchor Geometric and Geotechnical Failure
* Waler at El. 745.5 ft, inclination 20° below horizontal, free length $25.0\text{ ft}$, bond length $24.0\text{ ft}$.
* Top of bond zone: $745.5 - 25.0 \sin(20^\circ) = \text{El. } 736.95\text{ ft}$.
* Bottom of bond zone: $736.95 - 24.0 \sin(20^\circ) = \text{El. } 728.74\text{ ft}$.
* Top of dense sand and gravel aquifer: **El. 720.0 ft**.
* **Geometric Reality:** The entire $24.0\text{ ft}$ bond zone terminates **8.74 ft above** the sand and gravel aquifer, lying 100% within the compressible CL clay aquitard (El. 738.0 to El. 720.0). Kesterline applied $\tau_{\text{bond}} = 20\text{ psi}$ from *FHWA-IF-99-015 Table 4* for dense sand and gravel to an anchor bonded in cohesive clay.
* Actual clay bond stress is $\tau_{\text{bond}} \approx 6.0\text{ to } 8.0\text{ psi}$, yielding ultimate pullout capacity $Q_{\text{ult}} = 32.6\text{ to } 43.4\text{ kips}$.
* When passive toe resistance is corrected using actual clay strength ($s_u = 900\text{–}1,100\text{ psf}$), required anchor reaction increases from $T_h = 8,803\text{ lb/ft}$ ($T_{\text{design}} = 56.2\text{ kips}$) to $T_h = 14,003\text{ to } 17,469\text{ lb/ft}$ ($T_{\text{design}} = 89.4\text{ to } 111.5\text{ kips}$). Actual capacity ($32.6\text{–}43.4\text{ kips}$) is less than 40% of demand ($\text{FS} = 0.24\text{–}0.48 \ll 2.0$), guaranteeing anchor pullout failure.

---

### Reconciliation of Design Checks

* **Checks That CAN Be Carried Forward:**
  1. *Active Lateral Driving Demand Envelope (§R2.3):* $P_{\text{total}} = 19,610\text{ lb/ft}$ and $M_D = 237,293\text{ ft-lb/ft}$ (incorporates water table at El. 742.0 ft and 250 psf surcharge; verified as active driving baseline).
  2. *Sheet-Pile Section Size (§R2.6):* PZ-35 Grade 50 ($S_x = 48.5\text{ in}^3/\text{ft}$, $M_{\text{allow}} = 121.0\text{ kip-ft/ft}$) is structurally robust and adequate, subject to re-analysis under true boundary reactions.
  3. *Waler Section Sizing (§11.4):* Double MC 12×50 channels ($M_{\text{allow}} = 223.0\text{ kip-ft}$) are adequate to resist corrected anchor reactions ($63.0\text{ to } 78.8\text{ kip-ft}$).
  4. *Anchor Tendon Material (§10.3 / §R2.5):* (4) 0.6-in Grade 270 strand ($0.6\text{ GUTS} = 140\text{ kips}$) is adequate for steel tensile demand.
* **Checks That CANNOT Be Carried Forward:**
  1. *Dewatering Basis (§R2.1):* Unapproved, unpermitted relief wells; no Block B dewatering plan on file.
  2. *Excavation Base Heave (§R2.2):* Fails under ambient artesian conditions ($\text{FS} = 0.58 \ll 1.50$); trigger threshold at El. 727.0 ft yields $\text{FS} = 1.48 < 1.50$.
  3. *Sheet-Pile Toe Embedment (§R2.4):* Overstated $s_u = 1,400\text{ psf}$ yields rotational failure under actual conditions ($\text{FS} = 0.31\text{ to } 0.81 \ll 1.50$).
  4. *Aquitard Penetration (§R2.4):* Toe at El. 719.5 ft punctures confining clay into artesian aquifer (*GIR §9.6* violation).
  5. *Anchor Bond Capacity (§R2.5):* Bond zone is 100% in compressible clay; sand/gravel bond stress ($\tau = 20\text{ psi}$) is invalid; pullout failure occurs ($\text{FS} = 0.24\text{–}0.48$).
  6. *Wall Deflection & Trigger Thresholds (§R2.7):* Deflections will exceed $H/200 = 1.44\text{ in}$; stop-work trigger allows non-conforming safety factors.

---

### Constructive Impact on Permanent Work Already Built at Block B

1. **48 Driven Steel Pipe Piles (Driven 11/2025 to Tips at El. 686–690 ft):** Aquifer depressurization by $11.5\text{ ft}$ ($\Delta u = -717.6\text{ psf}$) triggers downward consolidation drainage throughout the $18\text{ ft}$ normally-consolidated CL clay aquitard. As the clay consolidates and settles relative to the rigid piles, positive shaft resistance ($+85\text{ kips}$ credited in *CB-GEO-004*) reverses into negative skin friction (downdrag) of $85\text{ to } 120+\text{ kips}$ per pile. This plunges net allowable capacity below the design service load of $180\text{ kips}$ per pile, risking structural overstress and foundation plunge.
2. **Continuous 3.0-ft Basement Mat (Cast 01/12/2026, Underside El. 731.5 ft):** The plant-room excavation cuts $5.5\text{ ft}$ below the mat underside. Subgrade loss and dewatering settlement will induce differential settlement exceeding *Spec 31 20 00 Article 3.6* tolerances ($1.0\text{ in}$ total, $0.5\text{ in}$ differential), causing severe structural flexural and punching shear cracking in the mat.
3. **Below-Grade Waterproofing & Construction Joint Waterstops:** Shearing and tilting of the mat will distort and tear the 6-in hydrophilic center-bulb PVC waterstop and rupture the Ordvale Aquastop HD bentonite membrane at permitted construction joint **CJ K-5** (grid K/5), located directly along the plant-room boundary. Pressurized groundwater from the El. 742.0 ft phreatic surface will flood the completed basement.
4. **Permanent Pile Caps:** Breaching the clay aquitard risks artesian piping and boiling, forming subgrade cavities and sinkholes that would undermine adjacent pile caps.

---

### Mandatory Prerequisite Deliverables Prior to Excavation Release

| Item | Required Deliverable | Responsible Party | Governing Reference | Technical Scope & Acceptance Criteria |
| :---: | :--- | :--- | :--- | :--- |
| **1** | **Submittal 31-SH-B Rev.3:** Redesigned SOE Package | **Kesterline Engineering, PC** (Byron A. Halvard, PE) | Spec 31 50 00; DBM Rev.2; GIR Rev.2 §6.3, §9.4, §9.6 | Sealed redesign correcting $s_u$ to $900\text{–}1,100\text{ psf}$; terminating toe $\ge \text{El. } 721.0\text{ ft}$ to preserve a $1.0\text{ ft}$ intact clay seal (or providing watertight cutoff); re-engineering lateral support (multi-level walers, internal rakers, or deep cased tiebacks into SW-GW); re-checking PZ-35 bending and walers; and providing adjacent-structure influence analysis. |
| **2** | **Submittal 31-DW-B:** Block B Dewatering & Depressurization Plan | **Rowan Bay Constructors, Inc.** / Dewatering Specialist (Ohio PE) | Spec 31 23 19; Spec 31 20 00; GIR Rev.2 §7.2, §8.2, §9.4; Ohio EPA NPDES | Comprehensive sealed dewatering plan dedicated to Block B; hydrogeologic pumping test data, well hydraulics, and drawdown modeling; 100% $N+1$ standby generator backup with automatic transfer; real-time piezometer telemetry with stop-work alarm at El. 726.5 ft; emergency ballast plan; Ohio EPA NPDES permit; and clay consolidation settlement analysis. |
| **3** | **Foundation Impact & Pile Downdrag Reconciliation** | **Calloway Braddock Structural Engineers** (Gregory Nash, PE) & **Kelbrook Geotechnical** | GIR Rev.2 §8.1, §8.3, §9.3; DBM Rev.2 §7.1–§7.2; Spec 31 20 00 Art. 3.6 | Formal engineering evaluation assessing Block B pile capacities under consolidation downdrag; differential settlement analysis between Block A and Block B mat; structural flexure and shear checks on existing 3.0-ft mat; and verification of waterproofing/waterstop continuity at CJ K-5. |
| **4** | **Geotechnical & Structural Instrumentation Plan** | **Rowan Bay Constructors, Inc.** / **Kelbrook Geotechnical, Inc.** | Spec 31 50 00; Spec 31 20 00; GIR Rev.2 §4.3, §7.3 | Inclinometers on shoring sheets; high-precision optical survey prisms on existing basement mat, pile caps, and perimeter walls; vibrating-wire piezometers (VW-B1 to VW-B3); and an Action Response Plan with Green, Amber (El. 726.2 ft), and Red / Stop-Work (El. 726.5 ft) thresholds. |

---

### Official Package A Register Entry

* **Item #:** `048`
* **Response / Disposition:**
  > Submittal 31-SH-B Rev.1 as supplemented by Rev.2 (letter KE-L-2026-0713, dated 07/13/2026) has been audited against project geotechnical records (KGI-2024-0417 Rev.2, Appendix A monitoring rounds 1–19, DBM Rev.2, S-101 Rev.4, S-102 Rev.2, and S-201 Rev.4) and is DISAPPROVED (NOT VERIFIED). Verification is DENIED on the following governing grounds: (1) Shoring design relies on conceptual pressure-relief wells, but Contractor has no approved Block B dewatering plan on file (Submittal 31-DW-A Rev.1 is strictly limited to Block A) and no Ohio EPA NPDES permit; (2) Excavation base heave under ambient artesian head El. 738.0 has a factored FS = 0.58 << 1.50 (unfactored FS = 0.64 << 1.0), resulting in immediate catastrophic hydraulic blow-out without fail-safe pumping; proposed stop-work trigger at El. 727.0 gives FS = 1.48, violating DBM §6.2 (FS ≥ 1.50 required); (3) Net passive toe resistance below subgrade is calculated using su = 1,400 psf, directly contradicting logged undrained shear strength Su = 900–1,100 psf (GIR §6.3), resulting in actual toe rotational FS = 0.31–0.81 << 1.50 and toe kick-out collapse; (4) Lowering sheet-pile tips to El. 719.5 breaches the CL clay aquitard, penetrating 0.5 ft into the confined SW-GW aquifer in direct violation of GIR §9.6, creating vertical piping conduits; (5) Tieback ground anchor bond zone (El. 736.95 to 728.74) is located entirely within the compressible CL clay aquitard, terminating 8.74 ft above the sand/gravel stratum; application of τbond = 20 psi is invalid, resulting in actual anchor pullout capacity Qult ≈ 32.6–43.4 kips against true anchor demand of 89.4–111.5 kips (FS = 0.24–0.48, tensile/pullout failure); (6) Dewatering drawdown (Δu = -718 psf) triggers downward consolidation of normally-consolidated clay, converting positive shaft friction to severe downdrag (-85 to -120+ kips) on the 48 permanent Block B piles, overstressing piles beyond design service load (180 kips), and inducing differential settlement and waterstop tearing at construction joint CJ K-5 on the existing basement mat. Excavation scheduled for 08/10/2026 CANNOT PROCEED and is POSTPONED. Contractor must submit: (a) Submittal 31-SH-B Rev.3 (sealed SOE redesign correcting su to 900–1,100 psf, toe at or above El. 721.0, and re-engineered lateral restraint); (b) Submittal 31-DW-B (sealed Block B dewatering/depressurization plan with N+1 backup power, continuous telemetry, and NPDES permit); (c) EOR/Geotechnical foundation impact reconciliation for pile downdrag and mat integrity; and (d) comprehensive instrumentation plan. Status remains OPEN. Item NOT closed.
* **Response By:** `A. Vance (Thelbridge)`
* **Response Date:** `07/20/2026`
* **Status:** `Open`
* **Verification Date:** `—`

---

### Verification Memorandum File Confirmation
The complete memorandum has been issued on the official template form, retaining all five standard sections, detailed calculations, data tables, and formal signature blocks, and is saved at:
`/filesystem/Thelbridge_Verification_Memo_Item048_BlockB.docx`