#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
RBRU MOOC Course Renderer: Separated Pages Architecture
Reads course_data.json and generates:
1. RBRU_MOOC_Modern_Physics_Interactive.html (Master Interactive App with Banner & Separated Pages)
2. index.html at root for GitHub Pages
3. moodle_pages/section_0_banner_overview.html (Course Banner & Section 0)
4. moodle_pages/chapter_1/ ... chapter_8/ (40 standalone HTML pages)
5. MOOC_Course_Structure_Separated_Pages.md
"""

import os
import json
import shutil
from simulators_library import get_simulator_html_and_js

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR = os.path.abspath(os.path.join(BASE_DIR, ".."))
MOODLE_DIR = os.path.join(BASE_DIR, "moodle_pages")
os.makedirs(MOODLE_DIR, exist_ok=True)

with open(os.path.join(BASE_DIR, "course_data.json"), "r", encoding="utf-8") as f:
    CHAPTERS_DATA = json.load(f)

# Flatten all pages for navigation calculation
ALL_SUBPAGES = []
for ch in CHAPTERS_DATA:
    for page in ch["pages"]:
        ALL_SUBPAGES.append({"chapter": ch, "page": page, "id": page["id"]})

print(f"Loaded {len(CHAPTERS_DATA)} chapters with {len(ALL_SUBPAGES)} subtopic pages.")

# -------------------------------------------------------------
# 1. SECTION 0 BANNER OVERVIEW (MOODLE GENERAL SECTION)
# -------------------------------------------------------------
def build_section_0_banner_html():
    chapters_cards_html = "".join([
        f"""<div class="ch-card">
          <span class="ch-num" style="color:{ch['color']};">บทที่ {ch['id']}</span>
          <div class="ch-name">{ch['title'].replace(f"บทที่ {ch['id']} ", '')}</div>
          <span class="ch-subcount">5 หัวข้อย่อย ({ch['id']}.1 - {ch['id']}.5)</span>
        </div>"""
        for ch in CHAPTERS_DATA
    ])

    return f"""<!DOCTYPE html>
<html lang="th">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>ยินดีต้อนรับสู่รายวิชา 4012920 ฟิสิกส์ยุคใหม่ (Modern Physics) | RBRU MOOC</title>
<style>
  :root {{
    --primary: #00f0ff;
    --primary-dark: #087f8c;
    --bg-dark: #0b1120;
    --bg-card: #0f172a;
    --text-main: #f8fafc;
    --text-muted: #94a3b8;
    --accent-gold: #f59e0b;
    --accent-emerald: #10b981;
  }}
  body {{
    font-family: "Sarabun", "Prompt", -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
    line-height: 1.8;
    color: var(--text-main);
    background: var(--bg-dark);
    margin: 0;
    padding: 20px;
  }}
  .section0-container {{
    max-width: 1000px;
    margin: 0 auto;
    background: var(--bg-card);
    border: 1px solid rgba(255, 255, 255, 0.1);
    border-radius: 20px;
    overflow: hidden;
    box-shadow: 0 10px 40px rgba(0, 0, 0, 0.5);
  }}
  .banner-img-wrapper {{
    position: relative;
    width: 100%;
    overflow: hidden;
    background: #000;
  }}
  .banner-img {{
    width: 100%;
    height: auto;
    display: block;
    object-fit: cover;
  }}
  .banner-overlay {{
    position: absolute;
    bottom: 0;
    left: 0;
    right: 0;
    background: linear-gradient(0deg, var(--bg-card) 0%, rgba(15, 23, 42, 0.8) 50%, transparent 100%);
    padding: 30px 30px 10px;
  }}
  .course-badge {{
    display: inline-block;
    background: var(--primary);
    color: #0b1120;
    font-weight: 700;
    font-size: 0.85rem;
    padding: 4px 14px;
    border-radius: 20px;
    margin-bottom: 10px;
    text-transform: uppercase;
    letter-spacing: 0.5px;
  }}
  .course-title {{
    font-size: clamp(1.8rem, 3.5vw, 2.4rem);
    font-weight: 700;
    color: #ffffff;
    margin: 0 0 8px 0;
    line-height: 1.25;
  }}
  .course-subtitle {{
    color: var(--text-muted);
    font-size: 1.05rem;
    margin: 0;
  }}
  .section-body {{
    padding: 30px;
  }}
  .grid-info {{
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
    gap: 20px;
    margin-bottom: 30px;
  }}
  .info-box {{
    background: rgba(255, 255, 255, 0.03);
    border: 1px solid rgba(255, 255, 255, 0.08);
    border-radius: 12px;
    padding: 20px;
  }}
  .info-box h3 {{
    margin-top: 0;
    color: var(--primary);
    font-size: 1.15rem;
    display: flex;
    align-items: center;
    gap: 8px;
  }}
  .chapters-grid {{
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(220px, 1fr));
    gap: 14px;
    margin: 24px 0;
  }}
  .ch-card {{
    background: rgba(255, 255, 255, 0.02);
    border: 1px solid rgba(255, 255, 255, 0.08);
    border-radius: 10px;
    padding: 16px;
    transition: transform 0.2s, border-color 0.2s;
  }}
  .ch-card:hover {{
    transform: translateY(-3px);
    border-color: var(--primary);
    background: rgba(0, 240, 255, 0.05);
  }}
  .ch-num {{
    font-size: 0.8rem;
    font-weight: 700;
    display: block;
    margin-bottom: 4px;
  }}
  .ch-name {{
    font-size: 0.95rem;
    font-weight: 600;
    color: #ffffff;
    line-height: 1.4;
  }}
  .ch-subcount {{
    font-size: 0.78rem;
    color: var(--text-muted);
    margin-top: 8px;
    display: block;
  }}
  .cta-banner {{
    background: linear-gradient(135deg, rgba(8, 145, 178, 0.2) 0%, rgba(2, 132, 199, 0.1) 100%);
    border: 1px solid var(--primary);
    border-radius: 16px;
    padding: 28px;
    text-align: center;
    margin-top: 30px;
  }}
  .btn-launch {{
    display: inline-block;
    background: linear-gradient(135deg, #00f0ff 0%, #0284c7 100%);
    color: #0b1120;
    font-weight: 700;
    font-size: 1.05rem;
    padding: 14px 32px;
    border-radius: 30px;
    text-decoration: none;
    box-shadow: 0 4px 25px rgba(0, 240, 255, 0.4);
    transition: transform 0.2s, box-shadow 0.2s;
    margin: 8px;
  }}
  .btn-launch:hover {{
    transform: translateY(-2px);
    box-shadow: 0 6px 30px rgba(0, 240, 255, 0.6);
  }}
  .btn-git {{
    display: inline-block;
    background: rgba(255, 255, 255, 0.1);
    color: #ffffff;
    font-weight: 600;
    font-size: 1.05rem;
    padding: 14px 28px;
    border-radius: 30px;
    text-decoration: none;
    border: 1px solid rgba(255, 255, 255, 0.2);
    transition: background 0.2s;
    margin: 8px;
  }}
  .btn-git:hover {{
    background: rgba(255, 255, 255, 0.2);
  }}
</style>
</head>
<body>

<div class="section0-container">
  <div class="banner-img-wrapper">
    <img src="https://raw.githubusercontent.com/Tsanaphy2023/modernphysics/main/assets/images/modern_physics_banner.jpg" alt="RBRU Modern Physics 4012920 Banner" class="banner-img">
    <div class="banner-overlay">
      <span class="course-badge">RBRU MOOC • 4012920</span>
      <h1 class="course-title">ฟิสิกส์ยุคใหม่ (Modern Physics)</h1>
      <p class="course-subtitle">มหาวิทยาลัยราชภัฏรำไพพรรณี | คณะวิทยาศาสตร์และเทคโนโลยี</p>
    </div>
  </div>

  <div class="section-body">
    <div class="grid-info">
      <div class="info-box">
        <h3>👨‍🏫 อาจารย์ผู้รับผิดชอบรายวิชา</h3>
        <p style="margin:0 0 6px 0;"><b>ผู้ช่วยศาสตราจารย์ ดร.ชีวะ ทัศนา</b> (Asst. Prof. Dr. Chewa Thassana)</p>
        <p style="font-size:0.9rem; color:var(--text-muted); margin:0;">สาขาวิชาฟิสิกส์ คณะวิทยาศาสตร์และเทคโนโลยี มหาวิทยาลัยราชภัฏรำไพพรรณี</p>
      </div>
      <div class="info-box">
        <h3>🎯 ผลลัพธ์การเรียนรู้ (CLO: Course Learning Outcomes)</h3>
        <ul style="margin:0; padding-left:20px; font-size:0.9rem; color:var(--text-muted);">
          <li><b>CLO 1:</b> อธิบายแนวคิดและวิกฤตของฟิสิกส์ดั้งเดิมสู่จุดกำเนิดควอนตัม</li>
          <li><b>CLO 2:</b> วิเคราะห์และประยุกต์ทฤษฎีสัมพัทธภาพพิเศษและกลศาสตร์ควอนตัม</li>
          <li><b>CLO 3:</b> คำนวณปรากฏการณ์ในฟิสิกส์นิวเคลียร์และอนุภาคมูลฐาน</li>
          <li><b>CLO 4:</b> เชื่อมโยงฟิสิกส์ยุคใหม่กับเอกภพวิทยาและการทดลองเสมือนจริง 3D AR</li>
        </ul>
      </div>
    </div>

    <h3 style="color:var(--primary); font-size:1.25rem; margin: 30px 0 10px;">📚 โครงสร้างรายวิชา (8 บทเรียน • 40 หัวข้อย่อยแยกเพจ)</h3>
    <div class="chapters-grid">
      {chapters_cards_html}
    </div>

    <div class="cta-banner">
      <h2 style="margin: 0 0 10px 0; color: #ffffff; font-size: 1.5rem;">🚀 แพลตฟอร์มการเรียนรู้ออนไลน์ & ห้องแล็บ 3D AR</h2>
      <p style="color: var(--text-muted); margin-bottom: 20px;">สัมผัสประสบการณ์เรียนรู้แบบ Interactive จำลองสมการฟิสิกส์สด และห้องทดลองเสมือนจริง</p>
      <a href="https://tsanaphy2023.github.io/modernphysics/" target="_blank" class="btn-launch">🌐 เปิดระบบ Interactive Course & 3D AR Studio ↗</a>
      <a href="https://github.com/Tsanaphy2023/modernphysics" target="_blank" class="btn-git">📁 Source Code บน GitHub</a>
    </div>
  </div>
</div>

</body>
</html>"""

# Generate Section 0 file
sec0_path = os.path.join(MOODLE_DIR, "section_0_banner_overview.html")
with open(sec0_path, "w", encoding="utf-8") as f:
    f.write(build_section_0_banner_html())

print("Generated Section 0 Banner Overview in moodle_pages/section_0_banner_overview.html")


# -------------------------------------------------------------
# 2. GENERATE MOODLE STANDALONE SUBTOPIC PAGES (40 Pages)
# -------------------------------------------------------------
def build_standalone_moodle_html(ch, page):
    quiz = page["quiz"]
    opts_html = "".join([f"<li><b>{chr(65+i)}.</b> {opt}</li>" for i, opt in enumerate(quiz["options"])])
    ex = page["worked_example"]

    html = f"""<!DOCTYPE html>
<html lang="th">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{page["title"]} | RBRU MOOC ฟิสิกส์ยุคใหม่</title>
<style>
  :root {{
    --primary: {ch["color"]};
    --bg-dark: #0f172a;
    --text-dark: #1e293b;
    --text-light: #f8fafc;
    --card-bg: #ffffff;
    --border: #e2e8f0;
  }}
  body {{
    font-family: "Sarabun", "Prompt", -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
    line-height: 1.75;
    color: var(--text-dark);
    background: #f8fafc;
    margin: 0;
    padding: 20px;
  }}
  .moodle-page-wrapper {{
    max-width: 900px;
    margin: 0 auto;
    background: #ffffff;
    border: 1px solid var(--border);
    border-radius: 16px;
    overflow: hidden;
    box-shadow: 0 4px 20px rgba(0,0,0,0.05);
  }}
  .page-header {{
    background: {ch["bg_gradient"]};
    color: #ffffff;
    padding: 30px;
  }}
  .page-meta {{
    display: flex;
    gap: 8px;
    margin-bottom: 12px;
    flex-wrap: wrap;
  }}
  .tag {{
    background: rgba(255,255,255,0.2);
    padding: 4px 12px;
    border-radius: 20px;
    font-size: 0.85em;
    font-weight: bold;
  }}
  h1 {{ margin: 0 0 10px 0; font-size: 1.8em; line-height: 1.3; }}
  .content {{ padding: 30px; }}
  .formula-box {{
    background: #f0fdf4;
    border-left: 5px solid #10b981;
    border-radius: 8px;
    padding: 18px;
    margin: 20px 0;
  }}
  .formula-title {{ font-weight: bold; color: #047857; margin-bottom: 8px; display: block; }}
  .formula-math {{ font-size: 1.2em; text-align: center; padding: 10px 0; }}
  .example-card {{
    background: #f0f9ff;
    border: 1px solid #bae6fd;
    border-radius: 12px;
    padding: 20px;
    margin: 24px 0;
  }}
  .quiz-card {{
    background: #fefce8;
    border: 1px solid #fef08a;
    border-radius: 12px;
    padding: 20px;
    margin: 24px 0;
  }}
  .btn-ar {{
    display: inline-block;
    background: #0284c7;
    color: #ffffff;
    text-decoration: none;
    padding: 12px 24px;
    border-radius: 8px;
    font-weight: bold;
    margin-top: 15px;
    transition: background 0.2s;
  }}
  .btn-ar:hover {{ background: #0369a1; }}
  .data-table {{
    width: 100%;
    border-collapse: collapse;
    margin: 15px 0;
  }}
  .data-table th, .data-table td {{
    border: 1px solid #cbd5e1;
    padding: 10px 14px;
    text-align: left;
  }}
  .data-table th {{ background: #f1f5f9; }}
  .grid-3cards, .grid-2col {{
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
    gap: 16px;
    margin: 20px 0;
  }}
  .info-card {{
    background: #f8fafc;
    border: 1px solid #e2e8f0;
    border-radius: 8px;
    padding: 16px;
  }}
  .badge-tag {{
    display: inline-block;
    background: #e0f2fe;
    color: #0369a1;
    font-size: 0.8em;
    font-weight: bold;
    padding: 2px 8px;
    border-radius: 6px;
    margin-bottom: 6px;
  }}
  /* Interactive Simulator Styling */
  .interactive-sim-container {{
    background: #060913;
    border: 1px solid rgba(0, 240, 255, 0.25);
    border-radius: 14px;
    padding: 22px;
    margin: 25px 0;
    box-shadow: 0 8px 32px rgba(0,0,0,0.4);
    color: #f8fafc;
  }}
  .sim-panel {{ display: flex; flex-direction: column; gap: 14px; }}
  .sim-control-group {{ background: rgba(255,255,255,0.04); border: 1px solid rgba(255,255,255,0.08); border-radius: 10px; padding: 12px 16px; }}
  .sim-control-group label {{ display: block; font-size: 0.95rem; font-weight: 600; color: #cbd5e1; margin-bottom: 8px; }}
  .readout-val {{ color: #00f0ff; font-weight: 700; font-family: monospace; }}
  .sim-slider {{ width: 100%; height: 6px; border-radius: 3px; background: #1e293b; outline: none; -webkit-appearance: none; accent-color: #00f0ff; }}
  .sim-canvas-wrapper {{ width: 100%; overflow-x: auto; background: #020617; border: 1px solid rgba(255,255,255,0.1); border-radius: 10px; padding: 10px; text-align: center; }}
  .sim-canvas-wrapper canvas {{ max-width: 100%; height: auto; border-radius: 6px; display: inline-block; }}
  .sim-readout-grid {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(180px, 1fr)); gap: 12px; margin-top: 6px; }}
  .readout-card {{ background: rgba(15, 23, 42, 0.8); border: 1px solid rgba(255,255,255,0.06); border-radius: 8px; padding: 12px; text-align: center; }}
  .readout-lbl {{ font-size: 0.78rem; color: #94a3b8; margin-top: 4px; }}
</style>
<script src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
</head>
<body>

<div class="moodle-page-wrapper">
  <div class="page-header">
    <div class="page-meta">
      <span class="tag">บทที่ {ch["id"]}</span>
      <span class="tag">{page["tag"]}</span>
      <span class="tag">⏱️ {page["read_time"]}</span>
    </div>
    <h1>{page["title"]}</h1>
    <p>{page["summary"]}</p>
  </div>

  <div class="content">
    {page["content_html"]}

    <!-- Interactive Real-Time Simulator -->
    <div class="interactive-sim-container">
      <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:14px; border-bottom:1px solid rgba(255,255,255,0.1); padding-bottom:10px;">
        <h3 style="margin:0; color:#00f0ff; font-size:1.2rem;">🔬 ห้องปฏิบัติการเสมือนจริง 2D/3D Real-Time Simulator</h3>
        <span style="background:rgba(0,240,255,0.15); color:#00f0ff; font-size:0.75rem; font-weight:bold; padding:4px 10px; border-radius:20px; border:1px solid rgba(0,240,255,0.3);">LIVE INTERACTIVE</span>
      </div>
      <p style="color:#94a3b8; font-size:0.9rem; margin-bottom:15px;">ทดลองปรับตัวแปรและสังเกตผลการคำนวณทางฟิสิกส์แบบเรียลไทม์ได้โดยตรงในหน้านี้:</p>
      {get_simulator_html_and_js(page["id"], page.get("sim_type", ""), page["title"], standalone=True)}
    </div>

    <!-- Worked Example with Toggleable Hidden Solution -->
    <div class="example-card" style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:12px; padding:20px; margin:24px 0; box-shadow:0 2px 8px rgba(0,0,0,0.04);">
      <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:12px; border-bottom:1px solid #e2e8f0; padding-bottom:8px;">
        <h3 style="color:#0284c7; margin:0; font-size:1.15rem; display:flex; align-items:center; gap:8px;">
          <span>📐</span> <span>{ex["title"]}</span>
        </h3>
        <span style="background:#e0f2fe; color:#0369a1; font-size:0.75rem; font-weight:700; padding:3px 10px; border-radius:20px;">WORKED EXAMPLE</span>
      </div>
      <div style="margin-bottom:16px; font-size:1rem; line-height:1.7; color:#334155;">
        <b style="color:#0f172a;">โจทย์ตัวอย่าง:</b> {ex["problem"]}
      </div>
      
      <div class="solution-container" style="margin-top:12px;">
        <button type="button" class="btn-toggle-solution" onclick="toggleSolution('{page["id"]}')" id="btn-sol-{page["id"]}" style="background:linear-gradient(135deg, #0284c7, #0369a1); color:#ffffff; border:none; border-radius:8px; padding:9px 20px; font-size:0.92rem; font-weight:600; cursor:pointer; display:inline-flex; align-items:center; gap:8px; transition:all 0.2s ease; box-shadow:0 2px 6px rgba(2,132,199,0.25);">
          <span id="btn-icon-{page["id"]}">👁️</span>
          <span id="btn-text-{page["id"]}">คลิกเพื่อดูเฉลยและวิธีทำละเอียด</span>
        </button>
        <div class="solution-content" id="sol-content-{page["id"]}" style="display:none; margin-top:14px; padding:18px 22px; background:#ffffff; border:1px solid #bae6fd; border-radius:10px; border-left:4px solid #0284c7; box-shadow:0 4px 12px rgba(2,132,199,0.08);">
          <div style="font-weight:700; color:#0369a1; margin-bottom:10px; display:flex; align-items:center; gap:6px; font-size:0.95rem;">
            <span>📝</span> <span>เฉลยและขั้นตอนการคำนวณอย่างละเอียด:</span>
          </div>
          <div style="line-height:1.8; color:#1e293b; font-size:0.98rem;">
            {ex["solution"]}
          </div>
        </div>
      </div>
    </div>

    <div class="quiz-card">
      <h3 style="color: #854d0e; margin-top:0;">💡 คำถามทบทวนแนวคิด (Concept Check)</h3>
      <p><b>คำถาม:</b> {quiz["question"]}</p>
      <ul style="list-style: none; padding-left: 0;">
        {opts_html}
      </ul>
      <details style="margin-top: 15px; cursor: pointer;">
        <summary><b>เฉลยและคำอธิบายละเอียด (คลิกเพื่อดู)</b></summary>
        <div style="margin-top: 10px; padding: 12px; background: #ffffff; border-radius: 6px;">
          <b>คำตอบที่ถูกต้อง:</b> ข้อ {chr(65+quiz["correct"])}.<br>
          {quiz["explanation"]}
        </div>
      </details>
    </div>

    <div style="text-align: center; margin-top: 30px; padding: 20px; background: #0f172a; color: #ffffff; border-radius: 12px;">
      <h3 style="color: #38bdf8; margin: 0 0 10px 0;">🚀 ห้องปฏิบัติการเสมือนจริง 3D / AR</h3>
      <p style="color: #94a3b8; font-size: 0.9em;">เชื่อมต่อการทดลองเชิงลึกด้วย MediaPipe Hand Tracking และ Three.js Shader</p>
      <a href="https://tsanaphy2023.github.io/modernphysics/" target="_blank" class="btn-ar">🚀 เปิดห้องแล็บ AR เต็มจอ (GitHub Pages Global CDN) ↗</a>
    </div>
  </div>
</div>

<script>
function toggleSolution(pageId) {{
  const sol = document.getElementById("sol-content-" + pageId);
  const btn = document.getElementById("btn-sol-" + pageId);
  const txt = document.getElementById("btn-text-" + pageId);
  const ico = document.getElementById("btn-icon-" + pageId);
  if (!sol) return;
  if (sol.style.display === "none" || sol.style.display === "") {{
    sol.style.display = "block";
    if (txt) txt.textContent = "ซ่อนเฉลยและวิธีทำ";
    if (ico) ico.textContent = "🙈";
    if (btn) btn.style.background = "#475569";
    if (window.MathJax && window.MathJax.typesetPromise) {{
      window.MathJax.typesetPromise([sol]);
    }}
  }} else {{
    sol.style.display = "none";
    if (txt) txt.textContent = "คลิกเพื่อดูเฉลยและวิธีทำละเอียด";
    if (ico) ico.textContent = "👁️";
    if (btn) btn.style.background = "linear-gradient(135deg, #0284c7, #0369a1)";
  }}
}}
</script>

</body>
</html>"""
    return html

for ch in CHAPTERS_DATA:
    ch_dir = os.path.join(MOODLE_DIR, f"chapter_{ch['id']}")
    os.makedirs(ch_dir, exist_ok=True)
    for page in ch["pages"]:
        file_name = f"page_{page['id'].replace('.', '_')}.html"
        file_path = os.path.join(ch_dir, file_name)
        moodle_html = build_standalone_moodle_html(ch, page)
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(moodle_html)

print(f"Generated 40 Moodle standalone HTML pages in {MOODLE_DIR}")


# -------------------------------------------------------------
# 3. BUILD SUBTOPIC PAGES FOR MASTER INTERACTIVE APP
# -------------------------------------------------------------
def build_subtopic_page_html(ch, page, all_pages, current_idx):
    prev_page = all_pages[current_idx - 1] if current_idx > 0 else None
    next_page = all_pages[current_idx + 1] if current_idx < len(all_pages) - 1 else None

    # Navigation buttons
    prev_btn_html = f"""<button class="nav-page-btn prev-btn" onclick="navigateToPage('{prev_page["id"]}')">
        <span class="btn-subtext">← หัวข้อย่อยก่อนหน้า</span>
        <span class="btn-maintext">{prev_page["title"]}</span>
    </button>""" if prev_page else '<div class="nav-placeholder"></div>'

    next_btn_html = f"""<button class="nav-page-btn next-btn" onclick="navigateToPage('{next_page["id"]}')">
        <span class="btn-subtext">หัวข้อย่อยถัดไป →</span>
        <span class="btn-maintext">{next_page["title"]}</span>
    </button>""" if next_page else '<div class="nav-placeholder"></div>'

    # Quiz HTML
    quiz = page["quiz"]
    opts_html = "".join([
        f"""<button class="quiz-opt" onclick="checkQuiz('{page["id"]}', {i}, {quiz["correct"]})">{chr(65+i)}. {opt}</button>"""
        for i, opt in enumerate(quiz["options"])
    ])
    
    quiz_html = f"""
    <div class="concept-check-card" id="quiz-{page["id"]}">
      <div class="quiz-badge">💡 Concept Check: ทดสอบความเข้าใจ</div>
      <p class="quiz-question">{quiz["question"]}</p>
      <div class="quiz-options">
        {opts_html}
      </div>
      <div class="quiz-feedback" id="feedback-{page["id"]}" style="display:none;"></div>
    </div>
    """

    # Worked Example HTML with Toggle Button
    ex = page["worked_example"]
    example_html = f"""
    <div class="example-card" style="background:var(--bg-card); border:1px solid var(--border-color); border-radius:12px; padding:22px; margin:24px 0; box-shadow:0 4px 16px rgba(0,0,0,0.15);">
      <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:14px; border-bottom:1px solid var(--border-color); padding-bottom:10px;">
        <span class="example-title" style="font-weight:700; color:var(--primary); font-size:1.15rem;">📐 {ex["title"]}</span>
        <span class="example-badge" style="background:rgba(0,240,255,0.12); color:#00f0ff; font-size:0.75rem; font-weight:700; padding:4px 12px; border-radius:20px; border:1px solid rgba(0,240,255,0.3);">WORKED EXAMPLE</span>
      </div>
      <div class="example-problem" style="margin-bottom:16px; font-size:1rem; line-height:1.75; color:var(--text-main);">
        <b style="color:var(--text-highlight);">โจทย์ตัวอย่าง:</b> {ex["problem"]}
      </div>
      <div class="solution-wrapper" style="margin-top:12px;">
        <button type="button" class="btn-toggle-solution" onclick="toggleSolution('{page["id"]}')" id="btn-sol-{page["id"]}" style="background:linear-gradient(135deg, #0284c7, #0369a1); color:#ffffff; border:none; border-radius:8px; padding:9px 20px; font-size:0.92rem; font-weight:600; cursor:pointer; display:inline-flex; align-items:center; gap:8px; transition:all 0.2s ease; box-shadow:0 2px 8px rgba(2,132,199,0.3);">
          <span id="btn-icon-{page["id"]}">👁️</span>
          <span id="btn-text-{page["id"]}">คลิกเพื่อดูเฉลยและวิธีทำละเอียด</span>
        </button>
        <div class="solution-content" id="sol-content-{page["id"]}" style="display:none; margin-top:14px; padding:18px 22px; background:rgba(2,6,23,0.7); border:1px solid rgba(0,240,255,0.2); border-radius:10px; border-left:4px solid #00f0ff; box-shadow:0 4px 16px rgba(0,0,0,0.3);">
          <div style="font-weight:700; color:#00f0ff; margin-bottom:10px; display:flex; align-items:center; gap:6px; font-size:0.95rem;">
            <span>📝</span> <span>เฉลยและขั้นตอนการคำนวณอย่างละเอียด:</span>
          </div>
          <div class="example-solution" style="line-height:1.8; color:var(--text-main); font-size:0.98rem;">
            {ex["solution"]}
          </div>
        </div>
      </div>
    </div>
    """

    # Simulator HTML container
    sim_content = get_simulator_html_and_js(page["id"], page.get("sim_type", ""), page["title"], standalone=False)
    sim_html = f"""
    <div class="simulator-container" id="sim-box-{page["id"]}">
      <div class="sim-header">
        <span class="sim-title">⚡ Interactive Simulator: {page["title"]}</span>
        <span class="sim-badge">Live Computation</span>
      </div>
      <div class="sim-body" id="sim-body-{page["id"]}">
        {sim_content}
      </div>
    </div>
    """

    # AR Launcher Card
    ar_card_html = f"""
    <div class="ar-launcher-card">
      <span class="ar-badge">AR / 3D SIMULATION</span>
      <h4>🚀 ห้องปฏิบัติการเสมือนจริง 3D & AR สำหรับ {page["title"]}</h4>
      <p>เชื่อมต่อการจำลองเชิงปฏิสัมพันธ์ด้วย Three.js และ MediaPipe Hand Tracking รองรับการแสดงผลบนอุปกรณ์ทุกประเภท</p>
      <a href="https://tsanaphy2023.github.io/modernphysics/" target="_blank" class="btn-ar-launch">🌐 เปิดห้องทดลอง 3D / AR เต็มจอ (Global CDN) ↗</a>
    </div>
    """

    page_html = f"""
    <article class="subtopic-page" id="page-{page["id"]}" data-ch="{ch["id"]}" data-page="{page["id"]}" style="display: none;">
      <!-- Page Header -->
      <div class="page-top-banner" style="background: {ch["bg_gradient"]};">
        <div class="page-meta-row">
          <span class="page-chapter-pill">บทที่ {ch["id"]}</span>
          <span class="page-tag-pill">{page["tag"]}</span>
          <span class="page-time-pill">⏱️ อ่าน {page["read_time"]}</span>
        </div>
        <h1 class="page-main-heading">{page["title"]}</h1>
        <p class="page-summary-lead">{page["summary"]}</p>
      </div>

      <!-- Main Content -->
      <div class="page-inner-content">
        {page["content_html"]}
        {sim_html}
        {example_html}
        {quiz_html}
        {ar_card_html}
      </div>

      <!-- Bottom Pagination -->
      <div class="page-bottom-nav">
        {prev_btn_html}
        <button class="nav-page-btn toc-btn" onclick="openTocModal()">
          <span class="btn-subtext">สารบัญวิชา</span>
          <span class="btn-maintext">📋 รายการหัวข้อทั้งหมด</span>
        </button>
        {next_btn_html}
      </div>
    </article>
    """
    return page_html

# Render all subtopic pages
pages_html_list = []
for idx, item in enumerate(ALL_SUBPAGES):
    p_html = build_subtopic_page_html(item["chapter"], item["page"], [p["page"] for p in ALL_SUBPAGES], idx)
    pages_html_list.append(p_html)

all_rendered_pages_html = "\n".join(pages_html_list)

# Render Overview Page HTML (Welcome page)
overview_chapters_grid = "".join([
    f"""<div class="overview-ch-card" onclick="navigateToPage('{ch['pages'][0]['id']}')">
      <div class="ch-badge" style="background:{ch['color']}; display:inline-block; margin-bottom:8px;">บทที่ {ch['id']}</div>
      <h3 style="color:#ffffff; font-size:1.1rem; margin-bottom:6px;">{ch['title'].replace(f"บทที่ {ch['id']} ", "")}</h3>
      <p style="color:var(--text-muted); font-size:0.85rem; margin-bottom:10px;">{ch['description']}</p>
      <div class="ch-sub-pills">
        {"".join([f"<span class='mini-pill'>{p['id']}</span>" for p in ch['pages']])}
      </div>
    </div>"""
    for ch in CHAPTERS_DATA
])

overview_page_html = f"""
<article class="subtopic-page" id="page-overview" style="display: block;">
  <div class="hero-banner-card">
    <img src="assets/images/modern_physics_banner.jpg" onerror="this.src='https://raw.githubusercontent.com/Tsanaphy2023/modernphysics/main/assets/images/modern_physics_banner.jpg'" alt="Modern Physics Banner" class="hero-banner-img">
    <div class="hero-banner-content">
      <span class="hero-pill">RBRU MOOC COURSEWARE • 4012920</span>
      <h1 class="hero-title">ฟิสิกส์ยุคใหม่ (Modern Physics)</h1>
      <p class="hero-lead">หลักสูตรวิชาการและแพลตฟอร์มการเรียนรู้เชิงปฏิสัมพันธ์ (Interactive Course & 3D AR Simulator) ประจำมหาวิทยาลัยราชภัฏรำไพพรรณี</p>
      <div class="hero-actions">
        <button class="btn-hero-start" onclick="navigateToPage('1.1')">🚀 เริ่มต้นศึกษาบทที่ 1.1</button>
        <button class="btn-hero-outline" onclick="openTocModal()">📋 ดูสารบัญ 40 หัวข้อ</button>
        <a href="https://github.com/Tsanaphy2023/modernphysics" target="_blank" class="btn-hero-git">📁 GitHub Repo</a>
      </div>
    </div>
  </div>

  <div class="grid-2col" style="margin: 30px 0;">
    <div class="info-card" style="border-left: 4px solid var(--primary-cyan);">
      <h3 style="color: var(--primary-cyan); margin-top:0;">👨‍🏫 อาจารย์ผู้รับผิดชอบรายวิชา</h3>
      <p style="font-size: 1.05rem; font-weight: 600; margin-bottom: 4px; color:#ffffff;">ผู้ช่วยศาสตราจารย์ ดร.ชีวะ ทัศนา (Asst. Prof. Dr. Chewa Thassana)</p>
      <p style="color: var(--text-muted); font-size: 0.9rem; margin:0;">สาขาวิชาฟิสิกส์ คณะวิทยาศาสตร์และเทคโนโลยี มหาวิทยาลัยราชภัฏรำไพพรรณี</p>
      <p style="color: var(--text-muted); font-size: 0.85rem; margin-top:8px;">ระบบ E-Learning Portal: <a href="https://elearning.rbru.ac.th/course/view.php?id=262" target="_blank" style="color:var(--primary-cyan);">Course ID 262 (elearning.rbru.ac.th)</a></p>
    </div>
    <div class="info-card" style="border-left: 4px solid var(--accent-emerald);">
      <h3 style="color: var(--accent-emerald); margin-top:0;">🎯 จุดเด่นของแพลตฟอร์มรายวิชา</h3>
      <ul style="color: var(--text-muted); font-size: 0.9rem; padding-left: 20px; margin:0;">
        <li><b>40 หัวข้อย่อยแยกเพจสมบูรณ์:</b> 8 บทเรียน × 5 หน้าย่อย โฟกัสเฉพาะประเด็น</li>
        <li><b>Live Computation Simulators:</b> ปรับค่าตัวแปรเพื่อเห็นผลการคำนวณแบบ Real-time</li>
        <li><b>Worked Examples & Concept Checks:</b> ตัวอย่างโจทย์ละเอียดและแบบทดสอบตรวจคำตอบสด</li>
        <li><b>3D AR Physics Studio:</b> เชื่อมต่อระบบจำลองเสมือนจริงระดับสูง</li>
      </ul>
    </div>
  </div>

  <h2 style="font-size: 1.4rem; color: #ffffff; margin: 30px 0 16px;">📚 สารบัญทั้ง 8 บทเรียน (คลิกเพื่อเข้าสู่เนื้อหา)</h2>
  <div class="overview-grid">
    {overview_chapters_grid}
  </div>
</article>
"""

# Render Sidebar Accordion HTML
sidebar_chapters_html = []
for ch in CHAPTERS_DATA:
    subpages_links = []
    for page in ch["pages"]:
        subpages_links.append(f"""
        <li class="sidebar-subitem" id="nav-{page["id"]}" onclick="navigateToPage('{page["id"]}')">
          <span class="subitem-num">{page["id"]}</span>
          <span class="subitem-title">{page["title"].replace(f"{page['id']} ", "")}</span>
          <span class="check-icon" id="check-{page["id"]}">✓</span>
        </li>
        """)
    subpages_html = "".join(subpages_links)

    sidebar_chapters_html.append(f"""
    <div class="sidebar-chapter-group" id="ch-group-{ch["id"]}">
      <div class="sidebar-chapter-header" onclick="toggleChapterAccordion({ch["id"]})">
        <span class="ch-badge" style="background: {ch["color"]};">บทที่ {ch["id"]}</span>
        <span class="ch-title">{ch["title"].replace(f"บทที่ {ch['id']} ", "")}</span>
        <span class="accordion-arrow">▾</span>
      </div>
      <ul class="sidebar-sublist" id="sublist-{ch["id"]}">
        {subpages_html}
      </ul>
    </div>
    """)

sidebar_full_html = "".join(sidebar_chapters_html)

# Render Table of Contents Modal HTML
toc_cards_html = []
for ch in CHAPTERS_DATA:
    toc_pages = "".join([
        f"""<a href="javascript:void(0)" onclick="navigateToPage('{page["id"]}'); closeTocModal();" class="toc-modal-link">
            <span class="toc-num">{page["id"]}</span> {page["title"].replace(f"{page['id']} ", "")}
        </a>"""
        for page in ch["pages"]
    ])
    toc_cards_html.append(f"""
    <div class="toc-chapter-box">
      <div class="toc-ch-title" style="color: {ch["color"]};">บทที่ {ch["id"]} {ch["title"].replace(f"บทที่ {ch['id']} ", "")}</div>
      <div class="toc-links-grid">{toc_pages}</div>
    </div>
    """)
toc_full_modal_html = "".join(toc_cards_html)


# -------------------------------------------------------------
# 4. MASTER INTERACTIVE APP HTML
# -------------------------------------------------------------
MASTER_HTML = f"""<!DOCTYPE html>
<html lang="th" data-theme="dark">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>RBRU MOOC | ฟิสิกส์ยุคใหม่ (Modern Physics 4012920)</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Prompt:wght@300;400;500;600;700&family=Sarabun:wght@300;400;500;600;700&family=JetBrains+Mono:wght@400;600&display=swap" rel="stylesheet">
<script src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js" id="MathJax-script" async></script>
<style>
/* CSS DESIGN SYSTEM & TOKENS */
:root {{
  --bg-main: #0b1120;
  --bg-surface: #0f172a;
  --bg-card: rgba(30, 41, 59, 0.7);
  --bg-sidebar: #090e1a;
  --border-color: rgba(255, 255, 255, 0.08);
  --border-focus: #00f0ff;
  --text-main: #f8fafc;
  --text-muted: #94a3b8;
  --text-highlight: #38bdf8;
  --primary-cyan: #00f0ff;
  --primary-teal: #0891b2;
  --accent-gold: #f59e0b;
  --accent-coral: #f43f5e;
  --accent-emerald: #10b981;
  --accent-purple: #a855f7;
  --sidebar-w: 320px;
  --header-h: 65px;
  --radius-lg: 16px;
  --radius-md: 10px;
  --radius-sm: 6px;
  --shadow-main: 0 10px 30px -5px rgba(0, 0, 0, 0.5);
  --glass-bg: rgba(15, 23, 42, 0.85);
  --glass-border: 1px solid rgba(255, 255, 255, 0.08);
}}

[data-theme="light"] {{
  --bg-main: #f1f5f9;
  --bg-surface: #ffffff;
  --bg-card: #ffffff;
  --bg-sidebar: #f8fafc;
  --border-color: #e2e8f0;
  --border-focus: #0284c7;
  --text-main: #0f172a;
  --text-muted: #64748b;
  --text-highlight: #0284c7;
  --primary-cyan: #0284c7;
  --primary-teal: #0891b2;
  --glass-bg: rgba(255, 255, 255, 0.9);
  --glass-border: 1px solid #e2e8f0;
}}

* {{ box-sizing: border-box; margin: 0; padding: 0; }}

body {{
  font-family: "Sarabun", "Prompt", sans-serif;
  background: var(--bg-main);
  color: var(--text-main);
  line-height: 1.8;
  overflow-x: hidden;
}}

/* APP LAYOUT */
.app-container {{
  display: flex;
  min-height: 100vh;
}}

/* SIDEBAR */
.sidebar {{
  width: var(--sidebar-w);
  background: var(--bg-sidebar);
  border-right: var(--glass-border);
  display: flex;
  flex-direction: column;
  position: fixed;
  top: 0;
  bottom: 0;
  left: 0;
  z-index: 100;
  transition: transform 0.3s cubic-bezier(0.4, 0, 0.2, 1);
}}

.sidebar-header {{
  padding: 18px 20px;
  border-bottom: var(--glass-border);
  background: linear-gradient(135deg, rgba(8, 145, 178, 0.15) 0%, rgba(2, 132, 199, 0.05) 100%);
  cursor: pointer;
}}

.sidebar-brand {{
  font-size: 1.15rem;
  font-weight: 700;
  color: var(--primary-cyan);
  display: flex;
  align-items: center;
  gap: 10px;
}}

.sidebar-subbrand {{
  font-size: 0.82rem;
  color: var(--text-muted);
  margin-top: 4px;
}}

.sidebar-search-box {{
  padding: 12px 18px;
  border-bottom: var(--glass-border);
}}

.search-input {{
  width: 100%;
  padding: 10px 14px;
  border-radius: var(--radius-md);
  border: var(--glass-border);
  background: var(--bg-surface);
  color: var(--text-main);
  font-size: 0.88rem;
  outline: none;
  transition: border-color 0.2s;
}}

.search-input:focus {{
  border-color: var(--primary-cyan);
}}

.sidebar-scroll {{
  flex: 1;
  overflow-y: auto;
  padding: 14px 10px;
}}

.sidebar-home-item {{
  display: flex;
  align-items: center;
  gap: 10px;
  padding: 10px 12px;
  border-radius: var(--radius-md);
  margin-bottom: 12px;
  color: var(--primary-cyan);
  background: rgba(0, 240, 255, 0.08);
  font-weight: 600;
  font-size: 0.9rem;
  cursor: pointer;
  border: 1px solid rgba(0, 240, 255, 0.2);
  transition: all 0.2s;
}}

.sidebar-home-item:hover {{
  background: rgba(0, 240, 255, 0.15);
}}

.sidebar-chapter-group {{
  margin-bottom: 8px;
}}

.sidebar-chapter-header {{
  display: flex;
  align-items: center;
  gap: 8px;
  padding: 10px 12px;
  border-radius: var(--radius-md);
  cursor: pointer;
  background: rgba(255, 255, 255, 0.02);
  transition: all 0.2s;
}}

.sidebar-chapter-header:hover {{
  background: rgba(255, 255, 255, 0.06);
}}

.ch-badge {{
  font-size: 0.72rem;
  font-weight: 700;
  padding: 2px 7px;
  border-radius: 6px;
  color: #fff;
  white-space: nowrap;
}}

.ch-title {{
  font-size: 0.88rem;
  font-weight: 600;
  flex: 1;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}}

.accordion-arrow {{
  font-size: 0.8rem;
  color: var(--text-muted);
  transition: transform 0.25s;
}}

.sidebar-chapter-group.open .accordion-arrow {{
  transform: rotate(180deg);
}}

.sidebar-sublist {{
  list-style: none;
  padding: 4px 0 4px 12px;
  display: none;
}}

.sidebar-chapter-group.open .sidebar-sublist {{
  display: block;
}}

.sidebar-subitem {{
  display: flex;
  align-items: center;
  gap: 8px;
  padding: 7px 12px;
  border-radius: var(--radius-sm);
  font-size: 0.82rem;
  color: var(--text-muted);
  cursor: pointer;
  transition: all 0.2s;
  position: relative;
  margin: 2px 0;
}}

.sidebar-subitem:hover {{
  color: var(--text-main);
  background: rgba(255, 255, 255, 0.04);
}}

.sidebar-subitem.active {{
  color: var(--primary-cyan);
  background: rgba(0, 240, 255, 0.08);
  font-weight: 600;
  border-left: 3px solid var(--primary-cyan);
}}

.subitem-num {{
  font-family: "JetBrains Mono", monospace;
  font-size: 0.76rem;
  color: var(--text-muted);
}}

.sidebar-subitem.active .subitem-num {{
  color: var(--primary-cyan);
}}

.subitem-title {{
  flex: 1;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}}

.check-icon {{
  font-size: 0.72rem;
  color: var(--accent-emerald);
  opacity: 0;
}}

.sidebar-subitem.completed .check-icon {{
  opacity: 1;
}}

/* MAIN CONTENT VIEWPORT */
.main-viewport {{
  margin-left: var(--sidebar-w);
  flex: 1;
  display: flex;
  flex-direction: column;
  min-height: 100vh;
}}

/* TOP NAVBAR */
.top-navbar {{
  height: var(--header-h);
  background: var(--glass-bg);
  backdrop-filter: blur(16px);
  -webkit-backdrop-filter: blur(16px);
  border-bottom: var(--glass-border);
  position: sticky;
  top: 0;
  z-index: 90;
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 0 24px;
}}

.nav-left {{
  display: flex;
  align-items: center;
  gap: 14px;
}}

.btn-sidebar-toggle {{
  display: none;
  background: transparent;
  border: var(--glass-border);
  color: var(--text-main);
  padding: 8px 12px;
  border-radius: var(--radius-sm);
  cursor: pointer;
}}

.breadcrumbs {{
  font-size: 0.88rem;
  color: var(--text-muted);
  display: flex;
  align-items: center;
  gap: 8px;
}}

.bc-item {{
  color: var(--text-muted);
  cursor: pointer;
}}

.bc-item:hover {{
  color: var(--primary-cyan);
}}

.bc-current {{
  color: var(--text-main);
  font-weight: 600;
}}

.nav-right {{
  display: flex;
  align-items: center;
  gap: 12px;
}}

.course-progress-badge {{
  font-size: 0.8rem;
  background: rgba(16, 185, 129, 0.12);
  color: var(--accent-emerald);
  padding: 4px 12px;
  border-radius: 20px;
  font-weight: 600;
}}

.btn-icon {{
  background: var(--bg-surface);
  border: var(--glass-border);
  color: var(--text-main);
  width: 38px;
  height: 38px;
  border-radius: var(--radius-md);
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  font-size: 1.05rem;
  transition: all 0.2s;
  text-decoration: none;
}}

.btn-icon:hover {{
  border-color: var(--primary-cyan);
  color: var(--primary-cyan);
}}

/* SUBTOPIC TABS BAR (Active chapter's 5 subtopic pills) */
.subtopic-tabs-bar {{
  background: var(--bg-surface);
  border-bottom: var(--glass-border);
  padding: 10px 24px;
  display: flex;
  align-items: center;
  gap: 8px;
  overflow-x: auto;
  scrollbar-width: none;
}}

.subtopic-tabs-bar::-webkit-scrollbar {{
  display: none;
}}

.tab-pill {{
  background: rgba(255, 255, 255, 0.03);
  border: var(--glass-border);
  color: var(--text-muted);
  padding: 8px 16px;
  border-radius: 30px;
  font-size: 0.84rem;
  cursor: pointer;
  white-space: nowrap;
  transition: all 0.2s;
  display: flex;
  align-items: center;
  gap: 6px;
}}

.tab-pill:hover {{
  background: rgba(255, 255, 255, 0.08);
  color: var(--text-main);
}}

.tab-pill.active {{
  background: var(--primary-teal);
  color: #ffffff;
  font-weight: 600;
  border-color: var(--primary-cyan);
  box-shadow: 0 0 15px rgba(0, 240, 255, 0.25);
}}

/* CONTENT CONTAINER */
.content-stage {{
  flex: 1;
  max-width: 1060px;
  width: 100%;
  margin: 0 auto;
  padding: 30px 24px 80px;
}}

/* HERO BANNER CARD (OVERVIEW PAGE) */
.hero-banner-card {{
  background: #060a14;
  border: 1px solid rgba(0, 240, 255, 0.3);
  border-radius: var(--radius-lg);
  overflow: hidden;
  margin-bottom: 30px;
  box-shadow: 0 10px 40px rgba(0, 240, 255, 0.15);
}}

.hero-banner-img {{
  width: 100%;
  height: auto;
  display: block;
  object-fit: cover;
}}

.hero-banner-content {{
  padding: 30px;
  background: linear-gradient(180deg, rgba(6, 10, 20, 0.4) 0%, rgba(15, 23, 42, 0.95) 100%);
}}

.hero-pill {{
  display: inline-block;
  background: var(--primary-cyan);
  color: #060a14;
  font-size: 0.8rem;
  font-weight: 700;
  padding: 4px 14px;
  border-radius: 20px;
  margin-bottom: 12px;
}}

.hero-title {{
  font-size: clamp(1.8rem, 3.5vw, 2.5rem);
  font-weight: 700;
  color: #ffffff;
  margin-bottom: 10px;
  line-height: 1.25;
}}

.hero-lead {{
  color: var(--text-muted);
  font-size: 1.05rem;
  max-width: 800px;
  margin-bottom: 24px;
}}

.hero-actions {{
  display: flex;
  gap: 12px;
  flex-wrap: wrap;
}}

.btn-hero-start {{
  background: linear-gradient(135deg, #00f0ff 0%, #0284c7 100%);
  color: #060a14;
  font-weight: 700;
  padding: 12px 28px;
  border-radius: 30px;
  border: none;
  font-size: 0.95rem;
  cursor: pointer;
  box-shadow: 0 4px 20px rgba(0, 240, 255, 0.4);
  transition: transform 0.2s;
}}

.btn-hero-start:hover {{
  transform: translateY(-2px);
}}

.btn-hero-outline {{
  background: rgba(255, 255, 255, 0.05);
  color: #ffffff;
  font-weight: 600;
  padding: 12px 24px;
  border-radius: 30px;
  border: var(--glass-border);
  font-size: 0.95rem;
  cursor: pointer;
}}

.btn-hero-git {{
  background: rgba(255, 255, 255, 0.1);
  color: #ffffff;
  font-weight: 600;
  padding: 12px 24px;
  border-radius: 30px;
  border: 1px solid rgba(255, 255, 255, 0.2);
  text-decoration: none;
  font-size: 0.95rem;
  display: inline-flex;
  align-items: center;
}}

.overview-grid {{
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
  gap: 18px;
  margin: 20px 0;
}}

.overview-ch-card {{
  background: var(--bg-card);
  border: var(--glass-border);
  border-radius: var(--radius-md);
  padding: 20px;
  cursor: pointer;
  transition: all 0.25s;
}}

.overview-ch-card:hover {{
  border-color: var(--primary-cyan);
  transform: translateY(-3px);
  background: rgba(0, 240, 255, 0.05);
}}

.ch-sub-pills {{
  display: flex;
  gap: 6px;
  flex-wrap: wrap;
}}

.mini-pill {{
  background: rgba(255, 255, 255, 0.06);
  color: var(--text-muted);
  font-size: 0.75rem;
  padding: 2px 8px;
  border-radius: 12px;
  font-family: "JetBrains Mono", monospace;
}}

/* DEDICATED SUBTOPIC PAGE STYLING */
.subtopic-page {{
  animation: fadeInPage 0.35s cubic-bezier(0.16, 1, 0.3, 1);
}}

@keyframes fadeInPage {{
  from {{ opacity: 0; transform: translateY(12px); }}
  to {{ opacity: 1; transform: translateY(0); }}
}}

.page-top-banner {{
  padding: 36px 32px;
  border-radius: var(--radius-lg);
  color: #ffffff;
  margin-bottom: 28px;
  box-shadow: var(--shadow-main);
  position: relative;
  overflow: hidden;
}}

.page-meta-row {{
  display: flex;
  gap: 10px;
  margin-bottom: 14px;
  flex-wrap: wrap;
}}

.page-chapter-pill {{
  background: rgba(0,0,0,0.3);
  padding: 4px 12px;
  border-radius: 20px;
  font-size: 0.8rem;
  font-weight: 700;
}}

.page-tag-pill {{
  background: rgba(255,255,255,0.2);
  padding: 4px 12px;
  border-radius: 20px;
  font-size: 0.8rem;
  font-weight: 600;
}}

.page-time-pill {{
  background: rgba(0,0,0,0.2);
  padding: 4px 12px;
  border-radius: 20px;
  font-size: 0.8rem;
}}

.page-main-heading {{
  font-size: clamp(1.6rem, 3vw, 2.3rem);
  font-weight: 700;
  line-height: 1.25;
  margin-bottom: 12px;
}}

.page-summary-lead {{
  font-size: 1.05rem;
  opacity: 0.92;
  max-width: 800px;
}}

/* THEORY SECTIONS & CARDS */
.theory-section {{
  margin-bottom: 30px;
}}

.theory-section h3 {{
  font-size: 1.35rem;
  color: var(--text-highlight);
  margin: 24px 0 12px;
}}

.theory-section p {{
  margin-bottom: 16px;
  font-size: 1.02rem;
  color: var(--text-main);
}}

.grid-3cards {{
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
  gap: 18px;
  margin: 20px 0;
}}

.grid-2col {{
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));
  gap: 18px;
  margin: 20px 0;
}}

.info-card {{
  background: var(--bg-card);
  border: var(--glass-border);
  border-radius: var(--radius-md);
  padding: 20px;
  backdrop-filter: blur(10px);
}}

.badge-tag {{
  display: inline-block;
  background: rgba(0, 240, 255, 0.1);
  color: var(--primary-cyan);
  font-size: 0.76rem;
  font-weight: 700;
  padding: 2px 10px;
  border-radius: 12px;
  margin-bottom: 8px;
}}

.info-card h4 {{
  font-size: 1.05rem;
  margin-bottom: 8px;
  color: var(--text-main);
}}

.info-card p {{
  font-size: 0.92rem;
  color: var(--text-muted);
  line-height: 1.6;
  margin: 0;
}}

/* FORMULA BOX */
.formula-box {{
  background: linear-gradient(135deg, rgba(8, 145, 178, 0.1) 0%, rgba(16, 185, 129, 0.05) 100%);
  border-left: 5px solid var(--primary-cyan);
  border-radius: var(--radius-md);
  padding: 22px;
  margin: 24px 0;
  border-top: var(--glass-border);
  border-right: var(--glass-border);
  border-bottom: var(--glass-border);
}}

.formula-header {{
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 10px;
  flex-wrap: wrap;
}}

.formula-title {{
  font-weight: 700;
  color: var(--primary-cyan);
  font-size: 1rem;
}}

.formula-category {{
  font-size: 0.75rem;
  background: rgba(0, 240, 255, 0.15);
  color: var(--primary-cyan);
  padding: 2px 8px;
  border-radius: 8px;
}}

.formula-math {{
  font-size: 1.25rem;
  padding: 12px 0;
  text-align: center;
  color: #ffffff;
}}

[data-theme="light"] .formula-math {{
  color: #0f172a;
}}

/* TABLES */
.data-table {{
  width: 100%;
  border-collapse: collapse;
  margin: 16px 0;
  font-size: 0.92rem;
}}

.data-table th, .data-table td {{
  border: var(--glass-border);
  padding: 12px 16px;
  text-align: left;
}}

.data-table th {{
  background: rgba(255, 255, 255, 0.04);
  color: var(--text-highlight);
}}

/* INTERACTIVE SIMULATORS */
.simulator-container {{
  background: var(--bg-surface);
  border: 1px solid var(--border-color);
  border-radius: var(--radius-lg);
  margin: 30px 0;
  overflow: hidden;
  box-shadow: var(--shadow-main);
}}

.sim-header {{
  background: rgba(255, 255, 255, 0.03);
  border-bottom: var(--glass-border);
  padding: 14px 20px;
  display: flex;
  justify-content: space-between;
  align-items: center;
}}

.sim-title {{
  font-weight: 700;
  color: var(--accent-gold);
  font-size: 0.98rem;
}}

.sim-badge {{
  font-size: 0.75rem;
  background: rgba(245, 158, 11, 0.15);
  color: var(--accent-gold);
  padding: 2px 10px;
  border-radius: 12px;
  font-weight: 600;
}}

.sim-body {{
  padding: 24px;
}}

.sim-control-group {{
  margin-bottom: 16px;
}}

.sim-control-group label {{
  display: flex;
  justify-content: space-between;
  font-size: 0.9rem;
  font-weight: 600;
  margin-bottom: 6px;
}}

.sim-slider {{
  width: 100%;
  accent-color: var(--primary-cyan);
  cursor: pointer;
}}

.sim-canvas-wrapper {{
  background: #060913;
  border: 1px solid rgba(255, 255, 255, 0.06);
  border-radius: var(--radius-md);
  margin: 16px 0;
  position: relative;
  overflow: hidden;
  min-height: 220px;
  display: flex;
  align-items: center;
  justify-content: center;
}}

.sim-canvas-wrapper canvas {{
  max-width: 100%;
  display: block;
}}

.sim-readout-grid {{
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(160px, 1fr));
  gap: 12px;
  margin-top: 14px;
}}

.readout-card {{
  background: rgba(255, 255, 255, 0.02);
  border: var(--glass-border);
  padding: 12px 14px;
  border-radius: var(--radius-sm);
  text-align: center;
}}

.readout-val {{
  font-size: 1.25rem;
  font-weight: 700;
  color: var(--primary-cyan);
  font-family: "JetBrains Mono", monospace;
}}

.readout-lbl {{
  font-size: 0.76rem;
  color: var(--text-muted);
}}

/* WORKED EXAMPLE CARDS */
.example-card {{
  background: linear-gradient(135deg, rgba(2, 132, 199, 0.08) 0%, rgba(30, 41, 59, 0.4) 100%);
  border: 1px solid rgba(2, 132, 199, 0.3);
  border-radius: var(--radius-lg);
  padding: 24px;
  margin: 28px 0;
}}

.example-header {{
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 12px;
}}

.example-title {{
  font-size: 1.1rem;
  font-weight: 700;
  color: #38bdf8;
}}

.example-badge {{
  font-size: 0.75rem;
  background: rgba(56, 189, 248, 0.15);
  color: #38bdf8;
  padding: 2px 10px;
  border-radius: 12px;
  font-weight: 600;
}}

.example-problem {{
  font-size: 0.98rem;
  margin-bottom: 14px;
  color: var(--text-main);
}}

.example-solution {{
  background: rgba(0, 0, 0, 0.3);
  border-radius: var(--radius-md);
  padding: 16px 18px;
  font-size: 0.95rem;
  border-left: 4px solid #38bdf8;
}}

[data-theme="light"] .example-solution {{
  background: #ffffff;
}}

/* CONCEPT CHECK QUIZ */
.concept-check-card {{
  background: linear-gradient(135deg, rgba(245, 158, 11, 0.08) 0%, rgba(30, 41, 59, 0.4) 100%);
  border: 1px solid rgba(245, 158, 11, 0.3);
  border-radius: var(--radius-lg);
  padding: 24px;
  margin: 28px 0;
}}

.quiz-badge {{
  font-size: 0.85rem;
  font-weight: 700;
  color: var(--accent-gold);
  margin-bottom: 8px;
}}

.quiz-question {{
  font-size: 1.05rem;
  font-weight: 600;
  margin-bottom: 16px;
}}

.quiz-options {{
  display: flex;
  flex-direction: column;
  gap: 10px;
}}

.quiz-opt {{
  background: rgba(255, 255, 255, 0.04);
  border: var(--glass-border);
  color: var(--text-main);
  padding: 12px 16px;
  border-radius: var(--radius-md);
  text-align: left;
  cursor: pointer;
  font-size: 0.95rem;
  transition: all 0.2s;
}}

.quiz-opt:hover {{
  background: rgba(255, 255, 255, 0.1);
  border-color: var(--accent-gold);
}}

.quiz-opt.correct {{
  background: rgba(16, 185, 129, 0.2) !important;
  border-color: var(--accent-emerald) !important;
  color: #ffffff;
}}

.quiz-opt.wrong {{
  background: rgba(244, 63, 94, 0.2) !important;
  border-color: var(--accent-coral) !important;
}}

.quiz-feedback {{
  margin-top: 16px;
  padding: 14px 18px;
  border-radius: var(--radius-md);
  font-size: 0.95rem;
}}

/* AR LAUNCHER CARD */
.ar-launcher-card {{
  background: linear-gradient(135deg, #0c4a6e 0%, #0f172a 100%);
  border: 1px solid var(--primary-cyan);
  border-radius: var(--radius-lg);
  padding: 26px;
  text-align: center;
  margin: 30px 0;
  box-shadow: 0 0 30px rgba(0, 240, 255, 0.15);
}}

.ar-badge {{
  display: inline-block;
  background: var(--primary-cyan);
  color: #0b1120;
  font-weight: 700;
  font-size: 0.8rem;
  padding: 3px 12px;
  border-radius: 20px;
  margin-bottom: 12px;
}}

.ar-launcher-card h4 {{
  font-size: 1.3rem;
  color: #ffffff;
  margin-bottom: 8px;
}}

.ar-launcher-card p {{
  color: #94a3b8;
  font-size: 0.95rem;
  max-width: 600px;
  margin: 0 auto 18px;
}}

.btn-ar-launch {{
  display: inline-block;
  background: linear-gradient(135deg, #00f0ff 0%, #0284c7 100%);
  color: #0b1120;
  font-weight: 700;
  font-size: 1rem;
  padding: 12px 28px;
  border-radius: 30px;
  text-decoration: none;
  box-shadow: 0 4px 20px rgba(0, 240, 255, 0.4);
  transition: transform 0.2s, box-shadow 0.2s;
}}

.btn-ar-launch:hover {{
  transform: translateY(-2px);
  box-shadow: 0 6px 25px rgba(0, 240, 255, 0.6);
}}

/* BOTTOM PAGINATION CONTROLS */
.page-bottom-nav {{
  display: flex;
  justify-content: space-between;
  align-items: stretch;
  gap: 14px;
  margin-top: 50px;
  padding-top: 24px;
  border-top: var(--glass-border);
  flex-wrap: wrap;
}}

.nav-page-btn {{
  flex: 1;
  min-width: 220px;
  background: var(--bg-surface);
  border: var(--glass-border);
  border-radius: var(--radius-md);
  padding: 16px 20px;
  color: var(--text-main);
  cursor: pointer;
  display: flex;
  flex-direction: column;
  text-align: left;
  transition: all 0.2s;
}}

.nav-page-btn.next-btn {{
  text-align: right;
}}

.nav-page-btn.toc-btn {{
  flex: 0.6;
  min-width: 160px;
  text-align: center;
  align-items: center;
  justify-content: center;
}}

.nav-page-btn:hover {{
  border-color: var(--primary-cyan);
  background: rgba(0, 240, 255, 0.05);
}}

.btn-subtext {{
  font-size: 0.76rem;
  color: var(--text-muted);
  margin-bottom: 4px;
}}

.btn-maintext {{
  font-size: 0.95rem;
  font-weight: 600;
  color: var(--text-highlight);
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}}

.nav-placeholder {{
  flex: 1;
}}

/* TOC MODAL */
.modal-backdrop {{
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: rgba(0,0,0,0.75);
  backdrop-filter: blur(8px);
  z-index: 1000;
  display: none;
  align-items: center;
  justify-content: center;
  padding: 20px;
}}

.modal-backdrop.open {{
  display: flex;
}}

.modal-content {{
  background: var(--bg-surface);
  border: var(--glass-border);
  border-radius: var(--radius-lg);
  max-width: 860px;
  width: 100%;
  max-height: 85vh;
  display: flex;
  flex-direction: column;
  overflow: hidden;
}}

.modal-header {{
  padding: 20px 24px;
  border-bottom: var(--glass-border);
  display: flex;
  justify-content: space-between;
  align-items: center;
}}

.modal-body {{
  padding: 24px;
  overflow-y: auto;
}}

.toc-chapter-box {{
  margin-bottom: 22px;
}}

.toc-ch-title {{
  font-size: 1.05rem;
  font-weight: 700;
  margin-bottom: 8px;
}}

.toc-links-grid {{
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(220px, 1fr));
  gap: 8px;
}}

.toc-modal-link {{
  background: rgba(255, 255, 255, 0.03);
  border: var(--glass-border);
  color: var(--text-main);
  padding: 8px 12px;
  border-radius: var(--radius-sm);
  text-decoration: none;
  font-size: 0.84rem;
  transition: all 0.2s;
}}

.toc-modal-link:hover {{
  background: rgba(0, 240, 255, 0.1);
  color: var(--primary-cyan);
}}

.toc-num {{
  font-family: "JetBrains Mono", monospace;
  font-weight: 700;
  color: var(--primary-cyan);
}}

/* RESPONSIVE MOBILE */
@media (max-width: 900px) {{
  .sidebar {{
    transform: translateX(-100%);
  }}
  .sidebar.open {{
    transform: translateX(0);
  }}
  .main-viewport {{
    margin-left: 0;
  }}
  .btn-sidebar-toggle {{
    display: block;
  }}
}}
</style>
</head>
<body>

<div class="app-container">
  <!-- SIDEBAR -->
  <aside class="sidebar" id="appSidebar">
    <div class="sidebar-header" onclick="navigateToPage('overview')">
      <div class="sidebar-brand">
        <span>⚛️</span>
        <span>RBRU MOOC</span>
      </div>
      <div class="sidebar-subbrand">ฟิสิกส์ยุคใหม่ (Modern Physics) 4012920</div>
    </div>

    <div class="sidebar-search-box">
      <div class="sidebar-home-item" onclick="navigateToPage('overview')">
        <span>🏠</span>
        <span>ภาพรวมรายวิชา & แบนเนอร์</span>
      </div>
      <input type="text" id="quickSearchInput" class="search-input" placeholder="🔍 ค้นหาหัวข้อ, สมการ, ทฤษฎี...">
    </div>

    <div class="sidebar-scroll">
      {sidebar_full_html}
    </div>
  </aside>

  <!-- MAIN VIEWPORT -->
  <main class="main-viewport">
    <!-- TOP NAVBAR -->
    <header class="top-navbar">
      <div class="nav-left">
        <button class="btn-sidebar-toggle" onclick="toggleSidebar()">☰ สารบัญ</button>
        <nav class="breadcrumbs" id="topBreadcrumbs">
          <span class="bc-item" onclick="navigateToPage('overview')">หน้าหลัก</span>
          <span>/</span>
          <span class="bc-item" id="bcChapter">ภาพรวม</span>
          <span>/</span>
          <span class="bc-current" id="bcPage">ยินดีต้อนรับ</span>
        </nav>
      </div>

      <div class="nav-right">
        <span class="course-progress-badge" id="progressBadge">กำลังศึกษา: ภาพรวมรายวิชา</span>
        <a href="https://github.com/Tsanaphy2023/modernphysics" target="_blank" class="btn-icon" title="GitHub Repository">🐙</a>
        <button class="btn-icon" onclick="openTocModal()" title="สารบัญบทเรียน">📋</button>
        <button class="btn-icon" onclick="toggleTheme()" title="เปลี่ยนธีม">🌓</button>
      </div>
    </header>

    <!-- SUBTOPIC TABS BAR (Active chapter's 5 subtopic pills) -->
    <nav class="subtopic-tabs-bar" id="subtopicTabsBar" style="display:none;">
      <!-- Injected dynamically via JS when switching chapters -->
    </nav>

    <!-- DEDICATED SUBTOPIC PAGES (Only 1 shown at a time) -->
    <section class="content-stage">
      {overview_page_html}
      {all_rendered_pages_html}
    </section>
  </main>
</div>

<!-- TABLE OF CONTENTS MODAL -->
<div class="modal-backdrop" id="tocModal" onclick="if(event.target===this) closeTocModal()">
  <div class="modal-content">
    <div class="modal-header">
      <h2 style="font-size: 1.25rem; color: var(--primary-cyan);">📋 สารบัญรายวิชาฟิสิกส์ยุคใหม่ (40 หัวข้อย่อย)</h2>
      <button class="btn-icon" onclick="closeTocModal()">✕</button>
    </div>
    <div class="modal-body">
      {toc_full_modal_html}
    </div>
  </div>
</div>

<!-- JAVASCRIPT APP CONTROLLER & SIMULATORS -->
<script>
// Data structure for router
const COURSE_DATA = {json.dumps(CHAPTERS_DATA, ensure_ascii=False)};
let currentPageId = "overview";
let completedPages = JSON.parse(localStorage.getItem("rbru_completed_pages") || "[]");

// Router & Page Navigation
function navigateToPage(pageId) {{
  const targetPage = document.getElementById("page-" + pageId);
  if (!targetPage) return;

  // Hide all pages
  document.querySelectorAll(".subtopic-page").forEach(p => p.style.display = "none");
  
  // Show target page
  targetPage.style.display = "block";
  window.scrollTo({{ top: 0, behavior: "smooth" }});
  currentPageId = pageId;
  window.location.hash = "p" + pageId.replace(".", "_");

  const tabsBar = document.getElementById("subtopicTabsBar");

  if (pageId === "overview") {{
    document.getElementById("bcChapter").textContent = "ภาพรวม";
    document.getElementById("bcPage").textContent = "ยินดีต้อนรับ";
    document.title = "ภาพรวมรายวิชา | RBRU MOOC ฟิสิกส์ยุคใหม่ (4012920)";
    tabsBar.style.display = "none";
    document.querySelectorAll(".sidebar-subitem").forEach(item => item.classList.remove("active"));
    document.getElementById("progressBadge").textContent = "ภาพรวมรายวิชา (40 หัวข้อย่อย)";
    return;
  }}

  tabsBar.style.display = "flex";

  // Find chapter and page meta
  let chObj = null;
  let pageObj = null;
  for (const ch of COURSE_DATA) {{
    const p = ch.pages.find(item => item.id === pageId);
    if (p) {{ chObj = ch; pageObj = p; break; }}
  }}

  // Update Breadcrumbs
  if (chObj && pageObj) {{
    document.getElementById("bcChapter").textContent = `บทที่ ${{chObj.id}}`;
    document.getElementById("bcPage").textContent = pageObj.title;
    document.title = `${{pageObj.title}} | RBRU MOOC ฟิสิกส์ยุคใหม่`;
  }}

  // Update Sidebar Active state & Accordion
  document.querySelectorAll(".sidebar-subitem").forEach(item => item.classList.remove("active"));
  const navItem = document.getElementById("nav-" + pageId);
  if (navItem) {{
    navItem.classList.add("active");
    const parentGroup = navItem.closest(".sidebar-chapter-group");
    if (parentGroup) parentGroup.classList.add("open");
  }}

  // Render Subtopic Tabs for active chapter
  renderSubtopicTabs(chObj, pageId);

  // Update Progress Badge
  updateProgressBadge();

  // Trigger Simulator redraw on page activation
  setTimeout(() => {{
    const sliders = targetPage.querySelectorAll("input[type='range'], select");
    sliders.forEach(s => s.dispatchEvent(new Event('input')));
    sliders.forEach(s => s.dispatchEvent(new Event('change')));
  }}, 60);

  // Typeset MathJax
  if (window.MathJax && MathJax.typesetPromise) {{
    MathJax.typesetPromise();
  }}

  // Close sidebar on mobile
  if (900 >= window.innerWidth) {{
    document.getElementById("appSidebar").classList.remove("open");
  }}
}}

function renderSubtopicTabs(chObj, activePageId) {{
  const tabsBar = document.getElementById("subtopicTabsBar");
  if (!chObj || !tabsBar) return;

  tabsBar.innerHTML = chObj.pages.map(p => `
    <button class="tab-pill ${{p.id === activePageId ? 'active' : ''}}" onclick="navigateToPage('${{p.id}}')">
      <span>${{p.id}}</span>
      <span>${{p.title.replace(p.id + ' ', '')}}</span>
    </button>
  `).join("");
}}

function toggleChapterAccordion(chId) {{
  const group = document.getElementById("ch-group-" + chId);
  if (group) group.classList.toggle("open");
}}

function toggleSidebar() {{
  document.getElementById("appSidebar").classList.toggle("open");
}}

function openTocModal() {{
  document.getElementById("tocModal").classList.add("open");
}}

function closeTocModal() {{
  document.getElementById("tocModal").classList.remove("open");
}}

function toggleTheme() {{
  const html = document.documentElement;
  const current = html.getAttribute("data-theme");
  const next = current === "light" ? "dark" : "light";
  html.setAttribute("data-theme", next);
  localStorage.setItem("rbru_theme", next);
}}

function updateProgressBadge() {{
  let total = 0;
  COURSE_DATA.forEach(c => total += c.pages.length);
  let currentNum = 1;
  let count = 0;
  for (const c of COURSE_DATA) {{
    for (const p of c.pages) {{
      count++;
      if (p.id === currentPageId) currentNum = count;
    }}
  }}
  document.getElementById("progressBadge").textContent = `หน้า ${{currentNum}} / ${{total}} (${{Math.round((currentNum/total)*100)}}%)`;
}}

// Quiz Checker
function checkQuiz(pageId, selectedIdx, correctIdx) {{
  const card = document.getElementById("quiz-" + pageId);
  const feedback = document.getElementById("feedback-" + pageId);
  if (!card || !feedback) return;

  const buttons = card.querySelectorAll(".quiz-opt");
  buttons.forEach((btn, idx) => {{
    btn.disabled = true;
    if (idx === correctIdx) btn.classList.add("correct");
    else if (idx === selectedIdx) btn.classList.add("wrong");
  }});

  // Find explanation
  let expl = "";
  for (const c of COURSE_DATA) {{
    const p = c.pages.find(item => item.id === pageId);
    if (p) {{ expl = p.quiz.explanation; break; }}
  }}

  feedback.style.display = "block";
  if (selectedIdx === correctIdx) {{
    feedback.style.background = "rgba(16, 185, 129, 0.15)";
    feedback.style.border = "1px solid #10b981";
    feedback.style.color = "#34d399";
    feedback.innerHTML = `<b>🎉 ถูกต้องยอดเยี่ยม!</b><br>${{expl}}`;
    
    // Mark completed
    if (!completedPages.includes(pageId)) {{
      completedPages.push(pageId);
      localStorage.setItem("rbru_completed_pages", JSON.stringify(completedPages));
      const navItem = document.getElementById("nav-" + pageId);
      if (navItem) navItem.classList.add("completed");
    }}
  }} else {{
    feedback.style.background = "rgba(244, 63, 94, 0.15)";
    feedback.style.border = "1px solid #f43f5e";
    feedback.style.color = "#fb7185";
    feedback.innerHTML = `<b>❌ ยังไม่ถูกต้อง</b><br>${{expl}}`;
  }}
}}

// Search Filter
document.getElementById("quickSearchInput")?.addEventListener("input", function(e) {{
  const q = e.target.value.toLowerCase().trim();
  document.querySelectorAll(".sidebar-subitem").forEach(item => {{
    const text = item.textContent.toLowerCase();
    if (!q || text.includes(q)) {{
      item.style.display = "flex";
    }} else {{
      item.style.display = "none";
    }}
  }});
}});

// Keyboard Navigation (Left = Prev, Right = Next)
window.addEventListener("keydown", (e) => {{
  if (e.target.tagName === "INPUT" || e.target.tagName === "TEXTAREA") return;
  const currPageEl = document.getElementById("page-" + currentPageId);
  if (!currPageEl) return;

  if (e.key === "ArrowRight") {{
    const nextBtn = currPageEl.querySelector(".next-btn");
    if (nextBtn) nextBtn.click();
  }} else if (e.key === "ArrowLeft") {{
    const prevBtn = currPageEl.querySelector(".prev-btn");
    if (prevBtn) prevBtn.click();
  }}
}});

// -------------------------------------------------------------
// WORKED EXAMPLE TOGGLE SOLUTION & SIMULATOR REDRAW ENGINE
// -------------------------------------------------------------
function toggleSolution(pageId) {{
  const sol = document.getElementById("sol-content-" + pageId);
  const btn = document.getElementById("btn-sol-" + pageId);
  const txt = document.getElementById("btn-text-" + pageId);
  const ico = document.getElementById("btn-icon-" + pageId);
  if (!sol) return;
  if (sol.style.display === "none" || sol.style.display === "") {{
    sol.style.display = "block";
    if (txt) txt.textContent = "ซ่อนเฉลยและวิธีทำ";
    if (ico) ico.textContent = "🙈";
    if (btn) btn.style.background = "#475569";
    if (window.MathJax && window.MathJax.typesetPromise) {{
      window.MathJax.typesetPromise([sol]);
    }}
  }} else {{
    sol.style.display = "none";
    if (txt) txt.textContent = "คลิกเพื่อดูเฉลยและวิธีทำละเอียด";
    if (ico) ico.textContent = "👁️";
    if (btn) btn.style.background = "linear-gradient(135deg, #0284c7, #0369a1)";
  }}
}}

// Initialize on load
window.addEventListener("DOMContentLoaded", () => {{
  // Apply saved theme
  const savedTheme = localStorage.getItem("rbru_theme") || "dark";
  document.documentElement.setAttribute("data-theme", savedTheme);

  // Restore completed checkmarks in sidebar
  completedPages.forEach(pId => {{
    const navItem = document.getElementById("nav-" + pId);
    if (navItem) navItem.classList.add("completed");
  }});

  // Check URL Hash for direct page navigation
  let initPage = "overview";
  if (window.location.hash) {{
    const hash = window.location.hash.replace("#p", "").replace("_", ".");
    if (document.getElementById("page-" + hash)) {{
      initPage = hash;
    }}
  }}
  navigateToPage(initPage);
}});
</script>

</body>
</html>"""

master_html_path = os.path.join(BASE_DIR, "RBRU_MOOC_Modern_Physics_Interactive.html")
with open(master_html_path, "w", encoding="utf-8") as f:
    f.write(MASTER_HTML)

# Also copy to root index.html for direct GitHub Pages deployment
root_index_path = os.path.join(ROOT_DIR, "index.html")
shutil.copyfile(master_html_path, root_index_path)

print(f"Master Interactive HTML generated at {master_html_path}")
print(f"Copied to root index.html at {root_index_path}")


# -------------------------------------------------------------
# 5. GENERATE MOOC COURSE STRUCTURE DOCUMENTATION
# -------------------------------------------------------------
doc_lines = [
    "# 🎓 แผนผังโครงสร้างรายวิชาและหัวข้อย่อยแบบแยกเพจ (RBRU MOOC Course ID 262)",
    "",
    "**รายวิชา:** ฟิสิกส์ยุคใหม่ (Modern Physics - 4012920)",
    "**อาจารย์ผู้รับผิดชอบ:** ผู้ช่วยศาสตราจารย์ ดร.ชีวะ ทัศนา",
    "**ระบบ E-Learning:** [elearning.rbru.ac.th/course/view.php?id=262](https://elearning.rbru.ac.th/course/view.php?id=262)",
    "**GitHub Repository:** [https://github.com/Tsanaphy2023/modernphysics](https://github.com/Tsanaphy2023/modernphysics)",
    "**GitHub Pages Portal:** [https://tsanaphy2023.github.io/modernphysics/](https://tsanaphy2023.github.io/modernphysics/)",
    "",
    "---",
    "",
    "## 🖼️ แบนเนอร์รายวิชา (Section 0 Banner Overview)",
    "",
    "![Modern Physics Banner](https://raw.githubusercontent.com/Tsanaphy2023/modernphysics/main/assets/images/modern_physics_banner.jpg)",
    "",
    "ไฟล์ HTML สำหรับใส่ใน **ส่วนหัวของรายวิชา (Section 0 / General):**",
    "`moodle_pages/section_0_banner_overview.html`",
    "",
    "---",
    "",
    "## 🏛️ สรุปภาพรวมโครงสร้างการแยกเพจ (Separated Pages Standard)",
    "",
    "ตามเกณฑ์และระเบียบการจัดทำรายวิชา MOOC ระดับมืออาชีพ หัวข้อย่อยของทุกบทเรียนได้รับการแยกออกเป็น **เพจอิสระ (Moodle Page: `mod_page`)** จำนวนรวมทั้งสิ้น **40 เพจย่อย** (8 บท × 5 เพจย่อย) เพื่อให้ผู้เรียนสามารถโฟกัสเนื้อหาทีละประเด็น ไม่เกิด Cognitive Overload พร้อมระบบแบบฝึกหัดและการเชื่อมต่อไปยังห้องปฏิบัติการ 3D / AR",
    "",
    "### 📁 รายการไฟล์ HTML สำหรับนำเข้า Moodle (Directory: `moodle_pages/`)",
    ""
]

for ch in CHAPTERS_DATA:
    doc_lines.append(f"### 📘 {ch['title']}")
    doc_lines.append(f"*{ch['description']}*\n")
    for page in ch["pages"]:
        doc_lines.append(f"- **เพจ `{page['id']}`:** `{page['title']}`")
        doc_lines.append(f"  - 🏷️ **หมวดหมู่:** {page['tag']} | ⏱️ **เวลาศึกษา:** {page['read_time']}")
        doc_lines.append(f"  - 📄 **ไฟล์ HTML พร้อมใช้:** `moodle_pages/chapter_{ch['id']}/page_{page['id'].replace('.', '_')}.html`")
        doc_lines.append(f"  - 🎯 **สาระสำคัญ:** {page['summary']}")
    doc_lines.append("")

doc_lines.extend([
    "---",
    "",
    "## 🚀 วิธีการนำไฟล์เข้าสู่ระบบ RBRU LMS (Moodle)",
    "",
    "### ตอนที่ 1: ติดตั้งแบนเนอร์และภาพรวมรายวิชา (Section 0)",
    "1. เข้าสู่ระบบ Moodle ที่ [elearning.rbru.ac.th/course/view.php?id=262](https://elearning.rbru.ac.th/course/view.php?id=262)",
    "2. คลิก **เปิดการแก้ไข (Turn editing on)** ที่มุมขวาบนของหน้าวิชา",
    "3. ใน **Section 0 (General / ข้อมูลทั่วไปของรายวิชา)** กดแก้ไข (Edit section summary) หรือเพิ่มแหล่งข้อมูลเป็น **Label / Text and media area**",
    "4. กดปุ่ม `HTML / Source Code` (`<>`)",
    "5. คัดลอกโค้ดจาก `moodle_pages/section_0_banner_overview.html` ไปวาง แล้วกดบันทึก",
    "",
    "### ตอนที่ 2: ติดตั้งหัวข้อย่อยแบบแยกเพจ (Section 1 ถึง 8)",
    "1. ในแต่ละบท (Section 1 ถึง 8) คลิก **+ เพิ่มกิจกรรมหรือแหล่งข้อมูล (+ Add an activity or resource)**",
    "2. เลือกชนิดแหล่งข้อมูลเป็น **หน้าเว็บ (Page)**",
    "3. ตั้งชื่อหน้าเว็บตามมาตรฐาน Clean Thai Naming (เช่น `1.1 ข้อจำกัดของฟิสิกส์ดั้งเดิม`)",
    "4. ในช่อง **เนื้อหาหน้าเว็บ (Page content)** กดปุ่ม `HTML / Source Code` (`<>`)",
    "5. คัดลอกโค้ดจากไฟล์ `moodle_pages/chapter_X/page_X_Y.html` ไปวาง แล้วกดบันทึก",
    "",
    "---",
    "จัดทำโดย: ระบบออกแบบรายวิชาอัตโนมัติ RBRU MOOC Course Builder (2026)"
])

doc_full_text = "\n".join(doc_lines)
with open(os.path.join(BASE_DIR, "MOOC_Course_Structure_Separated_Pages.md"), "w", encoding="utf-8") as f:
    f.write(doc_full_text)

print("Documentation MOOC_Course_Structure_Separated_Pages.md generated successfully.")
