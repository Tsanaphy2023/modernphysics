# บันทึกแบบจำลองเชิงการสอน: Strain-dependent PL และ Raman ในวัสดุ 2 มิติ

## หลักฐานที่ใช้กำหนดขอบเขต

วัสดุสองมิติมีโครงสร้างอิเล็กทรอนิกส์ การสั่นของโครงผลึก และ electron–phonon interaction ที่ไวต่อ strain, substrate, thickness, doping, defect และการเตรียมตัวอย่าง ดังนั้น Raman peak position, linewidth และ intensity รวมทั้ง photoluminescence peak ไม่ควรถูกตีความเป็นตัววัด strain เพียงตัวเดียวโดยตัดปัจจัยอื่นทิ้ง [1] [2]

งานทบทวนเกี่ยวกับ strain engineering ระบุว่า PL และ Raman เป็นวิธีเชิงแสงแบบไม่ทำลายที่ใช้ศึกษาการตอบสนองเชิงแสงของวัสดุ 2 มิติภายใต้ strain ได้ [2] ขณะที่งานทดลองกับ MoS₂ รายงานการเปลี่ยนแปลงของ band gap ที่ตรวจสอบด้วย PL และการเลื่อนของ Raman-active modes ภายใต้ strain [3]

> **ขอบเขตของ Virtual Lab:** ใช้ความสัมพันธ์เชิงคุณภาพ “tensile strain → PL energy และ selected Raman mode shift” เพื่อฝึกการตั้งสมมติฐานและอ่านหลักฐานร่วมกัน ไม่ใช่การทำนายค่าจริงสำหรับวัสดุหรือ geometry ใดโดยเฉพาะ

## แบบจำลองที่จะใช้

| สัญญาณ | ตัวแปรจาก Virtual Lab | ผลลัพธ์ที่แสดง | ข้อจำกัดสำคัญ |
|---|---|---|---|
| PL emission | strain, temperature, layer count, material preset | excitonic peak energy, linewidth proxy, normalized intensity | exciton/trion population, dielectric environment, defect และ carrier density ถูกย่อเป็น proxy |
| Raman | strain, temperature, material preset | peak positions ของ mode 1 และ mode 2, linewidth proxy | coefficient ของ strain ไม่เป็นสากลและขึ้นกับ direction, substrate, doping, number of layers และ laser energy |
| Evidence comparison | PL shift + Raman shift | reference marker ที่ strain = 0 และ current marker | การเลื่อนที่สอดคล้องกันเป็นเพียงหลักฐานสนับสนุน ต้องใช้ calibration/control เพิ่มเติม |

## References

[1]: https://www.nature.com/articles/s41699-020-0140-4 "Application of Raman spectroscopy to probe fundamental properties of two-dimensional materials"
[2]: https://www.nature.com/articles/s41377-020-00421-5 "Strain engineering of 2D semiconductors and graphene: from strain fields to band-structure tuning and photonic applications"
[3]: https://www.nature.com/articles/srep05649 "Lattice strain effects on the optical properties of MoS₂ nanosheets"
