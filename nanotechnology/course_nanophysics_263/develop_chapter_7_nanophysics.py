#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Develops Chapter 7 for Nanotechnological Physics (Course 263):
- Generates 5 Tailored 60 FPS Simulators with AR MediaPipe Integration:
  7.1: Nanoparticle Inhalation Dose & ROS Generation Kinetics
  7.2: ISO 14644 Cleanroom Laminar Airflow & Hierarchy of Controls
  7.3: Ecotoxicology Food Web Biomagnification & Bioconcentration (BCF)
  7.4: Research Ethics & FMEA 5x5 Risk Priority Number (RPN) Matrix
  7.5: Master Cleanroom Safety Audit & Spillage Response Studio
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
# 7.1: Inhalation Dose & ROS Kinetics Simulator
# ==============================================================================
SIM_7_1_HTML = """<!DOCTYPE html>
<html lang="th">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Lab 7.1: Inhalation Dose & ROS Kinetics</title>
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
        <span>⚠️</span>
        <span>แล็บ 7.1: ปริมาณการสูดดมและอนุมูลอิสระ ROS ของอนุภาคนาโน (Inhalation Dose & ROS Kinetics)</span>
      </div>
      <div class="badge">● ALVEOLAR DEPOSITION & OXIDATIVE STRESS</div>
    </div>

    <div class="canvas-box">
      <canvas id="toxCanvas"></canvas>
    </div>

    <div class="controls">
      <div class="ctrl-group">
        <div class="ctrl-lbl">
          <span>ขนาดอนุภาคนาโนละอองลอย (Aerosol Size: \(d\))</span>
          <span id="txtD">d = 20 nm (Deep Alveolar Deposition)</span>
        </div>
        <input type="range" id="sliderD" min="5" max="100" step="1" value="20">
      </div>
      <div class="ctrl-group">
        <div class="ctrl-lbl">
          <span>ความเข้มข้นในบรรยากาศ (Air Concentration: \(C_{nano}\))</span>
          <span id="txtC">Cnano = 15 μg/m³</span>
        </div>
        <input type="range" id="sliderC" min="1" max="50" step="1" value="15">
      </div>
    </div>

    <div class="hud">
      <div>อัตราการตกสะสมในถุงลมปอด: <span class="hud-val" id="hudDep">52.4% (Deep Lung)</span> | ดัชนีการสร้าง ROS: <span class="hud-val" id="hudROS">สูง (High Oxidative Risk)</span></div>
      <div>ระดับความมีชีวิตของเซลล์ (MTT Viability): <span class="hud-val" id="hudMTT">78.5% (Mild Cytotoxicity)</span></div>
      <button type="button" onclick="addAntioxidant()" style="background:#f43f5e; color:#ffffff; border:none; padding:6px 14px; border-radius:6px; font-weight:700; cursor:pointer;">⚡ เติมสารต้านอนุมูลอิสระ (Glutathione Detox)</button>
    </div>
  </div>

  <script src="ar_mediapipe_controller.js"></script>
  <script>
    const canvas = document.getElementById("toxCanvas");
    const ctx = canvas.getContext("2d");

    function resize() {
      canvas.width = canvas.parentElement.clientWidth;
      canvas.height = canvas.parentElement.clientHeight;
    }
    window.addEventListener("resize", resize);
    resize();

    let d_nm = 20;
    let conc_ug = 15;
    let detoxActive = false;
    let animTime = 0;

    const sliderD = document.getElementById("sliderD");
    const sliderC = document.getElementById("sliderC");
    const txtD = document.getElementById("txtD");
    const txtC = document.getElementById("txtC");
    const hudDep = document.getElementById("hudDep");
    const hudROS = document.getElementById("hudROS");
    const hudMTT = document.getElementById("hudMTT");

    sliderD.addEventListener("input", (e) => {
      d_nm = parseFloat(e.target.value);
      updateTox();
    });

    sliderC.addEventListener("input", (e) => {
      conc_ug = parseFloat(e.target.value);
      updateTox();
    });

    function addAntioxidant() {
      detoxActive = true;
      setTimeout(() => { detoxActive = false; }, 3000);
    }

    function updateTox() {
      txtD.textContent = "d = " + d_nm.toFixed(0) + " nm (" + (d_nm <= 30 ? "Deep Alveolar Penetration" : "Tracheobronchial Trapping") + ")";
      txtC.textContent = "Cnano = " + conc_ug.toFixed(0) + " μg/m³";
      const depEff = Math.max(10, 60 - Math.abs(d_nm - 20) * 0.6);
      hudDep.textContent = depEff.toFixed(1) + "% (Deep Lung)";
      const rosIndex = (conc_ug * (100 / d_nm));
      hudROS.textContent = rosIndex > 50 ? "สูงมาก (Severe ROS Stress)" : "ปานกลาง (Moderate ROS)";
      const mtt = Math.max(20, 100 - (rosIndex * 0.3));
      hudMTT.textContent = mtt.toFixed(1) + "% (" + (mtt > 80 ? "Low Toxicity" : "Cytotoxic") + ")";
    }

    function draw() {
      ctx.clearRect(0, 0, canvas.width, canvas.height);
      const w = canvas.width;
      const h = canvas.height;
      animTime += 0.03;

      const simW = w * 0.50;
      const cy = h * 0.5;

      // 3D Alveolar Sac Model Box
      ctx.fillStyle = "#020617";
      ctx.strokeStyle = "#334155";
      ctx.lineWidth = 2;
      ctx.fillRect(15, 15, simW - 15, h - 30);
      ctx.strokeRect(15, 15, simW - 15, h - 30);

      // Alveolar Spherical Cap (Tissue membrane)
      ctx.fillStyle = "rgba(244, 63, 94, 0.2)";
      ctx.strokeStyle = "#f43f5e";
      ctx.lineWidth = 2;
      ctx.beginPath();
      ctx.arc(simW * 0.5, cy, 75, 0, Math.PI * 2);
      ctx.fill();
      ctx.stroke();

      ctx.fillStyle = "#ffffff";
      ctx.font = "11px 'JetBrains Mono', monospace";
      ctx.fillText("Alveolar Macrophage & Capillary Wall", 30, 35);

      // Inhaled nanoparticles entering alveolar sac
      const pColor = detoxActive ? "#10b981" : "#f43f5e";
      ctx.fillStyle = pColor;
      for (let p = 0; p < 16; p++) {
        const ang = (p / 16) * Math.PI * 2 + animTime;
        const rad = 20 + ((p * 15 + animTime * 40) % 50);
        const px = (simW * 0.5) + Math.cos(ang) * rad;
        const py = cy + Math.sin(ang) * rad;
        ctx.beginPath(); ctx.arc(px, py, Math.max(2.5, d_nm * 0.06), 0, Math.PI * 2); ctx.fill();
      }

      // Right Side: Dose-Response Cell Viability Curve MTT
      const gx = w * 0.53;
      const gy = 15;
      const gw = w * 0.45;
      const gh = h - 30;

      ctx.fillStyle = "rgba(15, 23, 42, 0.9)";
      ctx.strokeStyle = "#334155";
      ctx.fillRect(gx, gy, gw, gh);
      ctx.strokeRect(gx, gy, gw, gh);

      ctx.fillStyle = "#f43f5e";
      ctx.font = "11px 'JetBrains Mono', monospace";
      ctx.fillText("MTT Cytotoxicity Curve: Viability vs Dose", gx + 10, gy + 18);

      // Plot Sigmoidal Dose-Response curve
      ctx.strokeStyle = "#00f0ff";
      ctx.lineWidth = 2.5;
      ctx.beginPath();
      const originX = gx + 25;
      const originY = gy + gh - 35;
      const plotW = gw - 50;
      const plotH = gh - 65;

      ctx.moveTo(originX, originY - plotH);
      for (let vx = 0; vx <= plotW; vx += 2) {
        const dose = (vx / plotW) * 50;
        const viability = 100 / (1 + Math.exp((dose - 25) / 6));
        const py = originY - (viability / 100.0) * plotH;
        ctx.lineTo(originX + vx, py);
      }
      ctx.stroke();

      // Current Dose marker
      const curX = originX + (conc_ug / 50.0) * plotW;
      const curV = 100 / (1 + Math.exp((conc_ug - 25) / 6));
      const curY = originY - (curV / 100.0) * plotH;

      ctx.fillStyle = "#facc15";
      ctx.beginPath(); ctx.arc(curX, curY, 6, 0, Math.PI * 2); ctx.fill();
      ctx.fillText(curV.toFixed(0) + "% Viability", curX - 35, curY - 12);

      requestAnimationFrame(draw);
    }
    draw();
    updateTox();
  </script>
</body>
</html>
"""

# ==============================================================================
# 7.2: Cleanroom Laminar Airflow & Safety Controls Simulator
# ==============================================================================
SIM_7_2_HTML = """<!DOCTYPE html>
<html lang="th">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Lab 7.2: ISO Cleanroom Laminar Flow & Hierarchy of Controls</title>
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
        <span>🛡️</span>
        <span>แล็บ 7.2: การไหลเวียนอากาศคลีนรูมและการควบคุมความเสี่ยง (ISO Cleanroom & Hierarchy of Controls)</span>
      </div>
      <div class="badge">● ISO 14644-1 CLASS 5 LAMINAR FLOW</div>
    </div>

    <div class="canvas-box">
      <canvas id="cleanCanvas"></canvas>
    </div>

    <div class="controls">
      <div class="ctrl-group">
        <div class="ctrl-lbl">
          <span>ความเร็วลมตู้ดูดควัน (Face Airflow Velocity: \(v\))</span>
          <span id="txtV">v = 0.50 m/s (Standard Safe Face Velocity)</span>
        </div>
        <input type="range" id="sliderV" min="0.2" max="1.0" step="0.05" value="0.5">
      </div>
      <div class="ctrl-group">
        <div class="ctrl-lbl">
          <span>ระดับชั้นความสะอาดห้องคลีนรูม (ISO Cleanroom Class)</span>
          <span id="txtClass">ISO Class 5 (Class 100: Max 3,520 particles/m³)</span>
        </div>
        <select id="selClass" style="background:#020617; color:#f8fafc; border:1px solid #334155; padding:6px; border-radius:6px; font-family:inherit; font-size:0.85rem;">
          <option value="4">ISO Class 4 (Class 10: Semiconductor Fab)</option>
          <option value="5" selected>ISO Class 5 (Class 100: Nanotech Synthesis)</option>
          <option value="7">ISO Class 7 (Class 10,000: General Nano Lab)</option>
        </select>
      </div>
    </div>

    <div class="hud">
      <div>ประสิทธิภาพแผ่นกรอง HEPA: <span class="hud-val" id="hudHEPA">99.999% (@ 0.1 μm ULPA)</span> | การเปิดรับสัมผัส OEL: <span class="hud-val" id="hudOEL">< 1.0 μg/m³ (Safe)</span></div>
      <div>สถานะความเสี่ยง (Risk Status): <span class="hud-val" id="hudRisk">🟢 ควบคุมได้สมบูรณ์ (Fully Controlled)</span></div>
      <button type="button" onclick="testSpillProtection()" style="background:#10b981; color:#020617; border:none; padding:6px 14px; border-radius:6px; font-weight:700; cursor:pointer;">⚡ ทดสอบระบบดูดระบายฉุกเฉิน (Emergency Exhaust)</button>
    </div>
  </div>

  <script src="ar_mediapipe_controller.js"></script>
  <script>
    const canvas = document.getElementById("cleanCanvas");
    const ctx = canvas.getContext("2d");

    function resize() {
      canvas.width = canvas.parentElement.clientWidth;
      canvas.height = canvas.parentElement.clientHeight;
    }
    window.addEventListener("resize", resize);
    resize();

    let faceV = 0.50;
    let isoClass = 5;
    let animTime = 0;

    const sliderV = document.getElementById("sliderV");
    const selClass = document.getElementById("selClass");
    const txtV = document.getElementById("txtV");
    const txtClass = document.getElementById("txtClass");
    const hudRisk = document.getElementById("hudRisk");

    sliderV.addEventListener("input", (e) => {
      faceV = parseFloat(e.target.value);
      updateClean();
    });

    selClass.addEventListener("change", (e) => {
      isoClass = parseInt(e.target.value);
      updateClean();
    });

    function testSpillProtection() {
      faceV = 0.85; sliderV.value = faceV;
      updateClean();
    }

    function updateClean() {
      txtV.textContent = "v = " + faceV.toFixed(2) + " m/s (" + (faceV >= 0.4 && faceV <= 0.6 ? "Standard Safe Face Velocity" : faceV < 0.4 ? "Airflow Too Low (Hazard!)" : "Turbulent Flow") + ")";
      txtClass.textContent = "ISO Class " + isoClass;
      if (faceV >= 0.4 && faceV <= 0.7) {
        hudRisk.textContent = "🟢 ควบคุมได้สมบูรณ์ (Safe Laminar Flow)";
      } else {
        hudRisk.textContent = "🔴 เสี่ยงต่อการรั่วไหล (Adjust Velocity!)";
      }
    }

    function draw() {
      ctx.clearRect(0, 0, canvas.width, canvas.height);
      const w = canvas.width;
      const h = canvas.height;
      animTime += 0.03;

      const simW = w * 0.55;

      // 3D Cleanroom Fume Hood Viewport
      ctx.fillStyle = "#020617";
      ctx.strokeStyle = "#334155";
      ctx.lineWidth = 2;
      ctx.fillRect(15, 15, simW - 15, h - 30);
      ctx.strokeRect(15, 15, simW - 15, h - 30);

      // Top HEPA / ULPA Filter Plenum
      ctx.fillStyle = "rgba(16, 185, 129, 0.4)";
      ctx.fillRect(30, 25, simW - 50, 25);
      ctx.strokeStyle = "#10b981"; ctx.strokeRect(30, 25, simW - 50, 25);
      ctx.fillStyle = "#ffffff"; ctx.font = "11px 'JetBrains Mono', monospace"; ctx.fillText("ULPA Filter Ceiling (99.999% Efficiency)", 40, 42);

      // Laminar Air Streamlines (Green arrows flowing downwards)
      ctx.strokeStyle = "rgba(0, 240, 255, 0.4)";
      ctx.lineWidth = 1.5;
      for (let x = 45; x < simW - 45; x += 30) {
        ctx.beginPath();
        ctx.moveTo(x, 50);
        ctx.lineTo(x, h - 50);
        ctx.stroke();

        // Moving air particles
        const py = 50 + ((animTime * (faceV * 180) + x * 2) % (h - 100));
        ctx.fillStyle = "#00f0ff";
        ctx.beginPath(); ctx.arc(x, py, 3, 0, Math.PI * 2); ctx.fill();
      }

      // Workbench surface (Bottom)
      ctx.fillStyle = "#334155";
      ctx.fillRect(30, h - 45, simW - 50, 15);

      // Right Side: Hierarchy of Controls Inverted Pyramid
      const gx = w * 0.58;
      const gy = 25;
      const gw = w * 0.39;
      const gh = h - 50;

      ctx.fillStyle = "rgba(15, 23, 42, 0.9)";
      ctx.strokeStyle = "#334155";
      ctx.fillRect(gx, gy, gw, gh);
      ctx.strokeRect(gx, gy, gw, gh);

      ctx.fillStyle = "#10b981";
      ctx.font = "11px 'JetBrains Mono', monospace";
      ctx.fillText("Hierarchy of Controls (NIOSH)", gx + 10, gy + 18);

      const levels = [
        { name: "1. Elimination (กำจัด)", col: "#10b981" },
        { name: "2. Substitution (ทดแทน)", col: "#38bdf8" },
        { name: "3. Engineering (ตู้ดูดควัน)", col: "#facc15" },
        { name: "4. Administrative (SOP)", col: "#fb923c" },
        { name: "5. PPE (หน้ากาก N100)", col: "#f43f5e" }
      ];

      levels.forEach((lvl, idx) => {
        const ly = gy + 32 + idx * 36;
        const lw = gw - 30 - idx * 16;
        ctx.fillStyle = lvl.col;
        ctx.fillRect(gx + 15 + idx * 8, ly, lw, 24);
        ctx.fillStyle = "#020617";
        ctx.font = "10px 'Sarabun', sans-serif";
        ctx.fillText(lvl.name, gx + 25 + idx * 8, ly + 16);
      });

      requestAnimationFrame(draw);
    }
    draw();
    updateClean();
  </script>
</body>
</html>
"""

# ==============================================================================
# 7.3: Ecotoxicology & Food Web BCF Simulator
# ==============================================================================
SIM_7_3_HTML = """<!DOCTYPE html>
<html lang="th">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Lab 7.3: Ecotoxicology & Food Web Biomagnification</title>
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
        <span>🐟</span>
        <span>แล็บ 7.3: การสะสมในห่วงโซ่อาหารและแฟกเตอร์ BCF (Ecotoxicology & BCF Solver)</span>
      </div>
      <div class="badge">● BIOMAGNIFICATION & AQUATIC RISK</div>
    </div>

    <div class="canvas-box">
      <canvas id="ecoCanvas"></canvas>
    </div>

    <div class="controls">
      <div class="ctrl-group">
        <div class="ctrl-lbl">
          <span>ความเข้มข้นสารนาโนในแหล่งน้ำ (Water Concentration: \(C_{water}\))</span>
          <span id="txtCw">Cwater = 2.5 mg/L (AgNPs / TiO2)</span>
        </div>
        <input type="range" id="sliderCw" min="0.1" max="10.0" step="0.1" value="2.5">
      </div>
      <div class="ctrl-group">
        <div class="ctrl-lbl">
          <span>แฟกเตอร์การสะสมทางชีวภาพ (Bioconcentration Factor: \(BCF\))</span>
          <span id="txtBCF">BCF = 1,450 L/kg</span>
        </div>
        <input type="range" id="sliderBCF" min="200" max="5000" step="50" value="1450">
      </div>
    </div>

    <div class="hud">
      <div>ความเข้มข้นในเนื้อเยื่อปลา (Cbiota): <span class="hud-val" id="hudBio">3,625 mg/kg</span> | อัตราส่วนความเสี่ยง (Risk Quotient RQ): <span class="hud-val" id="hudRQ">2.45 (High Ecotox Risk)</span></div>
      <div>การบำบัดของเสีย: <span class="hud-val" id="hudTreat">Coagulation + Membrane Active</span></div>
      <button type="button" onclick="activateFlocculation()" style="background:#00f0ff; color:#020617; border:none; padding:6px 14px; border-radius:6px; font-weight:700; cursor:pointer;">⚡ กระตุ้นการตกตะกอนสารแขวนลอยนาโน (Flocculation)</button>
    </div>
  </div>

  <script src="ar_mediapipe_controller.js"></script>
  <script>
    const canvas = document.getElementById("ecoCanvas");
    const ctx = canvas.getContext("2d");

    function resize() {
      canvas.width = canvas.parentElement.clientWidth;
      canvas.height = canvas.parentElement.clientHeight;
    }
    window.addEventListener("resize", resize);
    resize();

    let C_water = 2.5;
    let BCF = 1450;
    let animTime = 0;

    const sliderCw = document.getElementById("sliderCw");
    const sliderBCF = document.getElementById("sliderBCF");
    const txtCw = document.getElementById("txtCw");
    const txtBCF = document.getElementById("txtBCF");
    const hudBio = document.getElementById("hudBio");
    const hudRQ = document.getElementById("hudRQ");

    sliderCw.addEventListener("input", (e) => {
      C_water = parseFloat(e.target.value);
      updateEco();
    });

    sliderBCF.addEventListener("input", (e) => {
      BCF = parseFloat(e.target.value);
      updateEco();
    });

    function activateFlocculation() {
      C_water = 0.2; sliderCw.value = C_water;
      updateEco();
    }

    function updateEco() {
      txtCw.textContent = "Cwater = " + C_water.toFixed(1) + " mg/L";
      txtBCF.textContent = "BCF = " + BCF.toFixed(0) + " L/kg";
      const cBiota = C_water * BCF;
      hudBio.textContent = cBiota.toFixed(0) + " mg/kg";
      const rq = (C_water / 1.0);
      hudRQ.textContent = rq.toFixed(2) + " (" + (rq > 1.0 ? "High Ecotox Risk" : "Acceptable") + ")";
    }

    function draw() {
      ctx.clearRect(0, 0, canvas.width, canvas.height);
      const w = canvas.width;
      const h = canvas.height;
      animTime += 0.03;

      const simW = w * 0.55;
      const cy = h * 0.5;

      // Aquatic Food Chain Ecosystem
      ctx.fillStyle = "#020617";
      ctx.strokeStyle = "#334155";
      ctx.lineWidth = 2;
      ctx.fillRect(15, 15, simW - 15, h - 30);
      ctx.strokeRect(15, 15, simW - 15, h - 30);

      // Water body
      ctx.fillStyle = "rgba(0, 240, 255, 0.15)";
      ctx.fillRect(25, 25, simW - 35, h - 50);

      // Trophic level 1: Algae (Green circles)
      ctx.fillStyle = "#10b981";
      for (let a = 0; a < 6; a++) {
        const ax = 40 + a * 30;
        const ay = cy + 40 + Math.sin(animTime + a) * 10;
        ctx.beginPath(); ctx.arc(ax, ay, 6, 0, Math.PI * 2); ctx.fill();
      }
      ctx.fillStyle = "#ffffff"; ctx.font = "10px 'JetBrains Mono', monospace"; ctx.fillText("1. Algae (Primary Producer)", 30, h - 25);

      // Trophic level 2: Daphnia / Zooplankton (Yellow)
      ctx.fillStyle = "#facc15";
      for (let d = 0; d < 4; d++) {
        const dx = 50 + d * 55;
        const dy = cy - 10 + Math.sin(animTime * 1.5 + d) * 12;
        ctx.beginPath(); ctx.arc(dx, dy, 10, 0, Math.PI * 2); ctx.fill();
      }

      // Trophic level 3: Fish (Cyan Top Predator with biomagnified dots)
      ctx.fillStyle = "rgba(56, 189, 248, 0.6)";
      ctx.beginPath();
      ctx.ellipse(simW * 0.6, cy - 45, 45, 22, 0, 0, Math.PI * 2);
      ctx.fill();
      ctx.fillStyle = "#f43f5e";
      // accumulated nanoparticles in fish tissue
      for (let np = 0; np < 8; np++) {
        const nx = (simW * 0.6) - 20 + np * 5;
        const ny = cy - 45 + (np % 3) * 4;
        ctx.beginPath(); ctx.arc(nx, ny, 3, 0, Math.PI * 2); ctx.fill();
      }

      // Right Side: Biomagnification Trophic Level Bar Chart
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
      ctx.fillText("Trophic Level Accumulation", gx + 10, gy + 18);

      const trophics = [
        { name: "Water (น้ำ)", val: C_water * 10, col: "#00f0ff" },
        { name: "Algae (สาหร่าย)", val: C_water * 35, col: "#10b981" },
        { name: "Daphnia (ไรน้ำ)", val: C_water * 80, col: "#facc15" },
        { name: "Fish (ปลา)", val: C_water * 150, col: "#f43f5e" }
      ];

      trophics.forEach((tr, idx) => {
        const by = gy + 40 + idx * 45;
        ctx.fillStyle = "#94a3b8"; ctx.font = "10px 'Sarabun', sans-serif"; ctx.fillText(tr.name, gx + 15, by + 12);
        ctx.fillStyle = tr.col;
        ctx.fillRect(gx + 110, by, Math.min(gw - 130, tr.val), 18);
      });

      requestAnimationFrame(draw);
    }
    draw();
    updateEco();
  </script>
</body>
</html>
"""

# ==============================================================================
# 7.4: Research Ethics & FMEA Risk Priority Matrix Simulator
# ==============================================================================
SIM_7_4_HTML = """<!DOCTYPE html>
<html lang="th">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Lab 7.4: Research Ethics & FMEA Risk Matrix</title>
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
    .sim-title { font-size: 1.1rem; font-weight: 700; color: var(--purple); display: flex; align-items: center; gap: 8px; }
    .badge { background: rgba(192,132,252,0.15); border: 1px solid var(--purple); color: var(--purple); padding: 3px 10px; border-radius: 9999px; font-size: 0.75rem; font-family: 'JetBrains Mono', monospace; }
    .canvas-box { position: relative; width: 100%; height: 320px; background: #000; border: 1px solid #334155; border-radius: 10px; overflow: hidden; margin-bottom: 14px; }
    canvas { width: 100%; height: 100%; display: block; }
    .controls { display: grid; grid-template-columns: repeat(auto-fit, minmax(180px, 1fr)); gap: 12px; background: #0f172a; padding: 12px 16px; border-radius: 10px; border: 1px solid #1e293b; margin-bottom: 12px; }
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
        <span>⚖️</span>
        <span>แล็บ 7.4: จริยธรรมการวิจัยและเมทริกซ์ความเสี่ยง FMEA (Ethics & RPN Matrix)</span>
      </div>
      <div class="badge">● RPN = S × O × D & FAIR DATA</div>
    </div>

    <div class="canvas-box">
      <canvas id="fmeaCanvas"></canvas>
    </div>

    <div class="controls">
      <div class="ctrl-group">
        <div class="ctrl-lbl">
          <span>ความรุนแรงผลกระทบ (Severity: \(S\))</span>
          <span id="txtS">S = 8 / 10</span>
        </div>
        <input type="range" id="sliderS" min="1" max="10" step="1" value="8">
      </div>
      <div class="ctrl-group">
        <div class="ctrl-lbl">
          <span>โอกาสเกิดเหตุการณ์ (Occurrence: \(O\))</span>
          <span id="txtO">O = 3 / 10</span>
        </div>
        <input type="range" id="sliderO" min="1" max="10" step="1" value="3">
      </div>
      <div class="ctrl-group">
        <div class="ctrl-lbl">
          <span>ความยากในการตรวจจับ (Detection: \(D\))</span>
          <span id="txtD">D = 4 / 10</span>
        </div>
        <input type="range" id="sliderD" min="1" max="10" step="1" value="4">
      </div>
    </div>

    <div class="hud">
      <div>คะแนนลำดับความสำคัญของความเสี่ยง (RPN): <span class="hud-val" id="hudRPN">96 / 1000 (Medium Risk)</span> | ความโปร่งใสของข้อมูล: <span class="hud-val" id="hudData">100% FAIR Principles</span></div>
      <div>ระดับการกำกับดูแล: <span class="hud-val" id="hudGov">OECD & REACH Compliant</span></div>
      <button type="button" onclick="mitigateRisk()" style="background:#c084fc; color:#020617; border:none; padding:6px 14px; border-radius:6px; font-weight:700; cursor:pointer;">⚡ นำมาตรการ Safety-by-Design มาใช้</button>
    </div>
  </div>

  <script src="ar_mediapipe_controller.js"></script>
  <script>
    const canvas = document.getElementById("fmeaCanvas");
    const ctx = canvas.getContext("2d");

    function resize() {
      canvas.width = canvas.parentElement.clientWidth;
      canvas.height = canvas.parentElement.clientHeight;
    }
    window.addEventListener("resize", resize);
    resize();

    let S = 8, O = 3, D = 4;

    const sliderS = document.getElementById("sliderS");
    const sliderO = document.getElementById("sliderO");
    const sliderD = document.getElementById("sliderD");
    const txtS = document.getElementById("txtS");
    const txtO = document.getElementById("txtO");
    const txtD = document.getElementById("txtD");
    const hudRPN = document.getElementById("hudRPN");

    sliderS.addEventListener("input", (e) => { S = parseInt(e.target.value); updateFMEA(); });
    sliderO.addEventListener("input", (e) => { O = parseInt(e.target.value); updateFMEA(); });
    sliderD.addEventListener("input", (e) => { D = parseInt(e.target.value); updateFMEA(); });

    function mitigateRisk() {
      O = 1; D = 2;
      sliderO.value = O; sliderD.value = D;
      updateFMEA();
    }

    function updateFMEA() {
      txtS.textContent = "S = " + S + " / 10";
      txtO.textContent = "O = " + O + " / 10";
      txtD.textContent = "D = " + D + " / 10";
      const rpn = S * O * D;
      let level = rpn > 200 ? "High Risk (Action Required)" : rpn > 80 ? "Medium Risk (Acceptable with Controls)" : "Low Risk (Safe)";
      hudRPN.textContent = rpn + " / 1000 (" + level + ")";
    }

    function draw() {
      ctx.clearRect(0, 0, canvas.width, canvas.height);
      const w = canvas.width;
      const h = canvas.height;

      const simW = w * 0.50;
      const cy = h * 0.5;

      // 5x5 FMEA Risk Heatmap Matrix
      ctx.fillStyle = "#020617";
      ctx.strokeStyle = "#334155";
      ctx.lineWidth = 2;
      ctx.fillRect(15, 15, simW - 15, h - 30);
      ctx.strokeRect(15, 15, simW - 15, h - 30);

      const gridN = 5;
      const cellW = (simW - 50) / gridN;
      const cellH = (h - 60) / gridN;

      for (let r = 0; r < gridN; r++) {
        for (let c = 0; c < gridN; c++) {
          const x = 30 + c * cellW;
          const y = 30 + r * cellH;
          const score = (5 - r) * (c + 1);

          ctx.fillStyle = score > 15 ? "rgba(244, 63, 94, 0.6)" : score > 8 ? "rgba(250, 204, 21, 0.5)" : "rgba(16, 185, 129, 0.5)";
          ctx.fillRect(x, y, cellW - 2, cellH - 2);
        }
      }

      // Mark current S & O coordinate
      const curCol = Math.min(4, Math.floor((O - 1) / 2));
      const curRow = Math.min(4, 4 - Math.floor((S - 1) / 2));
      const mx = 30 + curCol * cellW + cellW * 0.5;
      const my = 30 + curRow * cellH + cellH * 0.5;

      ctx.fillStyle = "#ffffff";
      ctx.strokeStyle = "#020617";
      ctx.lineWidth = 3;
      ctx.beginPath(); ctx.arc(mx, my, 9, 0, Math.PI * 2); ctx.fill(); ctx.stroke();

      // Right Side: FAIR Data Principles Card
      const gx = w * 0.53;
      const gy = 15;
      const gw = w * 0.45;
      const gh = h - 30;

      ctx.fillStyle = "rgba(15, 23, 42, 0.9)";
      ctx.strokeStyle = "#334155";
      ctx.fillRect(gx, gy, gw, gh);
      ctx.strokeRect(gx, gy, gw, gh);

      ctx.fillStyle = "#c084fc";
      ctx.font = "11px 'JetBrains Mono', monospace";
      ctx.fillText("FAIR Principles in Nanotechnology", gx + 10, gy + 18);

      const fair = [
        "F - Findable (ค้นหาและระบุตัวตนได้ด้วย DOI)",
        "A - Accessible (เข้าถึงได้ตามมาตรฐานเปิด)",
        "I - Interoperable (แลกเปลี่ยนข้อมูลเชิงโครงสร้าง)",
        "R - Reusable (ทำซ้ำได้และมีใบอนุญาตชัดเจน)"
      ];

      fair.forEach((item, idx) => {
        ctx.fillStyle = "#ffffff";
        ctx.font = "11px 'Sarabun', sans-serif";
        ctx.fillText("✅ " + item, gx + 15, gy + 55 + idx * 35);
      });

      requestAnimationFrame(draw);
    }
    draw();
    updateFMEA();
  </script>
</body>
</html>
"""

# ==============================================================================
# 7.5: Master Cleanroom Safety Audit & Spillage Studio
# ==============================================================================
SIM_7_5_HTML = """<!DOCTYPE html>
<html lang="th">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Lab 7.5: Master Cleanroom Safety Audit Studio</title>
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
        <span>แล็บ 7.5: สตูดิโอตรวจสอบความปลอดภัยและเหตุฉุกเฉินสารนาโน (Master Safety Studio)</span>
      </div>
      <div class="badge">● AR HANDS MULTI-MODAL 60 FPS</div>
    </div>

    <div class="canvas-box">
      <canvas id="hubCanvas"></canvas>
    </div>

    <div class="hud">
      <div>โหมดการตรวจสอบความปลอดภัย 3D: <span class="hud-val" id="hudMode">1. แผนตอบโต้เหตุสารนาโนหกรั่วไหล (Spill Kit Response)</span></div>
      <div>สถานะกล้อง AR: <span class="hud-val" id="hudAR">Active (60 FPS Tracking)</span></div>
      <button type="button" class="btn-switch" onclick="switchBay()">🔄 สลับโหมดความปลอดภัย 3D</button>
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
    const bays = [
      "1. แผนตอบโต้เหตุสารนาโนหกรั่วไหล (Spill Kit Response)",
      "2. การตรวจสอบแรงดันและอัตราไหลตู้ดูดควัน (Fume Hood Audit)",
      "3. สถานีบำบัดของเสียและทำลายฤทธิ์สารนาโน (Neutralization Bay)"
    ];
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
        // Mode 0: Spill Area Containment
        ctx.fillStyle = "rgba(244, 63, 94, 0.3)";
        ctx.beginPath(); ctx.ellipse(cx, cy, 100, 45, 0, 0, Math.PI * 2); ctx.fill();
        ctx.strokeStyle = "#f43f5e"; ctx.stroke();

        // Absorbent barrier rings
        ctx.strokeStyle = "#facc15"; ctx.lineWidth = 3;
        ctx.beginPath(); ctx.ellipse(cx, cy, 120, 55, 0, 0, Math.PI * 2); ctx.stroke();
        ctx.fillStyle = "#facc15"; ctx.font = "12px 'JetBrains Mono', monospace"; ctx.fillText("Chemical Absorbent Boom Barrier", cx - 110, cy - 65);
      } else if (bayIndex === 1) {
        // Mode 1: Fume Hood Velocity Meter
        ctx.strokeStyle = "#10b981"; ctx.lineWidth = 3;
        ctx.strokeRect(cx - 100, cy - 40, 200, 80);
      } else {
        // Mode 2: Neutralization Waste Drum
        ctx.fillStyle = "#38bdf8"; ctx.fillRect(cx - 50, cy - 40, 100, 80);
      }

      requestAnimationFrame(draw);
    }
    draw();
  </script>
</body>
</html>
"""

# 1. Write simulators
ch7_sims = {
    "sim_nano_7_1.html": SIM_7_1_HTML,
    "sim_nano_7_2.html": SIM_7_2_HTML,
    "sim_nano_7_3.html": SIM_7_3_HTML,
    "sim_nano_7_4.html": SIM_7_4_HTML,
    "sim_nano_7_5.html": SIM_7_5_HTML
}

for fname, content in ch7_sims.items():
    with open(os.path.join(NANO_SIMS_DIR, fname), "w", encoding="utf-8") as f:
        f.write(content)
    with open(os.path.join(ROOT_SIMS_DIR, fname), "w", encoding="utf-8") as f:
        f.write(content)
    print(f"✅ Generated Chapter 7 Simulator: {fname}")

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
subprocess.run(["git", "commit", "-m", "feat(sims): add chapter 7 safety, ecotox, and ethics 60fps simulators"], cwd=TMP_GH, check=True)

remote_url = f"https://{os.environ.get('GH_PAT', '')}@github.com/Tsanaphy2023/modernphysics.git"
subprocess.run(["git", "push", "--force", remote_url, "gh-pages"], cwd=TMP_GH, check=True)
print("🎉 Force pushed Chapter 7 Simulators to gh-pages CDN!")

# 3. Re-run deploy_masterclass_formulas_course_263.py to update Moodle
subprocess.run(["python3", "nanotechnology/course_nanophysics_263/deploy_masterclass_formulas_course_263.py"], cwd=BASE_DIR, check=True)

print("🎉 Successfully developed, synced, and deployed Chapter 7 to Moodle Course 263!")
