# -*- coding: utf-8 -*-
"""
Chapter 5: วัสดุคาร์บอนระดับนาโนและวัสดุสองมิติ
Carbon Nanomaterials, Fullerenes, Carbon Nanotubes, Graphene, TMDs & Twistronics
"""

def get_chapter_5():
    return r"""
    <div class="chapter-container">
      <div class="chapter-hero">
        <div class="chapter-badge">CHAPTER 05 • NANOTECHNOLOGICAL PHYSICS</div>
        <h1 class="chapter-title">วัสดุคาร์บอนระดับนาโนและวัสดุสองมิติ</h1>
        <p class="chapter-subtitle">Carbon Nanomaterials, Fullerenes, Carbon Nanotubes, Graphene, TMDs & Twistronics</p>
      </div>

      <div class="diagram-wrap">
        <img src="../assets/diagrams/ch05_carbon_and_2d.svg" alt="วัสดุคาร์บอนระดับนาโนและวัสดุสองมิติ">
        <div class="caption">ภาพที่ 5.1 แผนผังวิวัฒนาการวัสดุคาร์บอน (0D C60, 1D CNTs, 2D Graphene), กรวยดิแรค, โครงสร้าง TMDs และ Moiré Flat Bands ใน Twistronics</div>
      </div>

      
    <div class="topic-section">
      <h2>5.1 ฟุลเลอรีน C60 และอนุพันธ์โมเลกุลคาร์บอน</h2>
      <div class="topic-en-title">(Buckminsterfullerene (C60), Endohedral Fullerenes & Molecular Carbon)</div>
      
      <div class="topic-intro">
        <p>การค้นพบโมเลกุลบัคมินสเตอร์ฟุลเลอรีน (Buckminsterfullerene: $	ext{C}_{60}$) ในปี 1985 โดยแฮโรลด์ โครโต, ริชาร์ด สมอลลีย์ และรอเบิร์ต เคิร์ล (ได้รับรางวัลโนเบลสาขาเคมีในปี 1996) ถือเป็นจุดเริ่มต้นของยุคทองแห่งวัสดุศาสตร์คาร์บอนระดับนาโน</p>
    <p>โมเลกุล $	ext{C}_{60}$ มีโครงสร้างรูปทรงกลมกลวงสมมาตรแบบไอโคซาฮีดรอนปลายตัด (Truncated Icosahedron สมมาตรกลุ่ม $I_h$) ประกอบด้วยอะตอมคาร์บอนไฮบริดไดเซชันแบบ $	ext{sp}^2$ จำนวน 60 อะตอม จัดเรียงตัวเป็นวงหกเหลี่ยม (Hexagons) 20 วง และวงห้าเหลี่ยม (Pentagons) 12 วง โดยวงห้าเหลี่ยมทำหน้าที่สร้างความโค้งเชิงบวก (Positive Gaussian Curvature) ให้แก่โครงตาข่ายตามทฤษฎีบทของออยเลอร์สำหรับทรงหลายหน้า ($V - E + F = 2$)</p>
    <p>ด้วยโครงสร้างอิเล็กตรอนที่มีสถานะ LUMO ต่ำและมีความสมมาตรสูง $	ext{C}_{60}$ จึงทำหน้าที่เป็นตัวรับอิเล็กตรอนที่ทรงประสิทธิภาพอย่างยิ่ง (Superb Electron Acceptor) สามารถรับอิเล็กตรอนได้มากถึง 6 ตัวอย่างผันกลับได้ นำไปสู่การพัฒนาอนุพันธ์ละลายน้ำได้ เช่น $	ext{PC}_{61}	ext{BM}$ สำหรับเซลล์แสงอาทิตย์อินทรีย์, ฟุลเลอรีนที่บรรจุอะตอมโลหะภายในโพรง (Endohedral Metallofullerenes: $M@	ext{C}_{82}$), และสารดักจับอนุมูลอิสระประสิทธิภาพสูงในการแพทย์</p>
  </div>

      <div class="subtopic-block">
        <h3>โครงสร้างพันธะและความสมมาตรตามกฎ Isolated Pentagon Rule (IPR)</h3>
            <p>ในโมเลกุล $	ext{C}_{60}$ มีความยาวพันธะ 2 ชนิด: พันธะเดี่ยว $6:5$ (ระหว่างวงหกเหลี่ยมกับวงห้าเหลี่ยม) ยาว $1.45	ext{ \AA}$ และพันธะคู่ $6:6$ (ระหว่างวงหหกเหลี่ยมสองวง) ยาว $1.38	ext{ \AA}$</p>
    <p>กฎ Isolated Pentagon Rule (IPR) ระบุว่าฟุลเลอรีนที่เสถียรจะต้องไม่มีวงห้าเหลี่ยมสองวงใดๆ อยู่ติดกันโดยตรง เพื่อลดความเค้นพันธะและการสะสมประจุ ซึ่ง $	ext{C}_{60}$ เป็นฟุลเลอรีนขนาดเล็กที่สุดที่สอดคล้องกับกฎ IPR นี้</p>
  </div>

      <div class="subtopic-block">
        <h3>อนุพันธ์ PCBM และเซลล์แสงอาทิตย์อินทรีย์ (Bulk Heterojunction OPV)</h3>
            <p>การนำ $	ext{PC}_{61}	ext{BM}$ หรือ $	ext{PC}_{71}	ext{BM}$ มาผสมกับพอลิเมอร์ตัวให้ เช่น $	ext{P3HT}$ หรือ $	ext{PTB7}$ ก่อให้เกิดโครงสร้าง Bulk Heterojunction ที่มีการถ่ายโอนประจุแบบ Ultra-fast ($< 100	ext{ fs}$) ทำให้มีประสิทธิภาพการแปลงพลังงานสูง</p>
  </div>
  <div class="formula-group">

        <div class="equation-box">
          <div class="equation-header">📌 สมการฟิสิกส์หลัก: สูตรทฤษฎีบททรงหลายหน้าของออยเลอร์สำหรับฟุลเลอรีน</div>
          <div class="formula-math">$$n_5 = 12, \qquad n_6 = \frac{N - 20}{2}, \qquad V - E + F = 2$$</div>
          <p style="font-size:9.5pt; margin:4px 0 0 0; color:#334155; line-height:1.75; text-indent:0;"><strong>คำอธิบายตัวแปรและนัยสำคัญ:</strong> จำนวนวงห้าเหลี่ยมคงที่ 12 วงเสมอสำหรับฟุลเลอรีนทุกขนาด</p>
        </div>
            
        <div class="equation-box">
          <div class="equation-header">📌 สมการฟิสิกส์หลัก: เส้นผ่านศูนย์กลางโมเลกุล C60</div>
          <div class="formula-math">$$D_{\text{C60}} = \sqrt{\frac{5a_{\text{C-C}}^2 (1 + \sqrt{5})}{2\pi^2}} \approx 0.710\text{ nm} \quad (7.10\text{ \AA})$$</div>
          <p style="font-size:9.5pt; margin:4px 0 0 0; color:#334155; line-height:1.75; text-indent:0;"><strong>คำอธิบายตัวแปรและนัยสำคัญ:</strong> เส้นผ่านศูนย์กลางโครงสร้างกรงคาร์บอน</p>
        </div>
              </div>

      <div class="table-block">
        <h3>📊 ตารางสมบัติกายภาพและอิเล็กทรอนิกส์ของ C60</h3>
        <table class="data-table">
          <thead><tr>
            <th>พารามิเตอร์</th><th>ค่าเฉพาะ</th><th>หน่วย</th></tr></thead>
<tbody><tr><td>มวลโมเลกุล (Molar Mass)</td><td>720.64</td><td>g/mol</td></tr><tr><td>เส้นผ่านศูนย์กลางลูกกรง (D_cage)</td><td>0.710 (7.10 Å)</td><td>nm</td></tr><tr><td>เส้นผ่านศูนย์กลางภายนอกรวมกลุ่มหมอกอิเล็กตรอน</td><td>1.018 (10.18 Å)</td><td>nm</td></tr><tr><td>ความหนาแน่นผลึก FCC</td><td>1.678</td><td>g/cm3</td></tr><tr><td>ช่องว่างแถบพลังงาน HOMO-LUMO (Optical)</td><td>1.86</td><td>eV</td></tr><tr><td>ความจุในการรับอิเล็กตรอน (Redox States)</td><td>สูงสุด 6 อิเล็กตรอน (C60^6-)</td><td>-</td></tr></tbody></table>
</div>
  <div class="examples-group">

        <div class="example-box">
          <div class="example-header">
            <span>📝 ตัวอย่างการคำนวณที่ 5.1: การคำนวณจำนวนวงหกเหลี่ยมและพันธะทั้งหมดในโมเลกุล C70</span>
            <span style="background:#dcfce7; color:#15803d; font-size:8.5pt; padding:3px 10px; border-radius:4px; font-weight:700;">Step-by-Step Worked Solution</span>
          </div>
          <p style="text-indent:0; margin-bottom:10px;"><strong>โจทย์ปัญหา (Problem Statement):</strong><br>โมเลกุลฟุลเลอรีน $	ext{C}_{70}$ มีอะตอมคาร์บอน $N = 70$ อะตอม แต่ละอะตอมมีพันธะเชื่อมต่อ 3 พันธะ (Crivalent Vertices) จงคำนวณหา (ก) จำนวนวงห้าเหลี่ยม $n_5$ (ข) จำนวนวงหกเหลี่ยม $n_6$ (ค) จำนวนพันธะเคมีทั้งหมด $E$</p>
          <div style="background:rgba(255,255,255,0.85); border:1px solid #e2e8f0; padding:12px 16px; border-radius:6px; margin:12px 0;">
            <strong style="color:#1e3a8a;">การวิเคราะห์และการคำนวณอย่างละเอียด:</strong><br>
            <p style="text-indent:0; margin:6px 0 0 0; line-height:1.85;">1. ตามกฎทรงหลายหน้าของออยเลอร์ จำนวนวงห้าเหลี่ยม $n_5 = 12$ วงเสมอ<br>2. จำนวนวงหกเหลี่ยม $n_6 = \frac{N - 20}{2} = \frac{70 - 20}{2} = 25$ วง<br>3. จำนวนหน้าทั้งหมด $F = n_5 + n_6 = 12 + 25 = 37$ หน้า<br>4. แต่ละอะตอมมี 3 พันธะและ 1 พันธะแชร์ระหว่าง 2 อะตอม: $E = \frac{3 N}{2} = \frac{3 \times 70}{2} = 105$ พันธะ</p>
          </div>
          <div style="background:#f0fdf4; border-left:4px solid #16a34a; padding:10px 14px; margin-top:10px; font-size:9.5pt; color:#166534; border-radius:0 6px 6px 0;">
            💡 <strong>นัยสำคัญทางกายภาพและการประยุกต์ใช้งาน (Physical Insight):</strong><br>
            <span style="color:#14532d;">โมเลกุล $	ext{C}_{70}$ มีรูปร่างคล้ายลูกรักบี้ ประกอบด้วยวงห้าเหลี่ยม 12 วง วงหกเหลี่ยม 25 วง และมีพันธะคาร์บอนทั้งหมด 105 พันธะ</span>
          </div>
        </div>
            
        <div class="example-box">
          <div class="example-header">
            <span>📝 ตัวอย่างการคำนวณที่ 5.2: การคำนวณความหนาแน่นผลึกของของแข็ง C60 (Fullerite)</span>
            <span style="background:#dcfce7; color:#15803d; font-size:8.5pt; padding:3px 10px; border-radius:4px; font-weight:700;">Step-by-Step Worked Solution</span>
          </div>
          <p style="text-indent:0; margin-bottom:10px;"><strong>โจทย์ปัญหา (Problem Statement):</strong><br>โมเลกุล $	ext{C}_{60}$ ตกผลึกเป็นของแข็ง Fullerite โครงสร้าง Face-Centered Cubic (FCC) ที่อุณหภูมิห้อง โดยมีค่าคงที่แลตทิซ $a = 1.417	ext{ nm}$ กำหนดมวลโมลาร์ $M = 720.64	ext{ g/mol}$ จงคำนวณความหนาแน่น $ho$</p>
          <div style="background:rgba(255,255,255,0.85); border:1px solid #e2e8f0; padding:12px 16px; border-radius:6px; margin:12px 0;">
            <strong style="color:#1e3a8a;">การวิเคราะห์และการคำนวณอย่างละเอียด:</strong><br>
            <p style="text-indent:0; margin:6px 0 0 0; line-height:1.85;">1. โครงสร้าง FCC มีจำนวนโมเลกุลต่อยูนิตเซลล์ $Z = 4$ โมเลกุล<br>2. ปริมาตรยูนิตเซลล์ $V_c = a^3 = (1.417 \times 10^{-7}\text{ cm})^3 = 2.845 \times 10^{-21}\text{ cm}^3$<br>3. มวลใน 1 ยูนิตเซลล์ $m = \frac{Z \times M}{N_A} = \frac{4 \times 720.64}{6.022 \times 10^{23}} = 4.787 \times 10^{-21}\text{ g}$<br>4. $\rho = \frac{m}{V_c} = \frac{4.787 \times 10^{-21}\text{ g}}{2.845 \times 10^{-21}\text{ cm}^3} = 1.683\text{ g/cm}^3$</p>
          </div>
          <div style="background:#f0fdf4; border-left:4px solid #16a34a; padding:10px 14px; margin-top:10px; font-size:9.5pt; color:#166534; border-radius:0 6px 6px 0;">
            💡 <strong>นัยสำคัญทางกายภาพและการประยุกต์ใช้งาน (Physical Insight):</strong><br>
            <span style="color:#14532d;">ความหนาแน่น $1.68	ext{ g/cm}^3$ ต่ำกว่ากราไฟต์ ($2.26	ext{ g/cm}^3$) และเพชร ($3.51	ext{ g/cm}^3$) เนื่องจากมีโพรงกลวงขนาดใหญ่อยู่ภายในโมเลกุล</span>
          </div>
        </div>
              </div>
  <div class="code-group">

        <div class="code-box">
          <div class="code-header">💻 แบบจำลองเชิงคำนวณภาษาไพทอน (Computational Python 3.11): กรณีศึกษา: สารต้านอนุมูลอิสระฟุลเลอรีนนาโนในเวชสำอางชะลอวัยและการรักษาโรคทางระบบประสาท</div>
          <pre><code>ด้วยความสามารถในการกำจัดอนุมูลอิสระ (Radical Sponge) ได้มากกว่าวิตามินซีถึง 172 เท่า โมเลกุล $	ext{C}_{60}$ ละลายน้ำได้จึงถูกนำมาใช้ในเซรั่มบำรุงผิวระดับพรีเมียมและการวิจัยยารักษาโรคพาร์กินสันและอัลไซเมอร์</code></pre>
        </div>
        <p style="font-size:9.5pt; color:#475569; margin-top:-6px; margin-bottom:18px; text-indent:0;"><em>คำอธิบายอัลกอริทึมการจำลอง:</em> สคริปต์ไพทอนสำหรับการคำนวณและจำลองเชิงตัวเลข</p>
              </div>
  <div class="lab-connection-block">
    <h3>🔬 การเชื่อมโยงสู่ห้องปฏิบัติการเสมือนจริงและเทคนิคการทดลอง (Virtual Lab Connection)</h3>
    <div style='background:#f0fdf4; border:1px solid #bbf7d0; border-left:5px solid #16a34a; padding:12px 16px; margin-bottom:14px; border-radius:6px;'><strong style='color:#166534; font-size:10.5pt;'>การจำลองพิกัด 3 มิติและโครงสร้างสมมาตรของโมเลกุล C60</strong><p style='margin:6px 0 0 0; color:#14532d; text-indent:0; line-height:1.8;'>c60_geometry_sim.py</p></div>
  </div>
  <div class="cases-block">
    <h3>🌐 กรณีศึกษางานวิจัยแนวหน้าและนวัตกรรมอุตสาหกรรม (Frontier Case Studies)</h3>
    <div style='background:#eff6ff; border:1px solid #bfdbfe; border-left:5px solid #2563eb; padding:12px 16px; margin-bottom:14px; border-radius:6px;'><strong style='color:#1e40af; font-size:10.5pt;'>การเชื่อมโยงกับ Virtual Lab 21: การจำลองโครงสร้างโมเลกุลฟุลเลอรีน C60 และอนุพันธ์ PCBM</strong><p style='margin:6px 0 0 0; color:#1e3a8a; text-indent:0; line-height:1.8;'>ผู้เรียนสามารถหมุนดูโมเลกุล $	ext{C}_{60}$ แบบ 3D ใน Lab 21 ตรวจสอบความยาวพันธะ $6:5$ และ $6:6$ และศึกษาการแทรกตัวของโมเลกุลโลหะใน Endohedral Fullerenes</p></div>
  </div>

      <div class="checkpoint-box" style="background:#fefce8; border:1px solid #fef08a; border-left:5px solid #eab308; padding:14px 18px; margin:24px 0 35px 0; border-radius:6px; page-break-inside:avoid;">
        <strong style="color:#854d0e; font-size:10pt;">🎯 จุดตรวจประเมินความเข้าใจและคำถามทบทวนประจำหัวข้อ 5.1 (Concept Checkpoint)</strong>
        <ul style="margin:8px 0 0 0; padding-left:20px; color:#713f12; font-size:9.5pt; line-height:1.8;">
          <li>จงอธิบายแนวคิดรวบยอดหลักของ ฟุลเลอรีน C60 และอนุพันธ์โมเลกุลคาร์บอน และความแตกต่างจากพฤติกรรมในระดับมหภาค</li>
          <li>พารามิเตอร์ใดเป็นปัจจัยวิกฤตที่ควบคุมสมบัติทางฟิสิกส์ในหัวข้อนี้ และมีผลกระทบอย่างไร?</li>
          <li>เชื่อมโยงหลักการฟิสิกส์ในหัวข้อนี้เข้ากับการประยุกต์ใช้จริงในเทคโนโลยีสมัยใหม่</li>
        </ul>
      </div>
    </div>
    
    <div class="topic-section">
      <h2>5.2 ท่อคาร์บอนนาโน: โครงสร้างไครัลลิตี้และสมบัติอิเล็กทรอนิกส์</h2>
      <div class="topic-en-title">(Carbon Nanotubes (CNTs), Chirality Physics & 1D Electronic Structure)</div>
      
      <div class="topic-intro">
        <p>ท่อคาร์บอนนาโน (Carbon Nanotubes: CNTs) ถูกค้นพบและรายงานอย่างเป็นระบบโดย ซูมิโอะ อิิจิมะ ในปี 1991 โดยมีโครงสร้างเสมือนแผ่นกราฟีนชั้นเดี่ยวที่ถูกม้วนตัวเป็นทรงกระบอกไร้รอยต่อในระดับเส้นผ่านศูนย์กลาง 1 ถึง 3 นาโนเมตร สำหรับท่อผนังเดี่ยว (Single-Walled Carbon Nanotubes: SWCNTs) หรือหลายชั้นซ้อนกันสำหรับท่อหลายผนัง (Multi-Walled Carbon Nanotubes: MWCNTs)</p>
    <p>ความมหัศจรรย์ทางฟิสิกส์ของ SWCNTs คือสมบัติทางไฟฟ้าถูกกำหนดอย่างสมบูรณ์ด้วยเวกเตอร์การม้วนตัวเชิงเรขาคณิตที่เรียกว่า เวกเตอร์ไครัลลิตี้ (Chiral Vector: $ec{C}_h = nec{a}_1 + mec{a}_2$) หรือคู่ดัชนี $(n, m)$ โดยท่อจะเป็นโลหะนำไฟฟ้าบริสุทธิ์ (Metallic) เมื่อ $(n - m)$ หารด้วย 3 ลงตัว และจะเป็นสารกึ่งตัวนำ (Semiconducting) เมื่อ $(n - m)$ หารด้วย 3 ไม่ลงตัว</p>
    <p>นอกจากสมบัติทางไฟฟ้าที่นำกระแสแบบบอลลิสติกได้สูงลิ่วแล้ว CNTs ยังเป็นวัสดุที่มีความแข็งแรงเชิงกลสูงที่สุดชนิดหนึ่งในเอกภพ ด้วยค่ามอดุลัสของยังก์ (Young's Modulus: $Y pprox 1.0	ext{ TPa}$) และความต้านทานแรงดึง (Tensile Strength $> 60	ext{ GPa}$) ซึ่งแข็งแกร่งกว่าเหล็กกล้ากว่า 100 เท่า ที่น้ำหนักเพียงหนึ่งในหก</p>
  </div>

      <div class="subtopic-block">
        <h3>เรขาคณิตของเวกเตอร์ไครัลลิตี้และการจำแนกชนิดของท่อ</h3>
            <p>1. ท่อแบบอาร์มแชร์ (Armchair: $n = m$, หรือ $(n, n)$): มุมไครัล $	heta = 30^\circ$ มีพฤติกรรมเป็นโลหะนำไฟฟ้าเสมอ (Metallic) นำกระแสไฟฟ้าได้ดีกว่าทองแดง</p>
    <p>2. ท่อแบบซิกแซก (Zigzag: $m = 0$, หรือ $(n, 0)$): มุมไครัล $	heta = 0^\circ$ เป็นโลหะเมื่อ $n$ หารด้วย 3 ลงตัว และเป็นสารกึ่งตัวนำเมื่อ $n$ หารด้วย 3 ไม่ลงตัว</p>
    <p>3. ท่อแบบไครัล (Chiral: $n 
eq m 
eq 0$): มุมไครัล $0^\circ < 	heta < 30^\circ$ มีโครงสร้างเกลียววนซ้ายหรือขวา</p>
  </div>

      <div class="subtopic-block">
        <h3>แบบจำลอง Zone Folding และช่องว่างแถบพลังงานของ Semiconducting SWCNTs</h3>
            <p>ช่องว่างแถบพลังงานของท่อสารกึ่งตัวนำแปรผกผันกับเส้นผ่านศูนย์กลางของท่อตามความสัมพันธ์: $E_g pprox rac{2 a_{	ext{C-C}} \gamma_0}{d_t} pprox rac{0.84	ext{ eV}\cdot	ext{nm}}{d_t}$</p>
    <p>ทำให้ท่อขนาดเส้นผ่านศูนย์กลาง $1	ext{ nm}$ มี $E_g pprox 0.84	ext{ eV}$ ซึ่งเหมาะอย่างยิ่งสำหรับทำช่องนำกระแสในทรานซิสเตอร์ยุคหลังซิลิคอน</p>
  </div>
  <div class="formula-group">

        <div class="equation-box">
          <div class="equation-header">📌 สมการฟิสิกส์หลัก: เส้นผ่านศูนย์กลางและมุมไครัลของท่อคาร์บอนนาโน</div>
          <div class="formula-math">$$d_t = \frac{a}{\pi} \sqrt{n^2 + nm + m^2}, \qquad \theta = \arctan\left( \frac{\sqrt{3} m}{2n + m} \right)$$</div>
          <p style="font-size:9.5pt; margin:4px 0 0 0; color:#334155; line-height:1.75; text-indent:0;"><strong>คำอธิบายตัวแปรและนัยสำคัญ:</strong> การคำนวณเส้นผ่านศูนย์กลาง dt และมุมไครัล θ</p>
        </div>
            
        <div class="equation-box">
          <div class="equation-header">📌 สมการฟิสิกส์หลัก: ช่องว่างแถบพลังงานของท่อคาร์บอนนาโนกึ่งตัวนำ</div>
          <div class="formula-math">$$E_g \approx \frac{2 \gamma_0 a_{\text{C-C}}}{d_t} \approx \frac{0.84}{d_t}\text{ eV} \quad (d_t\text{ in nm})$$</div>
          <p style="font-size:9.5pt; margin:4px 0 0 0; color:#334155; line-height:1.75; text-indent:0;"><strong>คำอธิบายตัวแปรและนัยสำคัญ:</strong> ช่องว่างแถบพลังงานแปรผกผันกับขนาดเส้นผ่านศูนย์กลาง</p>
        </div>
              </div>

      <div class="table-block">
        <h3>📊 ตารางเปรียบเทียบชนิดของท่อคาร์บอนนาโนตามดัชนีไครัล (n, m)</h3>
        <table class="data-table">
          <thead><tr>
            <th>ดัชนี (n, m)</th><th>ชนิดโครงสร้าง</th><th>มุมไครัล θ</th><th>สมบัติทางไฟฟ้า</th><th>dt (nm)</th><th>Eg (eV)</th></tr></thead>
<tbody><tr><td>(10, 10)</td><td>Armchair</td><td>30.0°</td><td>โลหะ (Metallic)</td><td>1.356 nm</td><td>0 eV (ไม่มี Bandgap)</td></tr><tr><td>(10, 0)</td><td>Zigzag</td><td>0.0°</td><td>สารกึ่งตัวนำ (Semiconductor)</td><td>0.783 nm</td><td>1.07 eV</td></tr><tr><td>(9, 0)</td><td>Zigzag (9/3=3)</td><td>0.0°</td><td>โลหะกึ่งตัวนำ (Small-gap Metal)</td><td>0.705 nm</td><td>~ 0.08 eV</td></tr><tr><td>(8, 4)</td><td>Chiral</td><td>19.1°</td><td>สารกึ่งตัวนำ (Semiconductor)</td><td>0.829 nm</td><td>1.01 eV</td></tr><tr><td>(6, 5)</td><td>Chiral (HiPco ยอดนิยม)</td><td>27.0°</td><td>สารกึ่งตัวนำ (Semiconductor)</td><td>0.747 nm</td><td>1.12 eV</td></tr></tbody></table>
</div>
  <div class="examples-group">

        <div class="example-box">
          <div class="example-header">
            <span>📝 ตัวอย่างการคำนวณที่ 5.3: การคำนวณเส้นผ่านศูนย์กลางและชนิดทางไฟฟ้าของท่อ (11, 7) SWCNT</span>
            <span style="background:#dcfce7; color:#15803d; font-size:8.5pt; padding:3px 10px; border-radius:4px; font-weight:700;">Step-by-Step Worked Solution</span>
          </div>
          <p style="text-indent:0; margin-bottom:10px;"><strong>โจทย์ปัญหา (Problem Statement):</strong><br>ท่อคาร์บอนนาโนมีดัชนีไครัล $(n, m) = (11, 7)$ กำหนดค่าคงที่โครงผลึกกราฟีน $a = 0.246	ext{ nm}$ และ $a_{	ext{C-C}} = 0.142	ext{ nm}$ จงคำนวณหา (ก) เส้นผ่านศูนย์กลาง $d_t$ (ข) มุมไครัล $	heta$ (ค) ระบุสมบัติทางไฟฟ้าและคำนวณหาช่องว่างแถบพลังงาน $E_g$</p>
          <div style="background:rgba(255,255,255,0.85); border:1px solid #e2e8f0; padding:12px 16px; border-radius:6px; margin:12px 0;">
            <strong style="color:#1e3a8a;">การวิเคราะห์และการคำนวณอย่างละเอียด:</strong><br>
            <p style="text-indent:0; margin:6px 0 0 0; line-height:1.85;">1. คำนวณ $n^2 + nm + m^2 = 11^2 + (11 \times 7) + 7^2 = 121 + 77 + 49 = 247$<br>2. $d_t = \frac{0.246}{\pi} \sqrt{247} = \frac{0.246 \times 15.716}{3.14159} = 1.2306\text{ nm}$<br>3. มุมไครัล $\theta = \arctan\left( \frac{\sqrt{3} \times 7}{2(11) + 7} \right) = \arctan\left( \frac{12.124}{29} \right) = \arctan(0.4181) = 22.69^\circ$<br>4. ตรวจสอบสมบัติทางไฟฟ้า: $n - m = 11 - 7 = 4$ (หารด้วย 3 ไม่ลงตัว $\implies$ สารกึ่งตัวนำ)<br>5. $E_g \approx \frac{0.84}{1.2306} = 0.6826\text{ eV}$</p>
          </div>
          <div style="background:#f0fdf4; border-left:4px solid #16a34a; padding:10px 14px; margin-top:10px; font-size:9.5pt; color:#166534; border-radius:0 6px 6px 0;">
            💡 <strong>นัยสำคัญทางกายภาพและการประยุกต์ใช้งาน (Physical Insight):</strong><br>
            <span style="color:#14532d;">ท่อ $(11, 7)$ เป็นท่อแบบไครัลกึ่งตัวนำ มีเส้นผ่านศูนย์กลาง $1.23	ext{ nm}$ และมีช่องว่างแถบพลังงาน $0.683	ext{ eV}$</span>
          </div>
        </div>
            
        <div class="example-box">
          <div class="example-header">
            <span>📝 ตัวอย่างการคำนวณที่ 5.4: การคำนวณแรงดึงสูงสุดที่ท่อคาร์บอนนาโนเดี่ยวสามารถรับได้</span>
            <span style="background:#dcfce7; color:#15803d; font-size:8.5pt; padding:3px 10px; border-radius:4px; font-weight:700;">Step-by-Step Worked Solution</span>
          </div>
          <p style="text-indent:0; margin-bottom:10px;"><strong>โจทย์ปัญหา (Problem Statement):</strong><br>ท่อ $(10, 10)$ SWCNT มีเส้นผ่านศูนย์กลาง $d_t = 1.356	ext{ nm}$ สมมติความหนาของผนังท่อเท่ากับระยะห่างระหว่างชั้นกราไฟต์ $t = 0.34	ext{ nm}$ กำหนดความต้านทานแรงดึง $\sigma_{	ext{UTS}} = 60	ext{ GPa}$ จงคำนวณแรงดึงสูงสุด $F_{	ext{max}}$ ก่อนท่อจะขาด</p>
          <div style="background:rgba(255,255,255,0.85); border:1px solid #e2e8f0; padding:12px 16px; border-radius:6px; margin:12px 0;">
            <strong style="color:#1e3a8a;">การวิเคราะห์และการคำนวณอย่างละเอียด:</strong><br>
            <p style="text-indent:0; margin:6px 0 0 0; line-height:1.85;">1. พื้นที่หน้าตัดวงแหวน $A \approx \pi d_t t = \pi (1.356 \times 10^{-9}\text{ m}) \times (0.34 \times 10^{-9}\text{ m}) = 1.448 \times 10^{-18}\text{ m}^2$<br>2. $F_{\text{max}} = \sigma_{\text{UTS}} \times A = (60 \times 10^9\text{ N/m}^2) \times (1.448 \times 10^{-18}\text{ m}^2) = 8.689 \times 10^{-8}\text{ N} = 86.89\text{ nN}$</p>
          </div>
          <div style="background:#f0fdf4; border-left:4px solid #16a34a; padding:10px 14px; margin-top:10px; font-size:9.5pt; color:#166534; border-radius:0 6px 6px 0;">
            💡 <strong>นัยสำคัญทางกายภาพและการประยุกต์ใช้งาน (Physical Insight):</strong><br>
            <span style="color:#14532d;">แรงดึงเกือบ 87 นาโนนิวตันสำหรับท่อที่มีขนาดเพียงโมเลกุลเดี่ยว แสดงถึงความแข็งแกร่งระดับมหาศาล</span>
          </div>
        </div>
              </div>
  <div class="code-group">

        <div class="code-box">
          <div class="code-header">💻 แบบจำลองเชิงคำนวณภาษาไพทอน (Computational Python 3.11): กรณีศึกษา: ไมโครโปรเซสเซอร์คาร์บอนนาโนทรานซิสเตอร์ 16 บิต (RV16X-NANO) โดย MIT</div>
          <pre><code>ทีมนักวิจัยของ MIT ประสบความสำเร็จในการสร้างชิปประมวลผลสถาปัตยกรรม RISC-V ที่ประกอบด้วย CNT-FET มากกว่า 14,000 ตัว ทำงานได้อย่างสมบูรณ์ โดยประหยัดพลังงานกว่าและเร็วกว่าชิปซิลิคอนแบบเดิมถึง 10 เท่า</code></pre>
        </div>
        <p style="font-size:9.5pt; color:#475569; margin-top:-6px; margin-bottom:18px; text-indent:0;"><em>คำอธิบายอัลกอริทึมการจำลอง:</em> สคริปต์ไพทอนสำหรับการคำนวณและจำลองเชิงตัวเลข</p>
              </div>
  <div class="lab-connection-block">
    <h3>🔬 การเชื่อมโยงสู่ห้องปฏิบัติการเสมือนจริงและเทคนิคการทดลอง (Virtual Lab Connection)</h3>
    <div style='background:#f0fdf4; border:1px solid #bbf7d0; border-left:5px solid #16a34a; padding:12px 16px; margin-bottom:14px; border-radius:6px;'><strong style='color:#166534; font-size:10.5pt;'>การคำนวณพารามิเตอร์ไครัลลิตี้ของท่อคาร์บอนนาโน</strong><p style='margin:6px 0 0 0; color:#14532d; text-indent:0; line-height:1.8;'>cnt_chirality_calculator.py</p></div>
  </div>
  <div class="cases-block">
    <h3>🌐 กรณีศึกษางานวิจัยแนวหน้าและนวัตกรรมอุตสาหกรรม (Frontier Case Studies)</h3>
    <div style='background:#eff6ff; border:1px solid #bfdbfe; border-left:5px solid #2563eb; padding:12px 16px; margin-bottom:14px; border-radius:6px;'><strong style='color:#1e40af; font-size:10.5pt;'>การเชื่อมโยงกับ Virtual Lab 22: การจำลองโครงสร้างไครัลลิตี้และแถบพลังงานของท่อคาร์บอนนาโน</strong><p style='margin:6px 0 0 0; color:#1e3a8a; text-indent:0; line-height:1.8;'>ผู้เรียนสามารถม้วนแผ่นกราฟีนตามดัชนี $(n, m)$ ใน Lab 22 สังเกตการเปลี่ยนรูปเป็นท่อ 3D และตรวจสอบกราฟ Density of States แบบ 1D Van Hove Singularities</p></div>
  </div>

      <div class="checkpoint-box" style="background:#fefce8; border:1px solid #fef08a; border-left:5px solid #eab308; padding:14px 18px; margin:24px 0 35px 0; border-radius:6px; page-break-inside:avoid;">
        <strong style="color:#854d0e; font-size:10pt;">🎯 จุดตรวจประเมินความเข้าใจและคำถามทบทวนประจำหัวข้อ 5.2 (Concept Checkpoint)</strong>
        <ul style="margin:8px 0 0 0; padding-left:20px; color:#713f12; font-size:9.5pt; line-height:1.8;">
          <li>จงอธิบายแนวคิดรวบยอดหลักของ ท่อคาร์บอนนาโน: โครงสร้างไครัลลิตี้และสมบัติอิเล็กทรอนิกส์ และความแตกต่างจากพฤติกรรมในระดับมหภาค</li>
          <li>พารามิเตอร์ใดเป็นปัจจัยวิกฤตที่ควบคุมสมบัติทางฟิสิกส์ในหัวข้อนี้ และมีผลกระทบอย่างไร?</li>
          <li>เชื่อมโยงหลักการฟิสิกส์ในหัวข้อนี้เข้ากับการประยุกต์ใช้จริงในเทคโนโลยีสมัยใหม่</li>
        </ul>
      </div>
    </div>
    
    <div class="topic-section">
      <h2>5.3 กราฟีน: กรวยดิแรค เฟอร์มิออนไร้มวล และอิเล็กทรอนิกส์ 2D</h2>
      <div class="topic-en-title">(Graphene Physics: Dirac Cones, Massless Dirac Fermions & Klein Tunneling)</div>
      
      <div class="topic-intro">
        <p>กราฟีน (Graphene) คือผลึกสองมิติของอะตอมคาร์บอนหนาเพียงหนึ่งชั้นอะตอมที่เรียงตัวกันเป็นโครงตาข่ายรังผึ้งหกเหลี่ยม (Honeycomb Lattice) ซึ่งถูกแยกเดี่ยวสำเร็จเป็นครั้งแรกในปี 2004 โดยอันเดร ไกม์ และคอนสแตนติน โนโวเซลอฟ ณ มหาวิทยาลัยแมนเชสเตอร์ (ได้รับรางวัลโนเบลสาขาฟิสิกส์ในปี 2010)</p>
    <p>ความโดดเด่นทางฟิสิกส์เชิงทฤษฎีของกราฟีนอยู่ที่โครงสร้างแถบพลังงานรอบจุดยอดของเขตบริลลูออง (จุด $K$ และ $K'$) ซึ่งแถบการนำและแถบเวเลนซ์สัมผัสกันเป็นจุดยอดรูปกรวยคู่ เรียกว่า กรวยดิแรค (Dirac Cones) ส่งผลให้ความสัมพันธ์การกระจายตัวของพลังงานเป็นเชิงเส้นสมบูรณ์: $E(ec{k}) = \pm \hbar v_F |ec{k}|$ โดยมีค่าความเร็วเฟอร์มิ $v_F pprox 10^6	ext{ m/s}$ (ประมาณ 1/300 ของความเร็วแสง)</p>
    <p>ความสัมพันธ์เชิงเส้นนี้ทำให้อิเล็กตรอนในกราฟีนประพฤติตนเสมือนเป็น อนุภาคดิแรคเฟอร์มิออนไร้มวลสัมพัทธภาพ (Relativistic Massless Dirac Fermions) ซึ่งอธิบายด้วยสมการดิแรค 2 มิติ ก่อให้เกิดปรากฏการณ์ควอนตัมเชิงทฤษฎีขั้นสูง เช่น ปรากฏการณ์ทะลุผ่านของไคลน์ (Klein Tunneling) ที่อิเล็กตรอนสามารถทะลุกำแพงศักย์สูงได้ด้วยความน่าจะเป็น 100% โดยไม่มีการสะท้อนกลับ และสภาพคล่องตัวของพาหะที่สูงเกิน $200,000	ext{ cm}^2/	ext{V}\cdot	ext{s}$</p>
  </div>

      <div class="subtopic-block">
        <h3>การแก้แบบจำลอง Tight-Binding สำหรับโครงตาข่ายรังผึ้งกราฟีน</h3>
            <p>โครงตาข่ายรังผึ้งประกอบด้วย 2 ซับแลตทิซย่อย $A$ และ $B$ ความสัมพันธ์การกระจายตัวพลังงานจาก Tight-Binding Model:</p>
    <p>$$E(k_x, k_y) = \pm t \sqrt{1 + 4\cos\left(rac{\sqrt{3} k_x a}{2}ight)\cos\left(rac{k_y a}{2}ight) + 4\cos^2\left(rac{k_y a}{2}ight)}$$</p>
    <p>เมื่อกระจายรอบจุดดิแรค $ec{k} = ec{K} + ec{q}$ ($|ec{q}| a \ll 1$) จะได้สมการเชิงเส้น: $E(ec{q}) = \pm \hbar v_F |ec{q}|$ โดยมี $v_F = rac{3 t a_{	ext{C-C}}}{2 \hbar} pprox 1.0 	imes 10^6	ext{ m/s}$ ($t pprox 2.8	ext{ eV}$)</p>
  </div>

      <div class="subtopic-block">
        <h3>ปรากฏการณ์ทะลุผ่านของไคลน์ (Klein Tunneling) และความสมมาตรแบบไครัล</h3>
            <p>อิเล็กตรอนในกราฟีนมีสถานะสปินเทียม (Pseudospin) ที่ชี้ตามทิศทางโมเมนตัมเสมอ (Chirality) เมื่ออิเล็กตรอนวิ่งชนกำแพงศักย์ไฟฟ้าในแนวตั้งฉาก ($	heta = 0$) การสะท้อนกลับจะต้องกลับทิศสปินเทียมซึ่งถูกห้ามโดยความสมมาตร ทำให้สัมประสิทธิ์การส่งผ่าน $T = 1.0$ เสมอโดยไม่ขึ้นกับความสูงของกำแพงศักย์</p>
  </div>
  <div class="formula-group">

        <div class="equation-box">
          <div class="equation-header">📌 สมการฟิสิกส์หลัก: ความสัมพันธ์การกระจายตัวเชิงเส้นรอบจุดดิแรค</div>
          <div class="formula-math">$$E(\vec{q}) = \pm \hbar v_F |\vec{q}| = \pm \hbar v_F \sqrt{q_x^2 + q_y^2}, \qquad v_F \approx 10^6\text{ m/s}$$</div>
          <p style="font-size:9.5pt; margin:4px 0 0 0; color:#334155; line-height:1.75; text-indent:0;"><strong>คำอธิบายตัวแปรและนัยสำคัญ:</strong> พลังงานเชิงเส้นของดิแรคเฟอร์มิออนไร้มวล</p>
        </div>
            
        <div class="equation-box">
          <div class="equation-header">📌 สมการฟิสิกส์หลัก: ความหนาแน่นของสถานะพลังงานในกราฟีน</div>
          <div class="formula-math">$$g(E) = \frac{2 |E|}{\pi (\hbar v_F)^2}, \qquad n = \frac{k_F^2}{\pi} = \frac{E_F^2}{\pi (\hbar v_F)^2}$$</div>
          <p style="font-size:9.5pt; margin:4px 0 0 0; color:#334155; line-height:1.75; text-indent:0;"><strong>คำอธิบายตัวแปรและนัยสำคัญ:</strong> DOS แปรผันตรงกับพลังงาน E และเป็นศูนย์ที่จุด Dirac Point</p>
        </div>
              </div>

      <div class="table-block">
        <h3>📊 ตารางสมบัติเด่นขั้นสุดยอดของกราฟีนชั้นเดี่ยว (Monolayer Graphene)</h3>
        <table class="data-table">
          <thead><tr>
            <th>สมบัติทางฟิสิกส์</th><th>ค่าเฉพาะ</th><th>การเปรียบเทียบกับวัสดุเดิม</th></tr></thead>
<tbody><tr><td>ความเร็วเฟอร์มิ v_F</td><td>~ 1.0 × 10^6 m/s</td><td>เร็วกว่าในซิลิคอน 10 เท่า</td></tr><tr><td>สภาพคล่องตัวของอิเล็กตรอน μ</td><td>> 200,000 cm2/V·s (บน h-BN)</td><td>สูงกว่าซิลิคอน 150 เท่า</td></tr><tr><td>สภาพนำความร้อน κ</td><td>3,000 - 5,000 W/m·K</td><td>สูงกว่าทองแดงและเพชร</td></tr><tr><td>ความแข็งแรงเชิงกล (Young's Modulus)</td><td>1.0 TPa (1,000 GPa)</td><td>แข็งแกร่งกว่าเหล็กกล้า 100 เท่า</td></tr><tr><td>ความโปร่งแสงทางสายตา (Transmittance)</td><td>97.7% (ดูดกลืน πα = 2.3%)</td><td>โปร่งแสงเกือบสมบูรณ์แบบ</td></tr><tr><td>พื้นที่ผิวจำเพาะทางทฤษฎี</td><td>2,630 m2/g</td><td>สูงที่สุดในบรรดาวัสดุคาร์บอน</td></tr></tbody></table>
</div>
  <div class="examples-group">

        <div class="example-box">
          <div class="example-header">
            <span>📝 ตัวอย่างการคำนวณที่ 5.5: การคำนวณตำแหน่งพลังงานเฟอร์มิและความเข้มข้นของพาหะในกราฟีนที่ถูกเกต</span>
            <span style="background:#dcfce7; color:#15803d; font-size:8.5pt; padding:3px 10px; border-radius:4px; font-weight:700;">Step-by-Step Worked Solution</span>
          </div>
          <p style="text-indent:0; margin-bottom:10px;"><strong>โจทย์ปัญหา (Problem Statement):</strong><br>แผ่นกราฟีนบนฉนวน $	ext{SiO}_2$ หนา $d = 300	ext{ nm}$ ($\epsilon_r = 3.9$) ถูกจ่ายแรงดันเกตหลัง $V_g = +40.0	ext{ V}$ จงคำนวณหา (ก) ความเข้มข้นพาหะประจุ $n$ (ข) ตำแหน่งระดับเฟอร์มิ $E_F$ เหนือจุดดิแรคในหน่วย eV</p>
          <div style="background:rgba(255,255,255,0.85); border:1px solid #e2e8f0; padding:12px 16px; border-radius:6px; margin:12px 0;">
            <strong style="color:#1e3a8a;">การวิเคราะห์และการคำนวณอย่างละเอียด:</strong><br>
            <p style="text-indent:0; margin:6px 0 0 0; line-height:1.85;">1. ความจุไฟฟ้าต่อหน่วยพื้นที่ $C_{\text{ox}} = \frac{\epsilon_0 \epsilon_r}{d} = \frac{(8.854 \times 10^{-12})(3.9)}{300 \times 10^{-9}} = 1.151 \times 10^{-4}\text{ F/m}^2$<br>2. ความหนาแน่นประจุ $n = \frac{C_{\text{ox}} V_g}{e} = \frac{(1.151 \times 10^{-4}) \times 40.0}{1.602 \times 10^{-19}} = 2.874 \times 10^{16}\text{ m}^{-2} = 2.874 \times 10^{12}\text{ cm}^{-2}$<br>3. เวกเตอร์คลื่นเฟอร์มิ $k_F = \sqrt{\pi n} = \sqrt{\pi \times (2.874 \times 10^{16})} = 3.005 \times 10^8\text{ m}^{-1}$<br>4. $E_F = \hbar v_F k_F = (1.0546 \times 10^{-34}) \times (1.0 \times 10^6) \times (3.005 \times 10^8) = 3.169 \times 10^{-20}\text{ J} = 0.1978\text{ eV}$</p>
          </div>
          <div style="background:#f0fdf4; border-left:4px solid #16a34a; padding:10px 14px; margin-top:10px; font-size:9.5pt; color:#166534; border-radius:0 6px 6px 0;">
            💡 <strong>นัยสำคัญทางกายภาพและการประยุกต์ใช้งาน (Physical Insight):</strong><br>
            <span style="color:#14532d;">แรงดันเกต $+40	ext{ V}$ ช่วยเลื่อนระดับเฟอร์มิขึ้นไป $0.198	ext{ eV}$ ในแถบการนำ เหนี่ยวนำให้อิเล็กตรอนมีความหนาแน่น $2.87 	imes 10^{12}	ext{ cm}^{-2}$</span>
          </div>
        </div>
            
        <div class="example-box">
          <div class="example-header">
            <span>📝 ตัวอย่างการคำนวณที่ 5.6: การคำนวณการดูดกลืนแสงเชิงทฤษฎีของกราฟีนชั้นเดี่ยว</span>
            <span style="background:#dcfce7; color:#15803d; font-size:8.5pt; padding:3px 10px; border-radius:4px; font-weight:700;">Step-by-Step Worked Solution</span>
          </div>
          <p style="text-indent:0; margin-bottom:10px;"><strong>โจทย์ปัญหา (Problem Statement):</strong><br>จงแสดงว่าการดูดกลืนแสงของกราฟีนชั้นเดี่ยวในย่านแสงขาวขึ้นกับค่าคงที่โครงสร้างละเอียด (Fine Structure Constant: $lpha = rac{e^2}{4\pi \epsilon_0 \hbar c} pprox rac{1}{137.036}$) เท่านั้น</p>
          <div style="background:rgba(255,255,255,0.85); border:1px solid #e2e8f0; padding:12px 16px; border-radius:6px; margin:12px 0;">
            <strong style="color:#1e3a8a;">การวิเคราะห์และการคำนวณอย่างละเอียด:</strong><br>
            <p style="text-indent:0; margin:6px 0 0 0; line-height:1.85;">จากการคำนวณพลศาสตร์ไฟฟ้าควอนตัม (QED in 2D) การดูดกลืนแสงของกราฟีนชั้นเดี่ยวมีค่าเท่ากับ: $$A = \pi \alpha = \pi \times \frac{1}{137.036} = 0.02292 \approx 2.3\%$$</p>
          </div>
          <div style="background:#f0fdf4; border-left:4px solid #16a34a; padding:10px 14px; margin-top:10px; font-size:9.5pt; color:#166534; border-radius:0 6px 6px 0;">
            💡 <strong>นัยสำคัญทางกายภาพและการประยุกต์ใช้งาน (Physical Insight):</strong><br>
            <span style="color:#14532d;">แสงทะลุผ่านได้ $T = 1 - A = 97.7\%$ ทำให้เราสามารถมองเห็นแผ่นกราฟีนหนาเพียง 1 อะตอมได้ด้วยตาเปล่าบนแผ่นรองรับซิลิคอนออกไซด์</span>
          </div>
        </div>
              </div>
  <div class="code-group">

        <div class="code-box">
          <div class="code-header">💻 แบบจำลองเชิงคำนวณภาษาไพทอน (Computational Python 3.11): กรณีศึกษา: ตัวปรับสัญญาณเชิงแสงความเร็วสูงยิ่งยวด (Graphene Electro-Optic Modulators 100 GHz)</div>
          <pre><code>การใช้วงจรกราฟีนดูดกลืนแสงที่ปรับจูนได้ด้วยไฟฟ้า (Pauli Blocking Effect) ช่วยสร้าง Electro-Optic Modulator ที่มีความเร็วการส่งข้อมูลเกิน 100 Gbit/s สำหรับศูนย์ข้อมูล AI และโครงข่าย 6G ในอนาคต</code></pre>
        </div>
        <p style="font-size:9.5pt; color:#475569; margin-top:-6px; margin-bottom:18px; text-indent:0;"><em>คำอธิบายอัลกอริทึมการจำลอง:</em> สคริปต์ไพทอนสำหรับการคำนวณและจำลองเชิงตัวเลข</p>
              </div>
  <div class="lab-connection-block">
    <h3>🔬 การเชื่อมโยงสู่ห้องปฏิบัติการเสมือนจริงและเทคนิคการทดลอง (Virtual Lab Connection)</h3>
    <div style='background:#f0fdf4; border:1px solid #bbf7d0; border-left:5px solid #16a34a; padding:12px 16px; margin-bottom:14px; border-radius:6px;'><strong style='color:#166534; font-size:10.5pt;'>การจำลองกรวยดิแรคและการกระจายตัวพลังงานของกราฟีน</strong><p style='margin:6px 0 0 0; color:#14532d; text-indent:0; line-height:1.8;'>graphene_dirac_cones.py</p></div>
  </div>
  <div class="cases-block">
    <h3>🌐 กรณีศึกษางานวิจัยแนวหน้าและนวัตกรรมอุตสาหกรรม (Frontier Case Studies)</h3>
    <div style='background:#eff6ff; border:1px solid #bfdbfe; border-left:5px solid #2563eb; padding:12px 16px; margin-bottom:14px; border-radius:6px;'><strong style='color:#1e40af; font-size:10.5pt;'>การเชื่อมโยงกับ Virtual Lab 23: การจำลองกรวยดิแรค กราฟีนฟิสิกส์ และ Klein Tunneling</strong><p style='margin:6px 0 0 0; color:#1e3a8a; text-indent:0; line-height:1.8;'>ผู้เรียนสามารถปรับแรงดันเกต $V_g$ ใน Lab 23 เพื่อเลื่อนระดับเฟอร์มิ $E_F$ ผ่านจุด Dirac Point และทดลองยิงคลื่นอิเล็กตรอนชนกำแพงศักย์เพื่อสังเกตปรากฏการณ์ Klein Tunneling</p></div>
  </div>

      <div class="checkpoint-box" style="background:#fefce8; border:1px solid #fef08a; border-left:5px solid #eab308; padding:14px 18px; margin:24px 0 35px 0; border-radius:6px; page-break-inside:avoid;">
        <strong style="color:#854d0e; font-size:10pt;">🎯 จุดตรวจประเมินความเข้าใจและคำถามทบทวนประจำหัวข้อ 5.3 (Concept Checkpoint)</strong>
        <ul style="margin:8px 0 0 0; padding-left:20px; color:#713f12; font-size:9.5pt; line-height:1.8;">
          <li>จงอธิบายแนวคิดรวบยอดหลักของ กราฟีน: กรวยดิแรค เฟอร์มิออนไร้มวล และอิเล็กทรอนิกส์ 2D และความแตกต่างจากพฤติกรรมในระดับมหภาค</li>
          <li>พารามิเตอร์ใดเป็นปัจจัยวิกฤตที่ควบคุมสมบัติทางฟิสิกส์ในหัวข้อนี้ และมีผลกระทบอย่างไร?</li>
          <li>เชื่อมโยงหลักการฟิสิกส์ในหัวข้อนี้เข้ากับการประยุกต์ใช้จริงในเทคโนโลยีสมัยใหม่</li>
        </ul>
      </div>
    </div>
    
    <div class="topic-section">
      <h2>5.4 โครงสร้างเฮเทอโร 2D แบบฟานเดอร์วาลส์และวัสดุทรานซิชันไดคัลโคจีไนด์</h2>
      <div class="topic-en-title">(van der Waals Heterostructures & Transition Metal Dichalcogenides (TMDs))</div>
      
      <div class="topic-intro">
        <p>การค้นพบวัสดุสองมิติตระกูลอื่นๆ นอกเหนือจากกราฟีน ได้นำไปสู่การปฏิวัติทางวัสดุศาสตร์ยุคใหม่ โดยเฉพาะกลุ่มสารประกอบไดคัลโคจีไนด์ของโลหะทรานซิชัน (Transition Metal Dichalcogenides: TMDs สูตรเคมี $M X_2$ เช่น $	ext{MoS}_2, 	ext{WS}_2, 	ext{MoSe}_2, 	ext{WSe}_2$)</p>
    <p>TMDs มีความพิเศษตรงที่เมื่อลดความหนาจากบัลค์ลงเหลือชั้นเดี่ยว (Monolayer) โครงสร้างแถบพลังงานจะเกิดการเปลี่ยนผ่านจากสารกึ่งตัวนำช่องว่างแถบพลังงานทางอ้อม (Indirect Bandgap) กลายเป็นช่องว่างแถบพลังงานทางตรง (Direct Bandgap) ในย่านแสงขาว ($1.5 - 2.1	ext{ eV}$) ส่งผลให้ประสิทธิภาพควอนตัมในการเปล่งแสงเรือง (Photoluminescence Quantum Yield) พุ่งสูงขึ้นกว่าเดิมหลายหมื่นเท่า</p>
    <p>นอกจากนี้ การนำแผ่นวัสดุ 2D ต่างชนิดกัน เช่น กราฟีน, h-BN (ฉนวน), $	ext{MoS}_2$ (สารกึ่งตัวนำ), และ $	ext{Bi}_2	ext{Sr}_2	ext{CaCu}_2	ext{O}_{8+\delta}$ (ตัวนำยิ่งยวด) มาวางซ้อนทับกันเป็นชั้นๆ โดยอาศัยแรงฟานเดอร์วาลส์โดยไม่มีข้อจำกัดเรื่องการเข้ากันของแลตทิซผลึก (Lattice Mismatch Free) เรียกว่า โครงสร้างเฮเทอโรฟานเดอร์วาลส์ (van der Waals Heterostructures) ซึ่งเปรียบเสมือนการต่อเลโก้ระดับอะตอมเพื่อสร้างอุปกรณ์อิเล็กทรอนิกส์และโฟโทนิกส์ตามสั่ง</p>
  </div>

      <div class="subtopic-block">
        <h3>ฟิสิกส์แวลลีย์ทรอนิกส์ (Valleytronics) และ Spin-Orbit Coupling ใน Monolayer TMDs</h3>
            <p>โครงสร้าง Monolayer TMDs ขาดสมมาตรการกลับจุดศูนย์กลาง (Broken Inversion Symmetry) ประกอบกับอันตรกิริยาสปิน-วงโคจร (Spin-Orbit Coupling) ที่แข็งแกร่งจากอะตอมโลหะหนัก ทำให้เกิดการจับคู่ระหว่างสปินและหุบเขาพลังงาน (Spin-Valley Locking) ที่จุด $K$ และ $K'$</p>
    <p>ทำให้สามารถใช้แสงโพลาไรซ์แบบวงกลมขวา ($\sigma^+$) และวงกลมซ้าย ($\sigma^-$) ในการกระตุ้นและควบคุมสถานะควอนตัมของหุบเขาพลังงานเพื่อประมวลผลข้อมูลในระบบ Valleytronics ได้อย่างสมบูรณ์แบบ</p>
  </div>

      <div class="subtopic-block">
        <h3>โบรอนไนไตรด์หกเหลี่ยม (h-BN) ฉนวนระดับอะตอมที่สมบูรณ์แบบ</h3>
            <p>h-BN เป็นสารสองมิติที่มีช่องว่างแถบพลังงานกว้างมาก ($E_g pprox 5.9	ext{ eV}$) มีพื้นผิวเรียบระดับอะตอมโดยไม่มี Dangling Bonds หรือประจุตกค้าง ทำหน้าที่เป็นแผ่นรองรับและชั้นห่อหุ้ม (Encapsulation Layer) ที่ช่วยรักษาสภาพคล่องตัวของกราฟีนและ TMDs ให้สูงถึงขีดจำกัดทางทฤษฎี</p>
  </div>
  <div class="formula-group">

        <div class="equation-box">
          <div class="equation-header">📌 สมการฟิสิกส์หลัก: การเปลี่ยนผ่านแถบพลังงานใน MoS2</div>
          <div class="formula-math">$$E_g^{\text{bulk}} = 1.29\text{ eV (Indirect)} \xrightarrow{\text{Monolayer}} E_g^{\text{1L}} = 1.90\text{ eV (Direct at } K\text{ point)}$$</div>
          <p style="font-size:9.5pt; margin:4px 0 0 0; color:#334155; line-height:1.75; text-indent:0;"><strong>คำอธิบายตัวแปรและนัยสำคัญ:</strong> การเปลี่ยนผ่านเป็น Direct Bandgap ในชั้นเดี่ยว</p>
        </div>
            
        <div class="equation-box">
          <div class="equation-header">📌 สมการฟิสิกส์หลัก: พลังงานยึดเหนี่ยวของเอ็กซิตอนในวัสดุ 2D</div>
          <div class="formula-math">$$E_b^{\text{exciton}} \approx \frac{\mu e^4}{2 \hbar^2 \epsilon_{\text{eff}}^2} \approx 0.3 - 0.5\text{ eV}$$</div>
          <p style="font-size:9.5pt; margin:4px 0 0 0; color:#334155; line-height:1.75; text-indent:0;"><strong>คำอธิบายตัวแปรและนัยสำคัญ:</strong> พลังงานยึดเหนี่ยวเอ็กซิตอนสูงมากเนื่องจากการลดทอน Dielectric Screening</p>
        </div>
              </div>

      <div class="table-block">
        <h3>📊 ตารางเปรียบเทียบสมบัติของวัสดุ 2D สำคัญ</h3>
        <table class="data-table">
          <thead><tr>
            <th>วัสดุ 2D</th><th>ชนิดวัสดุ</th><th>ช่องว่างแถบพลังงาน (1L)</th><th>ความยาวคลื่น PL</th><th>การประยุกต์ใช้งานเด่น</th></tr></thead>
<tbody><tr><td>Graphene</td><td>Semi-metal (Zero Gap)</td><td>0 eV</td><td>-</td><td>ขั้วไฟฟ้าโปร่งแสง, ทรานซิสเตอร์ความถี่สูง</td></tr><tr><td>h-BN</td><td>Insulator (Wide Gap)</td><td>5.9 eV</td><td>210 nm (Deep UV)</td><td>ชั้นฉนวนเกต, แผ่นรองรับความเรียบอะตอม</td></tr><tr><td>MoS2</td><td>Semiconductor (Direct)</td><td>1.90 eV</td><td>653 nm (แดง)</td><td>2D FETs, ไบโอเซนเซอร์, โฟโตดีเทกเตอร์</td></tr><tr><td>WS2</td><td>Semiconductor (Direct)</td><td>2.05 eV</td><td>605 nm (ส้ม)</td><td>Valleytronics, เลเซอร์ 2D, โฟโตแคทาลิซิส</td></tr><tr><td>Black Phosphorus (BP)</td><td>Semiconductor (Direct)</td><td>0.3 - 2.0 eV (Tunable)</td><td>อินฟราเรดคลื่นสั้น (IR)</td><td>โฟโตนิกส์ย่านอินฟราเรด, เทอร์โมอิเล็กทริก</td></tr></tbody></table>
</div>
  <div class="examples-group">

        <div class="example-box">
          <div class="example-header">
            <span>📝 ตัวอย่างการคำนวณที่ 5.7: การคำนวณความยาวคลื่นแสงเรือง Photoluminescence ของ Monolayer WS2</span>
            <span style="background:#dcfce7; color:#15803d; font-size:8.5pt; padding:3px 10px; border-radius:4px; font-weight:700;">Step-by-Step Worked Solution</span>
          </div>
          <p style="text-indent:0; margin-bottom:10px;"><strong>โจทย์ปัญหา (Problem Statement):</strong><br>แผ่น $	ext{WS}_2$ ชั้นเดี่ยวมีช่องว่างแถบพลังงานทางตรง $E_g = 2.05	ext{ eV}$ และมีพลังงานยึดเหนี่ยวเอ็กซิตอน $E_b = 0.32	ext{ eV}$ จงคำนวณหาพลังงานของโฟตอนเอ็กซิตอน $E_{	ext{photon}}$ และความยาวคลื่นแสงที่เปล่งออกมา $\lambda_{	ext{PL}}$</p>
          <div style="background:rgba(255,255,255,0.85); border:1px solid #e2e8f0; padding:12px 16px; border-radius:6px; margin:12px 0;">
            <strong style="color:#1e3a8a;">การวิเคราะห์และการคำนวณอย่างละเอียด:</strong><br>
            <p style="text-indent:0; margin:6px 0 0 0; line-height:1.85;">1. พลังงานการเปล่งแสงของเอ็กซิตอนอิสระ: $E_{\text{photon}} = E_g - E_b = 2.05\text{ eV} - 0.32\text{ eV} = 1.73\text{ eV}$<br>2. $\lambda_{\text{PL}} = \frac{h c}{E_{\text{photon}}} = \frac{1240\text{ eV}\cdot\text{nm}}{1.73\text{ eV}} = 716.8\text{ nm}$</p>
          </div>
          <div style="background:#f0fdf4; border-left:4px solid #16a34a; padding:10px 14px; margin-top:10px; font-size:9.5pt; color:#166534; border-radius:0 6px 6px 0;">
            💡 <strong>นัยสำคัญทางกายภาพและการประยุกต์ใช้งาน (Physical Insight):</strong><br>
            <span style="color:#14532d;">แสงเรืองอยู่ในย่านสีแดงเข้ม (Deep Red) และมีความเข้มสว่างสูงมากเนื่องจากเป็นรอยต่อแถบพลังงานทางตรง</span>
          </div>
        </div>
            
        <div class="example-box">
          <div class="example-header">
            <span>📝 ตัวอย่างการคำนวณที่ 5.8: การคำนวณอัตราส่วนเปิด-ปิดกระแส (Ion/Ioff Ratio) ใน MoS2 FET</span>
            <span style="background:#dcfce7; color:#15803d; font-size:8.5pt; padding:3px 10px; border-radius:4px; font-weight:700;">Step-by-Step Worked Solution</span>
          </div>
          <p style="text-indent:0; margin-bottom:10px;"><strong>โจทย์ปัญหา (Problem Statement):</strong><br>ทรานซิสเตอร์ $	ext{MoS}_2$ ชั้นเดี่ยวมีช่องว่างแถบพลังงาน $1.90	ext{ eV}$ เมื่อทำงานที่ $300	ext{ K}$ วัดกระแสเปิดได้ $I_{	ext{on}} = 50	ext{ }\mu	ext{A}$ และกระแสรั่วไหลขณะปิด $I_{	ext{off}} = 0.5	ext{ pA}$ จงคำนวณอัตราส่วน $I_{	ext{on}}/I_{	ext{off}}$</p>
          <div style="background:rgba(255,255,255,0.85); border:1px solid #e2e8f0; padding:12px 16px; border-radius:6px; margin:12px 0;">
            <strong style="color:#1e3a8a;">การวิเคราะห์และการคำนวณอย่างละเอียด:</strong><br>
            <p style="text-indent:0; margin:6px 0 0 0; line-height:1.85;">$$\frac{I_{\text{on}}}{I_{\text{off}}} = \frac{50 \times 10^{-6}\text{ A}}{0.5 \times 10^{-12}\text{ A}} = 1.0 \times 10^8 = 10^8$$</p>
          </div>
          <div style="background:#f0fdf4; border-left:4px solid #16a34a; padding:10px 14px; margin-top:10px; font-size:9.5pt; color:#166534; border-radius:0 6px 6px 0;">
            💡 <strong>นัยสำคัญทางกายภาพและการประยุกต์ใช้งาน (Physical Insight):</strong><br>
            <span style="color:#14532d;">อัตราส่วน $I_{	ext{on}}/I_{	ext{off}}$ สูงถึง $10^8$ ซึ่งเหนือกว่ากราฟีน FET (ซึ่งมีอัตราส่วนเพียง $\sim 10$ เนื่องจากไม่มีช่องว่างแถบพลังงาน) ทำให้ $	ext{MoS}_2$ เป็นวัสดุอุดมคติสำหรับวงจรตรรกะดิจิทัล</span>
          </div>
        </div>
              </div>
  <div class="code-group">

        <div class="code-box">
          <div class="code-header">💻 แบบจำลองเชิงคำนวณภาษาไพทอน (Computational Python 3.11): กรณีศึกษา: ทรานซิสเตอร์ 2D ขนาดเกต 1 นาโนเมตร (1-nm Gate MoS2 FET) โดย Lawrence Berkeley National Lab</div>
          <pre><code>การใช้ท่อคาร์บอนนาโนเดี่ยวขนาดเส้นผ่านศูนย์กลาง 1 nm ทำหน้าที่เป็นขั้วเกตควบคุมช่องนำกระแสแผ่น $	ext{MoS}_2$ ชั้นเดี่ยว ช่วยสร้างทรานซิสเตอร์ที่มีขนาดสั้นที่สุดในโลกโดยไม่เกิดปัญหาการรั่วไหลจาก Short-Channel Effects</code></pre>
        </div>
        <p style="font-size:9.5pt; color:#475569; margin-top:-6px; margin-bottom:18px; text-indent:0;"><em>คำอธิบายอัลกอริทึมการจำลอง:</em> สคริปต์ไพทอนสำหรับการคำนวณและจำลองเชิงตัวเลข</p>
              </div>
  <div class="lab-connection-block">
    <h3>🔬 การเชื่อมโยงสู่ห้องปฏิบัติการเสมือนจริงและเทคนิคการทดลอง (Virtual Lab Connection)</h3>
    <div style='background:#f0fdf4; border:1px solid #bbf7d0; border-left:5px solid #16a34a; padding:12px 16px; margin-bottom:14px; border-radius:6px;'><strong style='color:#166534; font-size:10.5pt;'>การจำลองสเปกตรัมการเปล่งแสง PL ของ Monolayer TMDs</strong><p style='margin:6px 0 0 0; color:#14532d; text-indent:0; line-height:1.8;'>tmd_photoluminescence.py</p></div>
  </div>
  <div class="cases-block">
    <h3>🌐 กรณีศึกษางานวิจัยแนวหน้าและนวัตกรรมอุตสาหกรรม (Frontier Case Studies)</h3>
    <div style='background:#eff6ff; border:1px solid #bfdbfe; border-left:5px solid #2563eb; padding:12px 16px; margin-bottom:14px; border-radius:6px;'><strong style='color:#1e40af; font-size:10.5pt;'>การเชื่อมโยงกับ Virtual Lab 24: การจำลองโครงสร้างเฮเทอโร 2D แบบฟานเดอร์วาลส์และแวลลีย์ทรอนิกส์</strong><p style='margin:6px 0 0 0; color:#1e3a8a; text-indent:0; line-height:1.8;'>ผู้เรียนสามารถต่อประกอบชั้นวัสดุ 2D ใน Lab 24 เช่น Graphene/h-BN/MoS2 สังเกตการจัดเรียงแถบพลังงาน Band Alignment และจำลองการควบคุมสปิน-แวลลีย์ด้วยแสงโพลาไรซ์</p></div>
  </div>

      <div class="checkpoint-box" style="background:#fefce8; border:1px solid #fef08a; border-left:5px solid #eab308; padding:14px 18px; margin:24px 0 35px 0; border-radius:6px; page-break-inside:avoid;">
        <strong style="color:#854d0e; font-size:10pt;">🎯 จุดตรวจประเมินความเข้าใจและคำถามทบทวนประจำหัวข้อ 5.4 (Concept Checkpoint)</strong>
        <ul style="margin:8px 0 0 0; padding-left:20px; color:#713f12; font-size:9.5pt; line-height:1.8;">
          <li>จงอธิบายแนวคิดรวบยอดหลักของ โครงสร้างเฮเทอโร 2D แบบฟานเดอร์วาลส์และวัสดุทรานซิชันไดคัลโคจีไนด์ และความแตกต่างจากพฤติกรรมในระดับมหภาค</li>
          <li>พารามิเตอร์ใดเป็นปัจจัยวิกฤตที่ควบคุมสมบัติทางฟิสิกส์ในหัวข้อนี้ และมีผลกระทบอย่างไร?</li>
          <li>เชื่อมโยงหลักการฟิสิกส์ในหัวข้อนี้เข้ากับการประยุกต์ใช้จริงในเทคโนโลยีสมัยใหม่</li>
        </ul>
      </div>
    </div>
    
    <div class="topic-section">
      <h2>5.5 ฟิสิกส์ทวิสต์ทรอนิกส์และมุมมหัศจรรย์ในกราฟีนสองชั้น</h2>
      <div class="topic-en-title">(Twistronics, Moiré Superlattices & Magic-Angle Twisted Bilayer Graphene)</div>
      
      <div class="topic-intro">
        <p>ทวิสต์ทรอนิกส์ (Twistronics) เป็นสาขาฟิสิกส์แนวหน้าแห่งศตวรรษที่ 21 ที่ศึกษาการปรับแต่งสมบัติทางอิเล็กทรอนิกส์ แสง และควอนตัมของวัสดุสองมิติผ่านการบิดมุมสัมพัทธ์ระหว่างชั้นผลึก (Twist Angle: $	heta$) ซึ่งนำไปสู่การเกิดลวดลายมัวเร (Moiré Superlattice) ที่มีคาบความยาวในระดับหลายสิบนาโนเมตร</p>
    <p>การค้นพบครั้งประวัติศาสตร์ในปี 2018 โดย พาโบล จาริลโล-เฮอร์เรโร และคณะ ณ สถาบันเทคโนโลยีแมสซาชูเซตส์ (MIT) พบว่าเมื่อนำแผ่นกราฟีนสองชั้นมาซ้อนทับกันแล้วบิดมุมทำมุมที่แม่นยำอย่างยิ่งที่ 'มุมมหัศจรรย์' (Magic Angle: $	heta_m pprox 1.1^\circ$) โครงสร้างแถบพลังงานจะแบนราบลงอย่างสมบูรณ์ เกิดเป็นแถบพลังงานแบนราบ (Flat Bands) ที่มีค่าความเร็วเฟอร์มิ $v_F 	o 0$</p>
    <p>ในสภาวะ Flat Bands นี้ พลังงานจลน์ของอิเล็กตรอนจะลดลงจนอันตรกิริยาผลักกันของคูลอมบ์ระหว่างอิเล็กตรอนกลายเป็นแรงหลักที่ควบคุมพฤติกรรมของระบบ นำไปสู่การค้นพบ สภาพนำยิ่งยวดแบบไร้แรงต้านทาน (Unconventional Superconductivity ที่อุณหภูมิวิกฤต $T_c pprox 1.7	ext{ K}$) และสถานะฉนวนมอตต์ที่เหนี่ยวนำด้วยสหสัมพันธ์ (Correlated Mott-like Insulator) ซึ่งสามารถสลับเปลี่ยนสถานะกันได้ง่ายดายเพียงแค่ปรับแรงดันไฟฟ้าที่ขั้วเกต</p>
  </div>

      <div class="figure-card">
        <img src="../assets/images/graphene_twistronics_moire_3d.jpg" alt="ภาพเสมือนจริง 3 มิติ: โครงสร้างซูเปอร์แลตทิซมัวเรในกราฟีนสองชั้นบิดมุมมหัศจรรย์ 1.1 องศา และการเกิดแถบพลังงานแบนราบนำสู่สภาพตัวนำยิ่งยวด">
        <div class="caption"><strong>ภาพที่ 5.5.1</strong>: ภาพเสมือนจริง 3 มิติ: โครงสร้างซูเปอร์แลตทิซมัวเรในกราฟีนสองชั้นบิดมุมมหัศจรรย์ 1.1 องศา และการเกิดแถบพลังงานแบนราบนำสู่สภาพตัวนำยิ่งยวด</div>
      </div>
            
      <div class="subtopic-block">
        <h3>เรขาคณิตของลวดลายมัวเรและมุมมหัศจรรย์ตามแบบจำลอง Bistritzer-MacDonald</h3>
            <p>คาบความยาวของลวดลายมัวเร: $\lambda_M = rac{a}{2 \sin(	heta/2)} pprox rac{a}{	heta}$ เมื่อ $	heta = 1.1^\circ$ จะได้ $\lambda_M pprox 13.4	ext{ nm}$</p>
    <p>แบบจำลองความต่อเนื่องของ Bistritzer-MacDonald ทำนายว่าพลังงานการคัปปลิ้งระหว่างชั้น $w$ จะชดเชยกับพลังงานจลน์ของดิแรคที่มุม $	heta_m pprox rac{\sqrt{3} w}{v_F k_D} pprox 1.08^\circ$ ส่งผลให้ความกว้างของแถบพลังงานแคบลงเหลือเพียง $\Delta E < 5	ext{ meV}$</p>
  </div>

      <div class="subtopic-block">
        <h3>ความคล้ายคลึงกับตัวนำยิ่งยวดอุณหภูมิสูงกลุ่มคิวเปรต (Cuprates)</h3>
            <p>เฟสไดอะแกรมของ Magic-Angle Twisted Bilayer Graphene (MATBG) มีความคล้ายคลึงอย่างน่าทึ่งกับเฟสไดอะแกรมของตัวนำยิ่งยวด High-Tc Cuprates โดยมีโดมสภาพนำยิ่งยวดขนาบข้างสถานะฉนวนมอตต์ ทำให้นักฟิสิกส์ใช้ MATBG เป็นระบบจำลองควอนตัม (Quantum Simulator) เพื่อไขปริศนาฟิสิกส์สภาพนำยิ่งยวดอุณหภูมิสูงที่ค้างคามากว่า 30 ปี</p>
  </div>
  <div class="formula-group">

        <div class="equation-box">
          <div class="equation-header">📌 สมการฟิสิกส์หลัก: คาบความยาวของ Moiré Superlattice</div>
          <div class="formula-math">$$\lambda_M = \frac{a}{2 \sin(\theta/2)} \approx \frac{a}{\theta \text{ (rad)}}, \qquad \lambda_M(1.1^\circ) \approx 13.4\text{ nm}$$</div>
          <p style="font-size:9.5pt; margin:4px 0 0 0; color:#334155; line-height:1.75; text-indent:0;"><strong>คำอธิบายตัวแปรและนัยสำคัญ:</strong> ขนาดของ Moiré Unit Cell ที่มุมมหัศจรรย์</p>
        </div>
            
        <div class="equation-box">
          <div class="equation-header">📌 สมการฟิสิกส์หลัก: เงื่อนไขมุมมหัศจรรย์อันดับแรก (Bistritzer-MacDonald Formula)</div>
          <div class="formula-math">$$\theta_m \approx \frac{\alpha_0 w_1}{\hbar v_F k_D} \approx 1.08^\circ \approx 1.1^\circ, \qquad v_F^* \to 0$$</div>
          <p style="font-size:9.5pt; margin:4px 0 0 0; color:#334155; line-height:1.75; text-indent:0;"><strong>คำอธิบายตัวแปรและนัยสำคัญ:</strong> ความเร็วเฟอร์มิยังผลลดลงเป็นศูนย์ที่มุมมหัศจรรย์</p>
        </div>
              </div>

      <div class="table-block">
        <h3>📊 ตารางวิวัฒนาการของคาบมัวเรและสมบัติทางฟิสิกส์ตามมุมบิด Twist Angle</h3>
        <table class="data-table">
          <thead><tr>
            <th>Twist Angle θ</th><th>คาบมัวเร λM</th><th>ความกว้างแถบพลังงาน</th><th>สถานะควอนตัมที่พบ</th></tr></thead>
<tbody><tr><td>0.0° (Bernal AB)</td><td>ไม่มีมัวเร</td><td>กว้าง (~ 1 eV)</td><td>สารกึ่งโลหะ 2D ดั้งเดิม</td></tr><tr><td>3.0°</td><td>4.7 nm</td><td>ปานกลาง (~ 150 meV)</td><td>Fermi velocity ลดลงเล็กน้อย</td></tr><tr><td>1.1° (Magic Angle)</td><td>13.4 nm</td><td>แบนราบสมบูรณ์ (< 5 meV)</td><td>Mott Insulator, Superconductivity, Magnetism</td></tr><tr><td>0.5°</td><td>28.2 nm</td><td>เกิด Lattice Reconstruction</td><td>โดเมนแยกส่วน AB/BA สลับกัน</td></tr><tr><td>0.1°</td><td>141.0 nm</td><td>เครือข่ายความเค้นโทโพโลยี</td><td>เครือข่ายท่อลำเลียง 1D Edge Channels</td></tr></tbody></table>
</div>
  <div class="examples-group">

        <div class="example-box">
          <div class="example-header">
            <span>📝 ตัวอย่างการคำนวณที่ 5.9: การคำนวณคาบความยาวของ Moiré Superlattice ใน MATBG</span>
            <span style="background:#dcfce7; color:#15803d; font-size:8.5pt; padding:3px 10px; border-radius:4px; font-weight:700;">Step-by-Step Worked Solution</span>
          </div>
          <p style="text-indent:0; margin-bottom:10px;"><strong>โจทย์ปัญหา (Problem Statement):</strong><br>แผ่นกราฟีนสองชั้นถูกวางซ้อนกันโดยมีมุมบิด $	heta = 1.08^\circ$ กำหนดค่าคงที่แลตทิซกราฟีน $a = 0.246	ext{ nm}$ จงคำนวณหา (ก) คาบความยาวมัวเร $\lambda_M$ (ข) พื้นที่ของ Moiré Unit Cell $A_M$ (ค) ความหนาแน่นของอิเล็กตรอน $n_s$ ที่ต้องใช้ในการเติมเต็ม 1 อิเล็กตรอนต่อ Moiré Unit Cell</p>
          <div style="background:rgba(255,255,255,0.85); border:1px solid #e2e8f0; padding:12px 16px; border-radius:6px; margin:12px 0;">
            <strong style="color:#1e3a8a;">การวิเคราะห์และการคำนวณอย่างละเอียด:</strong><br>
            <p style="text-indent:0; margin:6px 0 0 0; line-height:1.85;">1. แปลงมุมเป็นเรเดียน: $\theta = 1.08 \times \frac{\pi}{180} = 0.01885\text{ rad}$<br>2. $\lambda_M = \frac{a}{2 \sin(\theta/2)} \approx \frac{a}{\theta} = \frac{0.246\text{ nm}}{0.01885} = 13.05\text{ nm}$<br>3. พื้นที่ Moiré รังผึ้งหกเหลี่ยม: $A_M = \frac{\sqrt{3}}{2} \lambda_M^2 = \frac{\sqrt{3}}{2} (13.05 \times 10^{-7}\text{ cm})^2 = 1.475 \times 10^{-12}\text{ cm}^2$<br>4. ความหนาแน่นต่อ 1 อิเล็กตรอน: $n_s = \frac{1}{A_M} = \frac{1}{1.475 \times 10^{-12}} = 6.78 \times 10^{11}\text{ cm}^{-2}$</p>
          </div>
          <div style="background:#f0fdf4; border-left:4px solid #16a34a; padding:10px 14px; margin-top:10px; font-size:9.5pt; color:#166534; border-radius:0 6px 6px 0;">
            💡 <strong>นัยสำคัญทางกายภาพและการประยุกต์ใช้งาน (Physical Insight):</strong><br>
            <span style="color:#14532d;">การเติมเต็ม 4 อิเล็กตรอน (สปิน 2 × แวลลีย์ 2) ต้องใช้ความเข้มข้นประจุ $n = 4 n_s = 2.71 	imes 10^{12}	ext{ cm}^{-2}$ ซึ่งสามารถควบคุมได้อย่างง่ายดายด้วยเกตไฟฟ้า</span>
          </div>
        </div>
            
        <div class="example-box">
          <div class="example-header">
            <span>📝 ตัวอย่างการคำนวณที่ 5.1: การคำนวณอัตราส่วนพลังงานศักย์คูลอมบ์ต่อพลังงานจลน์ใน Flat Band</span>
            <span style="background:#dcfce7; color:#15803d; font-size:8.5pt; padding:3px 10px; border-radius:4px; font-weight:700;">Step-by-Step Worked Solution</span>
          </div>
          <p style="text-indent:0; margin-bottom:10px;"><strong>โจทย์ปัญหา (Problem Statement):</strong><br>ใน MATBG ที่มุมมหัศจรรย์ พลังงานจลน์ลดลงเหลือความกว้างแถบ $W = 4.0	ext{ meV}$ ระยะห่างเฉลี่ยระหว่างอิเล็กตรอนเท่ากับคาบมัวเร $r pprox \lambda_M = 13.0	ext{ nm}$ กำหนด $\epsilon_r = 5.0$ (ห่อหุ้มด้วย h-BN) จงคำนวณหาพลังงานคูลอมบ์ $U$ และอัตราส่วน $U/W$</p>
          <div style="background:rgba(255,255,255,0.85); border:1px solid #e2e8f0; padding:12px 16px; border-radius:6px; margin:12px 0;">
            <strong style="color:#1e3a8a;">การวิเคราะห์และการคำนวณอย่างละเอียด:</strong><br>
            <p style="text-indent:0; margin:6px 0 0 0; line-height:1.85;">1. $U = \frac{e^2}{4\pi \epsilon_0 \epsilon_r r} = \frac{(1.602 \times 10^{-19})^2}{4\pi (8.854 \times 10^{-12})(5.0)(13.0 \times 10^{-9})} = 3.55 \times 10^{-21}\text{ J} = 22.16\text{ meV}$<br>2. อัตราส่วน $\frac{U}{W} = \frac{22.16\text{ meV}}{4.0\text{ meV}} = 5.54$</p>
          </div>
          <div style="background:#f0fdf4; border-left:4px solid #16a34a; padding:10px 14px; margin-top:10px; font-size:9.5pt; color:#166534; border-radius:0 6px 6px 0;">
            💡 <strong>นัยสำคัญทางกายภาพและการประยุกต์ใช้งาน (Physical Insight):</strong><br>
            <span style="color:#14532d;">เนื่องจาก $U/W = 5.54 > 1$ ระบบจึงเข้าสู่สภาวะ Strongly Correlated Electron System อย่างสมบูรณ์ ทำให้เกิดสถานะตัวนำยิ่งยวดและฉนวนมอตต์</span>
          </div>
        </div>
              </div>
  <div class="code-group">

        <div class="code-box">
          <div class="code-header">💻 แบบจำลองเชิงคำนวณภาษาไพทอน (Computational Python 3.11): กรณีศึกษา: การสร้างตัวนำยิ่งยวดและฉนวนมอตต์ที่ควบคุมได้ด้วยสวิตช์ไฟฟ้า (Gate-Tunable Superconductors)</div>
          <pre><code>การใช้อุปกรณ์ MATBG ช่วยให้นักวิทยาศาสตร์สามารถเปิด-ปิดสวิตช์สภาพนำยิ่งยวดและเปลี่ยนสถานะเป็นฉนวนได้ทันทีด้วยการปรับแรงดันเกตเพียงไม่กี่โวลต์ ซึ่งนำไปสู่การพัฒนาทรานซิสเตอร์ตัวนำยิ่งยวดความเร็วสูงพิเศษสำหรับควอนตัมคอมพิวเตอร์</code></pre>
        </div>
        <p style="font-size:9.5pt; color:#475569; margin-top:-6px; margin-bottom:18px; text-indent:0;"><em>คำอธิบายอัลกอริทึมการจำลอง:</em> สคริปต์ไพทอนสำหรับการคำนวณและจำลองเชิงตัวเลข</p>
              </div>
  <div class="lab-connection-block">
    <h3>🔬 การเชื่อมโยงสู่ห้องปฏิบัติการเสมือนจริงและเทคนิคการทดลอง (Virtual Lab Connection)</h3>
    <div style='background:#f0fdf4; border:1px solid #bbf7d0; border-left:5px solid #16a34a; padding:12px 16px; margin-bottom:14px; border-radius:6px;'><strong style='color:#166534; font-size:10.5pt;'>การจำลองลวดลาย Moiré Superlattice และ Flat Bands ใน Twistronics</strong><p style='margin:6px 0 0 0; color:#14532d; text-indent:0; line-height:1.8;'>moire_superlattice_sim.py</p></div>
  </div>
  <div class="cases-block">
    <h3>🌐 กรณีศึกษางานวิจัยแนวหน้าและนวัตกรรมอุตสาหกรรม (Frontier Case Studies)</h3>
    <div style='background:#eff6ff; border:1px solid #bfdbfe; border-left:5px solid #2563eb; padding:12px 16px; margin-bottom:14px; border-radius:6px;'><strong style='color:#1e40af; font-size:10.5pt;'>การเชื่อมโยงกับ Virtual Lab 25: การจำลองทวิสต์ทรอนิกส์ ลวดลายมัวเร และมุมมหัศจรรย์ในกราฟีนสองชั้น</strong><p style='margin:6px 0 0 0; color:#1e3a8a; text-indent:0; line-height:1.8;'>ผู้เรียนสามารถปรับมุมบิด Twist Angle $	heta$ แบบละเอียดทศนิยมสองตำแหน่งใน Lab 25 สังเกตการขยายใหญ่ของลวดลายมัวเร และวัดการแบนราบของแถบพลังงาน Flat Bands</p></div>
  </div>

      <div class="checkpoint-box" style="background:#fefce8; border:1px solid #fef08a; border-left:5px solid #eab308; padding:14px 18px; margin:24px 0 35px 0; border-radius:6px; page-break-inside:avoid;">
        <strong style="color:#854d0e; font-size:10pt;">🎯 จุดตรวจประเมินความเข้าใจและคำถามทบทวนประจำหัวข้อ 5.5 (Concept Checkpoint)</strong>
        <ul style="margin:8px 0 0 0; padding-left:20px; color:#713f12; font-size:9.5pt; line-height:1.8;">
          <li>จงอธิบายแนวคิดรวบยอดหลักของ ฟิสิกส์ทวิสต์ทรอนิกส์และมุมมหัศจรรย์ในกราฟีนสองชั้น และความแตกต่างจากพฤติกรรมในระดับมหภาค</li>
          <li>พารามิเตอร์ใดเป็นปัจจัยวิกฤตที่ควบคุมสมบัติทางฟิสิกส์ในหัวข้อนี้ และมีผลกระทบอย่างไร?</li>
          <li>เชื่อมโยงหลักการฟิสิกส์ในหัวข้อนี้เข้ากับการประยุกต์ใช้จริงในเทคโนโลยีสมัยใหม่</li>
        </ul>
      </div>
    </div>
    

      <div class="summary-box">
        <h3 style="color:#1e40af; margin-top:0; font-size:13pt;">📋 สรุปสาระสำคัญประจำบทที่ 5 (Chapter 5 Key Takeaways)</h3>
        <ul style="margin:0; padding-left:22px; font-size:10pt; line-height:1.95; color:#1e293b;">
          <li style='margin-bottom:8px;'>ฟุลเลอรีน C60 มีโครงสร้างทรงกลมกรงคาร์บอนสมมาตร Ih ประกอบด้วย 12 วงห้าเหลี่ยมและ 20 วงหกเหลี่ยม ทำหน้าที่เป็นตัวรับอิเล็กตรอนชั้นยอดในเซลล์แสงอาทิตย์ OPV</li><li style='margin-bottom:8px;'>ท่อคาร์บอนนาโน (CNTs) มีสมบัติทางไฟฟ้าเป็นโลหะหรือสารกึ่งตัวนำตามเวกเตอร์ไครัลลิตี้ $(n, m)$ และมีความแข็งแรงเชิงกลสูงลิ่ว $Y pprox 1	ext{ TPa}$</li><li style='margin-bottom:8px;'>กราฟีนมีกรวยดิแรคและพฤติกรรมดิแรคเฟอร์มิออนไร้มวล $E = \hbar v_F k$ ทำให้เกิด Klein Tunneling และสภาพคล่องตัวสูงเกิน $200,000	ext{ cm}^2/	ext{V}\cdot	ext{s}$</li><li style='margin-bottom:8px;'>วัสดุ 2D TMDs (MoS2, WS2) เปลี่ยนผ่านเป็น Direct Bandgap เมื่อเป็นชั้นเดี่ยว และมีฟิสิกส์ Spin-Valley Locking สำหรับระบบ Valleytronics</li><li style='margin-bottom:8px;'>ทวิสต์ทรอนิกส์ในกราฟีนสองชั้นมุมมหัศจรรย์ ($	heta pprox 1.1^\circ$) ทำให้เกิด Moiré Flat Bands นำไปสู่สภาพนำยิ่งยวดและฉนวนมอตต์ที่ควบคุมได้ด้วยไฟฟ้า</li>
        </ul>
      </div>

      <div class="problems-section">
        <h3 style="color:#0f172a; margin-top:0; font-size:14pt; border-bottom:2px solid #cbd5e1; padding-bottom:8px;">
          📚 แบบฝึกหัดและโจทย์ปัญหาท้ายบทที่ 5 (End-of-Chapter Problems)
        </h3>
        
        <h4 style="color:#1e3a8a; font-size:11.5pt; margin-top:18px;">ตอนที่ 1: คำถามเชิงมโนทัศน์และการวิเคราะห์เชิงฟิสิกส์ (Conceptual & Analytical Questions)</h4>
        <ol style="padding-left:22px; font-size:10pt; line-height:1.9; color:#334155;">
          <li style='margin-bottom:8px;'>จงอธิบายกฎ Isolated Pentagon Rule (IPR) ในฟุลเลอรีน และเหตุใด C60 จึงเป็นฟุลเลอรีนขนาดเล็กที่สุดที่เสถียร</li><li style='margin-bottom:8px;'>เพราะเหตุใดท่อคาร์บอนนาโนแบบ Armchair $(n, n)$ จึงเป็นโลหะนำไฟฟ้าเสมอในขณะที่ท่อ Zigzag $(n, 0)$ มีทั้งแบบโลหะและกึ่งตัวนำ?</li><li style='margin-bottom:8px;'>จงอธิบายความหมายทางฟิสิกส์ของ Dirac Cones ในกราฟีน และเหตุใดอิเล็กตรอนจึงประพฤติตัวเสมือนไร้มวล</li><li style='margin-bottom:8px;'>ปรากฏการณ์ Klein Tunneling คืออะไร และเกิดจากความสมมาตรแบบใดของฟังก์ชันคลื่นในกราฟีน?</li><li style='margin-bottom:8px;'>ทำไม MoS2 เมื่อลดความหนาเหลือ 1 ชั้น จึงเปลี่ยนจาก Indirect Bandgap กลายเป็น Direct Bandgap?</li><li style='margin-bottom:8px;'>จงอธิบายความหมายของ Spin-Valley Locking ใน Monolayer TMDs และการประยุกต์ใช้ใน Valleytronics</li><li style='margin-bottom:8px;'>Moiré Superlattice คืออะไร และเกิดขึ้นได้อย่างไรในการซ้อนทับวัสดุ 2D?</li><li style='margin-bottom:8px;'>เพราะเหตุใดที่มุมมหัศจรรย์ $	heta pprox 1.1^\circ$ ในกราฟีนสองชั้นจึงเกิดสภาพนำยิ่งยวด (Superconductivity)?</li>
        </ol>

        <h4 style="color:#166534; font-size:11.5pt; margin-top:22px;">ตอนที่ 2: โจทย์ปัญหาการคำนวณเชิงตัวเลขและการพิสูจน์ (Quantitative & Numerical Problems)</h4>
        <ol style="padding-left:22px; font-size:10pt; line-height:1.9; color:#334155;">
          <li style='margin-bottom:8px;'>คำนวณจำนวนพันธะและจำนวนวงหกเหลี่ยมในโมเลกุลฟุลเลอรีน $	ext{C}_{84}$ ตามกฎทรงหลายหน้าของออยเลอร์</li><li style='margin-bottom:8px;'>ท่อคาร์บอนนาโนมีดัชนี $(12, 6)$ จงคำนวณหาเส้นผ่านศูนย์กลาง $d_t$, มุมไครัล $	heta$ และช่องว่างแถบพลังงาน $E_g$</li><li style='margin-bottom:8px;'>จงคำนวณความเข้มข้นพาหะ $n$ และความยาวคลื่นเฟอร์มิ $\lambda_F$ ในกราฟีนเมื่อระดับเฟอร์มิ $E_F = 0.25	ext{ eV}$</li><li style='margin-bottom:8px;'>คำนวณพลังงานของโฟตอนและความถี่แสงที่เปล่งจาก Monolayer $	ext{MoS}_2$ ($E_g = 1.90	ext{ eV}$, $E_b = 0.30	ext{ eV}$)</li><li style='margin-bottom:8px;'>จงคำนวณคาบความยาวมัวเร $\lambda_M$ และพื้นที่ยูนิตเซลล์ $A_M$ ของกราฟีนสองชั้นที่มุมบิด $	heta = 1.05^\circ$</li><li style='margin-bottom:8px;'>คำนวณหาความหนาแน่นผลึกของ Fullerite $	ext{C}_{70}$ ในโครงสร้าง FCC ที่มีค่าคงที่แลตทิซ $a = 1.50	ext{ nm}$</li><li style='margin-bottom:8px;'>ทรานซิสเตอร์ $	ext{WS}_2$ มีค่าสภาพคล่องตัว $\mu = 100	ext{ cm}^2/	ext{V}\cdot	ext{s}$ ความยาวแชนแนล $L = 100	ext{ nm}$ จงคำนวณเวลาการเดินทางของอิเล็กตรอนเมื่อ $V_{ds} = 1.0	ext{ V}$</li>
        </ol>

        <h4 style="color:#7c2d12; font-size:11.5pt; margin-top:22px;">ตอนที่ 3: โจทย์ประยุกต์ การออกแบบเชิงวิศวกรรม และการจำลอง (Applied Design & Modeling Problems)</h4>
        <ol style="padding-left:22px; font-size:10pt; line-height:1.9; color:#334155;">
          <li style='margin-bottom:8px;'>จงออกแบบสถาปัตยกรรมทรานซิสเตอร์ 2D TMD-FET สำหรับหน่วยประมวลผลตรรกะขนาดต่ำกว่า 2 นาโนเมตร</li><li style='margin-bottom:8px;'>ออกแบบระบบเซลล์แสงอาทิตย์อินทรีย์ประสิทธิภาพสูงโดยใช้โมเลกุล $	ext{PC}_{71}	ext{BM}$ ร่วมกับพอลิเมอร์ Bandgap แคบ</li><li style='margin-bottom:8px;'>วิเคราะห์แนวทางการนำ Twistronics ในวัสดุ 2D ซ้อนสามชั้น (Trilayer Graphene) มาประยุกต์สร้างควอนตัมคอมพิวเตอร์</li><li style='margin-bottom:8px;'>เขียนโค้ด Python เพื่อคำนวณและพล็อตกราฟแถบพลังงาน Dispersion Relation ของกราฟีน 2D รอบจุด Dirac Cone</li>
        </ol>
      </div>
    </div>
    """
