# -*- coding: utf-8 -*-
"""
Chapter 3: การสังเคราะห์และกระบวนการประดิษฐ์ระดับนาโน
Nanofabrication, Chemical Synthesis, EUV Lithography, ALD & Self-Assembly Mechanics
"""

def get_chapter_3():
    return r"""
    <div class="chapter-container">
      <div class="chapter-hero">
        <div class="chapter-badge">CHAPTER 03 • NANOTECHNOLOGICAL PHYSICS</div>
        <h1 class="chapter-title">การสังเคราะห์และกระบวนการประดิษฐ์ระดับนาโน</h1>
        <p class="chapter-subtitle">Nanofabrication, Chemical Synthesis, EUV Lithography, ALD & Self-Assembly Mechanics</p>
      </div>

      <div class="diagram-wrap">
        <img src="../assets/diagrams/ch03_nanofabrication.svg" alt="การสังเคราะห์และกระบวนการประดิษฐ์ระดับนาโน">
        <div class="caption">ภาพที่ 3.1 แผนภาพเปรียบเทียบ Bottom-Up vs Top-Down, เครื่องสแกนเนอร์ EUV, กลไก ALD สองขั้นตอน และการจัดตัวของ SAMs บนทองคำ</div>
      </div>

      
    <div class="topic-section">
      <h2>3.1 การสังเคราะห์แบบล่างขึ้นบน: วิถีทางเคมีและการเติบโตของผลึก</h2>
      <div class="topic-en-title">(Bottom-Up Chemical Synthesis & LaMer Crystal Growth)</div>
      
      <div class="topic-intro">
        <p>กระบวนการสังเคราะห์แบบล่างขึ้นบน (Bottom-Up Approach) เป็นแนวทางการสร้างโครงสร้างนาโนโดยเริ่มจากการประกอบอะตอม ไอออน หรือโมเลกุลเดี่ยวเข้าด้วยกันผ่านปฏิกิริยาเคมีและแรงระหว่างโมเลกุล จนเติบโตเป็นอนุภาคนาโนหรือผลึกที่มีขนาด รูปร่าง และโครงสร้างผลึกที่กำหนดไว้อย่างแม่นยำ</p>
    <p>ทฤษฎีพื้นฐานที่อธิบายการกำเนิดผลึกนาโนในสารละลายคือแบบจำลองของลาแมร์ (LaMer Nucleation and Growth Model) ซึ่งแบ่งกระบวนการออกเป็น 3 ขั้นตอนหลัก: การสะสมความเข้มข้นของมอนอเมอร์จนเกินจุดอิ่มตัวยิ่งยวด (Supersaturation), การเกิดนิวเคลียสอย่างรวดเร็วในช่วงเวลาสั้นๆ (Burst Nucleation), และการเติบโตของผลึกผ่านการแพร่ของมอนอเมอร์ (Diffusion-Controlled Growth)</p>
    <p>การแยกขั้นตอนการเกิดนิวเคลียสออกจากการเติบโตของผลึกอย่างเด็ดขาดเป็นกุญแจสำคัญในการได้อนุภาคนาโนที่มีการกระจายขนาดแคบมาก (Monodisperse Nanoparticles) ซึ่งมีความเบี่ยงเบนมาตรฐานต่ำกว่า 5% เหมาะสำหรับงานออปโตอิเล็กทรอนิกส์และการแพทย์แม่นยำ</p>
  </div>

      <div class="subtopic-block">
        <h3>แบบจำลองของลาแมร์และการเติบโตแบบออสวาลด์ริเพนนิ่ง (Ostwald Ripening)</h3>
            <p>1. ระยะที่ 1: ความเข้มข้นมอนอเมอร์ $C$ เพิ่มขึ้นจนถึงจุดอิ่มตัวยิ่งยวดวิกฤต $C_{	ext{min}}^{	ext{nucl}}$</p>
    <p>2. ระยะที่ 2: เกิดนิวเคลียสพร้อมกันอย่างรวดเร็ว (Burst Nucleation) ทำให้ความเข้มข้น $C$ ลดลงต่ำกว่า $C_{	ext{min}}^{	ext{nucl}}$ อย่างฉับพลันเพื่อหยุดการเกิดนิวเคลียสใหม่</p>
    <p>3. ระยะที่ 3: นิวเคลียสเดิมเติบโตอย่างสม่ำเสมอ หากปล่อยให้ทำปฏิกิริยานานเกินไปจะเกิด Ostwald Ripening ซึ่งอนุภาคเล็กจะละลายไปพอกพูนให้อนุภาคใหญ่ ทำให้การกระจายขนาดกว้างขึ้น</p>
  </div>

      <div class="subtopic-block">
        <h3>บทบาทของสารลดแรงตึงผิวและลิแกนด์แคปปิ้ง (Capping Ligands)</h3>
            <p>การใช้โมเลกุลลิแกนด์ เช่น Oleic Acid, TOP/TOPO หรือ PVP เข้าไปจับกับพื้นผิวผลึกจำเพาะหน้า ช่วยควบคุมรูปร่างผลึกให้เป็นทรงกลม, แท่งนาโน (Nanorods), แผ่นนาโน (Nanoplatelets), หรือรูปดาว (Nanostars)</p>
  </div>
  <div class="formula-group">

        <div class="equation-box">
          <div class="equation-header">📌 สมการฟิสิกส์หลัก: รัศมีวิกฤตของการเกิดนิวเคลียสทรงกลม</div>
          <div class="formula-math">$$r^* = \frac{2 \gamma V_m}{k_B T \ln S}, \qquad \Delta G^* = \frac{16 \pi \gamma^3 V_m^2}{3 (k_B T \ln S)^2}$$</div>
          <p style="font-size:9.5pt; margin:4px 0 0 0; color:#334155; line-height:1.75; text-indent:0;"><strong>คำอธิบายตัวแปรและนัยสำคัญ:</strong> รัศมีวิกฤตและพลังงานกระตุ้นในการเกิดนิวเคลียส</p>
        </div>
            
        <div class="equation-box">
          <div class="equation-header">📌 สมการฟิสิกส์หลัก: อัตราส่วนความอิ่มตัวยิ่งยวด (Supersaturation Ratio)</div>
          <div class="formula-math">$$S = \frac{C}{C_0}, \qquad \frac{dr}{dt} = \frac{D V_m (C_b - C_r)}{r}$$</div>
          <p style="font-size:9.5pt; margin:4px 0 0 0; color:#334155; line-height:1.75; text-indent:0;"><strong>คำอธิบายตัวแปรและนัยสำคัญ:</strong> อัตราส่วนความอิ่มตัวยิ่งยวดและอัตราการเติบโตของผลึก</p>
        </div>
              </div>

      <div class="table-block">
        <h3>📊 ตารางเปรียบเทียบวิธีการสังเคราะห์แบบ Bottom-Up ในสารละลาย</h3>
        <table class="data-table">
          <thead><tr>
            <th>เทคนิค</th><th>สารตั้งต้น</th><th>อุณหภูมิปฏิกิริยา</th><th>ข้อดี</th><th>ตัวอย่างผลิตภัณฑ์</th></tr></thead>
<tbody><tr><td>Hot-Injection Method</td><td>Organometallic Precursors</td><td>150 - 320 °C</td><td>ได้ Monodisperse QD คุณภาพสูงสุด</td><td>CdSe, InP, CsPbBr3 QDs</td></tr><tr><td>Hydrothermal/Solvothermal</td><td>เกลือโลหะในหม้อนึ่งความดัน</td><td>120 - 250 °C</td><td>ความดันสูง ได้ผลึกบริสุทธิ์สูง</td><td>TiO2, ZnO, Fe3O4 Nanorods</td></tr><tr><td>Sol-Gel Processing</td><td>Metal Alkoxides (TEOS)</td><td>25 - 100 °C</td><td>ทำเป็นฟิล์มและแอโรเจลรูพรุนได้ดี</td><td>SiO2, TiO2 Nanoparticles</td></tr><tr><td>Co-precipitation</td><td>เกลือคลอไรด์/ซัลเฟตในด่าง</td><td>25 - 80 °C</td><td>สังเคราะห์ได้ปริมาณมาก ต้นทุนต่ำ</td><td>Superparamagnetic Iron Oxide</td></tr></tbody></table>
</div>
  <div class="examples-group">

        <div class="example-box">
          <div class="example-header">
            <span>📝 ตัวอย่างการคำนวณที่ 3.1: การคำนวณรัศมีวิกฤตของการเกิดนิวเคลียส CdSe</span>
            <span style="background:#dcfce7; color:#15803d; font-size:8.5pt; padding:3px 10px; border-radius:4px; font-weight:700;">Step-by-Step Worked Solution</span>
          </div>
          <p style="text-indent:0; margin-bottom:10px;"><strong>โจทย์ปัญหา (Problem Statement):</strong><br>ในการสังเคราะห์ CdSe QD ที่อุณหภูมิ $T = 573	ext{ K}$ (300 °C) มีอัตราส่วนความอิ่มตัวยิ่งยวด $S = 8.0$ กำหนดพลังงานพื้นผิว $\gamma = 0.25	ext{ J/m}^2$ และปริมาตรโมลาร์ $V_m = 3.29 	imes 10^{-5}	ext{ m}^3/	ext{mol}$ จงคำนวณหารัศมีวิกฤต $r^*$</p>
          <div style="background:rgba(255,255,255,0.85); border:1px solid #e2e8f0; padding:12px 16px; border-radius:6px; margin:12px 0;">
            <strong style="color:#1e3a8a;">การวิเคราะห์และการคำนวณอย่างละเอียด:</strong><br>
            <p style="text-indent:0; margin:6px 0 0 0; line-height:1.85;">1. คำนวณเทอม $k_B T \ln S = (1.3806 \times 10^{-23}) \times 573 \times \ln(8.0) = 1.646 \times 10^{-20}\text{ J}$<br>2. แปลง $V_m$ ต่อโมเลกุล: $v_m = \frac{V_m}{N_A} = \frac{3.29 \times 10^{-5}}{6.022 \times 10^{23}} = 5.463 \times 10^{-29}\text{ m}^3$<br>3. $r^* = \frac{2 \gamma v_m}{k_B T \ln S} = \frac{2(0.25)(5.463 \times 10^{-29})}{1.646 \times 10^{-20}} = 1.659 \times 10^{-9}\text{ m} = 1.66\text{ nm}$</p>
          </div>
          <div style="background:#f0fdf4; border-left:4px solid #16a34a; padding:10px 14px; margin-top:10px; font-size:9.5pt; color:#166534; border-radius:0 6px 6px 0;">
            💡 <strong>นัยสำคัญทางกายภาพและการประยุกต์ใช้งาน (Physical Insight):</strong><br>
            <span style="color:#14532d;">นิวเคลียสที่มีรัศมีใหญ่กว่า $1.66	ext{ nm}$ จะมีความเสถียรและเติบโตต่อไปเป็นผลึกนาโน ส่วนที่เล็กกว่าจะละลายกลับคืน</span>
          </div>
        </div>
            
        <div class="example-box">
          <div class="example-header">
            <span>📝 ตัวอย่างการคำนวณที่ 3.2: การควบคุมรูปร่างแท่งนาโนทองคำ (Gold Nanorods) ด้วยสารลดแรงตึงผิว CTAB</span>
            <span style="background:#dcfce7; color:#15803d; font-size:8.5pt; padding:3px 10px; border-radius:4px; font-weight:700;">Step-by-Step Worked Solution</span>
          </div>
          <p style="text-indent:0; margin-bottom:10px;"><strong>โจทย์ปัญหา (Problem Statement):</strong><br>จงอธิบายกลไกทางฟิสิกส์เคมีที่ทำให้โมเลกุล CTAB ชี้นำการเติบโตของอนุภาคทองคำให้กลายเป็นแท่งนาโนที่มีอัตราส่วนกว้างยาว (Aspect Ratio) สูง</p>
          <div style="background:rgba(255,255,255,0.85); border:1px solid #e2e8f0; padding:12px 16px; border-radius:6px; margin:12px 0;">
            <strong style="color:#1e3a8a;">การวิเคราะห์และการคำนวณอย่างละเอียด:</strong><br>
            <p style="text-indent:0; margin:6px 0 0 0; line-height:1.85;">โมเลกุล CTAB เป็นสารลดแรงตึงผิวที่มีประจุบวก จะเข้าไปดูดซับอย่างจำเพาะเจาะจงบนระนาบผลึก $\{110\}$ และ $\{100\}$ ของทองคำ แต่ไม่เกาะบนระนาบ $\{111\}$ ที่ปลายแท่ง ทำให้ไอออนทองคำสามารถเข้าพอกพูนได้เฉพาะที่ปลายทั้งสองข้าง เกิดการเติบโตตามแกนยาวในทิศทาง $[001]$</p>
          </div>
          <div style="background:#f0fdf4; border-left:4px solid #16a34a; padding:10px 14px; margin-top:10px; font-size:9.5pt; color:#166534; border-radius:0 6px 6px 0;">
            💡 <strong>นัยสำคัญทางกายภาพและการประยุกต์ใช้งาน (Physical Insight):</strong><br>
            <span style="color:#14532d;">การปรับอัตราส่วน $	ext{AgNO}_3$ ในปฏิกิริยาช่วยให้สามารถปรับ Aspect Ratio ได้ตั้งแต่ 2 ถึง 10 ซึ่งเปลี่ยนพีค LSPR จาก 650 nm ไปจนถึง 1100 nm</span>
          </div>
        </div>
              </div>
  <div class="code-group">

        <div class="code-box">
          <div class="code-header">💻 แบบจำลองเชิงคำนวณภาษาไพทอน (Computational Python 3.11): กรณีศึกษา: โรงงานผลิตจุดควอนตัมปลอดแคดเมียม (InP/ZnSe/ZnS) มาตรฐานอุตสาหกรรม</div>
          <pre><code>บริษัท Nanosys และ Samsung ใช้กระบวนการ Hot-Injection แบบอัตโนมัติในการผลิตควอนตัมดอท InP คุณภาพสูงระดับตันต่อปี เพื่อใช้เป็นแผ่นฟิล์มเพิ่มประสิทธิภาพสีในจอทีวีระดับไฮเอนด์</code></pre>
        </div>
        <p style="font-size:9.5pt; color:#475569; margin-top:-6px; margin-bottom:18px; text-indent:0;"><em>คำอธิบายอัลกอริทึมการจำลอง:</em> สคริปต์ไพทอนสำหรับการคำนวณและจำลองเชิงตัวเลข</p>
              </div>
  <div class="lab-connection-block">
    <h3>🔬 การเชื่อมโยงสู่ห้องปฏิบัติการเสมือนจริงและเทคนิคการทดลอง (Virtual Lab Connection)</h3>
    <div style='background:#f0fdf4; border:1px solid #bbf7d0; border-left:5px solid #16a34a; padding:12px 16px; margin-bottom:14px; border-radius:6px;'><strong style='color:#166534; font-size:10.5pt;'>การจำลองแบบจำลองของลาแมร์</strong><p style='margin:6px 0 0 0; color:#14532d; text-indent:0; line-height:1.8;'>lamer_nucleation_sim.py</p></div>
  </div>
  <div class="cases-block">
    <h3>🌐 กรณีศึกษางานวิจัยแนวหน้าและนวัตกรรมอุตสาหกรรม (Frontier Case Studies)</h3>
    <div style='background:#eff6ff; border:1px solid #bfdbfe; border-left:5px solid #2563eb; padding:12px 16px; margin-bottom:14px; border-radius:6px;'><strong style='color:#1e40af; font-size:10.5pt;'>การเชื่อมโยงกับ Virtual Lab 11: การสังเคราะห์อนุภาคนาโนคอลลอยด์และการเติบโตตามแบบจำลองลาแมร์</strong><p style='margin:6px 0 0 0; color:#1e3a8a; text-indent:0; line-height:1.8;'>ผู้เรียนสามารถควบคุมความเร็วในการฉีดสารตั้งต้น อุณหภูมิ และความเข้มข้นลิแกนด์ใน Lab 11 เพื่อสังเกตการเกิด Burst Nucleation และการเปลี่ยนสีของสารละลาย</p></div>
  </div>

      <div class="checkpoint-box" style="background:#fefce8; border:1px solid #fef08a; border-left:5px solid #eab308; padding:14px 18px; margin:24px 0 35px 0; border-radius:6px; page-break-inside:avoid;">
        <strong style="color:#854d0e; font-size:10pt;">🎯 จุดตรวจประเมินความเข้าใจและคำถามทบทวนประจำหัวข้อ 3.1 (Concept Checkpoint)</strong>
        <ul style="margin:8px 0 0 0; padding-left:20px; color:#713f12; font-size:9.5pt; line-height:1.8;">
          <li>จงอธิบายแนวคิดรวบยอดหลักของ การสังเคราะห์แบบล่างขึ้นบน: วิถีทางเคมีและการเติบโตของผลึก และความแตกต่างจากพฤติกรรมในระดับมหภาค</li>
          <li>พารามิเตอร์ใดเป็นปัจจัยวิกฤตที่ควบคุมสมบัติทางฟิสิกส์ในหัวข้อนี้ และมีผลกระทบอย่างไร?</li>
          <li>เชื่อมโยงหลักการฟิสิกส์ในหัวข้อนี้เข้ากับการประยุกต์ใช้จริงในเทคโนโลยีสมัยใหม่</li>
        </ul>
      </div>
    </div>
    
    <div class="topic-section">
      <h2>3.2 การสังเคราะห์แบบบนลงล่าง: ลิโธกราฟีด้วยลำแสงอิเล็กตรอนและโฟตอน</h2>
      <div class="topic-en-title">(Top-Down Lithography: Extreme UV & Electron Beam Lithography)</div>
      
      <div class="topic-intro">
        <p>กระบวนการสังเคราะห์แบบบนลงล่าง (Top-Down Approach) คือการแกะสลักและลดขนาดชิ้นงานขนาดใหญ่ให้กลายเป็นลวดลายระดับนาโนเมตรด้วยเทคโนโลยีลิโธกราฟี (Lithography) และการกัดรอย (Etching) ซึ่งเป็นหัวใจสำคัญของอุตสาหกรรมเซมิคอนดักเตอร์และไมโครโปรเซสเซอร์ระดับโลก</p>
    <p>ขีดจำกัดการเลี้ยวเบนของแสงตามเกณฑ์ของเรย์ลี (Rayleigh Criterion: $	ext{CD} = k_1 rac{\lambda}{	ext{NA}}$) ได้ผลักดันให้เกิดการเปลี่ยนผ่านจากโฟโตลิโธกราฟีย่านรังสีอัลตราไวโอเลตลึก (Deep UV: $\lambda = 193	ext{ nm}$) สู่ระบบอัลตราไวโอเลตสุญญากาศยิ่งยวด (Extreme UV: EUV ที่ $\lambda = 13.5	ext{ nm}$) ซึ่งใช้แหล่งกำเนิดแสงเลเซอร์พลาสมาดีบุก (Sn Plasma) และระบบกระจกสะท้อนแสงมัลติเลเยอร์ Mo/Si</p>
    <p>สำหรับงานวิจัยระดับห้องปฏิบัติการ ลิโธกราฟีด้วยลำแสงอิเล็กตรอน (Electron Beam Lithography: EBL) เป็นเครื่องมือหลักที่สามารถสร้างลวดลายขนาดเล็กต่ำกว่า 10 นาโนเมตรได้โดยตรง (Direct-Write) เนื่องจากความยาวคลื่นเดอบรอยล์ของอิเล็กตรอนพลังงานสูงสั้นเพียงเศษส่วนของพิโกเมตร</p>
  </div>

      <div class="subtopic-block">
        <h3>เกณฑ์การแยกชัดของเรย์ลีและเทคนิค Resolution Enhancement Technologies (RET)</h3>
            <p>ขนาดวิกฤตขั้นต่ำ (Critical Dimension: CD): $	ext{CD} = k_1 rac{\lambda}{	ext{NA}}$ และระยะชัดลึก (Depth of Focus: DOF): $	ext{DOF} = k_2 rac{\lambda}{	ext{NA}^2}$</p>
    <p>เทคนิคเพิ่มความละเอียดได้แก่ Optical Proximity Correction (OPC), Phase-Shift Masks (PSM), Immersion Lithography (ใช้น้ำบริสุทธิ์ $n = 1.44$), และการสร้างลวดลายซ้ำซ้อน (Multi-Patterning: SADP, SAQP)</p>
  </div>

      <div class="subtopic-block">
        <h3>ฟิสิกส์การกระเจิงของอิเล็กตรอนใน EBL และ Proximity Effect</h3>
            <p>อิเล็กตรอนที่ยิงลงบนฟิล์มโฟโตรีซิสต์ (เช่น PMMA) จะเกิดการกระเจิงไปข้างหน้า (Forward Scattering) และการกระเจิงสะท้อนกลับจากแผ่นรองรับ (Backscattering) ก่อให้เกิดผลกระทบข้างเคียง (Proximity Effect) ซึ่งทำให้บริเวณใกล้เคียงได้รับปริมาณรังสีส่วนเกิน จึงต้องมีการชดเชยปริมาณโดสแบบไดนามิก</p>
  </div>
  <div class="formula-group">

        <div class="equation-box">
          <div class="equation-header">📌 สมการฟิสิกส์หลัก: สมการขนาดวิกฤตขั้นต่ำของเรย์ลี</div>
          <div class="formula-math">$$\text{CD} = k_1 \frac{\lambda}{\text{NA}}, \qquad \text{DOF} = k_2 \frac{\lambda}{\text{NA}^2}$$</div>
          <p style="font-size:9.5pt; margin:4px 0 0 0; color:#334155; line-height:1.75; text-indent:0;"><strong>คำอธิบายตัวแปรและนัยสำคัญ:</strong> เกณฑ์ของเรย์ลีสำหรับความละเอียดและระยะชัดลึก</p>
        </div>
            
        <div class="equation-box">
          <div class="equation-header">📌 สมการฟิสิกส์หลัก: ฟังก์ชันการกระจายจุดของลำแสงอิเล็กตรอน (EBL Point Spread Function)</div>
          <div class="formula-math">$$f(r) = \frac{1}{\pi (1+\eta)} \left[ \frac{1}{\alpha^2} e^{-r^2/\alpha^2} + \frac{\eta}{\beta^2} e^{-r^2/\beta^2} \right]$$</div>
          <p style="font-size:9.5pt; margin:4px 0 0 0; color:#334155; line-height:1.75; text-indent:0;"><strong>คำอธิบายตัวแปรและนัยสำคัญ:</strong> แบบจำลองสองเกาส์เซียนสำหรับ Proximity Effect</p>
        </div>
              </div>

      <div class="table-block">
        <h3>📊 ตารางเปรียบเทียบเทคโนโลยีลิโธกราฟีระดับนาโนเมตร</h3>
        <table class="data-table">
          <thead><tr>
            <th>เทคโนโลยี</th><th>ความยาวคลื่น λ</th><th>เลนส์เชิงตัวเลข NA</th><th>ขนาดเส้นวิกฤต CD</th><th>อัตราผลผลิต (Throughput)</th></tr></thead>
<tbody><tr><td>DUV Immersion (ArFi)</td><td>193 nm</td><td>1.35 (น้ำ)</td><td>38 nm (Single)</td><td>สูงมาก (> 250 เวเฟอร์/ชม.)</td></tr><tr><td>EUV Lithography</td><td>13.5 nm</td><td>0.33 (High-NA 0.55)</td><td>13 nm (High-NA < 8 nm)</td><td>สูง (~ 150 - 200 เวเฟอร์/ชม.)</td></tr><tr><td>Electron Beam (EBL)</td><td>0.0037 nm (30 keV)</td><td>> 0.5</td><td>< 5 nm</td><td>ต่ำมาก (สำหรับต้นแบบและมาสก์)</td></tr><tr><td>Nanoimprint (NIL)</td><td>ใช้แม่พิมพ์กลไก</td><td>-</td><td>< 10 nm</td><td>ปานกลาง (ต้นทุนต่ำ)</td></tr></tbody></table>
</div>
  <div class="examples-group">

        <div class="example-box">
          <div class="example-header">
            <span>📝 ตัวอย่างการคำนวณที่ 3.3: การคำนวณขนาดวิกฤต CD ของระบบ EUV Lithography ยุคใหม่</span>
            <span style="background:#dcfce7; color:#15803d; font-size:8.5pt; padding:3px 10px; border-radius:4px; font-weight:700;">Step-by-Step Worked Solution</span>
          </div>
          <p style="text-indent:0; margin-bottom:10px;"><strong>โจทย์ปัญหา (Problem Statement):</strong><br>เครื่องสแกนเนอร์ High-NA EUV ของ ASML ใช้ความยาวคลื่น $\lambda = 13.5	ext{ nm}$, มีค่า $NA = 0.55$ และตัวคูณกระบวนการ $k_1 = 0.30$ จงคำนวณหา (ก) ขนาดเส้นวิกฤต $	ext{CD}$ (ข) ระยะชัดลึก $	ext{DOF}$ เมื่อ $k_2 = 0.50$</p>
          <div style="background:rgba(255,255,255,0.85); border:1px solid #e2e8f0; padding:12px 16px; border-radius:6px; margin:12px 0;">
            <strong style="color:#1e3a8a;">การวิเคราะห์และการคำนวณอย่างละเอียด:</strong><br>
            <p style="text-indent:0; margin:6px 0 0 0; line-height:1.85;">1. $\text{CD} = k_1 \frac{\lambda}{\text{NA}} = 0.30 \times \frac{13.5\text{ nm}}{0.55} = 7.36\text{ nm}$<br>2. $\text{DOF} = k_2 \frac{\lambda}{\text{NA}^2} = 0.50 \times \frac{13.5\text{ nm}}{(0.55)^2} = 22.31\text{ nm}$</p>
          </div>
          <div style="background:#f0fdf4; border-left:4px solid #16a34a; padding:10px 14px; margin-top:10px; font-size:9.5pt; color:#166534; border-radius:0 6px 6px 0;">
            💡 <strong>นัยสำคัญทางกายภาพและการประยุกต์ใช้งาน (Physical Insight):</strong><br>
            <span style="color:#14532d;">ขนาดเส้นละเอียดถึง $7.36	ext{ nm}$ ช่วยให้สามารถผลิตชิปสถาปัตยกรรม 2 nm และ 1.4 nm (A14) ได้โดยไม่ต้องใช้ Multi-Patterning ซับซ้อน</span>
          </div>
        </div>
            
        <div class="example-box">
          <div class="example-header">
            <span>📝 ตัวอย่างการคำนวณที่ 3.4: การคำนวณปริมาณรังสี (Dose) และเวลาเปิดรับแสงใน EBL</span>
            <span style="background:#dcfce7; color:#15803d; font-size:8.5pt; padding:3px 10px; border-radius:4px; font-weight:700;">Step-by-Step Worked Solution</span>
          </div>
          <p style="text-indent:0; margin-bottom:10px;"><strong>โจทย์ปัญหา (Problem Statement):</strong><br>ต้องการสร้างลวดลายขนาด $100	ext{ }\mu	ext{m} 	imes 100	ext{ }\mu	ext{m}$ บนฟิล์ม PMMA โดยใช้กระแสลำอิเล็กตรอน $I = 100	ext{ pA}$ และปริมาณโดสที่ต้องการ $D = 250	ext{ }\mu	ext{C/cm}^2$ จงคำนวณเวลาที่ใช้ในการสแกนเขียนลวดลาย</p>
          <div style="background:rgba(255,255,255,0.85); border:1px solid #e2e8f0; padding:12px 16px; border-radius:6px; margin:12px 0;">
            <strong style="color:#1e3a8a;">การวิเคราะห์และการคำนวณอย่างละเอียด:</strong><br>
            <p style="text-indent:0; margin:6px 0 0 0; line-height:1.85;">1. พื้นที่ $A = (100 \times 10^{-4}\text{ cm})^2 = 1.0 \times 10^{-4}\text{ cm}^2$<br>2. ประจุไฟฟ้ารวมที่ต้องใช้ $Q = D \times A = (250 \times 10^{-6}\text{ C/cm}^2) \times (1.0 \times 10^{-4}\text{ cm}^2) = 2.5 \times 10^{-8}\text{ C}$<br>3. เวลาสแกน $t = \frac{Q}{I} = \frac{2.5 \times 10^{-8}\text{ C}}{100 \times 10^{-12}\text{ A}} = 250\text{ วินาที} = 4.17\text{ นาที}$</p>
          </div>
          <div style="background:#f0fdf4; border-left:4px solid #16a34a; padding:10px 14px; margin-top:10px; font-size:9.5pt; color:#166534; border-radius:0 6px 6px 0;">
            💡 <strong>นัยสำคัญทางกายภาพและการประยุกต์ใช้งาน (Physical Insight):</strong><br>
            <span style="color:#14532d;">เวลาที่ค่อนข้างนานนี้แสดงให้เห็นว่าเหตุใด EBL จึงเหมาะกับงานวิจัยต้นแบบ แต่ไม่สามารถใช้ในการผลิตชิปเชิงพาณิชย์ปริมาณมากได้</span>
          </div>
        </div>
              </div>
  <div class="code-group">

        <div class="code-box">
          <div class="code-header">💻 แบบจำลองเชิงคำนวณภาษาไพทอน (Computational Python 3.11): กรณีศึกษา: เครื่อง ASML Twinscan EXE:5000 High-NA EUV Scanner</div>
          <pre><code>เครื่องจักรเทคโนโลยีขั้นสูงสุดของมนุษยชาติมูลค่ากว่า 380 ล้านดอลลาร์สหรัฐ ที่ใช้กระจกสะท้อนแสงที่มีความเรียบระดับอะตอม เพื่อพิมพ์ลวดลายชิปประมวลผล AI ขนาด 2 นาโนเมตร</code></pre>
        </div>
        <p style="font-size:9.5pt; color:#475569; margin-top:-6px; margin-bottom:18px; text-indent:0;"><em>คำอธิบายอัลกอริทึมการจำลอง:</em> สคริปต์ไพทอนสำหรับการคำนวณและจำลองเชิงตัวเลข</p>
              </div>
  <div class="lab-connection-block">
    <h3>🔬 การเชื่อมโยงสู่ห้องปฏิบัติการเสมือนจริงและเทคนิคการทดลอง (Virtual Lab Connection)</h3>
    <div style='background:#f0fdf4; border:1px solid #bbf7d0; border-left:5px solid #16a34a; padding:12px 16px; margin-bottom:14px; border-radius:6px;'><strong style='color:#166534; font-size:10.5pt;'>การจำลอง Proximity Effect ใน Electron Beam Lithography</strong><p style='margin:6px 0 0 0; color:#14532d; text-indent:0; line-height:1.8;'>ebl_proximity_sim.py</p></div>
  </div>
  <div class="cases-block">
    <h3>🌐 กรณีศึกษางานวิจัยแนวหน้าและนวัตกรรมอุตสาหกรรม (Frontier Case Studies)</h3>
    <div style='background:#eff6ff; border:1px solid #bfdbfe; border-left:5px solid #2563eb; padding:12px 16px; margin-bottom:14px; border-radius:6px;'><strong style='color:#1e40af; font-size:10.5pt;'>การเชื่อมโยงกับ Virtual Lab 12: การจำลองลิโธกราฟีลำแสงอิเล็กตรอนและการกัดพลาสมา</strong><p style='margin:6px 0 0 0; color:#1e3a8a; text-indent:0; line-height:1.8;'>ผู้เรียนสามารถออกแบบหน้ากากวงจร ปรับพลังงานลำอิเล็กตรอน (10-100 keV) และชดเชย Proximity Effect ใน Lab 12 เพื่อสร้างเกตทรานซิสเตอร์นาโน</p></div>
  </div>

      <div class="checkpoint-box" style="background:#fefce8; border:1px solid #fef08a; border-left:5px solid #eab308; padding:14px 18px; margin:24px 0 35px 0; border-radius:6px; page-break-inside:avoid;">
        <strong style="color:#854d0e; font-size:10pt;">🎯 จุดตรวจประเมินความเข้าใจและคำถามทบทวนประจำหัวข้อ 3.2 (Concept Checkpoint)</strong>
        <ul style="margin:8px 0 0 0; padding-left:20px; color:#713f12; font-size:9.5pt; line-height:1.8;">
          <li>จงอธิบายแนวคิดรวบยอดหลักของ การสังเคราะห์แบบบนลงล่าง: ลิโธกราฟีด้วยลำแสงอิเล็กตรอนและโฟตอน และความแตกต่างจากพฤติกรรมในระดับมหภาค</li>
          <li>พารามิเตอร์ใดเป็นปัจจัยวิกฤตที่ควบคุมสมบัติทางฟิสิกส์ในหัวข้อนี้ และมีผลกระทบอย่างไร?</li>
          <li>เชื่อมโยงหลักการฟิสิกส์ในหัวข้อนี้เข้ากับการประยุกต์ใช้จริงในเทคโนโลยีสมัยใหม่</li>
        </ul>
      </div>
    </div>
    
    <div class="topic-section">
      <h2>3.3 การสะสมไอสารเคมี (CVD) และการสะสมไอสารเชิงฟิสิกส์ (PVD)</h2>
      <div class="topic-en-title">(Chemical Vapor Deposition (CVD) & Physical Vapor Deposition (PVD))</div>
      
      <div class="topic-intro">
        <p>การสร้างฟิล์มบางระดับนาโนเมตร (Thin Films) และโครงสร้างสองมิติ เช่น กราฟีนและวัสดุไดคัลโคจีไนด์ มีสองกระบวนการหลักที่ใช้ในอุตสาหกรรมและห้องปฏิบัติการ ได้แก่ การสะสมไอสารเคมี (Chemical Vapor Deposition: CVD) และการสะสมไอสารเชิงฟิสิกส์ (Physical Vapor Deposition: PVD)</p>
    <p>กระบวนการ CVD อาศัยการทำปฏิกิริยาเคมีของสารตั้งต้นสถานะแก๊สบนพื้นผิวแผ่นรองรับที่มีอุณหภูมิสูง เช่น การสลายตัวของก๊าซมีเทน ($	ext{CH}_4$) บนฟอยล์ทองแดงเพื่อสร้างแผ่นกราฟีนขนาดใหญ่ หรือการใช้พลาสมาช่วยกระตุ้น (Plasma-Enhanced CVD: PECVD) เพื่อลดอุณหภูมิในการเคลือบฟิล์มไดอิเล็กทริก</p>
    <p>ในทางตรงกันข้าม กระบวนการ PVD อาศัยการระเหยหรือดีดอะตอมของสารเป้าหมาย (Target) ในสภาวะสุญญากาศสูง ผ่านเทคนิคการระเหยด้วยความร้อน (Thermal Evaporation), ลำอิเล็กตรอน (E-Beam Evaporation), หรือการสปัตเตอริง (Magnetron Sputtering) โดยไม่มีปฏิกิริยาเคมีเกิดขึ้น เหมาะสำหรับการเคลือบขั้วไฟฟ้าโลหะและฟิล์มบางหลายชั้น</p>
  </div>

      <div class="subtopic-block">
        <h3>กลไกการเจริญเติบโตของกราฟีนบนฟอยล์ทองแดงในระบบ Thermal CVD</h3>
            <p>ทองแดงมีค่าความสามารถในการละลายคาร์บอนต่ำมาก ($< 0.001	ext{ atom}\%$) ทำให้การเติบโตของกราฟีนถูกจำกัดตัวเองบนพื้นผิว (Self-Limiting Surface Reaction) ส่งผลให้ได้กราฟีนชั้นเดี่ยว (Single-Layer Graphene) ที่มีความต่อเนื่องสูงเกือบ 100%</p>
    <p>ในขณะที่นิกเกิล (Ni) มีความสามารถในการละลายคาร์บอนสูง เมื่อลดอุณหภูมิลง คาร์บอนจะตกผลึกแยกตัวออกมาที่ผิว ก่อให้เกิดกราฟีนหลายชั้น (Few-Layer Graphene)</p>
  </div>

      <div class="subtopic-block">
        <h3>ฟิสิกส์การสปัตเตอริงด้วยแมกนีตรอน (Magnetron Sputtering)</h3>
            <p>การใช้สนามแม่เหล็กดักจับอิเล็กตรอนให้อยู่ใกล้ผิวเป้าหมาย ช่วยเพิ่มความหนาแน่นพลาสมาของไอออน $	ext{Ar}^+$ ส่งผลให้อัตราการดีดอะตอม (Sputtering Yield) สูงขึ้น และได้ฟิล์มที่มีการยึดเกาะแน่นหนาและมีความหนาแน่นสูง</p>
  </div>
  <div class="formula-group">

        <div class="equation-box">
          <div class="equation-header">📌 สมการฟิสิกส์หลัก: อัตราการตกสะสมฟิล์มในระบบสปัตเตอริง</div>
          <div class="formula-math">$$R_{\text{dep}} = \frac{J_{\text{ion}} Y_{\text{sputter}} M_{\text{target}}}{e \rho N_A}, \qquad Y = \frac{\text{จำนวนอะตอมที่หลุดออกมา}}{\text{จำนวนไอออนที่ชน}}$$</div>
          <p style="font-size:9.5pt; margin:4px 0 0 0; color:#334155; line-height:1.75; text-indent:0;"><strong>คำอธิบายตัวแปรและนัยสำคัญ:</strong> อัตราการเคลือบฟิล์มบางและ Sputtering Yield</p>
        </div>
            
        <div class="equation-box">
          <div class="equation-header">📌 สมการฟิสิกส์หลัก: สมการปฏิกิริยาการเติบโตของกราฟีนใน CVD</div>
          <div class="formula-math">$$\text{CH}_4\text{(g)} \xrightarrow{\text{Cu, } 1000^\circ\text{C}} \text{C}_{\text{graphene}}\text{(s)} + 2\text{H}_2\text{(g)}$$</div>
          <p style="font-size:9.5pt; margin:4px 0 0 0; color:#334155; line-height:1.75; text-indent:0;"><strong>คำอธิบายตัวแปรและนัยสำคัญ:</strong> ปฏิกิริยาการสลายตัวของมีเทนบนตัวเร่งปฏิกิริยาทองแดง</p>
        </div>
              </div>

      <div class="table-block">
        <h3>📊 ตารางเปรียบเทียบเทคนิค CVD และ PVD</h3>
        <table class="data-table">
          <thead><tr>
            <th>คุณลักษณะ</th><th>Chemical Vapor Deposition (CVD)</th><th>Magnetron Sputtering (PVD)</th><th>E-Beam Evaporation (PVD)</th></tr></thead>
<tbody><tr><td>กลไกหลัก</td><td>ปฏิกิริยาเคมีบนผิว</td><td>การชนทางกลของไอออนพลาสมา</td><td>การระเหยด้วยความร้อน/ลำแสง</td></tr><tr><td>ระดับสุญญากาศ</td><td>สุญญากาศต่ำ-ปานกลาง (1 - 100 Torr)</td><td>สุญญากาศสูง ($10^{-3} - 10^{-2}$ Torr)</td><td>สุญญากาศสูงยิ่งยวด ($< 10^{-6}$ Torr)</td></tr><tr><td>ความครอบคลุมรอยต่อ (Conformality)</td><td>ดีเยี่ยม (Conformal)</td><td>ปานกลาง-ดี</td><td>แย่ (แนวสายตา Line-of-Sight)</td></tr><tr><td>อุณหภูมิแผ่นรองรับ</td><td>สูง (300 - 1050 °C)</td><td>ต่ำ-ปานกลาง (ห้อง - 400 °C)</td><td>ต่ำ (อุณหภูมิห้อง)</td></tr><tr><td>วัสดุที่นิยมเคลือบ</td><td>Graphene, CNTs, Si3N4, SiO2</td><td>โลหะ, ออกไซด์, โลหะผสม</td><td>ทองคำ, ไทเทเนียม, อะลูมิเนียม</td></tr></tbody></table>
</div>
  <div class="examples-group">

        <div class="example-box">
          <div class="example-header">
            <span>📝 ตัวอย่างการคำนวณที่ 3.5: การคำนวณอัตราการสิ้นเปลืองก๊าซและปริมาณคาร์บอนในการเคลือบกราฟีน</span>
            <span style="background:#dcfce7; color:#15803d; font-size:8.5pt; padding:3px 10px; border-radius:4px; font-weight:700;">Step-by-Step Worked Solution</span>
          </div>
          <p style="text-indent:0; margin-bottom:10px;"><strong>โจทย์ปัญหา (Problem Statement):</strong><br>ต้องการเคลือบกราฟีนชั้นเดี่ยวบนฟอยล์ทองแดงพื้นที่ $A = 100	ext{ cm}^2$ กำหนดความหนาแน่นของอะตอมคาร์บอนในกราฟีน $n_C = 3.82 	imes 10^{15}	ext{ atoms/cm}^2$ จงคำนวณหามวลคาร์บอนทั้งหมดบนฟอยล์ และปริมาตรก๊าซมีเทน ($	ext{CH}_4$) ที่สภาวะมาตรฐาน STP ที่ต้องใช้ในทางทฤษฎี</p>
          <div style="background:rgba(255,255,255,0.85); border:1px solid #e2e8f0; padding:12px 16px; border-radius:6px; margin:12px 0;">
            <strong style="color:#1e3a8a;">การวิเคราะห์และการคำนวณอย่างละเอียด:</strong><br>
            <p style="text-indent:0; margin:6px 0 0 0; line-height:1.85;">1. จำนวนอะตอมคาร์บอนทั้งหมด $N_C = n_C \times A = (3.82 \times 10^{15}) \times 100 = 3.82 \times 10^{17}\text{ atoms}$<br>2. จำนวนโมล $n = \frac{3.82 \times 10^{17}}{6.022 \times 10^{23}} = 6.343 \times 10^{-7}\text{ โมล}$<br>3. มวลคาร์บอน $m = n \times 12.011\text{ g/mol} = 7.619 \times 10^{-6}\text{ g} = 7.62\text{ }\mu\text{g}$<br>4. ปริมาตรก๊าซมีเทน STP: $V = n \times 22.4\text{ L/mol} = 1.42 \times 10^{-5}\text{ L} = 0.0142\text{ mL}$</p>
          </div>
          <div style="background:#f0fdf4; border-left:4px solid #16a34a; padding:10px 14px; margin-top:10px; font-size:9.5pt; color:#166534; border-radius:0 6px 6px 0;">
            💡 <strong>นัยสำคัญทางกายภาพและการประยุกต์ใช้งาน (Physical Insight):</strong><br>
            <span style="color:#14532d;">มวลของกราฟีนทั้งแผ่นมีค่าน้อยกว่า 8 ไมโครกรัม แสดงถึงประสิทธิภาพการใช้วัตถุดิบขั้นสูงสุดของวัสดุสองมิติ</span>
          </div>
        </div>
            
        <div class="example-box">
          <div class="example-header">
            <span>📝 ตัวอย่างการคำนวณที่ 3.6: การคำนวณความหนาของฟิล์มบางทองคำจากการระเหย E-Beam</span>
            <span style="background:#dcfce7; color:#15803d; font-size:8.5pt; padding:3px 10px; border-radius:4px; font-weight:700;">Step-by-Step Worked Solution</span>
          </div>
          <p style="text-indent:0; margin-bottom:10px;"><strong>โจทย์ปัญหา (Problem Statement):</strong><br>ระบบ E-Beam Evaporator ทำงานที่อัตราการเคลือบ $r = 0.20	ext{ nm/s}$ เป็นเวลา $t = 3.0	ext{ นาที}$ จงคำนวณหาความหนาฟิล์ม $d$ และมวลของฟิล์มทองคำบนเวเฟอร์ขนาดเส้นผ่านศูนย์กลาง 4 นิ้ว ($ho_{	ext{Au}} = 19.3	ext{ g/cm}^3$)</p>
          <div style="background:rgba(255,255,255,0.85); border:1px solid #e2e8f0; padding:12px 16px; border-radius:6px; margin:12px 0;">
            <strong style="color:#1e3a8a;">การวิเคราะห์และการคำนวณอย่างละเอียด:</strong><br>
            <p style="text-indent:0; margin:6px 0 0 0; line-height:1.85;">1. เวลาทั้งหมด $t = 180\text{ s}$<br>2. ความหนา $d = r \times t = 0.20\text{ nm/s} \times 180\text{ s} = 36.0\text{ nm}$<br>3. พื้นที่เวเฟอร์ 4 นิ้ว ($R = 5.08\text{ cm}$): $A = \pi (5.08)^2 = 81.07\text{ cm}^2$<br>4. ปริมาตรฟิล์ม $V = A \times d = 81.07 \times (36 \times 10^{-7}\text{ cm}) = 2.919 \times 10^{-4}\text{ cm}^3$<br>5. มวลทองคำ $m = \rho \times V = 19.3 \times 2.919 \times 10^{-4} = 5.63 \times 10^{-3}\text{ g} = 5.63\text{ mg}$</p>
          </div>
          <div style="background:#f0fdf4; border-left:4px solid #16a34a; padding:10px 14px; margin-top:10px; font-size:9.5pt; color:#166534; border-radius:0 6px 6px 0;">
            💡 <strong>นัยสำคัญทางกายภาพและการประยุกต์ใช้งาน (Physical Insight):</strong><br>
            <span style="color:#14532d;">การควบคุมความหนาด้วย Quartz Crystal Microbalance (QCM) ช่วยให้ได้ความหนาแม่นยำในระดับ $0.1	ext{ nm}$</span>
          </div>
        </div>
              </div>
  <div class="code-group">

        <div class="code-box">
          <div class="code-header">💻 แบบจำลองเชิงคำนวณภาษาไพทอน (Computational Python 3.11): กรณีศึกษา: การผลิตกราฟีนแบบม้วนต่อม้วน (Roll-to-Roll CVD Graphene) สำหรับจอสัมผัสยืดหยุ่น</div>
          <pre><code>การพัฒนาระบบ Roll-to-Roll CVD ความกว้าง 30 นิ้ว ช่วยให้สามารถเคลือบฟิล์มกราฟีนโปร่งใสที่มีความต้านทานแผ่นต่ำกว่า $30	ext{ }\Omega/\square$ และความโปร่งแสง $> 90\%$ ลงบนฟอยล์ทองแดงได้อย่างต่อเนื่อง</code></pre>
        </div>
        <p style="font-size:9.5pt; color:#475569; margin-top:-6px; margin-bottom:18px; text-indent:0;"><em>คำอธิบายอัลกอริทึมการจำลอง:</em> สคริปต์ไพทอนสำหรับการคำนวณและจำลองเชิงตัวเลข</p>
              </div>
  <div class="lab-connection-block">
    <h3>🔬 การเชื่อมโยงสู่ห้องปฏิบัติการเสมือนจริงและเทคนิคการทดลอง (Virtual Lab Connection)</h3>
    <div style='background:#f0fdf4; border:1px solid #bbf7d0; border-left:5px solid #16a34a; padding:12px 16px; margin-bottom:14px; border-radius:6px;'><strong style='color:#166534; font-size:10.5pt;'>การคำนวณจลนศาสตร์การเติบโตของฟิล์มบางใน CVD</strong><p style='margin:6px 0 0 0; color:#14532d; text-indent:0; line-height:1.8;'>cvd_film_growth.py</p></div>
  </div>
  <div class="cases-block">
    <h3>🌐 กรณีศึกษางานวิจัยแนวหน้าและนวัตกรรมอุตสาหกรรม (Frontier Case Studies)</h3>
    <div style='background:#eff6ff; border:1px solid #bfdbfe; border-left:5px solid #2563eb; padding:12px 16px; margin-bottom:14px; border-radius:6px;'><strong style='color:#1e40af; font-size:10.5pt;'>การเชื่อมโยงกับ Virtual Lab 13: การจำลองการสังเคราะห์กราฟีนด้วย CVD และการเคลือบฟิล์มบาง PVD</strong><p style='margin:6px 0 0 0; color:#1e3a8a; text-indent:0; line-height:1.8;'>ผู้เรียนสามารถควบคุมอุณหภูมิเตา อัตราการไหลของก๊าซ $	ext{CH}_4/	ext{H}_2$ และความดันใน Lab 13 เพื่อสังเกตการสร้างชั้นกราฟีนบนฟอยล์ทองแดง</p></div>
  </div>

      <div class="checkpoint-box" style="background:#fefce8; border:1px solid #fef08a; border-left:5px solid #eab308; padding:14px 18px; margin:24px 0 35px 0; border-radius:6px; page-break-inside:avoid;">
        <strong style="color:#854d0e; font-size:10pt;">🎯 จุดตรวจประเมินความเข้าใจและคำถามทบทวนประจำหัวข้อ 3.3 (Concept Checkpoint)</strong>
        <ul style="margin:8px 0 0 0; padding-left:20px; color:#713f12; font-size:9.5pt; line-height:1.8;">
          <li>จงอธิบายแนวคิดรวบยอดหลักของ การสะสมไอสารเคมี (CVD) และการสะสมไอสารเชิงฟิสิกส์ (PVD) และความแตกต่างจากพฤติกรรมในระดับมหภาค</li>
          <li>พารามิเตอร์ใดเป็นปัจจัยวิกฤตที่ควบคุมสมบัติทางฟิสิกส์ในหัวข้อนี้ และมีผลกระทบอย่างไร?</li>
          <li>เชื่อมโยงหลักการฟิสิกส์ในหัวข้อนี้เข้ากับการประยุกต์ใช้จริงในเทคโนโลยีสมัยใหม่</li>
        </ul>
      </div>
    </div>
    
    <div class="topic-section">
      <h2>3.4 การสะสมชั้นอะตอม (Atomic Layer Deposition - ALD)</h2>
      <div class="topic-en-title">(Atomic Layer Deposition (ALD) & Self-Limiting Surface Reactions)</div>
      
      <div class="topic-intro">
        <p>การสะสมชั้นอะตอม (Atomic Layer Deposition: ALD) เป็นเทคนิคการเคลือบฟิล์มบางไอสารเคมีขั้นสูงสุดที่อาศัยปฏิกิริยาเคมีที่จำกัดตัวเองบนพื้นผิวแบบต่อเนื่องเป็นลำดับ (Sequential Self-Limiting Surface Reactions) โดยแบ่งการป้อนสารตั้งต้นออกเป็นสองครึ่งปฏิกิริยาที่แยกจากกันด้วยการชะล้างด้วยก๊าซเฉื่อย</p>
    <p>จุดเด่นอันเป็นเอกลักษณ์ของ ALD คือการควบคุมความหนาของฟิล์มได้อย่างแม่นยำในระดับอะตอมเดี่ยว (Atomic Scale Thickness Control) และมีความสม่ำเสมอในการเคลือบผิวอย่างสมบูรณ์แบบ (100% Conformality) แม้บนโครงสร้างที่มีอัตราส่วนกว้างยาวสูงมาก (Aspect Ratio > 1000:1) หรือในรูพรุนขนาดนาโนเมตร</p>
    <p>เทคโนโลยี ALD มีบทบาทสำคัญอย่างยิ่งยวดในการปฏิวัติอุตสาหกรรมไมโครชิป เช่น การเคลือบชั้นฉนวนเกตไดอิเล็กทริกค่าสูง (High-k Dielectrics เช่น $	ext{HfO}_2, 	ext{ZrO}_2$) ในทรานซิสเตอร์ FinFET และ GAAFET, การสร้างตัวเก็บประจุ 3D DRAM, และการเคลือบฟิล์มป้องกันการแพร่กระจายของความชื้นในจอแสดงผล OLED</p>
  </div>

      <div class="subtopic-block">
        <h3>กลไกปฏิกิริยาสองขั้นตอนของกระบวนการ ALD Al2O3</h3>
            <p>1. ขั้นตอนพัลส์ที่ 1 (TMA Pulse): ไตรเมทิลอะลูมิเนียม $	ext{Al(CH}_3)_3$ ทำปฏิกิริยากับหมู่ไฮดรอกซิล $-	ext{OH}$ บนผิว เกิดพันธะ $-	ext{O}-	ext{Al(CH}_3)_2$ และปล่อยมีเทน $	ext{CH}_4$ ออกมา เมื่อหมู่ $-	ext{OH}$ หมด ปฏิกิริยาจะหยุดลงเอง</p>
    <p>2. ขั้นตอนการชะล้างที่ 1 (Purge 1): เป่าก๊าซ $	ext{N}_2$ หรือ $	ext{Ar}$ เพื่อไล่โมเลกุล TMA ส่วนเกินและก๊าซผลพลอยได้ $	ext{CH}_4$ ออกจากห้องสุญญากาศ</p>
    <p>3. ขั้นตอนพัลส์ที่ 2 (Water Pulse): ป้อนไอระเหยน้ำ $	ext{H}_2	ext{O}$ เข้าทำปฏิกิริยากับหมู่ $-	ext{CH}_3$ สร้างชั้นอะลูมินา $-	ext{Al}-	ext{O}-	ext{Al}-$ และฟื้นฟูหมู่ $-	ext{OH}$ บนผิวใหม่</p>
    <p>4. ขั้นตอนการชะล้างที่ 2 (Purge 2): เป่าก๊าซเฉื่อยไล่น้ำและมีเทนส่วนเกิน ครบ 1 รอบปฏิกิริยา ALD Cycle ได้ความหนาเพิ่มขึ้น $pprox 0.10	ext{ nm}$ (Growth Per Cycle: GPC)</p>
  </div>

      <div class="subtopic-block">
        <h3>ช่วงอุณหภูมิการทำงานที่เหมาะสม (ALD Temperature Window)</h3>
            <p>ในช่วง ALD Window อัตราการเติบโตต่อรอบ (GPC) จะคงที่อย่างสมบูรณ์ หากอุณหภูมิต่ำเกินไปสารตั้งต้นอาจควบแน่นบนผิว หรือเกิดปฏิกิริยาไม่สมบูรณ์ หากอุณหภูมิสูงเกินไปสารตั้งต้นอาจสลายตัวด้วยความร้อน (CVD-like Decomposition) หรือเกิดการดีซอร์ปชัน</p>
  </div>
  <div class="formula-group">

        <div class="equation-box">
          <div class="equation-header">📌 สมการฟิสิกส์หลัก: สมการปฏิกิริยาเคมีของ ALD Al2O3</div>
          <div class="formula-math">$$\begin{aligned} \text{Surface-OH} + \text{Al(CH}_3)_3\text{(g)} &\to \text{Surface-O-Al(CH}_3)_2 + \text{CH}_4\text{(g)} \\ \text{Surface-O-Al(CH}_3)_2 + 2\text{H}_2\text{O(g)} &\to \text{Surface-O-Al(OH)}_2 + 2\text{CH}_4\text{(g)} \end{aligned}$$</div>
          <p style="font-size:9.5pt; margin:4px 0 0 0; color:#334155; line-height:1.75; text-indent:0;"><strong>คำอธิบายตัวแปรและนัยสำคัญ:</strong> สองครึ่งปฏิกิริยาการเกิด Al2O3 ใน 1 รอบ ALD Cycle</p>
        </div>
            
        <div class="equation-box">
          <div class="equation-header">📌 สมการฟิสิกส์หลัก: การคำนวณความหนารวมของฟิล์ม ALD</div>
          <div class="formula-math">$$d_{\text{film}} = N_{\text{cycles}} \times \text{GPC}, \qquad \text{GPC} \approx 0.09 - 0.12\text{ nm/cycle}$$</div>
          <p style="font-size:9.5pt; margin:4px 0 0 0; color:#334155; line-height:1.75; text-indent:0;"><strong>คำอธิบายตัวแปรและนัยสำคัญ:</strong> ความหนาฟิล์มแปรผันตรงอย่างแม่นยำตามจำนวนรอบ</p>
        </div>
              </div>

      <div class="table-block">
        <h3>📊 ตารางสารตั้งต้นและพารามิเตอร์ ALD สำหรับวัสดุสำคัญ</h3>
        <table class="data-table">
          <thead><tr>
            <th>วัสดุฟิล์ม</th><th>สารตั้งต้นโลหะ (Precursor)</th><th>สารออกซิแดนต์ (Reactant)</th><th>ALD Window (°C)</th><th>GPC (nm/cycle)</th></tr></thead>
<tbody><tr><td>Al2O3</td><td>Trimethylaluminum (TMA)</td><td>H2O หรือ O3</td><td>150 - 300 °C</td><td>0.10 nm</td></tr><tr><td>HfO2 (High-k)</td><td>Tetrakis(dimethylamido)hafnium (TDMAH)</td><td>H2O หรือ O3</td><td>180 - 280 °C</td><td>0.09 nm</td></tr><tr><td>TiO2</td><td>Titanium isopropoxide (TTIP)</td><td>H2O</td><td>150 - 250 °C</td><td>0.05 nm</td></tr><tr><td>ZnO</td><td>Diethylzinc (DEZ)</td><td>H2O</td><td>100 - 200 °C</td><td>0.18 nm</td></tr><tr><td>TiN (Conductor)</td><td>TiCl4</td><td>NH3</td><td>350 - 450 °C</td><td>0.03 nm</td></tr></tbody></table>
</div>
  <div class="examples-group">

        <div class="example-box">
          <div class="example-header">
            <span>📝 ตัวอย่างการคำนวณที่ 3.7: การคำนวณจำนวนรอบ ALD เพื่อสร้างชั้น High-k Dielectric HfO2 ใน GAAFET</span>
            <span style="background:#dcfce7; color:#15803d; font-size:8.5pt; padding:3px 10px; border-radius:4px; font-weight:700;">Step-by-Step Worked Solution</span>
          </div>
          <p style="text-indent:0; margin-bottom:10px;"><strong>โจทย์ปัญหา (Problem Statement):</strong><br>ต้องการสร้างชั้นเกตไดอิเล็กทริก $	ext{HfO}_2$ หนา $d = 2.25	ext{ nm}$ กำหนดอัตราการเติบโตต่อรอบ $	ext{GPC} = 0.090	ext{ nm/cycle}$ และเวลาต่อรอบ $	au = 4.0	ext{ วินาที}$ จงคำนวณหา (ก) จำนวนรอบที่ต้องใช้ $N$ (ข) เวลาทำงานรวมของระบบ</p>
          <div style="background:rgba(255,255,255,0.85); border:1px solid #e2e8f0; padding:12px 16px; border-radius:6px; margin:12px 0;">
            <strong style="color:#1e3a8a;">การวิเคราะห์และการคำนวณอย่างละเอียด:</strong><br>
            <p style="text-indent:0; margin:6px 0 0 0; line-height:1.85;">1. $N = \frac{d}{\text{GPC}} = \frac{2.25\text{ nm}}{0.090\text{ nm/cycle}} = 25\text{ รอบ (Cycles)}$<br>2. เวลาทำงานรวม $t = N \times \tau = 25 \times 4.0\text{ s} = 100\text{ วินาที} = 1\text{ นาที } 40\text{ วินาที}$</p>
          </div>
          <div style="background:#f0fdf4; border-left:4px solid #16a34a; padding:10px 14px; margin-top:10px; font-size:9.5pt; color:#166534; border-radius:0 6px 6px 0;">
            💡 <strong>นัยสำคัญทางกายภาพและการประยุกต์ใช้งาน (Physical Insight):</strong><br>
            <span style="color:#14532d;">การควบคุมความหนาในระดับเศษส่วนทศนิยมของนาโนเมตรช่วยให้ค่า Equivalent Oxide Thickness (EOT) ต่ำกว่า $0.5	ext{ nm}$ ป้องกันกระแสไฟฟ้ารั่วไหลได้ยอดเยี่ยม</span>
          </div>
        </div>
            
        <div class="example-box">
          <div class="example-header">
            <span>📝 ตัวอย่างการคำนวณที่ 3.8: การคำนวณค่าความจุไฟฟ้าของตัวเก็บประจุ 3D Trench Capacitor ที่เคลือบด้วย ALD</span>
            <span style="background:#dcfce7; color:#15803d; font-size:8.5pt; padding:3px 10px; border-radius:4px; font-weight:700;">Step-by-Step Worked Solution</span>
          </div>
          <p style="text-indent:0; margin-bottom:10px;"><strong>โจทย์ปัญหา (Problem Statement):</strong><br>ร่องลึก 3D มีพื้นที่ผิวประสิทธิผล $A = 10^{-6}	ext{ cm}^2$ เคลือบด้วยชั้นฉนวน $	ext{HfO}_2$ หนา $d = 3.0	ext{ nm}$ ($\epsilon_r = 25$) จงคำนวณค่าความจุไฟฟ้า $C$</p>
          <div style="background:rgba(255,255,255,0.85); border:1px solid #e2e8f0; padding:12px 16px; border-radius:6px; margin:12px 0;">
            <strong style="color:#1e3a8a;">การวิเคราะห์และการคำนวณอย่างละเอียด:</strong><br>
            <p style="text-indent:0; margin:6px 0 0 0; line-height:1.85;">$$C = \frac{\epsilon_0 \epsilon_r A}{d} = \frac{(8.854 \times 10^{-12}) \times 25 \times (10^{-6} \times 10^{-4}\text{ m}^2)}{3.0 \times 10^{-9}\text{ m}} = 7.378 \times 10^{-14}\text{ F} = 73.78\text{ fF}$$</p>
          </div>
          <div style="background:#f0fdf4; border-left:4px solid #16a34a; padding:10px 14px; margin-top:10px; font-size:9.5pt; color:#166534; border-radius:0 6px 6px 0;">
            💡 <strong>นัยสำคัญทางกายภาพและการประยุกต์ใช้งาน (Physical Insight):</strong><br>
            <span style="color:#14532d;">ความสม่ำเสมอ $100\%$ ในการเคลือบผนังร่องลึกทำให้เก็บประจุได้เพียงพอสำหรับหน่วยความจำ DRAM ขนาดจิ๋ว</span>
          </div>
        </div>
              </div>
  <div class="code-group">

        <div class="code-box">
          <div class="code-header">💻 แบบจำลองเชิงคำนวณภาษาไพทอน (Computational Python 3.11): กรณีศึกษา: การเคลือบฟิล์มป้องกันความชื้นบางเฉียบสำหรับจอพับได้ (Foldable OLED Encapsulation)</div>
          <pre><code>เทคโนโลยี Thin Film Encapsulation (TFE) โดยใช้ชั้นฟิล์มซ้อนสลับ $	ext{Al}_2	ext{O}_3	ext{ ALD}$ และพอลิเมอร์ ช่วยลดอัตราการซึมผ่านของไอน้ำ (WVTR) เหลือต่ำกว่า $10^{-6}	ext{ g/m}^2/	ext{day}$ ทำให้อุปกรณ์ OLED พับได้มีอายุการใช้งานยาวนานเกิน 10 ปี</code></pre>
        </div>
        <p style="font-size:9.5pt; color:#475569; margin-top:-6px; margin-bottom:18px; text-indent:0;"><em>คำอธิบายอัลกอริทึมการจำลอง:</em> สคริปต์ไพทอนสำหรับการคำนวณและจำลองเชิงตัวเลข</p>
              </div>
  <div class="lab-connection-block">
    <h3>🔬 การเชื่อมโยงสู่ห้องปฏิบัติการเสมือนจริงและเทคนิคการทดลอง (Virtual Lab Connection)</h3>
    <div style='background:#f0fdf4; border:1px solid #bbf7d0; border-left:5px solid #16a34a; padding:12px 16px; margin-bottom:14px; border-radius:6px;'><strong style='color:#166534; font-size:10.5pt;'>การจำลองกระบวนการเคลือบชั้นอะตอม ALD</strong><p style='margin:6px 0 0 0; color:#14532d; text-indent:0; line-height:1.8;'>ald_process_sim.py</p></div>
  </div>
  <div class="cases-block">
    <h3>🌐 กรณีศึกษางานวิจัยแนวหน้าและนวัตกรรมอุตสาหกรรม (Frontier Case Studies)</h3>
    <div style='background:#eff6ff; border:1px solid #bfdbfe; border-left:5px solid #2563eb; padding:12px 16px; margin-bottom:14px; border-radius:6px;'><strong style='color:#1e40af; font-size:10.5pt;'>การเชื่อมโยงกับ Virtual Lab 14: การจำลองการสะสมชั้นอะตอม ALD และการควบคุมรอบปฏิกิริยา</strong><p style='margin:6px 0 0 0; color:#1e3a8a; text-indent:0; line-height:1.8;'>ผู้เรียนสามารถควบคุมเวลาพัลส์ของ TMA และ $	ext{H}_2	ext{O}$ ใน Lab 14 สังเกตการเข้าจับของโมเลกุลบนผิว และวัดค่า Conformality ในร่องลึก</p></div>
  </div>

      <div class="checkpoint-box" style="background:#fefce8; border:1px solid #fef08a; border-left:5px solid #eab308; padding:14px 18px; margin:24px 0 35px 0; border-radius:6px; page-break-inside:avoid;">
        <strong style="color:#854d0e; font-size:10pt;">🎯 จุดตรวจประเมินความเข้าใจและคำถามทบทวนประจำหัวข้อ 3.4 (Concept Checkpoint)</strong>
        <ul style="margin:8px 0 0 0; padding-left:20px; color:#713f12; font-size:9.5pt; line-height:1.8;">
          <li>จงอธิบายแนวคิดรวบยอดหลักของ การสะสมชั้นอะตอม (Atomic Layer Deposition - ALD) และความแตกต่างจากพฤติกรรมในระดับมหภาค</li>
          <li>พารามิเตอร์ใดเป็นปัจจัยวิกฤตที่ควบคุมสมบัติทางฟิสิกส์ในหัวข้อนี้ และมีผลกระทบอย่างไร?</li>
          <li>เชื่อมโยงหลักการฟิสิกส์ในหัวข้อนี้เข้ากับการประยุกต์ใช้จริงในเทคโนโลยีสมัยใหม่</li>
        </ul>
      </div>
    </div>
    
    <div class="topic-section">
      <h2>3.5 การประกอบตัวเองระดับโมเลกุลและชั้นโมเลกุลจัดตัวชิด</h2>
      <div class="topic-en-title">(Self-Assembly, Self-Assembled Monolayers (SAMs) & DNA Origami)</div>
      
      <div class="topic-intro">
        <p>การประกอบตัวเองระดับโมเลกุล (Molecular Self-Assembly) คือกระบวนการที่โมเลกุลหรืออนุภาคนาโนจัดเรียงตัวเข้าสู่โครงสร้างที่มีระเบียบเชิงเรขาคณิตโดยธรรมชาติ โดยไม่ต้องอาศัยการบังคับจากแรงภายนอก แต่ขับเคลื่อนด้วยการลดลงของพลังงานอิสระของระบบ ($\Delta G < 0$) ผ่านอันตรกิริยาอย่างอ่อนที่ไม่ใช่พันธะโคเวเลนต์ เช่น พันธะไฮโดรเจน, แรงฟานเดอร์วาลส์, อันตรกิริยาไม่ชอบน้ำ (Hydrophobic Effects), และแรงดึงดูดทางไฟฟ้าสถิต</p>
    <p>ตัวอย่างที่โดดเด่นและถูกนำมาใช้งานอย่างกว้างขวางที่สุดคือชั้นโมเลกุลจัดตัวชิดเดี่ยว (Self-Assembled Monolayers: SAMs) เช่น การจัดตัวของโมเลกุลแอลเคนไธออล (Alkanethiols: $	ext{CH}_3(	ext{CH}_2)_{n-1}	ext{SH}$) บนพื้นผิวผลึกทองคำ $	ext{Au}(111)$ ซึ่งโมเลกุลจะยึดเกาะด้วยพันธะกึ่งโควาเลนต์ $	ext{Au}-	ext{S}$ และจัดระเบียบหางโซ่อัลคิลด้วยแรงฟานเดอร์วาลส์จนเกิดเป็นชั้นฟิล์มโมเลกุลที่เรียบแน่นระดับอะตอม</p>
    <p>ในระดับชีวโมเลกุลขั้นสูง เทคโนโลยีดีเอ็นเอพับกระดาษ (DNA Origami) สามารถนำสายดีเอ็นเอสายยาวมาพับและเชื่อมโยงด้วยสายสั้น (Staple Strands) ให้กลายเป็นโครงสร้าง 2 มิติและ 3 มิติขนาดนาโนเมตรที่ซับซ้อนตามที่ออกแบบในคอมพิวเตอร์ ทำหน้าที่เป็นฐานประกอบวงจรนาโนและหุ่นยนต์นำส่งยาระดับโมเลกุล</p>
  </div>

      <div class="subtopic-block">
        <h3>โครงสร้าง 3 ส่วนหลักของโมเลกุล SAMs</h3>
            <p>1. ส่วนหัวยึดเกาะ (Head Group): ทำหน้าที่ยึดเหนี่ยวกับผิวแผ่นรองรับด้วยพันธะเคมีจำเพาะ เช่น หมู่ไธออล $(-	ext{SH})$ บนทองคำ, หรือหมู่ไซเลน $(-	ext{SiCl}_3)$ บนซิลิกา/แก้ว</p>
    <p>2. ส่วนแกนกลางโซ่อัลคิล (Spacer/Alkyl Chain): ช่วยขับเคลื่อนการจัดเรียงตัวให้แน่นชิดผ่านแรงดึงดูดฟานเดอร์วาลส์ระหว่างโซ่ ทำให้โมเลกุลเอียงทำมุมประมาณ $30^\circ$ จากแนวตั้งฉากบน $	ext{Au}(111)$</p>
    <p>3. ส่วนหางฟังก์ชันนัล (Terminal/Tail Group): กำหนดสมบัติทางเคมีและฟิสิกส์ของพื้นผิวใหม่ เช่น หมู่ $-	ext{CH}_3$ ทำให้ผิวไม่ชอบน้ำอย่างยิ่ง (Superhydrophobic: มุมสัมผัสน้ำ $> 110^\circ$) หรือหมู่ $-	ext{COOH}, -	ext{NH}_2$ ทำให้ผิวชอบน้ำและจับกับโปรตีนได้</p>
  </div>

      <div class="subtopic-block">
        <h3>อุณหพลศาสตร์และพลังงานขับเคลื่อนการประกอบตัวเอง</h3>
            <p>การเกิดโครงสร้างระเบียบขับเคลื่อนด้วย $\Delta G = \Delta H - T \Delta S$ โดยเอนทาลปี $\Delta H$ มาจากการสร้างพันธะเคมีและแรงฟานเดอร์วาลส์ ส่วนเอนโทรปีของการจัดระเบียบโมเลกุลถูกชดเชยด้วยการปลดปล่อยโมเลกุลตัวทำละลายที่ผิว (Solvent Desolvation Entropy)</p>
  </div>
  <div class="formula-group">

        <div class="equation-box">
          <div class="equation-header">📌 สมการฟิสิกส์หลัก: สมการการดูดซับแบบแลงเมียร์สำหรับ SAMs</div>
          <div class="formula-math">$$\theta(t) = \frac{K C}{1 + K C} \left( 1 - e^{-k_{\text{ads}} C t} \right)$$</div>
          <p style="font-size:9.5pt; margin:4px 0 0 0; color:#334155; line-height:1.75; text-indent:0;"><strong>คำอธิบายตัวแปรและนัยสำคัญ:</strong> จลนศาสตร์การสร้างชั้น SAMs บนพื้นผิว</p>
        </div>
            
        <div class="equation-box">
          <div class="equation-header">📌 สมการฟิสิกส์หลัก: พลังงานอิสระของพื้นผิวและมุมสัมผัสของหยดน้ำ (Young's Equation)</div>
          <div class="formula-math">$$\gamma_{SV} = \gamma_{SL} + \gamma_{LV} \cos\theta_Y$$</div>
          <p style="font-size:9.5pt; margin:4px 0 0 0; color:#334155; line-height:1.75; text-indent:0;"><strong>คำอธิบายตัวแปรและนัยสำคัญ:</strong> สมการของยังอธิบายการปรับแต่งความชอบน้ำ/ไม่ชอบน้ำ</p>
        </div>
              </div>

      <div class="table-block">
        <h3>📊 ตารางระบบคู่หัวจับ-แผ่นรองรับที่นิยมใช้ในการสร้าง SAMs</h3>
        <table class="data-table">
          <thead><tr>
            <th>ระบบโมเลกุล SAM</th><th>แผ่นรองรับ (Substrate)</th><th>ชนิดพันธะที่หัว</th><th>มุมเอียงโมเลกุล</th><th>การประยุกต์ใช้งาน</th></tr></thead>
<tbody><tr><td>Alkanethiols (R-SH)</td><td>Au (111), Ag, Cu</td><td>Au-S (Covalent ~ 45 kcal/mol)</td><td>~ 30° บน Au, ~ 12° บน Ag</td><td>ไบโอเซนเซอร์, โมเลกุลาร์อิเล็กทรอนิกส์</td></tr><tr><td>Organosilanes (R-SiCl3)</td><td>SiO2, Glass, TiO2</td><td>Si-O-Si (Siloxane Network)</td><td>ไม่แน่นอน (Crosslinked)</td><td>การเคลือบกันน้ำ, ลิโธกราฟี</td></tr><tr><td>Phosphonic Acids (R-PO3H2)</td><td>Al2O3, ITO, TiO2</td><td>P-O-M (Coordination)</td><td>~ 20 - 35°</td><td>ขั้วต่อไดอิเล็กทริกใน Organic FETs</td></tr><tr><td>Fatty Acids (R-COOH)</td><td>Al2O3, Fe2O3</td><td>Carboxylate-Metal</td><td>~ 15 - 20°</td><td>การเคลือบป้องกันการสึกหรอและการกัดกร่อน</td></tr></tbody></table>
</div>
  <div class="examples-group">

        <div class="example-box">
          <div class="example-header">
            <span>📝 ตัวอย่างการคำนวณที่ 3.9: การคำนวณความหนาแน่นเชิงพื้นผิวและจำนวนโมเลกุล Thiol บนผิวทองคำ</span>
            <span style="background:#dcfce7; color:#15803d; font-size:8.5pt; padding:3px 10px; border-radius:4px; font-weight:700;">Step-by-Step Worked Solution</span>
          </div>
          <p style="text-indent:0; margin-bottom:10px;"><strong>โจทย์ปัญหา (Problem Statement):</strong><br>แผ่นทองคำ $	ext{Au}(111)$ พื้นที่ $A = 1.0	ext{ cm}^2$ ถูกเคลือบด้วยโมเลกุล Dodecanethiol ($	ext{C}_{12}	ext{H}_{25}	ext{SH}$) จนเต็มชั้น SAM สมบูรณ์ มีพื้นที่ครอบครองต่อโมเลกุล $a_0 = 0.214	ext{ nm}^2$ จงคำนวณหา (ก) จำนวนโมเลกุลทั้งหมดบนแผ่น (ข) มวลของชั้น SAMs ที่เกิดขึ้น</p>
          <div style="background:rgba(255,255,255,0.85); border:1px solid #e2e8f0; padding:12px 16px; border-radius:6px; margin:12px 0;">
            <strong style="color:#1e3a8a;">การวิเคราะห์และการคำนวณอย่างละเอียด:</strong><br>
            <p style="text-indent:0; margin:6px 0 0 0; line-height:1.85;">1. ความหนาแน่นโมเลกุลต่อหน่วยพื้นที่: $N_s = \frac{1}{a_0} = \frac{1}{0.214 \times 10^{-14}\text{ cm}^2} = 4.673 \times 10^{14}\text{ molecules/cm}^2$<br>2. จำนวนโมเลกุลทั้งหมด $N_{\text{total}} = N_s \times 1.0 = 4.673 \times 10^{14}\text{ molecules}$<br>3. มวลโมเลกุลของ Dodecanethiol: $M = 202.40\text{ g/mol}$<br>4. มวลรวม $m = \frac{4.673 \times 10^{14}}{6.022 \times 10^{23}} \times 202.40 = 1.571 \times 10^{-7}\text{ g} = 0.157\text{ }\mu\text{g}$</p>
          </div>
          <div style="background:#f0fdf4; border-left:4px solid #16a34a; padding:10px 14px; margin-top:10px; font-size:9.5pt; color:#166534; border-radius:0 6px 6px 0;">
            💡 <strong>นัยสำคัญทางกายภาพและการประยุกต์ใช้งาน (Physical Insight):</strong><br>
            <span style="color:#14532d;">มวลเพียง $0.157	ext{ }\mu	ext{g}$ สามารถเปลี่ยนสภาพผิวทองคำจากชอบน้ำกลายเป็นผิวไม่ชอบน้ำอย่างยิ่งได้อย่างสมบูรณ์</span>
          </div>
        </div>
            
        <div class="example-box">
          <div class="example-header">
            <span>📝 ตัวอย่างการคำนวณที่ 3.1: การคำนวณการเปลี่ยนแปลงพลังงานพื้นผิวตามสมการของยัง</span>
            <span style="background:#dcfce7; color:#15803d; font-size:8.5pt; padding:3px 10px; border-radius:4px; font-weight:700;">Step-by-Step Worked Solution</span>
          </div>
          <p style="text-indent:0; margin-bottom:10px;"><strong>โจทย์ปัญหา (Problem Statement):</strong><br>หยดน้ำบนผิวทองคำเปลือยมีมุมสัมผัส $	heta_1 = 45^\circ$ เมื่อเคลือบด้วย Octadecanethiol SAM ($-	ext{CH}_3$ terminal) มุมสัมผัสเปลี่ยนเป็น $	heta_2 = 112^\circ$ กำหนดความตึงผิวของน้ำ $\gamma_{LV} = 72.8	ext{ mN/m}$ จงคำนวณหาการเปลี่ยนแปลงค่า $(\gamma_{SV} - \gamma_{SL})$</p>
          <div style="background:rgba(255,255,255,0.85); border:1px solid #e2e8f0; padding:12px 16px; border-radius:6px; margin:12px 0;">
            <strong style="color:#1e3a8a;">การวิเคราะห์และการคำนวณอย่างละเอียด:</strong><br>
            <p style="text-indent:0; margin:6px 0 0 0; line-height:1.85;">1. สภาพเดิม: $(\gamma_{SV} - \gamma_{SL})_1 = \gamma_{LV} \cos(45^\circ) = 72.8 \times 0.7071 = +51.48\text{ mN/m}$<br>2. หลังเคลือบ SAM: $(\gamma_{SV} - \gamma_{SL})_2 = \gamma_{LV} \cos(112^\circ) = 72.8 \times (-0.3746) = -27.27\text{ mN/m}$<br>3. การเปลี่ยนแปลง $\Delta = -27.27 - 51.48 = -78.75\text{ mN/m}$</p>
          </div>
          <div style="background:#f0fdf4; border-left:4px solid #16a34a; padding:10px 14px; margin-top:10px; font-size:9.5pt; color:#166534; border-radius:0 6px 6px 0;">
            💡 <strong>นัยสำคัญทางกายภาพและการประยุกต์ใช้งาน (Physical Insight):</strong><br>
            <span style="color:#14532d;">ค่าพลังงานพื้นผิวลดลงอย่างมาก ส่งผลให้หยดน้ำม้วนตัวเป็นทรงกลมและไม่เกาะติดผิว</span>
          </div>
        </div>
              </div>
  <div class="code-group">

        <div class="code-box">
          <div class="code-header">💻 แบบจำลองเชิงคำนวณภาษาไพทอน (Computational Python 3.11): กรณีศึกษา: การสร้างชิปตรวจยีนด้วยดีเอ็นเอออริกามิ (DNA Origami Biosensors)</div>
          <pre><code>การจัดเรียงตัวรับโมเลกุลเดี่ยวบนแผ่นดีเอ็นเอออริกามิขนาด $100	ext{ nm} 	imes 70	ext{ nm}$ ช่วยให้สามารถตรวจจับการกลายพันธุ์ของยีนมะเร็งได้ในระดับโมเลกุลเดี่ยว (Single-Molecule Sensitivity) โดยไม่ต้องผ่านกระบวนการเพิ่มจำนวนสารพันธุกรรม PCR</code></pre>
        </div>
        <p style="font-size:9.5pt; color:#475569; margin-top:-6px; margin-bottom:18px; text-indent:0;"><em>คำอธิบายอัลกอริทึมการจำลอง:</em> สคริปต์ไพทอนสำหรับการคำนวณและจำลองเชิงตัวเลข</p>
              </div>
  <div class="lab-connection-block">
    <h3>🔬 การเชื่อมโยงสู่ห้องปฏิบัติการเสมือนจริงและเทคนิคการทดลอง (Virtual Lab Connection)</h3>
    <div style='background:#f0fdf4; border:1px solid #bbf7d0; border-left:5px solid #16a34a; padding:12px 16px; margin-bottom:14px; border-radius:6px;'><strong style='color:#166534; font-size:10.5pt;'>การจำลองจลนศาสตร์การเติบโตของชั้นโมเลกุล SAMs</strong><p style='margin:6px 0 0 0; color:#14532d; text-indent:0; line-height:1.8;'>sams_growth_kinetics.py</p></div>
  </div>
  <div class="cases-block">
    <h3>🌐 กรณีศึกษางานวิจัยแนวหน้าและนวัตกรรมอุตสาหกรรม (Frontier Case Studies)</h3>
    <div style='background:#eff6ff; border:1px solid #bfdbfe; border-left:5px solid #2563eb; padding:12px 16px; margin-bottom:14px; border-radius:6px;'><strong style='color:#1e40af; font-size:10.5pt;'>การเชื่อมโยงกับ Virtual Lab 15: การจำลองการประกอบตัวเองของโมเลกุล SAMs และ DNA Origami</strong><p style='margin:6px 0 0 0; color:#1e3a8a; text-indent:0; line-height:1.8;'>ผู้เรียนสามารถเลือกหัวจับและหางฟังก์ชันนัลใน Lab 15 เพื่อสังเกตการจัดเรียงตัวของโมเลกุล วัดมุมเอียง และทดสอบมุมสัมผัสหยดน้ำแบบอินเทอร์แอคทีฟ</p></div>
  </div>

      <div class="checkpoint-box" style="background:#fefce8; border:1px solid #fef08a; border-left:5px solid #eab308; padding:14px 18px; margin:24px 0 35px 0; border-radius:6px; page-break-inside:avoid;">
        <strong style="color:#854d0e; font-size:10pt;">🎯 จุดตรวจประเมินความเข้าใจและคำถามทบทวนประจำหัวข้อ 3.5 (Concept Checkpoint)</strong>
        <ul style="margin:8px 0 0 0; padding-left:20px; color:#713f12; font-size:9.5pt; line-height:1.8;">
          <li>จงอธิบายแนวคิดรวบยอดหลักของ การประกอบตัวเองระดับโมเลกุลและชั้นโมเลกุลจัดตัวชิด และความแตกต่างจากพฤติกรรมในระดับมหภาค</li>
          <li>พารามิเตอร์ใดเป็นปัจจัยวิกฤตที่ควบคุมสมบัติทางฟิสิกส์ในหัวข้อนี้ และมีผลกระทบอย่างไร?</li>
          <li>เชื่อมโยงหลักการฟิสิกส์ในหัวข้อนี้เข้ากับการประยุกต์ใช้จริงในเทคโนโลยีสมัยใหม่</li>
        </ul>
      </div>
    </div>
    

      <div class="summary-box">
        <h3 style="color:#1e40af; margin-top:0; font-size:13pt;">📋 สรุปสาระสำคัญประจำบทที่ 3 (Chapter 3 Key Takeaways)</h3>
        <ul style="margin:0; padding-left:22px; font-size:10pt; line-height:1.95; color:#1e293b;">
          <li style='margin-bottom:8px;'>การสังเคราะห์แบบ Bottom-Up อาศัยแบบจำลองของลาแมร์ในการแยก Burst Nucleation ออกจาก Growth เพื่อสร้างผลึก Monodisperse</li><li style='margin-bottom:8px;'>การสังเคราะห์แบบ Top-Down ผลักดันด้วย EUV Lithography ($\lambda = 13.5	ext{ nm}$) และ EBL สำหรับสร้างลวดลายขนาดต่ำกว่า 10 นาโนเมตร</li><li style='margin-bottom:8px;'>CVD ใช้ปฏิกิริยาเคมีบนผิวสร้างกราฟีนและฟิล์มบาง ขณะที่ PVD สปัตเตอริงและอีบีมใช้การระเหยทางกลในสุญญากาศ</li><li style='margin-bottom:8px;'>เทคโนโลยี ALD ใช้ปฏิกิริยาเคมีที่จำกัดตัวเองสองขั้นตอน ทำให้ควบคุมความหนาระดับอะตอมเดี่ยวและความสม่ำเสมอ $100\%$ ในร่องลึก 3D</li><li style='margin-bottom:8px;'>การประกอบตัวเองระดับโมเลกุล (SAMs และ DNA Origami) ขับเคลื่อนด้วยการลดพลังงานอิสระเพื่อสร้างโครงสร้างนาโนระเบียบสูงโดยธรรมชาติ</li>
        </ul>
      </div>

      <div class="problems-section">
        <h3 style="color:#0f172a; margin-top:0; font-size:14pt; border-bottom:2px solid #cbd5e1; padding-bottom:8px;">
          📚 แบบฝึกหัดและโจทย์ปัญหาท้ายบทที่ 3 (End-of-Chapter Problems)
        </h3>
        
        <h4 style="color:#1e3a8a; font-size:11.5pt; margin-top:18px;">ตอนที่ 1: คำถามเชิงมโนทัศน์และการวิเคราะห์เชิงฟิสิกส์ (Conceptual & Analytical Questions)</h4>
        <ol style="padding-left:22px; font-size:10pt; line-height:1.9; color:#334155;">
          <li style='margin-bottom:8px;'>จงอธิบาย 3 ขั้นตอนหลักในแบบจำลองการเกิดนิวเคลียสและการเติบโตของผลึกของลาแมร์ (LaMer Model)</li><li style='margin-bottom:8px;'>เพราะเหตุใดการเปลี่ยนความยาวคลื่นแสงจาก DUV (193 nm) สู่ EUV (13.5 nm) จึงเพิ่มความละเอียดของชิปได้อย่างก้าวกระโดด?</li><li style='margin-bottom:8px;'>จงเปรียบเทียบข้อดีและข้อจำกัดระหว่างเทคนิค CVD และ PVD Magnetron Sputtering</li><li style='margin-bottom:8px;'>อธิบายกลไก Self-Limiting ในกระบวนการ ALD Al2O3 และเหตุใดจึงได้ฟิล์มที่มีความสม่ำเสมอ 100% ในร่องลึก</li><li style='margin-bottom:8px;'>องค์ประกอบ 3 ส่วนของโมเลกุล SAMs ทำหน้าที่อะไรบ้างในการสร้างฟิล์มที่มีระเบียบ?</li><li style='margin-bottom:8px;'>ปรากฏการณ์ Ostwald Ripening คืออะไร และส่งผลเสียอย่างไรต่อการกระจายขนาดของอนุภาคนาโน?</li><li style='margin-bottom:8px;'>Proximity Effect ใน Electron Beam Lithography เกิดจากฟิสิกส์ใด และมีวิธีแก้ไขอย่างไร?</li><li style='margin-bottom:8px;'>จงอธิบายหลักการทำงานของเทคโนโลยี DNA Origami ในการประกอบโครงสร้างนาโน 3 มิติ</li>
        </ol>

        <h4 style="color:#166534; font-size:11.5pt; margin-top:22px;">ตอนที่ 2: โจทย์ปัญหาการคำนวณเชิงตัวเลขและการพิสูจน์ (Quantitative & Numerical Problems)</h4>
        <ol style="padding-left:22px; font-size:10pt; line-height:1.9; color:#334155;">
          <li style='margin-bottom:8px;'>คำนวณหารัศมีวิกฤต $r^*$ ของการเกิดนิวเคลียสทองคำที่ $T = 400	ext{ K}$ เมื่อ $S = 10.0$, $\gamma = 0.35	ext{ J/m}^2$, $V_m = 1.02 	imes 10^{-5}	ext{ m}^3/	ext{mol}$</li><li style='margin-bottom:8px;'>เครื่องฉายแสง EUV มี $	ext{NA} = 0.33$, $\lambda = 13.5	ext{ nm}$, $k_1 = 0.33$ จงคำนวณหาขนาดเส้นวิกฤตขั้นต่ำ CD</li><li style='margin-bottom:8px;'>ต้องการเคลือบฟิล์ม $	ext{Al}_2	ext{O}_3$ หนา 15.0 nm ด้วยเครื่อง ALD ที่มี $	ext{GPC} = 0.10	ext{ nm/cycle}$ จงคำนวณจำนวนรอบที่ต้องใช้</li><li style='margin-bottom:8px;'>จงคำนวณหามวลของฟิล์มเงิน (Ag) หนา 50 nm บนเวเฟอร์ขนาด 6 นิ้ว จากการเคลือบด้วย E-Beam Evaporation ($ho = 10.49	ext{ g/cm}^3$)</li><li style='margin-bottom:8px;'>แผ่นทองคำพื้นที่ $2.0	ext{ cm}^2$ เคลือบด้วย Decanethiol SAM ($a_0 = 0.214	ext{ nm}^2$) จงคำนวณจำนวนโมเลกุลและมวลรวมของสารบนแผ่น</li><li style='margin-bottom:8px;'>จงคำนวณระยะชัดลึก DOF ของระบบเลนส์ DUV Immersion ที่มี $\lambda = 193	ext{ nm}$, $	ext{NA} = 1.35$, $k_2 = 0.60$</li><li style='margin-bottom:8px;'>คำนวณเวลาที่ใช้ในการเขียนลวดลาย EBL พื้นที่ $200	ext{ }\mu	ext{m} 	imes 200	ext{ }\mu	ext{m}$ เมื่อใช้กระแส 200 pA และโดส $300	ext{ }\mu	ext{C/cm}^2$</li>
        </ol>

        <h4 style="color:#7c2d12; font-size:11.5pt; margin-top:22px;">ตอนที่ 3: โจทย์ประยุกต์ การออกแบบเชิงวิศวกรรม และการจำลอง (Applied Design & Modeling Problems)</h4>
        <ol style="padding-left:22px; font-size:10pt; line-height:1.9; color:#334155;">
          <li style='margin-bottom:8px;'>จงออกแบบกระบวนการผลิตเกตทรานซิสเตอร์ High-k Metal Gate (HKMG) ขนาด 3 นาโนเมตร โดยบูรณาการเทคนิค EUV, ALD และ RIE</li><li style='margin-bottom:8px;'>ออกแบบระบบสังเคราะห์กราฟีนคุณภาพสูงระดับอุตสาหกรรมด้วยเครื่อง Roll-to-Roll Plasma CVD</li><li style='margin-bottom:8px;'>วิเคราะห์แนวทางการออกแบบพื้นผิวซูเปอร์ไฮโดรโฟบิก (Superhydrophobic Surfaces) เลียนแบบใบบัวโดยใช้โมเลกุล SAMs</li><li style='margin-bottom:8px;'>เขียนโค้ด Python เพื่อจำลองความหนาของฟิล์ม ALD เทียบกับจำนวนรอบ และคำนวณค่าเบี่ยงเบนความหนาในร่องลึก Aspect Ratio 100:1</li>
        </ol>
      </div>
    </div>
    """
