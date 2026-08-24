#set text(
  font: ("Noto Sans", "Noto Sans Thai"),
  size: 11pt,
  lang: "th",
)

#set page(
  paper: "a4",
  margin: (x: 2.5cm, y: 2.5cm),
  header: align(right)[
    #text(size: 9pt, fill: gray)[เวิร์กชอปการเขียนโปรแกรม AI ด้วย Python - ฉบับวิชาการ]
  ],
  footer: context [
    #align(center)[#counter(page).display()]
  ],
)

#set heading(numbering: "1.1")
#show heading: set text(fill: rgb("#007BFF"))

// Title Page
#align(center + horizon)[
  #text(size: 32pt, weight: "bold", fill: rgb("#1A1A1A"))[เวิร์กชอปการเขียนโปรแกรม AI ด้วย Python]
  
  #v(1cm)
  #text(size: 18pt, fill: rgb("#007BFF"))[ฉบับวิชาการและวิชาชีพ (Modern Academic Edition)]
  
  #v(2cm)
  #text(size: 14pt)[จัดทำโดย]
  #v(0.5cm)
  #text(size: 16pt, weight: "bold")[Manus AI]
  
  #v(3cm)
  #text(size: 12pt, fill: gray)[สิงหาคม 2569]
]

#pagebreak()

#outline(indent: 2em)

#pagebreak()

#set par(justify: true, leading: 0.8em)

= บทนำ (Introduction)
ในยุคปัจจุบัน ปัญญาประดิษฐ์ (AI) ได้กลายเป็นหัวใจสำคัญของการขับเคลื่อนเทคโนโลยีและนวัตกรรม การเขียนโปรแกรมด้วยภาษา Python จึงเป็นทักษะที่จำเป็นอย่างยิ่งสำหรับนักพัฒนาและนักวิทยาศาสตร์ข้อมูล หลักสูตรนี้ออกแบบมาเพื่อปูพื้นฐานตั้งแต่ระดับเริ่มต้นไปจนถึงการประยุกต์ใช้งานจริงในระดับวิชาการและอุตสาหกรรม

= โครงสร้างข้อมูลและการวิเคราะห์ประสิทธิภาพ (Data Structures & Analysis)
การเลือกโครงสร้างข้อมูลที่เหมาะสมเป็นกุญแจสำคัญในการสร้างระบบ AI ที่มีประสิทธิภาพ

== ความซับซ้อนเชิงเวลา (Time Complexity)
เราใช้ Big O Notation ในการวัดประสิทธิภาพของอัลกอริทึม:
- *O(1)*: การเข้าถึงข้อมูลใน Dictionary
- *O(log n)*: Binary Search
- *O(n)*: การวนลูปผ่าน List
- *O(n log n)*: Sorting algorithms (เช่น Merge Sort)

= การเขียนโปรแกรมเชิงวัตถุสำหรับ AI (OOP for AI)
หลักการ OOP ช่วยให้เราสามารถออกแบบโมเดล AI ที่มีความยืดหยุ่นและบำรุงรักษาง่าย

== สี่เสาหลักของ OOP
1. *Encapsulation*: การห่อหุ้มข้อมูล
2. *Inheritance*: การสืบทอดคุณสมบัติ
3. *Polymorphism*: การพหุสัณฐาน
4. *Abstraction*: การนามธรรม

#figure(
  image("/home/ubuntu/infographic_oop_pillars_thai.png", width: 80%),
  caption: [สี่เสาหลักของ OOP ในบริบทของ AI],
)

= วิทยาการข้อมูลและการเรียนรู้ของเครื่อง (Data Science & ML)
การจัดการข้อมูลด้วย NumPy และ Pandas เป็นขั้นตอนแรกก่อนการสร้างโมเดล

== Machine Learning Workflow
กระบวนการทำงานเริ่มต้นตั้งแต่การรวบรวมข้อมูลไปจนถึงการประเมินผลโมเดล

#figure(
  image("/home/ubuntu/infographic_ml_workflow_thai.png", width: 80%),
  caption: [ขั้นตอนการทำงานของ Machine Learning],
)

= การเรียนรู้เชิงลึกและการปรับใช้ (Deep Learning & Deployment)
การใช้ PyTorch สำหรับการสร้าง Neural Networks และการนำโมเดลไปใช้งานจริงผ่าน FastAPI และ Docker

#figure(
  image("/home/ubuntu/infographic_neural_networks_thai.png", width: 80%),
  caption: [โครงสร้างของ Neural Networks],
)

#figure(
  image("/home/ubuntu/infographic_ai_deployment_thai.png", width: 80%),
  caption: [กลยุทธ์การ Deployment สำหรับ AI],
)

= สรุป (Conclusion)
หลักสูตรนี้มุ่งหวังให้ผู้เรียนสามารถนำความรู้ไปต่อยอดในการสร้างนวัตกรรม AI ที่มีประสิทธิภาพและได้มาตรฐานวิชาการ
