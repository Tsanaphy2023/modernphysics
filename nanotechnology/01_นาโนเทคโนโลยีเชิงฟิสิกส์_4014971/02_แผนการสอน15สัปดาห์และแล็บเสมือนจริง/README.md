# Nanophysics Virtual Lab 01 — Complete Delivery

ชุดนี้รวบรวม source code ของเว็บไซต์ **Nanophysics Virtual Lab 01** และสื่อการสอนภาษาไทยที่สร้างร่วมกันสำหรับรายวิชานาโนฟิสิกส์ระดับมหาวิทยาลัย

## โครงสร้างชุดไฟล์

| โฟลเดอร์/ไฟล์ | เนื้อหา |
|---|---|
| `website_source/` | React + TypeScript source code ของเว็บไซต์ Virtual Lab รวมโมดูล Geometry, Nano Materials, 2D/Quantum Materials, STM/STS และ STS spatial–energy linecut |
| `teaching_materials/` | แผนการสอน 15 สัปดาห์ ชุดโจทย์ โค้ด Python และแผนปฏิบัติการเสมือน |
| `DELIVERY_MANIFEST.txt` | รายการไฟล์ที่บรรจุในชุดดาวน์โหลด |

## การเริ่มเว็บไซต์บนเครื่อง

ต้องติดตั้ง Node.js 22 ขึ้นไปและ pnpm จากนั้นเปิด terminal ในโฟลเดอร์ `website_source/` แล้วรัน

```bash
pnpm install
pnpm dev
```

ตรวจสอบ type safety ได้ด้วย

```bash
pnpm check
```

> โมดูล STM/STS, PL/Raman, 2D mapping และสเปกตรัมทุกส่วนเป็น **conceptual/semi-empirical teaching model** สำหรับฝึกตั้งสมมติฐานและอ่านแนวโน้ม ไม่ใช่ผล DFT หรือข้อมูลที่สอบเทียบจากการทดลองจริง

## เอกสารในชุดการสอน

แผนการสอน ชุดโจทย์ แผนปฏิบัติการ และโค้ด Python อยู่ใน `teaching_materials/` โดยสคริปต์ Python ได้รับการออกแบบให้รันได้ตั้งแต่ต้นจนจบโดยไม่ต้องปรับค่าด้วยมือ
