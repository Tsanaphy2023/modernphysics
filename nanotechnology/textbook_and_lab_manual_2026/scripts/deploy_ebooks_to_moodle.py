#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Syncs Textbook and Lab Manual PDFs & E-Books to GitHub Pages and updates Moodle Course 263 Download Hub.
"""

import os
import shutil
import subprocess
import requests
import re

BASE_DIR = "/Users/chewathassana/Downloads/manus_backup2026/ModernPhysics"
PKG_DIR = os.path.join(BASE_DIR, "nanotechnology/textbook_and_lab_manual_2026")
DIST_DIR = os.path.join(PKG_DIR, "dist")
EBOOKS_ASSETS_DIR = os.path.join(BASE_DIR, "assets/ebooks")
DIAG_ASSETS_DIR = os.path.join(BASE_DIR, "assets/diagrams")

os.makedirs(EBOOKS_ASSETS_DIR, exist_ok=True)
os.makedirs(DIAG_ASSETS_DIR, exist_ok=True)

# Copy PDFs to assets/ebooks
for f in ["Nanotechnological_Physics_Masterclass_Textbook.pdf", "Nanotechnological_Physics_Laboratory_Manual.pdf", "Nanotechnological_Physics_Masterclass_Textbook.html", "Nanotechnological_Physics_Laboratory_Manual.html"]:
    src = os.path.join(DIST_DIR, f)
    if os.path.exists(src):
        shutil.copy(src, os.path.join(EBOOKS_ASSETS_DIR, f))
        print(f"✅ Copied to assets/ebooks: {f}")

# Copy Diagrams to assets/diagrams
diag_src = os.path.join(PKG_DIR, "assets/diagrams")
if os.path.exists(diag_src):
    for f in os.listdir(diag_src):
        if f.endswith(".svg"):
            shutil.copy(os.path.join(diag_src, f), os.path.join(DIAG_ASSETS_DIR, f))
            print(f"✅ Copied diagram: {f}")

# Push to gh-pages branch
TMP_GH = "/tmp/clean_gh_pages"
if os.path.exists(TMP_GH):
    shutil.rmtree(TMP_GH)
os.makedirs(TMP_GH, exist_ok=True)

shutil.copytree(os.path.join(BASE_DIR, "simulators"), os.path.join(TMP_GH, "simulators"))
shutil.copytree(os.path.join(BASE_DIR, "assets"), os.path.join(TMP_GH, "assets"))
with open(os.path.join(TMP_GH, ".nojekyll"), "w") as f:
    f.write("")
if os.path.exists(os.path.join(BASE_DIR, "index.html")):
    shutil.copy(os.path.join(BASE_DIR, "index.html"), os.path.join(TMP_GH, "index.html"))

subprocess.run(["git", "init"], cwd=TMP_GH, check=True)
subprocess.run(["git", "checkout", "-b", "gh-pages"], cwd=TMP_GH, check=True)
subprocess.run(["git", "add", "."], cwd=TMP_GH, check=True)
subprocess.run(["git", "commit", "-m", "feat(ebooks): add masterclass textbook and laboratory manual pdfs and vector diagrams"], cwd=TMP_GH, check=True)

remote_url = f"https://Tsanaphy2023:{os.environ.get('GH_PAT', '')}@github.com/Tsanaphy2023/modernphysics.git" if os.environ.get('GH_PAT') else "origin"
subprocess.run(["git", "push", "--force", remote_url, "gh-pages"], cwd=TMP_GH, check=True)
print("🎉 Force pushed Textbook & Lab Manual PDFs to gh-pages CDN!")

# Update Moodle Course 263 Section 0 with Luxury Download Cards
session = requests.Session()
session.cookies.set("MoodleSessionrbrulms", "lsd8fv1nrb9spqgtchgv9a1co1", domain="elearning.rbru.ac.th")

course_url = "https://elearning.rbru.ac.th/course/view.php?id=263"
r = session.get(course_url)

# Extract sesskey
sesskey = ""
m = re.search(r'\"sesskey\":\"([^\"]+)\"', r.text)
if m:
    sesskey = m.group(1)
print(f"Moodle Session Key: {sesskey}")

# Get section 0 edit page
edit_sec0_url = f"https://elearning.rbru.ac.th/course/editsection.php?id=2540&sr=0"
r_edit = session.get(edit_sec0_url)

m_sec = re.search(r'name=\"summary_editor\[text\]\"[^>]*>(.*?)</textarea>', r_edit.text, re.DOTALL)
existing_summary = m_sec.group(1) if m_sec else ""

# Build Luxury Download Hub HTML Component
CDN_BASE = "https://tsanaphy2023.github.io/modernphysics"
download_card_html = f"""
<!-- MASTERCLASS E-BOOK & LAB MANUAL DOWNLOAD HUB -->
<div style="margin: 24px 0; background: linear-gradient(135deg, #090e1a 0%, #0f172a 100%); border: 1px solid rgba(0, 240, 255, 0.4); border-left: 6px solid #00f0ff; border-radius: 16px; padding: 24px 28px; box-shadow: 0 10px 30px rgba(0, 0, 0, 0.6); font-family: 'Sarabun', sans-serif;">
  
  <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 10px; margin-bottom: 18px; border-bottom: 1px solid rgba(0, 240, 255, 0.2); padding-bottom: 12px;">
    <div style="display: flex; align-items: center; gap: 10px;">
      <span style="font-size: 1.4rem;">📚</span>
      <span style="font-weight: 800; font-size: 1.15rem; color: #38bdf8; letter-spacing: -0.2px;">คลังตำราเรียนและคู่มือปฏิบัติการฉบับสมบูรณ์ (Official E-Books & Lab Manuals)</span>
    </div>
    <span style="background: rgba(0, 240, 255, 0.15); border: 1px solid #00f0ff; color: #00f0ff; font-size: 0.78rem; font-weight: 700; font-family: 'JetBrains Mono', monospace; padding: 3px 12px; border-radius: 9999px;">
      BESTSELLER MASTERCLASS 2026
    </span>
  </div>

  <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap: 18px;">
    
    <!-- Card 1: Textbook -->
    <div style="background: rgba(2, 6, 23, 0.85); border: 1px solid rgba(56, 189, 248, 0.3); border-radius: 12px; padding: 18px 20px; display: flex; flex-direction: column; justify-content: space-between;">
      <div>
        <div style="font-size: 0.78rem; color: #38bdf8; font-weight: 700; font-family: 'JetBrains Mono', monospace; margin-bottom: 4px;">📖 TEXTBOOK (160+ PAGES)</div>
        <div style="font-size: 1.05rem; font-weight: 700; color: #ffffff; margin-bottom: 8px;">ตำราวิชาการ: นาโนเทคโนโลยีเชิงฟิสิกส์</div>
        <div style="font-size: 0.88rem; color: #cbd5e1; line-height: 1.6; margin-bottom: 14px;">
          เนื้อหาครบถ้วนทั้ง 8 บท 40 หัวข้อ จัดหน้าสไตล์ Springer/MIT Press ขอบใน 1.5 นิ้ว แผนผังเวกเตอร์ SVG คมชัด 100% พร้อมตัวอย่างคำนวณและการพิสูจน์คณิตศาสตร์
        </div>
      </div>
      <div style="display: flex; gap: 10px; flex-wrap: wrap;">
        <a href="{CDN_BASE}/assets/ebooks/Nanotechnological_Physics_Masterclass_Textbook.pdf" target="_blank" style="background: linear-gradient(135deg, #0284c7, #00f0ff); color: #020617; font-weight: 700; font-size: 0.85rem; padding: 8px 16px; border-radius: 8px; text-decoration: none; display: inline-flex; align-items: center; gap: 6px; box-shadow: 0 4px 12px rgba(0, 240, 255, 0.3);">
          <span>📥 ดาวน์โหลดตำรา (PDF)</span>
        </a>
        <a href="{CDN_BASE}/assets/ebooks/Nanotechnological_Physics_Masterclass_Textbook.html" target="_blank" style="background: rgba(15, 23, 42, 0.8); border: 1px solid #38bdf8; color: #38bdf8; font-weight: 600; font-size: 0.85rem; padding: 8px 14px; border-radius: 8px; text-decoration: none;">
          <span>🌐 เปิดอ่านออนไลน์ (E-Book)</span>
        </a>
      </div>
    </div>

    <!-- Card 2: Lab Manual -->
    <div style="background: rgba(2, 6, 23, 0.85); border: 1px solid rgba(16, 185, 129, 0.3); border-radius: 12px; padding: 18px 20px; display: flex; flex-direction: column; justify-content: space-between;">
      <div>
        <div style="font-size: 0.78rem; color: #10b981; font-weight: 700; font-family: 'JetBrains Mono', monospace; margin-bottom: 4px;">🔬 LAB MANUAL (40 VIRTUAL LABS)</div>
        <div style="font-size: 1.05rem; font-weight: 700; color: #ffffff; margin-bottom: 8px;">คู่มือปฏิบัติการจำลองเสมือนจริง 40 ปฏิบัติการ</div>
        <div style="font-size: 0.88rem; color: #cbd5e1; line-height: 1.6; margin-bottom: 14px;">
          คู่มือการทดลองจำลอง 60 FPS HTML5 Canvas ครบทุกบท พร้อมตารางบันทึกผล สมการควบคุม คำถามท้ายการทดลอง และระบบควบคุมไร้สัมผัส AR MediaPipe Hands
        </div>
      </div>
      <div style="display: flex; gap: 10px; flex-wrap: wrap;">
        <a href="{CDN_BASE}/assets/ebooks/Nanotechnological_Physics_Laboratory_Manual.pdf" target="_blank" style="background: linear-gradient(135deg, #059669, #10b981); color: #ffffff; font-weight: 700; font-size: 0.85rem; padding: 8px 16px; border-radius: 8px; text-decoration: none; display: inline-flex; align-items: center; gap: 6px; box-shadow: 0 4px 12px rgba(16, 185, 129, 0.3);">
          <span>📥 ดาวน์โหลดคู่มือแล็บ (PDF)</span>
        </a>
        <a href="{CDN_BASE}/assets/ebooks/Nanotechnological_Physics_Laboratory_Manual.html" target="_blank" style="background: rgba(15, 23, 42, 0.8); border: 1px solid #10b981; color: #10b981; font-weight: 600; font-size: 0.85rem; padding: 8px 14px; border-radius: 8px; text-decoration: none;">
          <span>🌐 เปิดอ่านออนไลน์ (E-Book)</span>
        </a>
      </div>
    </div>

  </div>

</div>
"""

# Append or replace download card in section 0
if "MASTERCLASS E-BOOK & LAB MANUAL DOWNLOAD HUB" in existing_summary:
    updated_sec0 = re.sub(r'<!-- MASTERCLASS E-BOOK & LAB MANUAL DOWNLOAD HUB -->.*?</div>\s*</div>\s*</div>', download_card_html, existing_summary, flags=re.DOTALL)
else:
    updated_sec0 = existing_summary + "\n" + download_card_html

# Post update to Moodle Section 0
post_data = {
    "id": "2540",
    "sr": "0",
    "sesskey": sesskey,
    "_qf__course_editsection_form": "1",
    "name": "",
    "summary_editor[text]": updated_sec0,
    "summary_editor[format]": "1",
    "summary_editor[itemid]": "0",
    "submitbutton": "บันทึกการเปลี่ยนแปลง"
}

r_post = session.post("https://elearning.rbru.ac.th/course/editsection.php", data=post_data)
if r_post.status_code == 200:
    print("🎉 Successfully deployed Download Hub to Moodle Course 263 Section 0!")
else:
    print(f"⚠️ Failed to update Moodle Section 0, status: {r_post.status_code}")
