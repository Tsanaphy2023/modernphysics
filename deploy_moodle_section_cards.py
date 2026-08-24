#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generates and Deploys High-Contrast 3D Visual Chapter Banners and
Interactive 3D Subtopic Cards Grids with Direct Navigation Links
into all 8 Chapter Sections on RBRU Moodle LMS (Course ID: 262).
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

# Load course data and moodle catalog
CATALOG_PATH = "/Users/chewathassana/Downloads/manus_backup2026/ModernPhysics/หนังสือ-เล่ม1-ฟิสิกส์ยุคใหม่/moodle_catalog.json"
COURSE_DATA_PATH = "/Users/chewathassana/Downloads/manus_backup2026/ModernPhysics/หนังสือ-เล่ม1-ฟิสิกส์ยุคใหม่/course_data.json"

with open(CATALOG_PATH, "r", encoding="utf-8") as f:
    moodle_catalog = json.load(f)

with open(COURSE_DATA_PATH, "r", encoding="utf-8") as f:
    course_data = json.load(f)

# Visual SVGs / 3D Icons for each subtopic
SVG_ICONS = {
    # Chapter 1
    "1.1": """<svg width="48" height="48" viewBox="0 0 64 64" fill="none"><circle cx="32" cy="32" r="28" fill="#0f172a" stroke="#f43f5e" stroke-width="2"/><path d="M16 44 C24 44 28 36 32 20 C36 12 40 44 48 44" stroke="#f43f5e" stroke-width="3" fill="none"/><line x1="16" y1="44" x2="48" y2="44" stroke="#475569" stroke-width="1.5"/><circle cx="32" cy="20" r="4" fill="#fb7185"/></svg>""",
    "1.2": """<svg width="48" height="48" viewBox="0 0 64 64" fill="none"><rect x="10" y="10" width="44" height="44" rx="8" fill="#0f172a" stroke="#f59e0b" stroke-width="2"/><circle cx="32" cy="32" r="14" fill="url(#pgrad)"/><defs><radialGradient id="pgrad"><stop offset="0%" stop-color="#fef08a"/><stop offset="100%" stop-color="#d97706"/></radialGradient></defs><path d="M22 32 Q32 18 42 32 Q32 46 22 32" stroke="#fef08a" stroke-width="1.5" fill="none"/></svg>""",
    "1.3": """<svg width="48" height="48" viewBox="0 0 64 64" fill="none"><circle cx="32" cy="32" r="28" fill="#0f172a" stroke="#00f0ff" stroke-width="2"/><path d="M12 20 L28 36" stroke="#facc15" stroke-width="3" stroke-dasharray="3 3"/><polygon points="26,38 32,36 30,30" fill="#facc15"/><rect x="26" y="38" width="24" height="6" rx="2" fill="#64748b"/><circle cx="44" cy="24" r="5" fill="#38bdf8"/><path d="M38 36 L48 18" stroke="#38bdf8" stroke-width="2"/></svg>""",
    "1.4": """<svg width="48" height="48" viewBox="0 0 64 64" fill="none"><circle cx="32" cy="32" r="28" fill="#0f172a" stroke="#a855f7" stroke-width="2"/><circle cx="32" cy="32" r="8" fill="#f43f5e"/><circle cx="32" cy="32" r="18" stroke="rgba(168,85,247,0.5)" stroke-width="1.5" stroke-dasharray="2 2"/><circle cx="32" cy="32" r="24" stroke="rgba(168,85,247,0.3)" stroke-width="1"/><circle cx="48" cy="24" r="4" fill="#38bdf8"/><path d="M48 24 L38 32" stroke="#facc15" stroke-width="2" stroke-dasharray="2 2"/></svg>""",
    "1.5": """<svg width="48" height="48" viewBox="0 0 64 64" fill="none"><rect x="8" y="12" width="48" height="40" rx="8" fill="#0f172a" stroke="#10b981" stroke-width="2"/><path d="M22 36 L28 24 L36 38 L42 30" stroke="#10b981" stroke-width="3" fill="none"/><circle cx="28" cy="24" r="3" fill="#34d399"/><circle cx="42" cy="30" r="3" fill="#34d399"/><text x="18" y="47" fill="#10b981" font-size="8" font-family="sans-serif" font-weight="bold">3D AR LAB</text></svg>""",

    # Chapter 2
    "2.1": """<svg width="48" height="48" viewBox="0 0 64 64" fill="none"><circle cx="32" cy="32" r="28" fill="#0f172a" stroke="#38bdf8" stroke-width="2"/><line x1="14" y1="32" x2="50" y2="32" stroke="#38bdf8" stroke-width="2.5"/><line x1="32" y1="14" x2="32" y2="50" stroke="#38bdf8" stroke-width="2.5"/><rect x="28" y="28" width="8" height="8" transform="rotate(45 32 32)" fill="#94a3b8"/><circle cx="50" cy="32" r="3" fill="#facc15"/></svg>""",
    "2.2": """<svg width="48" height="48" viewBox="0 0 64 64" fill="none"><circle cx="32" cy="32" r="28" fill="#0f172a" stroke="#00f0ff" stroke-width="2"/><line x1="14" y1="32" x2="50" y2="32" stroke="#64748b" stroke-width="1.5"/><line x1="32" y1="50" x2="32" y2="14" stroke="#64748b" stroke-width="1.5"/><line x1="18" y1="46" x2="46" y2="18" stroke="#facc15" stroke-width="2"/><line x1="18" y1="18" x2="46" y2="46" stroke="#facc15" stroke-width="2"/><line x1="16" y1="38" x2="48" y2="26" stroke="#00f0ff" stroke-width="2"/></svg>""",
    "2.3": """<svg width="48" height="48" viewBox="0 0 64 64" fill="none"><circle cx="32" cy="32" r="28" fill="#0f172a" stroke="#f59e0b" stroke-width="2"/><circle cx="32" cy="32" r="20" stroke="#f59e0b" stroke-width="2"/><line x1="32" y1="32" x2="32" y2="18" stroke="#ffffff" stroke-width="2"/><line x1="32" y1="32" x2="42" y2="38" stroke="#38bdf8" stroke-width="2"/><circle cx="32" cy="32" r="3" fill="#f59e0b"/></svg>""",
    "2.4": """<svg width="48" height="48" viewBox="0 0 64 64" fill="none"><circle cx="32" cy="32" r="28" fill="#0f172a" stroke="#ef4444" stroke-width="2"/><text x="14" y="38" fill="#facc15" font-size="14" font-family="monospace" font-weight="bold">E=mc²</text></svg>""",
    "2.5": """<svg width="48" height="48" viewBox="0 0 64 64" fill="none"><rect x="8" y="12" width="48" height="40" rx="8" fill="#0f172a" stroke="#10b981" stroke-width="2"/><polygon points="28,24 38,32 28,40" fill="#10b981"/><circle cx="32" cy="32" r="18" stroke="rgba(16,185,129,0.4)" stroke-width="1.5"/></svg>""",

    # Chapter 3
    "3.1": """<svg width="48" height="48" viewBox="0 0 64 64" fill="none"><circle cx="32" cy="32" r="28" fill="#0f172a" stroke="#38bdf8" stroke-width="2"/><path d="M12 32 Q22 18 32 32 T52 32" stroke="#38bdf8" stroke-width="3" fill="none"/><circle cx="32" cy="32" r="5" fill="#facc15"/></svg>""",
    "3.2": """<svg width="48" height="48" viewBox="0 0 64 64" fill="none"><circle cx="32" cy="32" r="28" fill="#0f172a" stroke="#a855f7" stroke-width="2"/><circle cx="32" cy="32" r="10" stroke="#a855f7" stroke-width="2"/><circle cx="32" cy="32" r="18" stroke="#38bdf8" stroke-width="2"/><circle cx="32" cy="32" r="25" stroke="#10b981" stroke-width="1.5"/></svg>""",
    "3.3": """<svg width="48" height="48" viewBox="0 0 64 64" fill="none"><circle cx="32" cy="32" r="28" fill="#0f172a" stroke="#f59e0b" stroke-width="2"/><path d="M14 32 Q24 22 32 14 Q40 22 50 32" stroke="#f59e0b" stroke-width="2" fill="none"/><path d="M14 32 Q24 42 32 50 Q40 42 50 32" stroke="#f59e0b" stroke-width="2" fill="none"/><text x="18" y="35" fill="#ffffff" font-size="10" font-family="monospace">ΔxΔp</text></svg>""",
    "3.4": """<svg width="48" height="48" viewBox="0 0 64 64" fill="none"><circle cx="32" cy="32" r="28" fill="#0f172a" stroke="#00f0ff" stroke-width="2"/><polygon points="20,16 44,16 38,48 26,48" fill="rgba(0,240,255,0.2)" stroke="#00f0ff" stroke-width="2"/><line x1="32" y1="12" x2="32" y2="52" stroke="#facc15" stroke-width="2"/></svg>""",
    "3.5": """<svg width="48" height="48" viewBox="0 0 64 64" fill="none"><rect x="8" y="12" width="48" height="40" rx="8" fill="#0f172a" stroke="#10b981" stroke-width="2"/><circle cx="26" cy="32" r="4" fill="#38bdf8"/><circle cx="38" cy="32" r="4" fill="#f43f5e"/><line x1="26" y1="32" x2="38" y2="32" stroke="#facc15" stroke-width="2" stroke-dasharray="2 2"/></svg>""",

    # Chapter 4
    "4.1": """<svg width="48" height="48" viewBox="0 0 64 64" fill="none"><circle cx="32" cy="32" r="28" fill="#0f172a" stroke="#00f0ff" stroke-width="2"/><path d="M14 32 Q24 16 32 32 T50 32" stroke="#00f0ff" stroke-width="2.5" fill="none"/><path d="M14 32 Q24 48 32 32 T50 32" stroke="#f59e0b" stroke-width="2" stroke-dasharray="2 2" fill="none"/><text x="44" y="24" fill="#00f0ff" font-size="12" font-family="serif">Ψ</text></svg>""",
    "4.2": """<svg width="48" height="48" viewBox="0 0 64 64" fill="none"><circle cx="32" cy="32" r="28" fill="#0f172a" stroke="#10b981" stroke-width="2"/><line x1="18" y1="16" x2="18" y2="48" stroke="#ffffff" stroke-width="3"/><line x1="46" y1="16" x2="46" y2="48" stroke="#ffffff" stroke-width="3"/><line x1="18" y1="48" x2="46" y2="48" stroke="#ffffff" stroke-width="3"/><path d="M18 40 Q32 20 46 40" stroke="#10b981" stroke-width="2.5" fill="none"/></svg>""",
    "4.3": """<svg width="48" height="48" viewBox="0 0 64 64" fill="none"><circle cx="32" cy="32" r="28" fill="#0f172a" stroke="#f59e0b" stroke-width="2"/><path d="M14 16 Q32 52 50 16" stroke="#64748b" stroke-width="2" fill="none"/><line x1="20" y1="40" x2="44" y2="40" stroke="#f59e0b" stroke-width="2"/><line x1="17" y1="30" x2="47" y2="30" stroke="#38bdf8" stroke-width="2"/></svg>""",
    "4.4": """<svg width="48" height="48" viewBox="0 0 64 64" fill="none"><circle cx="32" cy="32" r="28" fill="#0f172a" stroke="#f43f5e" stroke-width="2"/><rect x="28" y="16" width="8" height="32" fill="#475569"/><path d="M12 32 Q20 22 28 32 L36 38 Q42 36 52 32" stroke="#00f0ff" stroke-width="2.5" fill="none"/></svg>""",
    "4.5": """<svg width="48" height="48" viewBox="0 0 64 64" fill="none"><rect x="8" y="12" width="48" height="40" rx="8" fill="#0f172a" stroke="#10b981" stroke-width="2"/><circle cx="26" cy="32" r="6" fill="#00f0ff"/><circle cx="38" cy="32" r="6" fill="#f43f5e"/><path d="M26 32 Q32 24 38 32" stroke="#facc15" stroke-width="2"/></svg>""",

    # Chapter 5
    "5.1": """<svg width="48" height="48" viewBox="0 0 64 64" fill="none"><circle cx="32" cy="32" r="28" fill="#0f172a" stroke="#00f0ff" stroke-width="2"/><ellipse cx="32" cy="32" rx="20" ry="10" transform="rotate(-25 32 32)" stroke="#00f0ff" stroke-width="2" fill="none"/><circle cx="32" cy="32" r="6" fill="#f43f5e"/><circle cx="48" cy="24" r="3.5" fill="#38bdf8"/></svg>""",
    "5.2": """<svg width="48" height="48" viewBox="0 0 64 64" fill="none"><circle cx="32" cy="32" r="28" fill="#0f172a" stroke="#a855f7" stroke-width="2"/><circle cx="32" cy="22" r="10" fill="rgba(168,85,247,0.7)"/><circle cx="32" cy="42" r="10" fill="rgba(0,240,255,0.7)"/><circle cx="32" cy="32" r="4" fill="#ffffff"/></svg>""",
    "5.3": """<svg width="48" height="48" viewBox="0 0 64 64" fill="none"><circle cx="32" cy="32" r="28" fill="#0f172a" stroke="#10b981" stroke-width="2"/><rect x="18" y="22" width="12" height="20" fill="#1e293b" stroke="#00f0ff"/><rect x="34" y="22" width="12" height="20" fill="#1e293b" stroke="#00f0ff"/><text x="21" y="36" fill="#10b981" font-size="12" font-family="monospace">↑</text><text x="37" y="36" fill="#f43f5e" font-size="12" font-family="monospace">↓</text></svg>""",
    "5.4": """<svg width="48" height="48" viewBox="0 0 64 64" fill="none"><circle cx="32" cy="32" r="28" fill="#0f172a" stroke="#f59e0b" stroke-width="2"/><rect x="14" y="22" width="36" height="20" rx="3" fill="#020617" stroke="#475569"/><line x1="22" y1="22" x2="22" y2="42" stroke="#f43f5e" stroke-width="2.5"/><line x1="30" y1="22" x2="30" y2="42" stroke="#38bdf8" stroke-width="2.5"/><line x1="42" y1="22" x2="42" y2="42" stroke="#a855f7" stroke-width="2.5"/></svg>""",
    "5.5": """<svg width="48" height="48" viewBox="0 0 64 64" fill="none"><rect x="8" y="12" width="48" height="40" rx="8" fill="#0f172a" stroke="#10b981" stroke-width="2"/><line x1="14" y1="32" x2="50" y2="32" stroke="#f43f5e" stroke-width="4"/><circle cx="16" cy="32" r="3" fill="#ffffff"/><circle cx="48" cy="32" r="3" fill="#ffffff"/></svg>""",

    # Chapter 6
    "6.1": """<svg width="48" height="48" viewBox="0 0 64 64" fill="none"><circle cx="32" cy="32" r="28" fill="#0f172a" stroke="#f43f5e" stroke-width="2"/><circle cx="28" cy="28" r="7" fill="#f43f5e"/><circle cx="36" cy="28" r="7" fill="#38bdf8"/><circle cx="32" cy="36" r="7" fill="#f43f5e"/><circle cx="26" cy="36" r="6" fill="#38bdf8"/><circle cx="38" cy="36" r="6" fill="#f43f5e"/></svg>""",
    "6.2": """<svg width="48" height="48" viewBox="0 0 64 64" fill="none"><circle cx="32" cy="32" r="28" fill="#0f172a" stroke="#f59e0b" stroke-width="2"/><path d="M16 18 Q26 42 48 44" stroke="#f59e0b" stroke-width="3" fill="none"/><line x1="16" y1="44" x2="48" y2="44" stroke="#475569" stroke-width="1.5"/><text x="24" y="28" fill="#ffffff" font-size="10" font-family="sans-serif">T½</text></svg>""",
    "6.3": """<svg width="48" height="48" viewBox="0 0 64 64" fill="none"><circle cx="32" cy="32" r="28" fill="#0f172a" stroke="#ef4444" stroke-width="2"/><circle cx="32" cy="32" r="9" fill="#f59e0b"/><line x1="16" y1="32" x2="23" y2="32" stroke="#38bdf8" stroke-width="2"/><line x1="41" y1="26" x2="48" y2="20" stroke="#38bdf8" stroke-width="2"/><line x1="41" y1="38" x2="48" y2="44" stroke="#38bdf8" stroke-width="2"/></svg>""",
    "6.4": """<svg width="48" height="48" viewBox="0 0 64 64" fill="none"><circle cx="32" cy="32" r="28" fill="#0f172a" stroke="#00f0ff" stroke-width="2"/><rect x="28" y="16" width="10" height="32" rx="2" fill="#64748b"/><line x1="14" y1="24" x2="28" y2="24" stroke="#f43f5e" stroke-width="2"/><line x1="14" y1="32" x2="28" y2="32" stroke="#38bdf8" stroke-width="2"/><line x1="14" y1="40" x2="50" y2="40" stroke="#00f0ff" stroke-width="2"/></svg>""",
    "6.5": """<svg width="48" height="48" viewBox="0 0 64 64" fill="none"><rect x="8" y="12" width="48" height="40" rx="8" fill="#0f172a" stroke="#10b981" stroke-width="2"/><ellipse cx="32" cy="32" rx="18" ry="8" fill="none" stroke="#f43f5e" stroke-width="3"/><circle cx="32" cy="32" r="4" fill="#facc15"/></svg>""",

    # Chapter 7
    "7.1": """<svg width="48" height="48" viewBox="0 0 64 64" fill="none"><circle cx="32" cy="32" r="28" fill="#0f172a" stroke="#00f0ff" stroke-width="2"/><rect x="14" y="30" width="36" height="4" fill="#64748b"/><path d="M32 48 Q36 38 34 32 Q32 24 24 16" stroke="#00f0ff" stroke-width="2.5" fill="none"/><circle cx="24" cy="16" r="3" fill="#ffffff"/></svg>""",
    "7.2": """<svg width="48" height="48" viewBox="0 0 64 64" fill="none"><circle cx="32" cy="32" r="28" fill="#0f172a" stroke="#f59e0b" stroke-width="2"/><line x1="18" y1="18" x2="28" y2="32" stroke="#38bdf8" stroke-width="2.5"/><line x1="18" y1="46" x2="28" y2="32" stroke="#38bdf8" stroke-width="2.5"/><line x1="28" y1="32" x2="46" y2="32" stroke="#f59e0b" stroke-width="2.5" stroke-dasharray="2 2"/><circle cx="28" cy="32" r="4" fill="#00f0ff"/></svg>""",
    "7.3": """<svg width="48" height="48" viewBox="0 0 64 64" fill="none"><circle cx="32" cy="32" r="28" fill="#0f172a" stroke="#a855f7" stroke-width="2"/><circle cx="26" cy="26" r="6" fill="#f43f5e"/><circle cx="38" cy="26" r="6" fill="#10b981"/><circle cx="32" cy="38" r="6" fill="#38bdf8"/><circle cx="32" cy="32" r="18" stroke="rgba(0,240,255,0.4)" stroke-width="1.5" stroke-dasharray="3 3"/></svg>""",
    "7.4": """<svg width="48" height="48" viewBox="0 0 64 64" fill="none"><circle cx="32" cy="32" r="28" fill="#0f172a" stroke="#10b981" stroke-width="2"/><rect x="16" y="20" width="32" height="24" rx="4" fill="#1e293b" stroke="#10b981"/><text x="21" y="36" fill="#10b981" font-size="11" font-family="monospace">ΔQ=0</text></svg>""",
    "7.5": """<svg width="48" height="48" viewBox="0 0 64 64" fill="none"><rect x="8" y="12" width="48" height="40" rx="8" fill="#0f172a" stroke="#10b981" stroke-width="2"/><circle cx="32" cy="32" r="16" stroke="#f43f5e" stroke-width="2"/><line x1="16" y1="32" x2="48" y2="32" stroke="#00f0ff" stroke-width="2"/><circle cx="32" cy="32" r="5" fill="#facc15"/></svg>""",

    # Chapter 8
    "8.1": """<svg width="48" height="48" viewBox="0 0 64 64" fill="none"><circle cx="32" cy="32" r="28" fill="#0f172a" stroke="#38bdf8" stroke-width="2"/><circle cx="32" cy="32" r="4" fill="#ffffff"/><circle cx="20" cy="22" r="3" fill="#38bdf8"/><circle cx="46" cy="20" r="3" fill="#f59e0b"/><circle cx="44" cy="44" r="3" fill="#f43f5e"/><line x1="32" y1="32" x2="44" y2="44" stroke="#ef4444" stroke-width="1.5"/></svg>""",
    "8.2": """<svg width="48" height="48" viewBox="0 0 64 64" fill="none"><circle cx="32" cy="32" r="28" fill="#0f172a" stroke="#f59e0b" stroke-width="2"/><polygon points="16,32 48,16 48,48" fill="rgba(245,158,11,0.2)" stroke="#f59e0b" stroke-width="2"/><circle cx="16" cy="32" r="4" fill="#ffffff"/></svg>""",
    "8.3": """<svg width="48" height="48" viewBox="0 0 64 64" fill="none"><circle cx="32" cy="32" r="28" fill="#0f172a" stroke="#a855f7" stroke-width="2"/><circle cx="32" cy="32" r="18" fill="rgba(168,85,247,0.3)" stroke="#a855f7" stroke-width="1.5" stroke-dasharray="2 2"/><ellipse cx="32" cy="32" rx="14" ry="5" fill="#f59e0b"/></svg>""",
    "8.4": """<svg width="48" height="48" viewBox="0 0 64 64" fill="none"><circle cx="32" cy="32" r="28" fill="#0f172a" stroke="#ef4444" stroke-width="2"/><ellipse cx="32" cy="32" rx="22" ry="6" fill="rgba(245,158,11,0.6)"/><circle cx="32" cy="32" r="9" fill="#000000" stroke="#f59e0b" stroke-width="1.5"/></svg>""",
    "8.5": """<svg width="48" height="48" viewBox="0 0 64 64" fill="none"><rect x="8" y="12" width="48" height="40" rx="8" fill="#0f172a" stroke="#10b981" stroke-width="2"/><polygon points="24,20 40,20 48,32 40,44 24,44 16,32" fill="none" stroke="#facc15" stroke-width="2"/><circle cx="32" cy="32" r="3" fill="#facc15"/></svg>"""
}

# Formula Badges for each subtopic
FORMULAS = {
    "1.1": "I(λ) ∝ λ⁻⁴ (Rayleigh-Jeans)",
    "1.2": "E = nhf, u(λ,T) = (8πhc/λ⁵)/(e^(hc/λkT)-1)",
    "1.3": "hf = W₀ + K_max = W₀ + eV_s",
    "1.4": "1/λ = R_H (1/n₁² - 1/n₂²)",
    "1.5": "3D AR Quantum Optics Studio",

    "2.1": "Δt = 0 (Null Result), c = const",
    "2.2": "x' = γ(x - vt), t' = γ(t - vx/c²)",
    "2.3": "Δt = γΔt₀, L = L₀/γ (γ = 1/√(1-v²/c²))",
    "2.4": "E = γmc² = mc² + K, E² = (pc)² + (m₀c²)²",
    "2.5": "Twin Paradox & Doppler Aberration",

    "3.1": "λ = h/p = h/√(2mqV_a)",
    "3.2": "2d sin θ = nλ (Bragg Diffraction)",
    "3.3": "Δx · Δp_x ≥ ℏ/2, ΔE · Δt ≥ ℏ/2",
    "3.4": "d_min = 0.61λ / NA (Sub-Angstrom TEM)",
    "3.5": "Standing Matter Waves & Virtual Pairs",

    "4.1": "iℏ ∂Ψ/∂t = - (ℏ²/2m) ∇²Ψ + VΨ",
    "4.2": "E_n = n²h² / (8mL²), ψ_n = √(2/L) sin(nπx/L)",
    "4.3": "E_n = (n + ½)ℏω, E₀ = ½ℏω (Zero-Point)",
    "4.4": "T ≈ e^(-2κL), I_tunnel ∝ e^(-2κd)",
    "4.5": "Ψ = c₁ψ₁ + c₂ψ₂, ω_beat = (E₂-E₁)/ℏ",

    "5.1": "L = nℏ, r_n = n²a₀, E_n = -13.6/n² eV",
    "5.2": "n ≥ 1, 0 ≤ l ≤ n-1, |m_l| ≤ l, m_s = ±½",
    "5.3": "Pauli Principle: No identical 4 QNs",
    "5.4": "Discrete Emission vs Fraunhofer Lines",
    "5.5": "N₂ > N₁, Stimulated Emission Avalanche",

    "6.1": "R = R₀ A^(⅓), E_b = Δm · 931.5 MeV",
    "6.2": "N(t) = N₀ e^(-λt) = N₀ (½)^(t/T½)",
    "6.3": "²³⁵U + n → Ba + Kr + 3n + 200 MeV",
    "6.4": "I = I₀ e^(-μx) = I₀ (½)^(x/HVL)",
    "6.5": "²H + ³H → ⁴He + n + 17.6 MeV",

    "7.1": "r = p / (qB) (Anderson Positron 1932)",
    "7.2": "Strong (g), EM (γ), Weak (W/Z), Gravity (G)",
    "7.3": "Proton = uud, Neutron = udd, Pion = ud̄",
    "7.4": "ΔQ = 0, ΔB = 0, ΔL_e = 0, ΔL_μ = 0",
    "7.5": "H → γγ (m_H = 125.09 GeV, 5σ Discovery)",

    "8.1": "v = H₀ · d (H₀ ≈ 70 km/s/Mpc), z ≈ v/c",
    "8.2": "T_CMB = 2.7255 K, λ_peak = 1.06 mm",
    "8.3": "Dark Energy 68% | Dark Matter 27% | Normal 5%",
    "8.4": "R_s = 2GM/c² (Schwarzschild Horizon)",
    "8.5": "Ω = Ω_m + Ω_Λ, JWST Primordial z > 13"
}

def generate_section_html(ch_id, ch_title, ch_desc, pages_info):
    """
    Builds a stunning, responsive 3D Glassmorphism Cards Grid HTML for a chapter section.
    """
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
    .chapter-hero-banner {{
      background: linear-gradient(135deg, #090e1a 0%, #0f172a 100%);
      border: 1px solid rgba(0, 240, 255, 0.35);
      border-radius: 16px;
      padding: 22px 28px;
      margin-bottom: 20px;
      position: relative;
      overflow: hidden;
      box-shadow: 0 12px 35px rgba(0, 0, 0, 0.65);
    }}
    .chapter-hero-banner::before {{
      content: '';
      position: absolute;
      top: -50%;
      right: -20%;
      width: 400px;
      height: 400px;
      background: radial-gradient(circle, rgba(0, 240, 255, 0.12) 0%, transparent 70%);
      pointer-events: none;
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
      color: #020617 !himportant;
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

  <div class="chapter-hero-banner">
    <div class="chapter-badge-tag">⚛️ CHAPTER {ch_id} OVERVIEW</div>
    <h2 class="chapter-hero-title">บทที่ {ch_id} {ch_title}</h2>
    <p class="chapter-hero-desc">{ch_desc}</p>
  </div>

  <div class="topics-grid-3d">
    {card_items_html}
  </div>
</div>
"""
    return html

# 1. Generate and Push Section Summaries for Chapters 1 through 8
print("Starting deployment of 3D Visual Chapter Cards to Moodle...")

for ch_idx, ch in enumerate(course_data):
    ch_id = ch.get("id") or ch.get("chapter_num")
    ch_title = ch.get("title", "")
    if " " in ch_title:
        ch_title = ch_title.split(" ", 1)[1] # remove "บทที่ X " if duplicate
    ch_desc = ch.get("description", f"สำรวจและทำความเข้าใจฟิสิกส์ยุคใหม่ในบทที่ {ch_id} ผ่านบทเรียนเข้มข้น 5 หัวข้อย่อย พร้อมห้องปฏิบัติการเสมือนจริง 60 FPS และการควบคุมด้วยท่าทางมือ AR MediaPipe")

    s_num = str(ch_id)
    if s_num not in moodle_catalog:
        print(f"⚠️ Section {s_num} not found in moodle catalog!")
        continue

    sec_info = moodle_catalog[s_num]
    sec_db_id = sec_info["sec_db_id"]
    moodle_pages = sec_info["pages"]

    # Match pages with course_data pages
    combined_pages = []
    for p_idx, p in enumerate(ch["pages"]):
        p_copy = dict(p)
        if p_idx < len(moodle_pages):
            p_copy["cmid"] = moodle_pages[p_idx]["cmid"]
            p_copy["url"] = moodle_pages[p_idx]["url"]
        combined_pages.append(p_copy)

    # Generate Section HTML
    section_html = generate_section_html(ch_id, ch_title, ch_desc, combined_pages)

    # Save to local file for backup & repo
    out_fpath = f"/Users/chewathassana/Downloads/manus_backup2026/ModernPhysics/หนังสือ-เล่ม1-ฟิสิกส์ยุคใหม่/moodle_pages/section_{ch_id}_3d_cards_overview.html"
    with open(out_fpath, "w", encoding="utf-8") as f:
        f.write(section_html)

    # Push to Moodle editsection.php
    edit_url = f"{BASE_URL}/course/editsection.php?id={sec_db_id}"
    r_edit = session.get(edit_url)
    if r_edit.status_code != 200:
        print(f"❌ Failed to open editsection for Chapter {ch_id} (ID: {sec_db_id})")
        continue

    sesskey_m = re.search(r'name=\"sesskey\"\s+value=\"([^\"]+)\"', r_edit.text)
    if not sesskey_m:
        print(f"❌ sesskey not found for Chapter {ch_id}")
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
        "name": f"บทที่ {ch_id} {ch_title}",
        "summary_editor[text]": section_html,
        "summary_editor[format]": "1",
        "summary_editor[itemid]": get_val("summary_editor[itemid]"),
        "submitbutton": "บันทึกการเปลี่ยนแปลง"
    }

    resp = session.post(edit_url, data=payload)
    if resp.status_code in (200, 303, 302):
        print(f"  ✅ Deployed 3D Visual Cards Grid to Chapter {ch_id} (Section ID: {sec_db_id})")
    else:
        print(f"  ❌ Error posting Chapter {ch_id} (Status: {resp.status_code})")

print("🎉 Successfully updated all 8 Chapter Sections on Moodle with 3D Visual Card Grids and Direct Links!")
