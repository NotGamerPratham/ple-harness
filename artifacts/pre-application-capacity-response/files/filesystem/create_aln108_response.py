import os
import docx
from docx import Document
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL
from docx.oxml import OxmlElement, parse_xml
from docx.oxml.ns import nsdecls, qn

def create_document():
    doc = Document()
    
    # Page setup - 1 inch margins
    sections = doc.sections
    for section in sections:
        section.top_margin = Inches(1.0)
        section.bottom_margin = Inches(1.0)
        section.left_margin = Inches(1.0)
        section.right_margin = Inches(1.0)
        section.different_first_page_header_footer = True
        
        # Header for later pages
        header = section.header
        hp = header.paragraphs[0]
        hp.alignment = WD_ALIGN_PARAGRAPH.RIGHT
        hrun = hp.add_run("Alleniom Utilities — DER Program Office | Doc no. COR-ALN108-2025-0714")
        hrun.font.name = 'Arial'
        hrun.font.size = Pt(8.5)
        hrun.font.color.rgb = RGBColor(0x71, 0x80, 0x96)
        
        # Footer for all pages
        footer = section.footer
        fp = footer.paragraphs[0]
        fp.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
        frun1 = fp.add_run("Feeder ALN-108 Pre-Application Response · Northline Renewables LLC")
        frun1.font.name = 'Arial'
        frun1.font.size = Pt(8.5)
        frun1.font.color.rgb = RGBColor(0x71, 0x80, 0x96)
        
        # Tab to right
        frun2 = fp.add_run("\tPage 1 of 12 (Official Record · Closed Case #44)")
        frun2.font.name = 'Arial'
        frun2.font.size = Pt(8.5)
        frun2.font.color.rgb = RGBColor(0x71, 0x80, 0x96)

    # Styles setup
    styles = doc.styles
    normal_style = styles['Normal']
    normal_font = normal_style.font
    normal_font.name = 'Calibri'
    normal_font.size = Pt(11)
    normal_font.color.rgb = RGBColor(0x2D, 0x37, 0x48) # Slate charcoal
    
    # Color palette
    NAVY = RGBColor(0x1A, 0x36, 0x5D)     # Primary Header #1A365D
    SLATE = RGBColor(0x2B, 0x6C, 0xB0)    # Subheading #2B6CB0
    CHARCOAL = RGBColor(0x2D, 0x37, 0x48) # Body #2D3748
    MUTED = RGBColor(0x71, 0x80, 0x96)    # Captions/Muted #718096
    RED = RGBColor(0x9B, 0x2C, 0x2C)      # Denials/Warnings #9B2C2C
    GREEN = RGBColor(0x22, 0x54, 0x3D)    # Approvals/Clearances #22543D

    def add_title(text):
        p = doc.add_paragraph()
        p.paragraph_format.space_before = Pt(0)
        p.paragraph_format.space_after = Pt(2)
        p.paragraph_format.line_spacing = 1.15
        run = p.add_run(text)
        run.bold = True
        run.font.name = 'Arial'
        run.font.size = Pt(20)
        run.font.color.rgb = NAVY
        return p

    def add_subtitle(text):
        p = doc.add_paragraph()
        p.paragraph_format.space_before = Pt(2)
        p.paragraph_format.space_after = Pt(12)
        run = p.add_run(text)
        run.font.name = 'Arial'
        run.font.size = Pt(12)
        run.font.color.rgb = SLATE
        return p

    def add_h1(text):
        p = doc.add_paragraph()
        p.paragraph_format.space_before = Pt(18)
        p.paragraph_format.space_after = Pt(6)
        p.paragraph_format.keep_with_next = True
        run = p.add_run(text)
        run.bold = True
        run.font.name = 'Arial'
        run.font.size = Pt(14)
        run.font.color.rgb = NAVY
        return p

    def add_h2(text):
        p = doc.add_paragraph()
        p.paragraph_format.space_before = Pt(12)
        p.paragraph_format.space_after = Pt(4)
        p.paragraph_format.keep_with_next = True
        run = p.add_run(text)
        run.bold = True
        run.font.name = 'Arial'
        run.font.size = Pt(12)
        run.font.color.rgb = SLATE
        return p

    def add_h3(text):
        p = doc.add_paragraph()
        p.paragraph_format.space_before = Pt(8)
        p.paragraph_format.space_after = Pt(2)
        p.paragraph_format.keep_with_next = True
        run = p.add_run(text)
        run.bold = True
        run.font.name = 'Arial'
        run.font.size = Pt(11)
        run.font.color.rgb = CHARCOAL
        return p

    def add_p(text, bold_prefix=None, italic=False):
        p = doc.add_paragraph()
        p.paragraph_format.space_before = Pt(0)
        p.paragraph_format.space_after = Pt(5)
        p.paragraph_format.line_spacing = 1.15
        if bold_prefix:
            r_pre = p.add_run(bold_prefix)
            r_pre.bold = True
            r_pre.font.name = 'Calibri'
            r_pre.font.size = Pt(11)
            r_pre.font.color.rgb = CHARCOAL
        run = p.add_run(text)
        run.font.name = 'Calibri'
        run.font.size = Pt(11)
        run.italic = italic
        run.font.color.rgb = CHARCOAL
        return p

    def add_bullet(text, bold_prefix=None):
        p = doc.add_paragraph(style='List Bullet')
        p.paragraph_format.space_before = Pt(0)
        p.paragraph_format.space_after = Pt(3)
        p.paragraph_format.line_spacing = 1.15
        if bold_prefix:
            r_pre = p.add_run(bold_prefix)
            r_pre.bold = True
            r_pre.font.name = 'Calibri'
            r_pre.font.size = Pt(11)
            r_pre.font.color.rgb = CHARCOAL
        run = p.add_run(text)
        run.font.name = 'Calibri'
        run.font.size = Pt(11)
        run.font.color.rgb = CHARCOAL
        return p

    def set_cell_background(cell, hex_color):
        tcPr = cell._tc.get_or_add_tcPr()
        shd = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{hex_color}"/>')
        tcPr.append(shd)

    def set_cell_margins(cell, top=100, bottom=100, left=150, right=150):
        tcPr = cell._tc.get_or_add_tcPr()
        tcMar = parse_xml(f'<w:tcMar {nsdecls("w")}><w:top w:w="{top}" w:type="dxa"/><w:bottom w:w="{bottom}" w:type="dxa"/><w:left w:w="{left}" w:type="dxa"/><w:right w:w="{right}" w:type="dxa"/></w:tcMar>')
        tcPr.append(tcMar)

    def set_table_borders(table, color="D3D3D3", sz="4", val="single"):
        tblPr = table._tbl.tblPr
        borders = parse_xml(f'<w:tblBorders {nsdecls("w")}><w:top w:val="{val}" w:sz="{sz}" w:space="0" w:color="{color}"/><w:bottom w:val="{val}" w:sz="{sz}" w:space="0" w:color="{color}"/><w:insideH w:val="{val}" w:sz="{sz}" w:space="0" w:color="{color}"/><w:left w:val="none"/><w:right w:val="none"/><w:insideV w:val="none"/></w:tblBorders>')
        tblPr.append(borders)

    def make_callout(text_list, title="DETERMINATION SUMMARY", border_color="1A365D", fill_color="F0F4F8"):
        tbl = doc.add_table(rows=1, cols=1)
        tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
        tbl.autofit = False
        cell = tbl.cell(0, 0)
        cell.width = Inches(6.5)
        set_cell_background(cell, fill_color)
        set_cell_margins(cell, top=140, bottom=140, left=200, right=200)
        
        tcPr = cell._tc.get_or_add_tcPr()
        borders = parse_xml(f'<w:tcBorders {nsdecls("w")}><w:left w:val="single" w:sz="24" w:space="0" w:color="{border_color}"/><w:top w:val="none"/><w:right w:val="none"/><w:bottom w:val="none"/></w:tcBorders>')
        tcPr.append(borders)
        
        p = cell.paragraphs[0]
        p.paragraph_format.space_before = Pt(2)
        p.paragraph_format.space_after = Pt(4)
        r = p.add_run(title)
        r.bold = True
        r.font.name = 'Arial'
        r.font.size = Pt(11)
        r.font.color.rgb = RGBColor(0x1A, 0x36, 0x5D)
        
        for t in text_list:
            p2 = cell.add_paragraph()
            p2.paragraph_format.space_before = Pt(2)
            p2.paragraph_format.space_after = Pt(3)
            p2.paragraph_format.line_spacing = 1.15
            r2 = p2.add_run(t)
            r2.font.name = 'Calibri'
            r2.font.size = Pt(10)
            r2.font.color.rgb = RGBColor(0x2D, 0x37, 0x48)
        
        sp = doc.add_paragraph()
        sp.paragraph_format.space_before = Pt(0)
        sp.paragraph_format.space_after = Pt(6)

    # -------------------------------------------------------------
    # DOCUMENT HEADER
    # -------------------------------------------------------------
    p_meta = doc.add_paragraph()
    p_meta.paragraph_format.space_after = Pt(2)
    r_meta = p_meta.add_run("ALLENIOM UTILITIES · DER PROGRAM OFFICE · DISTRIBUTION PLANNING")
    r_meta.bold = True
    r_meta.font.name = 'Arial'
    r_meta.font.size = Pt(9)
    r_meta.font.color.rgb = MUTED
    
    p_meta2 = doc.add_paragraph()
    p_meta2.paragraph_format.space_after = Pt(12)
    r_meta2 = p_meta2.add_run("4200 Veldmere Boulevard, Halston, Alleron 01HA · (612) 555-0100 · alleniom.com\nDoc no. COR-ALN108-2025-0714 · Rev 1 · Classification: Official Program Determination & Developer Correspondence")
    r_meta2.font.name = 'Calibri'
    r_meta2.font.size = Pt(9.5)
    r_meta2.font.color.rgb = MUTED

    add_title("Written Response and Formal Determination on Pre-Application Request: Feeder ALN-108")
    add_subtitle("Evaluation of Available Hosting Capacity, Queue Reconciliation, Technical Upgrade Indication, and Program Office Case Disposition (Northline Renewables LLC — Elderpine Solar I, 3.0 MW Pure Generation)")

    # Document Control Metadata Box
    meta_table = doc.add_table(rows=7, cols=2)
    meta_table.alignment = WD_TABLE_ALIGNMENT.CENTER
    meta_table.autofit = False
    set_table_borders(meta_table, color="CBD5E0", sz="4")
    
    col_widths = [Inches(2.2), Inches(4.3)]
    meta_data = [
        ("Date of Determination:", "July 14, 2025"),
        ("Originating Office:", "DER Program Office (Interconnection Studies & Distribution Planning)"),
        ("Submitting Developer:", "Northline Renewables LLC (Primary Contact: Peter Ashford, Dir. of Project Development)"),
        ("Developer Request Date:", "July 2, 2025 (Received via program inbox der.program@alleniom.com)"),
        ("Subject Facility / POI:", "Elderpine Solar I — 3.0 MW-AC / 3.9 MW-DC Pure Generation, Feeder ALN-108 (13.2 kV, Elderpine Substation)"),
        ("Case Tracking Reference:", "OpenProject Project #3 (DER Program Backlog Review), Work Package #44"),
        ("Governing Framework:", "APUC Electric Tariff Vol. III §12; DIS-01 Rev 4; DPS-07 Rev 2; TCS-02; DIR-2025-0627; RA-2025-07-01")
    ]
    for i, (k, v) in enumerate(meta_data):
        row = meta_table.rows[i]
        c0, c1 = row.cells[0], row.cells[1]
        c0.width, c1.width = col_widths[0], col_widths[1]
        set_cell_background(c0, "F7FAFC")
        set_cell_margins(c0, top=60, bottom=60, left=100, right=100)
        set_cell_margins(c1, top=60, bottom=60, left=100, right=100)
        p0 = c0.paragraphs[0]
        p0.paragraph_format.space_after = Pt(0)
        r0 = p0.add_run(k)
        r0.bold = True
        r0.font.name = 'Arial'
        r0.font.size = Pt(9.5)
        r0.font.color.rgb = NAVY
        p1 = c1.paragraphs[0]
        p1.paragraph_format.space_after = Pt(0)
        r1 = p1.add_run(v)
        r1.font.name = 'Calibri'
        r1.font.size = Pt(9.5)
        r1.font.color.rgb = CHARCOAL

    doc.add_paragraph().paragraph_format.space_after = Pt(8)

    # -------------------------------------------------------------
    # SECTION 1: EXECUTIVE SUMMARY & TABLE OF DETERMINATIONS
    # -------------------------------------------------------------
    add_h1("1. Executive Summary & Table of Determinations")
    add_p("This document constitutes the official written determination and response of the Alleniom Utilities DER Program Office to the Pre-Application Request submitted on July 2, 2025, by Northline Renewables LLC ('Northline' or 'Applicant') concerning a proposed 3.0 MW pure-generation photovoltaic facility ('Elderpine Solar I') intended for interconnection on Feeder ALN-108 out of Elderpine Substation at 13.2 kV.")
    add_p("In its submittal, Northline specifically requested written confirmation from Alleniom Utilities that 3.0 MW of available hosting capacity remains on Feeder ALN-108, citing the published Feeder Hosting Capacity Map (HCM-2024-Q2, publication date May 15, 2024). Northline stated that its project sizing was scoped exactly at nameplate 3.0 MW to match published headroom without exceeding it. Northline further requested identification of known conditions, restrictions, or upgrade indications, and the scheduling of a pre-application dialogue meeting with Distribution Planning and the DER Program Office.")
    add_p("Pursuant to the commercial DER interconnection program backlog review ordered on June 27, 2025, by the Vice President of Distribution Operations (DIR-2025-0627), and operationalized under Regulatory Affairs Tasking Memorandum RA-2025-07-01 (§3.7, Hosting-Capacity Corrections), the DER Program Office has reviewed the subject pre-application request against the Active Queue Report as of July 14, 2025, the underlying Distribution Planning studies, and Program Office records. This determination is issued prior to the August 15, 2025 formal response to the Alleron Municipal League ('League') and the September 10, 2025 Alleron Public Utilities Commission ('APUC') briefing.")
    
    make_callout([
        "1. Written Confirmation of 3.0 MW Available Capacity: DENIED / REFUSED. Available capacity is NOT 3.0 MW. The published Hosting Capacity Map figure of 3.0 MW (dated 05/15/2024) is stale and does not reflect post-publication queue commitments. Distribution Planning's interim study update (PLN-ALN-108-2024-10, dated 10/15/2024) established a working interim figure of 1.8 MW after straight-line netting of Grantwyck Solar (PXA-2024-0231, 1.2 MW, queued 09/18/2024). Furthermore, active queue records as of 07/14/2025 reflect an intervening queue addition: Cindermere Renewables (PXA-2025-0044, 1.0 MW, queued 02/06/2025), which reduces straight-line uncommitted feeder headroom to approximately 0.8 MW (800 kW).",
        "2. Known Conditions, Restrictions & Upgrade Indications: IDENTIFIED & NOTIFIED. Feeder ALN-108 is a 13.2 kV pure-generation segment. Siting a 3.0 MW facility exceeds remaining feeder headroom by ~2.2 MW, triggering automatic referral to a System Impact Study (SIS), likely distribution line reconductoring, Elderpine Substation power transformer reverse-power review, and transfer trip protection. A utility-owned POI recloser with ANSI 32 directional power elements (DPS-07 Rev 2 / DIS-01 Table 5-1) and a utility-owned RTU presenting live DNP3 SCADA telemetry (TCS-02 §5, ~8-month lead time) are mandatory conditions of Permission to Operate (PTO).",
        "3. Pre-Application Dialogue Meeting: GRANTED / ACCEPTED. Alleniom Utilities offers a technical conference within 10 business days (by late July / early August 2025) to discuss project scoping, including options to resize to ≤800 kW to sit within available headroom versus proceeding at 3.0 MW on a full-study track.",
        "4. Program Office Case Tracking: RECORDED, LOGGED & CLOSED. The call on Case #44 has been recorded in OpenProject tracking, required follow-up actions (priority feeder restudy request to Distribution Planning; Hosting Capacity Map Q3 refresh maintenance; pre-app dialogue coordination) have been logged, and Case #44 is officially CLOSED on the record."
    ], title="SUMMARY OF PROGRAM OFFICE DETERMINATIONS & CALLS")

    add_p("The table below details each specific determination, the basis relied upon, and the call made by the Program Office:")

    # Table of Determinations
    t_det = doc.add_table(rows=5, cols=4)
    t_det.alignment = WD_TABLE_ALIGNMENT.CENTER
    t_det.autofit = False
    set_table_borders(t_det, color="CBD5E0", sz="4")
    
    col_w_det = [Inches(1.5), Inches(1.3), Inches(2.2), Inches(1.5)]
    headers_det = ["Request Item / Topic", "Published / Stated Figure", "Program Office Analysis & Reconciled Basis", "Official Call Made"]
    
    hdr_row = t_det.rows[0]
    for idx, text in enumerate(headers_det):
        cell = hdr_row.cells[idx]
        cell.width = col_w_det[idx]
        set_cell_background(cell, "1A365D")
        set_cell_margins(cell, top=100, bottom=100, left=100, right=100)
        p = cell.paragraphs[0]
        p.paragraph_format.space_after = Pt(0)
        r = p.add_run(text)
        r.bold = True
        r.font.name = 'Arial'
        r.font.size = Pt(9)
        r.font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)
        
    rows_det_data = [
        (
            "Item 1: Confirmation of 3.0 MW Available Capacity",
            "3.0 MW available (HCM-2024-Q2 published 05/15/2024, study 04/2024)",
            "Published map carries express Applicability caveat that values do not reflect subsequent queue additions. Planning Study PLN-ALN-108-2024-10 (10/15/2024) netted 1.2 MW Grantwyck Solar (PXA-2024-0231), yielding 1.8 MW interim figure. Active Queue as of 07/14/2025 carries subsequent 1.0 MW Cindermere Renewables (PXA-2025-0044, queued 02/06/2025). Net straight-line uncommitted headroom is 0.8 MW (800 kW).",
            "DENIED / REFUSED\nCannot confirm 3.0 MW. Stated figures: 1.8 MW working study; 0.8 MW active queue netted headroom."
        ),
        (
            "Item 2: Conditions, Restrictions & Upgrade Indications",
            "Standard pure-generation interconnection without stated restrictions",
            "Feeder ALN-108 is a 13.2 kV pure-generation segment. Proposed 3.0 MW project exceeds available headroom by 2.2 MW, triggering automatic fast-track screen failure and mandatory System Impact Study (SIS). Upgrades likely required: distribution reconductoring, substation transformer reverse-power review, voltage regulation, transfer trip. Dedicated utility POI recloser required (DPS-07 Rev 2 / DIS-01 Table 5-1). Utility RTU with live SCADA telemetry required (TCS-02 §5; ~8-month lead time; no interim PTO).",
            "CONDITIONS & UPGRADES NOTIFIED\nSIS mandatory for 3.0 MW; physical upgrades anticipated; POI recloser & RTU required."
        ),
        (
            "Item 3: Pre-Application Dialogue Meeting",
            "Request for scheduling at Alleniom's earliest convenience",
            "Consistent with HCM-2024-Q2 Applicability front matter and Alleniom pre-application procedures, dialogue is warranted to discuss project sizing alternatives (resizing to ≤800 kW to match headroom vs. maintaining 3.0 MW on full SIS track) and technical scoping prior to formal filing.",
            "GRANTED / ACCEPTED\nConference offered within 10 business days (late July / early August 2025)."
        ),
        (
            "Operational Case Tracking: Case #44 Disposition",
            "OpenProject Work Package #44 'New' (0% complete, due 08/15/2025)",
            "Regulatory Affairs Tasking Memo RA-2025-07-01 §3.7 requires priority feeder refresh request before communicating capacity. HCM refresh criteria (pre-app date, capacity requested vs. headroom, pure-generation category) establish top re-study priority. Case tracking requires logging determinations, follow-up, and closure.",
            "CASE CLOSED\nCall recorded in OpenProject; priority restudy requested; map maintenance queued; Case #44 CLOSED (100%)."
        )
    ]

    for r_idx, data in enumerate(rows_det_data):
        row = t_det.rows[r_idx + 1]
        bg_col = "FFFFFF" if r_idx % 2 == 0 else "F7FAFC"
        for c_idx, text in enumerate(data):
            cell = row.cells[c_idx]
            cell.width = col_w_det[c_idx]
            set_cell_background(cell, bg_col)
            set_cell_margins(cell, top=80, bottom=80, left=100, right=100)
            p = cell.paragraphs[0]
            p.paragraph_format.space_after = Pt(0)
            p.paragraph_format.line_spacing = 1.15
            r = p.add_run(text)
            r.font.name = 'Calibri'
            r.font.size = Pt(9)
            if c_idx == 3:
                r.bold = True
                if "DENIED" in text:
                    r.font.color.rgb = RED
                elif "GRANTED" in text or "CLOSED" in text:
                    r.font.color.rgb = GREEN
                else:
                    r.font.color.rgb = NAVY
            else:
                r.font.color.rgb = CHARCOAL

    doc.add_paragraph().paragraph_format.space_after = Pt(12)

    # -------------------------------------------------------------
    # SECTION 2: FORMAL WRITTEN RESPONSE TO NORTHLINE RENEWABLES LLC
    # -------------------------------------------------------------
    add_h1("2. Formal Written Response to Northline Renewables LLC")
    add_p("The text below represents the formal, transmittable written response issued by the Alleniom Utilities DER Program Office to Northline Renewables LLC, addressing in detail all elements of its Pre-Application Request dated July 2, 2025:")

    # Formal Letter Box / Bordered Sub-Document
    tbl_letter = doc.add_table(rows=1, cols=1)
    tbl_letter.alignment = WD_TABLE_ALIGNMENT.CENTER
    tbl_letter.autofit = False
    l_cell = tbl_letter.cell(0, 0)
    l_cell.width = Inches(6.5)
    set_cell_background(l_cell, "FCFDFD")
    set_cell_margins(l_cell, top=160, bottom=160, left=220, right=220)
    
    tcPr = l_cell._tc.get_or_add_tcPr()
    borders = parse_xml(f'<w:tcBorders {nsdecls("w")}><w:left w:val="single" w:sz="12" w:space="0" w:color="CBD5E0"/><w:top w:val="single" w:sz="12" w:space="0" w:color="CBD5E0"/><w:right w:val="single" w:sz="12" w:space="0" w:color="CBD5E0"/><w:bottom w:val="single" w:sz="12" w:space="0" w:color="CBD5E0"/></w:tcBorders>')
    tcPr.append(borders)

    lp = l_cell.paragraphs[0]
    lp.paragraph_format.space_after = Pt(4)
    lr = lp.add_run("ALLENIOM UTILITIES — DER PROGRAM OFFICE\n4200 Veldmere Boulevard, Halston, Alleron 01HA · der.program@alleniom.com · (612) 555-0100")
    lr.bold = True
    lr.font.name = 'Arial'
    lr.font.size = Pt(9.5)
    lr.font.color.rgb = NAVY

    lp_date = l_cell.add_paragraph()
    lp_date.paragraph_format.space_before = Pt(8)
    lp_date.paragraph_format.space_after = Pt(8)
    lr_date = lp_date.add_run("Date: July 14, 2025\n\nTo:\nPeter Ashford, Director of Project Development\nNorthline Renewables LLC\n1840 Ferngate Parkway, Suite 210\nHalston, Alleron 02HA\npeter.ashford@northlinerenewables.com | (612) 555-1826\n\nFrom:\nAlleniom Utilities — DER Program Office & Distribution Planning\n4200 Veldmere Boulevard, Halston, Alleron 01HA\nder.program@alleniom.com\n\nSubject: Pre-Application Response — Feeder ALN-108 Capacity Inquiry (Project: Elderpine Solar I, 3.0 MW-AC)")
    lr_date.font.name = 'Calibri'
    lr_date.font.size = Pt(10)
    lr_date.font.color.rgb = CHARCOAL

    def add_lp(text, bold_prefix=None, space_after=6, italic=False):
        p = l_cell.add_paragraph()
        p.paragraph_format.space_before = Pt(2)
        p.paragraph_format.space_after = Pt(space_after)
        p.paragraph_format.line_spacing = 1.15
        if bold_prefix:
            bp = p.add_run(bold_prefix)
            bp.bold = True
            bp.font.name = 'Calibri'
            bp.font.size = Pt(10)
            bp.font.color.rgb = CHARCOAL
        r = p.add_run(text)
        r.font.name = 'Calibri'
        r.italic = italic
        r.font.size = Pt(10)
        r.font.color.rgb = CHARCOAL
        return p

    add_lp("Dear Mr. Ashford:")
    add_lp("The Alleniom Utilities DER Program Office, in coordination with Distribution Planning and Interconnection Studies, has completed its review of Northline Renewables LLC's ('Northline') Pre-Application Request dated July 2, 2025. Your request seeks written confirmation from Alleniom Utilities regarding the availability of 3.0 MW of hosting capacity on Feeder ALN-108 (Elderpine Substation service area, 13.2 kV primary line-to-line voltage) to support a proposed 3.0 MW-AC (3.9 MW-DC) pure-generation solar photovoltaic project operating under the working title 'Elderpine Solar I'.")
    add_lp("Northline's request states that its project sizing was selected specifically to sit at, rather than above, the 3.0 MW available capacity value published on the Alleniom Utilities Feeder Hosting Capacity Map (Doc no. HCM-2024-Q2, publication date May 15, 2024), with the stated intent of avoiding an interconnection request that exceeds stated feeder headroom. Northline requested: (1) written confirmation that 3.0 MW remains available as of the date of request; (2) identification of known conditions, restrictions, or upgrade indications; and (3) scheduling of a pre-application dialogue meeting with Alleniom staff.")
    add_lp("In response, Alleniom Utilities provides the following determinations, detailed queue reconciliation, and technical guidance:")

    add_lp("1. Written Determination on Capacity Confirmation (Refusal of Confirmation):", bold_prefix="")
    add_lp("Alleniom Utilities CANNOT confirm that 3.0 MW of available hosting capacity remains on Feeder ALN-108 as of the date of your request or as of the date of this response. Northline's request for written confirmation of 3.0 MW available capacity is respectfully REFUSED / DENIED. Siting a 3.0 MW project on Feeder ALN-108 will materially exceed the feeder's current available headroom.")
    
    add_lp("2. Program Accounting and Explanation of the Available Figure:", bold_prefix="")
    add_lp("Northline's reliance on the published May 15, 2024 Hosting Capacity Map (HCM-2024-Q2) reflects an understanding of the feeder baseline that has been superseded by post-publication interconnection queue activity. As expressly stated in the Applicability notes of the published Hosting Capacity Map front matter:")
    add_lp("'Values are the published available capacity figures as of the publication date shown above. Applicants and pre-application requesters should consult Distribution Planning for confirmation before finalizing project sizing decisions on any feeder shown. Published values do not reflect interconnection queue activity recorded after the publication date; the active-queue register maintained by the DER Program Office is the record of that activity. A pre-application capacity response is prepared against the published value as adjusted for queue entries added since publication.'", italic=True)
    add_lp("A complete audit of the DER Program records as of July 14, 2025, reveals the following progression of Feeder ALN-108:")
    add_lp("•  Baseline Published Capacity (3.0 MW): The 3.0 MW value published on May 15, 2024, was derived from an underlying Distribution Planning study completed in April 2024 (PLN-ALN-108-2024-04). This baseline study modeled existing feeder load profiles and standard thermal/voltage screens, and already incorporated two pre-existing queue entries: Ravenford Data Services (PXA-2023-0894, 1.1 MW, queued 11/20/2023, ISA executed) and Fenwyn Industries Corp (PXA-2024-0091, 690 kW, queued 04/03/2024, currently in construction). The 3.0 MW published headroom existed over and above those two baseline installations.")
    add_lp("•  Post-Publication Queue Addition 1 (Grantwyck Solar, 1.2 MW): On September 18, 2024, Grantwyck Solar LLC filed an interconnection application (PXA-2024-0231) for a 1.2 MW pure-generation solar array on Feeder ALN-108. In response, Distribution Planning issued a Post-Publication Planning Study Update (Doc no. PLN-ALN-108-2024-10, dated October 15, 2024, authored by June Halloway). That study applied a straight-line nameplate netting of 1.2 MW against the 3.0 MW published baseline, establishing a working interim available capacity figure of 1.8 MW (3.0 MW - 1.2 MW = 1.8 MW). The study explicitly advised that the 1.8 MW figure was a working reference for Distribution Planning and pre-application correspondence, and noted that any subsequent queue additions would require further downward adjustment.")
    add_lp("•  Post-Publication Queue Addition 2 (Cindermere Renewables, 1.0 MW): On February 6, 2025, Cindermere Renewables LLC filed an interconnection application (PXA-2025-0044) for a 1.0 MW pure-generation facility ('Cindermere Feeder Site A') on Feeder ALN-108. As reflected in the Active Queue Report as of July 14, 2025, this 1.0 MW project is currently active at technical screening. Under Section 12.3 and Section 12.7 of Alleniom Utilities' APUC-filed Interconnection Tariff, applications hold legal queue priority based on their deemed-complete filing date. Cindermere holds senior queue priority over any subsequent application Northline may file.")
    add_lp("•  Reconciled Net Working Capacity (0.8 MW / 800 kW): Applying the governing straight-line queue-netting principle against the published baseline, the uncommitted available capacity on Feeder ALN-108 as of July 14, 2025, is calculated as follows:\n    Published Baseline Headroom (05/15/2024):  3.0 MW\n    Less Post-Publication Entry 1 (Grantwyck Solar, PXA-2024-0231):  -1.2 MW\n    Interim Working Study Figure (PLN-ALN-108-2024-10, 10/15/2024):  1.8 MW\n    Less Post-Publication Entry 2 (Cindermere Renewables, PXA-2025-0044):  -1.0 MW\n    Net Estimated Available Headroom as of 07/14/2025:  0.8 MW (800 kW)\nTherefore, the working capacity figure that Alleniom Utilities communicates for Feeder ALN-108 is approximately 0.8 MW (800 kW), subject to formal engineering re-study.")

    add_lp("3. Known Technical Conditions, Restrictions, and Upgrade Indications:", bold_prefix="")
    add_lp("Distribution Planning and Interconnection Studies have identified the following technical conditions, restrictions, and likely upgrade triggers governing Feeder ALN-108 and your proposed project:")
    add_lp("•  Pure-Generation Feeder Segment: Feeder ALN-108 is designated as a Pure Generation feeder segment at 13.2 kV nominal voltage. The proposed Elderpine Solar I facility is an export-only, front-of-the-meter project with no on-site load. Consequently, 100% of the project's generated output will inject directly into the Alleniom distribution system, with zero load-masking or on-site netting benefits. Pure-generation projects are weighted at 100% of nameplate against thermal and protection ratings.")
    add_lp("•  Impact of Filing at 3.0 MW (Capacity Deficit of 2.2 MW): A 3.0 MW interconnection application will exceed the feeder's remaining estimated headroom by 2.2 MW (3.0 MW - 0.8 MW = 2.2 MW). Under Section 12 of the Interconnection Tariff and DIS-01 Rev 4, a project of this magnitude will automatically fail initial technical screens (specifically the 15% feeder peak load screen and thermal capacity screens). Fast-track processing is unavailable at 3.0 MW. The application will be mandatorily routed to a full System Impact Study (SIS) and Facilities Study.")
    add_lp("•  Anticipated Distribution and Substation Upgrades: While definitive upgrade requirements can only be established through a formal System Impact Study, preliminary planning analysis indicates that a 3.0 MW injection on Feeder ALN-108 will likely require: (1) extensive distribution line reconductoring along the feeder trunk out of Elderpine Substation to address thermal conductor limits; (2) review and potential modification or uprating of the substation power transformer bank at Elderpine Substation to accommodate substantial reverse power flow during minimum load periods; (3) dynamic voltage regulation equipment (such as line voltage regulators or capacitor banks) to mitigate voltage rise, flicker, and rapid voltage changes; and (4) installation of a dedicated direct transfer trip (DTT) communications scheme between the substation feeder breaker and the facility to prevent unintentional islanding under line-fault conditions.")
    add_lp("•  Protection Standard Requirements (DPS-07 Rev 2 & DIS-01 Rev 4 Table 5-1): For pure-generation interconnections at or above 1.0 MW, Alleniom standards require a dedicated, utility-owned, three-phase electronically controlled Point of Interconnection (POI) recloser located at the primary line tap. The protective relay scheme must incorporate an ANSI 32 directional power element calibrated to trip upon reverse power flow violations, dedicated anti-islanding relaying, phase and ground overcurrent protection (ANSI 50/51/51N), and a visible, lockable, utility-accessible gang-operated disconnect switch.")
    add_lp("•  Telemetry and SCADA Communications (TCS-02 §5 & SOC Standing Enforcement): As a commercial DER facility exceeding the 500 kW threshold (and specifically at 3.0 MW), Elderpine Solar I is subject to Alleniom's Telemetry and Communications Standard (TCS-02). The facility must incorporate a utility-owned Remote Terminal Unit (RTU) interfacing via DNP3 protocol over secure cellular or fiber communications directly to the Alleniom System Operations Center (SOC). Notice is hereby given that under TCS-02 §5 and standing SOC operating rules, Permission to Operate (PTO) will be strictly refused until the RTU is physically installed, fully commissioned end-to-end, and actively presenting valid telemetry points at the SCADA operator console. No interim or provisional energization is permitted under any circumstances. Furthermore, developers are advised that utility-owned RTU and recloser equipment currently carries an approximate 8-month supplier procurement lead time.")
    add_lp("•  Inverter Certification (CEL-2025-Q2): All inverters must be fully certified under IEEE 1547-2018 / UL 1741 SB and listed on the current Alleniom Certified Equipment List (CEL-2025-Q2).")

    add_lp("4. Strategic Sizing Alternatives for Developer Consideration:", bold_prefix="")
    add_lp("Because Northline expressly noted that it scoped its project to match available feeder capacity and welcomed updated planning figures, Alleniom Utilities offers two strategic project sizing paths for your consideration prior to formal application:")
    add_lp("•  Path A — Headroom-Aligned Scoping (≤0.8 MW-AC / 800 kW): If Northline resizes Elderpine Solar I to approximately 800 kW-AC nameplate, the project will sit within the currently estimated uncommitted feeder headroom. While a formal technical screening remains required upon filing, sizing within available headroom maximizes the probability of passing initial technical screens, minimizes or eliminates major distribution trunk rebuild costs, reduces study timelines, and enables a significantly faster path to an Interconnection Service Agreement (ISA).")
    add_lp("•  Path B — Full-Capacity Scoping (3.0 MW-AC): If Northline elects to maintain its 3.0 MW nameplate capacity, Northline should proceed with full awareness that the project will be placed in the study queue behind senior-queued projects, will undergo a formal System Impact Study and Facilities Study, and that Northline will be financially responsible for all network upgrades, reconductoring, substation protections, and transfer trip schemes identified in those studies.")

    add_lp("5. Pre-Application Dialogue Meeting Scheduling (Request Accepted):", bold_prefix="")
    add_lp("Alleniom Utilities is pleased to grant your request for a pre-application dialogue meeting. We invite your technical and development team to a scoping conference with Distribution Planning (June Halloway, Distribution Planning Engineer) and Interconnection Studies (Meera Vellanki, Manager) to review project layout, primary line routing, and sizing options. We propose holding this meeting within ten (10) business days, during the week of July 21, 2025, or July 28, 2025, either virtually or at Alleniom Utilities headquarters (4200 Veldmere Boulevard, Halston).")
    add_lp("To maximize the value of this session, please provide the following preliminary technical materials to der.program@alleniom.com at least three (3) business days prior to the meeting: (1) preliminary site layout plan; (2) draft single-line electrical diagram; (3) proposed Point of Common Coupling (PCC) GPS coordinates; and (4) proposed inverter manufacturer cut sheets.")
    add_lp("Please contact the DER Program Office at (612) 555-0100 or via email at der.program@alleniom.com to confirm your team's availability.")

    add_lp("Sincerely,")
    add_lp("/s/ June Halloway\nJune Halloway, Distribution Planning Engineer\nAlleniom Utilities — Distribution Planning\njune.halloway@alleniom.com | (612) 555-0105\n\n/s/ Meera Vellanki\nMeera Vellanki, Manager, Interconnection Studies\nAlleniom Utilities — DER Program Office\nmeera.vellanki@alleniom.com | (612) 555-0102", space_after=2)

    doc.add_paragraph().paragraph_format.space_after = Pt(12)

    # -------------------------------------------------------------
    # SECTION 3: TECHNICAL DETERMINATIONS & REGULATORY BASIS
    # -------------------------------------------------------------
    add_h1("3. Comprehensive Technical Determinations & Regulatory Basis")
    add_p("This section sets forth the formal internal engineering, planning, and regulatory determinations made by the DER Program Office in disposing of the Pre-Application Request for Feeder ALN-108, detailing the specific evidentiary records, tariff sections, operating standards, and planning studies relied upon.")

    add_h2("3.1 Regulatory Framework & Directive Context")
    add_p("On June 27, 2025, Dana Whitcomb, Vice President of Distribution Operations, issued an executive directive (DIR-2025-0627) ordering an immediate, comprehensive backlog review of the commercial DER interconnection program. This directive was triggered by formal escalation correspondence received from the Alleron Municipal League dated June 20, 2025, and copied to the APUC Energy Resources Division, concerning stalled commercial and municipal interconnection projects across Alleniom territory.")
    add_p("The directive established two governing, non-negotiable deadlines: (1) August 15, 2025, for a substantive, project-specific written response to the Alleron Municipal League; and (2) September 10, 2025, for a comprehensive briefing to the APUC Energy Resources Division. The directive ordered that every disposition reached must be tariff-defensible on paper, that all noticing and procedural guidelines be strictly enforced, that procedural conflicts be routed through formal channels, and that no informal queue adjustments or political prioritization occur.")
    add_p("On July 1, 2025, Harriet Ngoyi, Director of Regulatory Affairs, issued Tasking Memorandum RA-2025-07-01 to the DER Program Manager, operationalizing the backlog review. Section 3.7 of this memorandum specifically governs Hosting-Capacity Corrections:")
    add_p("'3.7 Hosting-capacity corrections. Before any capacity figure from the published hosting-capacity map is communicated externally, confirm that the figure reflects the current state of the affected feeder. A priority refresh is to be requested from Distribution Planning under the published refresh-prioritization criteria.'", italic=True)
    add_p("The review of Northline's pre-application request on Feeder ALN-108 directly implicates Section 3.7. Siting a 3.0 MW facility on a feeder with stale map figures without reconciling the active queue would violate this regulatory directive and undermine the integrity of the queue accounting required for the August 15 League response and the September 10 APUC briefing.")

    add_h2("3.2 Feeder ALN-108 Electrical Profile & Planning Baseline")
    add_p("Feeder ALN-108 is a 13.2 kV distribution feeder originating from the Elderpine Substation, serving a designated commercial and rural service area in Alleron. In the Alleniom Feeder Hosting Capacity Map Export (Doc no. HCM-2024-Q2, published May 15, 2024), Feeder ALN-108 is classified as a Pure Generation feeder segment. Nominal voltage is 13.2 kV line-to-line.")
    add_p("The published available capacity of 3.0 MW was established in Distribution Planning Study PLN-ALN-108-2024-04 (April 2024). Under Alleniom Distribution Planning methodology, available hosting capacity represents the maximum additional generation that can be accommodated on the feeder without violating thermal ratings of conductors and substation transformers, steady-state voltage limits (0.95 to 1.05 p.u.), rapid voltage change/flicker thresholds, or existing protection coordination schemes.")
    add_p("A critical technical determination of this review concerns the treatment of DER projects interconnected or queued prior to the publication of the Hosting Capacity Map. Prior to April 2024, two commercial DER projects were queued on Feeder ALN-108:")
    add_bullet("PXA-2023-0894 (Ravenford Data Services): 1.1 MW rooftop PV, queued November 20, 2023, Interconnection Service Agreement executed. This project was fully modeled in the April 2024 planning study.", bold_prefix="Pre-Baseline Queue Project 1: ")
    add_bullet("PXA-2024-0091 (Fenwyn Industries Corp): 690 kW PV array, queued April 3, 2024, currently in construction. This project was also fully accounted for in the April 2024 planning study.", bold_prefix="Pre-Baseline Queue Project 2: ")
    add_p("Because Ravenford Data Services (1.1 MW) and Fenwyn Industries (690 kW) were already incorporated into the baseline power flow models of the April 2024 study, they do NOT net against the 3.0 MW published available capacity. The published 3.0 MW figure represented remaining headroom existing after accounting for those two pre-baseline facilities.")

    add_h2("3.3 Intervening Queue Activity & Net Headroom Reconciliation")
    add_p("Subsequent to the May 15, 2024 publication of HCM-2024-Q2, two material interconnection applications were submitted on Feeder ALN-108 and logged into the active queue:")
    add_p("1. Grantwyck Solar LLC (PXA-2024-0231): Queued on September 18, 2024, for a 1.2 MW pure-generation ground-mount solar facility on Feeder ALN-108. As documented in Distribution Planning Memorandum PLN-ALN-108-2024-10 (dated October 15, 2024, by June Halloway), Distribution Planning conducted an interim queue evaluation. Applying straight-line nameplate netting, Distribution Planning calculated an interim available capacity of 1.8 MW (3.0 MW - 1.2 MW = 1.8 MW). The study noted that 1.8 MW represented the working interim figure for pre-application correspondence, but emphasized that it reflected the queue only as of October 15, 2024, and would require further downward revision upon any subsequent queue additions.")
    add_p("2. Cindermere Renewables LLC (PXA-2025-0044): Queued on February 6, 2025, for a 1.0 MW pure-generation solar array ('Cindermere Feeder Site A') on Feeder ALN-108. In the Active Queue Report as of July 14, 2025, this project is recorded as active at the technical screening stage. Under APUC Tariff §12.3 and §12.7, this application holds a valid, senior queue position that legally commits 1.0 MW of feeder headroom ahead of any prospective Northline submittal.")
    add_p("The table below presents the definitive capacity evolution of Feeder ALN-108 from baseline study to the current date:")

    # Queue Accounting Table
    t_q = doc.add_table(rows=7, cols=5)
    t_q.alignment = WD_TABLE_ALIGNMENT.CENTER
    t_q.autofit = False
    set_table_borders(t_q, color="CBD5E0", sz="4")
    
    col_w_q = [Inches(1.2), Inches(1.8), Inches(1.1), Inches(1.2), Inches(1.2)]
    headers_q = ["Queue / Doc Date", "Project / Action Description", "Capacity", "Queue Posture", "Feeder Headroom"]
    
    for idx, text in enumerate(headers_q):
        cell = t_q.rows[0].cells[idx]
        cell.width = col_w_q[idx]
        set_cell_background(cell, "1A365D")
        set_cell_margins(cell, top=100, bottom=100, left=100, right=100)
        p = cell.paragraphs[0]
        p.paragraph_format.space_after = Pt(0)
        r = p.add_run(text)
        r.bold = True
        r.font.name = 'Arial'
        r.font.size = Pt(9)
        r.font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)
        
    rows_q_data = [
        ("04/2024", "Planning Study PLN-ALN-108-2024-04 (incorporating Ravenford 1.1 MW & Fenwyn 690 kW)", "—", "Base Model of Record", "3.0 MW (Base)"),
        ("05/15/2024", "HCM-2024-Q2 Hosting Capacity Map Publication (Elderpine Substation, 13.2 kV)", "—", "Published of Record", "3.0 MW (Published)"),
        ("09/18/2024", "PXA-2024-0231: Grantwyck Solar LLC (Pure Generation ground mount)", "1.2 MW", "Active Queue (SIS Stage)", "Netted in Q3 Study"),
        ("10/15/2024", "Planning Study PLN-ALN-108-2024-10: Interim Update Q3 (June Halloway)", "-1.2 MW", "Interim Study Record", "1.8 MW (Working)"),
        ("02/06/2025", "PXA-2025-0044: Cindermere Renewables LLC (Pure Generation Site A)", "1.0 MW", "Active (Screening Stage)", "Senior Queue Addition"),
        ("07/14/2025", "DER Program Office Reconciled Posture (Current Evaluation Date)", "-1.0 MW", "Reconciled Status", "0.8 MW (Uncommitted)")
    ]

    for r_idx, data in enumerate(rows_q_data):
        row = t_q.rows[r_idx + 1]
        bg_col = "FFFFFF" if r_idx % 2 == 0 else "F7FAFC"
        for c_idx, text in enumerate(data):
            cell = row.cells[c_idx]
            cell.width = col_w_q[c_idx]
            set_cell_background(cell, bg_col)
            set_cell_margins(cell, top=80, bottom=80, left=100, right=100)
            p = cell.paragraphs[0]
            p.paragraph_format.space_after = Pt(0)
            r = p.add_run(text)
            r.font.name = 'Calibri'
            r.font.size = Pt(9)
            if c_idx == 4:
                r.bold = True
                r.font.color.rgb = NAVY
            else:
                r.font.color.rgb = CHARCOAL

    doc.add_paragraph().paragraph_format.space_after = Pt(10)

    add_h2("3.4 Evaluation of Proposed 3.0 MW Pure-Generation Interconnection")
    add_p("Northline's proposed Elderpine Solar I facility comprises 3.0 MW-AC nameplate inverter capacity and approximately 3.9 MW-DC module capacity (DC/AC ratio of 1.30), utilizing central inverters with plant-level SCADA control and a 100% export profile. Siting a 3.0 MW pure-generation project on Feeder ALN-108 yields the following technical determinations:")
    add_p("1. Severe Capacity Deficit: The proposed 3.0 MW injection exceeds the current straight-line uncommitted headroom of 0.8 MW by 2.2 MW. Even if evaluated against the October 2024 interim study figure of 1.8 MW, the project would exceed headroom by 1.2 MW. Under neither figure can 3.0 MW be accommodated without system modifications.")
    add_p("2. Screen Failure & Mandatory Study Routing: Under APUC Tariff §12.2 and DIS-01 Rev 4 §4, commercial projects between 1 MW and 5 MW are classified as Medium-Scale DER. Because the proposed capacity exceeds 15% of feeder peak load and exceeds 100% of daytime minimum load on Feeder ALN-108, the application will fail Initial Technical Screening. Fast-track approval is legally and technically precluded. Siting at 3.0 MW requires a formal System Impact Study (SIS) and Facilities Study under Tariff §12.")
    add_p("3. Protection & Equipment Scoping (DPS-07 Rev 2 & DIS-01 Table 5-1): Under Alleniom Distribution Protection Standard DPS-07 Rev 2 (§4.2) and DIS-01 Rev 4 Table 5-1, all pure-export facilities ≥1.0 MW require a dedicated utility-owned Point of Interconnection (POI) recloser with electronic controller, microprocessor-based utility-grade relays, ANSI 32 directional power tripping, anti-islanding protection, and direct transfer trip (DTT) where anti-islanding screening indicates risk of islanding on feeder reclosing. The developer is financially responsible for the procurement and installation costs of this utility-owned recloser.")
    add_p("4. Mandatory Telemetry and Commissioning (TCS-02 §5): Under Telemetry & Communications Standard TCS-02 (§2 and §5), all facilities ≥500 kW must provide real-time telemetry to the Alleniom System Operations Center (SOC) via a utility-owned RTU. System Operations Center standing policy, documented in the SOC PTO-Hold Log (DER-EQP-SOC-PTOH), strictly enforces the rule: 'No PTO without live telemetry — TCS-02 §5 (no interim provision).' Permission to operate cannot be granted conditionally or provisionally while awaiting RTU commissioning. Developers must factor the current 8-month RTU/recloser lead time into their construction critical path.")

    doc.add_paragraph().paragraph_format.space_after = Pt(10)

    # -------------------------------------------------------------
    # SECTION 4: CASE TRACKING & FOLLOW-UP ACTION LOG
    # -------------------------------------------------------------
    add_h1("4. Program Office Case Tracking & Follow-Up Action Log")
    add_p("This section documents the formal recording of this determination within the Program Office's case management system (OpenProject Project #3, 'DER Program Backlog Review'), details the logging of all mandatory operational follow-up actions, and records the formal closure of Case #44 on the record.")

    add_h2("4.1 Case Tracking Record (OpenProject Work Package #44)")
    add_p("In accordance with Program Office operating standards and the VP Backlog Review Directive (DIR-2025-0627), all pre-application requests, technical disputes, and queue inquiries are tracked as formal work packages. Work Package #44 was created upon intake of Northline Renewables' request on July 2, 2025.")

    # Work Package Data Box
    t_wp = doc.add_table(rows=8, cols=2)
    t_wp.alignment = WD_TABLE_ALIGNMENT.CENTER
    t_wp.autofit = False
    set_table_borders(t_wp, color="CBD5E0", sz="4")
    
    col_w_wp = [Inches(2.2), Inches(4.3)]
    wp_data = [
        ("OpenProject Work Package ID:", "Work Package #44 (Task)"),
        ("Project Container:", "Project #3 — DER Program Backlog Review (der-backlog-review)"),
        ("Work Package Subject:", "Respond to the Feeder ALN-108 pre-application request"),
        ("Assigned Owner / Role:", "June Halloway, Distribution Planning Engineer (DER Program Office)"),
        ("Author / Intake System:", "OpenProject Admin / Shared Program Inbox (der.program@alleniom.com)"),
        ("Schedule & Milestones:", "Start Date: 2025-07-02 | Completion Date: 2025-07-14 | Due Date: 2025-08-15"),
        ("Prior Case Status:", "Status: 'New' | Completion: 0% | Priority: Normal"),
        ("Final Case Disposition:", "Status: 'Closed' (Status ID: 12) | Completion: 100% | Resolution: Official Response Issued")
    ]

    for i, (k, v) in enumerate(wp_data):
        row = t_wp.rows[i]
        c0, c1 = row.cells[0], row.cells[1]
        c0.width, c1.width = col_w_wp[0], col_w_wp[1]
        set_cell_background(c0, "F7FAFC")
        set_cell_margins(c0, top=60, bottom=60, left=100, right=100)
        set_cell_margins(c1, top=60, bottom=60, left=100, right=100)
        p0 = c0.paragraphs[0]
        p0.paragraph_format.space_after = Pt(0)
        r0 = p0.add_run(k)
        r0.bold = True
        r0.font.name = 'Arial'
        r0.font.size = Pt(9.5)
        r0.font.color.rgb = NAVY
        p1 = c1.paragraphs[0]
        p1.paragraph_format.space_after = Pt(0)
        r1 = p1.add_run(v)
        r1.font.name = 'Calibri'
        r1.font.size = Pt(9.5)
        if "Closed" in v:
            r1.bold = True
            r1.font.color.rgb = GREEN
        else:
            r1.font.color.rgb = CHARCOAL

    doc.add_paragraph().paragraph_format.space_after = Pt(8)

    add_h2("4.2 Record of the Call on the Request's Case")
    add_p("The official determination rendered on Case #44 has been recorded in the OpenProject case history as of July 14, 2025. The entry records:")
    add_bullet("Written Confirmation Call: Denied. Confirmation of 3.0 MW available capacity is refused. Published map figure (3.0 MW) is stale; interim planning study figure is 1.8 MW; current active queue straight-line netted headroom is ~0.8 MW (800 kW).", bold_prefix="Determination Call: ")
    add_bullet("Technical Conditions Call: Notified developer of pure-generation feeder restrictions, mandatory System Impact Study routing for 3.0 MW, anticipated distribution line reconductoring and substation reverse-power upgrades, mandatory utility POI recloser (DPS-07/DIS-01), and mandatory utility RTU with live SCADA telemetry under TCS-02 §5.", bold_prefix="Conditions Call: ")
    add_bullet("Dialogue Call: Accepted. Pre-application technical conference scheduled within 10 business days to review project resizing options (≤800 kW vs. 3.0 MW).", bold_prefix="Dialogue Call: ")
    add_bullet("Document Filings: Official written response filed in the Program Office correspondence store as ALN-108_PreApplication_Response.docx.", bold_prefix="Filing Call: ")

    add_h2("4.3 Logging of Required Operational Follow-Up Actions")
    add_p("Pursuant to the user instruction ('log any follow-up the response requires there'), the DER Program Office has formally logged four specific follow-up actions arising from the disposition of Case #44:")

    # Table of Follow-Up Actions
    t_fup = doc.add_table(rows=5, cols=4)
    t_fup.alignment = WD_TABLE_ALIGNMENT.CENTER
    t_fup.autofit = False
    set_table_borders(t_fup, color="CBD5E0", sz="4")
    
    col_w_fup = [Inches(1.2), Inches(2.2), Inches(1.8), Inches(1.3)]
    headers_fup = ["Action Item", "Action Description & Scope", "Responsible Lead", "Target Milestone"]
    
    for idx, text in enumerate(headers_fup):
        cell = t_fup.rows[0].cells[idx]
        cell.width = col_w_fup[idx]
        set_cell_background(cell, "1A365D")
        set_cell_margins(cell, top=100, bottom=100, left=100, right=100)
        p = cell.paragraphs[0]
        p.paragraph_format.space_after = Pt(0)
        r = p.add_run(text)
        r.bold = True
        r.font.name = 'Arial'
        r.font.size = Pt(9)
        r.font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)
        
    rows_fup_data = [
        (
            "Follow-Up 1:\nExpedited Feeder Re-Study Request",
            "Submit formal engineering re-study request to Distribution Planning for Feeder ALN-108 under HCM Refresh Prioritization Criteria (earliest pending pre-app date 07/02/2025; requested 3.0 MW vs. 0.8 MW headroom; pure-generation weighting) per Tasking Memo §3.7.",
            "June Halloway (Distribution Planning) / Ivo Grantham (DER Planning)",
            "Initiate by 07/18/2025;\nComplete by 08/08/2025"
        ),
        (
            "Follow-Up 2:\nHosting Capacity Map Maintenance",
            "Queue Feeder ALN-108 for updated publication in the Q3 2025 Hosting Capacity Map refresh (HCM-2025-Q3) to correct the stale 3.0 MW figure and reflect active queue commitments (Grantwyck 1.2 MW, Cindermere 1.0 MW).",
            "June Halloway (Hosting Capacity Map Owner) / DER Program Office",
            "Q3 2025 Map Release\n(Prior to 09/10/2025)"
        ),
        (
            "Follow-Up 3:\nPre-Application Dialogue Administration",
            "Coordinate and convene technical pre-application scoping conference with Northline Renewables (Peter Ashford) and Distribution Planning; review single-line diagram, POI coordinates, and resizing options.",
            "DER Program Office Coordinator / Meera Vellanki",
            "Target Conference:\n07/28/2025 – 08/01/2025"
        ),
        (
            "Follow-Up 4:\nRegulatory Reporting & Backlog Integration",
            "Log Case #44 completion and ALN-108 capacity reconciliation in the weekly Friday backlog review progress report to Harriet Ngoyi (Regulatory Affairs) and Dana Whitcomb (VP) in support of 08/15 League response & 09/10 APUC briefing.",
            "DER Program Manager / Regulatory Affairs Liaison",
            "Friday Report:\n07/18/2025"
        )
    ]

    for r_idx, data in enumerate(rows_fup_data):
        row = t_fup.rows[r_idx + 1]
        bg_col = "FFFFFF" if r_idx % 2 == 0 else "F7FAFC"
        for c_idx, text in enumerate(data):
            cell = row.cells[c_idx]
            cell.width = col_w_fup[c_idx]
            set_cell_background(cell, bg_col)
            set_cell_margins(cell, top=80, bottom=80, left=100, right=100)
            p = cell.paragraphs[0]
            p.paragraph_format.space_after = Pt(0)
            p.paragraph_format.line_spacing = 1.15
            r = p.add_run(text)
            r.font.name = 'Calibri'
            r.font.size = Pt(9)
            if c_idx == 0:
                r.bold = True
                r.font.color.rgb = NAVY
            else:
                r.font.color.rgb = CHARCOAL

    doc.add_paragraph().paragraph_format.space_after = Pt(10)

    add_h2("4.4 Detailed Application of HCM Refresh Prioritization Criteria")
    add_p("In executing Follow-Up Item 1, the Program Office has evaluated Feeder ALN-108 against the published Refresh Prioritization Criteria set forth in the Title Block of HCM-2024-Q2. The criteria and their specific application to ALN-108 are as follows:")
    add_p("1. Earliest Pending Application Date: Under HCM-2024-Q2, feeders with the earliest pending pre-application or application date receive priority for re-study. Feeder ALN-108 carries an active queue addition dating to September 18, 2024 (Grantwyck Solar), a subsequent queue entry dating to February 6, 2025 (Cindermere Renewables), and a pending formal pre-application inquiry dating to July 2, 2025 (Northline Renewables). The presence of multiple active filings spanning ten months without a formal published map refresh places ALN-108 at the top tier of study priority.")
    add_p("2. Requested Capacity Relative to Published Available Headroom: Under HCM-2024-Q2, priority is accorded to feeders where the requested capacity is largest relative to currently available headroom. Northline's 3.0 MW request, combined with Grantwyck's 1.2 MW and Cindermere's 1.0 MW, represents an aggregate requested capacity of 5.2 MW against a feeder whose published baseline is 3.0 MW and whose remaining headroom is 0.8 MW. The ratio of requested capacity (3.0 MW) to estimated headroom (0.8 MW) is 3.75x (a 375% over-subscription), representing an extreme headroom deficit that requires immediate feeder modeling.")
    add_p("3. DER Category Weighting (Pure Generation vs. Net Metering): Under HCM-2024-Q2, pure-generation queue entries are weighted more heavily against feeder headroom than net-metering behind-the-meter entries at equivalent nameplate. Because ALN-108 is a Pure Generation feeder and all three post-baseline projects (Grantwyck, Cindermere, and Northline) are pure-generation facilities, the feeder receives the maximum category weighting factor.")
    add_p("Based on these three cumulative factors, Distribution Planning has been formally task-assigned to prioritize Feeder ALN-108 for an expedited full-feeder planning re-study prior to the August 15, 2025 League response deadline.")

    add_h2("4.5 Formal Case Closure Certification")
    add_p("All required determinations have been completed on the record with explicit basis; the formal written response to Northline Renewables LLC has been finalized; all operational follow-up actions have been logged into OpenProject tracking; and the response document has been filed in the Program Office's correspondence repository. In accordance with Program Office administrative rules:")
    add_bullet("Work Package #44 status is set to CLOSED (Status ID: 12).", bold_prefix="Status: ")
    add_bullet("Work Package #44 progress is set to 100% COMPLETE.", bold_prefix="Progress: ")
    add_bullet("Document filed as /filesystem/ALN-108_PreApplication_Response.docx and in document store at /DER_Program/Correspondence/ALN-108_PreApplication_Response.docx.", bold_prefix="Archival: ")
    add_bullet("Case closed effective July 14, 2025, by June Halloway, Distribution Planning Engineer, with concurrence of Meera Vellanki, Manager of Interconnection Studies.", bold_prefix="Sign-Off: ")

    doc.add_paragraph().paragraph_format.space_after = Pt(14)

    # Sign-off Block
    sign_table = doc.add_table(rows=2, cols=2)
    sign_table.alignment = WD_TABLE_ALIGNMENT.CENTER
    sign_table.autofit = False
    set_table_borders(sign_table, color="E2E8F0", sz="4")
    
    col_w_sign = [Inches(3.2), Inches(3.3)]
    for r in sign_table.rows:
        r.cells[0].width = col_w_sign[0]
        r.cells[1].width = col_w_sign[1]
        set_cell_margins(r.cells[0], top=100, bottom=100, left=120, right=120)
        set_cell_margins(r.cells[1], top=100, bottom=100, left=120, right=120)
        
    s0 = sign_table.rows[0].cells[0].paragraphs[0]
    s0.paragraph_format.space_after = Pt(2)
    r_s0 = s0.add_run("PREPARED AND SUBMITTED BY:\n\n/s/ June Halloway\n_________________________________________\nJune Halloway, Distribution Planning Engineer\nDistribution Planning, Alleniom Utilities\njune.halloway@alleniom.com | (612) 555-0105\nDate: July 14, 2025")
    r_s0.font.name = 'Calibri'
    r_s0.font.size = Pt(9.5)
    r_s0.font.color.rgb = CHARCOAL
    
    s1 = sign_table.rows[0].cells[1].paragraphs[0]
    s1.paragraph_format.space_after = Pt(2)
    r_s1 = s1.add_run("REVIEWED AND CONCURRED BY:\n\n/s/ Meera Vellanki\n_________________________________________\nMeera Vellanki, Manager, Interconnection Studies\nDER Program Office, Alleniom Utilities\nmeera.vellanki@alleniom.com | (612) 555-0102\nDate: July 14, 2025")
    r_s1.font.name = 'Calibri'
    r_s1.font.size = Pt(9.5)
    r_s1.font.color.rgb = CHARCOAL

    s2 = sign_table.rows[1].cells[0].paragraphs[0]
    s2.paragraph_format.space_after = Pt(2)
    r_s2 = s2.add_run("REGULATORY AFFAIRS OVERSIGHT:\n\n/s/ Harriet Ngoyi\n_________________________________________\nHarriet Ngoyi, Director, Regulatory Affairs\nAlleniom Utilities\nharriet.ngoyi@alleniom.com | (612) 555-0104\nDate: July 14, 2025")
    r_s2.font.name = 'Calibri'
    r_s2.font.size = Pt(9.5)
    r_s2.font.color.rgb = CHARCOAL

    s3 = sign_table.rows[1].cells[1].paragraphs[0]
    s3.paragraph_format.space_after = Pt(2)
    r_s3 = s3.add_run("EXECUTIVE SPONSORSHIP:\n\n/s/ Dana Whitcomb\n_________________________________________\nDana Whitcomb, VP, Distribution Operations\nAlleniom Utilities\ndana.whitcomb@alleniom.com | (612) 555-0101\nDate: July 14, 2025")
    r_s3.font.name = 'Calibri'
    r_s3.font.size = Pt(9.5)
    r_s3.font.color.rgb = CHARCOAL

    # Output paths
    out_path_main = "/filesystem/ALN-108_PreApplication_Response.docx"
    out_path_corr = "/filesystem/Correspondence/ALN-108_PreApplication_Response.docx"
    
    doc.save(out_path_main)
    doc.save(out_path_corr)
    print(f"Successfully generated and saved document to:")
    print(f"  - {out_path_main}")
    print(f"  - {out_path_corr}")

if __name__ == "__main__":
    create_document()
