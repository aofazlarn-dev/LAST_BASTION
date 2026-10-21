# LAST BASTION · Art Spec v2 (สไตล์สว่าง แบบเกมวางแผนบนมือถือ)

เอกสารนี้ใช้สั่ง GPT วาดภาพชุดใหม่ทั้งเกมให้ **โทนเดียวกัน** ตามภาพตัวอย่างที่เลือก: สีสด แดดสว่าง หญ้าเขียวสด ทางดินสีทราย ตัวละครหัวโตตัวเล็ก ดูเหมือนโมเดล 3D ที่เรนเดอร์สวย ๆ (เลิกใช้ pixel art)

ชื่อไฟล์ในเอกสารนี้ตรงกับในเกม Claude ตัดภาพจาก sheet ให้อัตโนมัติ · ภาพชุดเดิม (v1 ใน `docs/ART_SPEC.md`) ยังใช้ในเกมจนกว่าจะได้ชุดใหม่

---

## 1. สไตล์ (สำคัญที่สุด)

| เรื่อง | ข้อกำหนด |
| --- | --- |
| ลุค | Stylized 3D render แบบเกม strategy มือถือ: ผิวเรียบ แสงนุ่ม มีขอบแสง (rim light) บาง ๆ ไม่มีเส้นขอบดำหนา |
| แสง | กลางวันแดดอุ่น แสงมาจาก **ซ้ายบน** ทุกภาพ เงาในตัวนุ่ม ๆ |
| สี | สดอิ่ม หญ้าเขียวสด ดินสีทราย หินเทาอุ่น · **ฝ่ายเรา = ฟ้า/น้ำเงิน #3f7fd9 กับเงิน** · ศัตรูห้ามใช้ฟ้าเป็นสีหลัก |
| สัดส่วน | ตัวละครหัวโต ตัวสั้น (สูงราว 3 หัว) ท่าทางชัด อาวุธใหญ่กว่าจริงนิดหน่อย ดูออกแม้ตัวเล็กแค่ 40 px |
| มุมกล้อง | มองลงจากด้านบนเฉียง ~50° (3/4 top-down) **ทุกภาพมุมเดียวกัน** |
| ทิศ | ตัวละครและ Monster **หันขวา** (เกมพลิกซ้ายเอง) |
| พื้นหลัง | **โปร่งใส** ไม่มีพื้น ไม่มีเงาที่พื้น (เกมใส่เงาเอง) ไม่มีตัวหนังสือ ไม่มีโลโก้ |
| แสงเรืองแสง | ใช้ได้ แต่ต้องอยู่ในช่องของตัวเอง **ห้ามล้นข้ามไปช่องข้าง ๆ** |

### Master prompt (ใส่นำหน้าทุกคำสั่ง)

```
Stylized 3D-rendered game asset sheet for a bright, colorful mobile strategy / base-defense game.
Sunny daylight from the top-left, soft painterly shading, subtle rim light, saturated but clean colors,
chunky cute proportions (about 3 heads tall), readable silhouettes at small size.
Camera: 3/4 top-down view at about 50 degrees, every object facing right.
Transparent background, no ground, no cast shadow, no text, no logo, no watermark.
Layout: an exact grid of equal cells (given below). One object per cell, centered, fully inside its cell
with at least 10% empty margin on every side. Nothing may touch or cross the cell borders.
```

แล้วต่อด้วย `Grid: <คอลัมน์> columns x <แถว> rows. Cells, left to right, top to bottom:` ตามด้วยรายการ prompt ของ sheet นั้น

### เคล็ดลับให้ทุกภาพเข้าชุดกัน

1. ทำ **Sheet 01 (ตัวละคร)** ก่อน เลือกภาพที่ชอบที่สุดเก็บไว้เป็น "ภาพต้นแบบสไตล์"
2. ทุกครั้งที่สั่ง sheet ต่อไป **แนบภาพต้นแบบไปด้วย** แล้วพิมพ์ว่า `Match the exact art style, lighting, colors and camera angle of the attached reference.`
3. สั่ง Monster ทีละตระกูลในแชตเดียวกัน แล้วบอกว่า `same creature design, only change the variant` ทุกตัวในตระกูลจะหน้าตาเข้ากัน
4. ขอขนาดภาพ **1536×1024 (แนวนอน)** ทุก sheet ยกเว้นพื้นผิว (1024×1024)
5. ถ้า GPT วาดเกินช่องหรือเรียงผิด สั่งใหม่ว่า `Keep the exact grid: N columns x M rows, one object per cell, nothing crossing cells.`

---

## 2. รายการ Sheet

แต่ละ sheet ระบุ **ตาราง (คอลัมน์ × แถว)** และลำดับภาพจาก **ซ้ายไปขวา บนลงล่าง** ช่องที่เขียน "ว่าง" ให้เว้นว่างไว้

### Sheet 01 · ตัวละครฝ่ายเรา (6 × 2) → `sheets2/01_characters.png`

| ลำดับ | ไฟล์ | prompt |
| --- | --- | --- |
| 1 | hero_archer | heroic ranger archer, blue hooded cloak, silver trim, drawing a big longbow |
| 2 | hero_warrior | heroic knight, shining silver plate, blue tabard, sword and big blue shield |
| 3 | hero_mage | battle mage in blue robes with gold trim, staff with a glowing fire orb |
| 4 | hero_engineer | engineer with goggles, leather apron, giant wrench, small crossbow on the back |
| 5 | hero_healer | priestess healer in white and blue robes, glowing golden holy staff |
| 6 | worker | cheerful villager worker, straw hat, blue scarf, holding an axe |
| 7 | worker_wood | the same worker carrying a bundle of logs on the back |
| 8 | worker_stone | the same worker carrying a big sack of stones |
| 9 | u_archer | militia archer, green hood, blue tunic, short bow |
| 10 | u_sword | footman, chainmail, round blue shield, short sword |
| 11 | u_medic | field medic in white with a green cross armband and herb satchel |
| 12 | ว่าง | |

### Sheet 02 · บ้านหลักและกำแพง (6 × 4) → `sheets2/02_camp_walls.png`

กำแพงต้องต่อกันได้: ชิ้น "หน้า" ด้านซ้ายขวาตัดตรง · ชิ้น "ข้าง" คือกำแพงชุดเดียวกันที่มองจากด้านข้าง (เป็นแนวยาวขึ้นลง) ด้านบนล่างตัดตรง

| ลำดับ | ไฟล์ | prompt |
| --- | --- | --- |
| 1–5 | camp1 … camp5 | บ้านหลัก Lv1 เต็นท์ผ้าใบธงฟ้า → Lv2 เต็นท์ใหญ่มีลังเสบียง → Lv3 บ้านไม้หลังคาฟาง → Lv4 หอไม้มีฐานหิน → Lv5 ป้อมหินเล็กธงฟ้า (ใหญ่ขึ้นทีละขั้น) |
| 6 | ว่าง | |
| 7–9 | wall1 wall2 wall3 | กำแพงด้านหน้า: รั้วไม้แหลม → กำแพงหินมีใบเสมา → กำแพงหินเสริมเหล็ก |
| 10–12 | wall_side1 wall_side2 wall_side3 | กำแพงชุดเดียวกัน มองจากด้านข้าง (แนวตั้ง ยาวขึ้นลง) |
| 13–15 | wall_corner1 wall_corner2 wall_corner3 | เสามุมกำแพงชุดเดียวกัน (ไม้ → หิน → เหล็ก) |
| 16–18 | gate1 gate2 gate3 | ประตูด้านหน้า: ประตูไม้ → ประตูหิน → ซุ้มประตูเหล็ก มีธงฟ้าเล็ก ๆ |
| 19–21 | gate_side1 gate_side2 gate_side3 | ประตูชุดเดียวกัน มองจากด้านข้าง |
| 22–24 | ว่าง | |

### Sheet 03 · อาคารและของบนพื้น (6 × 3) → `sheets2/03_buildings_props.png`

| ลำดับ | ไฟล์ | prompt |
| --- | --- | --- |
| 1–3 | tower1 tower2 tower3 | ป้อมธนู: หอไม้ขาสูงหลังคาแดง → ฐานหินหัวไม้ → หอหินสูงหลังคาเหล็กธงฟ้า |
| 4 | barracks | ค่ายทหาร หลังคาแดง ป้ายดาบไขว้ ชั้นวางอาวุธ หุ่นซ้อม |
| 5 | infirmary | เต็นท์พยาบาลสีขาว กากบาทเขียว เตียงสนาม ตะกร้าสมุนไพร |
| 6 | workshop | โรงตีเหล็ก ปล่องควัน เตาไฟส้ม ทั่งตีเหล็ก |
| 7 | tree1 | ต้นโอ๊กพุ่มกลมสีเขียวสด |
| 8 | tree2 | ต้นสนทรงกรวย |
| 9 | rock | ก้อนหินใหญ่สีเทาอุ่น มีมอส |
| 10 | stump | ตอไม้ |
| 11 | pebbles | กองเศษหิน |
| 12 | tuft | กอหญ้า |
| 13 | flower | ดอกไม้ป่าเล็ก ๆ |
| 14 | firepit | กองไฟล้อมหิน |
| 15 | loot_bag | ถุงหนังของดรอป เรืองแสงทองบาง ๆ |
| 16–18 | ว่าง | |

### พื้นผิว (ทีละภาพ · 1024×1024 · ต่อกันได้ไร้รอยต่อ · ไม่ต้องโปร่งใส)

Prompt นำหน้า (ใช้แทน Master prompt): `Seamless tileable top-down ground texture for a bright stylized mobile strategy game, sunny, soft painterly, no objects, no text.`

| ไฟล์ | prompt |
| --- | --- |
| `sheets2/grass.png` | lush bright green grass with tiny flowers |
| `sheets2/ground_forest.png` | darker forest floor with moss, leaves and roots |
| `sheets2/ground_rocky.png` | rocky grey gravel with sparse dry grass |
| `sheets2/ground_waste.png` | cracked ashen wasteland with faint red glow in the cracks |
| `sheets2/water.png` | clear turquoise-blue lake water with soft ripples |
| `sheets2/dirt.png` | warm sandy dirt path |

### Sheet 10 · ไอเทม 18 ชิ้น (6 × 3) → `sheets2/10_items.png`

ไอคอนวางเฉียง สีตามระดับ: ธรรมดา = ไม้/หนังน้ำตาล · หายาก = ฟ้าเงิน · มหากาพย์ = ม่วงหรือทองเรืองแสง

| แถว | ไฟล์ (ซ้าย → ขวา) |
| --- | --- |
| 1 | bow_common1 ธนูไม้ · bow_common2 ธนูสั้น · bow_common3 ธนูพราน · bow_rare1 ธนูยาวพราน · bow_rare2 ธนูกระดูกหมาป่า · bow_rare3 ธนูไม้มะเกลือ |
| 2 | bow_epic1 ธนูเงาจันทร์ · bow_epic2 ธนูเพลิงอรุณ · bow_epic3 ธนูพายุคลั่ง · armor_common1 เสื้อหนังเก่า · armor_common2 เสื้อผ้าป่าน · armor_common3 เสื้อนวม |
| 3 | armor_rare1 เกราะหนังหมาป่า · armor_rare2 เสื้อคลุมพราน · armor_rare3 เกราะไม้ไผ่สาน · armor_epic1 เกราะเหล็กกล้า · armor_epic2 เสื้อคลุมรัตติกาล · armor_epic3 เกราะเกล็ดงู |

### Sheet 11 · เอฟเฟกต์ (6 × 3) → `sheets2/11_fx.png`

| แถว | ไฟล์ (ซ้าย → ขวา) |
| --- | --- |
| 1 | fx_arrow ลูกธนูชี้ขวา · fx_bolt ลูกพลังเวท · fx_fireball ลูกไฟพุ่งขวา · fx_frostbolt ลูกน้ำแข็งพุ่งขวา · fx_web ใยแมงมุมพุ่งขวา · fx_blast ระเบิดสีส้ม |
| 2 | fx_hit ประกายโดนตี · fx_heal ประกายรักษาสีเขียว · fx_levelup วงแสงทองพุ่งขึ้น · fx_recall วงวาร์ปสีฟ้า (มองจากบน) · fx_volley ลูกธนูหลายดอกแผ่ไปทางขวา · fx_sunburn Monster ไหม้เป็นเถ้า |
| 3 | fx_rubble ซากไม้และหินจากอาคารพัง · fx_flame เปลวไฟ · fx_frost ประกายน้ำแข็ง · ว่าง · ว่าง · ว่าง |

### Sheet 12 · ไอคอน UI (6 × 4) → `sheets2/12_ui.png`

ไอคอนทรงชัด ขอบเข้ม ใช้ในปุ่มขนาดเล็ก

| แถว | ไฟล์ (ซ้าย → ขวา) |
| --- | --- |
| 1 | ui_wood ท่อนไม้ · ui_stone ก้อนหิน · ui_hp หัวใจ · ui_mp คริสตัลฟ้า · ui_exp ดาวทอง · ui_skill_volley ลูกธนูสามดอก |
| 2 | ui_build ค้อน · ui_repair โล่มีค้อน · ui_bag เป้ · ui_home บ้าน · ui_map แผนที่ · ui_menu เฟือง |
| 3 | ui_bestiary หนังสือมอนสเตอร์ · ui_night พระจันทร์เสี้ยว · ui_day ดวงอาทิตย์ · ui_warn ป้ายเตือน · ui_worker คนงาน · ui_army หมวกทหาร |
| 4 | ui_mode_free เข็มทิศ · ui_mode_follow รอยเท้าตามธง · ui_mode_guard โล่มีป้อม · ui_res_heroweapon ธนู+ลูกศรขึ้น · ui_res_unitweapon ดาบ+ลูกศรขึ้น · ui_res_unitarmor โล่+ลูกศรขึ้น |

---

## 3. Monster (1 sheet ต่อ 1 ตระกูล · 16 ตระกูล + บอส)

ทุกตัวในตระกูลเดียวกันใช้ **ตัวต้นแบบเดียวกัน** เปลี่ยนแค่ธาตุและสี ระดับสูงให้ตัวใหญ่ขึ้น หน้าดุขึ้น แต่ยังเป็นสไตล์สดใสเดียวกัน (น่ากลัวแบบการ์ตูน ไม่สยอง)

- ระดับต่ำ 8 แบบ: ตาราง **4 × 2**
- ระดับกลางและสูง 5 แบบ: ตาราง **3 × 2** (ช่องสุดท้ายว่าง)
- บอส 5 ตัว: ตาราง **3 × 2** (ช่องสุดท้ายว่าง) ตัวใหญ่ มีมงกุฎทอง


### zombie · ระดับต่ำ (4 × 2) → `sheets2/mon_zombie.png`

ตัวต้นแบบ: *a shambling rotting zombie, hunched, arms stretched forward, torn rags*

| ลำดับ | ไฟล์ | ชื่อ | ธาตุ (ต่อท้าย prompt) |
| --- | --- | --- | --- |
| 1 | zombie0 | ซอมบี้ | normal base version |
| 2 | zombie1 | ซอมบี้เน่า | rotting, mossy and decayed (yellow-brown tint) |
| 3 | zombie2 | ซอมบี้พิษ | poisonous, dripping toxic green ooze |
| 4 | zombie3 | ซอมบี้เพลิง | burning, flames and embers on its body (orange-red) |
| 5 | zombie4 | ซอมบี้น้ำแข็ง | frozen, ice crystals and frost (pale blue) |
| 6 | zombie5 | ซอมบี้เงา | shadowy, made of dark purple smoke |
| 7 | zombie6 | ซอมบี้หิน | stone-skinned, rocky grey armor plates |
| 8 | zombie7 | ซอมบี้คลั่ง | berserk, red glowing eyes, battle scars, furious |

### wolf · ระดับต่ำ (4 × 2) → `sheets2/mon_wolf.png`

ตัวต้นแบบ: *a lean feral wolf in mid-run, bared fangs, bristling fur*

| ลำดับ | ไฟล์ | ชื่อ | ธาตุ (ต่อท้าย prompt) |
| --- | --- | --- | --- |
| 1 | wolf0 | หมาป่า | normal base version |
| 2 | wolf1 | หมาป่าเน่า | rotting, mossy and decayed (yellow-brown tint) |
| 3 | wolf2 | หมาป่าพิษ | poisonous, dripping toxic green ooze |
| 4 | wolf3 | หมาป่าเพลิง | burning, flames and embers on its body (orange-red) |
| 5 | wolf4 | หมาป่าน้ำแข็ง | frozen, ice crystals and frost (pale blue) |
| 6 | wolf5 | หมาป่าเงา | shadowy, made of dark purple smoke |
| 7 | wolf6 | หมาป่าหิน | stone-skinned, rocky grey armor plates |
| 8 | wolf7 | หมาป่าคลั่ง | berserk, red glowing eyes, battle scars, furious |

### slime · ระดับต่ำ (4 × 2) → `sheets2/mon_slime.png`

ตัวต้นแบบ: *a round gelatinous slime blob with glowing eyes and a bubbling core about to burst*

| ลำดับ | ไฟล์ | ชื่อ | ธาตุ (ต่อท้าย prompt) |
| --- | --- | --- | --- |
| 1 | slime0 | สไลม์ | normal base version |
| 2 | slime1 | สไลม์เน่า | rotting, mossy and decayed (yellow-brown tint) |
| 3 | slime2 | สไลม์พิษ | poisonous, dripping toxic green ooze |
| 4 | slime3 | สไลม์เพลิง | burning, flames and embers on its body (orange-red) |
| 5 | slime4 | สไลม์น้ำแข็ง | frozen, ice crystals and frost (pale blue) |
| 6 | slime5 | สไลม์เงา | shadowy, made of dark purple smoke |
| 7 | slime6 | สไลม์หิน | stone-skinned, rocky grey armor plates |
| 8 | slime7 | สไลม์คลั่ง | berserk, red glowing eyes, battle scars, furious |

### bat · ระดับต่ำ (4 × 2) → `sheets2/mon_bat.png`

ตัวต้นแบบ: *a giant bat with leathery wings fully spread, glowing eyes*

| ลำดับ | ไฟล์ | ชื่อ | ธาตุ (ต่อท้าย prompt) |
| --- | --- | --- | --- |
| 1 | bat0 | ค้างคาว | normal base version |
| 2 | bat1 | ค้างคาวเน่า | rotting, mossy and decayed (yellow-brown tint) |
| 3 | bat2 | ค้างคาวพิษ | poisonous, dripping toxic green ooze |
| 4 | bat3 | ค้างคาวเพลิง | burning, flames and embers on its body (orange-red) |
| 5 | bat4 | ค้างคาวน้ำแข็ง | frozen, ice crystals and frost (pale blue) |
| 6 | bat5 | ค้างคาวเงา | shadowy, made of dark purple smoke |
| 7 | bat6 | ค้างคาวหิน | stone-skinned, rocky grey armor plates |
| 8 | bat7 | ค้างคาวคลั่ง | berserk, red glowing eyes, battle scars, furious |

### skel · ระดับต่ำ (4 × 2) → `sheets2/mon_skel.png`

ตัวต้นแบบ: *a skeleton archer holding a crude bow, cracked skull, bony ribcage*

| ลำดับ | ไฟล์ | ชื่อ | ธาตุ (ต่อท้าย prompt) |
| --- | --- | --- | --- |
| 1 | skel0 | โครงกระดูกนักธนู | normal base version |
| 2 | skel1 | โครงกระดูกนักธนูเน่า | rotting, mossy and decayed (yellow-brown tint) |
| 3 | skel2 | โครงกระดูกนักธนูพิษ | poisonous, dripping toxic green ooze |
| 4 | skel3 | โครงกระดูกนักธนูเพลิง | burning, flames and embers on its body (orange-red) |
| 5 | skel4 | โครงกระดูกนักธนูน้ำแข็ง | frozen, ice crystals and frost (pale blue) |
| 6 | skel5 | โครงกระดูกนักธนูเงา | shadowy, made of dark purple smoke |
| 7 | skel6 | โครงกระดูกนักธนูหิน | stone-skinned, rocky grey armor plates |
| 8 | skel7 | โครงกระดูกนักธนูคลั่ง | berserk, red glowing eyes, battle scars, furious |

### ghoul · ระดับกลาง (3 × 2) → `sheets2/mon_ghoul.png`

ตัวต้นแบบ: *a gaunt pale ghoul with long claws and sunken eyes, crouched*

| ลำดับ | ไฟล์ | ชื่อ | ธาตุ (ต่อท้าย prompt) |
| --- | --- | --- | --- |
| 1 | ghoul0 | กูล | normal base version |
| 2 | ghoul1 | กูลเน่า | rotting, mossy and decayed (yellow-brown tint) |
| 3 | ghoul2 | กูลพิษ | poisonous, dripping toxic green ooze |
| 4 | ghoul3 | กูลเพลิง | burning, flames and embers on its body (orange-red) |
| 5 | ghoul4 | กูลน้ำแข็ง | frozen, ice crystals and frost (pale blue) |

### spider · ระดับกลาง (3 × 2) → `sheets2/mon_spider.png`

ตัวต้นแบบ: *a giant hairy spider with eight long legs and a bulbous abdomen*

| ลำดับ | ไฟล์ | ชื่อ | ธาตุ (ต่อท้าย prompt) |
| --- | --- | --- | --- |
| 1 | spider0 | แมงมุมยักษ์ | normal base version |
| 2 | spider1 | แมงมุมยักษ์เน่า | rotting, mossy and decayed (yellow-brown tint) |
| 3 | spider2 | แมงมุมยักษ์พิษ | poisonous, dripping toxic green ooze |
| 4 | spider3 | แมงมุมยักษ์เพลิง | burning, flames and embers on its body (orange-red) |
| 5 | spider4 | แมงมุมยักษ์น้ำแข็ง | frozen, ice crystals and frost (pale blue) |

### orc · ระดับกลาง (3 × 2) → `sheets2/mon_orc.png`

ตัวต้นแบบ: *a hulking orc brute with tusks, crude armor and a heavy spiked club*

| ลำดับ | ไฟล์ | ชื่อ | ธาตุ (ต่อท้าย prompt) |
| --- | --- | --- | --- |
| 1 | orc0 | ออร์ก | normal base version |
| 2 | orc1 | ออร์กเน่า | rotting, mossy and decayed (yellow-brown tint) |
| 3 | orc2 | ออร์กพิษ | poisonous, dripping toxic green ooze |
| 4 | orc3 | ออร์กเพลิง | burning, flames and embers on its body (orange-red) |
| 5 | orc4 | ออร์กน้ำแข็ง | frozen, ice crystals and frost (pale blue) |

### wisp · ระดับกลาง (3 × 2) → `sheets2/mon_wisp.png`

ตัวต้นแบบ: *a floating fire wisp, a ball of living flame with a bright core*

| ลำดับ | ไฟล์ | ชื่อ | ธาตุ (ต่อท้าย prompt) |
| --- | --- | --- | --- |
| 1 | wisp0 | ภูตไฟ | normal base version |
| 2 | wisp1 | ภูตไฟเน่า | rotting, mossy and decayed (yellow-brown tint) |
| 3 | wisp2 | ภูตไฟพิษ | poisonous, dripping toxic green ooze |
| 4 | wisp3 | ภูตไฟเพลิง | burning, flames and embers on its body (orange-red) |
| 5 | wisp4 | ภูตไฟน้ำแข็ง | frozen, ice crystals and frost (pale blue) |

### bonemage · ระดับกลาง (3 × 2) → `sheets2/mon_bonemage.png`

ตัวต้นแบบ: *a skeleton mage in a tattered robe holding a bone staff with a glowing orb*

| ลำดับ | ไฟล์ | ชื่อ | ธาตุ (ต่อท้าย prompt) |
| --- | --- | --- | --- |
| 1 | bonemage0 | นักเวทกระดูก | normal base version |
| 2 | bonemage1 | นักเวทกระดูกเน่า | rotting, mossy and decayed (yellow-brown tint) |
| 3 | bonemage2 | นักเวทกระดูกพิษ | poisonous, dripping toxic green ooze |
| 4 | bonemage3 | นักเวทกระดูกเพลิง | burning, flames and embers on its body (orange-red) |
| 5 | bonemage4 | นักเวทกระดูกน้ำแข็ง | frozen, ice crystals and frost (pale blue) |

### beetle · ระดับกลาง (3 × 2) → `sheets2/mon_beetle.png`

ตัวต้นแบบ: *a large armored bomb beetle with a glowing fuse-like horn*

| ลำดับ | ไฟล์ | ชื่อ | ธาตุ (ต่อท้าย prompt) |
| --- | --- | --- | --- |
| 1 | beetle0 | ด้วงระเบิด | normal base version |
| 2 | beetle1 | ด้วงระเบิดเน่า | rotting, mossy and decayed (yellow-brown tint) |
| 3 | beetle2 | ด้วงระเบิดพิษ | poisonous, dripping toxic green ooze |
| 4 | beetle3 | ด้วงระเบิดเพลิง | burning, flames and embers on its body (orange-red) |
| 5 | beetle4 | ด้วงระเบิดน้ำแข็ง | frozen, ice crystals and frost (pale blue) |

### knight · ระดับสูง (3 × 2) → `sheets2/mon_knight.png`

ตัวต้นแบบ: *an undead death knight in dark plate armor with a greatsword and shield, glowing visor*

| ลำดับ | ไฟล์ | ชื่อ | ธาตุ (ต่อท้าย prompt) |
| --- | --- | --- | --- |
| 1 | knight0 | อัศวินมรณะ | normal base version |
| 2 | knight1 | อัศวินมรณะเน่า | rotting, mossy and decayed (yellow-brown tint) |
| 3 | knight2 | อัศวินมรณะพิษ | poisonous, dripping toxic green ooze |
| 4 | knight3 | อัศวินมรณะเพลิง | burning, flames and embers on its body (orange-red) |
| 5 | knight4 | อัศวินมรณะน้ำแข็ง | frozen, ice crystals and frost (pale blue) |

### were · ระดับสูง (3 × 2) → `sheets2/mon_were.png`

ตัวต้นแบบ: *a muscular werewolf, half man half wolf, running on all fours*

| ลำดับ | ไฟล์ | ชื่อ | ธาตุ (ต่อท้าย prompt) |
| --- | --- | --- | --- |
| 1 | were0 | มนุษย์หมาป่า | normal base version |
| 2 | were1 | มนุษย์หมาป่าเน่า | rotting, mossy and decayed (yellow-brown tint) |
| 3 | were2 | มนุษย์หมาป่าพิษ | poisonous, dripping toxic green ooze |
| 4 | were3 | มนุษย์หมาป่าเพลิง | burning, flames and embers on its body (orange-red) |
| 5 | were4 | มนุษย์หมาป่าน้ำแข็ง | frozen, ice crystals and frost (pale blue) |

### golem · ระดับสูง (3 × 2) → `sheets2/mon_golem.png`

ตัวต้นแบบ: *a massive stone golem made of stacked boulders with glowing cracks*

| ลำดับ | ไฟล์ | ชื่อ | ธาตุ (ต่อท้าย prompt) |
| --- | --- | --- | --- |
| 1 | golem0 | โกเลมหิน | stone-skinned, rocky grey armor plates |
| 2 | golem1 | โกเลมหินเน่า | rotting, mossy and decayed (yellow-brown tint) |
| 3 | golem2 | โกเลมหินพิษ | poisonous, dripping toxic green ooze |
| 4 | golem3 | โกเลมหินเพลิง | burning, flames and embers on its body (orange-red) |
| 5 | golem4 | โกเลมหินน้ำแข็ง | frozen, ice crystals and frost (pale blue) |

### demon · ระดับสูง (3 × 2) → `sheets2/mon_demon.png`

ตัวต้นแบบ: *a winged demon with horns, bat-like wings and red skin*

| ลำดับ | ไฟล์ | ชื่อ | ธาตุ (ต่อท้าย prompt) |
| --- | --- | --- | --- |
| 1 | demon0 | ปีศาจปีก | normal base version |
| 2 | demon1 | ปีศาจปีกเน่า | rotting, mossy and decayed (yellow-brown tint) |
| 3 | demon2 | ปีศาจปีกพิษ | poisonous, dripping toxic green ooze |
| 4 | demon3 | ปีศาจปีกเพลิง | burning, flames and embers on its body (orange-red) |
| 5 | demon4 | ปีศาจปีกน้ำแข็ง | frozen, ice crystals and frost (pale blue) |

### lich · ระดับสูง (3 × 2) → `sheets2/mon_lich.png`

ตัวต้นแบบ: *a hooded lich sorcerer with a skull face and a staff topped with a glowing crystal*

| ลำดับ | ไฟล์ | ชื่อ | ธาตุ (ต่อท้าย prompt) |
| --- | --- | --- | --- |
| 1 | lich0 | ลิชมรณะ | normal base version |
| 2 | lich1 | ลิชมรณะเน่า | rotting, mossy and decayed (yellow-brown tint) |
| 3 | lich2 | ลิชมรณะพิษ | poisonous, dripping toxic green ooze |
| 4 | lich3 | ลิชมรณะเพลิง | burning, flames and embers on its body (orange-red) |
| 5 | lich4 | ลิชมรณะน้ำแข็ง | frozen, ice crystals and frost (pale blue) |

### บอส (3 × 2) → `sheets2/mon_boss.png`

| ลำดับ | ไฟล์ | ชื่อ | prompt |
| --- | --- | --- | --- |
| 1 | boss0 | ราชาซอมบี้ | the Zombie King, a giant zombie wearing a rusted golden crown and royal rags, much larger and menacing |
| 2 | boss1 | จ้าวฝูงหมาป่า | the Alpha Wolf Lord, a huge black dire wolf with a golden crown-like mane and scars |
| 3 | boss2 | ราชินีแมงมุม | the Spider Queen, an enormous spider with a crown of horns, egg sacs on its back, spitting web |
| 4 | boss3 | โกเลมโบราณ | the Ancient Golem, a towering golem of ancient carved stone with golden runes and a crown of crystals |
| 5 | boss4 | มังกรเงา | the Shadow Dragon, a dark dragon with huge wings, smoky shadow body and glowing eyes |

---

## 4. ท่าทางแบบเฟรม (ทำทีหลัง · ไม่บังคับ)

ตอนนี้เกมขยับตัวละครด้วยโค้ด (เดินโยก ง้างโจมตี ล้มตาย) ถ้าอยากได้อนิเมชันจริง ทำ sheet ท่าทางทีละตัว เริ่มจาก hero_archer, worker, zombie0, wolf0

ตาราง **6 × 4** ขนาด 1536×1024 · ตัวละครตัวเดียวกันทุกช่อง ขนาดเท่ากัน เท้าอยู่ระดับเดียวกันทุกช่อง หันขวา

| แถว | ท่า | จำนวนเฟรม |
| --- | --- | --- |
| 1 | idle ยืนหายใจ | 4 (ช่อง 5–6 ว่าง) |
| 2 | walk เดิน | 6 |
| 3 | attack โจมตี (ง้าง → ปล่อย → กลับ) | 6 |
| 4 | death ล้มลง | 4 (ช่อง 5–6 ว่าง) |

ชื่อไฟล์: `sheets2/anim_<ชื่อตัว>.png` เช่น `anim_hero_archer.png`

GPT มักวาดหลายเฟรมให้หน้าตาเหมือนกันได้ไม่ดี ถ้าไม่เนียน ลองเครื่องมือทำอนิเมชันจากภาพเดียว เช่น PixelLab หรือส่งแค่ภาพนิ่งมา ผมใช้วิธีขยับด้วยโค้ดต่อได้

---

## 5. ส่งภาพกลับมา

1. อัปโหลดไว้ในโฟลเดอร์ `assets/sheets2/` ของ repo ตั้งชื่อตามที่ระบุ แล้วกด **Commit changes**
2. ไม่ต้องครบทีเดียว ส่งทีละ sheet ได้ ภาพไหนยังไม่มี เกมใช้ชุดเดิมไปก่อน
3. บอก Claude ว่า "ใส่ภาพชุดใหม่" แล้วจะตัด ย่อ และใส่เข้าเกมให้

**ลำดับที่แนะนำ:** 01 ตัวละคร → พื้นผิว grass / water / dirt → 02 กำแพง → 03 อาคาร → Monster ระดับต่ำ 5 ตระกูล + บอส → ที่เหลือ

