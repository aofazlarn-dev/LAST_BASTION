# LAST BASTION · Art Spec · โหมด Lord Rush

ภาพชุดเพิ่มสำหรับโหมด Lord Rush (`rush.html`) จุดหลักคือ **Hero ขี่ม้า** เหมือนในโฆษณา ที่เหลือเป็นของเสริมให้ฉากดูเป็นหุบเขาทะเลทราย

ใช้สไตล์และกติกาเดียวกับ **Art Spec v2** (ภาพนิ่ง) และ **Art Spec v3** (ท่าทาง) ทุกอย่าง: Stylized 3D สีสด แดดจากซ้ายบน มุมกล้อง 3/4 top-down ~50° หันขวา พื้นหลังโปร่งใส ขนาดภาพ 1536×1024

ทำทีละชิ้นได้ ชิ้นที่ยังไม่มี เกมใช้ภาพเดิมแทน (Hero เดินเท้า, ป้อมธนู, รั้วไม้)

---

## 1. ภาพอ้างอิงที่ต้องแนบ

| สั่งอะไร | แนบภาพนี้ไปด้วย |
| --- | --- |
| Hero ขี่ม้า (ภาพนิ่ง) | ภาพนิ่ง v2 ของ Hero อาชีพนั้น เช่น `hero_warrior` · ถ้าทำม้าตัวแรกเสร็จแล้ว แนบ `mount_warrior` ไปด้วยเพื่อให้ม้าเหมือนกันทุกอาชีพ |
| ท่าทางของ Hero ขี่ม้า | ภาพนิ่ง `mount_<อาชีพ>` ที่ได้จาก Sheet R1 |
| ของประกอบฉาก | ภาพต้นแบบสไตล์จาก Sheet 01 ของ v2 |

ม้าต้องเป็นแบบเดียวกันทุกอาชีพ ต่างกันแค่คนขี่ ให้สั่ง `mount_warrior` ก่อน เลือกภาพที่ชอบ แล้วแนบไปทุกครั้งที่สั่งอาชีพอื่นพร้อมพิมพ์ว่า `Use the exact same horse as the attached mount_warrior, only change the rider.`

### หน้าตาม้า (ใช้ทุกภาพ)

```
A sturdy, chunky war horse with a cute, slightly oversized head, light grey / white coat,
dark grey mane and tail, wearing blue (#3f7fd9) and silver cloth barding with a small
silver crest on the chest, brown leather saddle and reins.
```

---

## 2. ภาพนิ่ง

### Sheet R1 · Hero ขี่ม้า + ป้อมหน้าไม้ (3 × 2) → `sheets2/r1_mounts.png`

| ลำดับ | ไฟล์ | อะไร |
| --- | --- | --- |
| 1 | `mount_warrior` | อัศวินชุดเดิมของ `hero_warrior` ขี่ม้า ถือดาบชูขึ้นและโล่ฟ้า |
| 2 | `mount_archer` | นักธนูชุดเดิมของ `hero_archer` ขี่ม้า ถือธนูยาว |
| 3 | `mount_mage` | จอมเวทชุดเดิมของ `hero_mage` ขี่ม้า ถือคทาลูกไฟ |
| 4 | `ballista1` | ป้อมหน้าไม้ Lv1: หอไม้เตี้ย มีหน้าไม้ยักษ์ (ballista) อยู่ด้านบน |
| 5 | `ballista2` | Lv2: ฐานหิน หอสูงขึ้น หน้าไม้ใหญ่ขึ้น ธงฟ้า |
| 6 | `ballista3` | Lv3: หอหินเสริมเหล็ก หน้าไม้คู่ ประดับเงิน-ฟ้า |

<details><summary>prompt · Sheet R1</summary>

```
Stylized 3D-rendered game asset sheet for a bright, colorful mobile strategy / base-defense game.
Sunny daylight from the top-left, soft painterly shading, subtle rim light, saturated but clean colors,
chunky cute proportions (about 3 heads tall), readable silhouettes at small size.
Camera: 3/4 top-down view at about 50 degrees, every object facing right.
Transparent background, no ground, no cast shadow, no text, no logo, no watermark.
Layout: an exact grid of equal cells (given below). One object per cell, centered, fully inside its cell
with at least 10% empty margin on every side. Nothing may touch or cross the cell borders.
Match the exact art style, lighting, colors and camera angle of the attached reference.

The horse in cells 1-3 is the same horse: a sturdy, chunky war horse with a cute, slightly oversized head,
light grey / white coat, dark grey mane and tail, blue (#3f7fd9) and silver cloth barding with a small
silver crest on the chest, brown leather saddle and reins. Horse shown in side 3/4 view, standing,
all four hooves on the same baseline, the whole horse and rider fit inside the cell.

Grid: 3 columns x 2 rows. Cells, left to right, top to bottom:
1. the attached knight hero (same armor, blue tabard, sword and blue shield) riding the war horse, sword raised
2. the attached ranger archer hero (same blue hooded cloak) riding the same war horse, holding a longbow
3. the attached battle mage hero (same blue and gold robes) riding the same war horse, holding a staff with a glowing fire orb
4. small wooden defense tower with a giant crossbow (ballista) mounted on top, blue pennant
5. taller tower on a stone base with a bigger ballista on top, blue flag
6. strong stone and iron tower with a double ballista on top, silver and blue decorations
```
</details>

ถ้า GPT วาดม้า 3 ตัวไม่เหมือนกัน ให้สั่งทีละช่องแทน (ภาพเดี่ยว 1024×1024 หนึ่งภาพต่อหนึ่งไฟล์ ชื่อไฟล์ตามตาราง)

### Sheet R2 · ของประกอบฉากหุบเขาทะเลทราย (4 × 2) → `sheets2/r2_desert.png`

| ลำดับ | ไฟล์ | อะไร |
| --- | --- | --- |
| 1 | `cactus1` | กระบองเพชรต้นสูง แขน 2 ข้าง |
| 2 | `cactus2` | กระบองเพชรกอเตี้ย |
| 3 | `cliff1` | ก้อนหินผาสีน้ำตาลแดงก้อนใหญ่ ขอบหุบเขา |
| 4 | `cliff2` | หินผาซ้อนกันเป็นชั้น ทรงต่างจากก้อนแรก |
| 5 | `dry_bush` | พุ่มไม้แห้งสีน้ำตาลอ่อน |
| 6 | `barricade` | เครื่องกีดขวางขวางถนน: ท่อนซุงแหลมไขว้กัน มัดเชือก ธงฟ้าเล็ก |
| 7 | `boulder` | ก้อนหินกลมใหญ่ สำหรับกับดักหินกลิ้ง (กลมเกือบสมบูรณ์ หมุนแล้วดูดี) |
| 8 | ว่าง | |

<details><summary>prompt · Sheet R2</summary>

```
Stylized 3D-rendered game asset sheet for a bright, colorful mobile strategy / base-defense game.
Sunny daylight from the top-left, soft painterly shading, subtle rim light, saturated but clean colors,
readable silhouettes at small size.
Camera: 3/4 top-down view at about 50 degrees, every object facing right.
Transparent background, no ground, no cast shadow, no text, no logo, no watermark.
Layout: an exact grid of equal cells (given below). One object per cell, centered, fully inside its cell
with at least 10% empty margin on every side. Nothing may touch or cross the cell borders.
Match the exact art style, lighting, colors and camera angle of the attached reference.
Theme: warm sandy desert canyon.

Grid: 4 columns x 2 rows. Cells, left to right, top to bottom:
1. tall saguaro cactus with two arms
2. short round cluster of small cacti
3. large reddish-brown canyon boulder, rough rock face
4. layered sandstone rock formation, different shape from cell 3
5. dry tumbleweed-like desert bush, light brown
6. road barricade made of crossed sharpened logs tied with rope, small blue flag on top
7. big round grey boulder, almost a perfect sphere, cracked stone texture
8. empty
```
</details>

---

## 3. ท่าทางของ Hero ขี่ม้า

ใช้ **Prompt หลักของ Art Spec v3** แล้วแนบภาพนิ่ง `mount_<อาชีพ>` ทุกครั้ง · จุดต่างจากตัวเดินเท้า: "เท้า" คือ **กีบม้า** ต้องอยู่ระดับเดียวกันทุกเฟรม และม้ากับคนขี่ต้องอยู่ในช่องทั้งตัว (ตัวกว้างกว่าคนเดินเท้า ช่องแนวนอนพอดีอยู่แล้ว)

| อาชีพ | ท่า | ไฟล์ | เฟรม | ตาราง | ความเร็ว |
| --- | --- | --- | --- | --- | --- |
| ทุกอาชีพ | idle | `anim/mount_<อาชีพ>_idle.png` | 4 | 2 × 2 | 6 fps |
| ทุกอาชีพ | walk (ควบม้า) | `anim/mount_<อาชีพ>_walk.png` | 6 | 3 × 2 | 12 fps |
| ทุกอาชีพ | attack | `anim/mount_<อาชีพ>_attack.png` | 6 | 3 × 2 | 12 fps |
| ทุกอาชีพ | death | `anim/mount_<อาชีพ>_death.png` | 4 | 2 × 2 | 10 fps |

### Prompt หลัก (ต่อด้วยรายการเฟรมด้านล่าง)

```
Use the attached image as the exact character reference.
Same rider, same horse, same outfit, same colors, same proportions, same art style, same lighting
(sunny, from the top-left), same 3/4 top-down camera at about 50 degrees. Do not redesign anything.
Create a {N}-frame {ACT} animation sprite sheet of the rider on the horse.
Grid: {GRID}, all cells exactly the same size, read left to right, top to bottom.
Every frame: the whole horse and rider, facing right, same scale in every frame, the lowest hoof
on the same baseline near the bottom of the cell, centered, at least 10% empty margin,
nothing crossing cell borders. Transparent background, no ground, no cast shadow, no text.
```

### เฟรม · idle (ใช้ได้ทุกอาชีพ) · `{N}=4` `{ACT}=IDLE (breathing loop)` `{GRID}=2 columns x 2 rows`

```
Frame 1: horse standing still, rider upright, weapon resting
Frame 2: horse lowers its head slightly, tail swishes, rider breathes in
Frame 3: horse shakes its mane a little, one front hoof lifted slightly
Frame 4: back to the pose of frame 1, rider breathes out
```

### เฟรม · walk (ใช้ได้ทุกอาชีพ) · `{N}=6` `{ACT}=GALLOP CYCLE (loop)` `{GRID}=3 columns x 2 rows`

```
Frame 1: both front legs reaching forward, hind legs pushing back, body stretched long
Frame 2: front hooves land, hind legs start to come forward
Frame 3: all four legs gathered under the body, body slightly higher, mane flying
Frame 4: hind legs push off, front legs lift, body rising
Frame 5: front legs extended forward in the air, body at its highest
Frame 6: legs stretching out again, ready to loop back to frame 1
The rider leans slightly forward and stays on the saddle, cape and mane flowing back.
```

### เฟรม · attack · `{N}=6` `{GRID}=3 columns x 2 rows` (แต่ละอาชีพไม่เหมือนกัน)

<details><summary>mount_warrior · {ACT}=ATTACK – sword slash from horseback</summary>

```
Frame 1: horse steady, knight raises the sword over the shoulder
Frame 2: sword lifted high behind the head, body twisting back
Frame 3: big horizontal slash forward to the right, motion arc
Frame 4: follow through, sword low in front, horse rears slightly
Frame 5: horse front hooves come down, knight pulls sword back
Frame 6: return to ready pose, sword up, shield in front
```
</details>

<details><summary>mount_archer · {ACT}=ATTACK – shoot a bow from horseback</summary>

```
Frame 1: rider reaches for an arrow, bow lowered
Frame 2: arrow nocked, bow rising forward to the right
Frame 3: string pulled halfway
Frame 4: full draw to the cheek, body steady on the saddle
Frame 5: release – arrow just left the bow, string snapping, small motion lines
Frame 6: bow lowering back to the ready pose
```
</details>

<details><summary>mount_mage · {ACT}=ATTACK – cast a fireball from horseback</summary>

```
Frame 1: mage raises the staff, fire orb glowing softly
Frame 2: staff pulled back, orb glows brighter
Frame 3: staff swung forward to the right, a fireball forms at the tip
Frame 4: fireball launched forward, bright flash inside the cell
Frame 5: staff extended, small embers fading
Frame 6: back to the ready pose
```
</details>

### เฟรม · death (ใช้ได้ทุกอาชีพ) · `{N}=4` `{ACT}=DEATH` `{GRID}=2 columns x 2 rows`

```
Frame 1: hit – horse rears up in fright, rider jolts back
Frame 2: rider falls off backward, horse stumbles
Frame 3: rider on the ground, horse kneeling down
Frame 4: horse lying on its side, rider lying beside it, limp, eyes closed
```

---

## 4. ลำดับการทำ

| ลำดับ | อะไร | จำนวนภาพ |
| --- | --- | --- |
| A · ทำก่อน | `mount_<อาชีพที่เล่นบ่อย>` ภาพนิ่ง + idle, walk, attack | 4 |
| B | อีก 2 อาชีพ (ภาพนิ่งอยู่ใน Sheet R1 แล้ว) + idle, walk, attack | 6 |
| C | Sheet R1 แถวล่าง (ป้อมหน้าไม้) + Sheet R2 (ของประกอบฉาก) | 1–2 |
| D | death ของทั้ง 3 อาชีพ | 3 |
| | **รวม** | **15–16** |

ทำแค่ชุด A ก็เห็นผลชัดแล้ว Hero ที่อยู่กลางจอตลอดเวลาจะกลายเป็นขี่ม้าควบนำทัพ

### เช็กก่อนส่ง

- ม้าเหมือนกันทุกอาชีพ (สี, เกราะผ้าฟ้า-เงิน, อานม้า)
- ทุกเฟรม: ขนาดเท่ากัน กีบล่างสุดอยู่ระดับเดียวกัน ม้าไม่ล้นช่อง
- ท่าควบม้าวนกลับเฟรมแรกได้เนียน
- เฟรมไหนเพี้ยน สั่ง `Redraw only frame 4, keep all other frames exactly the same.`

## 5. ส่งภาพกลับมา

1. อัปโหลดไว้ใน repo ตามชื่อไฟล์ในตาราง: ภาพนิ่ง (sheet) ไว้ที่ `assets/sheets2/` · ท่าทางไว้ที่ `assets/anim/` แล้วกด **Commit changes** (หรือส่งไฟล์มาในแชตก็ได้)
2. บอก Claude ว่า "ใส่ภาพ Lord Rush" แล้วจะตัดภาพ จัดระดับกีบ และใส่เข้า `rush.html` ให้ (Hero ขี่ม้าวิ่งเร็วขึ้นเล็กน้อย ป้อมหน้าไม้ใช้ภาพใหม่ เครื่องกีดขวางและหินกลิ้งใช้ภาพใหม่ ฉากมีกระบองเพชรกับหินผา)
