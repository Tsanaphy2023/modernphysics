# ระบบจัดการทรัพยากรตัวละครและฉากหลัง (Asset Library Management System) สำหรับ CineMatic AI

ระบบ Asset Library Management ภายใน **CineMatic AI** ทำหน้าที่เป็นศูนย์กลางในการจัดเก็บ ค้นหา ควบคุมเวอร์ชัน และซิงโครไนซ์ทรัพยากรดิจิทัล (Digital Assets) ทั้งหมดที่ใช้ในการผลิตภาพยนตร์และซีรีส์ เพื่อให้มั่นใจว่าตัวละคร, ฉาก, อุปกรณ์ประกอบฉาก (Props) และสไตล์ภาพมีความสอดคล้องกันตลอดทั้งเรื่อง (Asset Consistency)

---

## **1. โครงสร้างและการจัดหมวดหมู่ทรัพยากร (Asset Taxonomy)**

ระบบแบ่งทรัพยากรออกเป็น 4 หมวดหมู่หลัก เพื่อให้สอดคล้องกับเวิร์กโฟลว์ของโมดูลต่างๆ:

1.  **Character Assets (ตัวละคร):**
    *   *3D Models:* ไฟล์โมเดลตัวละครในรูปแบบ FBX, USD หรือ Unreal Engine Skeletal Mesh
    *   *Rigging & Control Setups:* โครงสร้างกระดูกที่เชื่อมโยงกับระบบ MediaPipe Retargeting
    *   *Character Bible & Prompts:* ข้อมูลจำเพาะของตัวละคร เช่น สไตล์ภาพ (เช่น Semi-realistic anime, 3D render style, Pixar style), โทนสีเสื้อผ้า และลักษณะเด่น เพื่อรักษาความต่อเนื่องของตัวละครตามมาตรฐานโปรเจกต์
2.  **Environment & Set Assets (ฉากและสภาพแวดล้อม):**
    *   *Virtual Sets:* ฉาก 3 มิติ (เช่น ห้องทดลอง, เมืองไซเบอร์พังก์, ป่าแฟนตาซี)
    *   *HDRI & Lighting Presets:* ค่าแสงและสภาพแวดล้อมจำลอง (เช่น Golden Hour, Midnight Neon)
3.  **Prop Assets (อุปกรณ์ประกอบฉาก):**
    *   วัตถุหรือเครื่องมือที่ตัวละครต้องใช้งาน (เช่น โฮโลแกรมแท็บเล็ต, อุปกรณ์สแกน AR)
4.  **Audio & FX Assets (เสียงและเอฟเฟกต์พิเศษ):**
    *   ไฟล์เสียงพากย์, ดนตรีประกอบ (Soundtrack), และเสียงเอฟเฟกต์ (SFX)

---

## **2. สถาปัตยกรรมระบบหลังบ้าน (Backend Architecture)**

*   **Database (PostgreSQL / TiDB):** จัดเก็บ Metadata ของ Asset ทั้งหมด เช่น ID, ชื่อ, หมวดหมู่, แท็ก, ผู้ออกแบบ, วันที่สร้าง, และสถานะการใช้งาน
*   **Object Storage (S3-compatible Storage):** จัดเก็บไฟล์ขนาดใหญ่ เช่น โมเดล 3D (.fbx, .obj), ไฟล์เท็กซ์เจอร์ (.png, .exr), และไฟล์วิดีโอ
*   **Version Control System (Git LFS / DVC):** ควบคุมเวอร์ชันของไฟล์โมเดล 3 มิติ เพื่อให้ทีมงานสามารถย้อนกลับไปดูเวอร์ชันเก่าของตัวละครหรือฉากได้หากมีการแก้ไข

---

## **3. ฟีเจอร์หลักของ Asset Management Interface**

*   **Smart Search & Tagging:** ค้นหา Asset ได้อย่างรวดเร็วด้วยระบบ AI Tagging ที่วิเคราะห์จากลักษณะของโมเดลหรือบทภาพยนตร์
*   **Consistency Checker:** ระบบตรวจสอบอัตโนมัติว่าตัวละครในฉากปัจจุบันตรงกับ Character Bible หรือไม่ (เช่น ตรวจสอบสีผม เสื้อผ้า และสไตล์ 3D Render)
*   **One-Click Import to UE5:** ปุ่มลัดสำหรับส่ง Asset จากคลังกลางเข้าไปยัง Unreal Engine 5 ทันทีผ่าน Plugin เชื่อมต่อ
