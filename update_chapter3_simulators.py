#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generates hyper-realistic, 60 FPS physics simulations for all 5 subtopics of Chapter 3 (Wave-Particle Duality):
- sim_3_1.html: de Broglie Hypothesis & Matter Waves (Particle-Wave Envelope, Voltage vs Wavelength)
- sim_3_2.html: Particle Diffraction: Davisson-Germer Nickel Crystal & Single-Electron Double Slit Build-up
- sim_3_3.html: Wave Packets & Heisenberg Uncertainty Principle (Phase/Group Velocity & Fourier Spread)
- sim_3_4.html: Transmission & Scanning Electron Microscopy (TEM/SEM Optics Column & Atomic Resolution)
- sim_3_5.html: Chapter 3 Virtual Lab: Energy-Time Uncertainty, Quantum Vacuum Fluctuations & Standing Matter Waves
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
# 3.1 de Broglie Hypothesis & Matter Waves
# ==============================================================================
body_3_1 = """
  <div class="sim-card">
    <div class="sim-header">
      <div class="sim-title"><span>🔬</span> 3.1 สมมติฐานของเดอบรอยล์: คลื่นสสาร (Matter Wave) & ความยาวคลื่นเดอบรอยล์</div>
      <div class="badge-fps">● 60 FPS REAL-TIME</div>
    </div>
    <div class="control-grid">
      <div class="ctrl-box">
        <label>อนุภาคสสาร (Matter Particle):</label>
        <select id="sel_part">
          <option value="electron" selected>อิเล็กตรอน Electron (m = 9.11 × 10⁻³¹ kg)</option>
          <option value="proton">โปรตอน Proton (m = 1.67 × 10⁻²⁷ kg)</option>
          <option value="buckyball">โมเลกุลบัคกี้บอล C₆₀ (m = 1.20 × 10⁻²⁴ kg)</option>
        </select>
      </div>
      <div class="ctrl-box">
        <label>ความต่างศักย์เร่งอนุภาค (V_a): <span id="val_va" class="val-display">100</span> V</label>
        <input type="range" id="slider_va" min="10" max="10000" step="10" value="100">
      </div>
    </div>
    <div class="canvas-box"><canvas id="simCanvas" width="640" height="230"></canvas></div>
    <div class="readout-grid">
      <div class="readout-card"><div class="readout-val" id="val_lam">0.123 nm</div><div class="readout-lbl">ความยาวคลื่นเดอบรอยล์ (λ = h/p)</div></div>
      <div class="readout-card"><div class="readout-val" id="val_velocity">5.93 × 10⁶ m/s</div><div class="readout-lbl">ความเร็วอนุภาค (v = √(2qV/m))</div></div>
      <div class="readout-card"><div class="readout-val" id="val_p">5.40 × 10⁻²⁴ kg·m/s</div><div class="readout-lbl">โมเมนตัมของอนุภาค (p)</div></div>
    </div>
  </div>
"""

js_3_1 = """
    const cv = document.getElementById("simCanvas");
    const ctx = cv.getContext("2d");
    const selPart = document.getElementById("sel_part");
    const sliderVa = document.getElementById("slider_va");
    let tick = 0;

    function animate() {
      const partType = selPart.value;
      const Va = +sliderVa.value;
      document.getElementById("val_va").textContent = Va >= 1000 ? (Va/1000).toFixed(1) + " k" : Va;

      // Constants
      const h = 6.626e-34, q = 1.602e-19;
      let m = 9.109e-31; // kg
      let pCol = "#00f0ff";
      if (partType === "proton") { m = 1.673e-27; pCol = "#f59e0b"; }
      else if (partType === "buckyball") { m = 1.20e-24; pCol = "#10b981"; }

      const E_joule = q * Va;
      const v = Math.sqrt(2 * E_joule / m);
      const p = m * v;
      const lambda_m = h / p;
      const lambda_nm = lambda_m * 1e9;

      document.getElementById("val_lam").textContent = lambda_nm < 0.01 ? (lambda_nm*1000).toFixed(2) + " pm" : lambda_nm.toFixed(3) + " nm";
      document.getElementById("val_velocity").textContent = (v >= 1e6 ? (v/1e6).toFixed(2) + " × 10⁶" : (v/1e3).toFixed(1) + " × 10³") + " m/s";
      document.getElementById("val_p").textContent = p.toExponential(2) + " kg·m/s";

      ctx.clearRect(0, 0, cv.width, cv.height);

      // Left Panel: Particle in Matter Wave Envelope
      const cy = 115;
      
      // Electric Acceleration Plates
      ctx.fillStyle = "#334155";
      ctx.fillRect(40, 40, 8, 150); ctx.fillRect(160, 40, 8, 150);
      ctx.fillStyle = "#ef4444"; ctx.font = "10px sans-serif"; ctx.fillText("-", 42, 35);
      ctx.fillStyle = "#38bdf8"; ctx.fillText("+ (" + Va + "V)", 148, 35);

      ctx.strokeStyle = "rgba(56, 189, 248, 0.25)"; ctx.lineWidth = 1; ctx.setLineDash([3, 3]);
      for(let y=60; 180 >= y; y+=25) {
        ctx.beginPath(); ctx.moveTo(48, y); ctx.lineTo(160, y); ctx.stroke();
      }
      ctx.setLineDash([]);

      // Particle moving across
      const prog = (tick * (0.01 + Math.log10(Va)*0.015)) % 1;
      const partX = 60 + prog * 520;

      // Matter wave envelope surrounding particle
      const waveFreq = 0.08 + Math.min(0.4, 1.0 / (lambda_nm + 0.1));
      ctx.strokeStyle = pCol; ctx.lineWidth = 2.5;
      ctx.beginPath();
      for(let x = Math.max(30, partX - 70); Math.min(610, partX + 70) >= x; x += 2) {
        const dist = Math.abs(x - partX) / 70;
        const envelope = Math.exp(-dist * dist * 3.5);
        const y = cy + 28 * envelope * Math.sin((x - tick*4) * waveFreq);
        if (x === Math.max(30, partX - 70)) ctx.moveTo(x, y); else ctx.lineTo(x, y);
      }
      ctx.stroke();

      // Core Particle Sphere
      ctx.fillStyle = pCol;
      ctx.beginPath(); ctx.arc(partX, cy, 6, 0, Math.PI*2); ctx.fill();
      ctx.strokeStyle = "#ffffff"; ctx.lineWidth = 1.5; ctx.stroke();

      ctx.fillStyle = "#ffffff"; ctx.font = "bold 11px sans-serif";
      ctx.fillText(partType.toUpperCase(), partX - 25, cy - 35);

      // Bottom Formulas Card
      ctx.fillStyle = "#0f172a"; ctx.strokeStyle = "#1e293b"; ctx.lineWidth = 1.5;
      ctx.fillRect(200, 160, 420, 55); ctx.strokeRect(200, 160, 420, 55);

      ctx.fillStyle = "#00f0ff"; ctx.font = "11px 'JetBrains Mono', monospace";
      ctx.fillText("λ = h / p = h / √(2m·q·V_a)", 215, 182);
      ctx.fillStyle = "#94a3b8"; ctx.font = "10px sans-serif";
      ctx.fillText("สมมาตรของธรรมชาติ: เมื่อคลื่นแสงเป็นโฟตอนได้ สสารก็ประพฤติเป็นคลื่นได้", 215, 202);

      tick++;
      requestAnimationFrame(animate);
    }
    animate();
"""

# ==============================================================================
# 3.2 Particle Diffraction: Davisson-Germer & Double-Slit
# ==============================================================================
body_3_2 = """
  <div class="sim-card">
    <div class="sim-header">
      <div class="sim-title"><span>🔬</span> 3.2 การเลี้ยวเบนของอนุภาค: การทดลองเดวิสสัน-เกอร์เมอร์ & สลิตคู่ควอนตัม</div>
      <div class="badge-fps">● 60 FPS REAL-TIME</div>
    </div>
    <div class="tab-bar">
      <button class="tab-btn active" id="tabDG" onclick="setMode('dg')">🎯 การทดลองเดวิสสัน-เกอร์เมอร์ (Davisson-Germer)</button>
      <button class="tab-btn" id="tabSlit" onclick="setMode('slit')">✨ สลิตคู่อิเล็กตรอนทีละตัว (Double Slit)</button>
    </div>
    <div id="controlsDG" class="control-grid">
      <div class="ctrl-box">
        <label>ความต่างศักย์เร่งอิเล็กตรอน (V_a): <span id="val_dg_va" class="val-display">54</span> V</label>
        <input type="range" id="slider_dg_va" min="40" max="68" step="1" value="54">
      </div>
      <div class="ctrl-box">
        <label>มุมตรวจจับการกระเจิง (θ): <span id="val_dg_theta" class="val-display">50</span>°</label>
        <input type="range" id="slider_dg_theta" min="20" max="85" step="1" value="50">
      </div>
    </div>
    <div id="controlsSlit" class="control-grid" style="display:none;">
      <div class="ctrl-box">
        <label>อัตราการยิงอิเล็กตรอน (Electrons/frame): <span id="val_rate" class="val-display">5</span> ตัว/เฟรม</label>
        <input type="range" id="slider_rate" min="1" max="25" step="1" value="5">
      </div>
      <div class="ctrl-box">
        <button type="button" onclick="resetSlit()" style="background:#0284c7; color:#fff; border:none; padding:8px 16px; border-radius:6px; font-weight:700; cursor:pointer; font-family:'Sarabun', sans-serif; margin-top:10px;">🔄 รีเซ็ตฉากรับ (Clear Screen)</button>
      </div>
    </div>
    <div class="canvas-box"><canvas id="simCanvas" width="640" height="230"></canvas></div>
    <div class="readout-grid" id="readoutsDG">
      <div class="readout-card"><div class="readout-val" id="val_dg_lam">0.167 nm</div><div class="readout-lbl">ความยาวคลื่นเดอบรอยล์ (λ)</div></div>
      <div class="readout-card"><div class="readout-val" id="val_dg_bragg">0.165 nm</div><div class="readout-lbl">ความยาวคลื่นจากการเลี้ยวเบน Bragg</div></div>
      <div class="readout-card"><div class="readout-val" id="val_dg_status" style="color:#10b981;">พีคสูงสุดที่ 54V & 50°</div><div class="readout-lbl">การแทรกสอดแบบเสริมกัน!</div></div>
    </div>
    <div class="readout-grid" id="readoutsSlit" style="display:none;">
      <div class="readout-card"><div class="readout-val" id="val_tot_hits">0</div><div class="readout-lbl">จำนวนอิเล็กตรอนสะสม (Hits)</div></div>
      <div class="readout-card"><div class="readout-val" id="val_slit_status" style="color:#00f0ff;">ริ้วแทรกสอดเริ่มก่อตัว</div><div class="readout-lbl">พฤติกรรมคลื่นของอิเล็กตรอนเดี่ยว</div></div>
      <div class="readout-card"><div class="readout-val" id="val_pattern" style="color:#10b981;">Wave-Particle Duality</div><div class="readout-lbl">ข้อสรุปทวิภาวะ</div></div>
    </div>
  </div>
"""

js_3_2 = """
    const cv = document.getElementById("simCanvas");
    const ctx = cv.getContext("2d");
    let currentMode = "dg";
    let tick = 0;
    let hitCount = 0;
    let hitPoints = [];

    function setMode(mode) {
      currentMode = mode;
      document.getElementById("tabDG").classList.toggle("active", mode === "dg");
      document.getElementById("tabSlit").classList.toggle("active", mode === "slit");
      document.getElementById("controlsDG").style.display = mode === "dg" ? "grid" : "none";
      document.getElementById("controlsSlit").style.display = mode === "slit" ? "grid" : "none";
      document.getElementById("readoutsDG").style.display = mode === "dg" ? "grid" : "none";
      document.getElementById("readoutsSlit").style.display = mode === "slit" ? "grid" : "none";
    }

    function resetSlit() {
      hitCount = 0;
      hitPoints = [];
    }

    function animate() {
      ctx.clearRect(0, 0, cv.width, cv.height);

      if (currentMode === "dg") {
        const Va = +document.getElementById("slider_dg_va").value;
        const theta = +document.getElementById("slider_dg_theta").value;

        document.getElementById("val_dg_va").textContent = Va;
        document.getElementById("val_dg_theta").textContent = theta;

        const lambda_nm = 1.226 / Math.sqrt(Va);
        // Bragg condition for Nickel (D = 0.215 nm): lambda = D * sin(theta)
        const D = 0.215; // nm
        const bragg_lam = D * Math.sin(theta * Math.PI / 180);

        document.getElementById("val_dg_lam").textContent = lambda_nm.toFixed(3) + " nm";
        document.getElementById("val_dg_bragg").textContent = bragg_lam.toFixed(3) + " nm";

        // Intensity model centered at 54V and 50 deg
        const diffV = (Va - 54) / 4.0;
        const diffT = (theta - 50) / 6.0;
        const intensity = Math.exp(-(diffV*diffV + diffT*diffT));

        const statEl = document.getElementById("val_dg_status");
        if (intensity > 0.7) {
          statEl.textContent = "พีคสูงสุดที่ 54V & 50° (ตรงกัน 100%)"; statEl.style.color = "#10b981";
        } else {
          statEl.textContent = "ความเข้มต่ำ (" + (intensity*100).toFixed(0) + "%)"; statEl.style.color = "#f59e0b";
        }

        // Left Panel: Apparatus
        const gunX = 50, targetX = 170, targetY = 115;

        // Electron Gun
        ctx.fillStyle = "#334155"; ctx.fillRect(gunX, targetY - 12, 35, 24);
        ctx.fillStyle = "#38bdf8"; ctx.font = "9px sans-serif"; ctx.fillText("Gun (" + Va + "V)", gunX + 2, targetY + 4);

        // Nickel Crystal Target
        ctx.fillStyle = "#64748b"; ctx.fillRect(targetX, targetY - 40, 20, 80);
        ctx.fillStyle = "#00f0ff"; ctx.fillText("Nickel Crystal", targetX - 10, targetY + 55);

        // Incoming Beam
        ctx.strokeStyle = "#38bdf8"; ctx.lineWidth = 2.5;
        ctx.beginPath(); ctx.moveTo(gunX + 35, targetY); ctx.lineTo(targetX, targetY); ctx.stroke();

        // Scattered Beam at angle theta
        const rad = theta * Math.PI / 180;
        const detR = 95;
        const detX = targetX - detR * Math.cos(rad);
        const detY = targetY - detR * Math.sin(rad);

        ctx.strokeStyle = "rgba(16, 185, 129, " + (0.3 + intensity*0.7) + ")";
        ctx.lineWidth = 2 + intensity * 3;
        ctx.beginPath(); ctx.moveTo(targetX, targetY); ctx.lineTo(detX, detY); ctx.stroke();

        // Movable Detector
        ctx.fillStyle = "#10b981";
        ctx.beginPath(); ctx.arc(detX, detY, 6, 0, Math.PI*2); ctx.fill();
        ctx.fillStyle = "#ffffff"; ctx.font = "10px sans-serif"; ctx.fillText(theta + "°", detX - 12, detY - 8);

        // Right Panel: Polar Intensity Plot
        const ox = 420, oy = 175, pr = 135;
        ctx.fillStyle = "#0f172a"; ctx.strokeStyle = "#1e293b";
        ctx.fillRect(290, 20, 330, 185); ctx.strokeRect(290, 20, 330, 185);

        ctx.fillStyle = "#94a3b8"; ctx.font = "11px sans-serif";
        ctx.fillText("กราฟเชิงขั้วแสดงความเข้มของอิเล็กตรอนกระเจิง (I vs θ)", 305, 38);

        // Polar curve for current Va
        ctx.strokeStyle = "#00f0ff"; ctx.lineWidth = 2.5;
        ctx.beginPath();
        for(let a = 20; 85 >= a; a += 1) {
          const arad = a * Math.PI / 180;
          const dV = (Va - 54) / 4.0;
          const dT = (a - 50) / 6.0;
          const I_a = 0.2 + 0.8 * Math.exp(-(dV*dV + dT*dT));
          const r_len = I_a * 105;
          const px = 460 - r_len * Math.cos(arad);
          const py = oy - r_len * Math.sin(arad);
          if (a === 20) ctx.moveTo(px, py); else ctx.lineTo(px, py);
        }
        ctx.stroke();

        // Target center dot in polar
        ctx.fillStyle = "#f59e0b"; ctx.beginPath(); ctx.arc(460, oy, 4, 0, Math.PI*2); ctx.fill();
      }
      else {
        // Double-slit electron accumulation mode
        const rate = +document.getElementById("slider_rate").value;
        document.getElementById("val_rate").textContent = rate;

        // Add hits based on theoretical wave probability: I(y) ~ cos^2(ky)
        for(let r=0; rate > r; r++) {
          hitCount++;
          // Rejection sampling for double slit fringe distribution
          let py = 0, prob = 0;
          while(true) {
            py = (Math.random() - 0.5) * 160;
            prob = Math.pow(Math.cos(py * 0.09), 2) * Math.exp(-py*py / 3500);
            if (Math.random() < prob) break;
          }
          hitPoints.push({ x: 540 + Math.random()*25, y: 115 + py });
        }

        document.getElementById("val_tot_hits").textContent = hitCount.toLocaleString();

        // Left: Electron Gun & Double Slit
        ctx.fillStyle = "#334155"; ctx.fillRect(30, 100, 30, 30);
        ctx.fillStyle = "#38bdf8"; ctx.font = "9px sans-serif"; ctx.fillText("Gun", 36, 118);

        // Slits Barrier
        ctx.fillStyle = "#475569";
        ctx.fillRect(220, 25, 10, 75);
        ctx.fillRect(220, 107, 10, 16);
        ctx.fillRect(220, 130, 10, 75);

        ctx.fillStyle = "#94a3b8"; ctx.font = "10px sans-serif";
        ctx.fillText("สลิตคู่ (Double Slit)", 180, 20);

        // Incoming matter waves
        ctx.strokeStyle = "rgba(0, 240, 255, 0.4)"; ctx.lineWidth = 1.5;
        for(let w=0; 5 > w; w++) {
          const wx = 65 + ((tick*3 + w*30) % 150);
          ctx.beginPath(); ctx.moveTo(wx, 50); ctx.lineTo(wx, 180); ctx.stroke();
        }

        // Emerging circular waves from slits
        ctx.strokeStyle = "rgba(16, 185, 129, 0.35)"; ctx.lineWidth = 1.2;
        for(let c=0; 4 > c; c++) {
          const cr = ((tick*2.5 + c*35) % 180);
          ctx.beginPath(); ctx.arc(225, 103, cr, -Math.PI/2.5, Math.PI/2.5); ctx.stroke();
          ctx.beginPath(); ctx.arc(225, 127, cr, -Math.PI/2.5, Math.PI/2.5); ctx.stroke();
        }

        // Right: Detector Screen with hit points
        ctx.fillStyle = "#030712"; ctx.strokeStyle = "#00f0ff"; ctx.lineWidth = 1.5;
        ctx.fillRect(530, 25, 80, 180); ctx.strokeRect(530, 25, 80, 180);

        ctx.fillStyle = "#10b981";
        hitPoints.slice(-1500).forEach(pt => {
          ctx.fillRect(pt.x, pt.y, 1.8, 1.8);
        });
      }

      tick++;
      requestAnimationFrame(animate);
    }
    animate();
"""

# ==============================================================================
# 3.3 Wave Packets & Heisenberg Uncertainty Principle
# ==============================================================================
body_3_3 = """
  <div class="sim-card">
    <div class="sim-header">
      <div class="sim-title"><span>🔬</span> 3.3 กลุ่มคลื่น & หลักความไม่แน่นอนของไฮเซนเบิร์ก (Heisenberg Uncertainty)</div>
      <div class="badge-fps">● 60 FPS REAL-TIME</div>
    </div>
    <div class="control-grid">
      <div class="ctrl-box">
        <label>ความไม่แน่นอนของตำแหน่ง (Δx): <span id="val_dx" class="val-display">1.0</span> nm</label>
        <input type="range" id="slider_dx" min="0.2" max="3.0" step="0.1" value="1.0">
      </div>
      <div class="ctrl-box">
        <label>ความเร็วกลุ่มของอนุภาค (v_group): <span id="val_vg" class="val-display">2.0</span> × 10⁶ m/s</label>
        <input type="range" id="slider_vg" min="0.5" max="5.0" step="0.1" value="2.0">
      </div>
    </div>
    <div class="canvas-box"><canvas id="simCanvas" width="640" height="230"></canvas></div>
    <div class="readout-grid">
      <div class="readout-card"><div class="readout-val" id="val_dp">0.527 × 10⁻²⁴</div><div class="readout-lbl">ความไม่แน่นอนโมเมนตัม (Δp ≥ ℏ/(2Δx))</div></div>
      <div class="readout-card"><div class="readout-val" id="val_prod">0.527 × 10⁻³⁴</div><div class="readout-lbl">ผลคูณความไม่แน่นอน (Δx·Δp ≥ ℏ/2)</div></div>
      <div class="readout-card"><div class="readout-val" id="val_status" style="color:#10b981;">สอดคล้องกับขีดจำกัดควอนตัม</div><div class="readout-lbl">สถานะหลักความไม่แน่นอน</div></div>
    </div>
  </div>
"""

js_3_3 = """
    const cv = document.getElementById("simCanvas");
    const ctx = cv.getContext("2d");
    const sliderDx = document.getElementById("slider_dx");
    const sliderVg = document.getElementById("slider_vg");
    let tick = 0;

    function animate() {
      const dx_nm = +sliderDx.value;
      const vg_unit = +sliderVg.value;

      document.getElementById("val_dx").textContent = dx_nm.toFixed(1);
      document.getElementById("val_vg").textContent = vg_unit.toFixed(1);

      // hbar = 1.0545718e-34
      const dx_m = dx_nm * 1e-9;
      const dp_min = 1.0545718e-34 / (2 * dx_m);
      const prod = dx_m * dp_min;

      document.getElementById("val_dp").textContent = (dp_min * 1e24).toFixed(3) + " × 10⁻²⁴";
      document.getElementById("val_prod").textContent = (prod * 1e34).toFixed(3) + " × 10⁻³⁴";

      ctx.clearRect(0, 0, cv.width, cv.height);

      // Top Half: Wave Packet in Position Space (Psi(x))
      const topY = 70;
      ctx.fillStyle = "#94a3b8"; ctx.font = "11px sans-serif";
      ctx.fillText("ฟังก์ชันคลื่นกลุ่มในปริภูมิตำแหน่ง Ψ(x) [ตำแหน่งแน่นอนขึ้น = คลื่นบีบแคบ]", 30, 22);

      // Center position traveling with group velocity vg
      const packetX = 80 + ((tick * vg_unit * 1.2) % 480);
      const sigmaX = dx_nm * 25; // pixel width

      // Envelope and Carrier Waves
      ctx.strokeStyle = "#00f0ff"; ctx.lineWidth = 2.5;
      ctx.beginPath();
      for(let x = 30; 600 >= x; x += 2) {
        const dist = (x - packetX) / sigmaX;
        const envelope = Math.exp(-dist * dist / 2);
        const carrier = Math.sin((x - tick * vg_unit * 2.8) * 0.22);
        const y = topY - envelope * carrier * 38;
        if (x === 30) ctx.moveTo(x, y); else ctx.lineTo(x, y);
      }
      ctx.stroke();

      // Envelope Dotted Line
      ctx.strokeStyle = "rgba(245, 158, 11, 0.6)"; ctx.lineWidth = 1.5; ctx.setLineDash([3, 3]);
      ctx.beginPath();
      for(let x = 30; 600 >= x; x += 2) {
        const dist = (x - packetX) / sigmaX;
        const envelope = Math.exp(-dist * dist / 2);
        const y = topY - envelope * 38;
        if (x === 30) ctx.moveTo(x, y); else ctx.lineTo(x, y);
      }
      ctx.stroke(); ctx.setLineDash([]);

      // Width indicator (Delta x)
      ctx.strokeStyle = "#f59e0b"; ctx.lineWidth = 2;
      ctx.beginPath(); ctx.moveTo(packetX - sigmaX, topY + 42); ctx.lineTo(packetX + sigmaX, topY + 42); ctx.stroke();
      ctx.fillStyle = "#f59e0b"; ctx.font = "10px sans-serif";
      ctx.fillText("Δx = " + dx_nm.toFixed(1) + " nm", packetX - 25, topY + 56);

      // Divider line
      ctx.strokeStyle = "#1e293b"; ctx.lineWidth = 1.5;
      ctx.beginPath(); ctx.moveTo(30, 138); ctx.lineTo(610, 138); ctx.stroke();

      // Bottom Half: Momentum Spread in Momentum Space (Phi(p))
      const botY = 195;
      ctx.fillStyle = "#94a3b8"; ctx.font = "11px sans-serif";
      ctx.fillText("การแจกแจงโมเมนตัม Φ(p) [ยิ่ง Δx แคบ → Δp ยิ่งกว้างขึ้นตามการแปลงฟูเรียร์]", 30, 154);

      const sigmaP = (1.0 / dx_nm) * 45; // pixel width inversely proportional to dx!
      const pCenterX = 320;

      ctx.fillStyle = "rgba(16, 185, 129, 0.25)"; ctx.strokeStyle = "#10b981"; ctx.lineWidth = 2;
      ctx.beginPath(); ctx.moveTo(120, botY);
      for(let px = 120; 520 >= px; px += 2) {
        const distP = (px - pCenterX) / sigmaP;
        const envP = Math.exp(-distP * distP / 2);
        const yP = botY - envP * 34;
        ctx.lineTo(px, yP);
      }
      ctx.lineTo(520, botY); ctx.closePath(); ctx.fill(); ctx.stroke();

      ctx.fillStyle = "#10b981"; ctx.font = "10px sans-serif";
      ctx.fillText("Δp = " + (dp_min*1e24).toFixed(2) + " × 10⁻²⁴ kg·m/s", pCenterX - 60, botY + 14);

      tick++;
      requestAnimationFrame(animate);
    }
    animate();
"""

# ==============================================================================
# 3.4 Applications: Electron Microscope SEM/TEM & Atomic Resolution
# ==============================================================================
body_3_4 = """
  <div class="sim-card">
    <div class="sim-header">
      <div class="sim-title"><span>🔬</span> 3.4 การประยุกต์ใช้: กล้องจุลทรรศน์อิเล็กตรอน (TEM/SEM) & กำลังแยกขยายอะตอม</div>
      <div class="badge-fps">● 60 FPS REAL-TIME</div>
    </div>
    <div class="control-grid">
      <div class="ctrl-box">
        <label>แรงดันเร่งลำอิเล็กตรอน (V_acc): <span id="val_vacc" class="val-display">100</span> kV</label>
        <input type="range" id="slider_vacc" min="10" max="300" step="10" value="100">
      </div>
      <div class="ctrl-box">
        <label>โหมดกล้องเปรียบเทียบ:</label>
        <select id="sel_microscope">
          <option value="tem" selected>กล้องจุลทรรศน์อิเล็กตรอน TEM (λ = 0.0037 nm)</option>
          <option value="optical">กล้องจุลทรรศน์ใช้แสง Optical Light (λ = 500 nm)</option>
        </select>
      </div>
    </div>
    <div class="canvas-box"><canvas id="simCanvas" width="640" height="230"></canvas></div>
    <div class="readout-grid">
      <div class="readout-card"><div class="readout-val" id="val_lam_tem">0.00388 nm</div><div class="readout-lbl">ความยาวคลื่นลำแสง (λ)</div></div>
      <div class="readout-card"><div class="readout-val" id="val_res">0.12 nm (ระดับอะตอม)</div><div class="readout-lbl">ขีดจำกัดกำลังแยกขยาย (Abbe Limit)</div></div>
      <div class="readout-card"><div class="readout-val" id="val_mag" style="color:#10b981;">1,000,000 ×</div><div class="readout-lbl">กำลังขยายสูงสุด (Magnification)</div></div>
    </div>
  </div>
"""

js_3_4 = """
    const cv = document.getElementById("simCanvas");
    const ctx = cv.getContext("2d");
    const sliderVacc = document.getElementById("slider_vacc");
    const selMicro = document.getElementById("sel_microscope");
    let tick = 0;

    function animate() {
      const mode = selMicro.value;
      const Vacc_kV = +sliderVacc.value;
      document.getElementById("val_vacc").textContent = Vacc_kV;

      let lambda_nm, resolution_nm, magText;
      if (mode === "tem") {
        // Relativistic de Broglie: lambda = 1.226 / sqrt(V * (1 + 0.978e-6 * V))
        const V_volts = Vacc_kV * 1000;
        lambda_nm = 1.226 / Math.sqrt(V_volts * (1 + 0.978e-6 * V_volts));
        resolution_nm = 0.61 * lambda_nm / 0.02; // NA ~ 0.02 for EM lenses
        magText = (Vacc_kV * 10000).toLocaleString() + " ×";

        document.getElementById("val_lam_tem").textContent = lambda_nm.toFixed(5) + " nm";
        document.getElementById("val_res").textContent = resolution_nm.toFixed(2) + " nm (ระดับอะตอม)";
        document.getElementById("val_mag").textContent = magText;
        document.getElementById("val_mag").style.color = "#10b981";
      } else {
        lambda_nm = 500;
        resolution_nm = 0.61 * 500 / 1.4; // NA ~ 1.4 for Oil immersion
        document.getElementById("val_lam_tem").textContent = "500 nm (แสงเขียว)";
        document.getElementById("val_res").textContent = resolution_nm.toFixed(0) + " nm (ติดกำแพงเลี้ยวเบน)";
        document.getElementById("val_mag").textContent = "1,500 × (ขีดจำกัดแสง)";
        document.getElementById("val_mag").style.color = "#f43f5e";
      }

      ctx.clearRect(0, 0, cv.width, cv.height);

      // Left Panel: Column Schematic
      const colX = 100, colY = 20, colW = 60, colH = 185;
      ctx.fillStyle = "#0f172a"; ctx.strokeStyle = "#334155"; ctx.lineWidth = 1.5;
      ctx.fillRect(colX, colY, colW, colH); ctx.strokeRect(colX, colY, colW, colH);

      // Electron Gun at top
      ctx.fillStyle = mode === "tem" ? "#00f0ff" : "#f59e0b";
      ctx.fillRect(colX + 15, colY + 8, 30, 12);
      ctx.fillStyle = "#ffffff"; ctx.font = "8px sans-serif"; ctx.fillText(mode === "tem" ? "E-Gun" : "Lamp", colX + 18, colY + 17);

      // Magnetic Lenses
      ctx.fillStyle = "#475569";
      ctx.fillRect(colX + 5, colY + 45, 12, 16); ctx.fillRect(colX + colW - 17, colY + 45, 12, 16); // Condenser
      ctx.fillRect(colX + 5, colY + 115, 12, 16); ctx.fillRect(colX + colW - 17, colY + 115, 12, 16); // Objective

      // Specimen stage
      ctx.fillStyle = "#ef4444"; ctx.fillRect(colX + 10, colY + 85, 40, 4);

      // Ray beams
      ctx.strokeStyle = mode === "tem" ? "rgba(0, 240, 255, 0.7)" : "rgba(245, 158, 11, 0.7)";
      ctx.lineWidth = 1.8;
      ctx.beginPath();
      ctx.moveTo(colX + 30, colY + 20);
      ctx.lineTo(colX + 20, colY + 85); ctx.lineTo(colX + 30, colY + 175);
      ctx.moveTo(colX + 30, colY + 20);
      ctx.lineTo(colX + 40, colY + 85); ctx.lineTo(colX + 30, colY + 175);
      ctx.stroke();

      // Right Panel: Specimen View Screen (Comparison)
      const scrX = 230, scrY = 25, scrW = 380, scrH = 175;
      ctx.fillStyle = "#020617"; ctx.strokeStyle = "#1e293b"; ctx.lineWidth = 1.5;
      ctx.fillRect(scrX, scrY, scrW, scrH); ctx.strokeRect(scrX, scrY, scrW, scrH);

      ctx.fillStyle = "#94a3b8"; ctx.font = "11px sans-serif";
      ctx.fillText("ภาพจำลองตัวอย่างผลึกซิลิกอน (Silicon Crystal Lattice View)", scrX + 15, scrY + 20);

      if (mode === "tem") {
        // TEM mode: Crisp sharp atomic grid
        for(let r=0; 6 > r; r++) {
          for(let c=0; 12 > c; c++) {
            const ax = scrX + 35 + c * 28;
            const ay = scrY + 45 + r * 22;
            const glow = ctx.createRadialGradient(ax, ay, 1, ax, ay, 8);
            glow.addColorStop(0, "#00f0ff");
            glow.addColorStop(0.5, "rgba(0, 240, 255, 0.4)");
            glow.addColorStop(1, "transparent");
            ctx.fillStyle = glow;
            ctx.beginPath(); ctx.arc(ax, ay, 8, 0, Math.PI*2); ctx.fill();

            ctx.fillStyle = "#ffffff";
            ctx.beginPath(); ctx.arc(ax, ay, 2.5, 0, Math.PI*2); ctx.fill();
          }
        }
        ctx.fillStyle = "#10b981"; ctx.font = "bold 11px sans-serif";
        ctx.fillText("✓ มองเห็นระนาบอะตอมเดี่ยวคมชัด 100% (Atomic Lattice Resolution)", scrX + 15, scrY + scrH - 12);
      } else {
        // Optical mode: Blurred diffraction blob
        const blurGrad = ctx.createRadialGradient(scrX + scrW/2, scrY + scrH/2, 20, scrX + scrW/2, scrY + scrH/2, 110);
        blurGrad.addColorStop(0, "rgba(245, 158, 11, 0.8)");
        blurGrad.addColorStop(0.6, "rgba(239, 68, 68, 0.3)");
        blurGrad.addColorStop(1, "transparent");
        ctx.fillStyle = blurGrad;
        ctx.fillRect(scrX + 15, scrY + 35, scrW - 30, scrH - 55);

        ctx.fillStyle = "#f43f5e"; ctx.font = "bold 11px sans-serif";
        ctx.fillText("✗ มัวและเบลอเนื่องจากขีดจำกัดการเลี้ยวเบนของแสง (λ แสง > 500 nm)", scrX + 15, scrY + scrH - 12);
      }

      tick++;
      requestAnimationFrame(animate);
    }
    animate();
"""

# ==============================================================================
# 3.5 Virtual Lab: Energy-Time Uncertainty & Standing Matter Waves
# ==============================================================================
body_3_5 = """
  <div class="sim-card">
    <div class="sim-header">
      <div class="sim-title"><span>🔬</span> 3.5 ปฏิบัติการควอนตัม: ความไม่แน่นอนพลังงาน-เวลา & คลื่นนิ่งของสสาร</div>
      <div class="badge-fps">● 60 FPS REAL-TIME</div>
    </div>
    <div class="tab-bar">
      <button class="tab-btn active" id="tabVac" onclick="setMode('vac')">🌌 สุญญากาศควอนตัม (Quantum Vacuum Fluctuations)</button>
      <button class="tab-btn" id="tabWell" onclick="setMode('well')">🌊 คลื่นนิ่งในกล่องศักย์ (Standing Matter Waves)</button>
    </div>
    <div id="controlsVac" class="control-grid">
      <div class="ctrl-box">
        <label>พลังงานความผันผวนควอนตัม (ΔE): <span id="val_de" class="val-display">1.02</span> MeV (มวลคู่อิเล็กตรอน e⁺e⁻)</label>
        <input type="range" id="slider_de" min="0.5" max="5.0" step="0.1" value="1.02">
      </div>
      <div class="ctrl-box">
        <label>อนุภาคเสมือน (Virtual Particles):</label>
        <div style="color:#94a3b8; font-size:0.80rem; margin-top:4px;">กำเนิดและสลายตัวภายในเวลา Δt ≤ ℏ/(2ΔE)</div>
      </div>
    </div>
    <div id="controlsWell" class="control-grid" style="display:none;">
      <div class="ctrl-box">
        <label>เลขควอนตัมของคลื่นนิ่ง (n): <span id="val_n" class="val-display">3</span> (มี 3 ลูป)</label>
        <input type="range" id="slider_n" min="1" max="6" step="1" value="3">
      </div>
      <div class="ctrl-box">
        <label>ความกว้างกล่องศักย์ (L): 1.0 nm</label>
        <div style="color:#94a3b8; font-size:0.80rem; margin-top:4px;">เงื่อนไขคลื่นนิ่ง: L = n·(λ/2) → ควอนไทเซชันของพลังงาน</div>
      </div>
    </div>
    <div class="canvas-box"><canvas id="simCanvas" width="640" height="230"></canvas></div>
    <div class="readout-grid" id="readoutsVac">
      <div class="readout-card"><div class="readout-val" id="val_dt">3.22 × 10⁻²² s</div><div class="readout-lbl">อายุขัยสูงสุดอนุภาคเสมือน (Δt ≤ ℏ/2ΔE)</div></div>
      <div class="readout-card"><div class="readout-val" id="val_pairs">e⁻ + e⁺</div><div class="readout-lbl">คู่อนุภาค-ปฏิยานุภาคที่เกิดขึ้น</div></div>
      <div class="readout-card"><div class="readout-val" id="val_vac_stat" style="color:#10b981;">อนุรักษ์พลังงานในกรอบ Δt</div><div class="readout-lbl">หลักความไม่แน่นอนพลังงาน-เวลา</div></div>
    </div>
    <div class="readout-grid" id="readoutsWell" style="display:none;">
      <div class="readout-card"><div class="readout-val" id="val_well_lam">0.667 nm</div><div class="readout-lbl">ความยาวคลื่นเดอบรอยล์ (λ = 2L/n)</div></div>
      <div class="readout-card"><div class="readout-val" id="val_well_nodes">4 บัพ (Nodes)</div><div class="readout-lbl">จุดตรึงของฟังก์ชันคลื่น</div></div>
      <div class="readout-card"><div class="readout-val" id="val_well_e">3.38 eV</div><div class="readout-lbl">ระดับพลังงานควอนไทซ์ (E_n = n²·E₁)</div></div>
    </div>
  </div>
"""

js_3_5 = """
    const cv = document.getElementById("simCanvas");
    const ctx = cv.getContext("2d");
    let currentMode = "vac";
    let tick = 0;

    function setMode(mode) {
      currentMode = mode;
      document.getElementById("tabVac").classList.toggle("active", mode === "vac");
      document.getElementById("tabWell").classList.toggle("active", mode === "well");
      document.getElementById("controlsVac").style.display = mode === "vac" ? "grid" : "none";
      document.getElementById("controlsWell").style.display = mode === "well" ? "grid" : "none";
      document.getElementById("readoutsVac").style.display = mode === "vac" ? "grid" : "none";
      document.getElementById("readoutsWell").style.display = mode === "well" ? "grid" : "none";
    }

    let vPairs = [];
    for(let i=0; 12 > i; i++) {
      vPairs.push({
        x: 60 + Math.random()*520,
        y: 40 + Math.random()*150,
        birth: Math.random()*60
      });
    }

    function animate() {
      ctx.clearRect(0, 0, cv.width, cv.height);

      if (currentMode === "vac") {
        const dE_MeV = +document.getElementById("slider_de").value;
        document.getElementById("val_de").textContent = dE_MeV.toFixed(2);

        // dt = hbar / (2 * dE)
        const dE_Joules = dE_MeV * 1e6 * 1.602e-19;
        const dt_s = 1.0545718e-34 / (2 * dE_Joules);

        document.getElementById("val_dt").textContent = (dt_s * 1e22).toFixed(2) + " × 10⁻²² s";

        // Virtual pairs bubbling
        ctx.fillStyle = "rgba(148, 163, 184, 0.08)";
        ctx.fillRect(0, 0, cv.width, cv.height);

        vPairs.forEach(p => {
          const age = (tick - p.birth) % 40;
          if (age > 0 && 35 > age) {
            const sep = (age / 35) * 22;
            // Electron e- (Cyan)
            ctx.fillStyle = "#00f0ff";
            ctx.beginPath(); ctx.arc(p.x - sep, p.y, 4, 0, Math.PI*2); ctx.fill();
            // Positron e+ (Pink)
            ctx.fillStyle = "#f43f5e";
            ctx.beginPath(); ctx.arc(p.x + sep, p.y, 4, 0, Math.PI*2); ctx.fill();

            ctx.strokeStyle = "rgba(255, 255, 255, 0.3)"; ctx.lineWidth = 1;
            ctx.beginPath(); ctx.moveTo(p.x - sep, p.y); ctx.lineTo(p.x + sep, p.y); ctx.stroke();
          } else if (age >= 35) {
            p.x = 60 + Math.random()*520;
            p.y = 40 + Math.random()*150;
            p.birth = tick;
          }
        });

        ctx.fillStyle = "#94a3b8"; ctx.font = "11px sans-serif";
        ctx.fillText("สุญญากาศควอนตัมไม่เคยว่างเปล่า: คู่อนุภาคเสมือน (e⁻ / e⁺) ผุดขึ้นและสลายตัวภายในเวลา Δt", 40, 25);
      }
      else {
        // Standing Matter Wave in Infinite Well
        const n = +document.getElementById("slider_n").value;
        document.getElementById("val_n").textContent = n;

        const L = 1.0; // nm
        const lambda = (2 * L) / n;
        const E1 = 0.376; // eV for 1 nm well
        const En = n * n * E1;

        document.getElementById("val_well_lam").textContent = lambda.toFixed(3) + " nm";
        document.getElementById("val_well_nodes").textContent = (n + 1) + " บัพ (Nodes)";
        document.getElementById("val_well_e").textContent = En.toFixed(2) + " eV";

        const ox = 90, oy = 115, boxW = 460;

        // Hard Walls
        ctx.fillStyle = "#334155";
        ctx.fillRect(ox - 10, 30, 10, 160);
        ctx.fillRect(ox + boxW, 30, 10, 160);

        ctx.fillStyle = "#f43f5e"; ctx.font = "10px sans-serif";
        ctx.fillText("ผนังศักย์อนันต์ (x=0)", ox - 25, 22);
        ctx.fillText("ผนังศักย์อนันต์ (x=L)", ox + boxW - 25, 22);

        // Standing wave: psi(x, t) = A * sin(n*pi*x/L) * cos(omega*t)
        ctx.strokeStyle = "#00f0ff"; ctx.lineWidth = 3;
        ctx.beginPath();
        for(let px = 0; boxW >= px; px += 2) {
          const normX = px / boxW;
          const amp = Math.sin(n * Math.PI * normX) * Math.cos(tick * 0.08);
          const y = oy - amp * 55;
          if (px === 0) ctx.moveTo(ox + px, y); else ctx.lineTo(ox + px, y);
        }
        ctx.stroke();

        // Node indicators
        ctx.fillStyle = "#f59e0b";
        for(let k=0; n >= k; k++) {
          const nx = ox + (k / n) * boxW;
          ctx.beginPath(); ctx.arc(nx, oy, 4, 0, Math.PI*2); ctx.fill();
        }

        ctx.fillStyle = "#94a3b8"; ctx.font = "11px sans-serif";
        ctx.fillText("คลื่นนิ่งสสาร: ความยาวคลื่นที่พอดีขอบเขตนำไปสู่ 'การควอนไทซ์ของระดับพลังงาน' (E_n ∝ n²)", 75, 210);
      }

      tick++;
      requestAnimationFrame(animate);
    }
    animate();
"""

files = {
    "sim_3_1.html": wrap_html("3.1 สมมติฐานของเดอบรอยล์", body_3_1, js_3_1),
    "sim_3_2.html": wrap_html("3.2 การเลี้ยวเบนของอนุภาค", body_3_2, js_3_2),
    "sim_3_3.html": wrap_html("3.3 กลุ่มคลื่น & ความไม่แน่นอน", body_3_3, js_3_3),
    "sim_3_4.html": wrap_html("3.4 การประยุกต์ใช้ & กล้องจุลทรรศน์", body_3_4, js_3_4),
    "sim_3_5.html": wrap_html("3.5 ปฏิบัติการควอนตัม & คลื่นนิ่ง", body_3_5, js_3_5)
}

for fname, content in files.items():
    fpath = os.path.join(SIM_DIR, fname)
    with open(fpath, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"✅ Generated {fpath} ({len(content)} bytes)")

print("🎉 Successfully upgraded all Chapter 3 simulations to hyper-realistic 60 FPS engines!")
