import os
import sys
import docx
from docx import Document
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_TAB_ALIGNMENT
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL
from docx.oxml import OxmlElement, parse_xml
from docx.oxml.ns import nsdecls, qn

def generate_memo():
    template_path = 'Thelbridge_Verification_Memo_TEMPLATE_v1.docx'
    output_path = 'Thelbridge_Verification_Memo_Item051_BlockC.docx'
    
    doc = Document(template_path)
    
    def style_cell(cell, text, bold=False, italic=False, size_pt=8.5, color_rgb=(0,0,0), align=WD_ALIGN_PARAGRAPH.LEFT, bg_color=None, top_m=70, bot_m=70, left_m=110, right_m=110):
        tcPr = cell._element.get_or_add_tcPr()
        if bg_color:
            shd = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{bg_color}"/>')
            tcPr.append(shd)
        tcMar = parse_xml(f'<w:tcMar {nsdecls("w")}><w:top w:w="{top_m}" w:type="dxa"/><w:bottom w:w="{bot_m}" w:type="dxa"/><w:left w:w="{left_m}" w:type="dxa"/><w:right w:w="{right_m}" w:type="dxa"/></w:tcMar>')
        tcPr.append(tcMar)
        cell.vertical_alignment = WD_ALIGN_VERTICAL.CENTER
        p = cell.paragraphs[0]
        p.alignment = align
        p.paragraph_format.space_before = Pt(0)
        p.paragraph_format.space_after = Pt(0)
        p.paragraph_format.line_spacing = 1.12
        p.text = ""
        run = p.add_run(text)
        run.font.name = 'Calibri'
        run.font.size = Pt(size_pt)
        run.bold = bold
        run.italic = italic
        if color_rgb:
            run.font.color.rgb = RGBColor(*color_rgb)
        return p

    def set_table_borders(table, color="D3D3D3", sz="4", val="single"):
        tblPr = table._element.xpath('w:tblPr')
        if tblPr:
            borders = parse_xml(
                f'<w:tblBorders {nsdecls("w")}>'
                f'  <w:top w:val="{val}" w:sz="{sz}" w:space="0" w:color="{color}"/>'
                f'  <w:bottom w:val="{val}" w:sz="{sz}" w:space="0" w:color="{color}"/>'
                f'  <w:insideH w:val="{val}" w:sz="{sz}" w:space="0" w:color="{color}"/>'
                f'  <w:insideV w:val="none"/>'
                f'  <w:left w:val="none"/>'
                f'  <w:right w:val="none"/>'
                f'</w:tblBorders>'
            )
            tblPr[0].append(borders)

    # 1. Update Memo Header Fields (P3, P4, P5, P6 and add Cc)
    # P3: To
    p3 = doc.paragraphs[3]
    p3.text = ""
    p3.paragraph_format.space_before = Pt(0)
    p3.paragraph_format.space_after = Pt(2)
    p3.paragraph_format.line_spacing = 1.15
    p3.paragraph_format.tab_stops.clear_all()
    p3.paragraph_format.tab_stops.add_tab_stop(Inches(0.85), WD_TAB_ALIGNMENT.LEFT)
    r = p3.add_run("To:\t")
    r.font.name = 'Calibri'
    r.font.size = Pt(10.0)
    r.bold = True
    r = p3.add_run("Adrian Vance, Project Engineer (Structural/Geotechnical), Thelbridge Project Management Services")
    r.font.name = 'Calibri'
    r.font.size = Pt(10.0)

    # P4: From
    p4 = doc.paragraphs[4]
    p4.text = ""
    p4.paragraph_format.space_before = Pt(0)
    p4.paragraph_format.space_after = Pt(2)
    p4.paragraph_format.line_spacing = 1.15
    p4.paragraph_format.tab_stops.clear_all()
    p4.paragraph_format.tab_stops.add_tab_stop(Inches(0.85), WD_TAB_ALIGNMENT.LEFT)
    r = p4.add_run("From:\t")
    r.font.name = 'Calibri'
    r.font.size = Pt(10.0)
    r.bold = True
    r = p4.add_run("Rahul Nimkar, Geotechnical Reviewer, Thelbridge Project Management Services")
    r.font.name = 'Calibri'
    r.font.size = Pt(10.0)

    # Insert Cc before Date (P5)
    p_cc = doc.paragraphs[5].insert_paragraph_before()
    p_cc.paragraph_format.space_before = Pt(0)
    p_cc.paragraph_format.space_after = Pt(2)
    p_cc.paragraph_format.line_spacing = 1.15
    p_cc.paragraph_format.tab_stops.clear_all()
    p_cc.paragraph_format.tab_stops.add_tab_stop(Inches(0.85), WD_TAB_ALIGNMENT.LEFT)
    r = p_cc.add_run("Cc:\t")
    r.font.name = 'Calibri'
    r.font.size = Pt(10.0)
    r.bold = True
    r = p_cc.add_run("Rachel Marlbeck, University Program Director, Thornbury State University")
    r.font.name = 'Calibri'
    r.font.size = Pt(10.0)

    # P5: Date
    p5 = doc.paragraphs[6] # shifted by 1 due to p_cc insertion
    p5.text = ""
    p5.paragraph_format.space_before = Pt(0)
    p5.paragraph_format.space_after = Pt(2)
    p5.paragraph_format.line_spacing = 1.15
    p5.paragraph_format.tab_stops.clear_all()
    p5.paragraph_format.tab_stops.add_tab_stop(Inches(0.85), WD_TAB_ALIGNMENT.LEFT)
    r = p5.add_run("Date:\t")
    r.font.name = 'Calibri'
    r.font.size = Pt(10.0)
    r.bold = True
    r = p5.add_run("July 20, 2026")
    r.font.name = 'Calibri'
    r.font.size = Pt(10.0)

    # P6: Subject
    p6 = doc.paragraphs[7]
    p6.text = ""
    p6.paragraph_format.space_before = Pt(0)
    p6.paragraph_format.space_after = Pt(12)
    p6.paragraph_format.line_spacing = 1.15
    p6.paragraph_format.tab_stops.clear_all()
    p6.paragraph_format.tab_stops.add_tab_stop(Inches(0.85), WD_TAB_ALIGNMENT.LEFT)
    r = p6.add_run("Subject:\t")
    r.font.name = 'Calibri'
    r.font.size = Pt(10.0)
    r.bold = True
    r = p6.add_run("Package A Verification Register — Item 051: Block C Spread Footings and Long-Term Clay Settlement Verification")
    r.font.name = 'Calibri'
    r.font.size = Pt(10.0)

    # Locate Section Headings and Sign-off
    p_sec1 = None
    p_sec2 = None
    p_sec3 = None
    p_sec4 = None
    p_sec5 = None
    p_name = None
    p_title = None
    p_org = None
    p_date = None

    for p in doc.paragraphs:
        txt = p.text.strip()
        if "1.  PURPOSE" in txt:
            p_sec1 = p
        elif "2.  DOCUMENTS REVIEWED" in txt:
            p_sec2 = p
        elif "3.  BASIS OF REVIEW" in txt:
            p_sec3 = p
        elif "4.  FINDINGS" in txt:
            p_sec4 = p
        elif "5.  CONCLUSION AND RECOMMENDATION" in txt:
            p_sec5 = p
        elif txt == "Name":
            p_name = p
        elif txt == "Title":
            p_title = p
        elif "Thelbridge Project Management Services - Owner's Representative" in txt:
            p_org = p
        elif txt == "Date":
            p_date = p

    def add_p(target_p, runs_data, space_before=0, space_after=4.5, line_spacing=1.15, align=WD_ALIGN_PARAGRAPH.LEFT, bullet=False):
        p = target_p.insert_paragraph_before()
        p.alignment = align
        p.paragraph_format.space_before = Pt(space_before)
        p.paragraph_format.space_after = Pt(space_after)
        p.paragraph_format.line_spacing = line_spacing
        if bullet:
            p.paragraph_format.left_indent = Inches(0.25)
        for r_data in runs_data:
            text = r_data[0]
            bold = r_data[1] if len(r_data) > 1 else False
            italic = r_data[2] if len(r_data) > 2 else False
            size_pt = r_data[3] if len(r_data) > 3 else 10.0
            color_rgb = r_data[4] if len(r_data) > 4 else None
            run = p.add_run(text)
            run.font.name = 'Calibri'
            run.font.size = Pt(size_pt)
            run.bold = bold
            run.italic = italic
            if color_rgb:
                run.font.color.rgb = RGBColor(*color_rgb)
        return p

    def add_heading_sub(target_p, text, space_before=8, space_after=3):
        return add_p(target_p, [(text, True, False, 10.0, (31, 78, 121))], space_before=space_before, space_after=space_after)

    def remove_between(p_start, p_end):
        curr = p_start._element.getnext()
        while curr is not None and curr != p_end._element:
            nxt = curr.getnext()
            curr.getparent().remove(curr)
            curr = nxt

    # ==========================================
    # SECTION 1: PURPOSE
    # ==========================================
    remove_between(p_sec1, p_sec2)
    
    add_p(p_sec2, [
        ("This verification memorandum addresses ", False),
        ("Item 051", True),
        (" on the ", False),
        ("Thelbridge Review Comment and Verification Register — Package A", True),
        (" for the Birchwood Village Expansion Program. Item 051 is formally assigned to Rahul Nimkar, Geotechnical Reviewer, and falls due on July 20, 2026. This review occurs exactly two days prior to the scheduled Level-3 concrete placement on July 22, 2026 at 0530, which constitutes a contractual hold-point established at Notice to Proceed and reinforced by the Thornbury State University Owner Directive issued by Rachel Marlbeck on July 6, 2026.", False)
    ], space_before=4, space_after=5)

    add_p(p_sec2, [
        ("The purpose of this memorandum is to provide an authoritative geotechnical determination of the adequacy and long-term serviceability of the spread footing foundations supporting ", False),
        ("Block C", True),
        (" (columns C-1 through C-12, residential housing block over shared podium, drawing sheets S-101 and S-201) founded on the upper sand stratum directly overlying an 18-ft thick compressible clay aquitard (Stratum 2, CL clay, El. 738.0 to El. 720.0). Specifically, this memorandum determines:", False)
    ], space_before=2, space_after=4)

    add_p(p_sec2, [
        ("1.  Completeness and Technical Validity of EOR Calculations: ", True),
        ("Whether Foundation Settlement Calculation CB-GEO-007 (Rev.0, dated 09/30/2025), prepared and sealed by Gregory Nash, PE (Calloway Braddock Structural Engineers, LLC, Structural Engineer of Record), completely and accurately evaluates the total and differential serviceability settlement of the Block C spread footings, with particular focus on the primary consolidation contribution of the underlying normally consolidated Stratum 2 CL clay.", False)
    ], space_before=2, space_after=3, bullet=True)

    add_p(p_sec2, [
        ("2.  Compliance with Project Serviceability Limits: ", True),
        ("Whether the computed foundation settlements satisfy the strict serviceability criteria specified in Specification Section 31 20 00 Article 3.6.A and Design Basis Memorandum Rev.2 Section 7.3—namely, a maximum allowable total settlement of 1.0 inch, a maximum allowable differential settlement of 0.5 inch over 30 ft, and an angular distortion threshold of 1/500.", False)
    ], space_before=2, space_after=3, bullet=True)

    add_p(p_sec2, [
        ("3.  Correlation and Reconciliation with Field Monitoring: ", True),
        ("Whether empirical settlement measurements compiled through Round 15 (June 26, 2026) in Document SM-BLKC-2026-Rev14—recording a cumulative settlement of 0.61 inches at interior column footing MP-7 (FTG-C7)—correlate with theoretical soil mechanics, and whether the observed rate of settlement indicates ongoing, unabated primary consolidation.", False)
    ], space_before=2, space_after=3, bullet=True)

    add_p(p_sec2, [
        ("4.  Contractual Disposition and Hold-Point Impact: ", True),
        ("The definitive disposition of Register Item 051, the identification of all engineering deliverables and site actions required prior to closure, the assignment of responsibility for each deliverable, and the relationship between this item and the Level-3 concrete placement on July 22, 2026.", False)
    ], space_before=2, space_after=6, bullet=True)

    # ==========================================
    # SECTION 2: DOCUMENTS REVIEWED
    # ==========================================
    remove_between(p_sec2, p_sec3)

    add_p(p_sec3, [
        ("This technical evaluation is based upon an exhaustive review of the design calculations, geotechnical site investigation reports, laboratory testing certificates, field survey records, contract specifications, and official project correspondence. Table 2-1 itemizes the primary project documents relied upon:", False)
    ], space_before=4, space_after=6)

    tbl_docs = doc.add_table(rows=15, cols=5)
    tbl_docs.alignment = WD_TABLE_ALIGNMENT.CENTER
    set_table_borders(tbl_docs)
    col_widths = [Inches(0.5), Inches(1.3), Inches(2.5), Inches(1.6), Inches(0.85)]
    doc_headers = ["Item", "Doc Identifier", "Document Title & Scope", "Authoring Entity / Certifier", "Date"]
    for j, h in enumerate(doc_headers):
        cell = tbl_docs.cell(0, j)
        cell.width = col_widths[j]
        style_cell(cell, h, bold=True, size_pt=8.5, color_rgb=(255,255,255), align=WD_ALIGN_PARAGRAPH.CENTER, bg_color="1F4E79")

    doc_data = [
        ("1", "CB-GEO-007 Rev.0", "Block C Spread Footing Settlement (Calculation Sheet)", "Calloway Braddock (G. Nash, PE / M. Halbrook, PE)", "09/30/2025"),
        ("2", "KGI-2024-0417 Rev.2", "Geotechnical Investigation Report — Package A", "Kelbrook Geotechnical, Inc. (A. Roscombe, PE)", "02/14/2025"),
        ("3", "VMT-2025-0109-CON", "Laboratory Consolidation Test Report (ASTM D2435)", "Vantree Materials Testing, LLC (T. Brennard, PE)", "01/09/2025"),
        ("4", "VMT-2024-0917-INDEX", "Geotechnical Laboratory Index Test Data — Package A", "Vantree Materials Testing, LLC (T. Brennard, PE)", "01/09/2025"),
        ("5", "B-01 to B-09 Logs", "Boring Logs & Groundwater Monitoring Record", "Kelbrook Geotechnical, Inc. (A. Roscombe, PE)", "11/22/2024 – 06/28/2026"),
        ("6", "Spec 31 20 00 Rev.3", "Project Specification Section 31 20 00, 'Earth Moving'", "Calloway Braddock Structural Engineers, LLC", "03/06/2026"),
        ("7", "CB-DBM-001 Rev.2", "Design Basis Memorandum — Birchwood Village, Package A", "Calloway Braddock (G. Nash, PE)", "11/14/2025"),
        ("8", "SM-BLKC-2026-Rev14", "Settlement Monitoring Records — Block C (Rounds 1–15)", "Rowan Bay Constructors (D. Halloran, PLS)", "12/12/2025 – 06/26/2026"),
        ("9", "Sheet S-101 Rev.4", "Foundation Plan — Blocks A / B / C", "Calloway Braddock (G. Nash, PE)", "05/29/2026"),
        ("10", "Sheet S-201 Rev.4", "Foundation Sections and Details (Detail 3/S-201)", "Calloway Braddock (G. Nash, PE)", "05/29/2026"),
        ("11", "Verification Register", "Thelbridge Review Comment and Verification Register", "Thelbridge Project Management Services (A. Vance)", "Last updated 07/15/2026"),
        ("12", "Meeting Minutes No. 26", "Progress Meeting Minutes No. 26 (Progress Meeting 07/09)", "Thelbridge Project Management Services (A. Vance)", "07/10/2026"),
        ("13", "Monthly Report No. 14", "Monthly Progress Report No. 14 — June 2026", "Thelbridge Project Management Services (A. Vance)", "07/06/2026"),
        ("14", "Owner Directive", "Written Verification Required Before Permanent Work", "Thornbury State University (R. Marlbeck)", "07/06/2026")
    ]

    for i, row in enumerate(doc_data):
        bg = "F9FAFB" if i % 2 == 1 else "FFFFFF"
        for j, val in enumerate(row):
            cell = tbl_docs.cell(i+1, j)
            cell.width = col_widths[j]
            align = WD_ALIGN_PARAGRAPH.CENTER if j in [0, 4] else WD_ALIGN_PARAGRAPH.LEFT
            style_cell(cell, val, bold=(j==1), size_pt=8.0, color_rgb=(0,0,0), align=align, bg_color=bg)

    p_sec3._p.addprevious(tbl_docs._element)
    # removed empty p

    # ==========================================
    # SECTION 3: BASIS OF REVIEW
    # ==========================================
    remove_between(p_sec3, p_sec4)

    add_p(p_sec4, [
        ("The geotechnical review of Item 051 was performed against the governing contractual specifications, structural design criteria, geotechnical report recommendations, and applicable building codes and engineering standards:", False)
    ], space_before=4, space_after=4)

    add_p(p_sec4, [
        ("1.  Specification Section 31 20 00 ('Earth Moving', Rev.3), Article 3.6 — Settlement Tolerance:", True)
    ], space_before=3, space_after=2)
    add_p(p_sec4, [
        ("•  ", False),
        ("Article 3.6.A (Total and Differential Settlement Limits): ", True),
        ("Governs allowable foundation movements, mandating: 'Total settlement 1.0 in maximum; differential settlement 0.5 in maximum over 30 ft.'", False)
    ], space_before=1, space_after=2, bullet=True)
    add_p(p_sec4, [
        ("•  ", False),
        ("Article 3.6.B (Application and Mandatory Load Suspension): ", True),
        ("Establishes that tolerances apply to the completed foundation system and imposes a mandatory stop-work trigger: 'The tolerances of Paragraph A apply to the completed foundation system as constructed on the accepted subgrade and structural fill delivered under this Section. Where predicted or monitored settlements exceed the tolerances of Paragraph A, the Structural Engineer of Record shall be notified in writing and no additional load shall be applied until a written disposition is issued.'", False)
    ], space_before=1, space_after=2, bullet=True)
    add_p(p_sec4, [
        ("•  ", False),
        ("Article 3.6.C (Monitoring and Immediate Reporting): ", True),
        ("Requires field verification: 'Where settlement monitoring points are shown on the Drawings, readings shall be taken and transmitted to the Owner's Representative Engineer at the frequency indicated. Cumulative settlement approaching either tolerance of Paragraph A shall be reported immediately.'", False)
    ], space_before=1, space_after=4, bullet=True)

    add_p(p_sec4, [
        ("2.  Design Basis Memorandum Rev.2 (CB-DBM-001, 11/14/2025), Section 7.3 & Section 8:", True)
    ], space_before=3, space_after=2)
    add_p(p_sec4, [
        ("•  ", False),
        ("Section 7.3 (Shallow Foundations — Block C): ", True),
        ("Defines the Block C structural support system as isolated spread footings founded on Stratum 1 sand (SP-SM) above the compressible CL clay layer. Explicitly establishes that bearing capacity is evaluated under strength-level ASD load combinations (allowable bearing pressure 4,000 psf net per Section 9), and settlement is evaluated under service-level load combinations against the tolerances of Spec 31 20 00 Article 3.6 (1.0 in total, 0.5 in differential). Section 7.3 specifically cites calculation CB-GEO-007 as the governing settlement justification.", False)
    ], space_before=1, space_after=2, bullet=True)
    add_p(p_sec4, [
        ("•  ", False),
        ("Section 8.1 & 8.2 (Serviceability & Deflection Limits): ", True),
        ("Governs serviceability behavior under sustained loads and incorporates ACI 318-19 and AISC Design Guide 3 criteria.", False)
    ], space_before=1, space_after=4, bullet=True)

    add_p(p_sec4, [
        ("3.  Geotechnical Investigation Report Rev.2 (Kelbrook Geotechnical, Project KGI-2024-0417, 02/14/2025):", True)
    ], space_before=3, space_after=2)
    add_p(p_sec4, [
        ("•  ", False),
        ("Section 8.1 (Consolidation of the Clay Aquitard): ", True),
        ("Establishes that the 18-ft thick Stratum 2 CL clay layer (El. 738.0 to El. 720.0) is normally consolidated (OCR ≈ 1.03; preconsolidation pressure σ'p = 1,900 psf vs. in-situ effective overburden σ'0 = 1,850 psf at mid-depth El. 729.0). Mandates that because σ'p exceeds σ'0 by only ~50 psf, any net stress increase q exceeding 50 psf produces virgin one-dimensional consolidation settlement along the virgin compression slope (Cc = 0.28):", False)
    ], space_before=1, space_after=2, bullet=True)
    add_p(p_sec4, [
        ("Sc = [Cc · H / (1 + e0)] · log10[ (σ'0 + q) / σ'0 ]", True, False, 10.0, (31, 78, 121))
    ], space_before=2, space_after=2, align=WD_ALIGN_PARAGRAPH.CENTER)
    add_p(p_sec4, [
        ("•  ", False),
        ("Section 9.1 (Block C — Spread Footings): ", True),
        ("Directs the Structural Engineer of Record in explicit terms: 'Design bearing pressures must be evaluated against both bearing capacity (of the upper sand) and against consolidation settlement of the underlying clay. Because the clay is normally-consolidated, the Structural Engineer of Record must explicitly compute consolidation settlement of the clay under the stress increase q at mid-depth of the clay caused by each governing footing, using the parameters in Table 5-1; The computed settlement must be reconciled against the total-and-differential settlement tolerances specified in the project structural criteria; If computed settlement exceeds tolerance, footing sizes may be adjusted to reduce the stress increase, footings may be combined into a mat, or a deep-foundation alternative may be considered.'", False)
    ], space_before=1, space_after=4, bullet=True)

    add_p(p_sec4, [
        ("4.  Building Codes and Structural Serviceability Standards:", True)
    ], space_before=3, space_after=2)
    add_p(p_sec4, [
        ("•  ", False),
        ("Ohio Building Code (IBC 2021) Chapter 18: ", True),
        ("Governs allowable foundation bearing and mandates that total and differential settlements do not cause structural distress, instability, or loss of serviceability.", False)
    ], space_before=1, space_after=2, bullet=True)
    add_p(p_sec4, [
        ("•  ", False),
        ("AISC Design Guide 3 / Bjerrum (1963) Serviceability Criteria: ", True),
        ("Establishes the limiting angular distortion threshold of δ/L ≤ 1/500 for framed buildings supporting unreinforced partitions (e.g., CMU and gypsum per Spec 09 21 16) to prevent visible partition cracking, binding of openings, and secondary framing stresses.", False)
    ], space_before=1, space_after=2, bullet=True)
    add_p(p_sec4, [
        ("•  ", False),
        ("ASTM D2435 / D2435M: ", True),
        ("Standard test method governing one-dimensional incremental consolidation testing and parameter determination.", False)
    ], space_before=1, space_after=6, bullet=True)

    # ==========================================
    # SECTION 4: FINDINGS
    # ==========================================
    remove_between(p_sec4, p_sec5)

    # FINDING 1
    add_heading_sub(p_sec5, "Finding 1: Incomplete Design Calculation in CB-GEO-007 — Complete Omission of Primary Clay Consolidation Settlement", space_before=4, space_after=3)
    add_p(p_sec5, [
        ("Citation: ", True),
        ("Calloway Braddock Calculation CB-GEO-007 Rev.0, Cover Sheet (p. 1), Sheet 2 (p. 2), Sheet 3 (p. 3), Sheet 4 (p. 4), and Sheet 5 (p. 5); Kelbrook GIR Rev.2 §8.1 & §9.1; CB-DBM-001 Rev.2 §7.3.", False)
    ], space_before=0, space_after=3)
    add_p(p_sec5, [
        ("In Calculation CB-GEO-007 (Rev.0, sealed 09/30/2025 by Gregory Nash, PE), the Structural Engineer of Record evaluated the serviceability settlement of Block C spread footings (F-C1 through F-C12) ", False),
        ("solely and exclusively on the basis of immediate (elastic) settlement", True),
        (" using the Schmertmann strain-influence factor method (Sheet 3). Under Sheet 3, the EOR computed immediate settlements ranging from 0.70 inches at corner footing F-C12 to 0.90 inches at interior footing F-C6 (10.5 ft × 10.5 ft footing, net bearing pressure q_net = 3,730 psf), with a computed maximum differential immediate settlement of 0.20 inches (utilization 0.90 / 1.0 = 90% and 0.20 / 0.5 = 40%). On Sheet 3 (Row 70), the EOR concluded: 'Immediate elastic settlement of Block C spread footings computed by the Schmertmann method yields a maximum total settlement of 0.9 in and a maximum differential of 0.2 in between adjacent footings. Both values lie within the 1.0 in total / 0.5 in differential tolerance... Block C spread footing serviceability — SATISFACTORY.'", False)
    ], space_before=2, space_after=3)
    add_p(p_sec5, [
        ("However, a direct examination of Sheet 4 ('Sheet 4 — Consolidation: Long-Term Settlement Contribution — Stratum 2 CL Clay') reveals a critical, fatal deficiency: ", False),
        ("every single line item for consolidation settlement was left blank or dashed out ('—').", True),
        (" In Row 15 of Sheet 4, the EOR explicitly typed: ", False),
        ("'Not computed. Serviceability taken from the immediate settlement result on Sheet 3.'", True, True),
        (" Furthermore, on Sheet 5, while the EOR transcribed the laboratory consolidation test parameters from Vantree Report VMT-2025-0109-CON (Cc = 0.28, Cr = 0.045, e0 = 0.92, σ'p = 1,900 psf), he appended a dismissive note in Row 21 stating: '(Parameters listed here for the record and to close out the transmittal from the Vantree laboratory report. Governing serviceability check is presented on Sheet 3.)'", False)
    ], space_before=2, space_after=3)
    add_p(p_sec5, [
        ("Technical Evaluation: ", True),
        ("This omission is an egregious engineering error that renders Calculation CB-GEO-007 fundamentally invalid. The Schmertmann method calculates only the instantaneous elastic distortion within granular soils (Stratum 1 sand). It does not, and cannot, model hydrodynamic primary consolidation settlement of saturated fine-grained soils. Stratum 2 is an 18-ft thick saturated clay aquitard lying merely 2.5 ft beneath the footing bearing level. Leaving Sheet 4 uncalculated directly violates the explicit instructions of Kelbrook GIR Rev.2 Section 8.1 and Section 9.1, and breaches the contractual design basis set forth in DBM Rev.2 Section 7.3.", False)
    ], space_before=2, space_after=6)

    # FINDING 2
    add_heading_sub(p_sec5, "Finding 2: Independent Geotechnical Consolidation Settlement Analysis and Mathematical Working", space_before=6, space_after=3)
    add_p(p_sec5, [
        ("Citation: ", True),
        ("Kelbrook GIR Rev.2 §8.1 & §9.1 (pp. 14–16); Vantree Laboratory Report VMT-2025-0109-CON (p. 4); Vantree Index Test Data (Summary Sheet); CB-GEO-007 Sheets 2 & 5; Drawings S-101 and S-201.", False)
    ], space_before=0, space_after=3)
    add_p(p_sec5, [
        ("To determine the actual serviceability performance of the Block C spread footings, an independent one-dimensional consolidation analysis was executed applying Terzaghi 1D consolidation theory, the project stratigraphy, and the ASTM D2435 laboratory parameters. Table 4-1 summarizes the geotechnical baseline established for Stratum 2:", False)
    ], space_before=2, space_after=4)

    tbl_geo = doc.add_table(rows=11, cols=4)
    tbl_geo.alignment = WD_TABLE_ALIGNMENT.CENTER
    set_table_borders(tbl_geo)
    col_w_geo = [Inches(1.8), Inches(1.1), Inches(1.3), Inches(2.55)]
    geo_headers = ["Parameter", "Symbol", "Design Value", "Source / Derivation Basis"]
    for j, h in enumerate(geo_headers):
        cell = tbl_geo.cell(0, j)
        cell.width = col_w_geo[j]
        style_cell(cell, h, bold=True, size_pt=8.5, color_rgb=(255,255,255), align=WD_ALIGN_PARAGRAPH.CENTER, bg_color="1F4E79")

    geo_data = [
        ("Existing Grade / Footing Base", "El. / D_f", "El. 750.0 / El. 740.5", "Sheet S-101 Rev.4; CB-GEO-007 Sheet 2 (~2.5 ft above clay)"),
        ("Stratum 2 Clay Elevation Range", "Top – Bot", "El. 738.0 – El. 720.0", "Kelbrook GIR Rev.2 Table 6-1; Borings B-01, B-06, B-08, B-09"),
        ("Compressible Layer Thickness", "H", "18.0 ft (216 in)", "Stratum 2 aquitard thickness across Block C footprint"),
        ("Design Water Table Elevation", "El_gw", "El. 742.0 ft", "Kelbrook GIR Rev.2 Section 7.1; shallow standpipe array"),
        ("Total Unit Weights (Sand / Clay)", "γ_sand / γ_clay", "118 pcf / 120 pcf", "Vantree Index Test Data (Summary Sheet); ASTM D7263"),
        ("Effective Overburden at Mid-Clay", "σ'0", "1,850 psf", "El. 729.0 mid-layer effective stress (GIR §8.1; VMT report)"),
        ("Preconsolidation Pressure", "σ'p", "1,900 psf", "Vantree Report VMT-2025-0109-CON (Casagrande; B-06 U3, B-08 U2)"),
        ("Overconsolidation Ratio", "OCR", "1.027 ≈ 1.03", "OCR = σ'p / σ'0 = 1,900 / 1,850 (essentially normally consolidated)"),
        ("Virgin Compression Index", "Cc", "0.28", "ASTM D2435 virgin slope (B-06 U3 = 0.280; B-08 U2 = 0.281)"),
        ("Recompression Index / Void Ratio", "Cr / e0", "0.045 / 0.92", "Rebound slope Cr = 0.045; initial void ratio e0 = 0.92 (both tests)")
    ]

    for i, row in enumerate(geo_data):
        bg = "F9FAFB" if i % 2 == 1 else "FFFFFF"
        for j, val in enumerate(row):
            cell = tbl_geo.cell(i+1, j)
            cell.width = col_w_geo[j]
            align = WD_ALIGN_PARAGRAPH.CENTER if j in [1, 2] else WD_ALIGN_PARAGRAPH.LEFT
            style_cell(cell, val, bold=(j==0), size_pt=8.0, color_rgb=(0,0,0), align=align, bg_color=bg)

    p_sec5._p.addprevious(tbl_geo._element)
    # removed empty p

    add_p(p_sec5, [
        ("Mathematical Working — 1D Primary Consolidation Settlement:", True)
    ], space_before=2, space_after=2)

    add_p(p_sec5, [
        ("From CB-GEO-007 Sheet 2 (Rows 40–41), the net vertical stress increase imposed at the mid-depth of Stratum 2 clay (El. 729.0 ft) by the combined service dead and live loads of adjacent spread footings is ", False),
        ("Δσ = 900 psf", True),
        (" (calculated via Boussinesq superposition of four adjacent footings at grid center). The final vertical effective stress in the clay is therefore: ", False),
        ("σ'f = σ'0 + Δσ = 1,850 + 900 = 2,750 psf", True),
        (". Because σ'f (2,750 psf) substantially exceeds the preconsolidation pressure σ'p (1,900 psf), the clay is forced deep into virgin compression along the Cc slope.", False)
    ], space_before=1, space_after=3)

    add_p(p_sec5, [
        ("Working 2A: Standard Virgin Consolidation Settlement (Kelbrook GIR §8.1 Formula):", True)
    ], space_before=2, space_after=2)
    add_p(p_sec5, [
        ("Because the net stress increase Δσ (900 psf) is 18 times larger than the small preconsolidation margin (σ'p − σ'0 = 50 psf), virgin compression governs almost the entire loading increment. Applying the standard one-dimensional consolidation formulation defined in Kelbrook GIR Section 8.1:", False)
    ], space_before=1, space_after=2)
    add_p(p_sec5, [
        ("Sc = [Cc · H / (1 + e0)] · log10[ (σ'0 + Δσ) / σ'0 ]", True, False, 10.0, (31, 78, 121))
    ], space_before=2, space_after=2, align=WD_ALIGN_PARAGRAPH.CENTER)
    add_p(p_sec5, [
        ("Sc = [0.28 · (18 ft × 12 in/ft) / (1 + 0.92)] · log10[ (1,850 + 900) / 1,850 ]", False)
    ], space_before=1, space_after=1, align=WD_ALIGN_PARAGRAPH.CENTER)
    add_p(p_sec5, [
        ("Sc = [0.28 · 216 in / 1.92] · log10[ 2,750 / 1,850 ] = [60.48 / 1.92] · log10(1.486486)", False)
    ], space_before=1, space_after=1, align=WD_ALIGN_PARAGRAPH.CENTER)
    add_p(p_sec5, [
        ("Sc = 31.50 in · 0.172163 = ", False),
        ("5.423 inches (0.452 ft)", True, False, 10.0, (192, 0, 0))
    ], space_before=1, space_after=3, align=WD_ALIGN_PARAGRAPH.CENTER)
    add_p(p_sec5, [
        ("Note: This computed value of 5.42 in aligns precisely with Kelbrook GIR Table 8-1 ('Sensitivity of Computed Consolidation Settlement'), which benchmarks Sc = 5.9 in for q = 1,000 psf and Sc = 3.8 in for q = 600 psf.", False, True)
    ], space_before=1, space_after=3)

    add_p(p_sec5, [
        ("Working 2B: Two-Part Consolidation Settlement (Recompression + Virgin Compression):", True)
    ], space_before=2, space_after=2)
    add_p(p_sec5, [
        ("Evaluating the recompression increment between σ'0 (1,850 psf) and σ'p (1,900 psf) separately from the virgin compression increment between σ'p (1,900 psf) and σ'f (2,750 psf):", False)
    ], space_before=1, space_after=2)
    add_p(p_sec5, [
        ("•  Recompression Portion (σ'0 = 1,850 psf to σ'p = 1,900 psf):", False),
        ("\n   Sc,recomp = [Cr · H / (1 + e0)] · log10(σ'p / σ'0) = [0.045 · 216 / 1.92] · log10(1,900 / 1,850) = 5.0625 · 0.011581 = 0.059 in.", False)
    ], space_before=1, space_after=2)
    add_p(p_sec5, [
        ("•  Virgin Compression Portion (σ'p = 1,900 psf to σ'f = 2,750 psf):", False),
        ("\n   Sc,virgin = [Cc · H / (1 + e0)] · log10(σ'f / σ'p) = [0.28 · 216 / 1.92] · log10(2,750 / 1,900) = 31.50 · 0.160579 = 5.058 in.", False)
    ], space_before=1, space_after=2)
    add_p(p_sec5, [
        ("•  Total Primary Consolidation Settlement: ", True),
        ("Sc = Sc,recomp + Sc,virgin = 0.059 in + 5.058 in = ", False),
        ("5.117 inches (~5.12 inches)", True, False, 10.0, (192, 0, 0))
    ], space_before=1, space_after=3)

    add_p(p_sec5, [
        ("Working 2C: Total Predicted Settlement and Comparison to Tolerances:", True)
    ], space_before=2, space_after=2)
    add_p(p_sec5, [
        ("The total long-term settlement is the sum of immediate elastic settlement (Si) and primary clay consolidation settlement (Sc):", False)
    ], space_before=1, space_after=2)
    add_p(p_sec5, [
        ("S_total = Si + Sc = 0.90 in (immediate) + 5.12 to 5.42 in (consolidation) = ", False),
        ("6.02 to 6.32 inches", True, False, 10.5, (192, 0, 0))
    ], space_before=1, space_after=3, align=WD_ALIGN_PARAGRAPH.CENTER)

    tbl_comp = doc.add_table(rows=4, cols=6)
    tbl_comp.alignment = WD_TABLE_ALIGNMENT.CENTER
    set_table_borders(tbl_comp)
    col_w_comp = [Inches(1.5), Inches(1.1), Inches(1.1), Inches(1.0), Inches(1.0), Inches(1.05)]
    comp_headers = ["Serviceability Parameter", "EOR Computed (CB-GEO-007)", "True Predicted Value", "Spec 31 20 00 Tolerance", "Utilization Ratio", "Compliance Check"]
    for j, h in enumerate(comp_headers):
        cell = tbl_comp.cell(0, j)
        cell.width = col_w_comp[j]
        style_cell(cell, h, bold=True, size_pt=8.5, color_rgb=(255,255,255), align=WD_ALIGN_PARAGRAPH.CENTER, bg_color="1F4E79")

    comp_data = [
        ("Maximum Total Settlement", "0.90 in (Si only)", "6.02 – 6.32 in", "1.0 in", "602% – 632%", "NON-COMPLIANT (Fails by >5 in)"),
        ("Maximum Differential Settlement", "0.20 in (Si only)", "1.70 – 2.30 in", "0.5 in (over 30 ft)", "340% – 460%", "NON-COMPLIANT (Fails by ~1.5 in)"),
        ("Maximum Angular Distortion", "1 / 2,150", "1 / 156 – 1 / 180", "1 / 500 (AISC DG3)", "278% – 320%", "NON-COMPLIANT (Structural cracking)")
    ]

    for i, row in enumerate(comp_data):
        bg = "FDE8E8"
        for j, val in enumerate(row):
            cell = tbl_comp.cell(i+1, j)
            cell.width = col_w_comp[j]
            align = WD_ALIGN_PARAGRAPH.CENTER if j >= 1 else WD_ALIGN_PARAGRAPH.LEFT
            bold_val = (j in [0, 2, 5])
            c_rgb = (192, 0, 0) if j == 5 else (0, 0, 0)
            style_cell(cell, val, bold=bold_val, size_pt=8.0, color_rgb=c_rgb, align=align, bg_color=bg)

    p_sec5._p.addprevious(tbl_comp._element)
    # removed empty p

    add_p(p_sec5, [
        ("Differential Settlement & Distortion Working: ", True),
        ("At perimeter and corner footings (e.g., F-C1, F-C4, F-C12), tributary service loads are smaller (264 to 292 kips) and stress overlap is reduced, resulting in an estimated stress increase at mid-clay of Δσ ≈ 400 to 500 psf. The corresponding primary consolidation settlement at corner footings is Sc ≈ 2.7 to 3.3 inches, yielding total corner settlement of ~3.4 to 4.0 inches. The resulting differential settlement across the Block C footprint is ", False),
        ("ΔS_total = 1.7 to 2.3 inches", True),
        (" over typical column grid spans of 24 to 26 ft (and up to 2.5 inches diagonally). This corresponds to an angular distortion of ", False),
        ("θ = ΔS / L ≈ 2.0 in / (26 ft × 12 in/ft) = 1 / 156", True),
        (", more than three times steeper than the 1/500 damage threshold. Unmitigated, this level of distortion will cause severe cracking in the superstructure, extensive distress in masonry partitions (Spec 09 21 16), racking of door/window frames, and unmodeled moment transfer into the podium transfer slab.", False)
    ], space_before=1, space_after=6)

    # FINDING 3
    add_heading_sub(p_sec5, "Finding 3: Time-Rate of Consolidation and Hydrogeologic Boundary Conditions", space_before=6, space_after=3)
    add_p(p_sec5, [
        ("Citation: ", True),
        ("VMT-2025-0109-CON Summary Sheet (p. 4); Kelbrook GIR Rev.2 §8.1 (p. 15); Boring Logs B-01 through B-09.", False)
    ], space_before=0, space_after=3)
    add_p(p_sec5, [
        ("To determine whether consolidation settlement could dissipate during construction, a time-rate of consolidation analysis was conducted using Terzaghi's one-dimensional consolidation theory. In-situ drainage and consolidation parameters were established as follows:", False)
    ], space_before=2, space_after=3)
    add_p(p_sec5, [
        ("•  ", False),
        ("Coefficient of Consolidation (cv): ", True),
        ("From Vantree Report VMT-2025-0109-CON (Loads 5–7 virgin average, Taylor square-root-t method), cv = 4.5 × 10⁻⁴ cm²/s. In engineering units: cv = 4.5 × 10⁻⁴ × (86,400 / 929.0304) = ", False),
        ("0.04185 ft²/day", True),
        (" (~0.042 ft²/day).", False)
    ], space_before=1, space_after=2, bullet=True)
    add_p(p_sec5, [
        ("•  ", False),
        ("Drainage Boundary Conditions: ", True),
        ("Stratum 2 clay (El. 738.0 to El. 720.0) is bounded above by the medium-dense SP-SM sand (Stratum 1) and below by the highly permeable dense SW-GW sand and gravel aquifer (Stratum 3). Both contacts act as free-draining boundaries, establishing a ", False),
        ("double-drainage condition", True),
        (".", False)
    ], space_before=1, space_after=2, bullet=True)
    add_p(p_sec5, [
        ("•  ", False),
        ("Maximum Drainage Path Length (Hdr): ", True),
        ("Hdr = H / 2 = 18.0 ft / 2 = ", False),
        ("9.0 ft", True),
        (" (108 inches).", False)
    ], space_before=1, space_after=3, bullet=True)

    add_p(p_sec5, [
        ("Time-Rate Mathematical Working:", True)
    ], space_before=2, space_after=2)
    add_p(p_sec5, [
        ("Applying the standard dimensionless time factor relation t = (Tv · Hdr²) / cv:", False)
    ], space_before=1, space_after=2)
    add_p(p_sec5, [
        ("•  Time for 50% Primary Consolidation (U = 50%, Tv = 0.197):", False),
        ("\n   t_50 = (0.197 · 9.0²) / 0.04185 = 15.957 / 0.04185 = ", False),
        ("381 days (~1.04 years)", True, False, 10.0, (31, 78, 121))
    ], space_before=1, space_after=2)
    add_p(p_sec5, [
        ("•  Time for 90% Primary Consolidation (U = 90%, Tv = 0.848):", False),
        ("\n   t_90 = (0.848 · 9.0²) / 0.04185 = 68.688 / 0.04185 = ", False),
        ("1,641 days (~4.50 years)", True, False, 10.0, (31, 78, 121))
    ], space_before=1, space_after=3)
    add_p(p_sec5, [
        ("Engineering Conclusion on Timing: ", True),
        ("Primary consolidation requires approximately 4.5 years to reach 90% completion. This confirms that consolidation will continue across the entire construction window and persist for years into building occupancy. Claims that settlement is short-term or will dissipate prior to occupancy are scientifically refuted.", False)
    ], space_before=1, space_after=6)

    # FINDING 4
    add_heading_sub(p_sec5, "Finding 4: Reconciliation with Field Settlement Monitoring Data (SM-BLKC-2026-Rev14)", space_before=6, space_after=3)
    add_p(p_sec5, [
        ("Citation: ", True),
        ("Rowan Bay Constructors Settlement Monitoring Records SM-BLKC-2026-Rev14 (Rounds 1–15, certified by Dennis Halloran, PLS, OH #S-8642); Monthly Progress Report No. 14 §5.5; Progress Meeting Minutes No. 26 Item 26.7.1.", False)
    ], space_before=0, space_after=3)
    add_p(p_sec5, [
        ("Field settlement monitoring has been conducted on 12 brass pins set in finished column pedestals C-1 through C-12, surveyed using a Leica LS15 digital level and Invar staff closed on off-site benchmark BM-SITE-A1 (El. 752.483 ft NAVD88). Baseline Round 1 was established on 12/12/2025 following footing casting and backfill. Table 4-3 tracks the cumulative vertical movement at representative footings across key construction milestones:", False)
    ], space_before=2, space_after=4)

    tbl_mon = doc.add_table(rows=9, cols=7)
    tbl_mon.alignment = WD_TABLE_ALIGNMENT.CENTER
    set_table_borders(tbl_mon)
    col_w_mon = [Inches(0.6), Inches(0.95), Inches(1.5), Inches(0.9), Inches(0.9), Inches(0.9), Inches(1.0)]
    mon_headers = ["Round", "Date", "Construction Loading Milestone", "MP-1 (NW)", "MP-7 (Int, Max)", "MP-12 (SE, Min)", "ΔS_diff (MP7-12)"]
    for j, h in enumerate(mon_headers):
        cell = tbl_mon.cell(0, j)
        cell.width = col_w_mon[j]
        style_cell(cell, h, bold=True, size_pt=8.5, color_rgb=(255,255,255), align=WD_ALIGN_PARAGRAPH.CENTER, bg_color="1F4E79")

    mon_data = [
        ("1", "12/12/2025", "Baseline (footings cast/backfilled)", "0.00 in", "0.00 in", "0.00 in", "0.00 in"),
        ("3", "01/09/2026", "Level-1 column pedestals cast", "-0.04 in", "-0.06 in", "-0.03 in", "0.03 in"),
        ("6", "02/20/2026", "Level-2 framing & slab erected", "-0.11 in", "-0.16 in", "-0.08 in", "0.08 in"),
        ("9", "04/03/2026", "Level-2 CMU partitions placed", "-0.19 in", "-0.28 in", "-0.14 in", "0.14 in"),
        ("12", "05/15/2026", "Level-3 framing erected", "-0.29 in", "-0.42 in", "-0.21 in", "0.21 in"),
        ("13", "05/29/2026", "Roof steel framing erected", "-0.33 in", "-0.48 in", "-0.24 in", "0.24 in"),
        ("14", "06/12/2026", "Podium slab-on-grade formed", "-0.37 in", "-0.54 in", "-0.27 in", "0.27 in"),
        ("15", "06/26/2026", "Podium SOG cast (Latest Round)", "-0.42 in", "-0.61 in", "-0.31 in", "0.30 in")
    ]

    for i, row in enumerate(mon_data):
        bg = "F9FAFB" if i % 2 == 1 else "FFFFFF"
        if i == len(mon_data)-1:
            bg = "FFF2CC"
        for j, val in enumerate(row):
            cell = tbl_mon.cell(i+1, j)
            cell.width = col_w_mon[j]
            align = WD_ALIGN_PARAGRAPH.CENTER if j in [0, 1, 3, 4, 5, 6] else WD_ALIGN_PARAGRAPH.LEFT
            bold_val = (j in [4, 6] or i == len(mon_data)-1)
            c_rgb = (192, 0, 0) if (j in [4, 6] and i == len(mon_data)-1) else (0,0,0)
            style_cell(cell, val, bold=bold_val, size_pt=8.0, color_rgb=c_rgb, align=align, bg_color=bg)

    p_sec5._p.addprevious(tbl_mon._element)
    # removed empty p

    add_p(p_sec5, [
        ("Analysis of Settlement Rate and Curvature Trend: ", True),
        ("Crucially, the field record demonstrates that the incremental settlement rate has ", False),
        ("NOT stabilized or decelerated", True),
        (". On the contrary, the bi-weekly settlement rate at governing interior point MP-7 has more than doubled:", False)
    ], space_before=2, space_after=2)
    add_p(p_sec5, [
        ("•  Rounds 2–4 (12/12/2025 to 01/23/2026): ΔS = 0.03 in / 14 days (0.0021 in/day) — early column loading.", False)
    ], space_before=1, space_after=1, bullet=True)
    add_p(p_sec5, [
        ("•  Rounds 5–10 (01/23/2026 to 04/17/2026): ΔS = 0.03 to 0.04 in / 14 days (0.0025 in/day) — Level-2 framing and CMU.", False)
    ], space_before=1, space_after=1, bullet=True)
    add_p(p_sec5, [
        ("•  Rounds 11–12 (04/17/2026 to 05/15/2026): ΔS = 0.05 in / 14 days (0.0036 in/day) — Level-3 framing.", False)
    ], space_before=1, space_after=1, bullet=True)
    add_p(p_sec5, [
        ("•  Rounds 13–14 (05/15/2026 to 06/12/2026): ΔS = 0.06 in / 14 days (0.0043 in/day) — roof steel framing.", False)
    ], space_before=1, space_after=1, bullet=True)
    add_p(p_sec5, [
        ("•  Round 15 (06/12/2026 to 06/26/2026): ΔS = 0.07 in / 14 days (0.0050 in/day) — podium slab-on-grade concrete placed.", False)
    ], space_before=1, space_after=3, bullet=True)
    add_p(p_sec5, [
        ("The trend plot in SM-BLKC-2026-Rev14 exhibits ", False),
        ("pronounced concave-downward curvature", True),
        (". The curve has not entered a decelerating (concave-up) phase. This behavior represents active primary consolidation under progressive load addition.", False)
    ], space_before=1, space_after=3)

    add_p(p_sec5, [
        ("Reconciliation with Consolidation Mechanics: ", True),
        ("At 196 days post-baseline, theoretical instantaneous consolidation is U ≈ 36%. Under progressive construction loading, effective degree of consolidation is approximately 20% to 25% of the ultimate consolidation under loads applied to date. The observed 0.61 inches at MP-7 represents immediate elastic response plus the initial 20–25% of primary clay consolidation. ", False),
        ("Cumulative settlement has already consumed 61% of the 1.0-inch total tolerance", True),
        (" (and differential settlement of 0.30 in has consumed 60% of tolerance) ", False),
        ("BEFORE the addition of residential partitions (Spec 09 21 16), MEP systems, architectural finishes, facade cladding, and live loads.", True),
        (" The field data provides undeniable proof that the foundation is tracking the 6.0+ inch trajectory calculated in Finding 2, completely refuting the EOR's assumption that settlement was finished.", False)
    ], space_before=1, space_after=6)

    # FINDING 5
    add_heading_sub(p_sec5, "Finding 5: Non-Compliance with Contract Specifications and Project Governance", space_before=6, space_after=3)
    add_p(p_sec5, [
        ("Citation: ", True),
        ("Specification Section 31 20 00 Article 3.6; CB-DBM-001 Rev.2 §7.3; Progress Meeting Minutes No. 26; Owner Directive (07/06/2026).", False)
    ], space_before=0, space_after=3)
    add_p(p_sec5, [
        ("The technical findings above establish multiple direct violations of contract documents and project governance:", False)
    ], space_before=2, space_after=3)
    add_p(p_sec5, [
        ("1.  Violation of Specification 31 20 00 Article 3.6.A: ", True),
        ("Predicted total settlement of 6.02 to 6.32 inches exceeds the 1.0 inch contractual limit by over 5 inches (a 500%+ violation). Predicted differential settlement of 1.7 to 2.3 inches exceeds the 0.5 inch limit by 240% to 360%.", False)
    ], space_before=1, space_after=2, bullet=True)
    add_p(p_sec5, [
        ("2.  Mandatory Stop-Work Trigger under Specification 31 20 00 Article 3.6.B: ", True),
        ("Article 3.6.B mandates: 'Where predicted or monitored settlements exceed the tolerances of Paragraph A, the Structural Engineer of Record shall be notified in writing and no additional load shall be applied until a written disposition is issued.' Because monitored settlement (0.61 in) is accelerating and predicted settlement (6.0+ in) vastly exceeds tolerance, ", False),
        ("a contractual hold on additional loading at Block C is legally triggered.", True)
    ], space_before=1, space_after=2, bullet=True)
    add_p(p_sec5, [
        ("3.  Violation of Specification 31 20 00 Article 3.6.C: ", True),
        ("Monitored settlement at MP-7 (0.61 in) constitutes a threshold condition approaching tolerance that required immediate formal reporting and technical remediation by the EOR and Contractor.", False)
    ], space_before=1, space_after=2, bullet=True)
    add_p(p_sec5, [
        ("4.  Invalidation of Structural Design Basis (CB-DBM-001 §7.3): ", True),
        ("The structural design basis for Block C shallow foundations rested on calculation CB-GEO-007. Because CB-GEO-007 failed to calculate clay consolidation, the design basis is unsubstantiated and legally deficient.", False)
    ], space_before=1, space_after=6, bullet=True)

    # ==========================================
    # SECTION 5: CONCLUSION AND RECOMMENDATION
    # ==========================================
    remove_between(p_sec5, p_name)

    add_p(p_name, [
        ("5.1  Technical Determination and Register Disposition", True, False, 10.0, (31, 78, 121))
    ], space_before=4, space_after=2)
    add_p(p_name, [
        ("Based on the independent geotechnical analysis and empirical reconciliation presented herein, the technical determinations are:", False)
    ], space_before=1, space_after=2)
    add_p(p_name, [
        ("1.  Calculation CB-GEO-007 (Rev.0) is ", False),
        ("REJECTED", True, False, 10.0, (192, 0, 0)),
        (" as incomplete, technically deficient, and non-compliant with the contract documents. It omitted primary consolidation settlement of the 18-ft thick Stratum 2 CL clay layer.", False)
    ], space_before=1, space_after=2, bullet=True)
    add_p(p_name, [
        ("2.  The Block C spread footing foundation system as designed and detailed on Sheets S-101 and S-201 ", False),
        ("DOES NOT SATISFY", True, False, 10.0, (192, 0, 0)),
        (" the serviceability settlement limits of Specification Section 31 20 00 Article 3.6 or DBM Rev.2 Section 7.3.", False)
    ], space_before=1, space_after=2, bullet=True)
    add_p(p_name, [
        ("3.  The recommended disposition for Register Item 051 is: ", False),
        ("REJECTED / OPEN — ACTION REQUIRED", True, False, 10.0, (192, 0, 0)),
        (". Verification cannot be issued, and Item 051 cannot be closed at this time.", False)
    ], space_before=1, space_after=4, bullet=True)

    add_p(p_name, [
        ("5.2  Contractual Hold-Point Impact — Level-3 Concrete Placement (07/22/2026)", True, False, 10.0, (31, 78, 121))
    ], space_before=4, space_after=2)
    add_p(p_name, [
        ("Clarification of Structural Decoupling: ", True),
        ("The Level-3 concrete placement scheduled for 0530 on July 22, 2026, is located exclusively within ", False),
        ("Blocks A and B", True),
        (". Per Drawing S-101 Rev.4, Blocks A and B are founded on a continuous 3.0-ft thick reinforced concrete basement mat (underside El. 731.5) and 48 driven steel pipe piles bearing in the dense sand and gravel aquifer below El. 720.0. The foundation system for Blocks A and B is structurally independent of the Block C spread footings. Therefore, the rejection of Item 051 ", False),
        ("does not prevent the contractual release of the Level-3 concrete placement at Blocks A and B", True),
        (", provided that the hold-point critical materials verifications (Item 052 for rebar, Item 053 for concrete strength, and Item 057 for cover) and structural items (050 and 055) are closed.", False)
    ], space_before=1, space_after=3)
    add_p(p_name, [
        ("MANDATORY HOLD ON BLOCK C: ", True, False, 10.0, (192, 0, 0)),
        ("In strict compliance with Specification Section 31 20 00 Article 3.6.B, ", False),
        ("an immediate, mandatory freeze on additional loading is imposed on Block C.", True),
        (" Rowan Bay Constructors shall not place any additional structural framing, CMU partitions, gypsum walls, MEP installations, or finishes on Block C until the EOR issues a formal written disposition and an approved foundation remediation plan is fully accepted by Thelbridge and the Owner.", False)
    ], space_before=2, space_after=4)

    add_p(p_name, [
        ("5.3  Action Matrix Required Prior to Closure of Item 051", True, False, 10.0, (31, 78, 121))
    ], space_before=4, space_after=2)
    add_p(p_name, [
        ("Before Item 051 can be verified and closed on the Package A register, the specific deliverables and site actions detailed in Table 5-1 must be formally submitted, reviewed, and approved:", False)
    ], space_before=1, space_after=4)

    tbl_act = doc.add_table(rows=8, cols=5)
    tbl_act.alignment = WD_TABLE_ALIGNMENT.CENTER
    set_table_borders(tbl_act)
    col_w_act = [Inches(0.6), Inches(1.8), Inches(2.35), Inches(1.15), Inches(0.85)]
    act_headers = ["Action", "Required Deliverable / Site Action", "Scope & Technical Acceptance Criteria", "Responsible Party", "Target Date"]
    for j, h in enumerate(act_headers):
        cell = tbl_act.cell(0, j)
        cell.width = col_w_act[j]
        style_cell(cell, h, bold=True, size_pt=8.5, color_rgb=(255,255,255), align=WD_ALIGN_PARAGRAPH.CENTER, bg_color="1F4E79")

    act_data = [
        ("A-1", "Notice & Serviceability Disposition", "Formal written notification under Spec 31 20 00 Article 3.6.B acknowledging settlement exceedance and providing interim structural safety assessment.", "Gregory Nash, PE (Calloway Braddock)", "07/24/2026"),
        ("A-2", "Work Hold Enforcement on Block C", "Issue formal site stop-work order freezing all erection of structural steel, CMU/drywall partitions, and finishes on Block C.", "Marcus Whitfield / S. Kendrow (Rowan Bay)", "Immediate (07/20/2026)"),
        ("A-3", "Revised Calculation CB-GEO-007 (Rev.1)", "Complete revision of CB-GEO-007 computing 1D consolidation settlement on Sheet 4 for all 12 footings using VMT-2025-0109-CON parameters (Cc=0.28, Cr=0.045, e0=0.92, cv=4.5e-4).", "Gregory Nash, PE (Calloway Braddock)", "07/31/2026"),
        ("A-4", "Accelerated Survey & Tell-Tales", "Increase Block C monitoring cadence from 14 days to 7 days; install calibrated optical crack tell-tales across CMU partition joints; transmit weekly PLS-certified reports.", "Dennis Halloran, PLS (Rowan Bay Survey)", "Weekly (next 07/24/2026)"),
        ("A-5", "Block C Foundation Remediation Plan", "Sealed engineering remediation package evaluating underpinning (micropiles to dense aquifer below El. 720), mat stiffening with jacking points, or ground improvement.", "Gregory Nash, PE (Calloway Braddock)", "08/07/2026"),
        ("A-6", "Geotechnical Review & Concurrence", "Independent geotechnical review and formal written concurrence on revised calculation CB-GEO-007 Rev.1 and foundation remediation design.", "Alden Roscombe, PE (Kelbrook Geotechnical)", "08/14/2026"),
        ("A-7", "Verification Memo Closure & Hold Release", "Thelbridge geotechnical review of remediation package, concurrence, and updated survey data to issue final verification memo and close Item 051.", "Rahul Nimkar / A. Vance (Thelbridge)", "Following A-1 to A-6")
    ]

    for i, row in enumerate(act_data):
        bg = "F9FAFB" if i % 2 == 1 else "FFFFFF"
        for j, val in enumerate(row):
            cell = tbl_act.cell(i+1, j)
            cell.width = col_w_act[j]
            align = WD_ALIGN_PARAGRAPH.CENTER if j in [0, 4] else WD_ALIGN_PARAGRAPH.LEFT
            style_cell(cell, val, bold=(j in [0, 3]), size_pt=8.0, color_rgb=(0,0,0), align=align, bg_color=bg)

    p_name._p.addprevious(tbl_act._element)
    # removed empty p

    # Update Sign-off block
    p_name.text = "Rahul Nimkar"
    p_name.paragraph_format.space_before = Pt(16)
    p_name.paragraph_format.space_after = Pt(1)
    p_name.runs[0].font.name = 'Calibri'
    p_name.runs[0].font.size = Pt(10.0)
    p_name.runs[0].bold = True

    p_title.text = "Geotechnical Reviewer"
    p_title.paragraph_format.space_before = Pt(0)
    p_title.paragraph_format.space_after = Pt(1)
    p_title.runs[0].font.name = 'Calibri'
    p_title.runs[0].font.size = Pt(10.0)
    p_title.runs[0].bold = False

    p_org.text = "Thelbridge Project Management Services — Owner's Representative"
    p_org.paragraph_format.space_before = Pt(0)
    p_org.paragraph_format.space_after = Pt(1)
    p_org.runs[0].font.name = 'Calibri'
    p_org.runs[0].font.size = Pt(10.0)

    p_date.text = "July 20, 2026"
    p_date.paragraph_format.space_before = Pt(0)
    p_date.paragraph_format.space_after = Pt(0)
    p_date.runs[0].font.name = 'Calibri'
    p_date.runs[0].font.size = Pt(10.0)


    # Apply keep_with_next and table enhancements
    for p in doc.paragraphs:
        txt = p.text.strip()
        if any(h in txt for h in ["1.  PURPOSE", "2.  DOCUMENTS REVIEWED", "3.  BASIS OF REVIEW", "4.  FINDINGS", "5.  CONCLUSION AND RECOMMENDATION", "Finding 1:", "Finding 2:", "Finding 3:", "Finding 4:", "Finding 5:", "5.1  Technical", "5.2  Contractual", "5.3  Action Matrix", "Mathematical Working", "Working 2A:", "Working 2B:", "Working 2C:", "Time-Rate Mathematical", "Analysis of Settlement"]):
            p.paragraph_format.keep_with_next = True

    for t in doc.tables:
        trPr0 = t.rows[0]._tr.get_or_add_trPr()
        trPr0.append(parse_xml(f'<w:tblHeader {nsdecls("w")}/>'))
        for r in t.rows:
            trPr = r._tr.get_or_add_trPr()
            trPr.append(parse_xml(f'<w:cantSplit {nsdecls("w")}/>'))

    # Save document
    doc.save(output_path)
    print(f"Document successfully created and saved at: {output_path}")

if __name__ == '__main__':
    generate_memo()
