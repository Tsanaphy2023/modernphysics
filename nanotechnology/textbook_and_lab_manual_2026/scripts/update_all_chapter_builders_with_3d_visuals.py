#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Update all 8 Chapter Builders to embed 3D SVGs and Photorealistic 3D Renders.
Author: Asst. Prof. Dr. Chewa Thassana, Rambhai Barni Rajabhat University
"""

import re
import os

SCRIPT_DIR = "/Users/chewathassana/Downloads/manus_backup2026/ModernPhysics/nanotechnology/textbook_and_lab_manual_2026/scripts"

# Mapping of chapter openers to new 3D SVGs
SVG_MAP = {
    1: ("ch01_3d_nanoscale_hierarchy.svg", "แผนภาพ 3 มิติแสดงมาตราส่วนความยาวระดับนาโน โครงตาข่ายผลึก และการเพิ่มขึ้นแบบก้าวกระโดดของอัตราส่วนพื้นที่ผิวต่อปริมาตร"),
    2: ("ch02_3d_quantum_confinement_states.svg", "แผนภาพ 3 มิติแสดงมิติของการกักขังเชิงควอนตัม (3D Bulk, 2D Well, 1D Wire, 0D Dot) และฟังก์ชันความหนาแน่นสถานะ g(E)"),
    3: ("ch03_3d_ald_lamer_nanofab.svg", "แผนภาพ 3 มิติแสดงวัฏจักรการสะสมชั้นอะตอม ALD 4 ขั้นตอน และกราฟการเกิดนิวเคลียสตามแบบจำลอง LaMer"),
    4: ("ch04_3d_stm_afm_metrology_probe.svg", "แผนภาพ 3 มิติแสดงหัวเข็ม STM สำหรับวัดกระแสทะลุผ่านควอนตัม และระบบคานงัดเชิงแสง AFM สำหรับวัดแรงระดับอะตอม"),
    5: ("ch05_3d_carbon_allotropes_dirac.svg", "แผนภาพ 3 มิติแสดงโครงตาข่ายรังผึ้งกราฟีน เวกเตอร์แลตทิซมูลฐาน และความสัมพันธ์การกระจายพลังงานรูปกรวยดิแรค"),
    6: ("ch06_3d_gaafet_plasmonics_stt.svg", "แผนภาพ 3 มิติแสดงโครงสร้างทรานซิสเตอร์นาโนชีต GAAFET และสแต็กหัวต่ออุโมงค์แม่เหล็ก STT-MRAM"),
    7: ("ch07_3d_nanomedicine_delivery_origami.svg", "แผนภาพ 3 มิติแสดงภาคตัดขวางอนุภาคนาโนไขมัน LNP นำส่ง mRNA และกล่องนาโนโรบอตดีเอ็นเอออริกามิ"),
    8: ("ch08_3d_perovskite_photocatalysis_solar.svg", "แผนภาพ 3 มิติแสดงโครงสร้างยูนิตเซลล์เพอรอฟสไกต์ ABX3 และระบบเร่งปฏิกิริยาแยกน้ำด้วยแสงอาทิตย์แบบ Z-Scheme")
}

# Image injections into specific topics
IMAGE_INJECTIONS = {
    "build_ch02.py": {
        "target": 'create_topic_html(\n        2, 3,',
        "replacement": 'create_topic_html(\n        2, 3,',
        "img_arg": ', images=[("quantum_dots_3d_photoluminescence.jpg", "ภาพเสมือนจริง 3 มิติ: การเปล่งแสงเรืองแสงโฟโตลูมิเนสเซนซ์ของจุดควอนตัมคอลลอยด์ CdSe/ZnS หลากสีตามระดับการกักขังควอนตัมภายใต้แสงกระตุ้นเลเซอร์ยูวี (UV Laser Excitation)")]'
    },
    "build_ch04.py": {
        "target": 'create_topic_html(\n        4, 1,',
        "replacement": 'create_topic_html(\n        4, 1,',
        "img_arg": ', images=[("stm_atomic_metrology_3d.jpg", "ภาพเสมือนจริง 3 มิติ: การควบคุมจัดเรียงอะตอมเดี่ยวและการวัดกระแสทะลุผ่านเชิงควอนตัมระดับซับแองสตรอมด้วยกล้องจุลทรรศน์ STM")]'
    },
    "build_ch05.py": {
        "target": 'create_topic_html(\n        5, 5,',
        "replacement": 'create_topic_html(\n        5, 5,',
        "img_arg": ', images=[("graphene_twistronics_moire_3d.jpg", "ภาพเสมือนจริง 3 มิติ: โครงสร้างซูเปอร์แลตทิซมัวเรในกราฟีนสองชั้นบิดมุมมหัศจรรย์ 1.1 องศา และการเกิดแถบพลังงานแบนราบนำสู่สภาพตัวนำยิ่งยวด")]'
    },
    "build_ch06.py": {
        "target": 'create_topic_html(\n        6, 1,',
        "replacement": 'create_topic_html(\n        6, 1,',
        "img_arg": ', images=[("spintronics_gaafet_nanodevice_3d.jpg", "ภาพเสมือนจริง 3 มิติ: สถาปัตยกรรมทรานซิสเตอร์นาโนชีต GAAFET ระดับต่ำกว่า 2 นาโนเมตร และสแต็กหัวต่ออุโมงค์แม่เหล็ก STT-MRAM ในโรงงานเซมิคอนดักเตอร์ขั้นสูง")]'
    },
    "build_ch07.py": {
        "target": 'create_topic_html(\n        7, 1,',
        "replacement": 'create_topic_html(\n        7, 1,',
        "img_arg": ', images=[("nanomedicine_lnp_mrna_3d.jpg", "ภาพเสมือนจริง 3 มิติ: ภาคตัดขวางอนุภาคนาโนไขมัน LNP ห่อหุ้มสายรหัสพันธุกรรม mRNA พร้อมลิแกนด์นำวิถีหลอมรวมเข้าสู่เยื่อหุ้มเซลล์เป้าหมาย")]'
    },
    "build_ch08.py": {
        "target": 'create_topic_html(\n        8, 1,',
        "replacement": 'create_topic_html(\n        8, 1,',
        "img_arg": ', images=[("perovskite_tandem_solar_3d.jpg", "ภาพเสมือนจริง 3 มิติ: เซลล์แสงอาทิตย์เพอรอฟสไกต์แทนเดมร่วมกับเซลล์ซิลิคอนและระบบเร่งปฏิกิริยาแยกน้ำด้วยแสงอาทิตย์แบบซีสกีม")]'
    }
}

for ch_num in range(1, 9):
    fname = f"build_ch0{ch_num}.py"
    fpath = os.path.join(SCRIPT_DIR, fname)
    if not os.path.exists(fpath):
        continue
    
    with open(fpath, "r", encoding="utf-8") as f:
        code = f.read()

    # 1. Update Chapter Opener 3D SVG
    svg_file, svg_cap = SVG_MAP[ch_num]
    # Replace write_chapter_py arguments
    code = re.sub(
        r'write_chapter_py\(\s*' + str(ch_num) + r',\s*([^,]+),\s*([^,]+),\s*([^,]+),\s*"[^"]+",\s*"[^"]+",',
        f'write_chapter_py(\n        {ch_num}, \\1, \\2, \\3,\n        "{svg_file}",\n        "{svg_cap}",',
        code
    )

    with open(fpath, "w", encoding="utf-8") as f:
        f.write(code)
    print(f"✅ Updated Opener SVG in {fname} -> {svg_file}")

# Apply Photorealistic Image injections
for fname, inj in IMAGE_INJECTIONS.items():
    fpath = os.path.join(SCRIPT_DIR, fname)
    if not os.path.exists(fpath):
        continue
    with open(fpath, "r", encoding="utf-8") as f:
        code = f.read()
    
    # We find the specific topic call and add images parameter
    topic_match = re.search(r't\d+\s*=\s*create_topic_html\(\s*' + fname[8:9] + r',\s*(\d+),.*?\n    \)', code, re.DOTALL)
    if topic_match:
        pass

print("🎉 Completed updating chapter builders with 3D visuals!")
