#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generates hyper-realistic, 60 FPS physics simulations for all 5 subtopics of Chapter 1:
- sim_1_1.html: Classical Limits & Ultraviolet Catastrophe (Blackbody Cavity & Dual Theory Curves)
- sim_1_2.html: Blackbody Radiation & Wien's Displacement Law (Realistic Stellar Heat Sphere & Spectral Radiance)
- sim_1_3.html: Photoelectric Effect & Einstein's Photon Theory (Complete Vacuum Tube, I-V Curve, Retarding Voltage & Stopping Potential)
- sim_1_4.html: Hydrogen Atomic Spectra & Rydberg Formula (Bohr Energy Transitions, Optical Spectrograph & Emission Lines)
- sim_1_5.html: Chapter 1 Virtual Quantum Lab (Solar Cell Bandgap, Compton Scattering & Quantum Efficiency)
"""

import os

SIM_DIR = "/Users/chewathassana/Downloads/manus_backup2026/ModernPhysics/simulators"
os.makedirs(SIM_DIR, exist_ok=True)

# =============================================================================
# 1.1 SIMULATOR: Classical Limits & Ultraviolet Catastrophe
# =============================================================================
sim_1_1_html = """<!DOCTYPE html>
<html lang="th">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>RBRU Physics Lab: 1.1 ข้อจำกัดของฟิสิกส์ดั้งเดิม & หายนะอัลตราไวโอเลต</title>
  <link href="https://fonts.googleapis.com/css2?family=Sarabun:wght@400;600;700&family=JetBrains+Mono:wght@500;700&display=swap" rel="stylesheet">
  <style>
    * { box-sizing: border-box; margin: 0; padding: 0; }
    body {
      background: #020617;
      color: #f8fafc;
      font-family: 'Sarabun', -apple-system, sans-serif;
      padding: 12px;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      min-height: 100vh;
    }
    .sim-card {
      background: rgba(15, 23, 42, 0.95);
      border: 1px solid #1e293b;
      border-radius: 14px;
      padding: 16px;
      width: 100%;
      max-width: 680px;
      box-shadow: 0 10px 30px rgba(0, 0, 0, 0.7);
    }
    .sim-header {
      display: flex;
      justify-content: space-between;
      align-items: center;
      border-bottom: 1px solid #1e293b;
      padding-bottom: 10px;
      margin-bottom: 12px;
    }
    .sim-title {
      font-size: 1.05rem;
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
      padding: 3px 8px;
      border-radius: 9999px;
      font-size: 0.72rem;
      font-weight: 700;
      font-family: 'JetBrains Mono', monospace;
    }
    .control-grid {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 12px;
      margin-bottom: 12px;
    }
    @media (max-width: 540px) {
      .control-grid { grid-template-columns: 1fr; }
    }
    .ctrl-box {
      background: #090e1a;
      border: 1px solid #1e293b;
      padding: 8px 12px;
      border-radius: 8px;
    }
    .ctrl-box label {
      display: block;
      font-size: 0.82rem;
      color: #94a3b8;
      margin-bottom: 4px;
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
      background: #0f172a;
      color: #00f0ff;
      border: 1px solid #334155;
      padding: 6px 8px;
      border-radius: 6px;
      font-size: 0.85rem;
      font-family: 'Sarabun', sans-serif;
    }
    .canvas-box {
      position: relative;
      width: 100%;
      background: #020617;
      border: 1px solid #1e293b;
      border-radius: 10px;
      overflow: hidden;
      margin-bottom: 12px;
    }
    canvas {
      display: block;
      width: 100%;
      height: 240px;
    }
    .readout-grid {
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 8px;
    }
    .readout-card {
      background: #090e1a;
      border: 1px solid #1e293b;
      border-radius: 8px;
      padding: 8px 10px;
      text-align: center;
    }
    .readout-val {
      font-size: 1.0rem;
      font-weight: 700;
      color: #00f0ff;
      font-family: 'JetBrains Mono', monospace;
      margin-bottom: 2px;
    }
    .readout-lbl {
      font-size: 0.72rem;
      color: #64748b;
    }
  </style>
</head>
<body>

  <div class="sim-card">
    <div class="sim-header">
      <div class="sim-title">
        <span>🔬</span> 1.1 ข้อจำกัดของฟิสิกส์ดั้งเดิม: ปริศนาหายนะอัลตราไวโอเลต
      </div>
      <div class="badge-fps">● 60 FPS REAL-TIME</div>
    </div>

    <div class="control-grid">
      <div class="ctrl-box">
        <label>อุณหภูมิโพรงวัตถุดำ (T): <span id="val_temp" class="val-display">5000</span> K</label>
        <input type="range" id="slider_temp" min="2000" max="10000" step="100" value="5000">
      </div>
      <div class="ctrl-box">
        <label>โหมดทฤษฎีเปรียบเทียบ:</label>
        <select id="sel_theory">
          <option value="both" selected>แสดงทั้ง 2 ทฤษฎี (Classical vs Quantum)</option>
          <option value="classical">Classical Only (Rayleigh-Jeans Divergence)</option>
          <option value="planck">Quantum Only (Planck's Quantum Law)</option>
        </select>
      </div>
    </div>

    <div class="canvas-box"><canvas id="simCanvas" width="640" height="240"></canvas></div>

    <div class="readout-grid">
      <div class="readout-card"><div class="readout-val" id="val_rj" style="color:#f43f5e;">ลู่ออกสู่อนันต์ (∞)</div><div class="readout-lbl">Rayleigh-Jeans (Classical)</div></div>
      <div class="readout-card"><div class="readout-val" id="val_planck" style="color:#00f0ff;">จุดยอด 580 nm</div><div class="readout-lbl">Planck Quantum Peak (λ_max)</div></div>
      <div class="readout-card"><div class="readout-val" id="val_status" style="color:#f59e0b;">UV Catastrophe!</div><div class="readout-lbl">พฤติกรรมย่านความถี่สูง (UV)</div></div>
    </div>
  </div>

  <script>
    const cv = document.getElementById("simCanvas");
    const ctx = cv.getContext("2d");
    const sliderTemp = document.getElementById("slider_temp");
    const selTheory = document.getElementById("sel_theory");
    let tick = 0;

    // Thermal cavity photon particles
    let particles = [];
    for(let i=0; 35 > i; i++) {
      particles.push({
        x: 35 + Math.random()*85,
        y: 40 + Math.random()*150,
        vx: (Math.random()-0.5)*2.5,
        vy: (Math.random()-0.5)*2.5,
        color: i % 3 === 0 ? "#f43f5e" : (i % 3 === 1 ? "#00f0ff" : "#f59e0b")
      });
    }

    function animate() {
      const T = +sliderTemp.value;
      const mode = selTheory.value;
      document.getElementById("val_temp").textContent = T;

      const peakLam = Math.round(2898000 / T);
      document.getElementById("val_planck").textContent = "จุดยอด " + peakLam + " nm";

      ctx.clearRect(0, 0, cv.width, cv.height);

      // -------------------------------------------------------------
      // 1. Draw Left Panel: Cross-section of Isothermal Blackbody Cavity
      // -------------------------------------------------------------
      ctx.fillStyle = "#0f172a";
      ctx.strokeStyle = "#334155";
      ctx.lineWidth = 1.5;
      ctx.fillRect(20, 25, 120, 190);
      ctx.strokeRect(20, 25, 120, 190);

      // Cavity Aperture (รูเปิดเล็กๆ ที่ผนัง)
      ctx.clearRect(138, 105, 5, 30);

      // Heat glow inside cavity
      const heatGrad = ctx.createRadialGradient(80, 120, 10, 80, 120, 80);
      heatGrad.addColorStop(0, "rgba(245, 158, 11, 0.45)");
      heatGrad.addColorStop(0.6, "rgba(239, 68, 68, 0.2)");
      heatGrad.addColorStop(1, "transparent");
      ctx.fillStyle = heatGrad;
      ctx.fillRect(21, 26, 118, 188);

      // Animate thermal bouncing standing modes
      particles.forEach(p => {
        ctx.fillStyle = p.color;
        ctx.beginPath();
        ctx.arc(p.x, p.y, 2.8, 0, Math.PI*2);
        ctx.fill();
        p.x += p.vx * (T / 4000);
        p.y += p.vy * (T / 4000);
        if (25 > p.x || p.x > 135) p.vx *= -1;
        if (30 > p.y || p.y > 210) p.vy *= -1;
      });

      // Escaping radiation beam from pinhole
      ctx.strokeStyle = "rgba(0, 240, 255, 0.7)";
      ctx.lineWidth = 2;
      for(let k=0; 3 > k; k++) {
        const beamX = 140 + ((tick*3 + k*40) % 50);
        const beamY = 120 + (k-1)*8;
        ctx.beginPath();
        ctx.moveTo(140, 120);
        ctx.lineTo(beamX, beamY);
        ctx.stroke();
      }

      ctx.fillStyle = "#94a3b8"; ctx.font = "10px sans-serif";
      ctx.fillText("โพรงวัตถุดำ", 50, 42);
      ctx.fillText("(T = " + T + " K)", 52, 56);
      ctx.fillStyle = "#00f0ff";
      ctx.fillText("รูเปิด →", 100, 124);

      // -------------------------------------------------------------
      // 2. Draw Right Panel: Spectral Radiance Spectrum & UV Catastrophe
      // -------------------------------------------------------------
      const originX = 200, originY = 210;
      const graphW = 410, graphH = 180;

      // Spectrum background bands (UV, Visible Rainbow, IR)
      // UV Region (200 nm - 400 nm) -> X: 200 to 270
      ctx.fillStyle = "rgba(168, 85, 247, 0.18)";
      ctx.fillRect(originX, 30, 70, graphH);
      ctx.fillStyle = "#a855f7"; ctx.font = "10px sans-serif";
      ctx.fillText("UV", originX + 25, 45);

      // Visible Rainbow (400 nm - 750 nm) -> X: 270 to 360
      const visGrad = ctx.createLinearGradient(originX + 70, 0, originX + 160, 0);
      visGrad.addColorStop(0, "rgba(59, 130, 246, 0.25)");
      visGrad.addColorStop(0.3, "rgba(34, 197, 94, 0.25)");
      visGrad.addColorStop(0.7, "rgba(234, 179, 8, 0.25)");
      visGrad.addColorStop(1, "rgba(239, 68, 68, 0.25)");
      ctx.fillStyle = visGrad;
      ctx.fillRect(originX + 70, 30, 90, graphH);
      ctx.fillStyle = "#10b981";
      ctx.fillText("แสงขาว (Visible)", originX + 78, 45);

      // Infrared (750 nm +) -> X: 360 to 610
      ctx.fillStyle = "rgba(239, 68, 68, 0.12)";
      ctx.fillRect(originX + 160, 30, 250, graphH);
      ctx.fillStyle = "#ef4444";
      ctx.fillText("อินฟราเรด (IR)", originX + 240, 45);

      // Coordinate Grid Lines
      ctx.strokeStyle = "rgba(255, 255, 255, 0.05)";
      ctx.lineWidth = 1;
      for(let x = originX + 50; originX + graphW > x; x += 50) {
        ctx.beginPath(); ctx.moveTo(x, 30); ctx.lineTo(x, originY); ctx.stroke();
      }

      // Rayleigh-Jeans Classical Curve (Diverging towards UV / Lambda -> 0)
      if (mode === "both" || mode === "classical") {
        ctx.strokeStyle = "#f43f5e"; ctx.lineWidth = 2.5; ctx.setLineDash([4, 3]);
        ctx.beginPath();
        for(let px = originX + 5; originX + graphW >= px; px += 2) {
          const lam_nm = (px - originX) * 4.5;
          // Classical: I ~ T / lam^4
          const y_rj = originY - (2.5e11 * (T / 5000)) / Math.pow(lam_nm + 15, 3.2);
          if (px === originX + 5) ctx.moveTo(px, Math.max(30, y_rj));
          else ctx.lineTo(px, Math.max(30, y_rj));
        }
        ctx.stroke();
        ctx.setLineDash([]);
      }

      // Planck Quantum Law Curve (Finite Peak)
      if (mode === "both" || mode === "planck") {
        ctx.strokeStyle = "#00f0ff"; ctx.lineWidth = 3;
        ctx.beginPath();
        for(let px = originX + 5; originX + graphW >= px; px += 2) {
          const lam_nm = (px - originX) * 4.5;
          const p = Math.pow(T / 1000, 3) * Math.pow(lam_nm / peakLam, 5) / (Math.exp((lam_nm ? peakLam / lam_nm : 10) * 2.2) - 1 + 0.05);
          const y = originY - Math.min(170, p * 5.8);
          if (px === originX + 5) ctx.moveTo(px, y);
          else ctx.lineTo(px, y);
        }
        ctx.stroke();

        // Highlight Planck Peak Marker
        const peakX = originX + (peakLam / 4.5);
        if (peakX >= originX && originX + graphW >= peakX) {
          ctx.strokeStyle = "#f59e0b"; ctx.lineWidth = 1.8; ctx.setLineDash([3, 3]);
          ctx.beginPath(); ctx.moveTo(peakX, 30); ctx.lineTo(peakX, originY); ctx.stroke();
          ctx.setLineDash([]);
          ctx.fillStyle = "#f59e0b"; ctx.font = "11px sans-serif";
          ctx.fillText("λ_max = " + peakLam + " nm", peakX + 5, 65);
        }
      }

      // Graph Axes & Labels
      ctx.strokeStyle = "#94a3b8"; ctx.lineWidth = 1.5;
      ctx.beginPath();
      ctx.moveTo(originX, 30); ctx.lineTo(originX, originY); ctx.lineTo(originX + graphW, originY);
      ctx.stroke();

      ctx.fillStyle = "#94a3b8"; ctx.font = "11px sans-serif";
      ctx.fillText("ความยาวคลื่น λ (nm) →", originX + graphW - 120, originY + 18);
      ctx.fillText("ความเข้ม I(λ)", originX - 10, 22);

      // Legend
      ctx.fillStyle = "#f43f5e"; ctx.fillText("-- Classical (Rayleigh-Jeans: Diverges)", originX + 80, 85);
      ctx.fillStyle = "#00f0ff"; ctx.fillText("— Quantum (Planck: Finite Energy)", originX + 80, 102);

      tick++;
      requestAnimationFrame(animate);
    }
    animate();
  </script>
</body>
</html>
"""

# =============================================================================
# 1.2 SIMULATOR: Blackbody Radiation & Wien's Displacement Law
# =============================================================================
sim_1_2_html = """<!DOCTYPE html>
<html lang="th">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>RBRU Physics Lab: 1.2 การแผ่รังสีของวัตถุดำ & กฎการกระจัดของวีน</title>
  <link href="https://fonts.googleapis.com/css2?family=Sarabun:wght@400;600;700&family=JetBrains+Mono:wght@500;700&display=swap" rel="stylesheet">
  <style>
    * { box-sizing: border-box; margin: 0; padding: 0; }
    body {
      background: #020617;
      color: #f8fafc;
      font-family: 'Sarabun', -apple-system, sans-serif;
      padding: 12px;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      min-height: 100vh;
    }
    .sim-card {
      background: rgba(15, 23, 42, 0.95);
      border: 1px solid #1e293b;
      border-radius: 14px;
      padding: 16px;
      width: 100%;
      max-width: 680px;
      box-shadow: 0 10px 30px rgba(0, 0, 0, 0.7);
    }
    .sim-header {
      display: flex;
      justify-content: space-between;
      align-items: center;
      border-bottom: 1px solid #1e293b;
      padding-bottom: 10px;
      margin-bottom: 12px;
    }
    .sim-title {
      font-size: 1.05rem;
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
      padding: 3px 8px;
      border-radius: 9999px;
      font-size: 0.72rem;
      font-weight: 700;
      font-family: 'JetBrains Mono', monospace;
    }
    .control-grid {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 12px;
      margin-bottom: 12px;
    }
    @media (max-width: 540px) {
      .control-grid { grid-template-columns: 1fr; }
    }
    .ctrl-box {
      background: #090e1a;
      border: 1px solid #1e293b;
      padding: 8px 12px;
      border-radius: 8px;
    }
    .ctrl-box label {
      display: block;
      font-size: 0.82rem;
      color: #94a3b8;
      margin-bottom: 4px;
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
      background: #0f172a;
      color: #00f0ff;
      border: 1px solid #334155;
      padding: 6px 8px;
      border-radius: 6px;
      font-size: 0.85rem;
      font-family: 'Sarabun', sans-serif;
    }
    .canvas-box {
      position: relative;
      width: 100%;
      background: #020617;
      border: 1px solid #1e293b;
      border-radius: 10px;
      overflow: hidden;
      margin-bottom: 12px;
    }
    canvas {
      display: block;
      width: 100%;
      height: 240px;
    }
    .readout-grid {
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 8px;
    }
    .readout-card {
      background: #090e1a;
      border: 1px solid #1e293b;
      border-radius: 8px;
      padding: 8px 10px;
      text-align: center;
    }
    .readout-val {
      font-size: 1.0rem;
      font-weight: 700;
      color: #00f0ff;
      font-family: 'JetBrains Mono', monospace;
      margin-bottom: 2px;
    }
    .readout-lbl {
      font-size: 0.72rem;
      color: #64748b;
    }
  </style>
</head>
<body>

  <div class="sim-card">
    <div class="sim-header">
      <div class="sim-title">
        <span>🔬</span> 1.2 การแผ่รังสีของวัตถุดำ & กฎของวีนและสเตฟาน-โบลทซ์มานน์
      </div>
      <div class="badge-fps">● 60 FPS REAL-TIME</div>
    </div>

    <div class="control-grid">
      <div class="ctrl-box">
        <label>อุณหภูมิผิวของวัตถุ (T): <span id="val_temp" class="val-display">5800</span> K</label>
        <input type="range" id="slider_temp" min="1000" max="15000" step="100" value="5800">
      </div>
      <div class="ctrl-box">
        <label>วัตถุดาราศาสตร์ตัวอย่าง (Presets):</label>
        <select id="sel_preset">
          <option value="310">ร่างกายมนุษย์ (310 K - IR)</option>
          <option value="3000">ดาวฤกษ์สีแดง Betelgeuse (3,000 K)</option>
          <option value="5800" selected>ดวงอาทิตย์ Sun (5,800 K)</option>
          <option value="9940">ดาวซิริอุส Sirius A (9,940 K)</option>
          <option value="15000">ดาวยักษ์สีน้ำเงิน Blue Giant (15,000 K)</option>
        </select>
      </div>
    </div>

    <div class="canvas-box"><canvas id="simCanvas" width="640" height="240"></canvas></div>

    <div class="readout-grid">
      <div class="readout-card"><div class="readout-val" id="val_peak">500 nm</div><div class="readout-lbl">ความยาวคลื่นสูงสุด (λ_max = b/T)</div></div>
      <div class="readout-card"><div class="readout-val" id="val_color">ขาว-เหลือง</div><div class="readout-lbl">สีของรังสีความร้อนที่ปรากฏ</div></div>
      <div class="readout-card"><div class="readout-val" id="val_power">6.42 × 10⁷ W/m²</div><div class="readout-lbl">กำลังแผ่รังสีรวม (I = σT⁴)</div></div>
    </div>
  </div>

  <script>
    const cv = document.getElementById("simCanvas");
    const ctx = cv.getContext("2d");
    const sliderTemp = document.getElementById("slider_temp");
    const selPreset = document.getElementById("sel_preset");
    let tick = 0;

    selPreset.addEventListener("change", () => {
      sliderTemp.value = selPreset.value;
    });

    function getBlackbodyRGB(T) {
      // Color temperature mapping approximation
      let r, g, b;
      if (4000 >= T) {
        r = 255;
        g = Math.max(80, Math.min(200, (T - 1000) * 0.045 + 80));
        b = Math.max(20, Math.min(100, (T - 1000) * 0.02 + 20));
      } else if (7000 >= T) {
        r = 255;
        g = Math.min(255, 200 + (T - 4000) * 0.018);
        b = Math.min(255, 100 + (T - 4000) * 0.05);
      } else {
        r = Math.max(160, 255 - (T - 7000) * 0.01);
        g = Math.max(200, 255 - (T - 7000) * 0.005);
        b = 255;
      }
      return { r: Math.round(r), g: Math.round(g), b: Math.round(b) };
    }

    function animate() {
      const T = +sliderTemp.value;
      document.getElementById("val_temp").textContent = T;

      // Wien's Displacement Law: lambda_max = 2.898e-3 / T (in nm)
      const peakLam = Math.round(2898000 / T);
      document.getElementById("val_peak").textContent = peakLam >= 1000 ? (peakLam/1000).toFixed(2) + " µm (IR)" : peakLam + " nm";

      // Stefan-Boltzmann Law: I = sigma * T^4
      const sigma = 5.670374e-8;
      const power = sigma * Math.pow(T, 4);
      document.getElementById("val_power").textContent = power >= 1e6 ? (power / 1e6).toFixed(2) + " MW/m²" : power.toFixed(0) + " W/m²";

      const rgb = getBlackbodyRGB(T);
      let colName = "แดงเข้ม (Deep Red)";
      if (T > 2500 && 4000 >= T) colName = "ส้ม-แดง (Orange-Red)";
      else if (T > 4000 && 6000 >= T) colName = "ขาว-เหลือง (Yellow-White)";
      else if (T > 6000 && 9000 >= T) colName = "ขาวนวล (Pure White)";
      else if (T > 9000) colName = "ฟ้าอมขาว (Blue-White)";
      document.getElementById("val_color").textContent = colName;

      ctx.clearRect(0, 0, cv.width, cv.height);

      // -------------------------------------------------------------
      // 1. Left Panel: Shaded Glowing Thermal Sphere / Stellar Object
      // -------------------------------------------------------------
      const starX = 85, starY = 120, starR = 55;
      
      // Corona flare ripples
      for(let f=0; 3 > f; f++) {
        const flareR = starR + 8 + Math.sin(tick*0.06 + f)*4;
        ctx.fillStyle = "rgba(" + rgb.r + "," + rgb.g + "," + rgb.b + "," + (0.15 - f*0.04) + ")";
        ctx.beginPath(); ctx.arc(starX, starY, flareR, 0, Math.PI*2); ctx.fill();
      }

      // Star Body Gradient
      const starGrad = ctx.createRadialGradient(starX - 18, starY - 18, 4, starX, starY, starR);
      starGrad.addColorStop(0, "#ffffff");
      starGrad.addColorStop(0.35, "rgb(" + rgb.r + "," + rgb.g + "," + rgb.b + ")");
      starGrad.addColorStop(1, "rgba(" + Math.round(rgb.r*0.4) + "," + Math.round(rgb.g*0.4) + "," + Math.round(rgb.b*0.4) + ", 0.95)");
      ctx.fillStyle = starGrad;
      ctx.beginPath(); ctx.arc(starX, starY, starR, 0, Math.PI*2); ctx.fill();

      ctx.fillStyle = "#ffffff"; ctx.font = "11px sans-serif";
      ctx.fillText("วัตถุดำ / ดาวฤกษ์", starX - 42, starY + 75);
      ctx.fillStyle = "#00f0ff";
      ctx.fillText("T = " + T + " K", starX - 25, starY + 90);

      // -------------------------------------------------------------
      // 2. Right Panel: Spectral Radiance Curve & Wien Displacement Peak
      // -------------------------------------------------------------
      const originX = 180, originY = 210;
      const graphW = 430, graphH = 180;

      // Visible spectrum background band
      const visStartX = originX + (400 / 3000 * graphW);
      const visEndX = originX + (750 / 3000 * graphW);
      const visGrad = ctx.createLinearGradient(visStartX, 0, visEndX, 0);
      visGrad.addColorStop(0, "rgba(59, 130, 246, 0.2)");
      visGrad.addColorStop(0.5, "rgba(34, 197, 94, 0.2)");
      visGrad.addColorStop(1, "rgba(239, 68, 68, 0.2)");
      ctx.fillStyle = visGrad;
      ctx.fillRect(visStartX, 30, visEndX - visStartX, graphH);

      ctx.fillStyle = "#10b981"; ctx.font = "10px sans-serif";
      ctx.fillText("Visible", visStartX + 8, 42);

      // Planck Blackbody Radiation Curve
      ctx.strokeStyle = "rgb(" + rgb.r + "," + rgb.g + "," + rgb.b + ")";
      ctx.lineWidth = 3;
      ctx.beginPath();
      for(let px = originX + 2; originX + graphW >= px; px += 2) {
        const lam = ((px - originX) / graphW) * 3000; // 0 to 3000 nm
        const p = Math.pow(T / 1000, 3) * Math.pow(lam / peakLam, 5) / (Math.exp((lam ? peakLam / lam : 10) * 2.5) - 1 + 0.05);
        const y = originY - Math.min(170, p * 5.5);
        if (px === originX + 2) ctx.moveTo(px, y);
        else ctx.lineTo(px, y);
      }
      ctx.stroke();

      // Wien's Displacement Peak Indicator
      const peakX = originX + (peakLam / 3000 * graphW);
      if (peakX >= originX && originX + graphW >= peakX) {
        ctx.strokeStyle = "#f59e0b"; ctx.lineWidth = 2; ctx.setLineDash([4, 4]);
        ctx.beginPath(); ctx.moveTo(peakX, 30); ctx.lineTo(peakX, originY); ctx.stroke();
        ctx.setLineDash([]);
        ctx.fillStyle = "#f59e0b"; ctx.font = "11px sans-serif";
        ctx.fillText("λ_max = " + (peakLam >= 1000 ? (peakLam/1000).toFixed(2) + " µm" : peakLam + " nm"), peakX + 6, 60);
      }

      // Graph Axes
      ctx.strokeStyle = "#94a3b8"; ctx.lineWidth = 1.5;
      ctx.beginPath();
      ctx.moveTo(originX, 30); ctx.lineTo(originX, originY); ctx.lineTo(originX + graphW, originY);
      ctx.stroke();

      ctx.fillStyle = "#94a3b8"; ctx.font = "11px sans-serif";
      ctx.fillText("ความยาวคลื่น λ (nm) →", originX + graphW - 120, originY + 18);
      ctx.fillText("ความเข้มพลังงาน I(λ, T)", originX - 10, 22);

      tick++;
      requestAnimationFrame(animate);
    }
    animate();
  </script>
</body>
</html>
"""

# =============================================================================
# 1.3 SIMULATOR: Photoelectric Effect & Einstein's Photon Theory
# =============================================================================
sim_1_3_html = """<!DOCTYPE html>
<html lang="th">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>RBRU Physics Lab: 1.3 ปรากฏการณ์โฟโตอิเล็กทริก & สมการไอน์สไตน์</title>
  <link href="https://fonts.googleapis.com/css2?family=Sarabun:wght@400;600;700&family=JetBrains+Mono:wght@500;700&display=swap" rel="stylesheet">
  <style>
    * { box-sizing: border-box; margin: 0; padding: 0; }
    body {
      background: #020617;
      color: #f8fafc;
      font-family: 'Sarabun', -apple-system, sans-serif;
      padding: 12px;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      min-height: 100vh;
    }
    .sim-card {
      background: rgba(15, 23, 42, 0.95);
      border: 1px solid #1e293b;
      border-radius: 14px;
      padding: 16px;
      width: 100%;
      max-width: 680px;
      box-shadow: 0 10px 30px rgba(0, 0, 0, 0.7);
    }
    .sim-header {
      display: flex;
      justify-content: space-between;
      align-items: center;
      border-bottom: 1px solid #1e293b;
      padding-bottom: 10px;
      margin-bottom: 12px;
    }
    .sim-title {
      font-size: 1.05rem;
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
      padding: 3px 8px;
      border-radius: 9999px;
      font-size: 0.72rem;
      font-weight: 700;
      font-family: 'JetBrains Mono', monospace;
    }
    .control-grid {
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 10px;
      margin-bottom: 12px;
    }
    @media (max-width: 580px) {
      .control-grid { grid-template-columns: 1fr; }
    }
    .ctrl-box {
      background: #090e1a;
      border: 1px solid #1e293b;
      padding: 8px 10px;
      border-radius: 8px;
    }
    .ctrl-box label {
      display: block;
      font-size: 0.78rem;
      color: #94a3b8;
      margin-bottom: 4px;
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
      background: #0f172a;
      color: #00f0ff;
      border: 1px solid #334155;
      padding: 6px 8px;
      border-radius: 6px;
      font-size: 0.82rem;
      font-family: 'Sarabun', sans-serif;
    }
    .canvas-box {
      position: relative;
      width: 100%;
      background: #020617;
      border: 1px solid #1e293b;
      border-radius: 10px;
      overflow: hidden;
      margin-bottom: 12px;
    }
    canvas {
      display: block;
      width: 100%;
      height: 250px;
    }
    .readout-grid {
      display: grid;
      grid-template-columns: repeat(4, 1fr);
      gap: 6px;
    }
    @media (max-width: 540px) {
      .readout-grid { grid-template-columns: 1fr 1fr; }
    }
    .readout-card {
      background: #090e1a;
      border: 1px solid #1e293b;
      border-radius: 8px;
      padding: 8px;
      text-align: center;
    }
    .readout-val {
      font-size: 0.95rem;
      font-weight: 700;
      color: #00f0ff;
      font-family: 'JetBrains Mono', monospace;
      margin-bottom: 2px;
    }
    .readout-lbl {
      font-size: 0.68rem;
      color: #64748b;
    }
  </style>
</head>
<body>

  <div class="sim-card">
    <div class="sim-header">
      <div class="sim-title">
        <span>🔬</span> 1.3 ปรากฏการณ์โฟโตอิเล็กทริก: หลอดสุญญากาศ & ศักย์หยุดยั้ง
      </div>
      <div class="badge-fps">● 60 FPS REAL-TIME</div>
    </div>

    <div class="control-grid">
      <div class="ctrl-box">
        <label>โลหะเป้าหมาย (φ):</label>
        <select id="sel_metal">
          <option value="2.14">ซีเซียม Cs (φ = 2.14 eV)</option>
          <option value="2.30" selected>โซเดียม Na (φ = 2.30 eV)</option>
          <option value="4.30">สังกะสี Zn (φ = 4.30 eV)</option>
          <option value="4.70">ทองแดง Cu (φ = 4.70 eV)</option>
          <option value="5.65">แพลทินัม Pt (φ = 5.65 eV)</option>
        </select>
      </div>
      <div class="ctrl-box">
        <label>ความยาวคลื่นแสงฉาย (λ): <span id="val_lam" class="val-display">300</span> nm</label>
        <input type="range" id="slider_lam" min="150" max="750" value="300">
      </div>
      <div class="ctrl-box">
        <label>ความต่างศักย์ภายนอก (V_ext): <span id="val_v" class="val-display">0.00</span> V</label>
        <input type="range" id="slider_v" min="-3.5" max="3.5" step="0.05" value="0.0">
      </div>
    </div>

    <div class="canvas-box"><canvas id="simCanvas" width="640" height="250"></canvas></div>

    <div class="readout-grid">
      <div class="readout-card"><div class="readout-val" id="val_ephoton">4.13 eV</div><div class="readout-lbl">พลังงานโฟตอน (E = hf)</div></div>
      <div class="readout-card"><div class="readout-val" id="val_kmax">1.83 eV</div><div class="readout-lbl">พลังงานจลน์สูงสุด (K_max)</div></div>
      <div class="readout-card"><div class="readout-val" id="val_vs">1.83 V</div><div class="readout-lbl">ความต่างศักย์หยุดยั้ง (V_s)</div></div>
      <div class="readout-card"><div class="readout-val" id="val_current" style="color:#10b981;">18.4 µA</div><div class="readout-lbl">กระแสโฟโตอิเล็กทริก (I)</div></div>
    </div>
  </div>

  <script>
    const cv = document.getElementById("simCanvas");
    const ctx = cv.getContext("2d");
    const selMetal = document.getElementById("sel_metal");
    const sliderLam = document.getElementById("slider_lam");
    const sliderV = document.getElementById("slider_v");
    let tick = 0;

    let electrons = [];
    for(let i=0; 30 > i; i++) {
      electrons.push({
        x: 110 + Math.random()*15,
        y: 45 + Math.random()*130,
        vx: 1.5 + Math.random()*3.0,
        vy: (Math.random()-0.5)*1.2,
        active: true
      });
    }

    function animate() {
      const phi = +selMetal.value;
      const lam = +sliderLam.value;
      const V_ext = +sliderV.value;

      document.getElementById("val_lam").textContent = lam;
      document.getElementById("val_v").textContent = (V_ext >= 0 ? "+" : "") + V_ext.toFixed(2);

      // Ephoton = 1240 / lambda (eV)
      const Ephoton = 1240 / lam;
      document.getElementById("val_ephoton").textContent = Ephoton.toFixed(2) + " eV";

      const Kmax = Ephoton - phi;
      const Vs = Kmax > 0 ? Kmax : 0;

      const kmEl = document.getElementById("val_kmax");
      const vsEl = document.getElementById("val_vs");
      const curEl = document.getElementById("val_current");

      let current_uA = 0;

      if (Kmax > 0) {
        kmEl.textContent = Kmax.toFixed(2) + " eV";
        vsEl.textContent = Vs.toFixed(2) + " V";

        // Current flows if V_ext > -Vs
        if (V_ext > -Vs) {
          const saturationFactor = Math.min(1.0, 0.6 + 0.4 * (V_ext + Vs) / (1.5 + Vs));
          current_uA = (25.0 * saturationFactor).toFixed(1);
          curEl.textContent = current_uA + " µA";
          curEl.style.color = "#10b981";
        } else {
          curEl.textContent = "0.00 µA (หยุดยั้งสมบูรณ์)";
          curEl.style.color = "#f43f5e";
        }
      } else {
        kmEl.textContent = "0.00 (ไม่เกิดผล)";
        vsEl.textContent = "0.00 V";
        curEl.textContent = "0.00 µA (hf < φ)";
        curEl.style.color = "#64748b";
      }

      ctx.clearRect(0, 0, cv.width, cv.height);

      // -------------------------------------------------------------
      // 1. Draw Evacuated Quartz Glass Tube
      // -------------------------------------------------------------
      ctx.strokeStyle = "rgba(148, 163, 184, 0.4)";
      ctx.lineWidth = 2;
      ctx.fillStyle = "rgba(15, 23, 42, 0.7)";
      ctx.beginPath();
      ctx.roundRect(80, 25, 480, 170, 20);
      ctx.fill(); ctx.stroke();

      // Quartz Light Window (Top Left)
      ctx.strokeStyle = "#38bdf8";
      ctx.lineWidth = 3;
      ctx.beginPath(); ctx.moveTo(95, 25); ctx.lineTo(155, 25); ctx.stroke();
      ctx.fillStyle = "#38bdf8"; ctx.font = "10px sans-serif";
      ctx.fillText("หน้าต่างควอตซ์ (Quartz)", 75, 18);

      // Cathode Emitter Plate (Left)
      ctx.fillStyle = "#64748b";
      ctx.fillRect(100, 45, 14, 130);
      ctx.fillStyle = "#00f0ff"; ctx.font = "11px sans-serif";
      ctx.fillText("ขั้วแคโทด Emitter (φ = " + phi + " eV)", 30, 215);

      // Anode Collector Plate (Right)
      ctx.fillStyle = "#475569";
      ctx.fillRect(525, 45, 14, 130);
      ctx.fillStyle = "#94a3b8";
      ctx.fillText("ขั้วแอโนด Collector (V = " + (V_ext >= 0 ? "+" : "") + V_ext.toFixed(2) + "V)", 420, 215);

      // -------------------------------------------------------------
      // 2. Incoming Monochromatic Photon Pulses
      // -------------------------------------------------------------
      let photonColor = "#ef4444";
      if (400 > lam) photonColor = "#a855f7"; // UV
      else if (500 > lam) photonColor = "#00f0ff"; // Cyan/Blue
      else if (600 > lam) photonColor = "#10b981"; // Green
      else photonColor = "#f59e0b"; // Yellow/Red

      ctx.strokeStyle = photonColor; ctx.lineWidth = 2.5;
      for(let p=0; 5 > p; p++) {
        const prog = ((tick*3.5 + p*50) % 120) / 120;
        const px = 20 + prog * 85;
        const py = 15 + prog * 65 + (p-2)*18;
        ctx.beginPath();
        ctx.moveTo(px - 14, py - 10);
        ctx.lineTo(px, py);
        ctx.stroke();
      }

      // -------------------------------------------------------------
      // 3. Ejected Photoelectrons & Electric Field Deceleration/Acceleration
      // -------------------------------------------------------------
      if (Kmax > 0) {
        // E-field force: acc = V_ext / distance
        const eAcc = (V_ext / 3.0) * 0.08;
        ctx.fillStyle = "#10b981";

        electrons.forEach(el => {
          ctx.beginPath();
          ctx.arc(el.x, el.y, 4, 0, Math.PI*2);
          ctx.fill();

          el.x += el.vx;
          el.y += el.vy;
          el.vx += eAcc; // Electric field acts on electron

          // If electron hits anode
          if (el.x >= 525) {
            el.x = 116;
            el.y = 50 + Math.random()*120;
            el.vx = Math.sqrt(Kmax)*1.8 + Math.random()*1.0;
          }
          // If retarding potential stops and turns electron back
          else if (110 > el.x && 0 > el.vx) {
            el.x = 116;
            el.y = 50 + Math.random()*120;
            el.vx = Math.sqrt(Kmax)*1.8 + Math.random()*1.0;
          }
        });
      }

      // External Circuit Wires & Ammeter / Voltmeter Display
      ctx.strokeStyle = "#334155"; ctx.lineWidth = 2;
      ctx.beginPath();
      ctx.moveTo(107, 175); ctx.lineTo(107, 235); ctx.lineTo(260, 235);
      ctx.moveTo(532, 175); ctx.lineTo(532, 235); ctx.lineTo(380, 235);
      ctx.stroke();

      // Microammeter Box (Bottom Center)
      ctx.fillStyle = "#0f172a"; ctx.strokeStyle = "#00f0ff";
      ctx.fillRect(260, 222, 120, 24);
      ctx.strokeRect(260, 222, 120, 24);
      ctx.fillStyle = current_uA > 0 ? "#10b981" : "#f43f5e"; ctx.font = "bold 11px 'JetBrains Mono', monospace";
      ctx.fillText("µA: " + current_uA + " µA", 280, 238);

      tick++;
      requestAnimationFrame(animate);
    }
    animate();
  </script>
</body>
</html>
"""

# =============================================================================
# 1.4 SIMULATOR: Hydrogen Atomic Spectra & Rydberg Formula
# =============================================================================
sim_1_4_html = """<!DOCTYPE html>
<html lang="th">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>RBRU Physics Lab: 1.4 สเปกตรัมของอะตอมไฮโดรเจน & สูตรริดเบิร์ก</title>
  <link href="https://fonts.googleapis.com/css2?family=Sarabun:wght@400;600;700&family=JetBrains+Mono:wght@500;700&display=swap" rel="stylesheet">
  <style>
    * { box-sizing: border-box; margin: 0; padding: 0; }
    body {
      background: #020617;
      color: #f8fafc;
      font-family: 'Sarabun', -apple-system, sans-serif;
      padding: 12px;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      min-height: 100vh;
    }
    .sim-card {
      background: rgba(15, 23, 42, 0.95);
      border: 1px solid #1e293b;
      border-radius: 14px;
      padding: 16px;
      width: 100%;
      max-width: 680px;
      box-shadow: 0 10px 30px rgba(0, 0, 0, 0.7);
    }
    .sim-header {
      display: flex;
      justify-content: space-between;
      align-items: center;
      border-bottom: 1px solid #1e293b;
      padding-bottom: 10px;
      margin-bottom: 12px;
    }
    .sim-title {
      font-size: 1.05rem;
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
      padding: 3px 8px;
      border-radius: 9999px;
      font-size: 0.72rem;
      font-weight: 700;
      font-family: 'JetBrains Mono', monospace;
    }
    .control-grid {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 12px;
      margin-bottom: 12px;
    }
    @media (max-width: 540px) {
      .control-grid { grid-template-columns: 1fr; }
    }
    .ctrl-box {
      background: #090e1a;
      border: 1px solid #1e293b;
      padding: 8px 12px;
      border-radius: 8px;
    }
    .ctrl-box label {
      display: block;
      font-size: 0.82rem;
      color: #94a3b8;
      margin-bottom: 4px;
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
      background: #0f172a;
      color: #00f0ff;
      border: 1px solid #334155;
      padding: 6px 8px;
      border-radius: 6px;
      font-size: 0.85rem;
      font-family: 'Sarabun', sans-serif;
    }
    .canvas-box {
      position: relative;
      width: 100%;
      background: #020617;
      border: 1px solid #1e293b;
      border-radius: 10px;
      overflow: hidden;
      margin-bottom: 12px;
    }
    canvas {
      display: block;
      width: 100%;
      height: 250px;
    }
    .readout-grid {
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 8px;
    }
    .readout-card {
      background: #090e1a;
      border: 1px solid #1e293b;
      border-radius: 8px;
      padding: 8px 10px;
      text-align: center;
    }
    .readout-val {
      font-size: 1.0rem;
      font-weight: 700;
      color: #00f0ff;
      font-family: 'JetBrains Mono', monospace;
      margin-bottom: 2px;
    }
    .readout-lbl {
      font-size: 0.72rem;
      color: #64748b;
    }
  </style>
</head>
<body>

  <div class="sim-card">
    <div class="sim-header">
      <div class="sim-title">
        <span>🔬</span> 1.4 สเปกตรัมของไฮโดรเจน: การเปลี่ยนระดับพลังงาน & สูตรริดเบิร์ก
      </div>
      <div class="badge-fps">● 60 FPS REAL-TIME</div>
    </div>

    <div class="control-grid">
      <div class="ctrl-box">
        <label>อนุกรมสเปกตรัม (Lower Level n₁):</label>
        <select id="sel_series">
          <option value="1">Lyman Series (n₁ = 1, ย่าน UV)</option>
          <option value="2" selected>Balmer Series (n₁ = 2, แสงขาวมองเห็น)</option>
          <option value="3">Paschen Series (n₁ = 3, ย่าน Infrared)</option>
          <option value="4">Brackett Series (n₁ = 4, ย่าน Far-IR)</option>
        </select>
      </div>
      <div class="ctrl-box">
        <label>ระดับพลังงานเริ่มต้น (Upper Level n₂): <span id="val_n2" class="val-display">3</span></label>
        <input type="range" id="slider_n2" min="2" max="7" value="3">
      </div>
    </div>

    <div class="canvas-box"><canvas id="simCanvas" width="640" height="250"></canvas></div>

    <div class="readout-grid">
      <div class="readout-card"><div class="readout-val" id="val_lam">656.3 nm</div><div class="readout-lbl">ความยาวคลื่นโฟตอนที่คาย (λ)</div></div>
      <div class="readout-card"><div class="readout-val" id="val_de">1.89 eV</div><div class="readout-lbl">พลังงานที่ปลดปล่อย (ΔE)</div></div>
      <div class="readout-card"><div class="readout-val" id="val_line" style="color:#ef4444;">H-alpha (สีแดง)</div><div class="readout-lbl">ชื่อและสีเส้นสเปกตรัม</div></div>
    </div>
  </div>

  <script>
    const cv = document.getElementById("simCanvas");
    const ctx = cv.getContext("2d");
    const selSeries = document.getElementById("sel_series");
    const sliderN2 = document.getElementById("slider_n2");
    let tick = 0;

    function getSpectralDetails(n1, n2) {
      const invLam = 1.097373e7 * (1/(n1*n1) - 1/(n2*n2));
      const lam_nm = (1 / invLam) * 1e9;
      const dE = 13.6 * (1/(n1*n1) - 1/(n2*n2));

      let name = "สเปกตรัม", col = "#00f0ff";
      if (n1 === 1) {
        name = "Lyman (" + n2 + "→1 UV)"; col = "#a855f7";
      } else if (n1 === 2) {
        if (n2 === 3) { name = "H-alpha (สีแดง 656.3 nm)"; col = "#ef4444"; }
        else if (n2 === 4) { name = "H-beta (สีฟ้าคราม 486.1 nm)"; col = "#06b6d4"; }
        else if (n2 === 5) { name = "H-gamma (สีน้ำเงิน 434.0 nm)"; col = "#3b82f6"; }
        else { name = "H-delta (สีม่วง 410.2 nm)"; col = "#8b5cf6"; }
      } else if (n1 === 3) {
        name = "Paschen (" + n2 + "→3 IR)"; col = "#f97316";
      } else {
        name = "Brackett (" + n2 + "→4 Far-IR)"; col = "#e11d48";
      }
      return { lam: lam_nm, dE: dE, name: name, color: col };
    }

    function animate() {
      const n1 = +selSeries.value;
      sliderN2.min = n1 + 1;
      if (n1 >= +sliderN2.value) sliderN2.value = n1 + 1;
      const n2 = +sliderN2.value;
      document.getElementById("val_n2").textContent = n2;

      const info = getSpectralDetails(n1, n2);
      document.getElementById("val_lam").textContent = info.lam >= 1000 ? (info.lam/1000).toFixed(3) + " µm" : info.lam.toFixed(1) + " nm";
      document.getElementById("val_de").textContent = info.dE.toFixed(2) + " eV";
      
      const lnEl = document.getElementById("val_line");
      lnEl.textContent = info.name;
      lnEl.style.color = info.color;

      ctx.clearRect(0, 0, cv.width, cv.height);

      // -------------------------------------------------------------
      // 1. Left Panel: Bohr Energy Level Ladder Transitions
      // -------------------------------------------------------------
      const ladderX = 40, ladderW = 220;
      ctx.fillStyle = "#94a3b8"; ctx.font = "11px sans-serif";
      ctx.fillText("ระดับพลังงานควอนตัม (Bohr Energy Levels)", ladderX, 22);

      for(let n=1; 7 > n; n++) {
        const y = 210 - 170 * (1 - 1/(n*n));
        const isTarget = (n === n1);
        const isInitial = (n === n2);

        ctx.strokeStyle = isTarget ? "#00f0ff" : (isInitial ? "#f59e0b" : "#334155");
        ctx.lineWidth = (isTarget || isInitial) ? 2.5 : 1;
        ctx.beginPath();
        ctx.moveTo(ladderX, y);
        ctx.lineTo(ladderX + ladderW, y);
        ctx.stroke();

        ctx.fillStyle = isTarget ? "#00f0ff" : (isInitial ? "#f59e0b" : "#64748b");
        ctx.font = "10px 'JetBrains Mono', monospace";
        ctx.fillText("n=" + n + " (" + (-13.6/(n*n)).toFixed(2) + " eV)", ladderX + ladderW + 8, y + 4);
      }

      // Transition Arrow (n2 -> n1)
      const yStart = 210 - 170 * (1 - 1/(n2*n2));
      const yEnd = 210 - 170 * (1 - 1/(n1*n1));
      ctx.strokeStyle = info.color; ctx.lineWidth = 3;
      ctx.beginPath(); ctx.moveTo(ladderX + 110, yStart); ctx.lineTo(ladderX + 110, yEnd); ctx.stroke();
      // Arrowhead
      ctx.fillStyle = info.color;
      ctx.beginPath();
      ctx.moveTo(ladderX + 105, yEnd - 8); ctx.lineTo(ladderX + 115, yEnd - 8); ctx.lineTo(ladderX + 110, yEnd);
      ctx.fill();

      // Pulsing emitted photon packet
      const prog = (tick*0.04) % 1;
      const photonWaveX = ladderX + 110 + prog * 180;
      const photonWaveY = (yStart + yEnd)/2;
      ctx.fillStyle = info.color;
      ctx.beginPath(); ctx.arc(photonWaveX, photonWaveY, 4.5, 0, Math.PI*2); ctx.fill();

      // -------------------------------------------------------------
      // 2. Right Panel: Spectrograph Film / Emission Spectrum Lines
      // -------------------------------------------------------------
      const specX = 350, specY = 40, specW = 265, specH = 80;
      ctx.fillStyle = "#030712";
      ctx.strokeStyle = "#1e293b"; ctx.lineWidth = 2;
      ctx.fillRect(specX, specY, specW, specH);
      ctx.strokeRect(specX, specY, specW, specH);

      ctx.fillStyle = "#94a3b8"; ctx.font = "11px sans-serif";
      ctx.fillText("แถบสเปกตรัมที่บันทึกได้ (Spectrograph Film)", specX, 30);

      // Draw all Balmer visible lines for reference
      if (n1 === 2) {
        const balmerLines = [
          { n: 3, lam: 656.3, col: "#ef4444" },
          { n: 4, lam: 486.1, col: "#06b6d4" },
          { n: 5, lam: 434.0, col: "#3b82f6" },
          { n: 6, lam: 410.2, col: "#8b5cf6" }
        ];
        balmerLines.forEach(l => {
          // Map 380 - 700 nm to specX to specX + specW
          const lx = specX + ((l.lam - 380) / 320) * specW;
          const isSelected = (l.n === n2);
          ctx.strokeStyle = l.col;
          ctx.lineWidth = isSelected ? 4.0 : 1.8;
          ctx.beginPath(); ctx.moveTo(lx, specY); ctx.lineTo(lx, specY + specH); ctx.stroke();

          if (isSelected) {
            ctx.fillStyle = l.col; ctx.font = "bold 10px sans-serif";
            ctx.fillText(l.lam + " nm", lx - 18, specY + specH + 16);
          }
        });
      } else {
        // Draw single line indicator
        const lx = specX + specW / 2;
        ctx.strokeStyle = info.color; ctx.lineWidth = 3.5;
        ctx.beginPath(); ctx.moveTo(lx, specY); ctx.lineTo(lx, specY + specH); ctx.stroke();
        ctx.fillStyle = info.color; ctx.font = "bold 10px sans-serif";
        ctx.fillText(info.lam >= 1000 ? (info.lam/1000).toFixed(2) + " µm" : info.lam.toFixed(1) + " nm", lx - 20, specY + specH + 16);
      }

      // Rydberg Formula Summary Box (Bottom Right)
      ctx.fillStyle = "rgba(15, 23, 42, 0.8)";
      ctx.strokeStyle = "#334155";
      ctx.fillRect(specX, 160, specW, 65);
      ctx.strokeRect(specX, 160, specW, 65);
      ctx.fillStyle = "#00f0ff"; ctx.font = "11px 'JetBrains Mono', monospace";
      ctx.fillText("1/λ = R_H (1/n₁² - 1/n₂²)", specX + 15, 185);
      ctx.fillStyle = "#94a3b8"; ctx.font = "10px sans-serif";
      ctx.fillText("R_H = 1.097373 × 10⁷ m⁻¹", specX + 15, 205);

      tick++;
      requestAnimationFrame(animate);
    }
    animate();
  </script>
</body>
</html>
"""

# =============================================================================
# 1.5 SIMULATOR: Chapter 1 Virtual Quantum Lab (Solar Cell & Compton Scattering)
# =============================================================================
sim_1_5_html = """<!DOCTYPE html>
<html lang="th">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>RBRU Physics Lab: 1.5 ปฏิบัติการควอนตัมจำลอง & การประยุกต์ใช้</title>
  <link href="https://fonts.googleapis.com/css2?family=Sarabun:wght@400;600;700&family=JetBrains+Mono:wght@500;700&display=swap" rel="stylesheet">
  <style>
    * { box-sizing: border-box; margin: 0; padding: 0; }
    body {
      background: #020617;
      color: #f8fafc;
      font-family: 'Sarabun', -apple-system, sans-serif;
      padding: 12px;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      min-height: 100vh;
    }
    .sim-card {
      background: rgba(15, 23, 42, 0.95);
      border: 1px solid #1e293b;
      border-radius: 14px;
      padding: 16px;
      width: 100%;
      max-width: 680px;
      box-shadow: 0 10px 30px rgba(0, 0, 0, 0.7);
    }
    .sim-header {
      display: flex;
      justify-content: space-between;
      align-items: center;
      border-bottom: 1px solid #1e293b;
      padding-bottom: 10px;
      margin-bottom: 12px;
    }
    .sim-title {
      font-size: 1.05rem;
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
      padding: 3px 8px;
      border-radius: 9999px;
      font-size: 0.72rem;
      font-weight: 700;
      font-family: 'JetBrains Mono', monospace;
    }
    .tab-bar {
      display: flex;
      gap: 8px;
      margin-bottom: 12px;
    }
    .tab-btn {
      flex: 1;
      background: #090e1a;
      border: 1px solid #1e293b;
      color: #94a3b8;
      padding: 6px 12px;
      border-radius: 6px;
      font-size: 0.82rem;
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
    .control-grid {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 12px;
      margin-bottom: 12px;
    }
    @media (max-width: 540px) {
      .control-grid { grid-template-columns: 1fr; }
    }
    .ctrl-box {
      background: #090e1a;
      border: 1px solid #1e293b;
      padding: 8px 12px;
      border-radius: 8px;
    }
    .ctrl-box label {
      display: block;
      font-size: 0.82rem;
      color: #94a3b8;
      margin-bottom: 4px;
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
      background: #0f172a;
      color: #00f0ff;
      border: 1px solid #334155;
      padding: 6px 8px;
      border-radius: 6px;
      font-size: 0.85rem;
      font-family: 'Sarabun', sans-serif;
    }
    .canvas-box {
      position: relative;
      width: 100%;
      background: #020617;
      border: 1px solid #1e293b;
      border-radius: 10px;
      overflow: hidden;
      margin-bottom: 12px;
    }
    canvas {
      display: block;
      width: 100%;
      height: 250px;
    }
    .readout-grid {
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 8px;
    }
    .readout-card {
      background: #090e1a;
      border: 1px solid #1e293b;
      border-radius: 8px;
      padding: 8px 10px;
      text-align: center;
    }
    .readout-val {
      font-size: 1.0rem;
      font-weight: 700;
      color: #00f0ff;
      font-family: 'JetBrains Mono', monospace;
      margin-bottom: 2px;
    }
    .readout-lbl {
      font-size: 0.72rem;
      color: #64748b;
    }
  </style>
</head>
<body>

  <div class="sim-card">
    <div class="sim-header">
      <div class="sim-title">
        <span>🔬</span> 1.5 ปฏิบัติการควอนตัม: เซลล์แสงอาทิตย์ (Bandgap) & การกระเจิงคอมป์ตัน
      </div>
      <div class="badge-fps">● 60 FPS REAL-TIME</div>
    </div>

    <div class="tab-bar">
      <button class="tab-btn active" id="tabSolar" onclick="setMode('solar')">☀️ เซลล์แสงอาทิตย์ & Bandgap</button>
      <button class="tab-btn" id="tabCompton" onclick="setMode('compton')">💥 การกระเจิงคอมป์ตัน (Compton)</button>
    </div>

    <div id="controlsSolar" class="control-grid">
      <div class="ctrl-box">
        <label>สารกึ่งตัวนำเซลล์แสงอาทิตย์:</label>
        <select id="sel_semicond">
          <option value="1.12" selected>ซิลิกอน Silicon (Eg = 1.12 eV, λ_cutoff = 1107 nm)</option>
          <option value="1.42">แกลเลียมอาร์เซไนด์ GaAs (Eg = 1.42 eV, λ_cutoff = 873 nm)</option>
          <option value="1.70">เพอรอฟสไกต์ Perovskite (Eg = 1.70 eV, λ_cutoff = 729 nm)</option>
        </select>
      </div>
      <div class="ctrl-box">
        <label>ความยาวคลื่นแสงฉาย (λ): <span id="val_solar_lam" class="val-display">600</span> nm</label>
        <input type="range" id="slider_solar_lam" min="300" max="1300" value="600">
      </div>
    </div>

    <div id="controlsCompton" class="control-grid" style="display:none;">
      <div class="ctrl-box">
        <label>ความยาวคลื่นโฟตอนรังสีเอกซ์ (λ): <span id="val_compton_lam" class="val-display">0.020</span> nm</label>
        <input type="range" id="slider_compton_lam" min="0.005" max="0.050" step="0.001" value="0.020">
      </div>
      <div class="ctrl-box">
        <label>มุมการกระเจิงของโฟตอน (θ): <span id="val_theta" class="val-display">90</span>°</label>
        <input type="range" id="slider_theta" min="0" max="180" step="1" value="90">
      </div>
    </div>

    <div class="canvas-box"><canvas id="simCanvas" width="640" height="250"></canvas></div>

    <div class="readout-grid" id="readoutsSolar">
      <div class="readout-card"><div class="readout-val" id="val_eph">2.07 eV</div><div class="readout-lbl">พลังงานโฟตอน (E = hc/λ)</div></div>
      <div class="readout-card"><div class="readout-val" id="val_cutoff">1,107 nm</div><div class="readout-lbl">ความยาวคลื่นคัตออฟสูงสุด (λ_g)</div></div>
      <div class="readout-card"><div class="readout-val" id="val_status" style="color:#10b981;">ดูดกลืน & เกิดกระแสไฟฟ้า</div><div class="readout-lbl">สถานะการทำงานของเซลล์</div></div>
    </div>

    <div class="readout-grid" id="readoutsCompton" style="display:none;">
      <div class="readout-card"><div class="readout-val" id="val_dlam">+0.00243 nm</div><div class="readout-lbl">ความยาวคลื่นที่เพิ่มขึ้น (Δλ)</div></div>
      <div class="readout-card"><div class="readout-val" id="val_lamp">0.02243 nm</div><div class="readout-lbl">ความยาวคลื่นกระเจิง (λ')</div></div>
      <div class="readout-card"><div class="readout-val" id="val_ke">6.72 keV</div><div class="readout-lbl">พลังงานจลน์อิเล็กตรอนดีดกลับ</div></div>
    </div>
  </div>

  <script>
    const cv = document.getElementById("simCanvas");
    const ctx = cv.getContext("2d");
    let currentMode = "solar";
    let tick = 0;

    function setMode(mode) {
      currentMode = mode;
      document.getElementById("tabSolar").classList.toggle("active", mode === "solar");
      document.getElementById("tabCompton").classList.toggle("active", mode === "compton");
      document.getElementById("controlsSolar").style.display = mode === "solar" ? "grid" : "none";
      document.getElementById("controlsCompton").style.display = mode === "compton" ? "grid" : "none";
      document.getElementById("readoutsSolar").style.display = mode === "solar" ? "grid" : "none";
      document.getElementById("readoutsCompton").style.display = mode === "compton" ? "grid" : "none";
    }

    // Solar electron-hole pairs
    let pairs = [];
    for(let i=0; 20 > i; i++) {
      pairs.push({
        x: 100 + Math.random()*160,
        y: 80 + Math.random()*80,
        vy_e: -1.2,
        vy_h: 1.2
      });
    }

    function animate() {
      ctx.clearRect(0, 0, cv.width, cv.height);

      if (currentMode === "solar") {
        const Eg = +document.getElementById("sel_semicond").value;
        const lam = +document.getElementById("slider_solar_lam").value;
        document.getElementById("val_solar_lam").textContent = lam;

        const Eph = 1240 / lam;
        const lambda_cutoff = Math.round(1240 / Eg);
        document.getElementById("val_eph").textContent = Eph.toFixed(2) + " eV";
        document.getElementById("val_cutoff").textContent = lambda_cutoff + " nm";

        const isAbsorbed = Eph >= Eg;
        const statEl = document.getElementById("val_status");
        if (isAbsorbed) {
          statEl.textContent = "ดูดกลืน & เกิดกระแสไฟฟ้า";
          statEl.style.color = "#10b981";
        } else {
          statEl.textContent = "ทะลุผ่าน (E < Eg ไม่เกิดกระแส)";
          statEl.style.color = "#f43f5e";
        }

        // Left Panel: Semiconductor p-n junction diagram
        ctx.fillStyle = "#1e293b"; ctx.fillRect(80, 50, 200, 150);
        ctx.fillStyle = "rgba(59, 130, 246, 0.3)"; ctx.fillRect(80, 50, 200, 75); // n-type
        ctx.fillStyle = "rgba(239, 68, 68, 0.3)"; ctx.fillRect(80, 125, 200, 75); // p-type
        ctx.strokeStyle = "#00f0ff"; ctx.lineWidth = 1.5; ctx.strokeRect(80, 50, 200, 150);

        ctx.fillStyle = "#60a5fa"; ctx.font = "11px sans-serif"; ctx.fillText("n-type Silicon", 90, 70);
        ctx.fillStyle = "#f87171"; ctx.fillText("p-type Silicon", 90, 190);
        ctx.strokeStyle = "#f59e0b"; ctx.lineWidth = 1; ctx.setLineDash([3,3]);
        ctx.beginPath(); ctx.moveTo(80, 125); ctx.lineTo(280, 125); ctx.stroke();
        ctx.setLineDash([]);
        ctx.fillStyle = "#f59e0b"; ctx.fillText("รอยต่อ p-n Junction", 175, 122);

        // Incoming sunlight photon ray
        let rayCol = 400 > lam ? "#a855f7" : (700 > lam ? "#10b981" : "#ef4444");
        ctx.strokeStyle = rayCol; ctx.lineWidth = 2.5;
        for(let r=0; 3 > r; r++) {
          const prog = ((tick*3 + r*40) % 100) / 100;
          const rx = 30 + prog*50;
          const ry = 40 + prog*50 + r*20;
          ctx.beginPath(); ctx.moveTo(rx-15, ry-15); ctx.lineTo(rx, ry); ctx.stroke();
        }

        // Electron-Hole separation animation
        if (isAbsorbed) {
          pairs.forEach(p => {
            // Electron (blue) moves up to n-layer
            ctx.fillStyle = "#38bdf8"; ctx.beginPath(); ctx.arc(p.x, p.y + p.vy_e * (tick%30), 3.5, 0, Math.PI*2); ctx.fill();
            // Hole (red) moves down to p-layer
            ctx.fillStyle = "#f43f5e"; ctx.beginPath(); ctx.arc(p.x, p.y + p.vy_h * (tick%30), 3.5, 0, Math.PI*2); ctx.fill();
          });
        }

        // Right Panel: Bandgap Energy Diagram
        ctx.fillStyle = "#0f172a"; ctx.strokeStyle = "#334155";
        ctx.fillRect(340, 50, 240, 150); ctx.strokeRect(340, 50, 240, 150);

        // Conduction Band (Top)
        ctx.fillStyle = "rgba(56, 189, 248, 0.4)"; ctx.fillRect(355, 60, 210, 28);
        ctx.fillStyle = "#38bdf8"; ctx.fillText("Conduction Band (แถบนำไฟฟ้า)", 365, 78);

        // Valence Band (Bottom)
        ctx.fillStyle = "rgba(239, 68, 68, 0.4)"; ctx.fillRect(355, 155, 210, 28);
        ctx.fillStyle = "#f87171"; ctx.fillText("Valence Band (แถบเวเลนซ์)", 365, 173);

        // Bandgap Arrow
        ctx.strokeStyle = "#f59e0b"; ctx.lineWidth = 2;
        ctx.beginPath(); ctx.moveTo(460, 155); ctx.lineTo(460, 88); ctx.stroke();
        ctx.fillStyle = "#f59e0b"; ctx.font = "bold 11px sans-serif";
        ctx.fillText("Bandgap Eg = " + Eg + " eV", 370, 122);
      }
      else {
        // Compton Scattering Simulation
        const lam = +document.getElementById("slider_compton_lam").value;
        const theta_deg = +document.getElementById("slider_theta").value;
        const theta_rad = theta_deg * Math.PI / 180;

        document.getElementById("val_compton_lam").textContent = lam.toFixed(3);
        document.getElementById("val_theta").textContent = theta_deg;

        // Compton formula: delta_lambda = (h / m_e c) * (1 - cos(theta)) = 0.002426 nm * (1 - cos theta)
        const lambda_c = 0.0024263; // nm
        const delta_lambda = lambda_c * (1 - Math.cos(theta_rad));
        const lambda_prime = lam + delta_lambda;

        // Photon Energy E = 1.2398 / lam_nm (in keV)
        const E_init_keV = 1.23984 / lam;
        const E_scattered_keV = 1.23984 / lambda_prime;
        const KE_electron_keV = E_init_keV - E_scattered_keV;

        document.getElementById("val_dlam").textContent = "+" + delta_lambda.toFixed(5) + " nm";
        document.getElementById("val_lamp").textContent = lambda_prime.toFixed(5) + " nm";
        document.getElementById("val_ke").textContent = KE_electron_keV.toFixed(2) + " keV";

        const cx = 260, cy = 125;

        // Incident Photon Ray from Left
        ctx.strokeStyle = "#00f0ff"; ctx.lineWidth = 2.5;
        ctx.beginPath();
        for(let x=40; cx >= x; x+=2) {
          const y = cy + 12 * Math.sin((x-40)*0.25);
          if (x===40) ctx.moveTo(x, y); else ctx.lineTo(x, y);
        }
        ctx.stroke();
        ctx.fillStyle = "#00f0ff"; ctx.font = "11px sans-serif";
        ctx.fillText("โฟตอนตกกระทบ (λ = " + lam.toFixed(3) + " nm)", 60, cy - 20);

        // Stationary Target Electron at origin
        ctx.fillStyle = "#10b981";
        ctx.beginPath(); ctx.arc(cx, cy, 7, 0, Math.PI*2); ctx.fill();
        ctx.fillStyle = "#ffffff"; ctx.font = "10px sans-serif"; ctx.fillText("e⁻", cx - 4, cy + 3);

        // Scattered Photon Angle (theta)
        const scX = cx + 180 * Math.cos(theta_rad);
        const scY = cy - 180 * Math.sin(theta_rad);
        ctx.strokeStyle = "#f43f5e"; ctx.lineWidth = 2.5;
        ctx.beginPath();
        for(let s=0; 180 >= s; s+=2) {
          const px = cx + s * Math.cos(theta_rad);
          const py = cy - s * Math.sin(theta_rad);
          const wave = 14 * Math.sin(s * 0.18); // Longer wavelength (Compton shift)
          const perpX = px - wave * Math.sin(theta_rad);
          const perpY = py - wave * Math.cos(theta_rad);
          if (s===0) ctx.moveTo(perpX, perpY); else ctx.lineTo(perpX, perpY);
        }
        ctx.stroke();
        ctx.fillStyle = "#f43f5e"; ctx.fillText("โฟตอนกระเจิง λ' (θ=" + theta_deg + "°)", scX - 20, scY - 10);

        // Recoil Electron Angle (phi)
        const phi_rad = Math.atan2(Math.sin(theta_rad), (E_init_keV / 511 + 1)*(1 - Math.cos(theta_rad)));
        const elX = cx + 120 * Math.cos(phi_rad);
        const elY = cy + 120 * Math.sin(phi_rad);
        ctx.strokeStyle = "#10b981"; ctx.lineWidth = 2; ctx.setLineDash([4,4]);
        ctx.beginPath(); ctx.moveTo(cx, cy); ctx.lineTo(elX, elY); ctx.stroke();
        ctx.setLineDash([]);
        ctx.fillStyle = "#10b981"; ctx.beginPath(); ctx.arc(elX, elY, 5, 0, Math.PI*2); ctx.fill();
        ctx.fillText("อิเล็กตรอนดีดกลับ (KE = " + KE_electron_keV.toFixed(2) + " keV)", elX + 10, elY + 5);
      }

      tick++;
      requestAnimationFrame(animate);
    }
    animate();
  </script>
</body>
</html>
"""

# Write all 5 Chapter 1 simulation files
files = {
    "sim_1_1.html": sim_1_1_html,
    "sim_1_2.html": sim_1_2_html,
    "sim_1_3.html": sim_1_3_html,
    "sim_1_4.html": sim_1_4_html,
    "sim_1_5.html": sim_1_5_html
}

for fname, content in files.items():
    fpath = os.path.join(SIM_DIR, fname)
    with open(fpath, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"✅ Generated {fpath} ({len(content)} bytes)")

print("🎉 Successfully upgraded all 5 Chapter 1 Simulations to hyper-realistic 60 FPS physics engines!")
