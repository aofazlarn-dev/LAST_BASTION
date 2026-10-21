"""ตัด sheet ชุด v2: แบ่งแถวตามตาราง แล้วเรียงภาพในแถวจากซ้ายไปขวา (ไม่ต้องตรงคอลัมน์เป๊ะ)"""
import numpy as np, os, sys, json
from PIL import Image
from scipy import ndimage

SRC = sys.argv[1] if len(sys.argv) > 1 else 'assets/sheets2'
OUT = sys.argv[2] if len(sys.argv) > 2 else 'build/cut2'
os.makedirs(OUT, exist_ok=True)

def low(f): return [[f + '0', f + '1', f + '2', f + '3'], [f + '4', f + '5', f + '6', f + '7']]
def mid(f): return [[f + '0', f + '1', f + '2'], [f + '3', f + '4']]
SHEETS = {
 '01_characters.png': (2, [['hero_archer', 'hero_warrior', 'hero_mage', 'hero_engineer', 'hero_healer', 'worker'], ['worker_wood', 'worker_stone', 'u_archer', 'u_sword', 'u_medic']]),
 '02_camp_walls.png': (4, [['camp1', 'camp2', 'camp3', 'camp4', 'camp5'], ['wall1', 'wall2', 'wall3', 'wall_side1', 'wall_side2', 'wall_side3'],
                          ['wall_L1', 'wall_L2', 'wall_L3', 'wall_corner1', 'wall_corner2', 'wall_corner3'], ['gate1', 'gate2', 'gate3', 'gate_side1', 'gate_side2', 'gate_side3']]),
 '03_buildings_props.png': (3, [['tower1', 'tower2', 'tower3', 'barracks', 'infirmary', 'workshop'], ['tree1', 'tree2', 'rock', 'stump', 'pebbles', 'tuft'], ['flower', 'firepit', 'loot_bag']]),
 '10_items.png': (3, [['bow_common1', 'bow_common2', 'bow_common3', 'bow_rare1', 'bow_rare2', 'bow_rare3'], ['bow_epic1', 'bow_epic2', 'bow_epic3', 'armor_common1', 'armor_common2', 'armor_common3'],
                      ['armor_rare1', 'armor_rare2', 'armor_rare3', 'armor_epic1', 'armor_epic2', 'armor_epic3']]),
 '11_fx.png': (3, [['fx_arrow', 'fx_bolt', 'fx_fireball', 'fx_frostbolt', 'fx_web', 'fx_blast'], ['fx_hit', 'fx_heal', 'fx_levelup', 'fx_recall', 'fx_volley', 'fx_sunburn'], ['fx_rubble', 'fx_flame', 'fx_frost']]),
 '12_ui.png': (4, [['ui_wood', 'ui_stone', 'ui_hp', 'ui_mp', 'ui_exp', 'ui_skill_volley'], ['ui_build', 'ui_repair', 'ui_bag', 'ui_home', 'ui_map', 'ui_menu'],
                   ['ui_bestiary', 'ui_night', 'ui_day', 'ui_warn', 'ui_worker', 'ui_army'], ['ui_mode_free', 'ui_mode_follow', 'ui_mode_guard', 'ui_res_heroweapon', 'ui_res_unitweapon', 'ui_res_unitarmor']]),
 'mon_boss.png': (2, [['boss0', 'boss1', 'boss2'], ['boss3', 'boss4']]),
}
for f in ['zombie', 'wolf', 'slime', 'bat', 'skel']: SHEETS[f'mon_{f}.png'] = (2, low(f))
for f in ['ghoul', 'spider', 'orc', 'wisp', 'bonemage', 'beetle', 'knight', 'were', 'golem', 'demon', 'lich']: SHEETS[f'mon_{f}.png'] = (2, mid(f))

meta = {}
for f, (R, rows) in SHEETS.items():
    p = os.path.join(SRC, f)
    if not os.path.exists(p): print('missing', f); continue
    im = np.array(Image.open(p).convert('RGBA')).astype(np.uint8)
    H, W = im.shape[:2]; ch = H / R
    mask = im[..., 3] > 40
    lab, num = ndimage.label(mask)
    if num == 0: continue
    sizes = ndimage.sum(mask, lab, range(1, num + 1)); coms = ndimage.center_of_mass(mask, lab, range(1, num + 1))
    objs = ndimage.find_objects(lab)
    # ชิ้นที่ใหญ่เกินแถว (ติดกันข้ามแถว) แบ่งตามแถว
    rowlab = np.zeros_like(lab)
    yy = np.arange(H)[:, None].repeat(W, 1)
    rowof = np.minimum(R - 1, (yy / ch).astype(int))
    pieces = []   # (row, comx, size, mask-index-key)
    keyimg = np.zeros(lab.shape, np.int32); k = 0
    for i, sl in enumerate(objs):
        if sl is None or sizes[i] < 120: continue
        m = lab == (i + 1)
        if (sl[0].stop - sl[0].start) > 1.3 * ch:
            for r in range(R):
                mm = m & (rowof == r)
                if mm.sum() < 120: continue
                k += 1; keyimg[mm] = k; cy, cx = ndimage.center_of_mass(mm); pieces.append([r, cx, mm.sum(), k])
        else:
            k += 1; keyimg[m] = k; cy, cx = coms[i]; pieces.append([min(R - 1, int(cy // ch)), cx, sizes[i], k])
    for r, names in enumerate(rows):
        pr = [q for q in pieces if q[0] == r]
        if not pr: continue
        big = max(q[2] for q in pr)
        main = sorted([q for q in pr if q[2] >= big * 0.18], key=lambda q: q[1])
        # ถ้าจำนวนชิ้นใหญ่ > จำนวนชื่อ รวมชิ้นที่ใกล้กันที่สุดเข้าด้วยกัน
        while len(main) > len(names):
            gaps = [main[j + 1][1] - main[j][1] for j in range(len(main) - 1)]
            j = int(np.argmin(gaps)); a, b = main[j], main[j + 1]
            keyimg[keyimg == b[3]] = a[3]; a[1] = (a[1] * a[2] + b[1] * b[2]) / (a[2] + b[2]); a[2] += b[2]; main.pop(j + 1)
        if len(main) < len(names): print('WARN', f, 'row', r, 'found', len(main), 'expected', len(names))
        small = [q for q in pr if q[2] < big * 0.18]
        for q in small:   # ชิ้นเล็ก (ประกาย เศษ) ไปรวมกับภาพที่ใกล้ที่สุด ถ้าอยู่ไม่ไกล
            j = int(np.argmin([abs(q[1] - m_[1]) for m_ in main]))
            if abs(q[1] - main[j][1]) < W / max(len(names), 1) * 0.6: keyimg[keyimg == q[3]] = main[j][3]
        for n, q in zip(names, main):
            sel = keyimg == q[3]
            others = (keyimg > 0) & ~sel
            near = ndimage.binary_dilation(sel, iterations=12) & ~ndimage.binary_dilation(others, iterations=3)
            cell = im.copy(); cell[~near] = 0; cell[cell[..., 3] < 10] = 0
            ys, xs = np.where(cell[..., 3] > 0)
            sub = cell[ys.min():ys.max() + 1, xs.min():xs.max() + 1]
            Image.fromarray(sub).save(f'{OUT}/{n}.png'); meta[n] = sub.shape[:2]
json.dump(meta, open(os.path.join(OUT, 'meta.json'), 'w'))
print(len(meta))
