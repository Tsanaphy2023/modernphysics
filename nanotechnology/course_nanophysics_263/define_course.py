#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Defines the complete 8-Chapter, 40-Subtopic curriculum structure for
รายวิชา 4014971 นาโนเทคโนโลยีเชิงฟิสิกส์ (Nanotechnological Physics)
Course ID: 263 on RBRU MOOC (elearning.rbru.ac.th).
"""

import json
import os

COURSE_DATA = [
    {
        "id": 1,
        "title": "บทที่ 1 พื้นฐานนาโนฟิสิกส์และการคิดเชิงมาตราส่วน",
        "description": "ศึกษาประวัติศาสตร์ นิยาม และขอบเขตของมิติระดับนาโนเมตร (1-100 nm) กฎการแปลงมาตราส่วน (Scaling Laws) อัตราส่วนพื้นที่ผิวต่อปริมาตร พลังงานพื้นผิว จลนศาสตร์การเกาะกลุ่ม และการอ่านสเกลบาร์ภาพถ่ายกล้องจุลทรรศน์",
        "pages": [
            {
                "id": "1.1",
                "title": "1.1 มิติและมาตราส่วนระดับนาโน (Nanoscale Dimensions & Scaling Laws)",
                "summary": "ความหมายของระดับ 1–100 นาโนเมตร การเปรียบเทียบขนาดอะตอม โมเลกุล ไวรัส และเซลล์ พร้อมกฎการลดขนาดเชิงฟิสิกส์",
                "sim_type": "scale_comparison_3d",
                "formula": "1\\text{ nm} = 10^{-9}\\text{ m} = 10\\text{ \\AA}"
            },
            {
                "id": "1.2",
                "title": "1.2 สัดส่วนพื้นที่ผิวต่อปริมาตรและผลกระทบเชิงกายภาพ (Surface-to-Volume Ratio)",
                "summary": "การคำนวณอัตราส่วนพื้นที่ผิวต่อปริมาตรของอนุภาคทรงกลมและลูกบาศก์ และอิทธิพลต่อความว่องไวในการเกิดปฏิกิริยา",
                "sim_type": "surface_volume_calc",
                "formula": "\\frac{A}{V} = \\frac{6}{d} = \\frac{3}{R}"
            },
            {
                "id": "1.3",
                "title": "1.3 พลังงานพื้นผิวและพฤติกรรมการเกาะกลุ่มของอนุภาคนาโน (Surface Energy & Agglomeration)",
                "summary": "พลังงานอิสระที่ผิว ความไม่เสถียรทางเทอร์โมไดนามิกส์ แรงแวนเดอร์วาลส์ และกลไกการกระจายตัวของคอลลอยด์",
                "sim_type": "surface_energy_sim",
                "formula": "\\Delta G = \\gamma \\Delta A - T \\Delta S < 0"
            },
            {
                "id": "1.4",
                "title": "1.4 การอ่านสเกลบาร์และการวิเคราะห์ภาพกล้องจุลทรรศน์ (Scale Bar Metrology)",
                "summary": "เทคนิคการวัดขนาดอนุภาค การปรับเทียบกำลังขยาย และการสร้างฮิสโตแกรมการกระจายตัวของขนาดจากภาพ SEM/TEM",
                "sim_type": "scalebar_analyzer",
                "formula": "\\text{Actual Size} = \\frac{\\text{Measured Pixels}}{\\text{Scale Pixels}} \\times \\text{Scale Unit}"
            },
            {
                "id": "1.5",
                "title": "1.5 แบบฝึกหัดและปฏิบัติการจำลอง AR: พื้นที่ผิวและมาตราส่วนนาโน",
                "summary": "สรุปเนื้อหาหลัก ทำแบบทดสอบวัดผลสัมฤทธิ์ และทดลองปรับขนาดอนุภาคผ่านระบบตรวจจับท่าทางมือ AR MediaPipe",
                "sim_type": "ar_scale_lab",
                "formula": "D_{\\text{eff}} = \\left( \\frac{6}{\\rho S_{\\text{BET}}} \\right)"
            }
        ]
    },
    {
        "id": 2,
        "title": "บทที่ 2 สมบัติขึ้นกับขนาดและการกักขังเชิงควอนตัม",
        "description": "สำรวจฟิสิกส์ควอนตัมในมิตินาโน ปรากฏการณ์กักขังเชิงควอนตัม (Quantum Confinement) แบบจำลอง Brus อนุภาคควอนตัมดอท การสั่นพลาสมอนพื้นผิวเฉพาะที่ (LSPR) และสมบัติแม่เหล็กยิ่งยวด (Superparamagnetism)",
        "pages": [
            {
                "id": "2.1",
                "title": "2.1 ปรากฏการณ์การกักขังเชิงควอนตัมและแบบจำลอง Brus (Quantum Confinement & Brus Model)",
                "summary": "การเปลี่ยนแปลงของช่องว่างแถบพลังงาน (Band Gap) ตามขนาดอนุภาค และการจำลองศักย์หลุมทรงกลม 3 มิติ",
                "sim_type": "brus_model_sim",
                "formula": "E_g(R) = E_g^{\\text{bulk}} + \\frac{\\hbar^2 \\pi^2}{2 m_0^* R^2} - \\frac{1.786 e^2}{4\\pi\\varepsilon R}"
            },
            {
                "id": "2.2",
                "title": "2.2 อนุภาคควอนตัมดอทและสเปกตรัมการดูดกลืนและการคายแสง (Quantum Dots Photoluminescence)",
                "summary": "ฟิสิกส์ของสารกึ่งตัวนำขนาดนาโน การเรืองแสงที่ปรับค่าได้ตามขนาด การประยุกต์ใช้ในหลอด QLED และไบโออิมเมจจิ้ง",
                "sim_type": "qd_spectrum_sim",
                "formula": "\\lambda_{\\text{emission}} = \\frac{hc}{E_g(R)}"
            },
            {
                "id": "2.3",
                "title": "2.3 การสั่นพลาสมอนพื้นผิวเฉพาะที่ (Localized Surface Plasmon Resonance - LSPR)",
                "summary": "การสั่นพ้องของกลุ่มอิเล็กตรอนอิสระบนผิวโลหะนาโน (ทอง/เงิน) เมื่อถูกกระตุ้นด้วยแสง และการดูดกลืนแสงสีเฉพาะ",
                "sim_type": "lspr_plasmon_sim",
                "formula": "\\omega_{\\text{sp}} = \\frac{\\omega_p}{\\sqrt{1 + 2\\varepsilon_m}}"
            },
            {
                "id": "2.4",
                "title": "2.4 สภาพนำไฟฟ้าควอนไทซ์และสมบัติแม่เหล็กยิ่งยวด (Quantized Conductance & Superparamagnetism)",
                "summary": "การนำส่งกระแสแบบบัลลิสติก สูตร Landauer และการกลับทิศโมเมนต์แม่เหล็กด้วยความร้อนในโดเมนเดี่ยว",
                "sim_type": "superparamagnet_sim",
                "formula": "G = \\frac{2e^2}{h} \\sum_{n} T_n, \\quad \\tau = \\tau_0 \\exp\\left(\\frac{KV}{k_B T}\\right)"
            },
            {
                "id": "2.5",
                "title": "2.5 แบบฝึกหัดและปฏิบัติการจำลอง AR: สเปกตรัมควอนตัมดอทและ LSPR",
                "summary": "วิเคราะห์แถบแสงและทดลองสังเคราะห์ควอนตัมดอทเสมือนจริง ควบคุมแสงเลเซอร์ด้วยมือเปล่าผ่าน AR Camera",
                "sim_type": "ar_quantum_dot_lab",
                "formula": "I(\\lambda) = I_0 \\exp(-\\alpha(\\lambda) L)"
            }
        ]
    },
    {
        "id": 3,
        "title": "บทที่ 3 วิศวกรรมการสังเคราะห์และสร้างสรรค์วัสดุนาโน",
        "description": "เปรียบเทียบแนวคิด Top-Down vs Bottom-Up การสังเคราะห์ทางเคมีสารละลาย Sol-Gel ไฮโดรเทอร์มอล กระบวนการสะสมไอเคมีและกายภาพ (CVD/PVD) นาโนลิโทกราฟี และการประกอบตัวเองระดับโมเลกุล",
        "pages": [
            {
                "id": "3.1",
                "title": "3.1 แนวทางการสังเคราะห์แบบล่างขึ้นบนและบนลงล่าง (Bottom-up vs Top-down Synthesis)",
                "summary": "ข้อได้เปรียบ ข้อจำกัด ต้นทุน และความแม่นยำของการบดลดขนาดเทียบกับการสังเคราะห์จากอะตอมและโมเลกุล",
                "sim_type": "synthesis_pathway_sim",
                "formula": "\\text{Yield} = f(T, P, \\text{Precursor}, \\text{Catalyst})"
            },
            {
                "id": "3.2",
                "title": "3.2 กระบวนการโซล-เจลและเคมีสารละลาย (Sol-Gel Process & Solution Chemistry)",
                "summary": "ปฏิกิริยาไฮโดรไลซิสและการควบแน่นของแอลคอกไซด์ การเกิดโครงตาข่ายซิลิกาและการควบคุมขนาดรูพรุน",
                "sim_type": "sol_gel_reaction_sim",
                "formula": "\\equiv\\!\\text{Si-OR} + \\text{H}_2\\text{O} \\to \\,\\equiv\\!\\text{Si-OH} + \\text{ROH}"
            },
            {
                "id": "3.3",
                "title": "3.3 การสะสมไอสารเคมีและไอสารกายภาพ (CVD & PVD Thin Film Growth)",
                "summary": "หลักการ Thermal CVD, Plasma Enhanced CVD, Sputtering และการปลูกฟิล์มกราฟีน/โครงสร้างผลึกเดี่ยว",
                "sim_type": "cvd_growth_sim",
                "formula": "r_{\\text{growth}} = k_0 P_{\\text{gas}} \\exp\\left(-\\frac{E_a}{k_B T}\\right)"
            },
            {
                "id": "3.4",
                "title": "3.4 นาโนลิโทกราฟีและการสร้างลวดลายระดับนาโน (Nanolithography & Patterning)",
                "summary": "โฟโตลิโทกราฟีรังสีเอกซ์ตรีมยูวี (EUV) ลิโทกราฟีลำอิเล็กตรอน (E-beam) และนาโนอิมพรินต์",
                "sim_type": "lithography_resolution_sim",
                "formula": "R = k_1 \\frac{\\lambda}{\\text{NA}}, \\quad \\text{DOF} = k_2 \\frac{\\lambda}{\\text{NA}^2}"
            },
            {
                "id": "3.5",
                "title": "3.5 แบบฝึกหัดและปฏิบัติการจำลอง AR: การสังเคราะห์และควบคุมขนาดอนุภาค",
                "summary": "ทดลองปรับอุณหภูมิและอัตราการไหลของก๊าซในเตาปฏิกรณ์จำลอง CVD 3D ด้วยระบบท่าทางมือ AR",
                "sim_type": "ar_synthesis_lab",
                "formula": "\\Delta G_{\\text{crit}} = \\frac{16\\pi \\gamma^3}{3 (\\Delta G_v)^2}"
            }
        ]
    },
    {
        "id": 4,
        "title": "บทที่ 4 มาตรวิทยาและเครื่องมือวิเคราะห์ระดับอะตอม",
        "description": "เจาะลึกเครื่องมือวิเคราะห์ทางนาโนศาสตร์ กล้องจุลทรรศน์อิเล็กตรอน SEM / TEM / STEM กล้องจุลทรรศน์โพรบสแกน AFM / STM การเลี้ยวเบนรังสีเอกซ์ (XRD & Scherrer Formula) และการวัดขนาดอนุภาค DLS / Zeta Potential",
        "pages": [
            {
                "id": "4.1",
                "title": "4.1 กล้องจุลทรรศน์อิเล็กตรอนแบบส่องกราดและส่องผ่าน (SEM & TEM Metrology)",
                "summary": "อันตรกิริยาระหว่างลำอิเล็กตรอนกับตัวอย่าง อิเล็กตรอนทุติยภูมิ (SE) อิเล็กตรอนสะท้อนกลับ (BSE) และภาพโครงสร้างผลึก TEM",
                "sim_type": "electron_microscopy_sim",
                "formula": "\\lambda_e = \\frac{h}{\\sqrt{2 m_0 e V \\left(1 + \\frac{eV}{2m_0 c^2}\\right)}}"
            },
            {
                "id": "4.2",
                "title": "4.2 กล้องจุลทรรศน์โพรบสแกน (Scanning Probe Microscopy: AFM & STM)",
                "summary": "หลักการของแรงระหว่างอะตอม (Lennard-Jones) ในโหมดสัมผัส/เคาะ และการอุโมงค์ควอนตัมตรวจวัดความหนาแน่นอิเล็กตรอน",
                "sim_type": "afm_stm_scanner_sim",
                "formula": "I_{\\text{tunnel}} \\propto V_{\\text{bias}} \\exp(-2 \\kappa d), \\quad \\kappa = \\frac{\\sqrt{2m\\Phi}}{\\hbar}"
            },
            {
                "id": "4.3",
                "title": "4.3 การเลี้ยวเบนของรังสีเอกซ์และสมการเชอร์เรอร์ (XRD & Scherrer Analysis)",
                "summary": "กฎของแบรกก์ การวิเคราะห์เฟสผลึก การขยายตัวของพีคเลี้ยวเบน และการคำนวณขนาดผลึกผลึกนาโน",
                "sim_type": "xrd_diffractometer_sim",
                "formula": "2d\\sin\\theta = n\\lambda, \\quad D = \\frac{K \\lambda}{\\beta \\cos\\theta}"
            },
            {
                "id": "4.4",
                "title": "4.4 การกระเจิงแสงแบบพลวัตและศักย์ซีตา (DLS & Zeta Potential)",
                "summary": "การเคลื่อนที่แบบบราวน์เนียน ความสัมพันธ์สโตกส์-ไอน์สไตน์ และการทำนายความเสถียรของอนุภาคแขวนลอย",
                "sim_type": "dls_zeta_sim",
                "formula": "D_h = \\frac{k_B T}{6\\pi\\eta D_t}, \\quad \\mu_e = \\frac{2\\varepsilon \\zeta}{3\\eta} f(\\kappa a)"
            },
            {
                "id": "4.5",
                "title": "4.5 แบบฝึกหัดและปฏิบัติการจำลอง AR: การสแกนหัวโพรบ AFM/STM",
                "summary": "ปฏิบัติการบังคับหัวเข็มสแกนเสมือนจริงบนผิวคาร์บอนและวิเคราะห์โปรไฟล์ความสูงระดับแองสตรอม",
                "sim_type": "ar_spm_lab",
                "formula": "F(z) = -\\frac{H R}{6 z^2} + \\frac{H R \\sigma^6}{180 z^8}"
            }
        ]
    },
    {
        "id": 5,
        "title": "บทที่ 5 วัสดุสองมิติและอุปกรณ์นาโนอิเล็กทรอนิกส์",
        "description": "ศึกษาวัสดุมหัศจรรย์แห่งศตวรรษที่ 21 กราฟีนและวัสดุ 2D โครงสร้างแถบพลังงาน Dirac Cone ท่อคาร์บอนนาโน (CNT) ทรานซิสเตอร์ระดับนาโน (FET / FinFET / GAAFET) ทรานซิสเตอร์อิเล็กตรอนเดี่ยว (SET) และสปินทรอนิกส์ (GMR)",
        "pages": [
            {
                "id": "5.1",
                "title": "5.1 กราฟีนและวัสดุโครงสร้าง 2 มิติ (Graphene & 2D Nanomaterials)",
                "summary": "โครงสร้างรังผึ้งคาร์บอน สมบัติอิเล็กตรอนไร้มวลสัมพัทธ์ (Dirac Fermions) ความคล่องตัวสูงพิเศษ และ TMDs",
                "sim_type": "graphene_dirac_sim",
                "formula": "E(\\mathbf{k}) = \\pm \\hbar v_F |\\mathbf{k} - \\mathbf{K}|, \\quad v_F \\approx 10^6\\text{ m/s}"
            },
            {
                "id": "5.2",
                "title": "5.2 ท่อคาร์บอนนาโนและสมบัติการนำส่งทางไฟฟ้า (Carbon Nanotubes - CNT)",
                "summary": "เวกเตอร์ไครัลลิที (n,m) การม้วนแผ่นกราฟีน สมบัติความเป็นโลหะหรือสารกึ่งตัวนำ และการประยุกต์ใช้นำส่งความร้อน",
                "sim_type": "cnt_chirality_sim",
                "formula": "\\mathbf{C}_h = n\\mathbf{a}_1 + m\\mathbf{a}_2, \\quad d = \\frac{a}{\\pi}\\sqrt{n^2 + nm + m^2}"
            },
            {
                "id": "5.3",
                "title": "5.3 ทรานซิสเตอร์สนามผลและทรานซิสเตอร์อิเล็กตรอนเดี่ยว (Nano-FET & Single Electron Transistor)",
                "summary": "สถาปัตยกรรมมอสเฟตนาโนมิเตอร์ ปรากฏการณ์ชอร์ตแชนเนล และการปิดกั้นคูลอมบ์ (Coulomb Blockade)",
                "sim_type": "nano_fet_set_sim",
                "formula": "I_{ds} = \\mu C_{ox} \\frac{W}{L} \\left( (V_{gs} - V_{th}) V_{ds} - \\frac{V_{ds}^2}{2} \\right)"
            },
            {
                "id": "5.4",
                "title": "5.4 สปินทรอนิกส์และเทคโนโลยีหัวอ่านแม่เหล็ก (Spintronics & GMR/TMR Devices)",
                "summary": "การใช้สปินของอิเล็กตรอนบันทึกข้อมูล ปรากฏการณ์แมกนีโตรีซิสแตนซ์ขนาดยักษ์ (GMR) และหน่วยความจำ MRAM",
                "sim_type": "spintronics_gmr_sim",
                "formula": "\\text{GMR} = \\frac{R_{\\text{AP}} - R_{\\text{P}}}{R_{\\text{P}}} \\times 100\\%"
            },
            {
                "id": "5.5",
                "title": "5.5 แบบฝึกหัดและปฏิบัติการจำลอง AR: ทรานซิสเตอร์นาโนและแผ่นกราฟีน",
                "summary": "ทดสอบแรงดันเกท ควบคุมกระแสไฟฟ้าของทรานซิสเตอร์นาโน 3 มิติ และตรวจวัดแถบพลังงานด้วยท่าทางมือ",
                "sim_type": "ar_nanoelectronics_lab",
                "formula": "E_c = \\frac{e^2}{2 C_{\\Sigma}} \\gg k_B T"
            }
        ]
    },
    {
        "id": 6,
        "title": "บทที่ 6 นาโนเทคโนโลยีเพื่อพลังงาน สิ่งแวดล้อม และชีวการแพทย์",
        "description": "สำรวจการนำนาโนฟิสิกส์ไปประยุกต์แก้ปัญหาระดับโลก โซลาร์เซลล์รุ่นใหม่ (Perovskite & DSSC) ตัวเร่งปฏิกิริยานาโนกำจัดมลพิษ แบตเตอรี่นาโนและซูเปอร์คาปาซิเตอร์ ระบบนำส่งยาตรงเป้าหมาย และไบโอเซนเซอร์ SERS",
        "pages": [
            {
                "id": "6.1",
                "title": "6.1 โซลาร์เซลล์รุ่นใหม่และตัวเร่งปฏิกิริยานาโน (Perovskite Solar Cells & Nanocatalysis)",
                "summary": "การดูดกลืนแสงของผลึกเพอรอฟสไกต์ การแยกตัวของเอ็กไซตอน และปฏิกิริยาโฟโตคะตะไลซิสสลายสารมลพิษด้วย TiO2",
                "sim_type": "perovskite_photocatalysis_sim",
                "formula": "\\eta = \\frac{J_{sc} \\cdot V_{oc} \\cdot \\text{FF}}{P_{\\text{in}}} \\times 100\\%"
            },
            {
                "id": "6.2",
                "title": "6.2 การกักเก็บพลังงาน: นาโนแบตเตอรี่และซูเปอร์คาปาซิเตอร์ (Nano Batteries & Supercapacitors)",
                "summary": "การแพร่ของลิเทียมไอออนในโครงข่ายอนุภาคนาโน ชั้นประจุคู่ไฟฟ้า (EDLC) และการเพิ่มความหนาแน่นพลังงาน",
                "sim_type": "battery_diffusion_sim",
                "formula": "t_{\\text{diff}} \\approx \\frac{L^2}{D_{\\text{Li}}}, \\quad C = \\frac{\\varepsilon_0 \\varepsilon_r A}{d}"
            },
            {
                "id": "6.3",
                "title": "6.3 การนำส่งยาตรงเป้าหมายและอนุภาคไขมันระดับนาโน (Targeted Drug Delivery & LNPs)",
                "summary": "อนุภาคไขมันระดับนาโน (LNP) และโพลิเมอร์นาโนพาหะ การหลบหลีกระบบภูมิคุ้มกัน และการปลดปล่อยยาตรงเซลล์มะเร็ง",
                "sim_type": "drug_delivery_sim",
                "formula": "\\text{EPR Effect}: \\quad C_{\\text{tumor}}(t) = C_0 \\exp(-k_e t) \\left(1 - \\exp(-k_a t)\\right)"
            },
            {
                "id": "6.4",
                "title": "6.4 นาโนเซนเซอร์และการตรวจวินิจฉัยโรคทางการแพทย์ (Nanosensors & SERS Diagnostics)",
                "summary": "เทคนิค Surface-Enhanced Raman Scattering (SERS) ตรวจจับสารชีวโมเลกุลความเข้มข้นต่ำ และชิป Lab-on-a-Chip",
                "sim_type": "sers_biosensor_sim",
                "formula": "I_{\\text{SERS}} \\propto |E_{\\text{loc}}|^4 \\approx \\left|\\frac{E(\\omega)}{E_0}\\right|^4"
            },
            {
                "id": "6.5",
                "title": "6.5 แบบฝึกหัดและปฏิบัติการจำลอง AR: การนำส่งยาและโซลาร์เซลล์นาโน",
                "summary": "ทดลองฉีดอนุภาคยานาโนเข้าสู่เซลล์และสังเกตการดูดซับพลังงานแสงของเซลล์แสงอาทิตย์ในรูปแบบ 3 มิติ",
                "sim_type": "ar_nanomedicine_lab",
                "formula": "Q(t) = Q_0 \\left(1 - e^{-k t}\\right)"
            }
        ]
    },
    {
        "id": 7,
        "title": "บทที่ 7 ความปลอดภัย พิษวิทยา และจริยธรรมนาโนเทคโนโลยี",
        "description": "สร้างความตระหนักรู้ด้านความปลอดภัย พิษวิทยาของอนุภาคนาโน (Nanotoxicology) เส้นทางการรับสัมผัส ความเครียดจากออกซิเดชัน (ROS) การจัดการความเสี่ยงตามลำดับขั้นการควบคุม (Hierarchy of Controls) และจริยธรรมการวิจัย",
        "pages": [
            {
                "id": "7.1",
                "title": "7.1 ความเป็นพิษของอนุภาคนาโนและเส้นทางการรับสัมผัส (Nanotoxicology & Exposure Pathways)",
                "summary": "การสูดดม การซึมผ่านผิวหนัง และการเข้าสู่กระแสเลือด กลไกการสร้าง Reactive Oxygen Species (ROS) ทำลายเซลล์",
                "sim_type": "nanotox_ros_sim",
                "formula": "\\text{Dose} = \\int_0^T C_{\\text{nano}}(t) \\cdot V_{\\text{resp}} \\, dt"
            },
            {
                "id": "7.2",
                "title": "7.2 มาตรการควบคุมและขั้นตอนปฏิบัติงานมาตรฐาน (Hierarchy of Controls & Nano-SOP)",
                "summary": "การกำจัด การทดแทน การควบคุมทางวิศวกรรม (ตู้ดูดควัน/HEPA) การบริหารจัดการ และอุปกรณ์ป้องกันส่วนบุคคล (PPE)",
                "sim_type": "safety_controls_sim",
                "formula": "\\text{Risk} = \\text{Hazard} \\times \\text{Exposure}"
            },
            {
                "id": "7.3",
                "title": "7.3 การจัดการของเสียวัสดุนาโนและสิ่งแวดล้อม (Nano-waste Disposal & Environment)",
                "summary": "วัฏจักรชีวิตของผลิตภัณฑ์นาโน การบำบัดน้ำเสียปนเปื้อนอนุภาคนาโน และการป้องกันการสะสมในห่วงโซ่อาหาร",
                "sim_type": "waste_treatment_sim",
                "formula": "\\text{BCF} = \\frac{C_{\\text{biota}}}{C_{\\text{water}}}"
            },
            {
                "id": "7.4",
                "title": "7.4 จริยธรรมการวิจัยและการกำกับดูแลเทคโนโลยี (Research Ethics & Governance)",
                "summary": "ความโปร่งใสของข้อมูลวิจัย การประเมินผลกระทบทางสังคม กฎหมายและข้อบังคับสากลด้านความปลอดภัยนาโน",
                "sim_type": "ethics_governance_sim",
                "formula": "\\text{Integrity} = \\frac{\\text{Reproducible Data}}{\\text{Total Experiments}} = 1.00"
            },
            {
                "id": "7.5",
                "title": "7.5 แบบฝึกหัดและปฏิบัติการจำลอง AR: การประเมินความปลอดภัยในห้องปฏิบัติการ",
                "summary": "จำลองการตรวจสอบความปลอดภัยในห้องคลีนรูมและการจัดการเหตุสารนาโนรั่วไหลผ่านมุมมองเสมือนจริง 3D",
                "sim_type": "ar_safety_audit_lab",
                "formula": "\\text{Safety Index} = 1 - \\sum_i w_i P_i"
            }
        ]
    },
    {
        "id": 8,
        "title": "บทที่ 8 ปฏิบัติการจำลองระดับโมเลกุลและโครงงานวิจัยนาโนฟิสิกส์",
        "description": "บูรณาการองค์ความรู้ทั้งหมดผ่านฟิสิกส์เชิงคำนวณ การจำลองพลวัตโมเลกุล (Molecular Dynamics) และการจำลองสนามคลื่นแม่เหล็กไฟฟ้า (FDTD) การวางแผนโครงงานวิจัยนาโนฟิสิกส์ และการนำเสนอผลงานระดับมาตรฐานสากล",
        "pages": [
            {
                "id": "8.1",
                "title": "8.1 การจำลองสมบัติทางแสงของวัสดุนาโนด้วยระเบียบวิธีเชิงตัวเลข (FDTD Computational Optics)",
                "summary": "การแก้สมการแมกซ์เวลล์แบบผลต่างสืบเนื่อง (FDTD) คำนวณค่าการดูดกลืนและการกระเจิงแสงของอนุภาคนาโนทรงต่างๆ",
                "sim_type": "fdtd_optics_sim",
                "formula": "\\nabla \\times \\mathbf{E} = -\\frac{\\partial \\mathbf{B}}{\\partial t}, \\quad \\nabla \\times \\mathbf{H} = \\mathbf{J} + \\frac{\\partial \\mathbf{D}}{\\partial t}"
            },
            {
                "id": "8.2",
                "title": "8.2 การจำลองพลวัตโมเลกุลในระดับนาโน (Molecular Dynamics Simulation)",
                "summary": "การคำนวณการเคลื่อนที่ของอะตอมนับพันด้วยสมการนิวตัน ศักย์เลนนาร์ด-โจนส์ (Lennard-Jones) และอัลกอริทึม Verlet",
                "sim_type": "molecular_dynamics_sim",
                "formula": "m_i \\frac{d^2 \\mathbf{r}_i}{dt^2} = -\\nabla_i \\sum_{j \\neq i} V(r_{ij}), \\quad V(r) = 4\\varepsilon \\left[ \\left(\\frac{\\sigma}{r}\\right)^{12} - \\left(\\frac{\\sigma}{r}\\right)^6 \\right]"
            },
            {
                "id": "8.3",
                "title": "8.3 การออกแบบโครงงานวิจัยนาโนเทคโนโลยีเชิงฟิสิกส์ (Nanophysics Research Proposal Design)",
                "summary": "กระบวนการกำหนดโจทย์วิจัย การตั้งสมมติฐาน การเลือกเครื่องมือสังเคราะห์และวิเคราะห์ และการวางแผนงานวิจัย",
                "sim_type": "research_design_sim",
                "formula": "\\text{Hypothesis} \\to \\text{Synthesis} \\to \\text{Characterization} \\to \\text{Application}"
            },
            {
                "id": "8.4",
                "title": "8.4 การวิเคราะห์ข้อมูลขั้นสูงและการนำเสนอผลงานวิจัย (Data Analysis & Scientific Reporting)",
                "summary": "การวิเคราะห์สถิติ การพลอตกราฟมาตรฐานวารสารสากล การใส่แถบความคลาดเคลื่อน (Error Bars) และการเขียนบทความวิจัย",
                "sim_type": "scientific_graph_sim",
                "formula": "\\bar{x} = \\frac{1}{N}\\sum_{i=1}^N x_i, \\quad \\sigma_{\\bar{x}} = \\frac{s}{\\sqrt{N}}"
            },
            {
                "id": "8.5",
                "title": "8.5 ห้องปฏิบัติการเสมือนจริง 3D/AR เต็มรูปแบบพร้อมระบบตรวจจับท่าทางมือ (Universal AR Nanophysics Lab Hub)",
                "summary": "ศูนย์รวมการทดลองเสมือนจริง 3 มิติครบทุกหัวข้อในวิชานาโนฟิสิกส์ ควบคุมแบบไร้สัมผัส 60 FPS ด้วย AR MediaPipe",
                "sim_type": "ar_universal_nanolab",
                "formula": "\\mathcal{H} \\Psi = E \\Psi, \\quad \\Delta x \\Delta p \\ge \\frac{\\hbar}{2}"
            }
        ]
    }
]

def save_course_data():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    output_path = os.path.join(base_dir, "course_data.json")
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(COURSE_DATA, f, ensure_ascii=False, indent=2)
    print(f"✅ Generated course_data.json with {len(COURSE_DATA)} chapters and 40 subtopics.")
    print("🚀 Course definition ready for Nanotechnological Physics (Refined Titles)!")

if __name__ == "__main__":
    save_course_data()
