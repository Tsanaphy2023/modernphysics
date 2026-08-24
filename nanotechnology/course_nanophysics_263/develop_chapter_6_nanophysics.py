#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Develops Chapter 6 for Nanotechnological Physics (Course 263):
- Generates 5 Tailored 60 FPS Simulators with AR MediaPipe Integration:
  6.1: Perovskite & Quantum Dot Solar Cell PCE & J-V Curve Solver
  6.2: Supercapacitor & Nano-Battery Energy & Power Density Simulator
  6.3: Nanomedicine Targeted Drug Delivery & EPR Effect in Tumor Microenvironment
  6.4: Langmuir Nanofiltration & Heavy Metal Adsorption Water Treatment
  6.5: Master Environmental Nanosensor & Cleanroom Studio
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
# 6.1: Perovskite & QD Solar Cell Simulator
# ==============================================================================
SIM_6_1_HTML = """<!DOCTYPE html>
<html lang="th">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Lab 6.1: Perovskite & QD Solar Cell PCE Solver</title>
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
        <span>☀️</span>
        <span>แล็บ 6.1: การแปลงพลังงานแสงอาทิตย์และเส้นโค้ง J-V (Perovskite & QD Solar Cell PCE)</span>
      </div>
      <div class="badge">● AM 1.5G 100 mW/cm² STANDARD</div>
    </div>

    <div class="canvas-box">
      <canvas id="solarCanvas"></canvas>
    </div>

    <div class="controls">
      <div class="ctrl-group">
        <div class="ctrl-lbl">
          <span>ความหนาแน่นกระแสลัดวงจร (Short-Circuit Current: \(J_{sc}\))</span>
          <span id="txtJsc">Jsc = 24.5 mA/cm²</span>
        </div>
        <input type="range" id="sliderJsc" min="10.0" max="30.0" step="0.5" value="24.5">
      </div>
      <div class="ctrl-group">
        <div class="ctrl-lbl">
          <span>แรงดันไฟฟ้าวงจรเปิด (Open-Circuit Voltage: \(V_{oc}\))</span>
          <span id="txtVoc">Voc = 1.15 V</span>
        </div>
        <input type="range" id="sliderVoc" min="0.6" max="1.3" step="0.02" value="1.15">
      </div>
    </div>

    <div class="hud">
      <div>แฟกเตอร์เติมเต็ม (Fill Factor): <span class="hud-val" id="hudFF">0.82 (82.0%)</span> | กำลังไฟฟ้าสูงสุด: <span class="hud-val" id="hudPmax">23.1 mW/cm²</span></div>
      <div>ประสิทธิภาพการแปลงพลังงาน (PCE): <span class="hud-val" id="hudPCE">23.1% (High Efficiency Tandem)</span></div>
      <button type="button" onclick="setPerovskitePreset()" style="background:#facc15; color:#020617; border:none; padding:6px 14px; border-radius:6px; font-weight:700; cursor:pointer;">⚡ พรีเซต Perovskite/Si Tandem (PCE > 29%)</button>
    </div>
  </div>

  <script src="ar_mediapipe_controller.js"></script>
  <script>
    const canvas = document.getElementById("solarCanvas");
    const ctx = canvas.getContext("2d");

    function resize() {
      canvas.width = canvas.parentElement.clientWidth;
      canvas.height = canvas.parentElement.clientHeight;
    }
    window.addEventListener("resize", resize);
    resize();

    let Jsc = 24.5;
    let Voc = 1.15;
    const FF = 0.82;
    const Pin = 100.0; // mW/cm2
    let animTime = 0;

    const sliderJsc = document.getElementById("sliderJsc");
    const sliderVoc = document.getElementById("sliderVoc");
    const txtJsc = document.getElementById("txtJsc");
    const txtVoc = document.getElementById("txtVoc");
    const hudPmax = document.getElementById("hudPmax");
    const hudPCE = document.getElementById("hudPCE");

    sliderJsc.addEventListener("input", (e) => {
      Jsc = parseFloat(e.target.value);
      updateSolar();
    });

    sliderVoc.addEventListener("input", (e) => {
      Voc = parseFloat(e.target.value);
      updateSolar();
    });

    function setPerovskitePreset() {
      Jsc = 28.5; Voc = 1.25;
      sliderJsc.value = Jsc; sliderVoc.value = Voc;
      updateSolar();
    }

    function updateSolar() {
      txtJsc.textContent = "Jsc = " + Jsc.toFixed(1) + " mA/cm²";
      txtVoc.textContent = "Voc = " + Voc.toFixed(2) + " V";
      const Pmax = (Jsc * Voc * FF);
      const PCE = (Pmax / Pin) * 100;
      hudPmax.textContent = Pmax.toFixed(1) + " mW/cm²";
      hudPCE.textContent = PCE.toFixed(1) + "% (" + (PCE > 25 ? "Ultra-High Tandem" : "High Efficiency") + ")";
    }

    function draw() {
      ctx.clearRect(0, 0, canvas.width, canvas.height);
      const w = canvas.width;
      const h = canvas.height;
      animTime += 0.03;

      const simW = w * 0.50;
      const cy = h * 0.5;

      // 3D Solar Cell Photogeneration Layer Box
      ctx.fillStyle = "#020617";
      ctx.strokeStyle = "#334155";
      ctx.lineWidth = 2;
      ctx.fillRect(15, 15, simW - 15, h - 30);
      ctx.strokeRect(15, 15, simW - 15, h - 30);

      // Glass / ITO transparent anode (Top)
      ctx.fillStyle = "rgba(0, 240, 255, 0.25)";
      ctx.fillRect(30, 45, simW - 50, 20);
      ctx.strokeStyle = "#00f0ff"; ctx.strokeRect(30, 45, simW - 50, 20);
      ctx.fillStyle = "#ffffff"; ctx.font = "11px 'JetBrains Mono', monospace"; ctx.fillText("ITO Transparent Anode", 40, 60);

      // Perovskite Absorber Layer (Middle Amber)
      ctx.fillStyle = "rgba(250, 204, 21, 0.35)";
      ctx.fillRect(30, 70, simW - 50, 75);
      ctx.strokeStyle = "#facc15"; ctx.strokeRect(30, 70, simW - 50, 75);
      ctx.fillStyle = "#facc15"; ctx.fillText("Perovskite / QD Absorber Layer", 40, 110);

      // Metal Cathode (Bottom)
      ctx.fillStyle = "rgba(148, 163, 184, 0.3)";
      ctx.fillRect(30, 150, simW - 50, 25);
      ctx.strokeStyle = "#94a3b8"; ctx.strokeRect(30, 150, simW - 50, 25);
      ctx.fillStyle = "#ffffff"; ctx.fillText("Metal Back Contact (Ag / Au)", 40, 168);

      // Sunlight Photons & Generated Electron-Hole Pairs
      ctx.fillStyle = "#facc15";
      for (let p = 0; p < 8; p++) {
        const px = 45 + p * 28;
        const py = 20 + ((p * 20 + animTime * 60) % 50);
        ctx.beginPath(); ctx.arc(px, py, 3, 0, Math.PI * 2); ctx.fill();
      }

      // Generated Electrons (Cyan) flowing to top
      ctx.fillStyle = "#00f0ff";
      for (let e = 0; e < 6; e++) {
        const ex = 50 + e * 35;
        const ey = 135 - ((e * 15 + animTime * 45) % 65);
        ctx.beginPath(); ctx.arc(ex, ey, 4, 0, Math.PI * 2); ctx.fill();
      }

      // Right Side: J-V Characteristic Curve & MPP Point
      const gx = w * 0.53;
      const gy = 15;
      const gw = w * 0.45;
      const gh = h - 30;

      ctx.fillStyle = "rgba(15, 23, 42, 0.9)";
      ctx.strokeStyle = "#334155";
      ctx.fillRect(gx, gy, gw, gh);
      ctx.strokeRect(gx, gy, gw, gh);

      ctx.fillStyle = "#facc15";
      ctx.font = "11px 'JetBrains Mono', monospace";
      ctx.fillText("J-V Curve & Maximum Power Point (MPP)", gx + 10, gy + 18);

      // Plot J-V curve
      ctx.strokeStyle = "#00f0ff";
      ctx.lineWidth = 2.5;
      ctx.beginPath();
      const originX = gx + 25;
      const originY = gy + gh - 35;
      const plotW = gw - 50;
      const plotH = gh - 65;

      ctx.moveTo(originX, originY - (Jsc / 30.0) * plotH);
      for (let vx = 0; vx <= plotW; vx += 2) {
        const v = (vx / plotW) * Voc * 1.05;
        const j = Jsc * (1 - Math.exp((v - Voc) / 0.15));
        const py = originY - Math.max(0, (j / 30.0) * plotH);
        ctx.lineTo(originX + vx, py);
      }
      ctx.stroke();

      // Maximum power point marker
      const mppX = originX + (Voc * 0.85 / (Voc * 1.05)) * plotW;
      const mppY = originY - (Jsc * 0.9 / 30.0) * plotH;
      ctx.fillStyle = "#facc15";
      ctx.beginPath(); ctx.arc(mppX, mppY, 6, 0, Math.PI * 2); ctx.fill();
      ctx.fillText("MPP (" + ((Jsc * Voc * FF)).toFixed(1) + " mW/cm²)", mppX - 45, mppY - 12);

      requestAnimationFrame(draw);
    }
    draw();
    updateSolar();
  </script>
</body>
</html>
"""

# ==============================================================================
# 6.2: Supercapacitor & Nano-Battery Simulator
# ==============================================================================
SIM_6_2_HTML = """<!DOCTYPE html>
<html lang="th">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Lab 6.2: Nano-Supercapacitor Energy & Power Density</title>
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
        <span>🔋</span>
        <span>แล็บ 6.2: ตัวเก็บประจุยิ่งยวดกราฟีนรูพรุน 3D (Nano-Supercapacitor & EDLC Kinetics)</span>
      </div>
      <div class="badge">● RAGONE PLOT & ULTRA-FAST CHARGING</div>
    </div>

    <div class="canvas-box">
      <canvas id="capCanvas"></canvas>
    </div>

    <div class="controls">
      <div class="ctrl-group">
        <div class="ctrl-lbl">
          <span>ความจุไฟฟ้าจำเพาะ (Specific Capacitance: \(C\))</span>
          <span id="txtC">C = 350 F/g</span>
        </div>
        <input type="range" id="sliderC" min="100" max="600" step="10" value="350">
      </div>
      <div class="ctrl-group">
        <div class="ctrl-lbl">
          <span>หน้าต่างศักย์ไฟฟ้าการทำงาน (Voltage Window: \(V\))</span>
          <span id="txtV">V = 3.0 V (Ionic Liquid Electrolyte)</span>
        </div>
        <input type="range" id="sliderV" min="1.0" max="4.0" step="0.1" value="3.0">
      </div>
    </div>

    <div class="hud">
      <div>ความหนาแน่นพลังงาน (E): <span class="hud-val" id="hudE">131.3 Wh/kg</span> | กำลังไฟฟ้าสูงสุด (Pmax): <span class="hud-val" id="hudP">45.0 kW/kg</span></div>
      <div>เวลาในการชาร์จเต็ม (100% SoC): <span class="hud-val" id="hudTime">4.5 วินาที</span></div>
      <button type="button" onclick="fastChargePulse()" style="background:#00f0ff; color:#020617; border:none; padding:6px 14px; border-radius:6px; font-weight:700; cursor:pointer;">⚡ จ่ายพัลส์ชาร์จเร็ว (Fast Charge Pulse)</button>
    </div>
  </div>

  <script src="ar_mediapipe_controller.js"></script>
  <script>
    const canvas = document.getElementById("capCanvas");
    const ctx = canvas.getContext("2d");

    function resize() {
      canvas.width = canvas.parentElement.clientWidth;
      canvas.height = canvas.parentElement.clientHeight;
    }
    window.addEventListener("resize", resize);
    resize();

    let C_Fg = 350;
    let V_volt = 3.0;
    let chargeProgress = 0.5;
    let animTime = 0;

    const sliderC = document.getElementById("sliderC");
    const sliderV = document.getElementById("sliderV");
    const txtC = document.getElementById("txtC");
    const txtV = document.getElementById("txtV");
    const hudE = document.getElementById("hudE");
    const hudP = document.getElementById("hudP");

    sliderC.addEventListener("input", (e) => {
      C_Fg = parseFloat(e.target.value);
      updateCap();
    });

    sliderV.addEventListener("input", (e) => {
      V_volt = parseFloat(e.target.value);
      updateCap();
    });

    function fastChargePulse() {
      chargeProgress = 0.0;
    }

    function updateCap() {
      txtC.textContent = "C = " + C_Fg.toFixed(0) + " F/g";
      txtV.textContent = "V = " + V_volt.toFixed(1) + " V";
      // E = 0.5 * C * V^2 / 3.6 (Wh/kg)
      const E_Whkg = (0.5 * C_Fg * V_volt * V_volt) / 3.6;
      const P_kWkg = (V_volt * V_volt / (4 * 0.05)) / 1000;
      hudE.textContent = E_Whkg.toFixed(1) + " Wh/kg";
      hudP.textContent = P_kWkg.toFixed(1) + " kW/kg";
    }

    function draw() {
      ctx.clearRect(0, 0, canvas.width, canvas.height);
      const w = canvas.width;
      const h = canvas.height;
      animTime += 0.03;
      if (chargeProgress < 1.0) chargeProgress += 0.015;

      const simW = w * 0.50;
      const cy = h * 0.5;

      // 3D Porous Carbon Electrode Cell
      ctx.fillStyle = "#020617";
      ctx.strokeStyle = "#334155";
      ctx.lineWidth = 2;
      ctx.fillRect(15, 15, simW - 15, h - 30);
      ctx.strokeRect(15, 15, simW - 15, h - 30);

      // Anode Electrode (Porous Graphene, Left)
      ctx.fillStyle = "rgba(0, 240, 255, 0.25)";
      ctx.fillRect(30, 40, 60, h - 80);
      ctx.strokeStyle = "#00f0ff"; ctx.strokeRect(30, 40, 60, h - 80);
      ctx.fillStyle = "#ffffff"; ctx.font = "11px 'JetBrains Mono', monospace"; ctx.fillText("Anode (+)", 35, 60);

      // Cathode Electrode (Porous Graphene, Right)
      ctx.fillStyle = "rgba(244, 63, 94, 0.25)";
      ctx.fillRect(simW - 90, 40, 60, h - 80);
      ctx.strokeStyle = "#f43f5e"; ctx.strokeRect(simW - 90, 40, 60, h - 80);
      ctx.fillStyle = "#ffffff"; ctx.fillText("Cathode (-)", simW - 85, 60);

      // Electrolyte Separator Channel (Middle)
      ctx.fillStyle = "rgba(16, 185, 129, 0.15)";
      ctx.fillRect(95, 40, simW - 190, h - 80);

      // Electrolyte Ions accumulating (EDLC formation)
      ctx.fillStyle = "#facc15";
      for (let i = 0; i < 14; i++) {
        const ix = 95 + ((i * 20 + animTime * 40) % (simW - 190));
        const iy = 50 + (i % 6) * 35;
        ctx.beginPath(); ctx.arc(ix, iy, 4, 0, Math.PI * 2); ctx.fill();
      }

      // Right Side: Ragone Plot (Energy vs Power Density)
      const gx = w * 0.53;
      const gy = 15;
      const gw = w * 0.45;
      const gh = h - 30;

      ctx.fillStyle = "rgba(15, 23, 42, 0.9)";
      ctx.strokeStyle = "#334155";
      ctx.fillRect(gx, gy, gw, gh);
      ctx.strokeRect(gx, gy, gw, gh);

      ctx.fillStyle = "#00f0ff";
      ctx.font = "11px 'JetBrains Mono', monospace";
      ctx.fillText("Ragone Plot: Energy vs Power Density", gx + 10, gy + 18);

      // Axes
      ctx.strokeStyle = "#64748b";
      ctx.lineWidth = 1.5;
      ctx.beginPath();
      ctx.moveTo(gx + 30, gy + gh - 30);
      ctx.lineTo(gx + gw - 20, gy + gh - 30);
      ctx.moveTo(gx + 30, gy + gh - 30);
      ctx.lineTo(gx + 30, gy + 35);
      ctx.stroke();

      // Supercapacitor region (Top Left to Mid)
      ctx.fillStyle = "rgba(0, 240, 255, 0.4)";
      ctx.beginPath();
      ctx.ellipse(gx + gw * 0.65, gy + 60, 45, 25, 0, 0, Math.PI * 2);
      ctx.fill();
      ctx.fillStyle = "#ffffff";
      ctx.fillText("Nano-Supercapacitors", gx + gw * 0.45, gy + 65);

      // Battery region (Bottom Right)
      ctx.fillStyle = "rgba(16, 185, 129, 0.4)";
      ctx.beginPath();
      ctx.ellipse(gx + gw * 0.35, gy + gh - 65, 40, 20, 0, 0, Math.PI * 2);
      ctx.fill();
      ctx.fillStyle = "#ffffff";
      ctx.fillText("Li-Ion Batteries", gx + gw * 0.22, gy + gh - 60);

      requestAnimationFrame(draw);
    }
    draw();
    updateCap();
  </script>
</body>
</html>
"""

# ==============================================================================
# 6.3: Nanomedicine Targeted Drug Delivery Simulator
# ==============================================================================
SIM_6_3_HTML = """<!DOCTYPE html>
<html lang="th">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Lab 6.3: Nanomedicine & EPR Targeted Drug Delivery</title>
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
        <span>💊</span>
        <span>แล็บ 6.3: ระบบนำส่งยาพุ่งเป้าและปรากฏการณ์ EPR (Targeted Nanomedicine Delivery)</span>
      </div>
      <div class="badge">● ENHANCED PERMEABILITY & RETENTION</div>
    </div>

    <div class="canvas-box">
      <canvas id="medCanvas"></canvas>
    </div>

    <div class="controls">
      <div class="ctrl-group">
        <div class="ctrl-lbl">
          <span>ขนาดอนุภาคนาโนพาหะ (Nanocarrier Size: \(d\))</span>
          <span id="txtD">d = 85 nm (Optimal Tumor Penetration)</span>
        </div>
        <input type="range" id="sliderD" min="20" max="250" step="5" value="85">
      </div>
      <div class="ctrl-group">
        <div class="ctrl-lbl">
          <span>ประสิทธิภาพการกักเก็บตัวยา (Encapsulation Efficiency: \(EE\))</span>
          <span id="txtEE">EE = 92.5%</span>
        </div>
        <input type="range" id="sliderEE" min="50" max="98" step="1" value="92">
      </div>
    </div>

    <div class="hud">
      <div>การสะสมในเนื้องอก (EPR Uptake): <span class="hud-val" id="hudEPR">88.4% Tumor Selectivity</span> | การขับทิ้งที่ไต: <span class="hud-val" id="hudClear">ต่ำ (< 5%)</span></div>
      <div>การตอบสนองต่อ pH ในเนื้องอก: <span class="hud-val" id="hudpH">กรดอ่อน (pH 6.5 ➔ Triggered Release)</span></div>
      <button type="button" onclick="triggerRelease()" style="background:#f43f5e; color:#ffffff; border:none; padding:6px 14px; border-radius:6px; font-weight:700; cursor:pointer;">⚡ กระตุ้นการปลดปล่อยตัวยา (pH-Triggered Release)</button>
    </div>
  </div>

  <script src="ar_mediapipe_controller.js"></script>
  <script>
    const canvas = document.getElementById("medCanvas");
    const ctx = canvas.getContext("2d");

    function resize() {
      canvas.width = canvas.parentElement.clientWidth;
      canvas.height = canvas.parentElement.clientHeight;
    }
    window.addEventListener("resize", resize);
    resize();

    let size_nm = 85;
    let EE_pct = 92.5;
    let isReleasing = false;
    let animTime = 0;

    const sliderD = document.getElementById("sliderD");
    const sliderEE = document.getElementById("sliderEE");
    const txtD = document.getElementById("txtD");
    const txtEE = document.getElementById("txtEE");
    const hudEPR = document.getElementById("hudEPR");

    sliderD.addEventListener("input", (e) => {
      size_nm = parseFloat(e.target.value);
      updateMed();
    });

    sliderEE.addEventListener("input", (e) => {
      EE_pct = parseFloat(e.target.value);
      updateMed();
    });

    function triggerRelease() {
      isReleasing = true;
      setTimeout(() => { isReleasing = false; }, 3000);
    }

    function updateMed() {
      txtD.textContent = "d = " + size_nm.toFixed(0) + " nm (" + (size_nm >= 50 && size_nm <= 150 ? "Optimal EPR Window" : "Sub-optimal Size") + ")";
      txtEE.textContent = "EE = " + EE_pct.toFixed(1) + "%";
      const eprScore = Math.max(10, 100 - Math.abs(size_nm - 100) * 0.7);
      hudEPR.textContent = eprScore.toFixed(1) + "% Tumor Selectivity";
    }

    function draw() {
      ctx.clearRect(0, 0, canvas.width, canvas.height);
      const w = canvas.width;
      const h = canvas.height;
      animTime += 0.03;

      const simW = w * 0.55;
      const cy = h * 0.5;

      // Tumor Vasculature with Leaky Pores (EPR Effect)
      ctx.fillStyle = "#020617";
      ctx.strokeStyle = "#334155";
      ctx.lineWidth = 2;
      ctx.fillRect(15, 15, simW - 15, h - 30);
      ctx.strokeRect(15, 15, simW - 15, h - 30);

      // Blood vessel walls (Red tubes)
      ctx.fillStyle = "rgba(244, 63, 94, 0.3)";
      ctx.fillRect(25, 45, simW - 35, 30); // top vessel wall
      ctx.fillRect(25, 130, simW - 35, 30); // bottom vessel wall

      // Leaky endothelial fenestrations (Pores in vessel wall ~100-200nm)
      ctx.clearRect(80, 130, 25, 30);
      ctx.clearRect(160, 130, 25, 30);
      ctx.clearRect(240, 130, 25, 30);

      // Tumor Tissue Region (Bottom)
      ctx.fillStyle = "rgba(192, 132, 252, 0.2)";
      ctx.fillRect(25, 165, simW - 35, h - 190);
      ctx.fillStyle = "#c084fc"; ctx.font = "11px 'JetBrains Mono', monospace"; ctx.fillText("Tumor Tissue (pH 6.5, Leaky Vessels)", 35, h - 25);

      // Nanoparticles flowing through blood and extravasating
      ctx.fillStyle = isReleasing ? "#facc15" : "#00f0ff";
      for (let n = 0; n < 12; n++) {
        const nx = 35 + ((n * 35 + animTime * 70) % (simW - 60));
        let ny = 95;
        if (nx > 140 && nx < 220 && size_nm <= 150) {
          ny = 95 + ((nx - 140) * 0.8); // extravasating into tumor
        }
        ctx.beginPath(); ctx.arc(nx, ny, Math.max(3, size_nm * 0.06), 0, Math.PI * 2); ctx.fill();
      }

      // Right Side: Drug Release Profile Curve
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
      ctx.fillText("Cumulative Drug Release (%)", gx + 10, gy + 18);

      // Release curve (Fast in pH 6.5 tumor vs slow in pH 7.4 blood)
      ctx.strokeStyle = "#facc15";
      ctx.lineWidth = 2.5;
      ctx.beginPath();
      ctx.moveTo(gx + 20, gy + gh - 25);
      ctx.bezierCurveTo(gx + 40, gy + 45, gx + gw * 0.6, gy + 40, gx + gw - 15, gy + 40);
      ctx.stroke();

      requestAnimationFrame(draw);
    }
    draw();
    updateMed();
  </script>
</body>
</html>
"""

# ==============================================================================
# 6.4: Nanofiltration & Heavy Metal Adsorption Simulator
# ==============================================================================
SIM_6_4_HTML = """<!DOCTYPE html>
<html lang="th">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Lab 6.4: Nanofiltration & Heavy Metal Adsorption</title>
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
        <span>💧</span>
        <span>แล็บ 6.4: การกรองเมมเบรนนาโนและการดูดซับแลงเมียร์ (Langmuir Nanofiltration Solver)</span>
      </div>
      <div class="badge">● HEAVY METAL REJECTION (> 99.5%)</div>
    </div>

    <div class="canvas-box">
      <canvas id="filterCanvas"></canvas>
    </div>

    <div class="controls">
      <div class="ctrl-group">
        <div class="ctrl-lbl">
          <span>ความดันขับเคลื่อนเมมเบรน (Transmembrane Pressure: \(\Delta P\))</span>
          <span id="txtP">ΔP = 5.0 bar</span>
        </div>
        <input type="range" id="sliderP" min="1.0" max="10.0" step="0.5" value="5.0">
      </div>
      <div class="ctrl-group">
        <div class="ctrl-lbl">
          <span>ความเข้มข้นโลหะหนักเริ่มต้น (Heavy Metal Conc: \(C_0\))</span>
          <span id="txtC0">C0 = 50 mg/L (Pb²⁺ / Cd²⁺)</span>
        </div>
        <input type="range" id="sliderC0" min="5" max="100" step="5" value="50">
      </div>
    </div>

    <div class="hud">
      <div>ฟลักซ์น้ำสะอาด (Water Flux: \(J_w\)): <span class="hud-val" id="hudFlux">48.5 L/m²·h</span> | อัตรากำจัดโลหะหนัก: <span class="hud-val" id="hudRej">99.8% Rejection</span></div>
      <div>ความจุการดูดซับสูงสุด (qm): <span class="hud-val" id="hudQm">245 mg/g (GO-TiO2 Nanocomposite)</span></div>
      <button type="button" onclick="cleanMembrane()" style="background:#10b981; color:#020617; border:none; padding:6px 14px; border-radius:6px; font-weight:700; cursor:pointer;">⚡ ล้างย้อนเมมเบรนด้วยแสง UV (Photocatalytic Cleaning)</button>
    </div>
  </div>

  <script src="ar_mediapipe_controller.js"></script>
  <script>
    const canvas = document.getElementById("filterCanvas");
    const ctx = canvas.getContext("2d");

    function resize() {
      canvas.width = canvas.parentElement.clientWidth;
      canvas.height = canvas.parentElement.clientHeight;
    }
    window.addEventListener("resize", resize);
    resize();

    let pressure_bar = 5.0;
    let conc_mgL = 50;
    let animTime = 0;

    const sliderP = document.getElementById("sliderP");
    const sliderC0 = document.getElementById("sliderC0");
    const txtP = document.getElementById("txtP");
    const txtC0 = document.getElementById("txtC0");
    const hudFlux = document.getElementById("hudFlux");

    sliderP.addEventListener("input", (e) => {
      pressure_bar = parseFloat(e.target.value);
      updateFilter();
    });

    sliderC0.addEventListener("input", (e) => {
      conc_mgL = parseFloat(e.target.value);
      updateFilter();
    });

    function cleanMembrane() {
      alert("✨ ฉายรังสี UV ทำความสะอาดเมมเบรนด้วยกระบวนการ Photocatalysis ของ TiO2 สำเร็จ!");
    }

    function updateFilter() {
      txtP.textContent = "ΔP = " + pressure_bar.toFixed(1) + " bar";
      txtC0.textContent = "C0 = " + conc_mgL.toFixed(0) + " mg/L";
      const flux = pressure_bar * 9.7;
      hudFlux.textContent = flux.toFixed(1) + " L/m²·h";
    }

    function draw() {
      ctx.clearRect(0, 0, canvas.width, canvas.height);
      const w = canvas.width;
      const h = canvas.height;
      animTime += 0.03;

      const simW = w * 0.50;
      const cy = h * 0.5;

      // Cross-flow Nanofiltration Module Viewport
      ctx.fillStyle = "#020617";
      ctx.strokeStyle = "#334155";
      ctx.lineWidth = 2;
      ctx.fillRect(15, 15, simW - 15, h - 30);
      ctx.strokeRect(15, 15, simW - 15, h - 30);

      // Feed Channel (Top: Dirty Water with Heavy Metals)
      ctx.fillStyle = "rgba(244, 63, 94, 0.2)";
      ctx.fillRect(25, 30, simW - 35, 65);
      ctx.fillStyle = "#f43f5e"; ctx.font = "11px 'JetBrains Mono', monospace"; ctx.fillText("Feed Stream (Heavy Metal Ions: Pb²⁺, Cd²⁺)", 35, 48);

      // Nanoporous GO / TiO2 Membrane Layer (Middle)
      ctx.fillStyle = "rgba(16, 185, 129, 0.6)";
      ctx.fillRect(25, 95, simW - 35, 20);
      ctx.strokeStyle = "#10b981"; ctx.strokeRect(25, 95, simW - 35, 20);
      ctx.fillStyle = "#ffffff"; ctx.fillText("Graphene Oxide Nanofiltration Membrane", 35, 109);

      // Permeate Channel (Bottom: Ultra-Pure Water)
      ctx.fillStyle = "rgba(0, 240, 255, 0.2)";
      ctx.fillRect(25, 115, simW - 35, 65);
      ctx.fillStyle = "#00f0ff"; ctx.fillText("Permeate Stream (Ultra-Pure Clean Water)", 35, 165);

      // Filtered pure water droplets passing through
      ctx.fillStyle = "#00f0ff";
      for (let p = 0; p < 10; p++) {
        const px = 40 + p * 24;
        const py = 115 + ((p * 15 + animTime * (pressure_bar * 12)) % 60);
        ctx.beginPath(); ctx.arc(px, py, 3, 0, Math.PI * 2); ctx.fill();
      }

      // Rejected heavy metal particles trapped on membrane top
      ctx.fillStyle = "#f43f5e";
      for (let r = 0; r < 8; r++) {
        const rx = 35 + ((r * 30 + animTime * 35) % (simW - 60));
        ctx.beginPath(); ctx.arc(rx, 88, 4.5, 0, Math.PI * 2); ctx.fill();
      }

      // Right Side: Langmuir Adsorption Isotherm Plot qe vs Ce
      const gx = w * 0.53;
      const gy = 15;
      const gw = w * 0.45;
      const gh = h - 30;

      ctx.fillStyle = "rgba(15, 23, 42, 0.9)";
      ctx.strokeStyle = "#334155";
      ctx.fillRect(gx, gy, gw, gh);
      ctx.strokeRect(gx, gy, gw, gh);

      ctx.fillStyle = "#10b981";
      ctx.font = "11px 'JetBrains Mono', monospace";
      ctx.fillText("Langmuir Adsorption Isotherm qe(Ce)", gx + 10, gy + 18);

      // Plot Langmuir curve
      ctx.strokeStyle = "#facc15";
      ctx.lineWidth = 2.5;
      ctx.beginPath();
      const originX = gx + 25;
      const originY = gy + gh - 35;
      const plotW = gw - 50;
      const plotH = gh - 65;

      ctx.moveTo(originX, originY);
      for (let cx = 0; cx <= plotW; cx += 2) {
        const ce = (cx / plotW) * 100;
        const qe = (245 * 0.08 * ce) / (1 + 0.08 * ce);
        const py = originY - (qe / 250.0) * plotH;
        ctx.lineTo(originX + cx, py);
      }
      ctx.stroke();

      requestAnimationFrame(draw);
    }
    draw();
    updateFilter();
  </script>
</body>
</html>
"""

# ==============================================================================
# 6.5: Master Environmental Nanosensor & Gas Array Studio
# ==============================================================================
SIM_6_5_HTML = """<!DOCTYPE html>
<html lang="th">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Lab 6.5: Master Nanosensor & Environmental Array Studio</title>
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
        <span>แล็บ 6.5: สตูดิโอการประยุกต์ใช้นาโนเทคโนโลยีและเซนเซอร์ (Master Application Studio)</span>
      </div>
      <div class="badge">● AR HANDS MULTI-MODAL 60 FPS</div>
    </div>

    <div class="canvas-box">
      <canvas id="hubCanvas"></canvas>
    </div>

    <div class="hud">
      <div>โหมดการประยุกต์ใช้นาโนเทคโนโลยี 3D: <span class="hud-val" id="hudMode">1. เซนเซอร์ตรวจวัดก๊าซพิษ NO₂ (ZnO Nanowire Array)</span></div>
      <div>สถานะกล้อง AR: <span class="hud-val" id="hudAR">Active (60 FPS Tracking)</span></div>
      <button type="button" class="btn-switch" onclick="switchBay()">🔄 สลับโหมดการประยุกต์ใช้ 3D</button>
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
      "1. เซนเซอร์ตรวจวัดก๊าซพิษ NO₂ (ZnO Nanowire Array)",
      "2. แผงเซลล์แสงอาทิตย์เพอรอฟสไกต์แทนเดม (Perovskite Tandem)",
      "3. ระบบกรองบำบัดน้ำเสียเมมเบรนนาโน (Nanofiltration Plant)"
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
        // Mode 0: ZnO Nanowire Gas Sensor Array
        ctx.fillStyle = "#334155";
        ctx.fillRect(cx - 140, cy + 20, 280, 20); // substrate

        // Nanowire forest
        ctx.strokeStyle = "#00f0ff";
        ctx.lineWidth = 3;
        for (let nw = 0; nw < 14; nw++) {
          const nwx = cx - 120 + nw * 18;
          ctx.beginPath();
          ctx.moveTo(nwx, cy + 20);
          ctx.lineTo(nwx + Math.sin(animTime + nw) * 4, cy - 50);
          ctx.stroke();
        }

        // Gas molecules approaching (Yellow dots)
        ctx.fillStyle = "#facc15";
        for (let g = 0; g < 8; g++) {
          const gx = cx - 100 + g * 25;
          const gy = cy - 65 + Math.sin(animTime * 2 + g) * 15;
          ctx.beginPath(); ctx.arc(gx, gy, 4, 0, Math.PI * 2); ctx.fill();
        }
      } else if (bayIndex === 1) {
        // Mode 1: Tandem Solar Cell Modules
        ctx.fillStyle = "rgba(250, 204, 21, 0.3)";
        ctx.fillRect(cx - 100, cy - 40, 200, 80);
        ctx.strokeStyle = "#facc15"; ctx.strokeRect(cx - 100, cy - 40, 200, 80);
      } else {
        // Mode 2: Nanofiltration Crossflow Tube
        ctx.strokeStyle = "#10b981"; ctx.lineWidth = 3;
        ctx.strokeRect(cx - 120, cy - 30, 240, 60);
      }

      requestAnimationFrame(draw);
    }
    draw();
  </script>
</body>
</html>
"""

# 1. Write simulators
ch6_sims = {
    "sim_nano_6_1.html": SIM_6_1_HTML,
    "sim_nano_6_2.html": SIM_6_2_HTML,
    "sim_nano_6_3.html": SIM_6_3_HTML,
    "sim_nano_6_4.html": SIM_6_4_HTML,
    "sim_nano_6_5.html": SIM_6_5_HTML
}

for fname, content in ch6_sims.items():
    with open(os.path.join(NANO_SIMS_DIR, fname), "w", encoding="utf-8") as f:
        f.write(content)
    with open(os.path.join(ROOT_SIMS_DIR, fname), "w", encoding="utf-8") as f:
        f.write(content)
    print(f"✅ Generated Chapter 6 Simulator: {fname}")

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
subprocess.run(["git", "commit", "-m", "feat(sims): add chapter 6 tailored energy, medicine, and environmental 60fps simulators"], cwd=TMP_GH, check=True)

remote_url = f"https://{os.environ.get('GH_PAT', '')}@github.com/Tsanaphy2023/modernphysics.git"
subprocess.run(["git", "push", "--force", remote_url, "gh-pages"], cwd=TMP_GH, check=True)
print("🎉 Force pushed Chapter 6 Simulators to gh-pages CDN!")

# 3. Re-run deploy_masterclass_formulas_course_263.py to update Moodle
subprocess.run(["python3", "nanotechnology/course_nanophysics_263/deploy_masterclass_formulas_course_263.py"], cwd=BASE_DIR, check=True)

print("🎉 Successfully developed, synced, and deployed Chapter 6 to Moodle Course 263!")
