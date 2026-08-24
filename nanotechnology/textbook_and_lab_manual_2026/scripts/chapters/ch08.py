# -*- coding: utf-8 -*-
"""
Chapter 8: นาโนเทคโนโลยีเพื่อพลังงาน สิ่งแวดล้อม และความปลอดภัย
Perovskites, Solid-State Batteries, Photocatalysis, Nanotoxicology, ROS & Safe-by-Design Ethics
"""

def get_chapter_8():
    return r"""
    <div class="chapter-container">
      <div class="chapter-hero">
        <div class="chapter-badge">CHAPTER 08 • NANOTECHNOLOGICAL PHYSICS</div>
        <h1 class="chapter-title">นาโนเทคโนโลยีเพื่อพลังงาน สิ่งแวดล้อม และความปลอดภัย</h1>
        <p class="chapter-subtitle">Perovskites, Solid-State Batteries, Photocatalysis, Nanotoxicology, ROS & Safe-by-Design Ethics</p>
      </div>

      <div class="diagram-wrap">
        <img src="../assets/diagrams/ch08_energy_and_safety.svg" alt="นาโนเทคโนโลยีเพื่อพลังงาน สิ่งแวดล้อม และความปลอดภัย">
        <div class="caption">ภาพที่ 8.1 แผนผังเซลล์แสงอาทิตย์เพอรอฟสไกต์, แบตเตอรี่โซลิดสเตต, การแยกน้ำด้วยแสง Z-Scheme, กลไกพิษวิทยา ROS และกรอบ Safe-by-Design</div>
      </div>

      
    <div class="topic-section">
      <h2>8.1 เซลล์แสงอาทิตย์เพอรอฟสไกต์และนาโนเทคโนโลยีพลังงานแสง</h2>
      <div class="topic-en-title">(Perovskite Solar Cells, Tandem Devices & Photovoltaic Nanophysics)</div>
      
      <div class="topic-intro">
        <p>เซลล์แสงอาทิตย์เพอรอฟสไกต์เฮไลด์อินทรีย์-อนินทรีย์ (Halide Perovskite Solar Cells: PSCs โครงสร้างผลึก $A B X_3$ เช่น $	ext{CH}_3	ext{NH}_3	ext{PbI}_3$ หรือ $	ext{CsPbBr}_3$) เป็นเทคโนโลยีเซลล์แสงอาทิตย์ที่เติบโตรวดเร็วที่สุดในประวัติศาสตร์ โดยมีประสิทธิภาพการแปลงพลังงาน (Power Conversion Efficiency: PCE) พุ่งทะยานจาก $3.8\%$ ในปี 2009 สู่มากกว่า $26.1\%$ ในเซลล์เดี่ยว และทะลุ $33.9\%$ ในเซลล์แบบแทนเดมซิลิคอน-เพอรอฟสไกต์ (Perovskite-Silicon Tandem)</p>
    <p>ความโดดเด่นทางฟิสิกส์ของเพอรอฟสไกต์อยู่ที่คุณสมบัติ: สัมประสิทธิ์การดูดกลืนแสงที่สูงเป็นพิเศษ ($lpha > 10^5	ext{ cm}^{-1}$), ความยาวการแพร่ของพาหะประจุที่ยาวไกลเกิน $1	ext{ }\mu	ext{m}$ (Long Carrier Diffusion Length), พลังงานยึดเหนี่ยวเอ็กซิตอนที่ต่ำมาก ($E_b < 20	ext{ meV}$ ทำให้เอ็กซิตอนแตกตัวเป็นอิเล็กตรอนและโฮลอิสระได้ทันทีที่อุณหภูมิห้อง), และโครงสร้างแถบพลังงานที่มีความทนทานต่อข้อบกพร่องสูง (Defect Tolerance)</p>
    <p>การผสานเซลล์เพอรอฟสไกต์ที่มีช่องว่างแถบพลังงานกว้าง ($E_{g1} pprox 1.68	ext{ eV}$) เข้ากับเซลล์ซิลิคอนช่องว่างแคบ ($E_{g2} pprox 1.12	ext{ eV}$) ช่วยก้าวข้ามขีดจำกัดช็อกคลีย์-ไควเซอร์สำหรับรอยต่อเดี่ยว (Shockley-Queisser Limit: 33.7%) มุ่งสู่อนาคตพลังงานสะอาดที่มีต้นทุนต่ำและประสิทธิภาพสูงสุด</p>
  </div>

      <div class="subtopic-block">
        <h3>โครงสร้างผลึก ABX3 และดัชนีความทนทานของโกลด์ชมิดต์ (Goldschmidt Tolerance Factor)</h3>
            <p>สูตรความเสถียรของโครงสร้างเพอรอฟสไกต์: $t = rac{r_A + r_X}{\sqrt{2}(r_B + r_X)}$ และตัวประกอบแปดหน้า (Octahedral Factor): $\mu = rac{r_B}{r_X}$</p>
    <p>โครงสร้างเพอรอฟสไกต์ลูกบาศก์ที่เสถียรจะต้องมี $0.8 \le t \le 1.0$ และ $\mu \ge 0.414$ หากค่า $t$ เบี่ยงเบนออกไปจะเกิดการบิดเบี้ยวเป็นโครงสร้างเตตระโกนัลหรือออร์โธรอมบิก ซึ่งส่งผลต่อช่องว่างแถบพลังงาน</p>
  </div>

      <div class="subtopic-block">
        <h3>จลนศาสตร์การรวมตัวของพาหะและการดัดแปรพื้นผิวรอยต่อ (Passivation)</h3>
            <p>สมการจลนศาสตร์พาหะ: $-rac{dn}{dt} = k_1 n + k_2 n^2 + k_3 n^3$ (เมื่อ $k_1$ คือการรวมตัวผ่านกับดักข้อบกพร่อง SRH, $k_2$ คือการรวมตัวแบบเปล่งรังสี, และ $k_3$ คือการรวมตัวแบบออเจร์ Auger)</p>
    <p>การใช้โมเลกุลเกลือแอมโมเนียมอินทรีย์หรืออนุภาคนาโน 2D เพอรอฟสไกต์มาพาสซิเวชันที่ผิวหน้าช่วยลดค่า $k_1$ ทำให้แรงดันวงจรเปิด ($V_{	ext{oc}}$) สูงเข้าใกล้ขีดจำกัดทางรังสี</p>
  </div>
  <div class="formula-group">

        <div class="equation-box">
          <div class="equation-header">📌 สมการฟิสิกส์หลัก: ดัชนีความทนทานของโกลด์ชมิดต์ (Goldschmidt Tolerance Factor)</div>
          <div class="formula-math">$$t = \frac{r_A + r_X}{\sqrt{2}(r_B + r_X)}, \qquad \mu = \frac{r_B}{r_X}$$</div>
          <p style="font-size:9.5pt; margin:4px 0 0 0; color:#334155; line-height:1.75; text-indent:0;"><strong>คำอธิบายตัวแปรและนัยสำคัญ:</strong> เกณฑ์ความเสถียรของโครงสร้างผลึกเพอรอฟสไกต์</p>
        </div>
            
        <div class="equation-box">
          <div class="equation-header">📌 สมการฟิสิกส์หลัก: ประสิทธิภาพการแปลงพลังงานของเซลล์แสงอาทิตย์ (PCE)</div>
          <div class="formula-math">$$\text{PCE} = \frac{P_{\text{max}}}{P_{\text{in}}} = \frac{J_{\text{sc}} \times V_{\text{oc}} \times \text{FF}}{P_{\text{in}}}, \qquad \text{FF} = \frac{J_{\text{mp}} V_{\text{mp}}}{J_{\text{sc}} V_{\text{oc}}}$$</div>
          <p style="font-size:9.5pt; margin:4px 0 0 0; color:#334155; line-height:1.75; text-indent:0;"><strong>คำอธิบายตัวแปรและนัยสำคัญ:</strong> การคำนวณประสิทธิภาพเซลล์แสงอาทิตย์มาตรฐาน AM1.5G</p>
        </div>
              </div>

      <div class="table-block">
        <h3>📊 ตารางเปรียบเทียบเทคโนโลยีเซลล์แสงอาทิตย์ยุคต่างๆ</h3>
        <table class="data-table">
          <thead><tr>
            <th>เทคโนโลยีเซลล์</th><th>วัสดุหลัก</th><th>PCE ปัจจุบัน (%)</th><th>ข้อดีเด่น</th><th>ความท้าทายหลัก</th></tr></thead>
<tbody><tr><td>Silicon First-Gen</td><td>Mono/Poly-Si</td><td>24.5 - 26.8%</td><td>เสถียรภาพยาวนาน (> 25 ปี)</td><td>กระบวนการผลิตใช้พลังงานสูง</td></tr><tr><td>Thin-Film Second-Gen</td><td>CIGS, CdTe</td><td>19.0 - 22.5%</td><td>ใช้วัตถุดิบน้อย ยืดหยุ่นได้</td><td>ธาตุหายาก มีแคดเมียม</td></tr><tr><td>Perovskite Single-Junction</td><td>FAPbI3 / CsFAPbI3</td><td>26.1%</td><td>ต้นทุนต่ำ ดูดกลืนแสงสูงมาก</td><td>เสถียรภาพต่อความชื้นและความร้อน</td></tr><tr><td>Perovskite-Silicon Tandem</td><td>Perovskite on Silicon</td><td>33.9%</td><td>ประสิทธิภาพทะลุขีดจำกัด SQ</td><td>ความซับซ้อนในการผลิตเชิงอุตสาหกรรม</td></tr></tbody></table>
</div>
  <div class="examples-group">

        <div class="example-box">
          <div class="example-header">
            <span>📝 ตัวอย่างการคำนวณที่ 8.1: การคำนวณ Goldschmidt Tolerance Factor ของ Methylammonium Lead Iodide (MAPbI3)</span>
            <span style="background:#dcfce7; color:#15803d; font-size:8.5pt; padding:3px 10px; border-radius:4px; font-weight:700;">Step-by-Step Worked Solution</span>
          </div>
          <p style="text-indent:0; margin-bottom:10px;"><strong>โจทย์ปัญหา (Problem Statement):</strong><br>กำหนดรัศมีไอออนิก: $r_{	ext{MA}^+} = 0.217	ext{ nm}$, $r_{	ext{Pb}^{2+}} = 0.119	ext{ nm}$, $r_{	ext{I}^-} = 0.220	ext{ nm}$ จงคำนวณหา (ก) Tolerance factor $t$ (ข) Octahedral factor $\mu$ และวิเคราะห์ความเสถียรของผลึก</p>
          <div style="background:rgba(255,255,255,0.85); border:1px solid #e2e8f0; padding:12px 16px; border-radius:6px; margin:12px 0;">
            <strong style="color:#1e3a8a;">การวิเคราะห์และการคำนวณอย่างละเอียด:</strong><br>
            <p style="text-indent:0; margin:6px 0 0 0; line-height:1.85;">1. $t = \frac{r_{\text{MA}} + r_{\text{I}}}{\sqrt{2}(r_{\text{Pb}} + r_{\text{I}})} = \frac{0.217 + 0.220}{\sqrt{2}(0.119 + 0.220)} = \frac{0.437}{\sqrt{2}(0.339)} = \frac{0.437}{0.4794} = 0.9115$<br>2. $\mu = \frac{r_{\text{Pb}}}{r_{\text{I}}} = \frac{0.119}{0.220} = 0.5409$<br>3. เนื่องจาก $0.8 \le t = 0.912 \le 1.0$ และ $\mu = 0.541 > 0.414$</p>
          </div>
          <div style="background:#f0fdf4; border-left:4px solid #16a34a; padding:10px 14px; margin-top:10px; font-size:9.5pt; color:#166534; border-radius:0 6px 6px 0;">
            💡 <strong>นัยสำคัญทางกายภาพและการประยุกต์ใช้งาน (Physical Insight):</strong><br>
            <span style="color:#14532d;">โครงสร้างผลึก $	ext{MAPbI}_3$ มีความเสถียรในรูปแบบเพอรอฟสไกต์ลูกบาศก์ 3 มิติอย่างสมบูรณ์</span>
          </div>
        </div>
            
        <div class="example-box">
          <div class="example-header">
            <span>📝 ตัวอย่างการคำนวณที่ 8.2: การคำนวณประสิทธิภาพการแปลงพลังงาน (PCE) ของเซลล์เพอรอฟสไกต์</span>
            <span style="background:#dcfce7; color:#15803d; font-size:8.5pt; padding:3px 10px; border-radius:4px; font-weight:700;">Step-by-Step Worked Solution</span>
          </div>
          <p style="text-indent:0; margin-bottom:10px;"><strong>โจทย์ปัญหา (Problem Statement):</strong><br>เซลล์เพอรอฟสไกต์พื้นที่ $A = 1.0	ext{ cm}^2$ ภายใต้แสงจำลองมาตรฐาน $	ext{AM1.5G}$ ($P_{	ext{in}} = 100.0	ext{ mW/cm}^2$) ให้ค่ากระแสลัดวงจร $J_{	ext{sc}} = 25.5	ext{ mA/cm}^2$, แรงดันวงจรเปิด $V_{	ext{oc}} = 1.18	ext{ V}$, และ Fill Factor $	ext{FF} = 0.82$ จงคำนวณหาค่ากำลังไฟฟ้าสูงสุด $P_{	ext{max}}$ และประสิทธิภาพ $	ext{PCE}$</p>
          <div style="background:rgba(255,255,255,0.85); border:1px solid #e2e8f0; padding:12px 16px; border-radius:6px; margin:12px 0;">
            <strong style="color:#1e3a8a;">การวิเคราะห์และการคำนวณอย่างละเอียด:</strong><br>
            <p style="text-indent:0; margin:6px 0 0 0; line-height:1.85;">1. $P_{\text{max}} = J_{\text{sc}} \times V_{\text{oc}} \times \text{FF} = (25.5\text{ mA/cm}^2) \times (1.18\text{ V}) \times 0.82 = 24.674\text{ mW/cm}^2$<br>2. $\text{PCE} = \frac{P_{\text{max}}}{P_{\text{in}}} \times 100\% = \frac{24.674\text{ mW/cm}^2}{100.0\text{ mW/cm}^2} \times 100\% = 24.67\%$</p>
          </div>
          <div style="background:#f0fdf4; border-left:4px solid #16a34a; padding:10px 14px; margin-top:10px; font-size:9.5pt; color:#166534; border-radius:0 6px 6px 0;">
            💡 <strong>นัยสำคัญทางกายภาพและการประยุกต์ใช้งาน (Physical Insight):</strong><br>
            <span style="color:#14532d;">เซลล์แสงอาทิตย์มีประสิทธิภาพสูงถึง $24.67\%$ จัดอยู่ในกลุ่มเซลล์ประสิทธิภาพสูงระดับแนวหน้าของโลก</span>
          </div>
        </div>
              </div>
  <div class="code-group">

        <div class="code-box">
          <div class="code-header">💻 แบบจำลองเชิงคำนวณภาษาไพทอน (Computational Python 3.11): กรณีศึกษา: แผงเซลล์แสงอาทิตย์เพอรอฟสไกต์-ซิลิคอนแทนเดมเชิงพาณิชย์โดย Oxford PV</div>
          <pre><code>การผลิตแผงโซลาร์เซลล์แทนเดมขนาดเต็มแผ่นที่ให้ประสิทธิภาพสูงถึง 24.5% ในระดับโมดูล ซึ่งผลิตพลังงานไฟฟ้าได้มากกว่าแผงซิลิคอนเดิมถึง 20% ในพื้นที่ติดตั้งเท่าเดิม</code></pre>
        </div>
        <p style="font-size:9.5pt; color:#475569; margin-top:-6px; margin-bottom:18px; text-indent:0;"><em>คำอธิบายอัลกอริทึมการจำลอง:</em> สคริปต์ไพทอนสำหรับการคำนวณและจำลองเชิงตัวเลข</p>
              </div>
  <div class="lab-connection-block">
    <h3>🔬 การเชื่อมโยงสู่ห้องปฏิบัติการเสมือนจริงและเทคนิคการทดลอง (Virtual Lab Connection)</h3>
    <div style='background:#f0fdf4; border:1px solid #bbf7d0; border-left:5px solid #16a34a; padding:12px 16px; margin-bottom:14px; border-radius:6px;'><strong style='color:#166534; font-size:10.5pt;'>การจำลองเส้นโค้ง J-V และจุดทำงานกำลังสูงสุด MPP</strong><p style='margin:6px 0 0 0; color:#14532d; text-indent:0; line-height:1.8;'>perovskite_jv_curve.py</p></div>
  </div>
  <div class="cases-block">
    <h3>🌐 กรณีศึกษางานวิจัยแนวหน้าและนวัตกรรมอุตสาหกรรม (Frontier Case Studies)</h3>
    <div style='background:#eff6ff; border:1px solid #bfdbfe; border-left:5px solid #2563eb; padding:12px 16px; margin-bottom:14px; border-radius:6px;'><strong style='color:#1e40af; font-size:10.5pt;'>การเชื่อมโยงกับ Virtual Lab 36: การจำลองเซลล์แสงอาทิตย์เพอรอฟสไกต์และอุปกรณ์แทนเดม</strong><p style='margin:6px 0 0 0; color:#1e3a8a; text-indent:0; line-height:1.8;'>ผู้เรียนสามารถควบคุมสัดส่วนองค์ประกอบธาตุในเพอรอฟสไกต์ใน Lab 36 ปรับความหนาชั้นขนส่งอิเล็กตรอน/โฮล และวัดเส้นกราฟ J-V และค่า EQE</p></div>
  </div>

      <div class="checkpoint-box" style="background:#fefce8; border:1px solid #fef08a; border-left:5px solid #eab308; padding:14px 18px; margin:24px 0 35px 0; border-radius:6px; page-break-inside:avoid;">
        <strong style="color:#854d0e; font-size:10pt;">🎯 จุดตรวจประเมินความเข้าใจและคำถามทบทวนประจำหัวข้อ 8.1 (Concept Checkpoint)</strong>
        <ul style="margin:8px 0 0 0; padding-left:20px; color:#713f12; font-size:9.5pt; line-height:1.8;">
          <li>จงอธิบายแนวคิดรวบยอดหลักของ เซลล์แสงอาทิตย์เพอรอฟสไกต์และนาโนเทคโนโลยีพลังงานแสง และความแตกต่างจากพฤติกรรมในระดับมหภาค</li>
          <li>พารามิเตอร์ใดเป็นปัจจัยวิกฤตที่ควบคุมสมบัติทางฟิสิกส์ในหัวข้อนี้ และมีผลกระทบอย่างไร?</li>
          <li>เชื่อมโยงหลักการฟิสิกส์ในหัวข้อนี้เข้ากับการประยุกต์ใช้จริงในเทคโนโลยีสมัยใหม่</li>
        </ul>
      </div>
    </div>
    
    <div class="topic-section">
      <h2>8.2 แบตเตอรี่โซลิดสเตตและซูเปอร์คาปาซิเตอร์ระดับนาโน</h2>
      <div class="topic-en-title">(Solid-State Lithium Batteries, Silicon Anodes & Nanostructured Supercapacitors)</div>
      
      <div class="topic-intro">
        <p>การปฏิวัติยานยนต์ไฟฟ้า (EVs) และระบบกักเก็บพลังงานหมุนเวียน (Grid Storage) จำเป็นต้องอาศัยอุปกรณ์กักเก็บพลังงานไฟฟ้าระดับนาโนยุคใหม่ที่มีความหนาแน่นพลังงานสูง ปลอดภัย ไม่ติดไฟ และชาร์จเร็วเป็นพิเศษ</p>
    <p>เทคโนโลยีชั้นนำประกอบด้วย: แบตเตอรี่ลิเทียมโซลิดสเตต (All-Solid-State Lithium Batteries: ASSBs) ซึ่งแทนที่อิเล็กโทรไลต์เหลวไวไฟด้วยอิเล็กโทรไลต์ของแข็งเซรามิกตัวนำไอออนลิเทียมความเร็วสูง เช่น ซัลไฟด์ $	ext{Li}_{10}	ext{GeP}_2	ext{S}_{12}$ (LGPS) หรือการ์เนต $	ext{Li}_7	ext{La}_3	ext{Zr}_2	ext{O}_{12}$ (LLZO) ที่มีสภาพนำไอออนสูงเกิน $10^{-2}	ext{ S/cm}$ ที่อุณหภูมิห้อง</p>
    <p>ควบคู่ไปกับ ขั้วแอโนดซิลิคอนระดับนาโน (Nanostructured Silicon Anodes) ที่ให้ความจุทางทฤษฎีสูงถึง $4,200	ext{ mAh/g}$ (สูงกว่ากราไฟต์เดิมกว่า 10 เท่า) โดยใช้อนุภาคนาโน ซิลิคอนแบบแกนกลวง (Yolk-Shell) เพื่อรองรับการขยายตัวทางปริมาตรกว่า $300\%$ โดยไม่แตกหัก และ ซูเปอร์คาปาซิเตอร์โครงสร้างนาโนคาร์บอน/MXene ที่ให้ความหนาแน่นกำลังไฟฟ้าสูงและชาร์จเต็มได้ภายในไม่กี่วินาที</p>
  </div>

      <div class="subtopic-block">
        <h3>ฟิสิกส์การขนส่งไอออนและพื้นที่ผิวรอยต่อของแข็ง-ของแข็ง (Solid-Solid Interfaces)</h3>
            <p>การแพร่ของไอออนลิเทียมในอิเล็กโทรไลต์ของแข็งอธิบายด้วยความสัมพันธ์ของเนิร์นสต์-ไอน์สไตน์: $\sigma_i = rac{n_i e^2 D_i}{k_B T}$</p>
    <p>ปัญหาความต้านทานรอยต่อระหว่างขั้วไฟฟ้าและอิเล็กโทรไลต์ของแข็ง (Interfacial Resistance) แก้ไขได้ด้วยการเคลือบฟิล์มบางระดับอะตอม ALD เช่น $	ext{LiNbO}_3$ หนา $2 - 5	ext{ nm}$ เพื่อป้องกันปฏิกิริยาข้างเคียงและการเติบโตของกิ่งก้านลิเทียมเดนไดรต์ (Lithium Dendrites)</p>
  </div>

      <div class="subtopic-block">
        <h3>ซูเปอร์คาปาซิเตอร์ไฟฟ้าเคมี: EDLC และ Pseudocapacitance ใน MXenes</h3>
            <p>1. Electrical Double-Layer Capacitors (EDLC): กักเก็บประจุด้วยไฟฟ้าสถิตที่ผิวหน้ากราฟีนหรือถ่านกัมมันต์รูพรุน ($C = rac{\epsilon A}{d}$)</p>
    <p>2. Pseudocapacitance ในวัสดุ 2D MXenes ($	ext{Ti}_3	ext{C}_2	ext{T}_x$): กักเก็บประจุผ่านปฏิกิริยารีดอกซ์ที่รวดเร็วบนผิวหน้า ทำให้ได้ความจุเชิงปริมาตรสูงถึง $1,500	ext{ F/cm}^3$</p>
  </div>
  <div class="formula-group">

        <div class="equation-box">
          <div class="equation-header">📌 สมการฟิสิกส์หลัก: สมการสภาพนำไอออนตามแบบจำลองอาร์เรเนียส</div>
          <div class="formula-math">$$\sigma_i T = \sigma_0 \exp\left( -\frac{E_a}{k_B T} \right), \qquad D_i = \frac{\sigma_i k_B T}{n_i e^2}$$</div>
          <p style="font-size:9.5pt; margin:4px 0 0 0; color:#334155; line-height:1.75; text-indent:0;"><strong>คำอธิบายตัวแปรและนัยสำคัญ:</strong> สภาพนำไอออนลิเทียมและสัมประสิทธิ์การแพร่</p>
        </div>
            
        <div class="equation-box">
          <div class="equation-header">📌 สมการฟิสิกส์หลัก: ความหนาแน่นพลังงานและกำลังไฟฟ้าในไดอะแกรมราโกน (Ragone Plot)</div>
          <div class="formula-math">$$E = \frac{1}{2} C V^2 \quad (\text{Wh/kg}), \qquad P = \frac{V^2}{4 R_{\text{ESR}}} \quad (\text{W/kg})$$</div>
          <p style="font-size:9.5pt; margin:4px 0 0 0; color:#334155; line-height:1.75; text-indent:0;"><strong>คำอธิบายตัวแปรและนัยสำคัญ:</strong> ความสัมพันธ์ระหว่างพลังงานและกำลังไฟฟ้า</p>
        </div>
              </div>

      <div class="table-block">
        <h3>📊 ตารางเปรียบเทียบเทคโนโลยีการกักเก็บพลังงานไฟฟ้า</h3>
        <table class="data-table">
          <thead><tr>
            <th>เทคโนโลยี</th><th>ความหนาแน่นพลังงาน (Wh/kg)</th><th>ความหนาแน่นกำลัง (W/kg)</th><th>อายุการใช้งาน (Cycles)</th><th>ความปลอดภัย</th></tr></thead>
<tbody><tr><td>Li-ion แบบดั้งเดิม (Liquid)</td><td>200 - 260 Wh/kg</td><td>250 - 500 W/kg</td><td>1,000 - 2,000</td><td>เสี่ยงต่อการลุกไหม้จากความร้อนสูง</td></tr><tr><td>Solid-State Battery (ASSB)</td><td>400 - 500 Wh/kg</td><td>1,000 - 2,500 W/kg</td><td>> 5,000</td><td>ปลอดภัยสูงสุด ไม่ติดไฟ ไม่รั่วไหล</td></tr><tr><td>Lithium-Sulfur (Li-S)</td><td>450 - 550 Wh/kg</td><td>500 - 1,000 W/kg</td><td>500 - 1,000</td><td>ปานกลาง (มีปัญหา Shuttle Effect)</td></tr><tr><td>MXene/Graphene Supercapacitor</td><td>30 - 80 Wh/kg</td><td>10,000 - 50,000 W/kg</td><td>> 100,000</td><td>ปลอดภัยสูงมาก ชาร์จเต็มใน 10 วินาที</td></tr></tbody></table>
</div>
  <div class="examples-group">

        <div class="example-box">
          <div class="example-header">
            <span>📝 ตัวอย่างการคำนวณที่ 8.3: การคำนวณความจุไฟฟ้าจำเพาะของขั้วแอโนดคอมโพสิต Silicon-Graphite</span>
            <span style="background:#dcfce7; color:#15803d; font-size:8.5pt; padding:3px 10px; border-radius:4px; font-weight:700;">Step-by-Step Worked Solution</span>
          </div>
          <p style="text-indent:0; margin-bottom:10px;"><strong>โจทย์ปัญหา (Problem Statement):</strong><br>ขั้วแอโนดประกอบด้วยอนุภาคนาโนซิลิคอน ($C_{	ext{Si}} = 4000	ext{ mAh/g}$) ในสัดส่วน $15	ext{ wt}\%$ ผสมกับกราไฟต์ ($C_{	ext{Gr}} = 372	ext{ mAh/g}$) ในสัดส่วน $85	ext{ wt}\%$ จงคำนวณหาความจุจำเพาะรวมของขั้วแอโนด $C_{	ext{total}}$</p>
          <div style="background:rgba(255,255,255,0.85); border:1px solid #e2e8f0; padding:12px 16px; border-radius:6px; margin:12px 0;">
            <strong style="color:#1e3a8a;">การวิเคราะห์และการคำนวณอย่างละเอียด:</strong><br>
            <p style="text-indent:0; margin:6px 0 0 0; line-height:1.85;">1. $C_{\text{total}} = (0.15 \times C_{\text{Si}}) + (0.85 \times C_{\text{Gr}})$<br>2. $C_{\text{total}} = (0.15 \times 4000) + (0.85 \times 372) = 600 + 316.2 = 916.2\text{ mAh/g}$</p>
          </div>
          <div style="background:#f0fdf4; border-left:4px solid #16a34a; padding:10px 14px; margin-top:10px; font-size:9.5pt; color:#166534; border-radius:0 6px 6px 0;">
            💡 <strong>นัยสำคัญทางกายภาพและการประยุกต์ใช้งาน (Physical Insight):</strong><br>
            <span style="color:#14532d;">การเติมซิลิคอนเพียง $15\%$ ช่วยเพิ่มความจุของขั้วแอโนดขึ้นเกือบ $2.5$ เท่าเมื่อเทียบกับกราไฟต์บริสุทธิ์</span>
          </div>
        </div>
            
        <div class="example-box">
          <div class="example-header">
            <span>📝 ตัวอย่างการคำนวณที่ 8.4: การคำนวณความหนาแน่นพลังงานของซูเปอร์คาปาซิเตอร์ 2D MXene</span>
            <span style="background:#dcfce7; color:#15803d; font-size:8.5pt; padding:3px 10px; border-radius:4px; font-weight:700;">Step-by-Step Worked Solution</span>
          </div>
          <p style="text-indent:0; margin-bottom:10px;"><strong>โจทย์ปัญหา (Problem Statement):</strong><br>ซูเปอร์คาปาซิเตอร์ใช้ขั้ว $	ext{Ti}_3	ext{C}_2	ext{T}_x$ MXene มีค่าความจุจำเพาะ $C = 350	ext{ F/g}$ ทำงานที่หน้าต่างแรงดันไฟฟ้า $V = 1.20	ext{ V}$ จงคำนวณหาความหนาแน่นพลังงานจำเพาะ $E$ ในหน่วย $	ext{Wh/kg}$</p>
          <div style="background:rgba(255,255,255,0.85); border:1px solid #e2e8f0; padding:12px 16px; border-radius:6px; margin:12px 0;">
            <strong style="color:#1e3a8a;">การวิเคราะห์และการคำนวณอย่างละเอียด:</strong><br>
            <p style="text-indent:0; margin:6px 0 0 0; line-height:1.85;">1. พลังงานในหน่วยจูลต่อกรัม: $E = \frac{1}{2} C V^2 = \frac{1}{2} (350\text{ F/g}) \times (1.20\text{ V})^2 = 252.0\text{ J/g} = 252,000\text{ J/kg}$<br>2. แปลงเป็น $\text{Wh/kg}$ ($1\text{ Wh} = 3600\text{ J}$): $E = \frac{252,000}{3600} = 70.0\text{ Wh/kg}$</p>
          </div>
          <div style="background:#f0fdf4; border-left:4px solid #16a34a; padding:10px 14px; margin-top:10px; font-size:9.5pt; color:#166534; border-radius:0 6px 6px 0;">
            💡 <strong>นัยสำคัญทางกายภาพและการประยุกต์ใช้งาน (Physical Insight):</strong><br>
            <span style="color:#14532d;">ความหนาแน่นพลังงาน $70	ext{ Wh/kg}$ สูงเทียบเท่าแบตเตอรี่ตะกั่ว-กรด แต่สามารถจ่ายกำลังไฟฟ้าสูงและชาร์จเต็มได้ในเวลาเพียงไม่กี่วินาที</span>
          </div>
        </div>
              </div>
  <div class="code-group">

        <div class="code-box">
          <div class="code-header">💻 แบบจำลองเชิงคำนวณภาษาไพทอน (Computational Python 3.11): กรณีศึกษา: แบตเตอรี่โซลิดสเตตรถยนต์ไฟฟ้าชาร์จเต็มใน 10 นาที (QuantumScape & Toyota)</div>
          <pre><code>การใช้อิเล็กโทรไลต์ของแข็งเซรามิกที่มีตัวคั่นแบบไร้แอโนด (Anode-less Solid-State Architecture) ช่วยเพิ่มระยะทางวิ่งของ EV เป็นกว่า 1,000 กิโลเมตรต่อการชาร์จหนึ่งครั้ง พร้อมความปลอดภัยจากการไม่ติดไฟ 100%</code></pre>
        </div>
        <p style="font-size:9.5pt; color:#475569; margin-top:-6px; margin-bottom:18px; text-indent:0;"><em>คำอธิบายอัลกอริทึมการจำลอง:</em> สคริปต์ไพทอนสำหรับการคำนวณและจำลองเชิงตัวเลข</p>
              </div>
  <div class="lab-connection-block">
    <h3>🔬 การเชื่อมโยงสู่ห้องปฏิบัติการเสมือนจริงและเทคนิคการทดลอง (Virtual Lab Connection)</h3>
    <div style='background:#f0fdf4; border:1px solid #bbf7d0; border-left:5px solid #16a34a; padding:12px 16px; margin-bottom:14px; border-radius:6px;'><strong style='color:#166534; font-size:10.5pt;'>การจำลองเส้นโค้งการชาร์จ-คายประจุและ Ragone Plot</strong><p style='margin:6px 0 0 0; color:#14532d; text-indent:0; line-height:1.8;'>battery_supercap_ragone.py</p></div>
  </div>
  <div class="cases-block">
    <h3>🌐 กรณีศึกษางานวิจัยแนวหน้าและนวัตกรรมอุตสาหกรรม (Frontier Case Studies)</h3>
    <div style='background:#eff6ff; border:1px solid #bfdbfe; border-left:5px solid #2563eb; padding:12px 16px; margin-bottom:14px; border-radius:6px;'><strong style='color:#1e40af; font-size:10.5pt;'>การเชื่อมโยงกับ Virtual Lab 37: การจำลองแบตเตอรี่โซลิดสเตตและซูเปอร์คาปาซิเตอร์ระดับนาโน</strong><p style='margin:6px 0 0 0; color:#1e3a8a; text-indent:0; line-height:1.8;'>ผู้เรียนสามารถเลือกชนิดอิเล็กโทรไลต์ของแข็งใน Lab 37 จำลองการเคลื่อนที่ของไอออนลิเทียม วัดเส้นโค้งการชาร์จ-คายประจุ และสร้างกราฟ Ragone Plot</p></div>
  </div>

      <div class="checkpoint-box" style="background:#fefce8; border:1px solid #fef08a; border-left:5px solid #eab308; padding:14px 18px; margin:24px 0 35px 0; border-radius:6px; page-break-inside:avoid;">
        <strong style="color:#854d0e; font-size:10pt;">🎯 จุดตรวจประเมินความเข้าใจและคำถามทบทวนประจำหัวข้อ 8.2 (Concept Checkpoint)</strong>
        <ul style="margin:8px 0 0 0; padding-left:20px; color:#713f12; font-size:9.5pt; line-height:1.8;">
          <li>จงอธิบายแนวคิดรวบยอดหลักของ แบตเตอรี่โซลิดสเตตและซูเปอร์คาปาซิเตอร์ระดับนาโน และความแตกต่างจากพฤติกรรมในระดับมหภาค</li>
          <li>พารามิเตอร์ใดเป็นปัจจัยวิกฤตที่ควบคุมสมบัติทางฟิสิกส์ในหัวข้อนี้ และมีผลกระทบอย่างไร?</li>
          <li>เชื่อมโยงหลักการฟิสิกส์ในหัวข้อนี้เข้ากับการประยุกต์ใช้จริงในเทคโนโลยีสมัยใหม่</li>
        </ul>
      </div>
    </div>
    
    <div class="topic-section">
      <h2>8.3 การเร่งปฏิกิริยาด้วยแสงระดับนาโนเพื่อพลังงานไฮโดรเจนและการบำบัดสิ่งแวดล้อม</h2>
      <div class="topic-en-title">(Photocatalytic Water Splitting, CO2 Reduction & Environmental Remediation)</div>
      
      <div class="topic-intro">
        <p>การเร่งปฏิกิริยาด้วยแสงระดับนาโน (Semiconductor Nanophotocatalysis) เป็นเทคโนโลยีสีเขียวที่แปลงพลังงานแสงอาทิตย์โดยตรงเป็นพลังงานเคมีสะอาดในรูปของ ก๊าซไฮโดรเจนสีเขียว (Green Hydrogen จากกระบวนการแยกน้ำด้วยแสง Solar Water Splitting) และการเปลี่ยนก๊าซคาร์บอนไดออกไซด์เป็นเชื้อเพลิงสังเคราะห์ (Solar Fuels: $	ext{CO}_2$ Reduction to Methane/Methanol)</p>
    <p>กระบวนการทางฟิสิกส์เริ่มต้นเมื่อสารกึ่งตัวนำนาโน (เช่น $	ext{TiO}_2, 	ext{g-C}_3	ext{N}_4, 	ext{BiVO}_4$) ดูดกลืนโฟตอนที่มีพลังงาน $h
u \ge E_g$ ทำให้อิเล็กตรอนถูกกระตุ้นขึ้นสู่แถบการนำ ($e_{	ext{CB}}^-$) และทิ้งโฮลไว้ในแถบเวเลนซ์ ($h_{	ext{VB}}^+$)</p>
    <p>เงื่อนไขทางอุณหพลศาสตร์ที่สำคัญคือ: ขอบแถบการนำ $E_{	ext{CB}}$ จะต้องอยู่สูงกว่าศักย์ไฟฟ้าการรีดิวซ์น้ำสร้างไฮโดรเจน ($E^\circ(	ext{H}^+/	ext{H}_2) = 0.0	ext{ V}$ เทียบกับ NHE) และขอบแถบเวเลนซ์ $E_{	ext{VB}}$ จะต้องอยู่ต่ำกว่าศักย์ไฟฟ้าการออกซิไดซ์น้ำสร้างออกซิเจน ($E^\circ(	ext{O}_2/	ext{H}_2	ext{O}) = +1.23	ext{ V}$ เทียบกับ NHE) โดยโครงสร้างเฮเทอโรแบบ Z-Scheme ช่วยแยกประจุและคงไว้ซึ่งพลังงานรีดอกซ์สูงสุด</p>
  </div>

      <div class="subtopic-block">
        <h3>โครงสร้างรอยต่อเฮเทอโรแบบ Z-Scheme สำหรับการแยกน้ำด้วยแสง</h3>
            <p>ในระบบ Z-Scheme อิเล็กตรอนจากสารกึ่งตัวนำตัวที่ 1 (Oxygen-Evolving Photocatalyst เช่น $	ext{BiVO}_4$) จะรวมตัวกับโฮลจากสารกึ่งตัวนำตัวที่ 2 (Hydrogen-Evolving Photocatalyst เช่น $	ext{g-C}_3	ext{N}_4$) ที่รอยต่อ</p>
    <p>ทำให้เหลืออิเล็กตรอนที่มีศักย์รีดิวซ์สูงที่สุดในตัวที่ 2 เพื่อผลิต $	ext{H}_2$ และเหลือโฮลที่มีศักย์ออกซิไดซ์แรงที่สุดในตัวที่ 1 เพื่อผลิต $	ext{O}_2$ เลียนแบบระบบสังเคราะห์แสงของพืชธรรมชาติ</p>
  </div>

      <div class="subtopic-block">
        <h3>การบำบัดมลพิษทางน้ำและอากาศด้วยอนุมูลอิสระว่องไวสูง (AOPs)</h3>
            <p>โฮลในแถบเวเลนซ์ ($h^+$) และอิเล็กตรอน ($e^-$) จะทำปฏิกิริยากับน้ำและออกซิเจนเพื่อสร้างอนุมูลไฮดรอกซิล ($\cdot	ext{OH}$, ศักย์ออกซิเดชันสูง $+2.8	ext{ V}$) และอนุมูลซูเปอร์ออกไซด์ ($\cdot	ext{O}_2^-$) ซึ่งสามารถย่อยสลายสารมลพิษอินทรีย์ตกค้าง ยาปฏิชีวนะ และฆ่าเชื้อแบคทีเรียได้อย่างสมบูรณ์กลายเป็น $	ext{CO}_2$ และ $	ext{H}_2	ext{O}$</p>
  </div>
  <div class="formula-group">

        <div class="equation-box">
          <div class="equation-header">📌 สมการฟิสิกส์หลัก: เงื่อนไขศักย์ไฟฟ้ารีดอกซ์สำหรับการแยกน้ำ</div>
          <div class="formula-math">$$E_{\text{CB}} < 0.00\text{ V vs. NHE}, \qquad E_{\text{VB}} > +1.23\text{ V vs. NHE}, \qquad E_g \ge 1.23\text{ eV}$$</div>
          <p style="font-size:9.5pt; margin:4px 0 0 0; color:#334155; line-height:1.75; text-indent:0;"><strong>คำอธิบายตัวแปรและนัยสำคัญ:</strong> เกณฑ์อุณหพลศาสตร์สำหรับการแยกน้ำด้วยแสงอาทิตย์</p>
        </div>
            
        <div class="equation-box">
          <div class="equation-header">📌 สมการฟิสิกส์หลัก: ประสิทธิภาพการแปลงแสงอาทิตย์เป็นไฮโดรเจน (Solar-to-Hydrogen: STH)</div>
          <div class="formula-math">$$\text{STH} = \frac{r_{\text{H2}} \times \Delta G^\circ}{P_{\text{in}} \times A} = \frac{r_{\text{H2}}\text{ (mol/s)} \times 237,000\text{ J/mol}}{P_{\text{in}}\text{ (W/m}^2) \times A\text{ (m}^2)} \times 100\%$$</div>
          <p style="font-size:9.5pt; margin:4px 0 0 0; color:#334155; line-height:1.75; text-indent:0;"><strong>คำอธิบายตัวแปรและนัยสำคัญ:</strong> การคำนวณประสิทธิภาพ STH มาตรฐาน</p>
        </div>
              </div>

      <div class="table-block">
        <h3>📊 ตารางสารเร่งปฏิกิริยาด้วยแสงระดับนาโนและตำแหน่งแถบพลังงาน</h3>
        <table class="data-table">
          <thead><tr>
            <th>สารกึ่งตัวนำ</th><th>Bandgap Eg (eV)</th><th>ขอบแถบ ECB (V vs NHE)</th><th>ขอบแถบ EVB (V vs NHE)</th><th>การดูดกลืนแสง</th></tr></thead>
<tbody><tr><td>TiO2 (Anatase)</td><td>3.20 eV</td><td>-0.20 V</td><td>+3.00 V</td><td>UV เท่านั้น (< 387 nm)</td></tr><tr><td>g-C3N4 (Graphitic Carbon Nitride)</td><td>2.70 eV</td><td>-1.10 V</td><td>+1.60 V</td><td>แสงขาวสีน้ำเงิน (< 460 nm)</td></tr><tr><td>BiVO4</td><td>2.40 eV</td><td>+0.02 V</td><td>+2.42 V</td><td>แสงขาวสีน้ำเงิน-เขียว (< 520 nm)</td></tr><tr><td>CdS Nanorods</td><td>2.40 eV</td><td>-0.52 V</td><td>+1.88 V</td><td>แสงขาว (< 516 nm)</td></tr><tr><td>Z-Scheme: g-C3N4 / BiVO4</td><td>Overall 2.4 eV</td><td>-1.10 V (สำหรับ H2)</td><td>+2.42 V (สำหรับ O2)</td><td>แสงขาวเต็มสเปกตรัม</td></tr></tbody></table>
</div>
  <div class="examples-group">

        <div class="example-box">
          <div class="example-header">
            <span>📝 ตัวอย่างการคำนวณที่ 8.5: การคำนวณประสิทธิภาพ Solar-to-Hydrogen (STH) ของแผงแยกน้ำด้วยแสง</span>
            <span style="background:#dcfce7; color:#15803d; font-size:8.5pt; padding:3px 10px; border-radius:4px; font-weight:700;">Step-by-Step Worked Solution</span>
          </div>
          <p style="text-indent:0; margin-bottom:10px;"><strong>โจทย์ปัญหา (Problem Statement):</strong><br>แผงโฟโตคะตาลิซิสพื้นที่ $A = 0.50	ext{ m}^2$ ภายใต้แสงอาทิตย์ $P_{	ext{in}} = 1000	ext{ W/m}^2$ ผลิตก๊าซไฮโดรเจนได้ในอัตรา $r_{	ext{H2}} = 2.0 	imes 10^{-5}	ext{ mol/s}$ จงคำนวณหาประสิทธิภาพ $	ext{STH}$</p>
          <div style="background:rgba(255,255,255,0.85); border:1px solid #e2e8f0; padding:12px 16px; border-radius:6px; margin:12px 0;">
            <strong style="color:#1e3a8a;">การวิเคราะห์และการคำนวณอย่างละเอียด:</strong><br>
            <p style="text-indent:0; margin:6px 0 0 0; line-height:1.85;">1. กำลังแสงตกกระทบทั้งหมด $P_{\text{total}} = P_{\text{in}} \times A = (1000\text{ W/m}^2) \times (0.50\text{ m}^2) = 500.0\text{ W}$<br>2. พลังงานเคมีของไฮโดรเจนที่ผลิตได้ ($\Delta G^\circ = 237\text{ kJ/mol}$): $P_{\text{chem}} = (2.0 \times 10^{-5}\text{ mol/s}) \times (237,000\text{ J/mol}) = 4.74\text{ W}$<br>3. $\text{STH} = \frac{P_{\text{chem}}}{P_{\text{total}}} \times 100\% = \frac{4.74\text{ W}}{500.0\text{ W}} \times 100\% = 0.948\% \approx 0.95\%$</p>
          </div>
          <div style="background:#f0fdf4; border-left:4px solid #16a34a; padding:10px 14px; margin-top:10px; font-size:9.5pt; color:#166534; border-radius:0 6px 6px 0;">
            💡 <strong>นัยสำคัญทางกายภาพและการประยุกต์ใช้งาน (Physical Insight):</strong><br>
            <span style="color:#14532d;">เป้าหมายของกระทรวงพลังงานสหรัฐ (DOE) สำหรับการใช้งานเชิงพาณิชย์คือ $	ext{STH} \ge 5 - 10\%$ ซึ่งโครงสร้างนาโน Z-Scheme ยุคใหม่กำลังเข้าใกล้เป้าหมายนี้</span>
          </div>
        </div>
            
        <div class="example-box">
          <div class="example-header">
            <span>📝 ตัวอย่างการคำนวณที่ 8.6: การคำนวณปริมาณไฮดรอกซิลแรดิคัลในการย่อยสลายยาปฏิชีวนะตกค้าง</span>
            <span style="background:#dcfce7; color:#15803d; font-size:8.5pt; padding:3px 10px; border-radius:4px; font-weight:700;">Step-by-Step Worked Solution</span>
          </div>
          <p style="text-indent:0; margin-bottom:10px;"><strong>โจทย์ปัญหา (Problem Statement):</strong><br>จงอธิบายกลไกทางเคมีไฟฟ้าที่ทำให้โฮลในแถบเวเลนซ์ของ $	ext{TiO}_2$ ($E_{	ext{VB}} = +3.00	ext{ V}$ vs. NHE) สามารถสร้าง $\cdot	ext{OH}$ จากน้ำ ($E^\circ(\cdot	ext{OH}/	ext{H}_2	ext{O}) = +2.73	ext{ V}$ vs. NHE)</p>
          <div style="background:rgba(255,255,255,0.85); border:1px solid #e2e8f0; padding:12px 16px; border-radius:6px; margin:12px 0;">
            <strong style="color:#1e3a8a;">การวิเคราะห์และการคำนวณอย่างละเอียด:</strong><br>
            <p style="text-indent:0; margin:6px 0 0 0; line-height:1.85;">เนื่องจากศักย์ไฟฟ้าของโฮล ($+3.00\text{ V}$) มีค่าเป็นบวกมากกว่าศักย์รีดอกซ์การเกิดอนุมูลไฮดรอกซิล ($+2.73\text{ V}$) ปฏิกิริยาการถ่ายโอนประจุ $h_{\text{VB}}^+ + \text{H}_2\text{O} \to \cdot\text{OH} + \text{H}^+$ จึงเกิดขึ้นได้เองทางอุณหพลศาสตร์ ($\Delta G < 0$)</p>
          </div>
          <div style="background:#f0fdf4; border-left:4px solid #16a34a; padding:10px 14px; margin-top:10px; font-size:9.5pt; color:#166534; border-radius:0 6px 6px 0;">
            💡 <strong>นัยสำคัญทางกายภาพและการประยุกต์ใช้งาน (Physical Insight):</strong><br>
            <span style="color:#14532d;">อนุมูล $\cdot	ext{OH}$ ที่เกิดขึ้นมีความสามารถในการออกซิไดซ์สูงมากจนสามารถทำลายวงแหวนแอโรแมติกของยาปฏิชีวนะตกค้างให้แตกตัวเป็นก๊าซ $	ext{CO}_2$ ได้อย่างสมบูรณ์</span>
          </div>
        </div>
              </div>
  <div class="code-group">

        <div class="code-box">
          <div class="code-header">💻 แบบจำลองเชิงคำนวณภาษาไพทอน (Computational Python 3.11): กรณีศึกษา: ฟาร์มแยกน้ำผลิตไฮโดรเจนจากแสงอาทิตย์ขนาด 100 ตารางเมตร (NEDO ประเทศญี่ปุ่น)</div>
          <pre><code>โครงการวิจัยของมหาวิทยาลัยโตเกียวและองค์กร NEDO ประสบความสำเร็จในการติดตั้งแผงคะตาลิสต์แยกน้ำขนาด 100 ตารางเมตร ทำงานต่อเนื่องกลางแจ้งนานหลายเดือนด้วยความปลอดภัยสูงและต้นทุนต่ำ</code></pre>
        </div>
        <p style="font-size:9.5pt; color:#475569; margin-top:-6px; margin-bottom:18px; text-indent:0;"><em>คำอธิบายอัลกอริทึมการจำลอง:</em> สคริปต์ไพทอนสำหรับการคำนวณและจำลองเชิงตัวเลข</p>
              </div>
  <div class="lab-connection-block">
    <h3>🔬 การเชื่อมโยงสู่ห้องปฏิบัติการเสมือนจริงและเทคนิคการทดลอง (Virtual Lab Connection)</h3>
    <div style='background:#f0fdf4; border:1px solid #bbf7d0; border-left:5px solid #16a34a; padding:12px 16px; margin-bottom:14px; border-radius:6px;'><strong style='color:#166534; font-size:10.5pt;'>การจำลองอัตราการผลิตก๊าซไฮโดรเจนจากแสงอาทิตย์</strong><p style='margin:6px 0 0 0; color:#14532d; text-indent:0; line-height:1.8;'>solar_hydrogen_sim.py</p></div>
  </div>
  <div class="cases-block">
    <h3>🌐 กรณีศึกษางานวิจัยแนวหน้าและนวัตกรรมอุตสาหกรรม (Frontier Case Studies)</h3>
    <div style='background:#eff6ff; border:1px solid #bfdbfe; border-left:5px solid #2563eb; padding:12px 16px; margin-bottom:14px; border-radius:6px;'><strong style='color:#1e40af; font-size:10.5pt;'>การเชื่อมโยงกับ Virtual Lab 38: การจำลองการแยกน้ำด้วยแสงและการบำบัดมลพิษ Photocatalysis</strong><p style='margin:6px 0 0 0; color:#1e3a8a; text-indent:0; line-height:1.8;'>ผู้เรียนสามารถเลือกคู่สารกึ่งตัวนำ Z-Scheme ใน Lab 38 ปรับความยาวคลื่นแสง และวัดอัตราการผลิตก๊าซไฮโดรเจนและออกซิเจนแบบเรียลไทม์</p></div>
  </div>

      <div class="checkpoint-box" style="background:#fefce8; border:1px solid #fef08a; border-left:5px solid #eab308; padding:14px 18px; margin:24px 0 35px 0; border-radius:6px; page-break-inside:avoid;">
        <strong style="color:#854d0e; font-size:10pt;">🎯 จุดตรวจประเมินความเข้าใจและคำถามทบทวนประจำหัวข้อ 8.3 (Concept Checkpoint)</strong>
        <ul style="margin:8px 0 0 0; padding-left:20px; color:#713f12; font-size:9.5pt; line-height:1.8;">
          <li>จงอธิบายแนวคิดรวบยอดหลักของ การเร่งปฏิกิริยาด้วยแสงระดับนาโนเพื่อพลังงานไฮโดรเจนและการบำบัดสิ่งแวดล้อม และความแตกต่างจากพฤติกรรมในระดับมหภาค</li>
          <li>พารามิเตอร์ใดเป็นปัจจัยวิกฤตที่ควบคุมสมบัติทางฟิสิกส์ในหัวข้อนี้ และมีผลกระทบอย่างไร?</li>
          <li>เชื่อมโยงหลักการฟิสิกส์ในหัวข้อนี้เข้ากับการประยุกต์ใช้จริงในเทคโนโลยีสมัยใหม่</li>
        </ul>
      </div>
    </div>
    
    <div class="topic-section">
      <h2>8.4 พิษวิทยานาโนและความปลอดภัยต่อสิ่งแวดล้อมและสุขภาพ</h2>
      <div class="topic-en-title">(Nanotoxicology, Reactive Oxygen Species (ROS) & Cellular Biokinetics)</div>
      
      <div class="topic-intro">
        <p>การขยายตัวอย่างก้าวกระโดดของการผลิตและการใช้วัสดุนาโนในเชิงพาณิชย์ ทำให้สาขาวิชา พิษวิทยานาโน (Nanotoxicology) มีความสำคัญอย่างยิ่งยวดในการศึกษาผลกระทบทางชีววิทยา กลไกความเป็นพิษ และจลนศาสตร์การสะสมของอนุภาคนาโนในสิ่งมีชีวิตและสิ่งแวดล้อม (Environmental Health and Safety: EHS)</p>
    <p>กลไกความเป็นพิษหลักของวัสดุนาโนในระดับเซลล์เกิดจาก: การสร้างอนุมูลอิสระออกซิเจนที่ว่องไวเกินขนาด (Reactive Oxygen Species: ROS Generation เช่น $\cdot	ext{O}_2^-, 	ext{H}_2	ext{O}_2, \cdot	ext{OH}$) ที่กระตุ้นให้เกิด ภาวะเครียดออกซิเดชัน (Oxidative Stress), การทำลายเยื่อหุ้มเซลล์และเยื่อหุ้มไมโทคอนเดรีย (Lipid Peroxidation), การทำลายสายดีเอ็นเอ (DNA Damage), และการกระตุ้นการอักเสบเรื้อรัง (Chronic Inflammation)</p>
    <p>นอกจากนี้ อนุภาคนาโนเมื่อเข้าสู่กระแสเลือดจะถูกห่อหุ้มด้วยชั้นโปรตีนชีวภาพโดยธรรมชาติ ก่อให้เกิด 'โคโรนาโปรตีน' (Protein Corona) ซึ่งเปลี่ยนตัวตนทางชีววิทยา (Biological Identity) ของอนุภาค และกำหนดเส้นทางการกระจายตัวในอวัยวะ (Biodistribution) การดูดซึมเข้าสู่เซลล์ และอัตราการขับออกจากร่างกาย</p>
  </div>

      <div class="subtopic-block">
        <h3>กลไกการสร้าง ROS และผลกระทบต่อไมโทคอนเดรีย</h3>
            <p>1. ปฏิกิริยาคล้ายเฟนตัน (Fenton-like Reactions) บนผิวอนุภาคโลหะทรานซิชัน: $	ext{Fe}^{2+} + 	ext{H}_2	ext{O}_2 	o 	ext{Fe}^{3+} + \cdot	ext{OH} + 	ext{OH}^-$</p>
    <p>2. การถ่ายโอนอิเล็กตรอนระหว่างแถบพลังงานของสารกึ่งตัวนำกับระบบรีดอกซ์ของเซลล์ ก่อให้เกิดการรบกวนห่วงโซ่การถ่ายทอดอิเล็กตรอนในไมโทคอนเดรีย นำไปสู่การสูญเสียศักย์เยื่อหุ้ม ($\Delta \Psi_m$) และกระตุ้นวิถีการตายแบบ Apoptosis</p>
  </div>

      <div class="subtopic-block">
        <h3>พลศาสตร์ของ Protein Corona: Hard Corona vs Soft Corona</h3>
            <p>1. Hard Corona: ชั้นในสุดที่โปรตีนที่มีสัมพรรคภาพสูง (High Affinity เช่น Albumin, Apolipoprotein, Fibrinogen) ยึดเกาะแน่นหนาและอยู่ติดทนนานหลายชั่วโมง</p>
    <p>2. Soft Corona: ชั้นนอกที่โปรตีนยึดเกาะอย่างอ่อนๆ และเกิดการแลกเปลี่ยนกับสิ่งแวดล้อมอย่างต่อเนื่องตามเอฟเฟกต์ของวิญาล (Vroman Effect)</p>
  </div>
  <div class="formula-group">

        <div class="equation-box">
          <div class="equation-header">📌 สมการฟิสิกส์หลัก: ปฏิกิริยาฮาเบอร์-ไวสส์และการสร้าง ROS</div>
          <div class="formula-math">$$\cdot\text{O}_2^- + \text{H}_2\text{O}_2 \xrightarrow{\text{Fe/Cu Catalyst}} \text{O}_2 + \cdot\text{OH} + \text{OH}^-$$</div>
          <p style="font-size:9.5pt; margin:4px 0 0 0; color:#334155; line-height:1.75; text-indent:0;"><strong>คำอธิบายตัวแปรและนัยสำคัญ:</strong> การเร่งการสร้างอนุมูลอิสระพิษรุนแรงโดยอนุภาคนาโน</p>
        </div>
            
        <div class="equation-box">
          <div class="equation-header">📌 สมการฟิสิกส์หลัก: จลนศาสตร์การดูดซับโปรตีนโคโรนา (Vroman Effect)</div>
          <div class="formula-math">$$\theta_i(t) = \frac{k_{\text{on}, i} C_i}{k_{\text{off}, i} + \sum k_{\text{on}, j} C_j} \left( 1 - e^{-t/\tau_i} \right)$$</div>
          <p style="font-size:9.5pt; margin:4px 0 0 0; color:#334155; line-height:1.75; text-indent:0;"><strong>คำอธิบายตัวแปรและนัยสำคัญ:</strong> การแข่งขันแย่งชิงพื้นที่ผิวอนุภาคของโปรตีนในเลือด</p>
        </div>
              </div>

      <div class="table-block">
        <h3>📊 ตารางลักษณะทางกายภาพที่ส่งผลต่อความเป็นพิษของอนุภาคนาโน</h3>
        <table class="data-table">
          <thead><tr>
            <th>พารามิเตอร์ของอนุภาค</th><th>ลักษณะที่เพิ่มความเป็นพิษ</th><th>กลไกผลกระทบทางชีวภาพ</th></tr></thead>
<tbody><tr><td>ขนาดอนุภาค (Size)</td><td>เล็กมาก (< 10 - 20 nm)</td><td>พื้นที่ผิวสูงมาก แทรกผ่านเยื่อหุ้มเซลล์และนิวเคลียสได้</td></tr><tr><td>รูปร่าง (Shape)</td><td>เส้นใยยาว อัตราส่วนสูง (High Aspect Ratio)</td><td>เกิดภาวะ Phagocytosis ล้มเหลว คล้ายแร่ใยหิน (Asbestos-like)</td></tr><tr><td>ประจุพื้นผิว (Surface Charge)</td><td>ประจุบวกสูง (High Positive Zeta Potential)</td><td>จับกับเยื่อหุ้มเซลล์ประจุลบ ทำลายผนังเซลล์</td></tr><tr><td>ความสามารถในการละลาย (Dissolution)</td><td>ปล่อยไอออนโลหะพิษ (Cd2+, Zn2+, Ag+, Cu2+)</td><td>รบกวนสมดุลไอออนและยับยั้งการทำงานของเอนไซม์</td></tr><tr><td>กิจกรรมเร่งปฏิกิริยาแสง (Photocatalysis)</td><td>เกิดอิเล็กตรอน-โฮลเมื่อโดนแสง UV</td><td>สร้าง ROS ปริมาณมหาศาลทำลายเซลล์ผิวหนัง</td></tr></tbody></table>
</div>
  <div class="examples-group">

        <div class="example-box">
          <div class="example-header">
            <span>📝 ตัวอย่างการคำนวณที่ 8.7: การคำนวณพื้นที่ผิวจำเพาะและอัตราการปลดปล่อยไอออนพิษ</span>
            <span style="background:#dcfce7; color:#15803d; font-size:8.5pt; padding:3px 10px; border-radius:4px; font-weight:700;">Step-by-Step Worked Solution</span>
          </div>
          <p style="text-indent:0; margin-bottom:10px;"><strong>โจทย์ปัญหา (Problem Statement):</strong><br>อนุภาคนาโนสังกะสีออกไซด์ ($	ext{ZnO}$, $ho = 5.61	ext{ g/cm}^3$) มีขนาดเส้นผ่านศูนย์กลาง $d_1 = 10.0	ext{ nm}$ และ $d_2 = 100.0	ext{ nm}$ จงคำนวณหา (ก) พื้นที่ผิวจำเพาะ $	ext{SSA}$ ของทั้งสองขนาด (ข) อัตราส่วนพื้นที่ผิว $SSA_1 / SSA_2$</p>
          <div style="background:rgba(255,255,255,0.85); border:1px solid #e2e8f0; padding:12px 16px; border-radius:6px; margin:12px 0;">
            <strong style="color:#1e3a8a;">การวิเคราะห์และการคำนวณอย่างละเอียด:</strong><br>
            <p style="text-indent:0; margin:6px 0 0 0; line-height:1.85;">1. $\text{SSA}_1 = \frac{6}{\rho d_1} = \frac{6}{(5.61 \times 10^6\text{ g/m}^3) \times (10 \times 10^{-9}\text{ m})} = \frac{6}{0.0561} = 106.95\text{ m}^2/\text{g}$<br>2. $\text{SSA}_2 = \frac{6}{\rho d_2} = \frac{6}{(5.61 \times 10^6) \times (100 \times 10^{-9})} = 10.70\text{ m}^2/\text{g}$<br>3. อัตราส่วน $\frac{\text{SSA}_1}{\text{SSA}_2} = \frac{106.95}{10.70} = 10.0$</p>
          </div>
          <div style="background:#f0fdf4; border-left:4px solid #16a34a; padding:10px 14px; margin-top:10px; font-size:9.5pt; color:#166534; border-radius:0 6px 6px 0;">
            💡 <strong>นัยสำคัญทางกายภาพและการประยุกต์ใช้งาน (Physical Insight):</strong><br>
            <span style="color:#14532d;">อนุภาคขนาด 10 nm มีพื้นที่สัมผัสกับเซลล์และอัตราการปลดปล่อยไอออน $	ext{Zn}^{2+}$ สูงกว่าอนุภาคขนาด 100 nm ถึง 10 เท่า</span>
          </div>
        </div>
            
        <div class="example-box">
          <div class="example-header">
            <span>📝 ตัวอย่างการคำนวณที่ 8.8: การวิเคราะห์ศักย์ซีตา (Zeta Potential) และความเสถียรของคอลลอยด์</span>
            <span style="background:#dcfce7; color:#15803d; font-size:8.5pt; padding:3px 10px; border-radius:4px; font-weight:700;">Step-by-Step Worked Solution</span>
          </div>
          <p style="text-indent:0; margin-bottom:10px;"><strong>โจทย์ปัญหา (Problem Statement):</strong><br>อนุภาคนาโนทองคำที่เคลือบด้วยซิเตรตมีค่าศักย์ซีตา $\zeta = -42.0	ext{ mV}$ ในน้ำบริสุทธิ์ เมื่อเติมเกลือ $	ext{NaCl}$ จนความเข้มข้นสูง ค่าศักย์ซีตาลดลงเหลือ $\zeta = -12.0	ext{ mV}$ จงวิเคราะห์ความเสถียรของอนุภาค</p>
          <div style="background:rgba(255,255,255,0.85); border:1px solid #e2e8f0; padding:12px 16px; border-radius:6px; margin:12px 0;">
            <strong style="color:#1e3a8a;">การวิเคราะห์และการคำนวณอย่างละเอียด:</strong><br>
            <p style="text-indent:0; margin:6px 0 0 0; line-height:1.85;">1. ตามเกณฑ์ DLVO: อนุภาคที่มี $|\zeta| > 30\text{ mV}$ จะมีความเสถียรสูงเนื่องจากแรงผลักทางไฟฟ้าสถิตเอาชนะแรงดึงดูดฟานเดอร์วาลส์<br>2. เมื่อ $|\zeta| = 12\text{ mV} < 20\text{ mV}$ แรงผลักไฟฟ้าสถิตลดลงจนไม่เพียงพอ</p>
          </div>
          <div style="background:#f0fdf4; border-left:4px solid #16a34a; padding:10px 14px; margin-top:10px; font-size:9.5pt; color:#166534; border-radius:0 6px 6px 0;">
            💡 <strong>นัยสำคัญทางกายภาพและการประยุกต์ใช้งาน (Physical Insight):</strong><br>
            <span style="color:#14532d;">อนุภาคจะเกิดการเกาะกลุ่มรวมตัวกัน (Agglomeration) และตกตะกอน ส่งผลให้สีของสารละลายเปลี่ยนจากสีแดงเป็นสีม่วง-น้ำเงิน</span>
          </div>
        </div>
              </div>
  <div class="code-group">

        <div class="code-box">
          <div class="code-header">💻 แบบจำลองเชิงคำนวณภาษาไพทอน (Computational Python 3.11): กรณีศึกษา: การสั่งห้ามใช้ไทเทเนียมไดออกไซด์ (E171 / TiO2 Nanoparticles) ในอาหารของสหภาพยุโรป (EFSA, 2022)</div>
          <pre><code>องค์การความปลอดภัยด้านอาหารแห่งยุโรป (EFSA) ประกาศยกเลิกการใช้ $	ext{TiO}_2$ เป็นสารปรุงแต่งอาหาร เนื่องจากไม่สามารถตัดข้อกังวลเรื่องความเป็นพิษต่อสารพันธุกรรม (Genotoxicity) และการสะสมในลำไส้ของอนุภาคนาโนได้</code></pre>
        </div>
        <p style="font-size:9.5pt; color:#475569; margin-top:-6px; margin-bottom:18px; text-indent:0;"><em>คำอธิบายอัลกอริทึมการจำลอง:</em> สคริปต์ไพทอนสำหรับการคำนวณและจำลองเชิงตัวเลข</p>
              </div>
  <div class="lab-connection-block">
    <h3>🔬 การเชื่อมโยงสู่ห้องปฏิบัติการเสมือนจริงและเทคนิคการทดลอง (Virtual Lab Connection)</h3>
    <div style='background:#f0fdf4; border:1px solid #bbf7d0; border-left:5px solid #16a34a; padding:12px 16px; margin-bottom:14px; border-radius:6px;'><strong style='color:#166534; font-size:10.5pt;'>การจำลองระดับความเข้มข้น ROS และการตายของเซลล์ตามขนาดยา</strong><p style='margin:6px 0 0 0; color:#14532d; text-indent:0; line-height:1.8;'>nanotox_ros_dose_response.py</p></div>
  </div>
  <div class="cases-block">
    <h3>🌐 กรณีศึกษางานวิจัยแนวหน้าและนวัตกรรมอุตสาหกรรม (Frontier Case Studies)</h3>
    <div style='background:#eff6ff; border:1px solid #bfdbfe; border-left:5px solid #2563eb; padding:12px 16px; margin-bottom:14px; border-radius:6px;'><strong style='color:#1e40af; font-size:10.5pt;'>การเชื่อมโยงกับ Virtual Lab 39: การจำลองพิษวิทยานาโน การเกิด ROS และจลนศาสตร์ Protein Corona</strong><p style='margin:6px 0 0 0; color:#1e3a8a; text-indent:0; line-height:1.8;'>ผู้เรียนสามารถปรับขนาด รูปร่าง ประจุพื้นผิวของอนุภาคนาโนใน Lab 39 และติดตามการเกิดภาวะเครียดออกซิเดชัน ROS และการรอดชีวิตของเซลล์</p></div>
  </div>

      <div class="checkpoint-box" style="background:#fefce8; border:1px solid #fef08a; border-left:5px solid #eab308; padding:14px 18px; margin:24px 0 35px 0; border-radius:6px; page-break-inside:avoid;">
        <strong style="color:#854d0e; font-size:10pt;">🎯 จุดตรวจประเมินความเข้าใจและคำถามทบทวนประจำหัวข้อ 8.4 (Concept Checkpoint)</strong>
        <ul style="margin:8px 0 0 0; padding-left:20px; color:#713f12; font-size:9.5pt; line-height:1.8;">
          <li>จงอธิบายแนวคิดรวบยอดหลักของ พิษวิทยานาโนและความปลอดภัยต่อสิ่งแวดล้อมและสุขภาพ และความแตกต่างจากพฤติกรรมในระดับมหภาค</li>
          <li>พารามิเตอร์ใดเป็นปัจจัยวิกฤตที่ควบคุมสมบัติทางฟิสิกส์ในหัวข้อนี้ และมีผลกระทบอย่างไร?</li>
          <li>เชื่อมโยงหลักการฟิสิกส์ในหัวข้อนี้เข้ากับการประยุกต์ใช้จริงในเทคโนโลยีสมัยใหม่</li>
        </ul>
      </div>
    </div>
    
    <div class="topic-section">
      <h2>8.5 จริยธรรม กฎหมาย และการออกแบบความปลอดภัยตั้งแต่ต้น</h2>
      <div class="topic-en-title">(Safe-by-Design (SbD), Nanotechnology Regulation & Global Ethics)</div>
      
      <div class="topic-intro">
        <p>เพื่อให้การพัฒนาวิทยาศาสตร์และเทคโนโลยีนาโนเป็นไปอย่างยั่งยืนและได้รับความไว้วางใจจากสังคม จึงเกิดแนวคิดการออกแบบความปลอดภัยตั้งแต่ต้น (Safe-by-Design: SbD) ซึ่งเป็นกระบวนการบูรณาการการประเมินความเสี่ยงและมาตรการควบคุมความปลอดภัยเข้าสู่ขั้นตอนการวิจัยและพัฒนาผลิตภัณฑ์นาโนตั้งแต่วันแรก</p>
    <p>หลักการ SbD ครอบคลุมตลอดทั้งวงจรชีวิตของผลิตภัณฑ์ (Life Cycle Assessment: LCA) ตั้งแต่การคัดเลือกวัตถุดิบทางเลือกที่ไม่เป็นพิษ (Green Synthesis), การดัดแปรพื้นผิวเพื่อลดการสร้างอนุมูลอิสระ (Surface Passivation), การควบคุมไม่ให้อนุภาคฟุ้งกระจายในสายการผลิต, ไปจนถึงการบำบัดของเสียและการรีไซเคิลอย่างปลอดภัย</p>
    <p>ในระดับสากล องค์กรระหว่างประเทศ เช่น OECD, ISO (ISO/TC 229 Nanotechnologies), US-EPA, และ EU-REACH ได้กำหนดกรอบระเบียบข้อบังคับและมาตรฐานการติดฉลากผลิตภัณฑ์นาโน (Nano-Labeling) พร้อมทั้งวางแนวทางจริยธรรมสากลเพื่อป้องกันช่องว่างความเหลื่อมล้ำทางเทคโนโลยี (Nano-Divide) และความเสี่ยงจากการใช้งานในทางที่ผิดทางชีวภาพและการทหาร</p>
  </div>

      <div class="subtopic-block">
        <h3>เสาหลัก 3 ประการของกรอบแนวคิด Safe-by-Design (SbD)</h3>
            <p>1. วัสดุที่ปลอดภัย (Safe Materials): ปรับแต่งคุณสมบัติภายใน เช่น ขนาด รูปร่าง โครงสร้างผลึก และสารเคลือบผิวเพื่อขจัดความเป็นพิษ</p>
    <p>2. กระบวนการผลิตที่ปลอดภัย (Safe Production): ใช้ระบบปิด (Closed-loop Systems) การควบคุมในสภาวะของเหลว และอุปกรณ์ป้องกันส่วนบุคคลระดับมาตรฐาน (PAPR, HEPA Filtration)</p>
    <p>3. การใช้งานและการสิ้นสุดวงจรชีวิตที่ปลอดภัย (Safe Use & End-of-Life): ยึดตรึงอนุภาคนาโนไว้ในเมทริกซ์แข็ง (Matrix Immobilization) เพื่อป้องกันการหลุดรอดสู่สิ่งแวดล้อม</p>
  </div>

      <div class="subtopic-block">
        <h3>มิติจริยธรรม กฎหมาย และผลกระทบต่อสังคม (ELSI in Nanotechnology)</h3>
            <p>การประเมินผลกระทบด้านสิทธิส่วนบุคคลจากการใช้นาโนเซนเซอร์สอดแนม, การเข้าถึงยารักษาโรคนาโนอย่างเท่าเทียม, และการกำกับดูแลความปลอดภัยของอนุภาคนาโนสังเคราะห์ในเครื่องสำอางและอาหาร</p>
  </div>
  <div class="formula-group">

        <div class="equation-box">
          <div class="equation-header">📌 สมการฟิสิกส์หลัก: สมการประเมินความเสี่ยงทางพิษวิทยา (Risk Assessment Equation)</div>
          <div class="formula-math">$$\text{Risk} = \text{Hazard (ความเป็นอันตราย)} \times \text{Exposure (ระดับการสัมผัส)}$$</div>
          <p style="font-size:9.5pt; margin:4px 0 0 0; color:#334155; line-height:1.75; text-indent:0;"><strong>คำอธิบายตัวแปรและนัยสำคัญ:</strong> หลักการลดความเสี่ยงโดยลด Hazard ด้วย SbD หรือลด Exposure</p>
        </div>
            
        <div class="equation-box">
          <div class="equation-header">📌 สมการฟิสิกส์หลัก: ดัชนีการประเมินวัฏจักรชีวิตสิ่งแวดล้อม (Life Cycle Assessment)</div>
          <div class="formula-math">$$\text{Eco-Impact} = \sum_{i} m_i \times \text{Characterization Factor}_i$$</div>
          <p style="font-size:9.5pt; margin:4px 0 0 0; color:#334155; line-height:1.75; text-indent:0;"><strong>คำอธิบายตัวแปรและนัยสำคัญ:</strong> การประเมินผลกระทบต่อสิ่งแวดล้อมตลอดวงจรชีวิต</p>
        </div>
              </div>

      <div class="table-block">
        <h3>📊 ตารางมาตรฐานสากลและองค์กรกำกับดูแลนาโนเทคโนโลยี</h3>
        <table class="data-table">
          <thead><tr>
            <th>มาตรฐาน / กฎหมาย</th><th>องค์กรกำกับดูแล</th><th>ขอบเขตการบังคับใช้</th><th>ข้อกำหนดสำคัญ</th></tr></thead>
<tbody><tr><td>EU REACH Annexes for Nanomaterials</td><td>ECHA (สหภาพยุโรป)</td><td>สารเคมีและผลิตภัณฑ์นาโนทุกชนิด</td><td>ต้องลงทะเบียนข้อมูลคุณลักษณะนาโนเฉพาะ</td></tr><tr><td>ISO/TC 229</td><td>ISO สากล</td><td>คำศัพท์ มาตรวิทยา ความปลอดภัย</td><td>มาตรฐานวิธีวัดขนาดและทดสอบพิษวิทยา</td></tr><tr><td>TSCA Section 5 / SNUR</td><td>US EPA (สหรัฐอเมริกา)</td><td>สารเคมีใหม่ระดับนาโน</td><td>ต้องแจ้งล่วงหน้าก่อนผลิต/นำเข้า 90 วัน</td></tr><tr><td>OECD Mutual Acceptance of Data</td><td>OECD</td><td>ข้อมูลความปลอดภัยสากล</td><td>แนวทางการทดสอบพิษวิทยามาตรฐานที่เป็นที่ยอมรับร่วมกัน</td></tr></tbody></table>
</div>
  <div class="examples-group">

        <div class="example-box">
          <div class="example-header">
            <span>📝 ตัวอย่างการคำนวณที่ 8.9: การคำนวณการลดความเสี่ยงตามหลักการ Safe-by-Design</span>
            <span style="background:#dcfce7; color:#15803d; font-size:8.5pt; padding:3px 10px; border-radius:4px; font-weight:700;">Step-by-Step Worked Solution</span>
          </div>
          <p style="text-indent:0; margin-bottom:10px;"><strong>โจทย์ปัญหา (Problem Statement):</strong><br>อนุภาคนาโนชนิดเดิมมีคะแนนความเป็นอันตราย $	ext{Hazard}_1 = 8.0$ และคะแนนการสัมผัสในโรงงาน $	ext{Exposure}_1 = 6.0$ ($	ext{Risk}_1 = 48.0$) เมื่อนำหลักการ SbD มาใช้โดยการเคลือบผิวด้วยพอลิเมอร์ชีวภาพทำให้ Hazard ลดลงเหลือ $2.0$ และติดตั้งระบบกรองอากาศ HEPA ทำให้ Exposure ลดลงเหลือ $1.5$ จงคำนวณคะแนนความเสี่ยงใหม่ $	ext{Risk}_2$ และร้อยละการลดความเสี่ยง</p>
          <div style="background:rgba(255,255,255,0.85); border:1px solid #e2e8f0; padding:12px 16px; border-radius:6px; margin:12px 0;">
            <strong style="color:#1e3a8a;">การวิเคราะห์และการคำนวณอย่างละเอียด:</strong><br>
            <p style="text-indent:0; margin:6px 0 0 0; line-height:1.85;">1. $\text{Risk}_2 = \text{Hazard}_2 \times \text{Exposure}_2 = 2.0 \times 1.5 = 3.0$<br>2. ร้อยละการลดความเสี่ยง: $\frac{\text{Risk}_1 - \text{Risk}_2}{\text{Risk}_1} \times 100\% = \frac{48.0 - 3.0}{48.0} \times 100\% = \frac{45.0}{48.0} \times 100\% = 93.75\%$</p>
          </div>
          <div style="background:#f0fdf4; border-left:4px solid #16a34a; padding:10px 14px; margin-top:10px; font-size:9.5pt; color:#166534; border-radius:0 6px 6px 0;">
            💡 <strong>นัยสำคัญทางกายภาพและการประยุกต์ใช้งาน (Physical Insight):</strong><br>
            <span style="color:#14532d;">การบูรณาการทั้งการปรับแต่งวัสดุและการควบคุมกระบวนการผลิตช่วยลดความเสี่ยงโดยรวมลงได้มากกว่า $93\%$</span>
          </div>
        </div>
            
        <div class="example-box">
          <div class="example-header">
            <span>📝 ตัวอย่างการคำนวณที่ 8.1: การประเมินประสิทธิภาพของระบบกรองอากาศดักจับอนุภาคนาโน (HEPA Filtration)</span>
            <span style="background:#dcfce7; color:#15803d; font-size:8.5pt; padding:3px 10px; border-radius:4px; font-weight:700;">Step-by-Step Worked Solution</span>
          </div>
          <p style="text-indent:0; margin-bottom:10px;"><strong>โจทย์ปัญหา (Problem Statement):</strong><br>ระบบกรองอากาศ HEPA Class H14 มีประสิทธิภาพการดักจับอนุภาคขนาดวิกฤต ($0.3	ext{ }\mu	ext{m}$) เท่ากับ $99.995\%$ หากในห้องปฏิบัติการมีอนุภาคนาโนฟุ้งกระจาย $N_{	ext{in}} = 10^8	ext{ particles/m}^3$ จงคำนวณจำนวนอนุภาคที่หลุดรอดผ่านแผ่นกรอง $N_{	ext{out}}$</p>
          <div style="background:rgba(255,255,255,0.85); border:1px solid #e2e8f0; padding:12px 16px; border-radius:6px; margin:12px 0;">
            <strong style="color:#1e3a8a;">การวิเคราะห์และการคำนวณอย่างละเอียด:</strong><br>
            <p style="text-indent:0; margin:6px 0 0 0; line-height:1.85;">1. อัตราการหลุดรอด: $P = 1.0 - 0.99995 = 0.00005 = 5.0 \times 10^{-5}$<br>2. $N_{\text{out}} = N_{\text{in}} \times P = 10^8 \times (5.0 \times 10^{-5}) = 5,000\text{ particles/m}^3$</p>
          </div>
          <div style="background:#f0fdf4; border-left:4px solid #16a34a; padding:10px 14px; margin-top:10px; font-size:9.5pt; color:#166534; border-radius:0 6px 6px 0;">
            💡 <strong>นัยสำคัญทางกายภาพและการประยุกต์ใช้งาน (Physical Insight):</strong><br>
            <span style="color:#14532d;">จำนวนอนุภาคที่หลุดรอดลดลงเหลือเพียง 5,000 อนุภาคต่อลูกบาศก์เมตร ซึ่งอยู่ในเกณฑ์มาตรฐานความปลอดภัยสำหรับห้องคลีนรูม</span>
          </div>
        </div>
              </div>
  <div class="code-group">

        <div class="code-box">
          <div class="code-header">💻 แบบจำลองเชิงคำนวณภาษาไพทอน (Computational Python 3.11): กรณีศึกษา: โครงการนาโนเทคโนโลยีปลอดภัยแห่งสหภาพยุโรป (EU Horizon NanoSafety Cluster & NANORIGO)</div>
          <pre><code>การจัดทำระบบฐานข้อมูลความปลอดภัยและเครื่องมือประเมินความเสี่ยงออนไลน์ระดับสากล เพื่อสนับสนุนผู้ประกอบการสตาร์ทอัพและโรงงานอุตสาหกรรมในการพัฒนาผลิตภัณฑ์นาโนตามมาตรฐาน Safe-and-Sustainable-by-Design (SSbD)</code></pre>
        </div>
        <p style="font-size:9.5pt; color:#475569; margin-top:-6px; margin-bottom:18px; text-indent:0;"><em>คำอธิบายอัลกอริทึมการจำลอง:</em> สคริปต์ไพทอนสำหรับการคำนวณและจำลองเชิงตัวเลข</p>
              </div>
  <div class="lab-connection-block">
    <h3>🔬 การเชื่อมโยงสู่ห้องปฏิบัติการเสมือนจริงและเทคนิคการทดลอง (Virtual Lab Connection)</h3>
    <div style='background:#f0fdf4; border:1px solid #bbf7d0; border-left:5px solid #16a34a; padding:12px 16px; margin-bottom:14px; border-radius:6px;'><strong style='color:#166534; font-size:10.5pt;'>การจำลองเมทริกซ์การประเมินความเสี่ยงและ Safe-by-Design</strong><p style='margin:6px 0 0 0; color:#14532d; text-indent:0; line-height:1.8;'>safe_by_design_matrix.py</p></div>
  </div>
  <div class="cases-block">
    <h3>🌐 กรณีศึกษางานวิจัยแนวหน้าและนวัตกรรมอุตสาหกรรม (Frontier Case Studies)</h3>
    <div style='background:#eff6ff; border:1px solid #bfdbfe; border-left:5px solid #2563eb; padding:12px 16px; margin-bottom:14px; border-radius:6px;'><strong style='color:#1e40af; font-size:10.5pt;'>การเชื่อมโยงกับ Virtual Lab 40: การจำลองการออกแบบความปลอดภัยตั้งแต่ต้น Safe-by-Design และการประเมินความเสี่ยง</strong><p style='margin:6px 0 0 0; color:#1e3a8a; text-indent:0; line-height:1.8;'>ผู้เรียนสามารถออกแบบกระบวนการผลิตนาโนที่ปลอดภัยใน Lab 40 ประเมินคะแนนความเสี่ยงตามมาตรฐาน OECD และทดสอบการจัดการวงจรชีวิตผลิตภัณฑ์</p></div>
  </div>

      <div class="checkpoint-box" style="background:#fefce8; border:1px solid #fef08a; border-left:5px solid #eab308; padding:14px 18px; margin:24px 0 35px 0; border-radius:6px; page-break-inside:avoid;">
        <strong style="color:#854d0e; font-size:10pt;">🎯 จุดตรวจประเมินความเข้าใจและคำถามทบทวนประจำหัวข้อ 8.5 (Concept Checkpoint)</strong>
        <ul style="margin:8px 0 0 0; padding-left:20px; color:#713f12; font-size:9.5pt; line-height:1.8;">
          <li>จงอธิบายแนวคิดรวบยอดหลักของ จริยธรรม กฎหมาย และการออกแบบความปลอดภัยตั้งแต่ต้น และความแตกต่างจากพฤติกรรมในระดับมหภาค</li>
          <li>พารามิเตอร์ใดเป็นปัจจัยวิกฤตที่ควบคุมสมบัติทางฟิสิกส์ในหัวข้อนี้ และมีผลกระทบอย่างไร?</li>
          <li>เชื่อมโยงหลักการฟิสิกส์ในหัวข้อนี้เข้ากับการประยุกต์ใช้จริงในเทคโนโลยีสมัยใหม่</li>
        </ul>
      </div>
    </div>
    

      <div class="summary-box">
        <h3 style="color:#1e40af; margin-top:0; font-size:13pt;">📋 สรุปสาระสำคัญประจำบทที่ 8 (Chapter 8 Key Takeaways)</h3>
        <ul style="margin:0; padding-left:22px; font-size:10pt; line-height:1.95; color:#1e293b;">
          <li style='margin-bottom:8px;'>เซลล์แสงอาทิตย์เพอรอฟสไกต์และแทนเดมซิลิคอน-เพอรอฟสไกต์ให้ประสิทธิภาพทะลุ 33.9% ก้าวข้ามขีดจำกัดช็อกคลีย์-ไควเซอร์</li><li style='margin-bottom:8px;'>แบตเตอรี่โซลิดสเตต (ASSBs) และขั้วแอโนดซิลิคอนนาโนให้ความหนาแน่นพลังงานสูง ปลอดภัย ไม่ติดไฟ ร่วมกับซูเปอร์คาปาซิเตอร์ MXene ชาร์จเร็ว</li><li style='margin-bottom:8px;'>การเร่งปฏิกิริยาด้วยแสง Z-Scheme แปลงพลังงานแสงอาทิตย์เป็นก๊าซไฮโดรเจนสะอาด และบำบัดมลพิษด้วยอนุมูลอิสระไฮดรอกซิล</li><li style='margin-bottom:8px;'>พิษวิทยานาโนศึกษาภาวะเครียดออกซิเดชัน (ROS), การทำลายเยื่อหุ้มเซลล์ และพลศาสตร์ของ Protein Corona</li><li style='margin-bottom:8px;'>กรอบแนวคิด Safe-by-Design (SbD) บูรณาการความปลอดภัยตลอดวงจรชีวิตผลิตภัณฑ์ พร้อมกฎระเบียบสากล OECD/ISO เพื่อการพัฒนาอย่างยั่งยืน</li>
        </ul>
      </div>

      <div class="problems-section">
        <h3 style="color:#0f172a; margin-top:0; font-size:14pt; border-bottom:2px solid #cbd5e1; padding-bottom:8px;">
          📚 แบบฝึกหัดและโจทย์ปัญหาท้ายบทที่ 8 (End-of-Chapter Problems)
        </h3>
        
        <h4 style="color:#1e3a8a; font-size:11.5pt; margin-top:18px;">ตอนที่ 1: คำถามเชิงมโนทัศน์และการวิเคราะห์เชิงฟิสิกส์ (Conceptual & Analytical Questions)</h4>
        <ol style="padding-left:22px; font-size:10pt; line-height:1.9; color:#334155;">
          <li style='margin-bottom:8px;'>จงอธิบายดัชนี Goldschmidt Tolerance Factor ในการทำนายความเสถียรของโครงสร้างผลึกเพอรอฟสไกต์</li><li style='margin-bottom:8px;'>เพราะเหตุใดเซลล์แสงอาทิตย์แบบแทนเดม Perovskite-Silicon จึงมีประสิทธิภาพสูงกว่าเซลล์รอยต่อเดี่ยว?</li><li style='margin-bottom:8px;'>จงอธิบายข้อดีของอิเล็กโทรไลต์ของแข็งเซรามิกในแบตเตอรี่โซลิดสเตตเมื่อเทียบกับอิเล็กโทรไลต์เหลวเดิม</li><li style='margin-bottom:8px;'>เพราะเหตุใดขั้วแอโนดซิลิคอนระดับนาโนจึงต้องออกแบบโครงสร้างเป็นแบบ Yolk-Shell?</li><li style='margin-bottom:8px;'>จงอธิบายเงื่อนไขทางอุณหพลศาสตร์ของแถบพลังงานในการแยกน้ำด้วยแสงอาทิตย์ (Water Splitting)</li><li style='margin-bottom:8px;'>ระบบ Z-Scheme Photocatalysis มีข้อได้เปรียบอย่างไรในการแยกประจุและคงศักย์รีดอกซ์?</li><li style='margin-bottom:8px;'>อนุมูลอิสระ Reactive Oxygen Species (ROS) ถูกสร้างขึ้นได้อย่างไรบนผิวของอนุภาคนาโน และทำลายเซลล์อย่างไร?</li><li style='margin-bottom:8px;'>จงอธิบายหลักการ 3 ประการของ Safe-by-Design (SbD) ในการพัฒนาผลิตภัณฑ์นาโนเทคโนโลยี</li>
        </ol>

        <h4 style="color:#166534; font-size:11.5pt; margin-top:22px;">ตอนที่ 2: โจทย์ปัญหาการคำนวณเชิงตัวเลขและการพิสูจน์ (Quantitative & Numerical Problems)</h4>
        <ol style="padding-left:22px; font-size:10pt; line-height:1.9; color:#334155;">
          <li style='margin-bottom:8px;'>คำนวณ Goldschmidt Tolerance Factor ของ $	ext{CsPbBr}_3$ กำหนด $r_{	ext{Cs}} = 0.188	ext{ nm}$, $r_{	ext{Pb}} = 0.119	ext{ nm}$, $r_{	ext{Br}} = 0.196	ext{ nm}$</li><li style='margin-bottom:8px;'>เซลล์เพอรอฟสไกต์ให้ $J_{	ext{sc}} = 26.0	ext{ mA/cm}^2$, $V_{	ext{oc}} = 1.20	ext{ V}$, $	ext{FF} = 0.83$ ภายใต้แสง $100	ext{ mW/cm}^2$ จงคำนวณค่า PCE</li><li style='margin-bottom:8px;'>ขั้วแอโนดคอมโพสิตมีซิลิคอน ($4000	ext{ mAh/g}$) $20	ext{ wt}\%$ ผสมกราไฟต์ ($372	ext{ mAh/g}$) $80	ext{ wt}\%$ จงคำนวณความจุจำเพาะรวม</li><li style='margin-bottom:8px;'>ซูเปอร์คาปาซิเตอร์ MXene มี $C = 400	ext{ F/g}$ ทำงานที่ $1.4	ext{ V}$ จงคำนวณความหนาแน่นพลังงานจำเพาะในหน่วย $	ext{Wh/kg}$</li><li style='margin-bottom:8px;'>แผงคะตาลิสต์พื้นที่ $1.0	ext{ m}^2$ รับแสง $1000	ext{ W/m}^2$ ผลิตไฮโดรเจนได้ $5.0 	imes 10^{-5}	ext{ mol/s}$ จงคำนวณประสิทธิภาพ STH</li><li style='margin-bottom:8px;'>อนุภาคนาโนทองคำทรงกลม ($ho = 19.3	ext{ g/cm}^3$) ขนาดเส้นผ่านศูนย์กลาง 15 nm จงคำนวณพื้นที่ผิวจำเพาะ SSA</li><li style='margin-bottom:8px;'>ระบบกรองอากาศ HEPA ดักจับอนุภาคได้ $99.99\%$ เมื่อมีฝุ่นนาโนเข้ามา $2.0 	imes 10^7	ext{ particles/m}^3$ จงคำนวณจำนวนอนุภาคที่หลุดรอด</li>
        </ol>

        <h4 style="color:#7c2d12; font-size:11.5pt; margin-top:22px;">ตอนที่ 3: โจทย์ประยุกต์ การออกแบบเชิงวิศวกรรม และการจำลอง (Applied Design & Modeling Problems)</h4>
        <ol style="padding-left:22px; font-size:10pt; line-height:1.9; color:#334155;">
          <li style='margin-bottom:8px;'>จงออกแบบแผงเซลล์แสงอาทิตย์ Perovskite-Silicon Tandem ความกว้าง 2 เมตรสำหรับติดตั้งบนหลังคารถยนต์ไฟฟ้า</li><li style='margin-bottom:8px;'>ออกแบบระบบแบตเตอรี่โซลิดสเตตลิเทียมเมทัลขนาด 100 kWh สำหรับอากาศยานพลังงานไฟฟ้า (eVTOL)</li><li style='margin-bottom:8px;'>วิเคราะห์แนวทางการนำกรอบ Safe-by-Design มาใช้ในโรงงานผลิตอนุภาคนาโนคาร์บอนควอนตัมดอทระดับอุตสาหกรรม</li><li style='margin-bottom:8px;'>เขียนโค้ด Python เพื่อคำนวณและพล็อตกราฟประสิทธิภาพ STH เทียบกับอัตราการผลิตก๊าซไฮโดรเจนที่ความเข้มแสงต่างๆ</li>
        </ol>
      </div>
    </div>
    """
