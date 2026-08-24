# งานคงค้าง: 3D Model Controls

## งานคงค้าง: ชุดไฟล์ส่งมอบทั้งหมด

- [x] ตรวจสอบรายการไฟล์เว็บไซต์ โค้ด Python เอกสารแผนการสอน และเอกสารประกอบ
- [x] สร้างไฟล์ ZIP ที่รวม source code และสื่อการสอน โดยตัด dependency/cache ออก
- [x] ตรวจสอบเนื้อหาใน ZIP และส่งมอบชุดดาวน์โหลด

## งานคงค้าง: STS Spatial–Energy Linecut

- [x] กำหนด defect/interface linecut model และข้อจำกัดของ LDOS proxy
- [x] เพิ่ม linecut control, spatial–energy heatmap และ clickable position probe
- [x] เชื่อมตำแหน่ง probe กับ local dI/dV spectrum และ readout เชิงฟิสิกส์
- [x] ตรวจ TypeScript ปฏิสัมพันธ์ และ responsive layout ของ STS linecut
- [x] บันทึก checkpoint และส่งมอบ STS linecut mapping

## งานคงค้าง: STM/STS Virtual Workbench

- [x] กำหนดแบบจำลอง tunnelling current และ LDOS เชิงการสอน พร้อมข้อจำกัด
- [x] สร้าง STM/STS workbench แบบโต้ตอบสำหรับ bias, tip–sample distance และ temperature
- [x] เพิ่ม atomic-scale topography, I–z trace และ dI/dV spectrum พร้อม readout/evidence prompts
- [x] เชื่อมเส้นทางนำทางจากหน้า Nano Materials ไปยัง STM/STS Lab
- [x] ตรวจ TypeScript ปฏิสัมพันธ์ และ responsive layout ของโมดูล STM/STS
- [x] บันทึก checkpoint และส่งมอบโมดูล STM/STS

- [x] เพิ่ม state และ event handlers สำหรับ drag rotation, wheel zoom และ pinch zoom
- [x] เชื่อม transform ของมุมมองเข้ากับ sphere, cube และ cylinder บน specimen stage
- [x] เพิ่มปุ่มรีเซ็ตมุมมองและคำแนะนำการควบคุมที่เข้าถึงได้
- [x] ทดสอบการควบคุมบนเดสก์ท็อปและมือถือ พร้อมตรวจการคอมไพล์
- [x] บันทึก checkpoint และส่งมอบเวอร์ชันที่อัปเดต

## งานคงค้าง: Standard View Presets

- [x] กำหนดค่า yaw, pitch และ zoom สำหรับ Top, Front และ Isometric views
- [x] เพิ่มปุ่ม preset view พร้อมสถานะแอ็กทีฟใน stage toolbar
- [x] ตรวจสอบ responsive layout และ TypeScript หลังเพิ่มตัวควบคุม
- [x] บันทึก checkpoint และส่งมอบเวอร์ชันที่อัปเดต

## งานคงค้าง: Nano Materials Virtual Laboratory

- [x] จัดทำ taxonomy ของเครื่องมือสร้างและวิเคราะห์วัสดุนาโน พร้อมระดับการจำลอง
- [x] ออกแบบเครื่องมือหลัก AFM, MFM, SEM, TEM และ XRD ให้มีตัวควบคุม ผลลัพธ์ และคำถามการเรียนรู้
- [x] สร้าง instrument hub และเส้นทางเข้าโมดูลการทดลองในเว็บไซต์
- [x] เพิ่มต้นแบบ interactive สำหรับเครื่องมือหลักและ catalog สำหรับเครื่องมือเสริม
- [x] ตรวจการคอมไพล์ ความสอดคล้องเชิงการสอน และ responsive layout
- [x] บันทึก checkpoint และส่งมอบเวอร์ชันที่อัปเดต

## งานคงค้าง: Interactive Spectrum Fitting

- [x] กำหนดช่วงสเปกตรัม สัญญาณเป้าหมาย และพารามิเตอร์ fit สำหรับ Raman, XPS และ UV-Vis
- [x] เพิ่มเครื่องมือและ workbench spectrum fitting แบบโต้ตอบใน Nano Materials Lab
- [x] เพิ่มกราฟ measured/fitted/component และ readout ค่าพารามิเตอร์เชิงการสอน
- [x] ตรวจการคอมไพล์ การแสดงผลบนเดสก์ท็อป/มือถือ และปฏิสัมพันธ์ของ sliders
- [x] บันทึก checkpoint และส่งมอบเวอร์ชันที่อัปเดต

## งานคงค้าง: Line Shape Selection

- [x] กำหนด Gaussian, Lorentzian และ pseudo-Voigt profiles สำหรับแบบจำลองเชิงการสอน
- [x] เพิ่มตัวเลือก line shape และคำอธิบายของรูปแบบเส้นโค้งใน Spectrum Fitting panel
- [x] เชื่อม line shape กับ fitted envelope, selected component และ fit match score
- [x] ตรวจการคอมไพล์และการแสดงผลบนเดสก์ท็อป/มือถือ
- [x] บันทึก checkpoint และส่งมอบเวอร์ชันที่อัปเดต

## งานคงค้าง: Residual Plot

- [x] กำหนด residual model, zero reference และตัวชี้วัดสรุปสำหรับสเปกตรัมจำลอง
- [x] เพิ่มกราฟ residual ใต้สเปกตรัมหลักและเชื่อมกับ line shape/fit parameters
- [x] เพิ่ม readout ค่า RMSE และ largest residual เพื่อใช้ตรวจคุณภาพ fit
- [x] ตรวจการคอมไพล์ ปฏิสัมพันธ์ และ responsive layout ของ residual panel
- [x] บันทึก checkpoint และส่งมอบเวอร์ชันที่อัปเดต

## งานคงค้าง: Modern Nanotechnology Content Update

- [x] รวบรวมแหล่งอ้างอิงร่วมสมัยจากหน่วยงานวิจัย มาตรฐาน และวารสารวิชาการ
- [x] คัดเลือกหัวข้ออัปเดตสำหรับเนื้อหารายวิชาและ Nano Materials Virtual Lab
- [x] จัดทำ roadmap สำหรับนำหัวข้อใหม่ไปใช้ในบทเรียนและโมดูลจำลอง

## งานคงค้าง: 2D Materials & Quantum Materials Virtual Lab

- [x] ตรวจสอบแบบจำลองขั้นต่ำสำหรับ layer-dependent gap, strain, gate field, exciton และ transport proxy
- [x] ออกแบบหน้าโมดูล 2D/quantum materials พร้อมตัวควบคุมและผลลัพธ์การเรียนรู้
- [x] เตรียมสินทรัพย์ภาพและสร้าง interactive plots สำหรับ band structure กับ optical response
- [x] เชื่อม route จาก Nano Materials Lab และทดสอบการคำนวณ/การแสดงผลข้ามอุปกรณ์
- [x] บันทึก checkpoint และส่งมอบเวอร์ชันที่อัปเดต

## งานคงค้าง: Strain-dependent PL & Raman

- [x] ตรวจสอบแนวโน้ม strain-dependent excitonic PL และ Raman-mode shift สำหรับแบบจำลองเชิงการสอน
- [x] เพิ่มกราฟ PL emission และ Raman response ที่เชื่อมกับ strain control เดิม
- [x] เพิ่ม reference markers, peak-shift readout และคำถามเชิงหลักฐานสำหรับนักศึกษา
- [x] ตรวจการคอมไพล์ ปฏิสัมพันธ์ และ responsive layout ของกราฟใหม่
- [x] บันทึก checkpoint และส่งมอบเวอร์ชันที่อัปเดต

## งานคงค้าง: 2D PL & Raman Mapping

- [x] กำหนด strain field เชิงการสอนและความสัมพันธ์กับ PL/Raman map
- [x] เพิ่ม heatmap ที่สลับแสดง strain, PL shift และ Raman shift ได้
- [x] เพิ่มจุด probe แบบคลิกได้และ readout สเปกตรัมเฉพาะตำแหน่ง
- [x] ตรวจการคอมไพล์ ปฏิสัมพันธ์ และ responsive layout ของ mapping workbench
- [x] บันทึก checkpoint และส่งมอบเวอร์ชันที่อัปเดต
