from pathlib import Path
from openai import OpenAI
import time

OUT = Path('/home/ubuntu/nano_ebook_work/chapters')
OUT.mkdir(parents=True, exist_ok=True)

client = OpenAI()

course_context = """
รายวิชา: 4014971 นาโนเทคโนโลยีเชิงฟิสิกส์ (Nanotechnological Physics) ระดับปริญญาตรี
กรอบ 15 สัปดาห์ เน้นการออกแบบย้อนกลับ (backward design) และการเรียนรู้เชิงรุก
CLO 1 อธิบายระดับนาโน ความสัมพันธ์ขนาด–พื้นที่ผิว และสมบัติที่ขึ้นกับขนาดด้วยหลักฟิสิกส์
CLO 2 เลือกวิธีสังเคราะห์หรือเครื่องมือตรวจวิเคราะห์ให้เหมาะกับโจทย์ พร้อมเหตุผลเรื่องชนิดข้อมูล ข้อจำกัด และความปลอดภัย
CLO 3 ปฏิบัติการ/วิเคราะห์ข้อมูลตาม SOP บันทึกอย่างเป็นระบบ และปฏิบัติอย่างปลอดภัยและมีจริยธรรม
CLO 4 วิเคราะห์ภาพ สเปกตรัม หรือข้อมูลเชิงปริมาณ ด้วยกราฟ สถิติพื้นฐาน และความไม่แน่นอน แล้วสรุปตามหลักฐาน
CLO 5 ประเมินการประยุกต์ใช้โดยพิจารณากลไก ประโยชน์ ข้อจำกัด ความเสี่ยง และผลกระทบต่อสังคม/สิ่งแวดล้อม
CLO 6 สื่อสารและทำงานร่วมกันอย่างรับผิดชอบ อ้างอิงข้อมูลเหมาะสม และตอบคำถามจากหลักฐาน
CLO 7 (ใช้สำหรับสายครู) ออกแบบกิจกรรมระดับโรงเรียนที่ถูกต้อง ปลอดภัย และประเมินผลสอดคล้อง
แนว Lab: เริ่มด้วยแบบจำลองมหภาคและ Data Lab ใช้ชุดข้อมูล ภาพ หรือสเปกตรัมที่ได้รับอนุญาตเป็นหลัก หลีกเลี่ยงผงนาโนแห้งในกิจกรรมผู้เรียน เว้นแต่มี SOP การประเมินความเสี่ยง ระบบควบคุม และผู้กำกับดูแลครบถ้วน
"""

sources = """
อ้างอิงที่อนุญาต (ใช้เลขในวงเล็บเหลี่ยมเฉพาะเมื่อมีการอ้างข้อเท็จจริงสำคัญ):
[1] เอกสาร มคอ.3 รายวิชา 4014971 นาโนเทคโนโลยีเชิงฟิสิกส์ (เอกสารรายวิชาที่ผู้ใช้ให้)
[2] National Institute of Standards and Technology. Engineering and Optical Characterization of Magnetic Nanoparticles. https://www.nist.gov/programs-projects/engineering-and-optical-characterization-magnetic-nanoparticles-mnps
[3] Hackley, V. A., & Clogston, J. D. NIST–NCL Joint Assay Protocol: Measuring the Size of Nanoparticles in Aqueous Media Using Batch-Mode Dynamic Light Scattering. NCBI Bookshelf. https://www.ncbi.nlm.nih.gov/books/NBK604904/
[4] University of North Carolina at Chapel Hill. Laboratory Safety Manual, Chapter 18: Safe Use of Nanomaterials. https://policies.unc.edu/TDClient/2833/Portal/KB/Article/132030/Laboratory-Safety-Manual-Chapter-18-Safe-Use-of-Nanomaterials
[5] NIOSH. Current Strategies for Engineering Controls in Nanomaterial Production and Downstream Handling Processes. https://www.cdc.gov/niosh/docs/2014-102/default.html
[6] National Nanotechnology Initiative. https://www.nano.gov/
ใช้การอ้างอิงแบบ [2] ในเนื้อหาเท่านั้น ห้ามสร้างแหล่งอ้างอิงใหม่ ห้ามสร้างเลข DOI หรือ URL ที่ไม่อยู่ในรายการ
"""

chapters = [
    ("01", "บทที่ 1 พื้นฐานนาโนเทคโนโลยีเชิงฟิสิกส์และการคิดเชิงมาตราส่วน", """
เนื้อหาต้องมี: ความหมายของระดับนาโน 1–100 nm, การแปลงหน่วย, อะตอม/โมเลกุล/วัสดุ, พื้นที่ผิวต่อปริมาตร, การเปรียบเทียบขนาด, ข้อจำกัดของการเปรียบเทียบเชิงอุปมา, กิจกรรม Predict–Observe–Explain, Lab แบบจำลองพื้นที่ผิว, Data Lab อ่าน scale bar, ตัวอย่างโจทย์คำนวณ 3 ข้อ, โค้ด Python คำนวณ A/V และสร้างกราฟ, แบบฝึกหัดแนวคิด 6 ข้อและแบบทดสอบย่อย 5 ข้อพร้อมแนวเฉลยย่อ
"""),
    ("02", "บทที่ 2 สมบัติที่ขึ้นกับขนาด พื้นผิว และการกักขังเชิงควอนตัม", """
เนื้อหาต้องมี: สมบัติทางแสง แม่เหล็ก ไฟฟ้า และปฏิกิริยาที่เกี่ยวข้องกับขนาด/รูปร่าง/องค์ประกอบ/ตัวกลาง; อธิบายควอนตัมอย่างระวัง; ตัวอย่าง nanoparticles แม่เหล็กโดยไม่กล่าวอ้างเกินแหล่งอ้างอิง; Data Lab อ่านสเปกตรัม; โค้ด Python สร้างชุดข้อมูลสเปกตรัมตัวอย่างและหา peak; กิจกรรมโต้แย้งจากหลักฐาน; แบบฝึกหัด 8 ข้อและแบบทดสอบย่อย 5 ข้อพร้อมแนวเฉลยย่อ
"""),
    ("03", "บทที่ 3 การสังเคราะห์วัสดุนาโนและการออกแบบกระบวนการ", """
เนื้อหาต้องมี: top-down/bottom-up, แนวคิด nucleation-growth ระดับอธิบาย, sol-gel, precipitation, hydrothermal, physical vapor deposition, lithography ในระดับแนวคิด, ตัวแปรกระบวนการ, การทำซ้ำได้, คุณภาพข้อมูล, การเลือกกระบวนการจากโจทย์, risk-based thinking, workshop ออกแบบ process flow, แบบฟอร์มอธิบายตัวแปร, แบบฝึกหัดและ case study พร้อมแนวเฉลยย่อ
"""),
    ("04", "บทที่ 4 เครื่องมือการตรวจวิเคราะห์: จากคำถามวิจัยสู่หลักฐาน", """
เนื้อหาต้องมี: กรอบ Question–Information–Technique–Limitation; microscopy (optical, SEM, TEM, AFM) ระดับแนวคิด, XRD, UV-Vis, FTIR/Raman, DLS และ zeta potential ระดับแนวคิด; สิ่งที่วัดได้/ไม่ได้; DLS รายงาน hydrodynamic diameter และขึ้นกับการเตรียมตัวอย่าง/ตัวกลาง; ตารางเลือกเครื่องมือ; decision activity; Data Lab เปรียบเทียบภาพกับ DLS; แบบฝึกหัด 10 ข้อและเฉลยย่อ
"""),
    ("05", "บทที่ 5 การวิเคราะห์ข้อมูล ความไม่แน่นอน และการสื่อสารผล", """
เนื้อหาต้องมี: data integrity, การจัดตารางข้อมูล, mean/SD, กราฟที่รับผิดชอบ, error bars, outlier อย่างระมัดระวัง, repeatability vs reproducibility, calibration concept, uncertainty statement, การเขียน caption, การไม่ตกแต่งภาพ/กราฟให้บิดเบือน, Python pandas/matplotlib ตัวอย่างอ่าน CSV สรุปสถิติและ plot error bars, ใบงานวิเคราะห์ข้อมูล, rubrics ตีความกราฟ, แบบฝึกหัดพร้อมเฉลยย่อ
"""),
    ("06", "บทที่ 6 ห้องปฏิบัติการและห้องวิเคราะห์ข้อมูลเพื่อการเรียนรู้ระดับนาโน", """
เนื้อหาต้องมี: ข้อกำหนดการทำ Lab ปลอดภัย, hierarchy of controls ระดับนำไปใช้, SOP/SDS/risk assessment, การจัดการของเสีย, structure ของสมุดปฏิบัติการ, Lab A surface area model, Lab B image analysis, Lab C spectrum/DLS dataset, pre-lab/post-lab, checklist ความปลอดภัย, วิธีให้ผู้สอนเตรียมชุดข้อมูล, accommodation สำหรับผู้เรียน, case scenario เหตุผิดปกติ, rubric ปฏิบัติการและสมุดบันทึก, แบบฝึกหัดพร้อมเฉลยย่อ; ให้เน้นว่านี่ไม่ใช่ SOP ปฏิบัติการจริง
"""),
    ("07", "บทที่ 7 การประยุกต์ใช้นาโนเทคโนโลยีและการตัดสินใจอย่างรับผิดชอบ", """
เนื้อหาต้องมี: การประยุกต์ในวัสดุ พลังงาน อิเล็กทรอนิกส์ เซนเซอร์ การแพทย์ และสิ่งแวดล้อมในระดับภาพรวม; value–risk–evidence framework; life-cycle thinking, uncertainty, green design, social equity, การแยกข้อมูลวิทยาศาสตร์ออกจากข้ออ้างทางการตลาด, structured academic debate, case study 3 กรณี, แบบฟอร์ม decision memo, แบบฝึกหัดและเฉลยย่อ
"""),
    ("08", "บทที่ 8 โครงงานบูรณาการ: ออกแบบ ตรวจวิเคราะห์ และสื่อสารคำตอบ", """
เนื้อหาต้องมี: capstone design brief, ขั้นตอนเลือกปัญหา คำถาม สมมติฐาน ข้อมูล/เครื่องมือ ข้อจำกัด/ความปลอดภัย การตีความผล และสื่อสาร, data-based project ที่ไม่ต้องสังเคราะห์วัสดุจริง, timeline 6 สัปดาห์, role map ของกลุ่ม, peer feedback protocol, poster/oral presentation, rubric โครงงาน, ตัวอย่างหัวข้อ 6 หัวข้อพร้อมขอบเขตข้อมูล, reflection เชื่อม CLO 1–6, สำหรับสายครูมี microteaching CLO7, แบบประเมินและแนวเฉลย/แนวทางให้คะแนน
"""),
    ("09", "บทที่ 9 การวัดและประเมินผลการเรียนรู้ในรายวิชานาโนเทคโนโลยีเชิงฟิสิกส์", """
เนื้อหาต้องมี: constructive alignment, แผน assessment 100 คะแนน, diagnostic/formative/summative, blueprint เชื่อม CLO, rubric แบบ analytic, validity/reliability/fairness ระดับปฏิบัติ, ตัวอย่างข้อสอบปรนัยและอัตนัยที่วัดการใช้เหตุผล ไม่ใช่จำคำ, checklists, self/peer assessment, เกณฑ์ผ่านความปลอดภัย, feedback loop, template บันทึกผล CLO, ตัวอย่างการตีความข้อมูลผลสัมฤทธิ์แบบสรุป, แบบฝึกหัดผู้สอน
"""),
    ("10", "บทที่ 10 การนำไปใช้ในชั้นเรียนและพัฒนาการสอนอย่างต่อเนื่อง", """
เนื้อหาต้องมี: แผน 15 สัปดาห์ฉบับย่อ, การจัดชั้นเรียนขนาดต่างกัน, online/hybrid Data Lab, universal design for learning, การใช้ AI อย่างมีจริยธรรมในงานสรุป/เขียนรายงาน, รายการอุปกรณ์ตามระดับความพร้อม (minimum/standard/advanced), quality assurance ของรายวิชา, action plan ผู้สอน, ภาคสรุปความรู้ทั้งเล่ม, แบบทดสอบสังเคราะห์ปลายเล่ม 15 ข้อพร้อมเฉลยย่อ, glossary 40 คำ และดัชนีคำสำคัญเบื้องต้น
"""),
]

base_prompt = f"""
คุณเป็นผู้เขียนตำราวิชาการภาษาไทยสำหรับผู้เรียนระดับปริญญาตรี เขียนเนื้อหาที่แม่นยำ ชัดเจน และนำไปใช้สอนได้จริงสำหรับ eBook วิชา 'นาโนเทคโนโลยีเชิงฟิสิกส์' โปรดสร้างเนื้อหารายบทตามโจทย์ที่กำหนดด้านล่าง

{course_context}
{sources}

รูปแบบการเขียน:
- เขียนภาษาไทยเป็นหลัก และตามด้วยศัพท์อังกฤษในวงเล็บเมื่อกล่าวครั้งแรก
- ใช้ Markdown ที่สมบูรณ์ มีหัวข้อระดับ ## และ ### ตาราง Markdown ย่อหน้าเต็ม และ blockquote เฉพาะจุดที่เป็นคำเตือนหรือหลักคิดสำคัญ
- ทุกบทต้องมี: บทนำ, วัตถุประสงค์ประจำบท, ภูมิหลังเชิงทฤษฎี, การประยุกต์ใช้ด้านวิทยาศาสตร์หรือการศึกษาวิทยาศาสตร์, ตาราง/ชุดข้อมูลตัวอย่าง, กิจกรรมการเรียนรู้หรือ Data Lab, โค้ด Python อย่างน้อยหนึ่งส่วนพร้อมคำอธิบาย (หากเป็นบทที่ไม่ต้องคำนวณให้เป็น pseudo-data/assessment helper ที่ใช้ได้จริง), สรุปบท, แบบฝึกหัด, คำถามแบบทดสอบย่อย และแนวเฉลยย่อ, เอกสารอ้างอิงเฉพาะที่ใช้ในบท
- โค้ดต้องใช้ NumPy, pandas หรือ matplotlib เท่านั้น และควรเป็นโค้ดที่รันได้โดยไม่ต้องพึ่งไฟล์ภายนอก ยกเว้นเมื่อมีการใช้ CSV ให้แทรกวิธีสร้าง dataframe ตัวอย่างในโค้ด
- ห้ามให้สูตร ขั้นตอนปริมาณ หรือเงื่อนไขที่ทำให้นักศึกษาสามารถสังเคราะห์หรือจัดการผงนาโนจริงได้เอง ให้เสนอเป็น Data Lab/แบบจำลอง/กิจกรรมภายใต้ SOP เท่านั้น
- อ้างอิงเฉพาะ [1]–[6] ตามที่ให้มาเมื่อกล่าวข้อเท็จจริง และใช้สำนวนระมัดระวังในประเด็นที่ขึ้นกับชนิดวัสดุหรือเงื่อนไขทดลอง
- ห้ามอ้างตัวเลขหรือผลการทดลองที่ไม่มีแหล่งที่มา; ชุดข้อมูลตัวอย่างต้องระบุว่าเป็น 'ข้อมูลจำลองเพื่อการเรียนรู้'
- ความยาวเป้าหมายต่อบทอย่างน้อย 4,000 คำภาษาไทย โดยเน้นคำอธิบายที่ละเอียด มีตัวอย่างและการเชื่อมโยงกับ CLO หลีกเลี่ยงการซ้ำเนื้อหาระหว่างบท
- ไม่ต้องสร้าง Title page หรือสารบัญรวม
"""

for code, title, scope in chapters:
    path = OUT / f'{code}.md'
    if path.exists() and path.stat().st_size > 2500:
        print(f'Skip existing {path.name}')
        continue
    prompt = base_prompt + f"\n\n# {title}\n\nขอบเขตเนื้อหาเฉพาะบท:\n{scope}\n"
    for attempt in range(3):
        try:
            resp = client.chat.completions.create(
                model='gpt-5-mini',
                messages=[
                    {'role': 'system', 'content': 'คุณเป็นนักวิชาการด้านฟิสิกส์วัสดุและนักออกแบบการเรียนรู้ที่รักษาความถูกต้องทางวิชาการและความปลอดภัยเป็นอันดับแรก'},
                    {'role': 'user', 'content': prompt},
                ],
                max_completion_tokens=18000,
            )
            text = resp.choices[0].message.content or ''
            if len(text) < 6000:
                raise RuntimeError(f'generated chapter too short: {len(text)} chars')
            path.write_text(text, encoding='utf-8')
            print(f'Wrote {path.name}: {len(text)} chars')
            break
        except Exception as exc:
            print(f'Attempt {attempt + 1} failed for {code}: {exc}')
            if attempt == 2:
                raise
            time.sleep(3 * (attempt + 1))

print('Generation complete')
