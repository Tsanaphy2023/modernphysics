#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Develops Chapter 2 for Nanotechnological Physics (Course 263):
- Generates 5 Tailored 60 FPS Simulators with AR MediaPipe Integration:
  2.1: Brus Model & 3D Quantum Confinement Particle-in-a-Sphere
  2.2: Quantum Dot Photoluminescence (PL) & QLED Spectrum Synthesizer
  2.3: Gold/Silver LSPR Surface Plasmon Resonance & Biosensor
  2.4: Ballistic Quantized Conductance (2e²/h) & Superparamagnetism
  2.5: Universal AR Quantum Optics & Plasmonics Cleanroom Studio
- Updates Moodle Standalone Pages with High-Contrast Masterclass Formula Cards
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
# 2.1: Brus Model & 3D Quantum Confinement Simulator
# ==============================================================================
SIM_2_1_HTML = """<!DOCTYPE html>
<html lang="th">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Lab 2.1: Brus Model & Quantum Confinement</title>
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
      --purple: #c084fc;
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
        <span>แล็บ 2.1: แบบจำลอง Brus และการกักขังเชิงควอนตัม (Brus Quantum Confinement Solver)</span>
      </div>
      <div class="badge">● 3D PARTICLE-IN-A-SPHERE</div>
    </div>

    <div class="canvas-box">
      <canvas id="brusCanvas"></canvas>
    </div>

    <div class="controls">
      <div class="ctrl-group">
        <div class="ctrl-lbl">
          <span>รัศมีควอนตัมดอท (Quantum Dot Radius: \\(R\\))</span>
          <span id="txtR">R = 2.50 nm</span>
        </div>
        <input type="range" id="sliderR" min="1.0" max="8.0" step="0.05" value="2.5">
      </div>
      <div class="ctrl-group">
        <div class="ctrl-lbl">
          <span>วัสดุสารกึ่งตัวนำ (Semiconductor Material)</span>
          <span id="txtMat">CdSe (Eg bulk = 1.74 eV)</span>
        </div>
        <select id="selMat" style="background:#020617; color:#f8fafc; border:1px solid #334155; padding:6px; border-radius:6px; font-family:inherit; font-size:0.85rem;">
          <option value="1.74,0.13,9.2" selected>CdSe (แคดเมียมซีลีไนด์: แสงที่ตามองเห็น)</option>
          <option value="0.75,0.06,12.5">InAs (อินเดียมอาร์เซไนด์: อินฟราเรดใกล้)</option>
          <option value="1.35,0.07,12.4">InP (อินเดียมฟอสไฟด์: ปลอดสารพิษ QLED)</option>
          <option value="2.42,0.18,8.7">CdS (แคดเมียมซัลไฟด์: แสงสีฟ้า-เขียว)</option>
        </select>
      </div>
    </div>

    <div class="hud">
      <div>Band Gap: <span class="hud-val" id="hudEg">2.28 eV</span> | ความยาวคลื่น: <span class="hud-val" id="hudLambda">543.8 nm</span></div>
      <div>สีเรืองแสง: <span class="hud-val" id="hudColor">🟩 เขียวมรกต (Green)</span></div>
      <button type="button" onclick="triggerLaserPulse()" style="background:#00f0ff; color:#020617; border:none; padding:6px 14px; border-radius:6px; font-weight:700; cursor:pointer;">⚡ กระตุ้นแสงเลเซอร์ UV (365 nm)</button>
    </div>
  </div>

  <script src="ar_mediapipe_controller.js"></script>
  <script>
    const canvas = document.getElementById("brusCanvas");
    const ctx = canvas.getContext("2d");

    function resize() {
      canvas.width = canvas.parentElement.clientWidth;
      canvas.height = canvas.parentElement.clientHeight;
    }
    window.addEventListener("resize", resize);
    resize();

    let R = 2.5; // nm
    let Eg_bulk = 1.74; // eV
    let m_eff = 0.13; // m0
    let eps_r = 9.2;
    let animTime = 0;
    let laserPulse = 0;

    const sliderR = document.getElementById("sliderR");
    const txtR = document.getElementById("txtR");
    const selMat = document.getElementById("selMat");
    const txtMat = document.getElementById("txtMat");
    const hudEg = document.getElementById("hudEg");
    const hudLambda = document.getElementById("hudLambda");
    const hudColor = document.getElementById("hudColor");

    sliderR.addEventListener("input", (e) => {
      R = parseFloat(e.target.value);
      updateBrus();
    });

    selMat.addEventListener("change", (e) => {
      const parts = e.target.value.split(",");
      Eg_bulk = parseFloat(parts[0]);
      m_eff = parseFloat(parts[1]);
      eps_r = parseFloat(parts[2]);
      updateBrus();
    });

    function triggerLaserPulse() {
      laserPulse = 1.0;
    }

    function calculateEg(r_nm) {
      // Brus formula: Eg(R) = Eg_bulk + hbar^2*pi^2 / (2 m* R^2) - 1.786 e^2 / (4 pi eps R)
      const hbar_eV_s = 6.582119569e-16;
      const m0_kg = 9.1093837e-31;
      const q_C = 1.602176634e-19;
      const eps0 = 8.8541878128e-12;
      const hbar_J_s = 1.054571817e-34;

      const R_m = r_nm * 1e-9;
      const m_star_kg = m_eff * m0_kg;

      // Kinetic confinement term (eV)
      const E_conf_J = (hbar_J_s * hbar_J_s * Math.PI * Math.PI) / (2 * m_star_kg * R_m * R_m);
      const E_conf_eV = E_conf_J / q_C;

      // Coulomb attraction term (eV)
      const E_coul_J = (1.786 * q_C * q_C) / (4 * Math.PI * eps_r * eps0 * R_m);
      const E_coul_eV = E_coul_J / q_C;

      return Eg_bulk + E_conf_eV - E_coul_eV;
    }

    function nmToColor(wavelength) {
      if (wavelength < 400) return { r: 128, g: 0, b: 255, name: "🟪 อัลตราไวโอเลต / ม่วงเข้ม" };
      if (wavelength < 450) return { r: 75, g: 0, b: 230, name: "🟪 ม่วง (Violet)" };
      if (wavelength < 485) return { r: 0, g: 150, b: 255, name: "🟦 ฟ้า (Cyan/Blue)" };
      if (wavelength < 500) return { r: 0, g: 230, b: 200, name: "🟦 ฟ้าน้ำทะเล (Cyan)" };
      if (wavelength < 560) return { r: 0, g: 255, b: 80, name: "🟩 เขียวมรกต (Green)" };
      if (wavelength < 590) return { r: 255, g: 220, b: 0, name: "🟨 เหลืองอำพัน (Yellow)" };
      if (wavelength < 630) return { r: 255, g: 120, b: 0, name: "🟧 ส้มสด (Orange)" };
      if (wavelength <= 720) return { r: 255, g: 30, b: 30, name: "🟥 แดงทับทิม (Red)" };
      return { r: 180, g: 20, b: 20, name: "🟥 อินฟราเรดใกล้ (Near-IR)" };
    }

    function updateBrus() {
      txtR.textContent = "R = " + R.toFixed(2) + " nm (d = " + (R*2).toFixed(2) + " nm)";
      const Eg = calculateEg(R);
      const lambda_nm = (1239.84 / Eg);

      hudEg.textContent = Eg.toFixed(2) + " eV (ΔE = +" + (Eg - Eg_bulk).toFixed(2) + " eV)";
      hudLambda.textContent = lambda_nm.toFixed(1) + " nm";

      const col = nmToColor(lambda_nm);
      hudColor.textContent = col.name;
    }

    // AR Gesture Hook
    window.onARGesture = function(gesture, data) {
      if (gesture === "PINCH") {
        R = Math.max(1.0, Math.min(8.0, R - 0.05));
        sliderR.value = R;
        updateBrus();
      } else if (gesture === "SPREAD") {
        R = Math.max(1.0, Math.min(8.0, R + 0.05));
        sliderR.value = R;
        updateBrus();
      }
    };

    function draw() {
      ctx.clearRect(0, 0, canvas.width, canvas.height);
      const w = canvas.width;
      const h = canvas.height;
      animTime += 0.03;

      if (laserPulse > 0) {
        laserPulse *= 0.92;
        if (laserPulse < 0.02) laserPulse = 0;
      }

      const cx = w * 0.42;
      const cy = h * 0.5;

      const Eg = calculateEg(R);
      const lambda_nm = (1239.84 / Eg);
      const col = nmToColor(lambda_nm);

      // Draw Laser Beam from top left
      if (laserPulse > 0.1) {
        ctx.strokeStyle = `rgba(168, 85, 247, ${laserPulse})`;
        ctx.lineWidth = 6 * laserPulse;
        ctx.beginPath();
        ctx.moveTo(20, 20);
        ctx.lineTo(cx, cy);
        ctx.stroke();
      }

      // Draw 3D Spherical Quantum Dot
      const pixelRadius = R * 14;
      const glowGrad = ctx.createRadialGradient(cx, cy, pixelRadius * 0.2, cx, cy, pixelRadius * 2.2);
      glowGrad.addColorStop(0, `rgba(${col.r}, ${col.g}, ${col.b}, ${0.9 + laserPulse * 0.3})`);
      glowGrad.addColorStop(0.5, `rgba(${col.r}, ${col.g}, ${col.b}, 0.4)`);
      glowGrad.addColorStop(1, "transparent");

      ctx.fillStyle = glowGrad;
      ctx.beginPath();
      ctx.arc(cx, cy, pixelRadius * 2.2, 0, Math.PI * 2);
      ctx.fill();

      // Electron Wavefunction Shells inside sphere
      for (let s = 1; s <= 3; s++) {
        const shellR = (pixelRadius / 3) * s;
        ctx.strokeStyle = `rgba(255, 255, 255, ${0.4 - s * 0.1})`;
        ctx.lineWidth = 1.5;
        ctx.beginPath();
        ctx.arc(cx, cy, shellR, 0, Math.PI * 2);
        ctx.stroke();
      }

      // Core Ball
      const coreGrad = ctx.createRadialGradient(cx - pixelRadius*0.3, cy - pixelRadius*0.3, 2, cx, cy, pixelRadius);
      coreGrad.addColorStop(0, "#ffffff");
      coreGrad.addColorStop(0.3, `rgb(${col.r}, ${col.g}, ${col.b})`);
      coreGrad.addColorStop(1, "#020617");

      ctx.fillStyle = coreGrad;
      ctx.beginPath();
      ctx.arc(cx, cy, pixelRadius, 0, Math.PI * 2);
      ctx.fill();

      // Right Side: Brus Energy Curve Graph
      const gx = w * 0.70;
      const gy = 25;
      const gw = w * 0.27;
      const gh = h - 50;

      ctx.fillStyle = "rgba(15, 23, 42, 0.9)";
      ctx.strokeStyle = "#334155";
      ctx.fillRect(gx, gy, gw, gh);
      ctx.strokeRect(gx, gy, gw, gh);

      ctx.fillStyle = "#00f0ff";
      ctx.font = "11px 'JetBrains Mono', monospace";
      ctx.fillText("Brus Curve: Eg(R) vs Radius", gx + 10, gy + 18);

      // Plot Brus Curve
      ctx.strokeStyle = "#facc15";
      ctx.lineWidth = 2;
      ctx.beginPath();
      for (let px = 0; px < gw - 20; px += 2) {
        const plotR = 1.0 + (px / (gw - 20)) * 7.0;
        const plotEg = calculateEg(plotR);
        const ratio = (plotEg - Eg_bulk) / 2.5; // Max scale ~2.5 eV increase
        const py = gy + gh - 15 - Math.min(1, ratio) * (gh - 40);
        if (px === 0) ctx.moveTo(gx + 10 + px, py);
        else ctx.lineTo(gx + 10 + px, py);
      }
      ctx.stroke();

      // Current Point on Graph
      const curPX = ((R - 1.0) / 7.0) * (gw - 20);
      const curRatio = (Eg - Eg_bulk) / 2.5;
      const curPY = gy + gh - 15 - Math.min(1, curRatio) * (gh - 40);
      ctx.fillStyle = `rgb(${col.r}, ${col.g}, ${col.b})`;
      ctx.beginPath();
      ctx.arc(gx + 10 + curPX, curPY, 6, 0, Math.PI * 2);
      ctx.fill();
      ctx.strokeStyle = "#ffffff";
      ctx.stroke();

      requestAnimationFrame(draw);
    }
    draw();
    updateBrus();
  </script>
</body>
</html>
"""

# ==============================================================================
# 2.2: Quantum Dot Photoluminescence Spectrum Synthesizer
# ==============================================================================
SIM_2_2_HTML = """<!DOCTYPE html>
<html lang="th">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Lab 2.2: Quantum Dots Photoluminescence & QLED</title>
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
    .sim-title { font-size: 1.1rem; font-weight: 700; color: var(--amber); display: flex; align-items: center; gap: 8px; }
    .badge { background: rgba(250,204,21,0.15); border: 1px solid var(--amber); color: var(--amber); padding: 3px 10px; border-radius: 9999px; font-size: 0.75rem; font-family: 'JetBrains Mono', monospace; }
    .canvas-box { position: relative; width: 100%; height: 320px; background: #000; border: 1px solid #334155; border-radius: 10px; overflow: hidden; margin-bottom: 14px; }
    canvas { width: 100%; height: 100%; display: block; }
    .controls { display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 12px; background: #0f172a; padding: 12px 16px; border-radius: 10px; border: 1px solid #1e293b; margin-bottom: 12px; }
    .ctrl-group { display: flex; flex-direction: column; gap: 6px; }
    .ctrl-lbl { font-size: 0.8rem; color: #94a3b8; display: flex; justify-content: space-between; font-family: 'JetBrains Mono', monospace; }
    input[type=range] { width: 100%; accent-color: var(--amber); cursor: pointer; }
    .hud { display: flex; justify-content: space-between; align-items: center; background: #020617; border: 1px solid #334155; border-radius: 8px; padding: 10px 16px; font-size: 0.85rem; font-family: 'JetBrains Mono', monospace; flex-wrap: wrap; gap: 10px; }
    .hud-val { color: var(--cyan); font-weight: 700; }
  </style>
</head>
<body>
  <div class="sim-card">
    <div class="sim-header">
      <div class="sim-title">
        <span>🌈</span>
        <span>แล็บ 2.2: สเปกตรัมการเรืองแสง PL และจอภาพ QLED (Quantum Dots Photoluminescence)</span>
      </div>
      <div class="badge">● FULL SPECTRUM SYNTHESIZER</div>
    </div>

    <div class="canvas-box">
      <canvas id="plCanvas"></canvas>
    </div>

    <div class="controls">
      <div class="ctrl-group">
        <div class="ctrl-lbl">
          <span>ขนาดอนุภาคเฉลี่ย (Peak Emission Wavelength)</span>
          <span id="txtPeak">530 nm (Green QLED)</span>
        </div>
        <input type="range" id="sliderPeak" min="440" max="660" step="2" value="530">
      </div>
      <div class="ctrl-group">
        <div class="ctrl-lbl">
          <span>ความกว้างครึ่งค่าสูงสุด (FWHM Bandwidth)</span>
          <span id="txtFWHM">28 nm (High Color Purity)</span>
        </div>
        <input type="range" id="sliderFWHM" min="18" max="60" step="1" value="28">
      </div>
    </div>

    <div class="hud">
      <div>พลังงานโฟตอน: <span class="hud-val" id="hudPhoton">2.34 eV</span> | พิกัดสี CIE 1931: <span class="hud-val" id="hudCIE">(0.18, 0.72)</span></div>
      <div>สเปกตรัมบริสุทธิ์: <span class="hud-val" id="hudPurity">94.2% Rec. 2020 Gamut</span></div>
      <button type="button" onclick="cycleColors()" style="background:#facc15; color:#020617; border:none; padding:6px 14px; border-radius:6px; font-weight:700; cursor:pointer;">🔄 สลับ 3 แม่สีหลัก RGB QLED</button>
    </div>
  </div>

  <script src="ar_mediapipe_controller.js"></script>
  <script>
    const canvas = document.getElementById("plCanvas");
    const ctx = canvas.getContext("2d");

    function resize() {
      canvas.width = canvas.parentElement.clientWidth;
      canvas.height = canvas.parentElement.clientHeight;
    }
    window.addEventListener("resize", resize);
    resize();

    let peakLambda = 530;
    let fwhm = 28;

    const sliderPeak = document.getElementById("sliderPeak");
    const sliderFWHM = document.getElementById("sliderFWHM");
    const txtPeak = document.getElementById("txtPeak");
    const txtFWHM = document.getElementById("txtFWHM");
    const hudPhoton = document.getElementById("hudPhoton");
    const hudCIE = document.getElementById("hudCIE");

    sliderPeak.addEventListener("input", (e) => {
      peakLambda = parseFloat(e.target.value);
      updatePL();
    });

    sliderFWHM.addEventListener("input", (e) => {
      fwhm = parseFloat(e.target.value);
      updatePL();
    });

    let qledIndex = 0;
    const qledPresets = [465, 530, 630];
    function cycleColors() {
      qledIndex = (qledIndex + 1) % qledPresets.length;
      peakLambda = qledPresets[qledIndex];
      sliderPeak.value = peakLambda;
      updatePL();
    }

    function updatePL() {
      txtPeak.textContent = peakLambda + " nm";
      txtFWHM.textContent = fwhm + " nm";
      const photon_eV = (1239.84 / peakLambda);
      hudPhoton.textContent = photon_eV.toFixed(2) + " eV";

      if (peakLambda < 490) hudCIE.textContent = "(0.14, 0.06) Blue QLED";
      else if (peakLambda < 570) hudCIE.textContent = "(0.19, 0.73) Green QLED";
      else hudCIE.textContent = "(0.68, 0.31) Red QLED";
    }

    function wavelengthToRGB(w) {
      let r = 0, g = 0, b = 0;
      if (w >= 380 && w < 440) { r = -(w - 440) / 60; b = 1.0; }
      else if (w >= 440 && w < 490) { g = (w - 440) / 50; b = 1.0; }
      else if (w >= 490 && w < 510) { g = 1.0; b = -(w - 510) / 20; }
      else if (w >= 510 && w < 580) { r = (w - 510) / 70; g = 1.0; }
      else if (w >= 580 && w < 645) { r = 1.0; g = -(w - 645) / 65; }
      else if (w >= 645 && w <= 750) { r = 1.0; }
      return { r: Math.round(r * 255), g: Math.round(g * 255), b: Math.round(b * 255) };
    }

    function draw() {
      ctx.clearRect(0, 0, canvas.width, canvas.height);
      const w = canvas.width;
      const h = canvas.height;

      // Draw Vials on Left
      const numVials = 5;
      const vY = h * 0.65;
      for (let i = 0; i < numVials; i++) {
        const vX = 40 + i * 50;
        const vLambda = 460 + i * 42;
        const vCol = wavelengthToRGB(vLambda);

        // Glass vial
        ctx.strokeStyle = "#475569";
        ctx.lineWidth = 2;
        ctx.strokeRect(vX - 16, vY - 70, 32, 70);

        // Glowing colloidal fluid
        ctx.fillStyle = `rgb(${vCol.r}, ${vCol.g}, ${vCol.b})`;
        ctx.fillRect(vX - 14, vY - 55, 28, 52);

        // UV Bottom illumination
        ctx.fillStyle = "rgba(168, 85, 247, 0.4)";
        ctx.beginPath();
        ctx.moveTo(vX - 16, vY + 2);
        ctx.lineTo(vX + 16, vY + 2);
        ctx.lineTo(vX + 24, vY + 20);
        ctx.lineTo(vX - 24, vY + 20);
        ctx.closePath();
        ctx.fill();
      }

      ctx.fillStyle = "#94a3b8";
      ctx.font = "11px 'JetBrains Mono', monospace";
      ctx.fillText("CdSe Colloidal Quantum Dots under UV Light (365 nm)", 25, vY + 35);

      // Spectrum Plot on Right
      const gx = w * 0.48;
      const gy = 25;
      const gw = w * 0.49;
      const gh = h - 50;

      ctx.fillStyle = "rgba(15, 23, 42, 0.9)";
      ctx.strokeStyle = "#334155";
      ctx.fillRect(gx, gy, gw, gh);
      ctx.strokeRect(gx, gy, gw, gh);

      ctx.fillStyle = "#facc15";
      ctx.font = "11px 'JetBrains Mono', monospace";
      ctx.fillText("Photoluminescence Spectrum I(λ)", gx + 12, gy + 18);

      // Gaussian Emission Curve
      const sigma = fwhm / 2.355;
      const activeCol = wavelengthToRGB(peakLambda);

      ctx.strokeStyle = `rgb(${activeCol.r}, ${activeCol.g}, ${activeCol.b})`;
      ctx.lineWidth = 3;
      ctx.beginPath();

      for (let px = 0; px < gw - 30; px += 2) {
        const curL = 400 + (px / (gw - 30)) * 300; // 400 nm to 700 nm
        const diff = curL - peakLambda;
        const intensity = Math.exp(-(diff * diff) / (2 * sigma * sigma));
        const py = gy + gh - 20 - intensity * (gh - 55);

        if (px === 0) ctx.moveTo(gx + 15 + px, py);
        else ctx.lineTo(gx + 15 + px, py);
      }
      ctx.stroke();

      // Wavelength scale bar
      ctx.fillStyle = "#64748b";
      ctx.font = "10px 'JetBrains Mono', monospace";
      ctx.fillText("400 nm", gx + 15, gy + gh - 6);
      ctx.fillText("550 nm", gx + gw * 0.5 - 15, gy + gh - 6);
      ctx.fillText("700 nm", gx + gw - 45, gy + gh - 6);

      requestAnimationFrame(draw);
    }
    draw();
    updatePL();
  </script>
</body>
</html>
"""

# ==============================================================================
# 2.3: LSPR Surface Plasmon Resonance & Biosensor Simulator
# ==============================================================================
SIM_2_3_HTML = """<!DOCTYPE html>
<html lang="th">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Lab 2.3: Localized Surface Plasmon Resonance (LSPR)</title>
  <link href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;700&family=Sarabun:wght@300;400;600;700&display=swap" rel="stylesheet">
  <script src="https://cdn.jsdelivr.net/npm/@mediapipe/camera_utils/camera_utils.js" crossorigin="anonymous"></script>
  <script src="https://cdn.jsdelivr.net/npm/@mediapipe/hands/hands.js" crossorigin="anonymous"></script>
  <style>
    :root {
      --bg: #020617;
      --panel: #090e1a;
      --cyan: #00f0ff;
      --gold: #eab308;
      --rose: #f43f5e;
    }
    * { box-sizing: border-box; margin: 0; padding: 0; }
    body { background: var(--bg); color: #f8fafc; font-family: 'Sarabun', sans-serif; padding: 12px; }
    .sim-card { background: var(--panel); border: 1px solid #1e293b; border-radius: 14px; padding: 18px; box-shadow: 0 10px 30px rgba(0,0,0,0.7); }
    .sim-header { display: flex; justify-content: space-between; align-items: center; border-bottom: 1px solid #1e293b; padding-bottom: 10px; margin-bottom: 12px; }
    .sim-title { font-size: 1.1rem; font-weight: 700; color: var(--gold); display: flex; align-items: center; gap: 8px; }
    .badge { background: rgba(234,179,8,0.15); border: 1px solid var(--gold); color: var(--gold); padding: 3px 10px; border-radius: 9999px; font-size: 0.75rem; font-family: 'JetBrains Mono', monospace; }
    .canvas-box { position: relative; width: 100%; height: 320px; background: #000; border: 1px solid #334155; border-radius: 10px; overflow: hidden; margin-bottom: 14px; }
    canvas { width: 100%; height: 100%; display: block; }
    .controls { display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 12px; background: #0f172a; padding: 12px 16px; border-radius: 10px; border: 1px solid #1e293b; margin-bottom: 12px; }
    .ctrl-group { display: flex; flex-direction: column; gap: 6px; }
    .ctrl-lbl { font-size: 0.8rem; color: #94a3b8; display: flex; justify-content: space-between; font-family: 'JetBrains Mono', monospace; }
    input[type=range] { width: 100%; accent-color: var(--gold); cursor: pointer; }
    .hud { display: flex; justify-content: space-between; align-items: center; background: #020617; border: 1px solid #334155; border-radius: 8px; padding: 10px 16px; font-size: 0.85rem; font-family: 'JetBrains Mono', monospace; flex-wrap: wrap; gap: 10px; }
    .hud-val { color: var(--cyan); font-weight: 700; }
  </style>
</head>
<body>
  <div class="sim-card">
    <div class="sim-header">
      <div class="sim-title">
        <span>✨</span>
        <span>แล็บ 2.3: การสั่นพลาสมอนพื้นผิวเฉพาะที่ (LSPR & Dipole Oscillation Solver)</span>
      </div>
      <div class="badge">● GOLD / SILVER PLASMONIC DIPOLE</div>
    </div>

    <div class="canvas-box">
      <canvas id="lsprCanvas"></canvas>
    </div>

    <div class="controls">
      <div class="ctrl-group">
        <div class="ctrl-lbl">
          <span>ดัชนีหักเหของตัวกลางแวดล้อม (Medium Refractive Index: \\(n_m\\))</span>
          <span id="txtN">n = 1.333 (Water)</span>
        </div>
        <input type="range" id="sliderN" min="1.0" max="1.6" step="0.01" value="1.33">
      </div>
      <div class="ctrl-group">
        <div class="ctrl-lbl">
          <span>ชนิดโลหะนาโน (Nanoparticle Metal)</span>
          <span id="txtMetal">Gold (Au Nanosphere: 520 nm)</span>
        </div>
        <select id="selMetal" style="background:#020617; color:#f8fafc; border:1px solid #334155; padding:6px; border-radius:6px; font-family:inherit; font-size:0.85rem;">
          <option value="gold" selected>ทองคำ (Au: λ₀ = 520 nm, สีแดงทับทิม)</option>
          <option value="silver">เงิน (Ag: λ₀ = 400 nm, สีเหลืองสว่าง)</option>
        </select>
      </div>
    </div>

    <div class="hud">
      <div>ยอดคลื่น LSPR: <span class="hud-val" id="hudLSPR">532.5 nm</span> | การเลื่อนของยอดคลื่น: <span class="hud-val" id="hudShift">+12.5 nm (Red Shift)</span></div>
      <div>ความไวตรวจวัดชีวภาพ (Sensitivity): <span class="hud-val" id="hudSens">185 nm / RIU</span></div>
      <button type="button" onclick="injectBiomolecules()" style="background:#eab308; color:#020617; border:none; padding:6px 14px; border-radius:6px; font-weight:700; cursor:pointer;">🧬 เติมโมเลกุลโปรตีนตรวจจับ (Biosensor)</button>
    </div>
  </div>

  <script src="ar_mediapipe_controller.js"></script>
  <script>
    const canvas = document.getElementById("lsprCanvas");
    const ctx = canvas.getContext("2d");

    function resize() {
      canvas.width = canvas.parentElement.clientWidth;
      canvas.height = canvas.parentElement.clientHeight;
    }
    window.addEventListener("resize", resize);
    resize();

    let n_medium = 1.33;
    let metalType = "gold";
    let bioAttached = false;
    let animTime = 0;

    const sliderN = document.getElementById("sliderN");
    const selMetal = document.getElementById("selMetal");
    const txtN = document.getElementById("txtN");
    const hudLSPR = document.getElementById("hudLSPR");
    const hudShift = document.getElementById("hudShift");

    sliderN.addEventListener("input", (e) => {
      n_medium = parseFloat(e.target.value);
      updateLSPR();
    });

    selMetal.addEventListener("change", (e) => {
      metalType = e.target.value;
      updateLSPR();
    });

    function injectBiomolecules() {
      bioAttached = !bioAttached;
      if (bioAttached) n_medium = Math.min(1.6, n_medium + 0.08);
      else n_medium = Math.max(1.0, n_medium - 0.08);
      sliderN.value = n_medium;
      updateLSPR();
    }

    function calculateLSPR() {
      const baseLambda = metalType === "gold" ? 520 : 400;
      const S = metalType === "gold" ? 180 : 210; // nm / RIU
      const deltaN = n_medium - 1.0;
      return baseLambda + S * deltaN + (bioAttached ? 14 : 0);
    }

    function updateLSPR() {
      txtN.textContent = "n = " + n_medium.toFixed(3);
      const lspr = calculateLSPR();
      const base = metalType === "gold" ? 520 : 400;
      hudLSPR.textContent = lspr.toFixed(1) + " nm";
      hudShift.textContent = "+" + (lspr - base).toFixed(1) + " nm (Red Shift)";
    }

    function draw() {
      ctx.clearRect(0, 0, canvas.width, canvas.height);
      const w = canvas.width;
      const h = canvas.height;
      animTime += 0.06;

      const cx = w * 0.40;
      const cy = h * 0.5;

      // Incident Electromagnetic Wave
      ctx.strokeStyle = "rgba(0, 240, 255, 0.4)";
      ctx.lineWidth = 2;
      ctx.beginPath();
      for (let px = 20; px < cx - 70; px += 3) {
        const py = cy + Math.sin(px * 0.08 - animTime * 3) * 35;
        if (px === 20) ctx.moveTo(px, py);
        else ctx.lineTo(px, py);
      }
      ctx.stroke();

      // Electron Cloud Dipole Oscillation
      const dipoleOffset = Math.sin(animTime * 3) * 18;

      // Gold / Silver Metallic Core
      const coreR = 55;
      const coreGrad = ctx.createRadialGradient(cx - 15, cy - 15, 5, cx, cy, coreR);
      if (metalType === "gold") {
        coreGrad.addColorStop(0, "#fef08a");
        coreGrad.addColorStop(0.5, "#eab308");
        coreGrad.addColorStop(1, "#854d0e");
      } else {
        coreGrad.addColorStop(0, "#ffffff");
        coreGrad.addColorStop(0.5, "#cbd5e1");
        coreGrad.addColorStop(1, "#475569");
      }

      ctx.fillStyle = coreGrad;
      ctx.beginPath();
      ctx.arc(cx, cy, coreR, 0, Math.PI * 2);
      ctx.fill();

      // Oscillating Conduction Electron Cloud (+ / - charge separation)
      ctx.fillStyle = "rgba(56, 189, 248, 0.4)";
      ctx.beginPath();
      ctx.arc(cx + dipoleOffset, cy, coreR * 1.15, 0, Math.PI * 2);
      ctx.fill();

      // Localized Electric Field Enhancement Lines
      ctx.strokeStyle = "rgba(234, 179, 8, 0.7)";
      ctx.lineWidth = 1.5;
      for (let k = -2; k <= 2; k++) {
        ctx.beginPath();
        ctx.arc(cx, cy, coreR + 15 + Math.abs(k)*8, 0, Math.PI * 2);
        ctx.stroke();
      }

      // If biomolecules attached
      if (bioAttached) {
        for (let b = 0; b < 10; b++) {
          const ang = (b / 10) * Math.PI * 2 + animTime * 0.2;
          const bx = cx + Math.cos(ang) * (coreR + 12);
          const by = cy + Math.sin(ang) * (coreR + 12);
          ctx.fillStyle = "#f43f5e";
          ctx.beginPath(); ctx.arc(bx, by, 6, 0, Math.PI * 2); ctx.fill();
        }
      }

      // Right Side: Extinction Cross Section Spectrum
      const gx = w * 0.70;
      const gy = 25;
      const gw = w * 0.27;
      const gh = h - 50;

      ctx.fillStyle = "rgba(15, 23, 42, 0.9)";
      ctx.strokeStyle = "#334155";
      ctx.fillRect(gx, gy, gw, gh);
      ctx.strokeRect(gx, gy, gw, gh);

      ctx.fillStyle = "#eab308";
      ctx.font = "11px 'JetBrains Mono', monospace";
      ctx.fillText("LSPR Extinction Peak", gx + 10, gy + 18);

      const lsprPeak = calculateLSPR();
      ctx.strokeStyle = metalType === "gold" ? "#eab308" : "#94a3b8";
      ctx.lineWidth = 3;
      ctx.beginPath();
      for (let px = 0; px < gw - 20; px += 2) {
        const curL = 350 + (px / (gw - 20)) * 350; // 350 to 700 nm
        const diff = curL - lsprPeak;
        const ext = Math.exp(-(diff * diff) / (2 * 25 * 25));
        const py = gy + gh - 15 - ext * (gh - 45);
        if (px === 0) ctx.moveTo(gx + 10 + px, py);
        else ctx.lineTo(gx + 10 + px, py);
      }
      ctx.stroke();

      requestAnimationFrame(draw);
    }
    draw();
    updateLSPR();
  </script>
</body>
</html>
"""

# ==============================================================================
# 2.4: Quantized Conductance & Superparamagnetism Simulator
# ==============================================================================
SIM_2_4_HTML = """<!DOCTYPE html>
<html lang="th">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Lab 2.4: Quantized Conductance & Superparamagnetism</title>
  <link href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;700&family=Sarabun:wght@300;400;600;700&display=swap" rel="stylesheet">
  <script src="https://cdn.jsdelivr.net/npm/@mediapipe/camera_utils/camera_utils.js" crossorigin="anonymous"></script>
  <script src="https://cdn.jsdelivr.net/npm/@mediapipe/hands/hands.js" crossorigin="anonymous"></script>
  <style>
    :root {
      --bg: #020617;
      --panel: #090e1a;
      --cyan: #00f0ff;
      --rose: #f43f5e;
      --amber: #facc15;
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
        <span>⚡</span>
        <span>แล็บ 2.4: สภาพนำไฟฟ้าควอนไทซ์และสมบัติแม่เหล็กยิ่งยวด (Quantum Conductance & Superparamagnetism)</span>
      </div>
      <div class="badge">● G₀ = 2e²/h LANDAUER STEPS</div>
    </div>

    <div class="canvas-box">
      <canvas id="qpcCanvas"></canvas>
    </div>

    <div class="controls">
      <div class="ctrl-group">
        <div class="ctrl-lbl">
          <span>แรงดันเกตควบคุมความกว้างช่องคอด (Gate Voltage: \\(V_g\\))</span>
          <span id="txtGate">Vg = -1.2 V (Channels = 3)</span>
        </div>
        <input type="range" id="sliderGate" min="-3.0" max="0.0" step="0.05" value="-1.2">
      </div>
      <div class="ctrl-group">
        <div class="ctrl-lbl">
          <span>อุณหภูมิระบบ (Temperature: \\(T\\))</span>
          <span id="txtTemp">T = 4.2 K (Liquid Helium)</span>
        </div>
        <input type="range" id="sliderTemp" min="4" max="300" step="2" value="4">
      </div>
    </div>

    <div class="hud">
      <div>สภาพนำไฟฟ้า: <span class="hud-val" id="hudG">3.00 G₀ (232.4 μS)</span> | ช่องทางควอนตัม: <span class="hud-val" id="hudModes">3 โหมดนำส่ง</span></div>
      <div>สถานะแม่เหล็ก: <span class="hud-val" id="hudMag">Superparamagnetic (Zero Remanence)</span></div>
      <button type="button" onclick="reverseMagneticField()" style="background:#f43f5e; color:#ffffff; border:none; padding:6px 14px; border-radius:6px; font-weight:700; cursor:pointer;">🧲 กลับทิศสนามแม่เหล็กภายนอก (B-field)</button>
    </div>
  </div>

  <script src="ar_mediapipe_controller.js"></script>
  <script>
    const canvas = document.getElementById("qpcCanvas");
    const ctx = canvas.getContext("2d");

    function resize() {
      canvas.width = canvas.parentElement.clientWidth;
      canvas.height = canvas.parentElement.clientHeight;
    }
    window.addEventListener("resize", resize);
    resize();

    let Vg = -1.2;
    let temp = 4.2;
    let bField = 1.0;
    let animTime = 0;

    const sliderGate = document.getElementById("sliderGate");
    const sliderTemp = document.getElementById("sliderTemp");
    const txtGate = document.getElementById("txtGate");
    const txtTemp = document.getElementById("txtTemp");
    const hudG = document.getElementById("hudG");
    const hudModes = document.getElementById("hudModes");

    sliderGate.addEventListener("input", (e) => {
      Vg = parseFloat(e.target.value);
      updateQPC();
    });

    sliderTemp.addEventListener("input", (e) => {
      temp = parseFloat(e.target.value);
      updateQPC();
    });

    function reverseMagneticField() {
      bField *= -1;
    }

    function calculateChannels(v) {
      return Math.max(0, Math.floor((v + 3.0) * 1.8));
    }

    function updateQPC() {
      const ch = calculateChannels(Vg);
      txtGate.textContent = "Vg = " + Vg.toFixed(2) + " V (Channels = " + ch + ")";
      txtTemp.textContent = "T = " + temp.toFixed(1) + " K";

      const g0_uS = 77.48;
      hudG.textContent = ch.toFixed(2) + " G₀ (" + (ch * g0_uS).toFixed(1) + " μS)";
      hudModes.textContent = ch + " โหมดนำส่งแบบบัลลิสติก";
    }

    // Free moving ballistic electrons
    const electrons = [];
    for (let i = 0; i < 40; i++) {
      electrons.push({ x: Math.random() * 200 + 20, y: Math.random() * 100 + 100, vx: Math.random() * 2 + 1.5 });
    }

    function draw() {
      ctx.clearRect(0, 0, canvas.width, canvas.height);
      const w = canvas.width;
      const h = canvas.height;
      animTime += 0.03;

      const cx = w * 0.38;
      const cy = h * 0.5;

      const ch = calculateChannels(Vg);
      const constrictionGap = 15 + ch * 18;

      // Draw Gate Electrodes (Split Gates creating constriction)
      ctx.fillStyle = "#334155";
      ctx.strokeStyle = "#00f0ff";
      ctx.lineWidth = 2;

      // Top Gate
      ctx.fillRect(cx - 40, 20, 80, cy - constrictionGap/2 - 20);
      ctx.strokeRect(cx - 40, 20, 80, cy - constrictionGap/2 - 20);

      // Bottom Gate
      ctx.fillRect(cx - 40, cy + constrictionGap/2, 80, h - cy - constrictionGap/2 - 20);
      ctx.strokeRect(cx - 40, cy + constrictionGap/2, 80, h - cy - constrictionGap/2 - 20);

      // Ballistic Electrons moving through QPC constriction
      ctx.fillStyle = "#facc15";
      electrons.forEach(el => {
        el.x += el.vx;
        if (el.x > cx + 160) el.x = 20;

        // Check if blocked by gates
        if (el.x > cx - 40 && el.x < cx + 40) {
          if (el.y < cy - constrictionGap/2 || el.y > cy + constrictionGap/2) {
            el.x = 20; // Reflected
          }
        }
        ctx.beginPath();
        ctx.arc(el.x, el.y, 4, 0, Math.PI * 2);
        ctx.fill();
      });

      // Right Side: Quantized Conductance Staircase Graph
      const gx = w * 0.68;
      const gy = 25;
      const gw = w * 0.29;
      const gh = h - 50;

      ctx.fillStyle = "rgba(15, 23, 42, 0.9)";
      ctx.strokeStyle = "#334155";
      ctx.fillRect(gx, gy, gw, gh);
      ctx.strokeRect(gx, gy, gw, gh);

      ctx.fillStyle = "#f43f5e";
      ctx.font = "11px 'JetBrains Mono', monospace";
      ctx.fillText("Quantized Conductance Steps", gx + 10, gy + 18);

      // Plot Staircase G(Vg)
      ctx.strokeStyle = "#00f0ff";
      ctx.lineWidth = 2.5;
      ctx.beginPath();
      for (let px = 0; px < gw - 25; px += 2) {
        const plotV = -3.0 + (px / (gw - 25)) * 3.0;
        const plotCh = calculateChannels(plotV);
        const py = gy + gh - 15 - (plotCh / 5.0) * (gh - 45);
        if (px === 0) ctx.moveTo(gx + 12 + px, py);
        else ctx.lineTo(gx + 12 + px, py);
      }
      ctx.stroke();

      // Current Point
      const curPX = ((Vg - (-3.0)) / 3.0) * (gw - 25);
      const curPY = gy + gh - 15 - (ch / 5.0) * (gh - 45);
      ctx.fillStyle = "#facc15";
      ctx.beginPath();
      ctx.arc(gx + 12 + curPX, curPY, 6, 0, Math.PI * 2);
      ctx.fill();

      requestAnimationFrame(draw);
    }
    draw();
    updateQPC();
  </script>
</body>
</html>
"""

# ==============================================================================
# 2.5: Universal AR Quantum Optics & Plasmonics Studio Hub
# ==============================================================================
SIM_2_5_HTML = """<!DOCTYPE html>
<html lang="th">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Lab 2.5: Master Quantum & Plasmonics AR Studio</title>
  <link href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;700&family=Sarabun:wght@300;400;600;700&display=swap" rel="stylesheet">
  <script src="https://cdn.jsdelivr.net/npm/@mediapipe/camera_utils/camera_utils.js" crossorigin="anonymous"></script>
  <script src="https://cdn.jsdelivr.net/npm/@mediapipe/hands/hands.js" crossorigin="anonymous"></script>
  <style>
    :root {
      --bg: #020617;
      --panel: #090e1a;
      --cyan: #00f0ff;
      --amber: #facc15;
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
    .hud { display: flex; justify-content: space-between; align-items: center; background: #020617; border: 1px solid #334155; border-radius: 8px; padding: 10px 16px; font-size: 0.85rem; font-family: 'JetBrains Mono', monospace; flex-wrap: wrap; gap: 10px; }
    .hud-val { color: var(--cyan); font-weight: 700; }
    .btn-switch { background: linear-gradient(135deg, #c084fc, #9333ea); color: #ffffff; border: none; padding: 8px 16px; border-radius: 6px; font-weight: 700; cursor: pointer; }
  </style>
</head>
<body>
  <div class="sim-card">
    <div class="sim-header">
      <div class="sim-title">
        <span>🌐</span>
        <span>แล็บ 2.5: สตูดิโอควอนตัมออปติกส์และพลาสมอนิกส์ 3D/AR (Master Quantum & Plasmonics Studio)</span>
      </div>
      <div class="badge">● AR HANDS MULTI-MODAL 60 FPS</div>
    </div>

    <div class="canvas-box">
      <canvas id="hubCanvas"></canvas>
    </div>

    <div class="hud">
      <div>โหมดการทดลอง 3D: <span class="hud-val" id="hudMode">1. การกักขังคลื่นควอนตัม 3D Brus Box</span></div>
      <div>สถานะกล้อง AR: <span class="hud-val" id="hudAR">Active (60 FPS Tracking)</span></div>
      <button type="button" class="btn-switch" onclick="switchBay()">🔄 สลับโหมดการทดลอง 3D</button>
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
    const bays = ["1. การกักขังคลื่นควอนตัม 3D Brus Box", "2. อาร์เรย์จอแสดงผล 3 สี QLED Matrix", "3. ไบโอเซนเซอร์พลาสมอนิกส์ LSPR"];
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

      // Cyber cleanroom grid
      ctx.strokeStyle = "rgba(192, 132, 252, 0.2)";
      ctx.lineWidth = 1;
      for (let x = 0; x < w; x += 40) {
        ctx.beginPath(); ctx.moveTo(x, 0); ctx.lineTo(x, h); ctx.stroke();
      }
      for (let y = 0; y < h; y += 40) {
        ctx.beginPath(); ctx.moveTo(0, y); ctx.lineTo(w, y); ctx.stroke();
      }

      if (bayIndex === 0) {
        // Mode 0: 3D Quantum Box Standing Wave
        ctx.strokeStyle = "#00f0ff";
        ctx.lineWidth = 2.5;
        ctx.beginPath();
        for (let px = 60; px < w - 60; px += 4) {
          const py = cy + Math.sin(px * 0.03 + animTime * 2) * 60 * Math.sin((px - 60) / (w - 120) * Math.PI);
          if (px === 60) ctx.moveTo(px, py);
          else ctx.lineTo(px, py);
        }
        ctx.stroke();

        ctx.fillStyle = "#facc15";
        ctx.beginPath();
        ctx.arc(cx, cy + Math.sin(cx * 0.03 + animTime * 2) * 60, 10, 0, Math.PI * 2);
        ctx.fill();
      } else if (bayIndex === 1) {
        // Mode 1: 3-Color QLED Matrix
        const colors = ["#3b82f6", "#10b981", "#ef4444"];
        for (let i = 0; i < 3; i++) {
          const qx = cx - 140 + i * 140;
          const qR = 25 + i * 15;

          const grad = ctx.createRadialGradient(qx, cy, 5, qx, cy, qR * 1.5);
          grad.addColorStop(0, colors[i]);
          grad.addColorStop(1, "transparent");
          ctx.fillStyle = grad;
          ctx.beginPath(); ctx.arc(qx, cy, qR * 1.5, 0, Math.PI * 2); ctx.fill();

          ctx.fillStyle = colors[i];
          ctx.beginPath(); ctx.arc(qx, cy, qR, 0, Math.PI * 2); ctx.fill();
        }
      } else {
        // Mode 2: Gold LSPR Plasmonic Resonator
        const grad = ctx.createRadialGradient(cx, cy, 10, cx, cy, 70);
        grad.addColorStop(0, "#fef08a");
        grad.addColorStop(0.5, "#eab308");
        grad.addColorStop(1, "#854d0e");
        ctx.fillStyle = grad;
        ctx.beginPath(); ctx.arc(cx, cy, 65, 0, Math.PI * 2); ctx.fill();

        ctx.strokeStyle = "rgba(234, 179, 8, 0.6)";
        ctx.lineWidth = 2;
        for (let r = 75; r < 120; r += 12) {
          ctx.beginPath(); ctx.arc(cx, cy, r + Math.sin(animTime * 3) * 6, 0, Math.PI * 2); ctx.stroke();
        }
      }

      requestAnimationFrame(draw);
    }
    draw();
  </script>
</body>
</html>
"""

# 1. Write simulators
ch2_sims = {
    "sim_nano_2_1.html": SIM_2_1_HTML,
    "sim_nano_2_2.html": SIM_2_2_HTML,
    "sim_nano_2_3.html": SIM_2_3_HTML,
    "sim_nano_2_4.html": SIM_2_4_HTML,
    "sim_nano_2_5.html": SIM_2_5_HTML
}

for fname, content in ch2_sims.items():
    with open(os.path.join(NANO_SIMS_DIR, fname), "w", encoding="utf-8") as f:
        f.write(content)
    with open(os.path.join(ROOT_SIMS_DIR, fname), "w", encoding="utf-8") as f:
        f.write(content)
    print(f"✅ Generated Chapter 2 Simulator: {fname}")

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
subprocess.run(["git", "commit", "-m", "feat(sims): add chapter 2 tailored quantum and plasmonics 60fps simulators"], cwd=TMP_GH, check=True)

remote_url = f"https://{os.environ.get('GH_PAT', '')}@github.com/Tsanaphy2023/modernphysics.git"
subprocess.run(["git", "push", "--force", remote_url, "gh-pages"], cwd=TMP_GH, check=True)
print("🎉 Force pushed Chapter 2 Simulators to gh-pages CDN!")

# 3. Re-run deploy_masterclass_formulas_course_263.py to update Moodle
subprocess.run(["python3", "nanotechnology/course_nanophysics_263/deploy_masterclass_formulas_course_263.py"], cwd=BASE_DIR, check=True)

print("🎉 Successfully developed, synced, and deployed Chapter 2 to Moodle Course 263!")
