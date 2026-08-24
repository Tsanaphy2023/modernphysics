#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generator for All 8 High-Contrast 3D Vector SVG Illustrations for Nanotechnological Physics Textbook.
Creates 8 Master 3D SVG diagrams with isometric perspective, gradient shaders, and vector math.
Author: Asst. Prof. Dr. Chewa Thassana, Rambhai Barni Rajabhat University
"""

import os

DIAGRAMS_DIR_1 = "/Users/chewathassana/Downloads/manus_backup2026/ModernPhysics/assets/diagrams"
DIAGRAMS_DIR_2 = "/Users/chewathassana/Downloads/manus_backup2026/ModernPhysics/nanotechnology/textbook_and_lab_manual_2026/assets/diagrams"

os.makedirs(DIAGRAMS_DIR_1, exist_ok=True)
os.makedirs(DIAGRAMS_DIR_2, exist_ok=True)

# 1. Chapter 1
svg_ch01 = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 900 450" width="100%" height="100%">
  <defs>
    <linearGradient id="bgGrad1" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#090e17"/><stop offset="50%" stop-color="#0f172a"/><stop offset="100%" stop-color="#1e1b4b"/>
    </linearGradient>
    <linearGradient id="cubeTop" x1="0%" y1="0%" x2="100%" y2="100%"><stop offset="0%" stop-color="#38bdf8"/><stop offset="100%" stop-color="#0284c7"/></linearGradient>
    <linearGradient id="cubeLeft" x1="0%" y1="0%" x2="100%" y2="100%"><stop offset="0%" stop-color="#0369a1"/><stop offset="100%" stop-color="#075985"/></linearGradient>
    <linearGradient id="cubeRight" x1="0%" y1="0%" x2="100%" y2="100%"><stop offset="0%" stop-color="#0284c7"/><stop offset="100%" stop-color="#0c4a6e"/></linearGradient>
    <linearGradient id="goldSphere" x1="30%" y1="30%" x2="100%" y2="100%"><stop offset="0%" stop-color="#fef08a"/><stop offset="40%" stop-color="#eab308"/><stop offset="80%" stop-color="#ca8a04"/><stop offset="100%" stop-color="#713f12"/></linearGradient>
    <filter id="glow1" x="-20%" y="-20%" width="140%" height="140%"><feGaussianBlur stdDeviation="6" result="blur"/><feComposite in="SourceGraphic" in2="blur" operator="over"/></filter>
  </defs>
  <rect width="900" height="450" rx="12" fill="url(#bgGrad1)" stroke="#334155" stroke-width="1.5"/>
  <g transform="translate(30, 25)">
    <rect width="360" height="32" rx="16" fill="rgba(56, 189, 248, 0.12)" stroke="#38bdf8" stroke-width="1"/>
    <text x="180" y="21" fill="#38bdf8" font-family="'JetBrains Mono', monospace" font-size="12" font-weight="bold" text-anchor="middle">FIGURE 1.1 • 3D NANOSCALE LENGTH SCALES &amp; S/V SCALING</text>
  </g>
  <g transform="translate(60, 90)">
    <text x="100" y="0" fill="#94a3b8" font-family="'Sarabun', sans-serif" font-size="13" font-weight="700" text-anchor="middle">1. มหภาค (Bulk Crystal: d = 1 cm)</text>
    <g transform="translate(40, 20)">
      <polygon points="60,0 120,30 60,60 0,30" fill="url(#cubeTop)" stroke="#e0f2fe" stroke-width="1"/>
      <polygon points="0,30 60,60 60,130 0,100" fill="url(#cubeLeft)" stroke="#e0f2fe" stroke-width="1"/>
      <polygon points="60,60 120,30 120,100 60,130" fill="url(#cubeRight)" stroke="#e0f2fe" stroke-width="1"/>
      <text x="60" y="160" fill="#38bdf8" font-family="'JetBrains Mono', monospace" font-size="11" text-anchor="middle">A/V = 6/d = 600 m⁻¹</text>
      <text x="60" y="178" fill="#64748b" font-family="'Sarabun', sans-serif" font-size="10" text-anchor="middle">อะตอมที่ผิว &lt; 0.0001%</text>
    </g>
    <g transform="translate(250, 0)">
      <text x="75" y="0" fill="#94a3b8" font-family="'Sarabun', sans-serif" font-size="13" font-weight="700" text-anchor="middle">2. อนุภาคนาโน (d = 2 nm)</text>
      <circle cx="50" cy="50" r="22" fill="url(#goldSphere)" filter="url(#glow1)"/>
      <circle cx="85" cy="40" r="16" fill="url(#goldSphere)"/>
      <circle cx="105" cy="70" r="20" fill="url(#goldSphere)" filter="url(#glow1)"/>
      <circle cx="45" cy="90" r="18" fill="url(#goldSphere)"/>
      <circle cx="80" cy="85" r="24" fill="url(#goldSphere)" filter="url(#glow1)"/>
      <circle cx="80" cy="85" r="32" fill="none" stroke="#38bdf8" stroke-width="1" stroke-dasharray="3 3"/>
      <text x="75" y="160" fill="#facc15" font-family="'JetBrains Mono', monospace" font-size="11" font-weight="bold" text-anchor="middle">A/V = 6/d = 3×10⁹ m⁻¹</text>
      <text x="75" y="178" fill="#10b981" font-family="'Sarabun', sans-serif" font-size="10" font-weight="bold" text-anchor="middle">อะตอมที่ผิว &gt; 50% (Quantum Surface)</text>
    </g>
  </g>
  <g transform="translate(480, 80)">
    <rect width="380" height="280" rx="8" fill="rgba(15, 23, 42, 0.7)" stroke="#334155" stroke-width="1"/>
    <text x="190" y="28" fill="#f8fafc" font-family="'Sarabun', sans-serif" font-size="13" font-weight="700" text-anchor="middle">กราฟความสัมพันธ์: อัตราส่วนพื้นที่ผิว &amp; อุณหภูมิหลอมเหลว</text>
    <line x1="60" y1="230" x2="340" y2="230" stroke="#64748b" stroke-width="1.5"/>
    <line x1="60" y1="230" x2="60" y2="50" stroke="#64748b" stroke-width="1.5"/>
    <path d="M 65,210 Q 80,195 110,130 T 200,85 T 330,80" fill="none" stroke="#f43f5e" stroke-width="3" filter="url(#glow1)"/>
    <path d="M 65,65 Q 85,150 140,195 T 330,225" fill="none" stroke="#38bdf8" stroke-width="3" filter="url(#glow1)"/>
    <rect x="60" y="50" width="75" height="180" fill="rgba(244, 63, 94, 0.12)" stroke="rgba(244, 63, 94, 0.4)" stroke-dasharray="3 3"/>
    <text x="97" y="160" fill="#facc15" font-family="'JetBrains Mono', monospace" font-size="10" font-weight="bold" text-anchor="middle" transform="rotate(-90 97 160)">NANOSCALE REGIME (1-10 nm)</text>
  </g>
  <g transform="translate(30, 395)">
    <rect width="840" height="38" rx="6" fill="rgba(30, 41, 59, 0.8)" stroke="#334155" stroke-width="1"/>
    <circle cx="25" cy="19" r="6" fill="#38bdf8"/><text x="40" y="23" fill="#cbd5e1" font-family="'Sarabun', sans-serif" font-size="10.5">อัตราส่วนพื้นที่ผิวต่อปริมาตรเพิ่มขึ้นแบบไฮเพอร์โบลาเมื่ออนุภาค &lt; 10 nm</text>
    <circle cx="430" cy="19" r="6" fill="#f43f5e"/><text x="445" y="23" fill="#cbd5e1" font-family="'Sarabun', sans-serif" font-size="10.5">อุณหภูมิหลอมเหลวของทองคำลดลงจาก 1,064 °C เหลือต่ำกว่า 400 °C ที่ขนาด 2 nm</text>
  </g>
</svg>"""

# 2. Chapter 2
svg_ch02 = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 900 450" width="100%" height="100%">
  <defs>
    <linearGradient id="bgGrad2" x1="0%" y1="0%" x2="100%" y2="100%"><stop offset="0%" stop-color="#020617"/><stop offset="50%" stop-color="#0f172a"/><stop offset="100%" stop-color="#1e1b4b"/></linearGradient>
    <filter id="glow2" x="-20%" y="-20%" width="140%" height="140%"><feGaussianBlur stdDeviation="5" result="blur"/><feComposite in="SourceGraphic" in2="blur" operator="over"/></filter>
  </defs>
  <rect width="900" height="450" rx="12" fill="url(#bgGrad2)" stroke="#334155" stroke-width="1.5"/>
  <g transform="translate(30, 25)">
    <rect width="450" height="32" rx="16" fill="rgba(168, 85, 247, 0.12)" stroke="#a855f7" stroke-width="1"/>
    <text x="225" y="21" fill="#c084fc" font-family="'JetBrains Mono', monospace" font-size="12" font-weight="bold" text-anchor="middle">FIGURE 2.1 • 3D QUANTUM CONFINEMENT DIMENSIONALITY &amp; DOS</text>
  </g>
  <g transform="translate(40, 80)">
    <rect width="185" height="330" rx="8" fill="rgba(15, 23, 42, 0.8)" stroke="#3b82f6" stroke-width="1.5"/>
    <text x="92" y="26" fill="#60a5fa" font-family="'Sarabun', sans-serif" font-size="13" font-weight="bold" text-anchor="middle">3D บัลค์ (Bulk)</text>
    <polygon points="92,70 142,95 92,120 42,95" fill="#3b82f6" opacity="0.8"/>
    <polygon points="42,95 92,120 92,170 42,145" fill="#1d4ed8" opacity="0.9"/>
    <polygon points="92,120 142,95 142,145 92,170" fill="#2563eb" opacity="0.85"/>
    <g transform="translate(20, 205)">
      <line x1="20" y1="80" x2="135" y2="80" stroke="#64748b" stroke-width="1"/>
      <line x1="20" y1="80" x2="20" y2="10" stroke="#64748b" stroke-width="1"/>
      <path d="M 20,80 Q 55,40 130,15" fill="none" stroke="#38bdf8" stroke-width="2.5" filter="url(#glow2)"/>
      <text x="77" y="45" fill="#38bdf8" font-family="'JetBrains Mono', monospace" font-size="9.5" font-weight="bold">g_3D ∝ √E</text>
    </g>
  </g>
  <g transform="translate(245, 80)">
    <rect width="185" height="330" rx="8" fill="rgba(15, 23, 42, 0.8)" stroke="#10b981" stroke-width="1.5"/>
    <text x="92" y="26" fill="#34d399" font-family="'Sarabun', sans-serif" font-size="13" font-weight="bold" text-anchor="middle">2D บ่อควอนตัม (Well)</text>
    <polygon points="92,90 142,110 92,130 42,110" fill="#10b981" opacity="0.9" filter="url(#glow2)"/>
    <polygon points="42,110 92,130 92,140 42,120" fill="#047857"/>
    <polygon points="92,130 142,110 142,120 92,140" fill="#059669"/>
    <g transform="translate(20, 205)">
      <line x1="20" y1="80" x2="135" y2="80" stroke="#64748b" stroke-width="1"/>
      <line x1="20" y1="80" x2="20" y2="10" stroke="#64748b" stroke-width="1"/>
      <path d="M 20,80 L 45,80 L 45,55 L 80,55 L 80,30 L 130,30" fill="none" stroke="#34d399" stroke-width="2.5" filter="url(#glow2)"/>
      <text x="77" y="25" fill="#34d399" font-family="'JetBrains Mono', monospace" font-size="9.5" font-weight="bold">g_2D ∝ Step(E)</text>
    </g>
  </g>
  <g transform="translate(450, 80)">
    <rect width="185" height="330" rx="8" fill="rgba(15, 23, 42, 0.8)" stroke="#f59e0b" stroke-width="1.5"/>
    <text x="92" y="26" fill="#fbbf24" font-family="'Sarabun', sans-serif" font-size="13" font-weight="bold" text-anchor="middle">1D ลวดควอนตัม (Wire)</text>
    <ellipse cx="55" cy="115" rx="12" ry="25" fill="#d97706"/>
    <rect x="55" y="90" width="75" height="50" fill="#f59e0b" opacity="0.85"/>
    <ellipse cx="130" cy="115" rx="12" ry="25" fill="#fbbf24" filter="url(#glow2)"/>
    <g transform="translate(20, 205)">
      <line x1="20" y1="80" x2="135" y2="80" stroke="#64748b" stroke-width="1"/>
      <line x1="20" y1="80" x2="20" y2="10" stroke="#64748b" stroke-width="1"/>
      <path d="M 20,80 L 40,80 L 40,15 Q 55,60 75,70 L 75,20 Q 90,60 130,70" fill="none" stroke="#fbbf24" stroke-width="2.5" filter="url(#glow2)"/>
      <text x="77" y="15" fill="#fbbf24" font-family="'JetBrains Mono', monospace" font-size="9.5" font-weight="bold">g_1D ∝ 1/√E</text>
    </g>
  </g>
  <g transform="translate(655, 80)">
    <rect width="205" height="330" rx="8" fill="rgba(15, 23, 42, 0.8)" stroke="#ec4899" stroke-width="1.5"/>
    <text x="102" y="26" fill="#f472b6" font-family="'Sarabun', sans-serif" font-size="13" font-weight="bold" text-anchor="middle">0D จุดควอนตัม (Dot)</text>
    <circle cx="102" cy="115" r="28" fill="#ec4899" opacity="0.8" filter="url(#glow2)"/>
    <circle cx="102" cy="115" r="8" fill="#fdf2f8"/>
    <ellipse cx="102" cy="115" rx="36" ry="12" fill="none" stroke="#f472b6" stroke-width="1" stroke-dasharray="2 2" transform="rotate(30 102 115)"/>
    <g transform="translate(25, 205)">
      <line x1="20" y1="80" x2="150" y2="80" stroke="#64748b" stroke-width="1"/>
      <line x1="20" y1="80" x2="20" y2="10" stroke="#64748b" stroke-width="1"/>
      <line x1="45" y1="80" x2="45" y2="15" stroke="#f472b6" stroke-width="3" filter="url(#glow2)"/>
      <line x1="80" y1="80" x2="80" y2="15" stroke="#f472b6" stroke-width="3" filter="url(#glow2)"/>
      <line x1="115" y1="80" x2="115" y2="15" stroke="#f472b6" stroke-width="3" filter="url(#glow2)"/>
      <line x1="140" y1="80" x2="140" y2="15" stroke="#f472b6" stroke-width="3" filter="url(#glow2)"/>
      <text x="80" y="10" fill="#f472b6" font-family="'JetBrains Mono', monospace" font-size="9.5" font-weight="bold">g_0D = ∑ 2δ(E-E_n)</text>
    </g>
  </g>
</svg>"""

# 3. Chapter 3: 3D ALD & LaMer Crystallization Nucleation
svg_ch03 = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 900 450" width="100%" height="100%">
  <defs>
    <linearGradient id="bgGrad3" x1="0%" y1="0%" x2="100%" y2="100%"><stop offset="0%" stop-color="#020617"/><stop offset="50%" stop-color="#0f172a"/><stop offset="100%" stop-color="#14532d"/></linearGradient>
    <filter id="glow3" x="-20%" y="-20%" width="140%" height="140%"><feGaussianBlur stdDeviation="5" result="blur"/><feComposite in="SourceGraphic" in2="blur" operator="over"/></filter>
  </defs>
  <rect width="900" height="450" rx="12" fill="url(#bgGrad3)" stroke="#334155" stroke-width="1.5"/>
  <g transform="translate(30, 25)">
    <rect width="450" height="32" rx="16" fill="rgba(16, 185, 129, 0.12)" stroke="#10b981" stroke-width="1"/>
    <text x="225" y="21" fill="#34d399" font-family="'JetBrains Mono', monospace" font-size="12" font-weight="bold" text-anchor="middle">FIGURE 3.1 • 3D ALD ATOMIC CYCLE &amp; LAMER CRYSTALLIZATION</text>
  </g>
  <!-- Left: 4-Step ALD Atomic Monolayer Cycle -->
  <g transform="translate(45, 80)">
    <rect width="400" height="330" rx="8" fill="rgba(15, 23, 42, 0.8)" stroke="#10b981" stroke-width="1.5"/>
    <text x="200" y="26" fill="#34d399" font-family="'Sarabun', sans-serif" font-size="13" font-weight="bold" text-anchor="middle">วัฏจักรการสะสมชั้นอะตอม (Atomic Layer Deposition: ALD)</text>
    <!-- Substrate base -->
    <rect x="30" y="240" width="340" height="40" rx="4" fill="#334155" stroke="#64748b"/>
    <text x="200" y="265" fill="#94a3b8" font-family="'JetBrains Mono', monospace" font-size="11" text-anchor="middle">Silicon Substrate (100)</text>
    <!-- Monolayer atoms A & B -->
    <g transform="translate(30, 220)">
      <circle cx="20" cy="0" r="10" fill="#3b82f6" filter="url(#glow3)"/><circle cx="60" cy="0" r="10" fill="#f43f5e"/>
      <circle cx="100" cy="0" r="10" fill="#3b82f6"/><circle cx="140" cy="0" r="10" fill="#f43f5e"/>
      <circle cx="180" cy="0" r="10" fill="#3b82f6"/><circle cx="220" cy="0" r="10" fill="#f43f5e"/>
      <circle cx="260" cy="0" r="10" fill="#3b82f6"/><circle cx="300" cy="0" r="10" fill="#f43f5e"/>
      <circle cx="340" cy="0" r="10" fill="#3b82f6"/>
    </g>
    <!-- Precursor Pulses Graphic -->
    <g transform="translate(40, 55)">
      <rect x="0" y="0" width="70" height="60" rx="4" fill="#1e293b" stroke="#3b82f6"/>
      <text x="35" y="25" fill="#38bdf8" font-size="9" text-anchor="middle" font-weight="bold">1. Pulse A</text>
      <text x="35" y="45" fill="#94a3b8" font-size="8" text-anchor="middle">TMA Precursor</text>
      <line x1="75" y1="30" x2="90" y2="30" stroke="#facc15" stroke-width="2"/>
      <rect x="95" y="0" width="70" height="60" rx="4" fill="#1e293b" stroke="#64748b"/>
      <text x="130" y="25" fill="#e2e8f0" font-size="9" text-anchor="middle" font-weight="bold">2. Purge N₂</text>
      <text x="130" y="45" fill="#94a3b8" font-size="8" text-anchor="middle">Remove Excess</text>
      <line x1="170" y1="30" x2="185" y2="30" stroke="#facc15" stroke-width="2"/>
      <rect x="190" y="0" width="70" height="60" rx="4" fill="#1e293b" stroke="#f43f5e"/>
      <text x="225" y="25" fill="#f87171" font-size="9" text-anchor="middle" font-weight="bold">3. Pulse B</text>
      <text x="225" y="45" fill="#94a3b8" font-size="8" text-anchor="middle">H₂O Vapor</text>
      <line x1="265" y1="30" x2="280" y2="30" stroke="#facc15" stroke-width="2"/>
      <rect x="285" y="0" width="70" height="60" rx="4" fill="#1e293b" stroke="#10b981"/>
      <text x="320" y="25" fill="#34d399" font-size="9" text-anchor="middle" font-weight="bold">4. Al₂O₃ Layer</text>
      <text x="320" y="45" fill="#94a3b8" font-size="8" text-anchor="middle">~0.1 nm/Cycle</text>
    </g>
    <text x="200" y="310" fill="#34d399" font-family="'JetBrains Mono', monospace" font-size="10.5" font-weight="bold" text-anchor="middle">Self-Limiting Surface Reaction: 100% Conformality</text>
  </g>
  <!-- Right: LaMer Nucleation Diagram -->
  <g transform="translate(470, 80)">
    <rect width="390" height="330" rx="8" fill="rgba(15, 23, 42, 0.8)" stroke="#f59e0b" stroke-width="1.5"/>
    <text x="195" y="26" fill="#fbbf24" font-family="'Sarabun', sans-serif" font-size="13" font-weight="bold" text-anchor="middle">ทฤษฎีการเกิดนิวเคลียสและการเติบโต (LaMer Model)</text>
    <line x1="50" y1="260" x2="350" y2="260" stroke="#64748b" stroke-width="1.5"/>
    <line x1="50" y1="260" x2="50" y2="50" stroke="#64748b" stroke-width="1.5"/>
    <!-- Saturation thresholds -->
    <line x1="50" y1="180" x2="350" y2="180" stroke="#64748b" stroke-dasharray="3 3"/>
    <text x="40" y="184" fill="#94a3b8" font-size="9" text-anchor="end">C_s</text>
    <line x1="50" y1="100" x2="350" y2="100" stroke="#f43f5e" stroke-dasharray="3 3"/>
    <text x="40" y="104" fill="#f87171" font-size="9" text-anchor="end">C_min</text>
    <!-- LaMer Curve -->
    <path d="M 50,250 Q 90,220 120,80 Q 150,70 170,120 Q 230,160 340,175" fill="none" stroke="#facc15" stroke-width="3" filter="url(#glow3)"/>
    <!-- Regions -->
    <rect x="50" y="50" width="70" height="210" fill="rgba(59, 130, 246, 0.08)"/>
    <text x="85" y="70" fill="#60a5fa" font-size="9" text-anchor="middle">I. Prenucleation</text>
    <rect x="120" y="50" width="50" height="210" fill="rgba(244, 63, 94, 0.15)"/>
    <text x="145" y="70" fill="#f87171" font-size="9" text-anchor="middle">II. Burst</text>
    <rect x="170" y="50" width="180" height="210" fill="rgba(16, 185, 129, 0.08)"/>
    <text x="260" y="70" fill="#34d399" font-size="9" text-anchor="middle">III. Diffusion-Controlled Growth</text>
    <text x="195" y="310" fill="#facc15" font-family="'JetBrains Mono', monospace" font-size="10.5" font-weight="bold" text-anchor="middle">Monodisperse Nanocrystal Synthesis</text>
  </g>
</svg>"""

# 4. Chapter 4: 3D STM & AFM Metrology
svg_ch04 = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 900 450" width="100%" height="100%">
  <defs>
    <linearGradient id="bgGrad4" x1="0%" y1="0%" x2="100%" y2="100%"><stop offset="0%" stop-color="#020617"/><stop offset="50%" stop-color="#0f172a"/><stop offset="100%" stop-color="#312e81"/></linearGradient>
    <filter id="glow4" x="-20%" y="-20%" width="140%" height="140%"><feGaussianBlur stdDeviation="6" result="blur"/><feComposite in="SourceGraphic" in2="blur" operator="over"/></filter>
  </defs>
  <rect width="900" height="450" rx="12" fill="url(#bgGrad4)" stroke="#334155" stroke-width="1.5"/>
  <g transform="translate(30, 25)">
    <rect width="450" height="32" rx="16" fill="rgba(99, 102, 241, 0.12)" stroke="#6366f1" stroke-width="1"/>
    <text x="225" y="21" fill="#818cf8" font-family="'JetBrains Mono', monospace" font-size="12" font-weight="bold" text-anchor="middle">FIGURE 4.1 • 3D STM QUANTUM TUNNELING &amp; AFM DEFLECTION</text>
  </g>
  <!-- Left: 3D STM Tunneling Tip -->
  <g transform="translate(50, 80)">
    <rect width="380" height="330" rx="8" fill="rgba(15, 23, 42, 0.8)" stroke="#38bdf8" stroke-width="1.5"/>
    <text x="190" y="26" fill="#38bdf8" font-family="'Sarabun', sans-serif" font-size="13" font-weight="bold" text-anchor="middle">กล้องจุลทรรศน์ส่องกราดแบบอุโมงค์ (STM Tip &amp; Tunneling)</text>
    <!-- Piezo Scanner Tube -->
    <rect x="160" y="45" width="60" height="50" fill="#475569" stroke="#94a3b8"/>
    <text x="190" y="75" fill="#f8fafc" font-size="9" text-anchor="middle" font-weight="bold">Piezo XYZ</text>
    <!-- Sharp Metallic Tip -->
    <polygon points="170,95 210,95 190,165" fill="#94a3b8" stroke="#cbd5e1"/>
    <circle cx="190" cy="165" r="4" fill="#00f0ff" filter="url(#glow4)"/>
    <!-- Tunneling Current Beam -->
    <line x1="190" y1="165" x2="190" y2="195" stroke="#00f0ff" stroke-width="3" stroke-dasharray="2 2" filter="url(#glow4)"/>
    <!-- Atomic Surface -->
    <g transform="translate(40, 205)">
      <circle cx="30" cy="0" r="14" fill="#eab308"/><circle cx="60" cy="0" r="14" fill="#eab308"/><circle cx="90" cy="0" r="14" fill="#eab308"/>
      <circle cx="120" cy="0" r="14" fill="#eab308"/><circle cx="150" cy="0" r="14" fill="#facc15" filter="url(#glow4)"/><circle cx="180" cy="0" r="14" fill="#eab308"/>
      <circle cx="210" cy="0" r="14" fill="#eab308"/><circle cx="240" cy="0" r="14" fill="#eab308"/><circle cx="270" cy="0" r="14" fill="#eab308"/>
    </g>
    <text x="190" y="270" fill="#38bdf8" font-family="'JetBrains Mono', monospace" font-size="12" font-weight="bold" text-anchor="middle">I ∝ V_bias exp(-2κ d) • κ = √(2mΦ)/ℏ</text>
    <text x="190" y="295" fill="#cbd5e1" font-family="'Sarabun', sans-serif" font-size="10" text-anchor="middle">ความละเอียดทางดิ่งระดับ 0.01 nm (Sub-Angstrom)</text>
  </g>
  <!-- Right: 3D AFM Cantilever & Laser Detector -->
  <g transform="translate(470, 80)">
    <rect width="380" height="330" rx="8" fill="rgba(15, 23, 42, 0.8)" stroke="#818cf8" stroke-width="1.5"/>
    <text x="190" y="26" fill="#818cf8" font-family="'Sarabun', sans-serif" font-size="13" font-weight="bold" text-anchor="middle">กล้องจุลทรรศน์แรงอะตอม (AFM Optical Lever System)</text>
    <!-- Laser diode -->
    <rect x="50" y="50" width="45" height="30" rx="4" fill="#f43f5e"/>
    <text x="72" y="70" fill="#ffffff" font-size="9" text-anchor="middle" font-weight="bold">Laser</text>
    <!-- Photodiode Detector -->
    <rect x="280" y="50" width="55" height="40" rx="4" fill="#1e293b" stroke="#10b981" stroke-width="2"/>
    <text x="307" y="75" fill="#34d399" font-size="9" text-anchor="middle" font-weight="bold">4-Quadrant</text>
    <!-- Cantilever -->
    <polygon points="120,150 240,150 240,140 120,140" fill="#64748b"/>
    <polygon points="230,150 240,150 235,180" fill="#94a3b8"/>
    <!-- Laser beam paths -->
    <line x1="95" y1="65" x2="235" y2="140" stroke="#f43f5e" stroke-width="2" filter="url(#glow4)"/>
    <line x1="235" y1="140" x2="280" y2="70" stroke="#f43f5e" stroke-width="2" filter="url(#glow4)"/>
    <!-- Sample surface -->
    <path d="M 50,205 Q 120,190 180,210 T 330,195" fill="none" stroke="#e2e8f0" stroke-width="4"/>
    <text x="190" y="270" fill="#818cf8" font-family="'JetBrains Mono', monospace" font-size="12" font-weight="bold" text-anchor="middle">F = -k_c Δz • Hooke's Law &amp; Lennard-Jones</text>
    <text x="190" y="295" fill="#cbd5e1" font-family="'Sarabun', sans-serif" font-size="10" text-anchor="middle">โหมด Contact, Non-Contact, Tapping &amp; KPFM</text>
  </g>
</svg>"""

# 5. Chapter 5
svg_ch05 = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 900 450" width="100%" height="100%">
  <defs>
    <linearGradient id="bgGrad5" x1="0%" y1="0%" x2="100%" y2="100%"><stop offset="0%" stop-color="#030712"/><stop offset="50%" stop-color="#0f172a"/><stop offset="100%" stop-color="#1e1b4b"/></linearGradient>
    <linearGradient id="diracGradUpper" x1="0%" y1="0%" x2="0%" y2="100%"><stop offset="0%" stop-color="#38bdf8"/><stop offset="100%" stop-color="#0284c7"/></linearGradient>
    <linearGradient id="diracGradLower" x1="0%" y1="0%" x2="0%" y2="100%"><stop offset="0%" stop-color="#a855f7"/><stop offset="100%" stop-color="#6b21a8"/></linearGradient>
    <filter id="glow5" x="-20%" y="-20%" width="140%" height="140%"><feGaussianBlur stdDeviation="6" result="blur"/><feComposite in="SourceGraphic" in2="blur" operator="over"/></filter>
  </defs>
  <rect width="900" height="450" rx="12" fill="url(#bgGrad5)" stroke="#334155" stroke-width="1.5"/>
  <g transform="translate(30, 25)">
    <rect width="480" height="32" rx="16" fill="rgba(56, 189, 248, 0.12)" stroke="#38bdf8" stroke-width="1"/>
    <text x="240" y="21" fill="#38bdf8" font-family="'JetBrains Mono', monospace" font-size="12" font-weight="bold" text-anchor="middle">FIGURE 5.1 • 3D GRAPHENE HONEYCOMB LATTICE &amp; DIRAC CONE PHYSICS</text>
  </g>
  <g transform="translate(50, 85)">
    <rect width="380" height="325" rx="8" fill="rgba(15, 23, 42, 0.75)" stroke="#0284c7" stroke-width="1.5"/>
    <text x="190" y="26" fill="#38bdf8" font-family="'Sarabun', sans-serif" font-size="13" font-weight="700" text-anchor="middle">โครงตาข่ายรังผึ้งกราฟีน (Honeycomb Lattice &amp; Sublattices A, B)</text>
    <g transform="translate(50, 50)" stroke="#38bdf8" stroke-width="2" fill="none">
      <polygon points="60,30 90,45 90,75 60,90 30,75 30,45"/>
      <polygon points="120,30 150,45 150,75 120,90 90,75 90,45"/>
      <polygon points="180,30 210,45 210,75 180,90 150,75 150,45"/>
      <polygon points="90,75 120,90 120,120 90,135 60,120 60,90"/>
      <polygon points="150,75 180,90 180,120 150,135 120,120 120,90"/>
      <polygon points="210,75 240,90 240,120 210,135 180,120 180,90"/>
    </g>
    <g transform="translate(50, 50)">
      <circle cx="60" cy="30" r="6" fill="#00f0ff" filter="url(#glow5)"/><circle cx="90" cy="45" r="6" fill="#f43f5e" filter="url(#glow5)"/>
      <circle cx="90" cy="75" r="6" fill="#00f0ff"/><circle cx="60" cy="90" r="6" fill="#f43f5e"/><circle cx="30" cy="75" r="6" fill="#00f0ff"/><circle cx="30" cy="45" r="6" fill="#f43f5e"/>
      <circle cx="120" cy="30" r="6" fill="#f43f5e"/><circle cx="150" cy="45" r="6" fill="#00f0ff"/><circle cx="150" cy="75" r="6" fill="#f43f5e"/><circle cx="120" cy="90" r="6" fill="#00f0ff"/>
    </g>
    <text x="190" y="270" fill="#facc15" font-family="'JetBrains Mono', monospace" font-size="11" font-weight="bold" text-anchor="middle">a = √3 a_cc = 0.246 nm • a_cc = 0.142 nm</text>
    <text x="190" y="295" fill="#cbd5e1" font-family="'Sarabun', sans-serif" font-size="10.5" text-anchor="middle"><tspan fill="#00f0ff">● ซับแลตทิซ A</tspan> และ <tspan fill="#f43f5e">● ซับแลตทิซ B</tspan> สร้างสมมาตรอินเวอร์ชัน</text>
  </g>
  <g transform="translate(460, 85)">
    <rect width="390" height="325" rx="8" fill="rgba(15, 23, 42, 0.75)" stroke="#a855f7" stroke-width="1.5"/>
    <text x="195" y="26" fill="#c084fc" font-family="'Sarabun', sans-serif" font-size="13" font-weight="700" text-anchor="middle">ความสัมพันธ์การกระจายพลังงานรูปกรวยดิแรค (3D Dirac Cone)</text>
    <g transform="translate(195, 155)">
      <polygon points="0,0 -85,-85 85,-85" fill="url(#diracGradUpper)" opacity="0.85" filter="url(#glow5)"/>
      <ellipse cx="0" cy="-85" rx="85" ry="22" fill="#38bdf8" opacity="0.6"/>
      <polygon points="0,0 -85,85 85,85" fill="url(#diracGradLower)" opacity="0.85" filter="url(#glow5)"/>
      <ellipse cx="0" cy="85" rx="85" ry="22" fill="#a855f7" opacity="0.6"/>
      <circle cx="0" cy="0" r="5" fill="#facc15" filter="url(#glow5)"/>
      <text x="12" y="4" fill="#facc15" font-family="'JetBrains Mono', monospace" font-size="11" font-weight="bold">K (Dirac Point)</text>
      <line x1="0" y1="-105" x2="0" y2="105" stroke="#f8fafc" stroke-width="1.5" stroke-dasharray="3 3"/>
      <text x="-15" y="-95" fill="#38bdf8" font-family="'JetBrains Mono', monospace" font-size="11" font-weight="bold">+E (π*)</text>
      <text x="-15" y="105" fill="#c084fc" font-family="'JetBrains Mono', monospace" font-size="11" font-weight="bold">-E (π)</text>
    </g>
    <text x="195" y="270" fill="#38bdf8" font-family="'JetBrains Mono', monospace" font-size="12" font-weight="bold" text-anchor="middle">E(q) = ± ℏ v_F |q| • v_F ≈ 10⁶ m/s</text>
    <text x="195" y="295" fill="#cbd5e1" font-family="'Sarabun', sans-serif" font-size="10.5" text-anchor="middle">อิเล็กตรอนประพฤติตนเสมือนอนุภาคไร้มวล (Massless Dirac Fermions)</text>
  </g>
</svg>"""

# 6. Chapter 6: 3D GAAFET Nanosheet & Spintronics STT-MRAM
svg_ch06 = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 900 450" width="100%" height="100%">
  <defs>
    <linearGradient id="bgGrad6" x1="0%" y1="0%" x2="100%" y2="100%"><stop offset="0%" stop-color="#020617"/><stop offset="50%" stop-color="#0f172a"/><stop offset="100%" stop-color="#1e1b4b"/></linearGradient>
    <filter id="glow6" x="-20%" y="-20%" width="140%" height="140%"><feGaussianBlur stdDeviation="5" result="blur"/><feComposite in="SourceGraphic" in2="blur" operator="over"/></filter>
  </defs>
  <rect width="900" height="450" rx="12" fill="url(#bgGrad6)" stroke="#334155" stroke-width="1.5"/>
  <g transform="translate(30, 25)">
    <rect width="460" height="32" rx="16" fill="rgba(245, 158, 11, 0.12)" stroke="#f59e0b" stroke-width="1"/>
    <text x="230" y="21" fill="#fbbf24" font-family="'JetBrains Mono', monospace" font-size="12" font-weight="bold" text-anchor="middle">FIGURE 6.1 • 3D GAAFET NANOSHEET &amp; SPINTRONICS MTJ STACK</text>
  </g>
  <!-- Left: 3D Gate-All-Around FET -->
  <g transform="translate(50, 80)">
    <rect width="380" height="330" rx="8" fill="rgba(15, 23, 42, 0.8)" stroke="#3b82f6" stroke-width="1.5"/>
    <text x="190" y="26" fill="#60a5fa" font-family="'Sarabun', sans-serif" font-size="13" font-weight="bold" text-anchor="middle">ทรานซิสเตอร์นาโนชีตโอบรอบ (Gate-All-Around: GAAFET)</text>
    <!-- Gate metal wrapper -->
    <rect x="80" y="55" width="220" height="150" rx="8" fill="rgba(245, 158, 11, 0.25)" stroke="#f59e0b" stroke-width="2"/>
    <text x="190" y="75" fill="#facc15" font-family="'JetBrains Mono', monospace" font-size="10" font-weight="bold" text-anchor="middle">Gate Metal &amp; High-k Dielectric (HfO₂)</text>
    <!-- 3 Stacked Si Nanosheets -->
    <rect x="50" y="90" width="280" height="18" rx="4" fill="#38bdf8" stroke="#e0f2fe" filter="url(#glow6)"/>
    <rect x="50" y="125" width="280" height="18" rx="4" fill="#38bdf8" stroke="#e0f2fe" filter="url(#glow6)"/>
    <rect x="50" y="160" width="280" height="18" rx="4" fill="#38bdf8" stroke="#e0f2fe" filter="url(#glow6)"/>
    <text x="60" y="103" fill="#0f172a" font-size="8" font-weight="bold">Si Nanosheet 1</text>
    <text x="60" y="138" fill="#0f172a" font-size="8" font-weight="bold">Si Nanosheet 2</text>
    <text x="60" y="173" fill="#0f172a" font-size="8" font-weight="bold">Si Nanosheet 3</text>
    <text x="190" y="270" fill="#38bdf8" font-family="'JetBrains Mono', monospace" font-size="11.5" font-weight="bold" text-anchor="middle">SS = 65 mV/dec • I_on/I_off &gt; 10⁷</text>
    <text x="190" y="295" fill="#cbd5e1" font-family="'Sarabun', sans-serif" font-size="10" text-anchor="middle">สนามไฟฟ้าเกตโอบล้อม 4 ทิศทาง ยุติปัญหา Short-Channel Effect</text>
  </g>
  <!-- Right: 3D STT-MRAM Magnetic Tunnel Junction -->
  <g transform="translate(470, 80)">
    <rect width="380" height="330" rx="8" fill="rgba(15, 23, 42, 0.8)" stroke="#f43f5e" stroke-width="1.5"/>
    <text x="190" y="26" fill="#f87171" font-family="'Sarabun', sans-serif" font-size="13" font-weight="bold" text-anchor="middle">หัวต่ออุโมงค์แม่เหล็ก (Magnetic Tunnel Junction: MTJ)</text>
    <!-- Free Layer -->
    <rect x="90" y="55" width="200" height="35" rx="4" fill="#f43f5e"/>
    <text x="190" y="77" fill="#ffffff" font-size="10" font-weight="bold" text-anchor="middle">Free Magnetic Layer (CoFeB) ⇄</text>
    <!-- Tunnel Barrier -->
    <rect x="90" y="95" width="200" height="20" rx="2" fill="#e2e8f0" stroke="#94a3b8"/>
    <text x="190" y="110" fill="#0f172a" font-size="9" font-weight="bold" text-anchor="middle">Tunnel Barrier (MgO ~1 nm)</text>
    <!-- Pinned Layer -->
    <rect x="90" y="120" width="200" height="35" rx="4" fill="#3b82f6"/>
    <text x="190" y="142" fill="#ffffff" font-size="10" font-weight="bold" text-anchor="middle">Pinned Reference Layer (CoFe) →</text>
    <!-- Spin current arrow -->
    <line x1="190" y1="165" x2="190" y2="215" stroke="#facc15" stroke-width="3" stroke-dasharray="3 3" filter="url(#glow6)"/>
    <text x="210" y="195" fill="#facc15" font-size="10" font-weight="bold">Spin Torque</text>
    <text x="190" y="270" fill="#f87171" font-family="'JetBrains Mono', monospace" font-size="11.5" font-weight="bold" text-anchor="middle">TMR = (R_AP - R_P)/R_P × 100% &gt; 200%</text>
    <text x="190" y="295" fill="#cbd5e1" font-family="'Sarabun', sans-serif" font-size="10" text-anchor="middle">สลับทิศทางแม่เหล็กด้วยการถ่ายโอนทอร์กของสปิน (STT Switching)</text>
  </g>
</svg>"""

# 7. Chapter 7: 3D Nanomedicine, Lipid Nanoparticles & DNA Origami
svg_ch07 = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 900 450" width="100%" height="100%">
  <defs>
    <linearGradient id="bgGrad7" x1="0%" y1="0%" x2="100%" y2="100%"><stop offset="0%" stop-color="#020617"/><stop offset="50%" stop-color="#0f172a"/><stop offset="100%" stop-color="#042f2e"/></linearGradient>
    <filter id="glow7" x="-20%" y="-20%" width="140%" height="140%"><feGaussianBlur stdDeviation="5" result="blur"/><feComposite in="SourceGraphic" in2="blur" operator="over"/></filter>
  </defs>
  <rect width="900" height="450" rx="12" fill="url(#bgGrad7)" stroke="#334155" stroke-width="1.5"/>
  <g transform="translate(30, 25)">
    <rect width="470" height="32" rx="16" fill="rgba(20, 184, 166, 0.12)" stroke="#14b8a6" stroke-width="1"/>
    <text x="235" y="21" fill="#2dd4bf" font-family="'JetBrains Mono', monospace" font-size="12" font-weight="bold" text-anchor="middle">FIGURE 7.1 • 3D LIPID NANOPARTICLE (LNP) &amp; DNA ORIGAMI NANOROBOT</text>
  </g>
  <!-- Left: 3D LNP Cutaway Structure -->
  <g transform="translate(50, 80)">
    <rect width="380" height="330" rx="8" fill="rgba(15, 23, 42, 0.8)" stroke="#14b8a6" stroke-width="1.5"/>
    <text x="190" y="26" fill="#2dd4bf" font-family="'Sarabun', sans-serif" font-size="13" font-weight="bold" text-anchor="middle">อนุภาคนาโนไขมันนำส่งยา (Lipid Nanoparticle: LNP)</text>
    <!-- LNP Outer Lipid Bilayer Sphere -->
    <circle cx="190" cy="130" r="75" fill="none" stroke="#2dd4bf" stroke-width="12" opacity="0.85"/>
    <circle cx="190" cy="130" r="60" fill="rgba(20, 184, 166, 0.2)"/>
    <!-- Encapsulated mRNA Helices -->
    <path d="M 150,110 Q 170,140 190,120 T 230,150" fill="none" stroke="#f43f5e" stroke-width="3.5" filter="url(#glow7)"/>
    <path d="M 160,140 Q 180,110 200,140 T 220,120" fill="none" stroke="#facc15" stroke-width="3" filter="url(#glow7)"/>
    <!-- Outer PEG & Targeting Ligands -->
    <g transform="translate(190, 130)">
      <line x1="0" y1="-75" x2="0" y2="-95" stroke="#38bdf8" stroke-width="2"/>
      <circle cx="0" cy="-95" r="4" fill="#38bdf8"/>
      <line x1="75" y1="0" x2="95" y2="0" stroke="#a855f7" stroke-width="2"/>
      <circle cx="95" cy="0" r="4" fill="#a855f7"/>
      <line x1="-75" y1="0" x2="-95" y2="0" stroke="#38bdf8" stroke-width="2"/>
      <circle cx="-95" cy="0" r="4" fill="#38bdf8"/>
    </g>
    <text x="190" y="270" fill="#2dd4bf" font-family="'JetBrains Mono', monospace" font-size="11.5" font-weight="bold" text-anchor="middle">mRNA Encapsulation Efficiency &gt; 95%</text>
    <text x="190" y="295" fill="#cbd5e1" font-family="'Sarabun', sans-serif" font-size="10" text-anchor="middle">ลิพิดประจุบวกไอออไนซ์ได้ ปลดปล่อยยีนเมื่อเข้าสู่เอนโดโซม pH ต่ำ</text>
  </g>
  <!-- Right: 3D DNA Origami Nanorobot -->
  <g transform="translate(470, 80)">
    <rect width="380" height="330" rx="8" fill="rgba(15, 23, 42, 0.8)" stroke="#f43f5e" stroke-width="1.5"/>
    <text x="190" y="26" fill="#f87171" font-family="'Sarabun', sans-serif" font-size="13" font-weight="bold" text-anchor="middle">หุ่นยนต์นาโนดีเอ็นเอออริกามิ (DNA Origami Nanorobot)</text>
    <!-- Barrel Hexagonal Box -->
    <polygon points="190,60 260,100 260,170 190,210 120,170 120,100" fill="rgba(244, 63, 94, 0.2)" stroke="#f43f5e" stroke-width="2" stroke-dasharray="3 3"/>
    <!-- DNA Staple strands bundle -->
    <line x1="140" y1="110" x2="240" y2="110" stroke="#facc15" stroke-width="3" filter="url(#glow7)"/>
    <line x1="130" y1="135" x2="250" y2="135" stroke="#38bdf8" stroke-width="3" filter="url(#glow7)"/>
    <line x1="140" y1="160" x2="240" y2="160" stroke="#10b981" stroke-width="3" filter="url(#glow7)"/>
    <!-- Aptamer Locks -->
    <circle cx="120" cy="135" r="7" fill="#facc15" filter="url(#glow7)"/>
    <text x="110" y="138" fill="#facc15" font-size="8" text-anchor="end" font-weight="bold">Aptamer Lock</text>
    <circle cx="260" cy="135" r="7" fill="#facc15" filter="url(#glow7)"/>
    <text x="270" y="138" fill="#facc15" font-size="8" font-anchor="start" font-weight="bold">Target Key</text>
    <text x="190" y="270" fill="#f87171" font-family="'JetBrains Mono', monospace" font-size="11.5" font-weight="bold" text-anchor="middle">Smart Payloaded Nanorobotics</text>
    <text x="190" y="295" fill="#cbd5e1" font-family="'Sarabun', sans-serif" font-size="10" text-anchor="middle">ปลดล็อกฝากล่องปล่อยสารเคมีบำบัดเฉพาะเมื่อจับกับแอนติเจนบนผิวมะเร็ง</text>
  </g>
</svg>"""

# 8. Chapter 8: 3D Perovskite Octahedral Cage & Z-Scheme Water Splitting
svg_ch08 = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 900 450" width="100%" height="100%">
  <defs>
    <linearGradient id="bgGrad8" x1="0%" y1="0%" x2="100%" y2="100%"><stop offset="0%" stop-color="#020617"/><stop offset="50%" stop-color="#0f172a"/><stop offset="100%" stop-color="#1e3a8a"/></linearGradient>
    <filter id="glow8" x="-20%" y="-20%" width="140%" height="140%"><feGaussianBlur stdDeviation="5" result="blur"/><feComposite in="SourceGraphic" in2="blur" operator="over"/></filter>
  </defs>
  <rect width="900" height="450" rx="12" fill="url(#bgGrad8)" stroke="#334155" stroke-width="1.5"/>
  <g transform="translate(30, 25)">
    <rect width="470" height="32" rx="16" fill="rgba(59, 130, 246, 0.12)" stroke="#3b82f6" stroke-width="1"/>
    <text x="235" y="21" fill="#60a5fa" font-family="'JetBrains Mono', monospace" font-size="12" font-weight="bold" text-anchor="middle">FIGURE 8.1 • 3D PEROVSKITE ABX3 LATTICE &amp; Z-SCHEME WATER SPLITTING</text>
  </g>
  <!-- Left: 3D Perovskite Unit Cell ABX3 -->
  <g transform="translate(50, 80)">
    <rect width="380" height="330" rx="8" fill="rgba(15, 23, 42, 0.8)" stroke="#facc15" stroke-width="1.5"/>
    <text x="190" y="26" fill="#facc15" font-family="'Sarabun', sans-serif" font-size="13" font-weight="bold" text-anchor="middle">โครงสร้างผลึกเพอรอฟสไกต์ (Perovskite ABX₃ Unit Cell)</text>
    <!-- Isometric Unit Cell Box -->
    <g transform="translate(90, 45)">
      <!-- Octahedron BX6 -->
      <polygon points="100,20 160,60 100,100 40,60" fill="rgba(56, 189, 248, 0.4)" stroke="#38bdf8"/>
      <polygon points="100,100 160,60 160,140 100,180" fill="rgba(2, 132, 199, 0.5)" stroke="#38bdf8"/>
      <polygon points="100,100 40,60 40,140 100,180" fill="rgba(3, 105, 161, 0.6)" stroke="#38bdf8"/>
      <!-- B cation (Pb2+) center -->
      <circle cx="100" cy="100" r="10" fill="#3b82f6" filter="url(#glow8)"/>
      <!-- A cations (Cs+ / MA+) at corners -->
      <circle cx="20" cy="30" r="12" fill="#eab308"/><circle cx="180" cy="30" r="12" fill="#eab308"/>
      <circle cx="20" cy="170" r="12" fill="#eab308"/><circle cx="180" cy="170" r="12" fill="#eab308"/>
      <!-- X anions (I-, Br-) at faces -->
      <circle cx="100" cy="20" r="7" fill="#f43f5e"/><circle cx="100" cy="180" r="7" fill="#f43f5e"/>
      <circle cx="40" cy="100" r="7" fill="#f43f5e"/><circle cx="160" cy="100" r="7" fill="#f43f5e"/>
    </g>
    <text x="190" y="270" fill="#facc15" font-family="'JetBrains Mono', monospace" font-size="11.5" font-weight="bold" text-anchor="middle">Tolerance Factor: t = (r_A + r_X)/[√2(r_B + r_X)]</text>
    <text x="190" y="295" fill="#cbd5e1" font-family="'Sarabun', sans-serif" font-size="10" text-anchor="middle">ประสิทธิภาพเซลล์แสงอาทิตย์ (PCE) ทะลุ 26.1% (Tandem &gt; 33%)</text>
  </g>
  <!-- Right: Z-Scheme Photocatalytic Water Splitting -->
  <g transform="translate(470, 80)">
    <rect width="380" height="330" rx="8" fill="rgba(15, 23, 42, 0.8)" stroke="#10b981" stroke-width="1.5"/>
    <text x="190" y="26" fill="#34d399" font-family="'Sarabun', sans-serif" font-size="13" font-weight="bold" text-anchor="middle">การเร่งปฏิกิริยาด้วยแสงสองขั้นตอน (Z-Scheme Photocatalysis)</text>
    <!-- Photocatalyst 1 (Oxygen Evolution) -->
    <rect x="70" y="60" width="85" height="130" rx="6" fill="#1e293b" stroke="#3b82f6" stroke-width="1.5"/>
    <text x="112" y="80" fill="#60a5fa" font-size="9" text-anchor="middle" font-weight="bold">PS I (BiVO₄)</text>
    <text x="112" y="105" fill="#38bdf8" font-size="8.5" text-anchor="middle">CB: +0.4V</text>
    <text x="112" y="170" fill="#38bdf8" font-size="8.5" text-anchor="middle">VB: +2.8V</text>
    <text x="112" y="185" fill="#f43f5e" font-size="8" text-anchor="middle">O₂ + 4H⁺ ← H₂O</text>
    <!-- Electron Mediator Shunt -->
    <path d="M 155,100 L 225,160" stroke="#facc15" stroke-width="3" stroke-dasharray="3 3" filter="url(#glow8)"/>
    <text x="190" y="125" fill="#facc15" font-size="9" text-anchor="middle" font-weight="bold">e⁻ Transfer</text>
    <!-- Photocatalyst 2 (Hydrogen Evolution) -->
    <rect x="225" y="40" width="85" height="130" rx="6" fill="#1e293b" stroke="#10b981" stroke-width="1.5"/>
    <text x="267" y="60" fill="#34d399" font-size="9" text-anchor="middle" font-weight="bold">PS II (g-C₃N₄)</text>
    <text x="267" y="85" fill="#10b981" font-size="8.5" text-anchor="middle">CB: -0.8V</text>
    <text x="267" y="100" fill="#facc15" font-size="8" text-anchor="middle">2H⁺ + 2e⁻ → H₂</text>
    <text x="267" y="150" fill="#10b981" font-size="8.5" text-anchor="middle">VB: +1.9V</text>
    <text x="190" y="270" fill="#34d399" font-family="'JetBrains Mono', monospace" font-size="11.5" font-weight="bold" text-anchor="middle">Overall Solar Water Splitting: 2H₂O → 2H₂ + O₂</text>
    <text x="190" y="295" fill="#cbd5e1" font-family="'Sarabun', sans-serif" font-size="10" text-anchor="middle">การแยกน้ำด้วยแสงอาทิตย์เลียนแบบการสังเคราะห์แสงธรรมชาติ</text>
  </g>
</svg>"""

files = [
    ("ch01_3d_nanoscale_hierarchy.svg", svg_ch01),
    ("ch02_3d_quantum_confinement_states.svg", svg_ch02),
    ("ch03_3d_ald_lamer_nanofab.svg", svg_ch03),
    ("ch04_3d_stm_afm_metrology_probe.svg", svg_ch04),
    ("ch05_3d_carbon_allotropes_dirac.svg", svg_ch05),
    ("ch06_3d_gaafet_plasmonics_stt.svg", svg_ch06),
    ("ch07_3d_nanomedicine_delivery_origami.svg", svg_ch07),
    ("ch08_3d_perovskite_photocatalysis_solar.svg", svg_ch08),
]

for fname, content in files:
    p1 = os.path.join(DIAGRAMS_DIR_1, fname)
    p2 = os.path.join(DIAGRAMS_DIR_2, fname)
    with open(p1, "w", encoding="utf-8") as f:
        f.write(content)
    with open(p2, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"✅ Generated 3D SVG: {fname}")

print("🎉 All 8 Chapter 3D SVG Vector illustrations generated successfully!")
