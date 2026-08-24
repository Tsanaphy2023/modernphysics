# Front matter: Cover, Half Title, Title, CIP, Foreword, Preface, TOC, Lists

def get_front_matter():
    return r"""
    <div class="cover-page">
      <div style="font-size: 11pt; color: #38bdf8; font-family: 'JetBrains Mono', monospace; font-weight: 700; letter-spacing: 2px; margin-bottom: 20px;">
        MASTERCLASS TEXTBOOK SERIES 2026
      </div>
      <h1 style="font-size: 32pt; font-weight: 800; color: #ffffff; margin: 0 0 16px 0; line-height: 1.2;">
        นาโนเทคโนโลยีเชิงฟิสิกส์
      </h1>
      <div style="font-size: 18pt; font-weight: 600; color: #94a3b8; margin-bottom: 30px;">
        Nanotechnological Physics: Theory, Computation &amp; Applications
      </div>
      <div style="width: 80px; height: 4px; background: #00f0ff; margin-bottom: 30px;"></div>
      <div style="font-size: 13pt; font-weight: 700; color: #ffffff; margin-bottom: 6px;">
        ผู้ช่วยศาสตราจารย์ ดร.ชีวะ ทัศนา (Asst. Prof. Dr. Chewa Thassana)
      </div>
      <div style="font-size: 10pt; color: #94a3b8;">
        สาขาวิชาฟิสิกส์ คณะวิทยาศาสตร์และเทคโนโลยี มหาวิทยาลัยราชภัฏรำไพพรรณี
      </div>
    </div>

    <!-- PREFACE & OUTLINE -->
    <div class="toc-page">
      <h2 style="color: #0369a1; border-bottom: 2px solid #0284c7; padding-bottom: 8px;">คำนำ (Preface)</h2>
      <p>
        หนังสือตำราวิชาการ <strong>“นาโนเทคโนโลยีเชิงฟิสิกส์ (Nanotechnological Physics)”</strong> เล่มนี้ ได้รับการประพันธ์ขึ้นเพื่อใช้เป็นตำราหลักสำหรับการเรียนการสอนในระดับอุดมศึกษา และเป็นเอกสารอ้างอิงระดับสูงสำหรับนักวิจัย วิศวกร และผู้สนใจวิทยาการด้านนาโนศาสตร์ โดยบูรณาการองค์ความรู้ทางฟิสิกส์บริสุทธิ์ กลศาสตร์ควอนตัม เทอร์โมไดนามิกส์ เคมีพื้นผิว และระเบียบวิธีเชิงคำนวณขั้นสูงเข้าด้วยกันอย่างเป็นระบบ
      </p>
      <p>
        โครงสร้างของตำราครอบคลุมเนื้อหาทั้งสิ้น 8 บทเรียน ตั้งแต่มโนทัศน์พื้นฐานและกฎการปรับสัดส่วน (Chapter 1), ปรากฏการณ์กักขังควอนตัม (Chapter 2), จลนพลศาสตร์การสังเคราะห์ (Chapter 3), การวิเคราะห์ลักษณะเฉพาะและมาตรวิทยานาโน (Chapter 4), วัสดุคาร์บอนและโครงสร้าง 2 มิติ (Chapter 5), การประยุกต์ใช้ในพลังงานและการแพทย์ (Chapter 6), พิษวิทยาและความปลอดภัย (Chapter 7) ไปจนถึงการจำลองทางคอมพิวเตอร์และโครงงานวิจัย (Chapter 8) พร้อมแบบฝึกหัด 3 ระดับและโค้ดตัวอย่างภาษาไพทอน
      </p>
    </div>
    """
