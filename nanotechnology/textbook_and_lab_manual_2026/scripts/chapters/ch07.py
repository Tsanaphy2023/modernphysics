# -*- coding: utf-8 -*-
"""
Chapter 7: นาโนเทคโนโลยีชีวภาพและนาโนการแพทย์แม่นยำ
Bionanotechnology, Lipid Nanoparticles (LNPs), mRNA Delivery, Bio-QDs, Magnetic Hyperthermia & DNA Nanorobotics
"""

def get_chapter_7():
    return r"""
    <div class="chapter-container">
      <div class="chapter-hero">
        <div class="chapter-badge">CHAPTER 07 • NANOTECHNOLOGICAL PHYSICS</div>
        <h1 class="chapter-title">นาโนเทคโนโลยีชีวภาพและนาโนการแพทย์แม่นยำ</h1>
        <p class="chapter-subtitle">Bionanotechnology, Lipid Nanoparticles (LNPs), mRNA Delivery, Bio-QDs, Magnetic Hyperthermia & DNA Nanorobotics</p>
      </div>

      <div class="diagram-wrap">
        <img src="../assets/diagrams/ch07_nanomedicine.svg" alt="นาโนเทคโนโลยีชีวภาพและนาโนการแพทย์แม่นยำ">
        <div class="caption">ภาพที่ 7.1 แผนผังโครงสร้าง LNP นำส่ง mRNA, กลไก FRET ในจุดควอนตัม, การบำบัดด้วยความร้อน SPIONs และกล่องนาโนโรบอตดีเอ็นเอ</div>
      </div>

      
    <div class="topic-section">
      <h2>7.1 อนุภาคนาโนไขมัน (LNPs) และระบบนำส่งยาชีวโมเลกุล mRNA</h2>
      <div class="topic-en-title">(Lipid Nanoparticles (LNPs), mRNA Delivery & Endosomal Escape)</div>
      
      <div class="topic-intro">
        <p>อนุภาคนาโนไขมัน (Lipid Nanoparticles: LNPs) เป็นเทคโนโลยีตัวนำส่งยาและสารพันธุกรรมระดับนาโนที่ประสบความสำเร็จสูงสุดในประวัติศาสตร์การแพทย์ยุคใหม่ โดยเป็นหัวใจสำคัญของวัคซีน mRNA ป้องกันโรคโควิด-19 (BNT162b2 และ mRNA-1273) และการบำบัดรักษาโรคทางพันธุกรรมด้วยการแก้ไขยีน (CRISPR-Cas9 In Vivo Delivery)</p>
    <p>โครงสร้าง LNP ทั่วไปมีขนาดเส้นผ่านศูนย์กลางเฉลี่ย $60 - 100	ext{ nm}$ ประกอบด้วยส่วนผสมของโมเลกุลไขมัน 4 ชนิดในอัตราส่วนที่แม่นยำ ได้แก่: ไขมันไอออนไนซ์ได้ (Ionizable Cationic Lipid), ไขมันตัวช่วย (Helper Phospholipid เช่น DSPC), คอเลสเตอรอล (Cholesterol สำหรับเพิ่มความเสถียรของโครงสร้าง), และไขมัน PEGylated (PEG-lipid สำหรับป้องกันการเกาะกลุ่มและยืดระยะเวลาไหลเวียนในกระแสเลือด)</p>
    <p>ความมหัศจรรย์ของ Ionizable Lipid อยู่ที่ค่า $	ext{p}K_a pprox 6.0 - 6.8$ ซึ่งจะมีประจุบวกที่สภาวะกรดอ่อน ($	ext{pH} pprox 4.0$) ในกระบวนการผลิตเพื่อจับกับสาย mRNA ที่มีประจุลบ แต่จะเปลี่ยนเป็นกลางทางไฟฟ้าที่ค่า $	ext{pH}$ ปกติของกระแสเลือด ($	ext{pH} pprox 7.4$) เพื่อลดความเป็นพิษต่อเซลล์ และกลับมามีประจุบวกอีกครั้งภายในถุงเอนโดโซม ($	ext{pH} pprox 5.0 - 5.5$) เพื่อทำลายเยื่อหุ้มเอนโดโซมและปลดปล่อย mRNA เข้าสู่ไซโตพลาสซึม (Endosomal Escape)</p>
  </div>

      <div class="subtopic-block">
        <h3>องค์ประกอบและสัดส่วนโมลาร์ของอนุภาค LNP มาตรฐาน</h3>
            <p>1. Ionizable Lipid (เช่น ALC-0315 หรือ SM-102, $\sim 46 - 50	ext{ mol}\%$): ทำหน้าที่ห่อหุ้ม mRNA และช่วยการหลุดรอดจากเอนโดโซม</p>
    <p>2. DSPC ($\sim 10	ext{ mol}\%$): สร้างโครงสร้างสองชั้นแบบ Lamellar รอบนอก</p>
    <p>3. Cholesterol ($\sim 38 - 40	ext{ mol}\%$): เพิ่มความแข็งแรงและความยืดหยุ่นของโครงสร้างแกนกลาง</p>
    <p>4. PEG-Lipid (เช่น ALC-0159 หรือ DMG-PEG2000, $\sim 1.5	ext{ mol}\%$): ควบคุมขนาดอนุภาคและป้องกันการถูกกลืนกินโดยระบบภูมิคุ้มกัน RES</p>
  </div>

      <div class="subtopic-block">
        <h3>ฟิสิกส์ของการเกิดสารเชิงซ้อนและกระบวนการ Microfluidic Mixing</h3>
            <p>การผสมสารละลายไขมันในเอทานอลเข้ากับสารละลาย mRNA ในบัฟเฟอร์ซิเตรต ($	ext{pH } 4.0$) อย่างรวดเร็วด้วยอุปกรณ์ Microfluidic Chaotic Mixer ที่มีอัตราส่วนการไหล $1:3$ ทำให้เกิดการรวมตัวแบบ Self-Assembly ที่รวดเร็ว ได้อนุภาคที่มีการกระจายขนาดแคบ (PDI $< 0.1$)</p>
  </div>
  <div class="formula-group">

        <div class="equation-box">
          <div class="equation-header">📌 สมการฟิสิกส์หลัก: อัตราส่วนประจุไนโตรเจนต่อฟอสเฟต (N/P Ratio)</div>
          <div class="formula-math">$$\text{N/P} = \frac{\text{โมลของไนโตรเจนประจุบวกใน Ionizable Lipid}}{\text{โมลของฟอสเฟตประจุลบใน mRNA}} \approx 4.0 - 6.0$$</div>
          <p style="font-size:9.5pt; margin:4px 0 0 0; color:#334155; line-height:1.75; text-indent:0;"><strong>คำอธิบายตัวแปรและนัยสำคัญ:</strong> อัตราส่วนประจุที่เหมาะสมที่สุดสำหรับการห่อหุ้ม</p>
        </div>
            
        <div class="equation-box">
          <div class="equation-header">📌 สมการฟิสิกส์หลัก: สมการเฮนเดอร์สัน-ฮัสเซลบัลค์สำหรับ Ionizable Lipids</div>
          <div class="formula-math">$$\text{pH} = \text{p}K_a + \log_{10}\left( \frac{[\text{Lipid}^0]}{[\text{Lipid}^+]} \right)$$</div>
          <p style="font-size:9.5pt; margin:4px 0 0 0; color:#334155; line-height:1.75; text-indent:0;"><strong>คำอธิบายตัวแปรและนัยสำคัญ:</strong> การคำนวณสัดส่วนประจุของไขมันตามค่า pH ของสิ่งแวดล้อม</p>
        </div>
              </div>

      <div class="table-block">
        <h3>📊 ตารางสูตรส่วนประกอบวัคซีน mRNA-LNP ที่ผ่านการอนุมัติระดับโลก</h3>
        <table class="data-table">
          <thead><tr>
            <th>ส่วนประกอบ LNP</th><th>วัคซีน Pfizer/BioNTech (BNT162b2)</th><th>วัคซีน Moderna (mRNA-1273)</th><th>หน้าที่หลัก</th></tr></thead>
<tbody><tr><td>Ionizable Lipid (mol%)</td><td>ALC-0315 (46.3%)</td><td>SM-102 (50.0%)</td><td>จับ mRNA และทำลายเยื่อหุ้มเอนโดโซม</td></tr><tr><td>Phospholipid (mol%)</td><td>DSPC (9.4%)</td><td>DSPC (10.0%)</td><td>สร้างโครงสร้างเยื่อหุ้ม</td></tr><tr><td>Cholesterol (mol%)</td><td>Cholesterol (42.7%)</td><td>Cholesterol (38.5%)</td><td>เพิ่มความคงตัวทางโครงสร้าง</td></tr><tr><td>PEG-Lipid (mol%)</td><td>ALC-0159 (1.6%)</td><td>PEG2000-DMG (1.5%)</td><td>ป้องกันการจับกลุ่ม ยืดอายุในกระแสเลือด</td></tr><tr><td>ขนาดอนุภาคเฉลี่ย</td><td>70 - 90 nm</td><td>80 - 100 nm</td><td>ขนาดที่เหมาะสมต่อการเข้าสู่ต่อมน้ำเหลือง</td></tr></tbody></table>
</div>
  <div class="examples-group">

        <div class="example-box">
          <div class="example-header">
            <span>📝 ตัวอย่างการคำนวณที่ 7.1: การคำนวณสัดส่วนโมเลกุลที่มีประจุบวกของ Ionizable Lipid ที่ pH ต่างๆ</span>
            <span style="background:#dcfce7; color:#15803d; font-size:8.5pt; padding:3px 10px; border-radius:4px; font-weight:700;">Step-by-Step Worked Solution</span>
          </div>
          <p style="text-indent:0; margin-bottom:10px;"><strong>โจทย์ปัญหา (Problem Statement):</strong><br>ไขมันไอออนไนซ์ได้ SM-102 มีค่า $	ext{p}K_a = 6.75$ จงคำนวณหาร้อยละของโมเลกุลที่มีประจุบวก ($\% 	ext{Lipid}^+$) ที่ (ก) สภาวะการผลิตในกรด $	ext{pH} = 4.5$ (ข) กระแสเลือด $	ext{pH} = 7.4$ (ค) ภายในเอนโดโซม $	ext{pH} = 5.5$</p>
          <div style="background:rgba(255,255,255,0.85); border:1px solid #e2e8f0; padding:12px 16px; border-radius:6px; margin:12px 0;">
            <strong style="color:#1e3a8a;">การวิเคราะห์และการคำนวณอย่างละเอียด:</strong><br>
            <p style="text-indent:0; margin:6px 0 0 0; line-height:1.85;">1. จากสมการ: $\frac{[\text{Lipid}^+]}{[\text{Lipid}_{\text{total}}]} = \frac{1}{1 + 10^{\text{pH} - \text{p}K_a}} \times 100\%$<br>2. ที่ $\text{pH} = 4.5$: $\Delta = 4.5 - 6.75 = -2.25 \implies \frac{1}{1 + 10^{-2.25}} = \frac{1}{1 + 0.0056} = 99.44\%$ (ประจุบวกเกือบ 100% จับ mRNA ได้แน่นหนา)<br>3. ที่ $\text{pH} = 7.4$: $\Delta = 7.4 - 6.75 = +0.65 \implies \frac{1}{1 + 10^{0.65}} = \frac{1}{1 + 4.467} = 18.29\%$ (ประจุเป็นกลางสูง ลดความเป็นพิษในเลือด)<br>4. ที่ $\text{pH} = 5.5$: $\Delta = 5.5 - 6.75 = -1.25 \implies \frac{1}{1 + 10^{-1.25}} = \frac{1}{1 + 0.0562} = 94.68\%$ (กลับมามีประจุบวกสูง ทำลายผนังเอนโดโซม)</p>
          </div>
          <div style="background:#f0fdf4; border-left:4px solid #16a34a; padding:10px 14px; margin-top:10px; font-size:9.5pt; color:#166534; border-radius:0 6px 6px 0;">
            💡 <strong>นัยสำคัญทางกายภาพและการประยุกต์ใช้งาน (Physical Insight):</strong><br>
            <span style="color:#14532d;">พฤติกรรมการเปลี่ยนประจุตามค่า pH นี้ช่วยให้ LNP นำส่ง mRNA ได้อย่างปลอดภัยและมีประสิทธิภาพสูงสุด</span>
          </div>
        </div>
            
        <div class="example-box">
          <div class="example-header">
            <span>📝 ตัวอย่างการคำนวณที่ 7.2: การคำนวณมวลของ Ionizable Lipid ที่ต้องใช้สำหรับ N/P Ratio = 6.0</span>
            <span style="background:#dcfce7; color:#15803d; font-size:8.5pt; padding:3px 10px; border-radius:4px; font-weight:700;">Step-by-Step Worked Solution</span>
          </div>
          <p style="text-indent:0; margin-bottom:10px;"><strong>โจทย์ปัญหา (Problem Statement):</strong><br>ต้องการผลิตวัคซีนที่มี mRNA ขนาด $m_{	ext{mRNA}} = 30.0	ext{ }\mu	ext{g}$ กำหนดมวลโมลาร์เฉลี่ยของนิวคลีโอไทด์ $M_{	ext{nt}} pprox 330	ext{ g/mol}$ และใช้ไขมัน ALC-0315 ($M_{	ext{lipid}} = 766.3	ext{ g/mol}$, 1 ไนโตรเจนต่อโมเลกุล) จงคำนวณหามวลของ ALC-0315 ที่ต้องใช้</p>
          <div style="background:rgba(255,255,255,0.85); border:1px solid #e2e8f0; padding:12px 16px; border-radius:6px; margin:12px 0;">
            <strong style="color:#1e3a8a;">การวิเคราะห์และการคำนวณอย่างละเอียด:</strong><br>
            <p style="text-indent:0; margin:6px 0 0 0; line-height:1.85;">1. จำนวนโมลของฟอสเฟตใน mRNA: $n_P = \frac{30.0 \times 10^{-6}\text{ g}}{330\text{ g/mol}} = 9.091 \times 10^{-8}\text{ โมล}$<br>2. โมลไนโตรเจนที่ต้องใช้สำหรับ $\text{N/P} = 6.0$: $n_N = 6.0 \times n_P = 6.0 \times (9.091 \times 10^{-8}) = 5.455 \times 10^{-7}\text{ โมล}$<br>3. มวลของ ALC-0315: $m = n_N \times M_{\text{lipid}} = (5.455 \times 10^{-7}\text{ โมล}) \times (766.3\text{ g/mol}) = 4.180 \times 10^{-4}\text{ g} = 418.0\text{ }\mu\text{g}$</p>
          </div>
          <div style="background:#f0fdf4; border-left:4px solid #16a34a; padding:10px 14px; margin-top:10px; font-size:9.5pt; color:#166534; border-radius:0 6px 6px 0;">
            💡 <strong>นัยสำคัญทางกายภาพและการประยุกต์ใช้งาน (Physical Insight):</strong><br>
            <span style="color:#14532d;">ต้องใช้ไขมัน ALC-0315 ปริมาณ $418.0	ext{ }\mu	ext{g}$ ต่อโดสวัคซีน เพื่อให้ได้ประสิทธิภาพการห่อหุ้ม $> 95\%$</span>
          </div>
        </div>
              </div>
  <div class="code-group">

        <div class="code-box">
          <div class="code-header">💻 แบบจำลองเชิงคำนวณภาษาไพทอน (Computational Python 3.11): กรณีศึกษา: การบำบัดรักษาโรคทางพันธุกรรม Transthyretin Amyloidosis (ATTR) ด้วย LNP-CRISPR (Intellia Therapeutics)</div>
          <pre><code>การฉีดอนุภาค LNP ที่บรรจุทั้ง Cas9 mRNA และ single guide RNA เข้าสู่กระแสเลือดโดยตรง เพื่อกำหนดยีนกลายพันธุ์ในตับของผู้ป่วยได้อย่างแม่นยำ ช่วยลดโปรตีนก่อโรคลงได้มากกว่า 87% ในการทดลองทางคลินิก</code></pre>
        </div>
        <p style="font-size:9.5pt; color:#475569; margin-top:-6px; margin-bottom:18px; text-indent:0;"><em>คำอธิบายอัลกอริทึมการจำลอง:</em> สคริปต์ไพทอนสำหรับการคำนวณและจำลองเชิงตัวเลข</p>
              </div>
  <div class="lab-connection-block">
    <h3>🔬 การเชื่อมโยงสู่ห้องปฏิบัติการเสมือนจริงและเทคนิคการทดลอง (Virtual Lab Connection)</h3>
    <div style='background:#f0fdf4; border:1px solid #bbf7d0; border-left:5px solid #16a34a; padding:12px 16px; margin-bottom:14px; border-radius:6px;'><strong style='color:#166534; font-size:10.5pt;'>การจำลองกระบวนการหลุดรอดจากเอนโดโซมของ LNP</strong><p style='margin:6px 0 0 0; color:#14532d; text-indent:0; line-height:1.8;'>lnp_endosomal_escape.py</p></div>
  </div>
  <div class="cases-block">
    <h3>🌐 กรณีศึกษางานวิจัยแนวหน้าและนวัตกรรมอุตสาหกรรม (Frontier Case Studies)</h3>
    <div style='background:#eff6ff; border:1px solid #bfdbfe; border-left:5px solid #2563eb; padding:12px 16px; margin-bottom:14px; border-radius:6px;'><strong style='color:#1e40af; font-size:10.5pt;'>การเชื่อมโยงกับ Virtual Lab 31: การจำลองการประกอบตัวของอนุภาคนาโนไขมัน LNP และระบบนำส่ง mRNA</strong><p style='margin:6px 0 0 0; color:#1e3a8a; text-indent:0; line-height:1.8;'>ผู้เรียนสามารถควบคุมอัตราส่วนการไหลใน Microfluidic Chip, ปรับ N/P Ratio และวัดค่าการห่อหุ้ม Encapsulation Efficiency ใน Lab 31</p></div>
  </div>

      <div class="checkpoint-box" style="background:#fefce8; border:1px solid #fef08a; border-left:5px solid #eab308; padding:14px 18px; margin:24px 0 35px 0; border-radius:6px; page-break-inside:avoid;">
        <strong style="color:#854d0e; font-size:10pt;">🎯 จุดตรวจประเมินความเข้าใจและคำถามทบทวนประจำหัวข้อ 7.1 (Concept Checkpoint)</strong>
        <ul style="margin:8px 0 0 0; padding-left:20px; color:#713f12; font-size:9.5pt; line-height:1.8;">
          <li>จงอธิบายแนวคิดรวบยอดหลักของ อนุภาคนาโนไขมัน (LNPs) และระบบนำส่งยาชีวโมเลกุล mRNA และความแตกต่างจากพฤติกรรมในระดับมหภาค</li>
          <li>พารามิเตอร์ใดเป็นปัจจัยวิกฤตที่ควบคุมสมบัติทางฟิสิกส์ในหัวข้อนี้ และมีผลกระทบอย่างไร?</li>
          <li>เชื่อมโยงหลักการฟิสิกส์ในหัวข้อนี้เข้ากับการประยุกต์ใช้จริงในเทคโนโลยีสมัยใหม่</li>
        </ul>
      </div>
    </div>
    
    <div class="topic-section">
      <h2>7.2 จุดควอนตัมชีวภาพและการสร้างภาพระดับเซลล์</h2>
      <div class="topic-en-title">(Biocompatible Quantum Dots, Bio-Imaging & Multiplexing)</div>
      
      <div class="topic-intro">
        <p>จุดควอนตัมชีวภาพ (Biocompatible Quantum Dots) ได้กลายมาเป็นหัววัดเรืองแสงยุคใหม่ (Fluorescent Probes) ที่เข้ามาปฏิวัติการสร้างภาพทางชีวการแพทย์ (Bio-imaging) และการวินิจฉัยโรคระดับเซลล์ โดยก้าวข้ามข้อจำกัดของสีย้อมอินทรีย์ดั้งเดิม (Organic Dyes) และโปรตีนเรืองแสง GFP</p>
    <p>จุดเด่นอันเป็นเอกลักษณ์ของจุดควอนตัมคือ: สเปกตรัมการดูดกลืนแสงที่กว้างต่อเนื่องในย่าน UV แต่มีสเปกตรัมการเปล่งแสงที่แคบ สมมาตร และปรับแต่งได้ตามขนาด (Narrow Emission FWHM $< 30	ext{ nm}$), ความสว่างของสัญญาณเรืองแสงสูงกว่าสีย้อมอินทรีย์ 20 ถึง 100 เท่า, และที่สำคัญที่สุดคือ ความทนทานต่อการฟอกจางด้วยแสง (Photostability) ที่สูงกว่าเดิมนับพันเท่า ทำให้สามารถบันทึกวิดีโอติดตามชีวโมเลกุลเดี่ยวได้ต่อเนื่องยาวนานหลายชั่วโมง</p>
    <p>เพื่อความปลอดภัยต่อเซลล์สิ่งมีชีวิต ได้มีการพัฒนา จุดควอนตัมปลอดสารพิษ (Cadmium-Free Quantum Dots เช่น $	ext{InP/ZnS}$, $	ext{AgInS}_2$, และ Carbon/Graphene Dots) ที่เคลือบผิวด้วยพอลิเมอร์ชอบน้ำและโมเลกุลชีวภาพเป้าหมาย (Antibodies, Peptides) เพื่อการวินิจฉัยมะเร็งแบบมัลติเพล็กซ์ (Multiplexed Imaging) ที่สามารถตรวจหาตัวบ่งชี้มะเร็ง 5 ชนิดได้พร้อมกันด้วยแหล่งกำเนิดแสงเลเซอร์เพียงความยาวคลื่นเดียว</p>
  </div>

      <div class="subtopic-block">
        <h3>โครงสร้างคอร์-เชลล์-เชลล์ (Core-Shell-Shell) และการดัดแปรพื้นผิว (Surface Bioconjugation)</h3>
            <p>1. แกนผลึก (Core เช่น InP หรือ AgInS2): ทำหน้าที่กำหนดความยาวคลื่นการเปล่งแสงตามผลการกักขังควอนตัม</p>
    <p>2. ชั้นเปลือกป้องกัน (Shell เช่น ZnSe/ZnS): ป้องกันการสูญเสียพลังงานแบบไร้รังสีที่ผิว (Passivation) เพิ่ม Quantum Yield $> 80\%$</p>
    <p>3. ชั้นห่อหุ้มชีวภาพ (Hydrophilic Polymer Coating): เคลือบด้วย PEG หรือ Amphiphilic Polymer เพื่อป้องกันการสะสมประจุและทำให้ละลายในน้ำได้ดี</p>
    <p>4. แขนต่อชีวภาพ (Bioconjugation via EDC/NHS Chemistry): ติดโมเลกุลแอนติบอดีหรือกรดโฟลิก (Folic Acid) เพื่อจับกับตัวรับบนผิวเซลล์มะเร็งอย่างจำเพาะเจาะจง</p>
  </div>

      <div class="subtopic-block">
        <h3>การสร้างภาพในย่านหน้าต่างชีวภาพใกล้อินฟราเรด (NIR-II Window: 1000 - 1700 nm)</h3>
            <p>การใช้จุดควอนตัม $	ext{Ag}_2	ext{S}$ หรือ $	ext{PbS}$ ที่เปล่งแสงในย่าน NIR-II ช่วยให้แสงสามารถทะลุผ่านผิวหนังและเนื้อเยื่อได้ลึกกว่า 1 เซนติเมตร โดยมีการกระเจิงและการเรืองแสงพื้นหลังของเนื้อเยื่อ (Autofluorescence) ต่ำที่สุด</p>
  </div>
  <div class="formula-group">

        <div class="equation-box">
          <div class="equation-header">📌 สมการฟิสิกส์หลัก: ความสว่างเชิงแสงสัมพัทธ์ของจุดควอนตัม</div>
          <div class="formula-math">$$B = \epsilon(\lambda_{\text{ex}}) \times \Phi_{\text{PL}} \approx 10^5 - 10^6\text{ M}^{-1}\text{cm}^{-1}$$</div>
          <p style="font-size:9.5pt; margin:4px 0 0 0; color:#334155; line-height:1.75; text-indent:0;"><strong>คำอธิบายตัวแปรและนัยสำคัญ:</strong> ความสว่างแปรผันตามสัมประสิทธิ์การดูดกลืนและ Quantum Yield</p>
        </div>
            
        <div class="equation-box">
          <div class="equation-header">📌 สมการฟิสิกส์หลัก: ประสิทธิภาพการถ่ายโอนพลังงานเรโซแนนซ์ฟอร์สเตอร์ (FRET)</div>
          <div class="formula-math">$$E_{\text{FRET}} = \frac{R_0^6}{R_0^6 + r^6}, \qquad R_0 \approx 4 - 6\text{ nm}$$</div>
          <p style="font-size:9.5pt; margin:4px 0 0 0; color:#334155; line-height:1.75; text-indent:0;"><strong>คำอธิบายตัวแปรและนัยสำคัญ:</strong> FRET ระหว่างจุดควอนตัมตัวให้และสีย้อมตัวรับ</p>
        </div>
              </div>

      <div class="table-block">
        <h3>📊 ตารางเปรียบเทียบคุณสมบัติระหว่าง Organic Dyes, GFP และ Quantum Dots</h3>
        <table class="data-table">
          <thead><tr>
            <th>คุณสมบัติ</th><th>สีย้อมอินทรีย์ (Organic Dyes)</th><th>โปรตีนเรืองแสง (GFP)</th><th>จุดควอนตัมชีวภาพ (Bio-QDs)</th></tr></thead>
<tbody><tr><td>ความกว้างสเปกตรัมเปล่งแสง (FWHM)</td><td>กว้าง (50 - 100 nm) มีหางเบ้</td><td>กว้าง (~ 50 nm)</td><td>แคบมาก สมมาตร (20 - 30 nm)</td></tr><tr><td>สเปกตรัมการดูดกลืน</td><td>แคบ (ต้องใช้เลเซอร์จำเพาะ)</td><td>แคบ</td><td>กว้างต่อเนื่อง (ใช้เลเซอร์เดียวตื่นตัวทุกสี)</td></tr><tr><td>ความทนต่อการฟอกจาง (Photostability)</td><td>ต่ำ (ฟอกจางในไม่กี่วินาที)</td><td>ปานกลาง (ฟอกจางในไม่กี่นาที)</td><td>สูงมาก (> หลายชั่วโมง ไม่ฟอกจาง)</td></tr><tr><td>ความสว่าง (Brightness)</td><td>1×</td><td>0.5×</td><td>20× - 100×</td></tr><tr><td>ความสามารถตรวจวัดหลายสี (Multiplexing)</td><td>จำกัด (1-3 สี สเปกตรัมซ้อนทับ)</td><td>จำกัด (2-3 สี)</td><td>ดีเยี่ยม (> 5-10 สีพร้อมกัน)</td></tr></tbody></table>
</div>
  <div class="examples-group">

        <div class="example-box">
          <div class="example-header">
            <span>📝 ตัวอย่างการคำนวณที่ 7.3: การคำนวณประสิทธิภาพการถ่ายโอนพลังงาน FRET ในเซนเซอร์ตรวจจับ DNA</span>
            <span style="background:#dcfce7; color:#15803d; font-size:8.5pt; padding:3px 10px; border-radius:4px; font-weight:700;">Step-by-Step Worked Solution</span>
          </div>
          <p style="text-indent:0; margin-bottom:10px;"><strong>โจทย์ปัญหา (Problem Statement):</strong><br>คู่เซนเซอร์ FRET ประกอบด้วยจุดควอนตัมสีเขียว ($R_0 = 5.2	ext{ nm}$) และสีย้อม Cy5 เมื่อเกิดการจับคู่สายดีเอ็นเอเป้าหมายทำให้ระยะห่างระหว่างจุดควอนตัมกับสีย้อมลดลงเหลือ $r = 4.0	ext{ nm}$ จงคำนวณหาประสิทธิภาพการถ่ายโอนพลังงาน $E_{	ext{FRET}}$</p>
          <div style="background:rgba(255,255,255,0.85); border:1px solid #e2e8f0; padding:12px 16px; border-radius:6px; margin:12px 0;">
            <strong style="color:#1e3a8a;">การวิเคราะห์และการคำนวณอย่างละเอียด:</strong><br>
            <p style="text-indent:0; margin:6px 0 0 0; line-height:1.85;">1. คำนวณอัตราส่วนระยะทาง: $\frac{r}{R_0} = \frac{4.0}{5.2} = 0.7692$<br>2. $(\frac{r}{R_0})^6 = (0.7692)^6 = 0.2079$<br>3. $E_{\text{FRET}} = \frac{1}{1 + (r/R_0)^6} = \frac{1}{1 + 0.2079} = \frac{1}{1.2079} = 0.8279 = 82.8\%$</p>
          </div>
          <div style="background:#f0fdf4; border-left:4px solid #16a34a; padding:10px 14px; margin-top:10px; font-size:9.5pt; color:#166534; border-radius:0 6px 6px 0;">
            💡 <strong>นัยสำคัญทางกายภาพและการประยุกต์ใช้งาน (Physical Insight):</strong><br>
            <span style="color:#14532d;">ประสิทธิภาพการถ่ายโอนพลังงานสูงถึง $82.8\%$ ทำให้แสงสีเขียวของจุดควอนตัมดับลงและกระตุ้นให้สีย้อม Cy5 เปล่งแสงสีแดงอย่างชัดเจน</span>
          </div>
        </div>
            
        <div class="example-box">
          <div class="example-header">
            <span>📝 ตัวอย่างการคำนวณที่ 7.4: การคำนวณจำนวนโมเลกุลแอนติบอดีที่ต่อบนผิวอนุภาคควอนตัมดอทเดี่ยว</span>
            <span style="background:#dcfce7; color:#15803d; font-size:8.5pt; padding:3px 10px; border-radius:4px; font-weight:700;">Step-by-Step Worked Solution</span>
          </div>
          <p style="text-indent:0; margin-bottom:10px;"><strong>โจทย์ปัญหา (Problem Statement):</strong><br>จุดควอนตัม $	ext{InP/ZnS}$ ขนาดเส้นผ่านศูนย์กลางรวมชั้นพอลิเมอร์ $D = 12.0	ext{ nm}$ มีพื้นที่ผิว $A = \pi D^2$ แอนติบอดี IgG แต่ละตัวมีพื้นที่สัมผัสบนผิว $a_{	ext{Ab}} pprox 25.0	ext{ nm}^2$ สมมติการจัดเรียงตัวแบบปิดแน่น $50\%$ จงคำนวณจำนวนแอนติบอดีเฉลี่ยต่อหนึ่งอนุภาค</p>
          <div style="background:rgba(255,255,255,0.85); border:1px solid #e2e8f0; padding:12px 16px; border-radius:6px; margin:12px 0;">
            <strong style="color:#1e3a8a;">การวิเคราะห์และการคำนวณอย่างละเอียด:</strong><br>
            <p style="text-indent:0; margin:6px 0 0 0; line-height:1.85;">1. พื้นที่ผิวอนุภาค $A = \pi (12.0\text{ nm})^2 = 452.39\text{ nm}^2$<br>2. พื้นที่ประสิทธิผล $A_{\text{eff}} = 452.39 \times 0.50 = 226.2\text{ nm}^2$<br>3. จำนวนแอนติบอดี $N = \frac{226.2\text{ nm}^2}{25.0\text{ nm}^2} = 9.05 \approx 9\text{ โมเลกุล}$</p>
          </div>
          <div style="background:#f0fdf4; border-left:4px solid #16a34a; padding:10px 14px; margin-top:10px; font-size:9.5pt; color:#166534; border-radius:0 6px 6px 0;">
            💡 <strong>นัยสำคัญทางกายภาพและการประยุกต์ใช้งาน (Physical Insight):</strong><br>
            <span style="color:#14532d;">อนุภาคควอนตัมดอทแต่ละตัวจะมีแอนติบอดีติดอยู่เฉลี่ย 9 โมเลกุล ช่วยเพิ่มแรงยึดเกาะแบบ Multivalent Binding กับเซลล์มะเร็งเป้าหมาย</span>
          </div>
        </div>
              </div>
  <div class="code-group">

        <div class="code-box">
          <div class="code-header">💻 แบบจำลองเชิงคำนวณภาษาไพทอน (Computational Python 3.11): กรณีศึกษา: การผ่าตัดนำทางด้วยภาพเรืองแสงแบบเรียลไทม์ (Fluorescence-Guided Surgery) สำหรับเนื้องอกในสมอง</div>
          <pre><code>การฉีดจุดควอนตัม NIR-II ที่จับจำเพาะกับตัวรับ Integrin $lpha_veta_3$ บนเซลล์มะเร็งสมอง ช่วยให้ศัลยแพทย์สามารถมองเห็นขอบเขตของเนื้องอกได้อย่างชัดเจนแบบเรียลไทม์ระหว่างผ่าตัด ทำให้ตัดเนื้องอกออกได้หมดจดโดยไม่ทำลายเนื้อสมองปกติ</code></pre>
        </div>
        <p style="font-size:9.5pt; color:#475569; margin-top:-6px; margin-bottom:18px; text-indent:0;"><em>คำอธิบายอัลกอริทึมการจำลอง:</em> สคริปต์ไพทอนสำหรับการคำนวณและจำลองเชิงตัวเลข</p>
              </div>
  <div class="lab-connection-block">
    <h3>🔬 การเชื่อมโยงสู่ห้องปฏิบัติการเสมือนจริงและเทคนิคการทดลอง (Virtual Lab Connection)</h3>
    <div style='background:#f0fdf4; border:1px solid #bbf7d0; border-left:5px solid #16a34a; padding:12px 16px; margin-bottom:14px; border-radius:6px;'><strong style='color:#166534; font-size:10.5pt;'>การจำลองประสิทธิภาพ FRET ระหว่างจุดควอนตัมกับตัวรับ</strong><p style='margin:6px 0 0 0; color:#14532d; text-indent:0; line-height:1.8;'>fret_efficiency_sim.py</p></div>
  </div>
  <div class="cases-block">
    <h3>🌐 กรณีศึกษางานวิจัยแนวหน้าและนวัตกรรมอุตสาหกรรม (Frontier Case Studies)</h3>
    <div style='background:#eff6ff; border:1px solid #bfdbfe; border-left:5px solid #2563eb; padding:12px 16px; margin-bottom:14px; border-radius:6px;'><strong style='color:#1e40af; font-size:10.5pt;'>การเชื่อมโยงกับ Virtual Lab 32: การจำลองการสร้างภาพระดับเซลล์ด้วยจุดควอนตัมและระบบ FRET</strong><p style='margin:6px 0 0 0; color:#1e3a8a; text-indent:0; line-height:1.8;'>ผู้เรียนสามารถเลือกคอนจูเกตจุดควอนตัมกับแอนติบอดีใน Lab 32 ส่องตรวจเซลล์มะเร็ง และวัดการเปลี่ยนแปลงของสัญญาณเรืองแสงแบบ Multiplexed Imaging</p></div>
  </div>

      <div class="checkpoint-box" style="background:#fefce8; border:1px solid #fef08a; border-left:5px solid #eab308; padding:14px 18px; margin:24px 0 35px 0; border-radius:6px; page-break-inside:avoid;">
        <strong style="color:#854d0e; font-size:10pt;">🎯 จุดตรวจประเมินความเข้าใจและคำถามทบทวนประจำหัวข้อ 7.2 (Concept Checkpoint)</strong>
        <ul style="margin:8px 0 0 0; padding-left:20px; color:#713f12; font-size:9.5pt; line-height:1.8;">
          <li>จงอธิบายแนวคิดรวบยอดหลักของ จุดควอนตัมชีวภาพและการสร้างภาพระดับเซลล์ และความแตกต่างจากพฤติกรรมในระดับมหภาค</li>
          <li>พารามิเตอร์ใดเป็นปัจจัยวิกฤตที่ควบคุมสมบัติทางฟิสิกส์ในหัวข้อนี้ และมีผลกระทบอย่างไร?</li>
          <li>เชื่อมโยงหลักการฟิสิกส์ในหัวข้อนี้เข้ากับการประยุกต์ใช้จริงในเทคโนโลยีสมัยใหม่</li>
        </ul>
      </div>
    </div>
    
    <div class="topic-section">
      <h2>7.3 การรักษาด้วยความร้อนแม่เหล็กเฉพาะจุดและการบำบัดมะเร็ง</h2>
      <div class="topic-en-title">(Magnetic Hyperthermia, Superparamagnetic Iron Oxide (SPIONs) & Targeted Therapy)</div>
      
      <div class="topic-intro">
        <p>การรักษาด้วยความร้อนเหนี่ยวนำเชิงแม่เหล็ก (Magnetic Hyperthermia Therapy: MHT) เป็นเทคโนโลยีการรักษามะเร็งแบบไม่รุกล้ำ (Non-Invasive) ที่ใช้ประโยชน์จากอนุภาคนาโนเหล็กออกไซด์ที่มีพฤติกรรมซูเปอร์พาราแมกเนติก (Superparamagnetic Iron Oxide Nanoparticles: SPIONs เช่น $	ext{Fe}_3	ext{O}_4$ หรือ $\gamma	ext{-Fe}_2	ext{O}_3$ ขนาดเส้นผ่านศูนย์กลาง $10 - 20	ext{ nm}$)</p>
    <p>เมื่อ SPIONs อยู่ภายใต้สนามแม่เหล็กไฟฟ้ากระแสสลับความถี่สูง (Alternating Magnetic Field: AMF ความถี่ $100 - 500	ext{ kHz}$) อนุภาคจะแปลงพลังงานสนามแม่เหล็กเป็นความร้อนเฉพาะจุดผ่านกระบวนการคลายตัวทางแม่เหล็ก (Magnetic Relaxation Mechanisms) ได้แก่ การคลายตัวแบบนีล (Néel Relaxation) และการคลายตัวแบบบราวน์ (Brownian Relaxation)</p>
    <p>ความร้อนที่เกิดขึ้นจะเพิ่มอุณหภูมิของก้อนเนื้องอกขึ้นสู่ระดับ $42 - 45^\circ	ext{C}$ (ระดับ Hyperthermia) ซึ่งเพียงพอที่จะกระตุ้นให้เซลล์มะเร็งเกิดการตายแบบอะพอพโทซิส (Apoptosis) และกระตุ้นการตอบสนองของระบบภูมิคุ้มกันร่างกาย (Immunogenic Cell Death) โดยไม่ทำอันตรายต่อเซลล์ปกติข้างเคียงซึ่งมีความทนทานต่อความร้อนสูงกว่า</p>
  </div>

      <div class="subtopic-block">
        <h3>ฟิสิกส์การกำเนิดความร้อน: กลไกของนีลและบราวน์ (Néel vs Brownian Relaxation)</h3>
            <p>1. การคลายตัวแบบนีล (Néel Relaxation, $	au_N$): การหมุนกลับทิศของโมเมนต์แม่เหล็กภายในผลึกข้ามกำแพงความไม่แปรเปลี่ยนเชิงทิศทาง (Anisotropy Barrier: $K_u V$): $	au_N = 	au_0 \exp\left(rac{K_u V}{k_B T}ight)$</p>
    <p>2. การคลายตัวแบบบราวน์ (Brownian Relaxation, $	au_B$): การหมุนทางกลของอนุภาคทั้งตัวในของเหลวหนืด: $	au_B = rac{3 \eta V_H}{k_B T}$</p>
    <p>เวลาคลายตัวยังผล: $rac{1}{	au_{	ext{eff}}} = rac{1}{	au_N} + rac{1}{	au_B}$ กลไกที่เร็วกว่าจะเป็นตัวควบคุมหลักในการกำเนิดความร้อน</p>
  </div>

      <div class="subtopic-block">
        <h3>อัตราการดูดกลืนพลังงานจำเพาะ (Specific Absorption Rate: SAR / SLP)</h3>
            <p>ประสิทธิภาพการทำความร้อนของอนุภาคระบุด้วยค่า SAR: $	ext{SAR} = rac{C_{	ext{med}}}{m_{	ext{Fe}}} \left(rac{\Delta T}{\Delta t}ight)_{	ext{initial}}$ มีหน่วยเป็นวัตต์ต่อกรัมของโลหะเหล็ก ($	ext{W/g}_	ext{Fe}$) ซึ่งในอนุภาคทรงลูกบาศก์หรือคอร์-เชลล์สมัยใหม่มีค่าสูงเกิน $1,000	ext{ W/g}$</p>
  </div>
  <div class="formula-group">

        <div class="equation-box">
          <div class="equation-header">📌 สมการฟิสิกส์หลัก: อัตราการดูดกลืนพลังงานจำเพาะ (SAR Formula)</div>
          <div class="formula-math">$$\text{SAR} = \frac{C_{\text{sample}}}{m_{\text{magnetic}}} \left. \frac{dT}{dt} \right|_{t=0} = \pi \mu_0 \chi'' f H_0^2$$</div>
          <p style="font-size:9.5pt; margin:4px 0 0 0; color:#334155; line-height:1.75; text-indent:0;"><strong>คำอธิบายตัวแปรและนัยสำคัญ:</strong> ประสิทธิภาพการแปลงพลังงานสนามแม่เหล็กเป็นความร้อน</p>
        </div>
            
        <div class="equation-box">
          <div class="equation-header">📌 สมการฟิสิกส์หลัก: เวลาคลายตัวแบบนีลและบราวน์</div>
          <div class="formula-math">$$\tau_N = \tau_0 \exp\left( \frac{K_u V}{k_B T} \right), \qquad \tau_B = \frac{3 \eta V_H}{k_B T}$$</div>
          <p style="font-size:9.5pt; margin:4px 0 0 0; color:#334155; line-height:1.75; text-indent:0;"><strong>คำอธิบายตัวแปรและนัยสำคัญ:</strong> การหมุนสปินภายในผลึกและการหมุนทางกลของอนุภาค</p>
        </div>
              </div>

      <div class="table-block">
        <h3>📊 ตารางเปรียบเทียบคุณสมบัติทางความร้อนของอนุภาคแม่เหล็กนาโนชนิดต่างๆ</h3>
        <table class="data-table">
          <thead><tr>
            <th>ชนิดอนุภาคนาโน</th><th>ขนาดผลึก (nm)</th><th>โครงสร้างรูปร่าง</th><th>ค่า SAR (W/g ที่ 300 kHz, 20 kA/m)</th><th>การประยุกต์ใช้งาน</th></tr></thead>
<tbody><tr><td>Fe3O4 (Magnetite)</td><td>14 nm</td><td>ทรงกลม (Spherical)</td><td>150 - 300 W/g</td><td>ผ่านการรับรอง FDA (NanoTherm)</td></tr><tr><td>Fe3O4 Nanocubes</td><td>19 nm</td><td>ลูกบาศก์ (Cubic)</td><td>800 - 1,200 W/g</td><td>ความร้อนสูง สลายก้อนเนื้องอกเร็ว</td></tr><tr><td>Zn0.4Fe2.6O4 (Zn-doped)</td><td>15 nm</td><td>ทรงกลม</td><td>600 - 900 W/g</td><td>เพิ่ม Magnetization และความร้อน</td></tr><tr><td>CoFe2O4@MnFe2O4</td><td>12 nm / 3 nm</td><td>Core-Shell แลกเปลี่ยนสปิน</td><td>2,000 - 3,500 W/g</td><td>ระดับงานวิจัยประสิทธิภาพสูงสุด</td></tr></tbody></table>
</div>
  <div class="examples-group">

        <div class="example-box">
          <div class="example-header">
            <span>📝 ตัวอย่างการคำนวณที่ 7.5: การคำนวณเวลาคลายตัวแบบนีลและบราวน์ของ SPIONs</span>
            <span style="background:#dcfce7; color:#15803d; font-size:8.5pt; padding:3px 10px; border-radius:4px; font-weight:700;">Step-by-Step Worked Solution</span>
          </div>
          <p style="text-indent:0; margin-bottom:10px;"><strong>โจทย์ปัญหา (Problem Statement):</strong><br>อนุภาคนาโน $	ext{Fe}_3	ext{O}_4$ ทรงกลมมีเส้นผ่านศูนย์กลางผลึก $d = 12.0	ext{ nm}$ ($V = 9.048 	imes 10^{-25}	ext{ m}^3$) และเส้นผ่านศูนย์กลางไฮโดรไดนามิกรวมสารเคลือบ $d_H = 30.0	ext{ nm}$ ($V_H = 1.414 	imes 10^{-23}	ext{ m}^3$) ในน้ำที่มีความหนืด $\eta = 0.001	ext{ Pa}\cdot	ext{s}$ ที่ $T = 310	ext{ K}$ ($37^\circ	ext{C}$) กำหนดค่าคงที่แอนไอโซโทรปี $K_u = 1.5 	imes 10^4	ext{ J/m}^3$ และ $	au_0 = 10^{-9}	ext{ s}$ จงคำนวณหา (ก) $	au_N$ (ข) $	au_B$ (ค) $	au_{	ext{eff}}$</p>
          <div style="background:rgba(255,255,255,0.85); border:1px solid #e2e8f0; padding:12px 16px; border-radius:6px; margin:12px 0;">
            <strong style="color:#1e3a8a;">การวิเคราะห์และการคำนวณอย่างละเอียด:</strong><br>
            <p style="text-indent:0; margin:6px 0 0 0; line-height:1.85;">1. คำนวณพลังงานแอนไอโซโทรปี: $K_u V = (1.5 \times 10^4) \times (9.048 \times 10^{-25}) = 1.357 \times 10^{-20}\text{ J}$<br>2. พลังงานความร้อน $k_B T = (1.3806 \times 10^{-23}) \times 310 = 4.280 \times 10^{-21}\text{ J}$<br>3. $\frac{K_u V}{k_B T} = \frac{1.357 \times 10^{-20}}{4.280 \times 10^{-21}} = 3.171$<br>4. $\tau_N = 10^{-9} \times e^{3.171} = 2.383 \times 10^{-8}\text{ s} = 23.83\text{ ns}$<br>5. $\tau_B = \frac{3(0.001)(1.414 \times 10^{-23})}{4.280 \times 10^{-21}} = 9.911 \times 10^{-6}\text{ s} = 9.91\text{ }\mu\text{s}$<br>6. $\tau_{\text{eff}} = \frac{\tau_N \tau_B}{\tau_N + \tau_B} \approx \tau_N = 23.83\text{ ns}$</p>
          </div>
          <div style="background:#f0fdf4; border-left:4px solid #16a34a; padding:10px 14px; margin-top:10px; font-size:9.5pt; color:#166534; border-radius:0 6px 6px 0;">
            💡 <strong>นัยสำคัญทางกายภาพและการประยุกต์ใช้งาน (Physical Insight):</strong><br>
            <span style="color:#14532d;">เนื่องจาก $	au_N \ll 	au_B$ กลไกการกำเนิดความร้อนหลักของอนุภาคขนาดนี้จึงเกิดจาก Néel Relaxation ข้ามกำแพงผลึกภายใน</span>
          </div>
        </div>
            
        <div class="example-box">
          <div class="example-header">
            <span>📝 ตัวอย่างการคำนวณที่ 7.6: การคำนวณอัตราการเพิ่มอุณหภูมิและการหาค่า SAR</span>
            <span style="background:#dcfce7; color:#15803d; font-size:8.5pt; padding:3px 10px; border-radius:4px; font-weight:700;">Step-by-Step Worked Solution</span>
          </div>
          <p style="text-indent:0; margin-bottom:10px;"><strong>โจทย์ปัญหา (Problem Statement):</strong><br>สารละลาย SPIONs ปริมาตร $1.0	ext{ mL}$ มีความเข้มข้นธาตุเหล็ก $m_{	ext{Fe}} = 5.0	ext{ mg}$ นำไปใส่ในสนามแม่เหล็ก $f = 300	ext{ kHz}$, $H = 15	ext{ kA/m}$ พบว่าอุณหภูมิเพิ่มขึ้นจาก $37.0^\circ	ext{C}$ สู่ $43.0^\circ	ext{C}$ ในเวลา $30.0	ext{ วินาที}$ กำหนดความจุความร้อนจำเพาะของน้ำ $C_p = 4.184	ext{ J/g}\cdot	ext{K}$ จงคำนวณหาค่า SAR</p>
          <div style="background:rgba(255,255,255,0.85); border:1px solid #e2e8f0; padding:12px 16px; border-radius:6px; margin:12px 0;">
            <strong style="color:#1e3a8a;">การวิเคราะห์และการคำนวณอย่างละเอียด:</strong><br>
            <p style="text-indent:0; margin:6px 0 0 0; line-height:1.85;">1. มวลสารละลายน้ำ $m_w \approx 1.0\text{ g}$ ความจุความร้อนรวม $C_{\text{sample}} = 1.0\text{ g} \times 4.184\text{ J/g}\cdot\text{K} = 4.184\text{ J/K}$<br>2. อัตราการเพิ่มอุณหภูมิ $\frac{\Delta T}{\Delta t} = \frac{43.0 - 37.0}{30.0} = \frac{6.0\text{ K}}{30.0\text{ s}} = 0.20\text{ K/s}$<br>3. $\text{SAR} = \frac{C_{\text{sample}}}{m_{\text{Fe}}} \left(\frac{\Delta T}{\Delta t}\right) = \frac{4.184\text{ J/K}}{5.0 \times 10^{-3}\text{ g}} \times (0.20\text{ K/s}) = 167.36\text{ W/g}$</p>
          </div>
          <div style="background:#f0fdf4; border-left:4px solid #16a34a; padding:10px 14px; margin-top:10px; font-size:9.5pt; color:#166534; border-radius:0 6px 6px 0;">
            💡 <strong>นัยสำคัญทางกายภาพและการประยุกต์ใช้งาน (Physical Insight):</strong><br>
            <span style="color:#14532d;">ค่า SAR เท่ากับ $167.4	ext{ W/g}$ สามารถสร้างความร้อนจนถึงระดับ $43^\circ	ext{C}$ ได้อย่างรวดเร็วเพื่อทำลายเซลล์มะเร็ง</span>
          </div>
        </div>
              </div>
  <div class="code-group">

        <div class="code-box">
          <div class="code-header">💻 แบบจำลองเชิงคำนวณภาษาไพทอน (Computational Python 3.11): กรณีศึกษา: การรักษามะเร็งสมอง Glioblastoma ด้วยเทคโนโลยี NanoTherm (MagForce AG, เยอรมนี)</div>
          <pre><code>การฉีดอนุภาคนาโนเหล็กออกไซด์เข้าสู่ก้อนเนื้องอกในสมองโดยตรง แล้วกระตุ้นด้วยเครื่องสนามแม่เหล็กภายนอก ช่วยยืดอายุขัยเฉลี่ยของผู้ป่วยมะเร็งสมองระยะสุดท้ายได้มากกว่าสองเท่าเมื่อเทียบกับการรักษาแบบเดิม</code></pre>
        </div>
        <p style="font-size:9.5pt; color:#475569; margin-top:-6px; margin-bottom:18px; text-indent:0;"><em>คำอธิบายอัลกอริทึมการจำลอง:</em> สคริปต์ไพทอนสำหรับการคำนวณและจำลองเชิงตัวเลข</p>
              </div>
  <div class="lab-connection-block">
    <h3>🔬 การเชื่อมโยงสู่ห้องปฏิบัติการเสมือนจริงและเทคนิคการทดลอง (Virtual Lab Connection)</h3>
    <div style='background:#f0fdf4; border:1px solid #bbf7d0; border-left:5px solid #16a34a; padding:12px 16px; margin-bottom:14px; border-radius:6px;'><strong style='color:#166534; font-size:10.5pt;'>การจำลองอุณหภูมิความร้อนแม่เหล็กไฮเปอร์เทอร์เมีย</strong><p style='margin:6px 0 0 0; color:#14532d; text-indent:0; line-height:1.8;'>magnetic_hyperthermia_sim.py</p></div>
  </div>
  <div class="cases-block">
    <h3>🌐 กรณีศึกษางานวิจัยแนวหน้าและนวัตกรรมอุตสาหกรรม (Frontier Case Studies)</h3>
    <div style='background:#eff6ff; border:1px solid #bfdbfe; border-left:5px solid #2563eb; padding:12px 16px; margin-bottom:14px; border-radius:6px;'><strong style='color:#1e40af; font-size:10.5pt;'>การเชื่อมโยงกับ Virtual Lab 33: การจำลองการรักษาด้วยความร้อนแม่เหล็กไฮเปอร์เทอร์เมีย SPIONs</strong><p style='margin:6px 0 0 0; color:#1e3a8a; text-indent:0; line-height:1.8;'>ผู้เรียนสามารถควบคุมความถี่และความเข้มสนามแม่เหล็ก AMF ใน Lab 33 เลือกขนาดอนุภาคนาโน และติดตามเส้นโค้งอุณหภูมิการทำลายเซลล์มะเร็ง</p></div>
  </div>

      <div class="checkpoint-box" style="background:#fefce8; border:1px solid #fef08a; border-left:5px solid #eab308; padding:14px 18px; margin:24px 0 35px 0; border-radius:6px; page-break-inside:avoid;">
        <strong style="color:#854d0e; font-size:10pt;">🎯 จุดตรวจประเมินความเข้าใจและคำถามทบทวนประจำหัวข้อ 7.3 (Concept Checkpoint)</strong>
        <ul style="margin:8px 0 0 0; padding-left:20px; color:#713f12; font-size:9.5pt; line-height:1.8;">
          <li>จงอธิบายแนวคิดรวบยอดหลักของ การรักษาด้วยความร้อนแม่เหล็กเฉพาะจุดและการบำบัดมะเร็ง และความแตกต่างจากพฤติกรรมในระดับมหภาค</li>
          <li>พารามิเตอร์ใดเป็นปัจจัยวิกฤตที่ควบคุมสมบัติทางฟิสิกส์ในหัวข้อนี้ และมีผลกระทบอย่างไร?</li>
          <li>เชื่อมโยงหลักการฟิสิกส์ในหัวข้อนี้เข้ากับการประยุกต์ใช้จริงในเทคโนโลยีสมัยใหม่</li>
        </ul>
      </div>
    </div>
    
    <div class="topic-section">
      <h2>7.4 ระบบอวัยวะบนชิปและของไหลจุลภาคระดับนาโน</h2>
      <div class="topic-en-title">(Lab-on-a-Chip, Nanofluidics & Organ-on-a-Chip Platforms)</div>
      
      <div class="topic-intro">
        <p>ระบบห้องปฏิบัติการบนชิป (Lab-on-a-Chip: LOC) และระบบอวัยวะบนชิป (Organ-on-a-Chip: OOC) เป็นการหลอมรวมเทคโนโลยีการประดิษฐ์ระดับไมโคร/นาโน เข้ากับพลศาสตร์ของไหลและชีววิทยาของเซลล์ เพื่อจำลองการทำงานทางสรีรวิทยาของอวัยวะมนุษย์บนแผ่นชิปขนาดเท่าสไลด์แก้ว</p>
    <p>ในสเกลไมโครและนาโนฟลูอิดิกส์ พฤติกรรมของของไหลจะถูกควบคุมโดย แรงตึงผิว (Surface Tension), ปรากฏการณ์แคพิลลารี (Capillary Action), และการไหลแบบราบเรียบสมบูรณ์ (Laminar Flow ที่มีเลขเรย์โนลด์ส $	ext{Re} \ll 1$) ซึ่งไม่มีความปั่นป่วน ทำให้การผสมของของเหลวเกิดขึ้นผ่านการแพร่ระดับโมเลกุล (Diffusion) เท่านั้น</p>
    <p>เทคโนโลยี Organ-on-a-Chip เช่น ปอดบนชิป (Lung-on-a-Chip), ตับบนชิป (Liver-on-a-Chip), และลำไส้บนชิป (Gut-on-a-Chip) ช่วยให้นักวิจัยสามารถทดสอบประสิทธิภาพและความเป็นพิษของยาตัวใหม่ได้แม่นยำกว่าการทดลองในสัตว์ทดลอง ลดระยะเวลาและต้นทุนการพัฒนายาลงกว่า 70% และผลักดันการแพทย์เฉพาะบุคคล (Personalized Medicine)</p>
  </div>

      <div class="subtopic-block">
        <h3>ฟิสิกส์ของช่องไหลระดับนาโน (Nanofluidics) และการซ้อนทับของชั้นไฟฟ้าสองชั้น (EDL Overlap)</h3>
            <p>เมื่อความสูงของช่องของไหล $h$ ลดลงจนเทียบเท่ากับความหนาของชั้นไฟฟ้าเดอบาย (Debye Length: $\lambda_D = \sqrt{rac{\epsilon_0 \epsilon_r k_B T}{2 e^2 I}} pprox 1 - 10	ext{ nm}$)</p>
    <p>ชั้นไฟฟ้าสองชั้น (Electric Double Layer: EDL) จะเกิดการซ้อนทับกันอย่างสมบูรณ์ ทำให้ช่องแคบมีเฉพาะไอออนขั้วตรงข้าม (Counter-ions) และกีดกันไอออนขั้วเดียวกัน (Co-ions) ออกไป นำไปสู่ปรากฏการณ์การคัดกรองไอออน (Ion Permselectivity) และการสร้างไดโอดของไหลนาโน (Nanofluidic Diodes)</p>
  </div>

      <div class="subtopic-block">
        <h3>โครงสร้าง Lung-on-a-Chip โดยสถาบัน Wyss Institute (Harvard)</h3>
            <p>การใช้แผ่นเยื่อพอลิเมอร์ PDMS ชนิดยืดหยุ่นที่มีรูพรุนระดับไมโครคั่นระหว่างช่องลม (เซลล์เยื่อบุผิวปอด) และช่องเลือด (เซลล์บุผนังหลอดเลือด) ร่วมกับการใช้แรงดันสุญญากาศเป็นจังหวะเพื่อจำลองการหายใจเข้า-ออกของปอดมนุษย์จริง</p>
  </div>
  <div class="formula-group">

        <div class="equation-box">
          <div class="equation-header">📌 สมการฟิสิกส์หลัก: เลขเรย์โนลด์สสำหรับของไหลจุลภาค</div>
          <div class="formula-math">$$\text{Re} = \frac{\rho v D_h}{\eta} \ll 1, \qquad D_h = \frac{4A}{P} = \frac{2 w h}{w + h}$$</div>
          <p style="font-size:9.5pt; margin:4px 0 0 0; color:#334155; line-height:1.75; text-indent:0;"><strong>คำอธิบายตัวแปรและนัยสำคัญ:</strong> การไหลแบบลามินาร์ราบเรียบสมบูรณ์</p>
        </div>
            
        <div class="equation-box">
          <div class="equation-header">📌 สมการฟิสิกส์หลัก: ความยาวเดอบายในช่องของไหลนาโน</div>
          <div class="formula-math">$$\lambda_D = \sqrt{\frac{\epsilon_0 \epsilon_r k_B T}{2 N_A e^2 I}}, \qquad I = \frac{1}{2} \sum c_i z_i^2$$</div>
          <p style="font-size:9.5pt; margin:4px 0 0 0; color:#334155; line-height:1.75; text-indent:0;"><strong>คำอธิบายตัวแปรและนัยสำคัญ:</strong> ความหนาของชั้นบรรยากาศไอออนิกไฟฟ้าสองชั้น</p>
        </div>
              </div>

      <div class="table-block">
        <h3>📊 ตารางเปรียบเทียบการทดสอบยาด้วยวิธีดั้งเดิมกับ Organ-on-a-Chip</h3>
        <table class="data-table">
          <thead><tr>
            <th>เกณฑ์การประเมิน</th><th>การเพาะเลี้ยงเซลล์ 2D ดั้งเดิม</th><th>การทดลองในสัตว์ (In Vivo)</th><th>ระบบ Organ-on-a-Chip (OOC)</th></tr></thead>
<tbody><tr><td>ความสมจริงทางสรีรวิทยา</td><td>ต่ำมาก (เซลล์แบนราบ ขาดแรงกล)</td><td>ปานกลาง (สายพันธุ์ต่างจากมนุษย์)</td><td>สูงมาก (มีแรงเฉือน การไหล 3D)</td></tr><tr><td>การทำนายความเป็นพิษในมนุษย์</td><td>< 50%</td><td>~ 60 - 70%</td><td>> 85 - 90%</td></tr><tr><td>ระยะเวลาการทดสอบ</td><td>หลายสัปดาห์</td><td>หลายเดือนถึงเป็นปี</td><td>ไม่กี่วันถึงสัปดาห์</td></tr><tr><td>จริยธรรมการวิจัย</td><td>ไม่มีปัญหาจริยธรรมสัตว์</td><td>มีข้อจำกัดด้านจริยธรรมสัตว์เข้มงวด</td><td>ลดและทดแทนการใช้สัตว์ทดลอง 100%</td></tr><tr><td>การแพทย์เฉพาะบุคคล</td><td>ทำได้ยาก</td><td>ทำไม่ได้</td><td>ทำได้โดยใช้เซลล์ต้นกำเนิด iPSCs ของผู้ป่วย</td></tr></tbody></table>
</div>
  <div class="examples-group">

        <div class="example-box">
          <div class="example-header">
            <span>📝 ตัวอย่างการคำนวณที่ 7.7: การคำนวณเลขเรย์โนลด์สในช่องของไหลจุลภาค Microfluidic Channel</span>
            <span style="background:#dcfce7; color:#15803d; font-size:8.5pt; padding:3px 10px; border-radius:4px; font-weight:700;">Step-by-Step Worked Solution</span>
          </div>
          <p style="text-indent:0; margin-bottom:10px;"><strong>โจทย์ปัญหา (Problem Statement):</strong><br>ช่องของไหล PDMS มีความกว้าง $w = 100	ext{ }\mu	ext{m}$ ความลึก $h = 50	ext{ }\mu	ext{m}$ มีสารละลายน้ำเลือด ($ho = 1050	ext{ kg/m}^3$, $\eta = 0.003	ext{ Pa}\cdot	ext{s}$) ไหลด้วยความเร็วเฉลี่ย $v = 1.0	ext{ mm/s}$ จงคำนวณหา (ก) เส้นผ่านศูนย์กลางไฮดรอลิก $D_h$ (ข) เลขเรย์โนลด์ส $	ext{Re}$</p>
          <div style="background:rgba(255,255,255,0.85); border:1px solid #e2e8f0; padding:12px 16px; border-radius:6px; margin:12px 0;">
            <strong style="color:#1e3a8a;">การวิเคราะห์และการคำนวณอย่างละเอียด:</strong><br>
            <p style="text-indent:0; margin:6px 0 0 0; line-height:1.85;">1. $D_h = \frac{2 w h}{w + h} = \frac{2(100 \times 10^{-6})(50 \times 10^{-6})}{(100 + 50) \times 10^{-6}} = \frac{10000 \times 10^{-12}}{150 \times 10^{-6}} = 6.667 \times 10^{-5}\text{ m} = 66.67\text{ }\mu\text{m}$<br>2. $\text{Re} = \frac{\rho v D_h}{\eta} = \frac{(1050\text{ kg/m}^3) \times (1.0 \times 10^{-3}\text{ m/s}) \times (6.667 \times 10^{-5}\text{ m})}{0.003\text{ Pa}\cdot\text{s}} = \frac{0.0700}{0.003} = 0.0233$</p>
          </div>
          <div style="background:#f0fdf4; border-left:4px solid #16a34a; padding:10px 14px; margin-top:10px; font-size:9.5pt; color:#166534; border-radius:0 6px 6px 0;">
            💡 <strong>นัยสำคัญทางกายภาพและการประยุกต์ใช้งาน (Physical Insight):</strong><br>
            <span style="color:#14532d;">เนื่องจาก $	ext{Re} = 0.0233 \ll 1$ ของไหลจึงไหลแบบลามินาร์อย่างสมบูรณ์ ปราศจากความปั่นป่วน สามารถควบคุมเส้นทางการไหลได้แม่นยำ</span>
          </div>
        </div>
            
        <div class="example-box">
          <div class="example-header">
            <span>📝 ตัวอย่างการคำนวณที่ 7.8: การคำนวณความยาวเดอบาย $\lambda_D$ ในสารละลายบัฟเฟอร์ PBS</span>
            <span style="background:#dcfce7; color:#15803d; font-size:8.5pt; padding:3px 10px; border-radius:4px; font-weight:700;">Step-by-Step Worked Solution</span>
          </div>
          <p style="text-indent:0; margin-bottom:10px;"><strong>โจทย์ปัญหา (Problem Statement):</strong><br>สารละลาย PBS มีความแรงไอออนิก $I = 150	ext{ mM} = 150	ext{ mol/m}^3$ ที่อุณหภูมิห้อง $T = 298	ext{ K}$ ($\epsilon_r = 78.4$) จงคำนวณหาความยาวเดอบาย $\lambda_D$</p>
          <div style="background:rgba(255,255,255,0.85); border:1px solid #e2e8f0; padding:12px 16px; border-radius:6px; margin:12px 0;">
            <strong style="color:#1e3a8a;">การวิเคราะห์และการคำนวณอย่างละเอียด:</strong><br>
            <p style="text-indent:0; margin:6px 0 0 0; line-height:1.85;">1. $\lambda_D = \sqrt{\frac{(8.854 \times 10^{-12})(78.4)(1.3806 \times 10^{-23})(298)}{2(6.022 \times 10^{23})(1.602 \times 10^{-19})^2(150)}} = \sqrt{\frac{2.853 \times 10^{-30}}{4.634 \times 10^{-12}}} = \sqrt{6.157 \times 10^{-19}} = 7.847 \times 10^{-10}\text{ m} = 0.785\text{ nm}$</p>
          </div>
          <div style="background:#f0fdf4; border-left:4px solid #16a34a; padding:10px 14px; margin-top:10px; font-size:9.5pt; color:#166534; border-radius:0 6px 6px 0;">
            💡 <strong>นัยสำคัญทางกายภาพและการประยุกต์ใช้งาน (Physical Insight):</strong><br>
            <span style="color:#14532d;">ความยาวเดอบาย $pprox 0.8	ext{ nm}$ ในสภาวะเกลือเข้มข้น หากเจือจางลง 100 เท่า ($1.5	ext{ mM}$) ค่า $\lambda_D$ จะเพิ่มขึ้นเป็น $7.85	ext{ nm}$ ทำให้เกิดการซ้อนทับของ EDL ในช่องนาโนขนาด 15 nm</span>
          </div>
        </div>
              </div>
  <div class="code-group">

        <div class="code-box">
          <div class="code-header">💻 แบบจำลองเชิงคำนวณภาษาไพทอน (Computational Python 3.11): กรณีศึกษา: การทดสอบความเป็นพิษต่อตับของยารักษาโรคใหม่ด้วย Human Liver-on-a-Chip (Emulate Inc.)</div>
          <pre><code>งานวิจัยที่ตีพิมพ์ในวารสาร Nature Communications แสดงให้เห็นว่าชิปตับมนุษย์สามารถตรวจจับความเป็นพิษต่อตับของยา 27 ชนิดที่มีผลร้ายแรงในมนุษย์แต่ไม่แสดงอาการในสัตว์ทดลองได้แม่นยำถึง 87% ช่วยป้องกันอันตรายต่อผู้ป่วยในการทดลองทางคลินิก</code></pre>
        </div>
        <p style="font-size:9.5pt; color:#475569; margin-top:-6px; margin-bottom:18px; text-indent:0;"><em>คำอธิบายอัลกอริทึมการจำลอง:</em> สคริปต์ไพทอนสำหรับการคำนวณและจำลองเชิงตัวเลข</p>
              </div>
  <div class="lab-connection-block">
    <h3>🔬 การเชื่อมโยงสู่ห้องปฏิบัติการเสมือนจริงและเทคนิคการทดลอง (Virtual Lab Connection)</h3>
    <div style='background:#f0fdf4; border:1px solid #bbf7d0; border-left:5px solid #16a34a; padding:12px 16px; margin-bottom:14px; border-radius:6px;'><strong style='color:#166534; font-size:10.5pt;'>การจำลองการแพร่และการไหลแบบลามินาร์ในช่องของไหลจุลภาค</strong><p style='margin:6px 0 0 0; color:#14532d; text-indent:0; line-height:1.8;'>microfluidics_diffusion_sim.py</p></div>
  </div>
  <div class="cases-block">
    <h3>🌐 กรณีศึกษางานวิจัยแนวหน้าและนวัตกรรมอุตสาหกรรม (Frontier Case Studies)</h3>
    <div style='background:#eff6ff; border:1px solid #bfdbfe; border-left:5px solid #2563eb; padding:12px 16px; margin-bottom:14px; border-radius:6px;'><strong style='color:#1e40af; font-size:10.5pt;'>การเชื่อมโยงกับ Virtual Lab 34: การจำลองของไหลจุลภาค Lab-on-a-Chip และ Organ-on-a-Chip</strong><p style='margin:6px 0 0 0; color:#1e3a8a; text-indent:0; line-height:1.8;'>ผู้เรียนสามารถออกแบบช่องไหล Microfluidic Channel ใน Lab 34 ปรับอัตราการไหล สังเกตการผสมแบบ Laminar Flow และทดสอบแรงเฉือนบนเซลล์เยื่อบุหลอดเลือด</p></div>
  </div>

      <div class="checkpoint-box" style="background:#fefce8; border:1px solid #fef08a; border-left:5px solid #eab308; padding:14px 18px; margin:24px 0 35px 0; border-radius:6px; page-break-inside:avoid;">
        <strong style="color:#854d0e; font-size:10pt;">🎯 จุดตรวจประเมินความเข้าใจและคำถามทบทวนประจำหัวข้อ 7.4 (Concept Checkpoint)</strong>
        <ul style="margin:8px 0 0 0; padding-left:20px; color:#713f12; font-size:9.5pt; line-height:1.8;">
          <li>จงอธิบายแนวคิดรวบยอดหลักของ ระบบอวัยวะบนชิปและของไหลจุลภาคระดับนาโน และความแตกต่างจากพฤติกรรมในระดับมหภาค</li>
          <li>พารามิเตอร์ใดเป็นปัจจัยวิกฤตที่ควบคุมสมบัติทางฟิสิกส์ในหัวข้อนี้ และมีผลกระทบอย่างไร?</li>
          <li>เชื่อมโยงหลักการฟิสิกส์ในหัวข้อนี้เข้ากับการประยุกต์ใช้จริงในเทคโนโลยีสมัยใหม่</li>
        </ul>
      </div>
    </div>
    
    <div class="topic-section">
      <h2>7.5 นาโนโรโบติกส์ชีวภาพและโครงสร้างดีเอ็นเอออริกามิ</h2>
      <div class="topic-en-title">(Bio-Nanorobotics, DNA Walkers & Autonomous Nanomachines)</div>
      
      <div class="topic-intro">
        <p>นาโนโรโบติกส์ชีวภาพ (Biological Nanorobotics) เป็นความก้าวหน้าขั้นสูงสุดของการบูรณาการชีววิทยาโมเลกุลเข้ากับวิศวกรรมหุ่นยนต์ระดับนาโน เพื่อสร้างเครื่องจักรโมเลกุลอัตโนมัติ (Autonomous Molecular Machines) ที่สามารถนำทาง ปฏิบัติการซ่อมแซมเซลล์ และส่งมอบยาเคมีบำบัดตรงสู่เป้าหมายระดับเซลล์เดี่ยว</p>
    <p>เทคโนโลยีที่เป็นรากฐานสำคัญคือ ดีเอ็นเอออริกามิเชิงพลศาสตร์ (Dynamic DNA Origami) และดีเอ็นเอวอล์กเกอร์ (DNA Walkers) ซึ่งใช้หลักการจับคู่เบสที่แม่นยำของวัตสัน-คลิก ($	ext{A-T}, 	ext{G-C}$) ร่วมกับปฏิกิริยาการแทนที่สายดีเอ็นเอที่ขับเคลื่อนด้วยโทโฮลด์ (Toehold-Mediated DNA Strand Displacement: TMSD) ทำให้หุ่นยนต์ดีเอ็นเอสามารถ 'เดิน' ก้าวไปข้างหน้าตามรางนำทาง, 'เปิด-ปิด' ฝากล่องนาโนเพื่อปล่อยยา, หรือประกอบโมเลกุลตามตรรกะคอมพิวเตอร์เชิงโมเลกุล (DNA Computing Logic Gates)</p>
    <p>ในระดับการประยุกต์ใช้งานในร่างกาย นาโนโรบอตที่ขับเคลื่อนด้วยเอนไซม์ (Enzyme-Powered Nanomotors เช่น อนุภาคที่ขับเคลื่อนด้วยเอนไซม์ยูรีเอสหรือคะตาเลส) สามารถว่ายทวนกระแสของเหลวในร่างกายและเจาะทะลุผ่านเมือกเนื้องอกในกระเพาะปัสสาวะเพื่อทำลายก้อนมะเร็งได้อย่างแม่นยำ</p>
  </div>

      <div class="subtopic-block">
        <h3>กลไก Toehold-Mediated Strand Displacement (TMSD)</h3>
            <p>การเริ่มต้นปฏิกิริยาเกิดขึ้นเมื่อสายดีเอ็นเอขาเข้า (Invading Strand) เข้าจับกับบริเวณสายเดี่ยวสั้นๆ เรียกว่า โทโฮลด์ (Toehold, ความยาว 4 - 8 เบส) บนโครงสร้างคู่เดิม</p>
    <p>จากนั้นจะเกิดกระบวนการย้ายตำแหน่งของกิ่งสาขา (Branch Migration) อย่างเป็นลำดับจนกระทั่งสายเดิมหลุดออกไปอย่างสมบูรณ์ กระบวนการนี้ให้อัตราเร็วปฏิกิริยาที่ปรับแต่งได้กว้างถึง $10^6$ เท่าตามความยาวของโทโฮลด์</p>
  </div>

      <div class="subtopic-block">
        <h3>หุ่นยนต์นาโนกล่องดีเอ็นเอ (DNA Nanorobot with Aptamer Logic Locks)</h3>
            <p>หุ่นยนต์ดีเอ็นเอทรงกระบอกกลวงบรรจุเอนไซม์ทรอมบิน (Thrombin) ไว้ภายในโพรง ถูกปิดล็อคด้วยสายแอปทาเมอร์คู่ เมื่อหุ่นยนต์พบตัวบ่งชี้มะเร็งนิวคลีโอลิน (Nucleolin) บนผิวหลอดเลือดเนื้องอก ล็อคจะเปิดออกและปล่อยทรอมบินเพื่อทำให้เกิดลิ่มเลือดอุดตันตัดเส้นเลือดเลี้ยงเนื้องอกจนมะเร็งฝ่อตาย</p>
  </div>
  <div class="formula-group">

        <div class="equation-box">
          <div class="equation-header">📌 สมการฟิสิกส์หลัก: อัตราเร็วปฏิกิริยาการแทนที่สาย Toehold TMSD</div>
          <div class="formula-math">$$k_{\text{TMSD}} = k_0 \times 10^{\alpha \, L_{\text{toehold}}}, \qquad 0 \le L_{\text{toehold}} \le 8\text{ nt}$$</div>
          <p style="font-size:9.5pt; margin:4px 0 0 0; color:#334155; line-height:1.75; text-indent:0;"><strong>คำอธิบายตัวแปรและนัยสำคัญ:</strong> อัตราเร็วเพิ่มขึ้นแบบเอกซ์โพเนนเชียลตามความยาวโทโฮลด์</p>
        </div>
            
        <div class="equation-box">
          <div class="equation-header">📌 สมการฟิสิกส์หลัก: แรงขับเคลื่อนและพลังงานกลของ DNA Walker</div>
          <div class="formula-math">$$F_{\text{stall}} \approx 2 - 5\text{ pN}, \qquad \Delta G_{\text{step}} = -\Delta G_{\text{hybridization}} \approx -10\text{ to } -20\text{ kcal/mol}$$</div>
          <p style="font-size:9.5pt; margin:4px 0 0 0; color:#334155; line-height:1.75; text-indent:0;"><strong>คำอธิบายตัวแปรและนัยสำคัญ:</strong> แรงกลระดับพิโกนิวตันจากพลังงานพันธะไฮโดรเจน</p>
        </div>
              </div>

      <div class="table-block">
        <h3>📊 ตารางเปรียบเทียบชนิดของเครื่องจักรและมอเตอร์ระดับนาโน</h3>
        <table class="data-table">
          <thead><tr>
            <th>ชนิดนาโนโรบอต</th><th>แหล่งพลังงานขับเคลื่อน</th><th>ความเร็วการเคลื่อนที่</th><th>กลไกควบคุม</th><th>การประยุกต์ใช้งาน</th></tr></thead>
<tbody><tr><td>DNA Walker</td><td>ปฏิกิริยาตัดสาย/แทนที่เบส DNA</td><td>0.1 - 1.0 nm/นาที</td><td>โปรแกรมด้วยลำดับเบส</td><td>โรงงานประกอบโมเลกุล, คำนวณตรรกะ</td></tr><tr><td>Enzyme-Powered Motor</td><td>ปฏิกิริยาย่อยสลายเคมี (Urea, H2O2)</td><td>1 - 50 μm/วินาที</td><td>การไล่ระดับความเข้มข้นสาร</td><td>นำส่งยาในกระเพาะปัสสาวะ/กระเพาะอาหาร</td></tr><tr><td>Magnetic Nanorobot</td><td>สนามแม่เหล็กหมุนภายนอก</td><td>5 - 100 μm/วินาที</td><td>ควบคุมทิศทางด้วยสนามแม่เหล็ก</td><td>การผ่าตัดจุลภาคในหลอดเลือดตา</td></tr><tr><td>Bio-Hybrid Spermbot</td><td>เซลล์อสุจิหรือแบคทีเรียธรรมชาติ</td><td>20 - 150 μm/วินาที</td><td>การตอบสนองต่อสารเคมี (Chemotaxis)</td><td>การรักษาภาวะมีบุตรยาก, นำส่งยาเนื้องอก</td></tr></tbody></table>
</div>
  <div class="examples-group">

        <div class="example-box">
          <div class="example-header">
            <span>📝 ตัวอย่างการคำนวณที่ 7.9: การคำนวณอัตราเร็วปฏิกิริยา TMSD ตามความยาวโทโฮลด์</span>
            <span style="background:#dcfce7; color:#15803d; font-size:8.5pt; padding:3px 10px; border-radius:4px; font-weight:700;">Step-by-Step Worked Solution</span>
          </div>
          <p style="text-indent:0; margin-bottom:10px;"><strong>โจทย์ปัญหา (Problem Statement):</strong><br>ปฏิกิริยา TMSD มีอัตราเร็วพื้นฐานที่ไม่มีโทโฮลด์ $k_0 = 1.0	ext{ M}^{-1}	ext{s}^{-1}$ โดยอัตราเร็วจะเพิ่มขึ้น 10 เท่าต่อทุกๆ 1 เบสที่เพิ่มขึ้น ($lpha = 1.0$) จนกระทั่งอิ่มตัวที่ 6 เบส ($k_{	ext{max}} = 10^6	ext{ M}^{-1}	ext{s}^{-1}$) จงคำนวณหาค่าคงที่อัตราเร็ว $k$ สำหรับโทโฮลด์ความยาว (ก) $L = 3	ext{ nt}$ (ข) $L = 5	ext{ nt}$ (ค) คำนวณเวลาครึ่งชีวิตของปฏิกิริยาเมื่อความเข้มข้นสายขาเข้า $C = 1.0	ext{ }\mu	ext{M}$ สำหรับ $L = 5	ext{ nt}$</p>
          <div style="background:rgba(255,255,255,0.85); border:1px solid #e2e8f0; padding:12px 16px; border-radius:6px; margin:12px 0;">
            <strong style="color:#1e3a8a;">การวิเคราะห์และการคำนวณอย่างละเอียด:</strong><br>
            <p style="text-indent:0; margin:6px 0 0 0; line-height:1.85;">1. สำหรับ $L = 3\text{ nt}$: $k = 1.0 \times 10^3 = 1.0 \times 10^3\text{ M}^{-1}\text{s}^{-1}$<br>2. สำหรับ $L = 5\text{ nt}$: $k = 1.0 \times 10^5\text{ M}^{-1}\text{s}^{-1}$<br>3. ปฏิกิริยาอันดับหนึ่งเทียม: $k_{\text{obs}} = k \times C = (1.0 \times 10^5\text{ M}^{-1}\text{s}^{-1}) \times (1.0 \times 10^{-6}\text{ M}) = 0.10\text{ s}^{-1}$<br>4. เวลาครึ่งชีวิต $t_{1/2} = \frac{\ln(2)}{k_{\text{obs}}} = \frac{0.6931}{0.10\text{ s}^{-1}} = 6.93\text{ วินาที}$</p>
          </div>
          <div style="background:#f0fdf4; border-left:4px solid #16a34a; padding:10px 14px; margin-top:10px; font-size:9.5pt; color:#166534; border-radius:0 6px 6px 0;">
            💡 <strong>นัยสำคัญทางกายภาพและการประยุกต์ใช้งาน (Physical Insight):</strong><br>
            <span style="color:#14532d;">การปรับความยาวโทโฮลด์เป็น 5 เบส ทำให้หุ่นยนต์ดีเอ็นเอสามารถตอบสนองและเปิดฝากล่องยาได้ภายในเวลาเพียงไม่กี่วินาที</span>
          </div>
        </div>
            
        <div class="example-box">
          <div class="example-header">
            <span>📝 ตัวอย่างการคำนวณที่ 7.1: การคำนวณกำลังและประสิทธิภาพเชิงกลของ DNA Nanomotor</span>
            <span style="background:#dcfce7; color:#15803d; font-size:8.5pt; padding:3px 10px; border-radius:4px; font-weight:700;">Step-by-Step Worked Solution</span>
          </div>
          <p style="text-indent:0; margin-bottom:10px;"><strong>โจทย์ปัญหา (Problem Statement):</strong><br>มอเตอร์ดีเอ็นเอก้าวเดินด้วยแรงฉุด $F = 3.0	ext{ pN}$ ด้วยความเร็ว $v = 0.50	ext{ nm/s}$ โดยใช้พลังงานจากการสลายพันธะไฮโดรเจน 1 ก้าว $\Delta G = 15.0	ext{ kcal/mol} = 62.76	ext{ kJ/mol}$ ($1.042 	imes 10^{-19}	ext{ J}$ ต่อก้าวขนาด $5.0	ext{ nm}$) จงคำนวณหากำลังกล $P$ และประสิทธิภาพทางกล $\eta$</p>
          <div style="background:rgba(255,255,255,0.85); border:1px solid #e2e8f0; padding:12px 16px; border-radius:6px; margin:12px 0;">
            <strong style="color:#1e3a8a;">การวิเคราะห์และการคำนวณอย่างละเอียด:</strong><br>
            <p style="text-indent:0; margin:6px 0 0 0; line-height:1.85;">1. กำลังกล $P = F \times v = (3.0 \times 10^{-12}\text{ N}) \times (0.50 \times 10^{-9}\text{ m/s}) = 1.50 \times 10^{-21}\text{ W}$<br>2. งานกลต่อหนึ่งก้าว $W = F \times \Delta x = (3.0 \times 10^{-12}\text{ N}) \times (5.0 \times 10^{-9}\text{ m}) = 1.50 \times 10^{-20}\text{ J}$<br>3. ประสิทธิภาพเชิงกล $\eta = \frac{W}{\Delta G_{\text{step}}} = \frac{1.50 \times 10^{-20}\text{ J}}{1.042 \times 10^{-19}\text{ J}} = 0.1439 = 14.4\%$</p>
          </div>
          <div style="background:#f0fdf4; border-left:4px solid #16a34a; padding:10px 14px; margin-top:10px; font-size:9.5pt; color:#166534; border-radius:0 6px 6px 0;">
            💡 <strong>นัยสำคัญทางกายภาพและการประยุกต์ใช้งาน (Physical Insight):</strong><br>
            <span style="color:#14532d;">ประสิทธิภาพเชิงกล $14.4\%$ จัดว่าสูงมากสำหรับเครื่องจักรระดับโมเลกุลเดี่ยวที่ทำงานภายใต้การชนของโมเลกุลน้ำแบบบราวน์</span>
          </div>
        </div>
              </div>
  <div class="code-group">

        <div class="code-box">
          <div class="code-header">💻 แบบจำลองเชิงคำนวณภาษาไพทอน (Computational Python 3.11): กรณีศึกษา: หุ่นยนต์นาโนดีเอ็นเออัจฉริยะรักษามะเร็งในสัตว์ทดลอง (Nature Biotechnology, 2018)</div>
          <pre><code>ทีมนักวิทยาศาสตร์ร่วมระหว่างสถาบัน NCNST ประเทศจีนและมหาวิทยาลัยแอริโซนา ประสบความสำเร็จในการใช้นาโนโรบอตดีเอ็นเอที่ติดโมเลกุล Thrombin นำส่งสู่หลอดเลือดเนื้องอกในหนูทดลอง ทำให้ก้อนมะเร็งฝ่อตัวลงและยับยั้งการแพร่กระจายของมะเร็งได้อย่างสมบูรณ์</code></pre>
        </div>
        <p style="font-size:9.5pt; color:#475569; margin-top:-6px; margin-bottom:18px; text-indent:0;"><em>คำอธิบายอัลกอริทึมการจำลอง:</em> สคริปต์ไพทอนสำหรับการคำนวณและจำลองเชิงตัวเลข</p>
              </div>
  <div class="lab-connection-block">
    <h3>🔬 การเชื่อมโยงสู่ห้องปฏิบัติการเสมือนจริงและเทคนิคการทดลอง (Virtual Lab Connection)</h3>
    <div style='background:#f0fdf4; border:1px solid #bbf7d0; border-left:5px solid #16a34a; padding:12px 16px; margin-bottom:14px; border-radius:6px;'><strong style='color:#166534; font-size:10.5pt;'>การจำลองจลนศาสตร์การเดินของ DNA Walker บนแผ่นนาโน</strong><p style='margin:6px 0 0 0; color:#14532d; text-indent:0; line-height:1.8;'>dna_walker_sim.py</p></div>
  </div>
  <div class="cases-block">
    <h3>🌐 กรณีศึกษางานวิจัยแนวหน้าและนวัตกรรมอุตสาหกรรม (Frontier Case Studies)</h3>
    <div style='background:#eff6ff; border:1px solid #bfdbfe; border-left:5px solid #2563eb; padding:12px 16px; margin-bottom:14px; border-radius:6px;'><strong style='color:#1e40af; font-size:10.5pt;'>การเชื่อมโยงกับ Virtual Lab 35: การจำลองนาโนโรโบติกส์ชีวภาพและดีเอ็นเอออริกามิ</strong><p style='margin:6px 0 0 0; color:#1e3a8a; text-indent:0; line-height:1.8;'>ผู้เรียนสามารถออกแบบสายรหัสดีเอ็นเอออริกามิใน Lab 35 ประกอบเป็นกล่องนาโนบรรจุยา และจำลองการเปิดกล่องด้วยสัญญาณดีเอ็นเอเป้าหมาย</p></div>
  </div>

      <div class="checkpoint-box" style="background:#fefce8; border:1px solid #fef08a; border-left:5px solid #eab308; padding:14px 18px; margin:24px 0 35px 0; border-radius:6px; page-break-inside:avoid;">
        <strong style="color:#854d0e; font-size:10pt;">🎯 จุดตรวจประเมินความเข้าใจและคำถามทบทวนประจำหัวข้อ 7.5 (Concept Checkpoint)</strong>
        <ul style="margin:8px 0 0 0; padding-left:20px; color:#713f12; font-size:9.5pt; line-height:1.8;">
          <li>จงอธิบายแนวคิดรวบยอดหลักของ นาโนโรโบติกส์ชีวภาพและโครงสร้างดีเอ็นเอออริกามิ และความแตกต่างจากพฤติกรรมในระดับมหภาค</li>
          <li>พารามิเตอร์ใดเป็นปัจจัยวิกฤตที่ควบคุมสมบัติทางฟิสิกส์ในหัวข้อนี้ และมีผลกระทบอย่างไร?</li>
          <li>เชื่อมโยงหลักการฟิสิกส์ในหัวข้อนี้เข้ากับการประยุกต์ใช้จริงในเทคโนโลยีสมัยใหม่</li>
        </ul>
      </div>
    </div>
    

      <div class="summary-box">
        <h3 style="color:#1e40af; margin-top:0; font-size:13pt;">📋 สรุปสาระสำคัญประจำบทที่ 7 (Chapter 7 Key Takeaways)</h3>
        <ul style="margin:0; padding-left:22px; font-size:10pt; line-height:1.95; color:#1e293b;">
          <li style='margin-bottom:8px;'>อนุภาคนาโนไขมัน (LNPs) อาศัยคุณสมบัติ Ionizable Lipid ปรับเปลี่ยนประจุตาม pH เพื่อห่อหุ้ม mRNA และช่วยการหลุดรอดจากเอนโดโซม</li><li style='margin-bottom:8px;'>จุดควอนตัมชีวภาพปลอดสารพิษมีความสว่างและเสถียรภาพแสงสูงมาก รองรับการตรวจวัดแบบ Multiplexed Imaging และระบบ FRET</li><li style='margin-bottom:8px;'>การบำบัดด้วยความร้อนแม่เหล็ก (SPIONs) แปลงพลังงานสนามแม่เหล็ก AMF เป็นความร้อนผ่าน Néel และ Brownian Relaxation ทำลายมะเร็งเฉพาะจุด</li><li style='margin-bottom:8px;'>เทคโนโลยี Organ-on-a-Chip จำลองสรีรวิทยาอวัยวะมนุษย์ด้วยของไหลจุลภาคแบบ Laminar Flow ลดและทดแทนการใช้สัตว์ทดลอง</li><li style='margin-bottom:8px;'>นาโนโรโบติกส์ชีวภาพและ DNA Origami ใช้กลไก Toehold Strand Displacement (TMSD) สร้างเครื่องจักรโมเลกุลอัตโนมัติสำหรับนำส่งยาแม่นยำ</li>
        </ul>
      </div>

      <div class="problems-section">
        <h3 style="color:#0f172a; margin-top:0; font-size:14pt; border-bottom:2px solid #cbd5e1; padding-bottom:8px;">
          📚 แบบฝึกหัดและโจทย์ปัญหาท้ายบทที่ 7 (End-of-Chapter Problems)
        </h3>
        
        <h4 style="color:#1e3a8a; font-size:11.5pt; margin-top:18px;">ตอนที่ 1: คำถามเชิงมโนทัศน์และการวิเคราะห์เชิงฟิสิกส์ (Conceptual & Analytical Questions)</h4>
        <ol style="padding-left:22px; font-size:10pt; line-height:1.9; color:#334155;">
          <li style='margin-bottom:8px;'>จงอธิบายบทบาทของไขมัน 4 ชนิดในโครงสร้างอนุภาคนาโนไขมัน (LNPs) สำหรับวัคซีน mRNA</li><li style='margin-bottom:8px;'>เพราะเหตุใดค่า pKa ของ Ionizable Lipid ที่เหมาะสมจึงต้องอยู่ในช่วง 6.0 - 6.8?</li><li style='margin-bottom:8px;'>จงเปรียบเทียบข้อดีและข้อจำกัดระหว่างจุดควอนตัมชีวภาพ (Bio-QDs) กับสีย้อมอินทรีย์ดั้งเดิม</li><li style='margin-bottom:8px;'>อธิบายกลไกการถ่ายโอนพลังงาน Förster Resonance Energy Transfer (FRET) และความสัมพันธ์กับระยะห่าง $1/r^6$</li><li style='margin-bottom:8px;'>จงเปรียบเทียบความแตกต่างระหว่างการคลายตัวแบบนีล (Néel) และการคลายตัวแบบบราวน์ (Brownian) ใน SPIONs</li><li style='margin-bottom:8px;'>ค่า SAR (Specific Absorption Rate) บ่งบอกถึงคุณสมบัติใดในการรักษาด้วยความร้อนแม่เหล็ก?</li><li style='margin-bottom:8px;'>เพราะเหตุใดการไหลในช่องของไหลจุลภาค Microfluidics จึงเป็นการไหลแบบ Laminar Flow เสมอ?</li><li style='margin-bottom:8px;'>จงอธิบายหลักการทำงานของ Toehold-Mediated Strand Displacement (TMSD) ในการควบคุมการเปิด-ปิดกล่องนาโนโรบอตดีเอ็นเอ</li>
        </ol>

        <h4 style="color:#166534; font-size:11.5pt; margin-top:22px;">ตอนที่ 2: โจทย์ปัญหาการคำนวณเชิงตัวเลขและการพิสูจน์ (Quantitative & Numerical Problems)</h4>
        <ol style="padding-left:22px; font-size:10pt; line-height:1.9; color:#334155;">
          <li style='margin-bottom:8px;'>คำนวณร้อยละของประจุบวกในไขมัน ALC-0315 ($	ext{p}K_a = 6.09$) ที่ $	ext{pH} = 7.4$ และที่ $	ext{pH} = 5.0$</li><li style='margin-bottom:8px;'>ต้องการผลิตวัคซีน mRNA ปริมาณ $50	ext{ }\mu	ext{g}$ ให้มีอัตราส่วน $	ext{N/P} = 5.0$ จงคำนวณหามวลของ Ionizable Lipid ที่ต้องใช้ ($M = 710	ext{ g/mol}$)</li><li style='margin-bottom:8px;'>คู่ FRET มีค่า $R_0 = 5.0	ext{ nm}$ จงคำนวณหาประสิทธิภาพการถ่ายโอนพลังงาน $E_{	ext{FRET}}$ เมื่อโมเลกุลอยู่ห่างกัน $3.5	ext{ nm}$</li><li style='margin-bottom:8px;'>อนุภาค $	ext{Fe}_3	ext{O}_4$ ทรงกลมมีเส้นผ่านศูนย์กลางผลึก $14	ext{ nm}$ ($K_u = 1.3 	imes 10^4	ext{ J/m}^3$) ที่ $300	ext{ K}$ จงคำนวณเวลาคลายตัวแบบนีล $	au_N$</li><li style='margin-bottom:8px;'>สารละลาย SPIONs มวลเหล็ก 4.0 mg ในน้ำ 1.0 mL มีอุณหภูมิเพิ่มขึ้น 8.0 °C ในเวลา 40 วินาที จงคำนวณหาค่า SAR</li><li style='margin-bottom:8px;'>ช่อง Microfluidics มี $w = 120	ext{ }\mu	ext{m}$, $h = 40	ext{ }\mu	ext{m}$ มีน้ำไหลด้วยความเร็ว $2.0	ext{ mm/s}$ จงคำนวณหาเลขเรย์โนลด์ส $	ext{Re}$</li><li style='margin-bottom:8px;'>ปฏิกิริยา TMSD มีโทโฮลด์ยาว 4 เบส ($k = 1.0 	imes 10^4	ext{ M}^{-1}	ext{s}^{-1}$) ในสารละลายความเข้มข้น $2.0	ext{ }\mu	ext{M}$ จงคำนวณหาเวลาครึ่งชีวิต $t_{1/2}$</li>
        </ol>

        <h4 style="color:#7c2d12; font-size:11.5pt; margin-top:22px;">ตอนที่ 3: โจทย์ประยุกต์ การออกแบบเชิงวิศวกรรม และการจำลอง (Applied Design & Modeling Problems)</h4>
        <ol style="padding-left:22px; font-size:10pt; line-height:1.9; color:#334155;">
          <li style='margin-bottom:8px;'>จงออกแบบสูตรตำรับอนุภาคนาโน LNP สำหรับการนำส่งยีนบำบัดรักษาโรคมะเร็งตับ โดยระบุชนิดไขมันและสัดส่วนโมลาร์</li><li style='margin-bottom:8px;'>ออกแบบระบบอวัยวะบนชิปไต (Kidney-on-a-Chip) สำหรับการตรวจวัดความเป็นพิษต่อหน่วยไตของอนุภาคนาโน</li><li style='margin-bottom:8px;'>วิเคราะห์แนวทางการใช้นาโนโรบอตดีเอ็นเอร่วมกับอนุภาคแม่เหล็กในการนำส่งยาสลายลิ่มเลือดในหลอดเลือดสมองอุดตัน</li><li style='margin-bottom:8px;'>เขียนโค้ด Python เพื่อจำลองการแพร่กระจายความร้อนในก้อนเนื้องอกทรงกลมที่ถูกกระตุ้นด้วยอนุภาคแม่เหล็ก SPIONs</li>
        </ol>
      </div>
    </div>
    """
