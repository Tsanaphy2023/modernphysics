## บทที่ 1: ความรู้เบื้องต้นเกี่ยวกับปัญญาประดิษฐ์ (Introduction to AI)

ในบทแรกนี้ เราจะเริ่มต้นการเดินทางเข้าสู่โลกของปัญญาประดิษฐ์ (AI) โดยทำความเข้าใจแนวคิดพื้นฐานที่สำคัญและความสัมพันธ์ระหว่างคำศัพท์ต่างๆ ที่มักได้ยินบ่อยครั้ง เช่น ปัญญาประดิษฐ์ (AI), การเรียนรู้ของเครื่อง (Machine Learning), และการเรียนรู้เชิงลึก (Deep Learning) เพื่อสร้างรากฐานที่มั่นคงก่อนจะลงลึกในรายละเอียดทางเทคนิคต่อไป

### AI, Machine Learning, และ Deep Learning คืออะไร และแตกต่างกันอย่างไร

บ่อยครั้งที่คำว่า AI, Machine Learning (ML), และ Deep Learning (DL) ถูกใช้สลับกันไปมา แต่ในความเป็นจริงแล้ว ทั้งสามคำนี้มีความหมายและขอบเขตที่แตกต่างกัน โดยมีความสัมพันธ์เป็นลำดับชั้นซ้อนกันอยู่

> **ปัญญาประดิษฐ์ (Artificial Intelligence - AI)** เป็นศาสตร์และวิศวกรรมในการสร้างเครื่องจักรที่มีความฉลาด โดยเฉพาะอย่างยิ่งโปรแกรมคอมพิวเตอร์ที่ชาญฉลาด [1] AI เป็นแนวคิดที่กว้างที่สุด ครอบคลุมเทคนิคใดๆ ก็ตามที่ทำให้คอมพิวเตอร์สามารถเลียนแบบพฤติกรรมและความสามารถของมนุษย์ได้ เช่น การแก้ปัญหา การเรียนรู้ การวางแผน การเข้าใจภาษา และการรับรู้

> **การเรียนรู้ของเครื่อง (Machine Learning - ML)** เป็นส่วนหนึ่ง (subset) ของ AI ที่เน้นการพัฒนาอัลกอริทึมที่ช่วยให้คอมพิวเตอร์สามารถเรียนรู้จากข้อมูลได้ด้วยตนเองโดยไม่ต้องถูกโปรแกรมไว้อย่างชัดเจน [2] แทนที่จะเขียนกฎเกณฑ์ตายตัว ML จะใช้วิธีการทางสถิติเพื่อค้นหารูปแบบ (patterns) ที่ซ่อนอยู่ในข้อมูล และใช้รูปแบบเหล่านั้นในการตัดสินใจหรือคาดการณ์อนาคต

> **การเรียนรู้เชิงลึก (Deep Learning - DL)** เป็นส่วนย่อย (subfield) ของ ML ที่ใช้อัลกอริทึมซึ่งได้รับแรงบันดาลใจจากโครงสร้างและการทำงานของสมองมนุษย์ที่เรียกว่า **โครงข่ายประสาทเทียม (Artificial Neural Networks)** โดยเฉพาะโครงข่ายที่มีหลายชั้น (deep neural networks) [3] DL มีความสามารถโดดเด่นในการเรียนรู้จากข้อมูลที่ไม่มีโครงสร้าง (unstructured data) จำนวนมหาศาล เช่น รูปภาพ วิดีโอ และข้อความ

ภาพด้านล่างนี้แสดงให้เห็นถึงความสัมพันธ์เชิงลำดับชั้นระหว่าง AI, ML, และ DL ได้อย่างชัดเจน

![ความสัมพันธ์ระหว่าง AI, ML, และ DL](https://private-us-east-1.manuscdn.com/sessionFile/OO4QhUUsaoBTGAbGU9i0j2/sandbox/pRb06yRMC7k7XW9CBSc5bm-images_1760366739295_na1fn_L2hvbWUvdWJ1bnR1L2RpYWdyYW1zL2FpX21sX2RsX3JlbGF0aW9uc2hpcA.png?Policy=eyJTdGF0ZW1lbnQiOlt7IlJlc291cmNlIjoiaHR0cHM6Ly9wcml2YXRlLXVzLWVhc3QtMS5tYW51c2Nkbi5jb20vc2Vzc2lvbkZpbGUvT080UWhVVXNhb0JUR0FiR1U5aTBqMi9zYW5kYm94L3BSYjA2eVJNQzdrN1hXOUNCU2M1Ym0taW1hZ2VzXzE3NjAzNjY3MzkyOTVfbmExZm5fTDJodmJXVXZkV0oxYm5SMUwyUnBZV2R5WVcxekwyRnBYMjFzWDJSc1gzSmxiR0YwYVc5dWMyaHBjQS5wbmciLCJDb25kaXRpb24iOnsiRGF0ZUxlc3NUaGFuIjp7IkFXUzpFcG9jaFRpbWUiOjE3OTg3NjE2MDB9fX1dfQ__&Key-Pair-Id=K2HSFNDJXOU9YS&Signature=mB-z6ulKihGgA2JkHT5nGmeDZ-LM5Y5mXQ6h6WWfqnIgtl3EdsT363IwtpoI7RihIS3qHeZmHVKcJ2B5MniIpkoZtGkra3NLGR1jR7~4vIJis7st~vmTzVQ8d4UnwrgpgQmxB1SBHRTGgJVuKwdB1F6qJ5MMj2SRjsd0fxYGzR0lii5EgwvTAJkricR6FMBdBI95L-t3z0G9S8B5di4uDRo9-C4ny4wb5ZOHBne62Wg4juYSrgOdPO2YnPvlh~k30t-wlD~Wn3uCq6s0QWzDQEKg0XgS6tJC-T8iEonfUFlwzwmA5sQunv7ET1T25mnpwwnNAGVgTh5DSn4FwWZrdQ__)
*ภาพที่ 1.1: แผนภาพแสดงความสัมพันธ์ระหว่าง Artificial Intelligence (AI), Machine Learning (ML), และ Deep Learning (DL)*

| คุณสมบัติ | Artificial Intelligence (AI) | Machine Learning (ML) | Deep Learning (DL) |
| :--- | :--- | :--- | :--- |
| **ขอบเขต** | แนวคิดที่กว้างที่สุดในการสร้างเครื่องจักรที่ฉลาด | Subset ของ AI ที่เรียนรู้จากข้อมูล | Subset ของ ML ที่ใช้โครงข่ายประสาทเทียมหลายชั้น |
| **วิธีการ** | ใช้ตรรกะ, กฎเกณฑ์, และการเรียนรู้ | ใช้อัลกอริทึมทางสถิติเพื่อค้นหารูปแบบ | ใช้โครงข่ายประสาทเทียม (Neural Networks) ที่ซับซ้อน |
| **การดึงคุณลักษณะ (Feature Extraction)** | ส่วนใหญ่มนุษย์เป็นผู้กำหนด | มนุษย์เป็นผู้กำหนดและปรับปรุง | เรียนรู้และดึงคุณลักษณะจากข้อมูลได้เองโดยอัตโนมัติ |
| **ปริมาณข้อมูล** | ต้องการข้อมูลหลากหลายรูปแบบ | ต้องการข้อมูลที่มีโครงสร้างจำนวนมากพอสมควร | ต้องการข้อมูลจำนวนมหาศาล (Big Data) เพื่อประสิทธิภาพสูงสุด |
| **ตัวอย่าง** | ระบบผู้เชี่ยวชาญ, หุ่นยนต์สนทนา (Chatbot) | การพยากรณ์ราคาหุ้น, การแนะนำสินค้า | รถยนต์ไร้คนขับ, การแปลภาษา, การวิเคราะห์ภาพทางการแพทย์ |

*ตารางที่ 1.1: ตารางเปรียบเทียบความแตกต่างระหว่าง AI, ML, และ DL*

### ประเภทของการเรียนรู้ของเครื่อง (Types of Machine Learning)

การเรียนรู้ของเครื่องสามารถแบ่งออกเป็น 3 ประเภทหลักตามลักษณะของข้อมูลและการเรียนรู้ของอัลกอริทึม ได้แก่

1.  **การเรียนรู้แบบมีผู้สอน (Supervised Learning)**
    เป็นประเภทที่พบได้บ่อยที่สุด อัลกอริทึมจะเรียนรู้จากชุดข้อมูลที่ผ่านการ "ติดฉลาก" (labeled data) มาแล้ว ซึ่งหมายความว่าข้อมูลแต่ละชุดจะมีคำตอบที่ถูกต้องกำกับอยู่ เป้าหมายคือการเรียนรู้ฟังก์ชันที่สามารถจับคู่ข้อมูลนำเข้า (input) ไปยังผลลัพธ์ (output) ที่ถูกต้องได้
    *   **ตัวอย่าง:** การจำแนกอีเมลว่าเป็นสแปมหรือไม่ (Spam/Not Spam), การทำนายราคาบ้านจากข้อมูลคุณสมบัติต่างๆ ของบ้าน

2.  **การเรียนรู้แบบไม่มีผู้สอน (Unsupervised Learning)**
    ในทางตรงกันข้าม อัลกอริทึมจะเรียนรู้จากชุดข้อมูลที่ "ไม่มีฉลาก" (unlabeled data) เป้าหมายคือการค้นหาโครงสร้างหรือรูปแบบที่ซ่อนอยู่ในข้อมูลด้วยตัวเอง โดยไม่มีคำตอบที่ถูกต้องชี้นำ
    *   **ตัวอย่าง:** การจัดกลุ่มลูกค้าตามพฤติกรรมการซื้อ (Customer Segmentation), การลดมิติของข้อมูลเพื่อการแสดงผล

3.  **การเรียนรู้แบบเสริมแรง (Reinforcement Learning)**
    เป็นรูปแบบการเรียนรู้ที่แตกต่างออกไป โดยมี "เอเจนต์" (agent) ที่เรียนรู้ที่จะตัดสินใจในสภาพแวดล้อม (environment) เพื่อให้ได้รางวัล (reward) สูงสุด เอเจนต์จะเรียนรู้ผ่านการลองผิดลองถูก (trial and error) โดยจะได้รับการตอบกลับในรูปแบบของรางวัล (เมื่อทำได้ดี) หรือการลงโทษ (เมื่อทำได้ไม่ดี)
    *   **ตัวอย่าง:** การฝึก AI ให้เล่นเกมคอมพิวเตอร์, การควบคุมหุ่นยนต์ให้เดิน, การจัดการระบบการจราจร

![ประเภทของ Machine Learning](https://private-us-east-1.manuscdn.com/sessionFile/OO4QhUUsaoBTGAbGU9i0j2/sandbox/pRb06yRMC7k7XW9CBSc5bm-images_1760366739296_na1fn_L2hvbWUvdWJ1bnR1L2RpYWdyYW1zL21sX3R5cGVz.png?Policy=eyJTdGF0ZW1lbnQiOlt7IlJlc291cmNlIjoiaHR0cHM6Ly9wcml2YXRlLXVzLWVhc3QtMS5tYW51c2Nkbi5jb20vc2Vzc2lvbkZpbGUvT080UWhVVXNhb0JUR0FiR1U5aTBqMi9zYW5kYm94L3BSYjA2eVJNQzdrN1hXOUNCU2M1Ym0taW1hZ2VzXzE3NjAzNjY3MzkyOTZfbmExZm5fTDJodmJXVXZkV0oxYm5SMUwyUnBZV2R5WVcxekwyMXNYM1I1Y0dWei5wbmciLCJDb25kaXRpb24iOnsiRGF0ZUxlc3NUaGFuIjp7IkFXUzpFcG9jaFRpbWUiOjE3OTg3NjE2MDB9fX1dfQ__&Key-Pair-Id=K2HSFNDJXOU9YS&Signature=Y267Zg7aH1PsmRK~YlUULCEnXcHsZrkBJqlHv4QZ4-UsHGyAg6aJHEUd3nQzMmr00jp2Ercl2b0xjsNENRkICcGeIFd47u0578b7rU1jfWmYUwooQS8U3AKw1P~CM3XOQqsgrHuck5jg4NK0kzqwaM2fjO6TDF73yVlMJGL~RL1h2CPU9qh4QvXnjl~u5r6YS~YAVyXxXaWX5KUVCNtbMtwNnlrfJdNww5yED5r6eNidiLE9InzGYmmx-c3CVNSyr9rgR5cVOLU6-NuZDsU2QkjX2B-AiAy~V5qm-yvXagrsx2AWqF23ArLdZKAK4CIpQpIkjyenC9WvJeo5LdOrCw__)
*ภาพที่ 1.2: แผนภาพแสดงประเภทหลักของการเรียนรู้ของเครื่อง*

### ตัวอย่างการประยุกต์ใช้ AI ในโลกแห่งความเป็นจริง

ปัญญาประดิษฐ์ได้แทรกซึมเข้ามาเป็นส่วนหนึ่งของชีวิตประจำวันและภาคธุรกิจต่างๆ อย่างกว้างขวาง ตัวอย่างที่เห็นได้ชัดเจนมีดังนี้

*   **ในชีวิตประจำวัน:**
    *   **ระบบแนะนำ (Recommendation Systems):** Netflix แนะนำภาพยนตร์ที่คุณน่าจะชอบ, Spotify สร้างเพลย์ลิสต์เพลงใหม่ให้คุณ, Amazon แนะนำสินค้าที่เกี่ยวข้องกับที่คุณเคยซื้อ
    *   **ผู้ช่วยเสมือน (Virtual Assistants):** Siri, Google Assistant, และ Alexa ที่สามารถตอบคำถาม, ตั้งนาฬิกาปลุก, หรือควบคุมอุปกรณ์สมาร์ทโฮมผ่านคำสั่งเสียง
    *   **การรู้จำใบหน้า (Facial Recognition):** การปลดล็อกสมาร์ทโฟน, การแท็กเพื่อนในรูปภาพบนโซเชียลมีเดีย

*   **ในภาคธุรกิจ:**
    *   **การเงินการธนาคาร:** การตรวจจับการฉ้อโกงบัตรเครดิต (Fraud Detection), การประเมินความเสี่ยงสินเชื่อ, การซื้อขายหุ้นด้วยอัลกอริทึม (Algorithmic Trading)
    *   **การแพทย์:** การวิเคราะห์ภาพถ่ายทางการแพทย์ (เช่น X-ray, MRI) เพื่อช่วยวินิจฉัยโรค, การค้นพบยาใหม่, การพัฒนาระบบผู้ช่วยแพทย์ส่วนบุคคล
    *   **ยานยนต์:** ระบบรถยนต์ไร้คนขับ (Self-Driving Cars) ที่ใช้ AI ในการรับรู้สภาพแวดล้อมและตัดสินใจเส้นทาง
    *   **การค้าปลีก:** การจัดการสินค้าคงคลัง, การวิเคราะห์พฤติกรรมลูกค้าในร้านค้า, การสร้างประสบการณ์การช็อปปิ้งเฉพาะบุคคล

ในบทต่อไป เราจะเตรียมความพร้อมเครื่องมือที่จำเป็นสำหรับการลงมือปฏิบัติจริงกับ AI และ Machine Learning ด้วยภาษาไพทอน ซึ่งเป็นภาษาที่ได้รับความนิยมสูงสุดในวงการนี้

### อ้างอิง
[1] John McCarthy, "What is Artificial Intelligence?" - http://jmc.stanford.edu/articles/whatisai/whatisai.pdf

[2] Tom M. Mitchell, "Machine Learning" (1997)

[3] Ian Goodfellow, Yoshua Bengio, and Aaron Courville, "Deep Learning" (2016)

