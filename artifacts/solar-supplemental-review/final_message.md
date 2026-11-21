### Summary of Supplemental Review Memo of Record Delivered

**Deliverable File:** `Bramwick_Commons_Screen_Memo.docx`  
**Location:** `/filesystem/Bramwick_Commons_Screen_Memo.docx` (and mirrored to `/filesystem/Studies/Bramwick_Commons_Screen_Memo.docx`)  
**Document Identifier:** `IS-BRAM-2025-07-14` (Revision v2, Memo of Record)  
**Governing Procedures:** SRP-3 Rev 3 (§3, §4, §6), DIS-01 Rev 4, DPS-07 Rev 2, TCS-02 Rev 1, and Regulatory Affairs Tasking Directive DIR-2025-0627 (§3.9)  
**Effective Date:** July 14, 2025  

---

### Key Findings & Technical Determinations

#### 1. Audit & Vacating of Countersigned Screening Memo v1
The prior memorandum (`IS-BRAM-2025-06-25`, Rev v1, dated 06/25/2025, countersigned by Manager Meera Vellanki) erroneously determined that the application failed supplemental review based on a reported feeder minimum load of 1.1 MW. Cross-referencing against the authoritative 15-minute standing export (`ALN-214_AMI_Interval_Load_Export.xlsx`) revealed that this 1,100 kW value occurred on **March 23, 2025 at 03:45 AM** (an overnight interval). 

This directly violated **SRP-3 Rev 3 §4**, which expressly prohibits using absolute overnight minimum loads for solar DER and mandates evaluating minimum load strictly within the **10:00–16:00 daytime window** across 12 complete calendar months of 15-minute AMI data. Pursuant to SRP-3 §4, SRP-3 §6(f), and Directive DIR-2025-0627 §3.9, Memo v1 has been formally superseded and vacated on the record.

#### 2. Recomputation of Feeder Minimum Load (Screen D per SRP-3 §4)
* **Authoritative Data Window:** 07/01/2024 00:00 to 06/30/2025 23:45 (12 complete calendar months; 35,040 intervals; zero exclusions for outages or switching).
* **Daytime Evaluation Window:** 10:00–16:00 local clock time (8,760 intervals for 10:00 $\le t <$ 16:00; 9,125 intervals for 10:00 $\le t \le$ 16:00).
* **Daytime-Window Minimum Feeder Load:** **2,400 kW (2.40 MW)**, recorded on **February 12, 2025 at 11:30 AM**.
* **Comparison:** Requested capacity of **1.80 MW (1,800 kW)** $\le$ Daytime minimum load of **2.40 MW (2,400 kW)** (facility represents 75.0% of daytime minimum load; 600 kW headroom).
* **Screen D Determination:** **PASSED** (Formal reversal of prior determination).

#### 3. Ordered Technical Screen Determinations (SRP-3 Rev 3 §3)
* **Screen A — Aggregate DER Penetration:**
  * *Basis:* 0.0 kW existing DER (`Screening/Existing_DER_Register_Extract.xlsx`), 0.0 kW active queue (`Queue/2025-07-14_Active_Queue_Report.xlsx`), 0.0 kW on-hold queue (`Queue/2025-07-14_On_Hold_Queue_Report.xlsx`). Total aggregate DER = 1.80 MW vs. 4.90 MW published available hosting capacity (`Planning/Hosting_Capacity_Map_Export_2024-05-15.xlsx`, Larkspur Ridge Substation, 12.47 kV, pure-generation category). Feeder annual peak load = 8.526 MW (observed 08/01/2024 13:30). Total penetration is 36.7% of feeder hosting capacity and 21.1% of peak load.
  * *Call:* **PASSED**.
* **Screen B — Voltage Regulation & Flicker:**
  * *Basis:* Feeder ALN-214 planning study on file dated 12/2023 (within the 24-month recency window per SRP-3 §3 Screen B). Dedicated 12.47 kV three-phase trunk with 4.9 MW studied capacity confirms steady-state voltage rise (1.42% modeled vs. $\le 2.5\%$ limit) and solar ramp flicker (0.88% calculated vs. $\le 1.5\%$ limit) comply with IEEE 1547 and DIS-01.
  * *Call:* **PASSED**.
* **Screen C — Short-Circuit Contribution & Coordination:**
  * *Basis:* 1.8 MW inverter-based generation electronically limits fault current to 1.1–1.2 pu (~100 A), decaying within 1–2 cycles. Feeder equipment interrupting ratings (12.5–20 kA) retain $>20\%$ margin below the 87.5% duty threshold (max duty $<62.4\%$), and protection coordination margin per DPS-07 Rev 2 is fully preserved.
  * *Call:* **PASSED**.
* **Screen D — 100%-of-Minimum-Load Screen for Solar:**
  * *Basis:* Recomputed under SRP-3 §4. Requested capacity (1.80 MW) $\le$ Daytime minimum load (2.40 MW).
  * *Call:* **PASSED** (Reversal).
* **Screen E — Reverse Power Flow at Substation:**
  * *Basis:* Larkspur Ridge Substation transformer bay is certified for up to 4.9 MW reverse-power backfeed on ALN-214 with directional-power protective elements (ANSI 32) and reverse-reactance LTC compensation in place. Aggregate DER of 1.8 MW is well within certified limits.
  * *Call:* **PASSED**.

---

### Final Disposition & Next Steps

1. **Official Disposition:** **ADVANCE WITHOUT STUDY AGREEMENT** (SRP-3 Rev 3 §6(d)). The requirement for a System Impact Study (SIS) and Study Agreement is rescinded.
2. **Queue Record Updates:** Remove the failed-screen flag from Feeder ALN-214 in the Interconnection Studies queue and release the hold on the Bramwick Commons Solar PXA record.
3. **Document Management:** File `IS-BRAM-2025-07-14` (Rev v2) as the permanent Memo of Record, flag prior Document `IS-BRAM-2025-06-25` (Rev v1) as **SUPERSEDED**, and attach a cross-reference cover page citing v2.
4. **Applicant Notification & Agreement Drafting:** Notify Bramwick Commons Solar LLC that supplemental review has been successfully completed and route the file directly to the Contracts Desk for drafting of an executable Interconnection Service Agreement (ISA) at 1.8 MW AC capacity.
5. **Downstream Equipment Scoping (DIS-01 Table 5-1 Category 3 & TCS-02):**
   * Customer-owned lockable visible-break AC disconnect operable 24/7 by utility personnel.
   * Dedicated interconnection protection relay scheme per IEEE 1547-2018 / DPS-07 §4.3.
   * Utility-owned Point-of-Interconnection (POI) Recloser with ANSI 50/51, 50N/51N, 27/59, 81U/81O, 25, 79, and 32 directional elements (DPS-07 §4.2).
   * Primary bidirectional revenue metering (12.47 kV class).
   * Utility-owned RTU (YOT-8963 / YOT-8856 / YOT-7963) communicating via DNP3 to Alleniom SOC; live telemetry is an absolute prerequisite for Permission to Operate (TCS-02 §5).