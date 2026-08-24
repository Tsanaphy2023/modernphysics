#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Fixes Chapter title duplicate numbering and deploys 3D Animated SVG Covers
along with interactive 3D subtopic cards grids into all 8 Chapter Sections on RBRU Moodle Course ID 262.
"""

import os
import re
import json
import requests

COURSE_ID = "262"
BASE_URL = "https://elearning.rbru.ac.th"

session = requests.Session()
session.cookies.set("MoodleSessionrbrulms", "lsd8fv1nrb9spqgtchgv9a1co1", domain="elearning.rbru.ac.th")
session.headers.update({
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Origin": BASE_URL,
    "Referer": f"{BASE_URL}/course/view.php?id={COURSE_ID}"
})

CATALOG_PATH = "/Users/chewathassana/Downloads/manus_backup2026/ModernPhysics/หนังสือ-เล่ม1-ฟิสิกส์ยุคใหม่/moodle_catalog.json"
COURSE_DATA_PATH = "/Users/chewathassana/Downloads/manus_backup2026/ModernPhysics/หนังสือ-เล่ม1-ฟิสิกส์ยุคใหม่/course_data.json"

with open(CATALOG_PATH, "r", encoding="utf-8") as f:
    moodle_catalog = json.load(f)

with open(COURSE_DATA_PATH, "r", encoding="utf-8") as f:
    course_data = json.load(f)

# ==============================================================================
# 3D Animated SVG Covers for Chapters 1 - 8
# ==============================================================================
def get_chapter_animated_cover_svg(ch_id):
    if ch_id == 1:
        # Chapter 1: Quantum Origins - Glowing Blackbody Cavity, Wave packets, Photoelectric & Spectral Lines
        return """
        <div class="cover-svg-wrapper">
          <svg class="cover-svg-anim" viewBox="0 0 760 220" fill="none" xmlns="http://www.w3.org/2000/svg">
            <defs>
              <linearGradient id="c1_bg" x1="0%" y1="0%" x2="100%" y2="100%">
                <stop offset="0%" stop-color="#090e1a"/>
                <stop offset="50%" stop-color="#0f172a"/>
                <stop offset="100%" stop-color="#1e1b4b"/>
              </linearGradient>
              <radialGradient id="c1_glow" cx="50%" cy="50%" r="50%">
                <stop offset="0%" stop-color="#f43f5e" stop-opacity="0.8"/>
                <stop offset="40%" stop-color="#f59e0b" stop-opacity="0.4"/>
                <stop offset="100%" stop-color="#f43f5e" stop-opacity="0"/>
              </radialGradient>
              <linearGradient id="c1_ray" x1="0%" y1="0%" x2="100%" y2="0%">
                <stop offset="0%" stop-color="#facc15"/>
                <stop offset="50%" stop-color="#38bdf8"/>
                <stop offset="100%" stop-color="#00f0ff"/>
              </linearGradient>
            </defs>
            <rect width="760" height="220" rx="14" fill="url(#c1_bg)"/>

            <!-- Grid Perspective Floor -->
            <g opacity="0.25" stroke="#00f0ff" stroke-width="1">
              <line x1="0" y1="180" x2="760" y2="180"/>
              <line x1="0" y1="200" x2="760" y2="200"/>
              <line x1="100" y1="160" x2="0" y2="220"/>
              <line x1="250" y1="160" x2="180" y2="220"/>
              <line x1="400" y1="160" x2="380" y2="220"/>
              <line x1="550" y1="160" x2="580" y2="220"/>
              <line x1="700" y1="160" x2="760" y2="220"/>
            </g>

            <!-- 3D Blackbody Cavity Glow (Left) -->
            <circle cx="140" cy="110" r="70" fill="url(#c1_glow)" class="anim-pulse"/>
            <polygon points="110,65 170,65 190,145 90,145" fill="#020617" stroke="#f59e0b" stroke-width="2"/>
            <circle cx="140" cy="105" r="18" fill="#facc15" filter="drop-shadow(0 0 10px #f59e0b)"/>
            <text x="80" y="175" fill="#facc15" font-family="'JetBrains Mono', monospace" font-size="11" font-weight="bold">Cavity E = nhf</text>

            <!-- Photoelectric Effect Plate & Ejected Electrons (Middle) -->
            <rect x="330" y="55" width="22" height="100" rx="4" fill="#334155" stroke="#00f0ff" stroke-width="2"/>
            <!-- Incident Photons -->
            <path d="M220 70 L330 90" stroke="#facc15" stroke-width="3" stroke-dasharray="6 4" class="anim-ray"/>
            <path d="M220 110 L330 120" stroke="#facc15" stroke-width="3" stroke-dasharray="6 4" class="anim-ray"/>
            <!-- Ejected Photoelectrons -->
            <circle cx="375" cy="80" r="6" fill="#38bdf8" class="anim-eject-1"/>
            <circle cx="410" cy="115" r="6" fill="#38bdf8" class="anim-eject-2"/>
            <circle cx="440" cy="70" r="6" fill="#38bdf8" class="anim-eject-3"/>
            <text x="310" y="175" fill="#00f0ff" font-family="'JetBrains Mono', monospace" font-size="11" font-weight="bold">hf = W₀ + eV_s</text>

            <!-- Hydrogen Spectral Series (Right) -->
            <g transform="translate(560, 45)">
              <circle cx="90" cy="65" r="45" stroke="rgba(168,85,247,0.4)" stroke-width="1.5" fill="none"/>
              <circle cx="90" cy="65" r="30" stroke="rgba(168,85,247,0.6)" stroke-width="1.5" fill="none"/>
              <circle cx="90" cy="65" r="14" fill="#f43f5e"/>
              <circle cx="120" cy="65" r="5" fill="#38bdf8" class="anim-orbit"/>
              <path d="M120 65 L90 51" stroke="#facc15" stroke-width="2" stroke-dasharray="3 3"/>
              <text x="35" y="130" fill="#a855f7" font-family="'JetBrains Mono', monospace" font-size="11" font-weight="bold">1/λ = R_H(1/n₁²-1/n₂²)</text>
            </g>
          </svg>
        </div>
        """
    elif ch_id == 2:
        # Chapter 2: Special Relativity - Minkowski Cone, Light Clock, Lorentz Grid & E=mc2
        return """
        <div class="cover-svg-wrapper">
          <svg class="cover-svg-anim" viewBox="0 0 760 220" fill="none" xmlns="http://www.w3.org/2000/svg">
            <defs>
              <linearGradient id="c2_bg" x1="0%" y1="0%" x2="100%" y2="100%">
                <stop offset="0%" stop-color="#020617"/>
                <stop offset="50%" stop-color="#0f172a"/>
                <stop offset="100%" stop-color="#0369a1"/>
              </linearGradient>
            </defs>
            <rect width="760" height="220" rx="14" fill="url(#c2_bg)"/>

            <!-- Light Cones (Left) -->
            <g transform="translate(130, 110)">
              <!-- Upper & Lower Cones -->
              <polygon points="0,0 -55,-65 55,-65" fill="rgba(56, 189, 248, 0.2)" stroke="#38bdf8" stroke-width="1.5"/>
              <polygon points="0,0 -55,65 55,65" fill="rgba(244, 63, 94, 0.2)" stroke="#f43f5e" stroke-width="1.5"/>
              <line x1="-70" y1="0" x2="70" y2="0" stroke="#64748b" stroke-width="1.5"/>
              <line x1="0" y1="-75" x2="0" y2="75" stroke="#64748b" stroke-width="1.5"/>
              <!-- Worldline -->
              <line x1="-30" y1="60" x2="30" y2="-60" stroke="#facc15" stroke-width="2.5" class="anim-pulse"/>
              <text x="-60" y="88" fill="#38bdf8" font-family="'JetBrains Mono', monospace" font-size="11" font-weight="bold">Minkowski Cone</text>
            </g>

            <!-- Light Clock & Time Dilation (Middle) -->
            <g transform="translate(360, 110)">
              <rect x="-40" y="-55" width="80" height="8" rx="2" fill="#64748b"/>
              <rect x="-40" y="47" width="80" height="8" rx="2" fill="#64748b"/>
              <!-- Zigzag photon path -->
              <path d="M-30 47 L0 -47 L30 47" stroke="#00f0ff" stroke-width="2.5" stroke-dasharray="4 3" class="anim-ray" fill="none"/>
              <circle cx="0" cy="-47" r="4" fill="#facc15"/>
              <text x="-48" y="88" fill="#00f0ff" font-family="'JetBrains Mono', monospace" font-size="11" font-weight="bold">Δt = γ Δt₀ (v → c)</text>
            </g>

            <!-- Relativistic Rocket & Energy Mass Equivalence (Right) -->
            <g transform="translate(580, 110)">
              <!-- Relativistic Warping Grid -->
              <ellipse cx="0" cy="0" rx="75" ry="30" stroke="rgba(0,240,255,0.4)" stroke-width="1.5" fill="none" class="anim-spin-slow"/>
              <ellipse cx="0" cy="0" rx="50" ry="20" stroke="rgba(245,158,11,0.5)" stroke-width="1.5" fill="none"/>
              <text x="-55" y="8" fill="#ffffff" font-family="'JetBrains Mono', monospace" font-size="20" font-weight="bold">E = γmc²</text>
              <text x="-65" y="88" fill="#facc15" font-family="'JetBrains Mono', monospace" font-size="11" font-weight="bold">Lorentz Invariance</text>
            </g>
          </svg>
        </div>
        """
    elif ch_id == 3:
        # Chapter 3: Wave-Particle Duality
        return """
        <div class="cover-svg-wrapper">
          <svg class="cover-svg-anim" viewBox="0 0 760 220" fill="none" xmlns="http://www.w3.org/2000/svg">
            <defs>
              <linearGradient id="c3_bg" x1="0%" y1="0%" x2="100%" y2="100%">
                <stop offset="0%" stop-color="#020617"/>
                <stop offset="50%" stop-color="#064e3b"/>
                <stop offset="100%" stop-color="#0f172a"/>
              </linearGradient>
            </defs>
            <rect width="760" height="220" rx="14" fill="url(#c3_bg)"/>

            <!-- De Broglie Matter Wave (Left) -->
            <g transform="translate(130, 110)">
              <path d="M-80 0 Q-40 -35 0 0 T80 0" stroke="#38bdf8" stroke-width="3" fill="none" class="anim-wave"/>
              <circle cx="0" cy="0" r="10" fill="#facc15" filter="drop-shadow(0 0 8px #f59e0b)"/>
              <text x="-55" y="65" fill="#38bdf8" font-family="'JetBrains Mono', monospace" font-size="11" font-weight="bold">λ = h / p (de Broglie)</text>
            </g>

            <!-- Davisson-Germer Bragg Diffraction (Middle) -->
            <g transform="translate(380, 110)">
              <circle cx="0" cy="0" r="15" fill="none" stroke="#10b981" stroke-width="2"/>
              <circle cx="0" cy="0" r="35" fill="none" stroke="#38bdf8" stroke-width="2" stroke-dasharray="4 4" class="anim-spin-slow"/>
              <circle cx="0" cy="0" r="55" fill="none" stroke="#a855f7" stroke-width="2"/>
              <circle cx="0" cy="0" r="5" fill="#ffffff"/>
              <text x="-50" y="65" fill="#10b981" font-family="'JetBrains Mono', monospace" font-size="11" font-weight="bold">2d sin θ = nλ (Bragg)</text>
            </g>

            <!-- Heisenberg Uncertainty Packet (Right) -->
            <g transform="translate(610, 110)">
              <path d="M-60 0 Q-30 -40 0 -5 Q30 35 60 0" stroke="#f59e0b" stroke-width="2.5" fill="none" class="anim-wave"/>
              <path d="M-60 0 Q-30 40 0 5 Q30 -35 60 0" stroke="#f59e0b" stroke-width="2.5" fill="none" class="anim-wave"/>
              <text x="-50" y="65" fill="#f59e0b" font-family="'JetBrains Mono', monospace" font-size="11" font-weight="bold">Δx · Δp ≥ ℏ/2</text>
            </g>
          </svg>
        </div>
        """
    elif ch_id == 4:
        # Chapter 4: Quantum Mechanics
        return """
        <div class="cover-svg-wrapper">
          <svg class="cover-svg-anim" viewBox="0 0 760 220" fill="none" xmlns="http://www.w3.org/2000/svg">
            <defs>
              <linearGradient id="c4_bg" x1="0%" y1="0%" x2="100%" y2="100%">
                <stop offset="0%" stop-color="#020617"/>
                <stop offset="50%" stop-color="#1e1b4b"/>
                <stop offset="100%" stop-color="#0f172a"/>
              </linearGradient>
            </defs>
            <rect width="760" height="220" rx="14" fill="url(#c4_bg)"/>

            <!-- Complex Wavefunction Phase Helix (Left) -->
            <g transform="translate(140, 110)">
              <path d="M-70 0 Q-35 -40 0 0 T70 0" stroke="#00f0ff" stroke-width="3" fill="none" class="anim-wave"/>
              <path d="M-70 0 Q-35 40 0 0 T70 0" stroke="#f43f5e" stroke-width="2" stroke-dasharray="3 3" fill="none" class="anim-wave"/>
              <text x="-65" y="65" fill="#00f0ff" font-family="'JetBrains Mono', monospace" font-size="11" font-weight="bold">Ψ(x,t) = Re + i Im</text>
            </g>

            <!-- 1D Potential Well & Harmonic Oscillator (Middle) -->
            <g transform="translate(380, 110)">
              <line x1="-50" y1="-50" x2="-50" y2="40" stroke="#64748b" stroke-width="2"/>
              <line x1="50" y1="-50" x2="50" y2="40" stroke="#64748b" stroke-width="2"/>
              <line x1="-50" y1="40" x2="50" y2="40" stroke="#64748b" stroke-width="2"/>
              <path d="M-50 20 Q0 -25 50 20" stroke="#10b981" stroke-width="2.5" fill="none"/>
              <path d="M-50 -10 Q-25 -35 0 -10 Q25 15 50 -10" stroke="#38bdf8" stroke-width="2" fill="none"/>
              <text x="-50" y="65" fill="#10b981" font-family="'JetBrains Mono', monospace" font-size="11" font-weight="bold">E_n = n²h²/(8mL²)</text>
            </g>

            <!-- Quantum Tunneling & STM (Right) -->
            <g transform="translate(610, 110)">
              <rect x="-15" y="-50" width="30" height="90" fill="#334155" stroke="#f59e0b" stroke-width="1.5"/>
              <path d="M-70 10 Q-40 -20 -15 10 L15 25 Q45 20 70 25" stroke="#00f0ff" stroke-width="2.5" fill="none"/>
              <text x="-55" y="65" fill="#f59e0b" font-family="'JetBrains Mono', monospace" font-size="11" font-weight="bold">Tunneling T ∝ e^(-2κL)</text>
            </g>
          </svg>
        </div>
        """
    elif ch_id == 5:
        # Chapter 5: Atomic Physics & Spectroscopy
        return """
        <div class="cover-svg-wrapper">
          <svg class="cover-svg-anim" viewBox="0 0 760 220" fill="none" xmlns="http://www.w3.org/2000/svg">
            <defs>
              <linearGradient id="c5_bg" x1="0%" y1="0%" x2="100%" y2="100%">
                <stop offset="0%" stop-color="#020617"/>
                <stop offset="50%" stop-color="#311042"/>
                <stop offset="100%" stop-color="#0f172a"/>
              </linearGradient>
            </defs>
            <rect width="760" height="220" rx="14" fill="url(#c5_bg)"/>

            <!-- Bohr-Sommerfeld Precession (Left) -->
            <g transform="translate(130, 110)">
              <ellipse cx="0" cy="0" rx="60" ry="25" stroke="#00f0ff" stroke-width="2" fill="none" transform="rotate(-20)" class="anim-spin-slow"/>
              <circle cx="0" cy="0" r="10" fill="#f43f5e"/>
              <circle cx="50" cy="-18" r="4.5" fill="#38bdf8"/>
              <text x="-60" y="65" fill="#00f0ff" font-family="'JetBrains Mono', monospace" font-size="11" font-weight="bold">Bohr: L = n·ℏ</text>
            </g>

            <!-- 3D Orbital Lobes s, p, d (Middle) -->
            <g transform="translate(380, 110)">
              <circle cx="0" cy="-25" r="22" fill="rgba(0, 240, 255, 0.7)"/>
              <circle cx="0" cy="25" r="22" fill="rgba(244, 63, 94, 0.7)"/>
              <circle cx="0" cy="0" r="6" fill="#ffffff"/>
              <text x="-55" y="65" fill="#a855f7" font-family="'JetBrains Mono', monospace" font-size="11" font-weight="bold">Orbitals (n, l, m_l, m_s)</text>
            </g>

            <!-- 3-Level Laser Resonator (Right) -->
            <g transform="translate(610, 110)">
              <rect x="-65" y="-35" width="10" height="70" fill="#64748b"/>
              <rect x="55" y="-35" width="10" height="70" fill="#64748b"/>
              <line x1="-55" y1="0" x2="55" y2="0" stroke="#f43f5e" stroke-width="4" class="anim-pulse"/>
              <line x1="65" y1="0" x2="95" y2="0" stroke="#f43f5e" stroke-width="5"/>
              <text x="-60" y="65" fill="#f43f5e" font-family="'JetBrains Mono', monospace" font-size="11" font-weight="bold">Laser 632.8 nm (N₂ > N₁)</text>
            </g>
          </svg>
        </div>
        """
    elif ch_id == 6:
        # Chapter 6: Nuclear Physics
        return """
        <div class="cover-svg-wrapper">
          <svg class="cover-svg-anim" viewBox="0 0 760 220" fill="none" xmlns="http://www.w3.org/2000/svg">
            <defs>
              <linearGradient id="c6_bg" x1="0%" y1="0%" x2="100%" y2="100%">
                <stop offset="0%" stop-color="#020617"/>
                <stop offset="50%" stop-color="#450a0a"/>
                <stop offset="100%" stop-color="#0f172a"/>
              </linearGradient>
            </defs>
            <rect width="760" height="220" rx="14" fill="url(#c6_bg)"/>

            <!-- Nucleon Core (Left) -->
            <g transform="translate(130, 110)">
              <circle cx="-12" cy="-12" r="12" fill="#f43f5e"/>
              <circle cx="12" cy="-12" r="12" fill="#38bdf8"/>
              <circle cx="0" cy="14" r="12" fill="#f43f5e"/>
              <circle cx="-16" cy="8" r="10" fill="#38bdf8"/>
              <circle cx="16" cy="8" r="10" fill="#f43f5e"/>
              <text x="-60" y="65" fill="#f43f5e" font-family="'JetBrains Mono', monospace" font-size="11" font-weight="bold">⁵⁶Fe Peak (8.79 MeV)</text>
            </g>

            <!-- Nuclear Fission Chain (Middle) -->
            <g transform="translate(380, 110)">
              <circle cx="-40" cy="0" r="14" fill="#f59e0b"/>
              <line x1="-20" y1="-8" x2="20" y2="-30" stroke="#38bdf8" stroke-width="2"/>
              <line x1="-20" y1="8" x2="20" y2="30" stroke="#38bdf8" stroke-width="2"/>
              <circle cx="35" cy="-35" r="9" fill="#10b981"/>
              <circle cx="35" cy="35" r="9" fill="#f43f5e"/>
              <text x="-50" y="65" fill="#f59e0b" font-family="'JetBrains Mono', monospace" font-size="11" font-weight="bold">²³⁵U + n → Ba + Kr + 3n</text>
            </g>

            <!-- Tokamak Fusion Torus (Right) -->
            <g transform="translate(610, 110)">
              <ellipse cx="0" cy="0" rx="60" ry="24" stroke="#475569" stroke-width="10" fill="none"/>
              <ellipse cx="0" cy="0" rx="55" ry="20" stroke="#f43f5e" stroke-width="4" fill="none" class="anim-pulse"/>
              <text x="-60" y="65" fill="#38bdf8" font-family="'JetBrains Mono', monospace" font-size="11" font-weight="bold">D-T Tokamak (Q > 10)</text>
            </g>
          </svg>
        </div>
        """
    elif ch_id == 7:
        # Chapter 7: Particle Physics & Standard Model
        return """
        <div class="cover-svg-wrapper">
          <svg class="cover-svg-anim" viewBox="0 0 760 220" fill="none" xmlns="http://www.w3.org/2000/svg">
            <defs>
              <linearGradient id="c7_bg" x1="0%" y1="0%" x2="100%" y2="100%">
                <stop offset="0%" stop-color="#020617"/>
                <stop offset="50%" stop-color="#1e1b4b"/>
                <stop offset="100%" stop-color="#0f172a"/>
              </linearGradient>
            </defs>
            <rect width="760" height="220" rx="14" fill="url(#c7_bg)"/>

            <!-- Cloud Chamber Positron (Left) -->
            <g transform="translate(130, 110)">
              <circle cx="0" cy="0" r="45" stroke="#334155" stroke-width="2" fill="#090e1a"/>
              <rect x="-40" y="-3" width="80" height="6" fill="#64748b"/>
              <path d="M0 40 Q15 15 10 0 Q5 -20 -15 -35" stroke="#00f0ff" stroke-width="2.5" fill="none"/>
              <text x="-55" y="65" fill="#00f0ff" font-family="'JetBrains Mono', monospace" font-size="11" font-weight="bold">Positron (Anderson 1932)</text>
            </g>

            <!-- Feynman Beta Decay (Middle) -->
            <g transform="translate(380, 110)">
              <line x1="-50" y1="0" x2="-10" y2="0" stroke="#10b981" stroke-width="2.5"/>
              <line x1="-10" y1="0" x2="30" y2="-30" stroke="#10b981" stroke-width="2.5"/>
              <path d="M-10 0 Q10 15 30 15" stroke="#f43f5e" stroke-width="2" stroke-dasharray="3 3"/>
              <circle cx="-10" cy="0" r="4" fill="#facc15"/>
              <line x1="30" y1="15" x2="55" y2="0" stroke="#38bdf8" stroke-width="2.5"/>
              <line x1="30" y1="15" x2="55" y2="35" stroke="#a855f7" stroke-width="2.5" stroke-dasharray="3 3"/>
              <text x="-60" y="65" fill="#facc15" font-family="'JetBrains Mono', monospace" font-size="11" font-weight="bold">d → u + W⁻ → e⁻ + ν̄ₑ</text>
            </g>

            <!-- LHC Collision & Higgs 125 GeV (Right) -->
            <g transform="translate(610, 110)">
              <circle cx="0" cy="0" r="40" stroke="#475569" stroke-width="1.5" fill="none"/>
              <line x1="-55" y1="0" x2="55" y2="0" stroke="#f43f5e" stroke-width="2"/>
              <circle cx="0" cy="0" r="8" fill="#facc15" class="anim-pulse"/>
              <text x="-60" y="65" fill="#10b981" font-family="'JetBrains Mono', monospace" font-size="11" font-weight="bold">Higgs Peak 125.09 GeV</text>
            </g>
          </svg>
        </div>
        """
    else:
        # Chapter 8: Astrophysics & Cosmology
        return """
        <div class="cover-svg-wrapper">
          <svg class="cover-svg-anim" viewBox="0 0 760 220" fill="none" xmlns="http://www.w3.org/2000/svg">
            <defs>
              <linearGradient id="c8_bg" x1="0%" y1="0%" x2="100%" y2="100%">
                <stop offset="0%" stop-color="#020617"/>
                <stop offset="50%" stop-color="#090e1a"/>
                <stop offset="100%" stop-color="#0284c7"/>
              </linearGradient>
            </defs>
            <rect width="760" height="220" rx="14" fill="url(#c8_bg)"/>

            <!-- Hubble Expanding Universe (Left) -->
            <g transform="translate(130, 110)">
              <circle cx="0" cy="0" r="6" fill="#ffffff"/>
              <circle cx="-35" cy="-25" r="4" fill="#38bdf8"/>
              <circle cx="45" cy="-20" r="4" fill="#f59e0b"/>
              <circle cx="35" cy="35" r="4" fill="#f43f5e"/>
              <line x1="0" y1="0" x2="35" y2="35" stroke="#ef4444" stroke-width="1.5"/>
              <text x="-55" y="65" fill="#38bdf8" font-family="'JetBrains Mono', monospace" font-size="11" font-weight="bold">v = H₀·d (Hubble Law)</text>
            </g>

            <!-- Dark Matter Galaxy & Rotation Curve (Middle) -->
            <g transform="translate(380, 110)">
              <ellipse cx="0" cy="0" rx="55" ry="20" stroke="rgba(168,85,247,0.5)" stroke-width="1.5" fill="none" class="anim-spin-slow"/>
              <circle cx="0" cy="0" r="10" fill="#f59e0b"/>
              <text x="-65" y="65" fill="#a855f7" font-family="'JetBrains Mono', monospace" font-size="11" font-weight="bold">Dark Energy 68% | DM 27%</text>
            </g>

            <!-- Schwarzschild Black Hole Horizon (Right) -->
            <g transform="translate(610, 110)">
              <ellipse cx="0" cy="0" rx="50" ry="12" fill="rgba(245,158,11,0.7)"/>
              <circle cx="0" cy="0" r="22" fill="#000000" stroke="#f59e0b" stroke-width="2"/>
              <text x="-60" y="65" fill="#facc15" font-family="'JetBrains Mono', monospace" font-size="11" font-weight="bold">R_s = 2GM/c² (Horizon)</text>
            </g>
          </svg>
        </div>
        """

# Visual SVGs & Formulas for Subtopic Cards
from deploy_moodle_section_cards import SVG_ICONS, FORMULAS

def generate_section_html_with_animated_cover(ch_id, clean_title, ch_desc, pages_info):
    cover_svg = get_chapter_animated_cover_svg(ch_id)

    card_items_html = ""
    for p in pages_info:
        pid = p["id"]
        ptitle = p["title"]
        psummary = p.get("summary", "")[:95] + "..."
        cmid = p.get("cmid", "")
        url = p.get("url", f"{BASE_URL}/mod/page/view.php?id={cmid}")
        svg = SVG_ICONS.get(pid, SVG_ICONS.get("1.1"))
        formula = FORMULAS.get(pid, "Modern Physics Concept")

        card_items_html += f"""
        <div class="topic-card-3d">
          <div class="card-top-header">
            <div class="card-icon-3d">{svg}</div>
            <div class="topic-badge">หัวข้อ {pid}</div>
          </div>
          <h3 class="topic-title">{ptitle}</h3>
          <div class="formula-badge">{formula}</div>
          <p class="topic-summary">{psummary}</p>
          <a href="{url}" class="btn-enter-lesson">
            <span>🚀 เข้าสู่บทเรียน & ปฏิบัติการจำลอง</span>
            <span class="arrow-icon">→</span>
          </a>
        </div>
        """

    html = f"""
<div class="chapter-overview-container" style="font-family: 'Sarabun', -apple-system, sans-serif; color: #f8fafc; margin-bottom: 24px;">
  <style>
    @keyframes pulse-slow {{
      0%, 100% {{ transform: scale(1); opacity: 0.85; }}
      50% {{ transform: scale(1.08); opacity: 1.0; }}
    }}
    @keyframes spin-slow {{
      from {{ transform: rotate(0deg); }}
      to {{ transform: rotate(360deg); }}
    }}
    @keyframes dash-flow {{
      to {{ stroke-dashoffset: -20; }}
    }}
    .anim-pulse {{ animation: pulse-slow 3s infinite ease-in-out; }}
    .anim-spin-slow {{ transform-origin: center; animation: spin-slow 20s linear infinite; }}
    .anim-ray {{ animation: dash-flow 1s linear infinite; }}
    .anim-wave {{ animation: pulse-slow 2.5s infinite ease-in-out; }}

    .cover-svg-wrapper {{
      width: 100%;
      border-radius: 16px;
      overflow: hidden;
      margin-bottom: 16px;
      border: 1px solid rgba(0, 240, 255, 0.4);
      box-shadow: 0 10px 30px rgba(0, 0, 0, 0.6);
      background: #020617;
    }}
    .cover-svg-anim {{
      display: block;
      width: 100%;
      height: auto;
    }}

    .chapter-hero-banner {{
      background: linear-gradient(135deg, #090e1a 0%, #0f172a 100%);
      border: 1px solid rgba(0, 240, 255, 0.35);
      border-radius: 16px;
      padding: 20px 24px;
      margin-bottom: 20px;
      position: relative;
      overflow: hidden;
      box-shadow: 0 12px 35px rgba(0, 0, 0, 0.65);
    }}
    .chapter-badge-tag {{
      display: inline-flex;
      align-items: center;
      gap: 6px;
      background: rgba(0, 240, 255, 0.15);
      border: 1px solid #00f0ff;
      color: #00f0ff;
      padding: 4px 12px;
      border-radius: 9999px;
      font-size: 0.80rem;
      font-weight: 700;
      font-family: 'JetBrains Mono', monospace;
      margin-bottom: 8px;
    }}
    .chapter-hero-title {{
      font-size: 1.45rem;
      font-weight: 700;
      color: #ffffff;
      margin-bottom: 8px;
      letter-spacing: -0.3px;
    }}
    .chapter-hero-desc {{
      font-size: 0.92rem;
      color: #cbd5e1;
      line-height: 1.6;
      max-width: 800px;
    }}
    .topics-grid-3d {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
      gap: 16px;
      margin-top: 16px;
    }}
    .topic-card-3d {{
      background: rgba(9, 14, 26, 0.92);
      border: 1px solid #1e293b;
      border-radius: 14px;
      padding: 16px;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      transition: all 0.25s ease;
      box-shadow: 0 6px 20px rgba(0, 0, 0, 0.4);
      position: relative;
    }}
    .topic-card-3d:hover {{
      transform: translateY(-4px);
      border-color: #00f0ff;
      box-shadow: 0 12px 30px rgba(0, 240, 255, 0.25);
    }}
    .card-top-header {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 10px;
    }}
    .card-icon-3d {{
      width: 48px;
      height: 48px;
      display: flex;
      align-items: center;
      justify-content: center;
      background: #0f172a;
      border-radius: 10px;
      border: 1px solid #334155;
    }}
    .topic-badge {{
      background: rgba(56, 189, 248, 0.15);
      border: 1px solid rgba(56, 189, 248, 0.4);
      color: #38bdf8;
      padding: 3px 8px;
      border-radius: 6px;
      font-size: 0.75rem;
      font-weight: 700;
      font-family: 'JetBrains Mono', monospace;
    }}
    .topic-title {{
      font-size: 1.02rem;
      font-weight: 700;
      color: #f8fafc;
      margin-bottom: 6px;
      line-height: 1.4;
    }}
    .formula-badge {{
      background: #020617;
      border: 1px solid #334155;
      color: #facc15;
      padding: 4px 8px;
      border-radius: 6px;
      font-size: 0.75rem;
      font-family: 'JetBrains Mono', monospace;
      margin-bottom: 8px;
      overflow: hidden;
      text-overflow: ellipsis;
      white-space: nowrap;
    }}
    .topic-summary {{
      font-size: 0.82rem;
      color: #94a3b8;
      line-height: 1.5;
      margin-bottom: 14px;
      flex-grow: 1;
    }}
    .btn-enter-lesson {{
      display: flex;
      align-items: center;
      justify-content: space-between;
      background: linear-gradient(135deg, #0284c7 0%, #00f0ff 100%);
      color: #020617 !important;
      text-decoration: none !important;
      font-weight: 700;
      font-size: 0.82rem;
      padding: 8px 14px;
      border-radius: 8px;
      transition: all 0.2s ease;
    }}
    .btn-enter-lesson:hover {{
      box-shadow: 0 0 14px rgba(0, 240, 255, 0.6);
      transform: scale(1.02);
    }}
    .arrow-icon {{
      font-size: 1.1rem;
      font-weight: 900;
    }}
  </style>

  {cover_svg}

  <div class="chapter-hero-banner">
    <div class="chapter-badge-tag">⚛️ CHAPTER {ch_id} OVERVIEW</div>
    <h2 class="chapter-hero-title">บทที่ {ch_id} {clean_title}</h2>
    <p class="chapter-hero-desc">{ch_desc}</p>
  </div>

  <div class="topics-grid-3d">
    {card_items_html}
  </div>
</div>
"""
    return html

# 1. Update and Push to Moodle
print("🚀 Deploying 3D Animated Covers and Clean Titles to Moodle...")

for ch_idx, ch in enumerate(course_data):
    ch_id = ch.get("id") or ch.get("chapter_num")
    raw_title = ch.get("title", "")
    # Strictly strip any leading 'บทที่ X ' or 'X '
    clean_title = re.sub(r'^(บทที่\s*\d+\s*|\d+\s*)', '', raw_title).strip()
    formatted_section_name = f"บทที่ {ch_id} {clean_title}"

    ch_desc = ch.get("description", f"สำรวจและทำความเข้าใจฟิสิกส์ยุคใหม่ในบทที่ {ch_id} ผ่านบทเรียนเข้มข้น 5 หัวข้อย่อย พร้อมห้องปฏิบัติการเสมือนจริง 60 FPS และการควบคุมด้วยท่าทางมือ AR MediaPipe")

    s_num = str(ch_id)
    if s_num not in moodle_catalog:
        print(f"⚠️ Section {s_num} not found in moodle catalog!")
        continue

    sec_info = moodle_catalog[s_num]
    sec_db_id = sec_info["sec_db_id"]
    moodle_pages = sec_info["pages"]

    combined_pages = []
    for p_idx, p in enumerate(ch["pages"]):
        p_copy = dict(p)
        if p_idx < len(moodle_pages):
            p_copy["cmid"] = moodle_pages[p_idx]["cmid"]
            p_copy["url"] = moodle_pages[p_idx]["url"]
        combined_pages.append(p_copy)

    # Generate Section HTML with Animated 3D Cover
    section_html = generate_section_html_with_animated_cover(ch_id, clean_title, ch_desc, combined_pages)

    out_fpath = f"/Users/chewathassana/Downloads/manus_backup2026/ModernPhysics/หนังสือ-เล่ม1-ฟิสิกส์ยุคใหม่/moodle_pages/section_{ch_id}_3d_cards_overview.html"
    with open(out_fpath, "w", encoding="utf-8") as f:
        f.write(section_html)

    edit_url = f"{BASE_URL}/course/editsection.php?id={sec_db_id}"
    r_edit = session.get(edit_url)
    if r_edit.status_code != 200:
        print(f"❌ Failed to open editsection for {formatted_section_name} (ID: {sec_db_id})")
        continue

    sesskey_m = re.search(r'name=\"sesskey\"\s+value=\"([^\"]+)\"', r_edit.text)
    if not sesskey_m:
        print(f"❌ sesskey not found for {formatted_section_name}")
        continue
    sesskey = sesskey_m.group(1)

    def get_val(name):
        m = re.search(rf'<input[^>]*name=[\"\']{re.escape(name)}[\"\'][^>]*value=[\"\']([^\"\']*)[\"\']', r_edit.text)
        return m.group(1) if m else ''

    payload = {
        "context": get_val("context") or "19080",
        "id": sec_db_id,
        "course": COURSE_ID,
        "sesskey": sesskey,
        "_qf__editsection_form": "1",
        "mform_isexpanded_id_generalhdr": "1",
        "mform_isexpanded_id_availabilityconditions": "0",
        "name": formatted_section_name,
        "summary_editor[text]": section_html,
        "summary_editor[format]": "1",
        "summary_editor[itemid]": get_val("summary_editor[itemid]"),
        "submitbutton": "บันทึกการเปลี่ยนแปลง"
    }

    resp = session.post(edit_url, data=payload)
    if resp.status_code in (200, 303, 302):
        print(f"  ✅ Fixed Title: '{formatted_section_name}' & Deployed 3D Animated Cover (Section ID: {sec_db_id})")
    else:
        print(f"  ❌ Error posting Chapter {ch_id} (Status: {resp.status_code})")

print("🎉 Successfully cleaned all Chapter titles and deployed 3D Animated SVG Covers across all sections on Moodle!")
