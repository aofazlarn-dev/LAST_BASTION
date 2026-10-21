// บอทจำลองผู้เล่น: ใช้แค่คำสั่งเดียวกับที่ผู้เล่นจริงส่ง (move/moveTo/build/train/repair/equip/salvage/skill/recall)
// ใช้: node tools/botsim.js <core.js> [จำนวนแผนที่] [ระดับฝีมือ 0..1]
const { Core, DATA } = require(process.argv[2]);
const SEEDS = Number(process.argv[3] || 8);
const SKILL = Number(process.argv[4] || 1);   // 1 = เล่นเก่ง, 0.5 = เล่นพอใช้ (สร้างช้า ไม่ค่อยซ่อม)
const S = DATA.tile;

function score(it) {
  const s = it.stats;
  return (s.atk || 0) * 3 + (s.hp || 0) * 0.5 + (s.def || 0) * 6 + (s.as || 0) * 120 + (s.crit || 0) * 120 + (s.spd || 0) * 0.5;
}

function plan(st) {
  // แผนสร้าง: ป้อมชั้นใน, กำแพงวงรอบ (เว้นประตู 4 ทิศ), ป้อมเพิ่ม
  const N = st.map.n, c = N / 2, out = [], seen = new Set();
  const add = (kind, x, y) => { const k = x + "," + y; if (!seen.has(k)) { seen.add(k); out.push({ kind, x, y }); } };
  for (let k = 0; k < 3; k++) { const a = k * 2 * Math.PI / 3 + 0.5; add("tower", Math.round(c + Math.cos(a) * 5), Math.round(c + Math.sin(a) * 5)); }
  for (let a = 0; a < 360; a += 3) {
    const x = Math.round(c + Math.cos(a * Math.PI / 180) * 8), y = Math.round(c + Math.sin(a * Math.PI / 180) * 8);
    add(a % 90 < 6 ? "gate" : "wall", x, y);
  }
  for (let k = 0; k < 9; k++) { const a = k * 2 * Math.PI / 9; add("tower", Math.round(c + Math.cos(a) * 6.3), Math.round(c + Math.sin(a) * 6.3)); }
  return out;
}

function runSeed(seed) {
  const st = Core.createState(seed), h = st.heroes[0], todo = plan(st);
  const cmd = (c) => Core.applyCommand(st, { heroId: "p1", ...c });
  let deaths = 0, bosses = 0, built = 0, nightReached = 1; const builtToday = {}; let trained = 0, workerDeaths = 0;
  for (let i = 0; i < 20 * 60 * 40 && !st.result; i++) {
    if (i % 20 === 0 && !h.dead) {
      const night = Core.phase(st) === "night" || !!st.wave;
      // ของ: สวมชิ้นที่ดีกว่า ย่อยที่เหลือเมื่อกระเป๋าใกล้เต็ม
      for (const it of [...h.bag]) {
        const cur = h.equip[it.slot];
        if (!cur || score(it) > score(cur)) cmd({ type: "equip", itemId: it.id });
      }
      while (h.bag.length > 8) cmd({ type: "salvage", itemId: h.bag[0].id });
      // ฐาน
      const stock = st.stock[1], camp = st.buildings.find((b) => b.type === "camp");
      const has = (t) => st.buildings.some((b) => b.type === t);
      const count = (t) => st.units.filter((u) => u.type === t).length;
      const pop = (k) => Core.popUsed(st, 1, k || "army") < Core.popCap(st, 1, k || "army");
      if (count("worker") < (SKILL >= 0.75 ? 3 + camp.lv : 2) && pop("worker") && stock.wood >= 15 + (count("worker") ? 20 : 0)) cmd({ type: "hire", unit: "worker" });
      if (SKILL >= 0.75 && !night && (camp.hp < camp.maxHp * 0.85 || st.buildings.some((b) => b.hp < b.maxHp * 0.6))) cmd({ type: "repair" });
      if (SKILL >= 0.75) {
        // ผู้เล่นเก่ง: ทำตามลำดับเป้าหมายทีละข้อ (เก็บของจนกว่าจะทำข้อแรกที่ยังไม่เสร็จได้)
        const C = st.map.n / 2, spots = [[3, -5], [-5, -5], [3, 3], [-5, 3], [0, -6], [0, 5]];
        const place = (kind) => {
          // หาที่ว่างรอบบ้านหลัก (วงใน 3–9 ช่อง)
          for (let rad = 3; rad <= 9; rad++) for (let k = 0; k < 16; k++) {
            const a = (k / 16) * Math.PI * 2, tx = Math.round(C + Math.cos(a) * rad), ty = Math.round(C + Math.sin(a) * rad);
            const r = cmd({ type: "build", kind, tx, ty });
            if (r === true || r === "cost" || r === "locked") return r;
          }
          return "done";   // ไม่มีที่ว่างจริง ๆ ข้ามไป
        };
        const towers = () => st.buildings.filter((b) => b.type === "tower");
        const towerTo = (lv, n) => () => { const t = towers().filter((x) => x.lv < lv).slice(0, n)[0]; return t ? cmd({ type: "upgrade", id: t.id }) : "done"; };
        const need = (cond, act) => (cond() ? act() : "done");
        const goals = [
          () => need(() => towers().length < 3, () => buildNext("tower")),
          () => need(() => camp.lv < 2, () => cmd({ type: "upgrade", id: camp.id })),
          () => need(() => !has("barracks"), () => place("barracks")),
          () => need(() => count("archer") < 2, () => cmd({ type: "hire", unit: "archer" })),
          () => need(() => count("swordsman") < 1, () => cmd({ type: "hire", unit: "swordsman" })),
          () => need(() => towers().some((t) => t.lv < 2), towerTo(2)),
          () => need(() => !has("infirmary"), () => place("infirmary")),
          () => need(() => count("medic") < 1, () => cmd({ type: "hire", unit: "medic" })),
          () => need(() => camp.lv < 3, () => cmd({ type: "upgrade", id: camp.id })),
          () => need(() => !has("workshop"), () => place("workshop")),
          () => need(() => st.research[1].unitWeapon < 2, () => cmd({ type: "research", key: "unitWeapon" })),
          () => need(() => count("archer") < 4, () => cmd({ type: "hire", unit: "archer" })),
          () => need(() => towers().some((t) => t.lv < 3), towerTo(3)),
          () => need(() => todo.some((t) => t.kind !== "tower"), () => buildNext("wall")),
          () => need(() => towers().length < 8, () => buildNext("tower")),
          () => need(() => st.research[1].heroWeapon < 3, () => cmd({ type: "research", key: "heroWeapon" })),
          () => need(() => camp.lv < 4, () => cmd({ type: "upgrade", id: camp.id })),
          () => need(() => st.research[1].unitArmor < 3, () => cmd({ type: "research", key: "unitArmor" })),
          () => need(() => count("swordsman") < 3, () => cmd({ type: "hire", unit: "swordsman" })),
          () => need(() => towers().some((t) => t.lv < 3), towerTo(3)),
          () => need(() => st.buildings.some((w) => (w.type === "wall" || w.type === "gate") && w.lv < Math.min(3, camp.lv)), () => { const w = st.buildings.find((x) => (x.type === "wall" || x.type === "gate") && x.lv < Math.min(3, camp.lv)); return cmd({ type: "upgrade", id: w.id }); }),
          () => need(() => camp.lv < 5, () => cmd({ type: "upgrade", id: camp.id })),
          () => need(() => st.research[1].unitWeapon < 5, () => cmd({ type: "research", key: "unitWeapon" })),
          () => need(() => count("archer") < 8, () => cmd({ type: "hire", unit: "archer" })),
        ];
        function buildNext(kind) {
          for (let k = 0; k < todo.length; k++) {
            const t = todo[k];
            if ((kind === "tower") !== (t.kind === "tower")) continue;
            const r = cmd({ type: "build", kind: t.kind, tx: t.x, ty: t.y });
            if (r === true) { todo.splice(k, 1); built++; return true; }
            if (r === "blocked" || r === "far") { todo.splice(k, 1); k--; continue; }
            if (r === "cost") return "cost";
          }
          return "done";
        }
        for (let n = 0; n < 4; n++) {
          let progressed = false;
          for (const [gi, g] of goals.entries()) {
            const r = g();
            if (process.env.DEBUG && i % 1200 === 0 && n === 0 && r !== "done") console.log("  goal", gi, "->", r, JSON.stringify(st.stock[1]), "campLv", camp.lv);
            if (r === "done" || r === "max" || r === "maxWorker" || r === "maxArmy" || r === "maxLv" || r === "needCamp" || r === "locked") continue;   // ทำตอนนี้ไม่ได้ ข้ามไปข้อถัดไป
            if (r === true) progressed = true;
            break;   // ข้อแรกที่ยังไม่เสร็จ: ทำได้ก็ทำ ไม่ได้ก็รอเก็บของ
          }
          if (!progressed) break;
        }
      }
      // ผู้เล่นเก่ง: สร้างป้อม 3 แรก แล้วเก็บของอัปเกรดก่อน ค่อยสร้างเพิ่มเมื่อมีค่ายทหารแล้ว
      const towersNow = st.buildings.filter((b) => b.type === "tower");
      const saving = SKILL >= 0.75 && towersNow.length >= 3 && (camp.lv < 2 || !has("barracks") || towersNow.some((t) => t.lv < Math.min(3, camp.lv)));
      const budget = SKILL >= 0.75 ? 0 : (builtToday[st.day] || 0) < 8 ? 1 : 0;
      const reserve = SKILL >= 0.75 && count("worker") < 4 ? 35 : SKILL >= 0.75 ? 25 : 0;
      for (let k = 0, n = 0; k < todo.length && n < budget; k++) {
        const t = todo[k];
        if (t.kind !== "tower" && st.stock[1].wood - 5 < reserve) continue;
        const r = cmd({ type: "build", kind: t.kind, tx: t.x, ty: t.y });
        if (r === true) { todo.splice(k, 1); k--; n++; built++; builtToday[st.day] = (builtToday[st.day] || 0) + 1; }
        else if (r === "blocked" || r === "far") { todo.splice(k, 1); k--; }
        else if (r === "cost" && t.kind !== "tower") break;
      }
      // Hero
      const dCamp = Math.hypot(h.x - st.camp.x, h.y - st.camp.y) / S;
      if (h.hp < h.maxHp * 0.4 && dCamp > 6) cmd({ type: "recall" });
      else if (night) { if (dCamp > 5 && !h.recall) cmd({ type: "moveTo", x: st.camp.x + (Math.random() - 0.5) * 120, y: st.camp.y + 70 }); }
      else if (!h.recall && h.hp > h.maxHp * 0.7) {
        const loot = st.loot.find((l) => Math.hypot(l.x - h.x, l.y - h.y) < 300);
        const range = 14 + h.lv * 1.5;
        const prey = st.monsters.filter((m) => !m.wave && Math.hypot(m.x - st.camp.x, m.y - st.camp.y) / S < range)
          .sort((a, b) => Math.hypot(a.x - h.x, a.y - h.y) - Math.hypot(b.x - h.x, b.y - h.y))[0];
        const tgt = loot || prey;
        if (tgt && (!h.path || i % 60 === 0)) cmd({ type: "moveTo", x: tgt.x, y: tgt.y });
      } else if (!h.recall && h.hp <= h.maxHp * 0.7 && dCamp > 3) cmd({ type: "moveTo", x: st.camp.x, y: st.camp.y + 80 });
      if (i % 40 === 0) cmd({ type: "skill" });
    }
    Core.step(st);
    if (process.env.DEBUG && i % 600 === 0) console.log(`t${i / 20}s day${st.day} ${JSON.stringify(st.stock[1])} units ${st.units.map((u) => u.job + (u.hidden ? "h" : "") + (u.wait ? "w" + u.wait : "")).join(",")} todo0 ${todo[0] && todo[0].kind}`);
    for (const e of st.events.splice(0)) {
      if (e.type === "death" && e.kind === "hero") deaths++;
      if (e.type === "bossDown") bosses++;
      if (e.type === "night") { nightReached = e.night; if (process.env.TRACE) { const cp = st.buildings.find((b) => b.type === "camp"); console.log(`  night ${e.night}: camp Lv${cp && cp.lv} towers ${st.buildings.filter((b) => b.type === "tower").map((b) => b.lv).join("")} walls ${st.buildings.filter((b) => b.type === "wall").length} units ${st.units.map((u) => u.type[0]).join("")} research ${Object.values(st.research[1]).join("")} stock ${JSON.stringify(st.stock[1])} heroLv ${h.lv}`); } }
      if (e.type === "trained") trained++;
      if (e.type === "death" && e.kind === "unit") workerDeaths++;
    }
  }
  const camp = st.buildings.find((b) => b.type === "camp");
  return { seed, campLv: camp ? camp.lv : 0, towers: st.buildings.filter((b) => b.type === "tower").map((b) => b.lv).join(""), units: st.units.map((u) => u.type[0]).join(""), research: Object.values(st.research[1]).join(""), result: st.result, night: nightReached, lv: h.lv, deaths, bosses, built, kills: st.kills[1] || 0,
    gear: [h.equip.weapon, h.equip.armor].map((x) => (x ? x.rarity[0] + x.ilv : "-")).join("/") };
}

const rows = [];
const t0 = Date.now();
for (let k = 1; k <= SEEDS; k++) rows.push(runSeed(Number(process.env.SEED || 0) || k * 104729));
for (const r of rows) console.log(JSON.stringify(r));
const wins = rows.filter((r) => r.result === "win").length;
console.log(`skill ${SKILL}: wins ${wins}/${rows.length}, avg night reached ${(rows.reduce((a, r) => a + r.night, 0) / rows.length).toFixed(1)}, avg lv ${(rows.reduce((a, r) => a + r.lv, 0) / rows.length).toFixed(1)}, avg deaths ${(rows.reduce((a, r) => a + r.deaths, 0) / rows.length).toFixed(1)}, ${((Date.now() - t0) / 1000).toFixed(0)}s`);
