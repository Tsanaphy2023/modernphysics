# บันทึกตรวจสอบผลลัพธ์ exciton absorption spectra

สคริปต์ `quantum_confinement_exciton_spectra.py` รันได้สำเร็จด้วย Python, NumPy และ Matplotlib และสร้างไฟล์ `quantum_confinement_exciton_spectra.png` ขนาด 2160 × 1440 พิกเซล

ผลตรวจสอบสำคัญมีดังนี้

1. กราฟแผงซ้ายบนแสดง exciton absorption peak ที่เลื่อนไปยังพลังงานสูงขึ้นเมื่อรัศมี quantum dot ลดลง ซึ่งสอดคล้องกับแนวโน้ม quantum confinement
2. กราฟแผงขวาบนแสดง exciton series แบบ n = 1–4 และ continuum onset โดย peak n = 1 มี oscillator strength สูงที่สุดตามแบบจำลอง `1/n^3`
3. กราฟแผงซ้ายล่างเปรียบเทียบ monodisperse กับการกระจายขนาดที่มี sigma = 0.20 และ 0.50 nm เพื่อสาธิต inhomogeneous broadening
4. กราฟแผงขวาล่างแสดง 1s exciton energy, continuum onset และ binding energy ในฟังก์ชันของเส้นผ่านศูนย์กลาง
5. มีการปรับฟังก์ชัน ensemble ให้เลือกปิด continuum ได้ในแผง broadening เพื่อไม่ให้ continuum tail กลบการสาธิตผลของ size distribution
6. ผลลัพธ์เป็น pedagogical model ไม่ใช่การคำนวณ many-body absorption spectrum แบบเต็มรูปแบบ จึงควรอภิปรายข้อจำกัด ได้แก่ dielectric mismatch, finite barrier, surface polarization, phonons, disorder, exchange และ atomistic band structure
