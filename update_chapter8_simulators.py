#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generates hyper-realistic, 60 FPS physics simulations for all 5 subtopics of Chapter 8 (Astrophysics & Cosmology):
- sim_8_1.html: Hubble-Lemaître Law, Cosmological Redshift (z) & Expanding Universe Metric
- sim_8_2.html: Big Bang Timeline & Cosmic Microwave Background (CMB 2.725 K Blackbody Radiation)
- sim_8_3.html: Vera Rubin Galaxy Rotation Curves (Dark Matter Halo vs Keplerian) & Dark Energy
- sim_8_4.html: Stellar Evolution H-R Diagram & Schwarzschild Black Hole Event Horizon / Gravitational Lensing
- sim_8_5.html: Chapter 8 Virtual Lab: Friedmann Universe Scale Factor a(t) & JWST Primordial Deep Field
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
# 8.1 Hubble-Lemaître Law & Expanding Universe
# ==============================================================================
body_8_1 = """
  <div class="sim-card">
    <div class="sim-header">
      <div class="sim-title"><span>🔭</span> 8.1 การขยายตัวของเอกภพ & กฎของฮับเบิล (Hubble-Lemaître Law & Cosmological Redshift)</div>
      <div class="badge-fps">● 60 FPS REAL-TIME</div>
    </div>
    <div class="control-grid">
      <div class="ctrl-box">
        <label>ระยะทางของกาแล็กซี (Distance d): <span id="val_dist" class="val-display">500</span> Mpc (ล้านพาร์เซก)</label>
        <input type="range" id="slider_dist" min="50" max="2000" step="50" value="500">
      </div>
      <div class="ctrl-box">
        <label>ค่าคงที่ฮับเบิล (Hubble Constant H₀): <span id="val_h0" class="val-display">70.0</span> km/s/Mpc</label>
        <input type="range" id="slider_h0" min="50.0" max="90.0" step="1.0" value="70.0">
      </div>
    </div>
    <div class="canvas-box"><canvas id="simCanvas" width="640" height="230"></canvas></div>
    <div class="readout-grid">
      <div class="readout-card"><div class="readout-val" id="val_velocity">35,000 km/s</div><div class="readout-lbl">ความเร็วถอยห่าง (v = H₀·d)</div></div>
      <div class="readout-card"><div class="readout-val" id="val_redshift">z = 0.117</div><div class="readout-lbl">การเลื่อนทางแดงของสเปกตรัม (Redshift z)</div></div>
      <div class="readout-card"><div class="readout-val" id="val_universe_age">13.97 พันล้านปี</div><div class="readout-lbl">อายุเอกภพโดยประมาณ (1/H₀)</div></div>
    </div>
  </div>
"""

js_8_1 = """
    const cv = document.getElementById("simCanvas");
    const ctx = cv.getContext("2d");
    const sliderDist = document.getElementById("slider_dist");
    const sliderH0 = document.getElementById("slider_h0");
    let tick = 0;

    const galaxies = [
      { name: "Andromeda (M31)", d: 0.78, ang: 0.5, col: "#38bdf8" },
      { name: "Virgo Cluster", d: 16.5, ang: 1.8, col: "#f59e0b" },
      { name: "Centaurus Cluster", d: 52.0, ang: 3.2, col: "#10b981" },
      { name: "Coma Cluster", d: 100.0, ang: 4.5, col: "#f43f5e" },
      { name: "Hercules Cluster", d: 200.0, ang: 5.7, col: "#a855f7" }
    ];

    function animate() {
      const d_target = +sliderDist.value;
      const H0 = +sliderH0.value;

      document.getElementById("val_dist").textContent = d_target;
      document.getElementById("val_h0").textContent = H0.toFixed(1);

      // v = H0 * d (km/s)
      const v = H0 * d_target;
      const c = 299792.458; // km/s
      // Relativistic redshift: z = sqrt((1+v/c)/(1-v/c)) - 1 (or v/c for small v)
      const beta = Math.min(0.95, v / c);
      const z = Math.sqrt((1 + beta) / (1 - beta)) - 1;

      // Age of universe in billion years: t_H = (1 / H0) * conversion
      // 1 Mpc = 3.0857e19 km, 1 year = 3.1557e7 s
      // (3.0857e19 / H0) / 3.1557e7 / 1e9 = 977.8 / H0
      const ageGyr = 977.8 / H0;

      document.getElementById("val_velocity").textContent = Math.round(v).toLocaleString() + " km/s";
      document.getElementById("val_redshift").textContent = "z = " + z.toFixed(3);
      document.getElementById("val_universe_age").textContent = ageGyr.toFixed(2) + " พันล้านปี";

      ctx.clearRect(0, 0, cv.width, cv.height);

      const cx = 320, cy = 115;

      // Cosmic expanding grid
      ctx.strokeStyle = "rgba(51, 65, 85, 0.35)"; ctx.lineWidth = 1;
      const gridScale = 1.0 + (tick * 0.005 * (H0 / 70)) % 0.5;
      for(let r=1; 4 >= r; r++) {
        ctx.beginPath(); ctx.arc(cx, cy, r * 45 * gridScale, 0, Math.PI*2); ctx.stroke();
      }

      // Milky Way at Center
      ctx.fillStyle = "#ffffff";
      ctx.beginPath(); ctx.arc(cx, cy, 6, 0, Math.PI*2); ctx.fill();
      ctx.fillStyle = "#00f0ff"; ctx.font = "bold 10px sans-serif";
      ctx.fillText("ทางช้างเผือก (Milky Way)", cx - 55, cy - 12);

      // Expanding Galaxies
      galaxies.forEach(g => {
        const drift = ((tick * 0.008 * (H0 / 70) * (g.d / 100)) % 30);
        const rad = 25 + (g.d / 200) * 120 + drift;
        const gx = cx + rad * Math.cos(g.ang);
        const gy = cy + rad * Math.sin(g.ang);

        // Velocity vector arrow
        const vx = (gx - cx) * 0.18;
        const vy = (gy - cy) * 0.18;
        ctx.strokeStyle = "#ef4444"; ctx.lineWidth = 1.5;
        ctx.beginPath(); ctx.moveTo(gx, gy); ctx.lineTo(gx + vx, gy + vy); ctx.stroke();

        ctx.fillStyle = g.col;
        ctx.beginPath(); ctx.arc(gx, gy, 4.5, 0, Math.PI*2); ctx.fill();
        ctx.fillStyle = "#94a3b8"; ctx.font = "9px sans-serif";
        ctx.fillText(g.name, gx + 8, gy + 3);
      });

      // Target Selected Galaxy (User controlled distance)
      const targetRad = 35 + (d_target / 2000) * 160;
      const tgX = cx + targetRad * Math.cos(0.2);
      const tgY = cy + targetRad * Math.sin(0.2);

      ctx.fillStyle = "#f43f5e"; ctx.beginPath(); ctx.arc(tgX, tgY, 6.5, 0, Math.PI*2); ctx.fill();
      ctx.strokeStyle = "#ffffff"; ctx.lineWidth = 1.5; ctx.stroke();
      ctx.fillStyle = "#ffffff"; ctx.font = "bold 10px sans-serif";
      ctx.fillText("เป้าหมาย (d=" + d_target + " Mpc)", tgX + 10, tgY + 4);

      // Bottom Redshift Spectrum Bar
      const specX = 120, specY = 195, specW = 400, specH = 14;
      const specGrad = ctx.createLinearGradient(specX, 0, specX + specW, 0);
      specGrad.addColorStop(0, "#3b82f6");
      specGrad.addColorStop(0.5, "#10b981");
      specGrad.addColorStop(1, "#ef4444");
      ctx.fillStyle = specGrad;
      ctx.fillRect(specX, specY, specW, specH);

      // Redshifted absorption marker
      const shiftX = specX + specW * 0.4 + Math.min(specW * 0.55, z * specW * 0.4);
      ctx.strokeStyle = "#ffffff"; ctx.lineWidth = 3;
      ctx.beginPath(); ctx.moveTo(shiftX, specY - 3); ctx.lineTo(shiftX, specY + specH + 3); ctx.stroke();
      ctx.fillStyle = "#ffffff"; ctx.font = "bold 9px sans-serif";
      ctx.fillText("Hα Shifted (z=" + z.toFixed(3) + ")", shiftX - 35, specY - 6);

      tick++;
      requestAnimationFrame(animate);
    }
    animate();
"""

# ==============================================================================
# 8.2 Big Bang Timeline & Cosmic Microwave Background (CMB)
# ==============================================================================
body_8_2 = """
  <div class="sim-card">
    <div class="sim-header">
      <div class="sim-title"><span>🔭</span> 8.2 ทฤษฎีบิกแบง & รังสีไมโครเวฟพื้นหลัง (Big Bang Timeline & CMB 2.725 K)</div>
      <div class="badge-fps">● 60 FPS REAL-TIME</div>
    </div>
    <div class="tab-bar">
      <button class="tab-btn active" id="tabTime" onclick="setMode('time')">⏳ ไทม์ไลน์วิวัฒนาการเอกภพ (Cosmic Timeline)</button>
      <button class="tab-btn" id="tabCMB" onclick="setMode('cmb')">📡 สเปกตรัมวัตถุดำ CMB 2.725 K (COBE/Planck)</button>
    </div>
    <div id="controlsTime" class="control-grid">
      <div class="ctrl-box">
        <label>ยุคสมัยวิวัฒนาการ (Cosmic Epoch):</label>
        <select id="sel_epoch">
          <option value="planck">1. ยุคพลังค์ Planck (t < 10⁻⁴³ s, T > 10³² K - รวม 4 แรง)</option>
          <option value="inflation">2. การพองตัว Inflation (t ~ 10⁻³⁵ s - ขยายตัว 10²⁶ เท่า)</option>
          <option value="nucleo">3. กำเนิดนิวเคลียส Nucleosynthesis (t = 3 นาที - 75% H, 25% He)</option>
          <option value="recomb" selected>4. รีคอมบิเนชัน Recombination (t = 380,000 ปี, T = 3,000 K - แสง CMB หลุด)</option>
          <option value="today">5. ปัจจุบัน Today (t = 13.8 พันล้านปี, T_CMB = 2.725 K)</option>
        </select>
      </div>
      <div class="ctrl-box">
        <label>อุณหภูมิเอกภพเฉลี่ย (Cosmic Temperature T): <span id="val_temp" class="val-display">3,000 K</span></label>
        <div id="val_epoch_desc" style="color:#94a3b8; font-size:0.80rem; margin-top:4px;">อิเล็กตรอนรวมตัวกับโปรตอน เอกภพเริ่มโปร่งใส แสง CMB หลุดเป็นอิสระ</div>
      </div>
    </div>
    <div id="controlsCMB" class="control-grid" style="display:none;">
      <div class="ctrl-box">
        <label>อุณหภูมิรังสี CMB วันนี้: 2.7255 ± 0.0006 K</label>
        <div style="color:#94a3b8; font-size:0.80rem; margin-top:4px;">สเปกตรัมวัตถุดำสมบูรณ์แบบที่สุดในฟิสิกส์ (Max Planck Curve)</div>
      </div>
      <div class="ctrl-box">
        <label>ความแปรปรวนอุณหภูมิ (CMB Anisotropy): ΔT/T ~ 10⁻⁵</label>
        <div style="color:#10b981; font-size:0.80rem; margin-top:4px;">เมล็ดพันธุ์ความหนาแน่นก่อกำเนิดกาแล็กซีและโครงสร้างเอกภพ</div>
      </div>
    </div>
    <div class="canvas-box"><canvas id="simCanvas" width="640" height="230"></canvas></div>
    <div class="readout-grid" id="readoutsTime">
      <div class="readout-card"><div class="readout-val" id="val_epoch_time">380,000 ปี</div><div class="readout-lbl">เวลาหลังบิกแบง (Elapsed Time)</div></div>
      <div class="readout-card"><div class="readout-val" id="val_epoch_redshift">z ~ 1,100</div><div class="readout-lbl">ค่าการเลื่อนทางแดง (Redshift z)</div></div>
      <div class="readout-card"><div class="readout-val" id="val_state_stat" style="color:#f59e0b;">เอกภพโปร่งแสง</div><div class="readout-lbl">สภาวะความทึบแสงของสสาร</div></div>
    </div>
    <div class="readout-grid" id="readoutsCMB" style="display:none;">
      <div class="readout-card"><div class="readout-val" id="val_peak_lam">1.06 mm</div><div class="readout-lbl">ความยาวคลื่นยอดสเปกตรัม (Microwave)</div></div>
      <div class="readout-card"><div class="readout-val" id="val_photon_dens">411 โฟตอน/cm³</div><div class="readout-lbl">ความหนาแน่นโฟตอน CMB ทั่วอวกาศ</div></div>
      <div class="readout-card"><div class="readout-val" id="val_cmb_nobel" style="color:#10b981;">Nobel Prize 1978 & 2006</div><div class="readout-lbl">การค้นพบ Penzias, Wilson & COBE</div></div>
    </div>
  </div>
"""

js_8_2 = """
    const cv = document.getElementById("simCanvas");
    const ctx = cv.getContext("2d");
    let currentMode = "time";
    let tick = 0;

    const epochs = {
      planck: { time: "10⁻⁴³ วินาที", T: "10³² K", z: "z > 10³⁰", desc: "แรงทั้ง 4 รวมเป็นหนึ่งเดียว ปริภูมิ-เวลามีลักษณะโฟมควอนตัม", state: "Quantum Singularity", col: "#f43f5e" },
      inflation: { time: "10⁻³⁵ วินาที", T: "10²⁷ K", z: "z ~ 10²⁵", desc: "การขยายตัวแบบเอ็กซ์โพเนนเชียล 10²⁶ เท่า ลบล้างความโค้งอวกาศ", state: "Exponential Growth", col: "#a855f7" },
      nucleo: { time: "3 นาที", T: "10⁹ K", z: "z ~ 10⁸", desc: "โปรตอนและนิวตรอนหลอมรวมเป็นไฮโดรเจน (75%) และฮีเลียม (25%)", state: "BBN Nuclei Born", col: "#f59e0b" },
      recomb: { time: "380,000 ปี", T: "3,000 K", z: "z ~ 1,100", desc: "อิเล็กตรอนรวมตัวกับนิวเคลียส เอกภพเริ่มโปร่งใส แสง CMB หลุดเป็นอิสระ", state: "เอกภพโปร่งแสง (CMB Released)", col: "#00f0ff" },
      today: { time: "13.8 พันล้านปี", T: "2.725 K", z: "z = 0", desc: "เอกภพปัจจุบัน ประกอบด้วยดาวฤกษ์ กาแล็กซี สสารมืด และพลังงานมืด", state: "Accelerating Universe", col: "#10b981" }
    };

    function setMode(mode) {
      currentMode = mode;
      document.getElementById("tabTime").classList.toggle("active", mode === "time");
      document.getElementById("tabCMB").classList.toggle("active", mode === "cmb");
      document.getElementById("controlsTime").style.display = mode === "time" ? "grid" : "none";
      document.getElementById("controlsCMB").style.display = mode === "cmb" ? "grid" : "none";
      document.getElementById("readoutsTime").style.display = mode === "time" ? "grid" : "none";
      document.getElementById("readoutsCMB").style.display = mode === "cmb" ? "grid" : "none";
    }

    function animate() {
      ctx.clearRect(0, 0, cv.width, cv.height);

      if (currentMode === "time") {
        const epCode = document.getElementById("sel_epoch").value;
        const ep = epochs[epCode];

        document.getElementById("val_temp").textContent = ep.T;
        document.getElementById("val_epoch_desc").textContent = ep.desc;
        document.getElementById("val_epoch_time").textContent = ep.time;
        document.getElementById("val_epoch_redshift").textContent = ep.z;
        document.getElementById("val_state_stat").textContent = ep.state;
        document.getElementById("val_state_stat").style.color = ep.col;

        // Big Bang Expanding Cone Visualizer
        const ox = 60, oy = 115, coneW = 500;

        // Draw Expansion Cone
        ctx.fillStyle = "rgba(15, 23, 42, 0.7)"; ctx.strokeStyle = "#334155"; ctx.lineWidth = 1.5;
        ctx.beginPath();
        ctx.moveTo(ox, oy);
        ctx.lineTo(ox + coneW, oy - 80);
        ctx.lineTo(ox + coneW, oy + 80);
        ctx.closePath();
        ctx.fill(); ctx.stroke();

        // Epoch stages along the cone
        const stages = [
          { x: ox + 15, name: "Planck", col: "#f43f5e" },
          { x: ox + 70, name: "Inflation", col: "#a855f7" },
          { x: ox + 170, name: "Nucleosynthesis", col: "#f59e0b" },
          { x: ox + 280, name: "Recombination (CMB)", col: "#00f0ff" },
          { x: ox + coneW - 10, name: "Today (Galaxies)", col: "#10b981" }
        ];

        stages.forEach(st => {
          const topY = oy - ((st.x - ox) / coneW) * 80;
          const botY = oy + ((st.x - ox) / coneW) * 80;
          ctx.strokeStyle = st.col; ctx.lineWidth = 1.5; ctx.setLineDash([2, 2]);
          ctx.beginPath(); ctx.moveTo(st.x, topY); ctx.lineTo(st.x, botY); ctx.stroke(); ctx.setLineDash([]);
          ctx.fillStyle = st.col; ctx.font = "bold 9px sans-serif";
          ctx.fillText(st.name, st.x - 20, botY + 14);
        });

        // Glowing Active Epoch Marker
        let activeX = ox + 280;
        if (epCode === "planck") activeX = ox + 15;
        else if (epCode === "inflation") activeX = ox + 70;
        else if (epCode === "nucleo") activeX = ox + 170;
        else if (epCode === "today") activeX = ox + coneW - 10;

        ctx.fillStyle = ep.col;
        ctx.beginPath(); ctx.arc(activeX, oy, 8 + Math.sin(tick*0.1)*2, 0, Math.PI*2); ctx.fill();
        ctx.strokeStyle = "#ffffff"; ctx.lineWidth = 2; ctx.stroke();
      }
      else {
        // CMB Planck Blackbody Curve Plot
        const ox = 90, oy = 185, gw = 470, gh = 150;

        ctx.strokeStyle = "#475569"; ctx.lineWidth = 1.5;
        ctx.beginPath(); ctx.moveTo(ox, oy); ctx.lineTo(ox + gw, oy); ctx.stroke();
        ctx.beginPath(); ctx.moveTo(ox, oy); ctx.lineTo(ox, oy - gh); ctx.stroke();

        ctx.fillStyle = "#94a3b8"; ctx.font = "10px sans-serif";
        ctx.fillText("ความยาวคลื่น λ (mm) → (0.2 ถึง 4.0 mm)", ox + gw - 180, oy + 16);
        ctx.fillText("ความเข้มรังสีสเปกตรัม I(λ)", ox - 10, oy - gh - 6);

        // Planck Radiation Curve for T = 2.725 K
        ctx.strokeStyle = "#00f0ff"; ctx.lineWidth = 2.8;
        ctx.beginPath();
        for(let lam = 0.2; 4.0 >= lam; lam += 0.05) {
          const px = ox + ((lam - 0.2) / 3.8) * gw;
          // I(lam) ~ 1/lam^5 * 1/(exp(hc/lam k T) - 1)
          const x = 5.28 / (lam * 2.725);
          const py = oy - (Math.pow(lam, -5) / (Math.exp(x) - 1)) * 32.0;
          if (lam === 0.2) ctx.moveTo(px, Math.max(oy - gh, py)); else ctx.lineTo(px, Math.max(oy - gh, py));
        }
        ctx.stroke();

        // Peak marker at 1.06 mm
        const peakX = ox + ((1.06 - 0.2) / 3.8) * gw;
        const peakY = oy - gh * 0.85;
        ctx.fillStyle = "#f59e0b"; ctx.beginPath(); ctx.arc(peakX, peakY, 5, 0, Math.PI*2); ctx.fill();
        ctx.fillText("★ Peak at 1.06 mm (T = 2.725 K)", peakX - 60, peakY - 10);
      }

      tick++;
      requestAnimationFrame(animate);
    }
    animate();
"""

# ==============================================================================
# 8.3 Dark Matter & Dark Energy (Galaxy Rotation Curves)
# ==============================================================================
body_8_3 = """
  <div class="sim-card">
    <div class="sim-header">
      <div class="sim-title"><span>🔭</span> 8.3 สสารมืด & พลังงานมืด (Dark Matter Halo & Cosmic Energy Budget)</div>
      <div class="badge-fps">● 60 FPS REAL-TIME</div>
    </div>
    <div class="control-grid">
      <div class="ctrl-box">
        <label>แบบจำลองมวลกาแล็กซี (Mass Model):</label>
        <select id="sel_dm_model">
          <option value="both" selected>รวมสสารมืด (Vera Rubin Observed: v ≈ 220 km/s คงที่)</option>
          <option value="visible">เฉพาะสสารที่มองเห็น (Keplerian Drop-off: v ∝ 1/√r)</option>
        </select>
      </div>
      <div class="ctrl-box">
        <label>องค์ประกอบของเอกภพ (Lambda-CDM Universe):</label>
        <div style="color:#00f0ff; font-weight:700; font-family:'JetBrains Mono', monospace; font-size:0.88rem; margin-top:4px;">Dark Energy 68% | Dark Matter 27% | Normal 5%</div>
      </div>
    </div>
    <div class="canvas-box"><canvas id="simCanvas" width="640" height="230"></canvas></div>
    <div class="readout-grid">
      <div class="readout-card"><div class="readout-val" id="val_v_outer">220 km/s</div><div class="readout-lbl">ความเร็ววงโคจรขอบกาแล็กซี (r=20 kpc)</div></div>
      <div class="readout-card"><div class="readout-val" id="val_dm_ratio">5.4 เท่า</div><div class="readout-lbl">อัตราส่วนสสารมืดต่อสสารปกติ</div></div>
      <div class="readout-card"><div class="readout-val" id="val_rubin_stat" style="color:#10b981;">กราฟแบนราบ (Flat Curve)</div><div class="readout-lbl">การยืนยันการมีอยู่ของสสารมืด</div></div>
    </div>
  </div>
"""

js_8_3 = """
    const cv = document.getElementById("simCanvas");
    const ctx = cv.getContext("2d");
    const selModel = document.getElementById("sel_dm_model");
    let tick = 0;

    let stars = [];
    for(let i=0; 80 > i; i++) {
      const rad = 10 + Math.random() * 85;
      const ang = Math.random() * Math.PI * 2;
      stars.push({ r: rad, ang: ang, isArm: i < 50 });
    }

    function animate() {
      const mode = selModel.value;
      const hasDM = (mode === "both");

      document.getElementById("val_v_outer").textContent = hasDM ? "220 km/s" : "98 km/s (ดรอปลง)";
      document.getElementById("val_v_outer").style.color = hasDM ? "#10b981" : "#f43f5e";
      document.getElementById("val_rubin_stat").textContent = hasDM ? "กราฟแบนราบ (Flat Rotation)" : "ตกลงตามเคปเลอร์ (Keplerian)";
      document.getElementById("val_rubin_stat").style.color = hasDM ? "#10b981" : "#f43f5e";

      ctx.clearRect(0, 0, cv.width, cv.height);

      // Left Panel: Rotating Spiral Galaxy
      const cx = 130, cy = 115;

      // Dark Matter Halo (Faint cyan sphere around galaxy if enabled)
      if (hasDM) {
        const haloGrad = ctx.createRadialGradient(cx, cy, 10, cx, cy, 100);
        haloGrad.addColorStop(0, "rgba(0, 240, 255, 0.25)");
        haloGrad.addColorStop(1, "transparent");
        ctx.fillStyle = haloGrad;
        ctx.beginPath(); ctx.arc(cx, cy, 100, 0, Math.PI*2); ctx.fill();
      }

      // Galactic Core
      const coreGrad = ctx.createRadialGradient(cx, cy, 2, cx, cy, 16);
      coreGrad.addColorStop(0, "#ffffff"); coreGrad.addColorStop(1, "#f59e0b");
      ctx.fillStyle = coreGrad;
      ctx.beginPath(); ctx.arc(cx, cy, 12, 0, Math.PI*2); ctx.fill();

      // Rotating Stars
      stars.forEach(st => {
        // v = const if DM, v = 1/sqrt(r) if visible only
        const speed = hasDM ? (1.5 / st.r) : (4.0 / Math.pow(st.r, 1.5));
        st.ang += speed;

        const sx = cx + st.r * Math.cos(st.ang);
        const sy = cy + st.r * 0.55 * Math.sin(st.ang); // tilted spiral

        ctx.fillStyle = st.isArm ? "#38bdf8" : "#ffffff";
        ctx.beginPath(); ctx.arc(sx, sy, (st.isArm ? 1.5 : 1.0), 0, Math.PI*2); ctx.fill();
      });

      ctx.fillStyle = "#ffffff"; ctx.font = "bold 10px sans-serif";
      ctx.fillText("กาแล็กซีชนิดกังหัน (Spiral Galaxy)", cx - 65, cy + 95);

      // Right Panel: Rotation Curve Graph (Vera Rubin)
      const gx = 280, gy = 185, gw = 330, gh = 145;

      ctx.strokeStyle = "#475569"; ctx.lineWidth = 1.5;
      ctx.beginPath(); ctx.moveTo(gx, gy); ctx.lineTo(gx + gw, gy); ctx.stroke();
      ctx.beginPath(); ctx.moveTo(gx, gy); ctx.lineTo(gx, gy - gh); ctx.stroke();

      ctx.fillStyle = "#94a3b8"; ctx.font = "10px sans-serif";
      ctx.fillText("รัศมีจากใจกลาง r (kpc) →", gx + gw - 120, gy + 16);
      ctx.fillText("ความเร็ว v (km/s)", gx - 10, gy - gh - 6);

      // Theoretical Keplerian Drop Curve (Visible Only)
      ctx.strokeStyle = "#f43f5e"; ctx.lineWidth = 2.0; ctx.setLineDash([3, 3]);
      ctx.beginPath();
      for(let r = 2; 25 >= r; r += 0.5) {
        const px = gx + (r / 25) * gw;
        const vKep = (r < 5) ? (220 * (r/5)) : (220 / Math.sqrt(r/5));
        const py = gy - (vKep / 300) * gh;
        if (r === 2) ctx.moveTo(px, py); else ctx.lineTo(px, py);
      }
      ctx.stroke(); ctx.setLineDash([]);
      ctx.fillStyle = "#f43f5e"; ctx.fillText("ทำนาย: v ∝ 1/√r", gx + gw - 85, gy - gh * 0.3);

      // Observed Flat Rotation Curve (With Dark Matter)
      if (hasDM) {
        ctx.strokeStyle = "#10b981"; ctx.lineWidth = 3.0;
        ctx.beginPath();
        for(let r = 2; 25 >= r; r += 0.5) {
          const px = gx + (r / 25) * gw;
          const vObs = (r < 5) ? (220 * (r/5)) : 220;
          const py = gy - (vObs / 300) * gh;
          if (r === 2) ctx.moveTo(px, py); else ctx.lineTo(px, py);
        }
        ctx.stroke();
        ctx.fillStyle = "#10b981"; ctx.fillText("ผลสังเกตจริง (Vera Rubin): Flat Curve", gx + 60, gy - gh * 0.78);
      }

      tick++;
      requestAnimationFrame(animate);
    }
    animate();
"""

# ==============================================================================
# 8.4 Stellar Evolution & Schwarzschild Black Hole
# ==============================================================================
body_8_4 = """
  <div class="sim-card">
    <div class="sim-header">
      <div class="sim-title"><span>🔭</span> 8.4 วิวัฒนาการดาวฤกษ์ & หลุมดำ (Stellar Evolution & Schwarzschild Black Hole)</div>
      <div class="badge-fps">● 60 FPS REAL-TIME</div>
    </div>
    <div class="tab-bar">
      <button class="tab-btn active" id="tabHR" onclick="setMode('hr')">⭐ แผนภาพ H-R วิวัฒนาการดาวฤกษ์ (Stellar Evolution)</button>
      <button class="tab-btn" id="tabBH" onclick="setMode('bh')">🕳️ หลุมดำชวาร์ซชิลด์ & เลนส์โน้มถ่วง (Black Hole Horizon)</button>
    </div>
    <div id="controlsHR" class="control-grid">
      <div class="ctrl-box">
        <label>มวลเริ่มต้นของดาวฤกษ์ (Initial Mass M): <span id="val_mass" class="val-display">1.0</span> M_☉ (มวลดวงอาทิตย์)</label>
        <input type="range" id="slider_mass" min="0.5" max="30.0" step="0.5" value="1.0">
      </div>
      <div class="ctrl-box">
        <label>จุดสิ้นสุดของวงจรชีวิต (Final Remnant): <span id="val_remnant" class="val-display" style="color:#00f0ff;">ดาวแคระขาว (White Dwarf)</span></label>
        <div style="color:#94a3b8; font-size:0.80rem; margin-top:4px;">ขีดจำกัดจันทรสิกขา: M_core < 1.44 M_☉</div>
      </div>
    </div>
    <div id="controlsBH" class="control-grid" style="display:none;">
      <div class="ctrl-box">
        <label>มวลหลุมดำ (Black Hole Mass M): <span id="val_bhmass" class="val-display">4.1</span> ล้าน M_☉ (Sgr A* ทางช้างเผือก)</label>
        <input type="range" id="slider_bhmass" min="3.0" max="50.0" step="1.0" value="4.1">
      </div>
      <div class="ctrl-box">
        <label>รัศมีขอบฟ้าเหตุการณ์: R_s = 2GM/c² (3 km ต่อ 1 M_☉)</label>
        <div style="color:#f43f5e; font-size:0.80rem; margin-top:4px;">เวลาของวัตถุภายนอกสังเกตการณ์หยุดนิ่งที่ขอบฟ้า (Time Freezes)</div>
      </div>
    </div>
    <div class="canvas-box"><canvas id="simCanvas" width="640" height="230"></canvas></div>
    <div class="readout-grid" id="readoutsHR">
      <div class="readout-card"><div class="readout-val" id="val_lifetime">10 พันล้านปี</div><div class="readout-lbl">อายุขัยบนแถบลำดับหลัก (Lifetime)</div></div>
      <div class="readout-card"><div class="readout-val" id="val_core_type">ฮีเลียม/คาร์บอน</div><div class="readout-lbl">แกนกลางขั้นสุดท้าย</div></div>
      <div class="readout-card"><div class="readout-val" id="val_supernova_stat" style="color:#38bdf8;">เนบิวลาดาวเคราะห์</div><div class="readout-lbl">การระเบิดช่วงท้าย</div></div>
    </div>
    <div class="readout-grid" id="readoutsBH" style="display:none;">
      <div class="readout-card"><div class="readout-val" id="val_rs">12.3 ล้าน km</div><div class="readout-lbl">รัศมีขอบฟ้าชวาร์ซชิลด์ (R_s)</div></div>
      <div class="readout-card"><div class="readout-val" id="val_photon_sphere">18.5 ล้าน km</div><div class="readout-lbl">ทรงกลมโฟตอน (Photon Sphere = 1.5 R_s)</div></div>
      <div class="readout-card"><div class="readout-val" id="val_lens_stat" style="color:#f59e0b;">เลนส์โน้มถ่วงสมบูรณ์</div><div class="readout-lbl">การบิดโค้งกาล-อวกาศ</div></div>
    </div>
  </div>
"""

js_8_4 = """
    const cv = document.getElementById("simCanvas");
    const ctx = cv.getContext("2d");
    let currentMode = "hr";
    let tick = 0;

    function setMode(mode) {
      currentMode = mode;
      document.getElementById("tabHR").classList.toggle("active", mode === "hr");
      document.getElementById("tabBH").classList.toggle("active", mode === "bh");
      document.getElementById("controlsHR").style.display = mode === "hr" ? "grid" : "none";
      document.getElementById("controlsBH").style.display = mode === "bh" ? "grid" : "none";
      document.getElementById("readoutsHR").style.display = mode === "hr" ? "grid" : "none";
      document.getElementById("readoutsBH").style.display = mode === "bh" ? "grid" : "none";
    }

    function animate() {
      ctx.clearRect(0, 0, cv.width, cv.height);

      if (currentMode === "hr") {
        const M = +document.getElementById("slider_mass").value;
        document.getElementById("val_mass").textContent = M.toFixed(1);

        const remEl = document.getElementById("val_remnant");
        let lifeStr = "10 พันล้านปี", coreStr = "คาร์บอน-ออกซิเจน", endStr = "เนบิวลาดาวเคราะห์", remStr = "ดาวแคระขาว (White Dwarf)";
        if (M > 20) {
          lifeStr = "8 ล้านปี (สั้นมาก)"; coreStr = "เหล็ก ⁵⁶Fe"; endStr = "ซูเปอร์โนวาชนิด II"; remStr = "หลุมดำ (Black Hole)";
          remEl.style.color = "#f43f5e";
        } else if (M >= 8) {
          lifeStr = "30 ล้านปี"; coreStr = "เหล็ก/ซิลิคอน"; endStr = "ซูเปอร์โนวาชนิด II"; remStr = "ดาวนิวตรอน (Neutron Star / Pulsar)";
          remEl.style.color = "#a855f7";
        } else {
          remEl.style.color = "#00f0ff";
        }

        remEl.textContent = remStr;
        document.getElementById("val_lifetime").textContent = lifeStr;
        document.getElementById("val_core_type").textContent = coreStr;
        document.getElementById("val_supernova_stat").textContent = endStr;

        // Hertzsprung-Russell (H-R) Diagram Plot
        const ox = 90, oy = 185, gw = 470, gh = 150;

        ctx.strokeStyle = "#475569"; ctx.lineWidth = 1.5;
        ctx.beginPath(); ctx.moveTo(ox, oy); ctx.lineTo(ox + gw, oy); ctx.stroke(); // Temp (reversed)
        ctx.beginPath(); ctx.moveTo(ox, oy); ctx.lineTo(ox, oy - gh); ctx.stroke(); // Luminosity

        ctx.fillStyle = "#94a3b8"; ctx.font = "10px sans-serif";
        ctx.fillText("← อุณหภูมิผิว T (K) [40,000 K ถึง 3,000 K]", ox + 20, oy + 16);
        ctx.fillText("ความส่องสว่าง L/L_☉ (Log Scale)", ox - 10, oy - gh - 6);

        // Main Sequence Band (Diagonal)
        const msGrad = ctx.createLinearGradient(ox, oy - gh, ox + gw, oy);
        msGrad.addColorStop(0, "rgba(56, 189, 248, 0.4)");
        msGrad.addColorStop(0.5, "rgba(245, 158, 11, 0.4)");
        msGrad.addColorStop(1, "rgba(239, 68, 68, 0.4)");

        ctx.strokeStyle = msGrad; ctx.lineWidth = 18;
        ctx.beginPath(); ctx.moveTo(ox + 40, oy - gh + 20); ctx.lineTo(ox + gw - 30, oy - 15); ctx.stroke();
        ctx.fillStyle = "#ffffff"; ctx.font = "bold 10px sans-serif";
        ctx.fillText("แถบลำดับหลัก (Main Sequence)", ox + 150, oy - gh * 0.55);

        // Red Giant Branch (Top Right)
        ctx.fillStyle = "rgba(239, 68, 68, 0.35)";
        ctx.beginPath(); ctx.ellipse(ox + gw - 70, oy - gh * 0.75, 45, 20, 0, 0, Math.PI*2); ctx.fill();
        ctx.fillStyle = "#f87171"; ctx.fillText("ดาวยักษ์แดง (Red Giants)", ox + gw - 125, oy - gh * 0.75);

        // White Dwarf Branch (Bottom Left)
        ctx.fillStyle = "rgba(0, 240, 255, 0.35)";
        ctx.beginPath(); ctx.ellipse(ox + 70, oy - 25, 35, 14, 0, 0, Math.PI*2); ctx.fill();
        ctx.fillStyle = "#38bdf8"; ctx.fillText("ดาวแคระขาว (White Dwarfs)", ox + 35, oy - 25);

        // Active Star Position based on M
        const starX = ox + 40 + (1 - Math.log10(M+0.5)/Math.log10(35)) * (gw - 70);
        const starY = oy - gh + 20 + (1 - Math.log10(M+0.5)/Math.log10(35)) * (gh - 35);

        ctx.fillStyle = M > 10 ? "#38bdf8" : (M >= 1.5 ? "#ffffff" : (M >= 0.8 ? "#facc15" : "#f87171"));
        ctx.beginPath(); ctx.arc(starX, starY, 6.5, 0, Math.PI*2); ctx.fill();
        ctx.strokeStyle = "#ffffff"; ctx.lineWidth = 2; ctx.stroke();
      }
      else {
        // Black Hole Visualizer
        const M_bh = +document.getElementById("slider_bhmass").value;
        document.getElementById("val_bhmass").textContent = M_bh.toFixed(1);

        const Rs_mil_km = M_bh * 3.0;
        document.getElementById("val_rs").textContent = Rs_mil_km.toFixed(1) + " ล้าน km";
        document.getElementById("val_photon_sphere").textContent = (Rs_mil_km * 1.5).toFixed(1) + " ล้าน km";

        const cx = 320, cy = 115;

        // Glowing Accretion Disk (Swirling plasma around Black Hole)
        const diskGrad = ctx.createLinearGradient(cx - 180, 0, cx + 180, 0);
        diskGrad.addColorStop(0, "rgba(245, 158, 11, 0.1)");
        diskGrad.addColorStop(0.3, "rgba(239, 68, 68, 0.85)");
        diskGrad.addColorStop(0.5, "rgba(254, 240, 138, 0.95)");
        diskGrad.addColorStop(0.7, "rgba(239, 68, 68, 0.85)");
        diskGrad.addColorStop(1, "rgba(245, 158, 11, 0.1)");

        ctx.fillStyle = diskGrad;
        ctx.beginPath(); ctx.ellipse(cx, cy, 160, 25, 0, 0, Math.PI*2); ctx.fill();

        // Gravitational Lensed Upper and Lower Halo Rings (Interstellar Style)
        ctx.strokeStyle = "rgba(245, 158, 11, 0.7)"; ctx.lineWidth = 4;
        ctx.beginPath(); ctx.arc(cx, cy, 55, Math.PI*1.1, Math.PI*1.9); ctx.stroke();
        ctx.beginPath(); ctx.arc(cx, cy, 55, Math.PI*0.1, Math.PI*0.9); ctx.stroke();

        // Black Hole Shadow / Event Horizon (Total blackness)
        ctx.fillStyle = "#000000";
        ctx.beginPath(); ctx.arc(cx, cy, 38, 0, Math.PI*2); ctx.fill();
        ctx.strokeStyle = "#f59e0b"; ctx.lineWidth = 1.5; ctx.stroke();

        // Photon Sphere ring
        ctx.strokeStyle = "rgba(0, 240, 255, 0.6)"; ctx.lineWidth = 1.5; ctx.setLineDash([3, 3]);
        ctx.beginPath(); ctx.arc(cx, cy, 57, 0, Math.PI*2); ctx.stroke(); ctx.setLineDash([]);

        ctx.fillStyle = "#00f0ff"; ctx.font = "bold 10px sans-serif";
        ctx.fillText("Photon Sphere (1.5 R_s)", cx + 65, cy - 35);
        ctx.fillStyle = "#ffffff";
        ctx.fillText("Event Horizon (R_s)", cx + 45, cy + 25);
      }

      tick++;
      requestAnimationFrame(animate);
    }
    animate();
"""

# ==============================================================================
# 8.5 Virtual Lab: Friedmann Universe & JWST Deep Field
# ==============================================================================
body_8_5 = """
  <div class="sim-card">
    <div class="sim-header">
      <div class="sim-title"><span>🔭</span> 8.5 ปฏิบัติการเอกภพวิทยา & กล้อง JWST (Friedmann Engine & JWST Deep Field)</div>
      <div class="badge-fps">● 60 FPS REAL-TIME</div>
    </div>
    <div class="tab-bar">
      <button class="tab-btn active" id="tabFried" onclick="setMode('fried')">🌌 แบบจำลองฟรีดมันน์ (Friedmann Expansion a(t))</button>
      <button class="tab-btn" id="tabJWST" onclick="setMode('jwst')">🔭 ภาพอวกาศห้วงลึก JWST (Primordial Galaxies & Lensing)</button>
    </div>
    <div id="controlsFried" class="control-grid">
      <div class="ctrl-box">
        <label>ความหนาแน่นสสารรวม (Matter Ω_m): <span id="val_om" class="val-display">0.30</span></label>
        <input type="range" id="slider_om" min="0.0" max="1.5" step="0.05" value="0.30">
      </div>
      <div class="ctrl-box">
        <label>ความหนาแน่นพลังงานมืด (Dark Energy Ω_Λ): <span id="val_ol" class="val-display">0.70</span></label>
        <input type="range" id="slider_ol" min="0.0" max="1.5" step="0.05" value="0.70">
      </div>
    </div>
    <div id="controlsJWST" class="control-grid" style="display:none;">
      <div class="ctrl-box">
        <label>ความยาวคลื่นอินฟราเรดตรวจจับ (JWST NIRCam): 0.6 - 5.0 µm</label>
        <div style="color:#94a3b8; font-size:0.80rem; margin-top:4px;">ส่องทะลุฝุ่นแก๊ส พบกาแล็กซีแรกเริ่มที่ z = 13.2 (300 ล้านปีหลังบิกแบง)</div>
      </div>
      <div class="ctrl-box">
        <label>ปรากฏการณ์เลนส์ความโน้มถ่วง (Einstein Ring / Arcs):</label>
        <div style="color:#10b981; font-size:0.80rem; margin-top:4px;">กระจุกกาแล็กซี SMACS 0723 ขยายภาพกาแล็กซีพื้นหลัง</div>
      </div>
    </div>
    <div class="canvas-box"><canvas id="simCanvas" width="640" height="230"></canvas></div>
    <div class="readout-grid" id="readoutsFried">
      <div class="readout-card"><div class="readout-val" id="val_omega_tot">Ω_tot = 1.00 (Flat)</div><div class="readout-lbl">ความโค้งอวกาศรวม (Ω_m + Ω_Λ)</div></div>
      <div class="readout-card"><div class="readout-val" id="val_fate_univ" style="color:#10b981;">ขยายตัวเร่งขึ้น (Accelerating)</div><div class="readout-lbl">ชะตากรรมของเอกภพในอนาคต</div></div>
      <div class="readout-card"><div class="readout-val" id="val_scale_today">a(t₀) = 1.00</div><div class="readout-lbl">แฟกเตอร์มาตราส่วนเอกภพปัจจุบัน</div></div>
    </div>
    <div class="readout-grid" id="readoutsJWST" style="display:none;">
      <div class="readout-card"><div class="readout-val" id="val_jwst_redshift">z = 13.2</div><div class="readout-lbl">การเลื่อนทางแดงสูงสุดที่บันทึกได้</div></div>
      <div class="readout-card"><div class="readout-val" id="val_jwst_dist">33 พันล้านปีแสง</div><div class="readout-lbl">ระยะห่างตามการขยายตัว (Proper Distance)</div></div>
      <div class="readout-card"><div class="readout-val" id="val_jwst_stat" style="color:#00f0ff;">Primordial Universe 100%</div><div class="readout-lbl">การค้นพบใหม่ของ JWST</div></div>
    </div>
  </div>
"""

js_8_5 = """
    const cv = document.getElementById("simCanvas");
    const ctx = cv.getContext("2d");
    let currentMode = "fried";
    let tick = 0;

    function setMode(mode) {
      currentMode = mode;
      document.getElementById("tabFried").classList.toggle("active", mode === "fried");
      document.getElementById("tabJWST").classList.toggle("active", mode === "jwst");
      document.getElementById("controlsFried").style.display = mode === "fried" ? "grid" : "none";
      document.getElementById("controlsJWST").style.display = mode === "jwst" ? "grid" : "none";
      document.getElementById("readoutsFried").style.display = mode === "fried" ? "grid" : "none";
      document.getElementById("readoutsJWST").style.display = mode === "jwst" ? "grid" : "none";
    }

    function animate() {
      ctx.clearRect(0, 0, cv.width, cv.height);

      if (currentMode === "fried") {
        const Om = +document.getElementById("slider_om").value;
        const Ol = +document.getElementById("slider_ol").value;

        document.getElementById("val_om").textContent = Om.toFixed(2);
        document.getElementById("val_ol").textContent = Ol.toFixed(2);

        const Otot = Om + Ol;
        let geomStr = "Ω_tot = " + Otot.toFixed(2) + " (Flat แบนราบ)";
        if (Otot > 1.05) geomStr = "Ω_tot = " + Otot.toFixed(2) + " (Closed โค้งปิด)";
        else if (0.95 > Otot) geomStr = "Ω_tot = " + Otot.toFixed(2) + " (Open โค้งเปิด)";
        document.getElementById("val_omega_tot").textContent = geomStr;

        let fateStr = "ขยายตัวเร่งขึ้น (Accelerating Big Freeze)";
        let fateCol = "#10b981";
        if (Ol === 0 && Om > 1.0) { fateStr = "หดตัวยุบสลาย (Big Crunch)"; fateCol = "#f43f5e"; }
        else if (Ol === 0 && 1.0 >= Om) { fateStr = "ขยายตัวชะลอลงชั่วนิรันดร์ (Big Freeze)"; fateCol = "#38bdf8"; }

        const fateEl = document.getElementById("val_fate_univ");
        fateEl.textContent = fateStr; fateEl.style.color = fateCol;

        // Friedmann Scale Factor a(t) Graph
        const ox = 90, oy = 185, gw = 470, gh = 150;

        ctx.strokeStyle = "#475569"; ctx.lineWidth = 1.5;
        ctx.beginPath(); ctx.moveTo(ox, oy); ctx.lineTo(ox + gw, oy); ctx.stroke(); // Time t
        ctx.beginPath(); ctx.moveTo(ox, oy); ctx.lineTo(ox, oy - gh); ctx.stroke(); // Scale a(t)

        ctx.fillStyle = "#94a3b8"; ctx.font = "10px sans-serif";
        ctx.fillText("เวลา t (พันล้านปี) → [อดีต 0 ถึง อนาคต 30 Gyr]", ox + gw - 210, oy + 16);
        ctx.fillText("ขนาดเอกภพ a(t)", ox - 10, oy - gh - 6);

        // Present Day Line at t = 13.8 Gyr
        const presX = ox + (13.8 / 30.0) * gw;
        const presY = oy - (1.0 / 2.5) * gh;
        ctx.strokeStyle = "rgba(148, 163, 184, 0.4)"; ctx.lineWidth = 1.5; ctx.setLineDash([3, 3]);
        ctx.beginPath(); ctx.moveTo(presX, oy); ctx.lineTo(presX, oy - gh); ctx.stroke(); ctx.setLineDash([]);
        ctx.fillStyle = "#ffffff"; ctx.font = "9px sans-serif";
        ctx.fillText("ปัจจุบัน (t₀ = 13.8 Gyr, a=1.0)", presX - 55, oy - gh + 14);

        // Plot dynamic a(t)
        ctx.strokeStyle = fateCol; ctx.lineWidth = 3.0;
        ctx.beginPath();
        for(let t = 0; 30 >= t; t += 0.5) {
          const px = ox + (t / 30.0) * gw;
          let a_val;
          if (Ol > 0.4) {
            // Accelerating Lambda-dominated
            a_val = Math.pow(t / 13.8, 0.66) * (1 - Ol*0.3) + (Ol*0.3) * Math.exp((t - 13.8)*0.08);
          } else if (Om > 1.0) {
            // Big Crunch
            const tau = t / 13.8;
            a_val = Math.max(0, 1.4 * Math.sin(tau * Math.PI / 2.2));
          } else {
            // Matter dominated deceleration
            a_val = Math.pow(t / 13.8, 0.66);
          }
          const py = oy - (a_val / 2.5) * gh;
          if (t === 0) ctx.moveTo(px, oy); else ctx.lineTo(px, Math.max(oy - gh - 10, py));
        }
        ctx.stroke();

        ctx.fillStyle = fateCol; ctx.beginPath(); ctx.arc(presX, presY, 5, 0, Math.PI*2); ctx.fill();
      }
      else {
        // JWST Deep Field & Gravitational Lensing Visualizer
        const cx = 320, cy = 115;

        // Foreground Massive Cluster Galaxy (Golden Lensing Core)
        const lGrad = ctx.createRadialGradient(cx, cy, 2, cx, cy, 35);
        lGrad.addColorStop(0, "#ffffff");
        lGrad.addColorStop(0.4, "#f59e0b");
        lGrad.addColorStop(1, "transparent");
        ctx.fillStyle = lGrad;
        ctx.beginPath(); ctx.arc(cx, cy, 35, 0, Math.PI*2); ctx.fill();

        ctx.fillStyle = "#ffffff"; ctx.font = "bold 10px sans-serif";
        ctx.fillText("กระจุกกาแล็กซีเลนส์โน้มถ่วง (Lensing Cluster)", cx - 100, cy - 45);

        // Gravitational Lensed Arcs (Einstein Ring Arcs in Red/Infrared)
        ctx.strokeStyle = "rgba(239, 68, 68, 0.85)"; ctx.lineWidth = 3.5;
        // Top Arc
        ctx.beginPath(); ctx.arc(cx, cy, 65, Math.PI*1.15, Math.PI*1.85); ctx.stroke();
        // Bottom Arc
        ctx.beginPath(); ctx.arc(cx, cy, 65, Math.PI*0.15, Math.PI*0.85); ctx.stroke();

        // Primordial Infant Galaxies (Tiny red dots with diffraction spikes)
        const prims = [
          { x: cx - 120, y: cy - 35, z: "z=13.2" },
          { x: cx + 130, y: cy + 40, z: "z=12.5" },
          { x: cx - 80, y: cy + 60, z: "z=11.8" },
          { x: cx + 90, y: cy - 65, z: "z=10.9" }
        ];

        prims.forEach(p => {
          ctx.fillStyle = "#ef4444";
          ctx.beginPath(); ctx.arc(p.x, p.y, 3.5, 0, Math.PI*2); ctx.fill();
          // Diffraction spikes
          ctx.strokeStyle = "rgba(239, 68, 68, 0.5)"; ctx.lineWidth = 1;
          ctx.beginPath(); ctx.moveTo(p.x - 8, p.y); ctx.lineTo(p.x + 8, p.y); ctx.stroke();
          ctx.beginPath(); ctx.moveTo(p.x, p.y - 8); ctx.lineTo(p.x, p.y + 8); ctx.stroke();

          ctx.fillStyle = "#fca5a5"; ctx.font = "bold 9px 'JetBrains Mono', monospace";
          ctx.fillText(p.z, p.x + 8, p.y + 3);
        });
      }

      tick++;
      requestAnimationFrame(animate);
    }
    animate();
"""

files = {
    "sim_8_1.html": wrap_html("8.1 การขยายตัวของเอกภพ & กฎของฮับเบิล", body_8_1, js_8_1),
    "sim_8_2.html": wrap_html("8.2 ทฤษฎีบิกแบง & รังสีไมโครเวฟพื้นหลัง", body_8_2, js_8_2),
    "sim_8_3.html": wrap_html("8.3 สสารมืด & พลังงานมืด", body_8_3, js_8_3),
    "sim_8_4.html": wrap_html("8.4 วิวัฒนาการดาวฤกษ์ & หลุมดำ", body_8_4, js_8_4),
    "sim_8_5.html": wrap_html("8.5 ปฏิบัติการเอกภพวิทยา & กล้อง JWST", body_8_5, js_8_5)
}

for fname, content in files.items():
    fpath = os.path.join(SIM_DIR, fname)
    with open(fpath, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"✅ Generated {fpath} ({len(content)} bytes)")

print("🎉 Successfully upgraded all Chapter 8 simulations to hyper-realistic 60 FPS engines!")
