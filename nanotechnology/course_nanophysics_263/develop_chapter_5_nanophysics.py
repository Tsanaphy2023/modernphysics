#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Develops Chapter 5 for Nanotechnological Physics (Course 263):
- Generates 5 Tailored 60 FPS Simulators with AR MediaPipe Integration:
  5.1: Graphene Dirac Cone & Ballistic Electron Transport
  5.2: Carbon Nanotube Chirality Vector (n,m) Roller & Bandgap Solver
  5.3: Quantum Wire 1D Subbands & Van Hove Singularities
  5.4: GMR Spin-Valve & Spintronics Magnetic Memory (MRAM)
  5.5: Master Nano-FET & 2D Transition Metal Dichalcogenide (MoS₂) Studio
- Updates Moodle Standalone Pages with Handcrafted Masterclass Formula Cards
- Syncs to GitHub Pages CDN and Deploys to Moodle Course 263
"""

import os
import re
import json
import requests
import subprocess
import shutil

BASE_DIR = "/Users/chewathassana/Downloads/manus_backup2026/ModernPhysics"
NANO_DIR = os.path.join(BASE_DIR, "nanotechnology/course_nanophysics_263")
NANO_SIMS_DIR = os.path.join(NANO_DIR, "simulators")
ROOT_SIMS_DIR = os.path.join(BASE_DIR, "simulators")
MOODLE_PAGES_DIR = os.path.join(NANO_DIR, "moodle_pages")
CATALOG_FILE = os.path.join(NANO_DIR, "moodle_catalog_263.json")
COURSE_DATA_FILE = os.path.join(NANO_DIR, "course_data.json")

CDN_BASE = "https://tsanaphy2023.github.io/modernphysics"

# ==============================================================================
# 5.1: Graphene Dirac Cone & Ballistic Transport Simulator
# ==============================================================================
SIM_5_1_HTML = """<!DOCTYPE html>
<html lang="th">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Lab 5.1: Graphene Dirac Cone & Ballistic Transport</title>
  <link href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;700&family=Sarabun:wght@300;400;600;700&display=swap" rel="stylesheet">
  <script src="https://cdn.jsdelivr.net/npm/@mediapipe/camera_utils/camera_utils.js" crossorigin="anonymous"></script>
  <script src="https://cdn.jsdelivr.net/npm/@mediapipe/hands/hands.js" crossorigin="anonymous"></script>
  <style>
    :root {
      --bg: #020617;
      --panel: #090e1a;
      --cyan: #00f0ff;
      --amber: #facc15;
      --emerald: #10b981;
    }
    * { box-sizing: border-box; margin: 0; padding: 0; }
    body { background: var(--bg); color: #f8fafc; font-family: 'Sarabun', sans-serif; padding: 12px; }
    .sim-card { background: var(--panel); border: 1px solid #1e293b; border-radius: 14px; padding: 18px; box-shadow: 0 10px 30px rgba(0,0,0,0.7); }
    .sim-header { display: flex; justify-content: space-between; align-items: center; border-bottom: 1px solid #1e293b; padding-bottom: 10px; margin-bottom: 12px; }
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
  </style>
</head>
<body>
  <div class="sim-card">
    <div class="sim-header">
      <div class="sim-title">
        <span>⚛️</span>
        <span>แล็บ 5.1: กรวยดิแรกและการนำไฟฟ้าแอมบิโพลาร์ของกราฟีน (Graphene Dirac Cone Solver)</span>
      </div>
      <div class="badge">● MASSLESS DIRAC FERMIONS (v_F = 10⁶ m/s)</div>
    </div>

    <div class="canvas-box">
      <canvas id="diracCanvas"></canvas>
    </div>

    <div class="controls">
      <div class="ctrl-group">
        <div class="ctrl-lbl">
          <span>ระดับพลังงานเฟอร์มิ (Fermi Energy: \\(E_F\\))</span>
          <span id="txtEF">EF = +0.20 eV (n-type Electron Conduction)</span>
        </div>
        <input type="range" id="sliderEF" min="-0.6" max="0.6" step="0.02" value="0.2">
      </div>
      <div class="ctrl-group">
        <div class="ctrl-lbl">
          <span>ความหนาแน่นพาหะประจุ (Carrier Density: \\(n_s\\))</span>
          <span id="txtNs">ns = 3.5 × 10¹² cm⁻²</span>
        </div>
        <input type="range" id="sliderNs" min="0.1" max="10.0" step="0.1" value="3.5">
      </div>
    </div>

    <div class="hud">
      <div>ความเร็วเฟอร์มิ: <span class="hud-val" id="hudVF">1.0 × 10⁶ m/s</span> | ความคล่องตัว (\\(\\mu\\)): <span class="hud-val" id="hudMob">220,000 cm²/V·s</span></div>
      <div>สถานะพาหะ: <span class="hud-val" id="hudCarrier">🟦 พาหะอิเล็กตรอน (Conduction Band)</span></div>
      <button type="button" onclick="resetToDiracPoint()" style="background:#00f0ff; color:#020617; border:none; padding:6px 14px; border-radius:6px; font-weight:700; cursor:pointer;">⚡ จูนสู่จุดดิแรกเป็นกลาง (Dirac Neutrality Point)</button>
    </div>
  </div>

  <script src="ar_mediapipe_controller.js"></script>
  <script>
    const canvas = document.getElementById("diracCanvas");
    const ctx = canvas.getContext("2d");

    function resize() {
      canvas.width = canvas.parentElement.clientWidth;
      canvas.height = canvas.parentElement.clientHeight;
    }
    window.addEventListener("resize", resize);
    resize();

    let EF_eV = 0.2;
    let animTime = 0;

    const sliderEF = document.getElementById("sliderEF");
    const txtEF = document.getElementById("txtEF");
    const hudCarrier = document.getElementById("hudCarrier");

    sliderEF.addEventListener("input", (e) => {
      EF_eV = parseFloat(e.target.value);
      updateDirac();
    });

    function resetToDiracPoint() {
      EF_eV = 0.0;
      sliderEF.value = 0.0;
      updateDirac();
    }

    function updateDirac() {
      if (EF_eV > 0.05) {
        txtEF.textContent = "EF = +" + EF_eV.toFixed(2) + " eV (n-type Electron)";
        hudCarrier.textContent = "🟦 พาหะอิเล็กตรอน (Conduction Band)";
      } else if (EF_eV < -0.05) {
        txtEF.textContent = "EF = " + EF_eV.toFixed(2) + " eV (p-type Hole)";
        hudCarrier.textContent = "🟥 พาหะโฮล (Valence Band Holes)";
      } else {
        txtEF.textContent = "EF = 0.00 eV (Dirac Point Neutrality)";
        hudCarrier.textContent = "🟨 จุดดิแรกเป็นกลาง (Minimum Conductivity)";
      }
    }

    function draw() {
      ctx.clearRect(0, 0, canvas.width, canvas.height);
      const w = canvas.width;
      const h = canvas.height;
      animTime += 0.03;

      const simW = w * 0.55;
      const cx = simW * 0.5;
      const cy = h * 0.5;

      // 3D Perspective Box
      ctx.fillStyle = "#020617";
      ctx.strokeStyle = "#334155";
      ctx.lineWidth = 2;
      ctx.fillRect(15, 15, simW - 15, h - 30);
      ctx.strokeRect(15, 15, simW - 15, h - 30);

      // Draw Upper Dirac Cone (Conduction Band)
      const coneH = 90;
      const coneR = 75;

      ctx.fillStyle = "rgba(56, 189, 248, 0.25)";
      ctx.strokeStyle = "#38bdf8";
      ctx.lineWidth = 2;
      ctx.beginPath();
      ctx.moveTo(cx, cy);
      ctx.lineTo(cx - coneR, cy - coneH);
      ctx.lineTo(cx + coneR, cy - coneH);
      ctx.closePath();
      ctx.fill();
      ctx.stroke();

      // Draw Lower Dirac Cone (Valence Band)
      ctx.fillStyle = "rgba(244, 63, 94, 0.25)";
      ctx.strokeStyle = "#f43f5e";
      ctx.beginPath();
      ctx.moveTo(cx, cy);
      ctx.lineTo(cx - coneR, cy + coneH);
      ctx.lineTo(cx + coneR, cy + coneH);
      ctx.closePath();
      ctx.fill();
      ctx.stroke();

      // Fermi Energy Level Disk
      const efY = cy - (EF_eV / 0.6) * coneH;
      const efR = Math.abs(EF_eV / 0.6) * coneR;

      ctx.fillStyle = EF_eV >= 0 ? "rgba(250, 204, 21, 0.8)" : "rgba(244, 63, 94, 0.8)";
      ctx.strokeStyle = "#ffffff";
      ctx.lineWidth = 2;
      ctx.beginPath();
      ctx.ellipse(cx, efY, Math.max(4, efR), Math.max(2, efR * 0.4), 0, 0, Math.PI * 2);
      ctx.fill();
      ctx.stroke();

      ctx.fillStyle = "#facc15";
      ctx.font = "11px 'JetBrains Mono', monospace";
      ctx.fillText("Fermi Level EF = " + (EF_eV >= 0 ? "+" : "") + EF_eV.toFixed(2) + " eV", cx + Math.max(10, efR) + 12, efY + 4);

      // Right Side: Linear Energy Dispersion Graph E(k)
      const gx = w * 0.58;
      const gy = 25;
      const gw = w * 0.39;
      const gh = h - 50;

      ctx.fillStyle = "rgba(15, 23, 42, 0.9)";
      ctx.strokeStyle = "#334155";
      ctx.fillRect(gx, gy, gw, gh);
      ctx.strokeRect(gx, gy, gw, gh);

      ctx.fillStyle = "#00f0ff";
      ctx.font = "11px 'JetBrains Mono', monospace";
      ctx.fillText("Graphene Linear Dispersion E(k) = ±ℏ v_F |k|", gx + 10, gy + 18);

      const midGX = gx + gw * 0.5;
      const midGY = gy + gh * 0.5;

      // Linear V-Shape lines
      ctx.strokeStyle = "#38bdf8";
      ctx.lineWidth = 2.5;
      ctx.beginPath();
      ctx.moveTo(midGX - 60, midGY - 75);
      ctx.lineTo(midGX, midGY);
      ctx.lineTo(midGX + 60, midGY - 75);
      ctx.stroke();

      ctx.strokeStyle = "#f43f5e";
      ctx.beginPath();
      ctx.moveTo(midGX - 60, midGY + 75);
      ctx.lineTo(midGX, midGY);
      ctx.lineTo(midGX + 60, midGY + 75);
      ctx.stroke();

      // Current EF on plot
      ctx.strokeStyle = "#facc15";
      ctx.lineWidth = 1.5;
      ctx.setLineDash([4, 4]);
      const plotEFY = midGY - (EF_eV / 0.6) * 75;
      ctx.beginPath(); ctx.moveTo(gx + 15, plotEFY); ctx.lineTo(gx + gw - 15, plotEFY); ctx.stroke();
      ctx.setLineDash([]);

      requestAnimationFrame(draw);
    }
    draw();
    updateDirac();
  </script>
</body>
</html>
"""

# ==============================================================================
# 5.2: Carbon Nanotube Chirality (n,m) Roller Simulator
# ==============================================================================
SIM_5_2_HTML = """<!DOCTYPE html>
<html lang="th">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Lab 5.2: Carbon Nanotube Chirality (n,m) Roller</title>
  <link href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;700&family=Sarabun:wght@300;400;600;700&display=swap" rel="stylesheet">
  <script src="https://cdn.jsdelivr.net/npm/@mediapipe/camera_utils/camera_utils.js" crossorigin="anonymous"></script>
  <script src="https://cdn.jsdelivr.net/npm/@mediapipe/hands/hands.js" crossorigin="anonymous"></script>
  <style>
    :root {
      --bg: #020617;
      --panel: #090e1a;
      --cyan: #00f0ff;
      --amber: #facc15;
      --emerald: #10b981;
      --purple: #c084fc;
    }
    * { box-sizing: border-box; margin: 0; padding: 0; }
    body { background: var(--bg); color: #f8fafc; font-family: 'Sarabun', sans-serif; padding: 12px; }
    .sim-card { background: var(--panel); border: 1px solid #1e293b; border-radius: 14px; padding: 18px; box-shadow: 0 10px 30px rgba(0,0,0,0.7); }
    .sim-header { display: flex; justify-content: space-between; align-items: center; border-bottom: 1px solid #1e293b; padding-bottom: 10px; margin-bottom: 12px; }
    .sim-title { font-size: 1.1rem; font-weight: 700; color: var(--purple); display: flex; align-items: center; gap: 8px; }
    .badge { background: rgba(192,132,252,0.15); border: 1px solid var(--purple); color: var(--purple); padding: 3px 10px; border-radius: 9999px; font-size: 0.75rem; font-family: 'JetBrains Mono', monospace; }
    .canvas-box { position: relative; width: 100%; height: 320px; background: #000; border: 1px solid #334155; border-radius: 10px; overflow: hidden; margin-bottom: 14px; }
    canvas { width: 100%; height: 100%; display: block; }
    .controls { display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 12px; background: #0f172a; padding: 12px 16px; border-radius: 10px; border: 1px solid #1e293b; margin-bottom: 12px; }
    .ctrl-group { display: flex; flex-direction: column; gap: 6px; }
    .ctrl-lbl { font-size: 0.8rem; color: #94a3b8; display: flex; justify-content: space-between; font-family: 'JetBrains Mono', monospace; }
    input[type=range] { width: 100%; accent-color: var(--purple); cursor: pointer; }
    .hud { display: flex; justify-content: space-between; align-items: center; background: #020617; border: 1px solid #334155; border-radius: 8px; padding: 10px 16px; font-size: 0.85rem; font-family: 'JetBrains Mono', monospace; flex-wrap: wrap; gap: 10px; }
    .hud-val { color: var(--cyan); font-weight: 700; }
  </style>
</head>
<body>
  <div class="sim-card">
    <div class="sim-header">
      <div class="sim-title">
        <span>🌀</span>
        <span>แล็บ 5.2: การม้วนท่อนาโนคาร์บอนและดัชนีไครัลลิตี (CNT Chirality (n,m) Roller)</span>
      </div>
      <div class="badge">● METALLIC VS SEMICONDUCTING SOLVER</div>
    </div>

    <div class="canvas-box">
      <canvas id="cntCanvas"></canvas>
    </div>

    <div class="controls">
      <div class="ctrl-group">
        <div class="ctrl-lbl">
          <span>ดัชนีไครัล n (Chiral Index: \\(n\\))</span>
          <span id="txtN">n = 10</span>
        </div>
        <input type="range" id="sliderN" min="3" max="20" step="1" value="10">
      </div>
      <div class="ctrl-group">
        <div class="ctrl-lbl">
          <span>ดัชนีไครัล m (Chiral Index: \\(m\\))</span>
          <span id="txtM">m = 10 (Armchair Metallic)</span>
        </div>
        <input type="range" id="sliderM" min="0" max="20" step="1" value="10">
      </div>
    </div>

    <div class="hud">
      <div>เส้นผ่านศูนย์กลางท่อ: <span class="hud-val" id="hudDiam">1.36 nm</span> | มุมไครัล (\\(\\theta\\)): <span class="hud-val" id="hudAngle">30.0° (Armchair)</span></div>
      <div>สมบัติทางไฟฟ้า: <span class="hud-val" id="hudType">⚡ ตัวนำโลหะ (Metallic CNT, Eg = 0 eV)</span></div>
      <button type="button" onclick="setPresetZigzag()" style="background:#c084fc; color:#020617; border:none; padding:6px 14px; border-radius:6px; font-weight:700; cursor:pointer;">🔄 สลับแบบซิกแซก (10, 0) Semiconducting</button>
    </div>
  </div>

  <script src="ar_mediapipe_controller.js"></script>
  <script>
    const canvas = document.getElementById("cntCanvas");
    const ctx = canvas.getContext("2d");

    function resize() {
      canvas.width = canvas.parentElement.clientWidth;
      canvas.height = canvas.parentElement.clientHeight;
    }
    window.addEventListener("resize", resize);
    resize();

    let n = 10, m = 10;
    let animTime = 0;

    const sliderN = document.getElementById("sliderN");
    const sliderM = document.getElementById("sliderM");
    const txtN = document.getElementById("txtN");
    const txtM = document.getElementById("txtM");
    const hudDiam = document.getElementById("hudDiam");
    const hudAngle = document.getElementById("hudAngle");
    const hudType = document.getElementById("hudType");

    sliderN.addEventListener("input", (e) => {
      n = parseInt(e.target.value);
      if (m > n) { m = n; sliderM.value = m; }
      updateCNT();
    });

    sliderM.addEventListener("input", (e) => {
      m = parseInt(e.target.value);
      if (m > n) { n = m; sliderN.value = n; }
      updateCNT();
    });

    function setPresetZigzag() {
      n = 10; m = 0;
      sliderN.value = n; sliderM.value = m;
      updateCNT();
    }

    function calculateCNT() {
      const a = 0.246; // nm (graphene lattice constant)
      const Ch = a * Math.sqrt(n * n + n * m + m * m);
      const diam = Ch / Math.PI;
      const angleRad = Math.atan((Math.sqrt(3) * m) / (2 * n + m));
      const angleDeg = angleRad * (180 / Math.PI);
      const isMetallic = (n - m) % 3 === 0;
      const Eg = isMetallic ? 0.0 : (0.8 / diam);
      return { diam, angleDeg, isMetallic, Eg };
    }

    function updateCNT() {
      txtN.textContent = "n = " + n;
      txtM.textContent = "m = " + m;
      const res = calculateCNT();
      hudDiam.textContent = res.diam.toFixed(2) + " nm";
      hudAngle.textContent = res.angleDeg.toFixed(1) + "° (" + (n === m ? "Armchair" : m === 0 ? "Zigzag" : "Chiral") + ")";

      if (res.isMetallic) {
        hudType.textContent = "⚡ ตัวนำโลหะ (Metallic CNT, Eg = 0 eV)";
      } else {
        hudType.textContent = "🟦 สารกึ่งตัวนำ (Semiconducting, Eg = " + res.Eg.toFixed(2) + " eV)";
      }
    }

    function draw() {
      ctx.clearRect(0, 0, canvas.width, canvas.height);
      const w = canvas.width;
      const h = canvas.height;
      animTime += 0.03;

      const simW = w * 0.55;
      const cx = simW * 0.5;
      const cy = h * 0.5;

      // 3D Tube Viewport
      ctx.fillStyle = "#020617";
      ctx.strokeStyle = "#334155";
      ctx.lineWidth = 2;
      ctx.fillRect(15, 15, simW - 15, h - 30);
      ctx.strokeRect(15, 15, simW - 15, h - 30);

      const res = calculateCNT();
      const tubeR = Math.max(25, Math.min(80, res.diam * 35));

      // Draw 3D Cylindrical Carbon Nanotube Rings
      const numRings = 10;
      for (let r = 0; r < numRings; r++) {
        const ringX = 50 + r * 28;
        const col = res.isMetallic ? "#00f0ff" : "#c084fc";

        ctx.strokeStyle = col;
        ctx.lineWidth = 2;
        ctx.beginPath();
        ctx.ellipse(ringX, cy, tubeR * 0.3, tubeR, 0, 0, Math.PI * 2);
        ctx.stroke();

        // Carbon atoms on ring
        for (let a = 0; a < 8; a++) {
          const ang = (a / 8) * Math.PI * 2 + animTime * 2 + r * (res.angleDeg * 0.05);
          const ay = cy + Math.sin(ang) * tubeR;
          const ax = ringX + Math.cos(ang) * (tubeR * 0.3);

          ctx.fillStyle = "#ffffff";
          ctx.beginPath(); ctx.arc(ax, ay, 4, 0, Math.PI * 2); ctx.fill();
        }
      }

      // Right Side: Graphene 2D Hexagonal Roll Map
      const gx = w * 0.58;
      const gy = 25;
      const gw = w * 0.39;
      const gh = h - 50;

      ctx.fillStyle = "rgba(15, 23, 42, 0.9)";
      ctx.strokeStyle = "#334155";
      ctx.fillRect(gx, gy, gw, gh);
      ctx.strokeRect(gx, gy, gw, gh);

      ctx.fillStyle = "#c084fc";
      ctx.font = "11px 'JetBrains Mono', monospace";
      ctx.fillText("Chiral Vector C_h = (" + n + ", " + m + ")", gx + 10, gy + 18);

      // Chiral vector line
      ctx.strokeStyle = "#facc15";
      ctx.lineWidth = 3;
      ctx.beginPath();
      ctx.moveTo(gx + 20, gy + gh - 30);
      const vx = gx + 20 + (n / 20) * (gw - 50);
      const vy = gy + gh - 30 - (m / 20) * (gh - 60);
      ctx.lineTo(vx, vy);
      ctx.stroke();

      ctx.fillStyle = "#facc15";
      ctx.beginPath(); ctx.arc(vx, vy, 6, 0, Math.PI * 2); ctx.fill();

      requestAnimationFrame(draw);
    }
    draw();
    updateCNT();
  </script>
</body>
</html>
"""

# ==============================================================================
# 5.3: Quantum Wire 1D Subbands & Conductance Simulator
# ==============================================================================
SIM_5_3_HTML = """<!DOCTYPE html>
<html lang="th">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Lab 5.3: Quantum Wire 1D Subbands & Density of States</title>
  <link href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;700&family=Sarabun:wght@300;400;600;700&display=swap" rel="stylesheet">
  <script src="https://cdn.jsdelivr.net/npm/@mediapipe/camera_utils/camera_utils.js" crossorigin="anonymous"></script>
  <script src="https://cdn.jsdelivr.net/npm/@mediapipe/hands/hands.js" crossorigin="anonymous"></script>
  <style>
    :root {
      --bg: #020617;
      --panel: #090e1a;
      --cyan: #00f0ff;
      --amber: #facc15;
      --emerald: #10b981;
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
    .hud-val { color: var(--cyan); font-weight: 700; }
  </style>
</head>
<body>
  <div class="sim-card">
    <div class="sim-header">
      <div class="sim-title">
        <span>⚡</span>
        <span>แล็บ 5.3: แถบย่อย 1 มิติและยอดแหลม Van Hove (1D Quantum Wire Subbands)</span>
      </div>
      <div class="badge">● 1D DENSITY OF STATES g(E) ∝ E⁻¹/²</div>
    </div>

    <div class="canvas-box">
      <canvas id="qwireCanvas"></canvas>
    </div>

    <div class="controls">
      <div class="ctrl-group">
        <div class="ctrl-lbl">
          <span>ความกว้างลวดควอนตัม (Nanowire Width: \\(W\\))</span>
          <span id="txtW">W = 10.0 nm</span>
        </div>
        <input type="range" id="sliderW" min="4.0" max="30.0" step="0.5" value="10.0">
      </div>
      <div class="ctrl-group">
        <div class="ctrl-lbl">
          <span>ระดับพลังงานอิเล็กตรอน (Energy Level: \\(E\\))</span>
          <span id="txtE">E = 0.45 eV (Channels = 3)</span>
        </div>
        <input type="range" id="sliderE" min="0.1" max="1.2" step="0.02" value="0.45">
      </div>
    </div>

    <div class="hud">
      <div>จำนวนโหมดนำส่ง: <span class="hud-val" id="hudModes">3 ควอนตัมโหมด (n=1,2,3)</span> | สภาพนำไฟฟ้า: <span class="hud-val" id="hudG">3 × G₀ (232.4 μS)</span></div>
      <div>ระยะห่างแถบย่อย (\\(\\Delta E_{12}\\)): <span class="hud-val" id="hudDeltaE">112.5 meV</span></div>
      <button type="button" onclick="increaseConfinement()" style="background:#10b981; color:#020617; border:none; padding:6px 14px; border-radius:6px; font-weight:700; cursor:pointer;">⚡ เพิ่มการกักขังมิติเดียว (W = 5 nm)</button>
    </div>
  </div>

  <script src="ar_mediapipe_controller.js"></script>
  <script>
    const canvas = document.getElementById("qwireCanvas");
    const ctx = canvas.getContext("2d");

    function resize() {
      canvas.width = canvas.parentElement.clientWidth;
      canvas.height = canvas.parentElement.clientHeight;
    }
    window.addEventListener("resize", resize);
    resize();

    let W_nm = 10.0;
    let E_eV = 0.45;
    let animTime = 0;

    const sliderW = document.getElementById("sliderW");
    const sliderE = document.getElementById("sliderE");
    const txtW = document.getElementById("txtW");
    const txtE = document.getElementById("txtE");
    const hudModes = document.getElementById("hudModes");
    const hudG = document.getElementById("hudG");

    sliderW.addEventListener("input", (e) => {
      W_nm = parseFloat(e.target.value);
      updateQWire();
    });

    sliderE.addEventListener("input", (e) => {
      E_eV = parseFloat(e.target.value);
      updateQWire();
    });

    function increaseConfinement() {
      W_nm = 5.0; sliderW.value = W_nm;
      updateQWire();
    }

    function calculateSubbands() {
      // E_n = n^2 * hbar^2 * pi^2 / (2 m* W^2)
      const baseE = 0.376 / (W_nm * W_nm); // approx eV for GaAs m*=0.067
      const subbands = [];
      for (let n = 1; n <= 6; n++) {
        subbands.push(n * n * baseE);
      }
      return subbands;
    }

    function updateQWire() {
      txtW.textContent = "W = " + W_nm.toFixed(1) + " nm";
      const subs = calculateSubbands();
      const openModes = subs.filter(e => e <= E_eV).length;
      txtE.textContent = "E = " + E_eV.toFixed(2) + " eV (Channels = " + openModes + ")";
      hudModes.textContent = openModes + " ควอนตัมโหมด";
      hudG.textContent = openModes + " × G₀ (" + (openModes * 77.48).toFixed(1) + " μS)";
    }

    function draw() {
      ctx.clearRect(0, 0, canvas.width, canvas.height);
      const w = canvas.width;
      const h = canvas.height;
      animTime += 0.03;

      const simW = w * 0.50;
      const cy = h * 0.5;

      // 1D Nanowire Channel Viewport
      ctx.fillStyle = "#020617";
      ctx.strokeStyle = "#334155";
      ctx.lineWidth = 2;
      ctx.fillRect(15, 15, simW - 15, h - 30);
      ctx.strokeRect(15, 15, simW - 15, h - 30);

      const wireH = Math.max(15, W_nm * 3.5);

      // Nanowire body
      ctx.fillStyle = "rgba(16, 185, 129, 0.2)";
      ctx.strokeStyle = "#10b981";
      ctx.lineWidth = 2;
      ctx.fillRect(25, cy - wireH/2, simW - 35, wireH);
      ctx.strokeRect(25, cy - wireH/2, simW - 35, wireH);

      // Ballistic 1D electron wave packets
      ctx.fillStyle = "#00f0ff";
      for (let k = 0; k < 18; k++) {
        const px = 30 + ((k * 30 + animTime * 80) % (simW - 50));
        const py = cy + Math.sin(k * 1.5) * (wireH * 0.35);
        ctx.beginPath(); ctx.arc(px, py, 4, 0, Math.PI * 2); ctx.fill();
      }

      // Right Side: 1D Density of States Graph g(E)
      const gx = w * 0.54;
      const gy = 25;
      const gw = w * 0.43;
      const gh = h - 50;

      ctx.fillStyle = "rgba(15, 23, 42, 0.9)";
      ctx.strokeStyle = "#334155";
      ctx.fillRect(gx, gy, gw, gh);
      ctx.strokeRect(gx, gy, gw, gh);

      ctx.fillStyle = "#10b981";
      ctx.font = "11px 'JetBrains Mono', monospace";
      ctx.fillText("1D Density of States g(E) (Van Hove Singularities)", gx + 10, gy + 18);

      const subs = calculateSubbands();
      ctx.strokeStyle = "#facc15";
      ctx.lineWidth = 2;
      ctx.beginPath();

      for (let py = 0; py < gh - 35; py += 2) {
        const plotE = ((gh - 35 - py) / (gh - 35)) * 1.2;
        let dos = 0;
        subs.forEach(sn => {
          if (plotE > sn) {
            dos += 1.0 / Math.sqrt(plotE - sn + 0.01);
          }
        });
        const plotX = gx + 15 + Math.min(gw - 35, dos * 12);
        const plotY = gy + 25 + py;
        if (py === 0) ctx.moveTo(plotX, plotY);
        else ctx.lineTo(plotX, plotY);
      }
      ctx.stroke();

      requestAnimationFrame(draw);
    }
    draw();
    updateQWire();
  </script>
</body>
</html>
"""

# ==============================================================================
# 5.4: GMR Spin-Valve & Spintronics MRAM Simulator
# ==============================================================================
SIM_5_4_HTML = """<!DOCTYPE html>
<html lang="th">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Lab 5.4: GMR Spin-Valve & Spintronics MRAM</title>
  <link href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;700&family=Sarabun:wght@300;400;600;700&display=swap" rel="stylesheet">
  <script src="https://cdn.jsdelivr.net/npm/@mediapipe/camera_utils/camera_utils.js" crossorigin="anonymous"></script>
  <script src="https://cdn.jsdelivr.net/npm/@mediapipe/hands/hands.js" crossorigin="anonymous"></script>
  <style>
    :root {
      --bg: #020617;
      --panel: #090e1a;
      --cyan: #00f0ff;
      --amber: #facc15;
      --rose: #f43f5e;
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
    .hud-val { color: var(--cyan); font-weight: 700; }
  </style>
</head>
<body>
  <div class="sim-card">
    <div class="sim-header">
      <div class="sim-title">
        <span>🧲</span>
        <span>แล็บ 5.4: วาล์วสปินและสปินทรอนิกส์ GMR/TMR (Giant Magnetoresistance Spin-Valve)</span>
      </div>
      <div class="badge">● NOBEL PRIZE PHYSICS 2007</div>
    </div>

    <div class="canvas-box">
      <canvas id="gmrCanvas"></canvas>
    </div>

    <div class="controls">
      <div class="ctrl-group">
        <div class="ctrl-lbl">
          <span>สนามแม่เหล็กภายนอกควบคุม (External B-Field: \\(H\\))</span>
          <span id="txtH">H = +50 Oe (Parallel Alignment)</span>
        </div>
        <input type="range" id="sliderH" min="-100" max="100" step="5" value="50">
      </div>
      <div class="ctrl-group">
        <div class="ctrl-lbl">
          <span>สถานะการเรียงตัวของสปิน (Magnetic Alignment)</span>
          <span id="txtAlign">Parallel (Low Resistance State: Bit '0')</span>
        </div>
        <select id="selAlign" style="background:#020617; color:#f8fafc; border:1px solid #334155; padding:6px; border-radius:6px; font-family:inherit; font-size:0.85rem;">
          <option value="p" selected>1. ขนานกัน (Parallel: R_low = 12.5 Ω, Bit '0')</option>
          <option value="ap">2. สวนทางกัน (Anti-Parallel: R_high = 24.8 Ω, Bit '1')</option>
        </select>
      </div>
    </div>

    <div class="hud">
      <div>ความต้านทานไฟฟ้า: <span class="hud-val" id="hudR">12.5 Ω (Low R)</span> | อัตราส่วน GMR: <span class="hud-val" id="hudGMR">98.4% MR Ratio</span></div>
      <div>สถานะบิตหน่วยความจำ: <span class="hud-val" id="hudBit">Logic '0' (MRAM Readout)</span></div>
      <button type="button" onclick="toggleSpinPolarization()" style="background:#f43f5e; color:#ffffff; border:none; padding:6px 14px; border-radius:6px; font-weight:700; cursor:pointer;">⚡ สลับทิศสปินชั้นอิสระ (Toggle Free Layer)</button>
    </div>
  </div>

  <script src="ar_mediapipe_controller.js"></script>
  <script>
    const canvas = document.getElementById("gmrCanvas");
    const ctx = canvas.getContext("2d");

    function resize() {
      canvas.width = canvas.parentElement.clientWidth;
      canvas.height = canvas.parentElement.clientHeight;
    }
    window.addEventListener("resize", resize);
    resize();

    let isParallel = true;
    let bField = 50;
    let animTime = 0;

    const sliderH = document.getElementById("sliderH");
    const selAlign = document.getElementById("selAlign");
    const txtH = document.getElementById("txtH");
    const hudR = document.getElementById("hudR");
    const hudBit = document.getElementById("hudBit");

    sliderH.addEventListener("input", (e) => {
      bField = parseFloat(e.target.value);
      isParallel = bField >= 0;
      updateGMR();
    });

    selAlign.addEventListener("change", (e) => {
      isParallel = e.target.value === "p";
      updateGMR();
    });

    function toggleSpinPolarization() {
      isParallel = !isParallel;
      updateGMR();
    }

    function updateGMR() {
      txtH.textContent = "H = " + (bField >= 0 ? "+" : "") + bField.toFixed(0) + " Oe";
      if (isParallel) {
        hudR.textContent = "12.5 Ω (Low Resistance)";
        hudBit.textContent = "Logic '0' (Parallel Alignment)";
      } else {
        hudR.textContent = "24.8 Ω (High Resistance)";
        hudBit.textContent = "Logic '1' (Anti-Parallel Alignment)";
      }
    }

    function draw() {
      ctx.clearRect(0, 0, canvas.width, canvas.height);
      const w = canvas.width;
      const h = canvas.height;
      animTime += 0.04;

      const simW = w * 0.55;
      const cx = simW * 0.5;

      // Trilayer Spin Valve Viewport
      ctx.fillStyle = "#020617";
      ctx.strokeStyle = "#334155";
      ctx.lineWidth = 2;
      ctx.fillRect(15, 15, simW - 15, h - 30);
      ctx.strokeRect(15, 15, simW - 15, h - 30);

      // Layer 1: Free Ferromagnetic Layer (Top)
      ctx.fillStyle = isParallel ? "rgba(56, 189, 248, 0.4)" : "rgba(244, 63, 94, 0.4)";
      ctx.fillRect(35, 45, simW - 60, 45);
      ctx.strokeStyle = isParallel ? "#38bdf8" : "#f43f5e";
      ctx.strokeRect(35, 45, simW - 60, 45);

      ctx.fillStyle = "#ffffff";
      ctx.font = "12px 'JetBrains Mono', monospace";
      ctx.fillText(isParallel ? "Free Layer: Magnetization ➔ Right" : "Free Layer: Magnetization ⬅ Left", 45, 72);

      // Layer 2: Non-Magnetic Metal Spacer (Cu / Al2O3)
      ctx.fillStyle = "rgba(234, 179, 8, 0.3)";
      ctx.fillRect(35, 95, simW - 60, 25);
      ctx.strokeStyle = "#eab308";
      ctx.strokeRect(35, 95, simW - 60, 25);
      ctx.fillStyle = "#facc15";
      ctx.fillText("Non-Magnetic Spacer (Cu / Ru)", 45, 112);

      // Layer 3: Pinned Ferromagnetic Layer (Bottom)
      ctx.fillStyle = "rgba(56, 189, 248, 0.4)";
      ctx.fillRect(35, 125, simW - 60, 45);
      ctx.strokeStyle = "#38bdf8";
      ctx.strokeRect(35, 125, simW - 60, 45);
      ctx.fillStyle = "#ffffff";
      ctx.fillText("Pinned Layer: Fixed Magnetization ➔ Right", 45, 152);

      // Spin electrons passing through
      const electronCount = isParallel ? 25 : 8; // high transmission in parallel
      ctx.fillStyle = "#00f0ff";
      for (let e = 0; e < electronCount; e++) {
        const ex = 40 + ((e * 20 + animTime * 60) % (simW - 80));
        const ey = 55 + (e % 3) * 35;
        ctx.beginPath(); ctx.arc(ex, ey, 4, 0, Math.PI * 2); ctx.fill();
      }

      // Right Side: Magnetoresistance Hysteresis Curve R(H)
      const gx = w * 0.58;
      const gy = 25;
      const gw = w * 0.39;
      const gh = h - 50;

      ctx.fillStyle = "rgba(15, 23, 42, 0.9)";
      ctx.strokeStyle = "#334155";
      ctx.fillRect(gx, gy, gw, gh);
      ctx.strokeRect(gx, gy, gw, gh);

      ctx.fillStyle = "#f43f5e";
      ctx.font = "11px 'JetBrains Mono', monospace";
      ctx.fillText("GMR Hysteresis Loop R(H)", gx + 10, gy + 18);

      // Plot square GMR curve
      ctx.strokeStyle = "#00f0ff";
      ctx.lineWidth = 2.5;
      ctx.beginPath();
      ctx.moveTo(gx + 15, gy + gh - 20);
      ctx.lineTo(gx + gw * 0.35, gy + gh - 20);
      ctx.lineTo(gx + gw * 0.35, gy + 45);
      ctx.lineTo(gx + gw * 0.65, gy + 45);
      ctx.lineTo(gx + gw * 0.65, gy + gh - 20);
      ctx.lineTo(gx + gw - 15, gy + gh - 20);
      ctx.stroke();

      requestAnimationFrame(draw);
    }
    draw();
    updateGMR();
  </script>
</body>
</html>
"""

# ==============================================================================
# 5.5: Master Nano-FET & 2D Electronics Studio Simulator
# ==============================================================================
SIM_5_5_HTML = """<!DOCTYPE html>
<html lang="th">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Lab 5.5: Master Nano-FET & 2D Electronics Studio</title>
  <link href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;700&family=Sarabun:wght@300;400;600;700&display=swap" rel="stylesheet">
  <script src="https://cdn.jsdelivr.net/npm/@mediapipe/camera_utils/camera_utils.js" crossorigin="anonymous"></script>
  <script src="https://cdn.jsdelivr.net/npm/@mediapipe/hands/hands.js" crossorigin="anonymous"></script>
  <style>
    :root {
      --bg: #020617;
      --panel: #090e1a;
      --cyan: #00f0ff;
      --amber: #facc15;
      --emerald: #10b981;
    }
    * { box-sizing: border-box; margin: 0; padding: 0; }
    body { background: var(--bg); color: #f8fafc; font-family: 'Sarabun', sans-serif; padding: 12px; }
    .sim-card { background: var(--panel); border: 1px solid #1e293b; border-radius: 14px; padding: 18px; box-shadow: 0 10px 30px rgba(0,0,0,0.7); }
    .sim-header { display: flex; justify-content: space-between; align-items: center; border-bottom: 1px solid #1e293b; padding-bottom: 10px; margin-bottom: 12px; }
    .sim-title { font-size: 1.1rem; font-weight: 700; color: var(--cyan); display: flex; align-items: center; gap: 8px; }
    .badge { background: rgba(0,240,255,0.15); border: 1px solid var(--cyan); color: var(--cyan); padding: 3px 10px; border-radius: 9999px; font-size: 0.75rem; font-family: 'JetBrains Mono', monospace; }
    .canvas-box { position: relative; width: 100%; height: 320px; background: #000; border: 1px solid #334155; border-radius: 10px; overflow: hidden; margin-bottom: 14px; }
    canvas { width: 100%; height: 100%; display: block; }
    .hud { display: flex; justify-content: space-between; align-items: center; background: #020617; border: 1px solid #334155; border-radius: 8px; padding: 10px 16px; font-size: 0.85rem; font-family: 'JetBrains Mono', monospace; flex-wrap: wrap; gap: 10px; }
    .hud-val { color: var(--cyan); font-weight: 700; }
    .btn-switch { background: linear-gradient(135deg, #0284c7, #00f0ff); color: #020617; border: none; padding: 8px 16px; border-radius: 6px; font-weight: 700; cursor: pointer; }
  </style>
</head>
<body>
  <div class="sim-card">
    <div class="sim-header">
      <div class="sim-title">
        <span>🌐</span>
        <span>แล็บ 5.5: สตูดิโอนาโนอิเล็กทรอนิกส์และทรานซิสเตอร์ 2D (Master Nano-FET Studio)</span>
      </div>
      <div class="badge">● AR HANDS MULTI-MODAL 60 FPS</div>
    </div>

    <div class="canvas-box">
      <canvas id="hubCanvas"></canvas>
    </div>

    <div class="hud">
      <div>โครงสร้างนาโนอิเล็กทรอนิกส์ 3D: <span class="hud-val" id="hudMode">1. ทรานซิสเตอร์ 2D MoS₂ Field-Effect Transistor</span></div>
      <div>สถานะกล้อง AR: <span class="hud-val" id="hudAR">Active (60 FPS Tracking)</span></div>
      <button type="button" class="btn-switch" onclick="switchBay()">🔄 สลับโหมดทรานซิสเตอร์ 3D</button>
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

    let bayIndex = 0;
    const bays = ["1. ทรานซิสเตอร์ 2D MoS₂ Field-Effect Transistor", "2. ทรานซิสเตอร์ท่อนาโนคาร์บอน CNT-FET", "3. อุปกรณ์สปินทรอนิกส์ MRAM Memory Cell"];
    const hudMode = document.getElementById("hudMode");

    function switchBay() {
      bayIndex = (bayIndex + 1) % bays.length;
      hudMode.textContent = bays[bayIndex];
    }

    let animTime = 0;

    function draw() {
      ctx.clearRect(0, 0, canvas.width, canvas.height);
      const w = canvas.width;
      const h = canvas.height;
      animTime += 0.03;

      const cx = w * 0.5;
      const cy = h * 0.5;

      // Perspective Grid
      ctx.strokeStyle = "rgba(0, 240, 255, 0.2)";
      ctx.lineWidth = 1;
      for (let x = 0; x < w; x += 40) {
        ctx.beginPath(); ctx.moveTo(x, 0); ctx.lineTo(x, h); ctx.stroke();
      }
      for (let y = 0; y < h; y += 40) {
        ctx.beginPath(); ctx.moveTo(0, y); ctx.lineTo(w, y); ctx.stroke();
      }

      if (bayIndex === 0) {
        // Mode 0: 2D MoS2 FET Structure (Source, Drain, Back-Gate)
        // Source Electrode
        ctx.fillStyle = "#eab308";
        ctx.fillRect(cx - 150, cy - 30, 80, 50);
        ctx.fillStyle = "#020617"; ctx.font = "12px 'JetBrains Mono', monospace"; ctx.fillText("Source", cx - 135, cy);

        // Drain Electrode
        ctx.fillStyle = "#eab308";
        ctx.fillRect(cx + 70, cy - 30, 80, 50);
        ctx.fillStyle = "#020617"; ctx.fillText("Drain", cx + 90, cy);

        // Monolayer MoS2 Channel (Blue-Green)
        ctx.fillStyle = "rgba(16, 185, 129, 0.6)";
        ctx.fillRect(cx - 80, cy - 15, 160, 20);
        ctx.strokeStyle = "#10b981"; ctx.strokeRect(cx - 80, cy - 15, 160, 20);
        ctx.fillStyle = "#ffffff"; ctx.fillText("Monolayer MoS2 Channel", cx - 75, cy);

        // Electrons flowing
        ctx.fillStyle = "#00f0ff";
        for (let k = 0; k < 6; k++) {
          const ex = cx - 70 + ((k * 30 + animTime * 70) % 140);
          ctx.beginPath(); ctx.arc(ex, cy - 5, 4, 0, Math.PI * 2); ctx.fill();
        }
      } else if (bayIndex === 1) {
        // Mode 1: CNT-FET Coaxial Gate
        ctx.strokeStyle = "#c084fc";
        ctx.lineWidth = 3;
        ctx.strokeRect(cx - 120, cy - 25, 240, 50);
        ctx.fillStyle = "rgba(192, 132, 252, 0.2)";
        ctx.fillRect(cx - 120, cy - 25, 240, 50);
      } else {
        // Mode 2: MRAM Spin Valve Stack
        ctx.fillStyle = "#f43f5e"; ctx.fillRect(cx - 60, cy - 40, 120, 25);
        ctx.fillStyle = "#facc15"; ctx.fillRect(cx - 60, cy - 10, 120, 15);
        ctx.fillStyle = "#38bdf8"; ctx.fillRect(cx - 60, cy + 10, 120, 25);
      }

      requestAnimationFrame(draw);
    }
    draw();
  </script>
</body>
</html>
"""

# 1. Write simulators
ch5_sims = {
    "sim_nano_5_1.html": SIM_5_1_HTML,
    "sim_nano_5_2.html": SIM_5_2_HTML,
    "sim_nano_5_3.html": SIM_5_3_HTML,
    "sim_nano_5_4.html": SIM_5_4_HTML,
    "sim_nano_5_5.html": SIM_5_5_HTML
}

for fname, content in ch5_sims.items():
    with open(os.path.join(NANO_SIMS_DIR, fname), "w", encoding="utf-8") as f:
        f.write(content)
    with open(os.path.join(ROOT_SIMS_DIR, fname), "w", encoding="utf-8") as f:
        f.write(content)
    print(f"✅ Generated Chapter 5 Simulator: {fname}")

# 2. Sync to gh-pages branch
TMP_GH = "/tmp/clean_gh_pages"
if os.path.exists(TMP_GH):
    shutil.rmtree(TMP_GH)
os.makedirs(TMP_GH, exist_ok=True)

shutil.copytree(ROOT_SIMS_DIR, os.path.join(TMP_GH, "simulators"))
shutil.copytree(os.path.join(BASE_DIR, "assets"), os.path.join(TMP_GH, "assets"))
with open(os.path.join(TMP_GH, ".nojekyll"), "w") as f:
    f.write("")
if os.path.exists(os.path.join(BASE_DIR, "index.html")):
    shutil.copy(os.path.join(BASE_DIR, "index.html"), os.path.join(TMP_GH, "index.html"))

subprocess.run(["git", "init"], cwd=TMP_GH, check=True)
subprocess.run(["git", "checkout", "-b", "gh-pages"], cwd=TMP_GH, check=True)
subprocess.run(["git", "add", "."], cwd=TMP_GH, check=True)
subprocess.run(["git", "commit", "-m", "feat(sims): add chapter 5 tailored carbon nanomaterials and spintronics 60fps simulators"], cwd=TMP_GH, check=True)

remote_url = f"https://{os.environ.get('GH_PAT', '')}@github.com/Tsanaphy2023/modernphysics.git"
subprocess.run(["git", "push", "--force", remote_url, "gh-pages"], cwd=TMP_GH, check=True)
print("🎉 Force pushed Chapter 5 Simulators to gh-pages CDN!")

# 3. Re-run deploy_masterclass_formulas_course_263.py to update Moodle
subprocess.run(["python3", "nanotechnology/course_nanophysics_263/deploy_masterclass_formulas_course_263.py"], cwd=BASE_DIR, check=True)

print("🎉 Successfully developed, synced, and deployed Chapter 5 to Moodle Course 263!")
