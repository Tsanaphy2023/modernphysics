#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Flawless Moodle Course Restructurer & Deployer (RBRU Course ID 262)
Ensures:
- Section 0: Banner Overview (Version 3 Exact Portrait)
- Section 1: บทที่ 1 จุดกำเนิดของทฤษฎีควอนตัม (1.1 - 1.5)
- Section 2: บทที่ 2 ทฤษฎีสัมพัทธภาพพิเศษ (2.1 - 2.5)
- Section 3: บทที่ 3 ทวิภาวะของคลื่นและอนุภาค (3.1 - 3.5)
- Section 4: บทที่ 4 กลศาสตร์ควอนตัม (4.1 - 4.5)
- Section 5: บทที่ 5 ทฤษฎีอะตอมและสเปกตรัม (5.1 - 5.5)
- Section 6: บทที่ 6 ฟิสิกส์นิวเคลียร์ (6.1 - 6.5)
- Section 7: บทที่ 7 ฟิสิกส์อนุภาคมูลฐาน (7.1 - 7.5)
- Section 8: บทที่ 8 ความรู้เบื้องต้นเกี่ยวกับเอกภพวิทยา (8.1 - 8.5)
"""

import os
import json
import time
import requests
import re

BASE_DIR = "/Users/chewathassana/Downloads/manus_backup2026/ModernPhysics"
BOOK_DIR = os.path.join(BASE_DIR, "หนังสือ-เล่ม1-ฟิสิกส์ยุคใหม่")
MOODLE_PAGES_DIR = os.path.join(BOOK_DIR, "moodle_pages")

COURSE_ID = "262"
BASE_URL = "https://elearning.rbru.ac.th"

session = requests.Session()
session.cookies.set("MoodleSessionrbrulms", "lsd8fv1nrb9spqgtchgv9a1co1", domain="elearning.rbru.ac.th")
session.headers.update({
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Origin": BASE_URL,
    "Referer": f"{BASE_URL}/course/view.php?id={COURSE_ID}"
})

with open(os.path.join(BOOK_DIR, "course_data.json"), "r", encoding="utf-8") as f:
    CHAPTERS_DATA = json.load(f)


def get_sesskey():
    r = session.get(f"{BASE_URL}/course/view.php?id={COURSE_ID}")
    m = re.search(r'name=\"sesskey\"\s+value=\"([^\"]+)\"', r.text)
    if not m:
        m = re.search(r'\"sesskey\":\"([^\"]+)\"', r.text)
    return m.group(1) if m else None


# -------------------------------------------------------------
# 1. CLEAN UP MISPLACED MODULES IN SECTIONS 4 TO 8
# -------------------------------------------------------------
def cleanup_misplaced_modules():
    print("\n--- 1. Cleaning up misplaced modules in Sections 4 to 8 ---")
    r = session.get(f"{BASE_URL}/course/view.php?id={COURSE_ID}")
    sesskey = get_sesskey()

    sections = re.findall(r'<li[^>]*id=\"section-(\d+)\"[^>]*>(.*?)</li>\s*(?=<li[^>]*id=\"section-|\Z)', r.text, re.DOTALL)
    
    for s_num_str, s_html in sections:
        s_num = int(s_num_str)
        if s_num < 4:
            continue  # Keep Section 0, 1, 2, 3 safe

        # Find all activities in this section
        acts = re.findall(r'<li[^>]*class=\"activity\s+([^\"\s]+)[^>]*id=\"module-(\d+)\"[^>]*>(.*?)</li>', s_html, re.DOTALL)
        for m_type, m_id, m_html in acts:
            inst = re.search(r'<span class=\"instancename\"[^>]*>(.*?)</span>', m_html, re.DOTALL)
            name = re.sub(r'<[^>]+>', '', inst.group(1)).strip() if inst else "Unknown"
            
            print(f"  🗑️ Deleting from Section {s_num}: [mod={m_id}] {name}")
            del_payload = {
                "confirm": "1",
                "delete": m_id,
                "sesskey": sesskey,
                "sr": "0"
            }
            r_del = session.post(f"{BASE_URL}/course/mod.php", data=del_payload)
            time.sleep(0.3)


# -------------------------------------------------------------
# 2. UPDATE SECTION HEADERS & NAMES FOR ALL 8 SECTIONS
# -------------------------------------------------------------
def update_section_headers():
    print("\n--- 2. Updating Section Headers (Clean Titles) ---")
    r_course = session.get(f"{BASE_URL}/course/view.php?id={COURSE_ID}")
    sesskey = get_sesskey()

    for ch in CHAPTERS_DATA:
        s_num = ch["id"]
        s_title = ch["title"]
        
        sec_block = re.search(rf'<li[^>]*id=\"section-{s_num}\"[^>]*>(.*?)</li>\s*(?=<li[^>]*id=\"section-|\Z)', r_course.text, re.DOTALL)
        if not sec_block:
            print(f"  ❌ Section-{s_num} not found on page")
            continue

        edit_id_m = re.search(r'editsection\.php\?id=(\d+)', sec_block.group(1))
        if not edit_id_m:
            print(f"  ❌ editsection ID for Section {s_num} not found")
            continue

        sec_edit_id = edit_id_m.group(1)
        get_url = f"{BASE_URL}/course/editsection.php?id={sec_edit_id}"
        r_get = session.get(get_url)
        
        itemid_m = re.search(r'name=\"summary_editor\[itemid\]\"\s+value=\"([^\"]+)\"', r_get.text)
        itemid = itemid_m.group(1) if itemid_m else "0"

        payload = {
            "id": sec_edit_id,
            "course": COURSE_ID,
            "sesskey": sesskey,
            "_qf__editsection_form": "1",
            "mform_isexpanded_id_generalhdr": "1",
            "name": s_title,
            "summary_editor[text]": f"<p><b>{s_title}</b> — 5 หัวข้อย่อยแยกเพจ พร้อมแบบจำลองและแบบฝึกหัด</p>",
            "summary_editor[format]": "1",
            "summary_editor[itemid]": itemid,
            "availabilityconditionsjson": '{"op":"&","c":[],"showc":[]}',
            "submitbutton": "บันทึกการเปลี่ยนแปลง"
        }
        r_post = session.post(f"{BASE_URL}/course/editsection.php", data=payload, headers={"Referer": get_url})
        print(f"  📘 Section {s_num} Title Set to: {s_title} (Status: {r_post.status_code})")
        time.sleep(0.3)


# -------------------------------------------------------------
# 3. DEPLOY MISSING SUBTOPIC PAGES (CHAPTERS 4 TO 8)
# -------------------------------------------------------------
def deploy_chapters_4_to_8():
    print("\n--- 3. Deploying Subtopic Pages for Chapters 4 to 8 ---")
    sesskey = get_sesskey()

    for ch in CHAPTERS_DATA:
        ch_id = ch["id"]
        if ch_id < 4:
            continue  # Chapters 1, 2, 3 are already perfectly created

        print(f"\n=======================================================")
        print(f"📘 Creating Pages for Chapter {ch_id}: {ch['title']}")
        print(f"=======================================================")

        for page in ch["pages"]:
            page_id = page["id"]
            page_title = page["title"]

            html_filename = f"page_{page_id.replace('.', '_')}.html"
            html_filepath = os.path.join(MOODLE_PAGES_DIR, f"chapter_{ch_id}", html_filename)
            if not os.path.exists(html_filepath):
                print(f"  ❌ File not found: {html_filepath}")
                continue

            with open(html_filepath, "r", encoding="utf-8") as f:
                page_content = f.read()

            add_url = f"{BASE_URL}/course/modedit.php?add=page&type=&course={COURSE_ID}&section={ch_id}&return=0&sr=0"
            r_get = session.get(add_url)
            if r_get.status_code != 200:
                print(f"  ❌ Error loading add form for {page_id}: {r_get.status_code}")
                continue

            page_itemid_m = re.search(r'name=\"page\[itemid\]\"\s+value=\"([^\"]+)\"', r_get.text)
            intro_itemid_m = re.search(r'name=\"introeditor\[itemid\]\"\s+value=\"([^\"]+)\"', r_get.text)

            page_itemid = page_itemid_m.group(1) if page_itemid_m else "0"
            intro_itemid = intro_itemid_m.group(1) if intro_itemid_m else "0"

            payload = {
                "course": COURSE_ID,
                "coursemodule": "",
                "section": str(ch_id),
                "module": "15",
                "modulename": "page",
                "instance": "",
                "add": "page",
                "update": "0",
                "return": "0",
                "sr": "0",
                "beforemod": "0",
                "revision": "1",
                "sesskey": sesskey,
                "_qf__mod_page_mod_form": "1",
                "mform_isexpanded_id_general": "1",
                "mform_isexpanded_id_contentsection": "1",
                "name": page_title,
                "introeditor[text]": f"<p>{page['summary']}</p>",
                "introeditor[format]": "1",
                "introeditor[itemid]": intro_itemid,
                "page[text]": page_content,
                "page[format]": "1",
                "page[itemid]": page_itemid,
                "printintro": "0",
                "printlastmodified": "1",
                "display": "5",
                "availabilityconditionsjson": '{"op":"&","c":[],"showc":[]}',
                "submitbutton2": "บันทึกและกลับไปยังรายวิชา"
            }

            post_headers = {
                "Referer": add_url,
                "Content-Type": "application/x-www-form-urlencoded"
            }

            r_post = session.post(f"{BASE_URL}/course/modedit.php", data=payload, headers=post_headers)
            if r_post.status_code == 200:
                print(f"  ✅ Created Page: {page_title}")
            else:
                print(f"  ❌ Failed to create {page_title}: Status {r_post.status_code}")

            time.sleep(0.4)


# -------------------------------------------------------------
# 4. FINAL AUDIT & VERIFICATION
# -------------------------------------------------------------
def audit_course():
    print("\n=======================================================")
    print("📊 FINAL COURSE AUDIT & VERIFICATION")
    print("=======================================================")
    r = session.get(f"{BASE_URL}/course/view.php?id={COURSE_ID}")
    sections = re.findall(r'<li[^>]*id=\"section-(\d+)\"[^>]*>(.*?)</li>\s*(?=<li[^>]*id=\"section-|\Z)', r.text, re.DOTALL)
    
    total_pages = 0
    for s_num_str, s_html in sections:
        s_num = int(s_num_str)
        s_name = re.search(r'<h3[^>]*class=\"sectionname\"[^>]*>(.*?)</h3>', s_html, re.DOTALL)
        title = re.sub(r'<[^>]+>', '', s_name.group(1)).strip() if s_name else f"Section {s_num}"
        acts = re.findall(r'<span class=\"instancename\"[^>]*>(.*?)</span>', s_html, re.DOTALL)
        pages = [re.sub(r'<[^>]+>', '', a).strip() for a in acts if 'หน้าเว็บ' in a or re.match(r'^\d+\.\d+', a.strip())]
        total_pages += len(pages)
        print(f"\n📂 Section {s_num}: {title} ({len(pages)} pages)")
        for p in pages:
            print(f"   ✓ {p}")

    print(f"\n🎉 Total Subtopic Pages verified on Moodle: {total_pages} / 40")


if __name__ == "__main__":
    cleanup_misplaced_modules()
    update_section_headers()
    deploy_chapters_4_to_8()
    audit_course()
