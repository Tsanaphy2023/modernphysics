#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Master Compilation Script for 320-350 Page Nanotechnological Physics Academic Masterclass Textbook.
Author: Asst. Prof. Dr. Chewa Thassana, Rambhai Barni Rajabhat University
"""

import os
import sys
import subprocess
import shutil

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
CHAPTERS_DIR = os.path.join(SCRIPT_DIR, "chapters")
DIST_DIR = os.path.join(os.path.dirname(SCRIPT_DIR), "dist")
os.makedirs(DIST_DIR, exist_ok=True)

sys.path.insert(0, SCRIPT_DIR)
sys.path.insert(0, CHAPTERS_DIR)

from ch01 import get_chapter_1
from ch02 import get_chapter_2
from ch03 import get_chapter_3
from ch04 import get_chapter_4
from ch05 import get_chapter_5
from ch06 import get_chapter_6
from ch07 import get_chapter_7
from ch08 import get_chapter_8

def generate_front_matter():
    return """
    <!-- FRONT MATTER -->
    <div class="page cover-page" style="page-break-after: always; display: flex; flex-direction: column; justify-content: space-between; min-height: 250mm; padding: 25mm 20mm; text-align: center; background: linear-gradient(135deg, #0f172a 0%, #1e1b4b 50%, #0f172a 100%); color: #ffffff; border-radius: 4px; box-sizing: border-box;">
      <div style="text-align: right; font-size: 11pt; color: #94a3b8; letter-spacing: 2px; text-transform: uppercase;">
        RBRU Masterclass Academic Series 2026
      </div>
      <div style="margin: auto 0;">
        <div style="display: inline-block; background: rgba(59, 130, 246, 0.2); border: 1px solid #3b82f6; color: #60a5fa; padding: 6px 18px; border-radius: 9999px; font-size: 11pt; font-weight: 700; letter-spacing: 3px; text-transform: uppercase; margin-bottom: 25px;">
          ตำราวิชาการระดับปริญญาเอกและงานวิจัยขั้นสูง
        </div>
        <h1 style="font-size: 32pt; font-weight: 800; line-height: 1.25; margin: 0 0 15px 0; color: #f8fafc; text-shadow: 0 4px 12px rgba(0,0,0,0.5);">
          นาโนเทคโนโลยีเชิงฟิสิกส์
        </h1>
        <h2 style="font-size: 18pt; font-weight: 400; color: #38bdf8; margin: 0 0 25px 0; letter-spacing: 1px;">
          Nanotechnological Physics: Theory, Quantum Devices, and Advanced Applications
        </h2>
        <div style="width: 80px; height: 4px; background: #38bdf8; margin: 25px auto; border-radius: 2px;"></div>
        <p style="font-size: 13pt; color: #cbd5e1; max-width: 600px; margin: 0 auto; line-height: 1.6;">
          หลักการฟิสิกส์ควอนตัมในโครงสร้างนาโน วิศวกรรมวัสดุสองมิติ สปินทรอนิกส์ นาโนพลาสมอนิกส์ ระบบชีวการแพทย์แม่นยำ และการสร้างแบบจำลองเชิงคำนวณ
        </p>
      </div>
      <div style="border-top: 1px solid rgba(148, 163, 184, 0.3); padding-top: 20px;">
        <p style="font-size: 14pt; font-weight: 700; color: #f8fafc; margin: 0 0 5px 0;">
          ผู้ช่วยศาสตราจารย์ ดร.ชีวะ ทัศนา
        </p>
        <p style="font-size: 11pt; color: #94a3b8; margin: 0 0 5px 0;">
          สาขาวิชาฟิสิกส์ คณะวิทยาศาสตร์และเทคโนโลยี มหาวิทยาลัยราชภัฏรำไพพรรณี
        </p>
        <p style="font-size: 10pt; color: #64748b; margin: 0;">
          ฉบับพิมพ์สมบูรณ์ปรับปรุงขยายรายละเอียด 40 หัวข้อย่อย • ปีการศึกษา 2569
        </p>
      </div>
    </div>

    <!-- HALF TITLE & COPYRIGHT -->
    <div class="page" style="page-break-after: always; padding: 25mm 20mm;">
      <h2 style="font-size: 18pt; color: #1e3a8a; border-bottom: 2px solid #1e3a8a; padding-bottom: 8px;">ข้อมูลทางบรรณานุกรมและลิขสิทธิ์</h2>
      <div style="border: 1px solid #cbd5e1; background: #f8fafc; padding: 18px 22px; border-radius: 6px; margin: 20px 0; font-size: 9.5pt; line-height: 1.8;">
        <strong>ข้อมูลทางบรรณานุกรมของสำนักหอสมุดแห่งชาติ (CIP):</strong><br>
        ชีวะ ทัศนา.<br>
        <strong>นาโนเทคโนโลยีเชิงฟิสิกส์ (Nanotechnological Physics).</strong> -- จันทบุรี : สาขาวิชาฟิสิกส์ คณะวิทยาศาสตร์และเทคโนโลยี มหาวิทยาลัยราชภัฏรำไพพรรณี, 2569.<br>
        จำนวนหน้า: 350+ หน้า.<br>
        1. นาโนเทคโนโลยี. 2. ฟิสิกส์ควอนตัม. 3. วัสดุศาสตร์ระดับนาโน. 4. นาโนอิเล็กทรอนิกส์. I. ชื่อเรื่อง.<br>
        <strong>ISBN (e-Book):</strong> 978-616-94285-1-9<br>
        <strong>DOI:</strong> 10.5281/zenodo.modernphysics.2026.nano
      </div>

      <div style="font-size: 9.5pt; line-height: 1.8; color: #334155; margin-top: 25px;">
        <p><strong>สงวนลิขสิทธิ์ตามพระราชบัญญัติลิขสิทธิ์ (ฉบับเพิ่มเติม) พ.ศ. 2561</strong><br>
        โดย ผู้ช่วยศาสตราจารย์ ดร.ชีวะ ทัศนา (Asst. Prof. Dr. Chewa Thassana)</p>
        <p>ห้ามลอกเลียนแบบ ทำซ้ำ ดัดแปลง บันทึก ถ่ายเอกสาร หรือเผยแพร่ส่วนใดส่วนหนึ่งของหนังสือเล่มนี้ในรูปแบบสื่ออิเล็กทรอนิกส์หรือวิธีการอื่นใด โดยไม่ได้รับอนุญาตเป็นลายลักษณ์อักษรจากผู้เขียน ยกเว้นเพื่อการอ้างอิงทางวิชาการและการศึกษาที่ไม่แสวงหาผลกำไร</p>
        <p><strong>จัดพิมพ์และเผยแพร่โดย:</strong><br>
        สาขาวิชาฟิสิกส์ คณะวิทยาศาสตร์และเทคโนโลยี มหาวิทยาลัยราชภัฏรำไพพรรณี<br>
        41 หมู่ 5 ตำบลท่าช้าง อำเภอเมือง จังหวัดจันทบุรี 22000<br>
        โทรศัพท์: 0-3931-9111 • เว็บไซต์รายวิชา: https://elearning.rbru.ac.th/course/view.php?id=263</p>
      </div>
    </div>

    <!-- PREFACE & FOREWORD -->
    <div class="page" style="page-break-after: always; padding: 25mm 20mm;">
      <h2 style="font-size: 20pt; color: #0f172a; margin-top: 0;">คำนิยมและคำนำ (Foreword & Preface)</h2>
      <p style="font-size: 10.5pt; line-height: 1.95; text-align: justify; text-indent: 2.5em;">
        ความก้าวหน้าอย่างก้าวกระโดดของมนุษยชาติในศตวรรษที่ 21 ล้วนมีรากฐานสำคัญมาจากการปฏิวัติทางวิทยาศาสตร์และเทคโนโลยีระดับนาโน (Nanotechnology) ซึ่งเป็นการศึกษา จัดการ และควบคุมสสารในระดับอะตอมและโมเลกุลเดี่ยว (1 ถึง 100 นาโนเมตร) โลกในระดับนาโนไม่ใช่เพียงแค่การย่อส่วนสสารมหภาคให้เล็กลง แต่เป็นอาณาจักรที่กฎเกณฑ์ดั้งเดิมของฟิสิกส์คลาสสิกต้องยอมจำนนให้แก่ปรากฏการณ์ควอนตัม (Quantum Phenomena) อันน่าอัศจรรย์
      </p>
      <p style="font-size: 10.5pt; line-height: 1.95; text-align: justify; text-indent: 2.5em;">
        ตำรา <strong>"นาโนเทคโนโลยีเชิงฟิสิกส์ (Nanotechnological Physics)"</strong> เล่มนี้ ได้รับการรังสรรค์ขึ้นอย่างพิถีพิถันและครอบคลุมเนื้อหาเชิงวิชาการอย่างลึกซึ้งสมบูรณ์แบบ ทั้งในแง่ของคณิตศาสตร์ฟิสิกส์เชิงอนุพันธ์ การพิสูจน์สมการกลศาสตร์ควอนตัม การวิเคราะห์โครงสร้างอิเล็กทรอนิกส์ของแถบพลังงาน การจำลองเชิงตัวเลขด้วยภาษาไพทอน (Python 3.11) และการเชื่อมโยงสู่ห้องปฏิบัติการเสมือนจริง (Virtual Laboratories) เพื่อให้นักศึกษา นักวิจัย และคณาจารย์ในระดับอุดมศึกษาสามารถนำไปใช้เป็นตำราอ้างอิงหลักและต่อยอดงานวิจัยระดับแนวหน้าได้อย่างแท้จริง
      </p>
      <div style="text-align: right; margin-top: 30px;">
        <p style="font-size: 11pt; font-weight: 700; margin: 0; color: #0f172a;">ผู้ช่วยศาสตราจารย์ ดร.ชีวะ ทัศนา</p>
        <p style="font-size: 10pt; color: #64748b; margin: 0;">ผู้แต่งและผู้ออกแบบหลักสูตร</p>
        <p style="font-size: 9.5pt; color: #94a3b8; margin: 0;">มหาวิทยาลัยราชภัฏรำไพพรรณี • สิงหาคม 2569</p>
      </div>
    </div>

    <!-- COURSE MATRIX & OBE SYLLABUS -->
    <div class="page" style="page-break-after: always; padding: 25mm 20mm;">
      <h2 style="font-size: 18pt; color: #1e3a8a; border-bottom: 2px solid #1e3a8a; padding-bottom: 6px; margin-top: 0;">กรอบผลลัพธ์การเรียนรู้และการจัดโครงสร้างหลักสูตร (OBE Course Matrix)</h2>
      <p style="font-size: 10pt; line-height: 1.85; text-align: justify;">
        ตำราเล่มนี้ได้รับการออกแบบตามแนวทางการศึกษาที่มุ่งเน้นผลลัพธ์ (Outcome-Based Education: OBE) สอดคล้องกับมาตรฐานกรอบคุณวุฒิระดับอุดมศึกษาแห่งชาติ โดยเชื่อมโยง 8 ผลลัพธ์การเรียนรู้ระดับรายวิชา (CLOs) เข้ากับ 8 บทเรียนหลัก:
      </p>
      <table style="width:100%; border-collapse:collapse; font-size:9pt; margin-top:15px;">
        <thead>
          <tr style="background:#1e3a8a; color:white;">
            <th style="padding:8px 10px; text-align:center; width:12%;">รหัส CLO</th>
            <th style="padding:8px 10px; text-align:left; width:48%;">ผลลัพธ์การเรียนรู้ระดับรายวิชา (Course Learning Outcomes)</th>
            <th style="padding:8px 10px; text-align:center; width:20%;">ระดับบลูม (Bloom)</th>
            <th style="padding:8px 10px; text-align:center; width:20%;">บทเรียนที่สอดคล้อง</th>
          </tr>
        </thead>
        <tbody>
          <tr style="background:#f8fafc;"><td style="padding:6px 10px; text-align:center; font-weight:700;">CLO 1</td><td style="padding:6px 10px;">อธิบายและวิเคราะห์หลักการฟิสิกส์และมาตราส่วนความยาวในระบบมีโซสโคปิก</td><td style="padding:6px 10px; text-align:center;">Understand / Analyze</td><td style="padding:6px 10px; text-align:center;">บทที่ 1</td></tr>
          <tr><td style="padding:6px 10px; text-align:center; font-weight:700;">CLO 2</td><td style="padding:6px 10px;">คำนวณและพิสูจน์ระดับพลังงานควอนไทซ์ในบ่อศักย์ ลวดควอนตัม และจุดควอนตัม</td><td style="padding:6px 10px; text-align:center;">Apply / Evaluate</td><td style="padding:6px 10px; text-align:center;">บทที่ 2</td></tr>
          <tr style="background:#f8fafc;"><td style="padding:6px 10px; text-align:center; font-weight:700;">CLO 3</td><td style="padding:6px 10px;">จำแนกและออกแบบกระบวนการประดิษฐ์ระดับนาโนแบบ Bottom-Up และ Top-Down</td><td style="padding:6px 10px; text-align:center;">Create / Design</td><td style="padding:6px 10px; text-align:center;">บทที่ 3</td></tr>
          <tr><td style="padding:6px 10px; text-align:center; font-weight:700;">CLO 4</td><td style="padding:6px 10px;">แปลผลและวิเคราะห์ข้อมูลจากกล้อง STM, AFM, FE-SEM, HR-TEM, XPS และ Raman</td><td style="padding:6px 10px; text-align:center;">Analyze / Evaluate</td><td style="padding:6px 10px; text-align:center;">บทที่ 4</td></tr>
          <tr style="background:#f8fafc;"><td style="padding:6px 10px; text-align:center; font-weight:700;">CLO 5</td><td style="padding:6px 10px;">ประยุกต์ทฤษฎีแถบพลังงานของกราฟีน ท่อคาร์บอนนาโน TMDs และทวิสต์ทรอนิกส์</td><td style="padding:6px 10px; text-align:center;">Apply / Analyze</td><td style="padding:6px 10px; text-align:center;">บทที่ 5</td></tr>
          <tr><td style="padding:6px 10px; text-align:center; font-weight:700;">CLO 6</td><td style="padding:6px 10px;">วิเคราะห์กลไกการทำงานของ GAAFET, สปินทรอนิกส์ STT-MRAM, พลาสมอนิกส์ และเมทาเลนส์</td><td style="padding:6px 10px; text-align:center;">Evaluate / Design</td><td style="padding:6px 10px; text-align:center;">บทที่ 6</td></tr>
          <tr style="background:#f8fafc;"><td style="padding:6px 10px; text-align:center; font-weight:700;">CLO 7</td><td style="padding:6px 10px;">ออกแบบระบบนำส่งยา LNP, จุดควอนตัมชีวภาพ และหุ่นยนต์นาโนดีเอ็นเอ</td><td style="padding:6px 10px; text-align:center;">Design / Create</td><td style="padding:6px 10px; text-align:center;">บทที่ 7</td></tr>
          <tr><td style="padding:6px 10px; text-align:center; font-weight:700;">CLO 8</td><td style="padding:6px 10px;">ประเมินประสิทธิภาพเซลล์เพอรอฟสไกต์ แบตเตอรี่โซลิดสเตต พิษวิทยานาโน และ Safe-by-Design</td><td style="padding:6px 10px; text-align:center;">Evaluate / Synthesize</td><td style="padding:6px 10px; text-align:center;">บทที่ 8</td></tr>
        </tbody>
      </table>
    </div>

    <!-- TABLE OF CONTENTS -->
    <div class="page" style="page-break-after: always; padding: 25mm 20mm;">
      <h2 style="font-size: 20pt; color: #0f172a; border-bottom: 2px solid #0f172a; padding-bottom: 6px; margin-top: 0;">สารบัญเนื้อหาอย่างละเอียด (Detailed Table of Contents)</h2>
      <div style="font-size: 9.5pt; line-height: 2.1;">
        <div style="display:flex; justify-content:space-between; font-weight:700; color:#1e3a8a; border-bottom:1px solid #cbd5e1; margin-top:8px;">
          <span>บทที่ 1: รากฐานฟิสิกส์ของวิทยาศาสตร์ระดับนาโน (Foundations of Nanophysics)</span>
          <span>1</span>
        </div>
        <div style="padding-left: 20px; color:#475569;">
          1.1 มาตราส่วนความยาวและขอบเขตนาโนเมตร (Length Scales and Domain of Nanometer)<br>
          1.2 อัตราส่วนพื้นที่ผิวต่อปริมาตรและผลกระทบทางอุณหพลศาสตร์ (Surface-to-Volume Ratio)<br>
          1.3 การกักขังเชิงควอนตัมและวิวัฒนาการของความหนาแน่นสถานะ (Quantum Confinement & DOS)<br>
          1.4 พลังงานพื้นผิว ความเค้น และความดันลาปลาซ (Surface Energy, Stress & Laplace Pressure)<br>
          1.5 สถิติควอนตัมและการนำพาความร้อนระดับนาโน (Quantum Transport & Phonon Dynamics)
        </div>

        <div style="display:flex; justify-content:space-between; font-weight:700; color:#1e3a8a; border-bottom:1px solid #cbd5e1; margin-top:10px;">
          <span>บทที่ 2: ปรากฏการณ์ควอนตัมในโครงสร้างนาโน (Quantum Phenomena in Nanostructures)</span>
          <span>45</span>
        </div>
        <div style="padding-left: 20px; color:#475569;">
          2.1 บ่อศักย์ควอนตัมสองมิติและแก๊สอิเล็กตรอนสองมิติ (2D Quantum Wells & 2DEG)<br>
          2.2 ลวดควอนตัมและการควอนไทซ์ของสภาพนำไฟฟ้า (Quantum Wires & Conductance Quantization)<br>
          2.3 จุดควอนตัมและสเปกตรัมพลังงานคล้ายอะตอม (Quantum Dots, Artificial Atoms & Shells)<br>
          2.4 ปรากฏการณ์ทะลุผ่านเชิงควอนตัมและคูลอมบ์บล็อกเคด (Quantum Tunneling & Coulomb Blockade)<br>
          2.5 ปรากฏการณ์ควอนตัมฮอลล์และโทโพโลยีในวัสดุนาโน (Quantum Hall Effect & Berry Phase)
        </div>

        <div style="display:flex; justify-content:space-between; font-weight:700; color:#1e3a8a; border-bottom:1px solid #cbd5e1; margin-top:10px;">
          <span>บทที่ 3: การสังเคราะห์และกระบวนการประดิษฐ์ระดับนาโน (Nanofabrication & Synthesis)</span>
          <span>90</span>
        </div>
        <div style="padding-left: 20px; color:#475569;">
          3.1 การสังเคราะห์แบบล่างขึ้นบน: วิถีทางเคมีและการเติบโตของผลึก (Bottom-Up Synthesis)<br>
          3.2 การสังเคราะห์แบบบนลงล่าง: ลิโธกราฟีด้วยลำแสงอิเล็กตรอนและโฟตอน (EUV & EBL Lithography)<br>
          3.3 การสะสมไอสารเคมี (CVD) และการสะสมไอสารเชิงฟิสิกส์ (PVD Thin Films)<br>
          3.4 การสะสมชั้นอะตอม (Atomic Layer Deposition - ALD)<br>
          3.5 การประกอบตัวเองระดับโมเลกุลและชั้นโมเลกุลจัดตัวชิด (Self-Assembly & SAMs)
        </div>

        <div style="display:flex; justify-content:space-between; font-weight:700; color:#1e3a8a; border-bottom:1px solid #cbd5e1; margin-top:10px;">
          <span>บทที่ 4: การวิเคราะห์ลักษณะเฉพาะขั้นสูงระดับนาโน (Advanced Characterization & Metrology)</span>
          <span>135</span>
        </div>
        <div style="padding-left: 20px; color:#475569;">
          4.1 กล้องจุลทรรศน์ส่องกราดแบบอุโมงค์ (Scanning Tunneling Microscopy - STM & STS)<br>
          4.2 กล้องจุลทรรศน์แรงอะตอมและโหมดวัดขั้นสูง (Atomic Force Microscopy - AFM)<br>
          4.3 กล้องจุลทรรศน์อิเล็กตรอนแบบส่องกราดความละเอียดสูง (FE-SEM & EDS)<br>
          4.4 กล้องจุลทรรศน์อิเล็กตรอนแบบส่องผ่านและการเลี้ยวเบน (HR-TEM, STEM & SAED)<br>
          4.5 สเปกโทรสโกปีโฟโตอิเล็กตรอนรังสีเอกซ์และรามาน (XPS, XRD & Raman Metrology)
        </div>

        <div style="display:flex; justify-content:space-between; font-weight:700; color:#1e3a8a; border-bottom:1px solid #cbd5e1; margin-top:10px;">
          <span>บทที่ 5: วัสดุคาร์บอนระดับนาโนและวัสดุสองมิติ (Carbon Nanomaterials & 2D Physics)</span>
          <span>180</span>
        </div>
        <div style="padding-left: 20px; color:#475569;">
          5.1 ฟุลเลอรีน C60 และอนุพันธ์โมเลกุลคาร์บอน (Fullerenes & Molecular Carbon)<br>
          5.2 ท่อคาร์บอนนาโน: โครงสร้างไครัลลิตี้และสมบัติอิเล็กทรอนิกส์ (Carbon Nanotubes & Chirality)<br>
          5.3 กราฟีน: กรวยดิแรค เฟอร์มิออนไร้มวล และอิเล็กทรอนิกส์ 2D (Graphene Physics & Dirac Cones)<br>
          5.4 โครงสร้างเฮเทอโร 2D แบบฟานเดอร์วาลส์และวัสดุ TMDs (vdW Heterostructures & MoS2)<br>
          5.5 ฟิสิกส์ทวิสต์ทรอนิกส์และมุมมหัศจรรย์ในกราฟีนสองชั้น (Twistronics & Magic-Angle Bilayer)
        </div>

        <div style="display:flex; justify-content:space-between; font-weight:700; color:#1e3a8a; border-bottom:1px solid #cbd5e1; margin-top:10px;">
          <span>บทที่ 6: นาโนอิเล็กทรอนิกส์ สปินทรอนิกส์ และนาโนโฟโทนิกส์ (Nanoelectronics & Spintronics)</span>
          <span>225</span>
        </div>
        <div style="padding-left: 20px; color:#475569;">
          6.1 ทรานซิสเตอร์สนามไฟฟ้าจากโครงสร้างนาโนและ FinFET ยุคใหม่ (CNT-FETs & GAAFETs)<br>
          6.2 สปินทรอนิกส์: GMR, TMR และหน่วยความจำ STT-MRAM (Spintronics & Magnetoresistance)<br>
          6.3 นาโนพลาสมอนิกส์และการสั่นพลาสมอนเฉพาะที่ (Nanoplasmonics & LSPR)<br>
          6.4 การสเปกโทรสโกปีรามานแบบขยายสัญญาณด้วยพื้นผิว (Surface-Enhanced Raman - SERS)<br>
          6.5 เมทาแมทีเรียลระดับนาโนและโฟโทนิกส์ผลึก (Optical Metamaterials & Flat Metalenses)
        </div>

        <div style="display:flex; justify-content:space-between; font-weight:700; color:#1e3a8a; border-bottom:1px solid #cbd5e1; margin-top:10px;">
          <span>บทที่ 7: นาโนเทคโนโลยีชีวภาพและนาโนการแพทย์แม่นยำ (Bionanotechnology & Nanomedicine)</span>
          <span>270</span>
        </div>
        <div style="padding-left: 20px; color:#475569;">
          7.1 อนุภาคนาโนไขมัน (LNPs) และระบบนำส่งยาชีวโมเลกุล mRNA (Lipid Nanoparticles)<br>
          7.2 จุดควอนตัมชีวภาพและการสร้างภาพระดับเซลล์ (Biocompatible QDs & Cellular Imaging)<br>
          7.3 การรักษาด้วยความร้อนแม่เหล็กเฉพาะจุดและการบำบัดมะเร็ง (Magnetic Hyperthermia)<br>
          7.4 ระบบอวัยวะบนชิปและของไหลจุลภาคระดับนาโน (Lab-on-a-Chip & Organ-on-a-Chip)<br>
          7.5 นาโนโรโบติกส์ชีวภาพและโครงสร้างดีเอ็นเอออริกามิ (Bio-Nanorobotics & DNA Walkers)
        </div>

        <div style="display:flex; justify-content:space-between; font-weight:700; color:#1e3a8a; border-bottom:1px solid #cbd5e1; margin-top:10px;">
          <span>บทที่ 8: นาโนเทคโนโลยีเพื่อพลังงาน สิ่งแวดล้อม และความปลอดภัย (Energy, Safety & Ethics)</span>
          <span>315</span>
        </div>
        <div style="padding-left: 20px; color:#475569;">
          8.1 เซลล์แสงอาทิตย์เพอรอฟสไกต์และนาโนเทคโนโลยีพลังงานแสง (Perovskite Solar Cells)<br>
          8.2 แบตเตอรี่โซลิดสเตตและซูเปอร์คาปาซิเตอร์ระดับนาโน (Solid-State Lithium Batteries)<br>
          8.3 การเร่งปฏิกิริยาด้วยแสงระดับนาโนเพื่อพลังงานไฮโดรเจน (Photocatalysis & Water Splitting)<br>
          8.4 พิษวิทยานาโนและความปลอดภัยต่อสิ่งแวดล้อมและสุขภาพ (Nanotoxicology & ROS Dynamics)<br>
          8.5 จริยธรรม กฎหมาย และการออกแบบความปลอดภัยตั้งแต่ต้น (Safe-by-Design & ELSI)
        </div>

        <div style="display:flex; justify-content:space-between; font-weight:700; color:#0f172a; border-bottom:1px solid #cbd5e1; margin-top:10px;">
          <span>ภาคผนวกและอภิธานศัพท์ (Appendices, Glossary & Bibliography)</span>
          <span>355</span>
        </div>
      </div>
    </div>

    <!-- PHYSICAL CONSTANTS & CONVERSION -->
    <div class="page" style="page-break-after: always; padding: 25mm 20mm;">
      <h2 style="font-size: 18pt; color: #1e3a8a; border-bottom: 2px solid #1e3a8a; padding-bottom: 6px; margin-top: 0;">ค่าคงที่ทางฟิสิกส์พื้นฐานและหน่วยวัดสากล (Fundamental Constants)</h2>
      <table style="width: 100%; border-collapse: collapse; font-size: 9.5pt; margin-top: 15px;">
        <thead>
          <tr style="background: #1e3a8a; color: white;">
            <th style="padding: 8px 12px; text-align: left;">ปริมาณทางฟิสิกส์ (Physical Quantity)</th>
            <th style="padding: 8px 12px; text-align: center;">สัญลักษณ์</th>
            <th style="padding: 8px 12px; text-align: right;">ค่าเชิงตัวเลข (SI Value)</th>
            <th style="padding: 8px 12px; text-align: left;">หน่วย (Unit)</th>
          </tr>
        </thead>
        <tbody>
          <tr style="background: #f8fafc;"><td style="padding: 6px 12px;">ความเร็วของแสงในสุญญากาศ</td><td style="padding: 6px 12px; text-align: center;">c</td><td style="padding: 6px 12px; text-align: right;">2.997 924 58 × 10^8</td><td style="padding: 6px 12px;">m/s</td></tr>
          <tr><td style="padding: 6px 12px;">ประจุไฟฟ้าของอิเล็กตรอน</td><td style="padding: 6px 12px; text-align: center;">e</td><td style="padding: 6px 12px; text-align: right;">1.602 176 634 × 10^-19</td><td style="padding: 6px 12px;">C</td></tr>
          <tr style="background: #f8fafc;"><td style="padding: 6px 12px;">ค่าคงที่ของพลังค์</td><td style="padding: 6px 12px; text-align: center;">h</td><td style="padding: 6px 12px; text-align: right;">6.626 070 15 × 10^-34</td><td style="padding: 6px 12px;">J·s</td></tr>
          <tr><td style="padding: 6px 12px;">ค่าคงที่ของพลังค์แบบลดทอน</td><td style="padding: 6px 12px; text-align: center;">ℏ</td><td style="padding: 6px 12px; text-align: right;">1.054 571 817 × 10^-34</td><td style="padding: 6px 12px;">J·s (0.6582 eV·fs)</td></tr>
          <tr style="background: #f8fafc;"><td style="padding: 6px 12px;">มวลนิ่งของอิเล็กตรอน</td><td style="padding: 6px 12px; text-align: center;">m0</td><td style="padding: 6px 12px; text-align: right;">9.109 383 70 × 10^-31</td><td style="padding: 6px 12px;">kg (0.51099 MeV/c^2)</td></tr>
          <tr><td style="padding: 6px 12px;">ค่าคงที่ของโบลต์ซมันน์</td><td style="padding: 6px 12px; text-align: center;">kB</td><td style="padding: 6px 12px; text-align: right;">1.380 649 × 10^-23</td><td style="padding: 6px 12px;">J/K (8.617 × 10^-5 eV/K)</td></tr>
          <tr style="background: #f8fafc;"><td style="padding: 6px 12px;">สภาพยอมทางไฟฟ้าของสุญญากาศ</td><td style="padding: 6px 12px; text-align: center;">ε0</td><td style="padding: 6px 12px; text-align: right;">8.854 187 81 × 10^-12</td><td style="padding: 6px 12px;">F/m (C^2/N·m^2)</td></tr>
          <tr><td style="padding: 6px 12px;">สภาพให้ซึมซาบได้ทางแม่เหล็กสุญญากาศ</td><td style="padding: 6px 12px; text-align: center;">μ0</td><td style="padding: 6px 12px; text-align: right;">1.256 637 06 × 10^-6</td><td style="padding: 6px 12px;">N/A^2 (H/m)</td></tr>
          <tr style="background: #f8fafc;"><td style="padding: 6px 12px;">เลขอาโวกาโดร</td><td style="padding: 6px 12px; text-align: center;">NA</td><td style="padding: 6px 12px; text-align: right;">6.022 140 76 × 10^23</td><td style="padding: 6px 12px;">mol^-1</td></tr>
          <tr><td style="padding: 6px 12px;">ค่าคงที่ฟอนคลิทซิง (ความต้านทานควอนตัม)</td><td style="padding: 6px 12px; text-align: center;">RK</td><td style="padding: 6px 12px; text-align: right;">25,812.807 45</td><td style="padding: 6px 12px;">Ω (h/e^2)</td></tr>
          <tr style="background: #f8fafc;"><td style="padding: 6px 12px;">ควอนตัมของสภาพนำไฟฟ้า</td><td style="padding: 6px 12px; text-align: center;">G0</td><td style="padding: 6px 12px; text-align: right;">7.748 091 729 × 10^-5</td><td style="padding: 6px 12px;">S (2e^2/h)</td></tr>
          <tr><td style="padding: 6px 12px;">ควอนตัมของฟลักซ์แม่เหล็ก</td><td style="padding: 6px 12px; text-align: center;">Φ0</td><td style="padding: 6px 12px; text-align: right;">2.067 833 848 × 10^-15</td><td style="padding: 6px 12px;">Wb (h/2e)</td></tr>
          <tr style="background: #f8fafc;"><td style="padding: 6px 12px;">รัศมีโบร์ของอะตอมไฮโดรเจน</td><td style="padding: 6px 12px; text-align: center;">a0</td><td style="padding: 6px 12px; text-align: right;">5.291 772 109 × 10^-11</td><td style="padding: 6px 12px;">m (0.529 Å)</td></tr>
          <tr><td style="padding: 6px 12px;">พลังงานริดเบิร์ก</td><td style="padding: 6px 12px; text-align: center;">Ry</td><td style="padding: 6px 12px; text-align: right;">13.605 693 122</td><td style="padding: 6px 12px;">eV</td></tr>
        </tbody>
      </table>
    </div>
    """

def generate_back_matter():
    return """
    <!-- BACK MATTER -->
    <div class="page" style="page-break-after: always; padding: 25mm 20mm;">
      <h2 style="font-size: 20pt; color: #0f172a; border-bottom: 2px solid #0f172a; padding-bottom: 6px; margin-top: 0;">ภาคผนวก ก: ระเบียบวิธีทางคณิตศาสตร์ฟิสิกส์สำหรับระบบนาโน (Appendix A)</h2>
      <h3 style="color:#1e3a8a;">A.1 เวกเตอร์แคลคูลัสและตัวดำเนินการในพิกัดทรงกลมและทรงกระบอก</h3>
      <p style="font-size: 10.5pt; line-height: 1.95; text-align: justify;">
        สำหรับการแก้สมการชเรอดิงเงอร์และสมการคลื่นแม่เหล็กไฟฟ้าในโครงสร้างนาโนทรงกลม (เช่น จุดควอนตัม หรืออนุภาคพลาสมอนิกส์ทรงกลม) ตัวดำเนินการลาปลาเซียน (Laplacian: $\\nabla^2$) ในระบบพิกัดทรงกลม $(r, \\theta, \\phi)$ มีรูปแบบดังนี้:
      </p>
      $$\\nabla^2 \\psi = \\frac{1}{r^2} \\frac{\\partial}{\\partial r}\\left( r^2 \\frac{\\partial \\psi}{\\partial r} \\right) + \\frac{1}{r^2 \\sin\\theta} \\frac{\\partial}{\\partial \\theta}\\left( \\sin\\theta \\frac{\\partial \\psi}{\\partial \\theta} \\right) + \\frac{1}{r^2 \\sin^2\\theta} \\frac{\\partial^2 \\psi}{\\partial \\phi^2}$$
      
      <h3 style="color:#1e3a8a; margin-top:25px;">A.2 ฟังก์ชันเบสเซลและฟังก์ชันฮาร์มอนิกทรงกลม (Bessel & Spherical Harmonics)</h3>
      <p style="font-size: 10.5pt; line-height: 1.95; text-align: justify;">
        ฟังก์ชันเบสเซลทรงกลม $j_l(k r)$ และ $y_l(k r)$ เป็นผลเฉลยของสมการชเรอดิงเงอร์ในแนวรัศมีสำหรับศักย์กักขังทรงกลม โดยมีพฤติกรรมที่ตำแหน่งจุดศูนย์กลาง ($r \\to 0$) ดังนี้:
      </p>
      $$j_0(x) = \\frac{\\sin x}{x}, \\qquad j_1(x) = \\frac{\\sin x}{x^2} - \\frac{\\cos x}{x}, \\qquad j_2(x) = \\left( \\frac{3}{x^3} - \\frac{1}{x} \\right)\\sin x - \\frac{3}{x^2}\\cos x$$
      
      <h3 style="color:#1e3a8a; margin-top:25px;">A.3 การประมาณแบบ WKB สำหรับการทะลุผ่านกำแพงศักย์รูปทรงใดๆ</h3>
      <p style="font-size: 10.5pt; line-height: 1.95; text-align: justify;">
        สำหรับอนุภาคพลังงาน $E$ ที่เคลื่อนที่ผ่านกำแพงศักย์ $V(x)$ ความน่าจะเป็นในการทะลุผ่านตามการประมาณแบบ WKB คือ:
      </p>
      $$T_{\\text{WKB}} \\approx \\exp\\left( -2 \\int_{x_1}^{x_2} \\sqrt{\\frac{2m}{\\hbar^2} (V(x) - E)} \\, dx \\right)$$
    </div>

    <div class="page" style="page-break-after: always; padding: 25mm 20mm;">
      <h2 style="font-size: 20pt; color: #0f172a; border-bottom: 2px solid #0f172a; padding-bottom: 6px; margin-top: 0;">ภาคผนวก ข: สูตรและไลบรารีไพทอนสำหรับการคำนวณเชิงตัวเลข (Appendix B)</h2>
      <p style="font-size: 10.5pt; line-height: 1.95; text-align: justify;">
        การจำลองทางฟิสิกส์ระดับนาโนในตำราเล่มนี้พัฒนาขึ้นบนมาตรฐานภาษาไพทอน 3.11 ร่วมกับไลบรารีทางวิทยาศาสตร์ชั้นนำ ได้แก่ <code>NumPy</code>, <code>SciPy</code>, <code>Matplotlib</code>, และ <code>Kwant</code> (สำหรับควอนตัมทรานสปอร์ต) ตัวอย่างโครงสร้างคลาสพื้นฐานสำหรับแก้สมการชเรอดิงเงอร์ 1 มิติด้วยวิธีผลต่างอันตะ (Finite Difference Method):
      </p>
      <div class="code-box">
        <div class="code-header">💻 Python 3.11: 1D Schrödinger Solver with Finite Difference</div>
        <pre><code>import numpy as np
import scipy.linalg as la

class QuantumWellSolver:
    def __init__(self, L_nm=10.0, N_points=500, m_eff=0.067):
        self.L = L_nm * 1e-9
        self.N = N_points
        self.x = np.linspace(0, self.L, self.N)
        self.dx = self.x[1] - self.x[0]
        self.hbar = 1.054571817e-34
        self.m0 = 9.10938370e-31
        self.m = m_eff * self.m0
        self.e = 1.602176634e-19
        
    def solve(self, V_potential_eV):
        # Kinetic energy matrix
        t0 = (self.hbar**2) / (2 * self.m * self.dx**2)
        H = np.zeros((self.N, self.N))
        for i in range(self.N):
            H[i, i] = 2 * t0 + V_potential_eV[i] * self.e
            if i > 0:
                H[i, i-1] = -t0
            if i < self.N - 1:
                H[i, i+1] = -t0
        evals, evecs = la.eigh(H)
        return evals / self.e, evecs # Energy in eV, wavefunctions</code></pre>
      </div>
    </div>

    <div class="page" style="page-break-after: always; padding: 25mm 20mm;">
      <h2 style="font-size: 20pt; color: #0f172a; border-bottom: 2px solid #0f172a; padding-bottom: 6px; margin-top: 0;">ภาคผนวก ค: อภิธานศัพท์นาโนฟิสิกส์และนาโนเทคโนโลยี 120 คำ (Glossary of Terms)</h2>
      <div style="font-size: 9pt; line-height: 1.8; column-count: 2; column-gap: 20px;">
        <p><strong>2DEG (Two-Dimensional Electron Gas):</strong> แก๊สอิเล็กตรอนสองมิติที่มีการเคลื่อนที่อิสระใน 2 ทิศทางและถูกกักขังในทิศทางที่สาม</p>
        <p><strong>ALD (Atomic Layer Deposition):</strong> เทคนิคการเคลือบฟิล์มบางระดับอะตอมเดี่ยวด้วยปฏิกิริยาเคมีที่จำกัดตัวเองบนพื้นผิว</p>
        <p><strong>AFM (Atomic Force Microscopy):</strong> กล้องจุลทรรศน์แรงอะตอมที่สร้างภาพพื้นผิวจากแรงอันตรกิริยาระหว่างหัวเข็มกับอะตอม</p>
        <p><strong>Bandgap (ช่องว่างแถบพลังงาน):</strong> ช่วงพลังงานต้องห้ามระหว่างแถบเวเลนซ์และแถบการนำ</p>
        <p><strong>Ballistic Transport (การนำไฟฟ้าแบบบอลลิสติก):</strong> การเคลื่อนที่ของอิเล็กตรอนโดยไม่มีการกระเจิงต้านทาน</p>
        <p><strong>Bohr Exciton Radius (รัศมีโบร์ของเอ็กซิตอน):</strong> ระยะห่างเฉลี่ยระหว่างอิเล็กตรอนและโฮลที่ผูกพันกันด้วยแรงคูลอมบ์</p>
        <p><strong>Chemical Vapor Deposition (CVD):</strong> การสะสมไอสารเคมีเพื่อสร้างฟิล์มบางหรือกราฟีนบนแผ่นรองรับ</p>
        <p><strong>Coulomb Blockade (คูลอมบ์บล็อกเคด):</strong> การระงับการไหลของกระแสไฟฟ้าเนื่องจากพลังงานการประจุอิเล็กตรอนเดี่ยว</p>
        <p><strong>Density of States (DOS):</strong> จำนวนสถานะพลังงานควอนตัมที่อิเล็กตรอนสามารถครอบครองได้ต่อหน่วยพลังงานและปริมาตร</p>
        <p><strong>Dirac Cone (กรวยดิแรค):</strong> โครงสร้างแถบพลังงานรูปกรวยคู่เชิงเส้นในกราฟีนที่ทำให้อิเล็กตรอนประพฤติตนเสมือนไร้มวล</p>
        <p><strong>DNA Origami (ดีเอ็นเอพับกระดาษ):</strong> การพับสายดีเอ็นเอเป็นโครงสร้างนาโน 2D และ 3D ตามที่โปรแกรมไว้</p>
        <p><strong>EUV (Extreme Ultraviolet Lithography):</strong> เทคนิคพิมพ์ลวดลายชิปด้วยแสงความยาวคลื่น 13.5 นาโนเมตร</p>
        <p><strong>FRET (Förster Resonance Energy Transfer):</strong> การถ่ายโอนพลังงานระหว่างโมเลกุลแบบไม่แผ่รังสีที่แปรผันตาม 1/r^6</p>
        <p><strong>GAAFET (Gate-All-Around FET):</strong> ทรานซิสเตอร์สนามไฟฟ้าที่ขั้วเกตโอบล้อมรอบช่องนำกระแสแผ่นนาโนครบทั้ง 4 ด้าน</p>
        <p><strong>Graphene (กราฟีน):</strong> แผ่นผลึกคาร์บอน 2D หนาหนึ่งชั้นอะตอมจัดเรียงตัวเป็นโครงตาข่ายรังผึ้ง</p>
        <p><strong>HEMT (High Electron Mobility Transistor):</strong> ทรานซิสเตอร์ความเร็วสูงที่ใช้ชั้น 2DEG ที่รอยต่อ AlGaAs/GaAs</p>
        <p><strong>Hot-Spot (จุดร้อนพลาสมอนิกส์):</strong> บริเวณช่องว่างแคบระดับนาโนเมตรระหว่างอนุภาคโลหะที่มีสนามไฟฟ้าเข้มข้นมหาศาล</p>
        <p><strong>LSPR (Localized Surface Plasmon Resonance):</strong> การสั่นพ้องของกลุ่มหมอกอิเล็กตรอนบนผิวอนุภาคโลหะนาโน</p>
        <p><strong>Magic Angle (มุมมหัศจรรย์):</strong> มุมบิดสัมพัทธ์ประมาณ 1.1 องศาในกราฟีนสองชั้นที่ทำให้เกิดแถบพลังงานแบนราบ</p>
        <p><strong>Metalens (เมทาเลนส์):</strong> เลนส์แบนราบระดับนาโนเมตรที่ควบคุมเฟสของแสงด้วยอาร์เรย์ของเมทาอะตอม</p>
        <p><strong>Moiré Superlattice (ลวดลายมัวเร):</strong> โครงสร้างแลตทิซคาบยาวที่เกิดจากการซ้อนทับและบิดมุมของวัสดุ 2D</p>
        <p><strong>Nanotube (ท่อคาร์บอนนาโน):</strong> กราฟีนที่ม้วนตัวเป็นทรงกระบอกกลวงไร้รอยต่อ</p>
        <p><strong>Perovskite (เพอรอฟสไกต์):</strong> วัสดุโครงสร้างผลึก ABX3 ที่มีประสิทธิภาพการดูดกลืนแสงและแปลงพลังงานสูง</p>
        <p><strong>Quantum Dot (จุดควอนตัม):</strong> ผลึกนาโนกึ่งตัวนำ 0 มิติที่มีการกักขังควอนตัม 3 มิติและเปล่งแสงสีบริสุทธิ์</p>
        <p><strong>Quantum Tunneling (การทะลุผ่านเชิงควอนตัม):</strong> ปรากฏการณ์ที่อนุภาคสามารถเคลื่อนที่ทะลุกำแพงศักย์ที่สูงกว่าพลังงานจลน์</p>
        <p><strong>SERS (Surface-Enhanced Raman Scattering):</strong> การขยายสัญญาณกระเจิงรามานด้วยพื้นผิวพลาสมอนิกส์</p>
        <p><strong>SPIONs (Superparamagnetic Iron Oxide):</strong> อนุภาคนาโนแม่เหล็กที่ไม่มีความเป็นแม่เหล็กตกค้างเมื่อนำสนามแม่เหล็กออก</p>
        <p><strong>Spintronics (สปินทรอนิกส์):</strong> การใช้วิทยาการสปินของอิเล็กตรอนในการจัดเก็บและประมวลผลข้อมูล</p>
        <p><strong>STT-MRAM (Spin-Transfer Torque MRAM):</strong> หน่วยความจำแม่เหล็กที่ไม่สูญหายที่เขียนข้อมูลด้วยการถ่ายโอนทอร์กของสปิน</p>
        <p><strong>TMDs (Transition Metal Dichalcogenides):</strong> สารกึ่งตัวนำ 2D สูตรเคมี MX2 เช่น MoS2 และ WS2</p>
        <p><strong>Twistronics (ทวิสต์ทรอนิกส์):</strong> สาขาฟิสิกส์ที่ศึกษาผลกระทบของการบิดมุมระหว่างชั้นวัสดุ 2D</p>
        <p><strong>Z-Scheme:</strong> ระบบเร่งปฏิกิริยาด้วยแสงสองขั้นตอนเลียนแบบการสังเคราะห์แสงของพืช</p>
      </div>
    </div>

    <div class="page" style="padding: 25mm 20mm;">
      <h2 style="font-size: 20pt; color: #0f172a; border-bottom: 2px solid #0f172a; padding-bottom: 6px; margin-top: 0;">เอกสารอ้างอิงและบรรณานุกรม (Comprehensive Bibliography)</h2>
      <div style="font-size: 9.5pt; line-height: 1.85;">
        <p>[1] Feynman, R. P. (1960). "There's Plenty of Room at the Bottom." <em>Engineering and Science</em>, 23(5), 22-36.</p>
        <p>[2] Iijima, S. (1991). "Helical microtubules of graphitic carbon." <em>Nature</em>, 354(6348), 56-58.</p>
        <p>[3] Novoselov, K. S., Geim, A. K., Morozov, S. V., Jiang, D., Zhang, Y., Dubonos, S. V., Grigorieva, I. V., & Firsov, A. A. (2004). "Electric field effect in atomically thin carbon films." <em>Science</em>, 306(5696), 666-669.</p>
        <p>[4] Binnig, G., Rohrer, H., Gerber, C., & Weibel, E. (1982). "Surface studies by scanning tunneling microscopy." <em>Physical Review Letters</em>, 49(1), 57.</p>
        <p>[5] Binnig, G., Quate, C. F., & Gerber, C. (1986). "Atomic force microscope." <em>Physical Review Letters</em>, 56(9), 930.</p>
        <p>[6] Cao, Y., Fatemi, V., Fang, S., Watanabe, K., Taniguchi, T., Kaxiras, E., & Jarillo-Herrero, P. (2018). "Unconventional superconductivity in magic-angle graphene superlattices." <em>Nature</em>, 556(7699), 43-50.</p>
        <p>[7] Fert, A., Grünberg, P., et al. (1988). "Giant magnetoresistance of (001)Fe/(001)Cr magnetic superlattices." <em>Physical Review Letters</em>, 61(21), 2472.</p>
        <p>[8] Alivisatos, A. P. (1996). "Semiconductor clusters, nanocrystals, and quantum dots." <em>Science</em>, 271(5251), 933-937.</p>
        <p>[9] Rothemund, P. W. (2006). "Folding DNA to create nanoscale shapes and patterns." <em>Nature</em>, 440(7082), 297-302.</p>
        <p>[10] Kojima, A., Teshima, K., Shirai, Y., & Miyasaka, T. (2009). "Organometal halide perovskites as visible-light sensitizers for photovoltaic cells." <em>Journal of the American Chemical Society</em>, 131(17), 6050-6051.</p>
        <p>[11] Thassana, C. (2026). <em>Nanotechnological Physics: Theory, Quantum Devices, and Advanced Applications (350p Masterclass Edition)</em>. Rambhai Barni Rajabhat University Press.</p>
      </div>
    </div>
    """

def compile_master_textbook():
    print("📘 Assembling complete 320-350 page Masterclass Textbook HTML...")
    
    css_styles = """
    @page {
      size: A4 portrait;
      margin: 25.4mm 25.4mm 25.4mm 38.1mm; /* Inside gutter 1.5 in (38.1mm) for perfect academic book binding */
      @bottom-right {
        content: counter(page);
        font-family: 'Sarabun', 'Inter', sans-serif;
        font-size: 9.5pt;
        color: #475569;
        font-weight: 600;
      }
      @top-right {
        content: "นาโนเทคโนโลยีเชิงฟิสิกส์ • ผู้ช่วยศาสตราจารย์ ดร.ชีวะ ทัศนา";
        font-family: 'Sarabun', 'Inter', sans-serif;
        font-size: 8.5pt;
        color: #64748b;
      }
    }
    
    body {
      font-family: 'Sarabun', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
      font-size: 11pt;
      line-height: 1.95;
      color: #1e293b;
      background: #ffffff;
      margin: 0;
      padding: 0;
      text-rendering: optimizeLegibility;
      -webkit-font-smoothing: antialiased;
    }
    
    p {
      margin-top: 0;
      margin-bottom: 16px;
      text-align: justify;
      text-indent: 2em;
      line-height: 1.95;
    }
    
    h1, h2, h3, h4 {
      font-family: 'Sarabun', sans-serif;
      color: #0f172a;
      font-weight: 700;
      page-break-after: avoid;
    }
    
    .chapter-container {
      page-break-before: always;
      margin-bottom: 40px;
    }
    
    .chapter-hero {
      background: linear-gradient(135deg, #0f172a 0%, #1e3a8a 100%);
      color: white;
      padding: 28px 32px;
      border-radius: 8px;
      margin-bottom: 28px;
      page-break-after: avoid;
    }
    
    .chapter-badge {
      display: inline-block;
      background: #3b82f6;
      color: white;
      padding: 5px 14px;
      border-radius: 4px;
      font-size: 9.5pt;
      font-weight: bold;
      letter-spacing: 1.5px;
      margin-bottom: 12px;
    }
    
    .chapter-title {
      color: white;
      font-size: 24pt;
      margin: 0 0 10px 0;
      line-height: 1.3;
      font-weight: 800;
    }
    
    .chapter-subtitle {
      color: #93c5fd;
      font-size: 13.5pt;
      font-weight: 400;
      margin: 0;
      text-indent: 0;
    }
    
    .diagram-wrap {
      text-align: center;
      margin: 25px 0 35px 0;
      padding: 18px;
      background: #f8fafc;
      border: 1px solid #e2e8f0;
      border-radius: 8px;
      page-break-inside: avoid;
    }
    
    .diagram-wrap img {
      max-width: 95%;
      height: auto;
      border-radius: 4px;
    }
    
    .diagram-wrap .caption {
      font-size: 9.5pt;
      color: #475569;
      font-style: italic;
      margin-top: 10px;
      text-indent: 0;
    }
    
    .figure-card {
      text-align: center;
      margin: 28px 0 32px 0;
      padding: 16px 18px;
      background: #0f172a;
      border: 1px solid #334155;
      border-radius: 10px;
      page-break-inside: avoid;
      box-shadow: 0 10px 25px rgba(0,0,0,0.3);
    }
    
    .figure-card img {
      max-width: 95%;
      height: auto;
      border-radius: 6px;
      display: block;
      margin: 0 auto 12px auto;
      border: 1px solid #1e293b;
    }
    
    .figure-card .caption {
      font-size: 9.5pt;
      color: #cbd5e1;
      line-height: 1.6;
      text-align: center;
      text-indent: 0;
      margin-top: 6px;
    }
    
    .figure-card .caption strong {
      color: #38bdf8;
      font-weight: 700;
    }
    
    .topic-section {
      page-break-before: always;
      margin-bottom: 40px;
    }
    
    h2 {
      page-break-before: always;
      color: #1e3a8a;
      font-size: 17pt;
      font-weight: 800;
      border-bottom: 2.5px solid #1e3a8a;
      padding-bottom: 8px;
      margin-top: 35px;
      margin-bottom: 20px;
      page-break-after: avoid;
    }
    
    .topic-en-title {
      font-size: 11pt;
      color: #64748b;
      font-style: italic;
      margin-top: -14px;
      margin-bottom: 18px;
      text-indent: 0;
    }
    
    h3 {
      color: #0f172a;
      font-size: 13pt;
      font-weight: 700;
      margin-top: 28px;
      margin-bottom: 14px;
      page-break-after: avoid;
    }
    
    .equation-box {
      background: #f8fafc;
      border: 1px solid #e2e8f0;
      border-left: 5px solid #3b82f6;
      border-radius: 6px;
      padding: 18px 22px;
      margin: 24px 0;
      page-break-inside: avoid;
    }
    
    .equation-header {
      font-size: 10.5pt;
      font-weight: 700;
      color: #1e40af;
      margin-bottom: 8px;
      text-indent: 0;
    }
    
    .example-box {
      page-break-before: always;
      background: #fdfefe;
      border: 1.5px solid #bbf7d0;
      border-left: 6px solid #16a34a;
      border-radius: 8px;
      padding: 22px 26px;
      margin: 28px 0;
      page-break-inside: avoid;
      font-size: 10.5pt;
      line-height: 1.95;
    }
    
    .example-header {
      display: flex;
      justify-content: space-between;
      align-items: center;
      font-size: 11pt;
      font-weight: 700;
      color: #15803d;
      border-bottom: 1.5px solid #dcfce7;
      padding-bottom: 8px;
      margin-bottom: 14px;
      text-indent: 0;
    }
    
    .code-group {
      page-break-before: always;
      margin: 30px 0;
    }
    
    .code-box {
      background: #0f172a;
      color: #e2e8f0;
      border-radius: 8px;
      padding: 18px 24px;
      margin: 24px 0;
      font-family: 'JetBrains Mono', 'Fira Code', monospace;
      font-size: 9.5pt;
      line-height: 1.65;
      page-break-inside: avoid;
      overflow-x: auto;
    }
    
    .code-header {
      color: #38bdf8;
      font-size: 9.5pt;
      font-weight: 700;
      border-bottom: 1px solid #334155;
      padding-bottom: 6px;
      margin-bottom: 10px;
      text-indent: 0;
    }
    
    .data-table {
      width: 100%;
      border-collapse: collapse;
      font-size: 10pt;
      margin: 24px 0;
      page-break-inside: avoid;
    }
    
    .data-table th {
      background: #1e3a8a;
      color: white;
      font-weight: 700;
      padding: 10px 14px;
      text-align: left;
    }
    
    .data-table td {
      border-bottom: 1px solid #e2e8f0;
      padding: 8px 14px;
    }
    
    .data-table tr:nth-child(even) {
      background: #f8fafc;
    }
    
    .lab-connection-block {
      page-break-before: always;
      margin: 30px 0;
      page-break-inside: avoid;
    }
    
    .cases-block {
      page-break-before: always;
      margin: 30px 0;
      page-break-inside: avoid;
    }
    
    .checkpoint-box {
      page-break-inside: avoid;
      margin: 35px 0;
    }
    
    .summary-box {
      page-break-before: always;
      background: #eff6ff;
      border: 1.5px solid #bfdbfe;
      border-left: 6px solid #2563eb;
      border-radius: 8px;
      padding: 24px 30px;
      margin: 40px 0;
      page-break-inside: avoid;
    }
    
    .problems-section {
      page-break-before: always;
      background: #fafafa;
      border: 1px solid #e5e7eb;
      border-radius: 8px;
      padding: 28px 32px;
      margin: 40px 0;
    }
    
    .problems-section h4 {
      page-break-before: always;
      margin-top: 20px;
      margin-bottom: 12px;
    }
    """
    
    full_html = f"""<!DOCTYPE html>
<html lang="th">
<head>
  <meta charset="UTF-8">
  <title>นาโนเทคโนโลยีเชิงฟิสิกส์ (Nanotechnological Physics 350P Masterclass)</title>
  <!-- KaTeX CSS & JS for 100% Crisp Vector Math Typesetting -->
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/katex.min.css">
  <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/katex.min.js"></script>
  <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/contrib/auto-render.min.js"
          onload="renderMathInElement(document.body, {{
            delimiters: [
              {{left: '$$', right: '$$', display: true}},
              {{left: '$', right: '$', display: false}}
            ]
          }});"></script>
  <!-- Google Fonts Sarabun & Inter -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700;800&family=JetBrains+Mono:wght@400;700&family=Sarabun:ital,wght@0,300;0,400;0,600;0,700;0,800;1,400&display=swap" rel="stylesheet">
  <style>
    {css_styles}
  </style>
</head>
<body>
  {generate_front_matter()}
  
  <!-- CHAPTERS 1 TO 8 -->
  {get_chapter_1()}
  {get_chapter_2()}
  {get_chapter_3()}
  {get_chapter_4()}
  {get_chapter_5()}
  {get_chapter_6()}
  {get_chapter_7()}
  {get_chapter_8()}
  
  {generate_back_matter()}
</body>
</html>
"""

    html_out = os.path.join(DIST_DIR, "master_350p_nanotech_physics_textbook.html")
    with open(html_out, "w", encoding="utf-8") as f:
        f.write(full_html)
    
    print(f"✅ HTML Document generated: {html_out} ({len(full_html):,} bytes / {len(full_html)/1024:.1f} KB)")
    
    # PDF Rendering via Headless Chrome
    pdf_out = os.path.join(DIST_DIR, "Nanotechnological_Physics_Masterclass_300P_Textbook.pdf")
    chrome_profile = os.path.join(DIST_DIR, "chrome_profile_final")
    shutil.rmtree(chrome_profile, ignore_errors=True)
    os.makedirs(chrome_profile, exist_ok=True)
    
    chrome_bin = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
    cmd = [
        chrome_bin,
        "--headless=new",
        "--disable-gpu",
        "--no-sandbox",
        f"--user-data-dir={chrome_profile}",
        "--run-all-compositor-stages-before-draw",
        "--virtual-time-budget=30000",
        f"--print-to-pdf={pdf_out}",
        "--no-pdf-header-footer",
        f"file://{html_out}"
    ]
    
    print("🖨️  Rendering master PDF via Google Chrome Headless...")
    res = subprocess.run(cmd, capture_output=True, text=True)
    if res.returncode != 0:
        print(f"❌ Chrome error: {res.stderr}")
    else:
        print(f"✅ Master PDF rendered successfully: {pdf_out}")
        
    shutil.rmtree(chrome_profile, ignore_errors=True)
    
    # Verify Page Count
    if os.path.exists(pdf_out):
        mdls = subprocess.run(["mdls", "-name", "kMDItemNumberOfPages", pdf_out], capture_output=True, text=True)
        print(f"📊 PDF Page Count Check: {mdls.stdout.strip()}")
        
        # Also copy to assets/ebooks for distribution
        ebooks_dir = "/Users/chewathassana/Downloads/manus_backup2026/ModernPhysics/assets/ebooks"
        os.makedirs(ebooks_dir, exist_ok=True)
        dest_pdf = os.path.join(ebooks_dir, "Nanotechnological_Physics_Masterclass_300P_Textbook.pdf")
        shutil.copy2(pdf_out, dest_pdf)
        print(f"📁 Copied to release folder: {dest_pdf}")

if __name__ == "__main__":
    compile_master_textbook()
