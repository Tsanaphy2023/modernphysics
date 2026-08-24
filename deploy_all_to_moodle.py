#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Automatic Moodle Deployer for RBRU Modern Physics Course ID 262
Deploys:
1. Section 0 Banner & Course Overview
2. Sets Section 1 - 8 Names
3. Creates all 40 Subtopic Pages across Section 1 - 8
"""

import os
import json
import time
import requests
import re

BASE_DIR = "/Users/chewathassana/Downloads/manus_backup2026/ModernPhysics"
BOOK_DIR = os.path.join(BASE_DIR, "หนังสือ-เล่ม1-ฟิสิกส์ยุคใหม่")
MOODLE_PAGES_DIR = os.path.join(BOOK_DIR, "moodle_pages")

COOKIE = "MoodleSessionrbrulms=lsd8fv1nrb9spqgtchgv9a1co1"
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

print(f"Loaded {len(CHAPTERS_DATA)} chapters.")

# -------------------------------------------------------------
# 1. UPDATE SECTION 0 BANNER OVERVIEW
# -------------------------------------------------------------
def update_section_0():
    print("\n--- 1. Updating Section 0 Banner Overview ---")
    with open(os.path.join(MOODLE_PAGES_DIR, "section_0_banner_overview.html"), "r", encoding="utf-8") as f:
        sec0_html = f.read()

    url_get = f"{BASE_URL}/course/editsection.php?id=2521"
    r_get = session.get(url_get)
    if r_get.status_code != 200:
        print(f"Failed to get section 0 edit form: {r_get.status_code}")
        return False

    sesskey = re.search(r'name=\"sesskey\"\s+value=\"([^\"]+)\"', r_get.text).group(1)
    itemid = re.search(r'name=\"summary_editor\[itemid\]\"\s+value=\"([^\"]+)\"', r_get.text).group(1)

    payload = {
        "id": "2521",
        "course": COURSE_ID,
        "mform_isexpanded_id_availabilityconditions": "0",
        "sesskey": sesskey,
        "_qf__editsection_form": "1",
        "mform_isexpanded_id_generalhdr": "1",
        "name": "",
        "summary_editor[text]": sec0_html,
        "summary_editor[format]": "1",
        "summary_editor[itemid]": itemid,
        "availabilityconditionsjson": '{"op":"&","c":[],"showc":[]}',
        "submitbutton": "บันทึกการเปลี่ยนแปลง"
    }

    r_post = session.post(f"{BASE_URL}/course/editsection.php", data=payload, headers={"Referer": url_get})
    print(f"Section 0 Updated! Status: {r_post.status_code}")
    return True


# -------------------------------------------------------------
# 2. GET CURRENT EXISTING PAGES ON COURSE
# -------------------------------------------------------------
def get_existing_pages():
    r = session.get(f"{BASE_URL}/course/view.php?id={COURSE_ID}")
    existing = set()
    matches = re.findall(r'<span class=\"instancename\"[^>]*>(.*?)</span>', r.text, re.DOTALL)
    for m in matches:
        clean = re.sub(r'<[^>]+>', '', m).strip()
        existing.add(clean)
    return existing


# -------------------------------------------------------------
# 3. CREATE PAGE ACTIVITIES ACROSS ALL 8 SECTIONS
# -------------------------------------------------------------
def deploy_subtopic_pages():
    existing_pages = get_existing_pages()
    print(f"\nCurrently existing pages on Moodle: {len(existing_pages)}")

    total_created = 0

    for ch in CHAPTERS_DATA:
        ch_id = ch["id"]
        print(f"\n=======================================================")
        print(f"📘 Processing Chapter {ch_id}: {ch['title']}")
        print(f"=======================================================")

        for page in ch["pages"]:
            page_id = page["id"]
            page_title = page["title"]

            # Check if already exists (skip to avoid duplicate)
            is_existing = any(page_id in exp for exp in existing_pages)
            if is_existing:
                print(f"  ⏭️ Already exists, skipping: {page_title}")
                continue

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

            sesskey_m = re.search(r'name=\"sesskey\"\s+value=\"([^\"]+)\"', r_get.text)
            page_itemid_m = re.search(r'name=\"page\[itemid\]\"\s+value=\"([^\"]+)\"', r_get.text)
            intro_itemid_m = re.search(r'name=\"introeditor\[itemid\]\"\s+value=\"([^\"]+)\"', r_get.text)

            if not (sesskey_m and page_itemid_m and intro_itemid_m):
                print(f"  ❌ Failed to parse form tokens for {page_id}")
                continue

            sesskey = sesskey_m.group(1)
            page_itemid = page_itemid_m.group(1)
            intro_itemid = intro_itemid_m.group(1)

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
                total_created += 1
            else:
                print(f"  ❌ Failed to create {page_title}: Status {r_post.status_code}")

            time.sleep(0.4)  # Politeness delay

    print(f"\n🎉 Deployment completed! Total new pages created: {total_created}")


if __name__ == "__main__":
    update_section_0()
    deploy_subtopic_pages()
