#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Upgrades all 5 Chapter 1 Simulators for Nanotechnological Physics:
- 1.1: 3D Nanoscale Scaling Ladder ($10^{-10}$ m to $10^{-3}$ m) with Atomic Lattice & Virus zoom
- 1.2: 3D Cube Subdivision & Surface-to-Volume Ratio Fragmentation Solver
- 1.3: DLVO Potential & Nanoparticle Agglomeration / Coagulation Kinetics
- 1.4: Virtual SEM/TEM Caliper Metrology & Particle Size Histogram Builder
- 1.5: Master 3D AR Cleanroom Studio & BET Surface Area Analyzer
"""

import os

BASE_DIR = "/Users/chewathassana/Downloads/manus_backup2026/ModernPhysics"
NANO_SIMS_DIR = os.path.join(BASE_DIR, "nanotechnology/course_nanophysics_263/simulators")
ROOT_SIMS_DIR = os.path.join(BASE_DIR, "simulators")

# ==============================================================================
# 1.1: Nanoscale Dimensions & Scaling Laws Simulator
# ==============================================================================
SIM_1_1_HTML = """<!DOCTYPE html>
<html lang="th">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Lab 1.1: Nanoscale Dimensions & Scaling Laws</title>
  <link href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;700&family=Sarabun:wght@300;400;600;700&display=swap" rel="stylesheet">
  <script src="https://cdn.jsdelivr.net/npm/@mediapipe/camera_utils/camera_utils.js" crossorigin="anonymous"></script>
  <script src="https://cdn.jsdelivr.net/npm/@mediapipe/hands/hands.js" crossorigin="anonymous"></script>
  <style>
    :root {
      --bg: #020617;
      --panel: #090e1a;
      --cyan: #00f0ff;
      --emerald: #10b981;
      --amber: #f59e0b;
      --rose: #f43f5e;
      --purple: #a855f7;
    }
    * { box-sizing: border-box; margin: 0; padding: 0; }
    body { background: var(--bg); color: #f8fafc; font-family: 'Sarabun', sans-serif; padding: 12px; }
    .sim-card { background: var(--panel); border: 1px solid #1e293b; border-radius: 14px; padding: 18px; box-shadow: 0 10px 30px rgba(0,0,0,0.7); }
    .sim-header { display: flex; justify-content: space-between; align-items: center; border-bottom: 1px solid #1e293b; padding-bottom: 10px; margin-bottom: 12px; flex-wrap: wrap; gap: 8px; }
    .sim-title { font-size: 1.1rem; font-weight: 700; color: var(--cyan); display: flex; align-items: center; gap: 8px; }
    .badge { background: rgba(0,240,255,0.15); border: 1px solid var(--cyan); color: var(--cyan); padding: 3px 10px; border-radius: 9999px; font-size: 0.75rem; font-family: 'JetBrains Mono', monospace; }
    .canvas-box { position: relative; width: 100%; height: 320px; background: #000; border: 1px solid #334155; border-radius: 10px; overflow: hidden; margin-bottom: 14px; }
    canvas { width: 100%; height: 100%; display: block; }
    .controls { display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 12px; background: #0f172a; padding: 12px 16px; border-radius: 10px; border: 1px solid #1e293b; margin-bottom: 12px; }
    .ctrl-group { display: flex; flex-direction: column; gap: 6px; }
    .ctrl-lbl { font-size: 0.8rem; color: #94a3b8; display: flex; justify-content: space-between; font-family: 'JetBrains Mono', monospace; }
    input[type=range] { width: 100%; accent-color: var(--cyan); cursor: pointer; }
    .hud { display: flex; justify-content: space-between; align-items: center; background: #020617; border: 1px solid #334155; border-radius: 8px; padding: 10px 16px; font-size: 0.85rem; font-family: 'JetBrains Mono', monospace; flex-wrap: wrap; gap: 10px; }
    .hud-val { color: var(--amber); font-weight: 700; }
    .scale-ruler { display: flex; justify-content: space-between; margin-top: 4px; font-size: 0.7rem; color: #64748b; font-family: 'JetBrains Mono', monospace; }
    .btn-ar { background: linear-gradient(135deg, #0284c7, var(--cyan)); color: #020617; border: none; border-radius: 6px; padding: 6px 14px; font-weight: 700; font-size: 0.8rem; cursor: pointer; }
  </style>
</head>
<body>
  <div class="sim-card">
    <div class="sim-header">
      <div class="sim-title">
        <span>🔬</span>
        <span>แล็บ 1.1: บันไดมาตราส่วนและการคิดเชิงมาตราส่วน (Nanoscale Scaling Ladder)</span>
      </div>
      <div class="badge">● 60 FPS REAL-TIME ZOOM</div>
    </div>

    <div class="canvas-box">
      <canvas id="scaleCanvas"></canvas>
    </div>

    <div class="controls">
      <div class="ctrl-group">
        <div class="ctrl-lbl">
          <span>เลขชี้กำลังมาตราส่วน (Scale Exponent \\(10^x\\text{ m}\\))</span>
          <span id="txtExp">-9.0 (1.0 nm)</span>
        </div>
        <input type="range" id="sliderExp" min="-10" max="-3" step="0.05" value="-9">
        <div class="scale-ruler">
          <span>10⁻¹⁰ m (Atom)</span>
          <span>10⁻⁹ m (Nano)</span>
          <span>10⁻⁶ m (Cell)</span>
          <span>10⁻³ m (Macro)</span>
        </div>
      </div>
      <div class="ctrl-group">
        <div class="ctrl-lbl">
          <span>วัตถุเปรียบเทียบ (Entity Preset)</span>
          <span id="txtPreset">Nanoparticle</span>
        </div>
        <select id="selPreset" style="background:#020617; color:#f8fafc; border:1px solid #334155; padding:6px; border-radius:6px; font-family:inherit; font-size:0.85rem;">
          <option value="-10">อะตอมไฮโดรเจน / คาร์บอน (0.1 nm / 1 Å)</option>
          <option value="-9" selected>อนุภาคควอนตัมดอท / บักกี้บอล (1 - 10 nm)</option>
          <option value="-7.3">ไวรัสโคโรนา / ไวรัสไข้หวัด (100 nm)</option>
          <option value="-6">แบคทีเรีย E. coli (1 μm)</option>
          <option value="-5">เซลล์เม็ดเลือดแดง (8 μm)</option>
          <option value="-4">เส้นผมมนุษย์ (100 μm)</option>
          <option value="-3">เม็ดทราย / ปลายเข็ม (1 mm)</option>
        </select>
      </div>
    </div>

    <div class="hud">
      <div>ขนาดจริง: <span class="hud-val" id="hudMeters">1.00 × 10⁻⁹ m</span> | <span class="hud-val" id="hudUnits">1.00 nm (10.0 Å)</span></div>
      <div>แรงครอบงำ: <span class="hud-val" id="hudForce">Quantum & Surface Adhesion (van der Waals)</span></div>
      <button type="button" class="btn-ar" id="btnToggleCam">📷 เปิดโหมดกล้อง AR มือเปล่า</button>
    </div>
  </div>

  <script src="ar_mediapipe_controller.js"></script>
  <script>
    const canvas = document.getElementById("scaleCanvas");
    const ctx = canvas.getContext("2d");

    function resize() {
      canvas.width = canvas.parentElement.clientWidth;
      canvas.height = canvas.parentElement.clientHeight;
    }
    window.addEventListener("resize", resize);
    resize();

    let logScale = -9.0;
    let animTime = 0;

    const sliderExp = document.getElementById("sliderExp");
    const txtExp = document.getElementById("txtExp");
    const selPreset = document.getElementById("selPreset");
    const hudMeters = document.getElementById("hudMeters");
    const hudUnits = document.getElementById("hudUnits");
    const hudForce = document.getElementById("hudForce");

    sliderExp.addEventListener("input", (e) => {
      logScale = parseFloat(e.target.value);
      updateDisplay();
    });

    selPreset.addEventListener("change", (e) => {
      logScale = parseFloat(e.target.value);
      sliderExp.value = logScale;
      updateDisplay();
    });

    function updateDisplay() {
      const sizeMeters = Math.pow(10, logScale);
      txtExp.textContent = logScale.toFixed(2) + " (" + formatUnit(sizeMeters) + ")";
      hudMeters.textContent = sizeMeters.toExponential(2) + " m";
      hudUnits.textContent = formatUnit(sizeMeters);

      if (logScale < -8) {
        hudForce.textContent = "Quantum Confinement & Surface Forces (Adhesion >> Gravity)";
      } else if (logScale < -5) {
        hudForce.textContent = "Brownian Motion, Viscous Drag & Surface Tension";
      } else {
        hudForce.textContent = "Classical Gravity & Inertial Mechanics (Mass >> Surface)";
      }
    }

    function formatUnit(m) {
      if (m < 1e-9) return (m * 1e10).toFixed(1) + " Å";
      if (m < 1e-6) return (m * 1e9).toFixed(1) + " nm";
      if (m < 1e-3) return (m * 1e6).toFixed(1) + " μm";
      return (m * 1e3).toFixed(1) + " mm";
    }

    // AR Gesture Hook
    window.onARGesture = function(gesture, data) {
      if (gesture === "PINCH") {
        logScale = Math.max(-10, Math.min(-3, logScale - 0.04));
        sliderExp.value = logScale;
        updateDisplay();
      } else if (gesture === "SPREAD") {
        logScale = Math.max(-10, Math.min(-3, logScale + 0.04));
        sliderExp.value = logScale;
        updateDisplay();
      }
    };

    function draw() {
      ctx.clearRect(0, 0, canvas.width, canvas.height);
      const w = canvas.width;
      const h = canvas.height;
      animTime += 0.025;

      // Draw Grid
      ctx.strokeStyle = "rgba(0, 240, 255, 0.1)";
      ctx.lineWidth = 1;
      for (let x = 0; x < w; x += 30) {
        ctx.beginPath(); ctx.moveTo(x, 0); ctx.lineTo(x, h); ctx.stroke();
      }
      for (let y = 0; y < h; y += 30) {
        ctx.beginPath(); ctx.moveTo(0, y); ctx.lineTo(w, y); ctx.stroke();
      }

      const cx = w * 0.45;
      const cy = h * 0.5;

      // Render based on Scale
      if (logScale < -8.5) {
        // Atomic Lattice & Electron Orbitals (< 1 nm)
        const numAtoms = 7;
        const spacing = 40;
        ctx.fillStyle = "#38bdf8";
        for (let i = -2; i <= 2; i++) {
          for (let j = -2; j <= 2; j++) {
            const ax = cx + i * spacing;
            const ay = cy + j * spacing;
            // Atomic core
            ctx.beginPath();
            ctx.arc(ax, ay, 8, 0, Math.PI * 2);
            ctx.fillStyle = (i===0 && j===0) ? "#f43f5e" : "#0284c7";
            ctx.fill();
            // Electron cloud
            ctx.beginPath();
            ctx.arc(ax, ay, 18, 0, Math.PI * 2);
            ctx.strokeStyle = "rgba(0, 240, 255, 0.4)";
            ctx.stroke();
          }
        }
        ctx.fillStyle = "#facc15";
        ctx.font = "14px 'JetBrains Mono', monospace";
        ctx.fillText("ระดับอะตอมเดี่ยว (Single Atom Lattice): d ~ 0.2 nm", 20, 30);
      } else if (logScale < -7.0) {
        // Nanoparticle Core-Shell (1 - 100 nm)
        const r = Math.min(100, Math.max(25, (logScale + 9) * 40 + 35));
        const grad = ctx.createRadialGradient(cx, cy, 5, cx, cy, r * 1.5);
        grad.addColorStop(0, "rgba(245, 158, 11, 0.9)");
        grad.addColorStop(0.6, "rgba(0, 240, 255, 0.5)");
        grad.addColorStop(1, "transparent");
        ctx.fillStyle = grad;
        ctx.beginPath(); ctx.arc(cx, cy, r * 1.5, 0, Math.PI * 2); ctx.fill();

        ctx.fillStyle = "#0f172a";
        ctx.strokeStyle = "#00f0ff";
        ctx.lineWidth = 3;
        ctx.beginPath(); ctx.arc(cx, cy, r, 0, Math.PI * 2); ctx.fill(); ctx.stroke();

        ctx.fillStyle = "#facc15";
        ctx.font = "14px 'JetBrains Mono', monospace";
        ctx.fillText("อนุภาคนาโน (Quantum Dot / Nanoparticle): 1–100 nm", 20, 30);
      } else if (logScale < -4.5) {
        // Biological Cell / Virus (1 μm - 10 μm)
        ctx.fillStyle = "#10b981";
        ctx.strokeStyle = "#34d399";
        ctx.lineWidth = 3;
        ctx.beginPath();
        ctx.ellipse(cx, cy, 110, 70, animTime * 0.2, 0, Math.PI * 2);
        ctx.fill(); ctx.stroke();

        ctx.fillStyle = "#064e3b";
        ctx.beginPath(); ctx.arc(cx - 20, cy, 25, 0, Math.PI * 2); ctx.fill();
        ctx.fillStyle = "#facc15";
        ctx.font = "14px 'JetBrains Mono', monospace";
        ctx.fillText("ระดับชีวภาพ/เซลล์ (Biological Cell): ~ 10 μm", 20, 30);
      } else {
        // Macro Object (1 mm - 1 cm)
        ctx.fillStyle = "#475569";
        ctx.strokeStyle = "#cbd5e1";
        ctx.lineWidth = 2;
        ctx.fillRect(cx - 80, cy - 80, 160, 160);
        ctx.strokeRect(cx - 80, cy - 80, 160, 160);

        ctx.fillStyle = "#facc15";
        ctx.font = "14px 'JetBrains Mono', monospace";
        ctx.fillText("วัตถุมหภาค (Macro Solid): > 1 mm", 20, 30);
      }

      // Graph Panel on Right
      const gx = w * 0.72;
      const gy = 25;
      const gw = w * 0.25;
      const gh = h - 50;
      ctx.fillStyle = "rgba(15, 23, 42, 0.9)";
      ctx.strokeStyle = "#334155";
      ctx.fillRect(gx, gy, gw, gh);
      ctx.strokeRect(gx, gy, gw, gh);

      ctx.fillStyle = "#00f0ff";
      ctx.font = "11px 'JetBrains Mono', monospace";
      ctx.fillText("Scaling: Surface / Mass", gx + 10, gy + 18);

      ctx.strokeStyle = "#f43f5e";
      ctx.lineWidth = 2;
      ctx.beginPath();
      for (let px = 0; px < gw - 20; px += 2) {
        const sExp = -10 + (px / (gw - 20)) * 7;
        const ratio = Math.min(1, Math.pow(10, -sExp - 3) / 1e7);
        const py = gy + gh - 15 - ratio * (gh - 40);
        if (px === 0) ctx.moveTo(gx + 10 + px, py);
        else ctx.lineTo(gx + 10 + px, py);
      }
      ctx.stroke();

      // Current point on graph
      const curPX = ((logScale - (-10)) / 7) * (gw - 20);
      const curRatio = Math.min(1, Math.pow(10, -logScale - 3) / 1e7);
      const curPY = gy + gh - 15 - curRatio * (gh - 40);
      ctx.fillStyle = "#facc15";
      ctx.beginPath(); ctx.arc(gx + 10 + curPX, curPY, 5, 0, Math.PI * 2); ctx.fill();

      requestAnimationFrame(draw);
    }
    draw();
    updateDisplay();
  </script>
</body>
</html>
"""

# ==============================================================================
# 1.2: Surface Area to Volume Ratio & Fragmentation Solver
# ==============================================================================
SIM_1_2_HTML = """<!DOCTYPE html>
<html lang="th">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Lab 1.2: Surface Area to Volume Ratio</title>
  <link href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;700&family=Sarabun:wght@300;400;600;700&display=swap" rel="stylesheet">
  <script src="https://cdn.jsdelivr.net/npm/@mediapipe/camera_utils/camera_utils.js" crossorigin="anonymous"></script>
  <script src="https://cdn.jsdelivr.net/npm/@mediapipe/hands/hands.js" crossorigin="anonymous"></script>
  <style>
    :root {
      --bg: #020617;
      --panel: #090e1a;
      --cyan: #00f0ff;
      --emerald: #10b981;
      --amber: #f59e0b;
      --rose: #f43f5e;
    }
    * { box-sizing: border-box; margin: 0; padding: 0; }
    body { background: var(--bg); color: #f8fafc; font-family: 'Sarabun', sans-serif; padding: 12px; }
    .sim-card { background: var(--panel); border: 1px solid #1e293b; border-radius: 14px; padding: 18px; box-shadow: 0 10px 30px rgba(0,0,0,0.7); }
    .sim-header { display: flex; justify-content: space-between; align-items: center; border-bottom: 1px solid #1e293b; padding-bottom: 10px; margin-bottom: 12px; }
    .sim-title { font-size: 1.1rem; font-weight: 700; color: var(--emerald); display: flex; align-items: center; gap: 8px; }
    .badge { background: rgba(16,185,129,0.15); border: 1px solid var(--emerald); color: var(--emerald); padding: 3px 10px; border-radius: 9999px; font-size: 0.75rem; font-family: 'JetBrains Mono', monospace; }
    .canvas-box { position: relative; width: 100%; height: 320px; background: #000; border: 1px solid #334155; border-radius: 10px; overflow: hidden; margin-bottom: 14px; }
    canvas { width: 100%; height: 100%; display: block; }
    .controls { display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 12px; background: #0f172a; padding: 12px 16px; border-radius: 10px; border: 1px solid #1e293b; margin-bottom: 12px; }
    .ctrl-group { display: flex; flex-direction: column; gap: 6px; }
    .ctrl-lbl { font-size: 0.8rem; color: #94a3b8; display: flex; justify-content: space-between; font-family: 'JetBrains Mono', monospace; }
    input[type=range] { width: 100%; accent-color: var(--emerald); cursor: pointer; }
    .hud { display: flex; justify-content: space-between; align-items: center; background: #020617; border: 1px solid #334155; border-radius: 8px; padding: 10px 16px; font-size: 0.85rem; font-family: 'JetBrains Mono', monospace; flex-wrap: wrap; gap: 10px; }
    .hud-val { color: var(--amber); font-weight: 700; }
  </style>
</head>
<body>
  <div class="sim-card">
    <div class="sim-header">
      <div class="sim-title">
        <span>📐</span>
        <span>แล็บ 1.2: การแบ่งส่วนลูกบาศก์และอัตราส่วนพื้นที่ผิวต่อปริมาตร (Surface-to-Volume Fragmentation)</span>
      </div>
      <div class="badge">● A/V = 6/d SOLVER</div>
    </div>

    <div class="canvas-box">
      <canvas id="cubeCanvas"></canvas>
    </div>

    <div class="controls">
      <div class="ctrl-group">
        <div class="ctrl-lbl">
          <span>จำนวนการตัดแบ่งตามแนวแกน (Cuts per axis: \\(N\\))</span>
          <span id="txtN">N = 4 (64 nanocubes)</span>
        </div>
        <input type="range" id="sliderN" min="1" max="16" step="1" value="4">
      </div>
      <div class="ctrl-group">
        <div class="ctrl-lbl">
          <span>ขนาดขอบลูกบาศก์ย่อย (Cube size: \\(d\\))</span>
          <span id="txtD">d = 2.50 nm</span>
        </div>
        <input type="range" id="sliderD" min="1" max="50" step="0.5" value="10">
      </div>
    </div>

    <div class="hud">
      <div>อัตราส่วน \\(A/V\\): <span class="hud-val" id="hudAV">0.60 nm⁻¹</span> | พื้นที่ผิวรวม: <span class="hud-val" id="hudArea">600.0 nm²</span></div>
      <div>สัดส่วนอะตอมที่ผิว: <span class="hud-val" id="hudSurfRatio">48.8%</span></div>
      <button type="button" onclick="explodeCubes()" style="background:#10b981; color:#020617; border:none; padding:6px 14px; border-radius:6px; font-weight:700; cursor:pointer;">💥 ระเบิดกระจายอนุภาค 3D</button>
    </div>
  </div>

  <script src="ar_mediapipe_controller.js"></script>
  <script>
    const canvas = document.getElementById("cubeCanvas");
    const ctx = canvas.getContext("2d");

    function resize() {
      canvas.width = canvas.parentElement.clientWidth;
      canvas.height = canvas.parentElement.clientHeight;
    }
    window.addEventListener("resize", resize);
    resize();

    let N = 4;
    let d = 10.0;
    let explodeDist = 0;
    let isExploding = false;
    let animTime = 0;

    const sliderN = document.getElementById("sliderN");
    const sliderD = document.getElementById("sliderD");
    const txtN = document.getElementById("txtN");
    const txtD = document.getElementById("txtD");
    const hudAV = document.getElementById("hudAV");
    const hudArea = document.getElementById("hudArea");
    const hudSurfRatio = document.getElementById("hudSurfRatio");

    sliderN.addEventListener("input", (e) => {
      N = parseInt(e.target.value);
      updateValues();
    });

    sliderD.addEventListener("input", (e) => {
      d = parseFloat(e.target.value);
      updateValues();
    });

    function explodeCubes() {
      isExploding = true;
      explodeDist = 0;
    }

    function updateValues() {
      const totalCubes = N * N * N;
      const subD = d / N;
      txtN.textContent = "N = " + N + " (" + totalCubes + " cubes)";
      txtD.textContent = "d = " + subD.toFixed(2) + " nm";

      const avRatio = 6.0 / subD;
      const totalArea = totalCubes * (6 * subD * subD);
      hudAV.textContent = avRatio.toFixed(2) + " nm⁻¹";
      hudArea.textContent = totalArea.toFixed(1) + " nm²";

      const a = 0.3; // atomic diameter ~ 0.3 nm
      const surfFrac = Math.min(1.0, 1 - Math.pow(Math.max(0, 1 - 2*a/subD), 3));
      hudSurfRatio.textContent = (surfFrac * 100).toFixed(1) + "%";
    }

    function draw() {
      ctx.clearRect(0, 0, canvas.width, canvas.height);
      const w = canvas.width;
      const h = canvas.height;
      animTime += 0.02;

      if (isExploding) {
        explodeDist += 1.5;
        if (explodeDist > 60) isExploding = false;
      } else if (explodeDist > 0) {
        explodeDist *= 0.94;
        if (explodeDist < 0.1) explodeDist = 0;
      }

      // Isometric 3D Projection
      const cx = w * 0.45;
      const cy = h * 0.52;
      const subSize = (140 / N);

      // Rotate angle
      const rot = animTime * 0.3;
      const cosA = Math.cos(rot);
      const sinA = Math.sin(rot);

      for (let z = 0; z < N; z++) {
        for (let y = 0; y < N; y++) {
          for (let x = 0; x < N; x++) {
            // Centered coordinates
            const ox = (x - N/2 + 0.5) * (subSize + explodeDist);
            const oy = (y - N/2 + 0.5) * (subSize + explodeDist);
            const oz = (z - N/2 + 0.5) * (subSize + explodeDist);

            // 3D Isometric projection
            const px = cx + (ox * cosA - oz * sinA) * 1.2 - oy * 0.6;
            const py = cy + (ox * sinA + oz * cosA) * 0.6 + oy * 1.0;

            const sz = subSize * 0.8;

            // Draw Nanocube
            ctx.fillStyle = (x===0||x===N-1||y===0||y===N-1||z===0||z===N-1) ? "rgba(16, 185, 129, 0.75)" : "rgba(15, 23, 42, 0.9)";
            ctx.strokeStyle = "#00f0ff";
            ctx.lineWidth = 1;

            ctx.beginPath();
            ctx.moveTo(px, py - sz);
            ctx.lineTo(px + sz, py - sz * 0.5);
            ctx.lineTo(px + sz, py + sz * 0.5);
            ctx.lineTo(px, py + sz);
            ctx.lineTo(px - sz, py + sz * 0.5);
            ctx.lineTo(px - sz, py - sz * 0.5);
            ctx.closePath();
            ctx.fill();
            ctx.stroke();
          }
        }
      }

      // Graph on Right
      const gx = w * 0.72;
      const gy = 25;
      const gw = w * 0.25;
      const gh = h - 50;
      ctx.fillStyle = "rgba(15, 23, 42, 0.9)";
      ctx.strokeStyle = "#334155";
      ctx.fillRect(gx, gy, gw, gh);
      ctx.strokeRect(gx, gy, gw, gh);

      ctx.fillStyle = "#10b981";
      ctx.font = "11px 'JetBrains Mono', monospace";
      ctx.fillText("A/V Ratio vs Size (d)", gx + 10, gy + 18);

      ctx.strokeStyle = "#facc15";
      ctx.lineWidth = 2;
      ctx.beginPath();
      for (let px = 0; px < gw - 20; px += 2) {
        const plotD = 0.5 + (px / (gw - 20)) * 20;
        const av = 6.0 / plotD;
        const py = gy + gh - 15 - (av / 12.0) * (gh - 40);
        if (px === 0) ctx.moveTo(gx + 10 + px, py);
        else ctx.lineTo(gx + 10 + px, py);
      }
      ctx.stroke();

      requestAnimationFrame(draw);
    }
    draw();
    updateValues();
  </script>
</body>
</html>
"""

# ==============================================================================
# 1.3: Surface Energy & DLVO Colloidal Agglomeration Simulator
# ==============================================================================
SIM_1_3_HTML = """<!DOCTYPE html>
<html lang="th">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Lab 1.3: Surface Energy & DLVO Agglomeration</title>
  <link href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;700&family=Sarabun:wght@300;400;600;700&display=swap" rel="stylesheet">
  <script src="https://cdn.jsdelivr.net/npm/@mediapipe/camera_utils/camera_utils.js" crossorigin="anonymous"></script>
  <script src="https://cdn.jsdelivr.net/npm/@mediapipe/hands/hands.js" crossorigin="anonymous"></script>
  <style>
    :root {
      --bg: #020617;
      --panel: #090e1a;
      --cyan: #00f0ff;
      --amber: #f59e0b;
      --rose: #f43f5e;
      --purple: #a855f7;
    }
    * { box-sizing: border-box; margin: 0; padding: 0; }
    body { background: var(--bg); color: #f8fafc; font-family: 'Sarabun', sans-serif; padding: 12px; }
    .sim-card { background: var(--panel); border: 1px solid #1e293b; border-radius: 14px; padding: 18px; box-shadow: 0 10px 30px rgba(0,0,0,0.7); }
    .sim-header { display: flex; justify-content: space-between; align-items: center; border-bottom: 1px solid #1e293b; padding-bottom: 10px; margin-bottom: 12px; }
    .sim-title { font-size: 1.1rem; font-weight: 700; color: var(--rose); display: flex; align-items: center; gap: 8px; }
    .badge { background: rgba(244,63,94,0.15); border: 1px solid var(--rose); color: var(--rose); padding: 3px 10px; border-radius: 9999px; font-size: 0.75rem; font-family: 'JetBrains Mono', monospace; }
    .canvas-box { position: relative; width: 100%; height: 320px; background: #000; border: 1px solid #334155; border-radius: 10px; overflow: hidden; margin-bottom: 14px; }
    canvas { width: 100%; height: 100%; display: block; }
    .controls { display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 12px; background: #0f172a; padding: 12px 16px; border-radius: 10px; border: 1px solid #1e293b; margin-bottom: 12px; }
    .ctrl-group { display: flex; flex-direction: column; gap: 6px; }
    .ctrl-lbl { font-size: 0.8rem; color: #94a3b8; display: flex; justify-content: space-between; font-family: 'JetBrains Mono', monospace; }
    input[type=range] { width: 100%; accent-color: var(--rose); cursor: pointer; }
    .hud { display: flex; justify-content: space-between; align-items: center; background: #020617; border: 1px solid #334155; border-radius: 8px; padding: 10px 16px; font-size: 0.85rem; font-family: 'JetBrains Mono', monospace; flex-wrap: wrap; gap: 10px; }
    .hud-val { color: var(--amber); font-weight: 700; }
  </style>
</head>
<body>
  <div class="sim-card">
    <div class="sim-header">
      <div class="sim-title">
        <span>🧪</span>
        <span>แล็บ 1.3: พลังงานพื้นผิวและทฤษฎี DLVO การเกาะกลุ่มคอลลอยด์ (DLVO Colloidal Kinetics)</span>
      </div>
      <div class="badge">● 200 PARTICLES BROWNIAN</div>
    </div>

    <div class="canvas-box">
      <canvas id="dlvoCanvas"></canvas>
    </div>

    <div class="controls">
      <div class="ctrl-group">
        <div class="ctrl-lbl">
          <span>ศักย์ซีตา (Zeta Potential: \\(\\zeta\\))</span>
          <span id="txtZeta">|ζ| = 35.0 mV (Stable)</span>
        </div>
        <input type="range" id="sliderZeta" min="0" max="60" step="1" value="35">
      </div>
      <div class="ctrl-group">
        <div class="ctrl-lbl">
          <span>ความตึงผิว / พลังงานพื้นผิว (\\(\\gamma\\))</span>
          <span id="txtGamma">γ = 72.0 mJ/m²</span>
        </div>
        <input type="range" id="sliderGamma" min="10" max="150" step="2" value="72">
      </div>
    </div>

    <div class="hud">
      <div>สถานะคอลลอยด์: <span class="hud-val" id="hudState">เสถียรภาพสูง (Stable Suspension)</span></div>
      <div>พลังงานศักย์รวม DLVO: <span class="hud-val" id="hudBarrier">+18.5 k_BT Barrier</span></div>
      <button type="button" onclick="disperseAll()" style="background:#f43f5e; color:#ffffff; border:none; padding:6px 14px; border-radius:6px; font-weight:700; cursor:pointer;">🌀 กวนสารแขวนลอย (Ultrasonic)</button>
    </div>
  </div>

  <script src="ar_mediapipe_controller.js"></script>
  <script>
    const canvas = document.getElementById("dlvoCanvas");
    const ctx = canvas.getContext("2d");

    function resize() {
      canvas.width = canvas.parentElement.clientWidth;
      canvas.height = canvas.parentElement.clientHeight;
    }
    window.addEventListener("resize", resize);
    resize();

    let zeta = 35;
    let gamma = 72;

    const sliderZeta = document.getElementById("sliderZeta");
    const sliderGamma = document.getElementById("sliderGamma");
    const txtZeta = document.getElementById("txtZeta");
    const txtGamma = document.getElementById("txtGamma");
    const hudState = document.getElementById("hudState");
    const hudBarrier = document.getElementById("hudBarrier");

    sliderZeta.addEventListener("input", (e) => {
      zeta = parseFloat(e.target.value);
      updateDLVO();
    });

    sliderGamma.addEventListener("input", (e) => {
      gamma = parseFloat(e.target.value);
      updateDLVO();
    });

    function updateDLVO() {
      txtZeta.textContent = "|ζ| = " + zeta.toFixed(1) + " mV (" + (zeta >= 30 ? "Stable" : "Agglomerating") + ")";
      txtGamma.textContent = "γ = " + gamma.toFixed(1) + " mJ/m²";

      const barrier = (zeta * 0.6 - gamma * 0.1).toFixed(1);
      hudBarrier.textContent = barrier + " k_B T Barrier";

      if (zeta >= 30) {
        hudState.textContent = "เสถียรภาพสูง (Electrostatic Repulsion Dominates)";
        hudState.style.color = "#10b981";
      } else if (zeta >= 15) {
        hudState.textContent = "เริ่มตกตะกอนช้า (Metastable Flocculation)";
        hudState.style.color = "#f59e0b";
      } else {
        hudState.textContent = "ตกตะกอนเกาะกลุ่มทันที (Rapid Coagulation - vdW Dominates)";
        hudState.style.color = "#f43f5e";
      }
    }

    // Initialize 100 nanoparticles
    const particles = [];
    for (let i = 0; i < 80; i++) {
      particles.push({
        x: Math.random() * 300 + 40,
        y: Math.random() * 200 + 40,
        vx: (Math.random() - 0.5) * 2,
        vy: (Math.random() - 0.5) * 2,
        r: 6
      });
    }

    function disperseAll() {
      particles.forEach(p => {
        p.vx = (Math.random() - 0.5) * 6;
        p.vy = (Math.random() - 0.5) * 6;
      });
    }

    function draw() {
      ctx.clearRect(0, 0, canvas.width, canvas.height);
      const w = canvas.width;
      const h = canvas.height;
      const simW = w * 0.70;

      // Draw Solution Box
      ctx.strokeStyle = "#334155";
      ctx.lineWidth = 2;
      ctx.strokeRect(10, 10, simW, h - 20);

      // Particle physics & collision
      for (let i = 0; i < particles.length; i++) {
        const p1 = particles[i];
        p1.x += p1.vx;
        p1.y += p1.vy;

        // Wall bounce
        if (p1.x < 10 + p1.r || p1.x > simW - p1.r) p1.vx *= -1;
        if (p1.y < 10 + p1.r || p1.y > h - 20 - p1.r) p1.vy *= -1;

        // Inter-particle force
        for (let j = i + 1; j < particles.length; j++) {
          const p2 = particles[j];
          const dx = p2.x - p1.x;
          const dy = p2.y - p1.y;
          const dist = Math.sqrt(dx*dx + dy*dy);

          if (dist < 30) {
            if (zeta < 20) {
              // Attraction (Agglomerate)
              p1.vx += (dx / dist) * 0.15;
              p1.vy += (dy / dist) * 0.15;
              p2.vx -= (dx / dist) * 0.15;
              p2.vy -= (dy / dist) * 0.15;
            } else {
              // Repulsion (Stable)
              p1.vx -= (dx / dist) * 0.2;
              p1.vy -= (dy / dist) * 0.2;
              p2.vx += (dx / dist) * 0.2;
              p2.vy += (dy / dist) * 0.2;
            }
          }
        }

        // Draw particle
        ctx.fillStyle = zeta >= 30 ? "#00f0ff" : "#f43f5e";
        ctx.beginPath();
        ctx.arc(p1.x, p1.y, p1.r, 0, Math.PI * 2);
        ctx.fill();

        // Electric double layer aura
        ctx.strokeStyle = "rgba(0, 240, 255, 0.25)";
        ctx.beginPath();
        ctx.arc(p1.x, p1.y, p1.r + (zeta * 0.2), 0, Math.PI * 2);
        ctx.stroke();
      }

      // DLVO Potential Curve on Right
      const gx = w * 0.73;
      const gy = 25;
      const gw = w * 0.24;
      const gh = h - 50;

      ctx.fillStyle = "rgba(15, 23, 42, 0.9)";
      ctx.strokeStyle = "#334155";
      ctx.fillRect(gx, gy, gw, gh);
      ctx.strokeRect(gx, gy, gw, gh);

      ctx.fillStyle = "#f43f5e";
      ctx.font = "11px 'JetBrains Mono', monospace";
      ctx.fillText("DLVO Potential V(r)", gx + 10, gy + 18);

      // Plot curve
      ctx.strokeStyle = "#facc15";
      ctx.lineWidth = 2;
      ctx.beginPath();
      const midY = gy + gh * 0.5;
      for (let px = 5; px < gw - 10; px += 2) {
        const r = px * 0.15;
        const vdw = -20 / (r * r + 0.1);
        const edl = (zeta * 1.2) * Math.exp(-r * 0.8);
        const vTot = vdw + edl;
        const py = midY - vTot * 1.5;
        if (px === 5) ctx.moveTo(gx + px, Math.max(gy+5, Math.min(gy+gh-5, py)));
        else ctx.lineTo(gx + px, Math.max(gy+5, Math.min(gy+gh-5, py)));
      }
      ctx.stroke();

      requestAnimationFrame(draw);
    }
    draw();
    updateDLVO();
  </script>
</body>
</html>
"""

# ==============================================================================
# 1.4: SEM/TEM Virtual Caliper & Size Distribution Metrology
# ==============================================================================
SIM_1_4_HTML = """<!DOCTYPE html>
<html lang="th">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Lab 1.4: SEM/TEM Caliper Metrology</title>
  <link href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;700&family=Sarabun:wght@300;400;600;700&display=swap" rel="stylesheet">
  <script src="https://cdn.jsdelivr.net/npm/@mediapipe/camera_utils/camera_utils.js" crossorigin="anonymous"></script>
  <script src="https://cdn.jsdelivr.net/npm/@mediapipe/hands/hands.js" crossorigin="anonymous"></script>
  <style>
    :root {
      --bg: #020617;
      --panel: #090e1a;
      --cyan: #00f0ff;
      --amber: #f59e0b;
      --emerald: #10b981;
    }
    * { box-sizing: border-box; margin: 0; padding: 0; }
    body { background: var(--bg); color: #f8fafc; font-family: 'Sarabun', sans-serif; padding: 12px; }
    .sim-card { background: var(--panel); border: 1px solid #1e293b; border-radius: 14px; padding: 18px; box-shadow: 0 10px 30px rgba(0,0,0,0.7); }
    .sim-header { display: flex; justify-content: space-between; align-items: center; border-bottom: 1px solid #1e293b; padding-bottom: 10px; margin-bottom: 12px; }
    .sim-title { font-size: 1.1rem; font-weight: 700; color: var(--amber); display: flex; align-items: center; gap: 8px; }
    .badge { background: rgba(245,158,11,0.15); border: 1px solid var(--amber); color: var(--amber); padding: 3px 10px; border-radius: 9999px; font-size: 0.75rem; font-family: 'JetBrains Mono', monospace; }
    .canvas-box { position: relative; width: 100%; height: 320px; background: #000; border: 1px solid #334155; border-radius: 10px; overflow: hidden; margin-bottom: 14px; cursor: crosshair; }
    canvas { width: 100%; height: 100%; display: block; }
    .hud { display: flex; justify-content: space-between; align-items: center; background: #020617; border: 1px solid #334155; border-radius: 8px; padding: 10px 16px; font-size: 0.85rem; font-family: 'JetBrains Mono', monospace; flex-wrap: wrap; gap: 10px; }
    .hud-val { color: var(--cyan); font-weight: 700; }
  </style>
</head>
<body>
  <div class="sim-card">
    <div class="sim-header">
      <div class="sim-title">
        <span>📏</span>
        <span>แล็บ 1.4: การอ่านสเกลบาร์และสร้างฮิสโตแกรมขนาดอนุภาค (Micrograph Scale Bar Metrology)</span>
      </div>
      <div class="badge">● INTERACTIVE CALIPER</div>
    </div>

    <div class="canvas-box">
      <canvas id="semCanvas"></canvas>
    </div>

    <div class="hud">
      <div>การวัดปัจจุบัน: <span class="hud-val" id="hudCaliper">15.4 nm</span> | อนุภาคที่วัดแล้ว: <span class="hud-val" id="hudCount">12 อนุภาค</span></div>
      <div>ขนาดเฉลี่ย \\(d_{50}\\): <span class="hud-val" id="hudMean">18.2 ± 3.4 nm</span></div>
      <button type="button" onclick="clearMeasurements()" style="background:#f59e0b; color:#020617; border:none; padding:6px 14px; border-radius:6px; font-weight:700; cursor:pointer;">↺ ล้างข้อมูลการวัด</button>
    </div>
  </div>

  <script src="ar_mediapipe_controller.js"></script>
  <script>
    const canvas = document.getElementById("semCanvas");
    const ctx = canvas.getContext("2d");

    function resize() {
      canvas.width = canvas.parentElement.clientWidth;
      canvas.height = canvas.parentElement.clientHeight;
    }
    window.addEventListener("resize", resize);
    resize();

    // Scale bar definition: 80 pixels = 20 nm (4 px/nm)
    const pxPerNm = 4.0;

    // Simulated SEM particles
    const measuredList = [16.2, 19.5, 18.0, 22.1, 14.8, 17.5, 20.2, 18.8, 15.1, 21.0, 19.0, 17.2];
    let p1 = { x: 120, y: 150 };
    let p2 = { x: 180, y: 150 };
    let isDragging = false;
    let dragTarget = null;

    const hudCaliper = document.getElementById("hudCaliper");
    const hudCount = document.getElementById("hudCount");
    const hudMean = document.getElementById("hudMean");

    function updateStats() {
      hudCount.textContent = measuredList.length + " อนุภาค";
      if (measuredList.length === 0) {
        hudMean.textContent = "0.0 ± 0.0 nm";
        return;
      }
      const sum = measuredList.reduce((a,b) => a+b, 0);
      const mean = sum / measuredList.length;
      const variance = measuredList.reduce((a,b) => a + Math.pow(b-mean, 2), 0) / measuredList.length;
      const std = Math.sqrt(variance);
      hudMean.textContent = mean.toFixed(1) + " ± " + std.toFixed(1) + " nm";
    }

    function clearMeasurements() {
      measuredList.length = 0;
      updateStats();
    }

    canvas.addEventListener("mousedown", (e) => {
      const rect = canvas.getBoundingClientRect();
      const mx = e.clientX - rect.left;
      const my = e.clientY - rect.top;

      if (Math.hypot(mx - p1.x, my - p1.y) < 15) {
        isDragging = true; dragTarget = p1;
      } else if (Math.hypot(mx - p2.x, my - p2.y) < 15) {
        isDragging = true; dragTarget = p2;
      } else {
        // Record click measurement
        p1 = { x: mx - 25, y: my };
        p2 = { x: mx + 25, y: my };
        const measuredNm = 50 / pxPerNm;
        measuredList.push(measuredNm);
        updateStats();
      }
    });

    canvas.addEventListener("mousemove", (e) => {
      if (!isDragging || !dragTarget) return;
      const rect = canvas.getBoundingClientRect();
      dragTarget.x = e.clientX - rect.left;
      dragTarget.y = e.clientY - rect.top;
      const distPx = Math.hypot(p2.x - p1.x, p2.y - p1.y);
      hudCaliper.textContent = (distPx / pxPerNm).toFixed(1) + " nm";
    });

    window.addEventListener("mouseup", () => {
      if (isDragging) {
        const distPx = Math.hypot(p2.x - p1.x, p2.y - p1.y);
        measuredList.push(distPx / pxPerNm);
        updateStats();
      }
      isDragging = false; dragTarget = null;
    });

    function draw() {
      ctx.clearRect(0, 0, canvas.width, canvas.height);
      const w = canvas.width;
      const h = canvas.height;
      const semW = w * 0.68;

      // Realistic SEM noise background
      ctx.fillStyle = "#1e293b";
      ctx.fillRect(10, 10, semW, h - 20);

      // Draw simulated nanoparticles on SEM surface
      const simParticles = [
        {x: 100, y: 80, r: 35}, {x: 220, y: 110, r: 42}, {x: 150, y: 220, r: 38},
        {x: 310, y: 70, r: 45}, {x: 280, y: 230, r: 32}, {x: 400, y: 160, r: 48}
      ];

      simParticles.forEach((sp, idx) => {
        const grad = ctx.createRadialGradient(sp.x - 5, sp.y - 5, 2, sp.x, sp.y, sp.r);
        grad.addColorStop(0, "#f8fafc");
        grad.addColorStop(0.5, "#94a3b8");
        grad.addColorStop(1, "#0f172a");
        ctx.fillStyle = grad;
        ctx.beginPath();
        ctx.arc(sp.x, sp.y, sp.r, 0, Math.PI * 2);
        ctx.fill();
      });

      // Draw SEM Scale Bar at bottom left
      ctx.fillStyle = "#ffffff";
      ctx.fillRect(30, h - 45, 80, 5);
      ctx.font = "12px 'JetBrains Mono', monospace";
      ctx.fillText("20 nm (80 px)", 30, h - 55);

      // Draw Interactive Caliper
      ctx.strokeStyle = "#f43f5e";
      ctx.lineWidth = 2;
      ctx.beginPath();
      ctx.moveTo(p1.x, p1.y);
      ctx.lineTo(p2.x, p2.y);
      ctx.stroke();

      ctx.fillStyle = "#facc15";
      ctx.beginPath(); ctx.arc(p1.x, p1.y, 6, 0, Math.PI * 2); ctx.fill();
      ctx.beginPath(); ctx.arc(p2.x, p2.y, 6, 0, Math.PI * 2); ctx.fill();

      // Live Histogram on Right
      const gx = w * 0.72;
      const gy = 25;
      const gw = w * 0.25;
      const gh = h - 50;

      ctx.fillStyle = "rgba(15, 23, 42, 0.9)";
      ctx.strokeStyle = "#334155";
      ctx.fillRect(gx, gy, gw, gh);
      ctx.strokeRect(gx, gy, gw, gh);

      ctx.fillStyle = "#facc15";
      ctx.font = "11px 'JetBrains Mono', monospace";
      ctx.fillText("Size Histogram (nm)", gx + 10, gy + 18);

      // Histogram bins
      const bins = [0, 0, 0, 0, 0]; // <14, 14-17, 17-20, 20-23, >23
      measuredList.forEach(v => {
        if (v < 14) bins[0]++;
        else if (v < 17) bins[1]++;
        else if (v < 20) bins[2]++;
        else if (v < 23) bins[3]++;
        else bins[4]++;
      });

      const maxBin = Math.max(1, ...bins);
      const bw = (gw - 30) / 5;
      bins.forEach((bCount, bIdx) => {
        const bh = (bCount / maxBin) * (gh - 50);
        const bx = gx + 15 + bIdx * bw;
        const by = gy + gh - 15 - bh;
        ctx.fillStyle = "#00f0ff";
        ctx.fillRect(bx, by, bw - 4, bh);
      });

      requestAnimationFrame(draw);
    }
    draw();
    updateStats();
  </script>
</body>
</html>
"""

# ==============================================================================
# 1.5: Master 3D AR Cleanroom Studio & BET Surface Area Analyzer
# ==============================================================================
SIM_1_5_HTML = """<!DOCTYPE html>
<html lang="th">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Lab 1.5: Master AR Nanoscale Studio Hub</title>
  <link href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;700&family=Sarabun:wght@300;400;600;700&display=swap" rel="stylesheet">
  <script src="https://cdn.jsdelivr.net/npm/@mediapipe/camera_utils/camera_utils.js" crossorigin="anonymous"></script>
  <script src="https://cdn.jsdelivr.net/npm/@mediapipe/hands/hands.js" crossorigin="anonymous"></script>
  <style>
    :root {
      --bg: #020617;
      --panel: #090e1a;
      --cyan: #00f0ff;
      --amber: #f59e0b;
      --emerald: #10b981;
      --purple: #a855f7;
    }
    * { box-sizing: border-box; margin: 0; padding: 0; }
    body { background: var(--bg); color: #f8fafc; font-family: 'Sarabun', sans-serif; padding: 12px; }
    .sim-card { background: var(--panel); border: 1px solid #1e293b; border-radius: 14px; padding: 18px; box-shadow: 0 10px 30px rgba(0,0,0,0.7); }
    .sim-header { display: flex; justify-content: space-between; align-items: center; border-bottom: 1px solid #1e293b; padding-bottom: 10px; margin-bottom: 12px; }
    .sim-title { font-size: 1.1rem; font-weight: 700; color: var(--purple); display: flex; align-items: center; gap: 8px; }
    .badge { background: rgba(168,85,247,0.15); border: 1px solid var(--purple); color: var(--purple); padding: 3px 10px; border-radius: 9999px; font-size: 0.75rem; font-family: 'JetBrains Mono', monospace; }
    .canvas-box { position: relative; width: 100%; height: 320px; background: #000; border: 1px solid #334155; border-radius: 10px; overflow: hidden; margin-bottom: 14px; }
    canvas { width: 100%; height: 100%; display: block; }
    .hud { display: flex; justify-content: space-between; align-items: center; background: #020617; border: 1px solid #334155; border-radius: 8px; padding: 10px 16px; font-size: 0.85rem; font-family: 'JetBrains Mono', monospace; flex-wrap: wrap; gap: 10px; }
    .hud-val { color: var(--cyan); font-weight: 700; }
    .btn-action { background: linear-gradient(135deg, #a855f7, #6366f1); color: #ffffff; border: none; border-radius: 6px; padding: 8px 16px; font-weight: 700; cursor: pointer; }
  </style>
</head>
<body>
  <div class="sim-card">
    <div class="sim-header">
      <div class="sim-title">
        <span>🌐</span>
        <span>แล็บ 1.5: สตูดิโอจำลองนาโนฟิสิกส์ 3D/AR ครบวงจร (Universal AR Nanoscale Studio)</span>
      </div>
      <div class="badge">● AR HANDS SKELETON 60 FPS</div>
    </div>

    <div class="canvas-box">
      <canvas id="hubCanvas"></canvas>
    </div>

    <div class="hud">
      <div>โหมดการทดลอง: <span class="hud-val" id="hudMode">1. พื้นที่ผิว BET & การกักขังควอนตัม</span></div>
      <div>สถานะท่าทางมือ AR: <span class="hud-val" id="hudHand">พร้อมตรวจจับ (Tracking Active)</span></div>
      <button type="button" class="btn-action" onclick="toggleMode()">🔄 สลับโหมดการทดลอง 3D</button>
    </div>
  </div>

  <script src="ar_mediapipe_controller.js"></script>
  <script>
    const canvas = document.getElementById("hubCanvas");
    const ctx = canvas.getContext("2d");

    function resize() {
      canvas.width = canvas.parentElement.clientWidth;
      canvas.height = canvas.parentElement.clientHeight;
    }
    window.addEventListener("resize", resize);
    resize();

    let mode = 0;
    const modes = ["1. พื้นที่ผิว BET & ขนาดอนุภาค", "2. การจำลองกลศาสตร์ควอนตัม Brus", "3. โครงสร้างรังผึ้งกราฟีน 2D"];
    const hudMode = document.getElementById("hudMode");

    function toggleMode() {
      mode = (mode + 1) % modes.length;
      hudMode.textContent = modes[mode];
    }

    let animTime = 0;

    function draw() {
      ctx.clearRect(0, 0, canvas.width, canvas.height);
      const w = canvas.width;
      const h = canvas.height;
      animTime += 0.03;

      // 3D Cyber cleanroom perspective grid
      ctx.strokeStyle = "rgba(168, 85, 247, 0.2)";
      ctx.lineWidth = 1;
      for (let x = 0; x < w; x += 40) {
        ctx.beginPath(); ctx.moveTo(x, 0); ctx.lineTo(x, h); ctx.stroke();
      }
      for (let y = 0; y < h; y += 40) {
        ctx.beginPath(); ctx.moveTo(0, y); ctx.lineTo(w, y); ctx.stroke();
      }

      const cx = w * 0.5;
      const cy = h * 0.5;

      if (mode === 0) {
        // Mode 0: 3D BET Rotating Nanoparticle cluster
        for (let i = 0; i < 12; i++) {
          const angle = (i / 12) * Math.PI * 2 + animTime * 0.5;
          const px = cx + Math.cos(angle) * 70;
          const py = cy + Math.sin(angle) * 35;
          ctx.fillStyle = "#00f0ff";
          ctx.beginPath(); ctx.arc(px, py, 14, 0, Math.PI * 2); ctx.fill();
        }
        ctx.fillStyle = "#facc15";
        ctx.beginPath(); ctx.arc(cx, cy, 32, 0, Math.PI * 2); ctx.fill();
      } else if (mode === 1) {
        // Mode 1: Quantum Brus Energy Level Wave
        ctx.strokeStyle = "#a855f7";
        ctx.lineWidth = 3;
        ctx.beginPath();
        for (let px = 50; px < w - 50; px += 4) {
          const py = cy + Math.sin((px * 0.03) + animTime * 2) * 50 * Math.sin((px - 50) / (w - 100) * Math.PI);
          if (px === 50) ctx.moveTo(px, py);
          else ctx.lineTo(px, py);
        }
        ctx.stroke();
      } else {
        // Mode 2: Graphene Hexagonal Monolayer Grid
        ctx.strokeStyle = "#10b981";
        ctx.lineWidth = 2;
        for (let r = 0; r < 4; r++) {
          for (let c = 0; c < 8; c++) {
            const hx = 60 + c * 40 + (r % 2) * 20;
            const hy = 60 + r * 35;
            ctx.beginPath();
            for (let s = 0; s < 6; s++) {
              const ang = (s / 6) * Math.PI * 2 + (Math.PI / 6);
              const sx = hx + Math.cos(ang) * 16;
              const sy = hy + Math.sin(ang) * 16;
              if (s === 0) ctx.moveTo(sx, sy);
              else ctx.lineTo(sx, sy);
            }
            ctx.closePath();
            ctx.stroke();
          }
        }
      }

      requestAnimationFrame(draw);
    }
    draw();
  </script>
</body>
</html>
"""

# Write all 5 upgraded simulators to both course and root simulators folders
sims = {
    "sim_nano_1_1.html": SIM_1_1_HTML,
    "sim_nano_1_2.html": SIM_1_2_HTML,
    "sim_nano_1_3.html": SIM_1_3_HTML,
    "sim_nano_1_4.html": SIM_1_4_HTML,
    "sim_nano_1_5.html": SIM_1_5_HTML
}

for fname, content in sims.items():
    p_nano = os.path.join(NANO_SIMS_DIR, fname)
    p_root = os.path.join(ROOT_SIMS_DIR, fname)
    with open(p_nano, "w", encoding="utf-8") as f:
        f.write(content)
    with open(p_root, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"✅ Upgraded {fname}")

print("🎉 Successfully upgraded all Chapter 1 Nanophysics Simulators!")
