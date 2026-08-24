# หลักฐานสำหรับ 2D PL/Raman Mapping ใน Virtual Lab

## หลักการที่นำไปใช้

งาน AFM–Raman แบบ hyperspectral แสดงว่าการกดเฉพาะที่บนเยื่อวัสดุ 2 มิติสามารถสร้าง **strain field ที่กระจายไม่สม่ำเสมอในเชิงพื้นที่** และ Raman peak positions สามารถใช้สร้างแผนที่ของบริเวณ strain ได้ [1] งานดังกล่าวชี้ว่าบริเวณที่ Raman G และ 2D modes ลดความถี่สัมพันธ์กับ tensile strain ใน graphene-based membrane [1]

งานทบทวน strain engineering ระบุว่า absorption, reflectance, photoluminescence และ Raman spectroscopy เป็นวิธี optical แบบไม่ทำลายที่ใช้ศึกษาสมบัติเชิงแสงที่ถูกปรับด้วย strain ในวัสดุ 2 มิติได้ [2] อย่างไรก็ตาม Raman features ของวัสดุ 2 มิติไวต่อหลายปัจจัย รวมถึง thickness, substrate, doping, defects, temperature และ strain [3] ดังนั้นแผนที่ PL/Raman เดี่ยวไม่ควรถูกแปลเป็น “แผนที่ strain จริง” โดยปราศจาก calibration และ control measurements

## ขอบเขตของโมดูล

| องค์ประกอบ | การใช้งานในโมดูล | ข้อจำกัดที่สื่อสารกับนักศึกษา |
|---|---|---|
| Gaussian strain field | จำลอง local deformation, wrinkle หรือ nanoindentation บนแผ่น 2 มิติ | ไม่ใช่การคำนวณ elasticity tensor หรือ mechanical boundary condition จริง |
| PL energy map | แสดง local optical-energy shift ที่สัมพันธ์กับ strain proxy | PL ยังเปลี่ยนได้จาก exciton/trion population, doping, defects และ dielectric environment |
| Raman shift map | แสดง local phonon-mode shift ที่สัมพันธ์กับ strain proxy | peak position/linewidth/intensity ยังขึ้นกับ temperature, laser energy, thickness และ doping |
| Click probe | เลือกพิกัดเพื่ออ่าน local strain/PL/Raman value และ plot spectrum เชิงแนวคิด | ค่า local spectrum เป็น teaching model ไม่ใช่ hyperspectral fitting ของข้อมูลจริง |

## References

[1]: https://pmc.ncbi.nlm.nih.gov/articles/PMC4921963/ "Visualising the strain distribution in suspended two-dimensional materials under local deformation"
[2]: https://www.nature.com/articles/s41377-020-00421-5 "Strain engineering of 2D semiconductors and graphene: from strain fields to band-structure tuning and photonic applications"
[3]: https://www.nature.com/articles/s41699-020-0140-4 "Application of Raman spectroscopy to probe fundamental properties of two-dimensional materials"
