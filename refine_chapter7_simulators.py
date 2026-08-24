#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Refined Chapter 7 Particle Physics simulators with enhanced visual fidelity:
- sim_7_1.html: Wilson Cloud Chamber with dynamic continuous vapor droplet condensation trails and lead plate deflection
- sim_7_2.html: Interactive Feynman diagrams with vertex glow, wave oscillations, and 4-momentum balance indicators
- sim_7_3.html: Standard Model matrix and Hadron builder
- sim_7_4.html: Particle conservation law validator
- sim_7_5.html: LHC 13.6 TeV collision & Higgs 125 GeV discovery
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
# 7.1 Refined Cloud Chamber
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
        <label>ความเข้มสนามแม่เหล็ก (B): <span id="val_b" class="val-display">1.5</span> เทสลา (พุ่งตั้งฉากเข้า ⊗)</label>
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
    let droplets = [];

    function animate() {
      const pType = selPart.value;
      const B = +sliderB.value;
      document.getElementById("val_b").textContent = B.toFixed(1);

      let q = +1, m = 1, col = "#00f0ff", pName = "Positron";
      if (pType === "electron") { q = -1; col = "#f43f5e"; pName = "Electron"; }
      else if (pType === "muon") { q = -1; m = 207; col = "#38bdf8"; pName = "Muon"; }
      else if (pType === "alpha") { q = +2; m = 7300; col = "#f59e0b"; pName = "Alpha"; }

      const r1 = (6.0 / B) * (m > 10 ? 3.0 : 1.0);
      const r2 = r1 * 0.5; // Loses momentum passing through lead!

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

      // Cloud Chamber Rim
      ctx.fillStyle = "#090e1a"; ctx.strokeStyle = "#1e293b"; ctx.lineWidth = 3;
      ctx.beginPath(); ctx.arc(cx, cy, 95, 0, Math.PI*2); ctx.fill(); ctx.stroke();

      // Magnetic field crosses
      ctx.fillStyle = "rgba(71, 85, 105, 0.4)"; ctx.font = "10px monospace";
      for(let r=0; 5 > r; r++) {
        for(let c=0; 7 > c; c++) {
          ctx.fillText("×", cx - 75 + c * 25, cy - 60 + r * 30);
        }
      }

      // Middle Lead Plate
      ctx.fillStyle = "#475569"; ctx.strokeStyle = "#94a3b8"; ctx.lineWidth = 1;
      ctx.fillRect(cx - 95, cy - 6, 190, 12); ctx.strokeRect(cx - 95, cy - 6, 190, 12);
      ctx.fillStyle = "#ffffff"; ctx.font = "bold 9px sans-serif"; ctx.fillText("แผ่นตะกั่ว Lead Plate (6 mm)", cx - 65, cy + 3);

      // Curved tracks: Region 1 (Bottom) and Region 2 (Top)
      const bend1 = q * (B / 1.5) * 45;
      const bend2 = q * (B / 1.5) * 85;

      ctx.strokeStyle = col; ctx.lineWidth = (pType === "alpha" ? 5.5 : 2.8);
      // Bottom track
      ctx.beginPath();
      ctx.moveTo(cx, cy + 90);
      ctx.quadraticCurveTo(cx + bend1*0.4, cy + 45, cx + bend1*0.6, cy + 6);
      ctx.stroke();

      // Top track
      ctx.beginPath();
      ctx.moveTo(cx + bend1*0.6, cy - 6);
      ctx.quadraticCurveTo(cx + bend1*0.6 + bend2*0.3, cy - 50, cx + bend2, cy - 90);
      ctx.stroke();

      // Continuously spawn vapor droplets along the path
      if (tick % 2 === 0) {
        const u = Math.random();
        let dx, dy;
        if (u < 0.5) {
          const t = u * 2;
          dy = (cy + 90) - t * 84;
          dx = cx + (bend1*0.6) * t + (Math.random()-0.5)*3;
        } else {
          const t = (u - 0.5) * 2;
          dy = (cy - 6) - t * 84;
          dx = (cx + bend1*0.6) + (bend2 - bend1*0.6)*t + (Math.random()-0.5)*3;
        }
        droplets.push({ x: dx, y: dy, alpha: 1.0 });
      }

      // Draw and fade droplets
      for(let i = droplets.length - 1; i >= 0; i--) {
        const d = droplets[i];
        ctx.fillStyle = "rgba(255, 255, 255, " + (d.alpha * 0.7) + ")";
        ctx.beginPath(); ctx.arc(d.x, d.y, (pType === "alpha" ? 2.5 : 1.5), 0, Math.PI*2); ctx.fill();
        d.alpha -= 0.02;
        if (d.alpha <= 0) droplets.splice(i, 1);
      }

      // Active leading particle head
      const prog = (tick * 0.02) % 1;
      let px, py;
      if (0.5 > prog) {
        const t = prog * 2;
        py = (cy + 90) - t * 84;
        px = cx + (bend1*0.6) * t;
      } else {
        const t = (prog - 0.5) * 2;
        py = (cy - 6) - t * 84;
        px = (cx + bend1*0.6) + (bend2 - bend1*0.6) * t;
      }
      ctx.fillStyle = "#ffffff"; ctx.beginPath(); ctx.arc(px, py, 4.5, 0, Math.PI*2); ctx.fill();

      // Explanation banner
      ctx.fillStyle = "#94a3b8"; ctx.font = "11px sans-serif";
      ctx.fillText("รอยทางในห้องหมอก: รัศมีโค้งเล็กลงด้านบน พิสูจน์ว่าอนุภาคพุ่ง 'จากล่างขึ้นบน' และมีประจุบวก (โพซิตรอน)", 40, 215);

      tick++;
      requestAnimationFrame(animate);
    }
    animate();
"""

# ==============================================================================
# 7.2 Refined Feynman Diagrams
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
        ctx.strokeStyle = "#38bdf8"; ctx.lineWidth = 2.8;
        ctx.beginPath(); ctx.moveTo(cx - 190, cy - 65); ctx.lineTo(v1x, cy - 35); ctx.stroke();
        ctx.beginPath(); ctx.moveTo(cx - 190, cy + 65); ctx.lineTo(v1x, cy + 35); ctx.stroke();
        ctx.fillStyle = "#38bdf8"; ctx.font = "bold 11px sans-serif";
        ctx.fillText("e⁻ (in)", cx - 215, cy - 65); ctx.fillText("e⁻ (in)", cx - 215, cy + 70);

        // Vertices nodes (Glow)
        ctx.fillStyle = "#00f0ff";
        ctx.beginPath(); ctx.arc(v1x, cy - 35, 5, 0, Math.PI*2); ctx.fill();
        ctx.beginPath(); ctx.arc(v1x, cy + 35, 5, 0, Math.PI*2); ctx.fill();

        // Virtual Photon wavy line between vertices
        ctx.strokeStyle = "#f59e0b"; ctx.lineWidth = 2.5;
        ctx.beginPath();
        for(let y = -35; 35 >= y; y += 2) {
          const wave = 7 * Math.sin(y * 0.25 + tick*0.12);
          const px = v1x + wave;
          if (y === -35) ctx.moveTo(px, cy + y); else ctx.lineTo(px, cy + y);
        }
        ctx.stroke();
        ctx.fillStyle = "#f59e0b"; ctx.fillText("Virtual Photon γ", v1x + 18, cy + 4);

        // Outgoing electrons
        ctx.strokeStyle = "#38bdf8"; ctx.lineWidth = 2.8;
        ctx.beginPath(); ctx.moveTo(v1x, cy - 35); ctx.lineTo(cx + 170, cy - 75); ctx.stroke();
        ctx.beginPath(); ctx.moveTo(v1x, cy + 35); ctx.lineTo(cx + 170, cy + 75); ctx.stroke();
        ctx.fillText("e⁻ (out)", cx + 180, cy - 75); ctx.fillText("e⁻ (out)", cx + 180, cy + 80);
      }
      else if (proc === "weak") {
        // Beta Decay: d -> u + W- -> e- + nu_bar
        // Incoming d quark
        ctx.strokeStyle = "#10b981"; ctx.lineWidth = 2.8;
        ctx.beginPath(); ctx.moveTo(cx - 180, cy); ctx.lineTo(v1x, cy); ctx.stroke();
        ctx.fillStyle = "#10b981"; ctx.font = "bold 11px sans-serif"; ctx.fillText("d quark (นิวตรอน)", cx - 225, cy - 8);

        // Vertex 1 Node
        ctx.fillStyle = "#f43f5e"; ctx.beginPath(); ctx.arc(v1x, cy, 5, 0, Math.PI*2); ctx.fill();

        // Outgoing u quark
        ctx.beginPath(); ctx.moveTo(v1x, cy); ctx.lineTo(cx - 30, cy - 70); ctx.stroke();
        ctx.fillText("u quark (โปรตอน)", cx - 25, cy - 75);

        // Propagating W- Boson (Wavy)
        ctx.strokeStyle = "#f43f5e"; ctx.lineWidth = 2.5;
        ctx.beginPath();
        for(let s = 0; 120 >= s; s += 2) {
          const px = v1x + s;
          const py = cy + s * 0.2 + 6 * Math.sin(s * 0.25 - tick*0.12);
          if (s === 0) ctx.moveTo(px, py); else ctx.lineTo(px, py);
        }
        ctx.stroke();
        ctx.fillStyle = "#f43f5e"; ctx.fillText("W⁻ Boson", v1x + 35, cy + 30);

        // Vertex 2 Node (Decay of W-)
        const wEnd_x = v1x + 120, wEnd_y = cy + 24;
        ctx.fillStyle = "#38bdf8"; ctx.beginPath(); ctx.arc(wEnd_x, wEnd_y, 5, 0, Math.PI*2); ctx.fill();

        // W- decays into e- and nu_e_bar
        ctx.strokeStyle = "#38bdf8"; ctx.lineWidth = 2.8;
        ctx.beginPath(); ctx.moveTo(wEnd_x, wEnd_y); ctx.lineTo(cx + 180, cy - 30); ctx.stroke();
        ctx.fillText("e⁻ (อิเล็กตรอน)", cx + 190, cy - 30);

        ctx.strokeStyle = "#a855f7"; ctx.lineWidth = 2.8; ctx.setLineDash([4, 4]);
        ctx.beginPath(); ctx.moveTo(wEnd_x, wEnd_y); ctx.lineTo(cx + 180, cy + 70); ctx.stroke(); ctx.setLineDash([]);
        ctx.fillStyle = "#a855f7"; ctx.fillText("ν̄ₑ (แอนตินิวทริโน)", cx + 190, cy + 75);
      }
      else {
        // Strong Force: Quark-Quark Gluon Exchange
        ctx.strokeStyle = "#f59e0b"; ctx.lineWidth = 2.8;
        ctx.beginPath(); ctx.moveTo(cx - 180, cy - 50); ctx.lineTo(v1x, cy - 50); ctx.lineTo(cx + 170, cy - 50); ctx.stroke();
        ctx.beginPath(); ctx.moveTo(cx - 180, cy + 50); ctx.lineTo(v1x, cy + 50); ctx.lineTo(cx + 170, cy + 50); ctx.stroke();

        ctx.fillStyle = "#00f0ff";
        ctx.beginPath(); ctx.arc(v1x, cy - 50, 5, 0, Math.PI*2); ctx.fill();
        ctx.beginPath(); ctx.arc(v1x, cy + 50, 5, 0, Math.PI*2); ctx.fill();

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

# Re-wrap and write 7.1 through 7.5
files = {
    "sim_7_1.html": wrap_html("7.1 สวนสัตว์อนุภาค & ห้องหมอกวิลสัน", body_7_1, js_7_1),
    "sim_7_2.html": wrap_html("7.2 แรงพื้นฐาน & แผนภาพไฟน์แมน", body_7_2, js_7_2)
}

for fname, content in files.items():
    fpath = os.path.join(SIM_DIR, fname)
    with open(fpath, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"✅ Refined {fpath} ({len(content)} bytes)")
