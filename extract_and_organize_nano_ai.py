#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Extracts and Organizes Nanotechnology and Artificial Intelligence (AI)
knowledge bases, textbooks, lesson plans, lab designs, and simulation code
from /Users/chewathassana/Downloads/manus_backup2026
into /Users/chewathassana/Downloads/manus_backup2026/ModernPhysics/nanotechnology
"""

import os
import shutil
import zipfile
import glob

BASE_BACKUP = "/Users/chewathassana/Downloads/manus_backup2026"
DEST_DIR = "/Users/chewathassana/Downloads/manus_backup2026/ModernPhysics/nanotechnology"

os.makedirs(DEST_DIR, exist_ok=True)
os.makedirs(os.path.join(DEST_DIR, "01_นาโนเทคโนโลยีเชิงฟิสิกส์_4014971"), exist_ok=True)
os.makedirs(os.path.join(DEST_DIR, "02_ปัญญาประดิษฐ์และฟิสิกส์เชิงคำนวณ_AI_Physics"), exist_ok=True)
os.makedirs(os.path.join(DEST_DIR, "03_เอกสารต้นฉบับ_Original_Archives"), exist_ok=True)

print("🚀 Starting extraction and organization of Nanotechnology and AI data...")

# 1. Process Nanotechnology zip packages
nano_zip_1 = os.path.join(BASE_BACKUP, "2 ct2709@gmail.com/ฟิสิกส์-ฟิสิกส์การเกษตร/Analyzing Learning Objectives in Nanotechnological Physics Document.zip")
nano_zip_2 = os.path.join(BASE_BACKUP, "10 physics@rbru.ac.th/ฟิสิกส์-ฟิสิกส์การเกษตร/ข้อเสนอแนะสำหรับการสอนนาโนฟิสิกส์ใน 15 สัปดาห์.zip")

nano_target_1 = os.path.join(DEST_DIR, "01_นาโนเทคโนโลยีเชิงฟิสิกส์_4014971/01_ชุดหลักสูตรและเอกสารคำสอน")
nano_target_2 = os.path.join(DEST_DIR, "01_นาโนเทคโนโลยีเชิงฟิสิกส์_4014971/02_แผนการสอน15สัปดาห์และแล็บเสมือนจริง")

if os.path.exists(nano_zip_1):
    print(f"📦 Extracting: {os.path.basename(nano_zip_1)}")
    os.makedirs(nano_target_1, exist_ok=True)
    with zipfile.ZipFile(nano_zip_1, 'r') as zf:
        zf.extractall(nano_target_1)
    shutil.copy2(nano_zip_1, os.path.join(DEST_DIR, "03_เอกสารต้นฉบับ_Original_Archives/Analyzing_Learning_Objectives_Nanotech_Physics.zip"))

if os.path.exists(nano_zip_2):
    print(f"📦 Extracting: {os.path.basename(nano_zip_2)}")
    os.makedirs(nano_target_2, exist_ok=True)
    with zipfile.ZipFile(nano_zip_2, 'r') as zf:
        zf.extractall(nano_target_2)
    shutil.copy2(nano_zip_2, os.path.join(DEST_DIR, "03_เอกสารต้นฉบับ_Original_Archives/ข้อเสนอแนะสำหรับการสอนนาโนฟิสิกส์ใน_15_สัปดาห์.zip"))

# Check for nested zips in nano_target_1
for root, dirs, files in os.walk(nano_target_1):
    for f in files:
        if f.endswith('.zip'):
            nested_zip = os.path.join(root, f)
            extract_folder = os.path.splitext(nested_zip)[0]
            print(f"  📦 Unzipping nested: {f}")
            try:
                with zipfile.ZipFile(nested_zip, 'r') as zf:
                    zf.extractall(extract_folder)
            except Exception as e:
                print(f"    ⚠️ Error extracting {f}: {e}")

# 2. Extract Key AI & Computational Physics Markdown files
ai_cs_dir = os.path.join(BASE_BACKUP, "cs2026/06_ฟิสิกส์เชิงคำนวณ_และ_Spatial_Computing/D_สร้างโครงร่างหนังสือฟิสิกส์เชิงคำนวณใหม่_extracted")
if os.path.exists(ai_cs_dir):
    pinn_target = os.path.join(DEST_DIR, "02_ปัญญาประดิษฐ์และฟิสิกส์เชิงคำนวณ_AI_Physics/01_PINN_โครงข่ายประสาทเทียมฟิสิกส์")
    os.makedirs(pinn_target, exist_ok=True)
    for f in os.listdir(ai_cs_dir):
        if 'ปัญญาประดิษฐ์' in f or 'ฟิสิกส์เชิงคำนวณ' in f:
            src = os.path.join(ai_cs_dir, f)
            dst = os.path.join(pinn_target, f)
            shutil.copy2(src, dst)
            print(f"📄 Copied AI Physics: {f}")

# 3. Find and copy AI teaching documents and Python ML files
ai_zip_candidates = [
    os.path.join(BASE_BACKUP, "tsanac-gmail/ฟิสิกส์-ฟิสิกส์การเกษตร/36  Download เอกสารสอนปัญญาประดิษฐ์สำหรับฟิสิกส์เชิงคณิตศาสตร์.zip"),
    os.path.join(BASE_BACKUP, "tsanac-gmail/ฟิสิกส์-ฟิสิกส์การเกษตร/36 เอกสารสอนปัญญาประดิษฐ์ในฟิสิกส์เชิงคณิตศาสตร์.zip"),
    os.path.join(BASE_BACKUP, "7 jchome709@gmail.com/ฟิสิกส์-ฟิสิกส์การเกษตร/06 __ร่างเอกสารคำสอนปัญญาประดิษฐ์สำหรับฟิสิกส์แผนใหม่.zip"),
    os.path.join(BASE_BACKUP, "6 tsanaphysics@gmail.com/ปัญญาประดิษฐ์-ML-DL/31 -- การประยุกต์ใช้ปัญญาประดิษฐ์สำหรับข้อมูลและภาพด้วยภาษาไพทอน.zip"),
    os.path.join(BASE_BACKUP, "6 tsanaphysics@gmail.com/ปัญญาประดิษฐ์-ML-DL/26--R-- หนังสือแมกาซีนปัญญาประดิษฐ์และการเรียนรู้เชิงลึก.zip"),
    os.path.join(BASE_BACKUP, "tsanaphysics-outlook/ปัญญาประดิษฐ์-ML-DL/D-คู่มืออบรม AI Coding และ Python 24 ชั่วโมง.zip"),
    os.path.join(BASE_BACKUP, "8 nseconference@gmail.com/ปัญญาประดิษฐ์-ML-DL/08 ออกแบบและจัดทำ AI Agent สำหรับสร้างภาพยนต์ซีรีย์.zip"),
]

ai_target_dir = os.path.join(DEST_DIR, "02_ปัญญาประดิษฐ์และฟิสิกส์เชิงคำนวณ_AI_Physics/02_เอกสารคำสอนและคู่มืออบรม_AI")
os.makedirs(ai_target_dir, exist_ok=True)

for az in ai_zip_candidates:
    if os.path.exists(az):
        base_n = os.path.basename(az)
        folder_n = os.path.splitext(base_n)[0].strip()
        extract_to = os.path.join(ai_target_dir, folder_n)
        print(f"📦 Extracting AI archive: {base_n}")
        try:
            with zipfile.ZipFile(az, 'r') as zf:
                zf.extractall(extract_to)
            shutil.copy2(az, os.path.join(DEST_DIR, "03_เอกสารต้นฉบับ_Original_Archives", base_n))
        except Exception as e:
            print(f"  ⚠️ Error extracting {az}: {e}")

# 4. Generate README.md Index Catalog
readme_content = f"""# 🔬 คลังข้อมูลนาโนเทคโนโลยีและปัญญาประดิษฐ์ (Nanotechnology & AI Hub)

รวบรวมและจัดหมวดหมู่เอกสารคำสอน ตำรา แผนการสอน โครงการวิจัย แบบจำลอง 2D/3D และซอร์สโค้ดเชิงคำนวณที่เกี่ยวข้องกับ **นาโนเทคโนโลยี (Nanotechnology / Nanophysics)** และ **ปัญญาประดิษฐ์เชิงฟิสิกส์ (AI for Physics / PINN / Machine Learning)** ของมหาวิทยาลัยราชภัฏรำไพพรรณี (RBRU)

---

## 📁 โครงสร้างโฟลเดอร์สารบัญ

### 1. `01_นาโนเทคโนโลยีเชิงฟิสิกส์_4014971/`
* **`01_ชุดหลักสูตรและเอกสารคำสอน/`**
  * `เอกสารประกอบการสอน_นาโนเทคโนโลยีเชิงฟิสิกส์.md` / `.html`
  * `การวิเคราะห์ผลลัพธ์การเรียนรู้ของรายวิชา นาโนเทคโนโลยีเชิงฟิสิกส์.md`
  * `สไลด์คาบแรก_นาโนเทคโนโลยีเชิงฟิสิกส์.md`
  * `หลักฐานสำหรับแนวทางความปลอดภัยในห้องปฏิบัติการนาโน.md`
  * `แหล่งอ้างอิงสำหรับ eBook รายวิชา 4014971 นาโนเทคโนโลยีเชิงฟิสิกส์.md`
  * `build_nano_ebook.py` & `generate_nano_ebook_chapters.py`
  * `นาโนเทคโนโลยีเชิงฟิสิกส์: จากมาตราส่วนสู่หลักฐานและการตัดสินใจอย่างรับผิดชอบ.pptx`
  * `นาโนเชิงฟิสิกส์.pdf`
* **`02_แผนการสอน15สัปดาห์และแล็บเสมือนจริง/`**
  * `ข้อเสนอแนะและแผนการสอนรายวิชา “นาโนฟิสิกส์เชิงฟิสิกส์” 15 สัปดาห์.md`
  * `แผนห้องทดลองเสมือนจริง 2D/3D สำหรับรายวิชานาโนฟิสิกส์.md`
  * `nanomaterials_laboratory_architecture_th.md`
  * `modern_nanotechnology_research_notes_th.md`
  * `NanoMaterials.tsx` (React/Three.js 3D Nanomaterials Visualizer)
  * `miniproject_solution_nanophysics.py`

### 2. `02_ปัญญาประดิษฐ์และฟิสิกส์เชิงคำนวณ_AI_Physics/`
* **`01_PINN_โครงข่ายประสาทเทียมฟิสิกส์/`**
  * `บทที่ 5: ปัญญาประดิษฐ์ในฟิสิกส์เชิงคำนวณและโครงข่ายประสาทเทียมที่คำนึงถึงฟิสิกส์.md` (Physics-Informed Neural Networks)
  * `ฟิสิกส์เชิงคำนวณขั้นสูง: จากรากฐานคลาสสิก สารสนเทศควอนตัม สู่การค้นพบทางวิทยาศาสตร์ด้วยปัญญาประดิษฐ์.md`
* **`02_เอกสารคำสอนและคู่มืออบรม_AI/`**
  * เอกสารสอนปัญญาประดิษฐ์สำหรับฟิสิกส์เชิงคณิตศาสตร์
  * ร่างเอกสารคำสอนปัญญาประดิษฐ์สำหรับฟิสิกส์แผนใหม่
  * การประยุกต์ใช้ปัญญาประดิษฐ์สำหรับข้อมูลและภาพด้วยภาษาไพทอน
  * คู่มืออบรม AI Coding และ Python 24 ชั่วโมง
  * หนังสือแมกาซีนปัญญาประดิษฐ์และการเรียนรู้เชิงลึก
  * การออกแบบและจัดทำ AI Agent

### 3. `03_เอกสารต้นฉบับ_Original_Archives/`
* สำเนาไฟล์ `.zip` ต้นฉบับทั้งหมดจากคลังสำรอง `manus_backup2026` สำหรับเป็นชุดข้อมูลอ้างอิงถาวร
"""

with open(os.path.join(DEST_DIR, "README.md"), "w", encoding="utf-8") as f:
    f.write(readme_content)

print("\n🎉 Extraction and organization completed successfully!")
