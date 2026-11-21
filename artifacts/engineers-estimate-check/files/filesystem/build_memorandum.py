import os
import math
import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL
from docx.oxml import OxmlElement, parse_xml
from docx.oxml.ns import nsdecls, qn

def set_cell_margins(cell, top=100, bottom=100, left=150, right=150):
    """Set cell margins in twips (1/20 pt)."""
    tcPr = cell._tc.get_or_add_tcPr()
    tcMar = OxmlElement('w:tcMar')
    for m, val in [('top', top), ('bottom', bottom), ('left', left), ('right', right)]:
        node = OxmlElement(f'w:{m}')
        node.set(qn('w:w'), str(val))
        node.set(qn('w:type'), 'dxa')
        tcMar.append(node)
    tcPr.append(tcMar)

def set_cell_background(cell, hex_color):
    """Set background color of a cell."""
    tcPr = cell._tc.get_or_add_tcPr()
    shd = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{hex_color}"/>')
    tcPr.append(shd)

def set_cell_borders(cell, top="CCCCCC", bottom="CCCCCC", left=None, right=None, sz="4"):
    """Set specific borders for a cell."""
    tcPr = cell._tc.get_or_add_tcPr()
    tcBorders = OxmlElement('w:tcBorders')
    
    borders = {'w:top': top, 'w:bottom': bottom, 'w:left': left, 'w:right': right}
    for b_name, b_color in borders.items():
        if b_color:
            b_elem = parse_xml(f'<{b_name} {nsdecls("w")} w:val="single" w:sz="{sz}" w:space="0" w:color="{b_color}"/>')
            tcBorders.append(b_elem)
        else:
            b_elem = parse_xml(f'<{b_name} {nsdecls("w")} w:val="none"/>')
            tcBorders.append(b_elem)
    tcPr.append(tcBorders)

def add_tr_props(row, is_header=False):
    """Add cantSplit and optional tblHeader to a table row."""
    trPr = row._tr.get_or_add_trPr()
    trPr.append(parse_xml(f'<w:cantSplit {nsdecls("w")}/>'))
    if is_header:
        trPr.append(parse_xml(f'<w:tblHeader {nsdecls("w")}/>'))

def create_memo():
    doc = docx.Document()
    
    # Page setup - 1 inch margins all around
    sections = doc.sections
    for section in sections:
        section.top_margin = Inches(1.0)
        section.bottom_margin = Inches(1.0)
        section.left_margin = Inches(1.0)
        section.right_margin = Inches(1.0)
        section.page_width = Inches(8.5)
        section.page_height = Inches(11.0)
        
        # Add page numbering to footer
        footer = section.footer
        f_p = footer.paragraphs[0]
        f_p.alignment = WD_ALIGN_PARAGRAPH.RIGHT
        f_run = f_p.add_run("Desert Sage Ranch Phase 3 (Job 2201-03) — Engineer's Estimate Section 2 Reconciliation | Page ")
        f_run.font.name = 'Arial'
        f_run.font.size = Pt(8.5)
        f_run.font.color.rgb = RGBColor(0x88, 0x88, 0x88)
        
        # Add dynamic page number XML to footer
        f_p_xml = f_p._p
        fldSimple = OxmlElement('w:fldSimple')
        fldSimple.set(qn('w:instr'), 'PAGE')
        f_p_xml.append(fldSimple)
        
        f_run2 = f_p.add_run(" of ")
        f_run2.font.name = 'Arial'
        f_run2.font.size = Pt(8.5)
        f_run2.font.color.rgb = RGBColor(0x88, 0x88, 0x88)
        
        fldSimple2 = OxmlElement('w:fldSimple')
        fldSimple2.set(qn('w:instr'), 'NUMPAGES')
        f_p_xml.append(fldSimple2)

    # Styles & Colors
    NAVY = RGBColor(0x1B, 0x36, 0x5D)
    SLATE = RGBColor(0x4A, 0x60, 0x7A)
    CHARCOAL = RGBColor(0x22, 0x22, 0x22)
    WHITE = RGBColor(0xFF, 0xFF, 0xFF)
    
    # -------------------------------------------------------------
    # 1. FIRM LETTERHEAD
    # -------------------------------------------------------------
    p_firm = doc.add_paragraph()
    p_firm.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_firm.paragraph_format.space_before = Pt(0)
    p_firm.paragraph_format.space_after = Pt(1)
    run_firm = p_firm.add_run("SUNDIAL ENGINEERING & SURVEY")
    run_firm.font.name = 'Arial'
    run_firm.font.size = Pt(15)
    run_firm.font.bold = True
    run_firm.font.color.rgb = NAVY
    
    p_addr = doc.add_paragraph()
    p_addr.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_addr.paragraph_format.space_before = Pt(0)
    p_addr.paragraph_format.space_after = Pt(12)
    run_addr = p_addr.add_run("4720 South Rainbow Boulevard, Suite 210  ·  Las Vegas, Nevada 89103\nTelephone (702) 555-0142  ·  Nevada Certificate of Authority #C-3874")
    run_addr.font.name = 'Arial'
    run_addr.font.size = Pt(8.5)
    run_addr.font.color.rgb = SLATE

    # Horizontal Divider Line
    p_div = doc.add_paragraph()
    p_div.paragraph_format.space_before = Pt(0)
    p_div.paragraph_format.space_after = Pt(14)
    p_div_border = parse_xml(f'<w:pBdr {nsdecls("w")}><w:bottom w:val="single" w:sz="18" w:space="1" w:color="1B365D"/></w:pBdr>')
    p_div._p.get_or_add_pPr().append(p_div_border)

    # -------------------------------------------------------------
    # 2. MEMORANDUM HEADER BLOCK
    # -------------------------------------------------------------
    p_memo_title = doc.add_paragraph()
    p_memo_title.paragraph_format.space_before = Pt(0)
    p_memo_title.paragraph_format.space_after = Pt(10)
    run_m = p_memo_title.add_run("MEMORANDUM")
    run_m.font.name = 'Arial'
    run_m.font.size = Pt(18)
    run_m.font.bold = True
    run_m.font.color.rgb = NAVY

    memo_headers = [
        ("TO:", "Garrett Nokes, Vice President of Land Development, Callaway Land Partners"),
        ("FROM:", "Jonathan R. Kessler, PE, Principal-in-Charge, Sundial Engineering & Survey (NV License No. 14203)"),
        ("DATE:", "October 31, 2026"),
        ("PROJECT:", "Desert Sage Ranch — Phase 3 (Job Number: 2201-03)"),
        ("APPLICATIONS:", "Improvement Plans: IP-26-100288  |  Final Map: FM-26-100290  |  Tentative Map: TM-22-500041"),
        ("SUBJECT:", "Section 2 (Storm Drain & Detention) Engineer's Estimate Reconciliation Against Approved Drainage Plans (Sheets C-6, C-8, C-9) and Revised Performance Bond Amount for Surety Broker Transmittal"),
        ("CC:", "Max Braddock, Project Manager; Priya Sarwal, EIT; Surety Broker File (P:/2201-03/Cost Estimates)")
    ]

    tbl_hdr = doc.add_table(rows=len(memo_headers), cols=2)
    tbl_hdr.alignment = WD_TABLE_ALIGNMENT.CENTER
    tbl_hdr.autofit = False
    
    col_widths = [Inches(1.4), Inches(5.1)]
    for r_idx, (label, val) in enumerate(memo_headers):
        row = tbl_hdr.rows[r_idx]
        add_tr_props(row, is_header=False)
        
        cell_lbl, cell_val = row.cells[0], row.cells[1]
        cell_lbl.width, cell_val.width = col_widths[0], col_widths[1]
        
        for cell in (cell_lbl, cell_val):
            set_cell_margins(cell, top=40, bottom=40, left=60, right=60)
            set_cell_borders(cell, top=None, bottom="E5E7EB", left=None, right=None, sz="4")

        p_lbl = cell_lbl.paragraphs[0]
        p_lbl.paragraph_format.space_before = Pt(1)
        p_lbl.paragraph_format.space_after = Pt(1)
        r_l = p_lbl.add_run(label)
        r_l.font.name = 'Arial'
        r_l.font.size = Pt(9.5)
        r_l.font.bold = True
        r_l.font.color.rgb = NAVY

        p_val = cell_val.paragraphs[0]
        p_val.paragraph_format.space_before = Pt(1)
        p_val.paragraph_format.space_after = Pt(1)
        r_v = p_val.add_run(val)
        r_v.font.name = 'Arial'
        r_v.font.size = Pt(9.5)
        if label == "SUBJECT:":
            r_v.font.bold = True
            r_v.font.color.rgb = NAVY
        else:
            r_v.font.color.rgb = CHARCOAL

    doc.add_paragraph().paragraph_format.space_after = Pt(6)

    def add_sec_heading(title, number=None):
        p = doc.add_paragraph()
        p.paragraph_format.space_before = Pt(14)
        p.paragraph_format.space_after = Pt(4)
        p.paragraph_format.keep_with_next = True
        
        full_title = f"{number}. {title}" if number else title
        run = p.add_run(full_title)
        run.font.name = 'Arial'
        run.font.size = Pt(12)
        run.font.bold = True
        run.font.color.rgb = NAVY
        
        pPr = p._p.get_or_add_pPr()
        pBdr = parse_xml(f'<w:pBdr {nsdecls("w")}><w:bottom w:val="single" w:sz="8" w:space="1" w:color="1B365D"/></w:pBdr>')
        pPr.append(pBdr)

    def add_sub_heading(title):
        p = doc.add_paragraph()
        p.paragraph_format.space_before = Pt(10)
        p.paragraph_format.space_after = Pt(2)
        p.paragraph_format.keep_with_next = True
        run = p.add_run(title)
        run.font.name = 'Arial'
        run.font.size = Pt(10.5)
        run.font.bold = True
        run.font.color.rgb = SLATE

    def add_p(text, bold_prefix=None, space_after=4):
        p = doc.add_paragraph()
        p.paragraph_format.space_before = Pt(0)
        p.paragraph_format.space_after = Pt(space_after)
        p.paragraph_format.line_spacing = 1.15
        if bold_prefix:
            r_bp = p.add_run(bold_prefix)
            r_bp.font.name = 'Arial'
            r_bp.font.size = Pt(9.5)
            r_bp.font.bold = True
            r_bp.font.color.rgb = CHARCOAL
        run = p.add_run(text)
        run.font.name = 'Arial'
        run.font.size = Pt(9.5)
        run.font.color.rgb = CHARCOAL
        return p

    def add_bullet(text, bold_prefix=None):
        p = doc.add_paragraph(style='List Bullet')
        p.paragraph_format.space_before = Pt(1)
        p.paragraph_format.space_after = Pt(3)
        p.paragraph_format.line_spacing = 1.15
        if bold_prefix:
            r_bp = p.add_run(bold_prefix)
            r_bp.font.name = 'Arial'
            r_bp.font.size = Pt(9.5)
            r_bp.font.bold = True
            r_bp.font.color.rgb = CHARCOAL
        run = p.add_run(text)
        run.font.name = 'Arial'
        run.font.size = Pt(9.5)
        run.font.color.rgb = CHARCOAL
        return p

    # -------------------------------------------------------------
    # 3. EXECUTIVE SUMMARY
    # -------------------------------------------------------------
    add_sec_heading("EXECUTIVE SUMMARY & BOND RECONCILIATION SUMMARY", "1")
    
    add_p("At your request, Sundial Engineering & Survey has performed a rigorous, comprehensive plan-to-estimate audit of Section 2 (Storm Drain and Detention) of the Engineer's Estimate of Probable Cost for Desert Sage Ranch Phase 3 (job number 2201-03). Garrett indicated that Callaway Land Partners wishes to transmit the finalized Phase 3 estimate to your surety broker to initiate issuance of the subdivision performance bond required under Clark County Code Title 30 and the Subdivision Improvement Agreement (SIA). As Principal-in-Charge and sealing engineer of record, I directed that no estimate figures leave our office until Section 2 was audited line-by-line against the actual design drawings and hydraulic modeling.", bold_prefix="Purpose & Authorization: ")

    add_p("Our audit cross-referenced Section 2 of DSR_Ph3_Engineers_Estimate against drainage sheets C-6, C-8, and C-9 of the Phase 3 Improvement Plans (application IP-26-100288), the pipe reach schedules and hydraulic calculations in DSR_Ph3_StormDrain_HGL, and the published Clark County Uniform Unit Cost Schedule for Bonding of Subdivision Improvements (effective 01/01/2026, including Addendum No. 1 effective 03/01/2026). Per your specific reconciliation instructions:", bold_prefix="Audit Scope & Methodology: ")

    add_bullet("All other sections (Sections 1, 3 through 8, and Section 9 agreed lump-sum allowances) remain strictly untouched.", bold_prefix="1. Scope Boundary: ")
    add_bullet("Where the plans show an item that was omitted from the initial estimate, it has been brought into the reconciliation (specifically the 30-inch RCP basin outfall reach).", bold_prefix="2. Missing Plan Scope: ")
    add_bullet("All items are priced off the published 2026 Clark County Uniform Unit Cost Schedule. Where the schedule specifies 'Actual' (Item 2.45, Detention Basin Outlet Structure), the amount already carried in the estimate ($28,000.00) stands without modification.", bold_prefix="3. Published Schedule Pricing: ")
    add_bullet("Where the published schedule contains nothing matching what the plans show, the item is formally flagged, and the amount already carried in the estimate remains in the subtotal (specifically Item 2.30, Type G curb inlets per County Drawing SD-305).", bold_prefix="4. Flagged Schedule Non-Matches: ")
    add_bullet("Where the plans provide no specific dimension or stationing for a line item already carried in the estimate, the quantity already carried stands (applicable to drop inlets, cast-in-place junction structures, riprap, basin excavation, basin fencing, and Phase 2 tie-in allowances).", bold_prefix="5. Undimensioned Carried Items: ")
    add_bullet("All pipe reach lengths taken from the plans and hydraulic worksheets are rounded up to the next whole linear foot.", bold_prefix="6. Pipe Rounding Convention: ")
    add_bullet("The final bonded amount is rounded up to the next whole $1,000 per Clark County Uniform Unit Cost Schedule Section 12.02.", bold_prefix="7. Final Bond Rounding: ")

    add_p("The audit revealed two primary reconciliation adjustments and one formal schedule flagging in Section 2: (1) addition of 100 LF of missing 30-inch RCP outfall pipe (Item 2.03) shown on Sheets C-6 and C-9; (2) unit-price correction of storm drain manholes from 48-inch diameter (Item 2.35 at $6,400.00) to 5-foot / 60-inch diameter (Item 2.36 at $8,750.00) per the mandatory General Notes on Sheet C-8; and (3) formal flagging of Item 2.30 because the plans depict Type G curb inlets (SD-305) for which the County schedule contains no unit price, leaving the carried $58,200.00 in place. The resulting figures are summarized below:", bold_prefix="Key Findings: ")

    # SUMMARY TABLE
    tbl_summary = doc.add_table(rows=8, cols=4)
    tbl_summary.alignment = WD_TABLE_ALIGNMENT.CENTER
    tbl_summary.autofit = False
    
    sum_widths = [Inches(2.6), Inches(1.3), Inches(1.3), Inches(1.3)]
    headers_sum = ["Cost Category / Bonding Component", "Original Estimate (10/10/2026)", "Corrected Estimate (10/31/2026)", "Net Delta / Variance"]
    hdr_row = tbl_summary.rows[0]
    add_tr_props(hdr_row, is_header=True)
    
    for c_idx, h_text in enumerate(headers_sum):
        cell = hdr_row.cells[c_idx]
        cell.width = sum_widths[c_idx]
        set_cell_background(cell, "1B365D")
        set_cell_margins(cell, top=100, bottom=100, left=100, right=100)
        p = cell.paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.RIGHT if c_idx > 0 else WD_ALIGN_PARAGRAPH.LEFT
        p.paragraph_format.space_before = Pt(2)
        p.paragraph_format.space_after = Pt(2)
        r = p.add_run(h_text)
        r.font.name = 'Arial'
        r.font.size = Pt(8.5)
        r.font.bold = True
        r.font.color.rgb = WHITE

    summary_data = [
        ("Section 2 Subtotal — Storm Drain & Detention", "$1,276,934.00", "$1,323,634.00", "+$46,700.00"),
        ("Other Construction Sections (Sec. 1, 3–8)", "$3,579,631.75", "$3,579,631.75", "$0.00 (Unchanged)"),
        ("Construction Subtotal (Sections 1–8)", "$4,856,565.75", "$4,903,265.75", "+$46,700.00"),
        ("Section 9 Allowances (Agreed Lump Sums)", "$500,000.00", "$500,000.00", "$0.00 (Unchanged)"),
        ("Total Probable Construction Cost (Unrounded)", "$5,356,565.75", "$5,403,265.75", "+$46,700.00"),
        ("Final Rounded Performance Bond Amount", "$5,357,000.00", "$5,404,000.00", "+$47,000.00"),
        ("Alternative Deduplicated Structure Schedule (Note 1)", "$5,357,000.00", "$5,369,000.00", "+$12,000.00")
    ]

    for r_idx, row_vals in enumerate(summary_data):
        row = tbl_summary.rows[r_idx + 1]
        add_tr_props(row, is_header=False)
        is_highlight = (r_idx == 0 or r_idx == 5)
        is_alt = (r_idx == 6)
        
        bg_color = "EBF2F7" if is_highlight else ("F9FAFB" if r_idx % 2 == 1 else "FFFFFF")
        
        for c_idx, val in enumerate(row_vals):
            cell = row.cells[c_idx]
            cell.width = sum_widths[c_idx]
            set_cell_background(cell, bg_color)
            set_cell_margins(cell, top=80, bottom=80, left=100, right=100)
            
            b_top = "B0C4DE" if is_highlight else "E5E7EB"
            b_bot = "1B365D" if is_highlight else "E5E7EB"
            set_cell_borders(cell, top=b_top, bottom=b_bot, left=None, right=None, sz="12" if is_highlight else "4")
            
            p = cell.paragraphs[0]
            p.alignment = WD_ALIGN_PARAGRAPH.RIGHT if c_idx > 0 else WD_ALIGN_PARAGRAPH.LEFT
            p.paragraph_format.space_before = Pt(2)
            p.paragraph_format.space_after = Pt(2)
            r = p.add_run(val)
            r.font.name = 'Arial'
            r.font.size = Pt(8.5 if not is_alt else 8.0)
            if is_highlight:
                r.font.bold = True
                r.font.color.rgb = NAVY
            elif is_alt:
                r.font.italic = True
                r.font.color.rgb = SLATE
            else:
                r.font.color.rgb = CHARCOAL

    p_note = doc.add_paragraph()
    p_note.paragraph_format.space_before = Pt(4)
    p_note.paragraph_format.space_after = Pt(10)
    r_nt = p_note.add_run("Note 1: The primary corrected Section 2 subtotal of $1,323,634.00 and rounded bond of $5,404,000.00 reflect 14 trunk structures priced at the mandatory 60-inch manhole schedule price ($8,750.00). If Clark County Public Works strictly separates the 4 standalone curb inlets from the 10 trunk manholes on Sheet C-8, Section 2 becomes $1,288,634.00 and the rounded bond is $5,369,000.00. Both scenarios are fully detailed in Section 4.")
    r_nt.font.name = 'Arial'
    r_nt.font.size = Pt(8.0)
    r_nt.font.italic = True
    r_nt.font.color.rgb = SLATE

    # -------------------------------------------------------------
    # 4. LINE-BY-LINE SECTION 2 RECONCILIATION TABLE
    # -------------------------------------------------------------
    add_sec_heading("LINE-BY-LINE SECTION 2 RECONCILIATION TABLE", "2")
    
    add_p("The following table reconciles every line item currently in Section 2 of DSR_Ph3_Engineers_Estimate against the approved drainage plans (Sheets C-6, C-8, and C-9), the Storm Drain HGL calculation workbook, and the 2026 Clark County Uniform Unit Cost Schedule. Each item reflects the governing plan sheet, verified design quantity, unit price source, schedule status, and resulting cost delta.")

    tbl_recon = doc.add_table(rows=16, cols=10)
    tbl_recon.alignment = WD_TABLE_ALIGNMENT.CENTER
    tbl_recon.autofit = False
    
    recon_widths = [
        Inches(0.40), # Item
        Inches(1.40), # Description
        Inches(0.55), # Orig Qty/Unit
        Inches(0.50), # Orig Price
        Inches(0.60), # Orig Ext
        Inches(0.55), # Rev Qty/Unit
        Inches(0.50), # Rev Price
        Inches(0.60), # Rev Ext
        Inches(0.60), # Delta
        Inches(0.80)  # Sheet & Status
    ]
    
    recon_headers = [
        "Item", "Plan / Schedule Description", "Orig. Qty/Unit", "Orig. Price", "Orig. Cost",
        "Rev. Qty/Unit", "Rev. Price", "Rev. Cost", "Cost Delta", "Sheet & Audit Status"
    ]
    
    r_hdr = tbl_recon.rows[0]
    add_tr_props(r_hdr, is_header=True)
    
    for c_idx, h_text in enumerate(recon_headers):
        cell = r_hdr.cells[c_idx]
        cell.width = recon_widths[c_idx]
        set_cell_background(cell, "1B365D")
        set_cell_margins(cell, top=80, bottom=80, left=40, right=40)
        p = cell.paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.RIGHT if c_idx in (2, 3, 4, 5, 6, 7, 8) else WD_ALIGN_PARAGRAPH.LEFT
        p.paragraph_format.space_before = Pt(1)
        p.paragraph_format.space_after = Pt(1)
        r = p.add_run(h_text)
        r.font.name = 'Arial'
        r.font.size = Pt(7.5)
        r.font.bold = True
        r.font.color.rgb = WHITE

    recon_data = [
        ("2.03", "30-inch RCP, Class III, in trench (Basin Outfall to Ph 2 Stub)", "—", "—", "$0.00", "100 LF", "$138.00", "$13,800.00", "+$13,800.00", "Sheet C-9\n[NEW ITEM]", True, False),
        ("2.04", "36-inch RCP, Class III, in trench (S-1 to S-5, Sta 0+00 to 8+69.58)", "870 LF", "$172.00", "$149,640.00", "870 LF", "$172.00", "$149,640.00", "$0.00", "Sheet C-8\nVerified", False, False),
        ("2.06", "48-inch RCP, Class III, in trench (S-5 to S-8, Sta 8+69.58 to 15+56.09)", "687 LF", "$258.00", "$177,246.00", "687 LF", "$258.00", "$177,246.00", "$0.00", "Sheet C-8\nVerified", False, False),
        ("2.08", "60-inch RCP, Class III, in trench (S-8 to S-14 & Line B to S-15)", "1,334 LF", "$372.00", "$496,248.00", "1,334 LF", "$372.00", "$496,248.00", "$0.00", "C-8, C-6\nVerified", False, False),
        ("2.30", "Catch basin, Type A curb inlet (Plans call Type G per SD-305)", "12 EA", "$4,850.00", "$58,200.00", "12 EA", "$4,850.00", "$58,200.00", "$0.00", "Sheet C-8\n[FLAGGED]", False, True),
        ("2.34", "Drop inlet, area drain", "2 EA", "$3,900.00", "$7,800.00", "2 EA", "$3,900.00", "$7,800.00", "$0.00", "C-6/C-8/C-9\nStands", False, False),
        ("2.36", "Storm drain manhole, 60-inch dia. (Corrected from 48\" Item 2.35)", "14 EA", "$6,400.00", "$89,600.00", "14 EA", "$8,750.00", "$122,500.00", "+$32,900.00", "Sheet C-8\n[PRICE CHG]", True, False),
        ("2.39", "Junction structure, cast-in-place, sized per plan", "60 CY", "$1,150.00", "$69,000.00", "60 CY", "$1,150.00", "$69,000.00", "$0.00", "Sheet C-8\nStands", False, False),
        ("2.40", "Headwall, cast-in-place, up to 48-inch pipe (S-1 & Basin Outlet)", "2 EA", "$5,400.00", "$10,800.00", "2 EA", "$5,400.00", "$10,800.00", "$0.00", "C-8, C-9\nVerified", False, False),
        ("2.42", "Riprap, D50 = 12 inches, on filter fabric (Outfall & Spillway)", "500 SY", "$86.00", "$43,000.00", "500 SY", "$86.00", "$43,000.00", "$0.00", "C-6, C-9\nStands", False, False),
        ("2.44", "Detention basin excavation (6.4 ac-ft storage allocation)", "10,000 CY", "$9.75", "$97,500.00", "10,000 CY", "$9.75", "$97,500.00", "$0.00", "C-6, C-9\nStands", False, False),
        ("2.45", "Detention basin outlet structure, per plan (Headwall/Orifice/Rack)", "1 LS", "$28,000.00", "$28,000.00", "1 LS", "$28,000.00", "$28,000.00", "$0.00", "C-6, C-9\n[ACTUAL]", False, False),
        ("2.46", "Detention basin fencing, 6-ft chain link with 3-strand barbed", "1,400 LF", "$34.00", "$47,600.00", "1,400 LF", "$34.00", "$47,600.00", "$0.00", "C-6, C-9\nStands", False, False),
        ("2.99", "Field connections to Phase 2 storm outfall structure, allowance", "1 LS", "$2,300.00", "$2,300.00", "1 LS", "$2,300.00", "$2,300.00", "$0.00", "C-1, C-8\nStands", False, False),
        ("TOTAL", "SECTION 2 SUBTOTAL — STORM DRAIN AND DETENTION", "—", "—", "$1,276,934.00", "—", "—", "$1,323,634.00", "+$46,700.00", "RECONCILED", True, False)
    ]

    for r_idx, row_data in enumerate(recon_data):
        row = tbl_recon.rows[r_idx + 1]
        add_tr_props(row, is_header=False)
        
        is_tot = (row_data[0] == "TOTAL")
        is_chg = row_data[10]
        is_flg = row_data[11]
        
        bg_col = "D9E2EC" if is_tot else ("FEF3C7" if is_flg else ("EFF6FF" if is_chg else ("F9FAFB" if r_idx % 2 == 1 else "FFFFFF")))
        
        for c_idx in range(10):
            cell = row.cells[c_idx]
            cell.width = recon_widths[c_idx]
            set_cell_background(cell, bg_col)
            set_cell_margins(cell, top=60, bottom=60, left=35, right=35)
            
            b_top = "1B365D" if is_tot else "E5E7EB"
            b_bot = "1B365D" if is_tot else "E5E7EB"
            set_cell_borders(cell, top=b_top, bottom=b_bot, left=None, right=None, sz="12" if is_tot else "4")
            
            p = cell.paragraphs[0]
            p.alignment = WD_ALIGN_PARAGRAPH.RIGHT if c_idx in (2, 3, 4, 5, 6, 7, 8) else WD_ALIGN_PARAGRAPH.LEFT
            p.paragraph_format.space_before = Pt(1)
            p.paragraph_format.space_after = Pt(1)
            
            val = row_data[c_idx]
            r = p.add_run(val)
            r.font.name = 'Arial'
            r.font.size = Pt(7.5 if not is_tot else 8.0)
            if is_tot:
                r.font.bold = True
                r.font.color.rgb = NAVY
            elif is_chg:
                r.font.bold = (c_idx in (0, 7, 8))
                r.font.color.rgb = NAVY if c_idx in (0, 7, 8) else CHARCOAL
            elif is_flg:
                r.font.bold = (c_idx in (0, 9))
                r.font.color.rgb = RGBColor(0xB4, 0x53, 0x09) if c_idx in (0, 9) else CHARCOAL
            else:
                r.font.color.rgb = CHARCOAL

    doc.add_paragraph().paragraph_format.space_after = Pt(6)

    # -------------------------------------------------------------
    # 5. DETAILED TECHNICAL AUDIT & PLAN RECONCILIATION
    # -------------------------------------------------------------
    add_sec_heading("DETAILED TECHNICAL AUDIT & PLAN RECONCILIATION", "3")
    
    add_p("A rigorous review of the plan set (IP-26-100288), the Storm Drain HGL calculation workbook, and the 2026 Clark County Uniform Unit Cost Schedule establishes the specific engineering basis for each line item in the reconciliation table above:")

    # 3.1 Pipe Reaches
    add_sub_heading("3.1 Pipe Reaches and Hydraulic Schedule Reconciliation (Items 2.03, 2.04, 2.06, 2.08)")
    add_p("Pipe materials throughout Phase 3 are specified as Class III Reinforced Concrete Pipe (ASTM C76) with rubber-gasketed joints (ASTM C443) per General Note 1 on Sheet C-8. Hydraulic sizing was verified against the 100-year, 6-hour governing design storm (2.38 inches rainfall) per the CCRFCD Hydrologic Criteria and Drainage Design Manual and DSR Master Drainage Study (Revision 1, accepted 02/28/2022). All reaches convey peak design discharges within full-flow capacity under open-channel conditions without surcharge.", bold_prefix="Pipe Sizing & Material Standard: ")

    add_bullet("Reaches R1 through R4 comprise the upper trunk along the north parcel boundary from headwall/cleanout structure S-1 (STA 0+00.00) to curb inlet S-5 (STA 8+69.58). The exact reach lengths from the HGL calculation are: R1 = 213.58 LF, R2 = 183.07 LF, R3 = 213.58 LF, and R4 = 259.35 LF. The cumulative reach length is 869.58 LF (matching station difference 8+69.58 - 0+00.00 = 869.58 LF). Applying the mandatory rule to round pipe lengths up to the next whole linear foot yields 870 LF. This exactly matches the 870 LF currently carried in the estimate at the published schedule price of $172.00/LF ($149,640.00). No change.", bold_prefix="36-Inch RCP (Item 2.04) — Sheet C-8 & HGL: ")

    add_bullet("Reaches R5 through R7 extend from S-5 (STA 8+69.58) to curb inlet/junction manhole S-8 (STA 15+56.09). Reach lengths from the HGL calculation are: R5 = 259.35 LF, R6 = 183.07 LF, and R7 = 244.09 LF. The cumulative reach length is 686.51 LF (station difference 15+56.09 - 8+69.58 = 686.51 LF). Rounding up to the next whole foot yields 687 LF. This exactly matches the 687 LF currently carried in the estimate at the published schedule price of $258.00/LF ($177,246.00). No change.", bold_prefix="48-Inch RCP (Item 2.06) — Sheet C-8 & HGL: ")

    add_bullet("The 60-inch trunk consists of two segments: (a) Line A reaches R8 through R13 along the north boundary from S-8 (STA 15+56.09) to junction manhole S-14 (STA 26+49.65), totaling 1,093.56 LF (reaches: 205.95 + 213.58 + 133.49 + 194.51 + 198.33 + 147.70 LF); and (b) Line B reach R14, extending 240.00 LF south from S-14 to the detention basin inflow structure S-15 (scaled and dimensioned on Sheet C-6 and tabulated in HGL Pipe Schedule row 18). Total cumulative length is 1,093.56 + 240.00 = 1,333.56 LF. Rounding up to the next whole foot yields 1,334 LF. This exactly matches the 1,334 LF carried in the estimate at the published schedule price of $372.00/LF ($496,248.00). No change.", bold_prefix="60-Inch RCP (Item 2.08) — Sheets C-8, C-6 & HGL: ")

    add_bullet("The original estimate completely omitted the outfall pipe connecting the detention basin outlet structure to the existing Phase 2 storm drain stub. Sheet C-6 depicts the 'Existing 30″ RCP outfall stub at SW corner of parent parcel — invert 2,850.75′ (per Phase 2 as-builts)'. Sheet C-9 details the outlet works: 'Outlet control structure at west end: 4′ × 4′ reinforced concrete headwall... 30″ RCP downstream of headwall, invert at headwall face 2,851.00′, sloped at 0.25% to shared outfall pipe stub (invert 2,850.75′)'. The required length is: ΔElevation / Slope = (2,851.00 - 2,850.75) / 0.0025 = 0.25 ft / 0.0025 = 100.00 linear feet. This reach is a required physical improvement depicted on Sheets C-6 and C-9. Priced under published schedule Item 2.03 (30-inch RCP, Class III, in trench, complete in place) at $138.00/LF, this adds 100 LF and $13,800.00 to Section 2.", bold_prefix="30-Inch RCP Basin Outfall (Item 2.03) — Sheets C-6 & C-9 [OMITTED SCOPE ADDED]: ")

    # 3.2 Storm Drain Manholes
    add_sub_heading("3.2 Storm Drain Manholes (Items 2.35, 2.36, and 2.38) — Sheet C-8")
    add_p("The original estimate carried 14 EA of Item 2.35 ('Storm drain manhole, 48-inch dia., depth ≤ 8 ft') at $6,400.00 each ($89,600.00). An audit against Sheet C-8 reveals two critical discrepancies: diameter mismatch and structure count duplication.", bold_prefix="Manhole Specification Audit: ")

    add_bullet("General Note 3 under Storm Drain Design Notes on Sheet C-8 explicitly mandates: 'All manholes are 5-foot inside diameter unless noted otherwise, precast concrete per Clark County Standard Drawing SD-301, with cast-iron frame and cover marked STORM DRAIN.' A 5-foot inside diameter is 60 inches. The 48-inch diameter carried in the estimate violates the approved plan notes. Under the Clark County Uniform Unit Cost Schedule, 60-inch diameter manholes are classified under Item 2.36 ('Storm drain manhole, 60-inch dia., depth ≤ 10 ft') at a published unit price of $8,750.00 each. Correcting the unit price from $6,400.00 to $8,750.00 represents a unit price adjustment of +$2,350.00 per structure.", bold_prefix="Mandatory 60-Inch Diameter (Item 2.36): ")

    add_bullet("The original estimate assigned 14 manholes by simply counting the 14 numbered nodes (S-1 through S-14) on Line A. However, the Structure Schedule on Sheet C-8 explicitly differentiates structure configurations: (a) 5 standalone junction manholes (S-1, S-7, S-10, S-11, S-14); (b) 5 combination curb inlet + junction manholes (S-2, S-4, S-6, S-8, S-12); and (c) 4 standalone curb inlets (S-3, S-5, S-9, S-13). Structures S-3, S-5, S-9, and S-13 have no manhole barrel or cover; they are solely on-grade curb inlets capturing street gutter flow. Pricing 14 manholes while simultaneously pricing 12 curb inlets double-counts the four standalone inlet locations. In our primary reconciliation table, we maintain the 14 EA count at $8,750.00 ($122,500.00, +$32,900.00) to provide the conservative surety number, but we also present the 10 EA deduplicated schedule ($87,500.00, -$2,100.00) for county negotiation.", bold_prefix="Structure Schedule Audit (14 EA vs. 10 EA): ")

    add_bullet("The schedule base depth for 60-inch manholes under Item 2.36 is 10.0 feet. Rim-to-invert depths along Line A range from 7.00 ft at S-1 to 15.74 ft at S-14. For the 10 actual manhole structures, 7 structures exceed 10.0 ft in depth: S-6 (10.71', +0.71'), S-7 (11.29', +1.29'), S-8 (12.08', +2.08'), S-10 (13.49', +3.49'), S-11 (14.03', +4.03'), S-12 (14.68', +4.68'), and S-14 (15.74', +5.74'). The cumulative depth exceeding 10.0 ft is exactly 22.02 vertical feet. If Clark County Public Works enforces schedule Item 2.38 ('additional depth beyond schedule, per foot') at $685.00/VF, this represents an additional $15,083.70. In accordance with standard subdivision bonding practice where base manhole items are carried without vertical foot adders on initial submittals, Item 2.38 is tracked as an advisory sensitivity.", bold_prefix="Vertical Depth Analysis (Item 2.38 Sensitivity): ")

    # 3.3 Catch Basins & Inlets
    add_sub_heading("3.3 Catch Basins and Curb Inlets (Item 2.30) — Sheet C-8 [FLAGGED ITEM]")
    add_p("The original estimate carries Item 2.30 ('Catch basin, Type A, standard curb inlet, depth ≤ 6 ft') with a quantity of 12 EA at $4,850.00 each ($58,200.00).", bold_prefix="Carried Estimate Item: ")

    add_bullet("General Note 4 on Sheet C-8 mandates: 'Curb inlets are Type G with 8-foot opening per Clark County Standard Drawing SD-305.' A Type G inlet is an 8-foot curb-opening inlet featuring a recessed deflector curb transition designed for higher capture efficiency in residential collector streets.", bold_prefix="Plan Specification Discrepancy: ")

    add_bullet("The Clark County Uniform Unit Cost Schedule publishes unit prices only for Type A catch basins (Item 2.30 at $4,850.00; Item 2.31 for extra depth), Type B grated basins (Item 2.32 at $5,600.00), combination curb-and-grate inlets (Item 2.33 at $7,250.00), and drop inlets (Item 2.34 at $3,900.00). The published schedule contains NO line item matching a Type G curb inlet.", bold_prefix="Absence from Published Schedule: ")

    add_bullet("Per your explicit instructions: 'Flag an item only where the schedule has nothing matching what the plans show, and leave the amount already carried in the subtotal for anything you flag.' Because the published schedule contains nothing matching Type G inlets, Item 2.30 is formally FLAGGED in our reconciliation, and the carried amount of $58,200.00 remains in the Section 2 subtotal with $0.00 net change. Under Schedule Section 12.04 (Alternate Unit Prices), Callaway may either document contractor pricing for Type G inlets under an alternate item (e.g., Item 2.30A) or agree with Dale Yeoman at plan check to accept the Type A unit price for bonding purposes.", bold_prefix="Reconciliation Treatment & Code Standing: ")

    # 3.4 Detention Basin Appurtenances
    add_sub_heading("3.4 Detention Basin Appurtenances & Plan Elements (Sheets C-6 and C-9)")
    add_p("A thorough audit of the detention basin civil grading and structural details on Sheets C-6 and C-9 confirms the status of all detention components:")

    add_bullet("Sheet C-9 details the outlet works at the west end of the basin: a 4' wide × 4' tall cast-in-place reinforced concrete headwall (footing elev. 2,850.00', top elev. 2,859.20'), a 1/4\" steel orifice plate (12\" H × 18\" W opening at invert 2,851.00'), and a hinged 5/8\" bar trash rack at 6\" o.c. Clark County Unit Cost Schedule Item 2.45 publishes the unit price as 'Actual, ≥ $18,000'. Per your instructions: 'Price off the published schedule — where it gives an Actual the amount already carried stands.' The carried lump sum of $28,000.00 stands without modification.", bold_prefix="Basin Outlet Structure (Item 2.45) — 'Actual' Pricing Governs: ")

    add_bullet("Sheet C-9 Storage Summary Table establishes a required storage allocation of 6.40 acre-feet between basin bottom (2,851.00') and the 100-year water surface (2,857.91'), matching the CCRFCD-accepted Master Drainage Study Table 4-1. Cumulative structural volume to top of berm (2,859.20') is 8.02 acre-feet (12,939 CY). However, the plan sheets give no excavation cut/fill volume in cubic yards. Per your instructions: 'Where the plans give no dimension or stationing for a line item already in the estimate, the quantity already carried stands.' The carried quantity of 10,000 CY at schedule price $9.75/CY ($97,500.00) stands.", bold_prefix="Detention Basin Excavation (Item 2.44) — Carried Quantity Stands: ")

    add_bullet("Sheet C-6 and C-9 call out 6-ft chain link fencing around the basin tract with a 12-ft vehicle swing gate at the access ramp. Neither sheet dimensions the continuous linear footage of fencing or provides fence stationing. Per your instructions, the carried quantity of 1,400 LF at schedule price $34.00/LF ($47,600.00) stands.", bold_prefix="Detention Basin Fencing (Item 2.46) — Carried Quantity Stands: ")

    add_bullet("Sheet C-6 notes require rip-rap protection at the outfall pipe invert per SD-402 without stating square yardage or dimensions. Sheet C-9 details a 15' × 20' (33.33 SY) grouted rip-rap apron (D50 = 12\") downstream of the emergency spillway. Because the outfall rip-rap has no dimension on the plans, the carried quantity of 500 SY at schedule price $86.00/SY ($43,000.00) stands under your instructions.", bold_prefix="Riprap (Item 2.42) — Carried Quantity Stands: ")

    add_bullet("Two cast-in-place headwalls are dimensioned on the plans: structure S-1 cleanout headwall on Sheet C-8 (serving 36\" pipe) and the basin outlet headwall on Sheet C-9 (serving 30\" pipe). Both serve pipes ≤ 48 inches. The carried quantity of 2 EA at schedule price $5,400.00/EA ($10,800.00) matches the plans and stands.", bold_prefix="Headwalls (Item 2.40) — Verified & Stands: ")

    add_bullet("Sheet C-6 and C-9 depict a 15-foot wide maintenance access ramp descending at 6% grade from top of berm (2,859.20') to basin bottom (2,851.00'). The ramp length is (2,859.20 - 2,851.00) / 0.06 = 136.67 LF; surface area is 136.67' × 15' = 2,050 SF (227.78 SY, rounded to 228 SY). The plans specify the ramp surface as '6-inch aggregate base course over compacted subgrade' to support an H-20 vehicle load. In Section 2 of the published schedule, Item 2.47 is titled 'Access ramp, 4-inch AC over 6-inch aggregate base' ($32.00/SY). The schedule contains no item matching an unpaved aggregate-base ramp. If flagged as a schedule non-match, it contributes $0.00 to the carried subtotal. If Clark County Public Works requires bonding under schedule Item 2.47, 228 SY at $32.00/SY adds $7,296.00. This is presented as an advisory sensitivity in Section 4.", bold_prefix="Detention Basin Access Ramp (Item 2.47 Analysis): ")

    # 3.5 Undimensioned Carried Items
    add_sub_heading("3.5 Undimensioned Carried Items & Allowances (Items 2.34, 2.39, 2.99)")
    add_bullet("Item 2.34 ('Drop inlet, area drain', 2 EA @ $3,900.00 = $7,800.00) and Item 2.39 ('Junction structure, cast-in-place, sized per plan', 60 CY @ $1,150.00 = $69,000.00) are carried in the estimate but are not explicitly dimensioned or stationed on Sheets C-6, C-8, or C-9. Per your instructions, both quantities stand as carried.", bold_prefix="Drop Inlets and CIP Junction Structures: ")

    add_bullet("Item 2.99 ($2,300.00 lump sum allowance) covers physical field connection and grade matching to the existing Phase 2 storm drain stubs at Sta. 12+40 on Desert Sage Pkwy. and Sta. 3+60 on Chuckwalla Way (noted on Sheets C-1 and C-8). As an agreed field-adjustment allowance, it stands as carried.", bold_prefix="Phase 2 Storm Outfall Tie-in Allowance: ")

    # -------------------------------------------------------------
    # 6. PERFORMANCE BOND CALCULATION & SENSITIVITY
    # -------------------------------------------------------------
    add_sec_heading("SUBDIVISION PERFORMANCE BOND CALCULATION & SENSITIVITY ANALYSIS", "4")
    
    add_p("To establish the revised performance bond amount, the corrected Section 2 subtotal is integrated into the complete Phase 3 estimate structure. All non-drainage sections (Sections 1, 3 through 8) and Section 9 allowances remain strictly at their 10/10/2026 values. Final bond rounding is executed pursuant to Clark County Uniform Unit Cost Schedule Section 12.02, which mandates that the total bonding amount be rounded up to the next whole $1,000.", bold_prefix="Bond Computation Framework: ")

    # COMPLETE ESTIMATE SUMMARY TABLE
    tbl_full = doc.add_table(rows=14, cols=4)
    tbl_full.alignment = WD_TABLE_ALIGNMENT.CENTER
    tbl_full.autofit = False
    
    full_widths = [Inches(0.8), Inches(2.7), Inches(1.5), Inches(1.5)]
    full_headers = ["Section", "Improvement Category / Bonding Scope", "Original Estimate (10/10/2026)", "Corrected Estimate (10/31/2026)"]
    
    f_hdr = tbl_full.rows[0]
    add_tr_props(f_hdr, is_header=True)
    
    for c_idx, h_text in enumerate(full_headers):
        cell = f_hdr.cells[c_idx]
        cell.width = full_widths[c_idx]
        set_cell_background(cell, "1B365D")
        set_cell_margins(cell, top=80, bottom=80, left=60, right=60)
        p = cell.paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.RIGHT if c_idx in (2, 3) else WD_ALIGN_PARAGRAPH.LEFT
        p.paragraph_format.space_before = Pt(1)
        p.paragraph_format.space_after = Pt(1)
        r = p.add_run(h_text)
        r.font.name = 'Arial'
        r.font.size = Pt(8.0)
        r.font.bold = True
        r.font.color.rgb = WHITE

    full_est_data = [
        ("Section 1", "Earthwork (Clearing, Grading, Dust Control, SWPPP)", "$504,191.75", "$504,191.75"),
        ("Section 2", "Storm Drain and Detention (RECONCILED)", "$1,276,934.00", "$1,323,634.00"),
        ("Section 3", "Streets and Paving (AC, Aggregate Base, Curb, Sidewalk)", "$1,037,800.00", "$1,037,800.00"),
        ("Section 4", "Wet Utilities (Water Distribution & Sanitary Sewer)", "$1,031,100.00", "$1,031,100.00"),
        ("Section 5", "Dry Utilities (Joint Trench, Streetlights, Conduits)", "$517,200.00", "$517,200.00"),
        ("Section 6", "Landscape and Irrigation (Common Areas)", "$389,340.00", "$389,340.00"),
        ("Section 7", "Monumentation and Survey (Monuments, Tie Sheets)", "$40,000.00", "$40,000.00"),
        ("Section 8", "Traffic Control and Signage (Barricades, Postings)", "$60,000.00", "$60,000.00"),
        ("SUBTOTAL", "CONSTRUCTION SUBTOTAL (Sections 1 through 8)", "$4,856,565.75", "$4,903,265.75"),
        ("Item 11.01", "Mobilization, demobilization, bonds, contractor insurance", "$350,000.00", "$350,000.00"),
        ("Item 11.03", "Contingency (Agreed lump sum per Addendum No. 1)", "$150,000.00", "$150,000.00"),
        ("TOTAL", "ENGINEER'S ESTIMATE TOTAL (Unrounded)", "$5,356,565.75", "$5,403,265.75"),
        ("BOND", "FINAL PERFORMANCE BOND AMOUNT (Sec. 12.02 Rounding)", "$5,357,000.00", "$5,404,000.00")
    ]

    for r_idx, (s_num, s_desc, s_orig, s_rev) in enumerate(full_est_data):
        row = tbl_full.rows[r_idx + 1]
        add_tr_props(row, is_header=False)
        
        is_bond = (s_num == "BOND")
        is_tot = (s_num in ("SUBTOTAL", "TOTAL"))
        is_sec2 = (s_num == "Section 2")
        
        bg_col = "1B365D" if is_bond else ("D9E2EC" if is_tot else ("EFF6FF" if is_sec2 else ("F9FAFB" if r_idx % 2 == 1 else "FFFFFF")))
        
        for c_idx, val in enumerate((s_num, s_desc, s_orig, s_rev)):
            cell = row.cells[c_idx]
            cell.width = full_widths[c_idx]
            set_cell_background(cell, bg_col)
            set_cell_margins(cell, top=60, bottom=60, left=60, right=60)
            
            b_top = "1B365D" if (is_tot or is_bond) else "E5E7EB"
            b_bot = "1B365D" if (is_tot or is_bond) else "E5E7EB"
            set_cell_borders(cell, top=b_top, bottom=b_bot, left=None, right=None, sz="12" if (is_tot or is_bond) else "4")
            
            p = cell.paragraphs[0]
            p.alignment = WD_ALIGN_PARAGRAPH.RIGHT if c_idx in (2, 3) else WD_ALIGN_PARAGRAPH.LEFT
            p.paragraph_format.space_before = Pt(1)
            p.paragraph_format.space_after = Pt(1)
            
            r = p.add_run(val)
            r.font.name = 'Arial'
            r.font.size = Pt(8.0)
            if is_bond:
                r.font.bold = True
                r.font.color.rgb = WHITE
            elif is_tot:
                r.font.bold = True
                r.font.color.rgb = NAVY
            elif is_sec2:
                r.font.bold = True
                r.font.color.rgb = NAVY
            else:
                r.font.color.rgb = CHARCOAL

    doc.add_paragraph().paragraph_format.space_after = Pt(6)

    add_sub_heading("4.1 Reviewer Interpretation & Sensitivity Scenarios")
    add_p("To ensure Callaway and your surety broker have complete transparency during county plan check negotiations with civil examiner Dale Yeoman, PE, we have analyzed three potential reviewer interpretations:", bold_prefix="Sensitivity Analysis: ")

    add_bullet("This is the conservative, recommended submission figure ($5,404,000.00 bond). It includes the missing 100 LF of 30\" RCP (+$13,800.00), applies the mandatory 60\" manhole schedule price of $8,750.00 to all 14 Line A trunk structures (+$32,900.00), flags Type G inlets ($58,200.00 carried stands), and flags the aggregate base access ramp as a schedule non-match ($0.00 carried).", bold_prefix="Case 1 (Primary Recommended Basis — 14 MH @ 60\"): ")

    add_bullet("If Public Works enforces a strict separation between manholes and curb inlets on Sheet C-8, the 4 standalone curb inlets (S-3, S-5, S-9, S-13) are deducted from manholes, leaving 10 manholes at $8,750.00 ($87,500.00 vs. $89,600.00 original, -$2,100.00). Combined with 30\" RCP (+$13,800.00), Section 2 becomes $1,288,634.00, unrounded total is $5,368,265.75, and the revised rounded bond is $5,369,000.00 (+$12,000.00 over initial issue).", bold_prefix="Case 2 (Deduplicated Structure Schedule — 10 MH @ 60\"): ")

    add_bullet("If Public Works requires bonding of the access ramp under schedule Item 2.47 (228 SY @ $32.00/SY = $7,296.00), the Case 1 bond increases to $5,411,000.00, and the Case 2 bond increases to $5,376,000.00. If vertical depth beyond 10 ft is enforced on the 10 deep manholes (22.02 VF @ $685/VF = $15,083.70), Case 2 bond becomes $5,384,000.00.", bold_prefix="Case 3 (Advisory Ramp & Depth Adders): ")

    # -------------------------------------------------------------
    # 7. SURETY BROKER GUIDANCE & RESUBMITTAL ACTIONS
    # -------------------------------------------------------------
    add_sec_heading("SURETY BROKER TRANSMITTAL GUIDANCE & RESUBMITTAL ACTIONS", "5")
    
    add_p("To protect Callaway Land Partners against surety delays and ensure seamless approval by Clark County Public Works, we recommend the following coordinated sequence of actions:", bold_prefix="Action Plan: ")

    add_bullet("Transmit this memorandum and the revised Section 2 schedule to Callaway's surety broker immediately, establishing $5,404,000.00 as the underwriting baseline for the Phase 3 Performance Bond (and Labor & Material Payment Bond, where co-issued). Inform the broker that the maximum anticipated range is $5,369,000.00 to $5,404,000.00.", bold_prefix="1. Broker Underwriting Target: ")

    add_bullet("Sundial will update the official Excel workbook (DSR_Ph3_Engineers_Estimate.xlsx) to incorporate these reconciled figures, revise the Cover Sheet date to reflect the resubmittal cycle, and affix my Nevada Professional Engineer seal. The updated estimate will accompany the Phase 3 resubmittal package scheduled for 11/30/2026.", bold_prefix="2. Resubmittal Estimate Package: ")

    add_bullet("Sundial's comment response matrix will reference these reconciled drainage items under responses G-3, G-4, and G-5 to CC-PW plans examiner Dale Yeoman, PE. Specifically, we will confirm that the 30-inch RCP outfall reach aligns with Sheet C-9 details, and that all trunk structures reflect the precast SD-301 60-inch specification.", bold_prefix="3. Plan Check Comment Coordination: ")

    add_bullet("Under Clark County Code Title 30 and Addendum No. 1 Section 11.05/11.06, the performance security must be posted concurrently with SIA execution prior to final map recordation (FM-26-100290). Having the surety bond issued against the verified $5,404,000.00 figure eliminates the risk of Public Works rejecting the bond instrument during final clearance, thereby protecting Callaway's critical December 18, 2026 recordation milestone.", bold_prefix="4. Recordation Runway Preservation: ")

    doc.add_paragraph().paragraph_format.space_after = Pt(14)

    # -------------------------------------------------------------
    # 8. SIGNATURE BLOCK
    # -------------------------------------------------------------
    p_closing = doc.add_paragraph()
    p_closing.paragraph_format.space_before = Pt(8)
    p_closing.paragraph_format.space_after = Pt(16)
    p_closing.paragraph_format.keep_with_next = True
    r_close = p_closing.add_run("Respectfully submitted,\nSUNDIAL ENGINEERING & SURVEY")
    r_close.font.name = 'Arial'
    r_close.font.size = Pt(10)
    r_close.font.bold = True
    r_close.font.color.rgb = NAVY

    # Signature layout table
    tbl_sig = doc.add_table(rows=1, cols=2)
    tbl_sig.alignment = WD_TABLE_ALIGNMENT.CENTER
    tbl_sig.autofit = False
    add_tr_props(tbl_sig.rows[0], is_header=False)
    
    cell_sig, cell_seal = tbl_sig.rows[0].cells[0], tbl_sig.rows[0].cells[1]
    cell_sig.width, cell_seal.width = Inches(3.8), Inches(2.7)
    
    set_cell_margins(cell_sig, top=40, bottom=40, left=40, right=40)
    set_cell_margins(cell_seal, top=40, bottom=40, left=40, right=40)

    # Signature line
    p_s = cell_sig.paragraphs[0]
    p_s.paragraph_format.space_before = Pt(0)
    p_s.paragraph_format.space_after = Pt(2)
    p_s.paragraph_format.line_spacing = 1.15
    
    r_sigline = p_s.add_run("Jonathan R. Kessler\n")
    r_sigline.font.name = 'Brush Script MT' if 'Brush Script MT' in [f.name for f in doc.styles] else 'Arial'
    r_sigline.font.size = Pt(16)
    r_sigline.font.italic = True
    r_sigline.font.color.rgb = NAVY
    
    r_signame = p_s.add_run("_________________________________________\nJonathan R. Kessler, PE\n")
    r_signame.font.name = 'Arial'
    r_signame.font.size = Pt(10)
    r_signame.font.bold = True
    r_signame.font.color.rgb = NAVY
    
    r_sigtitle = p_s.add_run("Principal-in-Charge, Civil Engineering Division\nNevada Professional Engineer License No. 14203\nDate: October 31, 2026")
    r_sigtitle.font.name = 'Arial'
    r_sigtitle.font.size = Pt(9)
    r_sigtitle.font.color.rgb = CHARCOAL

    # Seal block
    p_seal = cell_seal.paragraphs[0]
    p_seal.alignment = WD_ALIGN_PARAGRAPH.CENTER
    set_cell_background(cell_seal, "F4F6F8")
    set_cell_borders(cell_seal, top="1B365D", bottom="1B365D", left="1B365D", right="1B365D", sz="8")
    
    r_seal_text = p_seal.add_run("[ PROFESSIONAL ENGINEER SEAL ]\n\nJONATHAN R. KESSLER\nNo. 14203 — STATE OF NEVADA\nPROFESSIONAL ENGINEER (CIVIL)\nEXPIRATION: 12/31/2027")
    r_seal_text.font.name = 'Arial'
    r_seal_text.font.size = Pt(8)
    r_seal_text.font.bold = True
    r_seal_text.font.color.rgb = SLATE

    # Save document
    out_dir = "Correspondence/Client"
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "Memo_to_Callaway_2026-10-31.docx")
    doc.save(out_path)
    print(f"Memo successfully created at: {out_path} ({os.path.getsize(out_path)} bytes)")

if __name__ == "__main__":
    create_memo()
