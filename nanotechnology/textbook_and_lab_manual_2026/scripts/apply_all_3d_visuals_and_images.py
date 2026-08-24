#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Precise injector for 3D SVGs and Photorealistic 3D Renders across all 8 chapters.
Places images parameter at the END of create_topic_html calls.
Author: Asst. Prof. Dr. Chewa Thassana, Rambhai Barni Rajabhat University
"""

import os
import re

SCRIPT_DIR = "/Users/chewathassana/Downloads/manus_backup2026/ModernPhysics/nanotechnology/textbook_and_lab_manual_2026/scripts"

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

# Injections with target pattern (end of the specific topic call before t4/t2/t6/etc.)
TOPIC_IMAGE_MAP = {
    "build_ch02.py": (
        "t3 = create_topic_html",
        "quantum_dots_3d_photoluminescence.jpg",
        "ภาพเสมือนจริง 3 มิติ: การเปล่งแสงเรืองแสงโฟโตลูมิเนสเซนซ์ของจุดควอนตัมคอลลอยด์ CdSe/ZnS หลากสีตามระดับการกักขังควอนตัมภายใต้แสงกระตุ้นเลเซอร์ยูวี (UV Laser Excitation)"
    ),
    "build_ch04.py": (
        "t1 = create_topic_html",
        "stm_atomic_metrology_3d.jpg",
        "ภาพเสมือนจริง 3 มิติ: การควบคุมจัดเรียงอะตอมเดี่ยวและการวัดกระแสทะลุผ่านเชิงควอนตัมระดับซับแองสตรอมด้วยกล้องจุลทรรศน์ STM"
    ),
    "build_ch05.py": (
        "t5 = create_topic_html",
        "graphene_twistronics_moire_3d.jpg",
        "ภาพเสมือนจริง 3 มิติ: โครงสร้างซูเปอร์แลตทิซมัวเรในกราฟีนสองชั้นบิดมุมมหัศจรรย์ 1.1 องศา และการเกิดแถบพลังงานแบนราบนำสู่สภาพตัวนำยิ่งยวด"
    ),
    "build_ch06.py": (
        "t1 = create_topic_html",
        "spintronics_gaafet_nanodevice_3d.jpg",
        "ภาพเสมือนจริง 3 มิติ: สถาปัตยกรรมทรานซิสเตอร์นาโนชีต GAAFET ระดับต่ำกว่า 2 นาโนเมตร และสแต็กหัวต่ออุโมงค์แม่เหล็ก STT-MRAM ในโรงงานเซมิคอนดักเตอร์ขั้นสูง"
    ),
    "build_ch07.py": (
        "t1 = create_topic_html",
        "nanomedicine_lnp_mrna_3d.jpg",
        "ภาพเสมือนจริง 3 มิติ: ภาคตัดขวางอนุภาคนาโนไขมัน LNP ห่อหุ้มสายรหัสพันธุกรรม mRNA พร้อมลิแกนด์นำวิถีหลอมรวมเข้าสู่เยื่อหุ้มเซลล์เป้าหมาย"
    ),
    "build_ch08.py": (
        "t1 = create_topic_html",
        "perovskite_tandem_solar_3d.jpg",
        "ภาพเสมือนจริง 3 มิติ: เซลล์แสงอาทิตย์เพอรอฟสไกต์แทนเดมร่วมกับเซลล์ซิลิคอนและระบบเร่งปฏิกิริยาแยกน้ำด้วยแสงอาทิตย์แบบซีสกีม"
    ),
}

for ch_num in range(1, 9):
    fname = f"build_ch0{ch_num}.py"
    fpath = os.path.join(SCRIPT_DIR, fname)
    if not os.path.exists(fpath):
        continue
    
    with open(fpath, "r", encoding="utf-8") as f:
        code = f.read()

    # Clean out any old misplaced images= keywords
    code = re.sub(r'images=\[[^\]]+\]\s*,\s*', '', code)

    # 1. Update Chapter Opener 3D SVG
    svg_file, svg_cap = SVG_MAP[ch_num]
    code = re.sub(
        r'write_chapter_py\(\s*' + str(ch_num) + r',\s*([^,]+),\s*([^,]+),\s*([^,]+),\s*"[^"]+",\s*"[^"]+",',
        f'write_chapter_py(\n        {ch_num}, \\1, \\2, \\3,\n        "{svg_file}",\n        "{svg_cap}",',
        code
    )

    # 2. If this chapter has an image to inject
    if fname in TOPIC_IMAGE_MAP:
        topic_var, img_file, img_cap = TOPIC_IMAGE_MAP[fname]
        # Find where this topic definition ends
        # Matches: topic_var ... \n    )
        pattern = r'(' + re.escape(topic_var) + r'\(.*?)(\n    \))'
        
        def repl(m):
            body = m.group(1)
            end = m.group(2)
            return f'{body},\n        images=[("{img_file}", "{img_cap}")]{end}'
        
        code = re.sub(pattern, repl, code, count=1, flags=re.DOTALL)
        print(f"  📸 Injected image {img_file} into {fname}")

    with open(fpath, "w", encoding="utf-8") as f:
        f.write(code)
    print(f"✅ Processed {fname}")

print("🎉 All 8 Chapter Builders sanitized and updated!")
