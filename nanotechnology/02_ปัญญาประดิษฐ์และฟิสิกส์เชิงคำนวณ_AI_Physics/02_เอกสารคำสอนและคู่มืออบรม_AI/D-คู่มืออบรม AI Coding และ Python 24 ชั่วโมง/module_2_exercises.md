# แบบฝึกหัดเชิงปฏิบัติการ Module 2: Data Structures & Object-Oriented Programming

## Exercise 1: Advanced Collections for Data Preprocessing (defaultdict & Counter)

**โจทย์:**
คุณได้รับชุดข้อมูลการใช้งานฟีเจอร์ในแอปพลิเคชัน AI ซึ่งอยู่ในรูปแบบ List of Tuples: `[(user_id, feature_name)]`

1.  ใช้ `collections.defaultdict` เพื่อจัดกลุ่ม `feature_name` ตาม `user_id`
2.  ใช้ `collections.Counter` เพื่อหา 3 ฟีเจอร์ที่มีการใช้งานมากที่สุดโดยรวม

**Input Data:**
```python
usage_data = [
    (101, 'Image_Recognition'), (102, 'Text_Summarization'), (101, 'Image_Recognition'),
    (103, 'Code_Generation'), (102, 'Text_Summarization'), (101, 'Code_Generation'),
    (104, 'Image_Recognition'), (103, 'Text_Summarization'), (101, 'Image_Recognition'),
    (105, 'Code_Generation'), (104, 'Text_Summarization'), (105, 'Image_Recognition')
]
```

**Expected Output:**
1.  Grouped Data (Dictionary)
2.  Top 3 Features (List of Tuples)

---

## Exercise 2: Object-Oriented Programming (OOP) - Model Configuration

**โจทย์:**
ออกแบบ Class ชื่อ `AIModelConfig` เพื่อจัดการ Hyperparameters ของโมเดล AI โดยใช้หลักการ Encapsulation และ `@property`

1.  กำหนด Private Attribute: `__learning_rate` (ค่าเริ่มต้น 0.001) และ `__epochs` (ค่าเริ่มต้น 10)
2.  สร้าง `@property` (Getter) สำหรับทั้งสอง Attribute
3.  สร้าง `@learning_rate.setter` เพื่อกำหนดเงื่อนไข: `learning_rate` ต้องมีค่าอยู่ระหว่าง 0.0001 ถึง 0.1 เท่านั้น หากไม่อยู่ในช่วง ให้แสดงข้อความเตือนและไม่เปลี่ยนแปลงค่า
4.  สร้าง Method ชื่อ `display_config()` ที่แสดงค่า Configuration ปัจจุบัน

**Expected Output:**
1.  การสร้าง Object และการแสดงค่าเริ่มต้น
2.  การพยายามตั้งค่า `learning_rate` ที่ถูกต้อง (เช่น 0.01)
3.  การพยายามตั้งค่า `learning_rate` ที่ไม่ถูกต้อง (เช่น 0.5)

---

## Exercise 3: Inheritance and Polymorphism - Data Processor

**โจทย์:**
สร้าง Class Hierarchy สำหรับการประมวลผลข้อมูล (Data Processing)

1.  **Parent Class:** `BaseProcessor` มี Method ชื่อ `process(self, data)` ที่คืนค่า `data` เดิมและแสดงข้อความ "Starting base processing..."
2.  **Child Class 1:** `NLPProcessor` สืบทอดจาก `BaseProcessor` และ **Override** Method `process(self, data)` เพื่อแปลงข้อความเป็นตัวพิมพ์เล็กทั้งหมด (Lowercase) และแสดงข้อความ "Applying NLP preprocessing..."
3.  **Child Class 2:** `ImageProcessor` สืบทอดจาก `BaseProcessor` และ **Override** Method `process(self, data)` เพื่อจำลองการปรับขนาดภาพ (Resize) และแสดงข้อความ "Applying image resizing..."
4.  สร้าง List ของ Object ทั้งสอง และใช้ Polymorphism เพื่อเรียกใช้ Method `process()`

**Input Data:**
```python
text_data = "THIS IS A SAMPLE TEXT FOR NLP"
image_data = "image_file.jpg"
```

**Expected Output:**
1.  ผลลัพธ์การประมวลผลของ `NLPProcessor` (ข้อความตัวพิมพ์เล็ก)
2.  ผลลัพธ์การประมวลผลของ `ImageProcessor` (ชื่อไฟล์เดิม)
3.  ข้อความแสดงการทำงานของแต่ละ Processor

---

## Exercise 4: Decorators - Function Timing

**โจทย์:**
สร้าง Decorator ชื่อ `timer` เพื่อวัดเวลาที่ใช้ในการทำงานของฟังก์ชันที่ถูกเรียกใช้

1.  สร้าง Decorator `timer` ที่รับฟังก์ชันเป็น Input
2.  ภายใน Decorator ให้ใช้ `time.time()` เพื่อวัดเวลาเริ่มต้นและสิ้นสุดการทำงานของฟังก์ชัน
3.  แสดงผลลัพธ์เวลาที่ใช้ในการทำงานของฟังก์ชันนั้น
4.  ใช้ Decorator นี้กับฟังก์ชันจำลองการคำนวณที่ใช้เวลานาน (เช่น การวนลูป 10 ล้านครั้ง)

**Expected Output:**
1.  ข้อความแสดงเวลาที่ใช้ในการทำงานของฟังก์ชัน
2.  ผลลัพธ์ที่ถูกต้องของฟังก์ชันที่ถูก Decorate

---

## Exercise 5: Context Managers - Custom File Handler

**โจทย์:**
สร้าง Custom Context Manager ชื่อ `SafeFileHandler` เพื่อจัดการการเปิดและปิดไฟล์อย่างปลอดภัย

1.  Class `SafeFileHandler` ต้องรับ `filename` และ `mode` เป็น Argument
2.  Implement Method `__enter__` เพื่อเปิดไฟล์และคืนค่า Object ของไฟล์
3.  Implement Method `__exit__` เพื่อปิดไฟล์โดยอัตโนมัติ ไม่ว่าจะเกิด Exception หรือไม่ก็ตาม
4.  ทดสอบการใช้งานโดยการเขียนข้อความลงในไฟล์ และตรวจสอบว่าไฟล์ถูกปิดแล้ว

**Expected Output:**
1.  ข้อความแสดงว่าไฟล์ถูกเปิดและปิดอย่างถูกต้อง
2.  การตรวจสอบสถานะของไฟล์ (เช่น การพยายามเข้าถึงไฟล์หลังออกจากบล็อก `with`)
3.  การตรวจสอบเนื้อหาของไฟล์ที่ถูกเขียน

---
