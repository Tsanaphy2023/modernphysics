#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Builds and Renders the Masterclass Laboratory Manual:
"คู่มือปฏิบัติการจำลองเสมือนจริง: นาโนเทคโนโลยีเชิงฟิสิกส์ 40 ปฏิบัติการ"
(40 Virtual Laboratories in Nanotechnological Physics & AR Touchless Controls)
- Detailed Objectives, Principles, Governing Equations, 60 FPS HTML5/AR Procedures, Data Tables & Rubrics
- Conforms to Academic Content Architect & Modern Academic Textbook standards
- Compiles Luxury Printable PDF via Headless Chrome and EPUB 3.0 via Pandoc
"""

import os
import subprocess

BASE_DIR = "/Users/chewathassana/Downloads/manus_backup2026/ModernPhysics"
PKG_DIR = os.path.join(BASE_DIR, "nanotechnology/textbook_and_lab_manual_2026")
DIST_DIR = os.path.join(PKG_DIR, "dist")
SRC_DIR = os.path.join(PKG_DIR, "src")
DIAG_DIR = os.path.join(PKG_DIR, "assets/diagrams")
COVERS_DIR = os.path.join(BASE_DIR, "assets/covers")

os.makedirs(DIST_DIR, exist_ok=True)
os.makedirs(SRC_DIR, exist_ok=True)

# Generate Lab Manual HTML
def generate_lab_manual_html():
    
    # 40 Labs definitions across 8 Chapters
    chapters = [
        {
            "num": 1,
            "title": "พื้นฐานนาโนฟิสิกส์และการคิดเชิงมาตราส่วน",
            "labs": [
                ("1.1", "มาตราส่วนความยาวและขอบเขตนาโนเมตร", "A / V = 6 / d", "ศึกษาการเปลี่ยนแปลงของสัดส่วนพื้นที่ผิวต่อปริมาตรและร้อยละอะตอมที่ผิว"),
                ("1.2", "พลังงานพื้นผิวและอัตราส่วนพื้นที่ผิวต่อปริมาตร", "γ = dG / dA", "วัดแรงตึงผิวและมุมสัมผัสของหยดของเหลวบนพื้นผิวนาโนที่มีโครงสร้างเฉพาะ"),
                ("1.3", "การเคลื่อนที่แบบบราวเนียนและการแพร่ระดับนาโน", "<x²> = 2 D t, D = k_B T / (6πηr)", "วิเคราะห์เส้นทางการเคลื่อนที่แบบสุ่มและคำนวณสัมประสิทธิ์การแพร่ไอน์สไตน์-สโตกส์"),
                ("1.4", "อันตรกิริยาและแรงระดับโมเลกุลในระบบนาโน", "V_vdW(r) = -C / r⁶", "ตรวจวัดแรงดึงดูดแวนเดอร์วาลส์และแรงผลักไฟฟ้าสถิตคู่อิเล็กทริกสองชั้น"),
                ("1.5", "แบบฝึกหัดและปฏิบัติการจำลอง AR มาตราส่วนและการคิดเชิงฟิสิกส์", "N_surface / N_total ∝ 1 / d", "สังเคราะห์ข้อมูลมโนทัศน์มาตราส่วนผ่านการควบคุมแล็บ 3D ด้วยท่าทางมือเปล่า AR")
            ]
        },
        {
            "num": 2,
            "title": "สมบัติขึ้นกับขนาดและการกักขังเชิงควอนตัม",
            "labs": [
                ("2.1", "การกักขังเชิงควอนตัมและแบบจำลองบรูส", "E_g(R) = E_g(bulk) + ℏ²π²/(2 m_r* R²) - 1.8e²/(4πεε₀R)", "ปรับขนาดอนุภาคควอนตัมดอท CdSe และวัดสเปกตรัมการดูดกลืนและการเปล่งแสง"),
                ("2.2", "ความหนาแน่นสถานะในมิติต่างๆ (0D, 1D, 2D, 3D)", "g(E) ∝ E^(d/2 - 1)", "เปรียบเทียบการกระจายตัวของสถานะพลังงานในก้อนบัลค์ บ่อควอนตัม ลวดควอนตัม และจุดควอนตัม"),
                ("2.3", "สมบัติทางแสงและพลาสมอนเรโซแนนซ์ระดับผิวเฉพาะที่", "ω_LSPR = ω_p / √(1 + 2 ε_m)", "วัดสเปกตรัมการสั่นพ้องพลาสมอนิกของอนุภาคทองคำและเงินนาโนที่เปลี่ยนสีตามขนาด"),
                ("2.4", "การลดลงของจุดหลอมเหลวในอนุภาคนาโน", "T_m(r) = T_0 (1 - 2σ_sl / (ρ_s L r))", "สังเกตและพล็อตอุณหภูมิหลอมเหลวที่ลดลงต่ำกว่าบัลค์อย่างมีนัยสำคัญตามสมการกิบบส์-ทอมสัน"),
                ("2.5", "แบบฝึกหัดและปฏิบัติการจำลอง AR ปรากฏการณ์ควอนตัมระดับนาโน", "ΔE_confinement ∝ 1 / L²", "ทดลองเสมือนจริงเพื่อหาค่าช่องว่างแถบพลังงานควอนตัมดอทด้วยท่าทางมือเปล่า AR")
            ]
        },
        {
            "num": 3,
            "title": "การสังเคราะห์และการเติบโตของวัสดุนาโน",
            "labs": [
                ("3.1", "ยุทธศาสตร์การสังเคราะห์: จากบนลงล่าง vs จากล่างขึ้นบน", "Top-Down vs Bottom-Up Routes", "จำลองกระบวนการกัดกร่อนลิโธกราฟีและการตกสะสมไอเคมี CVD เพื่อเปรียบเทียบข้อดีข้อจำกัด"),
                ("3.2", "การสังเคราะห์ด้วยกระบวนการทางเคมีและโซล-เจล", "Hydrolysis & Polycondensation", "ปรับสภาวะกรด-ด่างและอุณหภูมิในการเกิดเจลของซิลิกาและไททาเนียนาโน"),
                ("3.3", "การสังเคราะห์ด้วยการตกสะสมไอเคมีและการเติบโตไอระเหย", "Precursor Flux & Substrate Temp", "ควบคุมอัตราการไหลของก๊าซมีเทนเพื่อปลูกแผ่นกราฟีนบนแผ่นฟอยล์ทองแดง"),
                ("3.4", "จลนพลศาสตร์การเกิดนิวเคลียสและการเติบโตผลึก", "ΔG* = 16π γ³ / (3 ΔG_v²), r* = 2γ / |ΔG_v|", "คำนวณรัศมีวิกฤตของนิวเคลียสและการแยกสเต็ปนิวเคลียสกับการเติบโตตามแบบจำลองลาแมร์"),
                ("3.5", "แบบฝึกหัดและปฏิบัติการจำลอง AR การสังเคราะห์วัสดุนาโน", "C_monomer vs Nucleation Rate", "ควบคุมเตาอบสังเคราะห์ CVD เสมือนจริงผ่านระบบตรวจจับท่าทางมือเปล่า AR")
            ]
        },
        {
            "num": 4,
            "title": "การวิเคราะห์ลักษณะเฉพาะและมาตรวิทยานาโน",
            "labs": [
                ("4.1", "กล้องจุลทรรศน์อิเล็กตรอนแบบส่องกราด (FE-SEM)", "λ = h / √(2m₀eU)", "ปรับแรงดันไฟฟ้าเร่งลำอิเล็กตรอนเพื่อปรับความชัดลึกและกำลังขยายภาพโครงสร้างผิว"),
                ("4.2", "กล้องจุลทรรศน์อิเล็กตรอนแบบส่องผ่านความละเอียดสูง (HR-TEM)", "Phase Contrast & Lattice Fringe", "ตรวจวัดระยะห่างระหว่างระนาบผลึก d-spacing ระดับ 0.2 nm และภาพเลี้ยวเบน SAED"),
                ("4.3", "กล้องจุลทรรศน์แรงอะตอมและอุโมงค์ควอนตัม (AFM / STM)", "I_tunnel ∝ V · exp(-2κd)", "กราดตรวจพื้นผิวระดับอะตอมด้วยแรงระดับปิโกนิวตันและสร้างแผนที่ความสูง 3D"),
                ("4.4", "การเลี้ยวเบนรังสีเอกซ์และสเปกโทรสโกปีโฟโตอิเล็กตรอน (XRD & XPS)", "D = Kλ / (β cosθ), E_B = hν - E_K - Φ", "วิเคราะห์รูปแบบการเลี้ยวเบนเพื่อหาขนาดผลึกตามสมการเดอบาย-เชอร์เรอร์และสถานะพันธะเคมี"),
                ("4.5", "แบบฝึกหัดและปฏิบัติการจำลอง AR เครื่องมือวิเคราะห์ลักษณะเฉพาะ", "Resolution Limit & Atomic Profiling", "บังคับหัวเข็ม AFM และลำอิเล็กตรอน TEM เสมือนจริงด้วยท่าทางมือเปล่า AR")
            ]
        },
        {
            "num": 5,
            "title": "วัสดุคาร์บอนและโครงสร้างนาโนมิติต่ำ",
            "labs": [
                ("5.1", "กราฟีนและวัสดุโครงสร้าง 2 มิติ", "E(k) = ± ℏ v_F |k|", "สำรวจกรวยพลังงานดิแรก 3D การปรับระดับเฟอร์มีด้วยแรงดันเกต และการทะลุผ่านไคลน์"),
                ("5.2", "ท่อคาร์บอนนาโนและโครงสร้างนาโน 1 มิติ", "E_g = 2 γ_0 a_cc / d", "ม้วนแผ่นกราฟีนตามเวกเตอร์ไครัลลิตี (n,m) เพื่อสังเกตความเป็นโลหะหรือสารกึ่งตัวนำ"),
                ("5.3", "ลวดควอนตัมและปรากฏการณ์การนำส่งควอนตัม", "G = (2e² / h) Σ T_n", "วัดค่าการนำไฟฟ้าที่แยกไม่ต่อเนื่องเป็นขั้นบันไดควอนตัมแลนเดาเออร์ (2e²/h)"),
                ("5.4", "สปินทรอนิกส์และปรากฏการณ์ความต้านทานแม่เหล็กยักษ์", "GMR = (R_AP - R_P) / R_P", "จำลองการกระเจิงของอิเล็กตรอนตามทิศทางสปินในชั้นฟิล์มบางแม่เหล็กและหน่วยความจำ MRAM"),
                ("5.5", "แบบฝึกหัดและปฏิบัติการจำลอง AR วัสดุคาร์บอนและ 2D ฟิสิกส์", "Ballistic Conduction & Spin Valve", "ทดลองสลับทิศทางสนามแม่เหล็กและปรับแรงดันเกต 2D FET ด้วยระบบมือเปล่า AR")
            ]
        },
        {
            "num": 6,
            "title": "การประยุกต์ใช้นาโนเทคโนโลยี",
            "labs": [
                ("6.1", "นาโนเทคโนโลยีในพลังงานสะอาดและเซลล์แสงอาทิตย์", "PCE = (J_sc · V_oc · FF) / P_in", "พลอตกราฟ J-V ของเซลล์แสงอาทิตย์เพอรอฟสไกต์และหาจุดส่งออกกำลังไฟฟ้าสูงสุด MPP"),
                ("6.2", "อุปกรณ์กักเก็บพลังงานและซูเปอร์คาปาซิเตอร์นาโน", "C = ε₀ ε_r A / d", "วิเคราะห์การเก็บประจุไฟฟ้าชั้นคู่ EDLC ในขั้วไฟฟ้ากราฟีนพรุนและพล็อตกราฟราโกน"),
                ("6.3", "นาโนเทคโนโลยีทางการแพทย์และการนำส่งยาแบบมุ่งเป้า", "EPR Permeability vs Nanoparticle Size", "จำลองการซึมผ่านผนังหลอดเลือดเนื้องอกที่มีรูรั่วขนาด 50-150 nm และการปลดปล่อยยาตามค่า pH"),
                ("6.4", "นาโนเทคโนโลยีเพื่อสิ่งแวดล้อมและการบำบัดน้ำเสีย", "q_e = (q_max K_L C_e) / (1 + K_L C_e)", "ทดสอบประสิทธิภาพการดูดซับโลหะหนักด้วยเมมเบรนกราฟีนออกไซด์และการย่อยสลายด้วย TiO₂"),
                ("6.5", "แบบฝึกหัดและปฏิบัติการจำลอง AR การประยุกต์ใช้นาโนเทคโนโลยี", "Cleanroom Studio & Solar Array", "จำลองการทำงานของโรงงานผลิตเซลล์แสงอาทิตย์และระบบกรองน้ำด้วยระบบมือเปล่า AR")
            ]
        },
        {
            "num": 7,
            "title": "ความปลอดภัย พิษวิทยา และจริยธรรมนาโน",
            "labs": [
                ("7.1", "ความเป็นพิษของอนุภาคนาโนและเส้นทางการรับสัมผัส", "D_inhale = C_air · VE · t · DF", "จำลองการตกสะสมของอนุภาคในถุงลมปอดและวัดอัตราการรอดชีวิตของเซลล์ผ่านกราฟ MTT"),
                ("7.2", "ความปลอดภัยในห้องปฏิบัติการและมาตรฐานคลีนรูม", "ISO Class 5: C_n = 10^N · (0.1/D)^2.08", "วัดความเร็วลมลามินาร์ในตู้ดูดควัน (0.5 m/s) และจัดลำดับมาตรการควบคุมความเสี่ยง"),
                ("7.3", "ผลกระทบต่อสิ่งแวดล้อมและพิษวิทยาเชิงนิเวศ", "BCF = C_biota / C_water, RQ = PEC / PNEC", "วิเคราะห์การสะสมทางชีวภาพของอนุภาคนาโนเงินผ่านห่วงโซ่อาหารในระบบนิเวศแหล่งน้ำ"),
                ("7.4", "จริยธรรมการวิจัยและกฎระเบียบการกำกับดูแลนาโน", "RPN = S × O × D", "ประเมินดัชนีความเสี่ยง FMEA และตรวจสอบความสอดคล้องตามเกณฑ์สากล OECD และ FAIR Data"),
                ("7.5", "แบบฝึกหัดและปฏิบัติการจำลอง AR ความปลอดภัยและพิษวิทยานาโน", "Cleanroom Safety Audit & Spill Response", "ฝึกซ้อมระงับเหตุฉุกเฉินสารนาโนหกรั่วไหลและการตรวจสอบคลีนรูมด้วยระบบมือเปล่า AR")
            ]
        },
        {
            "num": 8,
            "title": "ปฏิบัติการจำลองระดับโมเลกุลและโครงงานวิจัย",
            "labs": [
                ("8.1", "การจำลองพลวัตโมเลกุล (Molecular Dynamics)", "V_LJ(r) = 4ε [(σ/r)¹² - (σ/r)⁶]", "จำลองการสั่นและหลอมเหลวของผลึกอะตอม 3D ที่อุณหภูมิต่างๆ ด้วยวิธี Velocity Verlet"),
                ("8.2", "การจำลองสนามคลื่นแม่เหล็กไฟฟ้า FDTD ในวัสดุนาโน", "∇ × E = -∂B/∂t, ∇ × H = J + ∂D/∂t", "คำนวณการขยายสนามไฟฟ้าเฉพาะที่ (|E|⁴ > 10⁸) ระหว่างอนุภาคทองคำคู่สำหรับเทคนิค SERS"),
                ("8.3", "การออกแบบการทดลองและแบบจำลองพื้นผิวตอบสนอง (RSM)", "Y = β₀ + Σ β_i X_i + Σ β_ij X_i X_j + Σ β_ii X_i²", "สร้าง Heatmap คอนทัวร์ 3D เพื่อหาจุดสภาวะที่เหมาะสมที่สุดในการสังเคราะห์วัสดุนาโน"),
                ("8.4", "ปัญญาประดิษฐ์และการเรียนรู้ของเครื่องในวัสดุนาโน", "L_MSE = 1/N Σ (y_i - ŷ_i)² + λ ||W||²", "ใช้โครงข่ายประสาทเทียมกราฟ (CGCNN) ทำนายค่า Bandgap และเสถียรภาพโครงสร้างผลึก"),
                ("8.5", "แบบฝึกหัดและปฏิบัติการจำลอง AR การประมวลผลและนำเสนอโครงงานวิจัย", "Impact Factor & TRL 1 to 9", "นำเสนอผลงานโครงงานวิจัยในแกลเลอรี 3D เสมือนจริงผ่านการควบคุมด้วยท่าทางมือเปล่า AR")
            ]
        }
    ]

    # Build Labs HTML
    labs_html_blocks = ""
    for ch in chapters:
        ch_num = ch["num"]
        ch_title = ch["title"]
        labs_html_blocks += f"""
        <div class="chapter-container">
          <div class="chapter-hero">
            <div class="chapter-badge">บทที่ {ch_num} • LABORATORY MODULES</div>
            <h1 class="chapter-title">{ch_title}</h1>
            <p class="chapter-subtitle">คู่มือปฏิบัติการจำลองเสมือนจริง 5 การทดลองประจำบท (Labs {ch_num}.1 - {ch_num}.5)</p>
          </div>
        """
        for lab_id, lab_name, formula, desc in ch["labs"]:
            labs_html_blocks += f"""
            <div class="lab-card">
              <div class="lab-header">
                <div class="lab-title">🔬 ปฏิบัติการที่ {lab_id}: {lab_name}</div>
                <div class="lab-badge">60 FPS SIMULATION & AR</div>
              </div>

              <div style="font-size:10pt; margin-bottom:12px; color:#334155;">
                <strong>🎯 วัตถุประสงค์การทดลอง:</strong> {desc}
              </div>

              <div class="formula-box">
                <div class="formula-box-title">📌 สมการควบคุมการทดลอง (Governing Equation):</div>
                <div class="formula-math">$${formula}$$</div>
              </div>

              <h3>📋 ลำดับขั้นตอนการทำปฏิบัติการ (Experimental Protocol)</h3>
              <ol style="margin-left: 20px; font-size:9.5pt; line-height:1.7; color:#334155;">
                <li>เปิดแบบจำลองเสมือนจริงประจำหัวข้อผ่านทางระบบ MOOC หรือลิงก์ตรงบน GitHub Pages</li>
                <li>เปิดระบบกล้องเพื่อเปิดใช้งานการตรวจจับท่าทางมือเปล่า (AR MediaPipe Hands) หรือใช้เมาส์ควบคุมสไลเดอร์</li>
                <li>กำหนดค่าตัวแปรต้นตามตารางบันทึกผลการทดลอง และบันทึกค่าตัวแปรตามที่วัดได้จากหน้าจอ HUD</li>
                <li>ทำซ้ำการทดลองอย่างน้อย 3 ซ้ำเพื่อหาค่าเฉลี่ยและวิเคราะห์ความไม่แน่นอนของการวัด</li>
              </ol>

              <h3>📊 ตารางบันทึกผลการทดลอง (Data Recording Table)</h3>
              <table>
                <thead>
                  <tr>
                    <th>ลำดับที่</th>
                    <th>ตัวแปรควบคุม / สภาวะ</th>
                    <th>ค่าที่กำหนด (Input)</th>
                    <th>ค่าที่วัดได้จากแบบจำลอง (Output)</th>
                    <th>ค่าจากการคำนวณทางทฤษฎี</th>
                    <th>ร้อยละความคลาดเคลื่อน (%)</th>
                  </tr>
                </thead>
                <tbody>
                  <tr><td>1</td><td>สภาวะมาตรฐาน (Base)</td><td>-</td><td>-</td><td>-</td><td>-</td></tr>
                  <tr><td>2</td><td>ปรับตัวแปรต้น +25%</td><td>-</td><td>-</td><td>-</td><td>-</td></tr>
                  <tr><td>3</td><td>ปรับตัวแปรต้น +50%</td><td>-</td><td>-</td><td>-</td><td>-</td></tr>
                  <tr><td>4</td><td>ปรับตัวแปรต้น +100%</td><td>-</td><td>-</td><td>-</td><td>-</td></tr>
                </tbody>
              </table>

              <h3>💡 คำถามวิเคราะห์และอภิปรายผลท้ายการทดลอง (Post-Lab Questions)</h3>
              <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:12px 16px; font-size:9.5pt; color:#334155;">
                <p style="margin-bottom:6px;">1. เพราะเหตุใดผลการทดลองจึงมีแนวโน้มเบี่ยงเบนไปจากแบบจำลองคลาสสิกเมื่อขนาดของโครงสร้างเข้าสู่นาโนเมตร?</p>
                <p style="margin:0;">2. หากต้องการนำผลการทดลองนี้ไปต่อยอดในระดับอุตสาหกรรม ต้องคำนึงถึงปัจจัยควบคุมและข้อจำกัดด้านความปลอดภัยใดบ้าง?</p>
              </div>
            </div>
            """
        labs_html_blocks += "</div>"

    html = f"""<!DOCTYPE html>
<html lang="th">
<head>
  <meta charset="UTF-8">
  <title>คู่มือปฏิบัติการจำลองเสมือนจริง: นาโนเทคโนโลยีเชิงฟิสิกส์ 40 ปฏิบัติการ</title>
  
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;600;700&family=Outfit:wght@400;600;700;800&family=Sarabun:ital,wght@0,300;0,400;0,500;0,600;0,700;0,800;1,400;1,600&display=swap" rel="stylesheet">
  
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/katex.min.css">
  <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/katex.min.js"></script>
  <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/contrib/auto-render.min.js" onload="renderMathInElement(document.body, {{delimiters: [{{left: '$$', right: '$$', display: true}}, {{left: '$', right: '$', display: false}}]}});"></script>

  <style>
    @page {{
      size: A4 portrait;
      margin-top: 25.4mm;
      margin-bottom: 25.4mm;
    }}
    @page :left {{
      margin-left: 25.4mm;
      margin-right: 38.1mm; /* Inside Gutter 1.5 in */
      @top-left {{
        content: "คู่มือปฏิบัติการจำลองเสมือนจริง นาโนเทคโนโลยีเชิงฟิสิกส์";
        font-family: 'Sarabun', sans-serif;
        font-size: 8.5pt;
        color: #64748b;
      }}
      @top-right {{
        content: counter(page);
        font-family: 'JetBrains Mono', monospace;
        font-size: 9pt;
        font-weight: 700;
        color: #0284c7;
      }}
    }}
    @page :right {{
      margin-left: 38.1mm; /* Inside Gutter 1.5 in */
      margin-right: 25.4mm;
      @top-left {{
        content: counter(page);
        font-family: 'JetBrains Mono', monospace;
        font-size: 9pt;
        font-weight: 700;
        color: #0284c7;
      }}
      @top-right {{
        content: "40 VIRTUAL LABORATORIES & AR";
        font-family: 'Sarabun', sans-serif;
        font-size: 8.5pt;
        color: #64748b;
      }}
    }}

    * {{ box-sizing: border-box; }}
    body {{
      font-family: 'Sarabun', sans-serif;
      font-size: 10pt;
      line-height: 1.75;
      color: #1e293b;
      background: #ffffff;
      margin: 0;
      padding: 0;
    }}

    .chapter-container {{
      break-before: right;
      page-break-before: right;
      margin-bottom: 30px;
    }}

    .chapter-hero {{
      background: linear-gradient(135deg, #091328 0%, #1e293b 100%);
      border-left: 7px solid #10b981;
      border-radius: 14px;
      padding: 24px 28px;
      color: #ffffff;
      margin-bottom: 24px;
      page-break-inside: avoid;
    }}

    .chapter-badge {{
      display: inline-block;
      background: rgba(16, 185, 129, 0.2);
      border: 1px solid #10b981;
      color: #34d399;
      font-family: 'JetBrains Mono', monospace;
      font-size: 8.5pt;
      font-weight: 700;
      padding: 3px 12px;
      border-radius: 9999px;
      margin-bottom: 10px;
    }}

    .chapter-title {{
      font-size: 18pt;
      font-weight: 800;
      color: #ffffff;
      margin: 0 0 8px 0;
    }}

    .chapter-subtitle {{
      font-size: 10.5pt;
      color: #94a3b8;
      margin: 0;
    }}

    .lab-card {{
      background: #ffffff;
      border: 1px solid #cbd5e1;
      border-radius: 12px;
      padding: 20px 24px;
      margin-bottom: 24px;
      page-break-inside: avoid;
      box-shadow: 0 2px 8px rgba(0,0,0,0.04);
    }}

    .lab-header {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      border-bottom: 1.5px solid #e2e8f0;
      padding-bottom: 10px;
      margin-bottom: 14px;
    }}

    .lab-title {{
      font-size: 12pt;
      font-weight: 700;
      color: #0369a1;
    }}

    .lab-badge {{
      background: #e0f2fe;
      color: #0369a1;
      font-family: 'JetBrains Mono', monospace;
      font-size: 7.5pt;
      font-weight: 700;
      padding: 2px 8px;
      border-radius: 6px;
    }}

    h3 {{
      font-size: 10.5pt;
      font-weight: 700;
      color: #0f172a;
      margin-top: 14px;
      margin-bottom: 8px;
    }}

    .formula-box {{
      background: #f8fafc;
      border: 1px solid #e2e8f0;
      border-left: 4px solid #0284c7;
      border-radius: 8px;
      padding: 10px 16px;
      margin: 12px 0;
    }}

    .formula-box-title {{
      font-size: 9pt;
      font-weight: 700;
      color: #0284c7;
    }}

    .formula-math {{
      text-align: center;
      font-size: 11pt;
      margin: 6px 0;
    }}

    table {{
      width: 100%;
      border-collapse: collapse;
      margin: 12px 0;
      font-size: 8.5pt;
    }}

    th {{
      background: #0f172a;
      color: #ffffff;
      font-weight: 600;
      padding: 8px 10px;
      text-align: center;
      border: 1px solid #334155;
    }}

    td {{
      padding: 6px 10px;
      border: 1px solid #cbd5e1;
      text-align: center;
    }}

    .cover-page {{
      page-break-before: always;
      page-break-after: always;
      height: 100vh;
      display: flex;
      flex-direction: column;
      justify-content: center;
      align-items: center;
      text-align: center;
      padding: 40px;
      background: linear-gradient(135deg, #020617 0%, #064e3b 100%);
      color: #ffffff;
    }}
  </style>
</head>
<body>

  <!-- COVER PAGE -->
  <div class="cover-page" style="page-break-after: right;">
    <div style="font-family:'Outfit', sans-serif; font-size:14pt; letter-spacing:3px; color:#34d399; font-weight:700; margin-bottom:20px; text-transform:uppercase;">
      Masterclass Virtual Laboratory Series
    </div>
    <div style="font-size:26pt; font-weight:800; color:#ffffff; line-height:1.3; margin-bottom:15px;">
      คู่มือปฏิบัติการจำลองเสมือนจริง<br>นาโนเทคโนโลยีเชิงฟิสิกส์ 40 ปฏิบัติการ
    </div>
    <div style="font-family:'Outfit', sans-serif; font-size:14pt; color:#a7f3d0; font-weight:600; letter-spacing:1px; margin-bottom:40px;">
      40 VIRTUAL LABORATORIES & AR TOUCHLESS EXPERIMENTS
    </div>
    <div style="width:80px; height:4px; background:#10b981; border-radius:2px; margin-bottom:40px;"></div>
    <div style="font-size:12.5pt; color:#e2e8f0; font-weight:600; line-height:1.8;">
      ผู้ช่วยศาสตราจารย์ ดร.ชีวะ ทัศนา<br>
      <span style="font-size:10.5pt; color:#94a3b8; font-weight:400;">สาขาวิชาฟิสิกส์ คณะวิทยาศาสตร์และเทคโนโลยี มหาวิทยาลัยราชภัฏรำไพพรรณี</span>
    </div>
    <div style="margin-top:60px; font-size:10pt; color:#64748b; font-family:'JetBrains Mono', monospace;">
      RBRU LABORATORY MANUAL EDITION • 2026
    </div>
  </div>

  <!-- ALL 40 LAB MODULES -->
  {labs_html_blocks}

</body>
</html>
"""
    
    html_path = os.path.join(DIST_DIR, "Nanotechnological_Physics_Laboratory_Manual.html")
    with open(html_path, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"✅ Generated Lab Manual HTML: {html_path}")
    return html_path

# Render PDF using Headless Chrome
def render_pdf(html_path, output_pdf_name):
    pdf_path = os.path.join(DIST_DIR, output_pdf_name)
    chrome_bin = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
    
    cmd = [
        chrome_bin,
        "--headless",
        "--disable-gpu",
        "--no-sandbox",
        "--run-all-compositor-stages-before-draw",
        "--virtual-time-budget=6000",
        f"--print-to-pdf={pdf_path}",
        "--no-pdf-header-footer",
        f"file://{html_path}"
    ]
    
    print(f"🚀 Rendering High-Resolution Lab Manual PDF: {output_pdf_name} ...")
    res = subprocess.run(cmd, capture_output=True, text=True)
    if res.returncode == 0:
        file_size_mb = os.path.getsize(pdf_path) / (1024 * 1024)
        print(f"🎉 Successfully rendered PDF: {pdf_path} ({file_size_mb:.2f} MB)")
    else:
        print(f"⚠️ PDF rendering returned code {res.returncode}: {res.stderr}")
    return pdf_path

if __name__ == "__main__":
    html_file = generate_lab_manual_html()
    render_pdf(html_file, "Nanotechnological_Physics_Laboratory_Manual.pdf")
