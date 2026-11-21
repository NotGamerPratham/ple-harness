A witness-test scope and scheduling package and the System Operations Center (SOC) release determinations have been established for the municipal array commissioning batch as of **07/14/2025** (pre-dating the 08/15/2025 Alleron Municipal League response). 

The deliverable has been generated and filed as a Word document named **`Municipal_Witness_Test_Package.docx`** in the Program Office's municipal commissioning folder in the document store (Nextcloud: `/DER_Program/Commissioning/Municipal/Municipal_Witness_Test_Package.docx`, with a synchronized local copy at `/filesystem/Commissioning/Municipal/Municipal_Witness_Test_Package.docx`).

---

### Key Findings & Determinations Summary

#### 1. Batch Scope Determination as of 07/14/2025
* **Initial Population (6 arrays):** Covered by `Checklist_Cravenwood_High.pdf` through `Checklist_Tresbay_Community_Center.pdf`.
* **Out of Scope (Withdrawn):** **Tresbay Community Center Array** (PXA-2025-0061, 560 kW) formally withdrew its interconnection request on **07/09/2025** per case tracking (OpenProject Project 3, Case #45) and POL-QM-05 Rev 3 §2.
* **Active In-Scope Population (5 arrays):**
  1. Cravenwood High School Array (860 kW)
  2. Darnwick Elementary School Array (640 kW)
  3. Holcott Public Library Array (510 kW)
  4. Lockmere Middle School Array (720 kW)
  5. Marden Falls Water Reclamation Facility (WRF) Array (980 kW)

---

#### 2. Certified Equipment List Carriage Analysis (CEL-2025-Q2 vs. CEL-2024-Q4)
Per the **Witness Test & Waiver Procedure (ENG-PRC-014 Rev 3 §3)**, waiver eligibility applies *only* to equipment listed on the *current* edition in force on the waiver date (**CEL-2025-Q2**, effective 04/30/2025). Models appearing solely on superseded lists or delisted between editions confer zero waiver eligibility:

1. **Cravenwood High School Array (860 kW):**
   * *Inverter Installed:* Solmery Power SM-215K-3P.
   * *Carriage Call:* **CARRIED** (CEL-2025-Q2 Inverters tab, row 6; UL 1741-SB).
   * *Waiver Eligibility:* Eligible for waiver (final disposition stays with Standards Engineering).
2. **Darnwick Elementary School Array (640 kW):**
   * *Inverter Installed:* Arvexa PV-750.
   * *Carriage Call:* **NOT CARRIED** (absent from CEL-2025-Q2 and superseded CEL-2024-Q4).
   * *Waiver Eligibility:* **INELIGIBLE FOR WAIVER**. On-site witness test is mandatory before PTO.
3. **Holcott Public Library Array (510 kW):**
   * *Inverter Installed:* Selvix SV-720.
   * *Carriage Call:* **NOT CARRIED** (listed on superseded CEL-2024-Q4, but delisted/removed from CEL-2025-Q2 per Front Matter change summary).
   * *Waiver Eligibility:* **INELIGIBLE FOR WAIVER** per ENG-PRC-014 Rev 3 §3 Corollaries 3 & 5. On-site witness test is mandatory before PTO.
4. **Lockmere Middle School Array (720 kW):**
   * *Inverter Installed:* Torvane Electric TE-180K (4 units).
   * *Carriage Call:* **CARRIED** (CEL-2025-Q2 Inverters tab, row 14; UL 1741-SB).
   * *Waiver Eligibility:* Eligible for waiver (final disposition stays with Standards Engineering).
5. **Marden Falls Water Reclamation Facility Array (980 kW):**
   * *Inverter Installed:* Solmery Power SM-245K-3P (4 units).
   * *Carriage Call:* **CARRIED** (CEL-2025-Q2 Inverters tab, row 7; UL 1741-SB).
   * *Waiver Eligibility:* Eligible for waiver (final disposition stays with Standards Engineering).

---

#### 3. Witness-Test Scope Package for Unlisted Arrays (Darnwick & Holcott)
* **Governing Basis:** IEEE 1547.1-2020, IEEE 1547-2018 (Category II), DIS-01 Rev 4 §5 (Table 5-1 Category 2), and ENG-PRC-014 Rev 3 §4.2.
* **Mandated Test Suite:**
  1. *Protective-Function Trip Testing:* ANSI 27-1/27-2 undervoltage, ANSI 59-1/59-2 overvoltage, ANSI 81U-1/81U-2 underfrequency, ANSI 81O-1/81O-2 overfrequency, and restoration delay timer (minimum 300 s reconnect timing).
  2. *Anti-Islanding Functional Verification:* Loss-of-grid opening under real power generation; disconnection required within ≤ 2.0 s.
  3. *Ride-Through & Autonomous Profile Verification:* Category II voltage/frequency ride-through envelope and autonomous Volt-VAR response.
  4. *Safety & Operability Verifications:* Lockable visible-break AC disconnect operation, phase rotation, ground resistance (≤ 5.0 Ω), and insulation resistance (> 1 MΩ at 1000 VDC).
* **Execution & Witnessing Responsibilities:**
  * *Test Performer:* Customer/EPC Commissioning Agent (provides test plan, calibrated secondary injection test sets, load banks, and qualified personnel).
  * *Test Witness:* Alleniom Utilities Commissioning / Standards Engineering Witness Engineer (P.E. or designated field engineer).
* **Prerequisites Required on File Prior to Scheduling:**
  1. Approved site-specific Test Plan.
  2. P.E.-stamped as-built Single-Line and Three-Line Drawings.
  3. Approved Protection Settings Sheet issued by Distribution Protection Engineering.
  4. Municipal AHJ electrical permit inspection sign-off.
  5. Current calibration certificates (within 12 months) for all test equipment.
  6. Manufacturer factory test reports and UL 1741 baseline data.
  7. Fully executed Interconnection Service Agreement (ISA).
  8. Completed Alleniom Commissioning Checklist Sections 1–4 signed by field engineering.

---

#### 4. System Operations Center (SOC) Release Roster as of 07/14/2025
Under **TCS-02 §5** and the standing **SOC PTO-Hold Log**, PTO is strictly prohibited without live, valid SCADA telemetry from a utility-owned RTU. Release readiness breaks down as follows:
* **Recommended for Immediate SOC Release (2 Sites):**
  * **Lockmere Middle School Array (720 kW):** Inverter carried on CEL-2025-Q2; checklist Sections 1–5 complete; RTU asset `RTU-LKM-171-04` installed 06/12/2025; cellular comms verified; end-to-end SCADA verified with SOC 06/17/2025 (ticket TKT-25-04188); live telemetry streaming continuously since 06/17/2025 15:20. Ready for SOC release to PTO immediately upon Standards Engineering countersigning the waiver disposition.
  * **Marden Falls WRF Array (980 kW):** Inverter carried on CEL-2025-Q2; checklist Sections 1–4 complete; utility RTU installed and provisioned; SCADA points verified end-to-end with SOC per TCS-02 §5. Ready for SOC release to PTO immediately upon Standards Engineering countersigning the waiver disposition.
* **Prohibited from SOC Release (3 Sites):**
  * **Cravenwood High School Array (860 kW):** Inverter is carried on CEL-2025-Q2 (waiver eligible), but utility RTU remains pending in the equipment delivery queue (TCS-02 §5 violation; PTO withheld).
  * **Darnwick Elementary School Array (640 kW):** Unlisted inverter (on-site witness test required) AND utility RTU pending allocation.
  * **Holcott Public Library Array (510 kW):** Unlisted inverter (on-site witness test required) AND utility RTU pending allocation.

---

#### 5. Case Tracking Execution & Reconciliation (OpenProject Project 3)
* **Scheduling Items Logged:**
  * **Work Package #47:** *Witness Test Scheduling: Darnwick Elementary School Array (640 kW)* — Logged and linked to Case #45.
  * **Work Package #48:** *Witness Test Scheduling: Holcott Public Library Array (510 kW)* — Logged and linked to Case #45.
* **Batch Determination Entry & Case Closure:**
  * The full batch determination was recorded directly on **Case #45** (*Process the municipal witness-test waiver batch*) via a formal activity record.
  * The description of Case #45 was updated to reflect all determinations.
  * Case #45 was marked **Closed** (status ID 12, 100% complete) as the arrays named in the package and the scheduling items standing on it are in exact agreement.