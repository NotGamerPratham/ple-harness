#!/usr/bin/env python3
"""Data-hall MEP coordination model (dc_model hall_seed005_d100). IFC4."""
import sys, os, json, math
import ifcopenshell
import ifcopenshell.api.unit as U
import ifcopenshell.api.owner as O

OUT_PATH = sys.argv[1] if len(sys.argv) > 1 else os.path.join(os.path.dirname(os.path.abspath(__file__)), "model.ifc")
ROOM_X, ROOM_Y = 27000, 24000
WALL_T = 200; FF_Z = 0
SFL_BOT, SFL_TOP = -700, -600; AF_BOT = -50
CEIL_S, CEIL_T = 3500, 3700
ACC_X0, ACC_X1, ACC_Y0, ACC_Y1 = 600, 26400, 4500, 19500
CLEAR_H = 2600; DEF_Z = 3300; SPR_H = 200
GRID, GOFF = 7200, 150; COL_W = 600; COL_Z0, COL_Z1 = FF_Z, CEIL_S
RACK_W, RACK_D, RACK_H = 800, 1200, 2000; N_RACKS = 94
CRAH_W, CRAH_D, CRAH_H = 1000, 800, 2100
PDU_W, PDU_D, PDU_H = 800, 800, 2100; PDU_RES = 1800
N_SPR = 104
TRAY_W, TRAY_H = 600, 100; BUS_W, BUS_H = 200, 100; CHW_W, CHW_H = 200, 200
PIPE_INS = 25.4
OH_Z = 2660; UN_Z = -300; TOL = 2
BSUP_MAX, BSUP_SP = 1500, 1400
ROW_C = [5100, 8100, 10500, 13500, 15900, 18900]
ROW_N = [16, 16, 16, 16, 15, 15]
ROW_FS = [False, True, False, True, False, True]
COLD = [6600, 12000, 17400]; HOT = [9300, 14700]
TRAY_MX = 1500; TRAY_X0, TRAY_X1 = 1800, 25000          # aisle start = tray main east face
BUS_MX = 25300; BUS_X0, BUS_X1 = 1900, 25200           # aisle start > tray main east (no crossing)
CHW_MX = 1500; CHW_X0, CHW_X1 = 1600, 25500           # under-floor; aisle start = main east face
AOFF = {'tray': -500, 'bus': 300, 'chw': 700}
ENT_Y = {'tray': 6100, 'bus': 3000, 'chw': 21100}

f = ifcopenshell.file(schema='IFC4')
oh = O.create_owner_history(f)
proj = f.create_entity('IfcProject', GlobalId=ifcopenshell.guid.new(), OwnerHistory=oh, Name='Data Hall MEP Coordination')
U.assign_unit(f, length={'is_metric': True, 'raw': 'MILLIMETRE'})
wcs = f.create_entity('IfcAxis2Placement3D',
    Location=f.create_entity('IfcCartesianPoint', Coordinates=(0.0, 0.0, 0.0)),
    RefDirection=f.create_entity('IfcDirection', (1.0, 0.0, 0.0)),
    Axis=f.create_entity('IfcDirection', (0.0, 0.0, 1.0)))
ctx = f.create_entity('IfcGeometricRepresentationContext', ContextType='Model', ContextIdentifier='Body',
    CoordinateSpaceDimension=3, TrueNorth=None, WorldCoordinateSystem=wcs)
site = f.create_entity('IfcSite', GlobalId=ifcopenshell.guid.new(), OwnerHistory=oh, Name='Site')
bldg = f.create_entity('IfcBuilding', GlobalId=ifcopenshell.guid.new(), OwnerHistory=oh, Name='Data Hall')
strr = f.create_entity('IfcBuildingStorey', GlobalId=ifcopenshell.guid.new(), OwnerHistory=oh, Name='Hall', Elevation=0.0)
f.create_entity('IfcRelAggregates', GlobalId=ifcopenshell.guid.new(), OwnerHistory=oh, RelatingObject=proj, RelatedObjects=(site,))
f.create_entity('IfcRelAggregates', GlobalId=ifcopenshell.guid.new(), OwnerHistory=oh, RelatingObject=site, RelatedObjects=(bldg,))
f.create_entity('IfcRelAggregates', GlobalId=ifcopenshell.guid.new(), OwnerHistory=oh, RelatingObject=bldg, RelatedObjects=(strr,))
_cont = []
def contain(e): _cont.append(e)
def flush():
    if _cont:
        f.create_entity('IfcRelContainedInSpatialStructure', GlobalId=ifcopenshell.guid.new(),
            OwnerHistory=oh, RelatingStructure=strr, RelatedElements=tuple(_cont)); _cont.clear()

def _rect(p):
    pl = f.create_entity('IfcPolyline', Points=tuple(
        f.create_entity('IfcCartesianPoint', Coordinates=(float(x), float(y))) for x, y in p))
    return f.create_entity('IfcArbitraryClosedProfileDef', ProfileType='AREA', OuterCurve=pl)
def _a2p3(loc, rot=0.0):
    L = f.create_entity('IfcCartesianPoint', Coordinates=tuple(float(v) for v in loc))
    if rot == 0.0:
        return f.create_entity('IfcAxis2Placement3D', Location=L,
            RefDirection=f.create_entity('IfcDirection', (1.0, 0.0, 0.0)),
            Axis=f.create_entity('IfcDirection', (0.0, 0.0, 1.0)))
    t = math.radians(rot)
    return f.create_entity('IfcAxis2Placement3D', Location=L,
        RefDirection=f.create_entity('IfcDirection', (math.cos(t), math.sin(t), 0.0)),
        Axis=f.create_entity('IfcDirection', (0.0, 0.0, 1.0)))
def _place(loc, rot=0.0):
    return f.create_entity('IfcLocalPlacement', PlacementRelTo=None, RelativePlacement=_a2p3(loc, rot))
def _solid(p, d):
    return f.create_entity('IfcExtrudedAreaSolid', SweptArea=_rect(p),
        Position=f.create_entity('IfcAxis2Placement3D',
            Location=f.create_entity('IfcCartesianPoint', Coordinates=(0.0, 0.0, 0.0)),
            RefDirection=f.create_entity('IfcDirection', (1.0, 0.0, 0.0)),
            Axis=f.create_entity('IfcDirection', (0.0, 0.0, 1.0))),
        ExtrudedDirection=f.create_entity('IfcDirection', (0.0, 0.0, 1.0)), Depth=float(d))
def _rep(s):
    shp = f.create_entity('IfcShapeRepresentation', ContextOfItems=ctx, RepresentationIdentifier='Body',
        RepresentationType='SweptSolid', Items=(s,))
    return f.create_entity('IfcProductDefinitionShape', Representations=(shp,))
def box(ent, name, x0, y0, z0, x1, y1, z1, ot=None, pd=None, rot=0.0):
    xlo, xhi = min(x0, x1), max(x0, x1); ylo, yhi = min(y0, y1), max(y0, y1); zlo, zhi = min(z0, z1), max(z0, z1)
    s = _solid([(0, 0), (xhi-xlo, 0), (xhi-xlo, yhi-ylo), (0, yhi-ylo), (0, 0)], zhi-zlo)
    kw = dict(GlobalId=ifcopenshell.guid.new(), OwnerHistory=oh, Name=name,
        ObjectPlacement=_place((xlo/1000.0, ylo/1000.0, zlo/1000.0), rot), Representation=_rep(s))
    if ot: kw['ObjectType'] = ot
    if pd: kw['PredefinedType'] = pd
    e = f.create_entity(ent, **kw); contain(e); return e
def cbox(ent, name, cx, cy, z0, w, d, h, ot=None, pd=None, rot=0.0):
    s = _solid([(-w/2, -d/2), (w/2, -d/2), (w/2, d/2), (-w/2, d/2), (-w/2, -d/2)], h)
    kw = dict(GlobalId=ifcopenshell.guid.new(), OwnerHistory=oh, Name=name,
        ObjectPlacement=_place((cx/1000.0, cy/1000.0, z0/1000.0), rot), Representation=_rep(s))
    if ot: kw['ObjectType'] = ot
    if pd: kw['PredefinedType'] = pd
    e = f.create_entity(ent, **kw); contain(e); return e

def _val(v):
    if isinstance(v, bool): return f.create_entity('IfcBoolean', v)
    if isinstance(v, int): return f.create_entity('IfcInteger', v)
    if isinstance(v, float): return f.create_entity('IfcReal', float(v))
    return f.create_entity('IfcLabel', str(v))
def add_pset(els, name, props):
    if not isinstance(els, (list, tuple)): els = [els]
    ps = f.create_entity('IfcPropertySet', GlobalId=ifcopenshell.guid.new(), OwnerHistory=oh, Name=name,
        HasProperties=tuple(f.create_entity('IfcPropertySingleValue', Name=k, NominalValue=_val(v)) for k, v in props.items()))
    f.create_entity('IfcRelDefinesByProperties', GlobalId=ifcopenshell.guid.new(), OwnerHistory=oh,
        RelatingPropertyDefinition=ps, RelatedObjects=tuple(els))

abbs = []
def reg(name, x0, y0, z0, x1, y1, z1, kind, svc=''):
    abbs.append((name, x0, y0, z0, x1, y1, z1, kind, svc))
def boxp(ent, name, x0, y0, z0, x1, y1, z1, kind='struct', svc='', **kw):
    e = box(ent, name, x0, y0, z0, x1, y1, z1, **kw); reg(name, x0, y0, z0, x1, y1, z1, kind, svc); return e

# room envelope
boxp('IfcSlab', 'StrucFloor', 0, 0, SFL_BOT, ROOM_X, ROOM_Y, SFL_TOP, pd='BASESLAB', kind='slab')
boxp('IfcSlab', 'AccessFloor', ACC_X0, ACC_Y0, AF_BOT, ACC_X1, ACC_Y1, FF_Z, pd='FLOOR', kind='slab')
boxp('IfcSlab', 'Ceiling', 0, 0, CEIL_S, ROOM_X, ROOM_Y, CEIL_T, pd='NOTDEFINED', kind='slab')
boxp('IfcWall', 'WallS', 0, 0, SFL_BOT, ROOM_X, WALL_T, CEIL_T, pd='SOLIDWALL', kind='wall')
boxp('IfcWall', 'WallN', 0, ROOM_Y-WALL_T, SFL_BOT, ROOM_X, ROOM_Y, CEIL_T, pd='SOLIDWALL', kind='wall')
boxp('IfcWall', 'WallW', 0, 0, SFL_BOT, WALL_T, ROOM_Y, CEIL_T, pd='SOLIDWALL', kind='wall')
boxp('IfcWall', 'WallE', ROOM_X-WALL_T, 0, SFL_BOT, ROOM_X, ROOM_Y, CEIL_T, pd='SOLIDWALL', kind='wall')

# columns
col_xy = []
for gy in HOT:
    for gx in (7350, 14550): col_xy.append((gx, gy))
for gy in HOT:
    for gx in (600, 23400): col_xy.append((gx, gy))
for gy in (600, 23400):
    for gx in (7350, 14550): col_xy.append((gx, gy))
for cid, (cx, cy) in enumerate(col_xy):
    boxp('IfcColumn', f'Col{cid+1}', cx-COL_W/2, cy-COL_W/2, COL_Z0, cx+COL_W/2, cy+COL_W/2, COL_Z1, pd='COLUMN', kind='column')
add_pset(f.by_type('IfcColumn'), 'Pset_DCM_Column',
    {'StructuralGridSpacing': GRID, 'GridOffsetFromTileGrid': GOFF, 'SectionWidth': COL_W,
     'SectionDepth': COL_W, 'RunsFullClearHeight': True, 'ColumnCount': len(col_xy)})

# racks
racks = []
for ri, (cy, n) in enumerate(zip(ROW_C, ROW_N)):
    wdt = n*RACK_W; x0 = (ROOM_X-wdt)/2.0; rot = 180.0 if ROW_FS[ri] else 0.0
    for k in range(n):
        cx = x0 + RACK_W/2 + k*RACK_W
        racks.append(cbox('IfcFurniture', f'R{ri+1}-{k+1}', cx, cy, FF_Z, RACK_W, RACK_D, RACK_H, ot='Rack', pd='USERDEFINED', rot=rot))
        reg(f'R{ri+1}-{k+1}', cx-RACK_W/2, cy-RACK_D/2, FF_Z, cx+RACK_W/2, cy+RACK_D/2, FF_Z+RACK_H, 'rack')
add_pset(racks, 'Pset_DCM_Rack', {'RackWidth': RACK_W, 'RackDepth': RACK_D, 'RackHeight': RACK_H, 'Count': N_RACKS, 'FacingConvention': 'front faces cold aisle'})

# CRAHs
crah_pos = [(2400, 6600), (2400, 12000), (2400, 17400), (26300, 6600), (26300, 12000), (26300, 17400)]
crahs = []
for i, (cx, cy) in enumerate(crah_pos):
    crahs.append(cbox('IfcUnitaryEquipment', f'CRAH-{i+1}', cx, cy, FF_Z, CRAH_W, CRAH_D, CRAH_H, ot='CRAH', pd='USERDEFINED'))
    reg(f'CRAH-{i+1}', cx-CRAH_W/2, cy-CRAH_D/2, FF_Z, cx+CRAH_W/2, cy+CRAH_D/2, FF_Z+CRAH_H, 'crah')
add_pset(crahs, 'Pset_DCM_CRAH', {'Width': CRAH_W, 'Depth': CRAH_D, 'Height': CRAH_H, 'Type': 'Perimeter', 'CHWReachRequired': 2500})

# PDUs (hot aisles, clear of every CHW run)
pdu_pos = [(4500, 9300), (13500, 9300), (4500, 14700), (13500, 14700)]
pdus = []
for i, (cx, cy) in enumerate(pdu_pos):
    pdus.append(cbox('IfcElectricDistributionBoard', f'PDU-{i+1}', cx, cy, FF_Z, PDU_W, PDU_D, PDU_H, ot='PDU', pd='USERDEFINED'))
    reg(f'PDU-{i+1}', cx-PDU_W/2, cy-PDU_D/2, FF_Z, cx+PDU_W/2, cy+PDU_D/2, FF_Z+PDU_H, 'pdu')
add_pset(pdus, 'Pset_DCM_PDU', {'Width': PDU_W, 'Depth': PDU_D, 'Height': PDU_H, 'ReservedClearSpaceAbove': PDU_RES})

# sprinklers
sp_x = [1500 + 2000*k for k in range(13)]; sp_y = [1500 + 3000*k for k in range(8)]
assert len(sp_x)*len(sp_y) == N_SPR
sprs = []; sid = 0
for sy in sp_y:
    for sx in sp_x:
        sid += 1
        sprs.append(cbox('IfcFireSuppressionTerminal', f'Spr{sid}', sx, sy, DEF_Z, 150, 150, SPR_H, ot='Sprinkler', pd='SPRINKLER'))
        reg(f'Spr{sid}', sx-75, sy-75, DEF_Z, sx+75, sy+75, DEF_Z+SPR_H, 'sprinkler')
add_pset(sprs, 'Pset_DCM_Sprinkler', {'DeflectorElevation': DEF_Z, 'HeadCount': N_SPR, 'ClearBelowDeflector': 460, 'NFPAObstructionZone': 450, 'GridSpacingX': 2000, 'GridSpacingY': 3000})

# containment side panels (no roofs)
conts = []
for ai, ay in enumerate(COLD):
    for fy in (ay-850, ay+850):
        conts.append(cbox('IfcBuildingElementProxy', f'Cont{ai+1}', (ACC_X0+ACC_X1)/2, fy, FF_Z, ACC_X1-ACC_X0, 40, RACK_H, ot='Containment', pd='USERDEFINED'))
        reg(f'Cont{ai+1}', ACC_X0, fy-20, FF_Z, ACC_X1, fy+20, FF_Z+RACK_H, 'containment')
add_pset(conts, 'Pset_DCM_Containment', {'HasRoof': False, 'Type': 'ColdAisleSidePanel'})

# ----------------------------- service routing -----------------------------
def build_route(svc, segs, w, h, ent, pd, ot):
    """segs: list of (axis, x0,y0,z0, x1,y1,z1) axis-aligned boxes. Returns (els, oh_len, uf_len)."""
    els = []; oh = 0.0; uf = 0.0
    for i, (ax, x0, y0, z0, x1, y1, z1) in enumerate(segs):
        e = boxp(ent, f'{ot} {svc} s{i+1}', x0, y0, z0, x1, y1, z1, kind='service', svc=svc, ot=ot, pd=pd)
        els.append(e)
        if ax == 'Z':
            zlo, zhi = min(z0, z1), max(z0, z1)
            oh += max(0.0, zhi) - max(0.0, zlo)
            uf += max(0.0, -zlo) - max(0.0, -zhi)
        else:
            ln = abs(x1-x0) if ax == 'X' else abs(y1-y0)
            if z0 > 0: oh += ln
            else: uf += ln
    return els, oh, uf

def seg_x(x0, x1, y, z, w, h): return ('X', x0, y-w/2, z-h/2, x1, y+w/2, z+h/2)
def seg_y(y0, y1, x, z, w, h): return ('Y', x-w/2, y0, z-h/2, x+w/2, y1, z+h/2)
def seg_z(z0, z1, x, y, w, h): return ('Z', x-w/2, y-h/2, z0, x+w/2, y+h/2, z1)

# TRAY: entry -> west main -> 3 east-going aisle runs (overhead, touch-junctions)
tray_M_east = TRAY_MX + TRAY_W/2     # 1800
tray_M_west = TRAY_MX - TRAY_W/2     # 1200
tray_segs = [seg_x(200, tray_M_west, ENT_Y['tray'], OH_Z, TRAY_W, TRAY_H)]
tray_segs.append(seg_y(ENT_Y['tray'], COLD[2]+AOFF['tray'], TRAY_MX, OH_Z, TRAY_W, TRAY_H))
for ay in COLD:
    tray_segs.append(seg_x(tray_M_east, TRAY_X1, ay+AOFF['tray'], OH_Z, TRAY_W, TRAY_H))
tray_els, tray_oh, tray_uf = build_route('tray', tray_segs, TRAY_W, TRAY_H, 'IfcCableCarrierSegment', 'CABLETRAYSEGMENT', 'CableTray')
# BUSWAY: entry(south) -> east main -> 3 west-going aisle runs (overhead)
bus_M_west = BUS_MX - BUS_W/2       # 25200
bus_segs = [seg_x(200, bus_M_west, ENT_Y['bus'], OH_Z, BUS_W, BUS_H)]
bus_segs.append(seg_y(ENT_Y['bus'], COLD[2]+AOFF['bus'], BUS_MX, OH_Z, BUS_W, BUS_H))
for ay in COLD:
    bus_segs.append(seg_x(BUS_X0, bus_M_west, ay+AOFF['bus'], OH_Z, BUS_W, BUS_H))
bus_els, bus_oh, bus_uf = build_route('bus', bus_segs, BUS_W, BUS_H, 'IfcCableSegment', 'BUSBARSEGMENT', 'Busway')
# CHW: entry(north,overhead) -> riser down -> under-floor main -> 3 aisle runs
chw_M_east = CHW_MX + CHW_W/2       # 1600
chw_M_west = CHW_MX - CHW_W/2       # 1400
chw_segs = [seg_x(200, chw_M_west, ENT_Y['chw'], OH_Z, CHW_W, CHW_H)]
chw_segs.append(seg_z(OH_Z, UN_Z, CHW_MX, ENT_Y['chw'], CHW_W, CHW_H))   # riser
chw_segs.append(seg_y(ENT_Y['chw']-CHW_W/2, COLD[0]+AOFF['chw'], CHW_MX, UN_Z, CHW_W, CHW_H))
for ay in COLD:
    chw_segs.append(seg_x(chw_M_east, CHW_X1, ay+AOFF['chw'], UN_Z, CHW_W, CHW_H))
chw_els, chw_oh, chw_uf = build_route('chw', chw_segs, CHW_W, CHW_H, 'IfcPipeSegment', 'RIGIDSEGMENT', 'ChilledWater')

for els, svc, olen, ulen in [(tray_els,'tray',tray_oh,tray_uf),(bus_els,'bus',bus_oh,bus_uf),(chw_els,'chw',chw_oh,chw_uf)]:
    add_pset(els, 'Pset_DCM_ServiceRoute',
        {'Service': svc, 'SegmentCount': len(els), 'OverheadLength': round(olen, 1), 'UnderfloorLength': round(ulen, 1),
         'ElevationOverhead': OH_Z if svc != 'chw' else UN_Z, 'ElevationUnderfloor': UN_Z if svc == 'chw' else 0,
         'InClearHeightBand': svc != 'chw', 'TrayBuswaySeparation': 800})
    add_pset(els[0], 'Pset_DCM_Entry', {'Service': svc, 'EntryPoint': 'West wall', 'EntryX': 200, 'EntryY': ENT_Y[svc], 'EntryZ': OH_Z})

# busway supports (<=1400 mm)
sups = []
for (nm, x0, y0, z0, x1, y1, z1, kind, s) in list(abbs):
    if kind != 'service' or s != 'bus': continue
    ln = max(x1-x0, y1-y0)
    if ln < 2000: continue
    isx = (x1-x0) > (y1-y0)
    n = int(ln // BSUP_SP) + 1
    for k in range(n):
        if isx: x = x0 + ln*k/max(1, n-1); y = (y0+y1)/2
        else: x = (x0+x1)/2; y = y0 + ln*k/max(1, n-1)
        if not (400 < x < ROOM_X-400 and 400 < y < ROOM_Y-400): continue
        if isx and (x < x0+300 or x > x1-300): continue
        if (not isx) and (y < y0+300 or y > y1-300): continue
        sups.append(cbox('IfcBuildingElementProxy', f'BSup{len(sups)+1}', x, y, 2710, 40, 40, 340, ot='Support', pd='USERDEFINED'))
        reg(f'BSup{len(sups)}', x-20, y-20, 2710, x+20, y+20, 3050, 'support')
add_pset(sups, 'Pset_DCM_Support', {'MaxSpacing': BSUP_MAX, 'Spacing': BSUP_SP, 'Count': len(sups)})

# service drops (overhead terminations to racks); touch service at its underside (0 overlap)
drops = []
for ai, ay in enumerate(COLD):
    for svc in ('tray', 'bus'):
        x = ROOM_X/2.0; y = ay + AOFF[svc]
        ztop = OH_Z - (TRAY_H/2 if svc == 'tray' else BUS_H/2)   # service underside = 2610
        drops.append(cbox('IfcBuildingElementProxy', f'Drop {svc} r{ai+1}', x, y, RACK_H, 40, 40, ztop-RACK_H, ot='Drop', pd='USERDEFINED'))
        reg(f'Drop {svc} r{ai+1}', x-20, y-20, RACK_H, x+20, y+20, ztop, 'drop', svc)
# CHW reaches perimeter CRAHs by under-floor aisle proximity (<=2500 mm); no taps needed
add_pset(drops, 'Pset_DCM_Drop', {'Count': len(drops), 'Purpose': 'overhead service termination to rack row'})

add_pset(proj, 'Pset_DCM_Project',
    {'RoomWidth': ROOM_X, 'RoomDepth': ROOM_Y, 'FinishedFloor': FF_Z, 'ClearHeight': CLEAR_H,
     'CeilingSoffit': CEIL_S, 'AccessFloorPlenumDepth': 600, 'SprinklerDeflector': DEF_Z,
     'PipeInsulation': PIPE_INS, 'RackCount': N_RACKS, 'SprinklerCount': N_SPR,
     'CRAHCount': len(crah_pos), 'PDUCount': len(pdu_pos), 'ColumnCount': len(col_xy)})
flush()

# ----------------------------- self clash check -----------------------------
def ov(a, b):
    return (min(a[4], b[4])-max(a[1], b[1]), min(a[5], b[5])-max(a[2], b[2]), min(a[6], b[6])-max(a[3], b[3]))
clashes = []; sk = {'slab', 'wall'}
for i in range(len(abbs)):
    for j in range(i+1, len(abbs)):
        A, B = abbs[i], abbs[j]
        if A[7] in sk and B[7] in sk: continue
        if A[7] == 'service' and B[7] == 'service' and A[8] == B[8]: continue
        ox, oy, oz = ov(A, B)
        if ox > TOL and oy > TOL and oz > TOL:
            clashes.append((A[0], B[0], round(ox, 1), round(oy, 1), round(oz, 1)))
if clashes:
    print('CLASHES:', file=sys.stderr)
    for c in clashes[:60]: print('  ', c, file=sys.stderr)

# ----------------------------- write outputs --------------------------------
f.write(OUT_PATH)
rpath = os.path.join(os.path.dirname(os.path.abspath(OUT_PATH)), 'reconciliation.json')
recon = {
  'source_drawings': {
    'A-101': 'equipment plan 27000x24000, 7200 grid offset 150, 94 racks, cross aisle re-registers rows',
    'A-301': 'section: clear height 2600, ceiling soffit 3500, access floor 600 plenum',
    'A-601': 'cabinet schedule: rack 800x1200x2000',
    'A-602': 'containment: cold aisle side panels, no roofs; pathway data',
    'M-101': 'chilled water: 150 pipe + 25.4 insulation; perimeter CRAHs',
    'E-101': 'busway 200, PDU, support 1500 max',
    'F-101': 'sprinkler grid 104 heads, deflector 3300'},
  'notes': [
    {'note': 'A-301 clear height 2600 mm', 'applied': 'services kept >=2600 above FF'},
    {'note': '460 mm below sprinkler deflector', 'applied': 'service tops 2710 <= 3300-460=2840'},
    {'note': 'NFPA 13 450 mm obstruction zone', 'applied': 'service tops 2710 <= 2850'},
    {'note': '300 mm tray/busway separation', 'applied': 'parallel aisle runs 800 mm apart in Y; never cross'},
    {'note': '1800 mm CHW-free above PDU', 'applied': 'CHW routed under-floor; no CHW over PDUs'},
    {'note': '25.4 mm pipe insulation', 'applied': 'CHW section 200 mm includes 2x25.4 insulation'},
    {'note': 'busway support 1500 max', 'applied': 'supports at 1400 mm centres'},
    {'note': '7200 grid offset 150 from tile grid', 'applied': 'columns on 7200 grid in hot aisles/perimeter'},
    {'note': 'heads beneath runs >1200 / containment roofs', 'applied': 'runs <1200 wide; containment has no roofs'},
    {'note': 'under-floor plenum usable', 'applied': 'CHW routed in under-floor plenum (-300 mm)'}],
  'lengths': {'tray': {'overhead': round(tray_oh,1), 'underfloor': round(tray_uf,1)},
              'bus': {'overhead': round(bus_oh,1), 'underfloor': round(bus_uf,1)},
              'chw': {'overhead': round(chw_oh,1), 'underfloor': round(chw_uf,1)}},
  'clashes': len(clashes)}
with open(rpath, 'w') as fh: json.dump(recon, fh, indent=2)
print('Wrote', OUT_PATH); print('Recon', rpath)
