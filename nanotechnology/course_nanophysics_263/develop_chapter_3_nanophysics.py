#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Develops Chapter 3 for Nanotechnological Physics (Course 263):
- Generates 5 Tailored 60 FPS Simulators with AR MediaPipe Integration:
  3.1: Top-Down vs Bottom-Up Nanofabrication Pathways
  3.2: Sol-Gel Hydrolysis & Network Gelation Kinetics
  3.3: CVD & PVD Thin Film Growth & Graphene Synthesis
  3.4: Extreme UV & E-Beam Nanolithography Resolution Simulator
  3.5: Universal AR Nanomaterials Synthesis & LaMer Nucleation Studio
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
# 3.1: Top-Down vs Bottom-Up Synthesis Pathways Simulator
# ==============================================================================
SIM_3_1_HTML = """<!DOCTYPE html>
<html lang="th">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Lab 3.1: Top-Down vs Bottom-Up Synthesis</title>
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
    .hud-val { color: var(--cyan); font-weight: 700; }
  </style>
</head>
<body>
  <div class="sim-card">
    <div class="sim-header">
      <div class="sim-title">
        <span>🏭</span>
        <span>แล็บ 3.1: การสังเคราะห์แบบบนลงล่าง vs ล่างขึ้นบน (Top-Down vs Bottom-Up Synthesis)</span>
      </div>
      <div class="badge">● DUAL PATHWAY ENGINE</div>
    </div>

    <div class="canvas-box">
      <canvas id="synCanvas"></canvas>
    </div>

    <div class="controls">
      <div class="ctrl-group">
        <div class="ctrl-lbl">
          <span>แนวทางการสังเคราะห์ (Synthesis Methodology)</span>
          <span id="txtMode">Bottom-Up (Chemical Self-Assembly)</span>
        </div>
        <select id="selMode" style="background:#020617; color:#f8fafc; border:1px solid #334155; padding:6px; border-radius:6px; font-family:inherit; font-size:0.85rem;">
          <option value="bottomup" selected>1. ล่างขึ้นบน (Bottom-Up: การก่อผลึกนิวคลีเอชันจากสารตั้งต้น)</option>
          <option value="topdown">2. บนลงล่าง (Top-Down: การบดลดขนาดเชิงกล Ball Milling)</option>
        </select>
      </div>
      <div class="ctrl-group">
        <div class="ctrl-lbl">
          <span>อัตราความเร็วการทำปฏิกิริยา (Reaction Rate / Energy Input)</span>
          <span id="txtRate">Speed = 1.0x</span>
        </div>
        <input type="range" id="sliderRate" min="0.2" max="3.0" step="0.1" value="1.0">
      </div>
    </div>

    <div class="hud">
      <div>ขนาดผลึกเฉลี่ย: <span class="hud-val" id="hudSize">8.4 ± 0.6 nm</span> | ความสม่ำเสมอ (PDI): <span class="hud-val" id="hudPDI">0.08 (Monodisperse)</span></div>
      <div>การควบคุมโครงสร้าง: <span class="hud-val" id="hudControl">ความแม่นยำระดับอะตอม (Atomic Precision)</span></div>
      <button type="button" onclick="resetSynthesis()" style="background:#10b981; color:#020617; border:none; padding:6px 14px; border-radius:6px; font-weight:700; cursor:pointer;">↺ เริ่มต้นรอบการสังเคราะห์ใหม่</button>
    </div>
  </div>

  <script src="ar_mediapipe_controller.js"></script>
  <script>
    const canvas = document.getElementById("synCanvas");
    const ctx = canvas.getContext("2d");

    function resize() {
      canvas.width = canvas.parentElement.clientWidth;
      canvas.height = canvas.parentElement.clientHeight;
    }
    window.addEventListener("resize", resize);
    resize();

    let mode = "bottomup";
    let speed = 1.0;
    let animTime = 0;

    const selMode = document.getElementById("selMode");
    const sliderRate = document.getElementById("sliderRate");
    const txtMode = document.getElementById("txtMode");
    const txtRate = document.getElementById("txtRate");
    const hudSize = document.getElementById("hudSize");
    const hudPDI = document.getElementById("hudPDI");
    const hudControl = document.getElementById("hudControl");

    selMode.addEventListener("change", (e) => {
      mode = e.target.value;
      updateStats();
      resetSynthesis();
    });

    sliderRate.addEventListener("input", (e) => {
      speed = parseFloat(e.target.value);
      txtRate.textContent = "Speed = " + speed.toFixed(1) + "x";
    });

    function updateStats() {
      if (mode === "bottomup") {
        txtMode.textContent = "Bottom-Up (Chemical Self-Assembly)";
        hudSize.textContent = "8.4 ± 0.6 nm";
        hudPDI.textContent = "0.08 (Monodisperse)";
        hudControl.textContent = "ความแม่นยำระดับอะตอม (Atomic Precision)";
      } else {
        txtMode.textContent = "Top-Down (High-Energy Ball Milling)";
        hudSize.textContent = "45.0 ± 22.4 nm";
        hudPDI.textContent = "0.45 (Polydisperse)";
        hudControl.textContent = "ผลึกมีความบกพร่องสูง (Mechanical Defects)";
      }
    }

    let entities = [];
    function resetSynthesis() {
      entities = [];
      if (mode === "bottomup") {
        // Monomers nucleating into nanodots
        for (let i = 0; i < 60; i++) {
          entities.push({ x: Math.random() * 250 + 40, y: Math.random() * 200 + 40, vx: (Math.random() - 0.5) * 2, vy: (Math.random() - 0.5) * 2, r: 4, cluster: false });
        }
      } else {
        // Large bulk grain fracturing
        entities.push({ x: 160, y: 150, r: 50, pieces: [] });
      }
    }
    resetSynthesis();

    function draw() {
      ctx.clearRect(0, 0, canvas.width, canvas.height);
      const w = canvas.width;
      const h = canvas.height;
      animTime += 0.03 * speed;

      const simW = w * 0.65;

      // Solution Chamber / Milling Chamber
      ctx.fillStyle = "#020617";
      ctx.strokeStyle = "#334155";
      ctx.lineWidth = 2;
      ctx.fillRect(15, 15, simW, h - 30);
      ctx.strokeRect(15, 15, simW, h - 30);

      if (mode === "bottomup") {
        // Bottom-Up Chemical Nucleation
        ctx.fillStyle = "#10b981";
        ctx.font = "12px 'JetBrains Mono', monospace";
        ctx.fillText("การรวมตัวจากสารตั้งต้นโมเลกุล (Precursor Nucleation)", 25, 35);

        entities.forEach((e1, i) => {
          e1.x += e1.vx * speed;
          e1.y += e1.vy * speed;
          if (e1.x < 25 || e1.x > simW - 15) e1.vx *= -1;
          if (e1.y < 45 || e1.y > h - 35) e1.vy *= -1;

          // Check nucleation pairing
          for (let j = i + 1; j < entities.length; j++) {
            const e2 = entities[j];
            const dist = Math.hypot(e2.x - e1.x, e2.y - e1.y);
            if (dist < 18 && !e1.cluster && !e2.cluster) {
              e1.cluster = true; e2.cluster = true;
              e1.r = 8;
            }
          }

          ctx.fillStyle = e1.cluster ? "#00f0ff" : "#facc15";
          ctx.beginPath();
          ctx.arc(e1.x, e1.y, e1.r, 0, Math.PI * 2);
          ctx.fill();
        });
      } else {
        // Top-Down Ball Milling Mechanical Shear
        ctx.fillStyle = "#f43f5e";
        ctx.font = "12px 'JetBrains Mono', monospace";
        ctx.fillText("การบดกระแทกเชิงกล (High-Energy Impact Ball)", 25, 35);

        // Grinding balls
        const b1X = 160 + Math.sin(animTime * 4) * 80;
        const b1Y = 150 + Math.cos(animTime * 3) * 60;
        ctx.fillStyle = "#94a3b8";
        ctx.beginPath(); ctx.arc(b1X, b1Y, 24, 0, Math.PI * 2); ctx.fill();

        // Shattered fragments
        for (let k = 0; k < 25; k++) {
          const fx = 160 + Math.sin(k * 1.5 + animTime) * 60;
          const fy = 150 + Math.cos(k * 2.1 + animTime) * 50;
          ctx.fillStyle = "#cbd5e1";
          ctx.fillRect(fx, fy, (k % 4) * 4 + 4, (k % 3) * 4 + 4);
        }
      }

      // Comparison Graph on Right
      const gx = w * 0.68;
      const gy = 25;
      const gw = w * 0.29;
      const gh = h - 50;

      ctx.fillStyle = "rgba(15, 23, 42, 0.9)";
      ctx.strokeStyle = "#334155";
      ctx.fillRect(gx, gy, gw, gh);
      ctx.strokeRect(gx, gy, gw, gh);

      ctx.fillStyle = mode === "bottomup" ? "#10b981" : "#f43f5e";
      ctx.font = "11px 'JetBrains Mono', monospace";
      ctx.fillText("Size Distribution Comparison", gx + 10, gy + 18);

      // Plot Distribution curve
      ctx.strokeStyle = mode === "bottomup" ? "#00f0ff" : "#f43f5e";
      ctx.lineWidth = 2.5;
      ctx.beginPath();
      const peakX = mode === "bottomup" ? 0.45 : 0.60;
      const spread = mode === "bottomup" ? 0.08 : 0.25;

      for (let px = 0; px < gw - 25; px += 2) {
        const xVal = px / (gw - 25);
        const diff = xVal - peakX;
        const curve = Math.exp(-(diff * diff) / (2 * spread * spread));
        const py = gy + gh - 15 - curve * (gh - 45);
        if (px === 0) ctx.moveTo(gx + 12 + px, py);
        else ctx.lineTo(gx + 12 + px, py);
      }
      ctx.stroke();

      requestAnimationFrame(draw);
    }
    draw();
    updateStats();
  </script>
</body>
</html>
"""

# ==============================================================================
# 3.2: Sol-Gel Hydrolysis & Network Gelation Simulator
# ==============================================================================
SIM_3_2_HTML = """<!DOCTYPE html>
<html lang="th">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Lab 3.2: Sol-Gel Hydrolysis & Condensation</title>
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
        <span>🧪</span>
        <span>แล็บ 3.2: กระบวนการโซล-เจลและเครือข่ายซิลิกา 3D (Sol-Gel Hydrolysis & Condensation)</span>
      </div>
      <div class="badge">● TEOS CROSS-LINKING</div>
    </div>

    <div class="canvas-box">
      <canvas id="solgelCanvas"></canvas>
    </div>

    <div class="controls">
      <div class="ctrl-group">
        <div class="ctrl-lbl">
          <span>สัดส่วนน้ำต่อสารตั้งต้น (\\(r = [\\text{H}_2\\text{O}]/[\\text{Si}]\\))</span>
          <span id="txtR">r = 4.0 (Full Hydrolysis)</span>
        </div>
        <input type="range" id="sliderR" min="1.0" max="10.0" step="0.5" value="4.0">
      </div>
      <div class="ctrl-group">
        <div class="ctrl-lbl">
          <span>สภาวะพีเอชตัวเร่งปฏิกิริยา (Catalyst pH Condition)</span>
          <span id="txtPH">pH = 2.0 (Acid Catalyst: Linear Fibers)</span>
        </div>
        <select id="selPH" style="background:#020617; color:#f8fafc; border:1px solid #334155; padding:6px; border-radius:6px; font-family:inherit; font-size:0.85rem;">
          <option value="acid" selected>กรด (pH &lt; 2.5: เกิดเส้นใยสายยาว Polymeric Gel)</option>
          <option value="base">เบส (pH &gt; 8.0: เกิดอนุภาคทรงกลมพรุน Particulate Gel)</option>
        </select>
      </div>
    </div>

    <div class="hud">
      <div>ระดับการควบแน่น: <span class="hud-val" id="hudCross">86.4% Cross-linked</span> | เวลาการเกิดเจล (\\(t_{\\text{gel}}\\)): <span class="hud-val" id="hudTgel">14.2 นาที</span></div>
      <div>โครงสร้างผลิตภัณฑ์: <span class="hud-val" id="hudProduct">3D Monolithic Silica Aerogel</span></div>
      <button type="button" onclick="triggerCondensation()" style="background:#c084fc; color:#020617; border:none; padding:6px 14px; border-radius:6px; font-weight:700; cursor:pointer;">⚡ เร่งปฏิกิริยาควบแน่น (Condensation)</button>
    </div>
  </div>

  <script src="ar_mediapipe_controller.js"></script>
  <script>
    const canvas = document.getElementById("solgelCanvas");
    const ctx = canvas.getContext("2d");

    function resize() {
      canvas.width = canvas.parentElement.clientWidth;
      canvas.height = canvas.parentElement.clientHeight;
    }
    window.addEventListener("resize", resize);
    resize();

    let r_ratio = 4.0;
    let phMode = "acid";
    let gelProgress = 0.5;
    let animTime = 0;

    const sliderR = document.getElementById("sliderR");
    const selPH = document.getElementById("selPH");
    const txtR = document.getElementById("txtR");
    const hudCross = document.getElementById("hudCross");
    const hudTgel = document.getElementById("hudTgel");

    sliderR.addEventListener("input", (e) => {
      r_ratio = parseFloat(e.target.value);
      updateSolGel();
    });

    selPH.addEventListener("change", (e) => {
      phMode = e.target.value;
      updateSolGel();
    });

    function triggerCondensation() {
      gelProgress = Math.min(1.0, gelProgress + 0.2);
      updateSolGel();
    }

    function updateSolGel() {
      txtR.textContent = "r = " + r_ratio.toFixed(1);
      const crossPct = (gelProgress * 95).toFixed(1);
      hudCross.textContent = crossPct + "% Cross-linked";
      const tgel = (30 / (r_ratio * (phMode === "acid" ? 0.8 : 1.5))).toFixed(1);
      hudTgel.textContent = tgel + " นาที";
    }

    // Grid of Si atoms
    const nodes = [];
    const rows = 5, cols = 7;
    for (let r = 0; r < rows; r++) {
      for (let c = 0; c < cols; c++) {
        nodes.push({
          ox: 60 + c * 40,
          oy: 60 + r * 45,
          x: 60 + c * 40,
          y: 60 + r * 45
        });
      }
    }

    function draw() {
      ctx.clearRect(0, 0, canvas.width, canvas.height);
      const w = canvas.width;
      const h = canvas.height;
      animTime += 0.03;

      const simW = w * 0.65;

      // Draw reaction box
      ctx.fillStyle = "#020617";
      ctx.strokeStyle = "#334155";
      ctx.lineWidth = 2;
      ctx.fillRect(15, 15, simW, h - 30);
      ctx.strokeRect(15, 15, simW, h - 30);

      // Animate silica polymer bonds
      nodes.forEach((n, idx) => {
        n.x = n.ox + Math.sin(animTime + idx) * (1 - gelProgress) * 6;
        n.y = n.oy + Math.cos(animTime + idx * 0.7) * (1 - gelProgress) * 6;
      });

      // Draw Si-O-Si bridging bonds
      ctx.strokeStyle = "rgba(0, 240, 255, 0.7)";
      ctx.lineWidth = 2;
      for (let r = 0; r < rows; r++) {
        for (let c = 0; c < cols; c++) {
          const idx = r * cols + c;
          // Right bond
          if (c < cols - 1 && Math.random() < gelProgress + 0.3) {
            ctx.beginPath();
            ctx.moveTo(nodes[idx].x, nodes[idx].y);
            ctx.lineTo(nodes[idx + 1].x, nodes[idx + 1].y);
            ctx.stroke();
          }
          // Down bond
          if (r < rows - 1 && Math.random() < gelProgress + 0.3) {
            ctx.beginPath();
            ctx.moveTo(nodes[idx].x, nodes[idx].y);
            ctx.lineTo(nodes[idx + cols].x, nodes[idx + cols].y);
            ctx.stroke();
          }
        }
      }

      // Draw Silicon (Si) & Oxygen (O) nodes
      nodes.forEach(n => {
        ctx.fillStyle = "#c084fc";
        ctx.beginPath();
        ctx.arc(n.x, n.y, 8, 0, Math.PI * 2);
        ctx.fill();
        ctx.strokeStyle = "#ffffff";
        ctx.stroke();
      });

      // Viscosity Curve on Right
      const gx = w * 0.68;
      const gy = 25;
      const gw = w * 0.29;
      const gh = h - 50;

      ctx.fillStyle = "rgba(15, 23, 42, 0.9)";
      ctx.strokeStyle = "#334155";
      ctx.fillRect(gx, gy, gw, gh);
      ctx.strokeRect(gx, gy, gw, gh);

      ctx.fillStyle = "#c084fc";
      ctx.font = "11px 'JetBrains Mono', monospace";
      ctx.fillText("Viscosity η(t) vs Time", gx + 10, gy + 18);

      // Plot exponential gelation transition
      ctx.strokeStyle = "#facc15";
      ctx.lineWidth = 2.5;
      ctx.beginPath();
      for (let px = 0; px < gw - 25; px += 2) {
        const t = px / (gw - 25);
        const eta = Math.pow(t, 5) * (gh - 45);
        const py = gy + gh - 15 - eta;
        if (px === 0) ctx.moveTo(gx + 12 + px, py);
        else ctx.lineTo(gx + 12 + px, py);
      }
      ctx.stroke();

      requestAnimationFrame(draw);
    }
    draw();
    updateSolGel();
  </script>
</body>
</html>
"""

# ==============================================================================
# 3.3: CVD & PVD Thin Film Growth Kinetics Simulator
# ==============================================================================
SIM_3_3_HTML = """<!DOCTYPE html>
<html lang="th">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Lab 3.3: CVD & PVD Thin Film Growth</title>
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
        <span>🔥</span>
        <span>แล็บ 3.3: การสะสมไอสารเคมีและการปลูกฟิล์มกราฟีน (CVD Reactor & Graphene Growth)</span>
      </div>
      <div class="badge">● ARRHENIUS GROWTH KINETICS</div>
    </div>

    <div class="canvas-box">
      <canvas id="cvdCanvas"></canvas>
    </div>

    <div class="controls">
      <div class="ctrl-group">
        <div class="ctrl-lbl">
          <span>อุณหภูมิเตาปฏิกรณ์ (Reactor Temperature: \\(T\\))</span>
          <span id="txtTemp">T = 1,000 °C (1,273 K)</span>
        </div>
        <input type="range" id="sliderTemp" min="600" max="1100" step="10" value="1000">
      </div>
      <div class="ctrl-group">
        <div class="ctrl-lbl">
          <span>อัตราการไหลของก๊าซมีเทน (CH₄ Flow Rate)</span>
          <span id="txtFlow">Flow = 30 sccm</span>
        </div>
        <input type="range" id="sliderFlow" min="5" max="100" step="5" value="30">
      </div>
    </div>

    <div class="hud">
      <div>อัตราการเติบโต: <span class="hud-val" id="hudRate">1.25 nm/min</span> | ความหนาฟิล์ม: <span class="hud-val" id="hudThick">1 Monolayer (Graphene)</span></div>
      <div>กลไกควบคุม: <span class="hud-val" id="hudRegime">Surface Reaction Limited</span></div>
      <button type="button" onclick="purgeChamber()" style="background:#00f0ff; color:#020617; border:none; padding:6px 14px; border-radius:6px; font-weight:700; cursor:pointer;">💨 ล้างห้องเตา (Ar/H₂ Purge)</button>
    </div>
  </div>

  <script src="ar_mediapipe_controller.js"></script>
  <script>
    const canvas = document.getElementById("cvdCanvas");
    const ctx = canvas.getContext("2d");

    function resize() {
      canvas.width = canvas.parentElement.clientWidth;
      canvas.height = canvas.parentElement.clientHeight;
    }
    window.addEventListener("resize", resize);
    resize();

    let tempC = 1000;
    let flow = 30;
    let filmCoverage = 0.2;
    let animTime = 0;

    const sliderTemp = document.getElementById("sliderTemp");
    const sliderFlow = document.getElementById("sliderFlow");
    const txtTemp = document.getElementById("txtTemp");
    const txtFlow = document.getElementById("txtFlow");
    const hudRate = document.getElementById("hudRate");
    const hudThick = document.getElementById("hudThick");

    sliderTemp.addEventListener("input", (e) => {
      tempC = parseFloat(e.target.value);
      updateCVD();
    });

    sliderFlow.addEventListener("input", (e) => {
      flow = parseFloat(e.target.value);
      updateCVD();
    });

    function purgeChamber() {
      filmCoverage = 0.05;
    }

    function calculateGrowthRate() {
      const T_K = tempC + 273.15;
      const Ea_eV = 1.2;
      const kB_eV = 8.617e-5;
      return 500 * (flow / 30) * Math.exp(-Ea_eV / (kB_eV * T_K));
    }

    function updateCVD() {
      txtTemp.textContent = "T = " + tempC + " °C (" + (tempC + 273) + " K)";
      txtFlow.textContent = "Flow = " + flow + " sccm";
      const rate = calculateGrowthRate();
      hudRate.textContent = rate.toFixed(2) + " nm/min";
      hudThick.textContent = filmCoverage >= 0.9 ? "Full Graphene Monolayer" : (filmCoverage * 100).toFixed(0) + "% Domain Coverage";
    }

    // Gas molecules (CH4 / C atoms)
    const gasAtoms = [];
    for (let i = 0; i < 35; i++) {
      gasAtoms.push({ x: Math.random() * 300 + 40, y: Math.random() * 80 + 30, vx: (Math.random() - 0.5) * 4, vy: Math.random() * 2 + 1 });
    }

    function draw() {
      ctx.clearRect(0, 0, canvas.width, canvas.height);
      const w = canvas.width;
      const h = canvas.height;
      animTime += 0.04;

      const simW = w * 0.65;
      const subY = h - 60;

      filmCoverage = Math.min(1.0, filmCoverage + calculateGrowthRate() * 0.0001);

      // CVD Tube Furnace Glow
      const glowR = Math.min(1.0, (tempC - 600) / 500);
      ctx.fillStyle = `rgba(245, 158, 11, ${0.1 + glowR * 0.25})`;
      ctx.fillRect(15, 15, simW, h - 30);
      ctx.strokeStyle = "#f59e0b";
      ctx.lineWidth = 2;
      ctx.strokeRect(15, 15, simW, h - 30);

      // Gas phase precursor molecules raining down
      ctx.fillStyle = "#38bdf8";
      gasAtoms.forEach(ga => {
        ga.x += ga.vx;
        ga.y += ga.vy;
        if (ga.x < 25 || ga.x > simW - 15) ga.vx *= -1;
        if (ga.y > subY - 10) {
          ga.y = 35;
          ga.x = Math.random() * (simW - 40) + 20;
        }
        ctx.beginPath();
        ctx.arc(ga.x, ga.y, 4, 0, Math.PI * 2);
        ctx.fill();
      });

      // Copper Substrate (Cu foil at bottom)
      ctx.fillStyle = "#b45309";
      ctx.fillRect(20, subY, simW - 10, 30);
      ctx.fillStyle = "#fde68a";
      ctx.font = "11px 'JetBrains Mono', monospace";
      ctx.fillText("Copper Catalyst Substrate (Cu 111)", 30, subY + 20);

      // Growing Graphene Hexagonal Domains on Cu
      ctx.strokeStyle = "#00f0ff";
      ctx.lineWidth = 2;
      const domains = Math.floor(filmCoverage * 12);
      for (let d = 0; d < domains; d++) {
        const dx = 40 + d * 26;
        ctx.beginPath();
        for (let s = 0; s < 6; s++) {
          const ang = (s / 6) * Math.PI * 2;
          const sx = dx + Math.cos(ang) * 12;
          const sy = subY - 8 + Math.sin(ang) * 6;
          if (s === 0) ctx.moveTo(sx, sy);
          else ctx.lineTo(sx, sy);
        }
        ctx.closePath();
        ctx.stroke();
      }

      // Right Side: Arrhenius Rate Graph
      const gx = w * 0.68;
      const gy = 25;
      const gw = w * 0.29;
      const gh = h - 50;

      ctx.fillStyle = "rgba(15, 23, 42, 0.9)";
      ctx.strokeStyle = "#334155";
      ctx.fillRect(gx, gy, gw, gh);
      ctx.strokeRect(gx, gy, gw, gh);

      ctx.fillStyle = "#00f0ff";
      ctx.font = "11px 'JetBrains Mono', monospace";
      ctx.fillText("Arrhenius Growth Rate ln(k)", gx + 10, gy + 18);

      ctx.strokeStyle = "#facc15";
      ctx.lineWidth = 2.5;
      ctx.beginPath();
      for (let px = 0; px < gw - 25; px += 2) {
        const plotT = 600 + (px / (gw - 25)) * 500;
        const T_K = plotT + 273.15;
        const rate = 500 * Math.exp(-1.2 / (8.617e-5 * T_K));
        const py = gy + gh - 15 - (rate / 15.0) * (gh - 45);
        if (px === 0) ctx.moveTo(gx + 12 + px, py);
        else ctx.lineTo(gx + 12 + px, py);
      }
      ctx.stroke();

      requestAnimationFrame(draw);
    }
    draw();
    updateCVD();
  </script>
</body>
</html>
"""

# ==============================================================================
# 3.4: Extreme UV & E-Beam Nanolithography Simulator
# ==============================================================================
SIM_3_4_HTML = """<!DOCTYPE html>
<html lang="th">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Lab 3.4: Extreme UV & E-Beam Nanolithography</title>
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
        <span>🔦</span>
        <span>แล็บ 3.4: นาโนลิโทกราฟีรังสีเอกซ์ตรีมยูวี (EUV & Rayleigh Resolution Solver)</span>
      </div>
      <div class="badge">● R = k₁ λ/NA SOLVER</div>
    </div>

    <div class="canvas-box">
      <canvas id="lithoCanvas"></canvas>
    </div>

    <div class="controls">
      <div class="ctrl-group">
        <div class="ctrl-lbl">
          <span>แหล่งกำเนิดแสง / รังสี (Wavelength: \\(\\lambda\\))</span>
          <span id="txtSource">EUV (13.5 nm)</span>
        </div>
        <select id="selSource" style="background:#020617; color:#f8fafc; border:1px solid #334155; padding:6px; border-radius:6px; font-family:inherit; font-size:0.85rem;">
          <option value="13.5,0.33" selected>Extreme UV (EUV: λ = 13.5 nm, NA = 0.33)</option>
          <option value="13.5,0.55">High-NA EUV (λ = 13.5 nm, NA = 0.55)</option>
          <option value="193,1.35">ArF Immersion (λ = 193 nm, NA = 1.35)</option>
          <option value="0.01,0.02">E-Beam Lithography (λ_e = 0.01 nm)</option>
        </select>
      </div>
      <div class="ctrl-group">
        <div class="ctrl-lbl">
          <span>แฟกเตอร์กระบวนการโฟโต้เรซิสต์ (Process Factor: \\(k_1\\))</span>
          <span id="txtK1">k₁ = 0.30 (Advanced OPC)</span>
        </div>
        <input type="range" id="sliderK1" min="0.25" max="0.60" step="0.01" value="0.30">
      </div>
    </div>

    <div class="hud">
      <div>ความละเอียดขั้นต่ำ (Critical Dimension): <span class="hud-val" id="hudCD">12.3 nm</span></div>
      <div>ระยะลึกโฟกัส (Depth of Focus): <span class="hud-val" id="hudDOF">62.0 nm</span></div>
      <button type="button" onclick="exposeWafer()" style="background:#f43f5e; color:#ffffff; border:none; padding:6px 14px; border-radius:6px; font-weight:700; cursor:pointer;">⚡ ฉายแสงผ่านหน้ากากโฟโตมาสก์ (Expose & Etch)</button>
    </div>
  </div>

  <script src="ar_mediapipe_controller.js"></script>
  <script>
    const canvas = document.getElementById("lithoCanvas");
    const ctx = canvas.getContext("2d");

    function resize() {
      canvas.width = canvas.parentElement.clientWidth;
      canvas.height = canvas.parentElement.clientHeight;
    }
    window.addEventListener("resize", resize);
    resize();

    let lambda_nm = 13.5;
    let NA = 0.33;
    let k1 = 0.30;
    let isExposed = true;
    let animTime = 0;

    const selSource = document.getElementById("selSource");
    const sliderK1 = document.getElementById("sliderK1");
    const txtSource = document.getElementById("txtSource");
    const txtK1 = document.getElementById("txtK1");
    const hudCD = document.getElementById("hudCD");
    const hudDOF = document.getElementById("hudDOF");

    selSource.addEventListener("change", (e) => {
      const parts = e.target.value.split(",");
      lambda_nm = parseFloat(parts[0]);
      NA = parseFloat(parts[1]);
      updateLitho();
    });

    sliderK1.addEventListener("input", (e) => {
      k1 = parseFloat(e.target.value);
      updateLitho();
    });

    function exposeWafer() {
      isExposed = true;
    }

    function calculateCD() {
      return (k1 * lambda_nm) / NA;
    }

    function updateLitho() {
      txtK1.textContent = "k₁ = " + k1.toFixed(2);
      const cd = calculateCD();
      hudCD.textContent = cd.toFixed(1) + " nm (Node Limit)";
      const dof = (0.5 * lambda_nm) / (NA * NA);
      hudDOF.textContent = dof.toFixed(1) + " nm";
    }

    function draw() {
      ctx.clearRect(0, 0, canvas.width, canvas.height);
      const w = canvas.width;
      const h = canvas.height;
      animTime += 0.04;

      const simW = w * 0.65;
      const cd = calculateCD();

      // Draw EUV Light Rays from Top
      ctx.fillStyle = "rgba(244, 63, 94, 0.15)";
      ctx.fillRect(20, 15, simW - 10, 50);

      // Photomask with slits
      ctx.fillStyle = "#334155";
      ctx.fillRect(20, 65, simW - 10, 18);

      const numSlits = 7;
      const slitW = Math.max(6, Math.min(24, cd * 1.2));
      for (let i = 0; i < numSlits; i++) {
        const sx = 45 + i * (slitW + 20);
        ctx.clearRect(sx, 65, slitW, 18);
      }

      // Projected EUV Light Cones through Mask to Wafer
      ctx.fillStyle = "rgba(0, 240, 255, 0.35)";
      for (let i = 0; i < numSlits; i++) {
        const sx = 45 + i * (slitW + 20);
        ctx.beginPath();
        ctx.moveTo(sx, 83);
        ctx.lineTo(sx + slitW, 83);
        ctx.lineTo(sx + slitW * 0.8, h - 70);
        ctx.lineTo(sx + slitW * 0.2, h - 70);
        ctx.closePath();
        ctx.fill();
      }

      // Silicon Wafer with Etched Nanopattern
      const subY = h - 70;
      ctx.fillStyle = "#1e293b";
      ctx.fillRect(20, subY, simW - 10, 50);

      // Etched features
      for (let i = 0; i < numSlits; i++) {
        const sx = 45 + i * (slitW + 20) + slitW * 0.2;
        ctx.fillStyle = "#00f0ff";
        ctx.fillRect(sx, subY, slitW * 0.6, 20);
      }

      ctx.fillStyle = "#facc15";
      ctx.font = "11px 'JetBrains Mono', monospace";
      ctx.fillText("Silicon Wafer (Etched Nanopattern CD = " + cd.toFixed(1) + " nm)", 30, h - 10);

      // Right Side: Rayleigh Resolution Curve
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
      ctx.fillText("CD vs Numerical Aperture (NA)", gx + 8, gy + 18);

      ctx.strokeStyle = "#00f0ff";
      ctx.lineWidth = 2.5;
      ctx.beginPath();
      for (let px = 0; px < gw - 25; px += 2) {
        const plotNA = 0.2 + (px / (gw - 25)) * 0.7;
        const plotCD = (k1 * lambda_nm) / plotNA;
        const py = gy + gh - 15 - Math.min(1, plotCD / 50.0) * (gh - 45);
        if (px === 0) ctx.moveTo(gx + 12 + px, py);
        else ctx.lineTo(gx + 12 + px, py);
      }
      ctx.stroke();

      requestAnimationFrame(draw);
    }
    draw();
    updateLitho();
  </script>
</body>
</html>
"""

# ==============================================================================
# 3.5: Universal AR Nanomaterials Synthesis Studio Hub
# ==============================================================================
SIM_3_5_HTML = """<!DOCTYPE html>
<html lang="th">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Lab 3.5: Master Nanomaterials Synthesis AR Studio</title>
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
    .hud { display: flex; justify-content: space-between; align-items: center; background: #020617; border: 1px solid #334155; border-radius: 8px; padding: 10px 16px; font-size: 0.85rem; font-family: 'JetBrains Mono', monospace; flex-wrap: wrap; gap: 10px; }
    .hud-val { color: var(--cyan); font-weight: 700; }
    .btn-switch { background: linear-gradient(135deg, #10b981, #059669); color: #ffffff; border: none; padding: 8px 16px; border-radius: 6px; font-weight: 700; cursor: pointer; }
  </style>
</head>
<body>
  <div class="sim-card">
    <div class="sim-header">
      <div class="sim-title">
        <span>🌐</span>
        <span>แล็บ 3.5: สตูดิโอการสังเคราะห์และนิวคลีเอชัน LaMer 3D/AR (Master Synthesis Studio)</span>
      </div>
      <div class="badge">● AR HANDS MULTI-MODAL 60 FPS</div>
    </div>

    <div class="canvas-box">
      <canvas id="hubCanvas"></canvas>
    </div>

    <div class="hud">
      <div>โหมดการสังเคราะห์ 3D: <span class="hud-val" id="hudMode">1. ทฤษฎีนิวคลีเอชัน LaMer Burst Model</span></div>
      <div>สถานะกล้อง AR: <span class="hud-val" id="hudAR">Active (60 FPS Hand Tracking)</span></div>
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
    const bays = ["1. ทฤษฎีนิวคลีเอชัน LaMer Burst Model", "2. เตาปฏิกรณ์ปลูกฟิล์ม CVD 3D Chamber", "3. การสร้างลวดลายนาโนลิโทกราฟี EUV"];
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
      ctx.strokeStyle = "rgba(16, 185, 129, 0.2)";
      ctx.lineWidth = 1;
      for (let x = 0; x < w; x += 40) {
        ctx.beginPath(); ctx.moveTo(x, 0); ctx.lineTo(x, h); ctx.stroke();
      }
      for (let y = 0; y < h; y += 40) {
        ctx.beginPath(); ctx.moveTo(0, y); ctx.lineTo(w, y); ctx.stroke();
      }

      if (bayIndex === 0) {
        // Mode 0: LaMer Burst Nucleation Particles
        ctx.fillStyle = "#10b981";
        for (let i = 0; i < 20; i++) {
          const ang = (i / 20) * Math.PI * 2 + animTime;
          const r = 50 + Math.sin(animTime * 2 + i) * 20;
          const px = cx + Math.cos(ang) * r;
          const py = cy + Math.sin(ang) * r * 0.5;
          ctx.beginPath(); ctx.arc(px, py, 6, 0, Math.PI * 2); ctx.fill();
        }
        ctx.fillStyle = "#facc15";
        ctx.beginPath(); ctx.arc(cx, cy, 18, 0, Math.PI * 2); ctx.fill();
      } else if (bayIndex === 1) {
        // Mode 1: CVD Furnace 3D Tube
        ctx.strokeStyle = "#f59e0b";
        ctx.lineWidth = 3;
        ctx.strokeRect(cx - 140, cy - 50, 280, 100);

        ctx.fillStyle = "rgba(245, 158, 11, 0.3)";
        ctx.fillRect(cx - 140, cy - 50, 280, 100);

        ctx.fillStyle = "#00f0ff";
        for (let k = 0; k < 8; k++) {
          const gx = cx - 120 + ((k * 35 + animTime * 60) % 240);
          ctx.beginPath(); ctx.arc(gx, cy, 5, 0, Math.PI * 2); ctx.fill();
        }
      } else {
        // Mode 2: Nanolithography Mask & Beams
        ctx.strokeStyle = "#f43f5e";
        ctx.lineWidth = 2;
        ctx.strokeRect(cx - 100, cy - 70, 200, 20);

        ctx.fillStyle = "rgba(0, 240, 255, 0.4)";
        ctx.fillRect(cx - 70, cy - 50, 140, 90);
      }

      requestAnimationFrame(draw);
    }
    draw();
  </script>
</body>
</html>
"""

# 1. Write simulators
ch3_sims = {
    "sim_nano_3_1.html": SIM_3_1_HTML,
    "sim_nano_3_2.html": SIM_3_2_HTML,
    "sim_nano_3_3.html": SIM_3_3_HTML,
    "sim_nano_3_4.html": SIM_3_4_HTML,
    "sim_nano_3_5.html": SIM_3_5_HTML
}

for fname, content in ch3_sims.items():
    with open(os.path.join(NANO_SIMS_DIR, fname), "w", encoding="utf-8") as f:
        f.write(content)
    with open(os.path.join(ROOT_SIMS_DIR, fname), "w", encoding="utf-8") as f:
        f.write(content)
    print(f"✅ Generated Chapter 3 Simulator: {fname}")

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
subprocess.run(["git", "commit", "-m", "feat(sims): add chapter 3 tailored nanofabrication and cvd 60fps simulators"], cwd=TMP_GH, check=True)

remote_url = f"https://{os.environ.get('GH_PAT', '')}@github.com/Tsanaphy2023/modernphysics.git"
subprocess.run(["git", "push", "--force", remote_url, "gh-pages"], cwd=TMP_GH, check=True)
print("🎉 Force pushed Chapter 3 Simulators to gh-pages CDN!")

# 3. Re-run deploy_masterclass_formulas_course_263.py to update Moodle
subprocess.run(["python3", "nanotechnology/course_nanophysics_263/deploy_masterclass_formulas_course_263.py"], cwd=BASE_DIR, check=True)

print("🎉 Successfully developed, synced, and deployed Chapter 3 to Moodle Course 263!")
