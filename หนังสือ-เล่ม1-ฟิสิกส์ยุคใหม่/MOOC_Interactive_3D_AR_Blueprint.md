# RBRU MOOC: ฟิสิกส์ยุคใหม่

## เป้าหมายการออกแบบ

เอกสารนี้เป็นโครงสร้างกลางสำหรับแปลงเนื้อหาฟิสิกส์ยุคใหม่ให้เป็นบทเรียนออนไลน์แบบ interactive web, 3D WebXR และ AR/MediaPipe โดยแบ่งทุกบทเป็นแนวคิดหลัก กิจกรรมจำลอง การแสดงผล 3D และหลักฐานการเรียนรู้

## สถาปัตยกรรมบทเรียนมาตรฐาน

ทุกบทใช้ลำดับเดียวกัน:

1. **Concept**: เนื้อหาอ่านสั้น สมการ ตัวอย่าง และคำศัพท์
2. **Explore**: ตัวแปรควบคุมแบบ real-time พร้อมกราฟและค่าที่วัดได้
3. **Build**: โมเดล 3D หรือ AR ที่ผู้เรียนหมุน ขยาย และวางในพื้นที่จริง
4. **Instrument**: MediaPipe gesture เป็นเครื่องมือควบคุม เช่น pinch, drag, rotate และสองมือปรับพารามิเตอร์
5. **Check**: คำถามทำนายผล แบบฝึกคำนวณ และ reflection
6. **Evidence**: บันทึกค่าการทดลอง กราฟ ภาพหน้าจอ และผลการทดลองซ้ำ

## บทที่ 1 จุดกำเนิดของทฤษฎีควอนตัม

### 1.1 ข้อจำกัดของฟิสิกส์ดั้งเดิม
- แนวคิด: black-body radiation, photoelectric effect, atomic spectra
- Interactive web: เปรียบเทียบคำทำนาย classical กับข้อมูลทดลอง
- 3D/AR: ห้องทดลองจำลองและแหล่งกำเนิดแสง
- MediaPipe: pinch ปรับความเข้มแสง, swipe เปลี่ยนความถี่

### 1.2 การแผ่รังสีของวัตถุดำและสมมติฐานของพลังค์
- ตัวแปร: อุณหภูมิ ความถี่ ความยาวคลื่น และค่าคงตัวของพลังค์
- Simulator: กราฟ Planck law แบบ real-time และจุดยอด Wien
- Evidence: ผู้เรียนบันทึกอุณหภูมิที่ทำให้ยอดกราฟเลื่อน

### 1.3 ปรากฏการณ์โฟโตอิเล็กทริกและโฟตอน
- ตัวแปร: work function, frequency, intensity, stopping potential
- Simulator: แสดงโฟตอนและอิเล็กตรอนที่หลุดจากผิวโลหะ
- AR/MediaPipe: เล็งหรือ pinch เลือกโลหะและปรับความถี่

### 1.4 สเปกตรัมไฮโดรเจนและสูตรริดเบิร์ก
- Simulator: เปลี่ยนระดับพลังงานและสร้างเส้นสเปกตรัม
- 3D: โมเดลการเปลี่ยนระดับพลังงานของอะตอมไฮโดรเจน

## บทที่ 2 ทฤษฎีสัมพัทธภาพพิเศษ

### 2.1 หลักการพื้นฐานของสัมพัทธภาพ
- Simulator: ผู้สังเกตสองกรอบอ้างอิงและนาฬิกาแสง
- Interaction: ลากยานอวกาศและเปรียบเทียบเวลาของผู้สังเกต

### 2.2 การแปลงลอเรนซ์
- Interactive web: แผนภาพ spacetime และเส้น worldline
- MediaPipe: drag เปลี่ยนความเร็ว, pinch ซูม spacetime diagram

### 2.3 การยืดของเวลาและการหดของระยะทาง
- Simulator: twin lab, light clock และ length contraction
- Evidence: เปรียบเทียบค่าคำนวณกับค่าจากภาพจำลอง

### 2.4 สมมูลมวล-พลังงาน
- Simulator: mass-energy converter และกราฟ E = mc^2
- 3D/AR: แสดงพลังงานเทียบกับวัตถุจริงตามสเกล

## บทที่ 3 ทวิภาวะของคลื่นและอนุภาค

### 3.1 สมมติฐานเดอบรอยล์
- Simulator: ปรับโมเมนตัมเพื่อดูความยาวคลื่นเดอบรอยล์
- 3D: คลื่น matter wave รอบอนุภาค

### 3.2 หลักความไม่แน่นอนของไฮเซนเบิร์ก
- Interactive web: trade-off ระหว่างตำแหน่งและโมเมนตัม
- Gesture: สองมือปรับความกว้าง wave packet และดู Fourier transform

## บทที่ 4 กลศาสตร์ควอนตัม

### 4.1 ฟังก์ชันคลื่นและสมการชโรดิงเจอร์
- Simulator: wavefunction, probability density และ measurement
- 3D: surface plot ของฟังก์ชันคลื่น

### 4.2 อนุภาคในกล่องศักย์
- Simulator: เปลี่ยนความกว้างกล่องและ quantum number
- Evidence: คาดการณ์ node ก่อนกดแสดงผล

### 4.3 ฮาร์มอนิกออสซิลเลเตอร์
- Interactive web: energy levels, eigenstates และ classical limit
- MediaPipe: หมุนโมเดลและ scrub ระดับพลังงาน

### 4.4 Quantum tunneling
- Simulator: ปรับ barrier height/width และดู transmission probability
- AR: วาง barrier ในพื้นที่จริงแล้วปรับด้วย pinch

## บทที่ 5 ทฤษฎีอะตอมและสเปกตรัม

### 5.1 แบบจำลองบอร์และซอมเมอร์เฟลด์
- 3D/AR: วงโคจรระดับพลังงานและการเปลี่ยนสถานะ

### 5.2 เลขควอนตัม
- Interactive web: เลือก n, l, m และ spin เพื่อสร้าง orbital
- 3D: orbital viewer แบบหมุนและตัด section ได้

### 5.3 หลักการกีดกันของเพาลีและตารางธาตุ
- Simulator: เติมอิเล็กตรอนลง orbital แบบตรวจคำตอบทันที
- Gesture: drag electron token ด้วยมือ

### 5.4 สเปกตรัมอะตอม
- Simulator: สร้าง emission/absorption spectrum และเทียบธาตุ
- Evidence: ระบุธาตุจากเส้นสเปกตรัมที่ตรวจวัด

## บทที่ 6 ฟิสิกส์นิวเคลียร์

### 6.1 โครงสร้างนิวเคลียส
- 3D/AR: สร้าง nucleus จาก proton/neutron และดู binding energy

### 6.2 การสลายกัมมันตรังสี
- Simulator: half-life, decay chain และ Monte Carlo particles
- Real-time graph: จำนวนอนุภาคกับเวลาและความไม่แน่นอนทางสถิติ

### 6.3 ฟิชชันและฟิวชัน
- Simulator: chain reaction, criticality และพลังงานที่ปลดปล่อย
- AR: วาง reactor model และปรับ control parameter ด้วยท่าทางมือ

### 6.4 การประยุกต์ใช้
- Interactive case studies: พลังงาน การแพทย์ และอุตสาหกรรม
- Check: เลือก isotope และการป้องกันรังสีให้เหมาะกับสถานการณ์

## บทที่ 7 ฟิสิกส์อนุภาคมูลฐาน

### 7.1 Particle Zoo
- 3D: อนุภาคแบบ interactive พร้อม mass, charge และ lifetime

### 7.2 แรงพื้นฐาน
- Simulator: เปรียบเทียบแรงแม่เหล็กไฟฟ้า แรงนิวเคลียร์เข้ม แรงนิวเคลียร์อ่อน และแรงโน้มถ่วง

### 7.3 Standard Model
- 3D/AR: ตาราง Standard Model แบบ spatial cards
- Gesture: pinch เปิดรายละเอียดอนุภาค, rotate หมุนตารางสามมิติ

### 7.4 ควาร์กและเลปตอน
- Interactive builder: ประกอบ hadron และตรวจ charge conservation
- Evidence: อธิบายเหตุผลขององค์ประกอบอนุภาค

## บทที่ 8 ความรู้เบื้องต้นเกี่ยวกับเอกภพวิทยา

### 8.1 การขยายตัวของเอกภพและกฎฮับเบิล
- Simulator: galaxy map, redshift และ Hubble plot
- Gesture: pan แผนที่และ pinch เปลี่ยนสเกลเวลา

### 8.2 Big Bang
- Interactive timeline: วิวัฒนาการเอกภพตามอุณหภูมิและเวลา
- 3D: cosmic expansion visualization

### 8.3 สสารมืดและพลังงานมืด
- Simulator: เปรียบเทียบ universe models และ rotation curve

### 8.4 วิวัฒนาการดาวฤกษ์และกาแล็กซี
- 3D/AR: stellar lifecycle และ galaxy morphology viewer

### 8.5 ตัวอย่างงานวิจัยดาราศาสตร์ฟิสิกส์
- Research dashboard: data card, hypothesis, visualization และ reflection
- Evidence: ผู้เรียนตีความข้อมูลและเขียนข้อจำกัดของแบบจำลอง

## ภาคผนวก ก ค่าคงตัวทางฟิสิกส์

### ก.1 ตารางค่าคงตัวและหน่วย
- Searchable reference พร้อม unit conversion แบบ real-time

### ก.2 เครื่องมือแปลงหน่วย
- Interactive calculator ตรวจ dimensional consistency

## ภาคผนวก ข โครงงาน Modern Physics with Python

### ข.1 Black Body Radiation
- Notebook/web app: ปรับอุณหภูมิและสร้าง Planck curve

### ข.2 Special Relativity Calculations
- Notebook/web app: คำนวณ gamma, time dilation และ length contraction

### ข.3 โครงงานบูรณาการ
- ผู้เรียนเลือก simulator หนึ่งหัวข้อ สร้างกราฟ อธิบาย model และส่งผลการทดลอง

## แม่แบบข้อมูลสำหรับแต่ละ Simulator

```json
{
  "id": "chapter-topic-lab",
  "chapter": 1,
  "topic": "Photoelectric Effect",
  "learningObjectives": [],
  "parameters": [],
  "observables": [],
  "equations": [],
  "visualization": "2d|3d|ar",
  "gestures": ["pinch", "drag", "rotate", "two-hand-scale"],
  "assessment": [],
  "evidence": ["graph", "measurement-log", "reflection"]
}
```

## แผนพัฒนาเทคนิค

### Web interactive
- HTML/CSS/JavaScript modules แยกตามบท
- Canvas/SVG สำหรับกราฟและแผนภาพ
- Web Worker สำหรับ Monte Carlo และการคำนวณที่หนัก

### 3D และ WebXR
- Three.js scene, OrbitControls และ GLTF/PBR assets
- รองรับ desktop, mobile และ WebXR เมื่ออุปกรณ์พร้อม
- มี fallback เป็น 2D สำหรับอุปกรณ์ที่ไม่รองรับ AR

### MediaPipe
- Hand Landmarker สำหรับ pinch, drag และ rotate
- Pose/gesture layer สำหรับการเลือกหรือควบคุมวัตถุในพื้นที่
- แยก gesture adapter ออกจาก physics model เพื่อทดสอบได้โดยไม่ใช้กล้อง

### การวัดผล
- ก่อนเรียน/หลังเรียนแบบ concept inventory
- บันทึก parameter changes และ prediction accuracy
- ตรวจ accessibility, touch interaction, keyboard fallback และ performance
