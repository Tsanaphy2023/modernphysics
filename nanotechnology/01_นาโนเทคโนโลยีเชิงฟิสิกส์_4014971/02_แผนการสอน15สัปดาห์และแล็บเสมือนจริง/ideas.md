# แนวคิดการออกแบบ: Nanophysics Virtual Lab 01

## แนวทางที่พิจารณา

### 1. Observatory Notebook

**Very Brief Intro:** ห้องปฏิบัติการเชิงวิทยาศาสตร์ในบรรยากาศของสมุดบันทึกภาคสนาม ใช้กระดาษอุ่น รอยเส้นพิมพ์ และข้อมูลสีน้ำเงินหมึกเพื่อให้การสังเกตมีน้ำหนักเหมือนหลักฐานทดลองจริง

**Probability:** 0.037

### 2. Precision Instrument Console

**Very Brief Intro:** หน้าจอเครื่องมือวัดในห้อง cleanroom ที่เงียบ สุขุม และแม่นยำ ผสานแผงควบคุมแบบ instrument panel กับพื้นที่แสดงผลที่โปร่งสำหรับให้นักศึกษาเปรียบเทียบเรขาคณิตและข้อมูลเชิงปริมาณ

**Probability:** 0.082

### 3. Museum of Invisible Matter

**Very Brief Intro:** ประสบการณ์จัดแสดงวัตถุระดับนาโนแบบพิพิธภัณฑ์ร่วมสมัย เน้นแสง เงา และโมเดลลอยตัวเพื่อทำให้สิ่งที่มองไม่เห็นเกิดความน่าตื่นตา

**Probability:** 0.014

---

## แนวทางที่เลือก: Precision Instrument Console

### Design Movement

ได้รับอิทธิพลจาก **Swiss scientific instrument design** และ **contemporary laboratory control interfaces**: มีวินัย ชัดเจน ใช้พื้นที่ว่างเพื่อสนับสนุนการอ่านค่า และให้ข้อมูลเป็นแกนกลางขององค์ประกอบ

### Core Principles

1. ทุกพื้นผิวต้องช่วยให้นักศึกษาอ่านค่า ทำนายผล หรือเปรียบเทียบข้อมูลได้ ไม่ใช้การตกแต่งที่แย่งความสนใจจากฟิสิกส์
2. แยกโลกของ “วัตถุ” และ “ข้อมูล” อย่างมีจังหวะ: ภาพโมเดล 3D อยู่บนพื้นหลังเข้ม ส่วนกราฟและการควบคุมอยู่บนกระดาษอุ่นที่อ่านง่าย
3. ใช้เส้น grid, scale marks และป้ายกำกับเชิงเครื่องมือเป็น motif ซ้ำ เพื่อทำให้พื้นที่ทั้งหมดรู้สึกเหมือน workbench เดียวกัน
4. ให้ feedback ของการปรับค่าเกิดทันที โดยตัวเลขสำคัญและกราฟต้องเปลี่ยนอย่างเห็นได้ชัดแต่ไม่เคลื่อนไหวเกินจำเป็น

### Color Philosophy

ใช้ **หมึกน้ำเงินเข้ม** เป็นพื้นที่ที่วัตถุระดับนาโนถูกสังเกต ใช้พื้นสีงาช้างอุ่นเป็นพื้นที่วิเคราะห์ และใช้ **phosphor lime** เป็นสีของค่าที่กำลังถูกวัดหรือเลือกอยู่ สีส้มสนิมใช้เฉพาะ warning/assumption เพื่อแยกสถานะเชิงวิทยาศาสตร์ ไม่ใช้ gradient สีม่วงหรือแสง neon

### Layout Paradigm

หน้าเว็บเป็น **instrument workbench แบบแนวนอน**: แถบสถานะด้านบน → แผงควบคุมแนวตั้งด้านซ้าย → เวทีโมเดลและค่าที่วัดได้กลางหน้า → สมุดบันทึกผลและกราฟด้านขวา/ด้านล่าง บนจอเล็กแผงเหล่านี้จะเรียงเป็นลำดับ “ตั้งค่า → สังเกต → วิเคราะห์”

### Signature Elements

1. **Calibration strip:** แถบขีด scale และค่าหน่วยที่วางตามขอบของแผงสำคัญ
2. **Lime measurement marker:** จุด/เส้นสีเขียวมะนาวสำหรับค่าที่กำลังเลือกและจุดข้อมูลหลัก
3. **Wireframe specimen stage:** ฐาน grid แบบ perspective ที่รองรับโมเดลอนุภาค 3D ทุกประเภท

### Interaction Philosophy

การปรับ slider ต้องรู้สึกเหมือนหมุน dial ของเครื่องมือ และผลที่สัมพันธ์กันต้องเปลี่ยนทันที ปุ่ม “บันทึก snapshot” และ “สุ่มตัวอย่าง” สร้างหลักฐานใน log โดยไม่บังคับให้นักศึกษาออกจาก workflow หลัก

### Animation

โมเดล 3D หมุนอย่างช้ามากเฉพาะเมื่อยังไม่มี interaction และหยุดเมื่อผู้ใช้เริ่มควบคุม ส่วนที่เปลี่ยนค่าใช้ transition ของ opacity/transform ภายใน 180–220ms พร้อม easing แบบ snappy ไม่มีแอนิเมชันที่รบกวนการอ่านกราฟ และเคารพ `prefers-reduced-motion`

### Typography System

หัวเรื่องใช้ **Space Grotesk** น้ำหนัก 600–700 เพื่อให้โครงสร้างเหมือนป้ายเครื่องมือ ตัวเลข ค่าหน่วย และ code label ใช้ **IBM Plex Mono** เพื่อเพิ่มความน่าเชื่อถือของข้อมูล ส่วนเนื้อหาใช้ **Noto Sans Thai** เพื่อรองรับภาษาไทยและอ่านเป็นธรรมชาติ ลำดับชั้น: label ตัวพิมพ์ใหญ่/mono → หัวข้อ Space Grotesk → คำอธิบาย Noto Sans Thai

### Brand Essence

**Nanophysics Virtual Lab 01 คือ workbench เชิงคำนวณสำหรับนักฟิสิกส์รุ่นใหม่ที่ต้องการเชื่อมรูปทรงระดับนาโนเข้ากับหลักฐานเชิงปริมาณอย่างตรวจสอบได้**

บุคลิก: **แม่นยำ, สงบ, กระตุ้นการค้นพบ**

### Brand Voice

น้ำเสียงตรง กระชับ และชวนให้ตั้งสมมติฐานก่อนดูผลลัพธ์ หลีกเลี่ยงคำโฆษณาทั่วไป และเรียกสิ่งต่าง ๆ ตามหน้าที่เชิงวิทยาศาสตร์

ตัวอย่างข้อความ:

> “ปรับรัศมี แล้วตรวจสอบว่าพื้นที่ผิวต่อปริมาตรเปลี่ยนเร็วเพียงใด”

> “บันทึกผลลัพธ์นี้เป็นหลักฐานก่อนเปลี่ยนตัวแปรถัดไป”

### Wordmark & Logo

โลโก้เป็นสัญลักษณ์ **ทรงกลมระดับนาโนที่ถูกตัดด้วยเส้นวัดแนวนอนและจุด calibration 3 จุด** สื่อถึง geometry + measurement โดยไม่มีข้อความในตัวสัญลักษณ์ Wordmark ใช้ตัวอักษร Space Grotesk ที่มีการจัดระยะตัวอักษรแบบ technical label

### Signature Brand Color

**Phosphor Lime — #C7F36B**: สีที่ใช้ชี้ measurement state, active control และหลักฐานที่นักศึกษาควรสังเกต

## Style Decisions

- หน้าเว็บใช้โหมดหลักสีเข้มแบบ instrument console แต่เขตการอ่านกราฟและสมุดบันทึกใช้พื้นงาช้างอุ่นเพื่อการอ่านระยะยาว
- ใช้ layout แบบ asymmetric workbench; หลีกเลี่ยง hero ที่จัดกึ่งกลางหรือการ์ดมุมมนซ้ำ ๆ
- โมเดล 3D เป็น primitive geometry แบบโปร่งและมีฐาน grid ไม่ใช้ภาพผลิตภัณฑ์สำเร็จรูปแทนการคำนวณ
- ภาพประกอบที่สร้างจะใช้เฉพาะส่วนแบรนด์/hero และต้องไม่มีตัวอักษร เพื่อไม่ให้ชนกับข้อความ UI ที่มีความแม่นยำ

### ส่วนขยายจากการทบทวนภาษาภาพ

- **Brand architecture:** `Nanophysics Virtual Lab / 01` เป็น wordmark หลักทุก route; `Nano Materials Lab` ทำหน้าที่เป็นป้าย module เชิงเทคนิคเท่านั้น
- **Evidence-first imagery:** visual เด่นต้องอ่านเป็น measurement evidence เช่น scan map, primitive model, calibration grid และ plotted trace ส่วนภาพเครื่องมือจริงใช้เป็นบรรยากาศรองเท่านั้น
- **Lime rule:** Phosphor Lime `#C7F36B` ใช้กับ active control, selected data, measurement marker, key numeric evidence และ primary action เท่านั้น หัวเรื่องหลักใช้หมึก/งาช้างเป็นโครงสร้าง
- **Catalog as instrument rack:** catalog และ learning section ต้องสื่อ workflow, observable และ evidence ผ่าน calibration strips, rack IDs, status labels และ scale marks แทน card grid เชิงการตลาด
- **Spectrum evidence rule:** ในหน้าสเปกตรัม เส้น measured, fitted envelope และ selected component ต้องแยกสี/เส้นให้ชัดเจน; lime สงวนไว้สำหรับ fit ที่ผู้ใช้กำลังแก้และค่าที่เลือกอยู่
- **Instrument rack metadata:** แต่ละเครื่องมือหลักต้องแสดง Rack ID, family และ observable เพื่อสื่อว่าเป็นโมดูลวัดในระบบเดียวกัน ไม่ใช่การ์ดนำทางทั่วไป
- **2D quantum evidence rule:** หน้า 2D/Quantum Materials ใช้ lime เฉพาะ marker, selected value และ primary action; headline ต้องระบุ hypothesis/variable/observable โดยตรง และทุก analysis card ต้องมี Rack ID, observable label และ calibration cue
- **Two-world analysis rhythm:** เขต analysis ของโมดูลควอนตัมใช้พื้นงาช้างอุ่นและ grid ที่ลดความเข้ม เพื่อแยกจาก specimen stage เข้มโดยไม่ใช้พื้น pastel สีเขียวเป็นชั้นนำสายตา
- **STM/STS evidence foreground:** ภาพ STM จริงใช้เป็น texture เชิงบรรยากาศเท่านั้น โดย foreground ต้องเป็น lattice, scan window, calibration reticle, junction gap marker และ trace ของ observable เสมอ
- **Module identity rule:** preset, control, stage, readout, analysis card และ footer ต้องเผย Rack/Module cue, observable และ unit/setpoint cue เพื่ออ่านเป็น instrument suite เดียวกัน
- **STM lime rule:** Lime ใน STM/STS หมายถึง active observable, selected local site, junction gap marker หรือ current scan action เท่านั้น; ไม่ใช้ตกแต่งหัวเรื่อง
