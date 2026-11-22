#!/usr/bin/env python3
"""Generate Bramwick_Commons_Screening_Memo.docx — the SRP-3 Rev 3 supplemental
review memo of record that supersedes Bramwick_Commons_Screening_Memo_v1.docx."""
from docx import Document
from docx.shared import Pt, Inches, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

doc = Document()

# ---- base style ----
style = doc.styles['Normal']
style.font.name = 'Calibri'
style.font.size = Pt(11)
style.paragraph_format.space_after = Pt(6)
style.paragraph_format.line_spacing = 1.08

def set_cell_border(cell, **kwargs):
    tc = cell._tc
    tcPr = tc.get_or_add_tcPr()
    tcBorders = OxmlElement('w:tcBorders')
    for edge in ('top','left','bottom','right'):
        if edge in kwargs:
            b = OxmlElement(f'w:{edge}')
            b.set(qn('w:val'), 'single')
            b.set(qn('w:sz'), str(kwargs[edge]))
            b.set(qn('w:color'), '808080')
            tcBorders.append(b)
    tcPr.append(tcBorders)

def shade(cell, fill):
    tcPr = cell._tc.get_or_add_tcPr()
    sh = OxmlElement('w:shd')
    sh.set(qn('w:val'),'clear'); sh.set(qn('w:color'),'auto'); sh.set(qn('w:fill'),fill)
    tcPr.append(sh)

def para(text='', bold=False, italic=False, size=None, align=None, space_after=None, space_before=None):
    p = doc.add_paragraph()
    if align: p.alignment = align
    if space_after is not None: p.paragraph_format.space_after = Pt(space_after)
    if space_before is not None: p.paragraph_format.space_before = Pt(space_before)
    if text:
        r = p.add_run(text); r.bold=bold; r.italic=italic
        if size: r.font.size = Pt(size)
    return p

def runs(p, items):
    for text,bold,italic in items:
        r=p.add_run(text); r.bold=bold; r.italic=italic
    return p

def heading(text, size=12):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(10); p.paragraph_format.space_after = Pt(4)
    r = p.add_run(text); r.bold=True; r.font.size=Pt(size)
    r.font.color.rgb = RGBColor(0x1F,0x38,0x64)
    return p

def kv_table(rows, widths=(2.7, 3.8)):
    t = doc.add_table(rows=0, cols=2)
    t.alignment = WD_TABLE_ALIGNMENT.CENTER
    for k,v in rows:
        cells = t.add_row().cells
        cells[0].text=''; cells[1].text=''
        rp = cells[0].paragraphs[0]; rr=rp.add_run(k); rr.bold=True; rr.font.size=Pt(10)
        vp = cells[1].paragraphs[0]; vr=vp.add_run(v); vr.font.size=Pt(10)
        for c in cells:
            set_cell_border(c, top=4,bottom=4,left=4,right=4)
            shade(c,'F2F2F2' if False else 'FFFFFF')
        shade(cells[0],'F2F2F2')
    for i,row in enumerate(t.rows):
        row.cells[0].width=Inches(widths[0]); row.cells[1].width=Inches(widths[1])
    return t

def grid_table(header, rows, widths=None, header_fill='1F3864'):
    t = doc.add_table(rows=1, cols=len(header))
    t.alignment = WD_TABLE_ALIGNMENT.CENTER
    hcells = t.rows[0].cells
    for i,h in enumerate(header):
        hcells[i].text=''
        p=hcells[i].paragraphs[0]; r=p.add_run(str(h)); r.bold=True; r.font.size=Pt(10)
        r.font.color.rgb=RGBColor(0xFF,0xFF,0xFF)
        shade(hcells[i], header_fill)
        set_cell_border(hcells[i], top=6,bottom=6,left=6,right=6)
    for row in rows:
        cells=t.add_row().cells
        for i,val in enumerate(row):
            cells[i].text=''
            p=cells[i].paragraphs[0]; r=p.add_run(str(val)); r.font.size=Pt(10)
            set_cell_border(cells[i], top=4,bottom=4,left=4,right=4)
    if widths:
        for r_ in t.rows:
            for i,w in enumerate(widths):
                r_.cells[i].width=Inches(w)
    return t

# ============================ HEADER ============================
p = para('Alleniom Utilities — DER Program Office', bold=True, size=14, align=WD_ALIGN_PARAGRAPH.LEFT)
para('4200 Veldmere Boulevard, Halston, Alleron 01HA · (612) 555-0100 · alleniom.com',
     size=9, space_after=8)

# doc control table
dc = doc.add_table(rows=1, cols=4)
dc.alignment = WD_TABLE_ALIGNMENT.CENTER
hdr = ['Doc no.', 'Rev', 'Date', 'Owner']
vals = ['IS-BRAM-2025-07-14', 'v2', '07/14/2025', 'Interconnection Studies']
for i,(h,v) in enumerate(zip(hdr,vals)):
    c = dc.rows[0].cells[i]; c.text=''
    pp=c.paragraphs[0]; r1=pp.add_run(h+'\n'); r1.bold=True; r1.font.size=Pt(9); r1.font.color.rgb=RGBColor(0xFF,0xFF,0xFF)
    r2=pp.add_run(v); r2.font.size=Pt(9); r2.font.color.rgb=RGBColor(0xFF,0xFF,0xFF)
    shade(c,'1F3864'); set_cell_border(c,top=6,bottom=6,left=6,right=6)
sup = dc.add_row().cells
sup_text = 'Supersedes: IS-BRAM-2025-06-25 v1  ·  File: Bramwick_Commons_Screening_Memo_v1.docx  (countersigned 06/25/2025)'
c = sup[0]; c.merge(sup[1]).merge(sup[2]).merge(sup[3])
c.text=''; pp=c.paragraphs[0]; r=pp.add_run(sup_text); r.italic=True; r.font.size=Pt(9)
shade(c,'F2F2F2'); set_cell_border(c,top=6,bottom=6,left=6,right=6)

para('', space_after=2)
para('SUPPLEMENTAL REVIEW SCREEN DETERMINATION — SCREEN D (100%-OF-MINIMUM-LOAD FOR SOLAR): '
     'RECOMPUTATION AND SUPERSESSION', bold=True, size=12, space_before=4, space_after=8)

# To/From/Date/Subject
for lbl,txt in [('To:  ','Meera Vellanki, Manager, Interconnection Studies'),
                ('From:  ','Priya Ranganathan, Staff Analyst, Interconnection Studies'),
                ('Date:  ','07/14/2025'),
                ('Subject:  ','Bramwick Commons Solar (1.8 MW, Feeder ALN-214) — Supplemental Review '
                             'Screen D determination; supersession of IS-BRAM-2025-06-25 v1')]:
    p=doc.add_paragraph(); r=p.add_run(lbl); r.bold=True; r2=p.add_run(txt)
    p.paragraph_format.space_after=Pt(2)

# Headline disposition (call made one way or the other, stated up front)
hp = doc.add_paragraph()
hp.paragraph_format.space_before=Pt(8); hp.paragraph_format.space_after=Pt(8)
hr = hp.add_run('Disposition (headline):  ')
hr.bold=True; hr.font.size=Pt(11); hr.font.color.rgb=RGBColor(0x1F,0x38,0x64)
hb = hp.add_run('Screen D recomputed on the ALN-214 AMI record (15-min, 12 months, daytime window '
               '10:00–16:00) yields a daytime-window minimum of 2.4 MW. 1.8 MW requested ≤ 2.4 MW — '
               'Screen D PASSES. The earlier memo IS-BRAM-2025-06-25 v1 used the absolute overnight '
               'minimum (1.1 MW), which SRP-3 §4 prohibits; its FAILED determination is reversed and v1 '
               'is superseded. Application advances without a study agreement on the Screen D basis, '
               'subject to the balance of the DIS-01 evaluation.')
hb.font.size=Pt(10.5)

# ============================ 1. PROJECT ============================
heading('1. Project')
kv_table([
    ('Applicant', 'Bramwick Commons Solar LLC'),
    ('Project', 'Bramwick Commons Solar'),
    ('Requested capacity', '1.8 MW (1,800 kW)'),
    ('Point of interconnection', 'Feeder ALN-214 (Larkspur Ridge substation, 12.47 kV)'),
    ('Resource type', 'Solar photovoltaic — pure generation (front-of-meter)'),
    ('DER class (DIS-01 §3 / Table 3-1)', 'Medium-scale, 1 MW–5 MW'),
    ('Application status (07/14/2025)', 'Pre-application dialogue tracked under Distribution Planning '
        'correspondence; not present in the Active Queue or On-Hold Queue as of 07/14/2025'),
])

p = doc.add_paragraph()
p.paragraph_format.space_before=Pt(6)
runs(p, [
 ('The application was routed to supplemental review following failure of the initial fast-track '
  '100%-of-minimum-load screen. The prior memo, IS-BRAM-2025-06-25 v1 (Bramwick_Commons_Screening_Memo_'
  'v1.docx, dated 06/25/2025 and countersigned), recorded a FAILED determination using a feeder minimum '
  'load of 1.1 MW. This memo recomputes Screen D under SRP-3 Rev 3 §4 directly on the ALN-214 AMI '
  'interval record and against the DER Program records as they stand at 07/14/2025, and supersedes v1 '
  'where the two determinations disagree, as §4 and §6(f) require.', False, False),
])

# ============================ 2. SCREEN APPLIED ============================
heading('2. Screen applied')
para('Screen D — 100%-of-minimum-load screen for solar, per §4 of SRP-3 (Rev 3, effective 02/10/2025). '
     'Under this screen the requested solar DER capacity is compared to the minimum load within the '
     'daytime window 10:00–16:00, determined from feeder AMI interval data. The absolute overnight '
     'minimum shall NOT be used. The requested capacity must be ≤ the daytime-window minimum for the '
     'site to pass. §4 further provides that feeder minimum-load figures produced for other purposes '
     '(planning studies, hosting-capacity map inputs, protection coordination) are not substitutes for '
     'the value computed under §4, and that where a prior supplemental review memo on the same feeder '
     'applied a different minimum-load basis, the reviewer shall recompute the value under §4 and, if '
     'the two disagree, supersede the earlier memo in the file.')

# ============================ 3. AUTHORITATIVE SOURCES ============================
heading('3. Authoritative sources reviewed (SRP-3 §5)')
para('(a) Feeder AMI interval data — ALN-214_AMI_Interval_Load_Export.xlsx (Alleniom AMI Data Warehouse '
     'standing export; 15-minute feeder-aggregate interval load, kW; as of 07/2025). Sole authoritative '
     'source for the Screen D minimum-load determination per §5(a).')
para('(c) DER queue — 2025-07-14 Active Queue Report and 2025-07-14 On-Hold Queue Report (DER Program '
     'Office, source ICQ); Existing-DER Register Extract, Abnormality Hold List, Standards Conflict Hold '
     'List, and SOC PTO-Hold Log, each as of 07/14/2025. Used for the Screen A aggregate-penetration '
     'cross-check and the queue-status reconciliation in §6.')
para('Hosting Capacity Map HCM-2024-Q2 (published 05/15/2024) — published available capacity for ALN-214. '
     'Reported for the Screen A/penetration cross-check only; per §4 it is a planning input and is not a '
     'substitute for the AMI daytime-window minimum.')

# ============================ 4. SCREEN D ANALYSIS ============================
heading('4. Screen D analysis (SRP-3 §4 / §6(c))')
kv_table([
    ('Subject feeder', 'ALN-214 (Larkspur Ridge, 12.47 kV)'),
    ('Data source', 'Alleniom AMI Data Warehouse — feeder-aggregate 15-minute interval data (standing export)'),
    ('Data window', '07/01/2024 00:00 – 06/30/2025 23:45 — the most recent complete twelve (12) calendar '
                     'months (Jul 2024–Jun 2025) as of the 07/14/2025 evaluation'),
    ('Interval cadence', 'Fifteen (15) minutes — aligned to the feeder AMI collection cadence'),
    ('Total intervals in window', '35,040 (365 days × 96) — complete; no missing intervals, no days short of 96'),
    ('Daytime window evaluated', 'Intervals whose start time falls within 10:00–16:00 (start 10:00 through 15:45)'),
    ('Daytime intervals evaluated', '8,760 (24 per day × 365 days)'),
    ('Interval exclusions', 'None. No known feeder outages, load transfers, or planned switching on ALN-214 '
        'are recorded in the DER Program records as of 07/14/2025; the AMI record contains no zero or '
        'non-positive load values and no missing intervals. No intervals excluded.'),
    ('Daytime-window minimum load', '2,400 kW (2.4 MW), occurring 2025-02-12 at 11:30'),
    ('Daytime mean / max (context)', '5,300 kW mean; 8,526 kW max (2024-08-01 13:30)'),
    ('Absolute overnight minimum (NOT used)', '1,100 kW (1.1 MW) at 2025-03-23 03:45 — the absolute feeder '
        'minimum; §4 prohibits its use for this screen and it is recorded here only to identify the value '
        'carried into v1'),
])
para('')
para('Seasonal context: monthly daytime-window minima ranged from 2.4 MW (Feb 2025) to 5.0 MW (Jul 2024), '
     'a normal winter-low / summer-high pattern. The 12-month daytime-window minimum (2.4 MW) occurs in '
     'the winter low-load month, as expected for a solar screen.', italic=True, size=10)

# ============================ 5. COMPARISON ============================
heading('5. Comparison (Screen D)')
para('1.8 MW requested is ≤ the 2.4 MW daytime-window minimum load — Screen D PASSED. The requested '
     'capacity equals 75% of the daytime-window minimum; the residual margin is 0.6 MW (600 kW).')
grid_table(['Requested capacity', 'Daytime-window minimum load (§4)', 'Margin', 'Result'],
           [['1.8 MW', '2.4 MW', '0.6 MW', 'PASS']],
           widths=[1.7, 2.6, 1.0, 1.0])

# ============================ 6. REVIEW OF EARLIER MEMO / RECORDS ============================
heading('6. Review of the earlier memo and reconciliation with DER Program records (07/14/2025)')

para('6.1  Error in the earlier memo\u2019s Screen D basis.', bold=True, space_after=2)
para('v1 used a feeder minimum load of 1.1 MW. That figure is the absolute overnight minimum on the '
     'ALN-214 AMI record (1,100 kW at 03:45 on 2025-03-23). SRP-3 §4 requires the daytime-window (10:00–16:00) '
     'minimum and states that the absolute overnight minimum shall NOT be used. The daytime-window minimum '
     'recomputed on the same record is 2.4 MW, which disagrees with the 1.1 MW used in v1. v1 also recorded '
     'a sixty-(60)-minute cadence and a data window of 06/24/2024–06/24/2025; the actual AMI export is '
     '15-minute cadence over 07/01/2024–06/30/2025. The recomputation uses the export as it stands.')

para('6.2  Supersession of v1.', bold=True, space_after=2)
para('Per §4 (final paragraph) and §6(f), where a prior supplemental review memo on the same feeder has '
     'applied a different minimum-load basis and the recomputed value disagrees, the reviewer shall '
     'supersede the earlier memo in the file. IS-BRAM-2025-06-25 v1 is superseded by this memo. v1 shall be '
     'flagged in the file and a cross-reference to this memo added to its cover.')

para('6.3  DER Program records as of 07/14/2025 (Screen A cross-check and queue reconciliation).', bold=True, space_after=2)
grid_table(['Record (as of 07/14/2025)', 'Finding for ALN-214 / Bramwick Commons Solar'],
   [['Existing-DER Register Extract', 'No DER site on ALN-214 (Larkspur Ridge).'],
    ['Active Queue Report', 'No project on feeder ALN-214; no Bramwick Commons Solar entry.'],
    ['On-Hold Queue Report', 'No Bramwick Commons Solar entry.'],
    ['Abnormality Hold List', 'No ALN-214 / Bramwick flag.'],
    ['Standards Conflict Hold List', 'No ALN-214 / Bramwick entry.'],
    ['SOC PTO-Hold Log', 'No ALN-214 site.'],
    ['Hosting Capacity Map HCM-2024-Q2', 'ALN-214 published available 4.9 MW, Pure Generation, last study 12/2023. '
        'Row note identifies ALN-214 as the POI for the Bramwick Commons Solar pre-application dialogue tracked '
        'under Distribution Planning correspondence.']],
   widths=[2.6, 3.9])
para('')
para('Aggregate nameplate DER on ALN-214 (existing + queued + requested) = 0 + 0 + 1.8 MW = 1.8 MW, below '
     'the 4.9 MW published available capacity. No Screen A (aggregate penetration) impediment is raised by '
     'the records. (The 4.9 MW figure is a planning input and, per §4, is not a substitute for the AMI '
     'daytime minimum; it is reported here only for the penetration cross-check. The numeric DIS-01 '
     'penetration threshold is not separately published in the materials on file.)', space_after=4)
para('Bramwick Commons Solar is a pre-application dialogue, not a queued PXA record as of 07/14/2025. The '
     'v1 disposition to "hold advancement of the PXA record" and to "return the supplemental review file to '
     'the Interconnection Studies queue with a failed-screen flag" therefore has no corresponding queue '
     'entry to act on; on the corrected record no failed-screen flag and no Study-Agreement hold should '
     'attach to ALN-214 or to Bramwick Commons Solar.')

# ============================ 7. DETERMINATIONS ============================
heading('7. Determinations (each with basis and call)')
grid_table(['Determination', 'Basis relied on', 'Call'],
   [['Screen D — 100%-of-minimum-load for solar (§4)',
     'Daytime-window minimum 2.4 MW from 15-min AMI, 12 calendar months (Jul 2024–Jun 2025), 8,760 '
     'daytime intervals (10:00–16:00), no exclusions. 1.8 MW ≤ 2.4 MW (75% of minimum; 0.6 MW margin).',
     'PASS'],
    ['Screen A cross-check — aggregate DER penetration on ALN-214 (§3)',
     'DER records of 07/14/2025: existing 0, queued 0, requested 1.8 MW → 1.8 MW aggregate; below 4.9 MW '
     'published available; no other DER on the feeder.',
     'No impediment on the record'],
    ['Earlier memo IS-BRAM-2025-06-25 v1',
     'Used the absolute overnight minimum (1.1 MW), which §4 prohibits; recomputed daytime minimum '
     '(2.4 MW) disagrees; §4/§6(f) require supersession. Metadata (60-min cadence; 06/24–06/24 window) '
     'inconsistent with the AMI export.',
     'SUPERSEDED'],
    ['Screens B, C, E (voltage/flicker, short-circuit, reverse power)',
     'Not the subject of the supplemental routing recorded in v1 (the 100%-of-minimum-load screen); no '
     'planning-study, short-circuit, or reverse-power data were part of v1 or of this recomputation. '
     'Remain subject to the balance of the DIS-01 evaluation (§3 — pass is necessary, not sufficient).',
     'Not determined in this re-review']],
   widths=[1.9, 3.6, 1.0])

# ============================ 8. DISPOSITION ============================
heading('8. Disposition (SRP-3 §6(d))')
for b in [
   'Screen D PASSED — the application advances without a study agreement on the Screen D basis. A Study '
   'Agreement is not required on the 100%-of-minimum-load screen; v1\u2019s contrary recommendation is reversed.',
   'Supersede and flag IS-BRAM-2025-06-25 v1 in the file; add a cross-reference to this memo on the v1 '
   'cover (§6, final paragraph).',
   'Clear the failed-screen flag on Feeder ALN-214 and on the Bramwick Commons Solar record; do not attach '
   'a Study-Agreement hold. (As of 07/14/2025 there is no Bramwick PXA record in the Active or On-Hold '
   'queue to hold in any event.)',
   'The application remains subject to the balance of the DIS-01 evaluation — protection per DPS-07 and '
   'telemetry per TCS-02 (utility RTU/SCADA required for ≥500 kW; Permission to Operate only on live '
   'telemetry) — before interconnection. Passing Screen D is necessary but not sufficient (SRP-3 §3).',
   'Because Bramwick Commons Solar is a pre-application dialogue rather than a queued application as of '
   '07/14/2025, this corrected Screen D determination should accompany the application when it is filed '
   'as a complete application and given a queue position. The PASS determination does not by itself '
   'establish queue position or interconnection approval.',
   'File this memo to the interconnection application record (and the Distribution Planning pre-application '
   'correspondence) within five (5) business days of screen completion per §6.',
]:
    p=doc.add_paragraph(style='List Bullet'); p.add_run(b).font.size=Pt(10.5)

# ============================ 9. IDENTIFIERS ============================
heading('9. Memo identifiers and supersession (SRP-3 §6(f))')
kv_table([
    ('Superseded memo', 'IS-BRAM-2025-06-25 v1 — Bramwick_Commons_Screening_Memo_v1.docx '
        '(06/25/2025; countersigned by Meera Vellanki, Manager, Interconnection Studies)'),
    ('Superseding memo', 'IS-BRAM-2025-07-14 v2 — this memo (07/14/2025)'),
    ('Reference standard', 'SRP-3 Rev 3 §4 (Supplemental Review Procedure, effective 02/10/2025); '
        'cross-references DIS-01 Rev 4 §4 and Table 3-1, DPS-07 Rev 2, TCS-02'),
])

# ============================ SIGNATURES ============================
para('', space_after=6)
para('Signed:', bold=True, space_after=0)
para('/s/ Priya Ranganathan', space_after=0)
para('Priya Ranganathan', space_after=0)
para('Staff Analyst, Interconnection Studies', space_after=0)
para('Alleniom Utilities · priya.ranganathan@alleniom.com', space_after=0)
para('07/14/2025', space_after=8)

para('Reviewed by:', bold=True, space_after=0)
para('____________________________________     Date: ____________', space_after=0)
para('Meera Vellanki', space_after=0)
para('Manager, Interconnection Studies', space_after=0)
para('Alleniom Utilities · meera.vellanki@alleniom.com', space_after=8)

para('File: /DER_Program/Studies/Bramwick_Commons_Screen_Memo.docx', size=9, space_after=0)
para('Reference standard: SRP-3 Rev 3 §4 (Supplemental Review Procedure)', size=9, space_after=0)
para('Data of record: ALN-214_AMI_Interval_Load_Export.xlsx (Alleniom AMI Data Warehouse, as of 07/2025); '
    'DER Program records as of 07/14/2025.', size=9, space_after=0)

doc.save('/filesystem/Studies/Bramwick_Commons_Screen_Memo.docx')
print('WROTE /filesystem/Studies/Bramwick_Commons_Screen_Memo.docx')
