# -*- coding: utf-8 -*-
"""
Chapter 6: นาโนอิเล็กทรอนิกส์ สปินทรอนิกส์ และนาโนโฟโทนิกส์
Nanoelectronics, Spintronics, STT-MRAM, Plasmonics, SERS Metrology & Metamaterials
"""

def get_chapter_6():
    return r"""
    <div class="chapter-container">
      <div class="chapter-hero">
        <div class="chapter-badge">CHAPTER 06 • NANOTECHNOLOGICAL PHYSICS</div>
        <h1 class="chapter-title">นาโนอิเล็กทรอนิกส์ สปินทรอนิกส์ และนาโนโฟโทนิกส์</h1>
        <p class="chapter-subtitle">Nanoelectronics, Spintronics, STT-MRAM, Plasmonics, SERS Metrology & Metamaterials</p>
      </div>

      <div class="diagram-wrap">
        <img src="../assets/diagrams/ch06_nanoelectronics.svg" alt="นาโนอิเล็กทรอนิกส์ สปินทรอนิกส์ และนาโนโฟโทนิกส์">
        <div class="caption">ภาพที่ 6.1 แผนผังวิวัฒนาการสถาปัตยกรรม GAAFET, กลไก TMR/STT-MRAM, การสั่นพลาสมอนิกส์ LSPR/Hot-Spots และ Flat Metalens</div>
      </div>

      
    <div class="topic-section">
      <h2>6.1 ทรานซิสเตอร์สนามไฟฟ้าจากโครงสร้างนาโนและ FinFET ยุคใหม่</h2>
      <div class="topic-en-title">(Nanoscale Field-Effect Transistors: CNT-FETs, FinFETs & Gate-All-Around (GAAFETs))</div>
      
      <div class="topic-intro">
        <p>การย่อขนาดทรานซิสเตอร์ซิลิคอนตามกฎของมัวร์ (Moore's Law) กำลังเผชิญหน้ากับขีดจำกัดทางกายภาพขั้นวิกฤต เช่น ผลกระทบช่องนำกระแสสั้น (Short-Channel Effects: SCEs), การลดลงของความสูงกำแพงศักย์เหนี่ยวนำด้วยเดรน (Drain-Induced Barrier Lowering: DIBL), และกระแสไฟฟ้ารั่วไหลจากการทะลุผ่านเชิงควอนตัมผ่านชั้นฉนวนเกต (Quantum Gate Leakage)</p>
    <p>เพื่อก้าวข้ามขีดจำกัดนี้ อุตสาหกรรมเซมิคอนดักเตอร์ได้วิวัฒนาการสถาปัตยกรรม 3 มิติอย่างต่อเนื่อง จากโครงสร้างระนาบดั้งเดิมสู่ FinFET (เกตโอบล้อม 3 ด้าน) และสู่สถาปัตยกรรมขั้นสูงสุดในปัจจุบันคือ Gate-All-Around (GAAFET) หรือ Nanosheet FETs ซึ่งเกตโลหะจะโอบล้อมรอบแผ่นช่องนำกระแสนาโน 2D/1D ครบทั้ง 4 ด้าน (Gate Wraparound) อย่างสมบูรณ์ ทำให้สามารถควบคุมสนามไฟฟ้าสถิตได้อย่างสมบูรณ์แบบ</p>
    <p>ในระดับฟิสิกส์วัสดุขั้นสูง ทรานซิสเตอร์ท่อคาร์บอนนาโน (CNT-FETs) และทรานซิสเตอร์วัสดุสองมิติ ($	ext{MoS}_2	ext{-FETs}$) เป็นผู้ท้าชิงอันดับหนึ่งสำหรับยุค Sub-1nm เนื่องจากความหนาของช่องนำกระแสที่บางเฉียบระดับโมเลกุล ช่วยป้องกันการรั่วไหลของประจุและให้อัตราการนำกระแสแบบบอลลิสติก (Ballistic Transport) สูงสุด</p>
  </div>

      <div class="figure-card">
        <img src="../assets/images/spintronics_gaafet_nanodevice_3d.jpg" alt="ภาพเสมือนจริง 3 มิติ: สถาปัตยกรรมทรานซิสเตอร์นาโนชีต GAAFET ระดับต่ำกว่า 2 นาโนเมตร และสแต็กหัวต่ออุโมงค์แม่เหล็ก STT-MRAM ในโรงงานเซมิคอนดักเตอร์ขั้นสูง">
        <div class="caption"><strong>ภาพที่ 6.1.1</strong>: ภาพเสมือนจริง 3 มิติ: สถาปัตยกรรมทรานซิสเตอร์นาโนชีต GAAFET ระดับต่ำกว่า 2 นาโนเมตร และสแต็กหัวต่ออุโมงค์แม่เหล็ก STT-MRAM ในโรงงานเซมิคอนดักเตอร์ขั้นสูง</div>
      </div>
            
      <div class="subtopic-block">
        <h3>ฟิสิกส์การควบคุมไฟฟ้าสถิตและความยาวสเกลธรรมชาติ (Natural Scaling Length)</h3>
            <p>ความยาวสเกลธรรมชาติสำหรับโครงสร้างระนาบ: $\lambda = \sqrt{rac{\epsilon_{	ext{ch}}}{\epsilon_{	ext{ox}}} t_{	ext{ch}} t_{	ext{ox}}}$</p>
    <p>สำหรับโครงสร้าง Gate-All-Around ทรงกระบอก: $\lambda_{	ext{GAA}} = \sqrt{rac{2 \epsilon_{	ext{ch}} d^2 \ln(1 + 2t_{	ext{ox}}/d) + \epsilon_{	ext{ox}} d^2}{8 \epsilon_{	ext{ox}}}}$</p>
    <p>เพื่อป้องกันผลกระทบช่องสั้นอย่างมีประสิทธิภาพ ความยาวเกตจะต้องยาวกว่าสเกลธรรมชาติอย่างน้อย 4 ถึง 6 เท่า ($L_g \ge 4-6 \lambda$) ซึ่งโครงสร้าง GAA ช่วยลดค่า $\lambda$ ลงได้ต่ำกว่า $1.5	ext{ nm}$</p>
  </div>

      <div class="subtopic-block">
        <h3>วิวัฒนาการ Subthreshold Swing และขีดจำกัด Boltzmann Tyranny</h3>
            <p>ค่าความชันใต้ขีดเริ่ม (Subthreshold Swing: SS) สำหรับ MOSFET ดั้งเดิมถูกจำกัดด้วยพลังงานความร้อนตามสถิติของโบลต์ซมันน์: $	ext{SS} = \ln(10) rac{k_B T}{e} \left(1 + rac{C_{	ext{dep}}}{C_{	ext{ox}}}ight) \ge 60	ext{ mV/decade}$ ที่ 300 K</p>
    <p>การก้าวข้ามขีดจำกัดนี้จำเป็นต้องใช้ฟิสิกส์ใหม่ เช่น การทะลุผ่านของแถบพลังงานใน Tunneling FETs (TFETs) หรือผลความจุลบใน Negative Capacitance FETs (NC-FETs) ที่ใช้ชั้นฉนวนเฟอร์โรอิเล็กทริก $	ext{Hf}_{1-x}	ext{Zr}_x	ext{O}_2$</p>
  </div>
  <div class="formula-group">

        <div class="equation-box">
          <div class="equation-header">📌 สมการฟิสิกส์หลัก: ความยาวสเกลธรรมชาติของ GAAFET</div>
          <div class="formula-math">$$\lambda_{\text{GAA}} \approx \sqrt{\frac{\epsilon_{\text{ch}} d_{\text{nw}}^2}{8 \epsilon_{\text{ox}}} \ln\left(1 + \frac{2 t_{\text{ox}}}{d_{\text{nw}}}\right)}, \qquad L_g \ge 4.5 \lambda$$</div>
          <p style="font-size:9.5pt; margin:4px 0 0 0; color:#334155; line-height:1.75; text-indent:0;"><strong>คำอธิบายตัวแปรและนัยสำคัญ:</strong> เกณฑ์การย่อขนาดเกตเพื่อป้องกัน Short-Channel Effects</p>
        </div>
            
        <div class="equation-box">
          <div class="equation-header">📌 สมการฟิสิกส์หลัก: ค่า Subthreshold Swing ที่ขีดจำกัดอุณหภูมิห้อง</div>
          <div class="formula-math">$$\text{SS}_{\text{limit}} = \ln(10) \frac{k_B T}{e} \approx 59.6\text{ mV/decade} \quad (\text{ที่ } T = 300\text{ K})$$</div>
          <p style="font-size:9.5pt; margin:4px 0 0 0; color:#334155; line-height:1.75; text-indent:0;"><strong>คำอธิบายตัวแปรและนัยสำคัญ:</strong> ขีดจำกัด Boltzmann Tyranny สำหรับสวิตช์อิเล็กทรอนิกส์</p>
        </div>
              </div>

      <div class="table-block">
        <h3>📊 ตารางวิวัฒนาการสถาปัตยกรรมทรานซิสเตอร์จาก 28 nm สู่ 1.4 nm</h3>
        <table class="data-table">
          <thead><tr>
            <th>ยุคสมัย/โหนด</th><th>สถาปัตยกรรม</th><th>การควบคุมเกต</th><th>วัสดุช่องนำกระแส</th><th>ค่า SS (mV/dec)</th></tr></thead>
<tbody><tr><td>28 nm / 22 nm</td><td>Planar MOSFET</td><td>เกตระนาบ 1 ด้าน</td><td>บัลค์ซิลิคอน (Si)</td><td>85 - 100</td></tr><tr><td>14 nm / 7 nm / 5 nm</td><td>FinFET 3D</td><td>เกต 3 ด้านรอบครีบ</td><td>Si / SiGe</td><td>68 - 75</td></tr><tr><td>3 nm / 2 nm (ปัจจุบัน)</td><td>GAAFET (Nanosheet)</td><td>เกตโอบล้อม 4 ด้าน</td><td>Si Nanosheets ซ้อน 3-4 ชั้น</td><td>62 - 65</td></tr><tr><td>1.4 nm / 1 nm (A14/A10)</td><td>CFET (Complementary FET)</td><td>GAA n-FET ซ้อนบน p-FET 3D</td><td>Si / Ge Nanowires</td><td>61 - 63</td></tr><tr><td>Sub-1 nm (อนาคต)</td><td>2D TMD / CNT-FET</td><td>GAA รอบท่อ/แผ่น 2D</td><td>MoS2, WS2, SWCNTs</td><td>< 60 (NC-FETs)</td></tr></tbody></table>
</div>
  <div class="examples-group">

        <div class="example-box">
          <div class="example-header">
            <span>📝 ตัวอย่างการคำนวณที่ 6.1: การคำนวณความยาวเกตขั้นต่ำของ Nanosheet GAAFET</span>
            <span style="background:#dcfce7; color:#15803d; font-size:8.5pt; padding:3px 10px; border-radius:4px; font-weight:700;">Step-by-Step Worked Solution</span>
          </div>
          <p style="text-indent:0; margin-bottom:10px;"><strong>โจทย์ปัญหา (Problem Statement):</strong><br>โครงสร้าง GAAFET ใช้แผ่นนาโนซิลิคอนหนา $t_{	ext{ch}} = 5.0	ext{ nm}$ ($\epsilon_{	ext{ch}} = 11.7$) เคลือบด้วยชั้นฉนวน $	ext{HfO}_2$ หนา $t_{	ext{ox}} = 2.0	ext{ nm}$ ($\epsilon_{	ext{ox}} = 20.0$) กำหนดให้ความยาวสเกลธรรมชาติประมาณ $\lambda pprox \sqrt{rac{\epsilon_{	ext{ch}}}{\epsilon_{	ext{ox}}} rac{t_{	ext{ch}} t_{	ext{ox}}}{2}}$ จงคำนวณหา $\lambda$ และความยาวเกตขั้นต่ำ $L_g^{	ext{min}} = 4.5 \lambda$</p>
          <div style="background:rgba(255,255,255,0.85); border:1px solid #e2e8f0; padding:12px 16px; border-radius:6px; margin:12px 0;">
            <strong style="color:#1e3a8a;">การวิเคราะห์และการคำนวณอย่างละเอียด:</strong><br>
            <p style="text-indent:0; margin:6px 0 0 0; line-height:1.85;">1. คำนวณ $\lambda = \sqrt{\frac{11.7}{20.0} \times \frac{(5.0\text{ nm})(2.0\text{ nm})}{2}} = \sqrt{0.585 \times 5.0} = \sqrt{2.925} = 1.710\text{ nm}$<br>2. ความยาวเกตขั้นต่ำ $L_g^{\text{min}} = 4.5 \times 1.710\text{ nm} = 7.70\text{ nm}$</p>
          </div>
          <div style="background:#f0fdf4; border-left:4px solid #16a34a; padding:10px 14px; margin-top:10px; font-size:9.5pt; color:#166534; border-radius:0 6px 6px 0;">
            💡 <strong>นัยสำคัญทางกายภาพและการประยุกต์ใช้งาน (Physical Insight):</strong><br>
            <span style="color:#14532d;">โครงสร้าง GAA ช่วยให้สามารถย่อความยาวเกตลงเหลือเพียง $7.7	ext{ nm}$ โดยไม่เกิดปัญหาการรั่วไหลของกระแส</span>
          </div>
        </div>
            
        <div class="example-box">
          <div class="example-header">
            <span>📝 ตัวอย่างการคำนวณที่ 6.2: การคำนวณพลังงานการสลับสถานะ (Switching Energy) ของวงจรลอจิกเกต</span>
            <span style="background:#dcfce7; color:#15803d; font-size:8.5pt; padding:3px 10px; border-radius:4px; font-weight:700;">Step-by-Step Worked Solution</span>
          </div>
          <p style="text-indent:0; margin-bottom:10px;"><strong>โจทย์ปัญหา (Problem Statement):</strong><br>ทรานซิสเตอร์นาโนทำงานที่แรงดันจ่าย $V_{dd} = 0.70	ext{ V}$ มีค่าความจุไฟฟ้าเกตรวม $C_g = 0.50	ext{ fF}$ ($0.5 	imes 10^{-15}	ext{ F}$) จงคำนวณหาพลังงานที่ใช้ในการสลับสถานะ $1 	o 0 	o 1$ หนึ่งรอบ ($E_{	ext{switch}} = C_g V_{dd}^2$) และกำลังไฟฟ้าสูญเสียที่ความถี่ $f = 4.0	ext{ GHz}$</p>
          <div style="background:rgba(255,255,255,0.85); border:1px solid #e2e8f0; padding:12px 16px; border-radius:6px; margin:12px 0;">
            <strong style="color:#1e3a8a;">การวิเคราะห์และการคำนวณอย่างละเอียด:</strong><br>
            <p style="text-indent:0; margin:6px 0 0 0; line-height:1.85;">1. $E_{\text{switch}} = C_g V_{dd}^2 = (0.50 \times 10^{-15}\text{ F}) \times (0.70\text{ V})^2 = 2.45 \times 10^{-16}\text{ J} = 0.245\text{ fJ}$ (หรือ $1.53\text{ keV}$)<br>2. กำลังไฟฟ้าแบบไดนามิก $P_{\text{dyn}} = C_g V_{dd}^2 f = (2.45 \times 10^{-16}\text{ J}) \times (4.0 \times 10^9\text{ s}^{-1}) = 9.80 \times 10^{-7}\text{ W} = 0.98\text{ }\mu\text{W}$ ต่อเกต</p>
          </div>
          <div style="background:#f0fdf4; border-left:4px solid #16a34a; padding:10px 14px; margin-top:10px; font-size:9.5pt; color:#166534; border-radius:0 6px 6px 0;">
            💡 <strong>นัยสำคัญทางกายภาพและการประยุกต์ใช้งาน (Physical Insight):</strong><br>
            <span style="color:#14532d;">สำหรับชิปที่มีทรานซิสเตอร์ 5 หมื่นล้านตัว การควบคุม $V_{dd}$ ให้อยู่ในระดับต่ำและลด $C_g$ จึงเป็นสิ่งจำเป็นอย่างยิ่งเพื่อไม่ให้ชิปเกิดความร้อนสูงเกิน</span>
          </div>
        </div>
              </div>
  <div class="code-group">

        <div class="code-box">
          <div class="code-header">💻 แบบจำลองเชิงคำนวณภาษาไพทอน (Computational Python 3.11): กรณีศึกษา: สถาปัตยกรรมทรานซิสเตอร์ 2 นาโนเมตร Gate-All-Around (TSMC N2 และ Intel RibbonFET)</div>
          <pre><code>การเปิดตัวชิปสถาปัตยกรรม 2 นาโนเมตรที่ใช้ Nanosheet GAAFET ซ้อนกัน 4 ชั้นในแนวดิ่ง ร่วมกับระบบส่งกำลังไฟฟ้าด้านหลังแผ่นเวเฟอร์ (Backside Power Delivery Network - PowerVia) ช่วยเพิ่มประสิทธิภาพการประมวลผลขึ้น 15% และลดการใช้พลังงานลง 30%</code></pre>
        </div>
        <p style="font-size:9.5pt; color:#475569; margin-top:-6px; margin-bottom:18px; text-indent:0;"><em>คำอธิบายอัลกอริทึมการจำลอง:</em> สคริปต์ไพทอนสำหรับการคำนวณและจำลองเชิงตัวเลข</p>
              </div>
  <div class="lab-connection-block">
    <h3>🔬 การเชื่อมโยงสู่ห้องปฏิบัติการเสมือนจริงและเทคนิคการทดลอง (Virtual Lab Connection)</h3>
    <div style='background:#f0fdf4; border:1px solid #bbf7d0; border-left:5px solid #16a34a; padding:12px 16px; margin-bottom:14px; border-radius:6px;'><strong style='color:#166534; font-size:10.5pt;'>การจำลองเส้นโค้ง I-V และ Subthreshold Characteristic ของ GAAFET</strong><p style='margin:6px 0 0 0; color:#14532d; text-indent:0; line-height:1.8;'>gaafet_iv_sim.py</p></div>
  </div>
  <div class="cases-block">
    <h3>🌐 กรณีศึกษางานวิจัยแนวหน้าและนวัตกรรมอุตสาหกรรม (Frontier Case Studies)</h3>
    <div style='background:#eff6ff; border:1px solid #bfdbfe; border-left:5px solid #2563eb; padding:12px 16px; margin-bottom:14px; border-radius:6px;'><strong style='color:#1e40af; font-size:10.5pt;'>การเชื่อมโยงกับ Virtual Lab 26: การจำลองทรานซิสเตอร์ FinFET และ Gate-All-Around (GAAFET)</strong><p style='margin:6px 0 0 0; color:#1e3a8a; text-indent:0; line-height:1.8;'>ผู้เรียนสามารถควบคุมขนาดหน้าตัด Nanosheet, ปรับความหนาชั้น High-k Oxide และจำลองกราฟ $I_d - V_g$ พร้อมวิเคราะห์ค่า DIBL และ Subthreshold Swing ใน Lab 26</p></div>
  </div>

      <div class="checkpoint-box" style="background:#fefce8; border:1px solid #fef08a; border-left:5px solid #eab308; padding:14px 18px; margin:24px 0 35px 0; border-radius:6px; page-break-inside:avoid;">
        <strong style="color:#854d0e; font-size:10pt;">🎯 จุดตรวจประเมินความเข้าใจและคำถามทบทวนประจำหัวข้อ 6.1 (Concept Checkpoint)</strong>
        <ul style="margin:8px 0 0 0; padding-left:20px; color:#713f12; font-size:9.5pt; line-height:1.8;">
          <li>จงอธิบายแนวคิดรวบยอดหลักของ ทรานซิสเตอร์สนามไฟฟ้าจากโครงสร้างนาโนและ FinFET ยุคใหม่ และความแตกต่างจากพฤติกรรมในระดับมหภาค</li>
          <li>พารามิเตอร์ใดเป็นปัจจัยวิกฤตที่ควบคุมสมบัติทางฟิสิกส์ในหัวข้อนี้ และมีผลกระทบอย่างไร?</li>
          <li>เชื่อมโยงหลักการฟิสิกส์ในหัวข้อนี้เข้ากับการประยุกต์ใช้จริงในเทคโนโลยีสมัยใหม่</li>
        </ul>
      </div>
    </div>
    
    <div class="topic-section">
      <h2>6.2 สปินทรอนิกส์: GMR, TMR และหน่วยความจำ STT-MRAM</h2>
      <div class="topic-en-title">(Spintronics: Giant & Tunnel Magnetoresistance, Spin-Transfer Torque (STT-MRAM))</div>
      
      <div class="topic-intro">
        <p>สปินทรอนิกส์ (Spintronics หรือ Spin Electronics) เป็นสาขาฟิสิกส์ประยุกต์ที่ใช้ประโยชน์จาก สปิน (Spin) ของอิเล็กตรอนควบคู่ไปกับประจุไฟฟ้า เพื่อสร้างอุปกรณ์จัดเก็บข้อมูล ประมวลผล และตรวจจับสนามแม่เหล็กที่มีความเร็วสูงยิ่งยวด ไม่สูญหายเมื่อตัดไฟ (Non-Volatile) และทนทานต่อรังสี</p>
    <p>จุดเริ่มต้นของสปินทรอนิกส์เกิดจากการค้นพบปรากฏการณ์ความต้านทานสนามแม่เหล็กยักษ์ (Giant Magnetoresistance: GMR) ในปี 1988 โดย อัลแบร์ แฟร์ และ เพเทอร์ กรึนแบร์ก (ได้รับรางวัลโนเบลสาขาฟิสิกส์ในปี 2007) ในโครงสร้างฟิล์มบางซ้อนสลับชั้นโลหะแม่เหล็กเฟอร์โร/โลหะธรรมดา (เช่น $	ext{Fe/Cr/Fe}$) ซึ่งความต้านทานไฟฟ้าจะลดลงอย่างมากเมื่อโมเมนต์แม่เหล็กของทั้งสองชั้นถูกเหนี่ยวนำให้ชี้ไปในทิศทางขนานกัน</p>
    <p>ต่อมาได้มีการพัฒนาสู่ ปรากฏการณ์ความต้านทานสนามแม่เหล็กแบบทะลุผ่าน (Tunnel Magnetoresistance: TMR) ในรอยต่อทะลุผ่านเชิงแม่เหล็ก (Magnetic Tunnel Junction: MTJ) ซึ่งใช้ฉนวนแมกนีเซียมออกไซด์ผลึกเดี่ยว $	ext{MgO}(001)$ เป็นกำแพงทะลุผ่าน ส่งผลให้อัตราส่วน TMR สูงเกิน $200 - 600\%$ ที่อุณหภูมิห้อง นำไปสู่การประดิษฐ์หน่วยความจำเข้าถึงโดยสุ่มเชิงแม่เหล็กที่ถ่ายโอนโมเมนตัมเชิงมุมของสปิน (Spin-Transfer Torque MRAM: STT-MRAM) และ SOT-MRAM</p>
  </div>

      <div class="subtopic-block">
        <h3>แบบจำลองการนำกระแสสองช่องของมอตต์ (Mott Two-Current Model)</h3>
            <p>อิเล็กตรอนที่มีสปินชี้ขึ้น (Spin-Up) และสปินชี้ลง (Spin-Down) จะมีกระบวนการกระเจิงและ Density of States ที่ระดับเฟอร์มิ $N_\uparrow(E_F) \neq N_\downarrow(E_F)$ แตกต่างกันในสารแม่เหล็กเฟอร์โร</p>
    <p>1. สถานะขนาน (Parallel: $P$): อิเล็กตรอนที่มีสปินทิศทางเดียวกับโมเมนต์แม่เหล็กจะเคลื่อนที่ผ่านได้โดยแทบไม่มีการกระเจิง ความต้านทานรวม $R_P = \frac{R_\uparrow R_\downarrow}{R_\uparrow + R_\downarrow}$ มีค่าต่ำ</p>
    <p>2. สถานะตรงข้าม (Antiparallel: $AP$): อิเล็กตรอนทั้งสองสปินจะถูกกระเจิงอย่างรุนแรงในชั้นใดชั้นหนึ่งเสมอ ความต้านทานรวม $R_{AP}$ จึงมีค่าสูงมาก</p>
  </div>

      <div class="subtopic-block">
        <h3>กลไก Spin-Transfer Torque (STT) และสมการของลันเดา-ลิฟชิตซ์-กิลเบิร์ต (LLG Equation)</h3>
            <p>เมื่อยิงกระแสอิเล็กตรอนที่มีโพลาไรเซชันของสปินสูงผ่านชั้นอิสระ (Free Layer) โมเมนตัมเชิงมุมของสปินจะถูกถ่ายโอนไปยังโมเมนต์แม่เหล็กของชั้นอิสระ ก่อให้เกิดทอร์กที่สามารถพลิกทิศทางแม่เหล็ก (Magnetization Switching) ได้โดยไม่ต้องใช้สนามแม่เหล็กภายนอก</p>
    <p>สมการ LLGS: $rac{dec{M}}{dt} = -\gamma (ec{M} 	imes ec{H}_{	ext{eff}}) + rac{lpha}{M_s} \left(ec{M} 	imes rac{dec{M}}{dt}ight) + ec{	au}_{	ext{STT}}$</p>
  </div>
  <div class="formula-group">

        <div class="equation-box">
          <div class="equation-header">📌 สมการฟิสิกส์หลัก: อัตราส่วน Tunnel Magnetoresistance (TMR Ratio) ตามสูตรของจูลลิแยร์</div>
          <div class="formula-math">$$\text{TMR} = \frac{R_{AP} - R_P}{R_P} = \frac{2 P_1 P_2}{1 - P_1 P_2}, \qquad P = \frac{N_\uparrow(E_F) - N_\downarrow(E_F)}{N_\uparrow(E_F) + N_\downarrow(E_F)}$$</div>
          <p style="font-size:9.5pt; margin:4px 0 0 0; color:#334155; line-height:1.75; text-indent:0;"><strong>คำอธิบายตัวแปรและนัยสำคัญ:</strong> อัตราส่วน TMR ในฟังก์ชันของสปินโพลาไรเซชัน P</p>
        </div>
            
        <div class="equation-box">
          <div class="equation-header">📌 สมการฟิสิกส์หลัก: ความหนาแน่นกระแสวิกฤตสำหรับการพลิกทิศทางสปิน (STT Critical Current)</div>
          <div class="formula-math">$$J_{c0} = \left(\frac{2e}{\hbar}\right) \left(\frac{\alpha \mu_0 M_s t_{\text{FL}}}{\eta}\right) (H_k + 2\pi M_s)$$</div>
          <p style="font-size:9.5pt; margin:4px 0 0 0; color:#334155; line-height:1.75; text-indent:0;"><strong>คำอธิบายตัวแปรและนัยสำคัญ:</strong> กระแสขั้นต่ำในการเขียนข้อมูล 0/1 ใน STT-MRAM</p>
        </div>
              </div>

      <div class="table-block">
        <h3>📊 ตารางเปรียบเทียบเทคโนโลยีหน่วยความจำกึ่งตัวนำกับ STT-MRAM</h3>
        <table class="data-table">
          <thead><tr>
            <th>คุณลักษณะ</th><th>SRAM (แคช)</th><th>DRAM (แรมหลัก)</th><th>NAND Flash</th><th>STT-MRAM (สปินทรอนิกส์)</th></tr></thead>
<tbody><tr><td>ความคงอยู่ของข้อมูล (Non-Volatile)</td><td>ไม่คงอยู่ (หายเมื่อดับไฟ)</td><td>ไม่คงอยู่ (ต้องรีเฟรช)</td><td>คงอยู่ (Non-Volatile)</td><td>คงอยู่ถาวร (Non-Volatile)</td></tr><tr><td>ความเร็วในการอ่าน/เขียน</td><td>เร็วมาก (< 1 ns)</td><td>ปานกลาง (10 - 20 ns)</td><td>ช้า (10 - 100 μs)</td><td>เร็วมาก (1 - 5 ns)</td></tr><tr><td>ความทนทานรอบการเขียน (Endurance)</td><td>ไม่จำกัด (> 10^16)</td><td>ไม่จำกัด (> 10^16)</td><td>จำกัด (10^4 - 10^5)</td><td>สูงมาก (> 10^12 - 10^15)</td></tr><tr><td>การใช้พลังงานขณะสแตนด์บาย</td><td>สูง (มีกระแสไฟฟ้ารั่ว)</td><td>ปานกลาง (ต้องรีเฟรช)</td><td>ศูนย์</td><td>ศูนย์ (Zero Leakage)</td></tr><tr><td>ความหนาแน่นต่อพื้นที่</td><td>ต่ำ (6 ทรานซิสเตอร์)</td><td>สูง (1T-1C)</td><td>สูงมาก (3D V-NAND)</td><td>สูง (1T-1MTJ)</td></tr></tbody></table>
</div>
  <div class="examples-group">

        <div class="example-box">
          <div class="example-header">
            <span>📝 ตัวอย่างการคำนวณที่ 6.3: การคำนวณอัตราส่วน TMR ของรอยต่อ CoFeB/MgO/CoFeB MTJ</span>
            <span style="background:#dcfce7; color:#15803d; font-size:8.5pt; padding:3px 10px; border-radius:4px; font-weight:700;">Step-by-Step Worked Solution</span>
          </div>
          <p style="text-indent:0; margin-bottom:10px;"><strong>โจทย์ปัญหา (Problem Statement):</strong><br>ขั้วแม่เหล็ก $	ext{CoFeB}$ ทั้งสองฝั่งมีสปินโพลาไรเซชัน $P_1 = P_2 = 0.65$ จงคำนวณหา (ก) อัตราส่วน TMR ตามแบบจำลองของจูลลิแยร์ (ข) ค่าความต้านทานในสถานะตรงข้าม $R_{AP}$ หากสถานะขนานมีค่า $R_P = 1.20	ext{ k}\Omega$</p>
          <div style="background:rgba(255,255,255,0.85); border:1px solid #e2e8f0; padding:12px 16px; border-radius:6px; margin:12px 0;">
            <strong style="color:#1e3a8a;">การวิเคราะห์และการคำนวณอย่างละเอียด:</strong><br>
            <p style="text-indent:0; margin:6px 0 0 0; line-height:1.85;">1. คำนวณเทอม $P_1 P_2 = (0.65)^2 = 0.4225$<br>2. $\text{TMR} = \frac{2 P_1 P_2}{1 - P_1 P_2} = \frac{2(0.4225)}{1 - 0.4225} = \frac{0.8450}{0.5775} = 1.4632 = 146.3\%<br>3. $R_{AP} = R_P \times (1 + \text{TMR}) = 1.20\text{ k}\Omega \times (1 + 1.4632) = 2.956\text{ k}\Omega$</p>
          </div>
          <div style="background:#f0fdf4; border-left:4px solid #16a34a; padding:10px 14px; margin-top:10px; font-size:9.5pt; color:#166534; border-radius:0 6px 6px 0;">
            💡 <strong>นัยสำคัญทางกายภาพและการประยุกต์ใช้งาน (Physical Insight):</strong><br>
            <span style="color:#14532d;">การเปลี่ยนแปลงความต้านทานจาก $1.20	ext{ k}\Omega$ เป็น $2.96	ext{ k}\Omega$ ให้สัญญาณระดับแรงดันที่อ่านค่าบิต 0 และ 1 ได้อย่างชัดเจนและแม่นยำ</span>
          </div>
        </div>
            
        <div class="example-box">
          <div class="example-header">
            <span>📝 ตัวอย่างการคำนวณที่ 6.4: การคำนวณกระแสวิกฤต STT สำหรับการเขียนข้อมูลในเซลล์ MRAM ขนาด 40 nm</span>
            <span style="background:#dcfce7; color:#15803d; font-size:8.5pt; padding:3px 10px; border-radius:4px; font-weight:700;">Step-by-Step Worked Solution</span>
          </div>
          <p style="text-indent:0; margin-bottom:10px;"><strong>โจทย์ปัญหา (Problem Statement):</strong><br>เซลล์ MTJ มีพื้นที่หน้าตัดวงรี $A = rac{\pi}{4} (40	ext{ nm}) (30	ext{ nm}) = 9.425 	imes 10^{-16}	ext{ m}^2$ มีความหนาแน่นกระแสวิกฤต $J_{c0} = 2.5 	imes 10^6	ext{ A/cm}^2$ จงคำนวณกระแสสวิตชิ่งขั้นต่ำ $I_{c0}$</p>
          <div style="background:rgba(255,255,255,0.85); border:1px solid #e2e8f0; padding:12px 16px; border-radius:6px; margin:12px 0;">
            <strong style="color:#1e3a8a;">การวิเคราะห์และการคำนวณอย่างละเอียด:</strong><br>
            <p style="text-indent:0; margin:6px 0 0 0; line-height:1.85;">1. แปลงพื้นที่เป็น $\text{cm}^2$: $A = 9.425 \times 10^{-12}\text{ cm}^2$<br>2. $I_{c0} = J_{c0} \times A = (2.5 \times 10^6\text{ A/cm}^2) \times (9.425 \times 10^{-12}\text{ cm}^2) = 2.356 \times 10^{-5}\text{ A} = 23.56\text{ }\mu\text{A}$</p>
          </div>
          <div style="background:#f0fdf4; border-left:4px solid #16a34a; padding:10px 14px; margin-top:10px; font-size:9.5pt; color:#166534; border-radius:0 6px 6px 0;">
            💡 <strong>นัยสำคัญทางกายภาพและการประยุกต์ใช้งาน (Physical Insight):</strong><br>
            <span style="color:#14532d;">กระแสสวิตชิ่งเพียง $23.6	ext{ }\mu	ext{A}$ สามารถจ่ายได้โดยตรงจากทรานซิสเตอร์ขับขนาดเล็ก ช่วยให้เซลล์ MRAM มีขนาดกะทัดรัดและกินไฟต่ำ</span>
          </div>
        </div>
              </div>
  <div class="code-group">

        <div class="code-box">
          <div class="code-header">💻 แบบจำลองเชิงคำนวณภาษาไพทอน (Computational Python 3.11): กรณีศึกษา: หน่วยความจำ STT-MRAM ฝังตัว (eMRAM) ในยานสำรวจอวกาศและรถยนต์ขับขี่อัตโนมัติ</div>
          <pre><code>บริษัทชั้นนำได้ผสานหน่วยความจำ eMRAM ขนาด 1 Gb บนชิปยานยนต์ ซึ่งทนต่ออุณหภูมิสูงกว่า 125 °C และทนต่อรังสีคอสมิกโดยไม่เกิดข้อผิดพลาด Bit-Flip ต่างจากหน่วยความจำแบบเดิม</code></pre>
        </div>
        <p style="font-size:9.5pt; color:#475569; margin-top:-6px; margin-bottom:18px; text-indent:0;"><em>คำอธิบายอัลกอริทึมการจำลอง:</em> สคริปต์ไพทอนสำหรับการคำนวณและจำลองเชิงตัวเลข</p>
              </div>
  <div class="lab-connection-block">
    <h3>🔬 การเชื่อมโยงสู่ห้องปฏิบัติการเสมือนจริงและเทคนิคการทดลอง (Virtual Lab Connection)</h3>
    <div style='background:#f0fdf4; border:1px solid #bbf7d0; border-left:5px solid #16a34a; padding:12px 16px; margin-bottom:14px; border-radius:6px;'><strong style='color:#166534; font-size:10.5pt;'>การจำลองการหมุนของสปินตามสมการ Landau-Lifshitz-Gilbert (LLG)</strong><p style='margin:6px 0 0 0; color:#14532d; text-indent:0; line-height:1.8;'>llg_spintronics_sim.py</p></div>
  </div>
  <div class="cases-block">
    <h3>🌐 กรณีศึกษางานวิจัยแนวหน้าและนวัตกรรมอุตสาหกรรม (Frontier Case Studies)</h3>
    <div style='background:#eff6ff; border:1px solid #bfdbfe; border-left:5px solid #2563eb; padding:12px 16px; margin-bottom:14px; border-radius:6px;'><strong style='color:#1e40af; font-size:10.5pt;'>การเชื่อมโยงกับ Virtual Lab 27: การจำลองสปินทรอนิกส์ TMR และหน่วยความจำ STT-MRAM</strong><p style='margin:6px 0 0 0; color:#1e3a8a; text-indent:0; line-height:1.8;'>ผู้เรียนสามารถควบคุมทิศทางโมเมนต์แม่เหล็ก $P/AP$ ใน Lab 27 ป้อนพัลส์กระแสเพื่อสังเกตการเกิด Spin-Transfer Torque Switching และวัดอัตราส่วน TMR</p></div>
  </div>

      <div class="checkpoint-box" style="background:#fefce8; border:1px solid #fef08a; border-left:5px solid #eab308; padding:14px 18px; margin:24px 0 35px 0; border-radius:6px; page-break-inside:avoid;">
        <strong style="color:#854d0e; font-size:10pt;">🎯 จุดตรวจประเมินความเข้าใจและคำถามทบทวนประจำหัวข้อ 6.2 (Concept Checkpoint)</strong>
        <ul style="margin:8px 0 0 0; padding-left:20px; color:#713f12; font-size:9.5pt; line-height:1.8;">
          <li>จงอธิบายแนวคิดรวบยอดหลักของ สปินทรอนิกส์: GMR, TMR และหน่วยความจำ STT-MRAM และความแตกต่างจากพฤติกรรมในระดับมหภาค</li>
          <li>พารามิเตอร์ใดเป็นปัจจัยวิกฤตที่ควบคุมสมบัติทางฟิสิกส์ในหัวข้อนี้ และมีผลกระทบอย่างไร?</li>
          <li>เชื่อมโยงหลักการฟิสิกส์ในหัวข้อนี้เข้ากับการประยุกต์ใช้จริงในเทคโนโลยีสมัยใหม่</li>
        </ul>
      </div>
    </div>
    
    <div class="topic-section">
      <h2>6.3 นาโนพลาสมอนิกส์และการสั่นพลาสมอนเฉพาะที่</h2>
      <div class="topic-en-title">(Nanoplasmonics, Surface Plasmon Polaritons (SPP) & Localized Plasmons (LSPR))</div>
      
      <div class="topic-intro">
        <p>นาโนพลาสมอนิกส์ (Nanoplasmonics) คือสาขาวิชาที่ศึกษาอันตรกิริยาอันทรงพลังระหว่างคลื่นแม่เหล็กไฟฟ้า (แสง) กับการแกว่งกวัดร่วมกันของกลุ่มหมอกอิเล็กตรอนอิสระ (Collective Free Electron Oscillations) บนพื้นผิวโลหะมีตระกูล เช่น ทองคำ (Au) และเงิน (Ag)</p>
    <p>ความสำคัญสูงสุดของพลาสมอนิกส์คือการสามารถบีบอัดและกักขังคลื่นแสงให้อยู่ในปริมาตรที่มีขนาดเล็กกว่าขีดจำกัดการเลี้ยวเบนของแสงตามธรรมชาติ (Sub-Diffraction-Limit Confinement: $V \ll (\lambda/2)^3$) ทำให้สามารถรวมพลังงานแสงลงในจุดที่มีขนาดเพียงไม่กี่นาโนเมตร</p>
    <p>ปรากฏการณ์หลักแบ่งออกเป็นสองรูปแบบ: คลื่นพลาสมอนโพลาริตอนที่ผิวระนาบ (Surface Plasmon Polaritons: SPPs ซึ่งเป็นคลื่นที่วิ่งเลียบไปตามรอยต่อโลหะ-ฉนวน) และ การสั่นพลาสมอนเฉพาะที่ของอนุภาคนาโน (Localized Surface Plasmon Resonance: LSPR) ซึ่งการสั่นพ้องของอิเล็กตรอนในอนุภาคนาโนทรงกลมหรือแท่งนาโนจะดูดกลืนและกระเจิงแสงสีเฉพาะอย่างรุนแรง พร้อมทั้งสร้างสนามไฟฟ้าเฉพาะที่ทวีคูณสูงขึ้นนับพันเท่า (Near-Field Enhancement)</p>
  </div>

      <div class="subtopic-block">
        <h3>ทฤษฎีการกระเจิงของมี (Mie Scattering Theory) สำหรับ LSPR ในอนุภาคทรงกลม</h3>
            <p>ภาคตัดขวางการดูดกลืนแสงของอนุภาคนาโนทรงกลมรัศมี $R$ ($R \ll \lambda$) ตามการประมาณแบบไดโพลไฟฟ้าสถิต:</p>
    <p>$$\sigma_{	ext{abs}}(\lambda) = rac{8\pi^2 R^3 \epsilon_m^{3/2}}{\lambda} 	ext{Im}\left[ rac{\epsilon_m(\lambda) - \epsilon_d}{\epsilon_m(\lambda) + 2\epsilon_d} ight]$$</p>
    <p>เงื่อนไขเรโซแนนซ์ของฟรอยลิช (Fröhlich Criterion) จะเกิดขึ้นเมื่อส่วนจริงของฟังก์ชันไดอิเล็กทริกโลหะเท่ากับ: $	ext{Re}[\epsilon_m(\lambda)] = -2 \epsilon_d$</p>
  </div>

      <div class="subtopic-block">
        <h3>ความไวต่อดัชนีหักเหของสิ่งแวดล้อม (Refractive Index Sensitivity) ในไบโอเซนเซอร์</h3>
            <p>ตำแหน่งความยาวคลื่นเรโซแนนซ์ $\lambda_{	ext{LSPR}}$ จะเลื่อนไปทางสีแดง (Red-shift) เมื่อดัชนีหักเหของสารรอบข้าง $n$ เพิ่มขึ้น: $\Delta \lambda = S_{	ext{RI}} 	imes \Delta n$ โดยมีค่าความไว $S_{	ext{RI}} pprox 100 - 800	ext{ nm/RIU}$ ทำให้สามารถตรวจจับการจับกันของแอนติเจน-แอนติบอดีหรือโปรตีนเป้าหมายบนผิวอนุภาคทองคำได้แบบเรียลไทม์โดยไม่ต้องติดฉลากเรืองแสง (Label-Free Biosensing)</p>
  </div>
  <div class="formula-group">

        <div class="equation-box">
          <div class="equation-header">📌 สมการฟิสิกส์หลัก: เงื่อนไขเรโซแนนซ์ฟรอยลิชสำหรับอนุภาคทรงกลม</div>
          <div class="formula-math">$$\text{Re}[\epsilon_m(\lambda_{\text{LSPR}})] = -2 \, \epsilon_d = -2 \, n_d^2$$</div>
          <p style="font-size:9.5pt; margin:4px 0 0 0; color:#334155; line-height:1.75; text-indent:0;"><strong>คำอธิบายตัวแปรและนัยสำคัญ:</strong> เงื่อนไขการเกิดพีคการดูดกลืน LSPR</p>
        </div>
            
        <div class="equation-box">
          <div class="equation-header">📌 สมการฟิสิกส์หลัก: แบบจำลองดรูดสำหรับฟังก์ชันไดอิเล็กทริกของโลหะ</div>
          <div class="formula-math">$$\epsilon_m(\omega) = 1 - \frac{\omega_p^2}{\omega(\omega + i\gamma)}, \qquad \omega_p = \sqrt{\frac{n_e e^2}{\epsilon_0 m_e}}$$</div>
          <p style="font-size:9.5pt; margin:4px 0 0 0; color:#334155; line-height:1.75; text-indent:0;"><strong>คำอธิบายตัวแปรและนัยสำคัญ:</strong> พลาสมาความถี่รวมของอิเล็กตรอนในโลหะ</p>
        </div>
              </div>

      <div class="table-block">
        <h3>📊 ตารางเปรียบเทียบสมบัติพลาสมอนิกส์ของโลหะชนิดต่างๆ</h3>
        <table class="data-table">
          <thead><tr>
            <th>โลหะ</th><th>พลาสมาความถี่ ℏωp (eV)</th><th>ช่วงความยาวคลื่น LSPR</th><th>ความสูญเสียเชิงแสง (Loss)</th><th>ความเสถียรทางเคมี</th></tr></thead>
<tbody><tr><td>เงิน (Ag)</td><td>9.01 eV</td><td>380 - 450 nm (UV-น้ำเงิน)</td><td>ต่ำที่สุด (Q-factor สูงสุด)</td><td>เกิดออกไซด์/ซัลไฟด์ง่าย</td></tr><tr><td>ทองคำ (Au)</td><td>8.95 eV</td><td>520 - 580 nm (เขียว-แดง)</td><td>ปานกลาง (Interband > 2.4 eV)</td><td>เสถียรสูงสุด ไม่ทำปฏิกิริยา (Biocompatible)</td></tr><tr><td>ทองแดง (Cu)</td><td>8.75 eV</td><td>570 - 620 nm (ส้ม-แดง)</td><td>ค่อนข้างสูง</td><td>เกิดออกไซด์ง่าย</td></tr><tr><td>อะลูมิเนียม (Al)</td><td>15.0 eV</td><td>200 - 400 nm (UV ลึก)</td><td>ปานกลางในย่าน UV</td><td>สร้างฟิล์ม Al2O3 ป้องกันตัวเอง</td></tr></tbody></table>
</div>
  <div class="examples-group">

        <div class="example-box">
          <div class="example-header">
            <span>📝 ตัวอย่างการคำนวณที่ 6.5: การคำนวณความยาวคลื่น LSPR ของอนุภาคนาโนทองคำในน้ำ</span>
            <span style="background:#dcfce7; color:#15803d; font-size:8.5pt; padding:3px 10px; border-radius:4px; font-weight:700;">Step-by-Step Worked Solution</span>
          </div>
          <p style="text-indent:0; margin-bottom:10px;"><strong>โจทย์ปัญหา (Problem Statement):</strong><br>อนุภาคนาโนทองคำทรงกลมแขวนลอยในน้ำ ($n_d = 1.333 \implies \epsilon_d = n_d^2 = 1.777$) ใช้แบบจำลองดรูดสำหรับทองคำ: $\hbar \omega_p = 9.0	ext{ eV}$ และ $\epsilon_\infty = 9.0$ จงคำนวณหาพลังงานโฟตอนเรโซแนนซ์ $E_{	ext{LSPR}}$ และความยาวคลื่น $\lambda_{	ext{LSPR}}$</p>
          <div style="background:rgba(255,255,255,0.85); border:1px solid #e2e8f0; padding:12px 16px; border-radius:6px; margin:12px 0;">
            <strong style="color:#1e3a8a;">การวิเคราะห์และการคำนวณอย่างละเอียด:</strong><br>
            <p style="text-indent:0; margin:6px 0 0 0; line-height:1.85;">1. เงื่อนไขฟรอยลิช: $\epsilon_m = \epsilon_\infty - \frac{\omega_p^2}{\omega^2} = -2 \epsilon_d$<br>2. จัดรูป: $\frac{\omega_p^2}{\omega^2} = \epsilon_\infty + 2 \epsilon_d = 9.0 + 2(1.777) = 12.554$<br>3. $\hbar \omega = \frac{\hbar \omega_p}{\sqrt{12.554}} = \frac{9.0\text{ eV}}{3.543} = 2.540\text{ eV}$<br>4. $\lambda_{\text{LSPR}} = \frac{1240\text{ eV}\cdot\text{nm}}{2.540\text{ eV}} = 488.2\text{ nm} \approx 520\text{ nm}$ (เมื่อรวม Interband Transitions)</p>
          </div>
          <div style="background:#f0fdf4; border-left:4px solid #16a34a; padding:10px 14px; margin-top:10px; font-size:9.5pt; color:#166534; border-radius:0 6px 6px 0;">
            💡 <strong>นัยสำคัญทางกายภาพและการประยุกต์ใช้งาน (Physical Insight):</strong><br>
            <span style="color:#14532d;">การดูดกลืนแสงสีเขียว-น้ำเงินอย่างรุนแรง ทำให้อนุภาคนาโนทองคำคอลลอยด์สะท้อนแสงสีแดงทับทิม (Ruby Red) ที่สวยงาม</span>
          </div>
        </div>
            
        <div class="example-box">
          <div class="example-header">
            <span>📝 ตัวอย่างการคำนวณที่ 6.6: การคำนวณการเลื่อนของพีค LSPR ในการตรวจวัดชีวโมเลกุล</span>
            <span style="background:#dcfce7; color:#15803d; font-size:8.5pt; padding:3px 10px; border-radius:4px; font-weight:700;">Step-by-Step Worked Solution</span>
          </div>
          <p style="text-indent:0; margin-bottom:10px;"><strong>โจทย์ปัญหา (Problem Statement):</strong><br>เซนเซอร์แท่งนาโนทองคำมีค่าความไว $S_{	ext{RI}} = 450	ext{ nm/RIU}$ เมื่อเกิดการจับตัวของแอนติบอดีบนผิวทำให้ดัชนีหักเหเฉพาะที่เปลี่ยนไป $\Delta n = 0.025$ จงคำนวณการเลื่อนของพีคสเปกตรัม $\Delta \lambda$</p>
          <div style="background:rgba(255,255,255,0.85); border:1px solid #e2e8f0; padding:12px 16px; border-radius:6px; margin:12px 0;">
            <strong style="color:#1e3a8a;">การวิเคราะห์และการคำนวณอย่างละเอียด:</strong><br>
            <p style="text-indent:0; margin:6px 0 0 0; line-height:1.85;">$$\Delta \lambda = S_{\text{RI}} \times \Delta n = 450\text{ nm/RIU} \times 0.025\text{ RIU} = 11.25\text{ nm}$$</p>
          </div>
          <div style="background:#f0fdf4; border-left:4px solid #16a34a; padding:10px 14px; margin-top:10px; font-size:9.5pt; color:#166534; border-radius:0 6px 6px 0;">
            💡 <strong>นัยสำคัญทางกายภาพและการประยุกต์ใช้งาน (Physical Insight):</strong><br>
            <span style="color:#14532d;">การเลื่อนของพีคไปทางสีแดง $11.25	ext{ nm}$ สามารถตรวจวัดได้อย่างง่ายดายด้วยสเปกโตรมิเตอร์มาตรฐาน</span>
          </div>
        </div>
              </div>
  <div class="code-group">

        <div class="code-box">
          <div class="code-header">💻 แบบจำลองเชิงคำนวณภาษาไพทอน (Computational Python 3.11): กรณีศึกษา: การรักษามะเร็งด้วยความร้อนเหนี่ยวนำเชิงแสง (Plasmonic Photothermal Therapy: PPTT)</div>
          <pre><code>การฉีดอนุภาคเปลือกทองคำนาโน (Gold Nanoshells) หรือแท่งทองคำนาโนที่ปรับแต่งพีค LSPR ให้อยู่ในย่านหน้าต่างชีวภาพใกล้อินฟราเรด (NIR: 800 nm) เข้าสู่เซลล์เนื้องอก แล้วฉายแสงเลเซอร์ NIR ทะลุผิวหนังเพื่อทำลายเซลล์มะเร็งด้วยความร้อนเฉพาะจุดโดยไม่ทำอันตรายต่อเนื้อเยื่อปกติ</code></pre>
        </div>
        <p style="font-size:9.5pt; color:#475569; margin-top:-6px; margin-bottom:18px; text-indent:0;"><em>คำอธิบายอัลกอริทึมการจำลอง:</em> สคริปต์ไพทอนสำหรับการคำนวณและจำลองเชิงตัวเลข</p>
              </div>
  <div class="lab-connection-block">
    <h3>🔬 การเชื่อมโยงสู่ห้องปฏิบัติการเสมือนจริงและเทคนิคการทดลอง (Virtual Lab Connection)</h3>
    <div style='background:#f0fdf4; border:1px solid #bbf7d0; border-left:5px solid #16a34a; padding:12px 16px; margin-bottom:14px; border-radius:6px;'><strong style='color:#166534; font-size:10.5pt;'>การจำลองสเปกตรัมการดูดกลืน LSPR ตามทฤษฎีของมี</strong><p style='margin:6px 0 0 0; color:#14532d; text-indent:0; line-height:1.8;'>mie_lspr_sim.py</p></div>
  </div>
  <div class="cases-block">
    <h3>🌐 กรณีศึกษางานวิจัยแนวหน้าและนวัตกรรมอุตสาหกรรม (Frontier Case Studies)</h3>
    <div style='background:#eff6ff; border:1px solid #bfdbfe; border-left:5px solid #2563eb; padding:12px 16px; margin-bottom:14px; border-radius:6px;'><strong style='color:#1e40af; font-size:10.5pt;'>การเชื่อมโยงกับ Virtual Lab 28: การจำลองนาโนพลาสมอนิกส์ LSPR และไบโอเซนเซอร์</strong><p style='margin:6px 0 0 0; color:#1e3a8a; text-indent:0; line-height:1.8;'>ผู้เรียนสามารถเปลี่ยนชนิดโลหะ (Au, Ag, Cu), ปรับขนาดและรูปร่างอนุภาค และเปลี่ยนดัชนีหักเหของสารละลายใน Lab 28 เพื่อสังเกตการเลื่อนของพีคพลาสมอนิกส์</p></div>
  </div>

      <div class="checkpoint-box" style="background:#fefce8; border:1px solid #fef08a; border-left:5px solid #eab308; padding:14px 18px; margin:24px 0 35px 0; border-radius:6px; page-break-inside:avoid;">
        <strong style="color:#854d0e; font-size:10pt;">🎯 จุดตรวจประเมินความเข้าใจและคำถามทบทวนประจำหัวข้อ 6.3 (Concept Checkpoint)</strong>
        <ul style="margin:8px 0 0 0; padding-left:20px; color:#713f12; font-size:9.5pt; line-height:1.8;">
          <li>จงอธิบายแนวคิดรวบยอดหลักของ นาโนพลาสมอนิกส์และการสั่นพลาสมอนเฉพาะที่ และความแตกต่างจากพฤติกรรมในระดับมหภาค</li>
          <li>พารามิเตอร์ใดเป็นปัจจัยวิกฤตที่ควบคุมสมบัติทางฟิสิกส์ในหัวข้อนี้ และมีผลกระทบอย่างไร?</li>
          <li>เชื่อมโยงหลักการฟิสิกส์ในหัวข้อนี้เข้ากับการประยุกต์ใช้จริงในเทคโนโลยีสมัยใหม่</li>
        </ul>
      </div>
    </div>
    
    <div class="topic-section">
      <h2>6.4 การสเปกโทรสโกปีรามานแบบขยายสัญญาณด้วยพื้นผิว</h2>
      <div class="topic-en-title">(Surface-Enhanced Raman Scattering (SERS) & Hot-Spot Physics)</div>
      
      <div class="topic-intro">
        <p>การสเปกโทรสโกปีรามานแบบขยายสัญญาณด้วยพื้นผิว (Surface-Enhanced Raman Scattering: SERS) เป็นปรากฏการณ์ทางนาโนโฟโทนิกส์ที่ค้นพบโดย มาร์ติน เฟลชมันน์ และคณะ ในปี 1974 ซึ่งสัญญาณการกระเจิงรามานที่ตามปกติอ่อนแอมาก (มีโอกาสเกิดเพียง 1 ใน $10^7$ โฟตอน) จะได้รับการขยายความเข้มสัญญาณให้แรงขึ้นอย่างมหาศาลถึง $10^6 - 10^{14}$ เท่า เมื่อโมเลกุลเป้าหมายถูกดูดซับอยู่บนพื้นผิวโครงสร้างโลหะนาโนพลาสมอนิกส์</p>
    <p>ปัจจัยการขยายสัญญาณอันยิ่งยวดนี้เกิดจากการทำงานร่วมกันของสองกลไกหลัก: กลไกทางแม่เหล็กไฟฟ้า (Electromagnetic Enhancement Mechanism: EM) ซึ่งคิดเป็นสัดส่วนมากกว่า $99.9\%$ ของการขยายตัว โดยสนามไฟฟ้าของแสงจะถูกบีบอัดและทวีคูณขึ้นอย่างรุนแรงที่บริเวณช่องแคบระดับนาโนเมตรระหว่างอนุภาคคู่ เรียกว่า 'จุดร้อนพลาสมอนิกส์' (Plasmonic Hot-Spots) ทำให้สัญญาณรามานขยายตัวตามกำลังสี่ของสนามไฟฟ้า ($	ext{EF}_{	ext{EM}} \propto |E_{	ext{loc}}/E_0|^4$)</p>
    <p>กลไกที่สองคือ กลไกทางเคมี (Chemical Enhancement: CM) ซึ่งเกิดจากการถ่ายโอนประจุ (Charge Transfer) ระหว่างระดับพลังงานของโมเลกุลกับระดับพลังงานเฟอร์มิของโลหะ ซึ่งช่วยขยายสัญญาณเพิ่มขึ้นอีก $10 - 100$ เท่า ส่งผลให้ SERS กลายเป็นเครื่องมือที่ทรงพลังที่สุดในการตรวจจับและระบุลายนิ้วมือโมเลกุลเดี่ยว (Single-Molecule SERS) ได้อย่างแม่นยำ</p>
  </div>

      <div class="subtopic-block">
        <h3>ฟิสิกส์ของ Plasmonic Hot-Spots และการขยายสัญญาณระดับกำลังสี่ ($|E|^4$ Approximation)</h3>
            <p>เมื่ออนุภาคนาโนทองคำสองอนุภาคเข้ามาใกล้กันโดยมีช่องว่างแคบ $g < 2	ext{ nm}$ โหมดพลาสมอนจะเกิดการจับคู่กันอย่างรุนแรง (Plasmonic Hybridization) ทำให้ความหนาแน่นสนามไฟฟ้าที่จุดกึ่งกลางทวีคูณสูงขึ้นกว่า $E_0$ ถึง 100 เท่า ($|E_{	ext{loc}}/E_0| pprox 100$)</p>
    <p>เนื่องจากสัญญาณ SERS ขึ้นกับทั้งสนามไฟฟ้าขาเข้าที่ความถี่ตกกระทบ $\omega_0$ และสนามไฟฟ้าที่ความถี่กระเจิงรามาน $\omega_R$: $I_{	ext{SERS}} \propto |E(\omega_0)|^2 |E(\omega_R)|^2 pprox |E_{	ext{loc}}|^4$</p>
    <p>ปัจจัยการขยายสัญญาณจึงมีค่าสูงถึง $	ext{EF} = (100)^4 = 10^8$ เท่า และเมื่อรวมกับโครงสร้างรูปดาวหรือกรงนาโนจะขยายได้สูงถึง $10^{12} - 10^{14}$ เท่า</p>
  </div>

      <div class="subtopic-block">
        <h3>โครงสร้างซับสเตรต SERS ขั้นสูงและการนำไปใช้ตรวจวัดสารเคมีอันตราย</h3>
            <p>การใช้แผ่นเวเฟอร์ซิลิคอนที่เคลือบด้วยอาร์เรย์ของเสานาโนเงิน (Silver Nanopillars) หรือแผ่นไฮบริด กราฟีน-อนุภาคทองคำ (Graphene-Mediated SERS) ช่วยให้ได้สัญญาณที่สม่ำเสมอและทำซ้ำได้สูง (Reproducibility) เหมาะสำหรับการตรวจหาสารกำจัดศัตรูพืชตกค้างและสารระเบิดระดับพิโกโมลาร์</p>
  </div>
  <div class="formula-group">

        <div class="equation-box">
          <div class="equation-header">📌 สมการฟิสิกส์หลัก: ปัจจัยการขยายสัญญาณแม่เหล็กไฟฟ้า SERS</div>
          <div class="formula-math">$$\text{EF}_{\text{EM}} = \left| \frac{E_{\text{loc}}(\omega_0)}{E_0} \right|^2 \left| \frac{E_{\text{loc}}(\omega_R)}{E_0} \right|^2 \approx \left| \frac{E_{\text{loc}}}{E_0} \right|^4$$</div>
          <p style="font-size:9.5pt; margin:4px 0 0 0; color:#334155; line-height:1.75; text-indent:0;"><strong>คำอธิบายตัวแปรและนัยสำคัญ:</strong> กฎการขยายสัญญาณตามกำลังสี่ของสนามไฟฟ้าเฉพาะที่</p>
        </div>
            
        <div class="equation-box">
          <div class="equation-header">📌 สมการฟิสิกส์หลัก: การคำนวณปัจจัยการขยายสัญญาณเชิงวิเคราะห์ (Analytical Enhancement Factor)</div>
          <div class="formula-math">$$\text{AEF} = \frac{I_{\text{SERS}} / N_{\text{SERS}}}{I_{\text{bulk}} / N_{\text{bulk}}} \approx 10^8 - 10^{12}$$</div>
          <p style="font-size:9.5pt; margin:4px 0 0 0; color:#334155; line-height:1.75; text-indent:0;"><strong>คำอธิบายตัวแปรและนัยสำคัญ:</strong> การเปรียบเทียบความเข้มสัญญาณต่อโมเลกุล</p>
        </div>
              </div>

      <div class="table-block">
        <h3>📊 ตารางเปรียบเทียบชนิดของ Hot-Spots ในโครงสร้างนาโน SERS</h3>
        <table class="data-table">
          <thead><tr>
            <th>ชนิดโครงสร้าง</th><th>ระยะช่องว่าง (Gap g)</th><th>การทวีคูณสนาม |E/E0|</th><th>ปัจจัยการขยาย EF</th><th>ระดับความสามารถในการตรวจวัด</th></tr></thead>
<tbody><tr><td>อนุภาคเดี่ยวทรงกลม (Single Sphere)</td><td>-</td><td>3 - 5</td><td>10^2 - 10^3</td><td>สารละลายความเข้มข้นมิลลิโมลาร์</td></tr><tr><td>อนุภาคเดี่ยวรูปดาว (Nanostar Tip)</td><td>ปลายแหลม r < 2 nm</td><td>20 - 30</td><td>10^5 - 10^6</td><td>ระดับไมโครโมลาร์ (μM)</td></tr><tr><td>อนุภาคคู่ไดเมอร์ (Nanoparticle Dimer)</td><td>1.0 - 2.0 nm</td><td>100 - 300</td><td>10^8 - 10^10</td><td>ระดับนาโนโมลาร์ถึงพิโกโมลาร์</td></tr><tr><td>อนุภาคบนฟิล์มกระจก (NPoM)</td><td>0.5 - 1.0 nm (SAM spacer)</td><td>500 - 1000</td><td>10^11 - 10^12</td><td>โมเลกุลเดี่ยว (Single-Molecule SERS)</td></tr></tbody></table>
</div>
  <div class="examples-group">

        <div class="example-box">
          <div class="example-header">
            <span>📝 ตัวอย่างการคำนวณที่ 6.7: การคำนวณปัจจัยการขยายสัญญาณ SERS EF จากความแรงของสนามไฟฟ้า</span>
            <span style="background:#dcfce7; color:#15803d; font-size:8.5pt; padding:3px 10px; border-radius:4px; font-weight:700;">Step-by-Step Worked Solution</span>
          </div>
          <p style="text-indent:0; margin-bottom:10px;"><strong>โจทย์ปัญหา (Problem Statement):</strong><br>ที่จุด Hot-Spot ระหว่างอนุภาคเงินคู่ มีค่าความแรงสนามไฟฟ้าเฉพาะที่ $|E_{	ext{loc}}| = 250 E_0$ จงคำนวณหาปัจจัยการขยายสัญญาณแม่เหล็กไฟฟ้า $	ext{EF}_{	ext{EM}}$ ในรูปทศนิยมและสเกลลอการิทึม</p>
          <div style="background:rgba(255,255,255,0.85); border:1px solid #e2e8f0; padding:12px 16px; border-radius:6px; margin:12px 0;">
            <strong style="color:#1e3a8a;">การวิเคราะห์และการคำนวณอย่างละเอียด:</strong><br>
            <p style="text-indent:0; margin:6px 0 0 0; line-height:1.85;">1. $\text{EF}_{\text{EM}} \approx \left| \frac{E_{\text{loc}}}{E_0} \right|^4 = (250)^4 = 3.906 \times 10^9$<br>2. ในสเกลลอการิทึม: $\log_{10}(\text{EF}) = \log_{10}(3.906 \times 10^9) = 9.59$</p>
          </div>
          <div style="background:#f0fdf4; border-left:4px solid #16a34a; padding:10px 14px; margin-top:10px; font-size:9.5pt; color:#166534; border-radius:0 6px 6px 0;">
            💡 <strong>นัยสำคัญทางกายภาพและการประยุกต์ใช้งาน (Physical Insight):</strong><br>
            <span style="color:#14532d;">สัญญาณรามานของโมเลกุลที่ตกอยู่ในจุด Hot-Spot นี้จะทวีความเข้มข้นขึ้นเกือบ 4 พันล้านเท่า ทำให้สามารถตรวจวัดได้แม้มีเพียงไม่กี่โมเลกุล</span>
          </div>
        </div>
            
        <div class="example-box">
          <div class="example-header">
            <span>📝 ตัวอย่างการคำนวณที่ 6.8: การคำนวณความเข้มข้นขีดจำกัดต่ำสุดในการตรวจจับ (Limit of Detection - LOD)</span>
            <span style="background:#dcfce7; color:#15803d; font-size:8.5pt; padding:3px 10px; border-radius:4px; font-weight:700;">Step-by-Step Worked Solution</span>
          </div>
          <p style="text-indent:0; margin-bottom:10px;"><strong>โจทย์ปัญหา (Problem Statement):</strong><br>การตรวจวัดรามานแบบดั้งเดิมของสารพิษสามารถตรวจจับได้ที่ความเข้มข้นต่ำสุด $C_{	ext{bulk}} = 10.0	ext{ mM}$ เมื่อนำมาตรวจด้วยแผ่นชิป SERS ที่มีค่า $	ext{AEF} = 5.0 	imes 10^8$ จงประเมินค่าความเข้มข้นขีดจำกัดต่ำสุดใหม่ $C_{	ext{LOD}}$</p>
          <div style="background:rgba(255,255,255,0.85); border:1px solid #e2e8f0; padding:12px 16px; border-radius:6px; margin:12px 0;">
            <strong style="color:#1e3a8a;">การวิเคราะห์และการคำนวณอย่างละเอียด:</strong><br>
            <p style="text-indent:0; margin:6px 0 0 0; line-height:1.85;">$$C_{\text{LOD}} \approx \frac{C_{\text{bulk}}}{\text{AEF}} = \frac{10.0 \times 10^{-3}\text{ M}}{5.0 \times 10^8} = 2.0 \times 10^{-11}\text{ M} = 20\text{ pM}$$</p>
          </div>
          <div style="background:#f0fdf4; border-left:4px solid #16a34a; padding:10px 14px; margin-top:10px; font-size:9.5pt; color:#166534; border-radius:0 6px 6px 0;">
            💡 <strong>นัยสำคัญทางกายภาพและการประยุกต์ใช้งาน (Physical Insight):</strong><br>
            <span style="color:#14532d;">ความไวเพิ่มขึ้นจนสามารถตรวจจับสารพิษได้ที่ระดับ 20 พิโกโมลาร์ (pico-molar) เหมาะสำหรับการตรวจสอบความปลอดภัยทางอาหารและนิติวิทยาศาสตร์</span>
          </div>
        </div>
              </div>
  <div class="code-group">

        <div class="code-box">
          <div class="code-header">💻 แบบจำลองเชิงคำนวณภาษาไพทอน (Computational Python 3.11): กรณีศึกษา: การตรวจจับสารกำจัดศัตรูพืชตกค้างบนเปลือกผลไม้แบบทันทีด้วยกระดาษทดสอบ SERS (Paper-based SERS Swab)</div>
          <pre><code>การใช้กระดาษกรองที่เคลือบด้วยอนุภาคนาโนเงินรูปดาว (Silver Nanostars) เช็ดถูบนผิวเปลือกส้ม สามารถตรวจจับสารตกค้างคลอร์ไพริฟอสได้ที่ความเข้มข้นต่ำกว่า 1 ส่วนในพันล้านส่วน (ppb) ภายในเวลาไม่ถึง 30 วินาที</code></pre>
        </div>
        <p style="font-size:9.5pt; color:#475569; margin-top:-6px; margin-bottom:18px; text-indent:0;"><em>คำอธิบายอัลกอริทึมการจำลอง:</em> สคริปต์ไพทอนสำหรับการคำนวณและจำลองเชิงตัวเลข</p>
              </div>
  <div class="lab-connection-block">
    <h3>🔬 การเชื่อมโยงสู่ห้องปฏิบัติการเสมือนจริงและเทคนิคการทดลอง (Virtual Lab Connection)</h3>
    <div style='background:#f0fdf4; border:1px solid #bbf7d0; border-left:5px solid #16a34a; padding:12px 16px; margin-bottom:14px; border-radius:6px;'><strong style='color:#166534; font-size:10.5pt;'>การจำลองการกระจายตัวของสนามไฟฟ้า $|E|^4$ ในช่องว่าง Hot-Spot</strong><p style='margin:6px 0 0 0; color:#14532d; text-indent:0; line-height:1.8;'>sers_hotspot_sim.py</p></div>
  </div>
  <div class="cases-block">
    <h3>🌐 กรณีศึกษางานวิจัยแนวหน้าและนวัตกรรมอุตสาหกรรม (Frontier Case Studies)</h3>
    <div style='background:#eff6ff; border:1px solid #bfdbfe; border-left:5px solid #2563eb; padding:12px 16px; margin-bottom:14px; border-radius:6px;'><strong style='color:#1e40af; font-size:10.5pt;'>การเชื่อมโยงกับ Virtual Lab 29: การจำลองการสเปกโทรสโกปีรามานขยายสัญญาณพื้นผิว SERS</strong><p style='margin:6px 0 0 0; color:#1e3a8a; text-indent:0; line-height:1.8;'>ผู้เรียนสามารถปรับระยะห่างระหว่างอนุภาคคู่ใน Lab 29 สังเกตการก่อตัวของ Hot-Spot และบันทึกสเปกตรัมลายนิ้วมือโมเลกุลเดี่ยว Rhodamine 6G</p></div>
  </div>

      <div class="checkpoint-box" style="background:#fefce8; border:1px solid #fef08a; border-left:5px solid #eab308; padding:14px 18px; margin:24px 0 35px 0; border-radius:6px; page-break-inside:avoid;">
        <strong style="color:#854d0e; font-size:10pt;">🎯 จุดตรวจประเมินความเข้าใจและคำถามทบทวนประจำหัวข้อ 6.4 (Concept Checkpoint)</strong>
        <ul style="margin:8px 0 0 0; padding-left:20px; color:#713f12; font-size:9.5pt; line-height:1.8;">
          <li>จงอธิบายแนวคิดรวบยอดหลักของ การสเปกโทรสโกปีรามานแบบขยายสัญญาณด้วยพื้นผิว และความแตกต่างจากพฤติกรรมในระดับมหภาค</li>
          <li>พารามิเตอร์ใดเป็นปัจจัยวิกฤตที่ควบคุมสมบัติทางฟิสิกส์ในหัวข้อนี้ และมีผลกระทบอย่างไร?</li>
          <li>เชื่อมโยงหลักการฟิสิกส์ในหัวข้อนี้เข้ากับการประยุกต์ใช้จริงในเทคโนโลยีสมัยใหม่</li>
        </ul>
      </div>
    </div>
    
    <div class="topic-section">
      <h2>6.5 เมทาแมทีเรียลระดับนาโนและโฟโทนิกส์ผลึก</h2>
      <div class="topic-en-title">(Optical Metamaterials, Negative Refraction, Photonic Crystals & Metalenses)</div>
      
      <div class="topic-intro">
        <p>เมทาแมทีเรียลเชิงแสง (Optical Metamaterials) คือวัสดุโครงสร้างประดิษฐ์ระดับนาโนเมตรที่ถูกออกแบบให้มีสมบัติทางแม่เหล็กไฟฟ้าแปลกใหม่ที่ไม่สามารถพบได้ในธรรมชาติ โดยมีหน่วยย่อยพื้นฐานเรียกว่า 'เมทาอะตอม' (Meta-atoms) ที่มีขนาดเล็กกว่าความยาวคลื่นของแสงอย่างมาก</p>
    <p>ความก้าวหน้าครั้งสำคัญคือการสร้างวัสดุที่มี ดัชนีหักเหเป็นลบ (Negative Index of Refraction: $n < 0$) จากการทำให้ค่าสภาพยอมทางไฟฟ้า ($\epsilon < 0$) และสภาพให้ซึมซาบได้ทางแม่เหล็ก ($\mu < 0$) มีค่าเป็นลบพร้อมกัน นำไปสู่การค้นพบ ปรากฏการณ์การหักเหย้อนกลับ (Negative Refraction), เลนส์สมบูรณ์แบบที่ไร้ความคลาดทรงกลมและก้าวข้ามขีดจำกัดการเลี้ยวเบน (Pendry's Superlens), และเทคโนโลยีเสื้อคลุมล่องหนเชิงแสง (Optical Invisibility Cloaking)</p>
    <p>ในระดับการใช้งานจริง เมทาเซอร์เฟส (Metasurfaces) ซึ่งเป็นเมทาแมทีเรียลแบบ 2 มิติบางเฉียบ ได้ปฏิวัติวงการทัศนศาสตร์ด้วยการสร้าง เมทาเลนส์ระนาบ (Flat Metalenses) ที่มีความหนาเพียงไม่กี่ร้อยนาโนเมตรแต่สามารถทดแทนชุดเลนส์แก้วหนาเตอะในกล้องสมาร์ทโฟนและแว่นตาเสมือนจริง AR/VR ได้อย่างสมบูรณ์</p>
  </div>

      <div class="subtopic-block">
        <h3>ฟิสิกส์ของดัชนีหักเหเป็นลบและเวกเตอร์ของพอยน์ติง (Left-Handed Materials)</h3>
            <p>ในวัสดุดัชนีหักเหเป็นลบ เวกเตอร์สนามไฟฟ้า $ec{E}$, สนามแม่เหล็ก $ec{H}$, และเวกเตอร์คลื่น $ec{k}$ จะเรียงตัวตามกฎมือซ้าย (Left-Handed Triad)</p>
    <p>เวกเตอร์ของพอยน์ติง $ec{S} = ec{E} 	imes ec{H}$ ซึ่งบอกทิศทางการไหลของพลังงาน จะมีทิศทางตรงกันข้ามกับเวกเตอร์คลื่น $ec{k}$ ($ec{S} \cdot ec{k} < 0$) ทำให้เฟสของคลื่นเคลื่อนที่ถอยหลังเข้าหาแหล่งกำเนิด</p>
  </div>

      <div class="subtopic-block">
        <h3>ผลึกโฟโทนิกส์ (Photonic Crystals) และแถบช่องว่างพลังงานเชิงแสง (Photonic Bandgap: PBG)</h3>
            <p>การจัดเรียงโครงสร้างไดอิเล็กทริกที่มีดัชนีหักเหแตกต่างกันให้มีคาบความสม่ำเสมอใน 1D, 2D หรือ 3D ก่อให้เกิด Photonic Bandgap ซึ่งแสงที่มีความถี่ในช่วงนี้จะไม่สามารถแพร่ผ่านโครงสร้างได้ นำไปสู่การสร้างท่อนำคลื่นแสงเลี้ยวหักศอกไร้การสูญเสียและเลเซอร์ไมโครคาวิตี้</p>
  </div>
  <div class="formula-group">

        <div class="equation-box">
          <div class="equation-header">📌 สมการฟิสิกส์หลัก: ดัชนีหักเหเชิงซ้อนของเมทาแมทีเรียล</div>
          <div class="formula-math">$$n = \sqrt{\epsilon_r \, \mu_r} = -\sqrt{|\epsilon_r| |\mu_r|} \quad (\text{เมื่อ } \epsilon_r < 0 \text{ และ } \mu_r < 0)$$</div>
          <p style="font-size:9.5pt; margin:4px 0 0 0; color:#334155; line-height:1.75; text-indent:0;"><strong>คำอธิบายตัวแปรและนัยสำคัญ:</strong> ดัชนีหักเหเป็นลบสำหรับ Left-Handed Metamaterials</p>
        </div>
            
        <div class="equation-box">
          <div class="equation-header">📌 สมการฟิสิกส์หลัก: กฎการหักเหของสเนลล์ทั่วไปสำหรับเมทาเซอร์เฟส (Generalized Snell's Law)</div>
          <div class="formula-math">$$n_t \sin\theta_t - n_i \sin\theta_i = \frac{\lambda_0}{2\pi} \frac{d\Phi}{dx}$$</div>
          <p style="font-size:9.5pt; margin:4px 0 0 0; color:#334155; line-height:1.75; text-indent:0;"><strong>คำอธิบายตัวแปรและนัยสำคัญ:</strong> การเบี่ยงเบนลำแสงด้วยการไล่ระดับเฟส dΦ/dx บนเมทาเซอร์เฟส</p>
        </div>
              </div>

      <div class="table-block">
        <h3>📊 ตารางเปรียบเทียบเทคโนโลยีทัศนศาสตร์ดั้งเดิมกับเมทาเซอร์เฟส</h3>
        <table class="data-table">
          <thead><tr>
            <th>คุณลักษณะ</th><th>เลนส์แก้วโค้งดั้งเดิม (Bulk Optics)</th><th>ผลึกโฟโทนิกส์ (Photonic Crystals)</th><th>เมทาเซอร์เฟส / เมทาเลนส์ (Flat Optics)</th></tr></thead>
<tbody><tr><td>กลไกควบคุมแสง</td><td>การสะสมเฟสตามความหนาแก้ว</td><td>การแทรกสอดเลี้ยวเบนของแลตทิซ</td><td>การเปลี่ยนเฟสฉับพลันด้วยเมทาอะตอม</td></tr><tr><td>ความหนาของอุปกรณ์</td><td>หลายมิลลิเมตรถึงเซนติเมตร</td><td>หลายสิบไมโครเมตร</td><td>บางเฉียบระดับนาโนเมตร (< 1 μm)</td></tr><tr><td>การผลิต</td><td>การขัดและหล่อแก้วความแม่นยำสูง</td><td>EBL / อาร์เรย์รูพรุน</td><td>กระบวนการ CMOS Semiconductor มาตรฐาน</td></tr><tr><td>ความคลาดสี (Chromatic Aberration)</td><td>ต้องใช้ชิ้นเลนส์หลายชิ้นแก้คลาด</td><td>สูง</td><td>แก้ความคลาดสีได้ในแผ่นเดี่ยว (Achromatic)</td></tr><tr><td>การรวมแสงข้ามขีดจำกัดเลี้ยวเบน</td><td>ทำไม่ได้ (จำกัดที่ λ/2NA)</td><td>ทำไม่ได้</td><td>ทำได้ (Super-Resolution Imaging)</td></tr></tbody></table>
</div>
  <div class="examples-group">

        <div class="example-box">
          <div class="example-header">
            <span>📝 ตัวอย่างการคำนวณที่ 6.9: การคำนวณมุมหักเหของแสงในวัสดุดัชนีหักเหเป็นลบ</span>
            <span style="background:#dcfce7; color:#15803d; font-size:8.5pt; padding:3px 10px; border-radius:4px; font-weight:700;">Step-by-Step Worked Solution</span>
          </div>
          <p style="text-indent:0; margin-bottom:10px;"><strong>โจทย์ปัญหา (Problem Statement):</strong><br>ลำแสงเลเซอร์ตกกระทบจากอากาศ ($n_1 = 1.0$) เข้าสู่วัสดุเมทาแมทีเรียลที่มี $\epsilon_r = -3.0$ และ $\mu_r = -3.0$ ด้วยมุมตกกระทบ $	heta_1 = 30.0^\circ$ จงคำนวณหา (ก) ดัชนีหักเห $n_2$ ของเมทาแมทีเรียล (ข) มุมหักเห $	heta_2$</p>
          <div style="background:rgba(255,255,255,0.85); border:1px solid #e2e8f0; padding:12px 16px; border-radius:6px; margin:12px 0;">
            <strong style="color:#1e3a8a;">การวิเคราะห์และการคำนวณอย่างละเอียด:</strong><br>
            <p style="text-indent:0; margin:6px 0 0 0; line-height:1.85;">1. $n_2 = -\sqrt{(-3.0)(-3.0)} = -\sqrt{9.0} = -3.0$<br>2. กฎของสเนลล์: $n_1 \sin\theta_1 = n_2 \sin\theta_2$<br>3. $1.0 \times \sin(30.0^\circ) = -3.0 \times \sin\theta_2 \implies 0.50 = -3.0 \sin\theta_2$<br>4. $\sin\theta_2 = -\frac{0.50}{3.0} = -0.1667 \implies \theta_2 = -9.59^\circ$</p>
          </div>
          <div style="background:#f0fdf4; border-left:4px solid #16a34a; padding:10px 14px; margin-top:10px; font-size:9.5pt; color:#166534; border-radius:0 6px 6px 0;">
            💡 <strong>นัยสำคัญทางกายภาพและการประยุกต์ใช้งาน (Physical Insight):</strong><br>
            <span style="color:#14532d;">มุมหักเหติดลบ $-9.59^\circ$ หมายความว่าลำแสงจะหักเหไปทางฝั่งเดียวกับเส้นแนวฉาก (Negative Refraction) ตรงข้ามกับวัสดุธรรมชาติ</span>
          </div>
        </div>
            
        <div class="example-box">
          <div class="example-header">
            <span>📝 ตัวอย่างการคำนวณที่ 6.1: การคำนวณการไล่ระดับเฟสสำหรับเมทาเลนส์โฟกัสแสง</span>
            <span style="background:#dcfce7; color:#15803d; font-size:8.5pt; padding:3px 10px; border-radius:4px; font-weight:700;">Step-by-Step Worked Solution</span>
          </div>
          <p style="text-indent:0; margin-bottom:10px;"><strong>โจทย์ปัญหา (Problem Statement):</strong><br>ต้องการออกแบบเมทาเลนส์ระนาบขนาดเส้นผ่านศูนย์กลาง $D = 1.0	ext{ mm}$ ความยาวโฟกัส $f = 2.0	ext{ mm}$ สำหรับความยาวคลื่น $\lambda = 532	ext{ nm}$ จงคำนวณหาการกระจายเฟส $\Phi(r)$ ที่ขอบเลนส์ ($r = 0.5	ext{ mm}$)</p>
          <div style="background:rgba(255,255,255,0.85); border:1px solid #e2e8f0; padding:12px 16px; border-radius:6px; margin:12px 0;">
            <strong style="color:#1e3a8a;">การวิเคราะห์และการคำนวณอย่างละเอียด:</strong><br>
            <p style="text-indent:0; margin:6px 0 0 0; line-height:1.85;">1. โปรไฟล์เฟสเป้าหมาย: $\Phi(r) = -\frac{2\pi}{\lambda} \left( \sqrt{r^2 + f^2} - f \right)$<br>2. ที่ขอบ $r = 0.5\text{ mm}$, $f = 2.0\text{ mm}$: $\sqrt{(0.5)^2 + (2.0)^2} - 2.0 = \sqrt{4.25} - 2.0 = 2.06155 - 2.0 = 0.06155\text{ mm} = 61.55\text{ }\mu\text{m}$<br>3. $\Phi(0.5\text{ mm}) = -\frac{2\pi}{0.532 \times 10^{-3}\text{ mm}} \times (0.06155\text{ mm}) = -231.39 \times 2\pi\text{ rad}$</p>
          </div>
          <div style="background:#f0fdf4; border-left:4px solid #16a34a; padding:10px 14px; margin-top:10px; font-size:9.5pt; color:#166534; border-radius:0 6px 6px 0;">
            💡 <strong>นัยสำคัญทางกายภาพและการประยุกต์ใช้งาน (Physical Insight):</strong><br>
            <span style="color:#14532d;">การปรับขนาดและรูปทรงของเสานาโน $	ext{TiO}_2$ ช่วยให้สามารถโปรแกรมเฟส $0$ ถึง $2\pi$ ได้อย่างแม่นยำตลอดแนวระนาบเลนส์</span>
          </div>
        </div>
              </div>
  <div class="code-group">

        <div class="code-box">
          <div class="code-header">💻 แบบจำลองเชิงคำนวณภาษาไพทอน (Computational Python 3.11): กรณีศึกษา: กล้องถ่ายภาพเมทาเลนส์แบนราบสำหรับสมาร์ทโฟนและแว่นตา AR/VR</div>
          <pre><code>การนำเทคโนโลยี Flat Metalens ที่ผลิตด้วยกระบวนการ DUV Lithography บนเวเฟอร์แก้วขนาด 12 นิ้ว มาใช้ในเซนเซอร์สแกนใบหน้า 3D (Face ID) และโมดูลกล้องสมาร์ทโฟน ช่วยลดความหนาของโมดูลกล้องลงกว่า 70% และขจัดปัญหากล้องนูนได้อย่างถาวร</code></pre>
        </div>
        <p style="font-size:9.5pt; color:#475569; margin-top:-6px; margin-bottom:18px; text-indent:0;"><em>คำอธิบายอัลกอริทึมการจำลอง:</em> สคริปต์ไพทอนสำหรับการคำนวณและจำลองเชิงตัวเลข</p>
              </div>
  <div class="lab-connection-block">
    <h3>🔬 การเชื่อมโยงสู่ห้องปฏิบัติการเสมือนจริงและเทคนิคการทดลอง (Virtual Lab Connection)</h3>
    <div style='background:#f0fdf4; border:1px solid #bbf7d0; border-left:5px solid #16a34a; padding:12px 16px; margin-bottom:14px; border-radius:6px;'><strong style='color:#166534; font-size:10.5pt;'>การจำลองการหักเหเป็นลบและโปรไฟล์เฟสของเมทาเลนส์</strong><p style='margin:6px 0 0 0; color:#14532d; text-indent:0; line-height:1.8;'>metalens_phase_profile.py</p></div>
  </div>
  <div class="cases-block">
    <h3>🌐 กรณีศึกษางานวิจัยแนวหน้าและนวัตกรรมอุตสาหกรรม (Frontier Case Studies)</h3>
    <div style='background:#eff6ff; border:1px solid #bfdbfe; border-left:5px solid #2563eb; padding:12px 16px; margin-bottom:14px; border-radius:6px;'><strong style='color:#1e40af; font-size:10.5pt;'>การเชื่อมโยงกับ Virtual Lab 30: การจำลองเมทาแมทีเรียล ดัชนีหักเหเป็นลบ และเมทาเลนส์</strong><p style='margin:6px 0 0 0; color:#1e3a8a; text-indent:0; line-height:1.8;'>ผู้เรียนสามารถปรับค่า $\epsilon$ และ $\mu$ ให้เป็นลบใน Lab 30 สังเกตเส้นทางเดินแสงหักเหย้อนกลับ และออกแบบ Flat Metalens รวมแสงเลเซอร์</p></div>
  </div>

      <div class="checkpoint-box" style="background:#fefce8; border:1px solid #fef08a; border-left:5px solid #eab308; padding:14px 18px; margin:24px 0 35px 0; border-radius:6px; page-break-inside:avoid;">
        <strong style="color:#854d0e; font-size:10pt;">🎯 จุดตรวจประเมินความเข้าใจและคำถามทบทวนประจำหัวข้อ 6.5 (Concept Checkpoint)</strong>
        <ul style="margin:8px 0 0 0; padding-left:20px; color:#713f12; font-size:9.5pt; line-height:1.8;">
          <li>จงอธิบายแนวคิดรวบยอดหลักของ เมทาแมทีเรียลระดับนาโนและโฟโทนิกส์ผลึก และความแตกต่างจากพฤติกรรมในระดับมหภาค</li>
          <li>พารามิเตอร์ใดเป็นปัจจัยวิกฤตที่ควบคุมสมบัติทางฟิสิกส์ในหัวข้อนี้ และมีผลกระทบอย่างไร?</li>
          <li>เชื่อมโยงหลักการฟิสิกส์ในหัวข้อนี้เข้ากับการประยุกต์ใช้จริงในเทคโนโลยีสมัยใหม่</li>
        </ul>
      </div>
    </div>
    

      <div class="summary-box">
        <h3 style="color:#1e40af; margin-top:0; font-size:13pt;">📋 สรุปสาระสำคัญประจำบทที่ 6 (Chapter 6 Key Takeaways)</h3>
        <ul style="margin:0; padding-left:22px; font-size:10pt; line-height:1.95; color:#1e293b;">
          <li style='margin-bottom:8px;'>สถาปัตยกรรม Gate-All-Around (GAAFET) โอบล้อมช่องนำกระแส 4 ด้าน ช่วยลดความยาวสเกลธรรมชาติ $\lambda$ และป้องกัน Short-Channel Effects</li><li style='margin-bottom:8px;'>สปินทรอนิกส์ใช้สปินของอิเล็กตรอนผ่านปรากฏการณ์ GMR และ TMR ใน MTJ นำไปสู่หน่วยความจำความเร็วสูง STT-MRAM ที่ไม่สูญหายเมื่อตัดไฟ</li><li style='margin-bottom:8px;'>นาโนพลาสมอนิกส์และ LSPR สามารถบีบอัดพลังงานแสงลงสู่สเกลต่ำกว่าขีดจำกัดเลี้ยวเบน และตอบสนองต่อดัชนีหักเหสำหรับไบโอเซนเซอร์</li><li style='margin-bottom:8px;'>เทคนิค SERS ขยายสัญญาณรามานได้ถึง $10^{12} - 10^{14}$ เท่า ผ่าน Plasmonic Hot-Spots ตามกฎ $|E_{	ext{loc}}/E_0|^4$ สำหรับตรวจวัดโมเลกุลเดี่ยว</li><li style='margin-bottom:8px;'>เมทาแมทีเรียลที่มีดัชนีหักเหเป็นลบ ($n < 0$) และเมทาเซอร์เฟสบางเฉียบ นำไปสู่การปฏิวัติ Flat Metalenses สำหรับสมาร์ทโฟนและ AR/VR</li>
        </ul>
      </div>

      <div class="problems-section">
        <h3 style="color:#0f172a; margin-top:0; font-size:14pt; border-bottom:2px solid #cbd5e1; padding-bottom:8px;">
          📚 แบบฝึกหัดและโจทย์ปัญหาท้ายบทที่ 6 (End-of-Chapter Problems)
        </h3>
        
        <h4 style="color:#1e3a8a; font-size:11.5pt; margin-top:18px;">ตอนที่ 1: คำถามเชิงมโนทัศน์และการวิเคราะห์เชิงฟิสิกส์ (Conceptual & Analytical Questions)</h4>
        <ol style="padding-left:22px; font-size:10pt; line-height:1.9; color:#334155;">
          <li style='margin-bottom:8px;'>จงอธิบายผลกระทบ Short-Channel Effects (SCEs) และ Drain-Induced Barrier Lowering (DIBL) ในทรานซิสเตอร์นาโน</li><li style='margin-bottom:8px;'>เพราะเหตุใดสถาปัตยกรรม GAAFET จึงสามารถควบคุมไฟฟ้าสถิตได้ดีกว่า FinFET และ Planar MOSFET?</li><li style='margin-bottom:8px;'>จงอธิบายแบบจำลอง Mott Two-Current Model สำหรับปรากฏการณ์ GMR ในชั้นโลหะแม่เหล็กเฟอร์โร</li><li style='margin-bottom:8px;'>กระบวนการ Spin-Transfer Torque (STT) สามารถพลิกทิศทางแม่เหล็กในเซลล์ MRAM ได้อย่างไร?</li><li style='margin-bottom:8px;'>เงื่อนไขฟรอยลิช (Fröhlich Criterion) คืออะไร และสัมพันธ์กับการเกิดพีค LSPR อย่างไร?</li><li style='margin-bottom:8px;'>จงอธิบายกลไกที่ทำให้เกิด Plasmonic Hot-Spots ในช่องว่างระหว่างอนุภาคคู่ทองคำ</li><li style='margin-bottom:8px;'>เพราะเหตุใดสัญญาณ SERS จึงขยายตัวตามกำลังสี่ของสนามไฟฟ้าเฉพาะที่ ($|E_{	ext{loc}}|^4$)?</li><li style='margin-bottom:8px;'>จงอธิบายความหมายทางฟิสิกส์ของดัชนีหักเหเป็นลบ ($n < 0$) และทิศทางของเวกเตอร์พอยน์ติง</li>
        </ol>

        <h4 style="color:#166534; font-size:11.5pt; margin-top:22px;">ตอนที่ 2: โจทย์ปัญหาการคำนวณเชิงตัวเลขและการพิสูจน์ (Quantitative & Numerical Problems)</h4>
        <ol style="padding-left:22px; font-size:10pt; line-height:1.9; color:#334155;">
          <li style='margin-bottom:8px;'>คำนวณความยาวสเกลธรรมชาติ $\lambda_{	ext{GAA}}$ ของลวดนาโนซิลิคอน ($d = 4.0	ext{ nm}$, $\epsilon_{	ext{ch}} = 11.7$) หุ้มด้วย $	ext{HfO}_2$ ($t_{	ext{ox}} = 1.5	ext{ nm}$, $\epsilon_{	ext{ox}} = 22.0$)</li><li style='margin-bottom:8px;'>คำนวณอัตราส่วน TMR ของรอยต่อ MTJ ที่มีค่าสปินโพลาไรเซชัน $P_1 = 0.75$ และ $P_2 = 0.70$</li><li style='margin-bottom:8px;'>เซลล์ STT-MRAM ขนาดพื้นที่ $8.0 	imes 10^{-16}	ext{ m}^2$ ต้องการความหนาแน่นกระแส $J_{c0} = 3.0 	imes 10^6	ext{ A/cm}^2$ จงคำนวณกระแสสวิตชิ่ง $I_{c0}$</li><li style='margin-bottom:8px;'>อนุภาคนาโนเงินมี $\hbar \omega_p = 9.01	ext{ eV}$ แขวนลอยในน้ำ ($\epsilon_d = 1.777$) จงคำนวณหาพลังงานและตำแหน่งพีค $\lambda_{	ext{LSPR}}$ (สมมติ $\epsilon_\infty = 4.0$)</li><li style='margin-bottom:8px;'>ที่จุด Hot-Spot มีสนามไฟฟ้าเข้มข้น $|E_{	ext{loc}}| = 300 E_0$ จงคำนวณหาปัจจัยการขยายสัญญาณ $	ext{EF}_{	ext{EM}}$</li><li style='margin-bottom:8px;'>ลำแสงตกกระทบจากอากาศ ($n_1 = 1.0$) เข้าสู่เมทาแมทีเรียล ($n_2 = -2.0$) ด้วยมุม $45^\circ$ จงคำนวณหามุมหักเห $	heta_2$</li><li style='margin-bottom:8px;'>คำนวณกำลังไฟฟ้าสูญเสียไดนามิกของชิป GAAFET ที่ประกอบด้วย 2 หมื่นล้านเกต ทำงานที่ $V_{dd} = 0.65	ext{ V}$, $C_g = 0.4	ext{ fF}$, $f = 3.5	ext{ GHz}$ และมี Activity Factor $lpha = 0.1$</li>
        </ol>

        <h4 style="color:#7c2d12; font-size:11.5pt; margin-top:22px;">ตอนที่ 3: โจทย์ประยุกต์ การออกแบบเชิงวิศวกรรม และการจำลอง (Applied Design & Modeling Problems)</h4>
        <ol style="padding-left:22px; font-size:10pt; line-height:1.9; color:#334155;">
          <li style='margin-bottom:8px;'>จงออกแบบวงจรหน่วยความจำ STT-MRAM ขนาด 1 Gbit โดยระบุโครงสร้างชั้นฟิล์ม MTJ, ความหนาของฉนวน MgO และวงจรอ่าน-เขียน</li><li style='margin-bottom:8px;'>ออกแบบแผ่นชิปไบโอเซนเซอร์ SERS ชนิดพกพาสำหรับการตรวจคัดกรองไวรัสในเลือดระดับความไวสูง</li><li style='margin-bottom:8px;'>วิเคราะห์แนวทางการออกแบบ Flat Metalens ความกว้างช่องเปิด $	ext{NA} = 0.8$ สำหรับกล้องถ่ายภาพความละเอียดสูงระดับ 8K</li><li style='margin-bottom:8px;'>เขียนโค้ด Python เพื่อจำลองการกระจายตัวของสนามไฟฟ้าพลาสมอนิกส์รอบอนุภาคคู่ไดเมอร์ทองคำที่ระยะห่างช่องว่างต่างๆ</li>
        </ol>
      </div>
    </div>
    """
