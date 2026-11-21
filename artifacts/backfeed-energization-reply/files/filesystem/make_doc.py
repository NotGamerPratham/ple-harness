import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL
from docx.oxml import OxmlElement, parse_xml
from docx.oxml.ns import qn, nsdecls

def create_document():
    doc = docx.Document()

    # Page setup - 1 inch margins all around
    for section in doc.sections:
        section.top_margin = Inches(1.0)
        section.bottom_margin = Inches(1.0)
        section.left_margin = Inches(1.0)
        section.right_margin = Inches(1.0)

    # Palette
    HEX_PRIMARY = "1A365D"      # Navy
    HEX_SECONDARY = "2B6CB0"    # Steel Blue
    HEX_DARK = "2D3748"         # Charcoal Text
    HEX_LIGHT_BG = "F7FAFC"     # Off-white / light slate
    HEX_BORDER = "CBD5E0"       # Subtle border gray
    HEX_WARN_BG = "FFF5F5"      # Light red tint
    HEX_WARN_BORDER = "E53E3E"  # Red border
    HEX_INFO_BG = "EBF8FF"      # Light blue tint
    HEX_INFO_BORDER = "3182CE"  # Blue border

    COLOR_PRIMARY = RGBColor(26, 54, 93)
    COLOR_SECONDARY = RGBColor(43, 108, 176)
    COLOR_DARK = RGBColor(45, 55, 72)
    COLOR_MUTED = RGBColor(113, 128, 150)
    COLOR_WARN = RGBColor(197, 48, 48)

    # Base typography
    normal_style = doc.styles['Normal']
    normal_style.font.name = 'Calibri'
    normal_style.font.size = Pt(10)
    normal_style.font.color.rgb = COLOR_DARK
    normal_style.paragraph_format.line_spacing = 1.15
    normal_style.paragraph_format.space_after = Pt(4)

    def set_cell_props(cell, fill_hex=None, borders=None, margins=None):
        tcPr = cell._tc.get_or_add_tcPr()
        if fill_hex:
            shd = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{fill_hex}"/>')
            tcPr.append(shd)
        if borders:
            tcBorders = parse_xml(f'<w:tcBorders {nsdecls("w")}>{borders}</w:tcBorders>')
            tcPr.append(tcBorders)
        if margins:
            top, bottom, left, right = margins
            tcMar = OxmlElement('w:tcMar')
            for m, val in [('top', top), ('bottom', bottom), ('left', left), ('right', right)]:
                node = OxmlElement(f'w:{m}')
                node.set(qn('w:w'), str(val))
                node.set(qn('w:type'), 'dxa')
                tcMar.append(node)
            tcPr.append(tcMar)

    # 1. Header / Letterhead
    p_head = doc.add_paragraph()
    p_head.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_head.paragraph_format.space_after = Pt(1)
    r_head = p_head.add_run("ALLENIOM UTILITIES")
    r_head.bold = True
    r_head.font.size = Pt(15)
    r_head.font.color.rgb = COLOR_PRIMARY

    p_subhead = doc.add_paragraph()
    p_subhead.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_subhead.paragraph_format.space_after = Pt(2)
    r_sub = p_subhead.add_run("DISTRIBUTION OPERATIONS  ·  DER PROGRAM OFFICE  ·  COMMISSIONING")
    r_sub.bold = True
    r_sub.font.size = Pt(9.5)
    r_sub.font.color.rgb = COLOR_SECONDARY

    p_addr = doc.add_paragraph()
    p_addr.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_addr.paragraph_format.space_after = Pt(10)
    r_addr = p_addr.add_run("4200 Veldmere Boulevard, Halston, Alleron 01HA  |  Telephone: (612) 555-0100  |  alleniom.com")
    r_addr.font.size = Pt(8.5)
    r_addr.font.color.rgb = COLOR_MUTED

    # Dividing rule
    p_div = doc.add_paragraph()
    p_div.paragraph_format.space_after = Pt(12)
    pBdr = parse_xml(f'<w:pBdr {nsdecls("w")}><w:bottom w:val="single" w:sz="12" w:space="1" w:color="{HEX_PRIMARY}"/></w:pBdr>')
    p_div._p.get_or_add_pPr().append(pBdr)

    # 2. Date & Address / Metadata Table
    t_meta = doc.add_table(rows=1, cols=2)
    t_meta.alignment = WD_TABLE_ALIGNMENT.CENTER
    t_meta.autofit = False
    t_meta.columns[0].width = Inches(4.0)
    t_meta.columns[1].width = Inches(2.5)

    c_recip = t_meta.cell(0, 0)
    c_meta = t_meta.cell(0, 1)

    p_dt = c_recip.paragraphs[0]
    p_dt.paragraph_format.space_after = Pt(4)
    r_dt = p_dt.add_run("July 14, 2025")
    r_dt.bold = True
    r_dt.font.size = Pt(10.5)

    p_rc = c_recip.add_paragraph()
    p_rc.paragraph_format.space_after = Pt(0)
    r_rc = p_rc.add_run(
        "Imogen Strathe, Project Manager\n"
        "Halbray Community Solar LP\n"
        "6120 Halbray Road\n"
        "Kelloway Township, Alleron 07KT\n"
        "Project Office: (612) 555-0784\n"
        "Email: project.office@halbraycommunitysolar.com"
    )
    r_rc.font.size = Pt(9.5)

    p_mf = c_meta.paragraphs[0]
    p_mf.paragraph_format.space_after = Pt(0)
    r_mf = p_mf.add_run(
        "INTERCONNECTION FILE RECORD\n"
        "Project: Halbray Field Solar Site 3\n"
        "Application ID: PXA-2024-0002\n"
        "Capacity: 2.3 MW ac (2,300 kW export)\n"
        "Service Agreement: ISA-Halbray-Field-Site-3\n"
        "Point of Interconnection: Feeder ALN-159 (13.2 kV)\n"
        "AHJ Electrical Permit: EP-25-0418\n"
        "Commissioning Checklist: CX-HB-03 Rev 0\n"
        "Review Date / Baseline: July 14, 2025"
    )
    r_mf.font.size = Pt(8.5)
    r_mf.font.color.rgb = COLOR_MUTED

    # Spacing
    p_sp1 = doc.add_paragraph()
    p_sp1.paragraph_format.space_after = Pt(4)

    # 3. Subject Box
    t_subj = doc.add_table(rows=1, cols=1)
    t_subj.alignment = WD_TABLE_ALIGNMENT.CENTER
    t_subj.autofit = False
    t_subj.columns[0].width = Inches(6.5)
    c_subj = t_subj.cell(0, 0)
    set_cell_props(
        c_subj,
        fill_hex=HEX_LIGHT_BG,
        borders=f'<w:left w:val="single" w:sz="24" w:color="{HEX_PRIMARY}"/><w:top w:val="single" w:sz="4" w:color="{HEX_BORDER}"/><w:right w:val="single" w:sz="4" w:color="{HEX_BORDER}"/><w:bottom w:val="single" w:sz="4" w:color="{HEX_BORDER}"/>',
        margins=(120, 120, 180, 180)
    )
    p_sb = c_subj.paragraphs[0]
    p_sb.paragraph_format.space_after = Pt(0)
    r_sb_lbl = p_sb.add_run("SUBJECT: ")
    r_sb_lbl.bold = True
    r_sb_lbl.font.size = Pt(10)
    r_sb_lbl.font.color.rgb = COLOR_PRIMARY
    r_sb_txt = p_sb.add_run(
        "ENGINEERING AND COMMISSIONING DETERMINATION ON REQUEST FOR PRE-PTO BACKFEED\n"
        "Project: Halbray Field Solar Site 3 (PXA-2024-0002) · Feeder ALN-159 · Requested Date: 07/29/2025"
    )
    r_sb_txt.bold = True
    r_sb_txt.font.size = Pt(10)
    r_sb_txt.font.color.rgb = COLOR_PRIMARY

    # Spacing
    p_sp2 = doc.add_paragraph()
    p_sp2.paragraph_format.space_after = Pt(6)

    # 4. Salutation
    p_sal = doc.add_paragraph()
    p_sal.paragraph_format.space_after = Pt(6)
    r_sal = p_sal.add_run("Dear Ms. Strathe:")
    r_sal.bold = True

    # 5. Section 1: Plain Determination & Direct Answer
    p_s1_h = doc.add_paragraph()
    p_s1_h.paragraph_format.space_before = Pt(8)
    p_s1_h.paragraph_format.space_after = Pt(3)
    r_s1_h = p_s1_h.add_run("1. Determination on the July 29, 2025 Energization Request")
    r_s1_h.bold = True
    r_s1_h.font.size = Pt(11)
    r_s1_h.font.color.rgb = COLOR_PRIMARY

    p_s1_1 = doc.add_paragraph()
    p_s1_1.add_run(
        "Alleniom Utilities DER Program Office and Commissioning Engineering have reviewed your letter of "
        "July 9, 2025, requesting that Alleniom energize the step-up transformer (T-1) and the 800 V ac collection system "
        "at Halbray Field Solar Site 3 (PXA-2024-0002) from feeder ALN-159 on July 29, 2025, under the pre-PTO backfeed "
        "provisions of our executed Interconnection Service Agreement (ISA-Halbray-Field-Site-3). You requested that "
        "Alleniom confirm this energization date or identify specifically what stands in the way."
    )

    # Callout Box: Direct Answer
    t_call = doc.add_table(rows=1, cols=1)
    t_call.alignment = WD_TABLE_ALIGNMENT.CENTER
    t_call.autofit = False
    t_call.columns[0].width = Inches(6.5)
    c_call = t_call.cell(0, 0)
    set_cell_props(
        c_call,
        fill_hex=HEX_WARN_BG,
        borders=f'<w:left w:val="single" w:sz="24" w:color="{HEX_WARN_BORDER}"/><w:top w:val="single" w:sz="4" w:color="{HEX_BORDER}"/><w:right w:val="single" w:sz="4" w:color="{HEX_BORDER}"/><w:bottom w:val="single" w:sz="4" w:color="{HEX_BORDER}"/>',
        margins=(120, 120, 180, 180)
    )
    p_cb = c_call.paragraphs[0]
    p_cb.paragraph_format.space_after = Pt(0)
    r_cb_b = p_cb.add_run("DETERMINATION SUMMARY:\n")
    r_cb_b.bold = True
    r_cb_b.font.size = Pt(10)
    r_cb_b.font.color.rgb = COLOR_WARN
    r_cb_t = p_cb.add_run(
        "Working from the official project and engineering records as they stand on July 14, 2025, Alleniom Utilities "
        "cannot confirm or commit to energizing Halbray Field Solar Site 3 on July 29, 2025 at this time. "
        "A mandatory statutory and regulatory prerequisite remains outstanding on the record: the facility has not yet "
        "received final electrical inspection approval from the Authority Having Jurisdiction (AHJ), Kelloway Township.\n\n"
        "However, energization on July 29, 2025 remains technically feasible and will be supported by Alleniom if and only if "
        "Kelloway Township conducts its scheduled final electrical inspection on July 24, 2025, issues written final electrical "
        "approval without open defects, and an official copy of that written approval is delivered to the DER Program Office "
        "in advance of July 29, 2025, alongside adherence to the pre-PTO backfeed isolation protocols detailed below."
    )
    r_cb_t.font.size = Pt(9.5)

    # 6. Section 2: What Stands in the Way and What It Rests On
    p_s2_h = doc.add_paragraph()
    p_s2_h.paragraph_format.space_before = Pt(10)
    p_s2_h.paragraph_format.space_after = Pt(3)
    r_s2_h = p_s2_h.add_run("2. Governing Basis: What Stands in the Way on the Record")
    r_s2_h.bold = True
    r_s2_h.font.size = Pt(11)
    r_s2_h.font.color.rgb = COLOR_PRIMARY

    p_s2_1 = doc.add_paragraph()
    p_s2_1.add_run(
        "From the perspective of a licensed professional electrical engineer and utility operator, energizing any portion "
        "of a customer's high-voltage or medium-voltage facility from a utility distribution feeder—even for auxiliary power "
        "or non-parallel pre-start checks—constitutes an active energization of the permitted installation. "
        "The obstacle standing in the way of backfeed authorization rests upon three binding legal, technical, and procedural authorities:"
    )

    # Bullet points for legal/technical basis
    p_b1 = doc.add_paragraph(style='List Bullet')
    p_b1.paragraph_format.space_after = Pt(3)
    r_b1_b = p_b1.add_run("Kelloway Township Electrical Permit EP-25-0418 Express Condition: ")
    r_b1_b.bold = True
    p_b1.add_run(
        "Electrical Permit EP-25-0418, issued on May 12, 2025 by Electrical Inspector Graham Telford of the Kelloway Township "
        "Building Department to your contractor, Tamsworth Electrical Constructors Inc. (Alleron Lic. #EC-11847), contains "
        "an express statutory directive on the face of the permit: "
    )
    r_b1_q = p_b1.add_run("“No permitted work shall be energized before final approval.”")
    r_b1_q.bold = True

    p_b2 = doc.add_paragraph(style='List Bullet')
    p_b2.paragraph_format.space_after = Pt(3)
    r_b2_b = p_b2.add_run("Statutory Scope of Permitted Work and National Electrical Code (NEC 2023): ")
    r_b2_b.bold = True
    p_b2.add_run(
        "Under Kelloway Township Ordinance 2024-03, the adopted electrical code is NFPA 70, National Electrical Code (NEC), "
        "2023 edition. The scope of work permitted under EP-25-0418 explicitly covers the entire facility: "
    )
    r_b2_q = p_b2.add_run(
        "“2.3 MW ac ground-mounted photovoltaic system: four inverter skids, the ac collection system, "
        "a 2,500 kVA pad-mounted step-up transformer and its 13.2 kV interconnection.” "
    )
    r_b2_q.italic = True
    p_b2.add_run(
        "Energizing transformer T-1 and the 800 V collection system (switchboard CSB-1 and feeders C-1 through C-4) "
        "from feeder ALN-159 energizes the core apparatus authorized under this permit. As a regulated utility, Alleniom Utilities "
        "is legally and ethically prohibited from energizing any permitted electrical installation prior to the AHJ's written final sign-off."
    )

    p_b3 = doc.add_paragraph(style='List Bullet')
    p_b3.paragraph_format.space_after = Pt(3)
    r_b3_b = p_b3.add_run("Alleniom DER Commissioning Checklist (CX-HB-03 Rev 0): ")
    r_b3_b.bold = True
    p_b3.add_run(
        "In accordance with Alleniom Utilities commissioning standards, the DER Commissioning Checklist for the site "
        "(Doc no. CX-HB-03, baseline dated July 14, 2025) explicitly establishes AHJ final inspection as an open prerequisite. "
        "Checklist item 9 tracks Permit EP-25-0418 as “Booked for 07/24/2025.” Until formal written approval is logged against CX-HB-03, "
        "the commissioning coordinator cannot sign off on feeder energization, and Distribution Operations cannot execute the switching order."
    )

    # 7. Section 3: Actions Required Before July 29, 2025 and By Whom
    p_s3_h = doc.add_paragraph()
    p_s3_h.paragraph_format.space_before = Pt(10)
    p_s3_h.paragraph_format.space_after = Pt(3)
    r_s3_h = p_s3_h.add_run("3. Required Actions Before July 29, 2025: Who Must Do What")
    r_s3_h.bold = True
    r_s3_h.font.size = Pt(11)
    r_s3_h.font.color.rgb = COLOR_PRIMARY

    p_s3_1 = doc.add_paragraph()
    p_s3_1.add_run(
        "To enable energization of the step-up transformer and collection system on the requested July 29, 2025 date, "
        "the following specific actions must be completed by the responsible parties:"
    )

    # Action Items Table
    t_act = doc.add_table(rows=5, cols=4)
    t_act.alignment = WD_TABLE_ALIGNMENT.CENTER
    t_act.autofit = False
    t_act.columns[0].width = Inches(1.1)
    t_act.columns[1].width = Inches(2.6)
    t_act.columns[2].width = Inches(1.4)
    t_act.columns[3].width = Inches(1.4)

    headers = ["Item", "Action Required", "Responsible Party", "Target Deadline"]
    for col_idx, text in enumerate(headers):
        cell = t_act.cell(0, col_idx)
        set_cell_props(cell, fill_hex=HEX_PRIMARY, margins=(80, 80, 100, 100))
        p = cell.paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.LEFT
        r = p.add_run(text)
        r.bold = True
        r.font.size = Pt(9)
        r.font.color.rgb = RGBColor(255, 255, 255)

    actions = [
        ("1. Complete AHJ Inspection",
         "Successfully host and pass the final electrical inspection booked with the Kelloway Township Building Department for Permit EP-25-0418. Ensure no outstanding code violations, safety deviations, or punch-list items.",
         "Tamsworth Electrical Constructors Inc. / Halbray Community Solar LP",
         "July 24, 2025"),

        ("2. Secure Written AHJ Approval",
         "Obtain written evidence of final electrical approval (e.g., Certificate of Final Electrical Approval or inspector's signed-off permit card) from Electrical Inspector Graham Telford.",
         "Tamsworth Electrical Constructors Inc. / Kelloway Township",
         "July 24–25, 2025"),

        ("3. Transmit Approval to Alleniom",
         "Submit the official written AHJ final approval document via email to der.program@alleniom.com (attn: S. Rennick, Commissioning) to clear Checklist CX-HB-03 item 9.",
         "Halbray Community Solar LP / Imogen Strathe",
         "Prior to July 28, 2025 (by 12:00 PM)"),

        ("4. Confirm Safety Lockout & On-Site Presence",
         "Verify all twelve (12) inverters are disabled and locked open at disconnects AD-1 to AD-4 and ACP-1 to ACP-4; provide qualified contractor personnel on site to coordinate switching with Distribution Operations.",
         "Tamsworth Electrical Constructors Inc. (R. Vance, E.E.)",
         "July 29, 2025 (08:00 AM)")
    ]

    for row_idx, data in enumerate(actions, start=1):
        for col_idx, text in enumerate(data):
            cell = t_act.cell(row_idx, col_idx)
            bg = HEX_LIGHT_BG if row_idx % 2 == 1 else "FFFFFF"
            set_cell_props(
                cell,
                fill_hex=bg,
                borders=f'<w:top w:val="single" w:sz="4" w:color="{HEX_BORDER}"/><w:bottom w:val="single" w:sz="4" w:color="{HEX_BORDER}"/>',
                margins=(60, 60, 80, 80)
            )
            p = cell.paragraphs[0]
            r = p.add_run(text)
            r.font.size = Pt(8.5)
            if col_idx == 0:
                r.bold = True

    # 8. Section 4: Operational and Safety Protocols Governing Pre-PTO Backfeed
    p_s4_h = doc.add_paragraph()
    p_s4_h.paragraph_format.space_before = Pt(10)
    p_s4_h.paragraph_format.space_after = Pt(3)
    r_s4_h = p_s4_h.add_run("4. Operational and Safety Protocols Governing the Pre-PTO Backfeed")
    r_s4_h.bold = True
    r_s4_h.font.size = Pt(11)
    r_s4_h.font.color.rgb = COLOR_PRIMARY

    p_s4_1 = doc.add_paragraph()
    p_s4_1.add_run(
        "Under the terms of Section “Pre-PTO backfeed” of your executed Interconnection Service Agreement (ISA-Halbray-Field-Site-3), "
        "utility backfeed energization is subject to strict operational restrictions that must be maintained throughout the evolution:"
    )

    p_s4_b1 = doc.add_paragraph(style='List Bullet')
    p_s4_b1.paragraph_format.space_after = Pt(3)
    r_s4_b1_b = p_s4_b1.add_run("Strict Prohibition on Parallel Generation: ")
    r_s4_b1_b.bold = True
    p_s4_b1.add_run(
        "Energization from feeder ALN-159 is provided strictly as one-way auxiliary and commissioning power for the site step-up "
        "transformer (T-1), switchboard CSB-1, tracker auxiliary panelboard AUX-1, and the 800 V collection circuits (C-1 to C-4). "
        "The generating facility must remain disabled and shall NOT operate in parallel with Alleniom's distribution system under any circumstances. "
        "Parallel operation is permitted only after Alleniom issues formal, written Permission to Operate (PTO)."
    )

    p_s4_b2 = doc.add_paragraph(style='List Bullet')
    p_s4_b2.paragraph_format.space_after = Pt(3)
    r_s4_b2_b = p_s4_b2.add_run("Physical Inverter Lockout/Tagout (LOTO): ")
    r_s4_b2_b.bold = True
    p_s4_b2.add_run(
        "All twelve (12) Nordreem string inverters—comprising eight (8) model NG-XT-225 (225 kW) and four (4) model NG-XT-125 (125 kW) "
        "across skids SK-1 through SK-4—must have their ac output circuits open and tagged out during initial utility energization. "
        "The 600 A, 1000 V ac fused disconnect switches AD-1 through AD-4 must be locked open. Individual inverter testing on utility power "
        "shall be executed sequentially under Tamsworth's internal test plan only after secondary bus voltage, phase rotation, "
        "and voltage balance have been verified at CSB-1 and ACP-1 through ACP-4."
    )

    p_s4_b3 = doc.add_paragraph(style='List Bullet')
    p_s4_b3.paragraph_format.space_after = Pt(3)
    r_s4_b3_b = p_s4_b3.add_run("Utility Switching Execution: ")
    r_s4_b3_b.bold = True
    p_s4_b3.add_run(
        "In accordance with utility operating procedures and ISA terms, backfeed switching is performed exclusively by Alleniom Utilities "
        "Distribution Operations under its own formal switching order. Tamsworth's designated qualified person (R. Vance, E.E., or designated site lead) "
        "must be on site to coordinate directly with the Alleniom switching supervisor, verify that site main switch PSW-1 and collection main "
        "CSB-1 are in their prescribed initial switching positions, and take formal delivery of utility voltage."
    )

    # 9. Section 5: Affirmation of Companion Technical Reviews
    p_s5_h = doc.add_paragraph()
    p_s5_h.paragraph_format.space_before = Pt(10)
    p_s5_h.paragraph_format.space_after = Pt(3)
    r_s5_h = p_s5_h.add_run("5. Status of Utility Facilities and Companion Technical Reviews")
    r_s5_h.bold = True
    r_s5_h.font.size = Pt(11)
    r_s5_h.font.color.rgb = COLOR_PRIMARY

    p_s5_1 = doc.add_paragraph()
    p_s5_1.add_run(
        "To provide you with complete visibility into the interconnection posture of Halbray Field Solar Site 3, we are pleased to confirm "
        "that all utility-side engineering packages, equipment installations, and internal technical reviews are in order and accepted, as summarized below:"
    )

    # Review status table
    t_rev = doc.add_table(rows=8, cols=4)
    t_rev.alignment = WD_TABLE_ALIGNMENT.CENTER
    t_rev.autofit = False
    t_rev.columns[0].width = Inches(1.5)
    t_rev.columns[1].width = Inches(1.3)
    t_rev.columns[2].width = Inches(1.4)
    t_rev.columns[3].width = Inches(2.3)

    rev_headers = ["Item / Review Domain", "Governing Standard", "Current Status", "Engineering Disposition / Notes"]
    for col_idx, text in enumerate(rev_headers):
        cell = t_rev.cell(0, col_idx)
        set_cell_props(cell, fill_hex=HEX_SECONDARY, margins=(80, 80, 100, 100))
        p = cell.paragraphs[0]
        r = p.add_run(text)
        r.bold = True
        r.font.size = Pt(8.5)
        r.font.color.rgb = RGBColor(255, 255, 255)

    rev_data = [
        ("Utility RTU & Telemetry", "TCS-02 §3.6", "ACCEPTED (07/02/2025)",
         "Procured, installed, and successfully point-to-point tested end-to-end. Formally accepted by SCADA/EMS Engineering (Marcus Deele)."),

        ("Utility POI Recloser", "DPS-07 §6.2", "ACCEPTED (07/07/2025)",
         "Site acceptance testing (Items 1 to 7) complete and accepted in writing by Distribution Protection Engineering (N. Achterberg, P.E.)."),

        ("Protection Coordination Study & Settings", "DPS-07 §5.1", "ISSUED (06/16/2025)",
         "Settings sheet and feeder coordination study issued by Distribution Protection Engineering (N. Achterberg, P.E.); archived in engineering records."),

        ("Primary Revenue Meter (RM-0002)", "ISA Terms", "SET (07/08/2025)",
         "Primary 13.2 kV revenue meter RM-0002 set and tested at the POI by Alleniom Metering Department."),

        ("Inverter Equipment Certification", "ENG-PRC-014 §4.1 / CEL-2025-Q2", "VERIFIED (07/14/2025)",
         "8 x NG-XT-225 and 4 x NG-XT-125 inverters verified actively listed on the current Certified Equipment List (CEL-2025-Q2, UL 1741-SB)."),

        ("Interconnection Queue Position", "APUC Tariff §12 / Active Queue", "ACTIVE & SECURE",
         "Project PXA-2024-0002 holds active queue position under weekly reports managed by Meera Vellanki. Executed ISA on file (11/18/2024)."),

        ("System Impact Study (SIS)", "APUC Tariff §12 / Studies Desk", "COMPLETE / ON FILE",
         "All SIS conditions tracked and maintained outside these commissioning records by Interconnection Studies.")
    ]

    for row_idx, data in enumerate(rev_data, start=1):
        for col_idx, text in enumerate(data):
            cell = t_rev.cell(row_idx, col_idx)
            bg = HEX_LIGHT_BG if row_idx % 2 == 1 else "FFFFFF"
            set_cell_props(
                cell,
                fill_hex=bg,
                borders=f'<w:top w:val="single" w:sz="4" w:color="{HEX_BORDER}"/><w:bottom w:val="single" w:sz="4" w:color="{HEX_BORDER}"/>',
                margins=(50, 50, 70, 70)
            )
            p = cell.paragraphs[0]
            r = p.add_run(text)
            r.font.size = Pt(8)
            if col_idx == 0:
                r.bold = True
            elif col_idx == 2:
                r.bold = True
                if "ACCEPTED" in text or "ISSUED" in text or "SET" in text or "VERIFIED" in text or "ACTIVE" in text:
                    r.font.color.rgb = COLOR_PRIMARY

    # 10. Section 6: Subsequent Roadmap to Permission to Operate (PTO)
    p_s6_h = doc.add_paragraph()
    p_s6_h.paragraph_format.space_before = Pt(10)
    p_s6_h.paragraph_format.space_after = Pt(3)
    r_s6_h = p_s6_h.add_run("6. Subsequent Path Toward Permission to Operate (PTO)")
    r_s6_h.bold = True
    r_s6_h.font.size = Pt(11)
    r_s6_h.font.color.rgb = COLOR_PRIMARY

    p_s6_1 = doc.add_paragraph()
    p_s6_1.add_run(
        "Please note that completion of the pre-PTO backfeed and contractor pre-start checks does not constitute permission to operate "
        "the generating facility in parallel with the Alleniom distribution system. Once your pre-start testing is concluded, the remaining "
        "steps to obtain commercial PTO are as follows:"
    )

    p_s6_b1 = doc.add_paragraph(style='List Bullet')
    p_s6_b1.paragraph_format.space_after = Pt(3)
    r_s6_b1_b = p_s6_b1.add_run("Formal Written PTO Request: ")
    r_s6_b1_b.bold = True
    p_s6_b1.add_run(
        "Halbray Community Solar LP must submit a formal written request for Permission to Operate to the DER Program Office upon "
        "satisfactory completion of all inverter and tracker pre-start checks."
    )

    p_s6_b2 = doc.add_paragraph(style='List Bullet')
    p_s6_b2.paragraph_format.space_after = Pt(3)
    r_s6_b2_b = p_s6_b2.add_run("Witness Test Determination (ENG-PRC-014 §4.1): ")
    r_s6_b2_b.bold = True
    p_s6_b2.add_run(
        "Upon receipt of the PTO request, Standards Engineering and Commissioning will evaluate the facility under procedure ENG-PRC-014. "
        "While the Nordreem inverter models are certified under CEL-2025-Q2, the Commissioning Coordinator will make a formal determination "
        "as to whether a formal utility on-site witness test is required or whether a witness-test waiver may be granted based on site protective devices."
    )

    p_s6_b3 = doc.add_paragraph(style='List Bullet')
    p_s6_b3.paragraph_format.space_after = Pt(3)
    r_s6_b3_b = p_s6_b3.add_run("Live Telemetry Confirmation (TCS-02 §5): ")
    r_s6_b3_b.bold = True
    p_s6_b3.add_run(
        "In accordance with TCS-02 §5, no facility ≥500 kW may receive PTO without live, valid SCADA telemetry actively streaming to the "
        "System Operations Center (SOC). At the time PTO is requested, the SOC Shift Supervisor must independently verify and certify that all required "
        "analog and status points (gross generation, POI voltage/current/frequency, net export, breaker status) are online and healthy. "
        "There is no provision in utility tariff or standards for conditional or interim PTO without live telemetry."
    )

    p_s6_b4 = doc.add_paragraph(style='List Bullet')
    p_s6_b4.paragraph_format.space_after = Pt(4)
    r_s6_b4_b = p_s6_b4.add_run("Written Issuance of PTO: ")
    r_s6_b4_b.bold = True
    p_s6_b4.add_run(
        "Upon successful resolution of the witness-test determination and SOC telemetry sign-off, the DER Program Office will issue "
        "the formal, written Permission to Operate, authorizing commercial parallel generation."
    )

    # 11. Closing & Program Contacts
    p_close = doc.add_paragraph()
    p_close.paragraph_format.space_before = Pt(8)
    p_close.paragraph_format.space_after = Pt(8)
    p_close.add_run(
        "In summary, we are fully prepared to support your target backfeed date of July 29, 2025, provided Tamsworth and Halbray "
        "complete the Kelloway Township inspection on July 24, 2025 and transmit the written final electrical approval to us prior to July 29. "
        "Please transmit the inspection certificate to der.program@alleniom.com as soon as Inspector Telford signs off. "
        "Should you have any questions regarding switching coordination or submittal requirements, please contact the undersigned directly."
    )

    # Signature Block
    p_sig = doc.add_paragraph()
    p_sig.paragraph_format.space_after = Pt(1)
    p_sig.add_run("Sincerely,")

    p_sign_name = doc.add_paragraph()
    p_sign_name.paragraph_format.space_before = Pt(24)
    p_sign_name.paragraph_format.space_after = Pt(1)
    r_sn = p_sign_name.add_run("S. Rennick")
    r_sn.bold = True
    r_sn.font.size = Pt(10.5)

    p_sign_title = doc.add_paragraph()
    p_sign_title.paragraph_format.space_after = Pt(14)
    r_st = p_sign_title.add_run(
        "Commissioning Coordinator & Electrical Engineer\n"
        "DER Program Office  ·  Commissioning Group\n"
        "Alleniom Utilities\n"
        "Email: s.rennick@alleniom.com  ·  Direct: (612) 555-0100"
    )
    r_st.font.size = Pt(9)
    r_st.font.color.rgb = COLOR_SECONDARY

    # CC Block
    p_cc = doc.add_paragraph()
    p_cc.paragraph_format.space_after = Pt(0)
    pBdr_cc = parse_xml(f'<w:pBdr {nsdecls("w")}><w:top w:val="single" w:sz="4" w:space="1" w:color="{HEX_BORDER}"/></w:pBdr>')
    p_cc._p.get_or_add_pPr().append(pBdr_cc)
    r_cc_lbl = p_cc.add_run("cc (via electronic distribution):\n")
    r_cc_lbl.bold = True
    r_cc_lbl.font.size = Pt(8)
    r_cc_lbl.font.color.rgb = COLOR_MUTED
    r_cc_txt = p_cc.add_run(
        "Dana Whitcomb, Vice President, Distribution Operations, Alleniom Utilities\n"
        "Harriet Ngoyi, Director, Regulatory Affairs, Alleniom Utilities\n"
        "Meera Vellanki, Manager, Interconnection Studies, Alleniom Utilities\n"
        "Marcus Deele, SCADA/EMS Engineering, Alleniom Utilities\n"
        "N. Achterberg, P.E., Distribution Protection Engineering, Alleniom Utilities\n"
        "Distribution Operations — DER Switching Desk, Alleniom Utilities\n"
        "R. Vance, Electrical Engineer, Tamsworth Electrical Constructors Inc.\n"
        "Graham Telford, Electrical Inspector, Kelloway Township Building Department"
    )
    r_cc_txt.font.size = Pt(8)
    r_cc_txt.font.color.rgb = COLOR_MUTED

    doc.save('/filesystem/Halbray_Backfeed_Reply.docx')
    print("Successfully generated /filesystem/Halbray_Backfeed_Reply.docx")

if __name__ == '__main__':
    create_document()
