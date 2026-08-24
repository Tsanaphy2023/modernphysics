#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generates hyper-realistic, 60 FPS physics simulations for all 5 subtopics of Chapter 2 (Special Relativity):
- sim_2_1.html: Michelson-Morley Interferometer & Postulates of Relativity (Live Fringe Shifts vs Null Result)
- sim_2_2.html: Lorentz Transformations & Dynamic Minkowski Spacetime Diagram (Light Cone & Event Boosts)
- sim_2_3.html: Time Dilation, Length Contraction & Atmospheric Muon Decay Experiment
- sim_2_4.html: Relativistic Mass, Momentum & Energy-Momentum Invariant (E=mc² & Speed of Light Limit)
- sim_2_5.html: Chapter 2 Virtual Relativity Lab: Twin Paradox Worldline Journey & Relativistic Doppler Starfield
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
# 2.1 Michelson-Morley Experiment & Postulates of Relativity
# ==============================================================================
body_2_1 = """
  <div class="sim-card">
    <div class="sim-header">
      <div class="sim-title"><span>🔬</span> 2.1 การทดลองไมเคิลสัน-มอร์ลีย์: ลมอีเธอร์ & สัจพจน์ความเร็วแสงคงที่</div>
      <div class="badge-fps">● 60 FPS REAL-TIME</div>
    </div>
    <div class="control-grid">
      <div class="ctrl-box">
        <label>สมมติฐานความเร็วลมอีเธอร์ (v/c): <span id="val_v" class="val-display">0.00</span> c</label>
        <input type="range" id="slider_v" min="0.00" max="0.80" step="0.02" value="0.00">
      </div>
      <div class="ctrl-box">
        <label>มุมการหมุนของแท่นทดลอง (θ): <span id="val_theta" class="val-display">0</span>°</label>
        <input type="range" id="slider_theta" min="0" max="90" step="15" value="0">
      </div>
    </div>
    <div class="canvas-box"><canvas id="simCanvas" width="640" height="230"></canvas></div>
    <div class="readout-grid">
      <div class="readout-card"><div class="readout-val" id="val_fringe_pred">0.00 ริ้ว</div><div class="readout-lbl">การเลื่อนริ้วตามทฤษฎีอีเธอร์ (Classical)</div></div>
      <div class="readout-card"><div class="readout-val" id="val_fringe_obs" style="color:#10b981;">0.00 ริ้ว (Null Result)</div><div class="readout-lbl">ผลการทดลองจริง (สัจพจน์ c คงที่)</div></div>
      <div class="readout-card"><div class="readout-val" id="val_status" style="color:#00f0ff;">ไม่มีอีเธอร์ (c คงที่)</div><div class="readout-lbl">ข้อสรุปสัมพัทธภาพพิเศษ</div></div>
    </div>
  </div>
"""

js_2_1 = """
    const cv = document.getElementById("simCanvas");
    const ctx = cv.getContext("2d");
    const sliderV = document.getElementById("slider_v");
    const sliderTheta = document.getElementById("slider_theta");
    let tick = 0;

    function animate() {
      const v = +sliderV.value;
      const theta = +sliderTheta.value;

      document.getElementById("val_v").textContent = v.toFixed(2);
      document.getElementById("val_theta").textContent = theta;

      // Classical ether predicted fringe shift: delta_N = (2L/lambda) * (v/c)^2 * cos(2*theta)
      const fringePred = (12.0 * v * v * Math.cos(theta * Math.PI / 90)).toFixed(2);
      document.getElementById("val_fringe_pred").textContent = fringePred + " ริ้ว";

      ctx.clearRect(0, 0, cv.width, cv.height);

      // Left Panel: Interferometer Apparatus
      const cx = 130, cy = 115, armLen = 70;

      // Ether Wind Indicator (Faint Cyan Arrows)
      if (v > 0) {
        ctx.strokeStyle = "rgba(0, 240, 255, 0.25)"; ctx.lineWidth = 1.5;
        for(let row=0; 5 > row; row++) {
          const arrowY = 30 + row * 40;
          const shiftX = (tick * v * 4) % 240;
          ctx.beginPath(); ctx.moveTo(shiftX, arrowY); ctx.lineTo(shiftX + 25, arrowY); ctx.stroke();
          ctx.beginPath(); ctx.moveTo(shiftX + 20, arrowY - 4); ctx.lineTo(shiftX + 25, arrowY); ctx.lineTo(shiftX + 20, arrowY + 4); ctx.stroke();
        }
        ctx.fillStyle = "rgba(0, 240, 255, 0.6)"; ctx.font = "10px sans-serif";
        ctx.fillText("ลมอีเธอร์ (v = " + v.toFixed(2) + "c) →", 20, 22);
      }

      // Laser Source
      ctx.fillStyle = "#ef4444"; ctx.fillRect(20, cy - 8, 22, 16);
      ctx.fillStyle = "#ffffff"; ctx.font = "9px sans-serif"; ctx.fillText("Laser", 21, cy + 4);

      // Beam Splitter (Semi-transparent mirror at 45 deg)
      ctx.strokeStyle = "#38bdf8"; ctx.lineWidth = 3;
      ctx.beginPath(); ctx.moveTo(cx - 12, cy + 12); ctx.lineTo(cx + 12, cy - 12); ctx.stroke();

      // Mirror 1 (Horizontal Arm)
      const m1x = cx + armLen, m1y = cy;
      ctx.fillStyle = "#64748b"; ctx.fillRect(m1x, cy - 12, 6, 24);

      // Mirror 2 (Vertical Arm)
      const m2x = cx, m2y = cy - armLen;
      ctx.fillStyle = "#64748b"; ctx.fillRect(cx - 12, m2y - 6, 24, 6);

      // Detector / Screen
      const detX = cx, detY = cy + armLen;
      ctx.fillStyle = "#1e293b"; ctx.strokeStyle = "#00f0ff"; ctx.lineWidth = 1.5;
      ctx.fillRect(detX - 16, detY, 32, 14); ctx.strokeRect(detX - 16, detY, 32, 14);
      ctx.fillStyle = "#00f0ff"; ctx.font = "9px sans-serif"; ctx.fillText("Sensor", detX - 14, detY + 10);

      // Light Beams (Red Monochromatic 632.8 nm Laser)
      ctx.strokeStyle = "#ef4444"; ctx.lineWidth = 2;
      // Laser to Splitter
      ctx.beginPath(); ctx.moveTo(42, cy); ctx.lineTo(cx, cy); ctx.stroke();
      // Splitter to Mirror 1 and back
      ctx.beginPath(); ctx.moveTo(cx, cy); ctx.lineTo(m1x, cy); ctx.stroke();
      // Splitter to Mirror 2 and back
      ctx.beginPath(); ctx.moveTo(cx, cy); ctx.lineTo(cx, m2y); ctx.stroke();
      // Splitter to Detector
      ctx.beginPath(); ctx.moveTo(cx, cy); ctx.lineTo(cx, detY); ctx.stroke();

      // Photon packets
      const p1 = (tick * 4) % (armLen * 2);
      const px1 = p1 < armLen ? cx + p1 : m1x - (p1 - armLen);
      ctx.fillStyle = "#fbbf24"; ctx.beginPath(); ctx.arc(px1, cy, 3, 0, Math.PI*2); ctx.fill();

      const p2 = (tick * 4) % (armLen * 2);
      const py2 = p2 < armLen ? cy - p2 : m2y + (p2 - armLen);
      ctx.fillStyle = "#fbbf24"; ctx.beginPath(); ctx.arc(cx, py2, 3, 0, Math.PI*2); ctx.fill();

      // Right Panel: Optical Interference Pattern (Fringes)
      const fBoxX = 270, fBoxY = 25, fBoxW = 345, fBoxH = 175;

      ctx.fillStyle = "#090e1a"; ctx.strokeStyle = "#1e293b"; ctx.lineWidth = 1.5;
      ctx.fillRect(fBoxX, fBoxY, fBoxW, fBoxH); ctx.strokeRect(fBoxX, fBoxY, fBoxW, fBoxH);

      ctx.fillStyle = "#94a3b8"; ctx.font = "11px sans-serif";
      ctx.fillText("ภาพริ้วแทรกสอดจริงบนฉากรับ (Observed Interference Fringes)", fBoxX + 15, fBoxY + 20);

      // Draw Interference Fringes
      const fringeY = fBoxY + 35, fringeH = 75;
      const fringeGrad = ctx.createLinearGradient(fBoxX + 15, 0, fBoxX + fBoxW - 15, 0);
      for(let step=0; 10 >= step; step++) {
        const stop = step / 10;
        const bright = step % 2 === 0 ? "rgba(239, 68, 68, 0.9)" : "rgba(15, 23, 42, 0.95)";
        fringeGrad.addColorStop(stop, bright);
      }
      ctx.fillStyle = fringeGrad;
      ctx.fillRect(fBoxX + 15, fringeY, fBoxW - 30, fringeH);
      ctx.strokeStyle = "#ef4444"; ctx.strokeRect(fBoxX + 15, fringeY, fBoxW - 30, fringeH);

      // Comparison Box
      ctx.fillStyle = "#0f172a"; ctx.strokeStyle = "#334155";
      ctx.fillRect(fBoxX + 15, 145, fBoxW - 30, 45); ctx.strokeRect(fBoxX + 15, 145, fBoxW - 30, 45);

      ctx.fillStyle = "#10b981"; ctx.font = "bold 11px 'JetBrains Mono', monospace";
      ctx.fillText("✓ สัจพจน์ข้อที่ 2: ความเร็วแสงในสุญญากาศ c มีค่าคงตัวในทุกกรอบอ้างอิงเฉื่อย", fBoxX + 22, 163);
      ctx.fillStyle = "#94a3b8"; ctx.font = "10px sans-serif";
      ctx.fillText("ไม่พบการเลื่อนของริ้วแทรกสอดแม้โลกโคจรด้วย v = 30 km/s (Null Result)", fBoxX + 22, 180);

      tick++;
      requestAnimationFrame(animate);
    }
    animate();
"""

# ==============================================================================
# 2.2 Lorentz Transformations & Minkowski Spacetime Diagram
# ==============================================================================
body_2_2 = """
  <div class="sim-card">
    <div class="sim-header">
      <div class="sim-title"><span>🔬</span> 2.2 การแปลงแบบลอเรนซ์ & แผนภาพกาลอวกาศมินคอฟสกี (Spacetime Diagram)</div>
      <div class="badge-fps">● 60 FPS REAL-TIME</div>
    </div>
    <div class="control-grid">
      <div class="ctrl-box">
        <label>ความเร็วสัมพัทธ์ของกรอบ S' (v/c): <span id="val_v" class="val-display">0.60</span> c</label>
        <input type="range" id="slider_v" min="0.00" max="0.95" step="0.01" value="0.60">
      </div>
      <div class="ctrl-box">
        <label>ตำแหน่งเหตุการณ์ในกรอบ S (x, ct):</label>
        <select id="sel_event">
          <option value="4,3" selected>เหตุการณ์ A: x = 4 ly, ct = 3 yr (สเปซไลก์)</option>
          <option value="2,4">เหตุการณ์ B: x = 2 ly, ct = 4 yr (ไทม์ไลก์)</option>
          <option value="3,3">เหตุการณ์ C: x = 3 ly, ct = 3 yr (แสง/ไลต์ไลก์)</option>
        </select>
      </div>
    </div>
    <div class="canvas-box"><canvas id="simCanvas" width="640" height="230"></canvas></div>
    <div class="readout-grid">
      <div class="readout-card"><div class="readout-val" id="val_gamma">1.250</div><div class="readout-lbl">ตัวประกอบลอเรนซ์ (γ = 1/√(1-v²/c²))</div></div>
      <div class="readout-card"><div class="readout-val" id="val_xprime">2.75 ly</div><div class="readout-lbl">พิกัด x' = γ(x - vt)</div></div>
      <div class="readout-card"><div class="readout-val" id="val_tprime">0.75 yr</div><div class="readout-lbl">พิกัด ct' = γ(ct - vx/c)</div></div>
    </div>
  </div>
"""

js_2_2 = """
    const cv = document.getElementById("simCanvas");
    const ctx = cv.getContext("2d");
    const sliderV = document.getElementById("slider_v");
    const selEvent = document.getElementById("sel_event");
    let tick = 0;

    function animate() {
      const v = +sliderV.value;
      const beta = v;
      const gamma = 1 / Math.sqrt(1 - beta*beta);

      document.getElementById("val_v").textContent = v.toFixed(2);
      document.getElementById("val_gamma").textContent = gamma.toFixed(3);

      const evParts = selEvent.value.split(",");
      const x = +evParts[0], ct = +evParts[1];

      // Lorentz Transform
      const xPrime = gamma * (x - beta * ct);
      const ctPrime = gamma * (ct - beta * x);

      document.getElementById("val_xprime").textContent = xPrime.toFixed(2) + " ly";
      document.getElementById("val_tprime").textContent = ctPrime.toFixed(2) + " yr";

      ctx.clearRect(0, 0, cv.width, cv.height);

      // Minkowski Spacetime Graph (Left-Center)
      const ox = 190, oy = 190, scale = 26;

      // Light Cone (x = ct and x = -ct)
      ctx.fillStyle = "rgba(245, 158, 11, 0.08)";
      ctx.beginPath(); ctx.moveTo(ox, oy); ctx.lineTo(ox + 160, oy - 160); ctx.lineTo(ox - 160, oy - 160); ctx.closePath(); ctx.fill();

      ctx.strokeStyle = "rgba(245, 158, 11, 0.45)"; ctx.lineWidth = 1.5; ctx.setLineDash([4, 4]);
      ctx.beginPath(); ctx.moveTo(ox - 160, oy + 160); ctx.lineTo(ox + 160, oy - 160); ctx.stroke();
      ctx.beginPath(); ctx.moveTo(ox - 160, oy - 160); ctx.lineTo(ox + 160, oy + 160); ctx.stroke();
      ctx.setLineDash([]);
      ctx.fillStyle = "#f59e0b"; ctx.font = "10px sans-serif"; ctx.fillText("Light Cone (x = ±ct)", ox + 80, oy - 145);

      // Grid Axes S (Rest Frame)
      ctx.strokeStyle = "#475569"; ctx.lineWidth = 1.5;
      ctx.beginPath(); ctx.moveTo(ox - 160, oy); ctx.lineTo(ox + 160, oy); ctx.stroke(); // x-axis
      ctx.beginPath(); ctx.moveTo(ox, oy + 20); ctx.lineTo(ox, oy - 170); ctx.stroke(); // ct-axis

      ctx.fillStyle = "#94a3b8"; ctx.font = "11px 'JetBrains Mono', monospace";
      ctx.fillText("x (ly)", ox + 145, oy + 15);
      ctx.fillText("ct (yr)", ox + 8, oy - 158);

      // Boosted Axes S' (Moving Frame tilted by angle alpha = arctan(v/c))
      const alpha = Math.atan(beta);
      ctx.strokeStyle = "#00f0ff"; ctx.lineWidth = 2;
      // x' axis (tilted up by alpha)
      ctx.beginPath(); ctx.moveTo(ox - 150 * Math.cos(alpha), oy + 150 * Math.sin(alpha)); ctx.lineTo(ox + 150 * Math.cos(alpha), oy - 150 * Math.sin(alpha)); ctx.stroke();
      // ct' axis (tilted right by alpha)
      ctx.beginPath(); ctx.moveTo(ox - 150 * Math.sin(alpha), oy + 150 * Math.cos(alpha)); ctx.lineTo(ox + 150 * Math.sin(alpha), oy - 150 * Math.cos(alpha)); ctx.stroke();

      ctx.fillStyle = "#00f0ff";
      ctx.fillText("x'", ox + 150 * Math.cos(alpha) + 5, oy - 150 * Math.sin(alpha) + 4);
      ctx.fillText("ct'", ox + 150 * Math.sin(alpha) + 5, oy - 150 * Math.cos(alpha) - 5);

      // Event Point E(x, ct)
      const ex = ox + x * scale;
      const ey = oy - ct * scale;

      ctx.fillStyle = "#f43f5e";
      ctx.beginPath(); ctx.arc(ex, ey, 6, 0, Math.PI*2); ctx.fill();
      ctx.strokeStyle = "#ffffff"; ctx.lineWidth = 1.5; ctx.stroke();

      ctx.fillStyle = "#ffffff"; ctx.font = "bold 11px sans-serif";
      ctx.fillText("E (" + x + ", " + ct + ")", ex + 8, ey - 6);

      // Right Panel: Formulas & Transformation Readouts
      const rBoxX = 390, rBoxY = 25, rBoxW = 230, rBoxH = 175;
      ctx.fillStyle = "#0f172a"; ctx.strokeStyle = "#1e293b"; ctx.lineWidth = 1.5;
      ctx.fillRect(rBoxX, rBoxY, rBoxW, rBoxH); ctx.strokeRect(rBoxX, rBoxY, rBoxW, rBoxH);

      ctx.fillStyle = "#00f0ff"; ctx.font = "bold 11px sans-serif";
      ctx.fillText("สมการการแปลงแบบลอเรนซ์", rBoxX + 14, rBoxY + 22);

      ctx.fillStyle = "#f8fafc"; ctx.font = "11px 'JetBrains Mono', monospace";
      ctx.fillText("x'  = γ (x - β·ct)", rBoxX + 14, rBoxY + 50);
      ctx.fillText("ct' = γ (ct - β·x)", rBoxX + 14, rBoxY + 72);
      ctx.fillText("γ   = " + gamma.toFixed(3), rBoxX + 14, rBoxY + 96);

      ctx.strokeStyle = "#334155";
      ctx.beginPath(); ctx.moveTo(rBoxX + 14, rBoxY + 110); ctx.lineTo(rBoxX + rBoxW - 14, rBoxY + 110); ctx.stroke();

      const s2 = ct*ct - x*x;
      let intervalType = s2 > 0 ? "Timelike (เป็นไปได้เชิงเหตุผล)" : (0 > s2 ? "Spacelike (ไม่สามารถส่งสัญญาณถึงกัน)" : "Lightlike (เชื่อมโยงด้วยแสง)");
      ctx.fillStyle = s2 >= 0 ? "#10b981" : "#f59e0b"; ctx.font = "10px sans-serif";
      ctx.fillText("ช่วงกาลอวกาศคงตัว (s²): " + s2.toFixed(1), rBoxX + 14, rBoxY + 132);
      ctx.fillText(intervalType, rBoxX + 14, rBoxY + 152);

      tick++;
      requestAnimationFrame(animate);
    }
    animate();
"""

# ==============================================================================
# 2.3 Time Dilation, Length Contraction & Muon Decay Experiment
# ==============================================================================
body_2_3 = """
  <div class="sim-card">
    <div class="sim-header">
      <div class="sim-title"><span>🔬</span> 2.3 การยืดออกของเวลา การหดสั้นของระยะทาง & มิวออนในชั้นบรรยากาศ</div>
      <div class="badge-fps">● 60 FPS REAL-TIME</div>
    </div>
    <div class="tab-bar">
      <button class="tab-btn active" id="tabClock" onclick="setMode('clock')">⏱️ นาฬิกาแสง (Light Clock Dilation)</button>
      <button class="tab-btn" id="tabMuon" onclick="setMode('muon')">🌌 การทดลองมิวออน (Muon Decay)</button>
    </div>
    <div id="controlsClock" class="control-grid">
      <div class="ctrl-box">
        <label>ความเร็วของยานอวกาศ (v/c): <span id="val_clock_v" class="val-display">0.80</span> c</label>
        <input type="range" id="slider_clock_v" min="0.00" max="0.95" step="0.01" value="0.80">
      </div>
      <div class="ctrl-box">
        <label>ความสูงของนาฬิกาแสง (L₀): 1.0 เมตร (คงตัว)</label>
        <div style="color:#94a3b8; font-size:0.80rem; margin-top:4px;">โฟตอนวิ่งด้วยความเร็วคงที่ c ในทุกกรอบอ้างอิง</div>
      </div>
    </div>
    <div id="controlsMuon" class="control-grid" style="display:none;">
      <div class="ctrl-box">
        <label>ความเร็วอนุภาคมิวออน (v/c): <span id="val_muon_v" class="val-display">0.995</span> c</label>
        <input type="range" id="slider_muon_v" min="0.500" max="0.999" step="0.001" value="0.995">
      </div>
      <div class="ctrl-box">
        <label>ความสูงจุดกำเนิดมิวออน: 10.0 km (ยอดชั้นบรรยากาศ)</label>
        <div style="color:#94a3b8; font-size:0.80rem; margin-top:4px;">อายุขัยแท้จริง τ₀ = 2.2 µs</div>
      </div>
    </div>
    <div class="canvas-box"><canvas id="simCanvas" width="640" height="230"></canvas></div>
    <div class="readout-grid" id="readoutsClock">
      <div class="readout-card"><div class="readout-val" id="val_gamma_clock">1.667</div><div class="readout-lbl">ตัวประกอบลอเรนซ์ (γ)</div></div>
      <div class="readout-card"><div class="readout-val" id="val_t0_clock">6.67 ns</div><div class="readout-lbl">เวลาเฉพาะบนยาน (Δt₀ = 2L/c)</div></div>
      <div class="readout-card"><div class="readout-val" id="val_t_clock" style="color:#f59e0b;">11.11 ns</div><div class="readout-lbl">เวลาบนโลก (Δt = γΔt₀) ยืดออก!</div></div>
    </div>
    <div class="readout-grid" id="readoutsMuon" style="display:none;">
      <div class="readout-card"><div class="readout-val" id="val_gamma_muon">10.01</div><div class="readout-lbl">ตัวประกอบลอเรนซ์ (γ)</div></div>
      <div class="readout-card"><div class="readout-val" id="val_hprime_muon">1.00 km</div><div class="readout-lbl">ระยะทางหดสั้นในกรอบมิวออน (H')</div></div>
      <div class="readout-card"><div class="readout-val" id="val_survive_muon" style="color:#10b981;">รอดถึงพื้น 49.2 %</div><div class="readout-lbl">ตรวจพบที่ระดับน้ำทะเล (Relativity)</div></div>
    </div>
  </div>
"""

js_2_3 = """
    const cv = document.getElementById("simCanvas");
    const ctx = cv.getContext("2d");
    let currentMode = "clock";
    let tick = 0;

    function setMode(mode) {
      currentMode = mode;
      document.getElementById("tabClock").classList.toggle("active", mode === "clock");
      document.getElementById("tabMuon").classList.toggle("active", mode === "muon");
      document.getElementById("controlsClock").style.display = mode === "clock" ? "grid" : "none";
      document.getElementById("controlsMuon").style.display = mode === "muon" ? "grid" : "none";
      document.getElementById("readoutsClock").style.display = mode === "clock" ? "grid" : "none";
      document.getElementById("readoutsMuon").style.display = mode === "muon" ? "grid" : "none";
    }

    let muons = [];
    for(let i=0; 30 > i; i++) {
      muons.push({
        x: 40 + Math.random()*220,
        y: 20 + Math.random()*150,
        alive: true
      });
    }

    function animate() {
      ctx.clearRect(0, 0, cv.width, cv.height);

      if (currentMode === "clock") {
        const v = +document.getElementById("slider_clock_v").value;
        document.getElementById("val_clock_v").textContent = v.toFixed(2);
        const gamma = 1 / Math.sqrt(1 - v*v);
        document.getElementById("val_gamma_clock").textContent = gamma.toFixed(3);

        const dt0 = 6.67;
        const dt = dt0 * gamma;
        document.getElementById("val_t0_clock").textContent = dt0.toFixed(2) + " ns";
        document.getElementById("val_t_clock").textContent = dt.toFixed(2) + " ns";

        // Left: Ship Frame S' (Stationary Light Clock)
        const s1x = 90, s1y = 40, s1w = 120, s1h = 140;
        ctx.fillStyle = "#0f172a"; ctx.strokeStyle = "#1e293b"; ctx.lineWidth = 1.5;
        ctx.fillRect(s1x, s1y, s1w, s1h); ctx.strokeRect(s1x, s1y, s1w, s1h);

        ctx.fillStyle = "#00f0ff"; ctx.font = "11px sans-serif";
        ctx.fillText("กรอบบนยาน (S' พักนิ่ง)", s1x + 10, s1y - 10);

        // Mirrors
        ctx.fillStyle = "#64748b"; ctx.fillRect(s1x + 20, s1y + 15, 80, 8); ctx.fillRect(s1x + 20, s1y + s1h - 23, 80, 8);

        // Bouncing photon S'
        const prog0 = (tick * 0.05) % 2;
        const photY0 = prog0 < 1 ? s1y + 25 + prog0 * 90 : s1y + 115 - (prog0 - 1) * 90;
        ctx.fillStyle = "#fbbf24"; ctx.beginPath(); ctx.arc(s1x + 60, photY0, 4.5, 0, Math.PI*2); ctx.fill();

        ctx.strokeStyle = "rgba(251, 191, 36, 0.4)"; ctx.lineWidth = 1.5; ctx.setLineDash([2, 2]);
        ctx.beginPath(); ctx.moveTo(s1x + 60, s1y + 25); ctx.lineTo(s1x + 60, s1y + 115); ctx.stroke();
        ctx.setLineDash([]);

        // Right: Earth Frame S (Moving Light Clock - Diagonal Zig-Zag)
        const s2x = 270, s2y = 40, s2w = 340, s2h = 140;
        ctx.fillStyle = "#0f172a"; ctx.strokeStyle = "#1e293b"; ctx.lineWidth = 1.5;
        ctx.fillRect(s2x, s2y, s2w, s2h); ctx.strokeRect(s2x, s2y, s2w, s2h);

        ctx.fillStyle = "#f59e0b"; ctx.font = "11px sans-serif";
        ctx.fillText("กรอบบนโลก (S มองเห็นยานแล่น v = " + v.toFixed(2) + "c)", s2x + 10, s2y - 10);

        // Moving Rocket & Diagonal Path
        const cycle = (tick * 0.05 / gamma) % 2;
        const shipShift = ((tick * 1.5 * v) % 200);

        // Path Zigzag
        ctx.strokeStyle = "rgba(245, 158, 11, 0.5)"; ctx.lineWidth = 2; ctx.setLineDash([3, 3]);
        ctx.beginPath();
        ctx.moveTo(s2x + 30, s2y + 25);
        ctx.lineTo(s2x + 30 + 70 * v * gamma, s2y + 115);
        ctx.lineTo(s2x + 30 + 140 * v * gamma, s2y + 25);
        ctx.stroke(); ctx.setLineDash([]);

        // Photon in S
        const photX1 = s2x + 30 + cycle * 70 * v * gamma;
        const photY1 = cycle < 1 ? s2y + 25 + cycle * 90 : s2y + 115 - (cycle - 1) * 90;
        ctx.fillStyle = "#fbbf24"; ctx.beginPath(); ctx.arc(photX1, photY1, 4.5, 0, Math.PI*2); ctx.fill();

        ctx.fillStyle = "#94a3b8"; ctx.font = "10px sans-serif";
        ctx.fillText("เส้นทางแสงยาวขึ้น → เวลายืดออก: Δt = γ·Δt₀", s2x + 15, s2y + s2h - 8);
      }
      else {
        // Muon Decay Mode
        const v = +document.getElementById("slider_muon_v").value;
        document.getElementById("val_muon_v").textContent = v.toFixed(3);
        const gamma = 1 / Math.sqrt(1 - v*v);
        document.getElementById("val_gamma_muon").textContent = gamma.toFixed(2);

        const hPrime = (10.0 / gamma).toFixed(2);
        document.getElementById("val_hprime_muon").textContent = hPrime + " km";

        // Survival probability: P = exp(- H / (gamma * v * c * tau0))
        const d_decay = gamma * v * 3e5 * 2.2e-6; // km
        const p_survive = Math.exp(-10.0 / d_decay) * 100;
        document.getElementById("val_survive_muon").textContent = "รอดถึงพื้น " + p_survive.toFixed(1) + " %";

        // Atmosphere Box
        ctx.fillStyle = "#0f172a"; ctx.strokeStyle = "#1e293b"; ctx.lineWidth = 1.5;
        ctx.fillRect(50, 20, 260, 185); ctx.strokeRect(50, 20, 260, 185);

        ctx.fillStyle = "rgba(59, 130, 246, 0.15)"; ctx.fillRect(51, 21, 258, 183);

        ctx.fillStyle = "#38bdf8"; ctx.font = "10px sans-serif";
        ctx.fillText("ชั้นบรรยากาศโลก (H = 10 km)", 60, 36);
        ctx.fillStyle = "#10b981";
        ctx.fillText("ระดับน้ำทะเล (Sea Level)", 60, 196);

        // Muon rain
        muons.forEach(m => {
          ctx.fillStyle = "#a855f7"; ctx.beginPath(); ctx.arc(m.x + 40, m.y, 3, 0, Math.PI*2); ctx.fill();
          m.y += v * 3.5;
          if (m.y > 195) {
            m.y = 30; m.x = 40 + Math.random()*200;
          }
        });

        // Comparison Graph (Right)
        const gx = 350, gy = 20, gw = 260, gh = 185;
        ctx.fillStyle = "#090e1a"; ctx.strokeStyle = "#1e293b";
        ctx.fillRect(gx, gy, gw, gh); ctx.strokeRect(gx, gy, gw, gh);

        ctx.fillStyle = "#f8fafc"; ctx.font = "11px sans-serif";
        ctx.fillText("การเปรียบเทียบการรอดชีวิตของมิวออน", gx + 15, gy + 24);

        // Classical bar (almost 0%)
        ctx.fillStyle = "#f43f5e"; ctx.fillRect(gx + 20, gy + 55, 12, 110);
        ctx.fillStyle = "#f43f5e"; ctx.font = "10px sans-serif"; ctx.fillText("Classical (0.3%)", gx + 38, gy + 115);

        // Relativistic bar
        const rBarH = Math.min(110, (p_survive / 100) * 110);
        ctx.fillStyle = "#10b981"; ctx.fillRect(gx + 140, gy + 55 + (110 - rBarH), 12, rBarH);
        ctx.fillStyle = "#10b981"; ctx.fillText("Relativity (" + p_survive.toFixed(1) + "%)", gx + 158, gy + 115);
      }

      tick++;
      requestAnimationFrame(animate);
    }
    animate();
"""

# ==============================================================================
# 2.4 Relativistic Mass, Momentum & Energy (E = mc²)
# ==============================================================================
body_2_4 = """
  <div class="sim-card">
    <div class="sim-header">
      <div class="sim-title"><span>🔬</span> 2.4 ความสมมูลมวล-พลังงาน: โมเมนตัมสัมพัทธภาพ & ขีดจำกัดความเร็วแสง (c)</div>
      <div class="badge-fps">● 60 FPS REAL-TIME</div>
    </div>
    <div class="control-grid">
      <div class="ctrl-box">
        <label>ความเร็วอนุภาค (v/c): <span id="val_v" class="val-display">0.850</span> c</label>
        <input type="range" id="slider_v" min="0.000" max="0.999" step="0.001" value="0.850">
      </div>
      <div class="ctrl-box">
        <label>อนุภาคเป้าหมาย (มวลนิ่ง m₀):</label>
        <select id="sel_particle">
          <option value="0.511" selected>อิเล็กตรอน Electron (m₀c² = 0.511 MeV)</option>
          <option value="938.3">โปรตอน Proton (m₀c² = 938.3 MeV)</option>
          <option value="1.0">มวล 1 กรัม (m₀c² = 9.0 × 10¹³ J)</option>
        </select>
      </div>
    </div>
    <div class="canvas-box"><canvas id="simCanvas" width="640" height="230"></canvas></div>
    <div class="readout-grid">
      <div class="readout-card"><div class="readout-val" id="val_gamma">1.898</div><div class="readout-lbl">ตัวประกอบลอเรนซ์ (γ)</div></div>
      <div class="readout-card"><div class="readout-val" id="val_ke">0.459 MeV</div><div class="readout-lbl">พลังงานจลน์ K = (γ-1)m₀c²</div></div>
      <div class="readout-card"><div class="readout-val" id="val_etot">0.970 MeV</div><div class="readout-lbl">พลังงานรวม E = γm₀c²</div></div>
    </div>
  </div>
"""

js_2_4 = """
    const cv = document.getElementById("simCanvas");
    const ctx = cv.getContext("2d");
    const sliderV = document.getElementById("slider_v");
    const selPart = document.getElementById("sel_particle");
    let tick = 0;

    function animate() {
      const v = +sliderV.value;
      const m0 = +selPart.value;

      document.getElementById("val_v").textContent = v.toFixed(3);
      const gamma = 1 / Math.sqrt(1 - v*v);
      document.getElementById("val_gamma").textContent = gamma.toFixed(3);

      const Etot = gamma * m0;
      const K = (gamma - 1) * m0;

      const unit = m0 === 1.0 ? " × 10¹³ J" : " MeV";
      const scaleVal = m0 === 1.0 ? 9.0 : 1.0;

      document.getElementById("val_ke").textContent = (K * scaleVal).toFixed(3) + unit;
      document.getElementById("val_etot").textContent = (Etot * scaleVal).toFixed(3) + unit;

      ctx.clearRect(0, 0, cv.width, cv.height);

      // Left Panel: Particle in Circular Accelerator
      const cx = 110, cy = 115, r = 65;
      ctx.strokeStyle = "#1e293b"; ctx.lineWidth = 12;
      ctx.beginPath(); ctx.arc(cx, cy, r, 0, Math.PI*2); ctx.stroke();
      ctx.strokeStyle = "#00f0ff"; ctx.lineWidth = 2;
      ctx.beginPath(); ctx.arc(cx, cy, r, 0, Math.PI*2); ctx.stroke();

      const ang = tick * (0.04 + v * 0.15);
      const px = cx + r * Math.cos(ang), py = cy + r * Math.sin(ang);
      ctx.fillStyle = "#f59e0b"; ctx.beginPath(); ctx.arc(px, py, 5.5, 0, Math.PI*2); ctx.fill();

      ctx.fillStyle = "#ffffff"; ctx.font = "10px sans-serif";
      ctx.fillText("เครื่องเร่งอนุภาค", cx - 35, cy - 8);
      ctx.fillStyle = "#00f0ff"; ctx.fillText("v = " + (v*100).toFixed(1) + "% c", cx - 30, cy + 8);

      // Right Panel: Relativistic vs Classical Curves
      const ox = 250, oy = 195, gw = 360, gh = 160;

      // Coordinate axes
      ctx.strokeStyle = "#475569"; ctx.lineWidth = 1.5;
      ctx.beginPath(); ctx.moveTo(ox, oy); ctx.lineTo(ox + gw, oy); ctx.lineTo(ox + gw - 6, oy - 4); ctx.stroke();
      ctx.beginPath(); ctx.moveTo(ox, oy); ctx.lineTo(ox, oy - gh); ctx.stroke();

      ctx.fillStyle = "#94a3b8"; ctx.font = "10px sans-serif";
      ctx.fillText("ความเร็วอนุภาค v/c →", ox + gw - 110, oy + 18);
      ctx.fillText("โมเมนตัม p", ox - 15, oy - gh - 6);

      // Speed of light asymptote (c Barrier)
      const cX = ox + gw - 25;
      ctx.strokeStyle = "#ef4444"; ctx.lineWidth = 1.5; ctx.setLineDash([4, 4]);
      ctx.beginPath(); ctx.moveTo(cX, oy); ctx.lineTo(cX, oy - gh); ctx.stroke();
      ctx.setLineDash([]);
      ctx.fillStyle = "#ef4444"; ctx.fillText("c (ขีดจำกัดความเร็วแสง)", cX - 65, oy - gh + 14);

      // Classical Curve p = m0 * v (Linear green)
      ctx.strokeStyle = "#10b981"; ctx.lineWidth = 2;
      ctx.beginPath();
      for(let x=0; (gw - 25) >= x; x+=4) {
        const vel = x / (gw - 25);
        const y = oy - (vel * 60);
        if (x===0) ctx.moveTo(ox + x, y); else ctx.lineTo(ox + x, y);
      }
      ctx.stroke();

      // Relativistic Curve p = gamma * m0 * v (Diverging Cyan)
      ctx.strokeStyle = "#00f0ff"; ctx.lineWidth = 2.5;
      ctx.beginPath();
      for(let x=0; (gw - 26) >= x; x+=2) {
        const vel = x / (gw - 25);
        const gam = 1 / Math.sqrt(1 - vel*vel);
        const y = oy - Math.min(gh - 10, vel * gam * 60);
        if (x===0) ctx.moveTo(ox + x, y); else ctx.lineTo(ox + x, y);
      }
      ctx.stroke();

      // Current position dot
      const curX = ox + v * (gw - 25);
      const curY = oy - Math.min(gh - 10, v * gamma * 60);
      ctx.fillStyle = "#f59e0b"; ctx.beginPath(); ctx.arc(curX, curY, 5, 0, Math.PI*2); ctx.fill();

      // Legends
      ctx.fillStyle = "#10b981"; ctx.fillText("— Classical: p = mv", ox + 15, oy - gh + 35);
      ctx.fillStyle = "#00f0ff"; ctx.fillText("— Relativistic: p = γmv → ∞", ox + 15, oy - gh + 52);

      tick++;
      requestAnimationFrame(animate);
    }
    animate();
"""

# ==============================================================================
# 2.5 Virtual Relativity Lab: Twin Paradox & Doppler Radar
# ==============================================================================
body_2_5 = """
  <div class="sim-card">
    <div class="sim-header">
      <div class="sim-title"><span>🔬</span> 2.5 ปฏิบัติการกาลอวกาศ: ปริศนาฝาแฝด (Twin Paradox) & ดอปเปลอร์สัมพัทธภาพ</div>
      <div class="badge-fps">● 60 FPS REAL-TIME</div>
    </div>
    <div class="tab-bar">
      <button class="tab-btn active" id="tabTwin" onclick="setMode('twin')">🚀 ปริศนาฝาแฝด (Twin Paradox Journey)</button>
      <button class="tab-btn" id="tabDoppler" onclick="setMode('doppler')">🌌 ดอปเปลอร์ & ทัศนศาสตร์ความเร็วสูง</button>
    </div>
    <div id="controlsTwin" class="control-grid">
      <div class="ctrl-box">
        <label>ความเร็วยานของแฝดอวกาศ (v/c): <span id="val_twin_v" class="val-display">0.80</span> c</label>
        <input type="range" id="slider_twin_v" min="0.50" max="0.95" step="0.05" value="0.80">
      </div>
      <div class="ctrl-box">
        <label>ระยะทางไป-กลับยังดาวอัลฟาเซนทอรี: 4.0 ปีแสง (ไป 4 + กลับ 4 ly)</label>
        <div style="color:#94a3b8; font-size:0.80rem; margin-top:4px;">กรอบบนโลกเป็นกรอบเฉื่อยแท้จริง ขณะที่ยานมีความเร่งตอนเลี้ยวกลับ</div>
      </div>
    </div>
    <div id="controlsDoppler" class="control-grid" style="display:none;">
      <div class="ctrl-box">
        <label>ความเร็วและทิศทางการพุ่งชน (v/c): <span id="val_dop_v" class="val-display">+0.75</span> c</label>
        <input type="range" id="slider_dop_v" min="-0.90" max="0.90" step="0.05" value="0.75">
      </div>
      <div class="ctrl-box">
        <label>ความถี่ดั้งเดิมของดวงดาว: f₀ = 500 THz (แสงสีเขียว 600 nm)</label>
        <div style="color:#94a3b8; font-size:0.80rem; margin-top:4px;">f_obs = f₀ √((1+β)/(1-β)) (การเลื่อนไปทางน้ำเงิน/แดง)</div>
      </div>
    </div>
    <div class="canvas-box"><canvas id="simCanvas" width="640" height="230"></canvas></div>
    <div class="readout-grid" id="readoutsTwin">
      <div class="readout-card"><div class="readout-val" id="val_earth_age">10.0 ปี</div><div class="readout-lbl">เวลาที่ผ่านไปบนโลก (Earth Twin)</div></div>
      <div class="readout-card"><div class="readout-val" id="val_ship_age">6.0 ปี</div><div class="readout-lbl">เวลาบนยานอวกาศ (Rocket Twin)</div></div>
      <div class="readout-card"><div class="readout-val" id="val_age_diff" style="color:#10b981;">แฝดบนยานเด็กกว่า 4.0 ปี</div><div class="readout-lbl">ความต่างของอายุเมื่อพบกัน</div></div>
    </div>
    <div class="readout-grid" id="readoutsDoppler" style="display:none;">
      <div class="readout-card"><div class="readout-val" id="val_dop_factor">2.65 ×</div><div class="readout-lbl">อัตราส่วนความถี่ (f_obs / f₀)</div></div>
      <div class="readout-card"><div class="readout-val" id="val_dop_lam">226 nm (UV)</div><div class="readout-lbl">ความยาวคลื่นที่ปรากฏ</div></div>
      <div class="readout-card"><div class="readout-val" id="val_dop_shift" style="color:#00f0ff;">Blueshift (เลื่อนไปทางน้ำเงิน)</div><div class="readout-lbl">ปรากฏการณ์ดอปเปลอร์</div></div>
    </div>
  </div>
"""

js_2_5 = """
    const cv = document.getElementById("simCanvas");
    const ctx = cv.getContext("2d");
    let currentMode = "twin";
    let tick = 0;

    function setMode(mode) {
      currentMode = mode;
      document.getElementById("tabTwin").classList.toggle("active", mode === "twin");
      document.getElementById("tabDoppler").classList.toggle("active", mode === "doppler");
      document.getElementById("controlsTwin").style.display = mode === "twin" ? "grid" : "none";
      document.getElementById("controlsDoppler").style.display = mode === "doppler" ? "grid" : "none";
      document.getElementById("readoutsTwin").style.display = mode === "twin" ? "grid" : "none";
      document.getElementById("readoutsDoppler").style.display = mode === "doppler" ? "grid" : "none";
    }

    let stars = [];
    for(let i=0; 50 > i; i++) {
      stars.push({
        x: Math.random() * 640,
        y: Math.random() * 230,
        z: 0.2 + Math.random()*0.8
      });
    }

    function animate() {
      ctx.clearRect(0, 0, cv.width, cv.height);

      if (currentMode === "twin") {
        const v = +document.getElementById("slider_twin_v").value;
        document.getElementById("val_twin_v").textContent = v.toFixed(2);
        const gamma = 1 / Math.sqrt(1 - v*v);

        const d_one_way = 4.0; // ly
        const t_earth = (2 * d_one_way) / v;
        const t_ship = t_earth / gamma;
        const diff = t_earth - t_ship;

        document.getElementById("val_earth_age").textContent = t_earth.toFixed(1) + " ปี";
        document.getElementById("val_ship_age").textContent = t_ship.toFixed(1) + " ปี";
        document.getElementById("val_age_diff").textContent = "แฝดบนยานเด็กกว่า " + diff.toFixed(1) + " ปี";

        // Journey Animation
        const ox = 70, starX = 540, y = 115;

        // Earth
        ctx.fillStyle = "#38bdf8"; ctx.beginPath(); ctx.arc(ox, y, 16, 0, Math.PI*2); ctx.fill();
        ctx.fillStyle = "#ffffff"; ctx.font = "11px sans-serif"; ctx.fillText("โลก (Earth)", ox - 24, y + 32);

        // Alpha Centauri Star
        ctx.fillStyle = "#f59e0b"; ctx.beginPath(); ctx.arc(starX, y, 18, 0, Math.PI*2); ctx.fill();
        ctx.fillText("Alpha Centauri (4 ly)", starX - 45, y + 32);

        // Flight Path
        ctx.strokeStyle = "rgba(148, 163, 184, 0.3)"; ctx.lineWidth = 1.5; ctx.setLineDash([4, 4]);
        ctx.beginPath(); ctx.moveTo(ox, y); ctx.lineTo(starX, y); ctx.stroke(); ctx.setLineDash([]);

        // Rocket position
        const prog = (tick * 0.008 * v) % 2;
        let rx = prog < 1 ? ox + prog * (starX - ox) : starX - (prog - 1) * (starX - ox);
        let headingRight = prog < 1;

        // Rocket
        ctx.fillStyle = "#00f0ff";
        ctx.beginPath(); ctx.arc(rx, y, 7, 0, Math.PI*2); ctx.fill();

        // Exhaust plume
        ctx.fillStyle = "#f43f5e";
        ctx.beginPath();
        const plumeX = headingRight ? rx - 10 : rx + 10;
        ctx.arc(plumeX, y, 3.5, 0, Math.PI*2); ctx.fill();

        // Current Age Display above heads
        const curEarthT = prog * (t_earth / 2);
        const curShipT = prog * (t_ship / 2);
        ctx.fillStyle = "#38bdf8"; ctx.font = "10px 'JetBrains Mono', monospace";
        ctx.fillText("Earth: " + curEarthT.toFixed(1) + " yr", ox - 20, y - 24);

        ctx.fillStyle = "#00f0ff";
        ctx.fillText("Rocket: " + curShipT.toFixed(1) + " yr", rx - 25, y - 18);
      }
      else {
        // Relativistic Doppler Effect Mode
        const beta = +document.getElementById("slider_dop_v").value;
        document.getElementById("val_dop_v").textContent = (beta >= 0 ? "+" : "") + beta.toFixed(2);

        // Doppler Factor: sqrt((1+beta)/(1-beta))
        const dopFactor = Math.sqrt((1 + beta) / (1 - beta));
        const lam_obs = 600 / dopFactor;

        document.getElementById("val_dop_factor").textContent = dopFactor.toFixed(2) + " ×";
        document.getElementById("val_dop_lam").textContent = lam_obs.toFixed(1) + " nm";

        const shiftEl = document.getElementById("val_dop_shift");
        if (beta > 0.05) {
          shiftEl.textContent = "Blueshift (เลื่อนไปทางน้ำเงิน/UV)"; shiftEl.style.color = "#00f0ff";
        } else if (-0.05 > beta) {
          shiftEl.textContent = "Redshift (เลื่อนไปทางแดง/IR)"; shiftEl.style.color = "#f43f5e";
        } else {
          shiftEl.textContent = "ไม่มีการเลื่อน (v ≈ 0)"; shiftEl.style.color = "#10b981";
        }

        // Warp Starfield
        let starCol = beta > 0 ? "rgba(56, 189, 248, " : "rgba(244, 63, 94, ";
        stars.forEach(s => {
          ctx.fillStyle = starCol + s.z + ")";
          ctx.beginPath(); ctx.arc(s.x, s.y, s.z * (2 + Math.abs(beta)*3), 0, Math.PI*2); ctx.fill();
          s.x += beta * 6 * s.z;
          if (s.x > 640) s.x = 0;
          if (0 > s.x) s.x = 640;
        });

        // Cockpit Reticle
        ctx.strokeStyle = "rgba(0, 240, 255, 0.4)"; ctx.lineWidth = 1.5;
        ctx.strokeRect(260, 65, 120, 100);
        ctx.beginPath(); ctx.moveTo(320, 100); ctx.lineTo(320, 130); ctx.moveTo(305, 115); ctx.lineTo(335, 115); ctx.stroke();

        ctx.fillStyle = "#ffffff"; ctx.font = "11px sans-serif";
        ctx.fillText("มุมมองหน้ารถ/ยานอวกาศ (Headlight Effect)", 200, 35);
      }

      tick++;
      requestAnimationFrame(animate);
    }
    animate();
"""

files = {
    "sim_2_1.html": wrap_html("2.1 การทดลองไมเคิลสัน-มอร์ลีย์", body_2_1, js_2_1),
    "sim_2_2.html": wrap_html("2.2 การแปลงแบบลอเรนซ์", body_2_2, js_2_2),
    "sim_2_3.html": wrap_html("2.3 การยืดออกของเวลา & มิวออน", body_2_3, js_2_3),
    "sim_2_4.html": wrap_html("2.4 ความสมมูลมวล-พลังงาน", body_2_4, js_2_4),
    "sim_2_5.html": wrap_html("2.5 ปฏิบัติการกาลอวกาศ & ปริศนาฝาแฝด", body_2_5, js_2_5)
}

for fname, content in files.items():
    fpath = os.path.join(SIM_DIR, fname)
    with open(fpath, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"✅ Generated {fpath} ({len(content)} bytes)")

print("🎉 Successfully upgraded all Chapter 2 simulations to hyper-realistic 60 FPS engines!")
