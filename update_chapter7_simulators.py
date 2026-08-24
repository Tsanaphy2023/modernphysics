#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generates hyper-realistic, 60 FPS physics simulations for all 5 subtopics of Chapter 7 (Particle Physics):
- sim_7_1.html: Particle Zoo & Wilson Cloud Chamber (Carl Anderson Positron Track in Lead Plate)
- sim_7_2.html: The 4 Fundamental Forces & Animated Feynman Diagrams (Moller Scattering & Beta Decay)
- sim_7_3.html: The Standard Model Matrix & Interactive Hadron Builder (Proton uud, Neutron udd, Pions)
- sim_7_4.html: Particle Conservation Laws & Decay Checker (Charge, Baryon B, Lepton Numbers L_e, L_mu, Strangeness)
- sim_7_5.html: Chapter 7 Virtual Lab: Large Hadron Collider (LHC Detector & Higgs Boson 125 GeV Discovery Peak)
"""

import os

SIM_DIR = "/Users/chewathassana/Downloads/manus_backup2026/ModernPhysics/simulators"
os.makedirs(SIM_DIR, exist_ok=True)

COMMON_CSS = """
    * { box-sizing: border-box; margin: 0; padding: 0; }
    body {
      background: #020617;
      color: #f8fafc;
      font-family: 'Sarabun', -apple-system, sans-serif;
      margin: 0;
      padding: 6px;
      overflow-x: hidden;
    }
    .sim-card {
      background: #090e1a;
      border: 1px solid #1e293b;
      border-radius: 12px;
      padding: 14px;
      width: 100%;
      max-width: 100%;
      box-shadow: 0 4px 20px rgba(0, 0, 0, 0.5);
    }
    .sim-header {
      display: flex;
      justify-content: space-between;
      align-items: center;
      border-bottom: 1px solid #1e293b;
      padding-bottom: 8px;
      margin-bottom: 10px;
    }
    .sim-title {
      font-size: 0.98rem;
      font-weight: 700;
      color: #00f0ff;
      display: flex;
      align-items: center;
      gap: 8px;
    }
    .badge-fps {
      background: rgba(16, 185, 129, 0.15);
      border: 1px solid rgba(16, 185, 129, 0.4);
      color: #10b981;
      padding: 2px 7px;
      border-radius: 9999px;
      font-size: 0.70rem;
      font-weight: 700;
      font-family: 'JetBrains Mono', monospace;
    }
    .control-grid {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 10px;
      margin-bottom: 10px;
    }
    @media (max-width: 540px) {
      .control-grid { grid-template-columns: 1fr; }
    }
    .ctrl-box {
      background: #0f172a;
      border: 1px solid #1e293b;
      padding: 6px 10px;
      border-radius: 7px;
    }
    .ctrl-box label {
      display: block;
      font-size: 0.80rem;
      color: #94a3b8;
      margin-bottom: 3px;
    }
    .ctrl-box .val-display {
      color: #00f0ff;
      font-weight: 700;
      font-family: 'JetBrains Mono', monospace;
    }
    input[type=range] {
      width: 100%;
      accent-color: #00f0ff;
      cursor: pointer;
    }
    select {
      width: 100%;
      background: #090e1a;
      color: #00f0ff;
      border: 1px solid #334155;
      padding: 5px 8px;
      border-radius: 6px;
      font-size: 0.82rem;
      font-family: 'Sarabun', sans-serif;
    }
    .canvas-box {
      position: relative;
      width: 100%;
      background: #020617;
      border: 1px solid #1e293b;
      border-radius: 8px;
      overflow: hidden;
      margin-bottom: 10px;
    }
    canvas {
      display: block;
      width: 100%;
      height: 230px;
    }
    .readout-grid {
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 8px;
    }
    .readout-card {
      background: #0f172a;
      border: 1px solid #1e293b;
      border-radius: 7px;
      padding: 6px 8px;
      text-align: center;
    }
    .readout-val {
      font-size: 0.95rem;
      font-weight: 700;
      color: #00f0ff;
      font-family: 'JetBrains Mono', monospace;
      margin-bottom: 1px;
    }
    .readout-lbl {
      font-size: 0.68rem;
      color: #64748b;
    }
    .tab-bar {
      display: flex;
      gap: 6px;
      margin-bottom: 10px;
    }
    .tab-btn {
      flex: 1;
      background: #0f172a;
      border: 1px solid #1e293b;
      color: #94a3b8;
      padding: 5px 10px;
      border-radius: 6px;
      font-size: 0.80rem;
      font-weight: 600;
      cursor: pointer;
      font-family: 'Sarabun', sans-serif;
      transition: all 0.2s;
    }
    .tab-btn.active {
      background: rgba(0, 240, 255, 0.15);
      border-color: #00f0ff;
      color: #00f0ff;
    }
"""

def wrap_html(title, body_content, js_content):
    return """<!DOCTYPE html>
<html lang="th">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>""" + title + """</title>
  <link href="https://fonts.googleapis.com/css2?family=Sarabun:wght@400;600;700&family=JetBrains+Mono:wght@500;700&display=swap" rel="stylesheet">
  <style>""" + COMMON_CSS + """</style>
</head>
<body>
""" + body_content + """
  <script>
""" + js_content + """
  </script>
</body>
</html>
"""

# ==============================================================================
# 7.1 Particle Zoo & Wilson Cloud Chamber (Positron Discovery)
# ==============================================================================
body_7_1 = """
  <div class="sim-card">
    <div class="sim-header">
      <div class="sim-title"><span>🔬</span> 7.1 สวนสัตว์อนุภาค & ห้องหมอกวิลสัน (Cloud Chamber & Positron Discovery)</div>
      <div class="badge-fps">● 60 FPS REAL-TIME</div>
    </div>
    <div class="control-grid">
      <div class="ctrl-box">
        <label>อนุภาคที่วิ่งเข้าห้องหมอก (Incident Particle):</label>
        <select id="sel_part">
          <option value="positron" selected>โพซิตรอน Positron (e⁺ - ปฏิยานุภาคของอิเล็กตรอน)</option>
          <option value="electron">อิเล็กตรอน Electron (e⁻ - ประจุลบ)</option>
          <option value="muon">มิวออน Muon (µ⁻ - รังสีคอสมิกพลังงานสูง)</option>
          <option value="alpha">แอลฟา Alpha (⁴He - รอยทางหนาทึบ)</option>
        </select>
      </div>
      <div class="ctrl-box">
        <label>ความเข้มสนามแม่เหล็ก (B): <span id="val_b" class="val-display">1.5</span> เทสลา (พุ่งตั้งฉากเข้า)</label>
        <input type="range" id="slider_b" min="0.5" max="3.0" step="0.1" value="1.5">
      </div>
    </div>
    <div class="canvas-box"><canvas id="simCanvas" width="640" height="230"></canvas></div>
    <div class="readout-grid">
      <div class="readout-card"><div class="readout-val" id="val_radius">4.2 cm</div><div class="readout-lbl">รัศมีความโค้งก่อนผ่านแผ่นตะกั่ว (r₁)</div></div>
      <div class="readout-card"><div class="readout-val" id="val_radius2">2.1 cm</div><div class="readout-lbl">รัศมีความโค้งหลังผ่านตะกั่ว (r₂) เล็กลง!</div></div>
      <div class="readout-card"><div class="readout-val" id="val_dir_stat" style="color:#10b981;">เบนขวา (ประจุบวก +e)</div><div class="readout-lbl">การพิสูจน์ปฏิสสารของ Anderson (1932)</div></div>
    </div>
  </div>
"""

js_7_1 = """
    const cv = document.getElementById("simCanvas");
    const ctx = cv.getContext("2d");
    const selPart = document.getElementById("sel_part");
    const sliderB = document.getElementById("slider_b");
    let tick = 0;

    function animate() {
      const pType = selPart.value;
      const B = +sliderB.value;
      document.getElementById("val_b").textContent = B.toFixed(1);

      let q = +1, m = 1, col = "#00f0ff", pName = "Positron";
      if (pType === "electron") { q = -1; col = "#f43f5e"; pName = "Electron"; }
      else if (pType === "muon") { q = -1; m = 207; col = "#38bdf8"; pName = "Muon"; }
      else if (pType === "alpha") { q = +2; m = 7300; col = "#f59e0b"; pName = "Alpha"; }

      const r1 = (6.0 / B) * (m > 10 ? 3.0 : 1.0);
      const r2 = r1 * 0.5; // Loses momentum after passing through lead plate!

      document.getElementById("val_radius").textContent = r1.toFixed(1) + " cm";
      document.getElementById("val_radius2").textContent = r2.toFixed(1) + " cm";

      const dirEl = document.getElementById("val_dir_stat");
      if (q > 0) {
        dirEl.textContent = "เบนขวา (ประจุบวก +" + q + "e)"; dirEl.style.color = "#00f0ff";
      } else {
        dirEl.textContent = "เบนซ้าย (ประจุลบ " + q + "e)"; dirEl.style.color = "#f43f5e";
      }

      ctx.clearRect(0, 0, cv.width, cv.height);

      const cx = 320, cy = 115;

      // Cloud Chamber Chamber Rim (Circle)
      ctx.fillStyle = "#090e1a"; ctx.strokeStyle = "#1e293b"; ctx.lineWidth = 3;
      ctx.beginPath(); ctx.arc(cx, cy, 95, 0, Math.PI*2); ctx.fill(); ctx.stroke();

      // Magnetic field crosses
      ctx.fillStyle = "rgba(71, 85, 105, 0.4)"; ctx.font = "10px monospace";
      for(let r=0; 5 > r; r++) {
        for(let c=0; 7 > c; c++) {
          ctx.fillText("×", cx - 75 + c * 25, cy - 60 + r * 30);
        }
      }

      // Middle Lead Plate (Carl Anderson setup: 6 mm Lead)
      ctx.fillStyle = "#475569"; ctx.strokeStyle = "#94a3b8"; ctx.lineWidth = 1;
      ctx.fillRect(cx - 95, cy - 5, 190, 10); ctx.strokeRect(cx - 95, cy - 5, 190, 10);
      ctx.fillStyle = "#ffffff"; ctx.font = "9px sans-serif"; ctx.fillText("แผ่นตะกั่ว Lead Plate (6 mm)", cx - 60, cy + 3);

      // Trajectory of particle moving upward through lead plate
      // Region 1: Below lead plate (Faster, larger radius r1)
      ctx.strokeStyle = col; ctx.lineWidth = (pType === "alpha" ? 5 : 2.5);
      ctx.beginPath();
      const bend1 = q * (B / 1.5) * 45;
      ctx.moveTo(cx, cy + 90);
      ctx.quadraticCurveTo(cx + bend1*0.4, cy + 45, cx + bend1*0.6, cy + 5);
      ctx.stroke();

      // Region 2: Above lead plate (Slower after energy loss, tighter radius r2)
      const bend2 = q * (B / 1.5) * 85;
      ctx.beginPath();
      ctx.moveTo(cx + bend1*0.6, cy - 5);
      ctx.quadraticCurveTo(cx + bend1*0.6 + bend2*0.3, cy - 50, cx + bend2, cy - 90);
      ctx.stroke();

      // Animated vapor droplets along track
      const prog = (tick * 0.03) % 1;
      const vy = (cy + 90) - prog * 180;
      const vx = vy > cy ? cx + (bend1*0.6)*((cy+90-vy)/90) : cx + bend1*0.6 + (bend2 - bend1*0.6)*((cy-vy)/90);
      ctx.fillStyle = "#ffffff"; ctx.beginPath(); ctx.arc(vx, vy, 4, 0, Math.PI*2); ctx.fill();

      // Explanation banner
      ctx.fillStyle = "#94a3b8"; ctx.font = "11px sans-serif";
      ctx.fillText("รอยทางในห้องหมอก: รัศมีโค้งเล็กลงด้านบน พิสูจน์ว่าอนุภาคพุ่ง 'จากล่างขึ้นบน' และมีประจุบวก (โพซิตรอน)", 40, 215);

      tick++;
      requestAnimationFrame(animate);
    }
    animate();
"""

# ==============================================================================
# 7.2 The 4 Fundamental Forces & Feynman Diagrams
# ==============================================================================
body_7_2 = """
  <div class="sim-card">
    <div class="sim-header">
      <div class="sim-title"><span>🔬</span> 7.2 แรงพื้นฐานในธรรมชาติ & แผนภาพไฟน์แมน (Feynman Diagrams & Force Carriers)</div>
      <div class="badge-fps">● 60 FPS REAL-TIME</div>
    </div>
    <div class="control-grid">
      <div class="ctrl-box">
        <label>กระบวนการอันตรกิริยา (Interaction Process):</label>
        <select id="sel_process">
          <option value="em" selected>แรงแม่เหล็กไฟฟ้า: การกระเจิง e⁻-e⁻ (แลกเปลี่ยนโฟตอนเสมือน γ)</option>
          <option value="weak">แรงนิวเคลียร์อย่างอ่อน: การสลายบีตาลบ (d → u + W⁻ → e⁻ + ν̄ₑ)</option>
          <option value="strong">แรงนิวเคลียร์อย่างเข้ม: การแลกเปลี่ยนกลูออนระหว่างควาร์ก (q-q via Gluon g)</option>
        </select>
      </div>
      <div class="ctrl-box">
        <label>อนุภาคสื่อแรง (Gauge Boson Carrier):</label>
        <div id="val_boson" style="color:#00f0ff; font-weight:700; font-family:'JetBrains Mono', monospace; font-size:0.95rem; margin-top:4px;">Photon γ (m = 0, Spin = 1)</div>
      </div>
    </div>
    <div class="canvas-box"><canvas id="simCanvas" width="640" height="230"></canvas></div>
    <div class="readout-grid">
      <div class="readout-card"><div class="readout-val" id="val_rel_strength">10⁻² (EM)</div><div class="readout-lbl">ความแรงสัมพัทธ์ของแรง</div></div>
      <div class="readout-card"><div class="readout-val" id="val_range">อนันต์ (Infinite)</div><div class="readout-lbl">ระยะการออกแรง (Range)</div></div>
      <div class="readout-card"><div class="readout-val" id="val_vertex_stat" style="color:#10b981;">อนุรักษ์โมเมนตัม 4 มิติ 100%</div><div class="readout-lbl">กฎการอนุรักษ์ที่จุดยอด (Vertex)</div></div>
    </div>
  </div>
"""

js_7_2 = """
    const cv = document.getElementById("simCanvas");
    const ctx = cv.getContext("2d");
    const selProc = document.getElementById("sel_process");
    let tick = 0;

    function animate() {
      const proc = selProc.value;
      const bEl = document.getElementById("val_boson");

      if (proc === "em") {
        bEl.textContent = "Photon γ (โฟตอน: มวล 0, สปิน 1)";
        document.getElementById("val_rel_strength").textContent = "10⁻² (EM)";
        document.getElementById("val_range").textContent = "อนันต์ (Infinite)";
      } else if (proc === "weak") {
        bEl.textContent = "W⁻ Boson (มวล 80.4 GeV, สปิน 1)";
        document.getElementById("val_rel_strength").textContent = "10⁻⁷ (Weak)";
        document.getElementById("val_range").textContent = "10⁻¹⁸ m (Sub-nuclear)";
      } else {
        bEl.textContent = "Gluon g (กลูออน: 8 Color Charges)";
        document.getElementById("val_rel_strength").textContent = "1.0 (Strong)";
        document.getElementById("val_range").textContent = "10⁻¹⁵ m (Femtometer)";
      }

      ctx.clearRect(0, 0, cv.width, cv.height);

      const cx = 320, cy = 115;

      // Coordinate time-space directions
      ctx.fillStyle = "#64748b"; ctx.font = "10px sans-serif";
      ctx.fillText("เวลา (Time t) →", 530, 215);
      ctx.fillText("↑ ตำแหน่ง (Space x)", 20, 30);

      const v1x = cx - 70, v1y = cy;
      const v2x = cx + 70, v2y = cy;

      if (proc === "em") {
        // Moller Scattering: e- + e- -> e- + e- via virtual photon
        // Incoming electron 1 (top-left) & 2 (bottom-left)
        ctx.strokeStyle = "#38bdf8"; ctx.lineWidth = 2.5;
        ctx.beginPath(); ctx.moveTo(cx - 190, cy - 65); ctx.lineTo(v1x, cy - 35); ctx.stroke();
        ctx.beginPath(); ctx.moveTo(cx - 190, cy + 65); ctx.lineTo(v1x, cy + 35); ctx.stroke();
        ctx.fillStyle = "#38bdf8"; ctx.font = "bold 11px sans-serif";
        ctx.fillText("e⁻ (in)", cx - 215, cy - 65); ctx.fillText("e⁻ (in)", cx - 215, cy + 70);

        // Virtual Photon wavy line between vertices
        ctx.strokeStyle = "#f59e0b"; ctx.lineWidth = 2.5;
        ctx.beginPath();
        for(let y = -35; 35 >= y; y += 2) {
          const wave = 7 * Math.sin(y * 0.25 + tick*0.1);
          const px = v1x + wave;
          if (y === -35) ctx.moveTo(px, cy + y); else ctx.lineTo(px, cy + y);
        }
        ctx.stroke();
        ctx.fillStyle = "#f59e0b"; ctx.fillText("Virtual Photon γ", v1x + 15, cy + 4);

        // Outgoing electrons
        ctx.strokeStyle = "#38bdf8"; ctx.lineWidth = 2.5;
        ctx.beginPath(); ctx.moveTo(v1x, cy - 35); ctx.lineTo(cx + 170, cy - 75); ctx.stroke();
        ctx.beginPath(); ctx.moveTo(v1x, cy + 35); ctx.lineTo(cx + 170, cy + 75); ctx.stroke();
        ctx.fillText("e⁻ (out)", cx + 180, cy - 75); ctx.fillText("e⁻ (out)", cx + 180, cy + 80);
      }
      else if (proc === "weak") {
        // Beta Decay: d -> u + W- -> e- + nu_bar
        // Incoming d quark
        ctx.strokeStyle = "#10b981"; ctx.lineWidth = 2.5;
        ctx.beginPath(); ctx.moveTo(cx - 180, cy); ctx.lineTo(v1x, cy); ctx.stroke();
        ctx.fillStyle = "#10b981"; ctx.font = "bold 11px sans-serif"; ctx.fillText("d quark (นิวตรอน)", cx - 220, cy - 8);

        // Outgoing u quark
        ctx.beginPath(); ctx.moveTo(v1x, cy); ctx.lineTo(cx - 30, cy - 70); ctx.stroke();
        ctx.fillText("u quark (โปรตอน)", cx - 25, cy - 75);

        // Propagating W- Boson (Wavy)
        ctx.strokeStyle = "#f43f5e"; ctx.lineWidth = 2.5;
        ctx.beginPath();
        for(let s = 0; 120 >= s; s += 2) {
          const px = v1x + s;
          const py = cy + s * 0.2 + 6 * Math.sin(s * 0.25 - tick*0.1);
          if (s === 0) ctx.moveTo(px, py); else ctx.lineTo(px, py);
        }
        ctx.stroke();
        ctx.fillStyle = "#f43f5e"; ctx.fillText("W⁻ Boson", v1x + 35, cy + 30);

        // W- decays into e- and nu_e_bar
        const wEnd_x = v1x + 120, wEnd_y = cy + 24;
        ctx.strokeStyle = "#38bdf8"; ctx.lineWidth = 2.5;
        ctx.beginPath(); ctx.moveTo(wEnd_x, wEnd_y); ctx.lineTo(cx + 180, cy - 30); ctx.stroke();
        ctx.fillText("e⁻ (อิเล็กตรอน)", cx + 190, cy - 30);

        ctx.strokeStyle = "#a855f7"; ctx.lineWidth = 2.5; ctx.setLineDash([3, 3]);
        ctx.beginPath(); ctx.moveTo(wEnd_x, wEnd_y); ctx.lineTo(cx + 180, cy + 70); ctx.stroke(); ctx.setLineDash([]);
        ctx.fillStyle = "#a855f7"; ctx.fillText("ν̄ₑ (แอนตินิวทริโน)", cx + 190, cy + 75);
      }
      else {
        // Strong Force: Quark-Quark Gluon Exchange
        ctx.strokeStyle = "#f59e0b"; ctx.lineWidth = 2.5;
        ctx.beginPath(); ctx.moveTo(cx - 180, cy - 50); ctx.lineTo(v1x, cy - 50); ctx.lineTo(cx + 170, cy - 50); ctx.stroke();
        ctx.beginPath(); ctx.moveTo(cx - 180, cy + 50); ctx.lineTo(v1x, cy + 50); ctx.lineTo(cx + 170, cy + 50); ctx.stroke();

        // Gluon Spring / Helix
        ctx.strokeStyle = "#00f0ff"; ctx.lineWidth = 2.5;
        ctx.beginPath();
        for(let y = -50; 50 >= y; y += 2) {
          const coil = 9 * Math.sin(y * 0.4 + tick*0.15);
          const px = v1x + coil;
          if (y === -50) ctx.moveTo(px, cy + y); else ctx.lineTo(px, cy + y);
        }
        ctx.stroke();
        ctx.fillStyle = "#00f0ff"; ctx.font = "bold 11px sans-serif";
        ctx.fillText("Gluon g (สปริงนิวเคลียร์)", v1x + 20, cy + 4);
      }

      tick++;
      requestAnimationFrame(animate);
    }
    animate();
"""

# ==============================================================================
# 7.3 The Standard Model Matrix & Hadron Builder
# ==============================================================================
body_7_3 = """
  <div class="sim-card">
    <div class="sim-header">
      <div class="sim-title"><span>🔬</span> 7.3 แบบจำลองมาตรฐาน & เครื่องมือสร้างฮาดรอน (Standard Model Matrix & Hadron Builder)</div>
      <div class="badge-fps">● 60 FPS REAL-TIME</div>
    </div>
    <div class="control-grid">
      <div class="ctrl-box">
        <label>เลือกฮาดรอนเป้าหมาย (Hadron Composition):</label>
        <select id="sel_hadron">
          <option value="proton" selected>โปรตอน Proton (u + u + d → บาริออน Q = +1)</option>
          <option value="neutron">นิวตรอน Neutron (u + d + d → บาริออน Q = 0)</option>
          <option value="pion_plus">ไพออนบวก Pi-Plus π⁺ (u + d̄ → มีซอน Q = +1)</option>
          <option value="delta_plus_plus">เดลตา-พลัสพลัส Δ⁺⁺ (u + u + u → บาริออน Q = +2)</option>
        </select>
      </div>
      <div class="ctrl-box">
        <label>ประเภทฮาดรอน (Hadron Family): <span id="val_family" class="val-display">Baryon (3 Quarks)</span></label>
        <div style="color:#94a3b8; font-size:0.80rem; margin-top:4px;">ยึดเหนี่ยวด้วยแรงนิวเคลียร์อย่างเข้มและประจุสี (Color Charge)</div>
      </div>
    </div>
    <div class="canvas-box"><canvas id="simCanvas" width="640" height="230"></canvas></div>
    <div class="readout-grid">
      <div class="readout-card"><div class="readout-val" id="val_tot_charge">+1 e</div><div class="readout-lbl">ประจุไฟฟ้ารวม (Total Charge Q)</div></div>
      <div class="readout-card"><div class="readout-val" id="val_baryon_num">B = 1</div><div class="readout-lbl">เลขบาริออน (Baryon Number)</div></div>
      <div class="readout-card"><div class="readout-val" id="val_color_sum" style="color:#10b981;">ขาว/ไร้สี (White Color Singlet)</div><div class="readout-lbl">สภาวะจำกัดขังควาร์ก (Confinement)</div></div>
    </div>
  </div>
"""

js_7_3 = """
    const cv = document.getElementById("simCanvas");
    const ctx = cv.getContext("2d");
    const selHad = document.getElementById("sel_hadron");
    let tick = 0;

    const hadronInfo = {
      proton: { name: "Proton p (uud)", fam: "Baryon (3 Quarks)", Q: "+1 e", B: "B = 1", quarks: [{name:"u", q:"+⅔", col:"#f43f5e"}, {name:"u", q:"+⅔", col:"#10b981"}, {name:"d", q:"-⅓", col:"#38bdf8"}] },
      neutron: { name: "Neutron n (udd)", fam: "Baryon (3 Quarks)", Q: "0 e", B: "B = 1", quarks: [{name:"u", q:"+⅔", col:"#f43f5e"}, {name:"d", q:"-⅓", col:"#10b981"}, {name:"d", q:"-⅓", col:"#38bdf8"}] },
      pion_plus: { name: "Pion π⁺ (ud̄)", fam: "Meson (Quark + Antiquark)", Q: "+1 e", B: "B = 0", quarks: [{name:"u", q:"+⅔", col:"#f43f5e"}, {name:"d̄", q:"+⅓", col:"#38bdf8"}] },
      delta_plus_plus: { name: "Delta Δ⁺⁺ (uuu)", fam: "Baryon (3 Quarks)", Q: "+2 e", B: "B = 1", quarks: [{name:"u", q:"+⅔", col:"#f43f5e"}, {name:"u", q:"+⅔", col:"#10b981"}, {name:"u", q:"+⅔", col:"#38bdf8"}] }
    };

    function animate() {
      const hType = selHad.value;
      const h = hadronInfo[hType];

      document.getElementById("val_family").textContent = h.fam;
      document.getElementById("val_tot_charge").textContent = h.Q;
      document.getElementById("val_baryon_num").textContent = h.B;

      ctx.clearRect(0, 0, cv.width, cv.height);

      const cx = 320, cy = 115;

      // Hadron Confinement Bag (Glowing circle)
      const bagR = 75 + Math.sin(tick*0.06)*3;
      const bagGrad = ctx.createRadialGradient(cx, cy, 5, cx, cy, bagR);
      bagGrad.addColorStop(0, "rgba(255, 255, 255, 0.15)");
      bagGrad.addColorStop(0.7, "rgba(0, 240, 255, 0.1)");
      bagGrad.addColorStop(1, "transparent");
      ctx.fillStyle = bagGrad;
      ctx.beginPath(); ctx.arc(cx, cy, bagR, 0, Math.PI*2); ctx.fill();

      ctx.strokeStyle = "rgba(0, 240, 255, 0.5)"; ctx.lineWidth = 1.5; ctx.setLineDash([4, 4]);
      ctx.beginPath(); ctx.arc(cx, cy, bagR, 0, Math.PI*2); ctx.stroke(); ctx.setLineDash([]);

      // Gluon strings connecting quarks (Inter-quark flux tubes)
      const qCount = h.quarks.length;
      let qPos = [];
      for(let i=0; qCount > i; i++) {
        const ang = (i * 2 * Math.PI / qCount) + tick*0.03;
        const qx = cx + 42 * Math.cos(ang);
        const qy = cy + 42 * Math.sin(ang);
        qPos.push({ x: qx, y: qy });
      }

      // Draw Gluon Springs between all quark pairs
      ctx.strokeStyle = "#f59e0b"; ctx.lineWidth = 2.0;
      for(let i=0; qCount > i; i++) {
        for(let j=i+1; qCount > j; j++) {
          ctx.beginPath();
          const p1 = qPos[i], p2 = qPos[j];
          const midX = (p1.x + p2.x)/2 + Math.sin(tick*0.1 + i)*8;
          const midY = (p1.y + p2.y)/2 + Math.cos(tick*0.1 + i)*8;
          ctx.moveTo(p1.x, p1.y); ctx.quadraticCurveTo(midX, midY, p2.x, p2.y); ctx.stroke();
        }
      }

      // Draw Quarks
      h.quarks.forEach((qk, idx) => {
        const p = qPos[idx];
        ctx.fillStyle = qk.col;
        ctx.beginPath(); ctx.arc(p.x, p.y, 14, 0, Math.PI*2); ctx.fill();
        ctx.strokeStyle = "#ffffff"; ctx.lineWidth = 2; ctx.stroke();

        ctx.fillStyle = "#ffffff"; ctx.font = "bold 11px sans-serif";
        ctx.fillText(qk.name, p.x - 4, p.y + 4);

        ctx.fillStyle = "#020617"; ctx.font = "9px 'JetBrains Mono', monospace";
        ctx.fillText(qk.q, p.x - 6, p.y + 24);
      });

      // Name & Title
      ctx.fillStyle = "#ffffff"; ctx.font = "bold 12px sans-serif";
      ctx.fillText(h.name, cx - 50, 30);

      tick++;
      requestAnimationFrame(animate);
    }
    animate();
"""

# ==============================================================================
# 7.4 Particle Conservation Laws & Decay Checker
# ==============================================================================
body_7_4 = """
  <div class="sim-card">
    <div class="sim-header">
      <div class="sim-title"><span>🔬</span> 7.4 กฎการอนุรักษ์ในฟิสิกส์อนุภาค (Particle Conservation Laws & Decay Validator)</div>
      <div class="badge-fps">● 60 FPS REAL-TIME</div>
    </div>
    <div class="control-grid">
      <div class="ctrl-box">
        <label>เลือกสมการกระบวนการสลายตัว (Decay / Reaction):</label>
        <select id="sel_decay">
          <option value="beta_decay" selected>n → p + e⁻ + ν̄ₑ (Beta Decay - เกิดขึ้นได้จริง)</option>
          <option value="pion_decay">π⁺ → µ⁺ + ν_µ (Pion Decay - อนุรักษ์เลปตอน)</option>
          <option value="proton_decay">p → e⁺ + π⁰ (Proton Decay - ต้องห้าม! ขัดกฎ B)</option>
          <option value="muon_wrong">µ⁻ → e⁻ + γ (Muon Decay - ต้องห้าม! ขัดกฎ L_e, L_µ)</option>
        </select>
      </div>
      <div class="ctrl-box">
        <label>ผลการตรวจสอบความถูกต้อง (Validator Status):</label>
        <div id="val_verdict" style="color:#10b981; font-weight:700; font-size:0.95rem; margin-top:4px;">✓ เกิดขึ้นได้จริงตามธรรมชาติ (Allowed via Weak)</div>
      </div>
    </div>
    <div class="canvas-box"><canvas id="simCanvas" width="640" height="230"></canvas></div>
    <div class="readout-grid">
      <div class="readout-card"><div class="readout-val" id="val_dq">ΔQ = 0 (อนุรักษ์)</div><div class="readout-lbl">ประจุไฟฟ้า (Electric Charge Q)</div></div>
      <div class="readout-card"><div class="readout-val" id="val_db">ΔB = 0 (อนุรักษ์)</div><div class="readout-lbl">เลขบาริออน (Baryon Number B)</div></div>
      <div class="readout-card"><div class="readout-val" id="val_dl">ΔL = 0 (อนุรักษ์)</div><div class="readout-lbl">เลขเลปตอน (Lepton Family Numbers)</div></div>
    </div>
  </div>
"""

js_7_4 = """
    const cv = document.getElementById("simCanvas");
    const ctx = cv.getContext("2d");
    const selDec = document.getElementById("sel_decay");
    let tick = 0;

    const decayRules = {
      beta_decay: {
        name: "n → p + e⁻ + ν̄ₑ",
        allowed: true, reason: "✓ เกิดขึ้นได้จริงตามธรรมชาติ (Allowed via Weak Interaction)",
        Q: "ΔQ = 0 (0 = +1 - 1 + 0)", B: "ΔB = 0 (1 = 1 + 0 + 0)", L: "ΔL_e = 0 (0 = 0 + 1 - 1)"
      },
      pion_decay: {
        name: "π⁺ → µ⁺ + ν_µ",
        allowed: true, reason: "✓ เกิดขึ้นได้จริงตามธรรมชาติ (Allowed via Weak Interaction)",
        Q: "ΔQ = 0 (+1 = +1 + 0)", B: "ΔB = 0 (0 = 0 + 0)", L: "ΔL_µ = 0 (0 = -1 + 1)"
      },
      proton_decay: {
        name: "p → e⁺ + π⁰",
        allowed: false, reason: "✗ ต้องห้าม! ละเมิดกฎการอนุรักษ์เลขบาริออน (ΔB = 1 ≠ 0)",
        Q: "ΔQ = 0 (+1 = +1 + 0)", B: "ΔB ≠ 0 (1 → 0 ขัดกฎ!)", L: "ΔL_e ≠ 0 (0 → -1 ขัดกฎ!)"
      },
      muon_wrong: {
        name: "µ⁻ → e⁻ + γ",
        allowed: false, reason: "✗ ต้องห้าม! ละเมิดการอนุรักษ์เลขเลปตอนแต่ละตระกูล (ΔL_e ≠ 0, ΔL_µ ≠ 0)",
        Q: "ΔQ = 0 (-1 = -1 + 0)", B: "ΔB = 0 (0 = 0 + 0)", L: "ΔL_µ ≠ 0 & ΔL_e ≠ 0 (ขัดกฎ!)"
      }
    };

    function animate() {
      const code = selDec.value;
      const d = decayRules[code];

      const verdEl = document.getElementById("val_verdict");
      verdEl.textContent = d.reason;
      verdEl.style.color = d.allowed ? "#10b981" : "#f43f5e";

      document.getElementById("val_dq").textContent = d.Q;
      document.getElementById("val_db").textContent = d.B;
      document.getElementById("val_dl").textContent = d.L;

      ctx.clearRect(0, 0, cv.width, cv.height);

      // Ledger Table Box
      const tx = 60, ty = 25, tw = 520, th = 175;
      ctx.fillStyle = "#0f172a"; ctx.strokeStyle = d.allowed ? "#10b981" : "#f43f5e"; ctx.lineWidth = 2;
      ctx.fillRect(tx, ty, tw, th); ctx.strokeRect(tx, ty, tw, th);

      ctx.fillStyle = "#ffffff"; ctx.font = "bold 13px 'JetBrains Mono', monospace";
      ctx.fillText("สมการ: " + d.name, tx + 20, ty + 30);

      // Table rows
      ctx.strokeStyle = "#334155"; ctx.lineWidth = 1;
      ctx.beginPath(); ctx.moveTo(tx + 20, ty + 45); ctx.lineTo(tx + tw - 20, ty + 45); ctx.stroke();

      ctx.fillStyle = "#94a3b8"; ctx.font = "11px sans-serif";
      ctx.fillText("กฎการอนุรักษ์ (Conservation Law)", tx + 25, ty + 65);
      ctx.fillText("สถานะการตรวจสอบ (Status)", tx + 330, ty + 65);

      ctx.fillStyle = "#f8fafc"; ctx.font = "11px 'JetBrains Mono', monospace";
      ctx.fillText("1. ประจุไฟฟ้า (Electric Charge Q)", tx + 25, ty + 95);
      ctx.fillStyle = "#10b981"; ctx.fillText("✓ ผ่าน (Conserved)", tx + 330, ty + 95);

      ctx.fillStyle = "#f8fafc";
      ctx.fillText("2. เลขบาริออน (Baryon Number B)", tx + 25, ty + 122);
      ctx.fillStyle = d.B.includes("ขัดกฎ") ? "#f43f5e" : "#10b981";
      ctx.fillText(d.B.includes("ขัดกฎ") ? "✗ ละเมิดกฎ (Violated)" : "✓ ผ่าน (Conserved)", tx + 330, ty + 122);

      ctx.fillStyle = "#f8fafc";
      ctx.fillText("3. เลขเลปตอน (Lepton Numbers L)", tx + 25, ty + 149);
      ctx.fillStyle = d.L.includes("ขัดกฎ") ? "#f43f5e" : "#10b981";
      ctx.fillText(d.L.includes("ขัดกฎ") ? "✗ ละเมิดกฎ (Violated)" : "✓ ผ่าน (Conserved)", tx + 330, ty + 149);

      tick++;
      requestAnimationFrame(animate);
    }
    animate();
"""

# ==============================================================================
# 7.5 Virtual Lab: Large Hadron Collider & Higgs Discovery
# ==============================================================================
body_7_5 = """
  <div class="sim-card">
    <div class="sim-header">
      <div class="sim-title"><span>🔬</span> 7.5 ปฏิบัติการชนอนุภาค LHC & การค้นพบฮิกส์โบซอน (Higgs Boson Discovery Lab)</div>
      <div class="badge-fps">● 60 FPS REAL-TIME</div>
    </div>
    <div class="tab-bar">
      <button class="tab-btn active" id="tabLHC" onclick="setMode('lhc')">💥 การชนกันของโปรตอนใน LHC (13.6 TeV Collision)</button>
      <button class="tab-btn" id="tabHiggs" onclick="setMode('higgs')">📊 สเปกตรัมการค้นพบฮิกส์ 125 GeV (Diphoton Peak)</button>
    </div>
    <div id="controlsLHC" class="control-grid">
      <div class="ctrl-box">
        <label>พลังงานจุดศูนย์กลางมวล (Center-of-Mass Energy): <span id="val_lhc_e" class="val-display">13.6</span> TeV</label>
        <input type="range" id="slider_lhc_e" min="7.0" max="14.0" step="0.2" value="13.6">
      </div>
      <div class="ctrl-box">
        <button type="button" onclick="triggerCollision()" style="background:linear-gradient(135deg, #f43f5e, #dc2626); color:#fff; border:none; padding:8px 16px; border-radius:6px; font-weight:700; cursor:pointer; font-family:'Sarabun', sans-serif; margin-top:8px;">💥 ยิงโปรตอนชนกัน (Collide Protons!)</button>
      </div>
    </div>
    <div id="controlsHiggs" class="control-grid" style="display:none;">
      <div class="ctrl-box">
        <label>ช่องทางการสลายตัวของฮิกส์: H → γ + γ (Diphoton Decay)</label>
        <div style="color:#94a3b8; font-size:0.80rem; margin-top:4px;">มวลนิ่งของฮิกส์โบซอน m_H = 125.09 GeV/c² (ระดับนัยสำคัญ 5σ)</div>
      </div>
      <div class="ctrl-box">
        <label>ความส่องสว่างสะสม (Integrated Luminosity): 140 fb⁻¹</label>
        <div style="color:#10b981; font-size:0.80rem; margin-top:4px;">รางวัลโนเบลฟิสิกส์ 2013 (Englert & Higgs)</div>
      </div>
    </div>
    <div class="canvas-box"><canvas id="simCanvas" width="640" height="230"></canvas></div>
    <div class="readout-grid" id="readoutsLHC">
      <div class="readout-card"><div class="readout-val" id="val_coll_tracks">48 อนุภาคย่อย</div><div class="readout-lbl">รอยทางอนุภาคที่ตรวจจับได้</div></div>
      <div class="readout-card"><div class="readout-val" id="val_mag_tesla">8.33 T</div><div class="readout-lbl">สนามแม่เหล็กตัวนำยิ่งยวด (Superconducting B)</div></div>
      <div class="readout-card"><div class="readout-val" id="val_lhc_stat" style="color:#10b981;">Beam Injected 60 FPS</div><div class="readout-lbl">สถานะเครื่องเร่งอนุภาค</div></div>
    </div>
    <div class="readout-grid" id="readoutsHiggs" style="display:none;">
      <div class="readout-card"><div class="readout-val" id="val_higgs_mass">125.09 GeV</div><div class="readout-lbl">มวลฮิกส์โบซอน (Higgs Mass Peak)</div></div>
      <div class="readout-card"><div class="readout-val" id="val_sigma_stat">5.9 σ (Gold Discovery)</div><div class="readout-lbl">ระดับนัยสำคัญทางสถิติ</div></div>
      <div class="readout-card"><div class="readout-val" id="val_higgs_field" style="color:#00f0ff;">ให้มวลแก่อนุภาคมูลฐาน</div><div class="readout-lbl">กลไกสนามฮิกส์ (Higgs Mechanism)</div></div>
    </div>
  </div>
"""

js_7_5 = """
    const cv = document.getElementById("simCanvas");
    const ctx = cv.getContext("2d");
    let currentMode = "lhc";
    let tick = 0;
    let collParticles = [];
    let isBoom = false;

    function setMode(mode) {
      currentMode = mode;
      document.getElementById("tabLHC").classList.toggle("active", mode === "lhc");
      document.getElementById("tabHiggs").classList.toggle("active", mode === "higgs");
      document.getElementById("controlsLHC").style.display = mode === "lhc" ? "grid" : "none";
      document.getElementById("controlsHiggs").style.display = mode === "higgs" ? "grid" : "none";
      document.getElementById("readoutsLHC").style.display = mode === "lhc" ? "grid" : "none";
      document.getElementById("readoutsHiggs").style.display = mode === "higgs" ? "grid" : "none";
    }

    function triggerCollision() {
      collParticles = [];
      for(let i=0; 50 > i; i++) {
        const ang = Math.random() * Math.PI * 2;
        const spd = 2.0 + Math.random() * 6.5;
        const col = i % 4 === 0 ? "#f43f5e" : (i % 4 === 1 ? "#00f0ff" : (i % 4 === 2 ? "#f59e0b" : "#10b981"));
        collParticles.push({ x: 320, y: 115, vx: Math.cos(ang)*spd, vy: Math.sin(ang)*spd, col: col });
      }
      isBoom = true;
    }

    function animate() {
      ctx.clearRect(0, 0, cv.width, cv.height);

      if (currentMode === "lhc") {
        const cx = 320, cy = 115;

        // Concentric Detector Cylinders (Tracker, ECAL, HCAL, Muon Chambers)
        const layers = [
          { r: 35, col: "rgba(56, 189, 248, 0.25)", name: "Tracker" },
          { r: 65, col: "rgba(16, 185, 129, 0.20)", name: "ECAL" },
          { r: 90, col: "rgba(245, 158, 11, 0.15)", name: "HCAL" },
          { r: 105, col: "rgba(239, 68, 68, 0.15)", name: "Muon" }
        ];

        layers.reverse().forEach(l => {
          ctx.fillStyle = l.col; ctx.strokeStyle = "#334155"; ctx.lineWidth = 1;
          ctx.beginPath(); ctx.arc(cx, cy, l.r, 0, Math.PI*2); ctx.fill(); ctx.stroke();
        });

        // Incoming Proton Beams along horizontal axis
        const beamProg = (tick * 6) % 150;
        ctx.fillStyle = "#f43f5e"; ctx.beginPath(); ctx.arc(cx - 150 + beamProg, cy, 4.5, 0, Math.PI*2); ctx.fill();
        ctx.fillStyle = "#00f0ff"; ctx.beginPath(); ctx.arc(cx + 150 - beamProg, cy, 4.5, 0, Math.PI*2); ctx.fill();

        // Particle Spray on collision
        if (collParticles.length > 0) {
          collParticles.forEach(p => {
            ctx.fillStyle = p.col; ctx.strokeStyle = p.col; ctx.lineWidth = 1.8;
            ctx.beginPath(); ctx.moveTo(320, 115); ctx.lineTo(p.x, p.y); ctx.stroke();
            ctx.beginPath(); ctx.arc(p.x, p.y, 3, 0, Math.PI*2); ctx.fill();
            p.x += p.vx; p.y += p.vy;
          });
        }

        ctx.fillStyle = "#ffffff"; ctx.font = "bold 11px sans-serif";
        ctx.fillText("LHC ATLAS / CMS Detector Simulation (13.6 TeV)", cx - 135, 20);
      }
      else {
        // Higgs 125 GeV Discovery Peak Histogram
        const ox = 100, oy = 185, gw = 450, gh = 150;

        ctx.strokeStyle = "#475569"; ctx.lineWidth = 1.5;
        ctx.beginPath(); ctx.moveTo(ox, oy); ctx.lineTo(ox + gw, oy); ctx.stroke(); // Mass axis
        ctx.beginPath(); ctx.moveTo(ox, oy); ctx.lineTo(ox, oy - gh); ctx.stroke(); // Events axis

        ctx.fillStyle = "#94a3b8"; ctx.font = "10px sans-serif";
        ctx.fillText("มวลไม่แปรเปลี่ยนของโฟตอนคู่ m_γγ (GeV) → (100 to 160 GeV)", ox + gw - 220, oy + 16);
        ctx.fillText("จำนวนคู่โฟตอน N", ox - 10, oy - gh - 6);

        // Smooth decaying background + Gaussian Peak at 125 GeV
        ctx.strokeStyle = "#f43f5e"; ctx.lineWidth = 2.5;
        ctx.beginPath();
        for(let m = 100; 160 >= m; m += 0.5) {
          const px = ox + ((m - 100) / 60) * gw;
          // Background decay
          const bg = 80 * Math.exp(-(m - 100) * 0.035);
          // Higgs Peak at 125 GeV
          const peak = 45 * Math.exp(-Math.pow(m - 125.0, 2) / (2 * 1.8 * 1.8));
          const py = oy - ((bg + peak) / 100) * gh;
          if (m === 100) ctx.moveTo(px, py); else ctx.lineTo(px, py);
        }
        ctx.stroke();

        // 125 GeV Marker
        const hX = ox + ((125.09 - 100) / 60) * gw;
        const hY = oy - ((80 * Math.exp(-25*0.035) + 45) / 100) * gh;
        ctx.strokeStyle = "#00f0ff"; ctx.lineWidth = 1.5; ctx.setLineDash([3, 3]);
        ctx.beginPath(); ctx.moveTo(hX, oy); ctx.lineTo(hX, hY); ctx.stroke(); ctx.setLineDash([]);

        ctx.fillStyle = "#00f0ff"; ctx.font = "bold 11px sans-serif";
        ctx.beginPath(); ctx.arc(hX, hY, 5, 0, Math.PI*2); ctx.fill();
        ctx.fillText("★ Higgs Peak (125.09 GeV, 5σ Discovery)", hX - 70, hY - 12);
      }

      tick++;
      requestAnimationFrame(animate);
    }
    animate();
"""

files = {
    "sim_7_1.html": wrap_html("7.1 สวนสัตว์อนุภาค & ห้องหมอกวิลสัน", body_7_1, js_7_1),
    "sim_7_2.html": wrap_html("7.2 แรงพื้นฐาน & แผนภาพไฟน์แมน", body_7_2, js_7_2),
    "sim_7_3.html": wrap_html("7.3 แบบจำลองมาตรฐาน & ควาร์ก", body_7_3, js_7_3),
    "sim_7_4.html": wrap_html("7.4 กฎการอนุรักษ์ในฟิสิกส์อนุภาค", body_7_4, js_7_4),
    "sim_7_5.html": wrap_html("7.5 ปฏิบัติการชนอนุภาค LHC & ฮิกส์โบซอน", body_7_5, js_7_5)
}

for fname, content in files.items():
    fpath = os.path.join(SIM_DIR, fname)
    with open(fpath, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"✅ Generated {fpath} ({len(content)} bytes)")

print("🎉 Successfully upgraded all Chapter 7 simulations to hyper-realistic 60 FPS engines!")
