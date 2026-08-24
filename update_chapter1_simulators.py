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

# 1.1
body_1_1 = """
  <div class="sim-card">
    <div class="sim-header">
      <div class="sim-title"><span>🔬</span> 1.1 ข้อจำกัดของฟิสิกส์ดั้งเดิม: ปริศนาหายนะอัลตราไวโอเลต</div>
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
    <div class="canvas-box"><canvas id="simCanvas" width="640" height="230"></canvas></div>
    <div class="readout-grid">
      <div class="readout-card"><div class="readout-val" id="val_rj" style="color:#f43f5e;">ลู่ออกสู่อนันต์ (∞)</div><div class="readout-lbl">Rayleigh-Jeans (Classical)</div></div>
      <div class="readout-card"><div class="readout-val" id="val_planck" style="color:#00f0ff;">จุดยอด 580 nm</div><div class="readout-lbl">Planck Quantum Peak (λ_max)</div></div>
      <div class="readout-card"><div class="readout-val" id="val_status" style="color:#f59e0b;">UV Catastrophe!</div><div class="readout-lbl">พฤติกรรมย่านความถี่สูง (UV)</div></div>
    </div>
  </div>
"""

js_1_1 = """
    const cv = document.getElementById("simCanvas");
    const ctx = cv.getContext("2d");
    const sliderTemp = document.getElementById("slider_temp");
    const selTheory = document.getElementById("sel_theory");
    let tick = 0;

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

      // Left Panel: Blackbody Cavity
      ctx.fillStyle = "#0f172a"; ctx.strokeStyle = "#334155"; ctx.lineWidth = 1.5;
      ctx.fillRect(20, 20, 115, 185); ctx.strokeRect(20, 20, 115, 185);
      ctx.clearRect(133, 95, 5, 30); // Pinhole

      const heatGrad = ctx.createRadialGradient(77, 112, 10, 77, 112, 75);
      heatGrad.addColorStop(0, "rgba(245, 158, 11, 0.45)");
      heatGrad.addColorStop(0.6, "rgba(239, 68, 68, 0.2)");
      heatGrad.addColorStop(1, "transparent");
      ctx.fillStyle = heatGrad; ctx.fillRect(21, 21, 113, 183);

      particles.forEach(p => {
        ctx.fillStyle = p.color; ctx.beginPath(); ctx.arc(p.x, p.y, 2.5, 0, Math.PI*2); ctx.fill();
        p.x += p.vx * (T / 4000); p.y += p.vy * (T / 4000);
        if (24 > p.x || p.x > 130) p.vx *= -1;
        if (25 > p.y || p.y > 200) p.vy *= -1;
      });

      ctx.strokeStyle = "rgba(0, 240, 255, 0.7)"; ctx.lineWidth = 2;
      for(let k=0; 3 > k; k++) {
        const beamX = 135 + ((tick*3 + k*40) % 45);
        ctx.beginPath(); ctx.moveTo(135, 110 + (k-1)*8); ctx.lineTo(beamX, 110 + (k-1)*8); ctx.stroke();
      }

      ctx.fillStyle = "#94a3b8"; ctx.font = "10px sans-serif";
      ctx.fillText("โพรงวัตถุดำ", 45, 36); ctx.fillText("(T = " + T + " K)", 48, 50);
      ctx.fillStyle = "#00f0ff"; ctx.fillText("รูเปิด →", 95, 114);

      // Right Panel: Spectrum
      const originX = 190, originY = 205, graphW = 425, graphH = 175;

      ctx.fillStyle = "rgba(168, 85, 247, 0.15)"; ctx.fillRect(originX, 30, 65, graphH);
      ctx.fillStyle = "#a855f7"; ctx.font = "10px sans-serif"; ctx.fillText("UV", originX + 22, 44);

      const visGrad = ctx.createLinearGradient(originX + 65, 0, originX + 155, 0);
      visGrad.addColorStop(0, "rgba(59, 130, 246, 0.25)"); visGrad.addColorStop(0.5, "rgba(34, 197, 94, 0.25)"); visGrad.addColorStop(1, "rgba(239, 68, 68, 0.25)");
      ctx.fillStyle = visGrad; ctx.fillRect(originX + 65, 30, 90, graphH);
      ctx.fillStyle = "#10b981"; ctx.fillText("Visible", originX + 85, 44);

      ctx.fillStyle = "rgba(239, 68, 68, 0.10)"; ctx.fillRect(originX + 155, 30, 270, graphH);
      ctx.fillStyle = "#ef4444"; ctx.fillText("Infrared (IR)", originX + 240, 44);

      // Curves
      if (mode === "both" || mode === "classical") {
        ctx.strokeStyle = "#f43f5e"; ctx.lineWidth = 2.5; ctx.setLineDash([4, 3]);
        ctx.beginPath();
        for(let px = originX + 5; originX + graphW >= px; px += 2) {
          const lam_nm = (px - originX) * 4.5;
          const y_rj = originY - (2.5e11 * (T / 5000)) / Math.pow(lam_nm + 15, 3.2);
          if (px === originX + 5) ctx.moveTo(px, Math.max(30, y_rj)); else ctx.lineTo(px, Math.max(30, y_rj));
        }
        ctx.stroke(); ctx.setLineDash([]);
      }

      if (mode === "both" || mode === "planck") {
        ctx.strokeStyle = "#00f0ff"; ctx.lineWidth = 3;
        ctx.beginPath();
        for(let px = originX + 5; originX + graphW >= px; px += 2) {
          const lam_nm = (px - originX) * 4.5;
          const p = Math.pow(T / 1000, 3) * Math.pow(lam_nm / peakLam, 5) / (Math.exp((lam_nm ? peakLam / lam_nm : 10) * 2.2) - 1 + 0.05);
          const y = originY - Math.min(165, p * 5.5);
          if (px === originX + 5) ctx.moveTo(px, y); else ctx.lineTo(px, y);
        }
        ctx.stroke();

        const peakX = originX + (peakLam / 4.5);
        if (peakX >= originX && originX + graphW >= peakX) {
          ctx.strokeStyle = "#f59e0b"; ctx.lineWidth = 1.8; ctx.setLineDash([3, 3]);
          ctx.beginPath(); ctx.moveTo(peakX, 30); ctx.lineTo(peakX, originY); ctx.stroke();
          ctx.setLineDash([]);
          ctx.fillStyle = "#f59e0b"; ctx.font = "11px sans-serif";
          ctx.fillText("λ_max = " + peakLam + " nm", peakX + 5, 62);
        }
      }

      ctx.strokeStyle = "#94a3b8"; ctx.lineWidth = 1.5;
      ctx.beginPath(); ctx.moveTo(originX, 30); ctx.lineTo(originX, originY); ctx.lineTo(originX + graphW, originY); ctx.stroke();
      ctx.fillStyle = "#94a3b8"; ctx.font = "11px sans-serif";
      ctx.fillText("ความยาวคลื่น λ (nm) →", originX + graphW - 120, originY + 16);
      ctx.fillText("ความเข้ม I(λ)", originX - 10, 22);

      ctx.fillStyle = "#f43f5e"; ctx.fillText("-- Classical (Rayleigh-Jeans)", originX + 70, 80);
      ctx.fillStyle = "#00f0ff"; ctx.fillText("— Quantum (Planck)", originX + 70, 96);

      tick++;
      requestAnimationFrame(animate);
    }
    animate();
"""

# 1.2
body_1_2 = """
  <div class="sim-card">
    <div class="sim-header">
      <div class="sim-title"><span>🔬</span> 1.2 การแผ่รังสีของวัตถุดำ & กฎของวีนและสเตฟาน-โบลทซ์มานน์</div>
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
    <div class="canvas-box"><canvas id="simCanvas" width="640" height="230"></canvas></div>
    <div class="readout-grid">
      <div class="readout-card"><div class="readout-val" id="val_peak">500 nm</div><div class="readout-lbl">ความยาวคลื่นสูงสุด (λ_max = b/T)</div></div>
      <div class="readout-card"><div class="readout-val" id="val_color">ขาว-เหลือง</div><div class="readout-lbl">สีของรังสีความร้อนที่ปรากฏ</div></div>
      <div class="readout-card"><div class="readout-val" id="val_power">6.42 × 10⁷ W/m²</div><div class="readout-lbl">กำลังแผ่รังสีรวม (I = σT⁴)</div></div>
    </div>
  </div>
"""

js_1_2 = """
    const cv = document.getElementById("simCanvas");
    const ctx = cv.getContext("2d");
    const sliderTemp = document.getElementById("slider_temp");
    const selPreset = document.getElementById("sel_preset");
    let tick = 0;

    selPreset.addEventListener("change", () => {
      sliderTemp.value = selPreset.value;
    });

    function getBlackbodyRGB(T) {
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

      const peakLam = Math.round(2898000 / T);
      document.getElementById("val_peak").textContent = peakLam >= 1000 ? (peakLam/1000).toFixed(2) + " µm (IR)" : peakLam + " nm";

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

      // Star Glow
      const starX = 80, starY = 115, starR = 50;
      for(let f=0; 3 > f; f++) {
        const flareR = starR + 8 + Math.sin(tick*0.06 + f)*4;
        ctx.fillStyle = "rgba(" + rgb.r + "," + rgb.g + "," + rgb.b + "," + (0.15 - f*0.04) + ")";
        ctx.beginPath(); ctx.arc(starX, starY, flareR, 0, Math.PI*2); ctx.fill();
      }

      const starGrad = ctx.createRadialGradient(starX - 15, starY - 15, 4, starX, starY, starR);
      starGrad.addColorStop(0, "#ffffff");
      starGrad.addColorStop(0.35, "rgb(" + rgb.r + "," + rgb.g + "," + rgb.b + ")");
      starGrad.addColorStop(1, "rgba(" + Math.round(rgb.r*0.4) + "," + Math.round(rgb.g*0.4) + "," + Math.round(rgb.b*0.4) + ", 0.95)");
      ctx.fillStyle = starGrad;
      ctx.beginPath(); ctx.arc(starX, starY, starR, 0, Math.PI*2); ctx.fill();

      ctx.fillStyle = "#ffffff"; ctx.font = "11px sans-serif";
      ctx.fillText("วัตถุดำ / ดาวฤกษ์", starX - 40, starY + 68);
      ctx.fillStyle = "#00f0ff";
      ctx.fillText("T = " + T + " K", starX - 22, starY + 82);

      // Spectrum
      const originX = 175, originY = 205, graphW = 440, graphH = 175;

      const visStartX = originX + (400 / 3000 * graphW);
      const visEndX = originX + (750 / 3000 * graphW);
      const visGrad = ctx.createLinearGradient(visStartX, 0, visEndX, 0);
      visGrad.addColorStop(0, "rgba(59, 130, 246, 0.2)"); visGrad.addColorStop(0.5, "rgba(34, 197, 94, 0.2)"); visGrad.addColorStop(1, "rgba(239, 68, 68, 0.2)");
      ctx.fillStyle = visGrad; ctx.fillRect(visStartX, 30, visEndX - visStartX, graphH);

      ctx.strokeStyle = "rgb(" + rgb.r + "," + rgb.g + "," + rgb.b + ")";
      ctx.lineWidth = 3;
      ctx.beginPath();
      for(let px = originX + 2; originX + graphW >= px; px += 2) {
        const lam = ((px - originX) / graphW) * 3000;
        const p = Math.pow(T / 1000, 3) * Math.pow(lam / peakLam, 5) / (Math.exp((lam ? peakLam / lam : 10) * 2.5) - 1 + 0.05);
        const y = originY - Math.min(165, p * 5.5);
        if (px === originX + 2) ctx.moveTo(px, y); else ctx.lineTo(px, y);
      }
      ctx.stroke();

      const peakX = originX + (peakLam / 3000 * graphW);
      if (peakX >= originX && originX + graphW >= peakX) {
        ctx.strokeStyle = "#f59e0b"; ctx.lineWidth = 2; ctx.setLineDash([4, 4]);
        ctx.beginPath(); ctx.moveTo(peakX, 30); ctx.lineTo(peakX, originY); ctx.stroke();
        ctx.setLineDash([]);
        ctx.fillStyle = "#f59e0b"; ctx.font = "11px sans-serif";
        ctx.fillText("λ_max = " + (peakLam >= 1000 ? (peakLam/1000).toFixed(2) + " µm" : peakLam + " nm"), peakX + 6, 60);
      }

      ctx.strokeStyle = "#94a3b8"; ctx.lineWidth = 1.5;
      ctx.beginPath(); ctx.moveTo(originX, 30); ctx.lineTo(originX, originY); ctx.lineTo(originX + graphW, originY); ctx.stroke();
      ctx.fillStyle = "#94a3b8"; ctx.font = "11px sans-serif";
      ctx.fillText("ความยาวคลื่น λ (nm) →", originX + graphW - 120, originY + 16);
      ctx.fillText("ความเข้ม I(λ)", originX - 10, 22);

      tick++;
      requestAnimationFrame(animate);
    }
    animate();
"""

# 1.3
body_1_3 = """
  <div class="sim-card">
    <div class="sim-header">
      <div class="sim-title"><span>🔬</span> 1.3 ปรากฏการณ์โฟโตอิเล็กทริก: หลอดสุญญากาศ & ศักย์หยุดยั้ง</div>
      <div class="badge-fps">● 60 FPS REAL-TIME</div>
    </div>
    <div class="control-grid" style="grid-template-columns: repeat(3, 1fr);">
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
    <div class="canvas-box"><canvas id="simCanvas" width="640" height="235"></canvas></div>
    <div class="readout-grid" style="grid-template-columns: repeat(4, 1fr);">
      <div class="readout-card"><div class="readout-val" id="val_ephoton">4.13 eV</div><div class="readout-lbl">พลังงานโฟตอน (E=hf)</div></div>
      <div class="readout-card"><div class="readout-val" id="val_kmax">1.83 eV</div><div class="readout-lbl">พลังงานจลน์ (K_max)</div></div>
      <div class="readout-card"><div class="readout-val" id="val_vs">1.83 V</div><div class="readout-lbl">ศักย์หยุดยั้ง (V_s)</div></div>
      <div class="readout-card"><div class="readout-val" id="val_current" style="color:#10b981;">18.4 µA</div><div class="readout-lbl">กระแสไฟฟ้า (I)</div></div>
    </div>
  </div>
"""

js_1_3 = """
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
        y: 40 + Math.random()*120,
        vx: 1.5 + Math.random()*3.0,
        vy: (Math.random()-0.5)*1.2
      });
    }

    function animate() {
      const phi = +selMetal.value;
      const lam = +sliderLam.value;
      const V_ext = +sliderV.value;

      document.getElementById("val_lam").textContent = lam;
      document.getElementById("val_v").textContent = (V_ext >= 0 ? "+" : "") + V_ext.toFixed(2);

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
        if (V_ext > -Vs) {
          const saturationFactor = Math.min(1.0, 0.6 + 0.4 * (V_ext + Vs) / (1.5 + Vs));
          current_uA = (25.0 * saturationFactor).toFixed(1);
          curEl.textContent = current_uA + " µA";
          curEl.style.color = "#10b981";
        } else {
          curEl.textContent = "0.00 µA (หยุดยั้ง)";
          curEl.style.color = "#f43f5e";
        }
      } else {
        kmEl.textContent = "0.00 (ไม่หลุด)";
        vsEl.textContent = "0.00 V";
        curEl.textContent = "0.00 µA";
        curEl.style.color = "#64748b";
      }

      ctx.clearRect(0, 0, cv.width, cv.height);

      // Tube
      ctx.strokeStyle = "rgba(148, 163, 184, 0.4)"; ctx.lineWidth = 2;
      ctx.fillStyle = "rgba(15, 23, 42, 0.7)";
      ctx.beginPath(); ctx.roundRect(80, 20, 480, 160, 16); ctx.fill(); ctx.stroke();

      // Window
      ctx.strokeStyle = "#38bdf8"; ctx.lineWidth = 3;
      ctx.beginPath(); ctx.moveTo(95, 20); ctx.lineTo(155, 20); ctx.stroke();

      // Plates
      ctx.fillStyle = "#64748b"; ctx.fillRect(100, 35, 14, 130);
      ctx.fillStyle = "#00f0ff"; ctx.font = "10px sans-serif";
      ctx.fillText("Emitter (φ=" + phi + "eV)", 35, 198);

      ctx.fillStyle = "#475569"; ctx.fillRect(525, 35, 14, 130);
      ctx.fillStyle = "#94a3b8";
      ctx.fillText("Collector (V=" + (V_ext >= 0 ? "+" : "") + V_ext.toFixed(2) + "V)", 440, 198);

      // Photons
      let photonColor = 400 > lam ? "#a855f7" : (500 > lam ? "#00f0ff" : (600 > lam ? "#10b981" : "#ef4444"));
      ctx.strokeStyle = photonColor; ctx.lineWidth = 2.5;
      for(let p=0; 5 > p; p++) {
        const prog = ((tick*3.5 + p*50) % 110) / 110;
        const px = 20 + prog * 85;
        const py = 15 + prog * 55 + (p-2)*16;
        ctx.beginPath(); ctx.moveTo(px - 14, py - 10); ctx.lineTo(px, py); ctx.stroke();
      }

      // Electrons
      if (Kmax > 0) {
        const eAcc = (V_ext / 3.0) * 0.08;
        ctx.fillStyle = "#10b981";
        electrons.forEach(el => {
          ctx.beginPath(); ctx.arc(el.x, el.y, 3.8, 0, Math.PI*2); ctx.fill();
          el.x += el.vx; el.y += el.vy; el.vx += eAcc;
          if (el.x >= 525 || (110 > el.x && 0 > el.vx)) {
            el.x = 116; el.y = 45 + Math.random()*110; el.vx = Math.sqrt(Kmax)*1.8 + Math.random()*1.0;
          }
        });
      }

      // Circuit
      ctx.strokeStyle = "#334155"; ctx.lineWidth = 1.5;
      ctx.beginPath();
      ctx.moveTo(107, 165); ctx.lineTo(107, 218); ctx.lineTo(260, 218);
      ctx.moveTo(532, 165); ctx.lineTo(532, 218); ctx.lineTo(380, 218);
      ctx.stroke();

      ctx.fillStyle = "#0f172a"; ctx.strokeStyle = "#00f0ff";
      ctx.fillRect(260, 206, 120, 22); ctx.strokeRect(260, 206, 120, 22);
      ctx.fillStyle = current_uA > 0 ? "#10b981" : "#f43f5e"; ctx.font = "bold 11px 'JetBrains Mono', monospace";
      ctx.fillText("µA: " + current_uA + " µA", 280, 222);

      tick++;
      requestAnimationFrame(animate);
    }
    animate();
"""

# 1.4
body_1_4 = """
  <div class="sim-card">
    <div class="sim-header">
      <div class="sim-title"><span>🔬</span> 1.4 สเปกตรัมของไฮโดรเจน: การเปลี่ยนระดับพลังงาน & สูตรริดเบิร์ก</div>
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
    <div class="canvas-box"><canvas id="simCanvas" width="640" height="235"></canvas></div>
    <div class="readout-grid">
      <div class="readout-card"><div class="readout-val" id="val_lam">656.3 nm</div><div class="readout-lbl">ความยาวคลื่นโฟตอนที่คาย (λ)</div></div>
      <div class="readout-card"><div class="readout-val" id="val_de">1.89 eV</div><div class="readout-lbl">พลังงานที่ปลดปล่อย (ΔE)</div></div>
      <div class="readout-card"><div class="readout-val" id="val_line" style="color:#ef4444;">H-alpha (สีแดง)</div><div class="readout-lbl">ชื่อและสีเส้นสเปกตรัม</div></div>
    </div>
  </div>
"""

js_1_4 = """
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
      if (n1 === 1) { name = "Lyman (" + n2 + "→1 UV)"; col = "#a855f7"; }
      else if (n1 === 2) {
        if (n2 === 3) { name = "H-alpha (สีแดง 656.3 nm)"; col = "#ef4444"; }
        else if (n2 === 4) { name = "H-beta (ฟ้าคราม 486.1 nm)"; col = "#06b6d4"; }
        else if (n2 === 5) { name = "H-gamma (น้ำเงิน 434.0 nm)"; col = "#3b82f6"; }
        else { name = "H-delta (ม่วง 410.2 nm)"; col = "#8b5cf6"; }
      } else if (n1 === 3) { name = "Paschen (" + n2 + "→3 IR)"; col = "#f97316"; }
      else { name = "Brackett (" + n2 + "→4 Far-IR)"; col = "#e11d48"; }
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
      lnEl.textContent = info.name; lnEl.style.color = info.color;

      ctx.clearRect(0, 0, cv.width, cv.height);

      // Left Panel: Bohr Ladder
      const ladderX = 35, ladderW = 215;
      ctx.fillStyle = "#94a3b8"; ctx.font = "11px sans-serif";
      ctx.fillText("ระดับพลังงานควอนตัม (Bohr Energy Levels)", ladderX, 18);

      for(let n=1; 7 > n; n++) {
        const y = 205 - 165 * (1 - 1/(n*n));
        const isTarget = (n === n1), isInitial = (n === n2);
        ctx.strokeStyle = isTarget ? "#00f0ff" : (isInitial ? "#f59e0b" : "#334155");
        ctx.lineWidth = (isTarget || isInitial) ? 2.5 : 1;
        ctx.beginPath(); ctx.moveTo(ladderX, y); ctx.lineTo(ladderX + ladderW, y); ctx.stroke();

        ctx.fillStyle = isTarget ? "#00f0ff" : (isInitial ? "#f59e0b" : "#64748b");
        ctx.font = "10px 'JetBrains Mono', monospace";
        ctx.fillText("n=" + n + " (" + (-13.6/(n*n)).toFixed(2) + " eV)", ladderX + ladderW + 6, y + 4);
      }

      // Transition Arrow
      const yStart = 205 - 165 * (1 - 1/(n2*n2));
      const yEnd = 205 - 165 * (1 - 1/(n1*n1));
      ctx.strokeStyle = info.color; ctx.lineWidth = 3;
      ctx.beginPath(); ctx.moveTo(ladderX + 105, yStart); ctx.lineTo(ladderX + 105, yEnd); ctx.stroke();
      ctx.fillStyle = info.color;
      ctx.beginPath(); ctx.moveTo(ladderX + 100, yEnd - 8); ctx.lineTo(ladderX + 110, yEnd - 8); ctx.lineTo(ladderX + 105, yEnd); ctx.fill();

      // Emitted Photon
      const prog = (tick*0.04) % 1;
      const photonWaveX = ladderX + 105 + prog * 175;
      ctx.fillStyle = info.color;
      ctx.beginPath(); ctx.arc(photonWaveX, (yStart + yEnd)/2, 4.5, 0, Math.PI*2); ctx.fill();

      // Right Panel: Spectrograph Film
      const specX = 350, specY = 35, specW = 265, specH = 75;
      ctx.fillStyle = "#030712"; ctx.strokeStyle = "#1e293b"; ctx.lineWidth = 2;
      ctx.fillRect(specX, specY, specW, specH); ctx.strokeRect(specX, specY, specW, specH);

      ctx.fillStyle = "#94a3b8"; ctx.font = "11px sans-serif";
      ctx.fillText("แถบสเปกโตรกราฟ (Spectrograph Film)", specX, 26);

      if (n1 === 2) {
        const balmerLines = [
          { n: 3, lam: 656.3, col: "#ef4444" },
          { n: 4, lam: 486.1, col: "#06b6d4" },
          { n: 5, lam: 434.0, col: "#3b82f6" },
          { n: 6, lam: 410.2, col: "#8b5cf6" }
        ];
        balmerLines.forEach(l => {
          const lx = specX + ((l.lam - 380) / 320) * specW;
          const isSelected = (l.n === n2);
          ctx.strokeStyle = l.col; ctx.lineWidth = isSelected ? 4.0 : 1.8;
          ctx.beginPath(); ctx.moveTo(lx, specY); ctx.lineTo(lx, specY + specH); ctx.stroke();
          if (isSelected) {
            ctx.fillStyle = l.col; ctx.font = "bold 10px sans-serif";
            ctx.fillText(l.lam + " nm", lx - 18, specY + specH + 15);
          }
        });
      } else {
        const lx = specX + specW / 2;
        ctx.strokeStyle = info.color; ctx.lineWidth = 3.5;
        ctx.beginPath(); ctx.moveTo(lx, specY); ctx.lineTo(lx, specY + specH); ctx.stroke();
        ctx.fillStyle = info.color; ctx.font = "bold 10px sans-serif";
        ctx.fillText(info.lam >= 1000 ? (info.lam/1000).toFixed(2) + " µm" : info.lam.toFixed(1) + " nm", lx - 20, specY + specH + 15);
      }

      // Summary
      ctx.fillStyle = "rgba(15, 23, 42, 0.8)"; ctx.strokeStyle = "#334155";
      ctx.fillRect(specX, 150, specW, 60); ctx.strokeRect(specX, 150, specW, 60);
      ctx.fillStyle = "#00f0ff"; ctx.font = "11px 'JetBrains Mono', monospace";
      ctx.fillText("1/λ = R_H (1/n₁² - 1/n₂²)", specX + 15, 172);
      ctx.fillStyle = "#94a3b8"; ctx.font = "10px sans-serif";
      ctx.fillText("R_H = 1.097373 × 10⁷ m⁻¹", specX + 15, 192);

      tick++;
      requestAnimationFrame(animate);
    }
    animate();
"""

# 1.5
body_1_5 = """
  <div class="sim-card">
    <div class="sim-header">
      <div class="sim-title"><span>🔬</span> 1.5 ปฏิบัติการควอนตัม: เซลล์แสงอาทิตย์ (Bandgap) & การกระเจิงคอมป์ตัน</div>
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
        <label>ความยาวคลื่นโฟตอนเอกซเรย์ (λ): <span id="val_compton_lam" class="val-display">0.020</span> nm</label>
        <input type="range" id="slider_compton_lam" min="0.005" max="0.050" step="0.001" value="0.020">
      </div>
      <div class="ctrl-box">
        <label>มุมการกระเจิงของโฟตอน (θ): <span id="val_theta" class="val-display">90</span>°</label>
        <input type="range" id="slider_theta" min="0" max="180" step="1" value="90">
      </div>
    </div>
    <div class="canvas-box"><canvas id="simCanvas" width="640" height="235"></canvas></div>
    <div class="readout-grid" id="readoutsSolar">
      <div class="readout-card"><div class="readout-val" id="val_eph">2.07 eV</div><div class="readout-lbl">พลังงานโฟตอน (E = hc/λ)</div></div>
      <div class="readout-card"><div class="readout-val" id="val_cutoff">1,107 nm</div><div class="readout-lbl">ความยาวคลื่นคัตออฟ (λ_g)</div></div>
      <div class="readout-card"><div class="readout-val" id="val_status" style="color:#10b981;">ดูดกลืน & เกิดกระแสไฟฟ้า</div><div class="readout-lbl">สถานะการทำงานเซลล์</div></div>
    </div>
    <div class="readout-grid" id="readoutsCompton" style="display:none;">
      <div class="readout-card"><div class="readout-val" id="val_dlam">+0.00243 nm</div><div class="readout-lbl">ความยาวคลื่นเพิ่มขึ้น (Δλ)</div></div>
      <div class="readout-card"><div class="readout-val" id="val_lamp">0.02243 nm</div><div class="readout-lbl">ความยาวคลื่นกระเจิง (λ')</div></div>
      <div class="readout-card"><div class="readout-val" id="val_ke">6.72 keV</div><div class="readout-lbl">พลังงานจลน์อิเล็กตรอนดีดกลับ</div></div>
    </div>
  </div>
"""

js_1_5 = """
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

    let pairs = [];
    for(let i=0; 20 > i; i++) {
      pairs.push({
        x: 90 + Math.random()*150,
        y: 70 + Math.random()*70,
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
          statEl.textContent = "ดูดกลืน & เกิดกระแสไฟฟ้า"; statEl.style.color = "#10b981";
        } else {
          statEl.textContent = "ทะลุผ่าน (E < Eg ไม่เกิดกระแส)"; statEl.style.color = "#f43f5e";
        }

        // p-n junction
        ctx.fillStyle = "#1e293b"; ctx.fillRect(70, 40, 190, 140);
        ctx.fillStyle = "rgba(59, 130, 246, 0.3)"; ctx.fillRect(70, 40, 190, 70);
        ctx.fillStyle = "rgba(239, 68, 68, 0.3)"; ctx.fillRect(70, 110, 190, 70);
        ctx.strokeStyle = "#00f0ff"; ctx.lineWidth = 1.5; ctx.strokeRect(70, 40, 190, 140);

        ctx.fillStyle = "#60a5fa"; ctx.font = "11px sans-serif"; ctx.fillText("n-type Silicon", 80, 58);
        ctx.fillStyle = "#f87171"; ctx.fillText("p-type Silicon", 80, 172);
        ctx.strokeStyle = "#f59e0b"; ctx.lineWidth = 1; ctx.setLineDash([3,3]);
        ctx.beginPath(); ctx.moveTo(70, 110); ctx.lineTo(260, 110); ctx.stroke(); ctx.setLineDash([]);
        ctx.fillStyle = "#f59e0b"; ctx.fillText("p-n Junction", 165, 107);

        let rayCol = 400 > lam ? "#a855f7" : (700 > lam ? "#10b981" : "#ef4444");
        ctx.strokeStyle = rayCol; ctx.lineWidth = 2.5;
        for(let r=0; 3 > r; r++) {
          const prog = ((tick*3 + r*40) % 90) / 90;
          const rx = 25 + prog*45, ry = 35 + prog*45 + r*18;
          ctx.beginPath(); ctx.moveTo(rx-14, ry-14); ctx.lineTo(rx, ry); ctx.stroke();
        }

        if (isAbsorbed) {
          pairs.forEach(p => {
            ctx.fillStyle = "#38bdf8"; ctx.beginPath(); ctx.arc(p.x, p.y + p.vy_e * (tick%28), 3.5, 0, Math.PI*2); ctx.fill();
            ctx.fillStyle = "#f43f5e"; ctx.beginPath(); ctx.arc(p.x, p.y + p.vy_h * (tick%28), 3.5, 0, Math.PI*2); ctx.fill();
          });
        }

        // Bandgap Diagram
        ctx.fillStyle = "#0f172a"; ctx.strokeStyle = "#334155";
        ctx.fillRect(320, 40, 260, 140); ctx.strokeRect(320, 40, 260, 140);

        ctx.fillStyle = "rgba(56, 189, 248, 0.4)"; ctx.fillRect(335, 50, 230, 26);
        ctx.fillStyle = "#38bdf8"; ctx.fillText("Conduction Band (แถบนำไฟฟ้า)", 345, 67);

        ctx.fillStyle = "rgba(239, 68, 68, 0.4)"; ctx.fillRect(335, 142, 230, 26);
        ctx.fillStyle = "#f87171"; ctx.fillText("Valence Band (แถบเวเลนซ์)", 345, 159);

        ctx.strokeStyle = "#f59e0b"; ctx.lineWidth = 2;
        ctx.beginPath(); ctx.moveTo(450, 142); ctx.lineTo(450, 78); ctx.stroke();
        ctx.fillStyle = "#f59e0b"; ctx.font = "bold 11px sans-serif";
        ctx.fillText("Bandgap Eg = " + Eg + " eV", 360, 114);
      }
      else {
        const lam = +document.getElementById("slider_compton_lam").value;
        const theta_deg = +document.getElementById("slider_theta").value;
        const theta_rad = theta_deg * Math.PI / 180;

        document.getElementById("val_compton_lam").textContent = lam.toFixed(3);
        document.getElementById("val_theta").textContent = theta_deg;

        const lambda_c = 0.0024263;
        const delta_lambda = lambda_c * (1 - Math.cos(theta_rad));
        const lambda_prime = lam + delta_lambda;

        const E_init_keV = 1.23984 / lam;
        const E_scattered_keV = 1.23984 / lambda_prime;
        const KE_electron_keV = E_init_keV - E_scattered_keV;

        document.getElementById("val_dlam").textContent = "+" + delta_lambda.toFixed(5) + " nm";
        document.getElementById("val_lamp").textContent = lambda_prime.toFixed(5) + " nm";
        document.getElementById("val_ke").textContent = KE_electron_keV.toFixed(2) + " keV";

        const cx = 250, cy = 115;

        ctx.strokeStyle = "#00f0ff"; ctx.lineWidth = 2.5;
        ctx.beginPath();
        for(let x=40; cx >= x; x+=2) {
          const y = cy + 12 * Math.sin((x-40)*0.25);
          if (x===40) ctx.moveTo(x, y); else ctx.lineTo(x, y);
        }
        ctx.stroke();
        ctx.fillStyle = "#00f0ff"; ctx.font = "11px sans-serif";
        ctx.fillText("โฟตอนตกกระทบ (λ = " + lam.toFixed(3) + " nm)", 55, cy - 18);

        ctx.fillStyle = "#10b981";
        ctx.beginPath(); ctx.arc(cx, cy, 7, 0, Math.PI*2); ctx.fill();
        ctx.fillStyle = "#ffffff"; ctx.font = "10px sans-serif"; ctx.fillText("e⁻", cx - 4, cy + 3);

        const scX = cx + 170 * Math.cos(theta_rad);
        const scY = cy - 170 * Math.sin(theta_rad);
        ctx.strokeStyle = "#f43f5e"; ctx.lineWidth = 2.5;
        ctx.beginPath();
        for(let s=0; 170 >= s; s+=2) {
          const px = cx + s * Math.cos(theta_rad);
          const py = cy - s * Math.sin(theta_rad);
          const wave = 13 * Math.sin(s * 0.18);
          const perpX = px - wave * Math.sin(theta_rad);
          const perpY = py - wave * Math.cos(theta_rad);
          if (s===0) ctx.moveTo(perpX, perpY); else ctx.lineTo(perpX, perpY);
        }
        ctx.stroke();
        ctx.fillStyle = "#f43f5e"; ctx.fillText("โฟตอนกระเจิง λ' (θ=" + theta_deg + "°)", scX - 20, scY - 10);

        const phi_rad = Math.atan2(Math.sin(theta_rad), (E_init_keV / 511 + 1)*(1 - Math.cos(theta_rad)));
        const elX = cx + 115 * Math.cos(phi_rad);
        const elY = cy + 115 * Math.sin(phi_rad);
        ctx.strokeStyle = "#10b981"; ctx.lineWidth = 2; ctx.setLineDash([4,4]);
        ctx.beginPath(); ctx.moveTo(cx, cy); ctx.lineTo(elX, elY); ctx.stroke();
        ctx.setLineDash([]);
        ctx.fillStyle = "#10b981"; ctx.beginPath(); ctx.arc(elX, elY, 5, 0, Math.PI*2); ctx.fill();
        ctx.fillText("อิเล็กตรอนดีดกลับ (KE = " + KE_electron_keV.toFixed(2) + " keV)", elX + 8, elY + 4);
      }

      tick++;
      requestAnimationFrame(animate);
    }
    animate();
"""

files = {
    "sim_1_1.html": wrap_html("1.1 ข้อจำกัดของฟิสิกส์ดั้งเดิม", body_1_1, js_1_1),
    "sim_1_2.html": wrap_html("1.2 การแผ่รังสีของวัตถุดำ & กฎของวีน", body_1_2, js_1_2),
    "sim_1_3.html": wrap_html("1.3 ปรากฏการณ์โฟโตอิเล็กทริก", body_1_3, js_1_3),
    "sim_1_4.html": wrap_html("1.4 สเปกตรัมของอะตอมไฮโดรเจน", body_1_4, js_1_4),
    "sim_1_5.html": wrap_html("1.5 ปฏิบัติการควอนตัมจำลอง", body_1_5, js_1_5)
}

for fname, content in files.items():
    fpath = os.path.join(SIM_DIR, fname)
    with open(fpath, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"✅ Generated {fpath} ({len(content)} bytes)")

print("🎉 Successfully generated all Chapter 1 simulators!")
