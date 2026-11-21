import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL
from docx.oxml import OxmlElement, parse_xml
from docx.oxml.ns import qn, nsdecls

def create_element(name):
    return OxmlElement(name)

def set_cell_background(cell, fill_hex):
    tcPr = cell._tc.get_or_add_tcPr()
    shd = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{fill_hex}"/>')
    tcPr.append(shd)

def set_cell_margins(cell, top=100, bottom=100, left=150, right=150):
    tcPr = cell._tc.get_or_add_tcPr()
    tcMar = OxmlElement('w:tcMar')
    for m, val in [('top', top), ('bottom', bottom), ('left', left), ('right', right)]:
        node = OxmlElement(f'w:{m}')
        node.set(qn('w:w'), str(val))
        node.set(qn('w:type'), 'dxa')
        tcMar.append(node)
    tcPr.append(tcMar)

def set_table_borders(table, color="D3D3D3"):
    tblPr = table._tbl.tblPr
    borders = parse_xml(f'''
        <w:tblBorders {nsdecls("w")}>
            <w:top w:val="single" w:sz="4" w:space="0" w:color="{color}"/>
            <w:bottom w:val="single" w:sz="4" w:space="0" w:color="{color}"/>
            <w:insideH w:val="single" w:sz="4" w:space="0" w:color="{color}"/>
            <w:left w:val="none"/>
            <w:right w:val="none"/>
            <w:insideV w:val="none"/>
        </w:tblBorders>
    ''')
    tblPr.append(borders)

doc = docx.Document()

# Set standard margins (1 inch)
for section in doc.sections:
    section.top_margin = Inches(1.0)
    section.bottom_margin = Inches(1.0)
    section.left_margin = Inches(1.0)
    section.right_margin = Inches(1.0)

# Colors
COLOR_PRIMARY = RGBColor(26, 54, 93)     # Deep Navy
COLOR_SECONDARY = RGBColor(74, 85, 104)  # Slate Gray
COLOR_BODY = RGBColor(45, 55, 72)        # Charcoal
COLOR_RED = RGBColor(155, 44, 44)        # Deep Red / Alert
COLOR_MUTED = RGBColor(113, 128, 150)    # Muted Gray

# Style base
normal_style = doc.styles['Normal']
normal_style.font.name = 'Calibri'
normal_style.font.size = Pt(10.5)
normal_style.font.color.rgb = COLOR_BODY
normal_style.paragraph_format.line_spacing = 1.15
normal_style.paragraph_format.space_after = Pt(4)

# Header block / Utility Letterhead
header_p = doc.add_paragraph()
header_p.alignment = WD_ALIGN_PARAGRAPH.CENTER
header_p.paragraph_format.space_after = Pt(1)
run_header_main = header_p.add_run("ALLENIOM UTILITIES")
run_header_main.bold = True
run_header_main.font.size = Pt(14)
run_header_main.font.color.rgb = COLOR_PRIMARY

subhead_p = doc.add_paragraph()
subhead_p.alignment = WD_ALIGN_PARAGRAPH.CENTER
subhead_p.paragraph_format.space_after = Pt(3)
run_subhead = subhead_p.add_run("DISTRIBUTION OPERATIONS · DER PROGRAM OFFICE · COMMISSIONING")
run_subhead.bold = True
run_subhead.font.size = Pt(9.5)
run_subhead.font.color.rgb = COLOR_SECONDARY

address_p = doc.add_paragraph()
address_p.alignment = WD_ALIGN_PARAGRAPH.CENTER
address_p.paragraph_format.space_after = Pt(14)
run_address = address_p.add_run("4200 Veldmere Boulevard, Halston, Alleron 01HA  |  (612) 555-0100  |  alleniom.com")
run_address.font.size = Pt(8.5)
run_address.font.color.rgb = COLOR_MUTED

# Divider line
div_p = doc.add_paragraph()
div_p.paragraph_format.space_after = Pt(12)
pBdr = parse_xml(f'<w:pBdr {nsdecls("w")}><w:bottom w:val="single" w:sz="12" w:space="1" w:color="1A365D"/></w:pBdr>')
div_p._p.get_or_add_pPr().append(pBdr)

# Date & Metadata Block
meta_table = doc.add_table(rows=1, cols=2)
meta_table.alignment = WD_TABLE_ALIGNMENT.CENTER
meta_table.autofit = False
meta_table.columns[0].width = Inches(4.0)
meta_table.columns[1].width = Inches(2.5)

cell_l = meta_table.cell(0, 0)
cell_r = meta_table.cell(0, 1)

p_date = cell_l.paragraphs[0]
p_date.paragraph_format.space_after = Pt(2)
r_date = p_date.add_run("July 14, 2025")
r_date.bold = True
r_date.font.size = Pt(10.5)

p_recip = cell_l.add_paragraph()
p_recip.paragraph_format.space_after = Pt(0)
r_recip = p_recip.add_run(
    "Imogen Strathe, Project Manager\n"
    "Halbray Community Solar LP\n"
    "6120 Halbray Road\n"
    "Kelloway Township, Alleron 07KT\n"
    "Project Office: (612) 555-0784"
)
r_recip.font.size = Pt(10)

p_ref = cell_r.paragraphs[0]
p_ref.paragraph_format.space_after = Pt(0)
r_ref = p_ref.add_run(
    "PROJECT RECORDS FILE:\n"
    "Project: Halbray Field Solar Site 3\n"
    "Application: PXA-2024-0002\n"
    "Agreement: ISA-Halbray-Field-Site-3\n"
    "Interconnection: Feeder ALN-159 (13.2 kV)\n"
    "AHJ Permit: EP-25-0418 (Kelloway Twp)\n"
    "Checklist Doc: CX-HB-03, Rev 0"
)
r_ref.font.size = Pt(8.5)
r_ref.font.color.rgb = COLOR_SECONDARY

# Spacing before subject
doc.add_paragraph().paragraph_format.space_after = Pt(4)

# Subject Line Box
subj_table = doc.add_table(rows=1, cols=1)
subj_table.alignment = WD_TABLE_ALIGNMENT.CENTER
subj_table.autofit = False
subj_table.columns[0].width = Inches(6.5)
subj_cell = subj_table.cell(0, 0)
set_cell_background(subj_cell, "F0F4F8")
set_cell_margins(subj_cell, top=120, bottom=120, left=180, right=180)
tcPr = subj_cell._tc.get_or_add_tcPr()
borders = parse_xml(f'<w:tcBorders {nsdecls("w")}><w:left w:val="single" w:sz="24" w:color="1A365D"/><w:top w:val="none"/><w:right w:val="none"/><w:bottom w:val="none"/></w:tcBorders>')
tcPr.append(borders)

subj_p = subj_cell.paragraphs[0]
subj_p.paragraph_format.space_after = Pt(0)
r_subj_bold = subj_p.add_run("SUBJECT: ")
r_subj_bold.bold = True
r_subj_bold.font.size = Pt(10.5)
r_subj_bold.font.color.rgb = COLOR_PRIMARY
r_subj_text = subj_p.add_run(
    "DETERMINATION ON PRE-PTO BACKFEED REQUEST (07/29/2025 TARGET DATE)\n"
    "Halbray Field Solar Site 3 (PXA-2024-0002), Feeder ALN-159 — Review as of 07/14/2025"
)
r_subj_text.bold = True
r_subj_text.font.size = Pt(10.5)
r_subj_text.font.color.rgb = COLOR_PRIMARY

p_spacing = doc.add_paragraph()
p_spacing.paragraph_format.space_after = Pt(6)

# Salutation
p_salut = doc.add_paragraph()
p_salut.paragraph_format.space_after = Pt(6)
r_salut = p_salut.add_run("Dear Ms. Strathe:")
r_salut.font.size = Pt(10.5)

print("Setup completed successfully.")
