"""ตัด sheet ท่าทาง (Art Spec v3) เป็นแถบเฟรม webp + meta
- แบ่งแถวตามตาราง เรียงภาพในแถวจากซ้ายไปขวา
- จัดเฟรมให้เท้าอยู่ระดับเดียวกัน ตำแหน่ง x อิงกึ่งกลางช่อง (เก็บท่าพุ่ง/ลูกพลังไว้)
- สเกลให้ความสูงเฉลี่ยของท่าเดิน/ยืนของตัวนั้น = REF px (เกมคำนวณสเกลจริงเทียบภาพนิ่งเอง)"""
import numpy as np, os, sys, json
from PIL import Image
from scipy import ndimage

SRC, OUT, SPEC = sys.argv[1], sys.argv[2], sys.argv[3]
os.makedirs(OUT, exist_ok=True)
S = json.load(open(SPEC))

# ไฟล์ที่อัปโหลดสลับชื่อ: ชื่อจริง -> ไฟล์ต้นทางที่มีภาพของท่านั้น (None = ไม่มี ต้องทำใหม่)
REMAP = {
    'worker_idle': 'u_sword_idle', 'worker_walk': 'u_medic_walk', 'worker_death': 'hero_healer_death',
    'hero_healer_death': 'worker_death', 'hero_healer_walk': 'worker_walk',
    'hero_engineer_walk': 'hero_healer_walk', 'hero_engineer_idle': 'u_archer_idle',
    'u_sword_death': 'u_archer_death',
    'hero_engineer_death': None, 'hero_engineer_hurt': None,
    'u_archer_death': None, 'u_archer_idle': None, 'u_archer_walk': None,
    'u_sword_idle': None, 'u_sword_walk': None, 'u_medic_walk': None,
    'boss2_death': None, 'boss2_walk': None, 'boss3_death': None, 'boss3_walk': None,
}

def frames_of(path, C, R, nframes):
    im = np.array(Image.open(path).convert('RGBA'))
    H, W = im.shape[:2]; ch, cw = H / R, W / C
    mask = im[..., 3] > 40
    lab, num = ndimage.label(mask)
    sizes = ndimage.sum(mask, lab, range(1, num + 1)); coms = ndimage.center_of_mass(mask, lab, range(1, num + 1))
    key = np.zeros(lab.shape, np.int32); pieces = []; k = 0
    rowof = np.minimum(R - 1, (np.arange(H)[:, None] / ch).astype(int)).repeat(W, 1)
    for i, sl in enumerate(ndimage.find_objects(lab)):
        if sl is None or sizes[i] < 80: continue
        m = lab == (i + 1)
        if (sl[0].stop - sl[0].start) > 1.3 * ch:
            for r in range(R):
                mm = m & (rowof == r)
                if mm.sum() < 80: continue
                k += 1; key[mm] = k; cy, cx = ndimage.center_of_mass(mm); pieces.append([r, cx, mm.sum(), k])
        else:
            k += 1; key[m] = k; cy, cx = coms[i]; pieces.append([min(R - 1, int(cy // ch)), cx, sizes[i], k])
    out = []
    for r in range(R):
        want = min(C, nframes - r * C)
        if want <= 0: break
        pr = [q for q in pieces if q[0] == r]
        if not pr: return None
        # จัดกลุ่มตามช่องคอลัมน์ก่อน (ภาพหนึ่งเฟรมอาจหลายชิ้น เช่น ลูกพลัง)
        cols = {}
        for q in pr:
            c = min(C - 1, int(q[1] // cw)); cols.setdefault(c, []).append(q)
        if len(cols) < want:
            print('  WARN', os.path.basename(path), 'row', r, 'cols', sorted(cols), 'want', want)
        for c in range(C):
            if len(out) >= nframes or c >= want: break
            qs = cols.get(c, [])
            if not qs: out.append(None); continue
            sel = np.isin(key, [q[3] for q in qs])
            others = (key > 0) & ~sel
            near = ndimage.binary_dilation(sel, iterations=10) & ~ndimage.binary_dilation(others, iterations=2)
            cell = im.copy(); cell[~near] = 0; cell[cell[..., 3] < 10] = 0
            ys, xs = np.where(cell[..., 3] > 0)
            # อ้างอิงกึ่งกลางช่อง
            ccx = (c + 0.5) * cw
            out.append(dict(img=cell[ys.min():ys.max() + 1, xs.min():xs.max() + 1], x0=xs.min() - ccx, x1=xs.max() + 1 - ccx, h=ys.max() + 1 - ys.min()))
    return out

def base_of(name):
    for a in ('_walk_wood', '_walk_stone', '_walk', '_idle', '_attack', '_death', '_hurt', '_skill', '_special', '_heal', '_chop', '_mine'):
        if name.endswith(a): return name[:-len(a)], a[1:]
    return name, 'fx'

# รวบรวมเฟรมทั้งหมด
raw = {}
for name, sp in S.items():
    src = REMAP.get(name, name)
    if src is None: print('skip (redo)', name); continue
    p = os.path.join(SRC, src + '.png')
    if not os.path.exists(p): print('missing', p); continue
    fr = frames_of(p, sp['c'], sp['r'], sp['frames'])
    if not fr or any(f is None for f in fr): print('BAD', name, '<-', src); continue
    raw[name] = fr

# ความสูงอ้างอิงของแต่ละตัว: ค่ามัธยฐานของเฟรมเดิน (ไม่มีใช้ยืน หรือท่าแรกที่มี)
ref = {}
for name, fr in raw.items():
    b, act = base_of(name)
    pri = {'walk': 0, 'idle': 1}.get(act, 2)
    hs = float(np.median([f['h'] for f in fr]))
    if b not in ref or pri < ref[b][0]: ref[b] = (pri, hs)

meta = {}
for name, fr in raw.items():
    b, act = base_of(name)
    REF = 192 if b.startswith('boss') else (160 if act == 'fx' else 128)
    # สเกลแยกต่อท่า: ท่าเดินใช้ความสูงเฉลี่ย ท่าอื่นใช้เฟรมแรก (ท่ายืนตรง) ให้สูงเท่าท่าเดิน
    # (GPT วาดตาราง 2x2 ตัวใหญ่กว่าตาราง 3x2 ถ้าไม่ปรับ ท่ายืนจะดูใหญ่/เด้ง)
    h0 = float(np.median([f['h'] for f in fr])) if act in ('walk', 'walk_wood', 'walk_stone') else float(fr[0]['h'])
    if act in ('walk_wood', 'walk_stone'): h0 = h0  # มีของบนหลัง สูงกว่าเล็กน้อยก็ได้
    sc = REF / (h0 if act != 'fx' else ref[b][1])
    print(f'{name:22s} scale-vs-walk {ref[b][1]/h0:.2f}')
    if act == 'fx': sc = 160 / max(max(f['img'].shape[:2]) for f in fr)
    left = max(-f['x0'] for f in fr) * sc; right = max(f['x1'] for f in fr) * sc
    half = int(np.ceil(max(left, right))) + 2
    Hh = int(np.ceil(max(f['h'] for f in fr) * sc)) + 4
    fw = 2 * half
    strip = Image.new('RGBA', (fw * len(fr), Hh), (0, 0, 0, 0))
    for i, f in enumerate(fr):
        im = Image.fromarray(f['img']); w, h = im.size
        im = im.resize((max(1, round(w * sc)), max(1, round(h * sc))), Image.LANCZOS)
        x = i * fw + half + int(round(f['x0'] * sc)); y = Hh - 2 - im.size[1]
        strip.alpha_composite(im, (max(i * fw, x), max(0, y)))
    strip.save(os.path.join(OUT, name + '.webp'), 'WEBP', quality=86, method=6)
    sp = S[name]
    loop = act in ('walk', 'idle', 'walk_wood', 'walk_stone', 'chop', 'mine', 'heal') or name in ('firepit', 'flag', 'fx_recall')
    meta[name] = dict(n=len(fr), w=fw, h=Hh, fps=sp['fps'], loop=loop, ref=REF, oy=round((Hh - 2) / Hh, 4))
json.dump(meta, open(os.path.join(OUT, 'anim.json'), 'w'), separators=(',', ':'))
print('done', len(meta))
