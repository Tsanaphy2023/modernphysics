#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generates 100% Vector Crispness SVG Infographic Diagrams for Nanotechnological Physics Textbook & Lab Manual.
"""

import os

SVG_DIR = "/Users/chewathassana/Downloads/manus_backup2026/ModernPhysics/nanotechnology/textbook_and_lab_manual_2026/assets/diagrams"
os.makedirs(SVG_DIR, exist_ok=True)

# ------------------------------------------------------------------------------
# 1. ch01_scale_and_surface.svg
# ------------------------------------------------------------------------------
svg_ch01 = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 900 420" width="100%" height="100%">
  <defs>
    <linearGradient id="bgGrad1" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#090e1a"/>
      <stop offset="100%" stop-color="#0f172a"/>
    </linearGradient>
    <linearGradient id="boxGrad1" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0284c7"/>
      <stop offset="100%" stop-color="#00f0ff"/>
    </linearGradient>
    <filter id="glow1">
      <feGaussianBlur stdDeviation="3" result="coloredBlur"/>
      <feMerge>
        <feMergeNode in="coloredBlur"/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>
  </defs>

  <!-- Background Card -->
  <rect width="900" height="420" rx="16" fill="url(#bgGrad1)" stroke="#00f0ff" stroke-opacity="0.35" stroke-width="1.5"/>

  <!-- Title -->
  <text x="450" y="38" text-anchor="middle" font-family="'Sarabun', sans-serif" font-size="18" font-weight="700" fill="#38bdf8" letter-spacing="0.5">
    แผนผังเปรียบเทียบมาตราส่วนความยาวและสัดส่วนพื้นที่ผิวต่อปริมาตร (Specific Surface Area)
  </text>
  <line x1="60" y1="52" x2="840" y2="52" stroke="#334155" stroke-width="1"/>

  <!-- Macro Scale Cube (1 cm) -->
  <g transform="translate(100, 90)">
    <rect width="140" height="140" fill="#1e293b" stroke="#64748b" stroke-width="2" rx="8"/>
    <!-- 3D Cube illusion -->
    <path d="M 0 0 L 30 -25 L 170 -25 L 140 0 Z" fill="#334155" stroke="#64748b" stroke-width="1.5"/>
    <path d="M 140 0 L 170 -25 L 170 115 L 140 140 Z" fill="#1e293b" stroke="#64748b" stroke-width="1.5"/>
    <text x="70" y="75" text-anchor="middle" font-family="'JetBrains Mono', monospace" font-size="15" font-weight="700" fill="#ffffff">บัลค์ (Bulk)</text>
    <text x="70" y="98" text-anchor="middle" font-family="'JetBrains Mono', monospace" font-size="13" fill="#94a3b8">d = 1 cm</text>
    
    <!-- Specs -->
    <rect x="-10" y="160" width="160" height="110" rx="8" fill="rgba(15, 23, 42, 0.8)" stroke="#334155" stroke-width="1"/>
    <text x="70" y="185" text-anchor="middle" font-family="'Sarabun', sans-serif" font-size="12" fill="#cbd5e1">ปริมาตร: 1.0 cm³</text>
    <text x="70" y="210" text-anchor="middle" font-family="'Sarabun', sans-serif" font-size="12" fill="#cbd5e1">พื้นที่ผิว: 6.0 cm²</text>
    <text x="70" y="235" text-anchor="middle" font-family="'JetBrains Mono', monospace" font-size="13" font-weight="700" fill="#38bdf8">A/V = 600 m⁻¹</text>
    <text x="70" y="258" text-anchor="middle" font-family="'Sarabun', sans-serif" font-size="11" fill="#facc15">อะตอมที่ผิว: &lt; 0.0001%</text>
  </g>

  <!-- Arrow Transition -->
  <g transform="translate(385, 175)">
    <path d="M 0 0 L 110 0" stroke="#00f0ff" stroke-width="3" stroke-dasharray="6,4"/>
    <polygon points="120,0 108,-6 108,6" fill="#00f0ff"/>
    <text x="60" y="-14" text-anchor="middle" font-family="'Sarabun', sans-serif" font-size="13" font-weight="700" fill="#00f0ff">แบ่งย่อยสู่ระดับนาโน</text>
    <text x="60" y="24" text-anchor="middle" font-family="'JetBrains Mono', monospace" font-size="12" fill="#facc15">N = 10²¹ อนุภาค</text>
  </g>

  <!-- Nano Scale Cube Group (1 nm) -->
  <g transform="translate(630, 90)">
    <!-- Cluster of tiny glowing nanocubes -->
    <g filter="url(#glow1)">
      <rect x="10" y="10" width="35" height="35" fill="url(#boxGrad1)" rx="4"/>
      <rect x="55" y="10" width="35" height="35" fill="url(#boxGrad1)" rx="4"/>
      <rect x="100" y="10" width="35" height="35" fill="url(#boxGrad1)" rx="4"/>
      <rect x="10" y="55" width="35" height="35" fill="url(#boxGrad1)" rx="4"/>
      <rect x="55" y="55" width="35" height="35" fill="url(#boxGrad1)" rx="4"/>
      <rect x="100" y="55" width="35" height="35" fill="url(#boxGrad1)" rx="4"/>
      <rect x="10" y="100" width="35" height="35" fill="url(#boxGrad1)" rx="4"/>
      <rect x="55" y="100" width="35" height="35" fill="url(#boxGrad1)" rx="4"/>
      <rect x="100" y="100" width="35" height="35" fill="url(#boxGrad1)" rx="4"/>
    </g>
    <text x="72" y="78" text-anchor="middle" font-family="'JetBrains Mono', monospace" font-size="13" font-weight="700" fill="#020617">NANO</text>

    <!-- Specs -->
    <rect x="-10" y="160" width="165" height="110" rx="8" fill="rgba(15, 23, 42, 0.8)" stroke="#00f0ff" stroke-width="1.2"/>
    <text x="72" y="185" text-anchor="middle" font-family="'Sarabun', sans-serif" font-size="12" fill="#cbd5e1">ปริมาตรรวม: 1.0 cm³</text>
    <text x="72" y="210" text-anchor="middle" font-family="'Sarabun', sans-serif" font-size="12" fill="#cbd5e1">พื้นที่ผิว: 60,000,000 cm²</text>
    <text x="72" y="235" text-anchor="middle" font-family="'JetBrains Mono', monospace" font-size="13" font-weight="700" fill="#00f0ff">A/V = 6×10⁹ m⁻¹</text>
    <text x="72" y="258" text-anchor="middle" font-family="'Sarabun', sans-serif" font-size="11" font-weight="700" fill="#10b981">อะตอมที่ผิว: &gt; 85% (Active!)</text>
  </g>

  <!-- Bottom Key Formula Bar -->
  <g transform="translate(60, 365)">
    <rect width="780" height="38" rx="8" fill="#020617" stroke="#334155" stroke-width="1"/>
    <text x="390" y="24" text-anchor="middle" font-family="'JetBrains Mono', monospace" font-size="13" fill="#ffffff">
      <tspan fill="#38bdf8" font-weight="700">A / V = 6 / d</tspan> &emsp;|&emsp; 
      <tspan fill="#facc15">N_surface / N_total ∝ 1 / d</tspan> &emsp;|&emsp; 
      <tspan fill="#34d399">ความว่องไวปฏิกิริยาเร่งเร่งปฏิกิริยา (Catalysis Rate) เพิ่มขึ้น 10⁶ เท่า</tspan>
    </text>
  </g>
</svg>
"""

# ------------------------------------------------------------------------------
# 2. ch02_quantum_confinement.svg
# ------------------------------------------------------------------------------
svg_ch02 = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 900 420" width="100%" height="100%">
  <defs>
    <linearGradient id="bgGrad2" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#090e1a"/>
      <stop offset="100%" stop-color="#0f172a"/>
    </linearGradient>
  </defs>

  <rect width="900" height="420" rx="16" fill="url(#bgGrad2)" stroke="#00f0ff" stroke-opacity="0.35" stroke-width="1.5"/>

  <text x="450" y="38" text-anchor="middle" font-family="'Sarabun', sans-serif" font-size="18" font-weight="700" fill="#38bdf8">
    การกักขังเชิงควอนตัมและความหนาแน่นสถานะพลังงาน (Quantum Confinement & Density of States)
  </text>
  <line x1="60" y1="52" x2="840" y2="52" stroke="#334155" stroke-width="1"/>

  <!-- 3D Bulk (0D Confinement) -->
  <g transform="translate(60, 80)">
    <rect width="170" height="260" rx="10" fill="#0f172a" stroke="#334155" stroke-width="1.5"/>
    <text x="85" y="30" text-anchor="middle" font-family="'Sarabun', sans-serif" font-size="14" font-weight="700" fill="#ffffff">3D บัลค์ (Bulk)</text>
    <text x="85" y="50" text-anchor="middle" font-family="'JetBrains Mono', monospace" font-size="11" fill="#94a3b8">ไมโคร / มาโคร</text>
    
    <!-- Mini DOS Plot 3D -->
    <path d="M 25 180 L 145 180 M 25 180 L 25 80" stroke="#64748b" stroke-width="1.5"/>
    <path d="M 25 180 Q 80 160, 145 95" fill="none" stroke="#38bdf8" stroke-width="2.5"/>
    <text x="85" y="210" text-anchor="middle" font-family="'JetBrains Mono', monospace" font-size="12" fill="#38bdf8">g(E) ∝ E^(1/2)</text>
    <text x="85" y="235" text-anchor="middle" font-family="'Sarabun', sans-serif" font-size="11" fill="#cbd5e1">แถบพลังงานต่อเนื่อง</text>
  </g>

  <!-- 2D Quantum Well (1D Confinement) -->
  <g transform="translate(260, 80)">
    <rect width="170" height="260" rx="10" fill="#0f172a" stroke="#334155" stroke-width="1.5"/>
    <text x="85" y="30" text-anchor="middle" font-family="'Sarabun', sans-serif" font-size="14" font-weight="700" fill="#ffffff">2D บ่อควอนตัม</text>
    <text x="85" y="50" text-anchor="middle" font-family="'JetBrains Mono', monospace" font-size="11" fill="#94a3b8">Graphene / MoS₂</text>

    <!-- Mini DOS Plot 2D (Step function) -->
    <path d="M 25 180 L 145 180 M 25 180 L 25 80" stroke="#64748b" stroke-width="1.5"/>
    <path d="M 25 180 L 45 180 L 45 150 L 95 150 L 95 115 L 145 115" fill="none" stroke="#facc15" stroke-width="2.5"/>
    <text x="85" y="210" text-anchor="middle" font-family="'JetBrains Mono', monospace" font-size="12" fill="#facc15">g(E) ∝ Step Function</text>
    <text x="85" y="235" text-anchor="middle" font-family="'Sarabun', sans-serif" font-size="11" fill="#cbd5e1">ขั้นบันไดพลังงานย่อย</text>
  </g>

  <!-- 1D Quantum Wire (2D Confinement) -->
  <g transform="translate(460, 80)">
    <rect width="170" height="260" rx="10" fill="#0f172a" stroke="#334155" stroke-width="1.5"/>
    <text x="85" y="30" text-anchor="middle" font-family="'Sarabun', sans-serif" font-size="14" font-weight="700" fill="#ffffff">1D ลวดควอนตัม</text>
    <text x="85" y="50" text-anchor="middle" font-family="'JetBrains Mono', monospace" font-size="11" fill="#94a3b8">Carbon Nanotube</text>

    <!-- Mini DOS Plot 1D (Van Hove singularities) -->
    <path d="M 25 180 L 145 180 M 25 180 L 25 80" stroke="#64748b" stroke-width="1.5"/>
    <path d="M 25 180 L 45 180 L 45 90 Q 55 160, 85 160 L 85 90 Q 95 160, 125 160 L 125 90" fill="none" stroke="#34d399" stroke-width="2.5"/>
    <text x="85" y="210" text-anchor="middle" font-family="'JetBrains Mono', monospace" font-size="12" fill="#34d399">g(E) ∝ E^(-1/2)</text>
    <text x="85" y="235" text-anchor="middle" font-family="'Sarabun', sans-serif" font-size="11" fill="#cbd5e1">Van Hove Singularities</text>
  </g>

  <!-- 0D Quantum Dot (3D Confinement) -->
  <g transform="translate(660, 80)">
    <rect width="170" height="260" rx="10" fill="#0f172a" stroke="#00f0ff" stroke-width="1.8"/>
    <text x="85" y="30" text-anchor="middle" font-family="'Sarabun', sans-serif" font-size="14" font-weight="700" fill="#00f0ff">0D ควอนตัมดอท</text>
    <text x="85" y="50" text-anchor="middle" font-family="'JetBrains Mono', monospace" font-size="11" fill="#facc15">CdSe / Perovskite</text>

    <!-- Mini DOS Plot 0D (Delta peaks) -->
    <path d="M 25 180 L 145 180 M 25 180 L 25 80" stroke="#64748b" stroke-width="1.5"/>
    <line x1="50" y1="180" x2="50" y2="90" stroke="#f43f5e" stroke-width="3"/>
    <line x1="85" y1="180" x2="85" y2="90" stroke="#f43f5e" stroke-width="3"/>
    <line x1="120" y1="180" x2="120" y2="90" stroke="#f43f5e" stroke-width="3"/>
    <text x="85" y="210" text-anchor="middle" font-family="'JetBrains Mono', monospace" font-size="12" fill="#f43f5e">g(E) ∝ Σ δ(E - E_n)</text>
    <text x="85" y="235" text-anchor="middle" font-family="'Sarabun', sans-serif" font-size="11" fill="#facc15">ระดับพลังงานแยกไม่ต่อเนื่อง</text>
  </g>

  <!-- Bottom Brus Equation Box -->
  <g transform="translate(60, 360)">
    <rect width="770" height="42" rx="8" fill="#020617" stroke="#334155" stroke-width="1"/>
    <text x="385" y="26" text-anchor="middle" font-family="'JetBrains Mono', monospace" font-size="12.5" fill="#ffffff">
      <tspan fill="#38bdf8" font-weight="700">แบบจำลองบรูส (Brus Model):</tspan> &nbsp;
      <tspan fill="#facc15">E_g(R) = E_g(bulk) + ℏ²π²/(2 m_r* R²) - 1.8e²/(4πεε₀R)</tspan>
    </text>
  </g>
</svg>
"""

# ------------------------------------------------------------------------------
# 3. ch03_synthesis_methods.svg
# ------------------------------------------------------------------------------
svg_ch03 = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 900 420" width="100%" height="100%">
  <defs>
    <linearGradient id="bgGrad3" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#090e1a"/>
      <stop offset="100%" stop-color="#0f172a"/>
    </linearGradient>
  </defs>
  <rect width="900" height="420" rx="16" fill="url(#bgGrad3)" stroke="#00f0ff" stroke-opacity="0.35" stroke-width="1.5"/>
  <text x="450" y="38" text-anchor="middle" font-family="'Sarabun', sans-serif" font-size="18" font-weight="700" fill="#38bdf8">
    ยุทธศาสตร์การสังเคราะห์โครงสร้างนาโน: จากบนลงล่าง vs จากล่างขึ้นบน (Top-Down vs Bottom-Up)
  </text>
  <line x1="60" y1="52" x2="840" y2="52" stroke="#334155" stroke-width="1"/>

  <!-- Top-Down Column -->
  <g transform="translate(80, 80)">
    <rect width="330" height="260" rx="12" fill="#0f172a" stroke="#38bdf8" stroke-width="1.5"/>
    <text x="165" y="32" text-anchor="middle" font-family="'Sarabun', sans-serif" font-size="15" font-weight="700" fill="#38bdf8">1. จากบนลงล่าง (Top-Down Route)</text>
    <text x="165" y="55" text-anchor="middle" font-family="'Sarabun', sans-serif" font-size="12" fill="#94a3b8">การแกะสลักและลดทอนขนาดจากบัลค์</text>
    
    <rect x="25" y="75" width="280" height="160" rx="8" fill="rgba(2, 6, 23, 0.8)" stroke="#334155"/>
    <text x="40" y="105" font-family="'Sarabun', sans-serif" font-size="12" fill="#cbd5e1">• ลิโธกราฟีด้วยลำอิเล็กตรอน (E-beam / EUV)</text>
    <text x="40" y="135" font-family="'Sarabun', sans-serif" font-size="12" fill="#cbd5e1">• การบดเชิงกลพลังงานสูง (Ball Milling)</text>
    <text x="40" y="165" font-family="'Sarabun', sans-serif" font-size="12" fill="#cbd5e1">• การกัดกร่อนพลาสมาเชิงปฏิกิริยา (RIE)</text>
    <text x="40" y="195" font-family="'Sarabun', sans-serif" font-size="12" fill="#facc15">✓ จุดเด่น: จัดวางตำแหน่งแม่นยำสูง</text>
    <text x="40" y="218" font-family="'Sarabun', sans-serif" font-size="12" fill="#f43f5e">✗ ข้อจำกัด: ต้นทุนเครื่องจักรสูง มีความเค้นตกค้าง</text>
  </g>

  <!-- Bottom-Up Column -->
  <g transform="translate(490, 80)">
    <rect width="330" height="260" rx="12" fill="#0f172a" stroke="#10b981" stroke-width="1.5"/>
    <text x="165" y="32" text-anchor="middle" font-family="'Sarabun', sans-serif" font-size="15" font-weight="700" fill="#10b981">2. จากล่างขึ้นบน (Bottom-Up Route)</text>
    <text x="165" y="55" text-anchor="middle" font-family="'Sarabun', sans-serif" font-size="12" fill="#94a3b8">การประกอบตัวเองระดับอะตอม/โมเลกุล</text>
    
    <rect x="25" y="75" width="280" height="160" rx="8" fill="rgba(2, 6, 23, 0.8)" stroke="#334155"/>
    <text x="40" y="105" font-family="'Sarabun', sans-serif" font-size="12" fill="#cbd5e1">• การตกสะสมไอเคมี (CVD / ALD)</text>
    <text x="40" y="135" font-family="'Sarabun', sans-serif" font-size="12" fill="#cbd5e1">• กระบวนการโซล-เจล (Sol-Gel Synthesis)</text>
    <text x="40" y="165" font-family="'Sarabun', sans-serif" font-size="12" fill="#cbd5e1">• การประกอบตัวเองโมเลกุล (Self-Assembly)</text>
    <text x="40" y="195" font-family="'Sarabun', sans-serif" font-size="12" fill="#10b981">✓ จุดเด่น: โครงผลึกสมบูรณ์สูง ขยายขนาดผลิตได้</text>
    <text x="40" y="218" font-family="'Sarabun', sans-serif" font-size="12" fill="#facc15">✗ ข้อจำกัด: ควบคุมการเกาะกลุ่ม (Agglomeration)</text>
  </g>

  <!-- Bottom Bar: LaMer Nucleation -->
  <g transform="translate(60, 360)">
    <rect width="780" height="42" rx="8" fill="#020617" stroke="#334155" stroke-width="1"/>
    <text x="390" y="26" text-anchor="middle" font-family="'JetBrains Mono', monospace" font-size="12.5" fill="#ffffff">
      <tspan fill="#38bdf8" font-weight="700">ทฤษฎีการเกิดนิวเคลียสลาแมร์ (LaMer Model):</tspan> &nbsp;
      <tspan fill="#facc15">C_min &lt; C_monomer &lt; C_crit (Nucleation Burst → Monodisperse Growth)</tspan>
    </text>
  </g>
</svg>
"""

# ------------------------------------------------------------------------------
# 4. ch04_characterization_suite.svg
# ------------------------------------------------------------------------------
svg_ch04 = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 900 420" width="100%" height="100%">
  <defs>
    <linearGradient id="bgGrad4" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#090e1a"/>
      <stop offset="100%" stop-color="#0f172a"/>
    </linearGradient>
  </defs>
  <rect width="900" height="420" rx="16" fill="url(#bgGrad4)" stroke="#00f0ff" stroke-opacity="0.35" stroke-width="1.5"/>
  <text x="450" y="38" text-anchor="middle" font-family="'Sarabun', sans-serif" font-size="18" font-weight="700" fill="#38bdf8">
    ชุดเครื่องมือมาตรวิทยาและวิเคราะห์ลักษณะเฉพาะของวัสดุนาโน (Nanometrology Suite)
  </text>
  <line x1="60" y1="52" x2="840" y2="52" stroke="#334155" stroke-width="1"/>

  <!-- 4 Pillars -->
  <g transform="translate(60, 80)">
    <!-- SEM / TEM -->
    <rect x="0" y="0" width="175" height="260" rx="10" fill="#0f172a" stroke="#38bdf8" stroke-width="1.5"/>
    <text x="87" y="30" text-anchor="middle" font-family="'Sarabun', sans-serif" font-size="14" font-weight="700" fill="#38bdf8">1. FE-SEM / HR-TEM</text>
    <text x="87" y="50" text-anchor="middle" font-family="'JetBrains Mono', monospace" font-size="11" fill="#94a3b8">ลำอิเล็กตรอนความยาวคลื่นสั้น</text>
    <text x="87" y="110" text-anchor="middle" font-family="'Sarabun', sans-serif" font-size="12" fill="#cbd5e1">สัณฐานวิทยา & โครงตาข่าย</text>
    <text x="87" y="140" text-anchor="middle" font-family="'JetBrains Mono', monospace" font-size="12" fill="#facc15">λ = h / √(2m₀eU)</text>
    <text x="87" y="180" text-anchor="middle" font-family="'Sarabun', sans-serif" font-size="11" fill="#94a3b8">กำลังขยาย: 1,000,000×</text>
    <text x="87" y="210" text-anchor="middle" font-family="'Sarabun', sans-serif" font-size="11" font-weight="700" fill="#10b981">ความละเอียด: 0.05 nm</text>
  </g>

  <g transform="translate(260, 80)">
    <!-- AFM / STM -->
    <rect x="0" y="0" width="175" height="260" rx="10" fill="#0f172a" stroke="#facc15" stroke-width="1.5"/>
    <text x="87" y="30" text-anchor="middle" font-family="'Sarabun', sans-serif" font-size="14" font-weight="700" fill="#facc15">2. AFM / STM Probe</text>
    <text x="87" y="50" text-anchor="middle" font-family="'JetBrains Mono', monospace" font-size="11" fill="#94a3b8">หัวเข็มกราดตรวจระดับอะตอม</text>
    <text x="87" y="110" text-anchor="middle" font-family="'Sarabun', sans-serif" font-size="12" fill="#cbd5e1">ภูมิประเทศผิว 3D & อุโมงค์</text>
    <text x="87" y="140" text-anchor="middle" font-family="'JetBrains Mono', monospace" font-size="12" fill="#38bdf8">I ∝ V · exp(-2κd)</text>
    <text x="87" y="180" text-anchor="middle" font-family="'Sarabun', sans-serif" font-size="11" fill="#94a3b8">แรงกระทำ: ปิโกนิวตัน (pN)</text>
    <text x="87" y="210" text-anchor="middle" font-family="'Sarabun', sans-serif" font-size="11" font-weight="700" fill="#10b981">แยกแยะอะตอมเดี่ยวได้</text>
  </g>

  <g transform="translate(460, 80)">
    <!-- XRD -->
    <rect x="0" y="0" width="175" height="260" rx="10" fill="#0f172a" stroke="#34d399" stroke-width="1.5"/>
    <text x="87" y="30" text-anchor="middle" font-family="'Sarabun', sans-serif" font-size="14" font-weight="700" fill="#34d399">3. XRD Diffraction</text>
    <text x="87" y="50" text-anchor="middle" font-family="'JetBrains Mono', monospace" font-size="11" fill="#94a3b8">การเลี้ยวเบนรังสีเอกซ์</text>
    <text x="87" y="110" text-anchor="middle" font-family="'Sarabun', sans-serif" font-size="12" fill="#cbd5e1">ขนาดผลึก & เฟสสาร</text>
    <text x="87" y="140" text-anchor="middle" font-family="'JetBrains Mono', monospace" font-size="12" fill="#facc15">D = Kλ / (β cosθ)</text>
    <text x="87" y="180" text-anchor="middle" font-family="'Sarabun', sans-serif" font-size="11" fill="#94a3b8">กฎของแบรกก์: 2d sinθ = nλ</text>
    <text x="87" y="210" text-anchor="middle" font-family="'Sarabun', sans-serif" font-size="11" font-weight="700" fill="#10b981">คำนวณ Scherrer Size</text>
  </g>

  <g transform="translate(660, 80)">
    <!-- XPS / Raman -->
    <rect x="0" y="0" width="175" height="260" rx="10" fill="#0f172a" stroke="#c084fc" stroke-width="1.5"/>
    <text x="87" y="30" text-anchor="middle" font-family="'Sarabun', sans-serif" font-size="14" font-weight="700" fill="#c084fc">4. XPS & Raman</text>
    <text x="87" y="50" text-anchor="middle" font-family="'JetBrains Mono', monospace" font-size="11" fill="#94a3b8">สเปกโทรสโกปีผิวและโฟนอน</text>
    <text x="87" y="110" text-anchor="middle" font-family="'Sarabun', sans-serif" font-size="12" fill="#cbd5e1">สถานะพันธะเคมี & การสั่น</text>
    <text x="87" y="140" text-anchor="middle" font-family="'JetBrains Mono', monospace" font-size="12" fill="#38bdf8">E_B = hν - E_K - Φ</text>
    <text x="87" y="180" text-anchor="middle" font-family="'Sarabun', sans-serif" font-size="11" fill="#94a3b8">วิเคราะห์ความลึกผิว 1-10 nm</text>
    <text x="87" y="210" text-anchor="middle" font-family="'Sarabun', sans-serif" font-size="11" font-weight="700" fill="#10b981">ตรวจจับ D, G, 2D Peak</text>
  </g>

  <!-- Bottom Formula -->
  <g transform="translate(60, 360)">
    <rect width="775" height="42" rx="8" fill="#020617" stroke="#334155" stroke-width="1"/>
    <text x="387" y="26" text-anchor="middle" font-family="'JetBrains Mono', monospace" font-size="12.5" fill="#ffffff">
      <tspan fill="#38bdf8" font-weight="700">เกณฑ์ความละเอียดเรย์ลี (Rayleigh Limit):</tspan> &nbsp;
      <tspan fill="#facc15">r = 0.61 λ / NA</tspan> &emsp;|&emsp; 
      <tspan fill="#34d399">De Broglie Wavelength: λ = 1.226 / √V (nm)</tspan>
    </text>
  </g>
</svg>
"""

# ------------------------------------------------------------------------------
# 5. ch05_2d_carbon_allotropes.svg
# ------------------------------------------------------------------------------
svg_ch05 = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 900 420" width="100%" height="100%">
  <defs>
    <linearGradient id="bgGrad5" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#090e1a"/>
      <stop offset="100%" stop-color="#0f172a"/>
    </linearGradient>
  </defs>
  <rect width="900" height="420" rx="16" fill="url(#bgGrad5)" stroke="#00f0ff" stroke-opacity="0.35" stroke-width="1.5"/>
  <text x="450" y="38" text-anchor="middle" font-family="'Sarabun', sans-serif" font-size="18" font-weight="700" fill="#38bdf8">
    อัญรูปคาร์บอนและวัสดุโครงสร้าง 2 มิติ (Carbon Allotropes & 2D Nanomaterials)
  </text>
  <line x1="60" y1="52" x2="840" y2="52" stroke="#334155" stroke-width="1"/>

  <!-- 3 Pillars: 0D C60, 1D CNT, 2D Graphene -->
  <g transform="translate(80, 80)">
    <rect width="220" height="260" rx="10" fill="#0f172a" stroke="#c084fc" stroke-width="1.5"/>
    <text x="110" y="30" text-anchor="middle" font-family="'Sarabun', sans-serif" font-size="14" font-weight="700" fill="#c084fc">0D ฟูลเลอรีน (C₆₀)</text>
    <text x="110" y="50" text-anchor="middle" font-family="'JetBrains Mono', monospace" font-size="11" fill="#94a3b8">Buckyball Sphere</text>
    <text x="110" y="110" text-anchor="middle" font-family="'Sarabun', sans-serif" font-size="12" fill="#cbd5e1">โครงสร้าง 12 ห้าเหลี่ยม</text>
    <text x="110" y="135" text-anchor="middle" font-family="'Sarabun', sans-serif" font-size="12" fill="#cbd5e1">20 หกเหลี่ยม (sp² hybrid)</text>
    <text x="110" y="175" text-anchor="middle" font-family="'JetBrains Mono', monospace" font-size="12" fill="#facc15">d ≈ 0.71 nm</text>
    <text x="110" y="210" text-anchor="middle" font-family="'Sarabun', sans-serif" font-size="11" fill="#10b981">ตัวรับอิเล็กตรอนในโซลาร์เซลล์</text>
  </g>

  <g transform="translate(340, 80)">
    <rect width="220" height="260" rx="10" fill="#0f172a" stroke="#34d399" stroke-width="1.5"/>
    <text x="110" y="30" text-anchor="middle" font-family="'Sarabun', sans-serif" font-size="14" font-weight="700" fill="#34d399">1D ท่อคาร์บอนนาโน (CNT)</text>
    <text x="110" y="50" text-anchor="middle" font-family="'JetBrains Mono', monospace" font-size="11" fill="#94a3b8">Chirality Vector (n,m)</text>
    <text x="110" y="110" text-anchor="middle" font-family="'Sarabun', sans-serif" font-size="12" fill="#cbd5e1">โลหะเมื่อ (n-m) mod 3 = 0</text>
    <text x="110" y="135" text-anchor="middle" font-family="'Sarabun', sans-serif" font-size="12" fill="#cbd5e1">กึ่งตัวนำ: E_g ≈ 0.8/d eV</text>
    <text x="110" y="175" text-anchor="middle" font-family="'JetBrains Mono', monospace" font-size="12" fill="#facc15">Young's Modulus: 1 TPa</text>
    <text x="110" y="210" text-anchor="middle" font-family="'Sarabun', sans-serif" font-size="11" fill="#10b981">การนำส่งกระแสแบบบัลลิสติก</text>
  </g>

  <g transform="translate(600, 80)">
    <rect width="220" height="260" rx="10" fill="#0f172a" stroke="#00f0ff" stroke-width="1.8"/>
    <text x="110" y="30" text-anchor="middle" font-family="'Sarabun', sans-serif" font-size="14" font-weight="700" fill="#00f0ff">2D กราฟีน (Graphene)</text>
    <text x="110" y="50" text-anchor="middle" font-family="'JetBrains Mono', monospace" font-size="11" fill="#94a3b8">Honeycomb Lattice</text>
    <text x="110" y="110" text-anchor="middle" font-family="'Sarabun', sans-serif" font-size="12" fill="#cbd5e1">กรวยดิแรกเชิงเส้น (Dirac Cones)</text>
    <text x="110" y="135" text-anchor="middle" font-family="'Sarabun', sans-serif" font-size="12" fill="#cbd5e1">E(k) = ± ℏ v_F |k|</text>
    <text x="110" y="175" text-anchor="middle" font-family="'JetBrains Mono', monospace" font-size="12" fill="#facc15">v_F ≈ 10⁶ m/s (Relativistic)</text>
    <text x="110" y="210" text-anchor="middle" font-family="'Sarabun', sans-serif" font-size="11" font-weight="700" fill="#10b981">การเคลื่อนที่: 200,000 cm²/Vs</text>
  </g>

  <!-- Bottom Formula -->
  <g transform="translate(60, 360)">
    <rect width="780" height="42" rx="8" fill="#020617" stroke="#334155" stroke-width="1"/>
    <text x="390" y="26" text-anchor="middle" font-family="'JetBrains Mono', monospace" font-size="12.5" fill="#ffffff">
      <tspan fill="#38bdf8" font-weight="700">สมการพลังงานดิแรก (Dirac Dispersion):</tspan> &nbsp;
      <tspan fill="#facc15">E(k) = ± ℏ v_F √(k_x² + k_y²)</tspan> &emsp;|&emsp; 
      <tspan fill="#34d399">Klein Tunneling Transmission = 1.0 (Zero Reflection)</tspan>
    </text>
  </g>
</svg>
"""

# ------------------------------------------------------------------------------
# 6. ch06_applications_matrix.svg
# ------------------------------------------------------------------------------
svg_ch06 = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 900 420" width="100%" height="100%">
  <defs>
    <linearGradient id="bgGrad6" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#090e1a"/>
      <stop offset="100%" stop-color="#0f172a"/>
    </linearGradient>
  </defs>
  <rect width="900" height="420" rx="16" fill="url(#bgGrad6)" stroke="#00f0ff" stroke-opacity="0.35" stroke-width="1.5"/>
  <text x="450" y="38" text-anchor="middle" font-family="'Sarabun', sans-serif" font-size="18" font-weight="700" fill="#38bdf8">
    เมทริกซ์การประยุกต์ใช้นาโนเทคโนโลยี: พลังงาน การแพทย์ และสิ่งแวดล้อม
  </text>
  <line x1="60" y1="52" x2="840" y2="52" stroke="#334155" stroke-width="1"/>

  <!-- Energy Pillar -->
  <g transform="translate(60, 80)">
    <rect width="235" height="260" rx="10" fill="#0f172a" stroke="#facc15" stroke-width="1.5"/>
    <text x="117" y="30" text-anchor="middle" font-family="'Sarabun', sans-serif" font-size="14" font-weight="700" fill="#facc15">1. พลังงานสะอาด (Clean Energy)</text>
    <text x="117" y="50" text-anchor="middle" font-family="'JetBrains Mono', monospace" font-size="11" fill="#94a3b8">PV & Energy Storage</text>
    <text x="15" y="85" font-family="'Sarabun', sans-serif" font-size="11.5" fill="#cbd5e1">• โซลาร์เซลล์เพอรอฟสไกต์ควอนตัมดอท</text>
    <text x="15" y="110" font-family="'Sarabun', sans-serif" font-size="11.5" fill="#cbd5e1">• ซูเปอร์คาปาซิเตอร์กราฟีนพรุน 3D</text>
    <text x="15" y="135" font-family="'Sarabun', sans-serif" font-size="11.5" fill="#cbd5e1">• แบตเตอรี่ลิเทียมซิลิคอนนาโนไวร์</text>
    <text x="117" y="180" text-anchor="middle" font-family="'JetBrains Mono', monospace" font-size="12" fill="#38bdf8">PCE = (J_sc · V_oc · FF)/P_in</text>
    <text x="117" y="215" text-anchor="middle" font-family="'Sarabun', sans-serif" font-size="11" font-weight="700" fill="#10b981">ประสิทธิภาพ &gt; 29% (Tandem)</text>
  </g>

  <!-- Nanomedicine Pillar -->
  <g transform="translate(332, 80)">
    <rect width="235" height="260" rx="10" fill="#0f172a" stroke="#f43f5e" stroke-width="1.5"/>
    <text x="117" y="30" text-anchor="middle" font-family="'Sarabun', sans-serif" font-size="14" font-weight="700" fill="#f43f5e">2. การแพทย์นาโน (Nanomedicine)</text>
    <text x="117" y="50" text-anchor="middle" font-family="'JetBrains Mono', monospace" font-size="11" fill="#94a3b8">Targeted Drug Delivery</text>
    <text x="15" y="85" font-family="'Sarabun', sans-serif" font-size="11.5" fill="#cbd5e1">• ปรากฏการณ์ EPR รั่วซึมสู่เซลล์มะเร็ง</text>
    <text x="15" y="110" font-family="'Sarabun', sans-serif" font-size="11.5" fill="#cbd5e1">• ลิโพโซมและพอลิเมอร์นาโนพาร์ติเคิล</text>
    <text x="15" y="135" font-family="'Sarabun', sans-serif" font-size="11.5" fill="#cbd5e1">• การปลดปล่อยยาตอบสนองต่อ pH</text>
    <text x="117" y="180" text-anchor="middle" font-family="'JetBrains Mono', monospace" font-size="12" fill="#facc15">d_opt = 50 - 150 nm</text>
    <text x="117" y="215" text-anchor="middle" font-family="'Sarabun', sans-serif" font-size="11" font-weight="700" fill="#10b981">ลดผลข้างเคียงต่อเซลล์ปกติ &gt; 80%</text>
  </g>

  <!-- Environment Pillar -->
  <g transform="translate(605, 80)">
    <rect width="235" height="260" rx="10" fill="#0f172a" stroke="#10b981" stroke-width="1.5"/>
    <text x="117" y="30" text-anchor="middle" font-family="'Sarabun', sans-serif" font-size="14" font-weight="700" fill="#10b981">3. สิ่งแวดล้อม (Environment)</text>
    <text x="117" y="50" text-anchor="middle" font-family="'JetBrains Mono', monospace" font-size="11" fill="#94a3b8">Water & Air Sensing</text>
    <text x="15" y="85" font-family="'Sarabun', sans-serif" font-size="11.5" fill="#cbd5e1">• เมมเบรนกรองน้ำกราฟีนออกไซด์ / TiO₂</text>
    <text x="15" y="110" font-family="'Sarabun', sans-serif" font-size="11.5" fill="#cbd5e1">• โฟโตแคทาลิซิสย่อยสลายสารมลพิษ</text>
    <text x="15" y="135" font-family="'Sarabun', sans-serif" font-size="11.5" fill="#cbd5e1">• เซนเซอร์ก๊าซพิษนาโนไวร์ ZnO</text>
    <text x="117" y="180" text-anchor="middle" font-family="'JetBrains Mono', monospace" font-size="12" fill="#38bdf8">J_w = A (ΔP - Δπ)</text>
    <text x="117" y="215" text-anchor="middle" font-family="'Sarabun', sans-serif" font-size="11" font-weight="700" fill="#10b981">อัตรากรองโลหะหนัก &gt; 99.8%</text>
  </g>

  <!-- Bottom Formula -->
  <g transform="translate(60, 360)">
    <rect width="780" height="42" rx="8" fill="#020617" stroke="#334155" stroke-width="1"/>
    <text x="390" y="26" text-anchor="middle" font-family="'JetBrains Mono', monospace" font-size="12.5" fill="#ffffff">
      <tspan fill="#38bdf8" font-weight="700">แบบจำลองการดูดซับแลงเมียร์ (Langmuir Isotherm):</tspan> &nbsp;
      <tspan fill="#facc15">q_e = (q_max K_L C_e) / (1 + K_L C_e)</tspan>
    </text>
  </g>
</svg>
"""

# ------------------------------------------------------------------------------
# 7. ch07_nanotoxicology_safety.svg
# ------------------------------------------------------------------------------
svg_ch07 = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 900 420" width="100%" height="100%">
  <defs>
    <linearGradient id="bgGrad7" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#090e1a"/>
      <stop offset="100%" stop-color="#0f172a"/>
    </linearGradient>
  </defs>
  <rect width="900" height="420" rx="16" fill="url(#bgGrad7)" stroke="#00f0ff" stroke-opacity="0.35" stroke-width="1.5"/>
  <text x="450" y="38" text-anchor="middle" font-family="'Sarabun', sans-serif" font-size="18" font-weight="700" fill="#38bdf8">
    กรอบความปลอดภัย พิษวิทยานาโน และลำดับขั้นการควบคุมความเสี่ยง (Hierarchy of Controls)
  </text>
  <line x1="60" y1="52" x2="840" y2="52" stroke="#334155" stroke-width="1"/>

  <!-- Left: Exposure & Cellular ROS -->
  <g transform="translate(60, 80)">
    <rect width="360" height="260" rx="12" fill="#0f172a" stroke="#f43f5e" stroke-width="1.5"/>
    <text x="180" y="30" text-anchor="middle" font-family="'Sarabun', sans-serif" font-size="14" font-weight="700" fill="#f43f5e">เส้นทางการรับสัมผัสและกลไก ROS</text>
    <text x="25" y="65" font-family="'Sarabun', sans-serif" font-size="12" fill="#cbd5e1">1. การสูดดม (Inhalation): เข้าสู่ถุงลมปอดลึก</text>
    <text x="25" y="90" font-family="'Sarabun', sans-serif" font-size="12" fill="#cbd5e1">2. การซึมผ่านผิวหนัง (Dermal Penetration)</text>
    <text x="25" y="115" font-family="'Sarabun', sans-serif" font-size="12" fill="#cbd5e1">3. การกลืนกินและระบบทางเดินอาหาร (Ingestion)</text>
    <line x1="25" y1="135" x2="335" y2="135" stroke="#334155"/>
    <text x="180" y="165" text-anchor="middle" font-family="'JetBrains Mono', monospace" font-size="12" fill="#facc15">d[ROS]/dt = k_gen · S_NP - k_scav · [GSH]</text>
    <text x="180" y="195" text-anchor="middle" font-family="'Sarabun', sans-serif" font-size="11.5" fill="#f43f5e">ความเครียดออกซิเดชัน ทำลาย DNA & ผนังเซลล์</text>
    <text x="180" y="225" text-anchor="middle" font-family="'Sarabun', sans-serif" font-size="11.5" font-weight="700" fill="#38bdf8">การทดสอบ: MTT Viability & LDH Release Assay</text>
  </g>

  <!-- Right: Hierarchy of Controls Pyramid -->
  <g transform="translate(460, 80)">
    <rect width="380" height="260" rx="12" fill="#0f172a" stroke="#10b981" stroke-width="1.5"/>
    <text x="190" y="30" text-anchor="middle" font-family="'Sarabun', sans-serif" font-size="14" font-weight="700" fill="#10b981">ลำดับขั้นการควบคุมความเสี่ยง (ISO 14644-1)</text>

    <g transform="translate(30, 50)">
      <!-- Elimination -->
      <polygon points="160,0 20,40 300,40" fill="#10b981"/>
      <text x="160" y="30" text-anchor="middle" font-family="'Sarabun', sans-serif" font-size="11" font-weight="700" fill="#020617">1. กำจัดอันตราย (Elimination / Safe-by-Design)</text>

      <!-- Engineering -->
      <polygon points="20,43 300,43 320,83 0,83" fill="#38bdf8"/>
      <text x="160" y="68" text-anchor="middle" font-family="'Sarabun', sans-serif" font-size="11" font-weight="700" fill="#020617">2. วิศวกรรมควบคุม (Fume Hood / HEPA Class 5)</text>

      <!-- Administrative -->
      <polygon points="0,86 320,86 335,126 -15,126" fill="#facc15"/>
      <text x="160" y="110" text-anchor="middle" font-family="'Sarabun', sans-serif" font-size="11" font-weight="700" fill="#020617">3. การบริหารจัดการ (SOP & Safety Training)</text>

      <!-- PPE -->
      <polygon points="-15,129 335,129 350,169 -30,169" fill="#f43f5e"/>
      <text x="160" y="153" text-anchor="middle" font-family="'Sarabun', sans-serif" font-size="11" font-weight="700" fill="#ffffff">4. อุปกรณ์ PPE (หน้ากาก N95/N100 & ถุงมือไนไตรล์คู่)</text>
    </g>
  </g>

  <!-- Bottom Formula -->
  <g transform="translate(60, 360)">
    <rect width="780" height="42" rx="8" fill="#020617" stroke="#334155" stroke-width="1"/>
    <text x="390" y="26" text-anchor="middle" font-family="'JetBrains Mono', monospace" font-size="12.5" fill="#ffffff">
      <tspan fill="#38bdf8" font-weight="700">ดัชนีลำดับความสำคัญความเสี่ยง (RPN):</tspan> &nbsp;
      <tspan fill="#facc15">RPN = S × O × D (Severity × Occurrence × Detection)</tspan> &emsp;|&emsp; 
      <tspan fill="#10b981">ISO Class 5: &lt; 3,520 particles/m³</tspan>
    </text>
  </g>
</svg>
"""

# ------------------------------------------------------------------------------
# 8. ch08_multiscale_simulations.svg
# ------------------------------------------------------------------------------
svg_ch08 = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 900 420" width="100%" height="100%">
  <defs>
    <linearGradient id="bgGrad8" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#090e1a"/>
      <stop offset="100%" stop-color="#0f172a"/>
    </linearGradient>
  </defs>
  <rect width="900" height="420" rx="16" fill="url(#bgGrad8)" stroke="#00f0ff" stroke-opacity="0.35" stroke-width="1.5"/>
  <text x="450" y="38" text-anchor="middle" font-family="'Sarabun', sans-serif" font-size="18" font-weight="700" fill="#38bdf8">
    ลำดับขั้นการจำลองหลายมาตราส่วนและปัญญาประดิษฐ์ (Multi-Scale Modeling & AI Inverse Design)
  </text>
  <line x1="60" y1="52" x2="840" y2="52" stroke="#334155" stroke-width="1"/>

  <!-- 4 Scales -->
  <g transform="translate(60, 80)">
    <!-- 1. Quantum DFT -->
    <rect x="0" y="0" width="175" height="260" rx="10" fill="#0f172a" stroke="#38bdf8" stroke-width="1.5"/>
    <text x="87" y="30" text-anchor="middle" font-family="'Sarabun', sans-serif" font-size="14" font-weight="700" fill="#38bdf8">1. ควอนตัม DFT</text>
    <text x="87" y="50" text-anchor="middle" font-family="'JetBrains Mono', monospace" font-size="11" fill="#94a3b8">10⁻¹⁰ m | 10⁻¹⁵ s</text>
    <text x="87" y="105" text-anchor="middle" font-family="'Sarabun', sans-serif" font-size="12" fill="#cbd5e1">โครงสร้างแถบพลังงาน</text>
    <text x="87" y="130" text-anchor="middle" font-family="'JetBrains Mono', monospace" font-size="11" fill="#facc15">Kohn-Sham DFT</text>
    <text x="87" y="175" text-anchor="middle" font-family="'Sarabun', sans-serif" font-size="11" fill="#94a3b8">ระดับ 10 - 1000 อะตอม</text>
    <text x="87" y="210" text-anchor="middle" font-family="'Sarabun', sans-serif" font-size="11" font-weight="700" fill="#10b981">คำนวณ Eg & Eform</text>
  </g>

  <g transform="translate(260, 80)">
    <!-- 2. Molecular Dynamics -->
    <rect x="0" y="0" width="175" height="260" rx="10" fill="#0f172a" stroke="#facc15" stroke-width="1.5"/>
    <text x="87" y="30" text-anchor="middle" font-family="'Sarabun', sans-serif" font-size="14" font-weight="700" fill="#facc15">2. พลวัตโมเลกุล (MD)</text>
    <text x="87" y="50" text-anchor="middle" font-family="'JetBrains Mono', monospace" font-size="11" fill="#94a3b8">10⁻⁹ m | 10⁻¹² s</text>
    <text x="87" y="105" text-anchor="middle" font-family="'Sarabun', sans-serif" font-size="12" fill="#cbd5e1">การจัดเรียง & การหลอม</text>
    <text x="87" y="130" text-anchor="middle" font-family="'JetBrains Mono', monospace" font-size="11" fill="#38bdf8">Lennard-Jones & REBO</text>
    <text x="87" y="175" text-anchor="middle" font-family="'Sarabun', sans-serif" font-size="11" fill="#94a3b8">ระดับ 10³ - 10⁷ อะตอม</text>
    <text x="87" y="210" text-anchor="middle" font-family="'Sarabun', sans-serif" font-size="11" font-weight="700" fill="#10b981">สมบัติเชิงความร้อน/กล</text>
  </g>

  <g transform="translate(460, 80)">
    <!-- 3. FDTD Electrodynamics -->
    <rect x="0" y="0" width="175" height="260" rx="10" fill="#0f172a" stroke="#f43f5e" stroke-width="1.5"/>
    <text x="87" y="30" text-anchor="middle" font-family="'Sarabun', sans-serif" font-size="14" font-weight="700" fill="#f43f5e">3. คลื่น FDTD</text>
    <text x="87" y="50" text-anchor="middle" font-family="'JetBrains Mono', monospace" font-size="11" fill="#94a3b8">10⁻⁷ m | 10⁻⁹ s</text>
    <text x="87" y="105" text-anchor="middle" font-family="'Sarabun', sans-serif" font-size="12" fill="#cbd5e1">พลาสมอน & แสงนาโน</text>
    <text x="87" y="130" text-anchor="middle" font-family="'JetBrains Mono', monospace" font-size="11" fill="#facc15">Yee Grid Maxwell</text>
    <text x="87" y="175" text-anchor="middle" font-family="'Sarabun', sans-serif" font-size="11" fill="#94a3b8">จุดร้อน Hotspots SERS</text>
    <text x="87" y="210" text-anchor="middle" font-family="'Sarabun', sans-serif" font-size="11" font-weight="700" fill="#10b981">อัตราขยายสนาม |E|⁴</text>
  </g>

  <g transform="translate(660, 80)">
    <!-- 4. AI & Inverse Design -->
    <rect x="0" y="0" width="175" height="260" rx="10" fill="#0f172a" stroke="#c084fc" stroke-width="1.8"/>
    <text x="87" y="30" text-anchor="middle" font-family="'Sarabun', sans-serif" font-size="14" font-weight="700" fill="#c084fc">4. AI Inverse Design</text>
    <text x="87" y="50" text-anchor="middle" font-family="'JetBrains Mono', monospace" font-size="11" fill="#facc15">Materials Informatics</text>
    <text x="87" y="105" text-anchor="middle" font-family="'Sarabun', sans-serif" font-size="12" fill="#cbd5e1">คัดกรองวัสดุความเร็วสูง</text>
    <text x="87" y="130" text-anchor="middle" font-family="'JetBrains Mono', monospace" font-size="11" fill="#00f0ff">Graph Neural Net CGCNN</text>
    <text x="87" y="175" text-anchor="middle" font-family="'Sarabun', sans-serif" font-size="11" fill="#94a3b8">สแกน 100,000 ชนิดในนาที</text>
    <text x="87" y="210" text-anchor="middle" font-family="'Sarabun', sans-serif" font-size="11" font-weight="700" fill="#10b981">เร่งค้นพบวัสดุใหม่ 100×</text>
  </g>

  <!-- Bottom Formula -->
  <g transform="translate(60, 360)">
    <rect width="775" height="42" rx="8" fill="#020617" stroke="#334155" stroke-width="1"/>
    <text x="387" y="26" text-anchor="middle" font-family="'JetBrains Mono', monospace" font-size="12.5" fill="#ffffff">
      <tspan fill="#38bdf8" font-weight="700">การอินทิเกรตแบบแวร์เลต์ (Velocity Verlet):</tspan> &nbsp;
      <tspan fill="#facc15">r(t + Δt) = r(t) + v(t)Δt + 1/2 a(t)Δt²</tspan> &emsp;|&emsp; 
      <tspan fill="#34d399">Loss: MSE + λ ||W||²</tspan>
    </text>
  </g>
</svg>
"""

# Save SVGs
with open(os.path.join(SVG_DIR, "ch01_scale_and_surface.svg"), "w", encoding="utf-8") as f:
    f.write(svg_ch01)
with open(os.path.join(SVG_DIR, "ch02_quantum_confinement.svg"), "w", encoding="utf-8") as f:
    f.write(svg_ch02)
with open(os.path.join(SVG_DIR, "ch03_synthesis_methods.svg"), "w", encoding="utf-8") as f:
    f.write(svg_ch03)
with open(os.path.join(SVG_DIR, "ch04_characterization_suite.svg"), "w", encoding="utf-8") as f:
    f.write(svg_ch04)
with open(os.path.join(SVG_DIR, "ch05_2d_carbon_allotropes.svg"), "w", encoding="utf-8") as f:
    f.write(svg_ch05)
with open(os.path.join(SVG_DIR, "ch06_applications_matrix.svg"), "w", encoding="utf-8") as f:
    f.write(svg_ch06)
with open(os.path.join(SVG_DIR, "ch07_nanotoxicology_safety.svg"), "w", encoding="utf-8") as f:
    f.write(svg_ch07)
with open(os.path.join(SVG_DIR, "ch08_multiscale_simulations.svg"), "w", encoding="utf-8") as f:
    f.write(svg_ch08)

print("✅ Generated all 8 SVG Infographic Diagrams successfully in assets/diagrams/")
