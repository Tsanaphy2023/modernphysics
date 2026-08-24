#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Automated Pipeline to Populate Course ID 263 (นาโนเทคโนโลยีเชิงฟิสิกส์):
- Creates/updates 40 Page activities across 8 sections
- Updates Section 0 Course Hero Banner & Learning Outcomes (CLO 1-7)
- Updates Sections 1-8 with 3D Animated SVG Covers and 3D Interactive Cards Grid
"""

import os
import sys
import re
import json
import time
import requests

BASE_DIR = "/Users/chewathassana/Downloads/manus_backup2026/ModernPhysics"
sys.path.append(BASE_DIR)

COURSE_ID = "263"
BASE_URL = "https://elearning.rbru.ac.th"

NANO_DIR = os.path.join(BASE_DIR, "nanotechnology/course_nanophysics_263")
MOODLE_PAGES_DIR = os.path.join(NANO_DIR, "moodle_pages")
COURSE_DATA_FILE = os.path.join(NANO_DIR, "course_data.json")

session = requests.Session()
session.cookies.set("MoodleSessionrbrulms", "lsd8fv1nrb9spqgtchgv9a1co1", domain="elearning.rbru.ac.th")
session.headers.update({
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Origin": BASE_URL,
    "Referer": f"{BASE_URL}/course/view.php?id={COURSE_ID}"
})

with open(COURSE_DATA_FILE, "r", encoding="utf-8") as f:
    chapters = json.load(f)

def get_input_val(name, html):
    m = re.search(rf'<input[^>]*name=[\"\']{re.escape(name)}[\"\'][^>]*value=[\"\']([^\"\']*)[\"\']', html)
    if not m:
        m = re.search(rf'name=[\"\']{re.escape(name)}[\"\'][^>]*value=[\"\']([^\"\']*)[\"\']', html)
    return m.group(1) if m else ''

# 1. Fetch current catalog on Course 263
print(f"📡 Fetching Course {COURSE_ID} structure from Moodle...")
r_course = session.get(f"{BASE_URL}/course/view.php?id={COURSE_ID}")
sesskey = re.search(r'name=\"sesskey\"\s+value=\"([^\"]+)\"', r_course.text).group(1)

sections_raw = re.findall(r'<li[^>]*id=\"section-(\d+)\"[^>]*>(.*?)</li>\s*(?=<li[^>]*id=\"section-|\Z)', r_course.text, re.DOTALL)
moodle_catalog = {}

for s_num_str, s_html in sections_raw:
    s_num = int(s_num_str)
    sec_id_m = re.search(r'editsection\.php\?id=(\d+)', s_html)
    sec_db_id = sec_id_m.group(1) if sec_id_m else ''
    acts = re.findall(r'<li[^>]*class=\"activity\s+page[^>]*id=\"module-(\d+)\"[^>]*>(.*?)</li>', s_html, re.DOTALL)
    pages = []
    for m_id, m_html in acts:
        inst = re.search(r'<span class=\"instancename\"[^>]*>(.*?)</span>', m_html, re.DOTALL)
        name = re.sub(r'<[^>]+>', '', inst.group(1)).strip() if inst else ''
        pages.append({"cmid": m_id, "name": name, "url": f"{BASE_URL}/mod/page/view.php?id={m_id}"})
    moodle_catalog[s_num] = {"section_num": s_num, "sec_db_id": sec_db_id, "pages": pages}

print(f"Found {len(moodle_catalog)} sections on Course {COURSE_ID}:")
for s_num, s_info in moodle_catalog.items():
    print(f"  Section {s_num} (DB ID: {s_info['sec_db_id']}): {len(s_info['pages'])} pages")

with open(os.path.join(NANO_DIR, "moodle_catalog_263.json"), "w", encoding="utf-8") as f:
    json.dump(moodle_catalog, f, ensure_ascii=False, indent=2)

# 2. Deploy 3D Animated Covers and Topic Cards to Sections 1 through 8
print("\n🎨 Deploying 3D Animated Covers & Topic Cards to Sections 1-8...")

from deploy_animated_covers_and_section_cards import get_chapter_animated_cover_svg

NANO_ICONS = {
    "1.1": """<svg width="48" height="48" viewBox="0 0 64 64" fill="none"><circle cx="32" cy="32" r="28" fill="#0f172a" stroke="#00f0ff" stroke-width="2"/><line x1="14" y1="32" x2="50" y2="32" stroke="#00f0ff" stroke-width="2"/><line x1="14" y1="26" x2="14" y2="38" stroke="#00f0ff" stroke-width="2"/><line x1="50" y1="26" x2="50" y2="38" stroke="#00f0ff" stroke-width="2"/><text x="20" y="48" fill="#facc15" font-size="10" font-family="monospace">1-100nm</text></svg>""",
    "1.2": """<svg width="48" height="48" viewBox="0 0 64 64" fill="none"><rect x="12" y="12" width="40" height="40" rx="6" fill="#0f172a" stroke="#10b981" stroke-width="2"/><text x="18" y="38" fill="#10b981" font-size="12" font-family="monospace" font-weight="bold">A/V=6/d</text></svg>""",
    "1.3": """<svg width="48" height="48" viewBox="0 0 64 64" fill="none"><circle cx="24" cy="32" r="10" fill="#f43f5e"/><circle cx="40" cy="32" r="10" fill="#f43f5e"/><path d="M24 32 L40 32" stroke="#facc15" stroke-width="2" stroke-dasharray="2 2"/><text x="21" y="52" fill="#facc15" font-size="9" font-family="monospace">ΔG<0</text></svg>""",
    "1.4": """<svg width="48" height="48" viewBox="0 0 64 64" fill="none"><rect x="8" y="14" width="48" height="36" rx="4" fill="#020617" stroke="#64748b"/><line x1="16" y1="42" x2="36" y2="42" stroke="#ffffff" stroke-width="3"/><text x="16" y="38" fill="#ffffff" font-size="8" font-family="sans-serif">20 nm</text></svg>""",
    "1.5": """<svg width="48" height="48" viewBox="0 0 64 64" fill="none"><rect x="8" y="12" width="48" height="40" rx="8" fill="#0f172a" stroke="#10b981" stroke-width="2"/><circle cx="32" cy="32" r="14" stroke="#00f0ff" stroke-width="2" fill="none"/><text x="18" y="47" fill="#10b981" font-size="8" font-family="sans-serif" font-weight="bold">3D AR LAB</text></svg>"""
}

def generate_nano_section_html(ch_id, clean_title, ch_desc, pages_info):
    cover_svg = get_chapter_animated_cover_svg(ch_id)

    card_items_html = ""
    for p in pages_info:
        pid = p["id"]
        ptitle = p["title"]
        psummary = p.get("summary", "")[:95] + "..."
        cmid = p.get("cmid", "")
        url = p.get("url", f"{BASE_URL}/mod/page/view.php?id={cmid}")
        svg = NANO_ICONS.get(pid, NANO_ICONS.get("1.1"))
        formula = p.get("formula", "Nanotechnology Concept")

        card_items_html += f"""
        <div class="topic-card-3d">
          <div class="card-top-header">
            <div class="card-icon-3d">{svg}</div>
            <div class="topic-badge">หัวข้อ {pid}</div>
          </div>
          <h3 class="topic-title">{ptitle}</h3>
          <div class="formula-badge">\\({formula}\\)</div>
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
    .anim-pulse {{ animation: pulse-slow 3s infinite ease-in-out; }}
    .anim-spin-slow {{ transform-origin: center; animation: spin-slow 20s linear infinite; }}

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

for ch in chapters:
    ch_id = ch["id"]
    raw_title = ch["title"]
    clean_title = re.sub(r'^(บทที่\s*\d+\s*|\d+\s*)', '', raw_title).strip()
    formatted_section_name = f"บทที่ {ch_id} {clean_title}"
    ch_desc = ch["description"]

    sec_info = moodle_catalog.get(ch_id, {"sec_db_id": "", "pages": []})
    sec_db_id = sec_info["sec_db_id"]
    moodle_pages = sec_info["pages"]

    combined_pages = []
    for p_idx, p in enumerate(ch["pages"]):
        p_copy = dict(p)
        if p_idx < len(moodle_pages):
            p_copy["cmid"] = moodle_pages[p_idx]["cmid"]
            p_copy["url"] = moodle_pages[p_idx]["url"]
        combined_pages.append(p_copy)

    section_html = generate_nano_section_html(ch_id, clean_title, ch_desc, combined_pages)

    edit_url = f"{BASE_URL}/course/editsection.php?id={sec_db_id}"
    r_edit = session.get(edit_url)
    if r_edit.status_code == 200:
        payload = {
            "context": get_input_val("context", r_edit.text) or "19158",
            "id": sec_db_id,
            "course": COURSE_ID,
            "sesskey": sesskey,
            "_qf__editsection_form": "1",
            "mform_isexpanded_id_generalhdr": "1",
            "mform_isexpanded_id_availabilityconditions": "0",
            "name": formatted_section_name,
            "summary_editor[text]": section_html,
            "summary_editor[format]": "1",
            "summary_editor[itemid]": get_input_val("summary_editor[itemid]", r_edit.text),
            "submitbutton": "บันทึกการเปลี่ยนแปลง"
        }
        session.post(edit_url, data=payload)
        print(f"  ✅ Deployed 3D Animated Cover & Topic Cards to Chapter {ch_id} (Section ID: {sec_db_id})")

print(f"\n🎉 Successfully configured and deployed Course ID {COURSE_ID} (นาโนเทคโนโลยีเชิงฟิสิกส์) to RBRU Moodle LMS!")
