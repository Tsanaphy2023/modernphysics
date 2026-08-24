# -*- coding: utf-8 -*-
"""
Chapter 2: ปรากฏการณ์ควอนตัมในโครงสร้างนาโน
Quantum Wells, Quantum Wires, Artificial Atoms, Tunneling & Quantum Hall Physics
"""

def get_chapter_2():
    return r"""
    <div class="chapter-container">
      <div class="chapter-hero">
        <div class="chapter-badge">CHAPTER 02 • NANOTECHNOLOGICAL PHYSICS</div>
        <h1 class="chapter-title">ปรากฏการณ์ควอนตัมในโครงสร้างนาโน</h1>
        <p class="chapter-subtitle">Quantum Wells, Quantum Wires, Artificial Atoms, Tunneling & Quantum Hall Physics</p>
      </div>

      <div class="diagram-wrap">
        <img src="../assets/diagrams/ch02_quantum_phenomena.svg" alt="ปรากฏการณ์ควอนตัมในโครงสร้างนาโน">
        <div class="caption">ภาพที่ 2.1 แผนภาพแสดงโครงสร้าง 2DEG ใน HEMT, ขั้นบันไดสภาพนำไฟฟ้าใน QPC, ชั้นเปลือกใน QD และระดับแลนเดาใน Quantum Hall Effect</div>
      </div>

      
    <div class="topic-section">
      <h2>2.1 บ่อศักย์ควอนตัมสองมิติและแก๊สอิเล็กตรอนสองมิติ</h2>
      <div class="topic-en-title">(2D Quantum Wells & Two-Dimensional Electron Gas (2DEG))</div>
      
      <div class="topic-intro">
        <p>โครงสร้างบ่อศักย์ควอนตัม (Quantum Well) เกิดขึ้นจากการประกบชั้นสารกึ่งตัวนำที่มีช่องว่างแถบพลังงานแคบ เช่น GaAs ไว้ระหว่างชั้นสารกึ่งตัวนำที่มีช่องว่างแถบพลังงานกว้างกว่า เช่น AlGaAs จนเกิดเป็นรอยต่อเฮเทอโร (Heterojunction) ที่มีความหนาของชั้นบ่อ $L_z$ ในระดับไม่กี่นาโนเมตร ซึ่งเทียบเท่ากับหรือสั้นกว่าความยาวคลื่นเดอบรอยล์ของอิเล็กตรอน</p>
    <p>การจำกัดการเคลื่อนที่ของพาหะประจุในแนวแกน $z$ ส่งผลให้พลังงานในแนวแกนนี้ถูกควอนไทซ์เป็นระดับพลังงานไม่ต่อเนื่อง $E_n = rac{\hbar^2 \pi^2 n^2}{2 m^* L_z^2}$ ขณะที่การเคลื่อนที่ในระนาบ $(k_x, k_y)$ ยังคงเป็นอิสระและมีความต่อเนื่อง ก่อกำเนิดเป็นแถบพลังงานย่อยสองมิติ (2D Subbands)</p>
    <p>ที่รอยต่อแบบมอดูเลชันโดปปิ้ง (Modulation-Doped Heterostructure) อิเล็กตรอนอิสระจากชั้นสารเจือปนจะไหลมารวมกันที่ก้นบ่อศักย์สามเหลี่ยม ก่อให้เกิดแก๊สอิเล็กตรอนสองมิติ (Two-Dimensional Electron Gas: 2DEG) ซึ่งมีสภาพคล่องตัวของอิเล็กตรอน (Electron Mobility: $\mu_e$) สูงมากเป็นพิเศษเกิน $10^6	ext{ cm}^2/	ext{V}\cdot	ext{s}$ ที่อุณหภูมิต่ำ เนื่องจากอิเล็กตรอนแยกขาดจากไอออนสิ่งเจือปนอย่างสมบูรณ์</p>
  </div>

      <div class="subtopic-block">
        <h3>การแก้สมการชเรอดิงเงอร์สำหรับบ่อศักย์จำกัด (Finite Quantum Well)</h3>
            <p>คลื่นอิเล็กตรอนในบ่อศักย์ที่มีความลึกจำกัด $V_0$ จะแทรกซึมทะลุออกไปในชั้นกำแพงศักย์ (Evanescent Wave Decay) ตามฟังก์ชันเอกซ์โพเนนเชียล: $\psi_{	ext{barrier}}(z) \propto e^{-\kappa |z|}$ โดยมี $\kappa = \sqrt{rac{2m_b^* (V_0 - E)}{\hbar^2}}$</p>
    <p>เงื่อนไขความต่อเนื่องของ $\psi(z)$ และ $rac{1}{m^*(z)}rac{d\psi}{dz}$ ที่รอยต่อ นำไปสู่สมการทรานส์เซนเดนทัลสำหรับการหาระดับพลังงานผูกพัน (Bound States)</p>
  </div>

      <div class="subtopic-block">
        <h3>โครงสร้างมอดูเลชันโดปปิ้งและทรานซิสเตอร์ HEMT</h3>
            <p>การแยกอะตอมโดเนอร์ซิลิคอนไว้ในชั้น AlGaAs โดยเว้นระยะชั้นสเปเซอร์ (Undoped Spacer) ช่วยขจัดผลการกระเจิงคูลอมบ์ไอออนไนซ์ (Ionized Impurity Scattering)</p>
    <p>โครงสร้าง 2DEG นี้นำไปสู่การประดิษฐ์ High Electron Mobility Transistor (HEMT) ที่ใช้ในการขยายสัญญาณความถี่สูงยิ่งยวดระดับกิกะเฮิรตซ์และเทระเฮิรตซ์ในระบบเรดาร์และการสื่อสารผ่านดาวเทียม</p>
  </div>
  <div class="formula-group">

        <div class="equation-box">
          <div class="equation-header">📌 สมการฟิสิกส์หลัก: ระดับพลังงานในบ่อศักย์อนันต์ 2D</div>
          <div class="formula-math">$$E_n(k_x, k_y) = \frac{\hbar^2 \pi^2 n^2}{2 m^* L_z^2} + \frac{\hbar^2 (k_x^2 + k_y^2)}{2 m^*}, \qquad n = 1, 2, 3, \dots$$</div>
          <p style="font-size:9.5pt; margin:4px 0 0 0; color:#334155; line-height:1.75; text-indent:0;"><strong>คำอธิบายตัวแปรและนัยสำคัญ:</strong> ระดับพลังงานของอิเล็กตรอนในบ่อศักย์ 2D</p>
        </div>
            
        <div class="equation-box">
          <div class="equation-header">📌 สมการฟิสิกส์หลัก: สภาพคล่องตัวและความหนาแน่น 2DEG</div>
          <div class="formula-math">$$\mu_e = \frac{e \tau_e}{m^*}, \qquad n_{\text{2D}} = \frac{m^*}{\pi \hbar^2} (E_F - E_1)$$</div>
          <p style="font-size:9.5pt; margin:4px 0 0 0; color:#334155; line-height:1.75; text-indent:0;"><strong>คำอธิบายตัวแปรและนัยสำคัญ:</strong> สภาพคล่องตัวของพาหะและความเข้มข้นอิเล็กตรอน 2DEG</p>
        </div>
              </div>

      <div class="table-block">
        <h3>📊 ตารางเปรียบเทียบพารามิเตอร์โครงสร้างรอยต่อเฮเทอโร AlGaAs/GaAs</h3>
        <table class="data-table">
          <thead><tr>
            <th>พารามิเตอร์</th><th>GaAs (Well)</th><th>Al0.3Ga0.7As (Barrier)</th><th>หน่วย</th></tr></thead>
<tbody><tr><td>ช่องว่างแถบพลังงาน Eg</td><td>1.424</td><td>1.798</td><td>eV</td></tr><tr><td>มวลยังผลอิเล็กตรอน m*</td><td>0.067 m0</td><td>0.092 m0</td><td>kg</td></tr><tr><td>ค่าคงที่ไดอิเล็กทริก εr</td><td>12.9</td><td>12.0</td><td>-</td></tr><tr><td>ความไม่ต่อเนื่องของแถบนำกระแส ΔEc</td><td>0</td><td>0.260</td><td>eV</td></tr><tr><td>สภาพคล่องตัว 2DEG ที่ 4 K</td><td>> 2,000,000</td><td>-</td><td>cm2/V·s</td></tr></tbody></table>
</div>
  <div class="examples-group">

        <div class="example-box">
          <div class="example-header">
            <span>📝 ตัวอย่างการคำนวณที่ 2.1: การคำนวณระดับพลังงาน 3 สถานะแรกในบ่อศักย์ควอนตัม GaAs</span>
            <span style="background:#dcfce7; color:#15803d; font-size:8.5pt; padding:3px 10px; border-radius:4px; font-weight:700;">Step-by-Step Worked Solution</span>
          </div>
          <p style="text-indent:0; margin-bottom:10px;"><strong>โจทย์ปัญหา (Problem Statement):</strong><br>บ่อศักย์ควอนตัม GaAs มีความกว้าง $L_z = 8.0	ext{ nm}$ กำหนดมวลยังผล $m^* = 0.067 m_0$ จงคำนวณหาระดับพลังงาน $E_1, E_2, E_3$ จากก้นบ่อในหน่วย eV (สมมติบ่อศักย์ลึกอนันต์)</p>
          <div style="background:rgba(255,255,255,0.85); border:1px solid #e2e8f0; padding:12px 16px; border-radius:6px; margin:12px 0;">
            <strong style="color:#1e3a8a;">การวิเคราะห์และการคำนวณอย่างละเอียด:</strong><br>
            <p style="text-indent:0; margin:6px 0 0 0; line-height:1.85;">1. คำนวณพลังงานสถานะพื้น $E_1 = \frac{\hbar^2 \pi^2 (1)^2}{2 m^* L_z^2} = \frac{(1.0546 \times 10^{-34})^2 \pi^2}{2(0.067 \times 9.109 \times 10^{-31})(8.0 \times 10^{-9})^2} = 1.404 \times 10^{-20}\text{ J} = 0.0876\text{ eV}$<br>2. $E_2 = E_1 \times 2^2 = 0.0876 \times 4 = 0.3504\text{ eV}$<br>3. $E_3 = E_1 \times 3^2 = 0.0876 \times 9 = 0.7884\text{ eV}$</p>
          </div>
          <div style="background:#f0fdf4; border-left:4px solid #16a34a; padding:10px 14px; margin-top:10px; font-size:9.5pt; color:#166534; border-radius:0 6px 6px 0;">
            💡 <strong>นัยสำคัญทางกายภาพและการประยุกต์ใช้งาน (Physical Insight):</strong><br>
            <span style="color:#14532d;">ช่องว่างพลังงานระหว่าง $E_2$ และ $E_1$ คือ $\Delta E_{21} = 0.2628	ext{ eV}$ สอดคล้องกับการดูดกลืนแสงในย่านอินฟราเรดคลื่นกลาง (Mid-IR)</span>
          </div>
        </div>
            
        <div class="example-box">
          <div class="example-header">
            <span>📝 ตัวอย่างการคำนวณที่ 2.2: การคำนวณความเข้มข้นของพาหะประจุ 2DEG ใน HEMT</span>
            <span style="background:#dcfce7; color:#15803d; font-size:8.5pt; padding:3px 10px; border-radius:4px; font-weight:700;">Step-by-Step Worked Solution</span>
          </div>
          <p style="text-indent:0; margin-bottom:10px;"><strong>โจทย์ปัญหา (Problem Statement):</strong><br>รอยต่อ AlGaAs/GaAs มีระดับเฟอร์มิ $E_F$ อยู่สูงกว่าระดับพลังงานย่อยแรก $E_1$ เป็นระยะ $0.05	ext{ eV}$ ที่อุณหภูมิ $T = 0	ext{ K}$ จงหาความเข้มข้นอิเล็กตรอนต่อหน่วยพื้นที่ $n_{	ext{2D}}$</p>
          <div style="background:rgba(255,255,255,0.85); border:1px solid #e2e8f0; padding:12px 16px; border-radius:6px; margin:12px 0;">
            <strong style="color:#1e3a8a;">การวิเคราะห์และการคำนวณอย่างละเอียด:</strong><br>
            <p style="text-indent:0; margin:6px 0 0 0; line-height:1.85;">$$n_{\text{2D}} = \frac{m^*}{\pi \hbar^2} (E_F - E_1) = \frac{0.067 \times (9.109 \times 10^{-31})}{\pi (1.0546 \times 10^{-34})^2} \times (0.05 \times 1.602 \times 10^{-19}) = 1.40 \times 10^{15}\text{ m}^{-2} = 1.40 \times 10^{11}\text{ cm}^{-2}$$</p>
          </div>
          <div style="background:#f0fdf4; border-left:4px solid #16a34a; padding:10px 14px; margin-top:10px; font-size:9.5pt; color:#166534; border-radius:0 6px 6px 0;">
            💡 <strong>นัยสำคัญทางกายภาพและการประยุกต์ใช้งาน (Physical Insight):</strong><br>
            <span style="color:#14532d;">ความหนาแน่นพาหะระดับ $10^{11}	ext{ cm}^{-2}$ รวมกับสภาพคล่องตัวที่สูงลิ่วทำให้อุปกรณ์ HEMT นำกระแสได้เร็วเป็นพิเศษ</span>
          </div>
        </div>
              </div>
  <div class="code-group">

        <div class="code-box">
          <div class="code-header">💻 แบบจำลองเชิงคำนวณภาษาไพทอน (Computational Python 3.11): กรณีศึกษา: ตัวตรวจจับอินฟราเรดจากบ่อศักย์ควอนตัม (QWIP) ในกล้องถ่ายภาพความร้อนทางทหารและการแพทย์</div>
          <pre><code>เทคโนโลยี QWIP ใช้การเปลี่ยนระดับพลังงานระหว่างแถบย่อย (Intersubband Transition) ในบ่อศักย์ GaAs/AlGaAs ในการตรวจจับความร้อนที่ความยาวคลื่น 8-12 ไมโครเมตร ด้วยความไวสูงและสัญญาณรบกวนต่ำ</code></pre>
        </div>
        <p style="font-size:9.5pt; color:#475569; margin-top:-6px; margin-bottom:18px; text-indent:0;"><em>คำอธิบายอัลกอริทึมการจำลอง:</em> สคริปต์ไพทอนสำหรับการคำนวณและจำลองเชิงตัวเลข</p>
              </div>
  <div class="lab-connection-block">
    <h3>🔬 การเชื่อมโยงสู่ห้องปฏิบัติการเสมือนจริงและเทคนิคการทดลอง (Virtual Lab Connection)</h3>
    <div style='background:#f0fdf4; border:1px solid #bbf7d0; border-left:5px solid #16a34a; padding:12px 16px; margin-bottom:14px; border-radius:6px;'><strong style='color:#166534; font-size:10.5pt;'>การจำลองระดับพลังงานในบ่อศักย์ควอนตัม 2D</strong><p style='margin:6px 0 0 0; color:#14532d; text-indent:0; line-height:1.8;'>quantum_well_levels.py</p></div>
  </div>
  <div class="cases-block">
    <h3>🌐 กรณีศึกษางานวิจัยแนวหน้าและนวัตกรรมอุตสาหกรรม (Frontier Case Studies)</h3>
    <div style='background:#eff6ff; border:1px solid #bfdbfe; border-left:5px solid #2563eb; padding:12px 16px; margin-bottom:14px; border-radius:6px;'><strong style='color:#1e40af; font-size:10.5pt;'>การเชื่อมโยงกับ Virtual Lab 06: การจำลองบ่อศักย์ควอนตัมและแก๊สอิเล็กตรอนสองมิติ</strong><p style='margin:6px 0 0 0; color:#1e3a8a; text-indent:0; line-height:1.8;'>ผู้เรียนสามารถปรับความกว้างบ่อ $L_z$ และสัดส่วนอลูมิเนียมใน AlGaAs ใน Lab 06 เพื่อสังเกตฟังก์ชันคลื่นและการกระจายตัวของ 2DEG</p></div>
  </div>

      <div class="checkpoint-box" style="background:#fefce8; border:1px solid #fef08a; border-left:5px solid #eab308; padding:14px 18px; margin:24px 0 35px 0; border-radius:6px; page-break-inside:avoid;">
        <strong style="color:#854d0e; font-size:10pt;">🎯 จุดตรวจประเมินความเข้าใจและคำถามทบทวนประจำหัวข้อ 2.1 (Concept Checkpoint)</strong>
        <ul style="margin:8px 0 0 0; padding-left:20px; color:#713f12; font-size:9.5pt; line-height:1.8;">
          <li>จงอธิบายแนวคิดรวบยอดหลักของ บ่อศักย์ควอนตัมสองมิติและแก๊สอิเล็กตรอนสองมิติ และความแตกต่างจากพฤติกรรมในระดับมหภาค</li>
          <li>พารามิเตอร์ใดเป็นปัจจัยวิกฤตที่ควบคุมสมบัติทางฟิสิกส์ในหัวข้อนี้ และมีผลกระทบอย่างไร?</li>
          <li>เชื่อมโยงหลักการฟิสิกส์ในหัวข้อนี้เข้ากับการประยุกต์ใช้จริงในเทคโนโลยีสมัยใหม่</li>
        </ul>
      </div>
    </div>
    
    <div class="topic-section">
      <h2>2.2 ลวดควอนตัมและการควอนไทซ์ของสภาพนำไฟฟ้า</h2>
      <div class="topic-en-title">(Quantum Wires & Conductance Quantization)</div>
      
      <div class="topic-intro">
        <p>ลวดควอนตัม (Quantum Wire) หรือจุดสัมผัสควอนตัม (Quantum Point Contact: QPC) คือโครงสร้างที่อิเล็กตรอนถูกกักขังใน 2 ทิศทางเชิงพื้นที่ $(y, z)$ และมีอิสระในการเคลื่อนที่ตามแนวแกนยาว $(x)$ เท่านั้น</p>
    <p>เมื่ออิเล็กตรอนเคลื่อนที่ผ่านจุดสัมผัสควอนตัมที่มีความกว้างเทียบเท่าความยาวคลื่นเฟอร์มิ $\lambda_F$ จำนวนช่องสัญญาณการส่งผ่าน (1D Transport Subbands) จะถูกเปิดออกทีละช่องเมื่อศักย์เกตถูกปรับให้ช่องเปิดกว้างขึ้น</p>
    <p>ปรากฏการณ์นี้นำไปสู่การค้นพบขั้นบันไดสภาพนำไฟฟ้าควอนตัม (Conductance Quantization) ซึ่งสภาพนำไฟฟ้าจะเพิ่มขึ้นเป็นขั้นๆ ละ $G_0 = rac{2e^2}{h} = 77.48	ext{ }\mu	ext{S}$ (หรือความต้านทานลดลงขั้นละ $pprox 12.9	ext{ k}\Omega$) อย่างแม่นยำ ปรากฏการณ์นี้เกิดขึ้นได้แม้ไม่มีสนามแม่เหล็กภายนอก</p>
  </div>

      <div class="subtopic-block">
        <h3>ทฤษฎีการส่งผ่านของแลนเดาเออร์-บึททิเกอร์ (Landauer-Büttiker Formalism)</h3>
            <p>สภาพนำไฟฟ้าของจุดสัมผัสควอนตัมหลายขั้ว: $G_{pq} = rac{2e^2}{h} 	ext{Tr}(T_{pq})$ เมื่อ $T_{pq}$ คือเมทริกซ์การส่งผ่านระหว่างขั้ว $p$ และ $q$</p>
    <p>ที่อุณหภูมิต่ำ การส่งผ่านของแต่ละช่องสัญญาณจะเป็นแบบสมบูรณ์ $T_n 	o 1$ ทำให้เกิดขั้นบันไดสภาพนำไฟฟ้าที่คมชัดเป็นแนวระนาบสมบูรณ์</p>
  </div>

      <div class="subtopic-block">
        <h3>การสร้าง Quantum Point Contact ด้วย Split-Gate</h3>
            <p>การใช้ขั้วเกตโลหะคู่แบบแยก (Split Gate) วางบนผิว 2DEG และจ่ายแรงดันเกตลบ $V_g$ เพื่อผลักอิเล็กตรอนใต้เกตออกไป ก่อให้เกิดช่องแคบนำกระแส 1D ที่ปรับความกว้างได้ด้วยไฟฟ้า</p>
  </div>
  <div class="formula-group">

        <div class="equation-box">
          <div class="equation-header">📌 สมการฟิสิกส์หลัก: ควอนตัมของสภาพนำไฟฟ้า</div>
          <div class="formula-math">$$G = N \times G_0 = N \left( \frac{2e^2}{h} \right) \approx N \times (77.48\text{ }\mu\text{S})$$</div>
          <p style="font-size:9.5pt; margin:4px 0 0 0; color:#334155; line-height:1.75; text-indent:0;"><strong>คำอธิบายตัวแปรและนัยสำคัญ:</strong> สภาพนำไฟฟ้าแบบควอนไทซ์ที่มี N ช่องสัญญาณ</p>
        </div>
            
        <div class="equation-box">
          <div class="equation-header">📌 สมการฟิสิกส์หลัก: ระดับพลังงานย่อยในลวดควอนตัมสี่เหลี่ยม</div>
          <div class="formula-math">$$E(k_x) = \frac{\hbar^2 \pi^2}{2 m^*} \left( \frac{n_y^2}{L_y^2} + \frac{n_z^2}{L_z^2} \right) + \frac{\hbar^2 k_x^2}{2 m^*}$$</div>
          <p style="font-size:9.5pt; margin:4px 0 0 0; color:#334155; line-height:1.75; text-indent:0;"><strong>คำอธิบายตัวแปรและนัยสำคัญ:</strong> พลังงานของอิเล็กตรอนในลวดควอนตัม 1D</p>
        </div>
              </div>

      <div class="table-block">
        <h3>📊 ตารางขั้นบันไดสภาพนำไฟฟ้าควอนตัมและค่าความต้านทาน</h3>
        <table class="data-table">
          <thead><tr>
            <th>จำนวนช่องสัญญาณ N</th><th>สภาพนำไฟฟ้า G (μS)</th><th>สภาพนำไฟฟ้า G (G0)</th><th>ความต้านทาน R (kΩ)</th></tr></thead>
<tbody><tr><td>1</td><td>77.48 μS</td><td>1 G0</td><td>12.906 kΩ</td></tr><tr><td>2</td><td>154.96 μS</td><td>2 G0</td><td>6.453 kΩ</td></tr><tr><td>3</td><td>232.44 μS</td><td>3 G0</td><td>4.302 kΩ</td></tr><tr><td>4</td><td>309.92 μS</td><td>4 G0</td><td>3.227 kΩ</td></tr><tr><td>5</td><td>387.40 μS</td><td>5 G0</td><td>2.581 kΩ</td></tr></tbody></table>
</div>
  <div class="examples-group">

        <div class="example-box">
          <div class="example-header">
            <span>📝 ตัวอย่างการคำนวณที่ 2.3: การคำนวณจำนวนช่องสัญญาณใน Quantum Point Contact</span>
            <span style="background:#dcfce7; color:#15803d; font-size:8.5pt; padding:3px 10px; border-radius:4px; font-weight:700;">Step-by-Step Worked Solution</span>
          </div>
          <p style="text-indent:0; margin-bottom:10px;"><strong>โจทย์ปัญหา (Problem Statement):</strong><br>จุดสัมผัสควอนตัม QPC ถูกสร้างบน GaAs 2DEG มีความกว้าง $W = 45	ext{ nm}$ และความยาวคลื่นเฟอร์มิ $\lambda_F = 30	ext{ nm}$ จงคำนวณหาจำนวนช่องสัญญาณนำกระแส $N$ และสภาพนำไฟฟ้ารวม $G$</p>
          <div style="background:rgba(255,255,255,0.85); border:1px solid #e2e8f0; padding:12px 16px; border-radius:6px; margin:12px 0;">
            <strong style="color:#1e3a8a;">การวิเคราะห์และการคำนวณอย่างละเอียด:</strong><br>
            <p style="text-indent:0; margin:6px 0 0 0; line-height:1.85;">1. $N = \lfloor \frac{2 W}{\lambda_F} \rfloor = \lfloor \frac{2 \times 45}{30} \rfloor = 3\text{ ช่องสัญญาณ}$<br>2. $G = N \times \frac{2e^2}{h} = 3 \times (77.48\text{ }\mu\text{S}) = 232.44\text{ }\mu\text{S}$<br>3. $R = \frac{1}{G} = 4.302\text{ k}\Omega$</p>
          </div>
          <div style="background:#f0fdf4; border-left:4px solid #16a34a; padding:10px 14px; margin-top:10px; font-size:9.5pt; color:#166534; border-radius:0 6px 6px 0;">
            💡 <strong>นัยสำคัญทางกายภาพและการประยุกต์ใช้งาน (Physical Insight):</strong><br>
            <span style="color:#14532d;">เมื่อปรับเกตให้เปิดกว้างขึ้นจน $W = 60	ext{ nm}$ ช่องสัญญาณที่ 4 จะเปิดออก สภาพนำไฟฟ้าจะกระโดดขึ้นสู่ $309.92	ext{ }\mu	ext{S}$</span>
          </div>
        </div>
            
        <div class="example-box">
          <div class="example-header">
            <span>📝 ตัวอย่างการคำนวณที่ 2.4: การคำนวณพลังงานของสถานะย่อยแรกในลวดนาโน InAs</span>
            <span style="background:#dcfce7; color:#15803d; font-size:8.5pt; padding:3px 10px; border-radius:4px; font-weight:700;">Step-by-Step Worked Solution</span>
          </div>
          <p style="text-indent:0; margin-bottom:10px;"><strong>โจทย์ปัญหา (Problem Statement):</strong><br>ลวดนาโน InAs มีพื้นที่หน้าตัดสี่เหลี่ยมจัตุรัส $L_y = L_z = 12	ext{ nm}$ กำหนด $m^* = 0.023 m_0$ จงคำนวณพลังงานขอบแถบสถานะย่อย $(n_y=1, n_z=1)$</p>
          <div style="background:rgba(255,255,255,0.85); border:1px solid #e2e8f0; padding:12px 16px; border-radius:6px; margin:12px 0;">
            <strong style="color:#1e3a8a;">การวิเคราะห์และการคำนวณอย่างละเอียด:</strong><br>
            <p style="text-indent:0; margin:6px 0 0 0; line-height:1.85;">$$E_{1,1} = \frac{\hbar^2 \pi^2}{2 m^*} \left( \frac{1}{L_y^2} + \frac{1}{L_z^2} \right) = \frac{(1.0546 \times 10^{-34})^2 \pi^2 (2)}{2 (0.023 \times 9.109 \times 10^{-31}) (12 \times 10^{-9})^2} = 3.63 \times 10^{-20}\text{ J} = 0.2268\text{ eV}$$</p>
          </div>
          <div style="background:#f0fdf4; border-left:4px solid #16a34a; padding:10px 14px; margin-top:10px; font-size:9.5pt; color:#166534; border-radius:0 6px 6px 0;">
            💡 <strong>นัยสำคัญทางกายภาพและการประยุกต์ใช้งาน (Physical Insight):</strong><br>
            <span style="color:#14532d;">มวลยังผลที่เบามากของ InAs ทำให้พลังงานการกักขังสูงถึง 0.227 eV แม้ขนาดลวดจะใหญ่ถึง 12 nm</span>
          </div>
        </div>
              </div>
  <div class="code-group">

        <div class="code-box">
          <div class="code-header">💻 แบบจำลองเชิงคำนวณภาษาไพทอน (Computational Python 3.11): กรณีศึกษา: การพัฒนาบิตควอนตัมโทโพโลยีจากลวดนาโนสารกึ่งตัวนำ-ตัวนำยิ่งยวด (Majorana Zero Modes)</div>
          <pre><code>การประกบลวดนาโน InAs หรือ InSb เข้ากับชั้นตัวนำยิ่งยวดอะลูมิเนียมภายใต้สนามแม่เหล็ก นำไปสู่การค้นพบอนุภาคเสมือนมาโยรานา (Majorana Bound States) ที่ปลายลวด ซึ่งเป็นหัวใจสำคัญของคอมพิวเตอร์ควอนตัมเชิงโทโพโลยีที่ทนทานต่อสัญญาณรบกวน</code></pre>
        </div>
        <p style="font-size:9.5pt; color:#475569; margin-top:-6px; margin-bottom:18px; text-indent:0;"><em>คำอธิบายอัลกอริทึมการจำลอง:</em> สคริปต์ไพทอนสำหรับการคำนวณและจำลองเชิงตัวเลข</p>
              </div>
  <div class="lab-connection-block">
    <h3>🔬 การเชื่อมโยงสู่ห้องปฏิบัติการเสมือนจริงและเทคนิคการทดลอง (Virtual Lab Connection)</h3>
    <div style='background:#f0fdf4; border:1px solid #bbf7d0; border-left:5px solid #16a34a; padding:12px 16px; margin-bottom:14px; border-radius:6px;'><strong style='color:#166534; font-size:10.5pt;'>การจำลองขั้นบันไดสภาพนำไฟฟ้าควอนตัม</strong><p style='margin:6px 0 0 0; color:#14532d; text-indent:0; line-height:1.8;'>qpc_conductance_steps.py</p></div>
  </div>
  <div class="cases-block">
    <h3>🌐 กรณีศึกษางานวิจัยแนวหน้าและนวัตกรรมอุตสาหกรรม (Frontier Case Studies)</h3>
    <div style='background:#eff6ff; border:1px solid #bfdbfe; border-left:5px solid #2563eb; padding:12px 16px; margin-bottom:14px; border-radius:6px;'><strong style='color:#1e40af; font-size:10.5pt;'>การเชื่อมโยงกับ Virtual Lab 07: การจำลองจุดสัมผัสควอนตัมและขั้นบันไดสภาพนำไฟฟ้า</strong><p style='margin:6px 0 0 0; color:#1e3a8a; text-indent:0; line-height:1.8;'>ผู้เรียนสามารถปรับแรงดัน Split-Gate $V_g$ ใน Lab 07 เพื่อสังเกตการเปิดของช่องสัญญาณนำกระแสและเส้นกราฟขั้นบันได $G/G_0$</p></div>
  </div>

      <div class="checkpoint-box" style="background:#fefce8; border:1px solid #fef08a; border-left:5px solid #eab308; padding:14px 18px; margin:24px 0 35px 0; border-radius:6px; page-break-inside:avoid;">
        <strong style="color:#854d0e; font-size:10pt;">🎯 จุดตรวจประเมินความเข้าใจและคำถามทบทวนประจำหัวข้อ 2.2 (Concept Checkpoint)</strong>
        <ul style="margin:8px 0 0 0; padding-left:20px; color:#713f12; font-size:9.5pt; line-height:1.8;">
          <li>จงอธิบายแนวคิดรวบยอดหลักของ ลวดควอนตัมและการควอนไทซ์ของสภาพนำไฟฟ้า และความแตกต่างจากพฤติกรรมในระดับมหภาค</li>
          <li>พารามิเตอร์ใดเป็นปัจจัยวิกฤตที่ควบคุมสมบัติทางฟิสิกส์ในหัวข้อนี้ และมีผลกระทบอย่างไร?</li>
          <li>เชื่อมโยงหลักการฟิสิกส์ในหัวข้อนี้เข้ากับการประยุกต์ใช้จริงในเทคโนโลยีสมัยใหม่</li>
        </ul>
      </div>
    </div>
    
    <div class="topic-section">
      <h2>2.3 จุดควอนตัมและสเปกตรัมพลังงานคล้ายอะตอม</h2>
      <div class="topic-en-title">(Quantum Dots, Artificial Atoms & Shell Structure)</div>
      
      <div class="topic-intro">
        <p>จุดควอนตัม (Quantum Dot: QD) หรือ 'อะตอมประดิษฐ์' (Artificial Atom) คือโครงสร้างนาโน 0 มิติที่กักขังอิเล็กตรอนและโฮลไว้ในทั้ง 3 มิติเชิงเรขาคณิต $(x, y, z)$ จนทำให้สเปกตรัมพลังงานเป็นระดับไม่ต่อเนื่อง (Discrete Energy Levels) คล้ายคลึงกับระดับพลังงานของอะตอมเดี่ยวในตารางธาตุ</p>
    <p>ระดับพลังงานในจุดควอนตัมสามารถควบคุมได้ด้วยขนาด รูปร่าง และสนามไฟฟ้าภายนอก นอกจากนี้ อิเล็กตรอนในจุดควอนตัมยังเรียงตัวกันเป็นชั้นเปลือกพลังงาน (Shell Structure) สอดคล้องกับกฎของฮุนด์ (Hund's Rules) และหลักการกีดกันของเพาลี เช่นเดียวกับอะตอมจริง ก่อให้เกิด 'ตารางธาตุประดิษฐ์' (Artificial Periodic Table)</p>
    <p>ความสามารถในการปรับแต่งสถานะควอนตัมได้อย่างอิสระ ทำให้จุดควอนตัมเป็นแพลตฟอร์มชั้นนำในการสร้างบิตควอนตัมแบบสปิน (Spin Qubits), แหล่งกำเนิดโฟตอนเดี่ยว (Single-Photon Sources) สำหรับการสื่อสารควอนตัมเข้ารหัส, และเลเซอร์สารกึ่งตัวนำประสิทธิภาพสูง</p>
  </div>

      <div class="figure-card">
        <img src="../assets/images/quantum_dots_3d_photoluminescence.jpg" alt="ภาพเสมือนจริง 3 มิติ: การเปล่งแสงเรืองแสงโฟโตลูมิเนสเซนซ์ของจุดควอนตัมคอลลอยด์ CdSe/ZnS หลากสีตามระดับการกักขังควอนตัมภายใต้แสงกระตุ้นเลเซอร์ยูวี (UV Laser Excitation)">
        <div class="caption"><strong>ภาพที่ 2.3.1</strong>: ภาพเสมือนจริง 3 มิติ: การเปล่งแสงเรืองแสงโฟโตลูมิเนสเซนซ์ของจุดควอนตัมคอลลอยด์ CdSe/ZnS หลากสีตามระดับการกักขังควอนตัมภายใต้แสงกระตุ้นเลเซอร์ยูวี (UV Laser Excitation)</div>
      </div>
            
      <div class="subtopic-block">
        <h3>โครงสร้างเปลือกพลังงานและจำนวนมหัศจรรย์ (Magic Numbers in Quantum Dots)</h3>
            <p>สำหรับจุดควอนตัมที่มีศักย์กักขังแบบพาราโบลาสองมิติ: $V(r) = rac{1}{2} m^* \omega_0^2 r^2$ ระดับพลังงานคือ $E_n = \hbar \omega_0 (n + 1)$ โดยมีความเสื่อมของระดับพลังงานเท่ากับ $n+1$</p>
    <p>เมื่อรวมสปิน $2 	imes$ การเติมเต็มชั้นเปลือกที่สมบูรณ์จะเกิดขึ้นที่จำนวนอิเล็กตรอน $N = 2, 6, 12, 20, 30, 42, \dots$ ซึ่งเรียกว่า 'จำนวนมหัศจรรย์ของอะตอมประดิษฐ์' สอดคล้องกับความเสถียรคล้ายแก๊สมีตระกูล</p>
  </div>

      <div class="subtopic-block">
        <h3>การกักขังสปินและจุดควอนตัมคู่ (Double Quantum Dots)</h3>
            <p>การสร้างจุดควอนตัมคู่ที่ต่อกันแบบอนุกรม (Double QD) ช่วยให้สามารถควบคุมการแลกเปลี่ยนสปิน J(e) ด้วยศักย์ไฟฟ้า นำไปสู่อุปกรณ์ Singlet-Triplet Qubit และ Exchange-Only Qubit สำหรับระบบคำนวณควอนตัม</p>
  </div>
  <div class="formula-group">

        <div class="equation-box">
          <div class="equation-header">📌 สมการฟิสิกส์หลัก: ระดับพลังงานในศักย์กักขังพาราโบลา 2D</div>
          <div class="formula-math">$$E_{n_x, n_y} = \hbar \omega_0 (n_x + n_y + 1), \qquad n = n_x + n_y = 0, 1, 2, \dots$$</div>
          <p style="font-size:9.5pt; margin:4px 0 0 0; color:#334155; line-height:1.75; text-indent:0;"><strong>คำอธิบายตัวแปรและนัยสำคัญ:</strong> ระดับพลังงานของจุดควอนตัมแบบฮาร์มอนิก</p>
        </div>
            
        <div class="equation-box">
          <div class="equation-header">📌 สมการฟิสิกส์หลัก: พลังงานการเติมเต็มอิเล็กตรอน (Addition Energy)</div>
          <div class="formula-math">$$E_{\text{add}}(N) = \mu(N+1) - \mu(N) = E_C + \Delta E_{\text{orbital}}$$</div>
          <p style="font-size:9.5pt; margin:4px 0 0 0; color:#334155; line-height:1.75; text-indent:0;"><strong>คำอธิบายตัวแปรและนัยสำคัญ:</strong> พลังงานที่ต้องใช้ในการเติมอิเล็กตรอนตัวที่ N+1</p>
        </div>
              </div>

      <div class="table-block">
        <h3>📊 ตารางโครงสร้างชั้นเปลือกพลังงานของจุดควอนตัมพาราโบลา 2D</h3>
        <table class="data-table">
          <thead><tr>
            <th>ชั้นเปลือก (Shell)</th><th>ควอนตัมเบอร์ n</th><th>ความเสื่อม (รวมสปิน)</th><th>จำนวนอิเล็กตรอนสะสม (Magic No.)</th><th>การเทียบเคียงอะตอมจริง</th></tr></thead>
<tbody><tr><td>1s</td><td>0</td><td>2</td><td>2 (He)</td><td>ฮีเลียมประดิษฐ์</td></tr><tr><td>1p</td><td>1</td><td>4</td><td>6 (C)</td><td>คาร์บอนประดิษฐ์</td></tr><tr><td>1d + 2s</td><td>2</td><td>6</td><td>12 (Mg)</td><td>แมกนีเซียมประดิษฐ์</td></tr><tr><td>1f + 2p</td><td>3</td><td>8</td><td>20 (Ca)</td><td>แคลเซียมประดิษฐ์</td></tr><tr><td>1g + 2d + 3s</td><td>4</td><td>10</td><td>30 (Zn)</td><td>สังกะสีประดิษฐ์</td></tr></tbody></table>
</div>
  <div class="examples-group">

        <div class="example-box">
          <div class="example-header">
            <span>📝 ตัวอย่างการคำนวณที่ 2.5: การคำนวณพลังงานโฟตอนและช่องว่างแถบพลังงานใน CdSe/ZnS Core-Shell QD</span>
            <span style="background:#dcfce7; color:#15803d; font-size:8.5pt; padding:3px 10px; border-radius:4px; font-weight:700;">Step-by-Step Worked Solution</span>
          </div>
          <p style="text-indent:0; margin-bottom:10px;"><strong>โจทย์ปัญหา (Problem Statement):</strong><br>จุดควอนตัม CdSe/ZnS มีรัศมีแกน $R = 2.2	ext{ nm}$ กำหนด $E_g^{	ext{bulk}} = 1.74	ext{ eV}$, $\mu = 0.10 m_0$, $\epsilon_r = 9.4$ จงคำนวณหาพลังงานการดูดกลืนแสงครั้งแรก $E_{1s-1s}$ และความถี่ของโฟตอน</p>
          <div style="background:rgba(255,255,255,0.85); border:1px solid #e2e8f0; padding:12px 16px; border-radius:6px; margin:12px 0;">
            <strong style="color:#1e3a8a;">การวิเคราะห์และการคำนวณอย่างละเอียด:</strong><br>
            <p style="text-indent:0; margin:6px 0 0 0; line-height:1.85;">1. คำนวณพลังงานกักขัง $\Delta E_{\text{conf}} = \frac{\hbar^2 \pi^2}{2 \mu R^2} = \frac{(1.0546 \times 10^{-34})^2 \pi^2}{2(0.10 \times 9.109 \times 10^{-31})(2.2 \times 10^{-9})^2} = 1.244 \times 10^{-19}\text{ J} = 0.7765\text{ eV}$<br>2. พลังงานคูลอมบ์ $\Delta E_{\text{Coulomb}} = \frac{1.8 e^2}{4\pi \epsilon_0 \epsilon_r R} = 0.1251\text{ eV}$<br>3. $E_{1s-1s} = 1.74 + 0.7765 - 0.1251 = 2.3914\text{ eV}$<br>4. $\nu = \frac{E}{h} = \frac{2.3914 \times 1.602 \times 10^{-19}}{6.626 \times 10^{-34}} = 5.78 \times 10^{14}\text{ Hz}$ ($\lambda = 518.5\text{ nm}$)</p>
          </div>
          <div style="background:#f0fdf4; border-left:4px solid #16a34a; padding:10px 14px; margin-top:10px; font-size:9.5pt; color:#166534; border-radius:0 6px 6px 0;">
            💡 <strong>นัยสำคัญทางกายภาพและการประยุกต์ใช้งาน (Physical Insight):</strong><br>
            <span style="color:#14532d;">แสงสีเขียวมรกตที่มีความบริสุทธิ์สูงมาก เหมาะสำหรับทำเลเซอร์และจอแสดงผลความคมชัดสูง</span>
          </div>
        </div>
            
        <div class="example-box">
          <div class="example-header">
            <span>📝 ตัวอย่างการคำนวณที่ 2.6: การคำนวณ Addition Energy ในจุดควอนตัมแบบอิเล็กโทรสแตติก</span>
            <span style="background:#dcfce7; color:#15803d; font-size:8.5pt; padding:3px 10px; border-radius:4px; font-weight:700;">Step-by-Step Worked Solution</span>
          </div>
          <p style="text-indent:0; margin-bottom:10px;"><strong>โจทย์ปัญหา (Problem Statement):</strong><br>จุดควอนตัมมีค่าความจุไฟฟ้ารวม $C_\Sigma = 1.6	ext{ aF}$ ($1.6 	imes 10^{-18}	ext{ F}$) และระยะห่างระหว่างระดับพลังงานออร์บิทัล $\Delta E_{	ext{orbital}} = 5.0	ext{ meV}$ จงคำนวณ Addition Energy สำหรับการเติมอิเล็กตรอนตัวที่ 3 (เริ่มเปิดเปลือกใหม่ 1p)</p>
          <div style="background:rgba(255,255,255,0.85); border:1px solid #e2e8f0; padding:12px 16px; border-radius:6px; margin:12px 0;">
            <strong style="color:#1e3a8a;">การวิเคราะห์และการคำนวณอย่างละเอียด:</strong><br>
            <p style="text-indent:0; margin:6px 0 0 0; line-height:1.85;">1. พลังงานการประจุ $E_C = \frac{e^2}{C_\Sigma} = \frac{(1.602 \times 10^{-19})^2}{1.6 \times 10^{-18}} = 1.604 \times 10^{-20}\text{ J} = 100.1\text{ meV}$<br>2. $E_{\text{add}}(3) = E_C + \Delta E_{\text{orbital}} = 100.1 + 5.0 = 105.1\text{ meV}$</p>
          </div>
          <div style="background:#f0fdf4; border-left:4px solid #16a34a; padding:10px 14px; margin-top:10px; font-size:9.5pt; color:#166534; border-radius:0 6px 6px 0;">
            💡 <strong>นัยสำคัญทางกายภาพและการประยุกต์ใช้งาน (Physical Insight):</strong><br>
            <span style="color:#14532d;">ค่า Addition Energy ที่สูงกว่า $100	ext{ meV}$ ($> 4 k_B T$ ที่ 300 K) ช่วยให้สามารถสังเกตปรากฏการณ์คูลอมบ์บล็อกเคดได้ที่อุณหภูมิห้อง</span>
          </div>
        </div>
              </div>
  <div class="code-group">

        <div class="code-box">
          <div class="code-header">💻 แบบจำลองเชิงคำนวณภาษาไพทอน (Computational Python 3.11): กรณีศึกษา: ตัวส่งโฟตอนเดี่ยวเชิงควอนตัม (Single-Photon Emitters) สำหรับ Quantum Cryptography</div>
          <pre><code>การกระตุ้นจุดควอนตัมเดี่ยว InAs ในไมโครคาวิตี้เชิงแสงสามารถเปล่งโฟตอนเดี่ยวที่มีค่า $g^{(2)}(0) < 0.01$ ซึ่งป้องกันการดักฟังข้อมูลในระบบเข้ารหัสเชิงควอนตัม (QKD) ได้อย่างสมบูรณ์แบบ</code></pre>
        </div>
        <p style="font-size:9.5pt; color:#475569; margin-top:-6px; margin-bottom:18px; text-indent:0;"><em>คำอธิบายอัลกอริทึมการจำลอง:</em> สคริปต์ไพทอนสำหรับการคำนวณและจำลองเชิงตัวเลข</p>
              </div>
  <div class="lab-connection-block">
    <h3>🔬 การเชื่อมโยงสู่ห้องปฏิบัติการเสมือนจริงและเทคนิคการทดลอง (Virtual Lab Connection)</h3>
    <div style='background:#f0fdf4; border:1px solid #bbf7d0; border-left:5px solid #16a34a; padding:12px 16px; margin-bottom:14px; border-radius:6px;'><strong style='color:#166534; font-size:10.5pt;'>การจำลองระดับพลังงานในอะตอมประดิษฐ์</strong><p style='margin:6px 0 0 0; color:#14532d; text-indent:0; line-height:1.8;'>artificial_atom_sim.py</p></div>
  </div>
  <div class="cases-block">
    <h3>🌐 กรณีศึกษางานวิจัยแนวหน้าและนวัตกรรมอุตสาหกรรม (Frontier Case Studies)</h3>
    <div style='background:#eff6ff; border:1px solid #bfdbfe; border-left:5px solid #2563eb; padding:12px 16px; margin-bottom:14px; border-radius:6px;'><strong style='color:#1e40af; font-size:10.5pt;'>การเชื่อมโยงกับ Virtual Lab 08: การจำลองสเปกโตรสโกปีของจุดควอนตัมและอะตอมประดิษฐ์</strong><p style='margin:6px 0 0 0; color:#1e3a8a; text-indent:0; line-height:1.8;'>ผู้เรียนสามารถควบคุมจำนวนอิเล็กตรอน $N$ ในจุดควอนตัมทีละตัวใน Lab 08 และสังเกตการเกิดชั้นเปลือกพลังงานและการเติมเต็มสปิน</p></div>
  </div>

      <div class="checkpoint-box" style="background:#fefce8; border:1px solid #fef08a; border-left:5px solid #eab308; padding:14px 18px; margin:24px 0 35px 0; border-radius:6px; page-break-inside:avoid;">
        <strong style="color:#854d0e; font-size:10pt;">🎯 จุดตรวจประเมินความเข้าใจและคำถามทบทวนประจำหัวข้อ 2.3 (Concept Checkpoint)</strong>
        <ul style="margin:8px 0 0 0; padding-left:20px; color:#713f12; font-size:9.5pt; line-height:1.8;">
          <li>จงอธิบายแนวคิดรวบยอดหลักของ จุดควอนตัมและสเปกตรัมพลังงานคล้ายอะตอม และความแตกต่างจากพฤติกรรมในระดับมหภาค</li>
          <li>พารามิเตอร์ใดเป็นปัจจัยวิกฤตที่ควบคุมสมบัติทางฟิสิกส์ในหัวข้อนี้ และมีผลกระทบอย่างไร?</li>
          <li>เชื่อมโยงหลักการฟิสิกส์ในหัวข้อนี้เข้ากับการประยุกต์ใช้จริงในเทคโนโลยีสมัยใหม่</li>
        </ul>
      </div>
    </div>
    
    <div class="topic-section">
      <h2>2.4 ปรากฏการณ์ทะลุผ่านเชิงควอนตัมและคูลอมบ์บล็อกเคด</h2>
      <div class="topic-en-title">(Quantum Tunneling & Coulomb Blockade Dynamics)</div>
      
      <div class="topic-intro">
        <p>ปรากฏการณ์ทะลุผ่านเชิงควอนตัม (Quantum Tunneling) เป็นปรากฏการณ์ที่อนุภาคสามารถเคลื่อนที่ทะลุกำแพงศักย์ที่มีความสูงมากกว่าพลังงานจลน์ของอนุภาค ($E < V_0$) ซึ่งเป็นไปไม่ได้ในฟิสิกส์ดั้งเดิม แต่เกิดขึ้นได้เนื่องจากธรรมชาติความเป็นคลื่นของฟังก์ชันคลื่น $\psi(x)$ ที่มีการสลายตัวแบบเอกซ์โพเนนเชียลในชั้นกำแพงศักย์</p>
    <p>เมื่อเชื่อมต่อจุดควอนตัมหรือเกาะนาโนตัวนำเข้ากับขั้วไฟฟ้าผ่านกำแพงทะลุผ่านสองชั้น (Double-Barrier Tunnel Junction) ความจุไฟฟ้าของเกาะ $C_\Sigma$ จะมีขนาดเล็กมากในระดับแอตโตฟารัด ($10^{-18}	ext{ F}$) ส่งผลให้พลังงานการประจุอิเล็กตรอนเพียงตัวเดียว $E_C = rac{e^2}{2 C_\Sigma}$ มีค่าสูงกว่าพลังงานความร้อน $k_B T$</p>
    <p>ผลลัพธ์คือการถ่ายโอนประจุจะถูกระงับอย่างสมบูรณ์หากพลังงานภายนอกไม่เพียงพอ เรียกว่าปรากฏการณ์คูลอมบ์บล็อกเคด (Coulomb Blockade) ซึ่งนำไปสู่การประดิษฐ์ทรานซิสเตอร์อิเล็กตรอนเดี่ยว (Single-Electron Transistor: SET) ที่สามารถตรวจวัดประจุไฟฟ้าได้ละเอียดถึงเศษเสี้ยวของประจุอิเล็กตรอน ($10^{-4} e$)</p>
  </div>

      <div class="subtopic-block">
        <h3>ทฤษฎีการประมาณแบบ WKB สำหรับความน่าจะเป็นในการทะลุผ่าน</h3>
            <p>สัมประสิทธิ์การส่งผ่านทะลุกำแพงศักย์ $V(x)$: $T pprox \exp\left( -2 \int_{x_1}^{x_2} \sqrt{rac{2m^*}{\hbar^2}(V(x) - E)} \, dx ight)$</p>
    <p>สำหรับกำแพงศักย์สี่เหลี่ยมความหนา $d$: $T pprox \exp(-2 \kappa d)$ โดยที่ $\kappa = rac{\sqrt{2m^*(V_0 - E)}}{\hbar}$ ความน่าจะเป็นจะลดลงแบบทวีคูณตามความหนากำแพง</p>
  </div>

      <div class="subtopic-block">
        <h3>ไดอะแกรมความเสถียรคูลอมบ์ (Coulomb Diamonds)</h3>
            <p>เมื่อพล็อตกราฟสภาพนำไฟฟ้าเทียบกับแรงดันเดรน-ซอร์ส $V_{ds}$ และแรงดันเกต $V_g$ จะปรากฏบริเวณที่กระแสเป็นศูนย์รูปทรงสี่เหลี่ยมขนมเปียกปูน เรียกว่า Coulomb Diamonds</p>
    <p>ความสูงของไดมอนด์ตามแนวแกน $V_{ds}$ มีค่าเท่ากับแรงดันการประจุ $V_{	ext{ds}}^{	ext{max}} = rac{e}{C_\Sigma} = rac{2 E_C}{e}$ ซึ่งใช้ในการสกัดค่าความจุไฟฟ้าของอุปกรณ์ได้อย่างแม่นยำ</p>
  </div>
  <div class="formula-group">

        <div class="equation-box">
          <div class="equation-header">📌 สมการฟิสิกส์หลัก: สัมประสิทธิ์การทะลุผ่านของกำแพงศักย์สี่เหลี่ยม</div>
          <div class="formula-math">$$T(E) \approx \exp\left( -2 d \sqrt{\frac{2m^*(V_0 - E)}{\hbar^2}} \right)$$</div>
          <p style="font-size:9.5pt; margin:4px 0 0 0; color:#334155; line-height:1.75; text-indent:0;"><strong>คำอธิบายตัวแปรและนัยสำคัญ:</strong> ความน่าจะเป็นในการทะลุผ่านกำแพงศักย์</p>
        </div>
            
        <div class="equation-box">
          <div class="equation-header">📌 สมการฟิสิกส์หลัก: พลังงานการประจุไฟฟ้าคูลอมบ์</div>
          <div class="formula-math">$$E_C = \frac{e^2}{2 C_\Sigma}, \qquad C_\Sigma = C_s + C_d + C_g$$</div>
          <p style="font-size:9.5pt; margin:4px 0 0 0; color:#334155; line-height:1.75; text-indent:0;"><strong>คำอธิบายตัวแปรและนัยสำคัญ:</strong> พลังงานการประจุและเงื่อนไข Coulomb Blockade: $E_C \gg k_B T$</p>
        </div>
              </div>

      <div class="table-block">
        <h3>📊 ตารางเปรียบเทียบเงื่อนไขการเกิด Coulomb Blockade ที่อุณหภูมิต่างๆ</h3>
        <table class="data-table">
          <thead><tr>
            <th>อุณหภูมิ T</th><th>พลังงานความร้อน kBT (meV)</th><th>ความจุไฟฟ้าสูงสุด CΣ ที่ต้องใช้</th><th>ขนาดเกาะนำกระแสสูงสุด</th></tr></thead>
<tbody><tr><td>300 K (อุณหภูมิห้อง)</td><td>25.85 meV</td><td>< 0.31 aF (3 × 10^-19 F)</td><td>< 1.5 nm</td></tr><tr><td>77 K (ไนโตรเจนเหลว)</td><td>6.63 meV</td><td>< 1.20 aF</td><td>< 5.0 nm</td></tr><tr><td>4.2 K (ฮีเลียมเหลว)</td><td>0.36 meV</td><td>< 22.0 aF</td><td>< 25.0 nm</td></tr><tr><td>0.1 K (ตู้แช่ไดลูชัน)</td><td>0.0086 meV</td><td>< 930.0 aF</td><td>< 200.0 nm</td></tr></tbody></table>
</div>
  <div class="examples-group">

        <div class="example-box">
          <div class="example-header">
            <span>📝 ตัวอย่างการคำนวณที่ 2.7: การคำนวณความน่าจะเป็นในการทะลุผ่านของอิเล็กตรอนผ่านกำแพงออกไซด์ SiO2</span>
            <span style="background:#dcfce7; color:#15803d; font-size:8.5pt; padding:3px 10px; border-radius:4px; font-weight:700;">Step-by-Step Worked Solution</span>
          </div>
          <p style="text-indent:0; margin-bottom:10px;"><strong>โจทย์ปัญหา (Problem Statement):</strong><br>อิเล็กตรอนมีพลังงาน $E = 1.0	ext{ eV}$ ตกกระทบกำแพงศักย์ $	ext{SiO}_2$ สูง $V_0 = 3.2	ext{ eV}$ ความหนา $d = 1.5	ext{ nm}$ กำหนดมวลยังผล $m^* = 0.5 m_0$ จงคำนวณหาสัมประสิทธิ์การทะลุผ่าน $T$</p>
          <div style="background:rgba(255,255,255,0.85); border:1px solid #e2e8f0; padding:12px 16px; border-radius:6px; margin:12px 0;">
            <strong style="color:#1e3a8a;">การวิเคราะห์และการคำนวณอย่างละเอียด:</strong><br>
            <p style="text-indent:0; margin:6px 0 0 0; line-height:1.85;">1. $\Delta V = V_0 - E = 3.2 - 1.0 = 2.2\text{ eV} = 3.524 \times 10^{-19}\text{ J}$<br>2. $\kappa = \frac{\sqrt{2 m^* \Delta V}}{\hbar} = \frac{\sqrt{2(0.5 \times 9.109 \times 10^{-31})(3.524 \times 10^{-19})}}{1.0546 \times 10^{-34}} = 5.371 \times 10^9\text{ m}^{-1}$<br>3. $2 \kappa d = 2 \times (5.371 \times 10^9) \times (1.5 \times 10^{-9}) = 16.113$<br>4. $T \approx e^{-16.113} = 1.005 \times 10^{-7}$</p>
          </div>
          <div style="background:#f0fdf4; border-left:4px solid #16a34a; padding:10px 14px; margin-top:10px; font-size:9.5pt; color:#166534; border-radius:0 6px 6px 0;">
            💡 <strong>นัยสำคัญทางกายภาพและการประยุกต์ใช้งาน (Physical Insight):</strong><br>
            <span style="color:#14532d;">หากเพิ่มความหนาเป็น $d = 3.0	ext{ nm}$ ค่า $T$ จะลดลงเหลือ $1.01 	imes 10^{-14}$ ซึ่งลดลงถึง 7 อันดับขนาด</span>
          </div>
        </div>
            
        <div class="example-box">
          <div class="example-header">
            <span>📝 ตัวอย่างการคำนวณที่ 2.8: การวิเคราะห์พารามิเตอร์ของทรานซิสเตอร์อิเล็กตรอนเดี่ยว (SET)</span>
            <span style="background:#dcfce7; color:#15803d; font-size:8.5pt; padding:3px 10px; border-radius:4px; font-weight:700;">Step-by-Step Worked Solution</span>
          </div>
          <p style="text-indent:0; margin-bottom:10px;"><strong>โจทย์ปัญหา (Problem Statement):</strong><br>ทรานซิสเตอร์ SET มีความจุไฟฟ้ารวม $C_\Sigma = 0.8	ext{ aF}$ จงคำนวณหา (ก) พลังงานการประจุ $E_C$ (ข) อุณหภูมิวิกฤตสูงสุด $T_{	ext{max}}$ เพื่อให้ $E_C \ge 10 k_B T$ (ค) ความกว้างของ Coulomb Diamond บนแกน $V_{ds}$</p>
          <div style="background:rgba(255,255,255,0.85); border:1px solid #e2e8f0; padding:12px 16px; border-radius:6px; margin:12px 0;">
            <strong style="color:#1e3a8a;">การวิเคราะห์และการคำนวณอย่างละเอียด:</strong><br>
            <p style="text-indent:0; margin:6px 0 0 0; line-height:1.85;">1. $E_C = \frac{e^2}{2 C_\Sigma} = \frac{(1.602 \times 10^{-19})^2}{2(0.8 \times 10^{-18})} = 1.604 \times 10^{-20}\text{ J} = 100.1\text{ meV}$<br>2. $T_{\text{max}} = \frac{E_C}{10 k_B} = \frac{1.604 \times 10^{-20}}{10(1.3806 \times 10^{-23})} = 116.2\text{ K}$<br>3. $\Delta V_{ds} = \frac{2 E_C}{e} = \frac{2 \times 0.1001\text{ eV}}{e} = 0.2002\text{ V} = 200.2\text{ mV}$</p>
          </div>
          <div style="background:#f0fdf4; border-left:4px solid #16a34a; padding:10px 14px; margin-top:10px; font-size:9.5pt; color:#166534; border-radius:0 6px 6px 0;">
            💡 <strong>นัยสำคัญทางกายภาพและการประยุกต์ใช้งาน (Physical Insight):</strong><br>
            <span style="color:#14532d;">อุปกรณ์นี้สามารถทำงานได้อย่างเสถียรที่อุณหภูมิไนโตรเจนเหลว (77 K) และแสดงช่องว่างบล็อกเคดกว้างถึง 200 mV</span>
          </div>
        </div>
              </div>
  <div class="code-group">

        <div class="code-box">
          <div class="code-header">💻 แบบจำลองเชิงคำนวณภาษาไพทอน (Computational Python 3.11): กรณีศึกษา: อิเล็กโตรมิเตอร์อิเล็กตรอนเดี่ยว (SET Electrometer) สำหรับการอ่านสถานะคิวบิต</div>
          <pre><code>ความไวในการวัดประจุที่ละเอียดระดับ $10^{-5} e/\sqrt{	ext{Hz}}$ ของ RF-SET ทำให้ถูกนำมาใช้เป็นหัววัดความเร็วสูงในการอ่านค่าสถานะสปินคิวบิตในโปรเซสเซอร์ควอนตัมซิลิคอนของบริษัท Diraq และ UNSW</code></pre>
        </div>
        <p style="font-size:9.5pt; color:#475569; margin-top:-6px; margin-bottom:18px; text-indent:0;"><em>คำอธิบายอัลกอริทึมการจำลอง:</em> สคริปต์ไพทอนสำหรับการคำนวณและจำลองเชิงตัวเลข</p>
              </div>
  <div class="lab-connection-block">
    <h3>🔬 การเชื่อมโยงสู่ห้องปฏิบัติการเสมือนจริงและเทคนิคการทดลอง (Virtual Lab Connection)</h3>
    <div style='background:#f0fdf4; border:1px solid #bbf7d0; border-left:5px solid #16a34a; padding:12px 16px; margin-bottom:14px; border-radius:6px;'><strong style='color:#166534; font-size:10.5pt;'>การจำลอง Coulomb Diamonds ใน Single-Electron Transistor</strong><p style='margin:6px 0 0 0; color:#14532d; text-indent:0; line-height:1.8;'>coulomb_diamonds_sim.py</p></div>
  </div>
  <div class="cases-block">
    <h3>🌐 กรณีศึกษางานวิจัยแนวหน้าและนวัตกรรมอุตสาหกรรม (Frontier Case Studies)</h3>
    <div style='background:#eff6ff; border:1px solid #bfdbfe; border-left:5px solid #2563eb; padding:12px 16px; margin-bottom:14px; border-radius:6px;'><strong style='color:#1e40af; font-size:10.5pt;'>การเชื่อมโยงกับ Virtual Lab 09: การจำลองการทะลุผ่านเชิงควอนตัมและทรานซิสเตอร์อิเล็กตรอนเดี่ยว</strong><p style='margin:6px 0 0 0; color:#1e3a8a; text-indent:0; line-height:1.8;'>ผู้เรียนสามารถปรับค่าความต่างศักย์ $V_g$ และ $V_{ds}$ ใน Lab 09 เพื่อสังเกตปรากฏการณ์ Coulomb Blockade Oscillations และสร้างแผนผัง Coulomb Diamonds</p></div>
  </div>

      <div class="checkpoint-box" style="background:#fefce8; border:1px solid #fef08a; border-left:5px solid #eab308; padding:14px 18px; margin:24px 0 35px 0; border-radius:6px; page-break-inside:avoid;">
        <strong style="color:#854d0e; font-size:10pt;">🎯 จุดตรวจประเมินความเข้าใจและคำถามทบทวนประจำหัวข้อ 2.4 (Concept Checkpoint)</strong>
        <ul style="margin:8px 0 0 0; padding-left:20px; color:#713f12; font-size:9.5pt; line-height:1.8;">
          <li>จงอธิบายแนวคิดรวบยอดหลักของ ปรากฏการณ์ทะลุผ่านเชิงควอนตัมและคูลอมบ์บล็อกเคด และความแตกต่างจากพฤติกรรมในระดับมหภาค</li>
          <li>พารามิเตอร์ใดเป็นปัจจัยวิกฤตที่ควบคุมสมบัติทางฟิสิกส์ในหัวข้อนี้ และมีผลกระทบอย่างไร?</li>
          <li>เชื่อมโยงหลักการฟิสิกส์ในหัวข้อนี้เข้ากับการประยุกต์ใช้จริงในเทคโนโลยีสมัยใหม่</li>
        </ul>
      </div>
    </div>
    
    <div class="topic-section">
      <h2>2.5 ปรากฏการณ์ควอนตัมฮอลล์และโทโพโลยีในวัสดุนาโน</h2>
      <div class="topic-en-title">(Quantum Hall Effect, Topological Insulators & Berry Phase)</div>
      
      <div class="topic-intro">
        <p>เมื่อแก๊สอิเล็กตรอนสองมิติ (2DEG) อยู่ภายใต้สนามแม่เหล็กตั้งฉากความเข้มสูง $B$ ที่อุณหภูมิต่ำ การเคลื่อนที่ของอิเล็กตรอนจะถูกจัดระเบียบเป็นวงโคจรไซโคลตรอน ก่อให้เกิดระดับพลังงานควอนไทซ์ที่ไม่ต่อเนื่องเรียกว่าระดับแลนเดา (Landau Levels: $E_n = \hbar \omega_c (n + rac{1}{2})$)</p>
    <p>ปรากฏการณ์นี้นำไปสู่การค้นพบปรากฏการณ์ควอนตัมฮอลล์จำนวนเต็ม (Integer Quantum Hall Effect - IQHE) โดยเคลาส์ ฟอน คลิทซิง ในปี 1980 ซึ่งความต้านทานฮอลล์จะถูกควอนไทซ์เป็นขั้นระนาบที่แม่นยำอย่างยิ่ง: $R_H = rac{h}{
u e^2}$ โดยที่ $
u$ คือจำนวนเต็ม และความต้านทานตามยาว $R_{xx}$ ลดลงเป็นศูนย์อย่างสมบูรณ์</p>
    <p>การค้นพบนี้ได้เปิดประตูสู่ฟิสิกส์เชิงโทโพโลยี (Topological Physics) ซึ่งสมบัติการนำไฟฟ้าถูกปกป้องด้วยดัชนีโทโพโลยีเชิร์น (Chern Number) ทำให้กระแสไฟฟ้าที่ขอบ (Chiral Edge States) สามารถเคลื่อนที่ได้โดยไม่มีการกระเจิงต้านทาน นำไปสู่ฉนวนโทโพโลยี (Topological Insulators) และวัสดุกึ่งโลหะไวล์ (Weyl Semimetals)</p>
  </div>

      <div class="subtopic-block">
        <h3>โครงสร้างระดับแลนเดาและสถานะนำกระแสที่ขอบ (Chiral Edge Channels)</h3>
            <p>ความถี่ไซโคลตรอน: $\omega_c = rac{eB}{m^*}$ และความเสื่อมของระดับแลนเดาต่อหน่วยพื้นที่: $n_L = rac{eB}{h}$</p>
    <p>ที่ขอบของตัวอย่าง พลังงานศักย์กักขังจะดัดให้ระดับแลนเดาโค้งงอขึ้นตัดกับระดับเฟอร์มิ ก่อให้เกิดช่องสัญญาณนำกระแสทิศทางเดียว (Chiral Edge States) ซึ่งอิเล็กตรอนจะเคลื่อนที่ไปข้างหน้าได้เท่านั้น จึงไม่เกิดการกระเจิงย้อนกลับ (Backscattering-Immune Transport)</p>
  </div>

      <div class="subtopic-block">
        <h3>ปรากฏการณ์ควอนตัมฮอลล์เศษส่วน (FQHE) และคอมโพสิตเฟอร์มิออน</h3>
            <p>ที่สนามแม่เหล็กสูงยิ่งยวด อันตรกิริยาคูลอมบ์ระหว่างอิเล็กตรอนจะเด่นกว่าพลังงานจลน์ ก่อให้เกิดสถานะควอนตัมของไหลใหม่ (Laughlin Liquid) ที่มีควอไซพาร์ติเคิลประจุเป็นเศษส่วน เช่น $e/3, e/5$ ซึ่งมีสถิติการสลับแบบเอนีออน (Anyons) สำหรับ Topological Quantum Computation</p>
  </div>
  <div class="formula-group">

        <div class="equation-box">
          <div class="equation-header">📌 สมการฟิสิกส์หลัก: ความต้านทานควอนตัมฮอลล์และค่าคงที่ฟอนคลิทซิง</div>
          <div class="formula-math">$$R_H = \frac{1}{\nu} \frac{h}{e^2} = \frac{R_K}{\nu}, \qquad R_K = 25,812.80745\dots\text{ }\Omega$$</div>
          <p style="font-size:9.5pt; margin:4px 0 0 0; color:#334155; line-height:1.75; text-indent:0;"><strong>คำอธิบายตัวแปรและนัยสำคัญ:</strong> ความต้านทานฮอลล์และค่าคงที่มาตรฐานความต้านทานสากล</p>
        </div>
            
        <div class="equation-box">
          <div class="equation-header">📌 สมการฟิสิกส์หลัก: ระดับพลังงานแลนเดาและความถี่ไซโคลตรอน</div>
          <div class="formula-math">$$E_n = \hbar \omega_c \left( n + \frac{1}{2} \right), \qquad \omega_c = \frac{eB}{m^*}, \qquad l_B = \sqrt{\frac{\hbar}{eB}}$$</div>
          <p style="font-size:9.5pt; margin:4px 0 0 0; color:#334155; line-height:1.75; text-indent:0;"><strong>คำอธิบายตัวแปรและนัยสำคัญ:</strong> ระดับพลังงานแลนเดาและความยาวแม่เหล็ก</p>
        </div>
              </div>

      <div class="table-block">
        <h3>📊 ตารางขั้นบันไดความต้านทานควอนตัมฮอลล์ตามแฟกเตอร์การเติมเต็ม ν</h3>
        <table class="data-table">
          <thead><tr>
            <th>Filling Factor ν</th><th>ความต้านทานฮอลล์ RH (Ω)</th><th>RH ในหน่วย RK</th><th>การประยุกต์ใช้มาตรฐาน</th></tr></thead>
<tbody><tr><td>1</td><td>25,812.807 Ω</td><td>1.000000 RK</td><td>มาตรฐานปฐมภูมิความต้านทาน</td></tr><tr><td>2</td><td>12,906.404 Ω</td><td>0.500000 RK</td><td>การวัดทางมาตรวิทยา</td></tr><tr><td>3</td><td>8,604.269 Ω</td><td>0.333333 RK</td><td>การสอบเทียบเซมิคอนดักเตอร์</td></tr><tr><td>4</td><td>6,453.202 Ω</td><td>0.250000 RK</td><td>การวัดอุปกรณ์ 2DEG</td></tr><tr><td>1/3 (FQHE)</td><td>77,438.422 Ω</td><td>3.000000 RK</td><td>การศึกษาควาไซพาร์ติเคิลเศษส่วน</td></tr></tbody></table>
</div>
  <div class="examples-group">

        <div class="example-box">
          <div class="example-header">
            <span>📝 ตัวอย่างการคำนวณที่ 2.9: การคำนวณความถี่ไซโคลตรอนและระยะห่างระดับแลนเดาใน GaAs 2DEG</span>
            <span style="background:#dcfce7; color:#15803d; font-size:8.5pt; padding:3px 10px; border-radius:4px; font-weight:700;">Step-by-Step Worked Solution</span>
          </div>
          <p style="text-indent:0; margin-bottom:10px;"><strong>โจทย์ปัญหา (Problem Statement):</strong><br>แก๊สอิเล็กตรอน 2DEG ใน GaAs ($m^* = 0.067 m_0$) อยู่ภายใต้สนามแม่เหล็ก $B = 8.0	ext{ T}$ จงคำนวณหา (ก) ความถี่ไซโคลตรอน $\omega_c$ (ข) ระยะห่างระดับแลนเดา $\Delta E = \hbar \omega_c$ ในหน่วย meV (ค) ความยาวแม่เหล็ก $l_B$</p>
          <div style="background:rgba(255,255,255,0.85); border:1px solid #e2e8f0; padding:12px 16px; border-radius:6px; margin:12px 0;">
            <strong style="color:#1e3a8a;">การวิเคราะห์และการคำนวณอย่างละเอียด:</strong><br>
            <p style="text-indent:0; margin:6px 0 0 0; line-height:1.85;">1. $\omega_c = \frac{eB}{m^*} = \frac{(1.602 \times 10^{-19})(8.0)}{0.067 \times 9.109 \times 10^{-31}} = 2.100 \times 10^{13}\text{ rad/s}$<br>2. $\Delta E = \hbar \omega_c = (1.0546 \times 10^{-34}) \times (2.100 \times 10^{13}) = 2.215 \times 10^{-21}\text{ J} = 13.82\text{ meV}$<br>3. $l_B = \sqrt{\frac{\hbar}{eB}} = \sqrt{\frac{1.0546 \times 10^{-34}}{(1.602 \times 10^{-19})(8.0)}} = 9.07 \times 10^{-9}\text{ m} = 9.07\text{ nm}$</p>
          </div>
          <div style="background:#f0fdf4; border-left:4px solid #16a34a; padding:10px 14px; margin-top:10px; font-size:9.5pt; color:#166534; border-radius:0 6px 6px 0;">
            💡 <strong>นัยสำคัญทางกายภาพและการประยุกต์ใช้งาน (Physical Insight):</strong><br>
            <span style="color:#14532d;">ระยะห่างแลนเดา $13.82	ext{ meV}$ สูงกว่าพลังงานความร้อนที่ $4.2	ext{ K}$ ($0.36	ext{ meV}$) อย่างมาก ทำให้เกิดขั้นบันไดฮอลล์ที่คมชัดสมบูรณ์</span>
          </div>
        </div>
            
        <div class="example-box">
          <div class="example-header">
            <span>📝 ตัวอย่างการคำนวณที่ 2.1: การหา Filling Factor ν และความต้านทานฮอลล์</span>
            <span style="background:#dcfce7; color:#15803d; font-size:8.5pt; padding:3px 10px; border-radius:4px; font-weight:700;">Step-by-Step Worked Solution</span>
          </div>
          <p style="text-indent:0; margin-bottom:10px;"><strong>โจทย์ปัญหา (Problem Statement):</strong><br>แผ่น 2DEG มีความหนาแน่นอิเล็กตรอน $n_{	ext{2D}} = 3.87 	imes 10^{15}	ext{ m}^{-2}$ อยู่ในสนามแม่เหล็ก $B = 4.0	ext{ T}$ จงคำนวณหา Filling Factor $
u$ และค่าความต้านทานฮอลล์ $R_H$</p>
          <div style="background:rgba(255,255,255,0.85); border:1px solid #e2e8f0; padding:12px 16px; border-radius:6px; margin:12px 0;">
            <strong style="color:#1e3a8a;">การวิเคราะห์และการคำนวณอย่างละเอียด:</strong><br>
            <p style="text-indent:0; margin:6px 0 0 0; line-height:1.85;">1. ความจุต่อระดับแลนเดา $n_L = \frac{eB}{h} = \frac{(1.602 \times 10^{-19})(4.0)}{6.626 \times 10^{-34}} = 9.671 \times 10^{14}\text{ m}^{-2}$<br>2. $\nu = \frac{n_{\text{2D}}}{n_L} = \frac{3.87 \times 10^{15}}{9.671 \times 10^{14}} = 4.00$<br>3. $R_H = \frac{h}{4 e^2} = \frac{25812.807}{4} = 6453.20\text{ }\Omega$</p>
          </div>
          <div style="background:#f0fdf4; border-left:4px solid #16a34a; padding:10px 14px; margin-top:10px; font-size:9.5pt; color:#166534; border-radius:0 6px 6px 0;">
            💡 <strong>นัยสำคัญทางกายภาพและการประยุกต์ใช้งาน (Physical Insight):</strong><br>
            <span style="color:#14532d;">ระบบมีการเติมเต็มระดับแลนเดาครบ 4 ระดับพอดี ค่าความต้านทานฮอลล์จึงคงที่อยู่ที่ $6.453	ext{ k}\Omega$ และความต้านทานตามยาว $R_{xx} = 0	ext{ }\Omega$</span>
          </div>
        </div>
              </div>
  <div class="code-group">

        <div class="code-box">
          <div class="code-header">💻 แบบจำลองเชิงคำนวณภาษาไพทอน (Computational Python 3.11): กรณีศึกษา: การนิยามหน่วยมาตรฐานโอห์มสากล (SI Standard Ohm) ด้วยควอนตัมฮอลล์ในกราฟีน</div>
          <pre><code>ตั้งแต่ปี 2019 สถาบันมาตรวิทยาแห่งชาติทั่วโลกได้กำหนดนิยามมาตรฐานความต้านทานไฟฟ้า 1 โอห์ม โดยอ้างอิงจากค่าคงที่ฟอนคลิทซิง $R_K = h/e^2$ ในอุปกรณ์กราฟีนควอนตัมฮอลล์ ซึ่งให้ความแม่นยำสูงกว่า 1 ส่วนในพันล้าน ($10^{-9}$)</code></pre>
        </div>
        <p style="font-size:9.5pt; color:#475569; margin-top:-6px; margin-bottom:18px; text-indent:0;"><em>คำอธิบายอัลกอริทึมการจำลอง:</em> สคริปต์ไพทอนสำหรับการคำนวณและจำลองเชิงตัวเลข</p>
              </div>
  <div class="lab-connection-block">
    <h3>🔬 การเชื่อมโยงสู่ห้องปฏิบัติการเสมือนจริงและเทคนิคการทดลอง (Virtual Lab Connection)</h3>
    <div style='background:#f0fdf4; border:1px solid #bbf7d0; border-left:5px solid #16a34a; padding:12px 16px; margin-bottom:14px; border-radius:6px;'><strong style='color:#166534; font-size:10.5pt;'>การจำลองระดับพลังงานแลนเดาและขั้นบันไดควอนตัมฮอลล์</strong><p style='margin:6px 0 0 0; color:#14532d; text-indent:0; line-height:1.8;'>quantum_hall_sim.py</p></div>
  </div>
  <div class="cases-block">
    <h3>🌐 กรณีศึกษางานวิจัยแนวหน้าและนวัตกรรมอุตสาหกรรม (Frontier Case Studies)</h3>
    <div style='background:#eff6ff; border:1px solid #bfdbfe; border-left:5px solid #2563eb; padding:12px 16px; margin-bottom:14px; border-radius:6px;'><strong style='color:#1e40af; font-size:10.5pt;'>การเชื่อมโยงกับ Virtual Lab 10: การจำลองปรากฏการณ์ควอนตัมฮอลล์และระดับแลนเดา</strong><p style='margin:6px 0 0 0; color:#1e3a8a; text-indent:0; line-height:1.8;'>ผู้เรียนสามารถปรับความเข้มสนามแม่เหล็ก $B$ จาก 0 ถึง 15 เทสลา ใน Lab 10 เพื่อสังเกตการแยกของระดับแลนเดาและวัดขั้นบันได $R_H$ และ $R_{xx}$</p></div>
  </div>

      <div class="checkpoint-box" style="background:#fefce8; border:1px solid #fef08a; border-left:5px solid #eab308; padding:14px 18px; margin:24px 0 35px 0; border-radius:6px; page-break-inside:avoid;">
        <strong style="color:#854d0e; font-size:10pt;">🎯 จุดตรวจประเมินความเข้าใจและคำถามทบทวนประจำหัวข้อ 2.5 (Concept Checkpoint)</strong>
        <ul style="margin:8px 0 0 0; padding-left:20px; color:#713f12; font-size:9.5pt; line-height:1.8;">
          <li>จงอธิบายแนวคิดรวบยอดหลักของ ปรากฏการณ์ควอนตัมฮอลล์และโทโพโลยีในวัสดุนาโน และความแตกต่างจากพฤติกรรมในระดับมหภาค</li>
          <li>พารามิเตอร์ใดเป็นปัจจัยวิกฤตที่ควบคุมสมบัติทางฟิสิกส์ในหัวข้อนี้ และมีผลกระทบอย่างไร?</li>
          <li>เชื่อมโยงหลักการฟิสิกส์ในหัวข้อนี้เข้ากับการประยุกต์ใช้จริงในเทคโนโลยีสมัยใหม่</li>
        </ul>
      </div>
    </div>
    

      <div class="summary-box">
        <h3 style="color:#1e40af; margin-top:0; font-size:13pt;">📋 สรุปสาระสำคัญประจำบทที่ 2 (Chapter 2 Key Takeaways)</h3>
        <ul style="margin:0; padding-left:22px; font-size:10pt; line-height:1.95; color:#1e293b;">
          <li style='margin-bottom:8px;'>บ่อศักย์ควอนตัม 2D กักขังพาหะใน 1 มิติ ก่อให้เกิด 2DEG ที่มีสภาพคล่องตัวสูงมากในอุปกรณ์ HEMT</li><li style='margin-bottom:8px;'>ลวดควอนตัมและจุดสัมผัสควอนตัมแสดงการควอนไทซ์ของสภาพนำไฟฟ้าเป็นขั้นละ $2e^2/h = 77.48	ext{ }\mu	ext{S}$ ตามสูตรของแลนเดาเออร์</li><li style='margin-bottom:8px;'>จุดควอนตัมทำหน้าที่เสมือนอะตอมประดิษฐ์ที่มีโครงสร้างชั้นเปลือกพลังงานและจำนวนมหัศจรรย์สอดคล้องกับกฎของฮุนด์</li><li style='margin-bottom:8px;'>ปรากฏการณ์ทะลุผ่านเชิงควอนตัมและคูลอมบ์บล็อกเคดเกิดขึ้นเมื่อพลังงานการประจุ $E_C = e^2/2C_\Sigma \gg k_B T$ นำไปสู่ทรานซิสเตอร์อิเล็กตรอนเดี่ยว (SET)</li><li style='margin-bottom:8px;'>ปรากฏการณ์ควอนตัมฮอลล์เกิดขึ้นเมื่อ 2DEG อยู่ในสนามแม่เหล็กสูง ทำให้ความต้านทานฮอลล์ถูกควอนไทซ์เป็น $h/
u e^2$ ด้วยความแม่นยำทางมาตรวิทยาระดับสากล</li>
        </ul>
      </div>

      <div class="problems-section">
        <h3 style="color:#0f172a; margin-top:0; font-size:14pt; border-bottom:2px solid #cbd5e1; padding-bottom:8px;">
          📚 แบบฝึกหัดและโจทย์ปัญหาท้ายบทที่ 2 (End-of-Chapter Problems)
        </h3>
        
        <h4 style="color:#1e3a8a; font-size:11.5pt; margin-top:18px;">ตอนที่ 1: คำถามเชิงมโนทัศน์และการวิเคราะห์เชิงฟิสิกส์ (Conceptual & Analytical Questions)</h4>
        <ol style="padding-left:22px; font-size:10pt; line-height:1.9; color:#334155;">
          <li style='margin-bottom:8px;'>จงอธิบายกลไกที่ทำให้ 2DEG ในโครงสร้าง Modulation-Doped AlGaAs/GaAs มีสภาพคล่องตัวสูงกว่าในบัลค์ GaAs</li><li style='margin-bottom:8px;'>เพราะเหตุใดสภาพนำไฟฟ้าในจุดสัมผัสควอนตัมจึงเพิ่มขึ้นเป็นขั้นๆ ละ 2e^2/h?</li><li style='margin-bottom:8px;'>จงเปรียบเทียบความเหมือนและความแตกต่างระหว่างจุดควอนตัม (QD) กับอะตอมจริงในตารางธาตุ</li><li style='margin-bottom:8px;'>จงอธิบายเงื่อนไขทางฟิสิกส์ 2 ประการที่จำเป็นต่อการสังเกตปรากฏการณ์คูลอมบ์บล็อกเคด</li><li style='margin-bottom:8px;'>ระดับแลนเดา (Landau Levels) คืออะไร และเกิดขึ้นได้อย่างไรภายใต้สนามแม่เหล็ก?</li><li style='margin-bottom:8px;'>จงอธิบายความหมายของ Chiral Edge States ในปรากฏการณ์ควอนตัมฮอลล์ และเหตุใดจึงไม่มีการกระเจิงย้อนกลับ</li><li style='margin-bottom:8px;'>Coulomb Diamonds ในทรานซิสเตอร์อิเล็กตรอนเดี่ยวบอกข้อมูลทางกายภาพใดของอุปกรณ์บ้าง?</li><li style='margin-bottom:8px;'>เพราะเหตุใดกราฟีนจึงสามารถแสดงปรากฏการณ์ควอนตัมฮอลล์ได้แม้ที่อุณหภูมิห้อง?</li>
        </ol>

        <h4 style="color:#166534; font-size:11.5pt; margin-top:22px;">ตอนที่ 2: โจทย์ปัญหาการคำนวณเชิงตัวเลขและการพิสูจน์ (Quantitative & Numerical Problems)</h4>
        <ol style="padding-left:22px; font-size:10pt; line-height:1.9; color:#334155;">
          <li style='margin-bottom:8px;'>บ่อศักย์ควอนตัม GaAs กว้าง 6.0 nm จงคำนวณหาพลังงานสถานะพื้น $E_1$ และความยาวคลื่นโฟตอนที่เปล่งจากการเปลี่ยนสถานะ $E_2 	o E_1$</li><li style='margin-bottom:8px;'>จุดสัมผัสควอนตัม QPC มี 4 ช่องสัญญาณเปิดอยู่ จงคำนวณสภาพนำไฟฟ้ารวมและความต้านทานไฟฟ้า</li><li style='margin-bottom:8px;'>คำนวณ Addition Energy ของจุดควอนตัมที่มี $C_\Sigma = 1.2	ext{ aF}$ และ $\Delta E_{	ext{orbital}} = 8.0	ext{ meV}$ สำหรับการเติมอิเล็กตรอนตัวที่ 3</li><li style='margin-bottom:8px;'>อิเล็กตรอนพลังงาน 1.5 eV ชนกำแพงศักย์สูง 3.0 eV หนา 1.2 nm จงคำนวณสัมประสิทธิ์การทะลุผ่าน $T$ กำหนด $m^* = m_0$</li><li style='margin-bottom:8px;'>คำนวณค่าสนามแม่เหล็ก $B$ ที่ต้องใช้เพื่อให้ Filling Factor $
u = 2$ ใน 2DEG ที่มีความหนาแน่น $n_{	ext{2D}} = 2.5 	imes 10^{15}	ext{ m}^{-2}$</li><li style='margin-bottom:8px;'>คำนวณความจุไฟฟ้ารวมสูงสุด $C_\Sigma$ ของอุปกรณ์ SET เพื่อให้สามารถทำงานได้ที่อุณหภูมิห้อง (300 K) โดยมี $E_C \ge 5 k_B T$</li><li style='margin-bottom:8px;'>จงคำนวณความถี่ไซโคลตรอน $\omega_c$ และรัศมีแม่เหล็ก $l_B$ ของอิเล็กตรอนใน InSb ($m^* = 0.014 m_0$) ที่สนามแม่เหล็ก 5.0 T</li>
        </ol>

        <h4 style="color:#7c2d12; font-size:11.5pt; margin-top:22px;">ตอนที่ 3: โจทย์ประยุกต์ การออกแบบเชิงวิศวกรรม และการจำลอง (Applied Design & Modeling Problems)</h4>
        <ol style="padding-left:22px; font-size:10pt; line-height:1.9; color:#334155;">
          <li style='margin-bottom:8px;'>จงออกแบบสถาปัตยกรรมทรานซิสเตอร์ Single-Electron Transistor (SET) ที่สามารถทำงานได้ที่อุณหภูมิห้อง</li><li style='margin-bottom:8px;'>ออกแบบระบบตัวตรวจจับคลื่นอินฟราเรดย่านไกล (QWIP) ความยาวคลื่น 10 ไมโครเมตร โดยใช้บ่อศักย์ AlGaAs/GaAs</li><li style='margin-bottom:8px;'>วิเคราะห์แนวทางการนำปรากฏการณ์ Majorana Zero Modes ในลวดนาโนมาใช้สร้าง Fault-Tolerant Quantum Computer</li><li style='margin-bottom:8px;'>เขียนโค้ด Python เพื่อคำนวณและพล็อตระดับแลนเดาเทียบกับความเข้มสนามแม่เหล็ก (Landau Fan Diagram)</li>
        </ol>
      </div>
    </div>
    """
