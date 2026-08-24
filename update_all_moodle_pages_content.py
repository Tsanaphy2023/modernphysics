#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Synchronize All 40 Subtopic Pages with Real-Time Simulators on RBRU Moodle Course ID 262
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

def get_input_val(name, html):
    m = re.search(rf'<input[^>]*name=[\"\']{re.escape(name)}[\"\'][^>]*value=[\"\']([^\"\']*)[\"\']', html)
    if not m:
        m = re.search(rf'name=[\"\']{re.escape(name)}[\"\'][^>]*value=[\"\']([^\"\']*)[\"\']', html)
    return m.group(1) if m else ''

# 1. Fetch current module IDs from Moodle
print("Fetching existing Moodle activities...")
r = session.get(f"{BASE_URL}/course/view.php?id={COURSE_ID}")
sesskey = re.search(r'name=\"sesskey\"\s+value=\"([^\"]+)\"', r.text).group(1)

pages_on_moodle = []
sections = re.findall(r'<li[^>]*id=\"section-(\d+)\"[^>]*>(.*?)</li>\s*(?=<li[^>]*id=\"section-|\Z)', r.text, re.DOTALL)

for s_num_str, s_html in sections:
    s_num = int(s_num_str)
    acts = re.findall(r'<li[^>]*class=\"activity\s+page[^>]*id=\"module-(\d+)\"[^>]*>(.*?)</li>', s_html, re.DOTALL)
    for m_id, m_html in acts:
        inst = re.search(r'<span class=\"instancename\"[^>]*>(.*?)</span>', m_html, re.DOTALL)
        name = re.sub(r'<[^>]+>', '', inst.group(1)).strip() if inst else ""
        pages_on_moodle.append({"section": s_num, "cmid": m_id, "name": name})

print(f"Found {len(pages_on_moodle)} Page modules on Moodle.")

# 2. Update each page's content with the new HTML containing Simulators
updated_count = 0
for pm in pages_on_moodle:
    cmid = pm["cmid"]
    name = pm["name"]
    match_ch = None
    match_p = None
    for ch in CHAPTERS_DATA:
        for p in ch["pages"]:
            if p["id"] in name:
                match_ch = ch
                match_p = p
                break
        if match_p:
            break

    if not match_p:
        print(f"  ⚠️ Could not match module {cmid}: {name}")
        continue

    p_id = match_p["id"]
    html_file = os.path.join(MOODLE_PAGES_DIR, f"chapter_{match_ch['id']}", f"page_{p_id.replace('.', '_')}.html")
    if not os.path.exists(html_file):
        print(f"  ❌ File not found: {html_file}")
        continue

    with open(html_file, "r", encoding="utf-8") as f:
        page_html = f.read()

    edit_url = f"{BASE_URL}/course/modedit.php?update={cmid}&return=0&sr=0"
    r_get = session.get(edit_url)
    if r_get.status_code != 200:
        print(f"  ❌ Error opening edit form for {p_id} (cmid {cmid}): {r_get.status_code}")
        continue

    sesskey = get_input_val("sesskey", r_get.text)
    instance = get_input_val("instance", r_get.text)
    page_itemid = get_input_val("page[itemid]", r_get.text)
    intro_itemid = get_input_val("introeditor[itemid]", r_get.text)

    if not (instance and page_itemid and intro_itemid):
        print(f"  ❌ Failed to parse tokens for {p_id}")
        continue

    payload = {
        "course": COURSE_ID,
        "coursemodule": cmid,
        "section": str(match_ch["id"]),
        "module": "15",
        "modulename": "page",
        "instance": instance,
        "add": "0",
        "update": cmid,
        "return": "0",
        "sr": "0",
        "beforemod": "0",
        "revision": "2",
        "sesskey": sesskey,
        "_qf__mod_page_mod_form": "1",
        "mform_isexpanded_id_general": "1",
        "mform_isexpanded_id_contentsection": "1",
        "name": match_p["title"],
        "introeditor[text]": f"<p>{match_p['summary']}</p>",
        "introeditor[format]": "1",
        "introeditor[itemid]": intro_itemid,
        "page[text]": page_html,
        "page[format]": "1",
        "page[itemid]": page_itemid,
        "printintro": "0",
        "printlastmodified": "1",
        "display": "5",
        "availabilityconditionsjson": '{"op":"&","c":[],"showc":[]}',
        "submitbutton2": "บันทึกและกลับไปยังรายวิชา"
    }

    post_headers = {
        "Referer": edit_url,
        "Origin": BASE_URL,
        "Content-Type": "application/x-www-form-urlencoded"
    }

    r_post = session.post(f"{BASE_URL}/course/modedit.php", data=payload, headers=post_headers)
    if r_post.status_code == 200:
        print(f"  ✅ Updated with Simulator: {match_p['title']}")
        updated_count += 1
    else:
        print(f"  ❌ Failed to update {match_p['title']}: Status {r_post.status_code}")

    time.sleep(0.2)

print(f"\n🎉 Successfully updated {updated_count} / {len(pages_on_moodle)} pages on Moodle with real-time Simulators!")
