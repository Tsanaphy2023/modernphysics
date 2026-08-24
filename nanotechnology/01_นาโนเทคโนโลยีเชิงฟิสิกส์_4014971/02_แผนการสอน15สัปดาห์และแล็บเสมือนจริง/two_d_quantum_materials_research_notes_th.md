# บันทึกการค้นคว้า: 2D Materials & Quantum Materials Virtual Lab

| ประเด็น | หลักฐานที่ใช้กำหนดแบบจำลองเชิงการสอน | แหล่งอ้างอิง |
|---|---|---|
| Layer / strain / field tuning | งานทบทวนปี 2024 อธิบายว่าช่องว่างพลังงานของวัสดุ 2 มิติขึ้นกับจำนวนชั้น strain, field, composition และ heterostructure โดยต้องระวังว่าแนวโน้มจริงขึ้นกับชนิดวัสดุและ substrate | [Boland et al., 2024](https://pmc.ncbi.nlm.nih.gov/articles/PMC11487627/) |
| Straintronics | การยืด/อัดเปลี่ยน band structure, optical response และสมบัติอิเล็กทรอนิกส์ จึงเหมาะเป็น control ที่ผู้เรียนปรับได้ในแบบจำลอง | [Boland et al., 2024](https://pmc.ncbi.nlm.nih.gov/articles/PMC11487627/) |
| Exciton transport | งานทดลองใน WSe2 แสดงว่า strain engineering สามารถสร้าง potential channel และทำให้ exciton transport มีความไม่สมมาตรตามทิศทาง จึงเหมาะเป็น transport proxy ที่เชื่อม strain กับ exciton response | [Dirnberger et al., 2021](https://pmc.ncbi.nlm.nih.gov/articles/PMC8555901/) |
| Metrology | NIST ชี้ว่ามาตรวิทยาของวัสดุ 2 มิติเป็นช่องว่างสำคัญสำหรับ 2D materials ที่เข้ากันได้กับ CMOS; ดังนั้น Virtual Lab ต้องสื่อความต่างระหว่าง conceptual model กับการยืนยันด้วยการวัดจริง | [NIST Metrology for 2D Materials](https://tsapps.nist.gov/publication/get_pdf.cfm?pub_id=956896) |

## ขอบเขตแบบจำลองที่จะใช้

1. **ไม่อ้างว่าเป็น DFT หรือ tight-binding fit ของวัสดุจริง** แต่ใช้ semi-empirical teaching model เพื่อสื่อ causal relationships
2. เลือก material presets: graphene-like (gapless), MoS2-like (direct-gap TMD), WSe2-like (exciton/strain) และ bilayer graphene-like (gate-tunable gap)
3. Controls: จำนวนชั้น, biaxial strain, gate field, temperature และ dielectric screening
4. Outputs: conceptual band-edge diagram, band gap, optical/exciton energy, exciton binding proxy, mobility/transport proxy และ measurement caveat
5. ทุก readout ต้องระบุหน่วย สถานะของ preset และ caveat ว่า substrate, defects, doping, stacking, twist angle และ measurement geometry อาจเปลี่ยนแนวโน้มจริง
