# -*- coding: utf-8 -*-
"""
Chapter 4: การวิเคราะห์ลักษณะเฉพาะขั้นสูงระดับนาโน
Advanced Characterization, Nanometrology, STM, AFM, FE-SEM, HR-TEM, XPS & Raman
"""

def get_chapter_4():
    return r"""
    <div class="chapter-container">
      <div class="chapter-hero">
        <div class="chapter-badge">CHAPTER 04 • NANOTECHNOLOGICAL PHYSICS</div>
        <h1 class="chapter-title">การวิเคราะห์ลักษณะเฉพาะขั้นสูงระดับนาโน</h1>
        <p class="chapter-subtitle">Advanced Characterization, Nanometrology, STM, AFM, FE-SEM, HR-TEM, XPS & Raman</p>
      </div>

      <div class="diagram-wrap">
        <img src="../assets/diagrams/ch04_characterization.svg" alt="การวิเคราะห์ลักษณะเฉพาะขั้นสูงระดับนาโน">
        <div class="caption">ภาพที่ 4.1 แผนผังการเปรียบเทียบเทคนิคกล้องจุลทรรศน์หัววัด (STM/AFM), กล้องจุลทรรศน์อิเล็กตรอน (FE-SEM/HR-TEM), และสเปกโตรสโกปี (XPS/XRD/Raman)</div>
      </div>

      
    <div class="topic-section">
      <h2>4.1 กล้องจุลทรรศน์ส่องกราดแบบอุโมงค์ (Scanning Tunneling Microscopy - STM)</h2>
      <div class="topic-en-title">(Scanning Tunneling Microscopy (STM) & Tunneling Spectroscopy (STS))</div>
      
      <div class="topic-intro">
        <p>การประดิษฐ์กล้องจุลทรรศน์ส่องกราดแบบอุโมงค์ (Scanning Tunneling Microscopy: STM) โดยเกิร์ด บินนิก และไฮน์ริช โรเรอร์ ในปี 1981 ณ ศูนย์วิจัยไอบีเอ็มซูริก (ได้รับรางวัลโนเบลสาขาฟิสิกส์ในปี 1986) ถือเป็นจุดเปลี่ยนครั้งประวัติศาสตร์ที่เปิดศักราชแห่งวิทยาศาสตร์และเทคโนโลยีระดับนาโน โดยทำให้นักฟิสิกส์สามารถ 'มองเห็น' และ 'จัดเรียง' อะตอมเดี่ยวบนพื้นผิวของแข็งได้เป็นครั้งแรกในประวัติศาสตร์มนุษยชาติ</p>
    <p>หลักการทำงานของ STM อาศัยปรากฏการณ์ทะลุผ่านเชิงควอนตัมของอิเล็กตรอนระหว่างหัวเข็มโลหะนำไฟฟ้าที่มีความแหลมคมระดับอะตอมเดี่ยว (เช่น เข็มทังสเตนหรือแพลทินัม-อิริเดียม) กับพื้นผิวตัวอย่างนำไฟฟ้า โดยเว้นระยะห่างสุญญากาศเพียง $d pprox 0.3 - 1.0	ext{ nm}$ ภายใต้แรงดันไบแอส $V_{	ext{bias}}$ ไม่กี่มิลลิโวลต์ถึงสองโวลต์</p>
    <p>กระแสทะลุผ่าน (Tunneling Current: $I_t$) มีความไวต่อระยะห่าง $d$ ในระดับเอกซ์โพเนนเชียลอย่างยิ่งยวด โดยการเปลี่ยนระยะห่างเพียง $0.1	ext{ nm}$ (ประมาณ 1 อังสตรอม) จะทำให้กระแสเปลี่ยนไปถึง 10 เท่า ($1000\%$) ส่งผลให้ STM มีความละเอียดในแนวดิ่งสูงถึง $0.01	ext{ nm}$ ($0.1	ext{ \AA}$) ซึ่งละเอียดกว่าขนาดของอะตอมเดี่ยว</p>
  </div>

      <div class="subtopic-block">
        <h3>ทฤษฎีของเทอร์ซอฟฟ์-ฮาแมนน์ (Tersoff-Hamann Theory of STM)</h3>
            <p>กระแสอุโมงค์คำนวณจากสูตรของ Tersoff-Hamann: $I_t \propto V 	imes ho_t(E_F) 	imes 	ext{LDOS}_s(r_0, E_F)$ โดยที่ $	ext{LDOS}_s$ คือความหนาแน่นของสถานะพลังงานเฉพาะที่ของตัวอย่าง (Local Density of States)</p>
    <p>ภาพภูมิประเทศที่บันทึกจากโหมด Constant Current แท้จริงแล้วไม่ใช่รูปทรงเรขาคณิตของอะตอม แต่เป็นพื้นผิวที่มีค่า LDOS เท่ากัน (Contour of Constant LDOS) ที่ระดับพลังงานเฟอร์มิ</p>
  </div>

      <div class="subtopic-block">
        <h3>สเปกโทรสโกปีการทะลุผ่านส่องกราด (Scanning Tunneling Spectroscopy: STS)</h3>
            <p>การตรึงหัวเข็มไว้ที่ตำแหน่งหนึ่งแล้วกวาดแรงดัน $V$ พร้อมวัดอนุพันธ์ $rac{dI}{dV}$ จะได้ข้อมูลที่แปรผันตรงกับ $	ext{LDOS}(E)$ ทำให้สามารถวัดช่องว่างแถบพลังงานและโครงสร้างอิเล็กทรอนิกส์ของโมเลกุลเดี่ยวได้โดยตรง</p>
  </div>
  <div class="formula-group">

        <div class="equation-box">
          <div class="equation-header">📌 สมการฟิสิกส์หลัก: กระแสทะลุผ่านควอนตัมใน STM</div>
          <div class="formula-math">$$I_t \propto V_{\text{bias}} \exp\left( -2 d \frac{\sqrt{2m \Phi}}{\hbar} \right) \approx V_{\text{bias}} \exp(-A \sqrt{\Phi} d)$$</div>
          <p style="font-size:9.5pt; margin:4px 0 0 0; color:#334155; line-height:1.75; text-indent:0;"><strong>คำอธิบายตัวแปรและนัยสำคัญ:</strong> กระแสอุโมงค์ลดลงแบบเอกซ์โพเนนเชียลตามระยะห่าง d</p>
        </div>
            
        <div class="equation-box">
          <div class="equation-header">📌 สมการฟิสิกส์หลัก: สเปกโทรสโกปีอนุพันธ์สภาพนำไฟฟ้า STS</div>
          <div class="formula-math">$$\frac{dI/dV}{I/V} \propto \text{LDOS}_s(E_F + eV), \qquad A = \frac{2\sqrt{2m}}{\hbar} \approx 1.025\text{ \AA}^{-1}\text{eV}^{-1/2}$$</div>
          <p style="font-size:9.5pt; margin:4px 0 0 0; color:#334155; line-height:1.75; text-indent:0;"><strong>คำอธิบายตัวแปรและนัยสำคัญ:</strong> การหา Local Density of States ด้วย STS</p>
        </div>
              </div>

      <div class="table-block">
        <h3>📊 ตารางพารามิเตอร์การทำงานและขีดความสามารถของ STM</h3>
        <table class="data-table">
          <thead><tr>
            <th>พารามิเตอร์</th><th>ค่าการทำงานทั่วไป</th><th>ขีดจำกัดสูงสุด</th><th>หน่วย</th></tr></thead>
<tbody><tr><td>ระยะห่างเข็ม-ผิว d</td><td>0.4 - 0.8</td><td>0.2 (เริ่มเกิดแรงสัมผัส)</td><td>nm</td></tr><tr><td>กระแสอุโมงค์ It</td><td>0.1 - 2.0</td><td>0.01 - 100</td><td>nA</td></tr><tr><td>แรงดันไบแอส Vbias</td><td>0.01 - 2.5</td><td>0.001 - 10</td><td>V</td></tr><tr><td>ความละเอียดในแนวราบ (x, y)</td><td>0.1 - 0.2</td><td>0.05 (Sub-atomic)</td><td>nm</td></tr><tr><td>ความละเอียดในแนวดิ่ง (z)</td><td>0.01 (0.1 Å)</td><td>0.001 (0.01 Å)</td><td>nm</td></tr></tbody></table>
</div>
  <div class="examples-group">

        <div class="example-box">
          <div class="example-header">
            <span>📝 ตัวอย่างการคำนวณที่ 4.1: การคำนวณการเปลี่ยนแปลงของกระแสอุโมงค์เมื่อระยะห่างเข็มเปลี่ยนไป 0.1 nm</span>
            <span style="background:#dcfce7; color:#15803d; font-size:8.5pt; padding:3px 10px; border-radius:4px; font-weight:700;">Step-by-Step Worked Solution</span>
          </div>
          <p style="text-indent:0; margin-bottom:10px;"><strong>โจทย์ปัญหา (Problem Statement):</strong><br>หัวเข็ม STM ทำงานเหนือพื้นผิวทองคำที่มีฟังก์ชันงานเฉลี่ย $\Phi = 4.5	ext{ eV}$ จงคำนวณอัตราส่วนกระแส $rac{I(d + 0.1	ext{ nm})}{I(d)}$</p>
          <div style="background:rgba(255,255,255,0.85); border:1px solid #e2e8f0; padding:12px 16px; border-radius:6px; margin:12px 0;">
            <strong style="color:#1e3a8a;">การวิเคราะห์และการคำนวณอย่างละเอียด:</strong><br>
            <p style="text-indent:0; margin:6px 0 0 0; line-height:1.85;">1. คำนวณค่าคงที่การสลายตัว $\kappa = \frac{\sqrt{2 m \Phi}}{\hbar} = \frac{\sqrt{2(9.109 \times 10^{-31})(4.5 \times 1.602 \times 10^{-19})}}{1.0546 \times 10^{-34}} = 1.087 \times 10^{10}\text{ m}^{-1} = 1.087\text{ \AA}^{-1}$<br>2. ระยะที่เพิ่มขึ้น $\Delta d = 0.1\text{ nm} = 1.0\text{ \AA}$<br>3. อัตราส่วนกระแส $\frac{I_2}{I_1} = \exp(-2 \kappa \Delta d) = \exp(-2 \times 1.087 \times 1.0) = \exp(-2.174) = 0.1137$</p>
          </div>
          <div style="background:#f0fdf4; border-left:4px solid #16a34a; padding:10px 14px; margin-top:10px; font-size:9.5pt; color:#166534; border-radius:0 6px 6px 0;">
            💡 <strong>นัยสำคัญทางกายภาพและการประยุกต์ใช้งาน (Physical Insight):</strong><br>
            <span style="color:#14532d;">กระแสลดลงเหลือเพียง $11.37\%$ (ลดลงเกือบ 10 เท่า) เมื่อเข็มถอยห่างออกมาเพียง $0.1	ext{ nm}$ แสดงถึงความไวระดับสุดยอด</span>
          </div>
        </div>
            
        <div class="example-box">
          <div class="example-header">
            <span>📝 ตัวอย่างการคำนวณที่ 4.2: การหาช่องว่างแถบพลังงานของแผ่น MoS2 ชั้นเดี่ยวด้วย STS</span>
            <span style="background:#dcfce7; color:#15803d; font-size:8.5pt; padding:3px 10px; border-radius:4px; font-weight:700;">Step-by-Step Worked Solution</span>
          </div>
          <p style="text-indent:0; margin-bottom:10px;"><strong>โจทย์ปัญหา (Problem Statement):</strong><br>จากการวัด STS บนแผ่น $	ext{MoS}_2$ ชั้นเดี่ยว พบว่ากระแสอุโมงค์ $I_t$ เป็นศูนย์ในช่วงแรงดันไบแอสตั้งแต่ $-1.35	ext{ V}$ ถึง $+0.85	ext{ V}$ จงคำนวณหา (ก) ช่องว่างแถบพลังงาน $E_g$ (ข) ชนิดของการโดปปิ้งในแผ่นตัวอย่าง</p>
          <div style="background:rgba(255,255,255,0.85); border:1px solid #e2e8f0; padding:12px 16px; border-radius:6px; margin:12px 0;">
            <strong style="color:#1e3a8a;">การวิเคราะห์และการคำนวณอย่างละเอียด:</strong><br>
            <p style="text-indent:0; margin:6px 0 0 0; line-height:1.85;">1. ขอบแถบเวเลนซ์ $E_v = -1.35\text{ eV}$ และขอบแถบนำกระแส $E_c = +0.85\text{ eV}$<br>2. ช่องว่างแถบพลังงาน $E_g = E_c - E_v = 0.85 - (-1.35) = 2.20\text{ eV}$<br>3. ระดับเฟอร์มิ ($0\text{ V}$) อยู่ใกล้ $E_c$ ($0.85\text{ eV}$) มากกว่า $E_v$ ($1.35\text{ eV}$)</p>
          </div>
          <div style="background:#f0fdf4; border-left:4px solid #16a34a; padding:10px 14px; margin-top:10px; font-size:9.5pt; color:#166534; border-radius:0 6px 6px 0;">
            💡 <strong>นัยสำคัญทางกายภาพและการประยุกต์ใช้งาน (Physical Insight):</strong><br>
            <span style="color:#14532d;">แผ่น $	ext{MoS}_2$ นี้มีช่องว่างแถบพลังงาน $2.20	ext{ eV}$ และมีพฤติกรรมเป็นสารกึ่งตัวนำชนิดเอ็น (n-type semiconductor)</span>
          </div>
        </div>
              </div>
  <div class="code-group">

        <div class="code-box">
          <div class="code-header">💻 แบบจำลองเชิงคำนวณภาษาไพทอน (Computational Python 3.11): กรณีศึกษา: การจัดเรียงอะตอมเดี่ยวสร้าง Quantum Mirage และโลโก้ไอบีเอ็ม (Don Eigler, 1989)</div>
          <pre><code>การใช้หัวเข็ม STM ลากอะตอมของก๊าซซีนอน 35 อะตอมมาเรียงเป็นตัวอักษร 'IBM' บนผิวผลึกนิกเกิลที่อุณหภูมิ 4 เคลวิน เป็นหมุดหมายแรกที่พิสูจน์คำทำนายของริชาร์ด ไฟน์แมนว่ามนุษย์สามารถจัดวางอะตอมทีละตัวได้จริง</code></pre>
        </div>
        <p style="font-size:9.5pt; color:#475569; margin-top:-6px; margin-bottom:18px; text-indent:0;"><em>คำอธิบายอัลกอริทึมการจำลอง:</em> สคริปต์ไพทอนสำหรับการคำนวณและจำลองเชิงตัวเลข</p>
              </div>
  <div class="lab-connection-block">
    <h3>🔬 การเชื่อมโยงสู่ห้องปฏิบัติการเสมือนจริงและเทคนิคการทดลอง (Virtual Lab Connection)</h3>
    <div style='background:#f0fdf4; border:1px solid #bbf7d0; border-left:5px solid #16a34a; padding:12px 16px; margin-bottom:14px; border-radius:6px;'><strong style='color:#166534; font-size:10.5pt;'>การคำนวณและจำลองกระแสอุโมงค์ STM</strong><p style='margin:6px 0 0 0; color:#14532d; text-indent:0; line-height:1.8;'>stm_tunneling_sim.py</p></div>
  </div>
  <div class="cases-block">
    <h3>🌐 กรณีศึกษางานวิจัยแนวหน้าและนวัตกรรมอุตสาหกรรม (Frontier Case Studies)</h3>
    <div style='background:#eff6ff; border:1px solid #bfdbfe; border-left:5px solid #2563eb; padding:12px 16px; margin-bottom:14px; border-radius:6px;'><strong style='color:#1e40af; font-size:10.5pt;'>การเชื่อมโยงกับ Virtual Lab 16: การจำลองกล้องจุลทรรศน์ส่องกราดแบบอุโมงค์ STM และ STS</strong><p style='margin:6px 0 0 0; color:#1e3a8a; text-indent:0; line-height:1.8;'>ผู้เรียนสามารถควบคุมหัวเข็ม STM สแกนพื้นผิวกราไฟต์ HOPG สังเกตอะตอมคาร์บอนแบบเรียลไทม์ และวัดกราฟสเปกโตรสโกปี $dI/dV$ ใน Lab 16</p></div>
  </div>

      <div class="checkpoint-box" style="background:#fefce8; border:1px solid #fef08a; border-left:5px solid #eab308; padding:14px 18px; margin:24px 0 35px 0; border-radius:6px; page-break-inside:avoid;">
        <strong style="color:#854d0e; font-size:10pt;">🎯 จุดตรวจประเมินความเข้าใจและคำถามทบทวนประจำหัวข้อ 4.1 (Concept Checkpoint)</strong>
        <ul style="margin:8px 0 0 0; padding-left:20px; color:#713f12; font-size:9.5pt; line-height:1.8;">
          <li>จงอธิบายแนวคิดรวบยอดหลักของ กล้องจุลทรรศน์ส่องกราดแบบอุโมงค์ (Scanning Tunneling Microscopy - STM) และความแตกต่างจากพฤติกรรมในระดับมหภาค</li>
          <li>พารามิเตอร์ใดเป็นปัจจัยวิกฤตที่ควบคุมสมบัติทางฟิสิกส์ในหัวข้อนี้ และมีผลกระทบอย่างไร?</li>
          <li>เชื่อมโยงหลักการฟิสิกส์ในหัวข้อนี้เข้ากับการประยุกต์ใช้จริงในเทคโนโลยีสมัยใหม่</li>
        </ul>
      </div>
    </div>
    
    <div class="topic-section">
      <h2>4.2 กล้องจุลทรรศน์แรงอะตอมและโหมดวัดขั้นสูง</h2>
      <div class="topic-en-title">(Atomic Force Microscopy (AFM) & Advanced Functional Modes)</div>
      
      <div class="topic-intro">
        <p>กล้องจุลทรรศน์แรงอะตอม (Atomic Force Microscopy: AFM) ถูกพัฒนาขึ้นโดยเกิร์ด บินนิก, คาลฟิน ควอท และคริสตอฟ เกอร์เบอร์ ในปี 1986 เพื่อก้าวข้ามข้อจำกัดของ STM ที่วัดได้เฉพาะตัวอย่างนำไฟฟ้า ทำให้สามารถถ่ายภาพพื้นผิวของฉนวนไฟฟ้า เซรามิก สารอินทรีย์ ดีเอ็นเอ และเซลล์สิ่งมีชีวิตได้อย่างคมชัดถึงระดับนาโนเมตร</p>
    <p>หลักการของ AFM อาศัยแรงอันตรกิริยาระหว่างอะตอม (Interatomic Forces) ระหว่างหัวเข็มแหลมคมที่ติดอยู่ปลายคานโยกยืดหยุ่น (Microcantilever) กับพื้นผิวตัวอย่าง โดยวัดการโก่งตัวของคานด้วยระบบสะท้อนแสงเลเซอร์เข้าสู่ตัวตรวจจับโฟโตไดโอดสี่ส่วน (Four-Quadrant Photodiode Detector)</p>
    <p>เส้นโค้งแรงเทียบกับระยะทางอธิบายด้วยศักย์เลนนาร์ด-โจนส์ (Lennard-Jones Potential) ซึ่งแบ่งเป็นโหมดสัมผัส (Contact Mode - แรงผลักคูลอมบ์), โหมดไม่สัมผัส (Non-Contact Mode - แรงดึงดูดฟานเดอร์วาลส์), และโหมดเคาะ (Tapping/AM-AFM) ซึ่งเป็นโหมดมาตรฐานที่ลดความเสียหายต่อตัวอย่างชีวภาพได้อย่างยอดเยี่ยม</p>
  </div>

      <div class="subtopic-block">
        <h3>ศักย์เลนนาร์ด-โจนส์และโหมดการทำงานของ AFM</h3>
            <p>ศักย์อันตรกิริยา: $V_{	ext{LJ}}(r) = 4\epsilon \left[ \left(rac{\sigma}{r}ight)^{12} - \left(rac{\sigma}{r}ight)^6 ight]$</p>
    <p>1. Contact Mode ($r < r_0$): ทำงานในย่านแรงผลักคูลอมบ์ของกลุ่มหมอกอิเล็กตรอน คานโยกโก่งตัวตามกฎของฮุก $F = -k \Delta z$</p>
    <p>2. Tapping Mode (Intermittent Contact): คานโยกถูกสั่นที่ความถี่เรโซแนนซ์ $f_0$ เมื่อเข้าใกล้ผิว แอมพลิจูดการสั่นจะลดลง ระบบฟีดแบ็กจะรักษาแอมพลิจูดให้คงที่เพื่อสร้างภาพความสูง</p>
    <p>3. PeakForce Tapping: ควบคุมแรงกดสูงสุดในแต่ละรอบการเคาะได้ต่ำกว่าพิโกนิวตัน ($< 50	ext{ pN}$) พร้อมวัดค่ามอดุลัสความยืดหยุ่นเชิงกลได้พร้อมกัน</p>
  </div>

      <div class="subtopic-block">
        <h3>โหมดการวัดสมบัติฟังก์ชันนัลขั้นสูง (Advanced Modes)</h3>
            <p>1. Kelvin Probe Force Microscopy (KPFM): วัดศักย์งานพื้นผิว (Surface Work Function) และศักย์สัมผัส CPD</p>
    <p>2. Conductive AFM (C-AFM): ใช้เข็มเคลือบโลหะ/เพชรนำไฟฟ้าวัดกระแสไฟฟ้าเฉพาะจุดระดับ pA</p>
    <p>3. Piezoresponse Force Microscopy (PFM): วัดการเปลี่ยนรูปเพียโซอิเล็กทริกและโดเมนเฟอร์โรอิเล็กทริก</p>
    <p>4. Magnetic Force Microscopy (MFM): ใช้เข็มเคลือบสารแม่เหล็กตรวจจับเส้นแรงแม่เหล็กบนฮาร์ดดิสก์</p>
  </div>
  <div class="formula-group">

        <div class="equation-box">
          <div class="equation-header">📌 สมการฟิสิกส์หลัก: กฎของฮุกสำหรับคานโยก AFM</div>
          <div class="formula-math">$$F = -k \Delta z, \qquad f_0 = \frac{1}{2\pi} \sqrt{\frac{k}{m^*}}$$</div>
          <p style="font-size:9.5pt; margin:4px 0 0 0; color:#334155; line-height:1.75; text-indent:0;"><strong>คำอธิบายตัวแปรและนัยสำคัญ:</strong> แรงกระทำและควอนตัมความถี่เรโซแนนซ์ของคานโยก</p>
        </div>
            
        <div class="equation-box">
          <div class="equation-header">📌 สมการฟิสิกส์หลัก: ศักย์เลนนาร์ด-โจนส์และแรงฟานเดอร์วาลส์</div>
          <div class="formula-math">$$F(r) = -\frac{dV_{\text{LJ}}}{dr} = \frac{24\epsilon}{\sigma} \left[ 2\left(\frac{\sigma}{r}\right)^{13} - \left(\frac{\sigma}{r}\right)^7 \right]$$</div>
          <p style="font-size:9.5pt; margin:4px 0 0 0; color:#334155; line-height:1.75; text-indent:0;"><strong>คำอธิบายตัวแปรและนัยสำคัญ:</strong> แรงอันตรกิริยาระหว่างหัวเข็มและพื้นผิว</p>
        </div>
              </div>

      <div class="table-block">
        <h3>📊 ตารางเปรียบเทียบโหมดการทำงานหลักของ AFM</h3>
        <table class="data-table">
          <thead><tr>
            <th>โหมดการวัด</th><th>แรงกระทำหลัก</th><th>แอมพลิจูดการสั่น</th><th>ข้อดี</th><th>ข้อจำกัด</th></tr></thead>
<tbody><tr><td>Contact Mode</td><td>แรงผลัก ($1 - 100	ext{ nN}$)</td><td>ไม่มี (สัมผัสคงที่)</td><td>ถ่ายภาพเร็ว ความละเอียดสูง</td><td>เข็มสึกหรอ ตัวอย่างนิ่มเสียหาย</td></tr><tr><td>Tapping Mode</td><td>แรงผลัก/ดึงสลับกัน</td><td>10 - 100 nm</td><td>ไม่ทำลายตัวอย่างชีวภาพ/พอลิเมอร์</td><td>ความเร็วการสแกนปานกลาง</td></tr><tr><td>Non-Contact Mode</td><td>แรงดึงดูด ($< 0.1	ext{ nN}$)</td><td>< 5 nm (ความถี่ FM)</td><td>ได้ Atomic Resolution ในสุญญากาศ</td><td>ควบคุมยาก ต้องใช้ UHV</td></tr><tr><td>PeakForce QNM</td><td>แรงกดสูงสุด (< 100 pN)</td><td>10 - 30 nm (1-2 kHz)</td><td>วัด Modulus, Adhesion ได้ทันที</td><td>ต้องใช้หัววัดที่สอบเทียบแม่นยำ</td></tr></tbody></table>
</div>
  <div class="examples-group">

        <div class="example-box">
          <div class="example-header">
            <span>📝 ตัวอย่างการคำนวณที่ 4.3: การคำนวณแรงกดของคานโยก AFM ใน Contact Mode</span>
            <span style="background:#dcfce7; color:#15803d; font-size:8.5pt; padding:3px 10px; border-radius:4px; font-weight:700;">Step-by-Step Worked Solution</span>
          </div>
          <p style="text-indent:0; margin-bottom:10px;"><strong>โจทย์ปัญหา (Problem Statement):</strong><br>คานโยกซิลิคอนไนไตรด์มีค่าคงที่สปริง $k = 0.20	ext{ N/m}$ เมื่อเลเซอร์ตรวจพบการโก่งตัว $\Delta z = 15.0	ext{ nm}$ จงคำนวณแรงกด $F$ ที่กระทำต่อตัวอย่างในหน่วยนาโนนิวตัน</p>
          <div style="background:rgba(255,255,255,0.85); border:1px solid #e2e8f0; padding:12px 16px; border-radius:6px; margin:12px 0;">
            <strong style="color:#1e3a8a;">การวิเคราะห์และการคำนวณอย่างละเอียด:</strong><br>
            <p style="text-indent:0; margin:6px 0 0 0; line-height:1.85;">$$F = k \times \Delta z = 0.20\text{ N/m} \times (15.0 \times 10^{-9}\text{ m}) = 3.0 \times 10^{-9}\text{ N} = 3.0\text{ nN}$$</p>
          </div>
          <div style="background:#f0fdf4; border-left:4px solid #16a34a; padding:10px 14px; margin-top:10px; font-size:9.5pt; color:#166534; border-radius:0 6px 6px 0;">
            💡 <strong>นัยสำคัญทางกายภาพและการประยุกต์ใช้งาน (Physical Insight):</strong><br>
            <span style="color:#14532d;">แรงกดเพียง $3	ext{ nN}$ อยู่ในระดับต่ำมาก ช่วยให้สามารถสแกนโครงสร้างชีวโมเลกุล เช่น สายดีเอ็นเอ โดยไม่ทำให้สายขาด</span>
          </div>
        </div>
            
        <div class="example-box">
          <div class="example-header">
            <span>📝 ตัวอย่างการคำนวณที่ 4.4: การคำนวณการเลื่อนของความถี่เรโซแนนซ์ใน Frequency Modulation AFM (FM-AFM)</span>
            <span style="background:#dcfce7; color:#15803d; font-size:8.5pt; padding:3px 10px; border-radius:4px; font-weight:700;">Step-by-Step Worked Solution</span>
          </div>
          <p style="text-indent:0; margin-bottom:10px;"><strong>โจทย์ปัญหา (Problem Statement):</strong><br>คานโยก AFM มีค่าคงที่สปริง $k = 40	ext{ N/m}$ และความถี่เรโซแนนซ์อิสระ $f_0 = 300.0	ext{ kHz}$ เมื่อหัวเข็มเข้าใกล้ผิวจนเกิดเกรเดียนต์ของแรง $rac{\partial F}{\partial z} = -0.08	ext{ N/m}$ (แรงดึงดูด) จงคำนวณความถี่ใหม่ $f$ และการเลื่อนของความถี่ $\Delta f$</p>
          <div style="background:rgba(255,255,255,0.85); border:1px solid #e2e8f0; padding:12px 16px; border-radius:6px; margin:12px 0;">
            <strong style="color:#1e3a8a;">การวิเคราะห์และการคำนวณอย่างละเอียด:</strong><br>
            <p style="text-indent:0; margin:6px 0 0 0; line-height:1.85;">1. ค่าคงที่สปริงยังผล $k_{\text{eff}} = k - \frac{\partial F}{\partial z} = 40 - (-0.08) = 40.08\text{ N/m}$<br>2. การเลื่อนความถี่ประมาณ: $\Delta f \approx \frac{f_0}{2k} \left( \frac{\partial F}{\partial z} \right) = \frac{300 \times 10^3}{2(40)} \times (-0.08) = -300\text{ Hz}$<br>3. ความถี่ใหม่ $f = 300,000 - 300 = 299,700\text{ Hz} = 299.70\text{ kHz}$</p>
          </div>
          <div style="background:#f0fdf4; border-left:4px solid #16a34a; padding:10px 14px; margin-top:10px; font-size:9.5pt; color:#166534; border-radius:0 6px 6px 0;">
            💡 <strong>นัยสำคัญทางกายภาพและการประยุกต์ใช้งาน (Physical Insight):</strong><br>
            <span style="color:#14532d;">การตรวจจับการเลื่อนความถี่เพียง $300	ext{ Hz}$ ช่วยให้ระบบ FM-AFM สร้างภาพโครงสร้างพันธะเคมีภายในโมเลกุลเดี่ยวได้อย่างคมชัด</span>
          </div>
        </div>
              </div>
  <div class="code-group">

        <div class="code-box">
          <div class="code-header">💻 แบบจำลองเชิงคำนวณภาษาไพทอน (Computational Python 3.11): กรณีศึกษา: การถ่ายภาพพันธะเคมีและโครงสร้างโมเลกุลเดี่ยวด้วย CO-functionalized Tip nc-AFM</div>
          <pre><code>ทีมนักวิจัยของ IBM และสถาบันฟิสิกส์ชั้นนำใช้หัวเข็ม AFM ที่ติดโมเลกุลคาร์บอนมอนอกไซด์ (CO) เดี่ยวที่ปลายเข็ม ถ่ายภาพวงแหวนเบนซีนและโครงสร้างพันธะโควาเลนต์ของโมเลกุลเพนทาซีน (Pentacene) ได้อย่างคมชัดจนเห็นโครงสร้างพันธะเคมีจริงเป็นครั้งแรก</code></pre>
        </div>
        <p style="font-size:9.5pt; color:#475569; margin-top:-6px; margin-bottom:18px; text-indent:0;"><em>คำอธิบายอัลกอริทึมการจำลอง:</em> สคริปต์ไพทอนสำหรับการคำนวณและจำลองเชิงตัวเลข</p>
              </div>
  <div class="lab-connection-block">
    <h3>🔬 การเชื่อมโยงสู่ห้องปฏิบัติการเสมือนจริงและเทคนิคการทดลอง (Virtual Lab Connection)</h3>
    <div style='background:#f0fdf4; border:1px solid #bbf7d0; border-left:5px solid #16a34a; padding:12px 16px; margin-bottom:14px; border-radius:6px;'><strong style='color:#166534; font-size:10.5pt;'>การจำลองศักย์และแรงเลนนาร์ด-โจนส์ใน AFM</strong><p style='margin:6px 0 0 0; color:#14532d; text-indent:0; line-height:1.8;'>afm_force_curve.py</p></div>
  </div>
  <div class="cases-block">
    <h3>🌐 กรณีศึกษางานวิจัยแนวหน้าและนวัตกรรมอุตสาหกรรม (Frontier Case Studies)</h3>
    <div style='background:#eff6ff; border:1px solid #bfdbfe; border-left:5px solid #2563eb; padding:12px 16px; margin-bottom:14px; border-radius:6px;'><strong style='color:#1e40af; font-size:10.5pt;'>การเชื่อมโยงกับ Virtual Lab 17: การจำลองกล้องจุลทรรศน์แรงอะตอม AFM และ Force Spectroscopy</strong><p style='margin:6px 0 0 0; color:#1e3a8a; text-indent:0; line-height:1.8;'>ผู้เรียนสามารถเลือกโหมด Contact, Tapping หรือ KPFM ใน Lab 17 สังเกตการสะท้อนของลำแสงเลเซอร์ และวัดเส้นโค้ง Force-Distance Curve</p></div>
  </div>

      <div class="checkpoint-box" style="background:#fefce8; border:1px solid #fef08a; border-left:5px solid #eab308; padding:14px 18px; margin:24px 0 35px 0; border-radius:6px; page-break-inside:avoid;">
        <strong style="color:#854d0e; font-size:10pt;">🎯 จุดตรวจประเมินความเข้าใจและคำถามทบทวนประจำหัวข้อ 4.2 (Concept Checkpoint)</strong>
        <ul style="margin:8px 0 0 0; padding-left:20px; color:#713f12; font-size:9.5pt; line-height:1.8;">
          <li>จงอธิบายแนวคิดรวบยอดหลักของ กล้องจุลทรรศน์แรงอะตอมและโหมดวัดขั้นสูง และความแตกต่างจากพฤติกรรมในระดับมหภาค</li>
          <li>พารามิเตอร์ใดเป็นปัจจัยวิกฤตที่ควบคุมสมบัติทางฟิสิกส์ในหัวข้อนี้ และมีผลกระทบอย่างไร?</li>
          <li>เชื่อมโยงหลักการฟิสิกส์ในหัวข้อนี้เข้ากับการประยุกต์ใช้จริงในเทคโนโลยีสมัยใหม่</li>
        </ul>
      </div>
    </div>
    
    <div class="topic-section">
      <h2>4.3 กล้องจุลทรรศน์อิเล็กตรอนแบบส่องกราดความละเอียดสูง</h2>
      <div class="topic-en-title">(Field-Emission SEM (FE-SEM) & Energy-Dispersive X-ray (EDS))</div>
      
      <div class="topic-intro">
        <p>กล้องจุลทรรศน์อิเล็กตรอนแบบส่องกราดแบบฟิลด์อิมิชชัน (Field-Emission Scanning Electron Microscopy: FE-SEM) เป็นเครื่องมือหลักในการตรวจสอบสัณฐานวิทยา พื้นผิว และโครงสร้าง 3 มิติของวัสดุนาโน โดยใช้ปืนยิงอิเล็กตรอนแบบสนามไฟฟ้าแรงสูง (Field Emission Gun: FEG) ซึ่งให้ลำแสงอิเล็กตรอนที่มีความสว่าง (Brightness) สูงกว่าหลอดไส้ทังสเตนแบบเดิมกว่า 1,000 เท่า และมีขนาดโฟกัสของลำแสงเล็กต่ำกว่า 1 นาโนเมตร</p>
    <p>เมื่อลำอิเล็กตรอนปฐมภูมิ (Primary Electrons: PE พลังงาน 0.5 - 30 keV) ยิงตกกระทบผิวตัวอย่าง จะเกิดอันตรกิริยาเป็นรูปหยดน้ำภายในเนื้อสาร (Interaction Volume) และปลดปล่อยสัญญาณต่างๆ ออกมา ได้แก่ อิเล็กตรอนทุติยภูมิ (Secondary Electrons: SE สำหรับวิเคราะห์สัณฐานผิวละเอียด), อิเล็กตรอนกระเจิงสะท้อนกลับ (Backscattered Electrons: BSE สำหรับแยกความแตกต่างของเลขอะตอม Z-contrast), และรังสีเอกซ์ลักษณะเฉพาะ (Characteristic X-rays สำหรับวิเคราะห์องค์ประกอบธาตุ)</p>
    <p>การติดตั้งตัวตรวจวัดสเปกโทรสโกปีการกระจายพลังงานรังสีเอกซ์ (Energy-Dispersive X-ray Spectroscopy: EDS หรือ EDX) ช่วยให้สามารถสร้างแผนที่การกระจายตัวของธาตุเชิงพื้นที่ (Elemental Mapping) ได้อย่างรวดเร็วและแม่นยำในระดับความละเอียดไม่กี่สิบนาโนเมตร</p>
  </div>

      <div class="subtopic-block">
        <h3>ฟิสิกส์ของสัญญาณอิเล็กตรอน SE, BSE และรังสีเอกซ์ EDS</h3>
            <p>1. Secondary Electrons (SE, พลังงาน $< 50	ext{ eV}$): หลุดออกมาจากชั้นผิวตื้นที่สุด ($< 5 - 10	ext{ nm}$) ให้ภาพสัณฐานภูมิประเทศและความคมชัดของขอบชิ้นงาน (Edge Effect)</p>
    <p>2. Backscattered Electrons (BSE, พลังงานสูงใกล้เคียง PE): เกิดจากการกระเจิงแบบยืดหยุ่นกับนิวเคลียส สัมประสิทธิ์การกระเจิง $\eta$ แปรผันตรงกับเลขอะตอม $Z$ ทำให้บริเวณที่มีธาตุหนักจะสว่างกว่าบริเวณธาตุเบา</p>
    <p>3. Characteristic X-rays (EDS): เกิดจากการที่อิเล็กตรอนชั้นในหลุดออก แล้วอิเล็กตรอนชั้นนอกตกลงมาแทนที่พร้อมคายโฟตอนรังสีเอกซ์ที่มีพลังงานจำเพาะต่อธาตุ เช่น $	ext{K}_lpha, 	ext{L}_lpha$</p>
  </div>

      <div class="subtopic-block">
        <h3>เทคนิค Low-Voltage High-Resolution SEM สำหรับวัสดุนาโนและชีวภาพ</h3>
            <p>การลดพลังงานลำอิเล็กตรอนเหลือ $0.5 - 1.0	ext{ keV}$ ช่วยลดขนาด Interaction Volume ให้อยู่เฉพาะที่ผิวหน้า ป้องกันการสะสมประจุ (Charging Effect) ในตัวอย่างฉนวน และลดความเสียหายจากลำแสงต่อตัวอย่างพอลิเมอร์และวัสดุ 2D</p>
  </div>
  <div class="formula-group">

        <div class="equation-box">
          <div class="equation-header">📌 สมการฟิสิกส์หลัก: ความลึกและขนาดปริมาตรอันตรกิริยาของกาเนีย (Kanaya-Okayama Range)</div>
          <div class="formula-math">$$R_{\text{KO}} = \frac{0.0276 \, A}{\rho \, Z^{0.89}} E_0^{1.67} \quad (\mu\text{m})$$</div>
          <p style="font-size:9.5pt; margin:4px 0 0 0; color:#334155; line-height:1.75; text-indent:0;"><strong>คำอธิบายตัวแปรและนัยสำคัญ:</strong> ความลึกการแทรกซึมของลำอิเล็กตรอนในเนื้อสาร</p>
        </div>
            
        <div class="equation-box">
          <div class="equation-header">📌 สมการฟิสิกส์หลัก: กฎการเลี้ยวเบนและพลังงานรังสีเอกซ์เอกลักษณ์ (Moseley's Law)</div>
          <div class="formula-math">$$\sqrt{\frac{E_X}{h c R_\infty}} = (Z - \sigma) \sqrt{\frac{1}{n_1^2} - \frac{1}{n_2^2}}$$</div>
          <p style="font-size:9.5pt; margin:4px 0 0 0; color:#334155; line-height:1.75; text-indent:0;"><strong>คำอธิบายตัวแปรและนัยสำคัญ:</strong> ความสัมพันธ์ระหว่างพลังงานรังสีเอกซ์ EDS และเลขอะตอม Z</p>
        </div>
              </div>

      <div class="table-block">
        <h3>📊 ตารางเปรียบเทียบสัญญาณที่เกิดขึ้นในกล้อง FE-SEM</h3>
        <table class="data-table">
          <thead><tr>
            <th>สัญญาณตรวจวัด</th><th>ช่วงพลังงาน</th><th>ความลึกที่หลุดออกมา</th><th>ข้อมูลที่ได้รับ</th><th>ตัวตรวจวัดที่ใช้</th></tr></thead>
<tbody><tr><td>Secondary Electrons (SE)</td><td>< 50 eV</td><td>2 - 10 nm</td><td>สัณฐานวิทยาผิว ความลึก 3D</td><td>In-Lens SE / Everhart-Thornley</td></tr><tr><td>Backscattered (BSE)</td><td>50 eV - E0</td><td>100 - 1000 nm</td><td>ความแตกต่างของธาตุ (Z-Contrast)</td><td>Solid-State Concentric Ring BSD</td></tr><tr><td>Characteristic X-rays</td><td>0.1 - 20 keV</td><td>500 - 3000 nm</td><td>ชนิดและปริมาณธาตุ (เชิงคุณภาพ/ปริมาณ)</td><td>Silicon Drift Detector (SDD-EDS)</td></tr><tr><td>Cathodoluminescence</td><td>1.5 - 4.0 eV (แสง)</td><td>100 - 500 nm</td><td>แถบพลังงานและข้อบกพร่องในผลึก</td><td>CL Optical Spectrometer</td></tr></tbody></table>
</div>
  <div class="examples-group">

        <div class="example-box">
          <div class="example-header">
            <span>📝 ตัวอย่างการคำนวณที่ 4.5: การคำนวณความลึกการแทรกซึมของลำอิเล็กตรอนในซิลิคอน</span>
            <span style="background:#dcfce7; color:#15803d; font-size:8.5pt; padding:3px 10px; border-radius:4px; font-weight:700;">Step-by-Step Worked Solution</span>
          </div>
          <p style="text-indent:0; margin-bottom:10px;"><strong>โจทย์ปัญหา (Problem Statement):</strong><br>ลำอิเล็กตรอนพลังงาน $E_0 = 15.0	ext{ keV}$ ยิงลงบนเวเฟอร์ซิลิคอน ($Z = 14$, $A = 28.085	ext{ g/mol}$, $ho = 2.33	ext{ g/cm}^3$) จงคำนวณหาความลึกการแทรกซึม $R_{	ext{KO}}$ ตามสมการของ Kanaya-Okayama</p>
          <div style="background:rgba(255,255,255,0.85); border:1px solid #e2e8f0; padding:12px 16px; border-radius:6px; margin:12px 0;">
            <strong style="color:#1e3a8a;">การวิเคราะห์และการคำนวณอย่างละเอียด:</strong><br>
            <p style="text-indent:0; margin:6px 0 0 0; line-height:1.85;">1. คำนวณเทอม $Z^{0.89} = 14^{0.89} = 10.51$<br>2. เทอมพลังงาน $E_0^{1.67} = 15^{1.67} = 93.36$<br>3. $R_{\text{KO}} = \frac{0.0276 \times 28.085}{2.33 \times 10.51} \times 93.36 = \frac{0.7751}{24.49} \times 93.36 = 2.955\text{ }\mu\text{m}$</p>
          </div>
          <div style="background:#f0fdf4; border-left:4px solid #16a34a; padding:10px 14px; margin-top:10px; font-size:9.5pt; color:#166534; border-radius:0 6px 6px 0;">
            💡 <strong>นัยสำคัญทางกายภาพและการประยุกต์ใช้งาน (Physical Insight):</strong><br>
            <span style="color:#14532d;">ที่พลังงาน 15 keV ลำแสงแทรกซึมลึกเกือบ 3 ไมโครเมตร ทำให้สัญญาณ EDS รวมข้อมูลจากชั้นใต้ผิวลงไปด้วย หากต้องการวิเคราะห์ฟิล์มบางระดับ 10 nm ต้องลดพลังงานลงเหลือต่ำกว่า 2 keV ($R_{	ext{KO}} pprox 0.08	ext{ }\mu	ext{m}$)</span>
          </div>
        </div>
            
        <div class="example-box">
          <div class="example-header">
            <span>📝 ตัวอย่างการคำนวณที่ 4.6: การระบุธาตุจากพลังงานรังสีเอกซ์ EDS K-alpha</span>
            <span style="background:#dcfce7; color:#15803d; font-size:8.5pt; padding:3px 10px; border-radius:4px; font-weight:700;">Step-by-Step Worked Solution</span>
          </div>
          <p style="text-indent:0; margin-bottom:10px;"><strong>โจทย์ปัญหา (Problem Statement):</strong><br>ตัวตรวจวัด EDS ตรวจพบสัญญาณพีครังสีเอกซ์ที่พลังงาน $E_X = 6.40	ext{ keV}$ และ $E_X = 8.04	ext{ keV}$ จงระบุว่าสัญญาณทั้งสองสอดคล้องกับธาตุชนิดใดในตารางธาตุ</p>
          <div style="background:rgba(255,255,255,0.85); border:1px solid #e2e8f0; padding:12px 16px; border-radius:6px; margin:12px 0;">
            <strong style="color:#1e3a8a;">การวิเคราะห์และการคำนวณอย่างละเอียด:</strong><br>
            <p style="text-indent:0; margin:6px 0 0 0; line-height:1.85;">1. พลังงาน $6.40\text{ keV}$ สอดคล้องกับเส้นสเปกตรัม $\text{Fe K}_\alpha$ (ธาตุเหล็ก $Z=26$ มี $K_\alpha = 6.404\text{ keV}$)<br>2. พลังงาน $8.04\text{ keV}$ สอดคล้องกับเส้นสเปกตรัม $\text{Cu K}_\alpha$ (ธาตุทองแดง $Z=29$ มี $K_\alpha = 8.048\text{ keV}$)</p>
          </div>
          <div style="background:#f0fdf4; border-left:4px solid #16a34a; padding:10px 14px; margin-top:10px; font-size:9.5pt; color:#166534; border-radius:0 6px 6px 0;">
            💡 <strong>นัยสำคัญทางกายภาพและการประยุกต์ใช้งาน (Physical Insight):</strong><br>
            <span style="color:#14532d;">สามารถระบุได้ทันทีว่าตัวอย่างประกอบด้วยอนุภาคเหล็กบนกริดทองแดงอย่างแม่นยำ</span>
          </div>
        </div>
              </div>
  <div class="code-group">

        <div class="code-box">
          <div class="code-header">💻 แบบจำลองเชิงคำนวณภาษาไพทอน (Computational Python 3.11): กรณีศึกษา: การวิเคราะห์โครงสร้างความผิดพลาดในชิปประมวลผล 3 นาโนเมตรด้วย Cross-Sectional FE-SEM</div>
          <pre><code>การตัดขวางโครงสร้างชิปด้วยลำไอออนโฟกัส (FIB) และนำมาถ่ายภาพด้วย In-Lens FE-SEM ที่ 1 keV ช่วยให้ตรวจสอบความหนาของชั้นออกไซด์และเกต GAAFET ขนาด 2-3 nm ได้อย่างชัดเจนโดยไม่มีการบิดเบือนของภาพ</code></pre>
        </div>
        <p style="font-size:9.5pt; color:#475569; margin-top:-6px; margin-bottom:18px; text-indent:0;"><em>คำอธิบายอัลกอริทึมการจำลอง:</em> สคริปต์ไพทอนสำหรับการคำนวณและจำลองเชิงตัวเลข</p>
              </div>
  <div class="lab-connection-block">
    <h3>🔬 การเชื่อมโยงสู่ห้องปฏิบัติการเสมือนจริงและเทคนิคการทดลอง (Virtual Lab Connection)</h3>
    <div style='background:#f0fdf4; border:1px solid #bbf7d0; border-left:5px solid #16a34a; padding:12px 16px; margin-bottom:14px; border-radius:6px;'><strong style='color:#166534; font-size:10.5pt;'>การจำลองขนาด Interaction Volume ใน FE-SEM</strong><p style='margin:6px 0 0 0; color:#14532d; text-indent:0; line-height:1.8;'>sem_interaction_volume.py</p></div>
  </div>
  <div class="cases-block">
    <h3>🌐 กรณีศึกษางานวิจัยแนวหน้าและนวัตกรรมอุตสาหกรรม (Frontier Case Studies)</h3>
    <div style='background:#eff6ff; border:1px solid #bfdbfe; border-left:5px solid #2563eb; padding:12px 16px; margin-bottom:14px; border-radius:6px;'><strong style='color:#1e40af; font-size:10.5pt;'>การเชื่อมโยงกับ Virtual Lab 18: การจำลองกล้องจุลทรรศน์อิเล็กตรอน FE-SEM และการวิเคราะห์ธาตุ EDS</strong><p style='margin:6px 0 0 0; color:#1e3a8a; text-indent:0; line-height:1.8;'>ผู้เรียนสามารถปรับค่าพลังงานเร่ง (Accelerating Voltage), โฟกัสลำแสง, เลือกตัวตรวจวัด In-Lens SE / BSE และทำ Elemental Mapping ใน Lab 18</p></div>
  </div>

      <div class="checkpoint-box" style="background:#fefce8; border:1px solid #fef08a; border-left:5px solid #eab308; padding:14px 18px; margin:24px 0 35px 0; border-radius:6px; page-break-inside:avoid;">
        <strong style="color:#854d0e; font-size:10pt;">🎯 จุดตรวจประเมินความเข้าใจและคำถามทบทวนประจำหัวข้อ 4.3 (Concept Checkpoint)</strong>
        <ul style="margin:8px 0 0 0; padding-left:20px; color:#713f12; font-size:9.5pt; line-height:1.8;">
          <li>จงอธิบายแนวคิดรวบยอดหลักของ กล้องจุลทรรศน์อิเล็กตรอนแบบส่องกราดความละเอียดสูง และความแตกต่างจากพฤติกรรมในระดับมหภาค</li>
          <li>พารามิเตอร์ใดเป็นปัจจัยวิกฤตที่ควบคุมสมบัติทางฟิสิกส์ในหัวข้อนี้ และมีผลกระทบอย่างไร?</li>
          <li>เชื่อมโยงหลักการฟิสิกส์ในหัวข้อนี้เข้ากับการประยุกต์ใช้จริงในเทคโนโลยีสมัยใหม่</li>
        </ul>
      </div>
    </div>
    
    <div class="topic-section">
      <h2>4.4 กล้องจุลทรรศน์อิเล็กตรอนแบบส่องผ่านและการเลี้ยวเบน</h2>
      <div class="topic-en-title">(High-Resolution TEM (HR-TEM), STEM & Electron Diffraction (SAED))</div>
      
      <div class="topic-intro">
        <p>กล้องจุลทรรศน์อิเล็กตรอนแบบส่องผ่านความละเอียดสูง (High-Resolution Transmission Electron Microscopy: HR-TEM) คือเครื่องมือวิเคราะห์ทางกายภาพที่มีความละเอียดเชิงพื้นที่สูงที่สุดในวงการวิทยาศาสตร์นาโน สามารถสร้างภาพแถวระนาบอะตอม (Atomic Lattice Fringes) และระบุตำแหน่งของอะตอมเดี่ยวในผลึกได้อย่างแม่นยำ โดยใช้อิเล็กตรอนพลังงานสูงยิ่งยวด (80 - 300 keV) ซึ่งมีความยาวคลื่นเดอบรอยล์สั้นเพียง $0.02 - 0.04	ext{ \AA}$ ส่องทะลุผ่านชิ้นงานที่มีความบางเป็นพิเศษ ($< 50	ext{ nm}$)</p>
    <p>การเกิดภาพใน HR-TEM อาศัยการแทรกสอดของเฟสคลื่นอิเล็กตรอน (Phase Contrast Mechanism) ซึ่งเกิดจากความแตกต่างของเฟสคลื่นที่เลี้ยวเบนผ่านสนามศักย์ไฟฟ้าของอะตอม โดยมีฟังก์ชันถ่ายโอนความเปรียบต่างเฟส (Contrast Transfer Function: CTF) ที่กำหนดขีดจำกัดความละเอียดของระบบเลนส์แม่เหล็กไฟฟ้า</p>
    <p>นอกจากนี้ โหมดการเลี้ยวเบนของอิเล็กตรอนเฉพาะพื้นที่ (Selected Area Electron Diffraction: SAED) ช่วยระบุโครงสร้างผลึก ทิศทางการจัดเรียง และความสมบูรณ์ของผลึกเดี่ยว ผลึกพหุ หรืออสัณฐานได้อย่างชัดเจน ขณะที่โหมดส่องกราดแบบส่องผ่าน (Scanning TEM: STEM) ร่วมกับตัวตรวจวัดมุมกว้าง (High-Angle Annular Dark-Field: HAADF) ให้ภาพที่มีความสว่างแปรผันตาม $Z^2$ (Atomic Number Contrast) ทำให้มองเห็นอะตอมโลหะหนักเดี่ยวที่กระจายตัวอยู่บนแผ่นกราฟีนได้อย่างสมบูรณ์</p>
  </div>

      <div class="subtopic-block">
        <h3>ฟังก์ชันถ่ายโอนความเปรียบต่างเฟส (Contrast Transfer Function - CTF) และ Scherzer Defocus</h3>
            <p>สมการ CTF: $T(u) = \sin\left( \pi \Delta f \lambda u^2 + rac{1}{2} \pi C_s \lambda^3 u^4 ight)$ เมื่อ $\Delta f$ คือระยะโฟกัสคลาดเคลื่อน และ $C_s$ คือความคลาดทรงกลม (Spherical Aberration)</p>
    <p>ที่จุด Scherzer Defocus: $\Delta f_{	ext{Sch}} = -1.2 \sqrt{C_s \lambda}$ จะได้ความละเอียดของกล้อง (Point Resolution): $d_{	ext{Sch}} pprox 0.65 (C_s \lambda^3)^{1/4}$</p>
    <p>การติดตั้งระบบแก้ไขความคลาดทรงกลม (Cs-Corrector) ในปัจจุบันช่วยผลักดันให้ความละเอียดของ HR-TEM ทะลุขีดจำกัดต่ำกว่า $0.5	ext{ \AA}$ ($0.05	ext{ nm}$)</p>
  </div>

      <div class="subtopic-block">
        <h3>การแปลผลลวดลายการเลี้ยวเบนอิเล็กตรอน SAED ตามกฎของแบร็กก์</h3>
            <p>รัศมีของวงแหวนหรือระยะห่างจุดเลี้ยวเบน $R$ สัมพันธ์กับระยะห่างระนาบผลึก $d_{hkl}$ ด้วยสมการกล้อง: $R 	imes d_{hkl} = \lambda L$ (โดยที่ $\lambda L$ คือค่าคงที่ของกล้อง Camera Constant)</p>
  </div>
  <div class="formula-group">

        <div class="equation-box">
          <div class="equation-header">📌 สมการฟิสิกส์หลัก: ความยาวคลื่นเดอบรอยล์แบบสัมพัทธภาพของอิเล็กตรอนใน TEM</div>
          <div class="formula-math">$$\lambda = \frac{h}{\sqrt{2 m_0 e V \left( 1 + \frac{e V}{2 m_0 c^2} \right)}} \approx \frac{1.226}{\sqrt{V (1 + 0.9788 \times 10^{-6} V)}}\text{ nm}$$</div>
          <p style="font-size:9.5pt; margin:4px 0 0 0; color:#334155; line-height:1.75; text-indent:0;"><strong>คำอธิบายตัวแปรและนัยสำคัญ:</strong> ความยาวคลื่นอิเล็กตรอนที่คำนึงถึงผลสัมพัทธภาพพิเศษ</p>
        </div>
            
        <div class="equation-box">
          <div class="equation-header">📌 สมการฟิสิกส์หลัก: สมการการเลี้ยวเบนของอิเล็กตรอน (Camera Equation)</div>
          <div class="formula-math">$$R \cdot d_{hkl} = \lambda L, \qquad d_{\text{Sch}} \approx 0.65 \, (C_s \lambda^3)^{1/4}$$</div>
          <p style="font-size:9.5pt; margin:4px 0 0 0; color:#334155; line-height:1.75; text-indent:0;"><strong>คำอธิบายตัวแปรและนัยสำคัญ:</strong> ความสัมพันธ์การเลี้ยวเบนและขีดจำกัดความละเอียด Scherzer</p>
        </div>
              </div>

      <div class="table-block">
        <h3>📊 ตารางความยาวคลื่นอิเล็กตรอน TEM ที่แรงดันเร่งต่างๆ</h3>
        <table class="data-table">
          <thead><tr>
            <th>แรงดันเร่ง (Accelerating Voltage)</th><th>ความเร็วอิเล็กตรอน (v/c)</th><th>ความยาวคลื่นไม่คิดสัมพัทธภาพ</th><th>ความยาวคลื่นสัมพัทธภาพ λ</th></tr></thead>
<tbody><tr><td>80 kV (สำหรับ 2D/Graphene)</td><td>0.503 c</td><td>0.0433 Å (0.00433 nm)</td><td>0.0418 Å (0.00418 nm)</td></tr><tr><td>120 kV (ชีววิทยา/ไวรัส)</td><td>0.587 c</td><td>0.0354 Å</td><td>0.0335 Å (0.00335 nm)</td></tr><tr><td>200 kV (มาตรฐานวัสดุศาสตร์)</td><td>0.695 c</td><td>0.0274 Å</td><td>0.0251 Å (0.00251 nm)</td></tr><tr><td>300 kV (ความละเอียดระดับอะตอมสูงสุด)</td><td>0.777 c</td><td>0.0224 Å</td><td>0.0197 Å (0.00197 nm)</td></tr></tbody></table>
</div>
  <div class="examples-group">

        <div class="example-box">
          <div class="example-header">
            <span>📝 ตัวอย่างการคำนวณที่ 4.7: การคำนวณความยาวคลื่นสัมพัทธภาพของอิเล็กตรอนที่ 200 kV</span>
            <span style="background:#dcfce7; color:#15803d; font-size:8.5pt; padding:3px 10px; border-radius:4px; font-weight:700;">Step-by-Step Worked Solution</span>
          </div>
          <p style="text-indent:0; margin-bottom:10px;"><strong>โจทย์ปัญหา (Problem Statement):</strong><br>กล้อง HR-TEM ทำงานที่แรงดันเร่ง $V = 200	ext{ kV}$ จงคำนวณหา (ก) ปัจจัยลอเรนซ์ $\gamma$ และความเร็วของอิเล็กตรอน (ข) ความยาวคลื่นเดอบรอยล์สัมพัทธภาพ $\lambda$</p>
          <div style="background:rgba(255,255,255,0.85); border:1px solid #e2e8f0; padding:12px 16px; border-radius:6px; margin:12px 0;">
            <strong style="color:#1e3a8a;">การวิเคราะห์และการคำนวณอย่างละเอียด:</strong><br>
            <p style="text-indent:0; margin:6px 0 0 0; line-height:1.85;">1. พลังงานจลน์ $E_k = 200\text{ keV} = 0.200\text{ MeV}$, พลังงานนิ่ง $E_0 = m_0 c^2 = 0.511\text{ MeV}$<br>2. $\gamma = 1 + \frac{E_k}{E_0} = 1 + \frac{0.200}{0.511} = 1.3914 \implies v = c \sqrt{1 - 1/\gamma^2} = 0.695 c = 2.084 \times 10^8\text{ m/s}$<br>3. โมเมนตัม $p = \gamma m_0 v = 1.3914 \times (9.109 \times 10^{-31}) \times (2.084 \times 10^8) = 2.641 \times 10^{-22}\text{ kg}\cdot\text{m/s}$<br>4. $\lambda = \frac{h}{p} = \frac{6.626 \times 10^{-34}}{2.641 \times 10^{-22}} = 2.509 \times 10^{-12}\text{ m} = 0.0251\text{ \AA} = 0.00251\text{ nm}$</p>
          </div>
          <div style="background:#f0fdf4; border-left:4px solid #16a34a; padding:10px 14px; margin-top:10px; font-size:9.5pt; color:#166534; border-radius:0 6px 6px 0;">
            💡 <strong>นัยสำคัญทางกายภาพและการประยุกต์ใช้งาน (Physical Insight):</strong><br>
            <span style="color:#14532d;">ความยาวคลื่นสั้นเพียง $0.025	ext{ \AA}$ สั้นกว่าระยะห่างระหว่างอะตอมในผลึก ($~ 2 - 3	ext{ \AA}$) กว่า 100 เท่า</span>
          </div>
        </div>
            
        <div class="example-box">
          <div class="example-header">
            <span>📝 ตัวอย่างการคำนวณที่ 4.8: การคำนวณระยะห่างระนาบผลึกทองคำจากภาพถ่าย HR-TEM Lattice Fringes</span>
            <span style="background:#dcfce7; color:#15803d; font-size:8.5pt; padding:3px 10px; border-radius:4px; font-weight:700;">Step-by-Step Worked Solution</span>
          </div>
          <p style="text-indent:0; margin-bottom:10px;"><strong>โจทย์ปัญหา (Problem Statement):</strong><br>จากภาพถ่าย HR-TEM ของอนุภาคนาโนทองคำ วัดระยะทางข้ามแถบระนาบผลึกคู่ขนานจำนวน 10 แถบได้ระยะรวม $L = 2.355	ext{ nm}$ จงคำนวณหาระยะห่างระนาบ $d_{hkl}$ และระบุว่าเป็นระนาบผลึกใดของทองคำ (FCC, $a = 0.4078	ext{ nm}$)</p>
          <div style="background:rgba(255,255,255,0.85); border:1px solid #e2e8f0; padding:12px 16px; border-radius:6px; margin:12px 0;">
            <strong style="color:#1e3a8a;">การวิเคราะห์และการคำนวณอย่างละเอียด:</strong><br>
            <p style="text-indent:0; margin:6px 0 0 0; line-height:1.85;">1. ระยะห่างระนาบ $d = \frac{L}{10} = \frac{2.355\text{ nm}}{10} = 0.2355\text{ nm} = 2.355\text{ \AA}$<br>2. คำนวณระยะห่างระนาบ $\{111\}$ ของทองคำ FCC: $d_{111} = \frac{a}{\sqrt{1^2 + 1^2 + 1^2}} = \frac{0.4078\text{ nm}}{\sqrt{3}} = 0.2354\text{ nm}$</p>
          </div>
          <div style="background:#f0fdf4; border-left:4px solid #16a34a; padding:10px 14px; margin-top:10px; font-size:9.5pt; color:#166534; border-radius:0 6px 6px 0;">
            💡 <strong>นัยสำคัญทางกายภาพและการประยุกต์ใช้งาน (Physical Insight):</strong><br>
            <span style="color:#14532d;">ระยะห่างตรงกับระนาบผลึก $	ext{Au}(111)$ อย่างแม่นยำ ซึ่งเป็นระนาบที่มีพลังงานพื้นผิวต่ำที่สุดและมีความหนาแน่นของอะตอมสูงสุด</span>
          </div>
        </div>
              </div>
  <div class="code-group">

        <div class="code-box">
          <div class="code-header">💻 แบบจำลองเชิงคำนวณภาษาไพทอน (Computational Python 3.11): กรณีศึกษา: การระบุตำแหน่งอะตอมแพลทินัมเดี่ยวบนตัวเร่งปฏิกิริยากราฟีน (Single-Atom Catalysts) ด้วย HAADF-STEM</div>
          <pre><code>การใช้เทคโนโลยี Aberration-Corrected HAADF-STEM ช่วยยืนยันการเกาะตัวของอะตอมเดี่ยว Pt ($Z=78$) บนแผ่นรองรับคาร์บอน ($Z=6$) ได้อย่างชัดเจน โดยอาศัยความเปรียบต่างของความสว่าง $Z^2$ ซึ่งช่วยให้ตัวเร่งปฏิกิริยาเซลล์เชื้อเพลิงมีประสิทธิภาพสูงสุด</code></pre>
        </div>
        <p style="font-size:9.5pt; color:#475569; margin-top:-6px; margin-bottom:18px; text-indent:0;"><em>คำอธิบายอัลกอริทึมการจำลอง:</em> สคริปต์ไพทอนสำหรับการคำนวณและจำลองเชิงตัวเลข</p>
              </div>
  <div class="lab-connection-block">
    <h3>🔬 การเชื่อมโยงสู่ห้องปฏิบัติการเสมือนจริงและเทคนิคการทดลอง (Virtual Lab Connection)</h3>
    <div style='background:#f0fdf4; border:1px solid #bbf7d0; border-left:5px solid #16a34a; padding:12px 16px; margin-bottom:14px; border-radius:6px;'><strong style='color:#166534; font-size:10.5pt;'>การคำนวณความยาวคลื่นสัมพัทธภาพและการเลี้ยวเบน TEM</strong><p style='margin:6px 0 0 0; color:#14532d; text-indent:0; line-height:1.8;'>tem_relativistic_calc.py</p></div>
  </div>
  <div class="cases-block">
    <h3>🌐 กรณีศึกษางานวิจัยแนวหน้าและนวัตกรรมอุตสาหกรรม (Frontier Case Studies)</h3>
    <div style='background:#eff6ff; border:1px solid #bfdbfe; border-left:5px solid #2563eb; padding:12px 16px; margin-bottom:14px; border-radius:6px;'><strong style='color:#1e40af; font-size:10.5pt;'>การเชื่อมโยงกับ Virtual Lab 19: การจำลองกล้องจุลทรรศน์อิเล็กตรอน HR-TEM และการเลี้ยวเบน SAED</strong><p style='margin:6px 0 0 0; color:#1e3a8a; text-indent:0; line-height:1.8;'>ผู้เรียนสามารถควบคุมการปรับโฟกัส Scherzer Defocus, ถ่ายภาพ Lattice Fringes และวิเคราะห์จุดเลี้ยวเบน SAED ของผลึกทองคำและซิลิคอนใน Lab 19</p></div>
  </div>

      <div class="checkpoint-box" style="background:#fefce8; border:1px solid #fef08a; border-left:5px solid #eab308; padding:14px 18px; margin:24px 0 35px 0; border-radius:6px; page-break-inside:avoid;">
        <strong style="color:#854d0e; font-size:10pt;">🎯 จุดตรวจประเมินความเข้าใจและคำถามทบทวนประจำหัวข้อ 4.4 (Concept Checkpoint)</strong>
        <ul style="margin:8px 0 0 0; padding-left:20px; color:#713f12; font-size:9.5pt; line-height:1.8;">
          <li>จงอธิบายแนวคิดรวบยอดหลักของ กล้องจุลทรรศน์อิเล็กตรอนแบบส่องผ่านและการเลี้ยวเบน และความแตกต่างจากพฤติกรรมในระดับมหภาค</li>
          <li>พารามิเตอร์ใดเป็นปัจจัยวิกฤตที่ควบคุมสมบัติทางฟิสิกส์ในหัวข้อนี้ และมีผลกระทบอย่างไร?</li>
          <li>เชื่อมโยงหลักการฟิสิกส์ในหัวข้อนี้เข้ากับการประยุกต์ใช้จริงในเทคโนโลยีสมัยใหม่</li>
        </ul>
      </div>
    </div>
    
    <div class="topic-section">
      <h2>4.5 สเปกโทรสโกปีโฟโตอิเล็กตรอนรังสีเอกซ์และรามาน</h2>
      <div class="topic-en-title">(X-ray Photoelectron Spectroscopy (XPS), XRD & Raman Metrology)</div>
      
      <div class="topic-intro">
        <p>การวิเคราะห์โครงสร้างทางเคมี พันธะ และผลึกศาสตร์ของวัสดุนาโนจำเป็นต้องอาศัยเทคนิคสเปกโทรสโกปีขั้นสูง 3 ประการหลัก ได้แก่ สเปกโทรสโกปีโฟโตอิเล็กตรอนรังสีเอกซ์ (X-ray Photoelectron Spectroscopy: XPS), การเลี้ยวเบนรังสีเอกซ์ (X-ray Diffraction: XRD), และสเปกโทรสโกปีรามาน (Raman Spectroscopy)</p>
    <p>XPS (หรือ ESCA) อาศัยปรากฏการณ์โฟโตอิเล็กทริกของไอน์สไตน์ โดยยิงรังสีเอกซ์พลังงานเอกรงค์ (เช่น $	ext{Al K}_lpha = 1486.6	ext{ eV}$) เพื่อให้อิเล็กตรอนชั้นใน (Core Electrons) หลุดออกมา และวัดพลังงานจลน์ $E_k$ เพื่อคำนวณพลังงานยึดเหนี่ยว (Binding Energy: $E_B = h
u - E_k - \Phi_{	ext{spec}}$) ซึ่งมีความไวต่อสถานะออกซิเดชันและพันธะเคมีที่ผิวตื้น ($< 5 - 10	ext{ nm}$)</p>
    <p>XRD วิเคราะห์โครงสร้างผลึก ขนาดผลึกเฉลี่ย (ตามสมการเดอบาย-เชอร์เรอร์: $D = rac{K\lambda}{eta \cos	heta}$) และความเค้นในโครงผลึก ขณะที่ Raman Spectroscopy เป็นเครื่องมือแบบไม่ทำลาย (Non-Destructive) ที่วิเคราะห์โหมดการสั่นของโมเลกุลและแลตทิซ (Phonon Modes) ซึ่งมีความสำคัญอย่างยิ่งในการระบุจำนวนชั้นและข้อบกพร่อง (Defects) ในกราฟีนและวัสดุ 2D</p>
  </div>

      <div class="subtopic-block">
        <h3>การวิเคราะห์การเลื่อนทางเคมี (Chemical Shift) ใน XPS</h3>
            <p>พลังงานยึดเหนี่ยว $E_B$ ของอิเล็กตรอนชั้นในจะเลื่อนไปตามสภาพแวดล้อมทางเคมี เช่น คาร์บอนในพันธะ $	ext{C}-	ext{C}$ ($	ext{sp}^2/	ext{sp}^3$) มี $E_B pprox 284.8	ext{ eV}$, พันธะ $	ext{C}-	ext{O}$ เลื่อนขึ้นเป็น $286.5	ext{ eV}$, พันธะ $	ext{C}=	ext{O}$ อยู่ที่ $288.0	ext{ eV}$, และพันธะ $	ext{O}-	ext{C}=	ext{O}$ อยู่ที่ $289.0	ext{ eV}$ ทำให้สามารถแยกองค์ประกอบของกราฟีนออกไซด์ (GO และ rGO) ได้อย่างละเอียด</p>
  </div>

      <div class="subtopic-block">
        <h3>สมการเดอบาย-เชอร์เรอร์ (Debye-Scherrer Equation) ใน XRD</h3>
            <p>ขนาดผลึกเฉลี่ย $D = rac{K \lambda}{eta \cos	heta}$ เมื่อ $K pprox 0.9$ คือตัวประกอบรูปร่างผลึก, $\lambda = 0.15406	ext{ nm}$ ($	ext{Cu K}_lpha$), และ $eta$ คือความกว้างครึ่งความสูงเต็ม (Full Width at Half Maximum: FWHM) ในหน่วยเรเดียน</p>
  </div>

      <div class="subtopic-block">
        <h3>รามานสเปกโทรสโกปีของกราฟีนและท่อคาร์บอนนาโน</h3>
            <p>พีคหลักของกราฟีนได้แก่: G band ($pprox 1582	ext{ cm}^{-1}$ จากการสั่นในระนาบ $	ext{E}_{2g}$), 2D band ($pprox 2690	ext{ cm}^{-1}$ จากกระบวนการ Double Resonance), และ D band ($pprox 1350	ext{ cm}^{-1}$ บ่งบอกถึงข้อบกพร่องและความไม่สมบูรณ์ของโครงสร้าง) โดยอัตราส่วนความสูง $I_{2D}/I_G > 2$ และความกว้าง $	ext{FWHM}_{2D} < 30	ext{ cm}^{-1}$ เป็นดัชนียืนยันกราฟีนชั้นเดี่ยวแท้</p>
  </div>
  <div class="formula-group">

        <div class="equation-box">
          <div class="equation-header">📌 สมการฟิสิกส์หลัก: สมการโฟโตอิเล็กทริกสำหรับ XPS</div>
          <div class="formula-math">$$E_B = h\nu - E_k - \Phi_{\text{spectrometer}}$$</div>
          <p style="font-size:9.5pt; margin:4px 0 0 0; color:#334155; line-height:1.75; text-indent:0;"><strong>คำอธิบายตัวแปรและนัยสำคัญ:</strong> การคำนวณพลังงานยึดเหนี่ยวของอิเล็กตรอนชั้นใน</p>
        </div>
            
        <div class="equation-box">
          <div class="equation-header">📌 สมการฟิสิกส์หลัก: สมการเดอบาย-เชอร์เรอร์สำหรับขนาดผลึกนาโน</div>
          <div class="formula-math">$$D = \frac{K \lambda}{\beta \cos\theta}, \qquad \beta = \sqrt{\beta_{\text{measured}}^2 - \beta_{\text{instrument}}^2}$$</div>
          <p style="font-size:9.5pt; margin:4px 0 0 0; color:#334155; line-height:1.75; text-indent:0;"><strong>คำอธิบายตัวแปรและนัยสำคัญ:</strong> การคำนวณขนาดผลึกเฉลี่ยจากความกว้างพีค XRD</p>
        </div>
              </div>

      <div class="table-block">
        <h3>📊 ตารางสรุปลักษณะเด่นของเทคนิค XPS, XRD และ Raman สำหรับวัสดุนาโน</h3>
        <table class="data-table">
          <thead><tr>
            <th>เทคนิค</th><th>แหล่งกระตุ้น</th><th>ข้อมูลที่ตรวจวัด</th><th>ความลึกในการวิเคราะห์</th><th>จุดเด่นหลัก</th></tr></thead>
<tbody><tr><td>XPS (ESCA)</td><td>รังสีเอกซ์ Al Kα (1.486 keV)</td><td>พลังงานยึดเหนี่ยว Eb, สถานะออกซิเดชัน</td><td>2 - 8 nm (ผิวหน้า)</td><td>บอกพันธะเคมีเชิงปริมาณแม่นยำ</td></tr><tr><td>XRD</td><td>รังสีเอกซ์ Cu Kα (8.04 keV)</td><td>มุมเลี้ยวเบน 2θ, ขนาดผลึก, แสตรน</td><td>1 - 10 μm (Bulk/Film)</td><td>บอกโครงสร้างผลึก ขนาดอนุภาคเฉลี่ย</td></tr><tr><td>Raman Spectroscopy</td><td>เลเซอร์ 532 / 633 / 785 nm</td><td>การเลื่อนรามาน (Raman Shift cm-1)</td><td>0.1 - 1 μm</td><td>ไม่ทำลายตัวอย่าง ยืนยันชั้นกราฟีน 2D</td></tr></tbody></table>
</div>
  <div class="examples-group">

        <div class="example-box">
          <div class="example-header">
            <span>📝 ตัวอย่างการคำนวณที่ 4.9: การคำนวณขนาดผลึกนาโน TiO2 จากข้อมูลพีค XRD</span>
            <span style="background:#dcfce7; color:#15803d; font-size:8.5pt; padding:3px 10px; border-radius:4px; font-weight:700;">Step-by-Step Worked Solution</span>
          </div>
          <p style="text-indent:0; margin-bottom:10px;"><strong>โจทย์ปัญหา (Problem Statement):</strong><br>ผลึกนาโน $	ext{TiO}_2$ อะนาเทส ให้พีคการเลี้ยวเบนระนาบ $(101)$ ที่มุม $2	heta = 25.30^\circ$ ($	heta = 12.65^\circ$) โดยมีค่าความกว้าง $	ext{FWHM} = 0.55^\circ$ กำหนดความกว้างเครื่องมือ $eta_{	ext{inst}} = 0.08^\circ$, $\lambda = 0.15406	ext{ nm}$ และ $K = 0.90$ จงคำนวณหาขนาดผลึกเฉลี่ย $D$</p>
          <div style="background:rgba(255,255,255,0.85); border:1px solid #e2e8f0; padding:12px 16px; border-radius:6px; margin:12px 0;">
            <strong style="color:#1e3a8a;">การวิเคราะห์และการคำนวณอย่างละเอียด:</strong><br>
            <p style="text-indent:0; margin:6px 0 0 0; line-height:1.85;">1. ความกว้างสุทธิ $\beta = \sqrt{(0.55)^2 - (0.08)^2} = \sqrt{0.3025 - 0.0064} = 0.5441^\circ$<br>2. แปลงเป็นเรเดียน: $\beta = 0.5441 \times \frac{\pi}{180} = 9.496 \times 10^{-3}\text{ rad}$<br>3. คำนวณ $\cos(\theta) = \cos(12.65^\circ) = 0.9757$<br>4. $D = \frac{K \lambda}{\beta \cos\theta} = \frac{0.90 \times 0.15406\text{ nm}}{(9.496 \times 10^{-3}) \times 0.9757} = \frac{0.13865}{0.009265} = 14.965\text{ nm} \approx 15.0\text{ nm}$</p>
          </div>
          <div style="background:#f0fdf4; border-left:4px solid #16a34a; padding:10px 14px; margin-top:10px; font-size:9.5pt; color:#166534; border-radius:0 6px 6px 0;">
            💡 <strong>นัยสำคัญทางกายภาพและการประยุกต์ใช้งาน (Physical Insight):</strong><br>
            <span style="color:#14532d;">ผลึกนาโน $	ext{TiO}_2$ มีขนาดเฉลี่ยประมาณ $15.0	ext{ nm}$ สอดคล้องกับขนาดที่วัดได้จากภาพถ่าย TEM</span>
          </div>
        </div>
            
        <div class="example-box">
          <div class="example-header">
            <span>📝 ตัวอย่างการคำนวณที่ 4.1: การวิเคราะห์คุณภาพและจำนวนชั้นของกราฟีนจากสเปกตรัมรามาน</span>
            <span style="background:#dcfce7; color:#15803d; font-size:8.5pt; padding:3px 10px; border-radius:4px; font-weight:700;">Step-by-Step Worked Solution</span>
          </div>
          <p style="text-indent:0; margin-bottom:10px;"><strong>โจทย์ปัญหา (Problem Statement):</strong><br>สเปกตรัมรามานของแผ่นกราฟีนที่กระตุ้นด้วยเลเซอร์ 532 nm แสดงพีค $I_D = 120	ext{ a.u.}$, $I_G = 1500	ext{ a.u.}$, $I_{2D} = 3600	ext{ a.u.}$ และมีความกว้าง $	ext{FWHM}_{2D} = 26.5	ext{ cm}^{-1}$ จงวิเคราะห์ (ก) จำนวนชั้นของกราฟีน (ข) ระดับความหนาแน่นของข้อบกพร่อง</p>
          <div style="background:rgba(255,255,255,0.85); border:1px solid #e2e8f0; padding:12px 16px; border-radius:6px; margin:12px 0;">
            <strong style="color:#1e3a8a;">การวิเคราะห์และการคำนวณอย่างละเอียด:</strong><br>
            <p style="text-indent:0; margin:6px 0 0 0; line-height:1.85;">1. อัตราส่วน $\frac{I_{2D}}{I_G} = \frac{3600}{1500} = 2.40$ ($> 2.0$)<br>2. ค่า $\text{FWHM}_{2D} = 26.5\text{ cm}^{-1}$ ($< 30\text{ cm}^{-1}$ และเป็นพีคเดี่ยวสมมาตรแบบ Lorentzian)<br>3. อัตราส่วน $\frac{I_D}{I_G} = \frac{120}{1500} = 0.08$ ($< 0.1$)</p>
          </div>
          <div style="background:#f0fdf4; border-left:4px solid #16a34a; padding:10px 14px; margin-top:10px; font-size:9.5pt; color:#166534; border-radius:0 6px 6px 0;">
            💡 <strong>นัยสำคัญทางกายภาพและการประยุกต์ใช้งาน (Physical Insight):</strong><br>
            <span style="color:#14532d;">ผลการวิเคราะห์ยืนยันว่าเป็น 'กราฟีนชั้นเดี่ยวคุณภาพสูง' (High-Quality Monolayer Graphene) ที่มีโครงสร้างสมบูรณ์และมีข้อบกพร่องต่ำมาก</span>
          </div>
        </div>
              </div>
  <div class="code-group">

        <div class="code-box">
          <div class="code-header">💻 แบบจำลองเชิงคำนวณภาษาไพทอน (Computational Python 3.11): กรณีศึกษา: การตรวจสอบคุณภาพกราฟีนและสารกึ่งตัวนำ 2D ในสายการผลิตเซมิคอนดักเตอร์ด้วย Automated Raman Mapping</div>
          <pre><code>การใช้ระบบ High-Speed Confocal Raman Imaging สามารถสแกนเวเฟอร์ขนาด 300 mm ได้ภายในเวลาไม่กี่นาที เพื่อสร้างแผนที่ความหนา ความเค้น และความสม่ำเสมอของฟิล์มกราฟีนและ $	ext{MoS}_2$ ก่อนส่งเข้ากระบวนการผลิตชิป</code></pre>
        </div>
        <p style="font-size:9.5pt; color:#475569; margin-top:-6px; margin-bottom:18px; text-indent:0;"><em>คำอธิบายอัลกอริทึมการจำลอง:</em> สคริปต์ไพทอนสำหรับการคำนวณและจำลองเชิงตัวเลข</p>
              </div>
  <div class="lab-connection-block">
    <h3>🔬 การเชื่อมโยงสู่ห้องปฏิบัติการเสมือนจริงและเทคนิคการทดลอง (Virtual Lab Connection)</h3>
    <div style='background:#f0fdf4; border:1px solid #bbf7d0; border-left:5px solid #16a34a; padding:12px 16px; margin-bottom:14px; border-radius:6px;'><strong style='color:#166534; font-size:10.5pt;'>การจำลองสมการ Scherrer สำหรับ XRD และสเปกตรัมรามาน</strong><p style='margin:6px 0 0 0; color:#14532d; text-indent:0; line-height:1.8;'>xrd_raman_sim.py</p></div>
  </div>
  <div class="cases-block">
    <h3>🌐 กรณีศึกษางานวิจัยแนวหน้าและนวัตกรรมอุตสาหกรรม (Frontier Case Studies)</h3>
    <div style='background:#eff6ff; border:1px solid #bfdbfe; border-left:5px solid #2563eb; padding:12px 16px; margin-bottom:14px; border-radius:6px;'><strong style='color:#1e40af; font-size:10.5pt;'>การเชื่อมโยงกับ Virtual Lab 20: การจำลองการวิเคราะห์สเปกโตรสโกปี XPS, XRD และ Raman</strong><p style='margin:6px 0 0 0; color:#1e3a8a; text-indent:0; line-height:1.8;'>ผู้เรียนสามารถ Deconvolute พีค XPS C1s, คำนวณขนาดผลึกจาก XRD และวิเคราะห์ชั้นกราฟีนจากสเปกตรัมรามานใน Lab 20</p></div>
  </div>

      <div class="checkpoint-box" style="background:#fefce8; border:1px solid #fef08a; border-left:5px solid #eab308; padding:14px 18px; margin:24px 0 35px 0; border-radius:6px; page-break-inside:avoid;">
        <strong style="color:#854d0e; font-size:10pt;">🎯 จุดตรวจประเมินความเข้าใจและคำถามทบทวนประจำหัวข้อ 4.5 (Concept Checkpoint)</strong>
        <ul style="margin:8px 0 0 0; padding-left:20px; color:#713f12; font-size:9.5pt; line-height:1.8;">
          <li>จงอธิบายแนวคิดรวบยอดหลักของ สเปกโทรสโกปีโฟโตอิเล็กตรอนรังสีเอกซ์และรามาน และความแตกต่างจากพฤติกรรมในระดับมหภาค</li>
          <li>พารามิเตอร์ใดเป็นปัจจัยวิกฤตที่ควบคุมสมบัติทางฟิสิกส์ในหัวข้อนี้ และมีผลกระทบอย่างไร?</li>
          <li>เชื่อมโยงหลักการฟิสิกส์ในหัวข้อนี้เข้ากับการประยุกต์ใช้จริงในเทคโนโลยีสมัยใหม่</li>
        </ul>
      </div>
    </div>
    

      <div class="summary-box">
        <h3 style="color:#1e40af; margin-top:0; font-size:13pt;">📋 สรุปสาระสำคัญประจำบทที่ 4 (Chapter 4 Key Takeaways)</h3>
        <ul style="margin:0; padding-left:22px; font-size:10pt; line-height:1.95; color:#1e293b;">
          <li style='margin-bottom:8px;'>STM ใช้กระแสทะลุผ่านควอนตัมที่แปรผันแบบเอกซ์โพเนนเชียลในการสร้างภาพและวัด LDOS ด้วย STS ในระดับอะตอมเดี่ยว</li><li style='margin-bottom:8px;'>AFM อาศัยแรงอันตรกิริยาระดับอะตอมตามศักย์เลนนาร์ด-โจนส์ สามารถวัดตัวอย่างฉนวนและสิ่งมีชีวิตได้ด้วย Tapping Mode และ PeakForce QNM</li><li style='margin-bottom:8px;'>FE-SEM ใช้ปืน FEG ให้ลำแสงความสว่างสูงและขนาดโฟกัสต่ำกว่า 1 nm ร่วมกับ EDS ในการสร้างแผนที่ธาตุเชิงพื้นที่</li><li style='margin-bottom:8px;'>HR-TEM และ Cs-corrected STEM มีความละเอียดต่ำกว่า 0.05 nm มองเห็นระนาบผลึก Lattice Fringes และอะตอมเดี่ยวแบบ HAADF</li><li style='margin-bottom:8px;'>XPS วิเคราะห์สถานะพันธะเคมีที่ผิวหน้า, XRD คำนวณขนาดผลึกตามสมการ Scherrer, และ Raman ยืนยันจำนวนชั้นและคุณภาพของวัสดุ 2D</li>
        </ul>
      </div>

      <div class="problems-section">
        <h3 style="color:#0f172a; margin-top:0; font-size:14pt; border-bottom:2px solid #cbd5e1; padding-bottom:8px;">
          📚 แบบฝึกหัดและโจทย์ปัญหาท้ายบทที่ 4 (End-of-Chapter Problems)
        </h3>
        
        <h4 style="color:#1e3a8a; font-size:11.5pt; margin-top:18px;">ตอนที่ 1: คำถามเชิงมโนทัศน์และการวิเคราะห์เชิงฟิสิกส์ (Conceptual & Analytical Questions)</h4>
        <ol style="padding-left:22px; font-size:10pt; line-height:1.9; color:#334155;">
          <li style='margin-bottom:8px;'>จงอธิบายเหตุใดกระแสอุโมงค์ใน STM จึงมีความไวต่อระยะห่างในระดับเศษส่วนของอังสตรอม</li><li style='margin-bottom:8px;'>เพราะเหตุใดภาพถ่ายจาก STM จึงเป็นภาพของ Local Density of States (LDOS) ไม่ใช่ภาพเรขาคณิตของอะตอม?</li><li style='margin-bottom:8px;'>จงเปรียบเทียบความแตกต่างระหว่าง Contact Mode และ Tapping Mode ในกล้อง AFM</li><li style='margin-bottom:8px;'>สัญญาณ SE และ BSE ในกล้อง FE-SEM เกิดจากกลไกทางฟิสิกส์ใด และให้ข้อมูลของชิ้นงานแตกต่างกันอย่างไร?</li><li style='margin-bottom:8px;'>จงอธิบายความหมายของ Scherzer Defocus ในกล้อง HR-TEM และเหตุใดจึงให้ความละเอียดสูงสุด</li><li style='margin-bottom:8px;'>ทำไมการเลี้ยวเบนของอิเล็กตรอน SAED จึงสามารถใช้วิเคราะห์ผลึกศาสตร์ของอนุภาคนาโนเดี่ยวได้?</li><li style='margin-bottom:8px;'>จงอธิบายหลักการวัด Chemical Shift ใน XPS ในการจำแนกสถานะพันธะของคาร์บอน</li><li style='margin-bottom:8px;'>ในการวิเคราะห์รามานของกราฟีน อัตราส่วน $I_{2D}/I_G$ และ $I_D/I_G$ บ่งบอกถึงคุณลักษณะใดบ้าง?</li>
        </ol>

        <h4 style="color:#166534; font-size:11.5pt; margin-top:22px;">ตอนที่ 2: โจทย์ปัญหาการคำนวณเชิงตัวเลขและการพิสูจน์ (Quantitative & Numerical Problems)</h4>
        <ol style="padding-left:22px; font-size:10pt; line-height:1.9; color:#334155;">
          <li style='margin-bottom:8px;'>หัวเข็ม STM มีฟังก์ชันงาน 4.0 eV จงคำนวณอัตราส่วนกระแสอุโมงค์เมื่อระยะห่าง $d$ เพิ่มขึ้น 0.15 nm</li><li style='margin-bottom:8px;'>คานโยก AFM มี $k = 0.5	ext{ N/m}$ และ $f_0 = 150	ext{ kHz}$ จงคำนวณมวลยังผล $m^*$ ของคานโยก</li><li style='margin-bottom:8px;'>คำนวณความลึก $R_{	ext{KO}}$ ของลำอิเล็กตรอน 20 keV ในแผ่นทองคำ ($ho = 19.3	ext{ g/cm}^3$, $Z = 79$, $A = 196.97	ext{ g/mol}$)</li><li style='margin-bottom:8px;'>กล้อง TEM ทำงานที่แรงดันเร่ง 300 kV จงคำนวณหาความยาวคลื่นสัมพัทธภาพของอิเล็กตรอนในหน่วยพิโกเมตร (pm)</li><li style='margin-bottom:8px;'>จากภาพ HR-TEM พบระยะห่าง 8 แถบผลึกเท่ากับ 1.632 nm จงคำนวณหาระยะห่างระนาบ $d_{hkl}$</li><li style='margin-bottom:8px;'>พีค XRD ของอนุภาคนาโน ZnO $(100)$ อยู่ที่ $2	heta = 31.75^\circ$ มี $	ext{FWHM} = 0.42^\circ$ จงคำนวณขนาดผลึกเฉลี่ย $D$ กำหนด $\lambda = 0.15406	ext{ nm}$</li><li style='margin-bottom:8px;'>ในการวัด XPS ด้วยรังสี Al Kα (1486.6 eV) ตรวจพบโฟโตอิเล็กตรอนมีพลังงานจลน์ $E_k = 1201.8	ext{ eV}$ กำหนด $\Phi_{	ext{spec}} = 4.2	ext{ eV}$ จงคำนวณหาพลังงานยึดเหนี่ยว $E_B$</li>
        </ol>

        <h4 style="color:#7c2d12; font-size:11.5pt; margin-top:22px;">ตอนที่ 3: โจทย์ประยุกต์ การออกแบบเชิงวิศวกรรม และการจำลอง (Applied Design & Modeling Problems)</h4>
        <ol style="padding-left:22px; font-size:10pt; line-height:1.9; color:#334155;">
          <li style='margin-bottom:8px;'>จงออกแบบชุดการวิเคราะห์ทางมาตรวิทยา (Metrology Suite) เพื่อตรวจสอบคุณภาพและความสมบูรณ์ของเวเฟอร์กราฟีนขนาด 300 mm</li><li style='margin-bottom:8px;'>ออกแบบระบบตัวตรวจจับ AFM ความเร็วสูง (High-Speed AFM) เพื่อถ่ายวิดีโอการเคลื่อนที่ของโปรเซสซอร์โมเลกุลชีวภาพแบบเรียลไทม์</li><li style='margin-bottom:8px;'>วิเคราะห์แนวทางการใช้เทคนิค Cryo-EM ร่วมกับ HR-TEM ในการหาโครงสร้าง 3 มิติของโปรตีนหนามไวรัสในระดับความละเอียดระดับอะตอม</li><li style='margin-bottom:8px;'>เขียนโค้ด Python เพื่อจำลองสเปกตรัม XRD ของอนุภาคนาโนที่มีขนาดผลึกแตกต่างกัน 3 ขนาด (5 nm, 15 nm, 50 nm)</li>
        </ol>
      </div>
    </div>
    """
