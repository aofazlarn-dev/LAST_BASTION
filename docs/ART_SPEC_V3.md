# LAST BASTION · Art Spec v3 · ท่าทาง (Animation)

ต่อยอดจาก **Art Spec v2**: ทุกท่าในเอกสารนี้ต้อง **แนบภาพนิ่งของตัวนั้นจากชุด v2** ไปให้ GPT ทุกครั้ง GPT จะได้วาดตัวเดิมเป๊ะ แค่เปลี่ยนท่า

เกมรองรับทั้งสองแบบ: ตัวที่มีไฟล์ท่าทางจะเล่นเฟรมจริง ตัวที่ยังไม่มีจะขยับด้วยโค้ดแบบตอนนี้ต่อไป ทำทีละตัวได้

---

## 1. กติกา (ทุกภาพ)

| เรื่อง | ข้อกำหนด |
| --- | --- |
| ภาพอ้างอิง | แนบภาพนิ่งจาก v2 ของตัวนั้นทุกครั้ง (เช่น `hero_archer` จาก Sheet 01) |
| ขนาดภาพ | **1536×1024** (แนวนอน) |
| 1 ภาพ = 1 ท่า | ตาราง 2 × 2 (4 เฟรม) หรือ 3 × 2 (6 เฟรม) ช่องเท่ากันทุกช่อง เรียงซ้าย→ขวา บน→ล่าง |
| ทุกเฟรม | หันขวา ขนาดตัวเท่ากัน **เท้าอยู่ระดับเดียวกัน** อยู่กลางช่อง เว้นขอบ 10% ไม่ล้นช่อง |
| พื้นหลัง | โปร่งใส ไม่มีพื้น ไม่มีเงา ไม่มีตัวหนังสือ |
| ท่าวนลูป | เฟรมสุดท้ายต้องต่อกลับเฟรมแรกได้เนียน (idle, walk, fly, chop, heal) |
| ชื่อไฟล์ | `anim/<ไฟล์ v2>_<ท่า>.png` เช่น `anim/hero_archer_walk.png` |
| ตัวต่างธาตุ | **ไม่ต้องวาดท่าใหม่** เช่น ซอมบี้เพลิง/น้ำแข็ง ใช้ท่าของ `zombie0` แล้วเกมเปลี่ยนสีให้ |

### Prompt หลัก (ใช้ทุกท่า แทน `{N}` `{ACT}` `{GRID}` ตามตาราง แล้วต่อด้วยรายการเฟรม)

```
Use the attached image as the exact character reference (from Art Spec v2).
Same design, same outfit, same colors, same proportions, same art style, same lighting
(sunny, from the top-left), same 3/4 top-down camera at about 50 degrees. Do not redesign anything.
Create a {N}-frame {ACT} animation sprite sheet.
Grid: {GRID}, all cells exactly the same size, read left to right, top to bottom.
Every frame: full body, facing right, same scale in every frame, feet (or lowest point) on the same
baseline near the bottom of the cell, centered, at least 10% empty margin, nothing crossing cell borders.
Transparent background, no ground, no cast shadow, no text.
```

### เช็กก่อนส่ง

- หน้าตา เสื้อผ้า สี ตรงกับภาพ v2 ทุกเฟรม
- ขนาดตัวและระดับเท้าเท่ากันทุกช่อง (วางเรียงกันดูแล้วไม่กระตุกขึ้นลง)
- เฟรมไหนเพี้ยน สั่งแก้เฉพาะเฟรมนั้น: `Redraw only frame 4, keep all other frames exactly the same.`
- ถ้า GPT ทำให้เหมือนกันทุกเฟรมไม่ได้จริง ๆ ใช้เครื่องมือทำอนิเมชันจากภาพเดียว เช่น PixelLab แทน (ใช้ชื่อไฟล์และตารางเดียวกัน)

---

## 2. ตัวละครฝ่ายเรา

### Hero Archer (เล่นได้ตอนนี้) · `hero_archer` · ลำดับ A · ทำก่อน

| ท่า | ไฟล์ | เฟรม | ตาราง | ความเร็ว |
| --- | --- | --- | --- | --- |
| idle | `anim/hero_archer_idle.png` | 4 | 2 × 2 | 6 fps |
| walk | `anim/hero_archer_walk.png` | 6 | 3 × 2 | 10 fps |
| attack | `anim/hero_archer_attack.png` | 6 | 3 × 2 | 12 fps |
| hurt | `anim/hero_archer_hurt.png` | 4 | 2 × 2 | 12 fps |
| death | `anim/hero_archer_death.png` | 4 | 2 × 2 | 10 fps |
| skill | `anim/hero_archer_skill.png` | 6 | 3 × 2 | 14 fps |

<details><summary>prompt · hero_archer_idle</summary>

```
Use the attached image as the exact character reference (from Art Spec v2).
Same design, same outfit, same colors, same proportions, same art style, same lighting
(sunny, from the top-left), same 3/4 top-down camera at about 50 degrees. Do not redesign anything.
Create a 4-frame IDLE (breathing loop) animation sprite sheet.
Grid: 2 columns x 2 rows, all cells exactly the same size, read left to right, top to bottom.
Every frame: full body, facing right, same scale in every frame, feet (or lowest point) on the same
baseline near the bottom of the cell, centered, at least 10% empty margin, nothing crossing cell borders.
Transparent background, no ground, no cast shadow, no text.

Frame 1: neutral stance, weight centered
Frame 2: chest rises slightly, shoulders up a little
Frame 3: top of the breath, tiny lift
Frame 4: chest falls back, slightly lower than frame 1
```
</details>

<details><summary>prompt · hero_archer_walk</summary>

```
Use the attached image as the exact character reference (from Art Spec v2).
Same design, same outfit, same colors, same proportions, same art style, same lighting
(sunny, from the top-left), same 3/4 top-down camera at about 50 degrees. Do not redesign anything.
Create a 6-frame WALK CYCLE (loop) animation sprite sheet.
Grid: 3 columns x 2 rows, all cells exactly the same size, read left to right, top to bottom.
Every frame: full body, facing right, same scale in every frame, feet (or lowest point) on the same
baseline near the bottom of the cell, centered, at least 10% empty margin, nothing crossing cell borders.
Transparent background, no ground, no cast shadow, no text.

Frame 1: contact – right foot forward touching the ground, left foot back, arms swinging opposite
Frame 2: down – weight on the right foot, body slightly lower, knees bent
Frame 3: passing – left leg passing the right leg, body at normal height
Frame 4: contact – left foot forward touching the ground, right foot back
Frame 5: down – weight on the left foot, body slightly lower
Frame 6: passing – right leg passing the left leg, body at normal height
```
</details>

<details><summary>prompt · hero_archer_attack</summary>

```
Use the attached image as the exact character reference (from Art Spec v2).
Same design, same outfit, same colors, same proportions, same art style, same lighting
(sunny, from the top-left), same 3/4 top-down camera at about 50 degrees. Do not redesign anything.
Create a 6-frame ATTACK – shoot a bow animation sprite sheet.
Grid: 3 columns x 2 rows, all cells exactly the same size, read left to right, top to bottom.
Every frame: full body, facing right, same scale in every frame, feet (or lowest point) on the same
baseline near the bottom of the cell, centered, at least 10% empty margin, nothing crossing cell borders.
Transparent background, no ground, no cast shadow, no text.

Frame 1: ready – standing, bow lowered, reaching for an arrow
Frame 2: nock – arrow placed on the string, bow rising
Frame 3: draw – bow raised forward, string pulled halfway
Frame 4: full draw – string pulled to the cheek, body leaning slightly back
Frame 5: release – arrow just left the bow, string snapping forward, small motion lines
Frame 6: recover – bow lowering back to the ready pose
```
</details>

<details><summary>prompt · hero_archer_hurt</summary>

```
Use the attached image as the exact character reference (from Art Spec v2).
Same design, same outfit, same colors, same proportions, same art style, same lighting
(sunny, from the top-left), same 3/4 top-down camera at about 50 degrees. Do not redesign anything.
Create a 4-frame HURT (short flinch) animation sprite sheet.
Grid: 2 columns x 2 rows, all cells exactly the same size, read left to right, top to bottom.
Every frame: full body, facing right, same scale in every frame, feet (or lowest point) on the same
baseline near the bottom of the cell, centered, at least 10% empty margin, nothing crossing cell borders.
Transparent background, no ground, no cast shadow, no text.

Frame 1: impact – body jolts back, eyes squeezed shut
Frame 2: leaning back the most, arms pulled in
Frame 3: recovering, leaning slightly back
Frame 4: back to neutral stance
```
</details>

<details><summary>prompt · hero_archer_death</summary>

```
Use the attached image as the exact character reference (from Art Spec v2).
Same design, same outfit, same colors, same proportions, same art style, same lighting
(sunny, from the top-left), same 3/4 top-down camera at about 50 degrees. Do not redesign anything.
Create a 4-frame DEATH animation sprite sheet.
Grid: 2 columns x 2 rows, all cells exactly the same size, read left to right, top to bottom.
Every frame: full body, facing right, same scale in every frame, feet (or lowest point) on the same
baseline near the bottom of the cell, centered, at least 10% empty margin, nothing crossing cell borders.
Transparent background, no ground, no cast shadow, no text.

Frame 1: hit – head snaps back, arms flung out
Frame 2: staggering backward, knees buckling
Frame 3: falling backward at about 45 degrees
Frame 4: lying on the back on the ground, limp, eyes closed
```
</details>

<details><summary>prompt · hero_archer_skill</summary>

```
Use the attached image as the exact character reference (from Art Spec v2).
Same design, same outfit, same colors, same proportions, same art style, same lighting
(sunny, from the top-left), same 3/4 top-down camera at about 50 degrees. Do not redesign anything.
Create a 6-frame SKILL – multi-shot volley animation sprite sheet.
Grid: 3 columns x 2 rows, all cells exactly the same size, read left to right, top to bottom.
Every frame: full body, facing right, same scale in every frame, feet (or lowest point) on the same
baseline near the bottom of the cell, centered, at least 10% empty margin, nothing crossing cell borders.
Transparent background, no ground, no cast shadow, no text.

Frame 1: crouch, three arrows on the string at once
Frame 2: bow raised high, glowing blue light on the arrows
Frame 3: full draw, body twisted, strong glow
Frame 4: release – three arrows fanning out to the right, bright flash
Frame 5: bow arm extended, arrows trailing light
Frame 6: recover to standing
```
</details>

### คนงาน · `worker` · ลำดับ A · ทำก่อน

| ท่า | ไฟล์ | เฟรม | ตาราง | ความเร็ว |
| --- | --- | --- | --- | --- |
| idle | `anim/worker_idle.png` | 4 | 2 × 2 | 6 fps |
| walk | `anim/worker_walk.png` | 6 | 3 × 2 | 10 fps |
| walk_wood | `anim/worker_walk_wood.png` | 6 | 3 × 2 | 10 fps |
| walk_stone | `anim/worker_walk_stone.png` | 6 | 3 × 2 | 10 fps |
| chop | `anim/worker_chop.png` | 6 | 3 × 2 | 12 fps |
| mine | `anim/worker_mine.png` | 6 | 3 × 2 | 12 fps |
| death | `anim/worker_death.png` | 4 | 2 × 2 | 10 fps |

<details><summary>prompt · worker_idle</summary>

```
Use the attached image as the exact character reference (from Art Spec v2).
Same design, same outfit, same colors, same proportions, same art style, same lighting
(sunny, from the top-left), same 3/4 top-down camera at about 50 degrees. Do not redesign anything.
Create a 4-frame IDLE (breathing loop) animation sprite sheet.
Grid: 2 columns x 2 rows, all cells exactly the same size, read left to right, top to bottom.
Every frame: full body, facing right, same scale in every frame, feet (or lowest point) on the same
baseline near the bottom of the cell, centered, at least 10% empty margin, nothing crossing cell borders.
Transparent background, no ground, no cast shadow, no text.

Frame 1: neutral stance, weight centered
Frame 2: chest rises slightly, shoulders up a little
Frame 3: top of the breath, tiny lift
Frame 4: chest falls back, slightly lower than frame 1
```
</details>

<details><summary>prompt · worker_walk</summary>

```
Use the attached image as the exact character reference (from Art Spec v2).
Same design, same outfit, same colors, same proportions, same art style, same lighting
(sunny, from the top-left), same 3/4 top-down camera at about 50 degrees. Do not redesign anything.
Create a 6-frame WALK CYCLE (loop) animation sprite sheet.
Grid: 3 columns x 2 rows, all cells exactly the same size, read left to right, top to bottom.
Every frame: full body, facing right, same scale in every frame, feet (or lowest point) on the same
baseline near the bottom of the cell, centered, at least 10% empty margin, nothing crossing cell borders.
Transparent background, no ground, no cast shadow, no text.

Frame 1: contact – right foot forward touching the ground, left foot back, arms swinging opposite
Frame 2: down – weight on the right foot, body slightly lower, knees bent
Frame 3: passing – left leg passing the right leg, body at normal height
Frame 4: contact – left foot forward touching the ground, right foot back
Frame 5: down – weight on the left foot, body slightly lower
Frame 6: passing – right leg passing the left leg, body at normal height
```
</details>

<details><summary>prompt · worker_walk_wood</summary>

```
Use the attached image as the exact character reference (from Art Spec v2).
Same design, same outfit, same colors, same proportions, same art style, same lighting
(sunny, from the top-left), same 3/4 top-down camera at about 50 degrees. Do not redesign anything.
Create a 6-frame WALK CYCLE carrying logs (loop) animation sprite sheet.
Grid: 3 columns x 2 rows, all cells exactly the same size, read left to right, top to bottom.
Every frame: full body, facing right, same scale in every frame, feet (or lowest point) on the same
baseline near the bottom of the cell, centered, at least 10% empty margin, nothing crossing cell borders.
Transparent background, no ground, no cast shadow, no text.
Creature note: same as a normal walk cycle but carrying a bundle of logs on the back, body bent slightly forward

Frame 1: contact – right foot forward touching the ground, left foot back, arms swinging opposite
Frame 2: down – weight on the right foot, body slightly lower, knees bent
Frame 3: passing – left leg passing the right leg, body at normal height
Frame 4: contact – left foot forward touching the ground, right foot back
Frame 5: down – weight on the left foot, body slightly lower
Frame 6: passing – right leg passing the left leg, body at normal height
```
</details>

<details><summary>prompt · worker_walk_stone</summary>

```
Use the attached image as the exact character reference (from Art Spec v2).
Same design, same outfit, same colors, same proportions, same art style, same lighting
(sunny, from the top-left), same 3/4 top-down camera at about 50 degrees. Do not redesign anything.
Create a 6-frame WALK CYCLE carrying a stone sack (loop) animation sprite sheet.
Grid: 3 columns x 2 rows, all cells exactly the same size, read left to right, top to bottom.
Every frame: full body, facing right, same scale in every frame, feet (or lowest point) on the same
baseline near the bottom of the cell, centered, at least 10% empty margin, nothing crossing cell borders.
Transparent background, no ground, no cast shadow, no text.
Creature note: same as a normal walk cycle but carrying a heavy sack of stones, body bent forward, slower steps

Frame 1: contact – right foot forward touching the ground, left foot back, arms swinging opposite
Frame 2: down – weight on the right foot, body slightly lower, knees bent
Frame 3: passing – left leg passing the right leg, body at normal height
Frame 4: contact – left foot forward touching the ground, right foot back
Frame 5: down – weight on the left foot, body slightly lower
Frame 6: passing – right leg passing the left leg, body at normal height
```
</details>

<details><summary>prompt · worker_chop</summary>

```
Use the attached image as the exact character reference (from Art Spec v2).
Same design, same outfit, same colors, same proportions, same art style, same lighting
(sunny, from the top-left), same 3/4 top-down camera at about 50 degrees. Do not redesign anything.
Create a 6-frame CHOP – cut a tree with an axe (loop) animation sprite sheet.
Grid: 3 columns x 2 rows, all cells exactly the same size, read left to right, top to bottom.
Every frame: full body, facing right, same scale in every frame, feet (or lowest point) on the same
baseline near the bottom of the cell, centered, at least 10% empty margin, nothing crossing cell borders.
Transparent background, no ground, no cast shadow, no text.

Frame 1: axe held at the waist
Frame 2: axe raised over the right shoulder
Frame 3: axe high above the head, body leaning back
Frame 4: swing down, axe at chest height, motion blur
Frame 5: impact – axe low in front, small wood chips flying
Frame 6: pull back to the waist position
```
</details>

<details><summary>prompt · worker_mine</summary>

```
Use the attached image as the exact character reference (from Art Spec v2).
Same design, same outfit, same colors, same proportions, same art style, same lighting
(sunny, from the top-left), same 3/4 top-down camera at about 50 degrees. Do not redesign anything.
Create a 6-frame MINE – break a rock with a pickaxe (loop) animation sprite sheet.
Grid: 3 columns x 2 rows, all cells exactly the same size, read left to right, top to bottom.
Every frame: full body, facing right, same scale in every frame, feet (or lowest point) on the same
baseline near the bottom of the cell, centered, at least 10% empty margin, nothing crossing cell borders.
Transparent background, no ground, no cast shadow, no text.

Frame 1: pickaxe held at the waist
Frame 2: pickaxe raised over the shoulder
Frame 3: pickaxe high, body leaning back
Frame 4: swing down hard, motion blur
Frame 5: impact – pickaxe hitting low in front, small stone chips flying
Frame 6: pull back to the waist position
```
</details>

<details><summary>prompt · worker_death</summary>

```
Use the attached image as the exact character reference (from Art Spec v2).
Same design, same outfit, same colors, same proportions, same art style, same lighting
(sunny, from the top-left), same 3/4 top-down camera at about 50 degrees. Do not redesign anything.
Create a 4-frame DEATH animation sprite sheet.
Grid: 2 columns x 2 rows, all cells exactly the same size, read left to right, top to bottom.
Every frame: full body, facing right, same scale in every frame, feet (or lowest point) on the same
baseline near the bottom of the cell, centered, at least 10% empty margin, nothing crossing cell borders.
Transparent background, no ground, no cast shadow, no text.

Frame 1: hit – head snaps back, arms flung out
Frame 2: staggering backward, knees buckling
Frame 3: falling backward at about 45 degrees
Frame 4: lying on the back on the ground, limp, eyes closed
```
</details>

### พลธนู · `u_archer` · ลำดับ B

| ท่า | ไฟล์ | เฟรม | ตาราง | ความเร็ว |
| --- | --- | --- | --- | --- |
| idle | `anim/u_archer_idle.png` | 4 | 2 × 2 | 6 fps |
| walk | `anim/u_archer_walk.png` | 6 | 3 × 2 | 10 fps |
| attack | `anim/u_archer_attack.png` | 6 | 3 × 2 | 12 fps |
| death | `anim/u_archer_death.png` | 4 | 2 × 2 | 10 fps |

<details><summary>prompt · u_archer_idle</summary>

```
Use the attached image as the exact character reference (from Art Spec v2).
Same design, same outfit, same colors, same proportions, same art style, same lighting
(sunny, from the top-left), same 3/4 top-down camera at about 50 degrees. Do not redesign anything.
Create a 4-frame IDLE (breathing loop) animation sprite sheet.
Grid: 2 columns x 2 rows, all cells exactly the same size, read left to right, top to bottom.
Every frame: full body, facing right, same scale in every frame, feet (or lowest point) on the same
baseline near the bottom of the cell, centered, at least 10% empty margin, nothing crossing cell borders.
Transparent background, no ground, no cast shadow, no text.

Frame 1: neutral stance, weight centered
Frame 2: chest rises slightly, shoulders up a little
Frame 3: top of the breath, tiny lift
Frame 4: chest falls back, slightly lower than frame 1
```
</details>

<details><summary>prompt · u_archer_walk</summary>

```
Use the attached image as the exact character reference (from Art Spec v2).
Same design, same outfit, same colors, same proportions, same art style, same lighting
(sunny, from the top-left), same 3/4 top-down camera at about 50 degrees. Do not redesign anything.
Create a 6-frame WALK CYCLE (loop) animation sprite sheet.
Grid: 3 columns x 2 rows, all cells exactly the same size, read left to right, top to bottom.
Every frame: full body, facing right, same scale in every frame, feet (or lowest point) on the same
baseline near the bottom of the cell, centered, at least 10% empty margin, nothing crossing cell borders.
Transparent background, no ground, no cast shadow, no text.

Frame 1: contact – right foot forward touching the ground, left foot back, arms swinging opposite
Frame 2: down – weight on the right foot, body slightly lower, knees bent
Frame 3: passing – left leg passing the right leg, body at normal height
Frame 4: contact – left foot forward touching the ground, right foot back
Frame 5: down – weight on the left foot, body slightly lower
Frame 6: passing – right leg passing the left leg, body at normal height
```
</details>

<details><summary>prompt · u_archer_attack</summary>

```
Use the attached image as the exact character reference (from Art Spec v2).
Same design, same outfit, same colors, same proportions, same art style, same lighting
(sunny, from the top-left), same 3/4 top-down camera at about 50 degrees. Do not redesign anything.
Create a 6-frame ATTACK – shoot a bow animation sprite sheet.
Grid: 3 columns x 2 rows, all cells exactly the same size, read left to right, top to bottom.
Every frame: full body, facing right, same scale in every frame, feet (or lowest point) on the same
baseline near the bottom of the cell, centered, at least 10% empty margin, nothing crossing cell borders.
Transparent background, no ground, no cast shadow, no text.

Frame 1: ready – standing, bow lowered, reaching for an arrow
Frame 2: nock – arrow placed on the string, bow rising
Frame 3: draw – bow raised forward, string pulled halfway
Frame 4: full draw – string pulled to the cheek, body leaning slightly back
Frame 5: release – arrow just left the bow, string snapping forward, small motion lines
Frame 6: recover – bow lowering back to the ready pose
```
</details>

<details><summary>prompt · u_archer_death</summary>

```
Use the attached image as the exact character reference (from Art Spec v2).
Same design, same outfit, same colors, same proportions, same art style, same lighting
(sunny, from the top-left), same 3/4 top-down camera at about 50 degrees. Do not redesign anything.
Create a 4-frame DEATH animation sprite sheet.
Grid: 2 columns x 2 rows, all cells exactly the same size, read left to right, top to bottom.
Every frame: full body, facing right, same scale in every frame, feet (or lowest point) on the same
baseline near the bottom of the cell, centered, at least 10% empty margin, nothing crossing cell borders.
Transparent background, no ground, no cast shadow, no text.

Frame 1: hit – head snaps back, arms flung out
Frame 2: staggering backward, knees buckling
Frame 3: falling backward at about 45 degrees
Frame 4: lying on the back on the ground, limp, eyes closed
```
</details>

### นักดาบ · `u_sword` · ลำดับ B

| ท่า | ไฟล์ | เฟรม | ตาราง | ความเร็ว |
| --- | --- | --- | --- | --- |
| idle | `anim/u_sword_idle.png` | 4 | 2 × 2 | 6 fps |
| walk | `anim/u_sword_walk.png` | 6 | 3 × 2 | 10 fps |
| attack | `anim/u_sword_attack.png` | 6 | 3 × 2 | 12 fps |
| death | `anim/u_sword_death.png` | 4 | 2 × 2 | 10 fps |

<details><summary>prompt · u_sword_idle</summary>

```
Use the attached image as the exact character reference (from Art Spec v2).
Same design, same outfit, same colors, same proportions, same art style, same lighting
(sunny, from the top-left), same 3/4 top-down camera at about 50 degrees. Do not redesign anything.
Create a 4-frame IDLE (breathing loop) animation sprite sheet.
Grid: 2 columns x 2 rows, all cells exactly the same size, read left to right, top to bottom.
Every frame: full body, facing right, same scale in every frame, feet (or lowest point) on the same
baseline near the bottom of the cell, centered, at least 10% empty margin, nothing crossing cell borders.
Transparent background, no ground, no cast shadow, no text.

Frame 1: neutral stance, weight centered
Frame 2: chest rises slightly, shoulders up a little
Frame 3: top of the breath, tiny lift
Frame 4: chest falls back, slightly lower than frame 1
```
</details>

<details><summary>prompt · u_sword_walk</summary>

```
Use the attached image as the exact character reference (from Art Spec v2).
Same design, same outfit, same colors, same proportions, same art style, same lighting
(sunny, from the top-left), same 3/4 top-down camera at about 50 degrees. Do not redesign anything.
Create a 6-frame WALK CYCLE (loop) animation sprite sheet.
Grid: 3 columns x 2 rows, all cells exactly the same size, read left to right, top to bottom.
Every frame: full body, facing right, same scale in every frame, feet (or lowest point) on the same
baseline near the bottom of the cell, centered, at least 10% empty margin, nothing crossing cell borders.
Transparent background, no ground, no cast shadow, no text.

Frame 1: contact – right foot forward touching the ground, left foot back, arms swinging opposite
Frame 2: down – weight on the right foot, body slightly lower, knees bent
Frame 3: passing – left leg passing the right leg, body at normal height
Frame 4: contact – left foot forward touching the ground, right foot back
Frame 5: down – weight on the left foot, body slightly lower
Frame 6: passing – right leg passing the left leg, body at normal height
```
</details>

<details><summary>prompt · u_sword_attack</summary>

```
Use the attached image as the exact character reference (from Art Spec v2).
Same design, same outfit, same colors, same proportions, same art style, same lighting
(sunny, from the top-left), same 3/4 top-down camera at about 50 degrees. Do not redesign anything.
Create a 6-frame ATTACK – sword slash animation sprite sheet.
Grid: 3 columns x 2 rows, all cells exactly the same size, read left to right, top to bottom.
Every frame: full body, facing right, same scale in every frame, feet (or lowest point) on the same
baseline near the bottom of the cell, centered, at least 10% empty margin, nothing crossing cell borders.
Transparent background, no ground, no cast shadow, no text.

Frame 1: guard stance, shield in front, sword at the side
Frame 2: wind-up – sword raised high behind the head
Frame 3: step forward, sword starting to swing down
Frame 4: mid swing – sword blurred in front of the body, motion arc
Frame 5: follow-through – sword low on the other side, shield still up
Frame 6: return to guard stance
```
</details>

<details><summary>prompt · u_sword_death</summary>

```
Use the attached image as the exact character reference (from Art Spec v2).
Same design, same outfit, same colors, same proportions, same art style, same lighting
(sunny, from the top-left), same 3/4 top-down camera at about 50 degrees. Do not redesign anything.
Create a 4-frame DEATH animation sprite sheet.
Grid: 2 columns x 2 rows, all cells exactly the same size, read left to right, top to bottom.
Every frame: full body, facing right, same scale in every frame, feet (or lowest point) on the same
baseline near the bottom of the cell, centered, at least 10% empty margin, nothing crossing cell borders.
Transparent background, no ground, no cast shadow, no text.

Frame 1: hit – head snaps back, arms flung out
Frame 2: staggering backward, knees buckling
Frame 3: falling backward at about 45 degrees
Frame 4: lying on the back on the ground, limp, eyes closed
```
</details>

### หมอ · `u_medic` · ลำดับ B

| ท่า | ไฟล์ | เฟรม | ตาราง | ความเร็ว |
| --- | --- | --- | --- | --- |
| idle | `anim/u_medic_idle.png` | 4 | 2 × 2 | 6 fps |
| walk | `anim/u_medic_walk.png` | 6 | 3 × 2 | 10 fps |
| heal | `anim/u_medic_heal.png` | 6 | 3 × 2 | 10 fps |
| death | `anim/u_medic_death.png` | 4 | 2 × 2 | 10 fps |

<details><summary>prompt · u_medic_idle</summary>

```
Use the attached image as the exact character reference (from Art Spec v2).
Same design, same outfit, same colors, same proportions, same art style, same lighting
(sunny, from the top-left), same 3/4 top-down camera at about 50 degrees. Do not redesign anything.
Create a 4-frame IDLE (breathing loop) animation sprite sheet.
Grid: 2 columns x 2 rows, all cells exactly the same size, read left to right, top to bottom.
Every frame: full body, facing right, same scale in every frame, feet (or lowest point) on the same
baseline near the bottom of the cell, centered, at least 10% empty margin, nothing crossing cell borders.
Transparent background, no ground, no cast shadow, no text.

Frame 1: neutral stance, weight centered
Frame 2: chest rises slightly, shoulders up a little
Frame 3: top of the breath, tiny lift
Frame 4: chest falls back, slightly lower than frame 1
```
</details>

<details><summary>prompt · u_medic_walk</summary>

```
Use the attached image as the exact character reference (from Art Spec v2).
Same design, same outfit, same colors, same proportions, same art style, same lighting
(sunny, from the top-left), same 3/4 top-down camera at about 50 degrees. Do not redesign anything.
Create a 6-frame WALK CYCLE (loop) animation sprite sheet.
Grid: 3 columns x 2 rows, all cells exactly the same size, read left to right, top to bottom.
Every frame: full body, facing right, same scale in every frame, feet (or lowest point) on the same
baseline near the bottom of the cell, centered, at least 10% empty margin, nothing crossing cell borders.
Transparent background, no ground, no cast shadow, no text.

Frame 1: contact – right foot forward touching the ground, left foot back, arms swinging opposite
Frame 2: down – weight on the right foot, body slightly lower, knees bent
Frame 3: passing – left leg passing the right leg, body at normal height
Frame 4: contact – left foot forward touching the ground, right foot back
Frame 5: down – weight on the left foot, body slightly lower
Frame 6: passing – right leg passing the left leg, body at normal height
```
</details>

<details><summary>prompt · u_medic_heal</summary>

```
Use the attached image as the exact character reference (from Art Spec v2).
Same design, same outfit, same colors, same proportions, same art style, same lighting
(sunny, from the top-left), same 3/4 top-down camera at about 50 degrees. Do not redesign anything.
Create a 6-frame HEAL – cast a healing spell (loop) animation sprite sheet.
Grid: 3 columns x 2 rows, all cells exactly the same size, read left to right, top to bottom.
Every frame: full body, facing right, same scale in every frame, feet (or lowest point) on the same
baseline near the bottom of the cell, centered, at least 10% empty margin, nothing crossing cell borders.
Transparent background, no ground, no cast shadow, no text.

Frame 1: kneeling slightly, hands reaching into the herb satchel
Frame 2: holding up a glowing green herb bundle
Frame 3: both hands forward, soft green light gathering
Frame 4: bright green healing burst from the hands
Frame 5: green sparkles floating forward
Frame 6: lowering the hands, glow fading
```
</details>

<details><summary>prompt · u_medic_death</summary>

```
Use the attached image as the exact character reference (from Art Spec v2).
Same design, same outfit, same colors, same proportions, same art style, same lighting
(sunny, from the top-left), same 3/4 top-down camera at about 50 degrees. Do not redesign anything.
Create a 4-frame DEATH animation sprite sheet.
Grid: 2 columns x 2 rows, all cells exactly the same size, read left to right, top to bottom.
Every frame: full body, facing right, same scale in every frame, feet (or lowest point) on the same
baseline near the bottom of the cell, centered, at least 10% empty margin, nothing crossing cell borders.
Transparent background, no ground, no cast shadow, no text.

Frame 1: hit – head snaps back, arms flung out
Frame 2: staggering backward, knees buckling
Frame 3: falling backward at about 45 degrees
Frame 4: lying on the back on the ground, limp, eyes closed
```
</details>

### Hero Warrior (ยังไม่เปิด) · `hero_warrior` · ลำดับ D · ทำทีหลัง

| ท่า | ไฟล์ | เฟรม | ตาราง | ความเร็ว |
| --- | --- | --- | --- | --- |
| idle | `anim/hero_warrior_idle.png` | 4 | 2 × 2 | 6 fps |
| walk | `anim/hero_warrior_walk.png` | 6 | 3 × 2 | 10 fps |
| attack | `anim/hero_warrior_attack.png` | 6 | 3 × 2 | 12 fps |
| hurt | `anim/hero_warrior_hurt.png` | 4 | 2 × 2 | 12 fps |
| death | `anim/hero_warrior_death.png` | 4 | 2 × 2 | 10 fps |

<details><summary>prompt · hero_warrior_idle</summary>

```
Use the attached image as the exact character reference (from Art Spec v2).
Same design, same outfit, same colors, same proportions, same art style, same lighting
(sunny, from the top-left), same 3/4 top-down camera at about 50 degrees. Do not redesign anything.
Create a 4-frame IDLE (breathing loop) animation sprite sheet.
Grid: 2 columns x 2 rows, all cells exactly the same size, read left to right, top to bottom.
Every frame: full body, facing right, same scale in every frame, feet (or lowest point) on the same
baseline near the bottom of the cell, centered, at least 10% empty margin, nothing crossing cell borders.
Transparent background, no ground, no cast shadow, no text.

Frame 1: neutral stance, weight centered
Frame 2: chest rises slightly, shoulders up a little
Frame 3: top of the breath, tiny lift
Frame 4: chest falls back, slightly lower than frame 1
```
</details>

<details><summary>prompt · hero_warrior_walk</summary>

```
Use the attached image as the exact character reference (from Art Spec v2).
Same design, same outfit, same colors, same proportions, same art style, same lighting
(sunny, from the top-left), same 3/4 top-down camera at about 50 degrees. Do not redesign anything.
Create a 6-frame WALK CYCLE (loop) animation sprite sheet.
Grid: 3 columns x 2 rows, all cells exactly the same size, read left to right, top to bottom.
Every frame: full body, facing right, same scale in every frame, feet (or lowest point) on the same
baseline near the bottom of the cell, centered, at least 10% empty margin, nothing crossing cell borders.
Transparent background, no ground, no cast shadow, no text.

Frame 1: contact – right foot forward touching the ground, left foot back, arms swinging opposite
Frame 2: down – weight on the right foot, body slightly lower, knees bent
Frame 3: passing – left leg passing the right leg, body at normal height
Frame 4: contact – left foot forward touching the ground, right foot back
Frame 5: down – weight on the left foot, body slightly lower
Frame 6: passing – right leg passing the left leg, body at normal height
```
</details>

<details><summary>prompt · hero_warrior_attack</summary>

```
Use the attached image as the exact character reference (from Art Spec v2).
Same design, same outfit, same colors, same proportions, same art style, same lighting
(sunny, from the top-left), same 3/4 top-down camera at about 50 degrees. Do not redesign anything.
Create a 6-frame ATTACK – sword slash animation sprite sheet.
Grid: 3 columns x 2 rows, all cells exactly the same size, read left to right, top to bottom.
Every frame: full body, facing right, same scale in every frame, feet (or lowest point) on the same
baseline near the bottom of the cell, centered, at least 10% empty margin, nothing crossing cell borders.
Transparent background, no ground, no cast shadow, no text.

Frame 1: guard stance, shield in front, sword at the side
Frame 2: wind-up – sword raised high behind the head
Frame 3: step forward, sword starting to swing down
Frame 4: mid swing – sword blurred in front of the body, motion arc
Frame 5: follow-through – sword low on the other side, shield still up
Frame 6: return to guard stance
```
</details>

<details><summary>prompt · hero_warrior_hurt</summary>

```
Use the attached image as the exact character reference (from Art Spec v2).
Same design, same outfit, same colors, same proportions, same art style, same lighting
(sunny, from the top-left), same 3/4 top-down camera at about 50 degrees. Do not redesign anything.
Create a 4-frame HURT (short flinch) animation sprite sheet.
Grid: 2 columns x 2 rows, all cells exactly the same size, read left to right, top to bottom.
Every frame: full body, facing right, same scale in every frame, feet (or lowest point) on the same
baseline near the bottom of the cell, centered, at least 10% empty margin, nothing crossing cell borders.
Transparent background, no ground, no cast shadow, no text.

Frame 1: impact – body jolts back, eyes squeezed shut
Frame 2: leaning back the most, arms pulled in
Frame 3: recovering, leaning slightly back
Frame 4: back to neutral stance
```
</details>

<details><summary>prompt · hero_warrior_death</summary>

```
Use the attached image as the exact character reference (from Art Spec v2).
Same design, same outfit, same colors, same proportions, same art style, same lighting
(sunny, from the top-left), same 3/4 top-down camera at about 50 degrees. Do not redesign anything.
Create a 4-frame DEATH animation sprite sheet.
Grid: 2 columns x 2 rows, all cells exactly the same size, read left to right, top to bottom.
Every frame: full body, facing right, same scale in every frame, feet (or lowest point) on the same
baseline near the bottom of the cell, centered, at least 10% empty margin, nothing crossing cell borders.
Transparent background, no ground, no cast shadow, no text.

Frame 1: hit – head snaps back, arms flung out
Frame 2: staggering backward, knees buckling
Frame 3: falling backward at about 45 degrees
Frame 4: lying on the back on the ground, limp, eyes closed
```
</details>

### Hero Mage (ยังไม่เปิด) · `hero_mage` · ลำดับ D · ทำทีหลัง

| ท่า | ไฟล์ | เฟรม | ตาราง | ความเร็ว |
| --- | --- | --- | --- | --- |
| idle | `anim/hero_mage_idle.png` | 4 | 2 × 2 | 6 fps |
| walk | `anim/hero_mage_walk.png` | 6 | 3 × 2 | 10 fps |
| attack | `anim/hero_mage_attack.png` | 6 | 3 × 2 | 12 fps |
| hurt | `anim/hero_mage_hurt.png` | 4 | 2 × 2 | 12 fps |
| death | `anim/hero_mage_death.png` | 4 | 2 × 2 | 10 fps |

<details><summary>prompt · hero_mage_idle</summary>

```
Use the attached image as the exact character reference (from Art Spec v2).
Same design, same outfit, same colors, same proportions, same art style, same lighting
(sunny, from the top-left), same 3/4 top-down camera at about 50 degrees. Do not redesign anything.
Create a 4-frame IDLE (breathing loop) animation sprite sheet.
Grid: 2 columns x 2 rows, all cells exactly the same size, read left to right, top to bottom.
Every frame: full body, facing right, same scale in every frame, feet (or lowest point) on the same
baseline near the bottom of the cell, centered, at least 10% empty margin, nothing crossing cell borders.
Transparent background, no ground, no cast shadow, no text.

Frame 1: neutral stance, weight centered
Frame 2: chest rises slightly, shoulders up a little
Frame 3: top of the breath, tiny lift
Frame 4: chest falls back, slightly lower than frame 1
```
</details>

<details><summary>prompt · hero_mage_walk</summary>

```
Use the attached image as the exact character reference (from Art Spec v2).
Same design, same outfit, same colors, same proportions, same art style, same lighting
(sunny, from the top-left), same 3/4 top-down camera at about 50 degrees. Do not redesign anything.
Create a 6-frame WALK CYCLE (loop) animation sprite sheet.
Grid: 3 columns x 2 rows, all cells exactly the same size, read left to right, top to bottom.
Every frame: full body, facing right, same scale in every frame, feet (or lowest point) on the same
baseline near the bottom of the cell, centered, at least 10% empty margin, nothing crossing cell borders.
Transparent background, no ground, no cast shadow, no text.

Frame 1: contact – right foot forward touching the ground, left foot back, arms swinging opposite
Frame 2: down – weight on the right foot, body slightly lower, knees bent
Frame 3: passing – left leg passing the right leg, body at normal height
Frame 4: contact – left foot forward touching the ground, right foot back
Frame 5: down – weight on the left foot, body slightly lower
Frame 6: passing – right leg passing the left leg, body at normal height
```
</details>

<details><summary>prompt · hero_mage_attack</summary>

```
Use the attached image as the exact character reference (from Art Spec v2).
Same design, same outfit, same colors, same proportions, same art style, same lighting
(sunny, from the top-left), same 3/4 top-down camera at about 50 degrees. Do not redesign anything.
Create a 6-frame ATTACK – cast a spell animation sprite sheet.
Grid: 3 columns x 2 rows, all cells exactly the same size, read left to right, top to bottom.
Every frame: full body, facing right, same scale in every frame, feet (or lowest point) on the same
baseline near the bottom of the cell, centered, at least 10% empty margin, nothing crossing cell borders.
Transparent background, no ground, no cast shadow, no text.

Frame 1: ready – staff held upright
Frame 2: staff raised, the orb starts glowing
Frame 3: orb glowing brightly, free hand pulled back
Frame 4: thrust – staff pointed forward, burst of light at the tip
Frame 5: magic released forward, small sparks
Frame 6: recover to the ready pose
```
</details>

<details><summary>prompt · hero_mage_hurt</summary>

```
Use the attached image as the exact character reference (from Art Spec v2).
Same design, same outfit, same colors, same proportions, same art style, same lighting
(sunny, from the top-left), same 3/4 top-down camera at about 50 degrees. Do not redesign anything.
Create a 4-frame HURT (short flinch) animation sprite sheet.
Grid: 2 columns x 2 rows, all cells exactly the same size, read left to right, top to bottom.
Every frame: full body, facing right, same scale in every frame, feet (or lowest point) on the same
baseline near the bottom of the cell, centered, at least 10% empty margin, nothing crossing cell borders.
Transparent background, no ground, no cast shadow, no text.

Frame 1: impact – body jolts back, eyes squeezed shut
Frame 2: leaning back the most, arms pulled in
Frame 3: recovering, leaning slightly back
Frame 4: back to neutral stance
```
</details>

<details><summary>prompt · hero_mage_death</summary>

```
Use the attached image as the exact character reference (from Art Spec v2).
Same design, same outfit, same colors, same proportions, same art style, same lighting
(sunny, from the top-left), same 3/4 top-down camera at about 50 degrees. Do not redesign anything.
Create a 4-frame DEATH animation sprite sheet.
Grid: 2 columns x 2 rows, all cells exactly the same size, read left to right, top to bottom.
Every frame: full body, facing right, same scale in every frame, feet (or lowest point) on the same
baseline near the bottom of the cell, centered, at least 10% empty margin, nothing crossing cell borders.
Transparent background, no ground, no cast shadow, no text.

Frame 1: hit – head snaps back, arms flung out
Frame 2: staggering backward, knees buckling
Frame 3: falling backward at about 45 degrees
Frame 4: lying on the back on the ground, limp, eyes closed
```
</details>

### Hero Engineer (ยังไม่เปิด) · `hero_engineer` · ลำดับ D · ทำทีหลัง

| ท่า | ไฟล์ | เฟรม | ตาราง | ความเร็ว |
| --- | --- | --- | --- | --- |
| idle | `anim/hero_engineer_idle.png` | 4 | 2 × 2 | 6 fps |
| walk | `anim/hero_engineer_walk.png` | 6 | 3 × 2 | 10 fps |
| attack | `anim/hero_engineer_attack.png` | 6 | 3 × 2 | 12 fps |
| hurt | `anim/hero_engineer_hurt.png` | 4 | 2 × 2 | 12 fps |
| death | `anim/hero_engineer_death.png` | 4 | 2 × 2 | 10 fps |

<details><summary>prompt · hero_engineer_idle</summary>

```
Use the attached image as the exact character reference (from Art Spec v2).
Same design, same outfit, same colors, same proportions, same art style, same lighting
(sunny, from the top-left), same 3/4 top-down camera at about 50 degrees. Do not redesign anything.
Create a 4-frame IDLE (breathing loop) animation sprite sheet.
Grid: 2 columns x 2 rows, all cells exactly the same size, read left to right, top to bottom.
Every frame: full body, facing right, same scale in every frame, feet (or lowest point) on the same
baseline near the bottom of the cell, centered, at least 10% empty margin, nothing crossing cell borders.
Transparent background, no ground, no cast shadow, no text.

Frame 1: neutral stance, weight centered
Frame 2: chest rises slightly, shoulders up a little
Frame 3: top of the breath, tiny lift
Frame 4: chest falls back, slightly lower than frame 1
```
</details>

<details><summary>prompt · hero_engineer_walk</summary>

```
Use the attached image as the exact character reference (from Art Spec v2).
Same design, same outfit, same colors, same proportions, same art style, same lighting
(sunny, from the top-left), same 3/4 top-down camera at about 50 degrees. Do not redesign anything.
Create a 6-frame WALK CYCLE (loop) animation sprite sheet.
Grid: 3 columns x 2 rows, all cells exactly the same size, read left to right, top to bottom.
Every frame: full body, facing right, same scale in every frame, feet (or lowest point) on the same
baseline near the bottom of the cell, centered, at least 10% empty margin, nothing crossing cell borders.
Transparent background, no ground, no cast shadow, no text.

Frame 1: contact – right foot forward touching the ground, left foot back, arms swinging opposite
Frame 2: down – weight on the right foot, body slightly lower, knees bent
Frame 3: passing – left leg passing the right leg, body at normal height
Frame 4: contact – left foot forward touching the ground, right foot back
Frame 5: down – weight on the left foot, body slightly lower
Frame 6: passing – right leg passing the left leg, body at normal height
```
</details>

<details><summary>prompt · hero_engineer_attack</summary>

```
Use the attached image as the exact character reference (from Art Spec v2).
Same design, same outfit, same colors, same proportions, same art style, same lighting
(sunny, from the top-left), same 3/4 top-down camera at about 50 degrees. Do not redesign anything.
Create a 6-frame ATTACK – swing a giant wrench animation sprite sheet.
Grid: 3 columns x 2 rows, all cells exactly the same size, read left to right, top to bottom.
Every frame: full body, facing right, same scale in every frame, feet (or lowest point) on the same
baseline near the bottom of the cell, centered, at least 10% empty margin, nothing crossing cell borders.
Transparent background, no ground, no cast shadow, no text.

Frame 1: wrench held on the shoulder
Frame 2: wind-up, wrench pulled back
Frame 3: step forward, swing starts
Frame 4: mid swing, motion arc
Frame 5: impact in front, small sparks
Frame 6: return to the shoulder
```
</details>

<details><summary>prompt · hero_engineer_hurt</summary>

```
Use the attached image as the exact character reference (from Art Spec v2).
Same design, same outfit, same colors, same proportions, same art style, same lighting
(sunny, from the top-left), same 3/4 top-down camera at about 50 degrees. Do not redesign anything.
Create a 4-frame HURT (short flinch) animation sprite sheet.
Grid: 2 columns x 2 rows, all cells exactly the same size, read left to right, top to bottom.
Every frame: full body, facing right, same scale in every frame, feet (or lowest point) on the same
baseline near the bottom of the cell, centered, at least 10% empty margin, nothing crossing cell borders.
Transparent background, no ground, no cast shadow, no text.

Frame 1: impact – body jolts back, eyes squeezed shut
Frame 2: leaning back the most, arms pulled in
Frame 3: recovering, leaning slightly back
Frame 4: back to neutral stance
```
</details>

<details><summary>prompt · hero_engineer_death</summary>

```
Use the attached image as the exact character reference (from Art Spec v2).
Same design, same outfit, same colors, same proportions, same art style, same lighting
(sunny, from the top-left), same 3/4 top-down camera at about 50 degrees. Do not redesign anything.
Create a 4-frame DEATH animation sprite sheet.
Grid: 2 columns x 2 rows, all cells exactly the same size, read left to right, top to bottom.
Every frame: full body, facing right, same scale in every frame, feet (or lowest point) on the same
baseline near the bottom of the cell, centered, at least 10% empty margin, nothing crossing cell borders.
Transparent background, no ground, no cast shadow, no text.

Frame 1: hit – head snaps back, arms flung out
Frame 2: staggering backward, knees buckling
Frame 3: falling backward at about 45 degrees
Frame 4: lying on the back on the ground, limp, eyes closed
```
</details>

### Hero Healer (ยังไม่เปิด) · `hero_healer` · ลำดับ D · ทำทีหลัง

| ท่า | ไฟล์ | เฟรม | ตาราง | ความเร็ว |
| --- | --- | --- | --- | --- |
| idle | `anim/hero_healer_idle.png` | 4 | 2 × 2 | 6 fps |
| walk | `anim/hero_healer_walk.png` | 6 | 3 × 2 | 10 fps |
| attack | `anim/hero_healer_attack.png` | 6 | 3 × 2 | 12 fps |
| hurt | `anim/hero_healer_hurt.png` | 4 | 2 × 2 | 12 fps |
| death | `anim/hero_healer_death.png` | 4 | 2 × 2 | 10 fps |

<details><summary>prompt · hero_healer_idle</summary>

```
Use the attached image as the exact character reference (from Art Spec v2).
Same design, same outfit, same colors, same proportions, same art style, same lighting
(sunny, from the top-left), same 3/4 top-down camera at about 50 degrees. Do not redesign anything.
Create a 4-frame IDLE (breathing loop) animation sprite sheet.
Grid: 2 columns x 2 rows, all cells exactly the same size, read left to right, top to bottom.
Every frame: full body, facing right, same scale in every frame, feet (or lowest point) on the same
baseline near the bottom of the cell, centered, at least 10% empty margin, nothing crossing cell borders.
Transparent background, no ground, no cast shadow, no text.

Frame 1: neutral stance, weight centered
Frame 2: chest rises slightly, shoulders up a little
Frame 3: top of the breath, tiny lift
Frame 4: chest falls back, slightly lower than frame 1
```
</details>

<details><summary>prompt · hero_healer_walk</summary>

```
Use the attached image as the exact character reference (from Art Spec v2).
Same design, same outfit, same colors, same proportions, same art style, same lighting
(sunny, from the top-left), same 3/4 top-down camera at about 50 degrees. Do not redesign anything.
Create a 6-frame WALK CYCLE (loop) animation sprite sheet.
Grid: 3 columns x 2 rows, all cells exactly the same size, read left to right, top to bottom.
Every frame: full body, facing right, same scale in every frame, feet (or lowest point) on the same
baseline near the bottom of the cell, centered, at least 10% empty margin, nothing crossing cell borders.
Transparent background, no ground, no cast shadow, no text.

Frame 1: contact – right foot forward touching the ground, left foot back, arms swinging opposite
Frame 2: down – weight on the right foot, body slightly lower, knees bent
Frame 3: passing – left leg passing the right leg, body at normal height
Frame 4: contact – left foot forward touching the ground, right foot back
Frame 5: down – weight on the left foot, body slightly lower
Frame 6: passing – right leg passing the left leg, body at normal height
```
</details>

<details><summary>prompt · hero_healer_attack</summary>

```
Use the attached image as the exact character reference (from Art Spec v2).
Same design, same outfit, same colors, same proportions, same art style, same lighting
(sunny, from the top-left), same 3/4 top-down camera at about 50 degrees. Do not redesign anything.
Create a 6-frame ATTACK – cast a spell animation sprite sheet.
Grid: 3 columns x 2 rows, all cells exactly the same size, read left to right, top to bottom.
Every frame: full body, facing right, same scale in every frame, feet (or lowest point) on the same
baseline near the bottom of the cell, centered, at least 10% empty margin, nothing crossing cell borders.
Transparent background, no ground, no cast shadow, no text.

Frame 1: ready – staff held upright
Frame 2: staff raised, the orb starts glowing
Frame 3: orb glowing brightly, free hand pulled back
Frame 4: thrust – staff pointed forward, burst of light at the tip
Frame 5: magic released forward, small sparks
Frame 6: recover to the ready pose
```
</details>

<details><summary>prompt · hero_healer_hurt</summary>

```
Use the attached image as the exact character reference (from Art Spec v2).
Same design, same outfit, same colors, same proportions, same art style, same lighting
(sunny, from the top-left), same 3/4 top-down camera at about 50 degrees. Do not redesign anything.
Create a 4-frame HURT (short flinch) animation sprite sheet.
Grid: 2 columns x 2 rows, all cells exactly the same size, read left to right, top to bottom.
Every frame: full body, facing right, same scale in every frame, feet (or lowest point) on the same
baseline near the bottom of the cell, centered, at least 10% empty margin, nothing crossing cell borders.
Transparent background, no ground, no cast shadow, no text.

Frame 1: impact – body jolts back, eyes squeezed shut
Frame 2: leaning back the most, arms pulled in
Frame 3: recovering, leaning slightly back
Frame 4: back to neutral stance
```
</details>

<details><summary>prompt · hero_healer_death</summary>

```
Use the attached image as the exact character reference (from Art Spec v2).
Same design, same outfit, same colors, same proportions, same art style, same lighting
(sunny, from the top-left), same 3/4 top-down camera at about 50 degrees. Do not redesign anything.
Create a 4-frame DEATH animation sprite sheet.
Grid: 2 columns x 2 rows, all cells exactly the same size, read left to right, top to bottom.
Every frame: full body, facing right, same scale in every frame, feet (or lowest point) on the same
baseline near the bottom of the cell, centered, at least 10% empty margin, nothing crossing cell borders.
Transparent background, no ground, no cast shadow, no text.

Frame 1: hit – head snaps back, arms flung out
Frame 2: staggering backward, knees buckling
Frame 3: falling backward at about 45 degrees
Frame 4: lying on the back on the ground, limp, eyes closed
```
</details>

---

## 3. Monster (ตัวแทนตระกูลละ 1 ตัว · ตัวต่างธาตุใช้ท่าเดียวกันแล้วเปลี่ยนสี)

ท่าขึ้นกับพฤติกรรมในเกม: เดินตี · วิ่งเร็ว · ตัวถึก · ยิงไกล · ระเบิดตัวเอง · บิน

### ซอมบี้ (ตัวแทนตระกูลซอมบี้ 8 ตัว) · `zombie0` · เดินตี · ลำดับ A · ทำก่อน

| ท่า | ไฟล์ | เฟรม | ตาราง | ความเร็ว |
| --- | --- | --- | --- | --- |
| walk | `anim/zombie0_walk.png` | 6 | 3 × 2 | 8 fps |
| attack | `anim/zombie0_attack.png` | 6 | 3 × 2 | 12 fps |
| death | `anim/zombie0_death.png` | 4 | 2 × 2 | 10 fps |

<details><summary>prompt · zombie0_walk</summary>

```
Use the attached image as the exact character reference (from Art Spec v2).
Same design, same outfit, same colors, same proportions, same art style, same lighting
(sunny, from the top-left), same 3/4 top-down camera at about 50 degrees. Do not redesign anything.
Create a 6-frame WALK – shambling / stalking (loop) animation sprite sheet.
Grid: 3 columns x 2 rows, all cells exactly the same size, read left to right, top to bottom.
Every frame: full body, facing right, same scale in every frame, feet (or lowest point) on the same
baseline near the bottom of the cell, centered, at least 10% empty margin, nothing crossing cell borders.
Transparent background, no ground, no cast shadow, no text.
Creature note: slow shambling walk, dragging one foot, arms reaching forward

Frame 1: contact – right foot forward touching the ground, left foot back, arms swinging opposite
Frame 2: down – weight on the right foot, body slightly lower, knees bent
Frame 3: passing – left leg passing the right leg, body at normal height
Frame 4: contact – left foot forward touching the ground, right foot back
Frame 5: down – weight on the left foot, body slightly lower
Frame 6: passing – right leg passing the left leg, body at normal height
```
</details>

<details><summary>prompt · zombie0_attack</summary>

```
Use the attached image as the exact character reference (from Art Spec v2).
Same design, same outfit, same colors, same proportions, same art style, same lighting
(sunny, from the top-left), same 3/4 top-down camera at about 50 degrees. Do not redesign anything.
Create a 6-frame ATTACK – claw / weapon strike animation sprite sheet.
Grid: 3 columns x 2 rows, all cells exactly the same size, read left to right, top to bottom.
Every frame: full body, facing right, same scale in every frame, feet (or lowest point) on the same
baseline near the bottom of the cell, centered, at least 10% empty margin, nothing crossing cell borders.
Transparent background, no ground, no cast shadow, no text.
Creature note: slow shambling walk, dragging one foot, arms reaching forward

Frame 1: ready, leaning forward
Frame 2: wind-up – arm or weapon pulled back high
Frame 3: lunge forward, strike starting
Frame 4: hit – arm or weapon fully forward, motion arc
Frame 5: follow-through, body low
Frame 6: recover to ready
```
</details>

<details><summary>prompt · zombie0_death</summary>

```
Use the attached image as the exact character reference (from Art Spec v2).
Same design, same outfit, same colors, same proportions, same art style, same lighting
(sunny, from the top-left), same 3/4 top-down camera at about 50 degrees. Do not redesign anything.
Create a 4-frame DEATH animation sprite sheet.
Grid: 2 columns x 2 rows, all cells exactly the same size, read left to right, top to bottom.
Every frame: full body, facing right, same scale in every frame, feet (or lowest point) on the same
baseline near the bottom of the cell, centered, at least 10% empty margin, nothing crossing cell borders.
Transparent background, no ground, no cast shadow, no text.
Creature note: slow shambling walk, dragging one foot, arms reaching forward

Frame 1: hit – head snaps back, arms flung out
Frame 2: staggering backward, knees buckling
Frame 3: falling backward at about 45 degrees
Frame 4: lying on the back on the ground, limp, eyes closed
```
</details>

### หมาป่า · `wolf0` · วิ่งเร็ว · ลำดับ A · ทำก่อน

| ท่า | ไฟล์ | เฟรม | ตาราง | ความเร็ว |
| --- | --- | --- | --- | --- |
| walk | `anim/wolf0_walk.png` | 6 | 3 × 2 | 14 fps |
| attack | `anim/wolf0_attack.png` | 6 | 3 × 2 | 14 fps |
| death | `anim/wolf0_death.png` | 4 | 2 × 2 | 10 fps |

<details><summary>prompt · wolf0_walk</summary>

```
Use the attached image as the exact character reference (from Art Spec v2).
Same design, same outfit, same colors, same proportions, same art style, same lighting
(sunny, from the top-left), same 3/4 top-down camera at about 50 degrees. Do not redesign anything.
Create a 6-frame RUN CYCLE – fast gallop or sprint (loop) animation sprite sheet.
Grid: 3 columns x 2 rows, all cells exactly the same size, read left to right, top to bottom.
Every frame: full body, facing right, same scale in every frame, feet (or lowest point) on the same
baseline near the bottom of the cell, centered, at least 10% empty margin, nothing crossing cell borders.
Transparent background, no ground, no cast shadow, no text.
Creature note: four-legged gallop

Frame 1: legs gathered under the body
Frame 2: front legs reaching forward, body stretched
Frame 3: front feet landing
Frame 4: back legs pushing, body compressed
Frame 5: all legs extended, slight air time
Frame 6: landing, back to gathered
```
</details>

<details><summary>prompt · wolf0_attack</summary>

```
Use the attached image as the exact character reference (from Art Spec v2).
Same design, same outfit, same colors, same proportions, same art style, same lighting
(sunny, from the top-left), same 3/4 top-down camera at about 50 degrees. Do not redesign anything.
Create a 6-frame ATTACK – leaping bite / pounce animation sprite sheet.
Grid: 3 columns x 2 rows, all cells exactly the same size, read left to right, top to bottom.
Every frame: full body, facing right, same scale in every frame, feet (or lowest point) on the same
baseline near the bottom of the cell, centered, at least 10% empty margin, nothing crossing cell borders.
Transparent background, no ground, no cast shadow, no text.
Creature note: four-legged gallop

Frame 1: crouch low, ready to spring
Frame 2: leap forward, body stretched
Frame 3: mouth or claws wide open at the peak
Frame 4: bite / strike in front, motion lines
Frame 5: landing
Frame 6: recover
```
</details>

<details><summary>prompt · wolf0_death</summary>

```
Use the attached image as the exact character reference (from Art Spec v2).
Same design, same outfit, same colors, same proportions, same art style, same lighting
(sunny, from the top-left), same 3/4 top-down camera at about 50 degrees. Do not redesign anything.
Create a 4-frame DEATH animation sprite sheet.
Grid: 2 columns x 2 rows, all cells exactly the same size, read left to right, top to bottom.
Every frame: full body, facing right, same scale in every frame, feet (or lowest point) on the same
baseline near the bottom of the cell, centered, at least 10% empty margin, nothing crossing cell borders.
Transparent background, no ground, no cast shadow, no text.
Creature note: four-legged gallop

Frame 1: hit – head snaps back, arms flung out
Frame 2: staggering backward, knees buckling
Frame 3: falling backward at about 45 degrees
Frame 4: lying on the back on the ground, limp, eyes closed
```
</details>

### สไลม์ · `slime0` · ระเบิดตัวเอง · ลำดับ A · ทำก่อน

| ท่า | ไฟล์ | เฟรม | ตาราง | ความเร็ว |
| --- | --- | --- | --- | --- |
| walk | `anim/slime0_walk.png` | 6 | 3 × 2 | 10 fps |
| attack | `anim/slime0_attack.png` | 6 | 3 × 2 | 14 fps |
| death | `anim/slime0_death.png` | 4 | 2 × 2 | 10 fps |

<details><summary>prompt · slime0_walk</summary>

```
Use the attached image as the exact character reference (from Art Spec v2).
Same design, same outfit, same colors, same proportions, same art style, same lighting
(sunny, from the top-left), same 3/4 top-down camera at about 50 degrees. Do not redesign anything.
Create a 6-frame MOVE – bouncing hop / scuttle (loop) animation sprite sheet.
Grid: 3 columns x 2 rows, all cells exactly the same size, read left to right, top to bottom.
Every frame: full body, facing right, same scale in every frame, feet (or lowest point) on the same
baseline near the bottom of the cell, centered, at least 10% empty margin, nothing crossing cell borders.
Transparent background, no ground, no cast shadow, no text.
Creature note: jelly body squashes and stretches

Frame 1: squashed flat, about to hop
Frame 2: stretching upward, leaving the ground
Frame 3: highest point, round shape
Frame 4: falling, stretched downward
Frame 5: landing, squashed wide
Frame 6: recovering to normal shape
```
</details>

<details><summary>prompt · slime0_attack</summary>

```
Use the attached image as the exact character reference (from Art Spec v2).
Same design, same outfit, same colors, same proportions, same art style, same lighting
(sunny, from the top-left), same 3/4 top-down camera at about 50 degrees. Do not redesign anything.
Create a 6-frame EXPLODE – swell and burst animation sprite sheet.
Grid: 3 columns x 2 rows, all cells exactly the same size, read left to right, top to bottom.
Every frame: full body, facing right, same scale in every frame, feet (or lowest point) on the same
baseline near the bottom of the cell, centered, at least 10% empty margin, nothing crossing cell borders.
Transparent background, no ground, no cast shadow, no text.
Creature note: jelly body squashes and stretches

Frame 1: normal shape, glowing core brightening
Frame 2: swelling bigger, cracks of light
Frame 3: very swollen, shaking, bright glow
Frame 4: about to burst, white-hot core
Frame 5: bursting into a round explosion
Frame 6: smoke puff and small fragments fading
```
</details>

<details><summary>prompt · slime0_death</summary>

```
Use the attached image as the exact character reference (from Art Spec v2).
Same design, same outfit, same colors, same proportions, same art style, same lighting
(sunny, from the top-left), same 3/4 top-down camera at about 50 degrees. Do not redesign anything.
Create a 4-frame DEATH animation sprite sheet.
Grid: 2 columns x 2 rows, all cells exactly the same size, read left to right, top to bottom.
Every frame: full body, facing right, same scale in every frame, feet (or lowest point) on the same
baseline near the bottom of the cell, centered, at least 10% empty margin, nothing crossing cell borders.
Transparent background, no ground, no cast shadow, no text.
Creature note: jelly body squashes and stretches

Frame 1: hit – head snaps back, arms flung out
Frame 2: staggering backward, knees buckling
Frame 3: falling backward at about 45 degrees
Frame 4: lying on the back on the ground, limp, eyes closed
```
</details>

### ค้างคาว · `bat0` · บิน · ลำดับ A · ทำก่อน

| ท่า | ไฟล์ | เฟรม | ตาราง | ความเร็ว |
| --- | --- | --- | --- | --- |
| walk | `anim/bat0_walk.png` | 6 | 3 × 2 | 12 fps |
| attack | `anim/bat0_attack.png` | 6 | 3 × 2 | 14 fps |
| death | `anim/bat0_death.png` | 4 | 2 × 2 | 10 fps |

<details><summary>prompt · bat0_walk</summary>

```
Use the attached image as the exact character reference (from Art Spec v2).
Same design, same outfit, same colors, same proportions, same art style, same lighting
(sunny, from the top-left), same 3/4 top-down camera at about 50 degrees. Do not redesign anything.
Create a 6-frame FLY – wing flap loop animation sprite sheet.
Grid: 3 columns x 2 rows, all cells exactly the same size, read left to right, top to bottom.
Every frame: full body, facing right, same scale in every frame, feet (or lowest point) on the same
baseline near the bottom of the cell, centered, at least 10% empty margin, nothing crossing cell borders.
Transparent background, no ground, no cast shadow, no text.
Creature note: small fast flaps

Frame 1: wings fully up
Frame 2: wings half down
Frame 3: wings fully down, body lifted
Frame 4: wings sweeping back up
Frame 5: wings half up
Frame 6: wings almost fully up
```
</details>

<details><summary>prompt · bat0_attack</summary>

```
Use the attached image as the exact character reference (from Art Spec v2).
Same design, same outfit, same colors, same proportions, same art style, same lighting
(sunny, from the top-left), same 3/4 top-down camera at about 50 degrees. Do not redesign anything.
Create a 6-frame ATTACK – swooping dive animation sprite sheet.
Grid: 3 columns x 2 rows, all cells exactly the same size, read left to right, top to bottom.
Every frame: full body, facing right, same scale in every frame, feet (or lowest point) on the same
baseline near the bottom of the cell, centered, at least 10% empty margin, nothing crossing cell borders.
Transparent background, no ground, no cast shadow, no text.
Creature note: small fast flaps

Frame 1: hovering, wings up
Frame 2: tilting forward, wings folding
Frame 3: diving forward and down, wings back
Frame 4: strike – claws or fangs forward at the lowest point
Frame 5: pulling up, wings opening wide
Frame 6: back to hover
```
</details>

<details><summary>prompt · bat0_death</summary>

```
Use the attached image as the exact character reference (from Art Spec v2).
Same design, same outfit, same colors, same proportions, same art style, same lighting
(sunny, from the top-left), same 3/4 top-down camera at about 50 degrees. Do not redesign anything.
Create a 4-frame DEATH – fall from the sky animation sprite sheet.
Grid: 2 columns x 2 rows, all cells exactly the same size, read left to right, top to bottom.
Every frame: full body, facing right, same scale in every frame, feet (or lowest point) on the same
baseline near the bottom of the cell, centered, at least 10% empty margin, nothing crossing cell borders.
Transparent background, no ground, no cast shadow, no text.
Creature note: small fast flaps

Frame 1: hit – wings jerked up, head back
Frame 2: tumbling, one wing folded
Frame 3: falling downward, wings limp
Frame 4: lying on the ground, wings spread flat
```
</details>

### โครงกระดูกนักธนู · `skel0` · ยิงไกล · ลำดับ A · ทำก่อน

| ท่า | ไฟล์ | เฟรม | ตาราง | ความเร็ว |
| --- | --- | --- | --- | --- |
| walk | `anim/skel0_walk.png` | 6 | 3 × 2 | 8 fps |
| attack | `anim/skel0_attack.png` | 6 | 3 × 2 | 12 fps |
| death | `anim/skel0_death.png` | 4 | 2 × 2 | 10 fps |

<details><summary>prompt · skel0_walk</summary>

```
Use the attached image as the exact character reference (from Art Spec v2).
Same design, same outfit, same colors, same proportions, same art style, same lighting
(sunny, from the top-left), same 3/4 top-down camera at about 50 degrees. Do not redesign anything.
Create a 6-frame WALK (loop) animation sprite sheet.
Grid: 3 columns x 2 rows, all cells exactly the same size, read left to right, top to bottom.
Every frame: full body, facing right, same scale in every frame, feet (or lowest point) on the same
baseline near the bottom of the cell, centered, at least 10% empty margin, nothing crossing cell borders.
Transparent background, no ground, no cast shadow, no text.
Creature note: shoots a bone arrow with a bow (use the bow-shooting frames)

Frame 1: contact – right foot forward touching the ground, left foot back, arms swinging opposite
Frame 2: down – weight on the right foot, body slightly lower, knees bent
Frame 3: passing – left leg passing the right leg, body at normal height
Frame 4: contact – left foot forward touching the ground, right foot back
Frame 5: down – weight on the left foot, body slightly lower
Frame 6: passing – right leg passing the left leg, body at normal height
```
</details>

<details><summary>prompt · skel0_attack</summary>

```
Use the attached image as the exact character reference (from Art Spec v2).
Same design, same outfit, same colors, same proportions, same art style, same lighting
(sunny, from the top-left), same 3/4 top-down camera at about 50 degrees. Do not redesign anything.
Create a 6-frame ATTACK – shoot a bow animation sprite sheet.
Grid: 3 columns x 2 rows, all cells exactly the same size, read left to right, top to bottom.
Every frame: full body, facing right, same scale in every frame, feet (or lowest point) on the same
baseline near the bottom of the cell, centered, at least 10% empty margin, nothing crossing cell borders.
Transparent background, no ground, no cast shadow, no text.
Creature note: shoots a bone arrow with a bow (use the bow-shooting frames)

Frame 1: ready – standing, bow lowered, reaching for an arrow
Frame 2: nock – arrow placed on the string, bow rising
Frame 3: draw – bow raised forward, string pulled halfway
Frame 4: full draw – string pulled to the cheek, body leaning slightly back
Frame 5: release – arrow just left the bow, string snapping forward, small motion lines
Frame 6: recover – bow lowering back to the ready pose
```
</details>

<details><summary>prompt · skel0_death</summary>

```
Use the attached image as the exact character reference (from Art Spec v2).
Same design, same outfit, same colors, same proportions, same art style, same lighting
(sunny, from the top-left), same 3/4 top-down camera at about 50 degrees. Do not redesign anything.
Create a 4-frame DEATH animation sprite sheet.
Grid: 2 columns x 2 rows, all cells exactly the same size, read left to right, top to bottom.
Every frame: full body, facing right, same scale in every frame, feet (or lowest point) on the same
baseline near the bottom of the cell, centered, at least 10% empty margin, nothing crossing cell borders.
Transparent background, no ground, no cast shadow, no text.
Creature note: shoots a bone arrow with a bow (use the bow-shooting frames)

Frame 1: hit – head snaps back, arms flung out
Frame 2: staggering backward, knees buckling
Frame 3: falling backward at about 45 degrees
Frame 4: lying on the back on the ground, limp, eyes closed
```
</details>

### กูล · `ghoul0` · เดินตี · ลำดับ C

| ท่า | ไฟล์ | เฟรม | ตาราง | ความเร็ว |
| --- | --- | --- | --- | --- |
| walk | `anim/ghoul0_walk.png` | 6 | 3 × 2 | 8 fps |
| attack | `anim/ghoul0_attack.png` | 6 | 3 × 2 | 12 fps |
| death | `anim/ghoul0_death.png` | 4 | 2 × 2 | 10 fps |

<details><summary>prompt · ghoul0_walk</summary>

```
Use the attached image as the exact character reference (from Art Spec v2).
Same design, same outfit, same colors, same proportions, same art style, same lighting
(sunny, from the top-left), same 3/4 top-down camera at about 50 degrees. Do not redesign anything.
Create a 6-frame WALK – shambling / stalking (loop) animation sprite sheet.
Grid: 3 columns x 2 rows, all cells exactly the same size, read left to right, top to bottom.
Every frame: full body, facing right, same scale in every frame, feet (or lowest point) on the same
baseline near the bottom of the cell, centered, at least 10% empty margin, nothing crossing cell borders.
Transparent background, no ground, no cast shadow, no text.
Creature note: crouched, fast claw swipes

Frame 1: contact – right foot forward touching the ground, left foot back, arms swinging opposite
Frame 2: down – weight on the right foot, body slightly lower, knees bent
Frame 3: passing – left leg passing the right leg, body at normal height
Frame 4: contact – left foot forward touching the ground, right foot back
Frame 5: down – weight on the left foot, body slightly lower
Frame 6: passing – right leg passing the left leg, body at normal height
```
</details>

<details><summary>prompt · ghoul0_attack</summary>

```
Use the attached image as the exact character reference (from Art Spec v2).
Same design, same outfit, same colors, same proportions, same art style, same lighting
(sunny, from the top-left), same 3/4 top-down camera at about 50 degrees. Do not redesign anything.
Create a 6-frame ATTACK – claw / weapon strike animation sprite sheet.
Grid: 3 columns x 2 rows, all cells exactly the same size, read left to right, top to bottom.
Every frame: full body, facing right, same scale in every frame, feet (or lowest point) on the same
baseline near the bottom of the cell, centered, at least 10% empty margin, nothing crossing cell borders.
Transparent background, no ground, no cast shadow, no text.
Creature note: crouched, fast claw swipes

Frame 1: ready, leaning forward
Frame 2: wind-up – arm or weapon pulled back high
Frame 3: lunge forward, strike starting
Frame 4: hit – arm or weapon fully forward, motion arc
Frame 5: follow-through, body low
Frame 6: recover to ready
```
</details>

<details><summary>prompt · ghoul0_death</summary>

```
Use the attached image as the exact character reference (from Art Spec v2).
Same design, same outfit, same colors, same proportions, same art style, same lighting
(sunny, from the top-left), same 3/4 top-down camera at about 50 degrees. Do not redesign anything.
Create a 4-frame DEATH animation sprite sheet.
Grid: 2 columns x 2 rows, all cells exactly the same size, read left to right, top to bottom.
Every frame: full body, facing right, same scale in every frame, feet (or lowest point) on the same
baseline near the bottom of the cell, centered, at least 10% empty margin, nothing crossing cell borders.
Transparent background, no ground, no cast shadow, no text.
Creature note: crouched, fast claw swipes

Frame 1: hit – head snaps back, arms flung out
Frame 2: staggering backward, knees buckling
Frame 3: falling backward at about 45 degrees
Frame 4: lying on the back on the ground, limp, eyes closed
```
</details>

### แมงมุมยักษ์ · `spider0` · วิ่งเร็ว · ลำดับ C

| ท่า | ไฟล์ | เฟรม | ตาราง | ความเร็ว |
| --- | --- | --- | --- | --- |
| walk | `anim/spider0_walk.png` | 6 | 3 × 2 | 14 fps |
| attack | `anim/spider0_attack.png` | 6 | 3 × 2 | 14 fps |
| death | `anim/spider0_death.png` | 4 | 2 × 2 | 10 fps |

<details><summary>prompt · spider0_walk</summary>

```
Use the attached image as the exact character reference (from Art Spec v2).
Same design, same outfit, same colors, same proportions, same art style, same lighting
(sunny, from the top-left), same 3/4 top-down camera at about 50 degrees. Do not redesign anything.
Create a 6-frame RUN CYCLE – fast gallop or sprint (loop) animation sprite sheet.
Grid: 3 columns x 2 rows, all cells exactly the same size, read left to right, top to bottom.
Every frame: full body, facing right, same scale in every frame, feet (or lowest point) on the same
baseline near the bottom of the cell, centered, at least 10% empty margin, nothing crossing cell borders.
Transparent background, no ground, no cast shadow, no text.
Creature note: eight legs scuttling in alternating groups; the attack is a lunging bite with fangs

Frame 1: legs gathered under the body
Frame 2: front legs reaching forward, body stretched
Frame 3: front feet landing
Frame 4: back legs pushing, body compressed
Frame 5: all legs extended, slight air time
Frame 6: landing, back to gathered
```
</details>

<details><summary>prompt · spider0_attack</summary>

```
Use the attached image as the exact character reference (from Art Spec v2).
Same design, same outfit, same colors, same proportions, same art style, same lighting
(sunny, from the top-left), same 3/4 top-down camera at about 50 degrees. Do not redesign anything.
Create a 6-frame ATTACK – leaping bite / pounce animation sprite sheet.
Grid: 3 columns x 2 rows, all cells exactly the same size, read left to right, top to bottom.
Every frame: full body, facing right, same scale in every frame, feet (or lowest point) on the same
baseline near the bottom of the cell, centered, at least 10% empty margin, nothing crossing cell borders.
Transparent background, no ground, no cast shadow, no text.
Creature note: eight legs scuttling in alternating groups; the attack is a lunging bite with fangs

Frame 1: crouch low, ready to spring
Frame 2: leap forward, body stretched
Frame 3: mouth or claws wide open at the peak
Frame 4: bite / strike in front, motion lines
Frame 5: landing
Frame 6: recover
```
</details>

<details><summary>prompt · spider0_death</summary>

```
Use the attached image as the exact character reference (from Art Spec v2).
Same design, same outfit, same colors, same proportions, same art style, same lighting
(sunny, from the top-left), same 3/4 top-down camera at about 50 degrees. Do not redesign anything.
Create a 4-frame DEATH animation sprite sheet.
Grid: 2 columns x 2 rows, all cells exactly the same size, read left to right, top to bottom.
Every frame: full body, facing right, same scale in every frame, feet (or lowest point) on the same
baseline near the bottom of the cell, centered, at least 10% empty margin, nothing crossing cell borders.
Transparent background, no ground, no cast shadow, no text.
Creature note: eight legs scuttling in alternating groups; the attack is a lunging bite with fangs

Frame 1: hit – head snaps back, arms flung out
Frame 2: staggering backward, knees buckling
Frame 3: falling backward at about 45 degrees
Frame 4: lying on the back on the ground, limp, eyes closed
```
</details>

### ออร์ก · `orc0` · ตัวถึก · ลำดับ C

| ท่า | ไฟล์ | เฟรม | ตาราง | ความเร็ว |
| --- | --- | --- | --- | --- |
| walk | `anim/orc0_walk.png` | 6 | 3 × 2 | 7 fps |
| attack | `anim/orc0_attack.png` | 6 | 3 × 2 | 10 fps |
| death | `anim/orc0_death.png` | 4 | 2 × 2 | 10 fps |

<details><summary>prompt · orc0_walk</summary>

```
Use the attached image as the exact character reference (from Art Spec v2).
Same design, same outfit, same colors, same proportions, same art style, same lighting
(sunny, from the top-left), same 3/4 top-down camera at about 50 degrees. Do not redesign anything.
Create a 6-frame WALK – heavy stomp (loop) animation sprite sheet.
Grid: 3 columns x 2 rows, all cells exactly the same size, read left to right, top to bottom.
Every frame: full body, facing right, same scale in every frame, feet (or lowest point) on the same
baseline near the bottom of the cell, centered, at least 10% empty margin, nothing crossing cell borders.
Transparent background, no ground, no cast shadow, no text.
Creature note: heavy spiked club smash

Frame 1: contact – right foot forward touching the ground, left foot back, arms swinging opposite
Frame 2: down – weight on the right foot, body slightly lower, knees bent
Frame 3: passing – left leg passing the right leg, body at normal height
Frame 4: contact – left foot forward touching the ground, right foot back
Frame 5: down – weight on the left foot, body slightly lower
Frame 6: passing – right leg passing the left leg, body at normal height
```
</details>

<details><summary>prompt · orc0_attack</summary>

```
Use the attached image as the exact character reference (from Art Spec v2).
Same design, same outfit, same colors, same proportions, same art style, same lighting
(sunny, from the top-left), same 3/4 top-down camera at about 50 degrees. Do not redesign anything.
Create a 6-frame ATTACK – overhead smash animation sprite sheet.
Grid: 3 columns x 2 rows, all cells exactly the same size, read left to right, top to bottom.
Every frame: full body, facing right, same scale in every frame, feet (or lowest point) on the same
baseline near the bottom of the cell, centered, at least 10% empty margin, nothing crossing cell borders.
Transparent background, no ground, no cast shadow, no text.
Creature note: heavy spiked club smash

Frame 1: ready, weapon or fists low
Frame 2: lift weapon / both fists high above the head
Frame 3: peak of the wind-up, body leaning back
Frame 4: smash down hard in front, motion blur
Frame 5: impact – dust and debris burst at the ground in front
Frame 6: pull weapon back up
```
</details>

<details><summary>prompt · orc0_death</summary>

```
Use the attached image as the exact character reference (from Art Spec v2).
Same design, same outfit, same colors, same proportions, same art style, same lighting
(sunny, from the top-left), same 3/4 top-down camera at about 50 degrees. Do not redesign anything.
Create a 4-frame DEATH animation sprite sheet.
Grid: 2 columns x 2 rows, all cells exactly the same size, read left to right, top to bottom.
Every frame: full body, facing right, same scale in every frame, feet (or lowest point) on the same
baseline near the bottom of the cell, centered, at least 10% empty margin, nothing crossing cell borders.
Transparent background, no ground, no cast shadow, no text.
Creature note: heavy spiked club smash

Frame 1: hit – head snaps back, arms flung out
Frame 2: staggering backward, knees buckling
Frame 3: falling backward at about 45 degrees
Frame 4: lying on the back on the ground, limp, eyes closed
```
</details>

### ภูตไฟ · `wisp0` · บิน · ลำดับ C

| ท่า | ไฟล์ | เฟรม | ตาราง | ความเร็ว |
| --- | --- | --- | --- | --- |
| walk | `anim/wisp0_walk.png` | 6 | 3 × 2 | 12 fps |
| attack | `anim/wisp0_attack.png` | 6 | 3 × 2 | 14 fps |
| death | `anim/wisp0_death.png` | 4 | 2 × 2 | 10 fps |

<details><summary>prompt · wisp0_walk</summary>

```
Use the attached image as the exact character reference (from Art Spec v2).
Same design, same outfit, same colors, same proportions, same art style, same lighting
(sunny, from the top-left), same 3/4 top-down camera at about 50 degrees. Do not redesign anything.
Create a 6-frame FLY – wing flap loop animation sprite sheet.
Grid: 3 columns x 2 rows, all cells exactly the same size, read left to right, top to bottom.
Every frame: full body, facing right, same scale in every frame, feet (or lowest point) on the same
baseline near the bottom of the cell, centered, at least 10% empty margin, nothing crossing cell borders.
Transparent background, no ground, no cast shadow, no text.
Creature note: no wings: the flame body flickers and pulses instead of flapping; the attack is a fiery lunge

Frame 1: wings fully up
Frame 2: wings half down
Frame 3: wings fully down, body lifted
Frame 4: wings sweeping back up
Frame 5: wings half up
Frame 6: wings almost fully up
```
</details>

<details><summary>prompt · wisp0_attack</summary>

```
Use the attached image as the exact character reference (from Art Spec v2).
Same design, same outfit, same colors, same proportions, same art style, same lighting
(sunny, from the top-left), same 3/4 top-down camera at about 50 degrees. Do not redesign anything.
Create a 6-frame ATTACK – swooping dive animation sprite sheet.
Grid: 3 columns x 2 rows, all cells exactly the same size, read left to right, top to bottom.
Every frame: full body, facing right, same scale in every frame, feet (or lowest point) on the same
baseline near the bottom of the cell, centered, at least 10% empty margin, nothing crossing cell borders.
Transparent background, no ground, no cast shadow, no text.
Creature note: no wings: the flame body flickers and pulses instead of flapping; the attack is a fiery lunge

Frame 1: hovering, wings up
Frame 2: tilting forward, wings folding
Frame 3: diving forward and down, wings back
Frame 4: strike – claws or fangs forward at the lowest point
Frame 5: pulling up, wings opening wide
Frame 6: back to hover
```
</details>

<details><summary>prompt · wisp0_death</summary>

```
Use the attached image as the exact character reference (from Art Spec v2).
Same design, same outfit, same colors, same proportions, same art style, same lighting
(sunny, from the top-left), same 3/4 top-down camera at about 50 degrees. Do not redesign anything.
Create a 4-frame DEATH – fall from the sky animation sprite sheet.
Grid: 2 columns x 2 rows, all cells exactly the same size, read left to right, top to bottom.
Every frame: full body, facing right, same scale in every frame, feet (or lowest point) on the same
baseline near the bottom of the cell, centered, at least 10% empty margin, nothing crossing cell borders.
Transparent background, no ground, no cast shadow, no text.
Creature note: no wings: the flame body flickers and pulses instead of flapping; the attack is a fiery lunge

Frame 1: hit – wings jerked up, head back
Frame 2: tumbling, one wing folded
Frame 3: falling downward, wings limp
Frame 4: lying on the ground, wings spread flat
```
</details>

### นักเวทกระดูก · `bonemage0` · ยิงไกล · ลำดับ C

| ท่า | ไฟล์ | เฟรม | ตาราง | ความเร็ว |
| --- | --- | --- | --- | --- |
| walk | `anim/bonemage0_walk.png` | 6 | 3 × 2 | 8 fps |
| attack | `anim/bonemage0_attack.png` | 6 | 3 × 2 | 12 fps |
| death | `anim/bonemage0_death.png` | 4 | 2 × 2 | 10 fps |

<details><summary>prompt · bonemage0_walk</summary>

```
Use the attached image as the exact character reference (from Art Spec v2).
Same design, same outfit, same colors, same proportions, same art style, same lighting
(sunny, from the top-left), same 3/4 top-down camera at about 50 degrees. Do not redesign anything.
Create a 6-frame WALK (loop) animation sprite sheet.
Grid: 3 columns x 2 rows, all cells exactly the same size, read left to right, top to bottom.
Every frame: full body, facing right, same scale in every frame, feet (or lowest point) on the same
baseline near the bottom of the cell, centered, at least 10% empty margin, nothing crossing cell borders.
Transparent background, no ground, no cast shadow, no text.
Creature note: raises the bone staff and fires a glowing orb

Frame 1: contact – right foot forward touching the ground, left foot back, arms swinging opposite
Frame 2: down – weight on the right foot, body slightly lower, knees bent
Frame 3: passing – left leg passing the right leg, body at normal height
Frame 4: contact – left foot forward touching the ground, right foot back
Frame 5: down – weight on the left foot, body slightly lower
Frame 6: passing – right leg passing the left leg, body at normal height
```
</details>

<details><summary>prompt · bonemage0_attack</summary>

```
Use the attached image as the exact character reference (from Art Spec v2).
Same design, same outfit, same colors, same proportions, same art style, same lighting
(sunny, from the top-left), same 3/4 top-down camera at about 50 degrees. Do not redesign anything.
Create a 6-frame ATTACK – ranged shot / spell animation sprite sheet.
Grid: 3 columns x 2 rows, all cells exactly the same size, read left to right, top to bottom.
Every frame: full body, facing right, same scale in every frame, feet (or lowest point) on the same
baseline near the bottom of the cell, centered, at least 10% empty margin, nothing crossing cell borders.
Transparent background, no ground, no cast shadow, no text.
Creature note: raises the bone staff and fires a glowing orb

Frame 1: ready
Frame 2: raise bow or staff, aim to the right
Frame 3: charging – glowing energy or arrow drawn
Frame 4: release – projectile leaves to the right, flash
Frame 5: recoil, slight lean back
Frame 6: recover
```
</details>

<details><summary>prompt · bonemage0_death</summary>

```
Use the attached image as the exact character reference (from Art Spec v2).
Same design, same outfit, same colors, same proportions, same art style, same lighting
(sunny, from the top-left), same 3/4 top-down camera at about 50 degrees. Do not redesign anything.
Create a 4-frame DEATH animation sprite sheet.
Grid: 2 columns x 2 rows, all cells exactly the same size, read left to right, top to bottom.
Every frame: full body, facing right, same scale in every frame, feet (or lowest point) on the same
baseline near the bottom of the cell, centered, at least 10% empty margin, nothing crossing cell borders.
Transparent background, no ground, no cast shadow, no text.
Creature note: raises the bone staff and fires a glowing orb

Frame 1: hit – head snaps back, arms flung out
Frame 2: staggering backward, knees buckling
Frame 3: falling backward at about 45 degrees
Frame 4: lying on the back on the ground, limp, eyes closed
```
</details>

### ด้วงระเบิด · `beetle0` · ระเบิดตัวเอง · ลำดับ C

| ท่า | ไฟล์ | เฟรม | ตาราง | ความเร็ว |
| --- | --- | --- | --- | --- |
| walk | `anim/beetle0_walk.png` | 6 | 3 × 2 | 10 fps |
| attack | `anim/beetle0_attack.png` | 6 | 3 × 2 | 14 fps |
| death | `anim/beetle0_death.png` | 4 | 2 × 2 | 10 fps |

<details><summary>prompt · beetle0_walk</summary>

```
Use the attached image as the exact character reference (from Art Spec v2).
Same design, same outfit, same colors, same proportions, same art style, same lighting
(sunny, from the top-left), same 3/4 top-down camera at about 50 degrees. Do not redesign anything.
Create a 6-frame MOVE – bouncing hop / scuttle (loop) animation sprite sheet.
Grid: 3 columns x 2 rows, all cells exactly the same size, read left to right, top to bottom.
Every frame: full body, facing right, same scale in every frame, feet (or lowest point) on the same
baseline near the bottom of the cell, centered, at least 10% empty margin, nothing crossing cell borders.
Transparent background, no ground, no cast shadow, no text.
Creature note: six legs scuttling instead of hopping; the glowing horn swells before the explosion

Frame 1: squashed flat, about to hop
Frame 2: stretching upward, leaving the ground
Frame 3: highest point, round shape
Frame 4: falling, stretched downward
Frame 5: landing, squashed wide
Frame 6: recovering to normal shape
```
</details>

<details><summary>prompt · beetle0_attack</summary>

```
Use the attached image as the exact character reference (from Art Spec v2).
Same design, same outfit, same colors, same proportions, same art style, same lighting
(sunny, from the top-left), same 3/4 top-down camera at about 50 degrees. Do not redesign anything.
Create a 6-frame EXPLODE – swell and burst animation sprite sheet.
Grid: 3 columns x 2 rows, all cells exactly the same size, read left to right, top to bottom.
Every frame: full body, facing right, same scale in every frame, feet (or lowest point) on the same
baseline near the bottom of the cell, centered, at least 10% empty margin, nothing crossing cell borders.
Transparent background, no ground, no cast shadow, no text.
Creature note: six legs scuttling instead of hopping; the glowing horn swells before the explosion

Frame 1: normal shape, glowing core brightening
Frame 2: swelling bigger, cracks of light
Frame 3: very swollen, shaking, bright glow
Frame 4: about to burst, white-hot core
Frame 5: bursting into a round explosion
Frame 6: smoke puff and small fragments fading
```
</details>

<details><summary>prompt · beetle0_death</summary>

```
Use the attached image as the exact character reference (from Art Spec v2).
Same design, same outfit, same colors, same proportions, same art style, same lighting
(sunny, from the top-left), same 3/4 top-down camera at about 50 degrees. Do not redesign anything.
Create a 4-frame DEATH animation sprite sheet.
Grid: 2 columns x 2 rows, all cells exactly the same size, read left to right, top to bottom.
Every frame: full body, facing right, same scale in every frame, feet (or lowest point) on the same
baseline near the bottom of the cell, centered, at least 10% empty margin, nothing crossing cell borders.
Transparent background, no ground, no cast shadow, no text.
Creature note: six legs scuttling instead of hopping; the glowing horn swells before the explosion

Frame 1: hit – head snaps back, arms flung out
Frame 2: staggering backward, knees buckling
Frame 3: falling backward at about 45 degrees
Frame 4: lying on the back on the ground, limp, eyes closed
```
</details>

### อัศวินมรณะ · `knight0` · เดินตี · ลำดับ C

| ท่า | ไฟล์ | เฟรม | ตาราง | ความเร็ว |
| --- | --- | --- | --- | --- |
| walk | `anim/knight0_walk.png` | 6 | 3 × 2 | 8 fps |
| attack | `anim/knight0_attack.png` | 6 | 3 × 2 | 12 fps |
| death | `anim/knight0_death.png` | 4 | 2 × 2 | 10 fps |

<details><summary>prompt · knight0_walk</summary>

```
Use the attached image as the exact character reference (from Art Spec v2).
Same design, same outfit, same colors, same proportions, same art style, same lighting
(sunny, from the top-left), same 3/4 top-down camera at about 50 degrees. Do not redesign anything.
Create a 6-frame WALK – shambling / stalking (loop) animation sprite sheet.
Grid: 3 columns x 2 rows, all cells exactly the same size, read left to right, top to bottom.
Every frame: full body, facing right, same scale in every frame, feet (or lowest point) on the same
baseline near the bottom of the cell, centered, at least 10% empty margin, nothing crossing cell borders.
Transparent background, no ground, no cast shadow, no text.
Creature note: heavy greatsword slash with shield

Frame 1: contact – right foot forward touching the ground, left foot back, arms swinging opposite
Frame 2: down – weight on the right foot, body slightly lower, knees bent
Frame 3: passing – left leg passing the right leg, body at normal height
Frame 4: contact – left foot forward touching the ground, right foot back
Frame 5: down – weight on the left foot, body slightly lower
Frame 6: passing – right leg passing the left leg, body at normal height
```
</details>

<details><summary>prompt · knight0_attack</summary>

```
Use the attached image as the exact character reference (from Art Spec v2).
Same design, same outfit, same colors, same proportions, same art style, same lighting
(sunny, from the top-left), same 3/4 top-down camera at about 50 degrees. Do not redesign anything.
Create a 6-frame ATTACK – claw / weapon strike animation sprite sheet.
Grid: 3 columns x 2 rows, all cells exactly the same size, read left to right, top to bottom.
Every frame: full body, facing right, same scale in every frame, feet (or lowest point) on the same
baseline near the bottom of the cell, centered, at least 10% empty margin, nothing crossing cell borders.
Transparent background, no ground, no cast shadow, no text.
Creature note: heavy greatsword slash with shield

Frame 1: ready, leaning forward
Frame 2: wind-up – arm or weapon pulled back high
Frame 3: lunge forward, strike starting
Frame 4: hit – arm or weapon fully forward, motion arc
Frame 5: follow-through, body low
Frame 6: recover to ready
```
</details>

<details><summary>prompt · knight0_death</summary>

```
Use the attached image as the exact character reference (from Art Spec v2).
Same design, same outfit, same colors, same proportions, same art style, same lighting
(sunny, from the top-left), same 3/4 top-down camera at about 50 degrees. Do not redesign anything.
Create a 4-frame DEATH animation sprite sheet.
Grid: 2 columns x 2 rows, all cells exactly the same size, read left to right, top to bottom.
Every frame: full body, facing right, same scale in every frame, feet (or lowest point) on the same
baseline near the bottom of the cell, centered, at least 10% empty margin, nothing crossing cell borders.
Transparent background, no ground, no cast shadow, no text.
Creature note: heavy greatsword slash with shield

Frame 1: hit – head snaps back, arms flung out
Frame 2: staggering backward, knees buckling
Frame 3: falling backward at about 45 degrees
Frame 4: lying on the back on the ground, limp, eyes closed
```
</details>

### มนุษย์หมาป่า · `were0` · วิ่งเร็ว · ลำดับ C

| ท่า | ไฟล์ | เฟรม | ตาราง | ความเร็ว |
| --- | --- | --- | --- | --- |
| walk | `anim/were0_walk.png` | 6 | 3 × 2 | 14 fps |
| attack | `anim/were0_attack.png` | 6 | 3 × 2 | 14 fps |
| death | `anim/were0_death.png` | 4 | 2 × 2 | 10 fps |

<details><summary>prompt · were0_walk</summary>

```
Use the attached image as the exact character reference (from Art Spec v2).
Same design, same outfit, same colors, same proportions, same art style, same lighting
(sunny, from the top-left), same 3/4 top-down camera at about 50 degrees. Do not redesign anything.
Create a 6-frame RUN CYCLE – fast gallop or sprint (loop) animation sprite sheet.
Grid: 3 columns x 2 rows, all cells exactly the same size, read left to right, top to bottom.
Every frame: full body, facing right, same scale in every frame, feet (or lowest point) on the same
baseline near the bottom of the cell, centered, at least 10% empty margin, nothing crossing cell borders.
Transparent background, no ground, no cast shadow, no text.
Creature note: runs on all fours, the attack is a two-claw pounce

Frame 1: legs gathered under the body
Frame 2: front legs reaching forward, body stretched
Frame 3: front feet landing
Frame 4: back legs pushing, body compressed
Frame 5: all legs extended, slight air time
Frame 6: landing, back to gathered
```
</details>

<details><summary>prompt · were0_attack</summary>

```
Use the attached image as the exact character reference (from Art Spec v2).
Same design, same outfit, same colors, same proportions, same art style, same lighting
(sunny, from the top-left), same 3/4 top-down camera at about 50 degrees. Do not redesign anything.
Create a 6-frame ATTACK – leaping bite / pounce animation sprite sheet.
Grid: 3 columns x 2 rows, all cells exactly the same size, read left to right, top to bottom.
Every frame: full body, facing right, same scale in every frame, feet (or lowest point) on the same
baseline near the bottom of the cell, centered, at least 10% empty margin, nothing crossing cell borders.
Transparent background, no ground, no cast shadow, no text.
Creature note: runs on all fours, the attack is a two-claw pounce

Frame 1: crouch low, ready to spring
Frame 2: leap forward, body stretched
Frame 3: mouth or claws wide open at the peak
Frame 4: bite / strike in front, motion lines
Frame 5: landing
Frame 6: recover
```
</details>

<details><summary>prompt · were0_death</summary>

```
Use the attached image as the exact character reference (from Art Spec v2).
Same design, same outfit, same colors, same proportions, same art style, same lighting
(sunny, from the top-left), same 3/4 top-down camera at about 50 degrees. Do not redesign anything.
Create a 4-frame DEATH animation sprite sheet.
Grid: 2 columns x 2 rows, all cells exactly the same size, read left to right, top to bottom.
Every frame: full body, facing right, same scale in every frame, feet (or lowest point) on the same
baseline near the bottom of the cell, centered, at least 10% empty margin, nothing crossing cell borders.
Transparent background, no ground, no cast shadow, no text.
Creature note: runs on all fours, the attack is a two-claw pounce

Frame 1: hit – head snaps back, arms flung out
Frame 2: staggering backward, knees buckling
Frame 3: falling backward at about 45 degrees
Frame 4: lying on the back on the ground, limp, eyes closed
```
</details>

### โกเลมหิน · `golem0` · ตัวถึก · ลำดับ C

| ท่า | ไฟล์ | เฟรม | ตาราง | ความเร็ว |
| --- | --- | --- | --- | --- |
| walk | `anim/golem0_walk.png` | 6 | 3 × 2 | 7 fps |
| attack | `anim/golem0_attack.png` | 6 | 3 × 2 | 10 fps |
| death | `anim/golem0_death.png` | 4 | 2 × 2 | 10 fps |

<details><summary>prompt · golem0_walk</summary>

```
Use the attached image as the exact character reference (from Art Spec v2).
Same design, same outfit, same colors, same proportions, same art style, same lighting
(sunny, from the top-left), same 3/4 top-down camera at about 50 degrees. Do not redesign anything.
Create a 6-frame WALK – heavy stomp (loop) animation sprite sheet.
Grid: 3 columns x 2 rows, all cells exactly the same size, read left to right, top to bottom.
Every frame: full body, facing right, same scale in every frame, feet (or lowest point) on the same
baseline near the bottom of the cell, centered, at least 10% empty margin, nothing crossing cell borders.
Transparent background, no ground, no cast shadow, no text.
Creature note: very slow stomp, both stone fists smash the ground

Frame 1: contact – right foot forward touching the ground, left foot back, arms swinging opposite
Frame 2: down – weight on the right foot, body slightly lower, knees bent
Frame 3: passing – left leg passing the right leg, body at normal height
Frame 4: contact – left foot forward touching the ground, right foot back
Frame 5: down – weight on the left foot, body slightly lower
Frame 6: passing – right leg passing the left leg, body at normal height
```
</details>

<details><summary>prompt · golem0_attack</summary>

```
Use the attached image as the exact character reference (from Art Spec v2).
Same design, same outfit, same colors, same proportions, same art style, same lighting
(sunny, from the top-left), same 3/4 top-down camera at about 50 degrees. Do not redesign anything.
Create a 6-frame ATTACK – overhead smash animation sprite sheet.
Grid: 3 columns x 2 rows, all cells exactly the same size, read left to right, top to bottom.
Every frame: full body, facing right, same scale in every frame, feet (or lowest point) on the same
baseline near the bottom of the cell, centered, at least 10% empty margin, nothing crossing cell borders.
Transparent background, no ground, no cast shadow, no text.
Creature note: very slow stomp, both stone fists smash the ground

Frame 1: ready, weapon or fists low
Frame 2: lift weapon / both fists high above the head
Frame 3: peak of the wind-up, body leaning back
Frame 4: smash down hard in front, motion blur
Frame 5: impact – dust and debris burst at the ground in front
Frame 6: pull weapon back up
```
</details>

<details><summary>prompt · golem0_death</summary>

```
Use the attached image as the exact character reference (from Art Spec v2).
Same design, same outfit, same colors, same proportions, same art style, same lighting
(sunny, from the top-left), same 3/4 top-down camera at about 50 degrees. Do not redesign anything.
Create a 4-frame DEATH animation sprite sheet.
Grid: 2 columns x 2 rows, all cells exactly the same size, read left to right, top to bottom.
Every frame: full body, facing right, same scale in every frame, feet (or lowest point) on the same
baseline near the bottom of the cell, centered, at least 10% empty margin, nothing crossing cell borders.
Transparent background, no ground, no cast shadow, no text.
Creature note: very slow stomp, both stone fists smash the ground

Frame 1: hit – head snaps back, arms flung out
Frame 2: staggering backward, knees buckling
Frame 3: falling backward at about 45 degrees
Frame 4: lying on the back on the ground, limp, eyes closed
```
</details>

### ปีศาจปีก · `demon0` · บิน · ลำดับ C

| ท่า | ไฟล์ | เฟรม | ตาราง | ความเร็ว |
| --- | --- | --- | --- | --- |
| walk | `anim/demon0_walk.png` | 6 | 3 × 2 | 12 fps |
| attack | `anim/demon0_attack.png` | 6 | 3 × 2 | 14 fps |
| death | `anim/demon0_death.png` | 4 | 2 × 2 | 10 fps |

<details><summary>prompt · demon0_walk</summary>

```
Use the attached image as the exact character reference (from Art Spec v2).
Same design, same outfit, same colors, same proportions, same art style, same lighting
(sunny, from the top-left), same 3/4 top-down camera at about 50 degrees. Do not redesign anything.
Create a 6-frame FLY – wing flap loop animation sprite sheet.
Grid: 3 columns x 2 rows, all cells exactly the same size, read left to right, top to bottom.
Every frame: full body, facing right, same scale in every frame, feet (or lowest point) on the same
baseline near the bottom of the cell, centered, at least 10% empty margin, nothing crossing cell borders.
Transparent background, no ground, no cast shadow, no text.
Creature note: big bat-like wings, clawed dive attack

Frame 1: wings fully up
Frame 2: wings half down
Frame 3: wings fully down, body lifted
Frame 4: wings sweeping back up
Frame 5: wings half up
Frame 6: wings almost fully up
```
</details>

<details><summary>prompt · demon0_attack</summary>

```
Use the attached image as the exact character reference (from Art Spec v2).
Same design, same outfit, same colors, same proportions, same art style, same lighting
(sunny, from the top-left), same 3/4 top-down camera at about 50 degrees. Do not redesign anything.
Create a 6-frame ATTACK – swooping dive animation sprite sheet.
Grid: 3 columns x 2 rows, all cells exactly the same size, read left to right, top to bottom.
Every frame: full body, facing right, same scale in every frame, feet (or lowest point) on the same
baseline near the bottom of the cell, centered, at least 10% empty margin, nothing crossing cell borders.
Transparent background, no ground, no cast shadow, no text.
Creature note: big bat-like wings, clawed dive attack

Frame 1: hovering, wings up
Frame 2: tilting forward, wings folding
Frame 3: diving forward and down, wings back
Frame 4: strike – claws or fangs forward at the lowest point
Frame 5: pulling up, wings opening wide
Frame 6: back to hover
```
</details>

<details><summary>prompt · demon0_death</summary>

```
Use the attached image as the exact character reference (from Art Spec v2).
Same design, same outfit, same colors, same proportions, same art style, same lighting
(sunny, from the top-left), same 3/4 top-down camera at about 50 degrees. Do not redesign anything.
Create a 4-frame DEATH – fall from the sky animation sprite sheet.
Grid: 2 columns x 2 rows, all cells exactly the same size, read left to right, top to bottom.
Every frame: full body, facing right, same scale in every frame, feet (or lowest point) on the same
baseline near the bottom of the cell, centered, at least 10% empty margin, nothing crossing cell borders.
Transparent background, no ground, no cast shadow, no text.
Creature note: big bat-like wings, clawed dive attack

Frame 1: hit – wings jerked up, head back
Frame 2: tumbling, one wing folded
Frame 3: falling downward, wings limp
Frame 4: lying on the ground, wings spread flat
```
</details>

### ลิชมรณะ · `lich0` · ยิงไกล · ลำดับ C

| ท่า | ไฟล์ | เฟรม | ตาราง | ความเร็ว |
| --- | --- | --- | --- | --- |
| walk | `anim/lich0_walk.png` | 6 | 3 × 2 | 8 fps |
| attack | `anim/lich0_attack.png` | 6 | 3 × 2 | 12 fps |
| death | `anim/lich0_death.png` | 4 | 2 × 2 | 10 fps |

<details><summary>prompt · lich0_walk</summary>

```
Use the attached image as the exact character reference (from Art Spec v2).
Same design, same outfit, same colors, same proportions, same art style, same lighting
(sunny, from the top-left), same 3/4 top-down camera at about 50 degrees. Do not redesign anything.
Create a 6-frame WALK (loop) animation sprite sheet.
Grid: 3 columns x 2 rows, all cells exactly the same size, read left to right, top to bottom.
Every frame: full body, facing right, same scale in every frame, feet (or lowest point) on the same
baseline near the bottom of the cell, centered, at least 10% empty margin, nothing crossing cell borders.
Transparent background, no ground, no cast shadow, no text.
Creature note: floating slightly, raises the crystal staff and fires dark magic

Frame 1: contact – right foot forward touching the ground, left foot back, arms swinging opposite
Frame 2: down – weight on the right foot, body slightly lower, knees bent
Frame 3: passing – left leg passing the right leg, body at normal height
Frame 4: contact – left foot forward touching the ground, right foot back
Frame 5: down – weight on the left foot, body slightly lower
Frame 6: passing – right leg passing the left leg, body at normal height
```
</details>

<details><summary>prompt · lich0_attack</summary>

```
Use the attached image as the exact character reference (from Art Spec v2).
Same design, same outfit, same colors, same proportions, same art style, same lighting
(sunny, from the top-left), same 3/4 top-down camera at about 50 degrees. Do not redesign anything.
Create a 6-frame ATTACK – ranged shot / spell animation sprite sheet.
Grid: 3 columns x 2 rows, all cells exactly the same size, read left to right, top to bottom.
Every frame: full body, facing right, same scale in every frame, feet (or lowest point) on the same
baseline near the bottom of the cell, centered, at least 10% empty margin, nothing crossing cell borders.
Transparent background, no ground, no cast shadow, no text.
Creature note: floating slightly, raises the crystal staff and fires dark magic

Frame 1: ready
Frame 2: raise bow or staff, aim to the right
Frame 3: charging – glowing energy or arrow drawn
Frame 4: release – projectile leaves to the right, flash
Frame 5: recoil, slight lean back
Frame 6: recover
```
</details>

<details><summary>prompt · lich0_death</summary>

```
Use the attached image as the exact character reference (from Art Spec v2).
Same design, same outfit, same colors, same proportions, same art style, same lighting
(sunny, from the top-left), same 3/4 top-down camera at about 50 degrees. Do not redesign anything.
Create a 4-frame DEATH animation sprite sheet.
Grid: 2 columns x 2 rows, all cells exactly the same size, read left to right, top to bottom.
Every frame: full body, facing right, same scale in every frame, feet (or lowest point) on the same
baseline near the bottom of the cell, centered, at least 10% empty margin, nothing crossing cell borders.
Transparent background, no ground, no cast shadow, no text.
Creature note: floating slightly, raises the crystal staff and fires dark magic

Frame 1: hit – head snaps back, arms flung out
Frame 2: staggering backward, knees buckling
Frame 3: falling backward at about 45 degrees
Frame 4: lying on the back on the ground, limp, eyes closed
```
</details>

### บอส 5 ตัว · ลำดับ B

ท่าเหมือนตระกูลพฤติกรรมของตัวเอง + ท่าพิเศษ 1 ท่า

#### ราชาซอมบี้ · `boss0` · เดินตี

| ท่า | ไฟล์ | เฟรม | ตาราง | ความเร็ว |
| --- | --- | --- | --- | --- |
| walk | `anim/boss0_walk.png` | 6 | 3 × 2 | 8 fps |
| attack | `anim/boss0_attack.png` | 6 | 3 × 2 | 12 fps |
| death | `anim/boss0_death.png` | 4 | 2 × 2 | 10 fps |
| special | `anim/boss0_special.png` | 6 | 3 × 2 | 10 fps |

<details><summary>prompt · boss0_walk</summary>

```
Use the attached image as the exact character reference (from Art Spec v2).
Same design, same outfit, same colors, same proportions, same art style, same lighting
(sunny, from the top-left), same 3/4 top-down camera at about 50 degrees. Do not redesign anything.
Create a 6-frame WALK – shambling / stalking (loop) animation sprite sheet.
Grid: 3 columns x 2 rows, all cells exactly the same size, read left to right, top to bottom.
Every frame: full body, facing right, same scale in every frame, feet (or lowest point) on the same
baseline near the bottom of the cell, centered, at least 10% empty margin, nothing crossing cell borders.
Transparent background, no ground, no cast shadow, no text.
Creature note: huge boss version, keep the golden crown in every frame

Frame 1: contact – right foot forward touching the ground, left foot back, arms swinging opposite
Frame 2: down – weight on the right foot, body slightly lower, knees bent
Frame 3: passing – left leg passing the right leg, body at normal height
Frame 4: contact – left foot forward touching the ground, right foot back
Frame 5: down – weight on the left foot, body slightly lower
Frame 6: passing – right leg passing the left leg, body at normal height
```
</details>

<details><summary>prompt · boss0_attack</summary>

```
Use the attached image as the exact character reference (from Art Spec v2).
Same design, same outfit, same colors, same proportions, same art style, same lighting
(sunny, from the top-left), same 3/4 top-down camera at about 50 degrees. Do not redesign anything.
Create a 6-frame ATTACK – claw / weapon strike animation sprite sheet.
Grid: 3 columns x 2 rows, all cells exactly the same size, read left to right, top to bottom.
Every frame: full body, facing right, same scale in every frame, feet (or lowest point) on the same
baseline near the bottom of the cell, centered, at least 10% empty margin, nothing crossing cell borders.
Transparent background, no ground, no cast shadow, no text.
Creature note: huge boss version, keep the golden crown in every frame

Frame 1: ready, leaning forward
Frame 2: wind-up – arm or weapon pulled back high
Frame 3: lunge forward, strike starting
Frame 4: hit – arm or weapon fully forward, motion arc
Frame 5: follow-through, body low
Frame 6: recover to ready
```
</details>

<details><summary>prompt · boss0_death</summary>

```
Use the attached image as the exact character reference (from Art Spec v2).
Same design, same outfit, same colors, same proportions, same art style, same lighting
(sunny, from the top-left), same 3/4 top-down camera at about 50 degrees. Do not redesign anything.
Create a 4-frame DEATH animation sprite sheet.
Grid: 2 columns x 2 rows, all cells exactly the same size, read left to right, top to bottom.
Every frame: full body, facing right, same scale in every frame, feet (or lowest point) on the same
baseline near the bottom of the cell, centered, at least 10% empty margin, nothing crossing cell borders.
Transparent background, no ground, no cast shadow, no text.
Creature note: huge boss version, keep the golden crown in every frame

Frame 1: hit – head snaps back, arms flung out
Frame 2: staggering backward, knees buckling
Frame 3: falling backward at about 45 degrees
Frame 4: lying on the back on the ground, limp, eyes closed
```
</details>

<details><summary>prompt · boss0_special</summary>

```
Use the attached image as the exact character reference (from Art Spec v2).
Same design, same outfit, same colors, same proportions, same art style, same lighting
(sunny, from the top-left), same 3/4 top-down camera at about 50 degrees. Do not redesign anything.
Create a 6-frame SPECIAL – summon minions animation sprite sheet.
Grid: 3 columns x 2 rows, all cells exactly the same size, read left to right, top to bottom.
Every frame: full body, facing right, same scale in every frame, feet (or lowest point) on the same
baseline near the bottom of the cell, centered, at least 10% empty margin, nothing crossing cell borders.
Transparent background, no ground, no cast shadow, no text.
Creature note: huge boss version, keep the golden crown in every frame

Frame 1: standing tall, arms down
Frame 2: both arms raised, green light from the crown
Frame 3: roaring upward, green energy swirling
Frame 4: slamming both hands toward the ground
Frame 5: green glow bursting from the ground around him
Frame 6: recover
```
</details>

#### จ้าวฝูงหมาป่า · `boss1` · วิ่งเร็ว

| ท่า | ไฟล์ | เฟรม | ตาราง | ความเร็ว |
| --- | --- | --- | --- | --- |
| walk | `anim/boss1_walk.png` | 6 | 3 × 2 | 14 fps |
| attack | `anim/boss1_attack.png` | 6 | 3 × 2 | 14 fps |
| death | `anim/boss1_death.png` | 4 | 2 × 2 | 10 fps |
| special | `anim/boss1_special.png` | 6 | 3 × 2 | 10 fps |

<details><summary>prompt · boss1_walk</summary>

```
Use the attached image as the exact character reference (from Art Spec v2).
Same design, same outfit, same colors, same proportions, same art style, same lighting
(sunny, from the top-left), same 3/4 top-down camera at about 50 degrees. Do not redesign anything.
Create a 6-frame RUN CYCLE – fast gallop or sprint (loop) animation sprite sheet.
Grid: 3 columns x 2 rows, all cells exactly the same size, read left to right, top to bottom.
Every frame: full body, facing right, same scale in every frame, feet (or lowest point) on the same
baseline near the bottom of the cell, centered, at least 10% empty margin, nothing crossing cell borders.
Transparent background, no ground, no cast shadow, no text.
Creature note: huge boss version, keep the golden crown in every frame

Frame 1: legs gathered under the body
Frame 2: front legs reaching forward, body stretched
Frame 3: front feet landing
Frame 4: back legs pushing, body compressed
Frame 5: all legs extended, slight air time
Frame 6: landing, back to gathered
```
</details>

<details><summary>prompt · boss1_attack</summary>

```
Use the attached image as the exact character reference (from Art Spec v2).
Same design, same outfit, same colors, same proportions, same art style, same lighting
(sunny, from the top-left), same 3/4 top-down camera at about 50 degrees. Do not redesign anything.
Create a 6-frame ATTACK – leaping bite / pounce animation sprite sheet.
Grid: 3 columns x 2 rows, all cells exactly the same size, read left to right, top to bottom.
Every frame: full body, facing right, same scale in every frame, feet (or lowest point) on the same
baseline near the bottom of the cell, centered, at least 10% empty margin, nothing crossing cell borders.
Transparent background, no ground, no cast shadow, no text.
Creature note: huge boss version, keep the golden crown in every frame

Frame 1: crouch low, ready to spring
Frame 2: leap forward, body stretched
Frame 3: mouth or claws wide open at the peak
Frame 4: bite / strike in front, motion lines
Frame 5: landing
Frame 6: recover
```
</details>

<details><summary>prompt · boss1_death</summary>

```
Use the attached image as the exact character reference (from Art Spec v2).
Same design, same outfit, same colors, same proportions, same art style, same lighting
(sunny, from the top-left), same 3/4 top-down camera at about 50 degrees. Do not redesign anything.
Create a 4-frame DEATH animation sprite sheet.
Grid: 2 columns x 2 rows, all cells exactly the same size, read left to right, top to bottom.
Every frame: full body, facing right, same scale in every frame, feet (or lowest point) on the same
baseline near the bottom of the cell, centered, at least 10% empty margin, nothing crossing cell borders.
Transparent background, no ground, no cast shadow, no text.
Creature note: huge boss version, keep the golden crown in every frame

Frame 1: hit – head snaps back, arms flung out
Frame 2: staggering backward, knees buckling
Frame 3: falling backward at about 45 degrees
Frame 4: lying on the back on the ground, limp, eyes closed
```
</details>

<details><summary>prompt · boss1_special</summary>

```
Use the attached image as the exact character reference (from Art Spec v2).
Same design, same outfit, same colors, same proportions, same art style, same lighting
(sunny, from the top-left), same 3/4 top-down camera at about 50 degrees. Do not redesign anything.
Create a 6-frame SPECIAL – howl animation sprite sheet.
Grid: 3 columns x 2 rows, all cells exactly the same size, read left to right, top to bottom.
Every frame: full body, facing right, same scale in every frame, feet (or lowest point) on the same
baseline near the bottom of the cell, centered, at least 10% empty margin, nothing crossing cell borders.
Transparent background, no ground, no cast shadow, no text.
Creature note: huge boss version, keep the golden crown in every frame

Frame 1: standing, head low
Frame 2: head lifting
Frame 3: head thrown back, mouth open, howling
Frame 4: howl peak, sound rings around the head
Frame 5: howl ending
Frame 6: head lowering
```
</details>

#### ราชินีแมงมุม · `boss2` · ยิงไกล

| ท่า | ไฟล์ | เฟรม | ตาราง | ความเร็ว |
| --- | --- | --- | --- | --- |
| walk | `anim/boss2_walk.png` | 6 | 3 × 2 | 8 fps |
| attack | `anim/boss2_attack.png` | 6 | 3 × 2 | 12 fps |
| death | `anim/boss2_death.png` | 4 | 2 × 2 | 10 fps |
| special | `anim/boss2_special.png` | 6 | 3 × 2 | 12 fps |

<details><summary>prompt · boss2_walk</summary>

```
Use the attached image as the exact character reference (from Art Spec v2).
Same design, same outfit, same colors, same proportions, same art style, same lighting
(sunny, from the top-left), same 3/4 top-down camera at about 50 degrees. Do not redesign anything.
Create a 6-frame WALK (loop) animation sprite sheet.
Grid: 3 columns x 2 rows, all cells exactly the same size, read left to right, top to bottom.
Every frame: full body, facing right, same scale in every frame, feet (or lowest point) on the same
baseline near the bottom of the cell, centered, at least 10% empty margin, nothing crossing cell borders.
Transparent background, no ground, no cast shadow, no text.
Creature note: huge boss version, keep the golden crown in every frame

Frame 1: contact – right foot forward touching the ground, left foot back, arms swinging opposite
Frame 2: down – weight on the right foot, body slightly lower, knees bent
Frame 3: passing – left leg passing the right leg, body at normal height
Frame 4: contact – left foot forward touching the ground, right foot back
Frame 5: down – weight on the left foot, body slightly lower
Frame 6: passing – right leg passing the left leg, body at normal height
```
</details>

<details><summary>prompt · boss2_attack</summary>

```
Use the attached image as the exact character reference (from Art Spec v2).
Same design, same outfit, same colors, same proportions, same art style, same lighting
(sunny, from the top-left), same 3/4 top-down camera at about 50 degrees. Do not redesign anything.
Create a 6-frame ATTACK – ranged shot / spell animation sprite sheet.
Grid: 3 columns x 2 rows, all cells exactly the same size, read left to right, top to bottom.
Every frame: full body, facing right, same scale in every frame, feet (or lowest point) on the same
baseline near the bottom of the cell, centered, at least 10% empty margin, nothing crossing cell borders.
Transparent background, no ground, no cast shadow, no text.
Creature note: huge boss version, keep the golden crown in every frame

Frame 1: ready
Frame 2: raise bow or staff, aim to the right
Frame 3: charging – glowing energy or arrow drawn
Frame 4: release – projectile leaves to the right, flash
Frame 5: recoil, slight lean back
Frame 6: recover
```
</details>

<details><summary>prompt · boss2_death</summary>

```
Use the attached image as the exact character reference (from Art Spec v2).
Same design, same outfit, same colors, same proportions, same art style, same lighting
(sunny, from the top-left), same 3/4 top-down camera at about 50 degrees. Do not redesign anything.
Create a 4-frame DEATH animation sprite sheet.
Grid: 2 columns x 2 rows, all cells exactly the same size, read left to right, top to bottom.
Every frame: full body, facing right, same scale in every frame, feet (or lowest point) on the same
baseline near the bottom of the cell, centered, at least 10% empty margin, nothing crossing cell borders.
Transparent background, no ground, no cast shadow, no text.
Creature note: huge boss version, keep the golden crown in every frame

Frame 1: hit – head snaps back, arms flung out
Frame 2: staggering backward, knees buckling
Frame 3: falling backward at about 45 degrees
Frame 4: lying on the back on the ground, limp, eyes closed
```
</details>

<details><summary>prompt · boss2_special</summary>

```
Use the attached image as the exact character reference (from Art Spec v2).
Same design, same outfit, same colors, same proportions, same art style, same lighting
(sunny, from the top-left), same 3/4 top-down camera at about 50 degrees. Do not redesign anything.
Create a 6-frame SPECIAL – spit web animation sprite sheet.
Grid: 3 columns x 2 rows, all cells exactly the same size, read left to right, top to bottom.
Every frame: full body, facing right, same scale in every frame, feet (or lowest point) on the same
baseline near the bottom of the cell, centered, at least 10% empty margin, nothing crossing cell borders.
Transparent background, no ground, no cast shadow, no text.
Creature note: huge boss version, keep the golden crown in every frame

Frame 1: rearing back on hind legs
Frame 2: abdomen pulsing
Frame 3: mouth opening
Frame 4: spitting a big web to the right
Frame 5: web flying, legs braced
Frame 6: recover
```
</details>

#### โกเลมโบราณ · `boss3` · ตัวถึก

| ท่า | ไฟล์ | เฟรม | ตาราง | ความเร็ว |
| --- | --- | --- | --- | --- |
| walk | `anim/boss3_walk.png` | 6 | 3 × 2 | 7 fps |
| attack | `anim/boss3_attack.png` | 6 | 3 × 2 | 10 fps |
| death | `anim/boss3_death.png` | 4 | 2 × 2 | 10 fps |
| special | `anim/boss3_special.png` | 6 | 3 × 2 | 10 fps |

<details><summary>prompt · boss3_walk</summary>

```
Use the attached image as the exact character reference (from Art Spec v2).
Same design, same outfit, same colors, same proportions, same art style, same lighting
(sunny, from the top-left), same 3/4 top-down camera at about 50 degrees. Do not redesign anything.
Create a 6-frame WALK – heavy stomp (loop) animation sprite sheet.
Grid: 3 columns x 2 rows, all cells exactly the same size, read left to right, top to bottom.
Every frame: full body, facing right, same scale in every frame, feet (or lowest point) on the same
baseline near the bottom of the cell, centered, at least 10% empty margin, nothing crossing cell borders.
Transparent background, no ground, no cast shadow, no text.
Creature note: huge boss version, keep the golden crown in every frame

Frame 1: contact – right foot forward touching the ground, left foot back, arms swinging opposite
Frame 2: down – weight on the right foot, body slightly lower, knees bent
Frame 3: passing – left leg passing the right leg, body at normal height
Frame 4: contact – left foot forward touching the ground, right foot back
Frame 5: down – weight on the left foot, body slightly lower
Frame 6: passing – right leg passing the left leg, body at normal height
```
</details>

<details><summary>prompt · boss3_attack</summary>

```
Use the attached image as the exact character reference (from Art Spec v2).
Same design, same outfit, same colors, same proportions, same art style, same lighting
(sunny, from the top-left), same 3/4 top-down camera at about 50 degrees. Do not redesign anything.
Create a 6-frame ATTACK – overhead smash animation sprite sheet.
Grid: 3 columns x 2 rows, all cells exactly the same size, read left to right, top to bottom.
Every frame: full body, facing right, same scale in every frame, feet (or lowest point) on the same
baseline near the bottom of the cell, centered, at least 10% empty margin, nothing crossing cell borders.
Transparent background, no ground, no cast shadow, no text.
Creature note: huge boss version, keep the golden crown in every frame

Frame 1: ready, weapon or fists low
Frame 2: lift weapon / both fists high above the head
Frame 3: peak of the wind-up, body leaning back
Frame 4: smash down hard in front, motion blur
Frame 5: impact – dust and debris burst at the ground in front
Frame 6: pull weapon back up
```
</details>

<details><summary>prompt · boss3_death</summary>

```
Use the attached image as the exact character reference (from Art Spec v2).
Same design, same outfit, same colors, same proportions, same art style, same lighting
(sunny, from the top-left), same 3/4 top-down camera at about 50 degrees. Do not redesign anything.
Create a 4-frame DEATH animation sprite sheet.
Grid: 2 columns x 2 rows, all cells exactly the same size, read left to right, top to bottom.
Every frame: full body, facing right, same scale in every frame, feet (or lowest point) on the same
baseline near the bottom of the cell, centered, at least 10% empty margin, nothing crossing cell borders.
Transparent background, no ground, no cast shadow, no text.
Creature note: huge boss version, keep the golden crown in every frame

Frame 1: hit – head snaps back, arms flung out
Frame 2: staggering backward, knees buckling
Frame 3: falling backward at about 45 degrees
Frame 4: lying on the back on the ground, limp, eyes closed
```
</details>

<details><summary>prompt · boss3_special</summary>

```
Use the attached image as the exact character reference (from Art Spec v2).
Same design, same outfit, same colors, same proportions, same art style, same lighting
(sunny, from the top-left), same 3/4 top-down camera at about 50 degrees. Do not redesign anything.
Create a 6-frame SPECIAL – ground slam shockwave animation sprite sheet.
Grid: 3 columns x 2 rows, all cells exactly the same size, read left to right, top to bottom.
Every frame: full body, facing right, same scale in every frame, feet (or lowest point) on the same
baseline near the bottom of the cell, centered, at least 10% empty margin, nothing crossing cell borders.
Transparent background, no ground, no cast shadow, no text.
Creature note: huge boss version, keep the golden crown in every frame

Frame 1: standing
Frame 2: both fists raised high, runes glowing gold
Frame 3: peak, body arched back
Frame 4: slamming both fists into the ground
Frame 5: golden shockwave ring and rocks bursting out
Frame 6: recover
```
</details>

#### มังกรเงา · `boss4` · บิน

| ท่า | ไฟล์ | เฟรม | ตาราง | ความเร็ว |
| --- | --- | --- | --- | --- |
| walk | `anim/boss4_walk.png` | 6 | 3 × 2 | 12 fps |
| attack | `anim/boss4_attack.png` | 6 | 3 × 2 | 14 fps |
| death | `anim/boss4_death.png` | 4 | 2 × 2 | 10 fps |
| special | `anim/boss4_special.png` | 6 | 3 × 2 | 12 fps |

<details><summary>prompt · boss4_walk</summary>

```
Use the attached image as the exact character reference (from Art Spec v2).
Same design, same outfit, same colors, same proportions, same art style, same lighting
(sunny, from the top-left), same 3/4 top-down camera at about 50 degrees. Do not redesign anything.
Create a 6-frame FLY – wing flap loop animation sprite sheet.
Grid: 3 columns x 2 rows, all cells exactly the same size, read left to right, top to bottom.
Every frame: full body, facing right, same scale in every frame, feet (or lowest point) on the same
baseline near the bottom of the cell, centered, at least 10% empty margin, nothing crossing cell borders.
Transparent background, no ground, no cast shadow, no text.
Creature note: huge boss version, keep the golden crown in every frame

Frame 1: wings fully up
Frame 2: wings half down
Frame 3: wings fully down, body lifted
Frame 4: wings sweeping back up
Frame 5: wings half up
Frame 6: wings almost fully up
```
</details>

<details><summary>prompt · boss4_attack</summary>

```
Use the attached image as the exact character reference (from Art Spec v2).
Same design, same outfit, same colors, same proportions, same art style, same lighting
(sunny, from the top-left), same 3/4 top-down camera at about 50 degrees. Do not redesign anything.
Create a 6-frame ATTACK – swooping dive animation sprite sheet.
Grid: 3 columns x 2 rows, all cells exactly the same size, read left to right, top to bottom.
Every frame: full body, facing right, same scale in every frame, feet (or lowest point) on the same
baseline near the bottom of the cell, centered, at least 10% empty margin, nothing crossing cell borders.
Transparent background, no ground, no cast shadow, no text.
Creature note: huge boss version, keep the golden crown in every frame

Frame 1: hovering, wings up
Frame 2: tilting forward, wings folding
Frame 3: diving forward and down, wings back
Frame 4: strike – claws or fangs forward at the lowest point
Frame 5: pulling up, wings opening wide
Frame 6: back to hover
```
</details>

<details><summary>prompt · boss4_death</summary>

```
Use the attached image as the exact character reference (from Art Spec v2).
Same design, same outfit, same colors, same proportions, same art style, same lighting
(sunny, from the top-left), same 3/4 top-down camera at about 50 degrees. Do not redesign anything.
Create a 4-frame DEATH – fall from the sky animation sprite sheet.
Grid: 2 columns x 2 rows, all cells exactly the same size, read left to right, top to bottom.
Every frame: full body, facing right, same scale in every frame, feet (or lowest point) on the same
baseline near the bottom of the cell, centered, at least 10% empty margin, nothing crossing cell borders.
Transparent background, no ground, no cast shadow, no text.
Creature note: huge boss version, keep the golden crown in every frame

Frame 1: hit – wings jerked up, head back
Frame 2: tumbling, one wing folded
Frame 3: falling downward, wings limp
Frame 4: lying on the ground, wings spread flat
```
</details>

<details><summary>prompt · boss4_special</summary>

```
Use the attached image as the exact character reference (from Art Spec v2).
Same design, same outfit, same colors, same proportions, same art style, same lighting
(sunny, from the top-left), same 3/4 top-down camera at about 50 degrees. Do not redesign anything.
Create a 6-frame SPECIAL – shadow breath animation sprite sheet.
Grid: 3 columns x 2 rows, all cells exactly the same size, read left to right, top to bottom.
Every frame: full body, facing right, same scale in every frame, feet (or lowest point) on the same
baseline near the bottom of the cell, centered, at least 10% empty margin, nothing crossing cell borders.
Transparent background, no ground, no cast shadow, no text.
Creature note: huge boss version, keep the golden crown in every frame

Frame 1: hovering, wings up
Frame 2: head pulled back, purple glow in the throat
Frame 3: mouth opening, glow brightening
Frame 4: breathing a stream of purple shadow fire to the right
Frame 5: breath at full length
Frame 6: closing mouth, smoke fading
```
</details>

---

## 4. เอฟเฟกต์และฉากที่ขยับ (ลำดับ C)

แนบภาพ v2 ของชิ้นนั้นไปด้วยเหมือนกัน (ธงใช้ธงจาก `camp1`)

| ไฟล์ | อะไร | เฟรม | ตาราง |
| --- | --- | --- | --- |
| `anim/fx_blast.png` | ระเบิด (เล่นครั้งเดียว) | 6 | 3 × 2 |
| `anim/firepit.png` | กองไฟหน้าค่าย (วนลูป) | 4 | 2 × 2 |
| `anim/fx_levelup.png` | เลเวลอัป (เล่นครั้งเดียว) | 6 | 3 × 2 |
| `anim/fx_recall.png` | วงวาร์ปกลับฐาน (วนลูป) | 4 | 2 × 2 |
| `anim/fx_heal.png` | ประกายรักษา (เล่นครั้งเดียว) | 4 | 2 × 2 |
| `anim/flag.png` | ธงฟ้าบนอาคาร (วนลูป) | 4 | 2 × 2 |

<details><summary>prompt · fx_blast</summary>

```
Use the attached image as the exact character reference (from Art Spec v2).
Same design, same outfit, same colors, same proportions, same art style, same lighting
(sunny, from the top-left), same 3/4 top-down camera at about 50 degrees. Do not redesign anything.
Create a 6-frame EFFECT animation sprite sheet.
Grid: 3 columns x 2 rows, all cells exactly the same size, read left to right, top to bottom.
Every frame: same center point and scale in every frame, centered, at least 10% empty margin, nothing crossing cell borders.
Transparent background, no ground, no cast shadow, no text.

Frame 1: tiny bright spark
Frame 2: growing orange fireball
Frame 3: full explosion with debris
Frame 4: explosion breaking apart into smoke
Frame 5: dark smoke puffs
Frame 6: last wisps of smoke fading
```
</details>

<details><summary>prompt · firepit</summary>

```
Use the attached image as the exact character reference (from Art Spec v2).
Same design, same outfit, same colors, same proportions, same art style, same lighting
(sunny, from the top-left), same 3/4 top-down camera at about 50 degrees. Do not redesign anything.
Create a 4-frame EFFECT animation sprite sheet.
Grid: 2 columns x 2 rows, all cells exactly the same size, read left to right, top to bottom.
Every frame: same center point and scale in every frame, centered, at least 10% empty margin, nothing crossing cell borders.
Transparent background, no ground, no cast shadow, no text.

Frame 1: flames medium
Frame 2: flames taller, leaning left
Frame 3: flames lower, sparks
Frame 4: flames taller, leaning right
```
</details>

<details><summary>prompt · fx_levelup</summary>

```
Use the attached image as the exact character reference (from Art Spec v2).
Same design, same outfit, same colors, same proportions, same art style, same lighting
(sunny, from the top-left), same 3/4 top-down camera at about 50 degrees. Do not redesign anything.
Create a 6-frame EFFECT animation sprite sheet.
Grid: 3 columns x 2 rows, all cells exactly the same size, read left to right, top to bottom.
Every frame: same center point and scale in every frame, centered, at least 10% empty margin, nothing crossing cell borders.
Transparent background, no ground, no cast shadow, no text.

Frame 1: golden ring appears on the ground
Frame 2: ring grows, light rising
Frame 3: pillar of golden light
Frame 4: pillar brightest with sparkles
Frame 5: light fading upward
Frame 6: last sparkles
```
</details>

<details><summary>prompt · fx_recall</summary>

```
Use the attached image as the exact character reference (from Art Spec v2).
Same design, same outfit, same colors, same proportions, same art style, same lighting
(sunny, from the top-left), same 3/4 top-down camera at about 50 degrees. Do not redesign anything.
Create a 4-frame EFFECT animation sprite sheet.
Grid: 2 columns x 2 rows, all cells exactly the same size, read left to right, top to bottom.
Every frame: same center point and scale in every frame, centered, at least 10% empty margin, nothing crossing cell borders.
Transparent background, no ground, no cast shadow, no text.

Frame 1: blue swirl circle
Frame 2: swirl rotated 90 degrees, brighter
Frame 3: swirl rotated 180 degrees
Frame 4: swirl rotated 270 degrees, brighter
```
</details>

<details><summary>prompt · fx_heal</summary>

```
Use the attached image as the exact character reference (from Art Spec v2).
Same design, same outfit, same colors, same proportions, same art style, same lighting
(sunny, from the top-left), same 3/4 top-down camera at about 50 degrees. Do not redesign anything.
Create a 4-frame EFFECT animation sprite sheet.
Grid: 2 columns x 2 rows, all cells exactly the same size, read left to right, top to bottom.
Every frame: same center point and scale in every frame, centered, at least 10% empty margin, nothing crossing cell borders.
Transparent background, no ground, no cast shadow, no text.

Frame 1: small green spark
Frame 2: green sparkles spreading
Frame 3: biggest green glow with plus signs
Frame 4: sparkles fading upward
```
</details>

<details><summary>prompt · flag</summary>

```
Use the attached image as the exact character reference (from Art Spec v2).
Same design, same outfit, same colors, same proportions, same art style, same lighting
(sunny, from the top-left), same 3/4 top-down camera at about 50 degrees. Do not redesign anything.
Create a 4-frame EFFECT animation sprite sheet.
Grid: 2 columns x 2 rows, all cells exactly the same size, read left to right, top to bottom.
Every frame: same center point and scale in every frame, centered, at least 10% empty margin, nothing crossing cell borders.
Transparent background, no ground, no cast shadow, no text.

Frame 1: blue flag waving, wave at the pole
Frame 2: wave in the middle
Frame 3: wave near the tip
Frame 4: flag almost straight
```
</details>

---

## 5. สรุปจำนวนและลำดับ

| ลำดับ | อะไร | จำนวนภาพ |
| --- | --- | --- |
| A · ทำก่อน | Hero Archer, คนงาน, Monster ระดับต่ำ 5 ตระกูล | 28 |
| B | พลธนู นักดาบ หมอ, บอส 5 ตัว | 32 |
| C | Monster ระดับกลาง/สูง 11 ตระกูล, เอฟเฟกต์ | 39 |
| D · ทำทีหลัง | Hero อีก 4 อาชีพ (ยังไม่เปิดในเกม) | 20 |
| | **รวม** | **119** |

ทำแค่ชุด A ก่อนก็เห็นผลชัดแล้ว: ตัวที่อยู่บนจอเกือบตลอดเวลาจะขยับจริง

## 6. ส่งภาพกลับมา

1. อัปโหลดไว้ใน `assets/anim/` ของ repo ชื่อไฟล์ตามตาราง แล้วกด **Commit changes**
2. ส่งทีละตัวได้ ตัวที่ยังไม่มีไฟล์ เกมใช้ท่าขยับด้วยโค้ดแทน
3. บอก Claude ว่า "ใส่ท่าทางชุดใหม่" แล้วจะตัดเฟรม จัดระดับเท้า และใส่เข้าเกมให้

