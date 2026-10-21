# LAST BASTION · รายการภาพสำหรับให้ AI วาด

ภาพทั้งหมดในเกมตอนนี้วาดด้วยโค้ดชั่วคราว ไฟล์นี้คือรายการภาพที่ต้องการ ชื่อไฟล์ตรงกับรหัสในเกม เมื่อได้ภาพแล้ววางในโฟลเดอร์ `assets/` ตามชื่อไฟล์ด้านล่าง แล้วบอก Claude ให้เชื่อมภาพเข้าเกม

อัปเดตล่าสุด: เวอร์ชัน 0.11 (21 ต.ค. 2026) · รวม **196 ภาพ** · เพิ่มไอคอนไอเทมรายชิ้น, ไอคอน UI, พื้นตามโซน, เอฟเฟกต์เพิ่ม

## ทำชุดไหนก่อน (แนะนำ)

ไม่ต้องทำครบทีเดียว ภาพไหนยังไม่มีเกมใช้ภาพวาดด้วยโค้ดแทน แนะนำทำตามลำดับนี้ เห็นผลในเกมเร็วที่สุด

| ชุด | ภาพ | จำนวน | ทำไม |
| --- | --- | --- | --- |
| A · เห็นตลอดเวลา | `heroes/archer`, `units/*`, `tiles/*`, `buildings/camp1`, `wall1`, `gate1`, `tower1` | 25 | อยู่บนจอทุกวินาที |
| B · Monster ที่เจอบ่อย | Monster ระดับต่ำ 40 ตัว + `boss0` | 41 | คืนแรกเจอแต่ตัวพวกนี้ |
| C · ไอคอน | `ui/*`, `items/*` | 42 | HUD กระเป๋า และแผงอาคาร |
| D · อาคารเลเวลสูง | สิ่งก่อสร้างที่เหลือ | 13 | เห็นเมื่ออัปเกรด |
| E · ที่เหลือ | Monster กลาง/สูง/บอส, `fx/*`, Hero อื่น | 75 | เจอช่วงท้ายเกม |

## กติกาทุกภาพ (สำคัญ)

| เรื่อง | ข้อกำหนด |
| --- | --- |
| มุมมอง | **Top-down มองจากด้านบนเฉียงเล็กน้อย** (3/4 top-down) เหมือนเกม 2D มุมสูง |
| ทิศทาง | ตัวละครและ Monster **หันหน้าไปทางขวา** (เกมจะหมุนภาพเอง) |
| พื้นหลัง | **โปร่งใส (PNG transparent)** ห้ามมีพื้น ห้ามมีเงาบนพื้น (เกมใส่เงาเอง) |
| สไตล์ | Pixel art แบบ 32-bit นุ่ม ๆ หรือ painterly 2D ให้เหมือนกันทุกภาพ โทนมืด dark fantasy เข้ากับภาพปก |
| กรอบ | ตัวละครอยู่กลางภาพ เว้นขอบรอบละ ~8% ไม่ล้นขอบ |
| ขนาดไฟล์ | ตามที่ระบุในแต่ละหมวด (สี่เหลี่ยมจัตุรัส) |
| ข้อความ | ห้ามมีตัวหนังสือ โลโก้ หรือลายน้ำในภาพ |
| สีทีม | ฝ่ายเรา = **ฟ้า #6fb6e8** (ผ้า ธง) · ศัตรูห้ามใช้ฟ้า เพื่อแยกฝ่ายออกเร็ว |
| อ่านง่าย | ในเกมตัวละครเล็กมาก (ราว 30–60 px บนจอ) ต้องดูออกจากรูปทรงอย่างเดียว ไม่ต้องใส่รายละเอียดเล็ก ๆ |

### Master prompt (ใช้นำหน้าทุก prompt)

```
Top-down 3/4 view game sprite for a dark fantasy survival base-defense game, single character centered,
facing right, transparent background, no ground, no shadow, no text, clean silhouette readable at small size,
consistent soft pixel-art style, moody lighting with warm torch highlights.
Subject:
```

แล้วต่อด้วยคำอธิบายในคอลัมน์ "prompt" ของแต่ละรายการ เช่น

```
Top-down 3/4 view game sprite ... Subject: a shambling rotting zombie, hunched, arms stretched forward, torn rags, poisonous, dripping toxic green ooze
```

**เคล็ดลับ:** สั่งทีละตระกูล (เช่น ซอมบี้ 8 แบบ) ในแชตเดียวกัน แล้วบอก GPT ว่า "keep the same character design and style, only change the variant" ภาพจะเข้าชุดกัน

---

## 1. Hero (5 อาชีพ · 192×192 px · โฟลเดอร์ `heroes/`)

| ไฟล์ | อาชีพ | prompt |
| --- | --- | --- |
| `heroes/archer.png` | Archer (เล่นได้แล้ว) | a hooded ranger archer in a blue cloak drawing a longbow, quiver on back, heroic |
| `heroes/warrior.png` | Warrior (ยังไม่เปิด) | a heavily armored warrior with sword and large shield, blue tabard, heroic |
| `heroes/mage.png` | Mage (ยังไม่เปิด) | a battle mage in blue robes holding a staff with a fire orb, heroic |
| `heroes/engineer.png` | Engineer (ยังไม่เปิด) | an engineer with goggles, leather apron, wrench and a small crossbow turret on the back |
| `heroes/healer.png` | Healer (ยังไม่เปิด) | a priestess healer in white and blue robes with a glowing holy staff |

## 2. ยูนิตฝ่ายเรา (128×128 px · โฟลเดอร์ `units/`)

ทุกตัวใส่สีประจำทีม **ฟ้า (#6fb6e8)** ที่ผ้าคลุมหรือเสื้อ

| ไฟล์ | ยูนิต | prompt |
| --- | --- | --- |
| `units/worker.png` | คนงาน | a villager worker with a straw hat carrying an axe, simple brown clothes, blue scarf |
| `units/worker_wood.png` | คนงาน (แบกไม้) | the same villager worker carrying a bundle of logs on the shoulder |
| `units/worker_stone.png` | คนงาน (แบกหิน) | the same villager worker carrying a sack of stones |
| `units/archer.png` | พลธนู | a militia archer in a green hood and blue tunic holding a short bow |
| `units/swordsman.png` | นักดาบ | a footman swordsman in chainmail with a blue round shield and short sword |
| `units/medic.png` | หมอ | a field medic in white robes with a green cross armband and a satchel of herbs |

## 3. สิ่งก่อสร้าง (โฟลเดอร์ `buildings/`)

มุมเดียวกับตัวละคร (มองเฉียงจากด้านบน) ฐานอาคารวางชิดขอบล่างของภาพ

| ไฟล์ | อาคาร | ขนาด | prompt |
| --- | --- | --- | --- |
| `buildings/camp1.png` | บ้านหลัก Lv1 | 256×256 | a canvas camp tent with a blue flag and a small campfire beside it |
| `buildings/camp2.png` | บ้านหลัก Lv2 | 256×256 | a larger reinforced tent with wooden poles, supply crates and a blue banner |
| `buildings/camp3.png` | บ้านหลัก Lv3 | 256×256 | a wooden longhouse with a steep roof, lit windows and a blue flag |
| `buildings/camp4.png` | บ้านหลัก Lv4 | 256×256 | a fortified wooden hall with stone foundation, watch platform and banners |
| `buildings/camp5.png` | บ้านหลัก Lv5 | 256×256 | a small stone keep with towers, blue banners and torches, the last bastion of humanity |
| `buildings/wall1.png` | กำแพงไม้ | 96×128 | a straight segment of sharpened wooden palisade stakes |
| `buildings/wall2.png` | กำแพงหิน | 96×128 | a straight segment of stacked grey stone wall with battlements |
| `buildings/wall3.png` | กำแพงเหล็ก | 96×128 | a stone wall segment reinforced with iron bands and iron spikes on top |
| `buildings/gate1.png` | ประตูไม้ | 96×128 | a wooden palisade gate with crossed beams, a small blue flag on top |
| `buildings/gate2.png` | ประตูหิน | 96×128 | a stone gatehouse with a wooden door and a blue flag |
| `buildings/gate3.png` | ประตูเหล็ก | 96×128 | a stone gatehouse with a heavy iron portcullis |
| `buildings/tower1.png` | ป้อมธนู Lv1 | 128×192 | a wooden archer watchtower on stilts with a red pointed roof |
| `buildings/tower2.png` | ป้อมธนู Lv2 | 128×192 | an archer tower with a stone base, wooden top and red roof |
| `buildings/tower3.png` | ป้อมธนู Lv3 | 128×192 | a tall stone archer tower with an iron roof, arrow slits and a big blue banner |
| `buildings/barracks.png` | ค่ายทหาร | 192×192 | a military barracks hall with a red roof, crossed swords sign, weapon rack and training dummy |
| `buildings/infirmary.png` | สถานพยาบาล | 192×192 | a white canvas field hospital tent with a green cross, cots and herb baskets |
| `buildings/workshop.png` | Workshop | 192×192 | a blacksmith workshop with a smoking chimney, glowing forge and anvil |

## 4. ฉากและทรัพยากร (โฟลเดอร์ `tiles/`)

| ไฟล์ | อะไร | ขนาด | prompt |
| --- | --- | --- | --- |
| `tiles/grass.png` | พื้นหญ้า (ต่อกันได้ไร้รอยต่อ) | 128×128 | seamless tileable dark green grass ground texture, top-down, subtle variation |
| `tiles/tree1.png` | ต้นไม้ 1 | 128×160 | a leafy dark green oak tree seen from above at an angle |
| `tiles/tree2.png` | ต้นไม้ 2 | 128×160 | a pine tree seen from above at an angle |
| `tiles/rock.png` | ก้อนหิน | 128×128 | a large grey boulder with cracks |
| `tiles/stump.png` | ตอไม้ | 64×64 | a cut tree stump |
| `tiles/pebbles.png` | เศษหิน | 64×64 | a small pile of broken stones |
| `tiles/water.png` | น้ำ (ต่อกันได้) | 128×128 | seamless tileable dark blue lake water texture, top-down |
| `tiles/ground_forest.png` | พื้นโซนป่าลึก (ต่อกันได้) | 128×128 | seamless tileable dark forest floor, moss, fallen leaves and roots, top-down |
| `tiles/ground_rocky.png` | พื้นโซนหุบเขาหิน (ต่อกันได้) | 128×128 | seamless tileable rocky grey gravel ground with sparse dry grass, top-down |
| `tiles/ground_waste.png` | พื้นโซนดินแดนรกร้าง (ต่อกันได้) | 128×128 | seamless tileable cracked dead ashen wasteland ground with faint red glow, top-down |
| `tiles/tuft.png` | กอหญ้าประดับ | 64×64 | a small tuft of wild grass |
| `tiles/flower.png` | ดอกไม้ประดับ | 32×32 | a tiny cluster of pale wildflowers |
| `tiles/firepit.png` | กองไฟหน้าค่าย | 96×96 | a small stone-ringed campfire with flames |
| `tiles/loot_bag.png` | ของดรอปบนพื้น | 64×64 | a small glowing leather loot pouch lying on the ground |

## 5. ไอเทม (18 ชิ้น · 128×128 px · โฟลเดอร์ `items/`)

ไอคอนวางบนพื้นหลังโปร่งใส หนึ่งไฟล์ต่อชื่อไอเทมในเกม แยกสีตามระดับ: ธรรมดา = เทา/น้ำตาล, หายาก = ฟ้า, มหากาพย์ = ม่วงหรือทองเรืองแสง
ใช้ Master prompt แบบไอคอน: `Game inventory icon, single object centered, transparent background, no text, dark fantasy soft pixel-art style. Subject:`

| ไฟล์ | ชื่อในเกม | ระดับ | prompt |
| --- | --- | --- | --- |
| `items/bow_common1.png` | ธนูไม้ | ธรรมดา | a simple wooden bow icon |
| `items/bow_common2.png` | ธนูสั้น | ธรรมดา | a short recurve bow icon |
| `items/bow_common3.png` | ธนูพราน | ธรรมดา | a hunter's bow wrapped in leather icon |
| `items/bow_rare1.png` | ธนูยาวพราน | หายาก | an ornate ranger longbow with blue gems icon |
| `items/bow_rare2.png` | ธนูกระดูกหมาป่า | หายาก | a bow carved from wolf bone with fur grip icon |
| `items/bow_rare3.png` | ธนูไม้มะเกลือ | หายาก | a black ebony wood bow with silver tips icon |
| `items/bow_epic1.png` | ธนูเงาจันทร์ | มหากาพย์ | a legendary glowing purple crescent moon bow icon |
| `items/bow_epic2.png` | ธนูเพลิงอรุณ | มหากาพย์ | a legendary bow wreathed in golden dawn fire icon |
| `items/bow_epic3.png` | ธนูพายุคลั่ง | มหากาพย์ | a legendary bow crackling with storm lightning icon |
| `items/armor_common1.png` | เสื้อหนังเก่า | ธรรมดา | a worn old leather vest icon |
| `items/armor_common2.png` | เสื้อผ้าป่าน | ธรรมดา | a plain hemp cloth shirt icon |
| `items/armor_common3.png` | เสื้อนวม | ธรรมดา | a padded quilted gambeson icon |
| `items/armor_rare1.png` | เกราะหนังหมาป่า | หายาก | a wolf-fur leather armor with blue trim icon |
| `items/armor_rare2.png` | เสื้อคลุมพราน | หายาก | a green ranger cloak with hood icon |
| `items/armor_rare3.png` | เกราะไม้ไผ่สาน | หายาก | a woven bamboo lamellar armor icon |
| `items/armor_epic1.png` | เกราะเหล็กกล้า | มหากาพย์ | a legendary polished steel plate armor glowing purple icon |
| `items/armor_epic2.png` | เสื้อคลุมรัตติกาล | มหากาพย์ | a legendary midnight cloak with stars and purple glow icon |
| `items/armor_epic3.png` | เกราะเกล็ดงู | มหากาพย์ | a legendary serpent scale armor with emerald glow icon |

## 6. เอฟเฟกต์ (64×64 px · โฟลเดอร์ `fx/`)

| ไฟล์ | prompt |
| --- | --- |
| `fx/arrow.png` | a single arrow pointing right, wooden shaft, red fletching |
| `fx/bolt.png` | a small glowing magic projectile orb |
| `fx/blast.png` | an orange fiery explosion burst seen from above |
| `fx/heal.png` | a soft green healing sparkle |
| `fx/hit.png` | a small white-yellow impact spark burst |
| `fx/volley.png` | a fan of glowing blue arrows spreading out to the right (skill effect) |
| `fx/levelup.png` | a golden ring of light rising upward with sparkles |
| `fx/recall.png` | a swirling blue teleport circle seen from above |
| `fx/sunburn.png` | a monster burning to ash in morning sunlight, orange embers and smoke |
| `fx/rubble.png` | a pile of broken wood and stone rubble from a destroyed building (ขนาด 128×128) |
| `fx/web.png` | a sticky white spider web projectile |
| `fx/fireball.png` | a small fireball projectile flying right |

## 7. ไอคอน UI (64×64 px · โฟลเดอร์ `ui/`)

ไอคอนปุ่มและ HUD รูปทรงชัด เส้นขอบเข้ม พื้นหลังโปร่งใส ไม่มีตัวหนังสือ ใช้ Master prompt แบบไอคอนเดียวกับไอเทม

| ไฟล์ | ใช้ที่ | prompt |
| --- | --- | --- |
| `ui/wood.png` | ทรัพยากรไม้ | a bundle of three cut logs |
| `ui/stone.png` | ทรัพยากรหิน | a small pile of grey stone blocks |
| `ui/hp.png` | หลอด HP | a red heart |
| `ui/mp.png` | หลอด MP | a blue mana droplet crystal |
| `ui/exp.png` | EXP / เลเวล | a golden star |
| `ui/skill_volley.png` | ปุ่มสกิลยิงกระจาย (Q) | three arrows fanning out, glowing blue |
| `ui/build.png` | ปุ่มสร้าง (B) | a hammer crossed with a wooden plank |
| `ui/repair.png` | ปุ่มซ่อม | a hammer and wrench with a green plus |
| `ui/bag.png` | ปุ่มกระเป๋า (I) | a leather backpack |
| `ui/home.png` | ปุ่มกลับฐาน (H) | a small tent with a blue swirl |
| `ui/map.png` | ปุ่มแผนที่ (M) | a rolled parchment map |
| `ui/menu.png` | ปุ่มเมนู (Esc) | a gear cog |
| `ui/bestiary.png` | สมุดมอนสเตอร์ | an old leather book with a monster claw mark |
| `ui/night.png` | ตัวบอกกลางคืน / เริ่มกลางคืนเลย | a crescent moon with a red eye glow |
| `ui/day.png` | ตัวบอกกลางวัน | a sun |
| `ui/warn.png` | เตือนทิศ Monster บุก | a red exclamation shield |
| `ui/worker.png` | จ้างคนงาน / โควตาคนงาน | a straw hat with an axe |
| `ui/army.png` | โควตาทหาร | a crossed sword and bow |
| `ui/mode_free.png` | โหมดยูนิต อิสระ | a compass with scattered footprints |
| `ui/mode_follow.png` | โหมดยูนิต ตาม Hero | footprints following a blue banner |
| `ui/mode_guard.png` | โหมดยูนิต เฝ้าค่าย | a blue shield in front of a palisade |
| `ui/res_heroweapon.png` | วิจัย อาวุธ Hero | a glowing bow with an upward arrow |
| `ui/res_unitweapon.png` | วิจัย อาวุธทหาร | a short sword with an upward arrow |
| `ui/res_unitarmor.png` | วิจัย เกราะทหาร | a round blue shield with an upward arrow |

## 8. Monster 100 ชนิด (โฟลเดอร์ `monsters/`)

ทุกตัวหันขวา ขนาดไฟล์ตามระดับ ตัวระดับสูงและบอสควรดูใหญ่และน่ากลัวกว่า

### ระดับต่ำ (40 ชนิด · ไฟล์ 128×128 px)

| # | ไฟล์ | ชื่อ | พฤติกรรม | prompt ตัวละคร (ต่อท้าย Master prompt) |
| --- | --- | --- | --- | --- |
| 1 | `monsters/zombie0.png` | ซอมบี้ | เดินเข้าตี | a shambling rotting zombie, hunched, arms stretched forward, torn rags |
| 2 | `monsters/zombie1.png` | ซอมบี้เน่า | เดินเข้าตี | a shambling rotting zombie, hunched, arms stretched forward, torn rags, rotting, mossy and decayed (yellow-brown tint) |
| 3 | `monsters/zombie2.png` | ซอมบี้พิษ | เดินเข้าตี | a shambling rotting zombie, hunched, arms stretched forward, torn rags, poisonous, dripping toxic green ooze |
| 4 | `monsters/zombie3.png` | ซอมบี้เพลิง | เดินเข้าตี | a shambling rotting zombie, hunched, arms stretched forward, torn rags, burning, flames and embers on its body (orange-red) |
| 5 | `monsters/zombie4.png` | ซอมบี้น้ำแข็ง | เดินเข้าตี | a shambling rotting zombie, hunched, arms stretched forward, torn rags, frozen, ice crystals and frost (pale blue) |
| 6 | `monsters/zombie5.png` | ซอมบี้เงา | เดินเข้าตี | a shambling rotting zombie, hunched, arms stretched forward, torn rags, shadowy, made of dark purple smoke |
| 7 | `monsters/zombie6.png` | ซอมบี้หิน | เดินเข้าตี | a shambling rotting zombie, hunched, arms stretched forward, torn rags, stone-skinned, rocky grey armor plates |
| 8 | `monsters/zombie7.png` | ซอมบี้คลั่ง | เดินเข้าตี | a shambling rotting zombie, hunched, arms stretched forward, torn rags, berserk, red glowing eyes, battle scars, furious |
| 9 | `monsters/wolf0.png` | หมาป่า | วิ่งเร็ว มาเป็นฝูง | a lean feral wolf in mid-run, bared fangs, bristling fur |
| 10 | `monsters/wolf1.png` | หมาป่าเน่า | วิ่งเร็ว มาเป็นฝูง | a lean feral wolf in mid-run, bared fangs, bristling fur, rotting, mossy and decayed (yellow-brown tint) |
| 11 | `monsters/wolf2.png` | หมาป่าพิษ | วิ่งเร็ว มาเป็นฝูง | a lean feral wolf in mid-run, bared fangs, bristling fur, poisonous, dripping toxic green ooze |
| 12 | `monsters/wolf3.png` | หมาป่าเพลิง | วิ่งเร็ว มาเป็นฝูง | a lean feral wolf in mid-run, bared fangs, bristling fur, burning, flames and embers on its body (orange-red) |
| 13 | `monsters/wolf4.png` | หมาป่าน้ำแข็ง | วิ่งเร็ว มาเป็นฝูง | a lean feral wolf in mid-run, bared fangs, bristling fur, frozen, ice crystals and frost (pale blue) |
| 14 | `monsters/wolf5.png` | หมาป่าเงา | วิ่งเร็ว มาเป็นฝูง | a lean feral wolf in mid-run, bared fangs, bristling fur, shadowy, made of dark purple smoke |
| 15 | `monsters/wolf6.png` | หมาป่าหิน | วิ่งเร็ว มาเป็นฝูง | a lean feral wolf in mid-run, bared fangs, bristling fur, stone-skinned, rocky grey armor plates |
| 16 | `monsters/wolf7.png` | หมาป่าคลั่ง | วิ่งเร็ว มาเป็นฝูง | a lean feral wolf in mid-run, bared fangs, bristling fur, berserk, red glowing eyes, battle scars, furious |
| 17 | `monsters/slime0.png` | สไลม์ | วิ่งชนแล้วระเบิด | a round gelatinous slime blob with glowing eyes and a bubbling core about to burst |
| 18 | `monsters/slime1.png` | สไลม์เน่า | วิ่งชนแล้วระเบิด | a round gelatinous slime blob with glowing eyes and a bubbling core about to burst, rotting, mossy and decayed (yellow-brown tint) |
| 19 | `monsters/slime2.png` | สไลม์พิษ | วิ่งชนแล้วระเบิด | a round gelatinous slime blob with glowing eyes and a bubbling core about to burst, poisonous, dripping toxic green ooze |
| 20 | `monsters/slime3.png` | สไลม์เพลิง | วิ่งชนแล้วระเบิด | a round gelatinous slime blob with glowing eyes and a bubbling core about to burst, burning, flames and embers on its body (orange-red) |
| 21 | `monsters/slime4.png` | สไลม์น้ำแข็ง | วิ่งชนแล้วระเบิด | a round gelatinous slime blob with glowing eyes and a bubbling core about to burst, frozen, ice crystals and frost (pale blue) |
| 22 | `monsters/slime5.png` | สไลม์เงา | วิ่งชนแล้วระเบิด | a round gelatinous slime blob with glowing eyes and a bubbling core about to burst, shadowy, made of dark purple smoke |
| 23 | `monsters/slime6.png` | สไลม์หิน | วิ่งชนแล้วระเบิด | a round gelatinous slime blob with glowing eyes and a bubbling core about to burst, stone-skinned, rocky grey armor plates |
| 24 | `monsters/slime7.png` | สไลม์คลั่ง | วิ่งชนแล้วระเบิด | a round gelatinous slime blob with glowing eyes and a bubbling core about to burst, berserk, red glowing eyes, battle scars, furious |
| 25 | `monsters/bat0.png` | ค้างคาว | บินข้ามกำแพง | a giant bat with leathery wings fully spread, glowing eyes |
| 26 | `monsters/bat1.png` | ค้างคาวเน่า | บินข้ามกำแพง | a giant bat with leathery wings fully spread, glowing eyes, rotting, mossy and decayed (yellow-brown tint) |
| 27 | `monsters/bat2.png` | ค้างคาวพิษ | บินข้ามกำแพง | a giant bat with leathery wings fully spread, glowing eyes, poisonous, dripping toxic green ooze |
| 28 | `monsters/bat3.png` | ค้างคาวเพลิง | บินข้ามกำแพง | a giant bat with leathery wings fully spread, glowing eyes, burning, flames and embers on its body (orange-red) |
| 29 | `monsters/bat4.png` | ค้างคาวน้ำแข็ง | บินข้ามกำแพง | a giant bat with leathery wings fully spread, glowing eyes, frozen, ice crystals and frost (pale blue) |
| 30 | `monsters/bat5.png` | ค้างคาวเงา | บินข้ามกำแพง | a giant bat with leathery wings fully spread, glowing eyes, shadowy, made of dark purple smoke |
| 31 | `monsters/bat6.png` | ค้างคาวหิน | บินข้ามกำแพง | a giant bat with leathery wings fully spread, glowing eyes, stone-skinned, rocky grey armor plates |
| 32 | `monsters/bat7.png` | ค้างคาวคลั่ง | บินข้ามกำแพง | a giant bat with leathery wings fully spread, glowing eyes, berserk, red glowing eyes, battle scars, furious |
| 33 | `monsters/skel0.png` | โครงกระดูกนักธนู | ยิงไกล ยิงป้อมได้ | a skeleton archer holding a crude bow, cracked skull, bony ribcage |
| 34 | `monsters/skel1.png` | โครงกระดูกนักธนูเน่า | ยิงไกล ยิงป้อมได้ | a skeleton archer holding a crude bow, cracked skull, bony ribcage, rotting, mossy and decayed (yellow-brown tint) |
| 35 | `monsters/skel2.png` | โครงกระดูกนักธนูพิษ | ยิงไกล ยิงป้อมได้ | a skeleton archer holding a crude bow, cracked skull, bony ribcage, poisonous, dripping toxic green ooze |
| 36 | `monsters/skel3.png` | โครงกระดูกนักธนูเพลิง | ยิงไกล ยิงป้อมได้ | a skeleton archer holding a crude bow, cracked skull, bony ribcage, burning, flames and embers on its body (orange-red) |
| 37 | `monsters/skel4.png` | โครงกระดูกนักธนูน้ำแข็ง | ยิงไกล ยิงป้อมได้ | a skeleton archer holding a crude bow, cracked skull, bony ribcage, frozen, ice crystals and frost (pale blue) |
| 38 | `monsters/skel5.png` | โครงกระดูกนักธนูเงา | ยิงไกล ยิงป้อมได้ | a skeleton archer holding a crude bow, cracked skull, bony ribcage, shadowy, made of dark purple smoke |
| 39 | `monsters/skel6.png` | โครงกระดูกนักธนูหิน | ยิงไกล ยิงป้อมได้ | a skeleton archer holding a crude bow, cracked skull, bony ribcage, stone-skinned, rocky grey armor plates |
| 40 | `monsters/skel7.png` | โครงกระดูกนักธนูคลั่ง | ยิงไกล ยิงป้อมได้ | a skeleton archer holding a crude bow, cracked skull, bony ribcage, berserk, red glowing eyes, battle scars, furious |

### ระดับกลาง (30 ชนิด · ไฟล์ 160×160 px)

| # | ไฟล์ | ชื่อ | พฤติกรรม | prompt ตัวละคร (ต่อท้าย Master prompt) |
| --- | --- | --- | --- | --- |
| 41 | `monsters/ghoul0.png` | กูล | เดินเข้าตี | a gaunt pale ghoul with long claws and sunken eyes, crouched |
| 42 | `monsters/ghoul1.png` | กูลเน่า | เดินเข้าตี | a gaunt pale ghoul with long claws and sunken eyes, crouched, rotting, mossy and decayed (yellow-brown tint) |
| 43 | `monsters/ghoul2.png` | กูลพิษ | เดินเข้าตี | a gaunt pale ghoul with long claws and sunken eyes, crouched, poisonous, dripping toxic green ooze |
| 44 | `monsters/ghoul3.png` | กูลเพลิง | เดินเข้าตี | a gaunt pale ghoul with long claws and sunken eyes, crouched, burning, flames and embers on its body (orange-red) |
| 45 | `monsters/ghoul4.png` | กูลน้ำแข็ง | เดินเข้าตี | a gaunt pale ghoul with long claws and sunken eyes, crouched, frozen, ice crystals and frost (pale blue) |
| 46 | `monsters/spider0.png` | แมงมุมยักษ์ | วิ่งเร็ว มาเป็นฝูง | a giant hairy spider with eight long legs and a bulbous abdomen |
| 47 | `monsters/spider1.png` | แมงมุมยักษ์เน่า | วิ่งเร็ว มาเป็นฝูง | a giant hairy spider with eight long legs and a bulbous abdomen, rotting, mossy and decayed (yellow-brown tint) |
| 48 | `monsters/spider2.png` | แมงมุมยักษ์พิษ | วิ่งเร็ว มาเป็นฝูง | a giant hairy spider with eight long legs and a bulbous abdomen, poisonous, dripping toxic green ooze |
| 49 | `monsters/spider3.png` | แมงมุมยักษ์เพลิง | วิ่งเร็ว มาเป็นฝูง | a giant hairy spider with eight long legs and a bulbous abdomen, burning, flames and embers on its body (orange-red) |
| 50 | `monsters/spider4.png` | แมงมุมยักษ์น้ำแข็ง | วิ่งเร็ว มาเป็นฝูง | a giant hairy spider with eight long legs and a bulbous abdomen, frozen, ice crystals and frost (pale blue) |
| 51 | `monsters/orc0.png` | ออร์ก | ถึก ทุบกำแพงแรง | a hulking orc brute with tusks, crude armor and a heavy spiked club |
| 52 | `monsters/orc1.png` | ออร์กเน่า | ถึก ทุบกำแพงแรง | a hulking orc brute with tusks, crude armor and a heavy spiked club, rotting, mossy and decayed (yellow-brown tint) |
| 53 | `monsters/orc2.png` | ออร์กพิษ | ถึก ทุบกำแพงแรง | a hulking orc brute with tusks, crude armor and a heavy spiked club, poisonous, dripping toxic green ooze |
| 54 | `monsters/orc3.png` | ออร์กเพลิง | ถึก ทุบกำแพงแรง | a hulking orc brute with tusks, crude armor and a heavy spiked club, burning, flames and embers on its body (orange-red) |
| 55 | `monsters/orc4.png` | ออร์กน้ำแข็ง | ถึก ทุบกำแพงแรง | a hulking orc brute with tusks, crude armor and a heavy spiked club, frozen, ice crystals and frost (pale blue) |
| 56 | `monsters/wisp0.png` | ภูตไฟ | บินข้ามกำแพง | a floating fire wisp, a ball of living flame with a bright core |
| 57 | `monsters/wisp1.png` | ภูตไฟเน่า | บินข้ามกำแพง | a floating fire wisp, a ball of living flame with a bright core, rotting, mossy and decayed (yellow-brown tint) |
| 58 | `monsters/wisp2.png` | ภูตไฟพิษ | บินข้ามกำแพง | a floating fire wisp, a ball of living flame with a bright core, poisonous, dripping toxic green ooze |
| 59 | `monsters/wisp3.png` | ภูตไฟเพลิง | บินข้ามกำแพง | a floating fire wisp, a ball of living flame with a bright core, burning, flames and embers on its body (orange-red) |
| 60 | `monsters/wisp4.png` | ภูตไฟน้ำแข็ง | บินข้ามกำแพง | a floating fire wisp, a ball of living flame with a bright core, frozen, ice crystals and frost (pale blue) |
| 61 | `monsters/bonemage0.png` | นักเวทกระดูก | ยิงไกล ยิงป้อมได้ | a skeleton mage in a tattered robe holding a bone staff with a glowing orb |
| 62 | `monsters/bonemage1.png` | นักเวทกระดูกเน่า | ยิงไกล ยิงป้อมได้ | a skeleton mage in a tattered robe holding a bone staff with a glowing orb, rotting, mossy and decayed (yellow-brown tint) |
| 63 | `monsters/bonemage2.png` | นักเวทกระดูกพิษ | ยิงไกล ยิงป้อมได้ | a skeleton mage in a tattered robe holding a bone staff with a glowing orb, poisonous, dripping toxic green ooze |
| 64 | `monsters/bonemage3.png` | นักเวทกระดูกเพลิง | ยิงไกล ยิงป้อมได้ | a skeleton mage in a tattered robe holding a bone staff with a glowing orb, burning, flames and embers on its body (orange-red) |
| 65 | `monsters/bonemage4.png` | นักเวทกระดูกน้ำแข็ง | ยิงไกล ยิงป้อมได้ | a skeleton mage in a tattered robe holding a bone staff with a glowing orb, frozen, ice crystals and frost (pale blue) |
| 66 | `monsters/beetle0.png` | ด้วงระเบิด | วิ่งชนแล้วระเบิด | a large armored bomb beetle with a glowing fuse-like horn |
| 67 | `monsters/beetle1.png` | ด้วงระเบิดเน่า | วิ่งชนแล้วระเบิด | a large armored bomb beetle with a glowing fuse-like horn, rotting, mossy and decayed (yellow-brown tint) |
| 68 | `monsters/beetle2.png` | ด้วงระเบิดพิษ | วิ่งชนแล้วระเบิด | a large armored bomb beetle with a glowing fuse-like horn, poisonous, dripping toxic green ooze |
| 69 | `monsters/beetle3.png` | ด้วงระเบิดเพลิง | วิ่งชนแล้วระเบิด | a large armored bomb beetle with a glowing fuse-like horn, burning, flames and embers on its body (orange-red) |
| 70 | `monsters/beetle4.png` | ด้วงระเบิดน้ำแข็ง | วิ่งชนแล้วระเบิด | a large armored bomb beetle with a glowing fuse-like horn, frozen, ice crystals and frost (pale blue) |

### ระดับสูง (25 ชนิด · ไฟล์ 192×192 px)

| # | ไฟล์ | ชื่อ | พฤติกรรม | prompt ตัวละคร (ต่อท้าย Master prompt) |
| --- | --- | --- | --- | --- |
| 71 | `monsters/knight0.png` | อัศวินมรณะ | เดินเข้าตี | an undead death knight in dark plate armor with a greatsword and shield, glowing visor |
| 72 | `monsters/knight1.png` | อัศวินมรณะเน่า | เดินเข้าตี | an undead death knight in dark plate armor with a greatsword and shield, glowing visor, rotting, mossy and decayed (yellow-brown tint) |
| 73 | `monsters/knight2.png` | อัศวินมรณะพิษ | เดินเข้าตี | an undead death knight in dark plate armor with a greatsword and shield, glowing visor, poisonous, dripping toxic green ooze |
| 74 | `monsters/knight3.png` | อัศวินมรณะเพลิง | เดินเข้าตี | an undead death knight in dark plate armor with a greatsword and shield, glowing visor, burning, flames and embers on its body (orange-red) |
| 75 | `monsters/knight4.png` | อัศวินมรณะน้ำแข็ง | เดินเข้าตี | an undead death knight in dark plate armor with a greatsword and shield, glowing visor, frozen, ice crystals and frost (pale blue) |
| 76 | `monsters/were0.png` | มนุษย์หมาป่า | วิ่งเร็ว มาเป็นฝูง | a muscular werewolf, half man half wolf, running on all fours |
| 77 | `monsters/were1.png` | มนุษย์หมาป่าเน่า | วิ่งเร็ว มาเป็นฝูง | a muscular werewolf, half man half wolf, running on all fours, rotting, mossy and decayed (yellow-brown tint) |
| 78 | `monsters/were2.png` | มนุษย์หมาป่าพิษ | วิ่งเร็ว มาเป็นฝูง | a muscular werewolf, half man half wolf, running on all fours, poisonous, dripping toxic green ooze |
| 79 | `monsters/were3.png` | มนุษย์หมาป่าเพลิง | วิ่งเร็ว มาเป็นฝูง | a muscular werewolf, half man half wolf, running on all fours, burning, flames and embers on its body (orange-red) |
| 80 | `monsters/were4.png` | มนุษย์หมาป่าน้ำแข็ง | วิ่งเร็ว มาเป็นฝูง | a muscular werewolf, half man half wolf, running on all fours, frozen, ice crystals and frost (pale blue) |
| 81 | `monsters/golem0.png` | โกเลมหิน | ถึก ทุบกำแพงแรง | a massive stone golem made of stacked boulders with glowing cracks, stone-skinned, rocky grey armor plates |
| 82 | `monsters/golem1.png` | โกเลมหินเน่า | ถึก ทุบกำแพงแรง | a massive stone golem made of stacked boulders with glowing cracks, rotting, mossy and decayed (yellow-brown tint) |
| 83 | `monsters/golem2.png` | โกเลมหินพิษ | ถึก ทุบกำแพงแรง | a massive stone golem made of stacked boulders with glowing cracks, poisonous, dripping toxic green ooze |
| 84 | `monsters/golem3.png` | โกเลมหินเพลิง | ถึก ทุบกำแพงแรง | a massive stone golem made of stacked boulders with glowing cracks, burning, flames and embers on its body (orange-red) |
| 85 | `monsters/golem4.png` | โกเลมหินน้ำแข็ง | ถึก ทุบกำแพงแรง | a massive stone golem made of stacked boulders with glowing cracks, frozen, ice crystals and frost (pale blue) |
| 86 | `monsters/demon0.png` | ปีศาจปีก | บินข้ามกำแพง | a winged demon with horns, bat-like wings and red skin |
| 87 | `monsters/demon1.png` | ปีศาจปีกเน่า | บินข้ามกำแพง | a winged demon with horns, bat-like wings and red skin, rotting, mossy and decayed (yellow-brown tint) |
| 88 | `monsters/demon2.png` | ปีศาจปีกพิษ | บินข้ามกำแพง | a winged demon with horns, bat-like wings and red skin, poisonous, dripping toxic green ooze |
| 89 | `monsters/demon3.png` | ปีศาจปีกเพลิง | บินข้ามกำแพง | a winged demon with horns, bat-like wings and red skin, burning, flames and embers on its body (orange-red) |
| 90 | `monsters/demon4.png` | ปีศาจปีกน้ำแข็ง | บินข้ามกำแพง | a winged demon with horns, bat-like wings and red skin, frozen, ice crystals and frost (pale blue) |
| 91 | `monsters/lich0.png` | ลิชมรณะ | ยิงไกล ยิงป้อมได้ | a hooded lich sorcerer with a skull face and a staff topped with a glowing crystal |
| 92 | `monsters/lich1.png` | ลิชมรณะเน่า | ยิงไกล ยิงป้อมได้ | a hooded lich sorcerer with a skull face and a staff topped with a glowing crystal, rotting, mossy and decayed (yellow-brown tint) |
| 93 | `monsters/lich2.png` | ลิชมรณะพิษ | ยิงไกล ยิงป้อมได้ | a hooded lich sorcerer with a skull face and a staff topped with a glowing crystal, poisonous, dripping toxic green ooze |
| 94 | `monsters/lich3.png` | ลิชมรณะเพลิง | ยิงไกล ยิงป้อมได้ | a hooded lich sorcerer with a skull face and a staff topped with a glowing crystal, burning, flames and embers on its body (orange-red) |
| 95 | `monsters/lich4.png` | ลิชมรณะน้ำแข็ง | ยิงไกล ยิงป้อมได้ | a hooded lich sorcerer with a skull face and a staff topped with a glowing crystal, frozen, ice crystals and frost (pale blue) |

### ระดับบอส (5 ชนิด · ไฟล์ 256×256 px)

| # | ไฟล์ | ชื่อ | พฤติกรรม | prompt ตัวละคร (ต่อท้าย Master prompt) |
| --- | --- | --- | --- | --- |
| 96 | `monsters/boss0.png` | ราชาซอมบี้ | เดินเข้าตี | the Zombie King, a giant zombie wearing a rusted golden crown and royal rags, much larger and menacing |
| 97 | `monsters/boss1.png` | จ้าวฝูงหมาป่า | วิ่งเร็ว มาเป็นฝูง | the Alpha Wolf Lord, a huge black dire wolf with a golden crown-like mane and scars |
| 98 | `monsters/boss2.png` | ราชินีแมงมุม | ยิงไกล ยิงป้อมได้ | the Spider Queen, an enormous spider with a crown of horns, egg sacs on its back, spitting web |
| 99 | `monsters/boss3.png` | โกเลมโบราณ | ถึก ทุบกำแพงแรง | the Ancient Golem, a towering golem of ancient carved stone with golden runes and a crown of crystals |
| 100 | `monsters/boss4.png` | มังกรเงา | บินข้ามกำแพง | the Shadow Dragon, a dark dragon with huge wings, smoky shadow body and glowing eyes |

---

## ส่งภาพกลับมา

1. วางไฟล์ในโฟลเดอร์ `assets/` ของ repo ตามชื่อด้านบน (เช่น `assets/monsters/zombie0.png`) อัปโหลดผ่านหน้าเว็บ GitHub ได้
2. ไม่ต้องครบทุกไฟล์ ภาพไหนยังไม่มี เกมจะใช้ภาพที่วาดด้วยโค้ดแทนไปก่อน
3. บอก Claude ว่า "ใส่ภาพเข้าเกม" แล้วจะเชื่อมให้ พร้อมย่อขนาดไฟล์ให้โหลดเร็วบนมือถือ
