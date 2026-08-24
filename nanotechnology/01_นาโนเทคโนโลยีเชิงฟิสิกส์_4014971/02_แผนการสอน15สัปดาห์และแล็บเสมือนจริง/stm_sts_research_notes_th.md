# บันทึกหลักฐานสำหรับ STM/STS Virtual Workbench

## หลักการที่จะใช้ในแบบจำลองเชิงการสอน

การทำ topography แบบ constant-current ปรับตำแหน่งปลายหัววัดในแกน z ผ่าน feedback loop เพื่อคงค่า tunnelling current ที่ setpoint และ bias ที่กำหนด ดังนั้นภาพ “ความสูง” จึงเป็น contrast ที่ขึ้นกับทั้ง geometry และ electronic structure ไม่ใช่การวัดความสูงเชิงเรขาคณิตโดยตรง [1]

ในกรณีที่ tip DOS และ matrix element เปลี่ยนกับพลังงานน้อย กระแส tunnelling ที่ bias หนึ่ง ๆ สัมพันธ์กับอินทิกรัลของ sample DOS ในหน้าต่างพลังงานที่ bias เปิดไว้ [2] ส่วน dI/dV ที่ตำแหน่งหนึ่งใช้เป็น proxy ของ LDOS ภายใต้ข้อสมมติฐานที่ระบุอย่างชัดเจน [1]

## ขอบเขตของโมดูล

โมดูลจะใช้แบบจำลอง semi-empirical เพื่อแสดงผลของ bias, tip–sample separation, temperature และ local site ต่อ (1) atomic-contrast topography (2) exponential I–z trace และ (3) dI/dV spectrum. แบบจำลองจะไม่อ้างว่าแยก tip DOS, tunnelling matrix element, barrier shape, lock-in broadening, disorder, many-body effects หรือ calibration ของเครื่องมือจริงได้ครบถ้วน

## STS spatial–energy linecut

STS linecut ใช้ชุด dI/dV spectra ตามตำแหน่งที่เรียงตลอดแนว A→B เพื่อสร้างภาพของ local density of states ใน space–energy dataset ซึ่งสอดคล้องกับนิยาม linecut ของการวัด STM/STS [1] แบบจำลองนี้จึงกำหนดให้ผู้เรียนเลือกได้สองทาง: defect crossing ใช้ Gaussian localized-state envelope ใกล้ตำแหน่ง defect; interface crossing ใช้ smooth interpolation ระหว่าง metal-like และ gapped LDOS พร้อม interface resonance เชิงสาธิต

แผนที่และสเปกตรัมที่แสดงเป็น **LDOS proxy** เท่านั้น ไม่ได้รวม tip DOS, setpoint normalization, lock-in modulation, drift, disorder, many-body effects หรือการ deconvolution ของ tip/sample จึงห้ามใช้ตีความเป็น band alignment, quasiparticle gap หรือ defect energy ของตัวอย่างจริงโดยตรง

หน้า `/stm-sts` แสดง linecut protocol, path selector, position slider, spatial–energy map, local dI/dV spectrum และ model note ครบตาม workflow แล้ว ขั้นตอนตรวจสอบถัดไปคือยืนยันการเปลี่ยนทั้ง map และ readout เมื่อสลับ path/ตำแหน่ง probe

ระหว่างการทดสอบผ่านเบราว์เซอร์ พบว่า path selector ปรากฏและ map แสดงผลได้ แต่การเลือก `Interface crossing` ยังไม่สะท้อนใน active readout จึงต้องตรวจและแก้ state transition ก่อนส่งมอบ

ตรวจสอบเพิ่มเติมแล้วพบว่า React อัปเดต state หลัง event loop ตามปกติ: `Interface crossing` เปลี่ยน active readout เป็น `ACTIVE / INTERFACE` ได้ และการเลือก cell บน map เปลี่ยน local probe เป็น `x 85% · interface axis` จึงยืนยันการเชื่อม path → map → local readout แล้ว

## ผลตรวจสอบเบื้องต้น

หน้า `/stm-sts` แสดง control stack, stage, junction readout และ analysis cards ครบถ้วนแล้ว และการสลับจาก MoS₂-like ไปยัง Defect-like เปลี่ยน sample tag กับ barrier proxy ตาม preset โดยยังคงแสดงว่าค่าทั้งหมดเป็น conceptual proxy

การคลิกตำแหน่ง defect ใน atomic contrast map อัปเดต local probe เป็น `localized defect` และเปลี่ยน junction readout พร้อมกัน ได้แก่ tunnelling current, dI/dV proxy, LDOS at eV และ apparent height จึงยืนยันว่าการเชื่อมโยง map → local response ทำงานแล้ว

## อ้างอิง

[1] Harvard Hoffman Lab, “STM Measurement Types.” https://hoffman.physics.harvard.edu/research/STMmeas.php

[2] Boston College Zeljkovic Lab, “Scanning Tunneling Microscopy.” https://www.bc.edu/bc-web/schools/morrissey/departments/physics/labs/Zeljkovic-Lab/research/facilities.html
