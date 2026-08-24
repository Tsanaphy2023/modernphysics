# แบบฝึกหัดและเฉลย Module 2: Data Structures & Object-Oriented Programming

## ส่วนที่ 1: แบบฝึกหัดเชิงปฏิบัติการ

### Exercise 1: Advanced Collections for Data Preprocessing (defaultdict & Counter)

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

### Exercise 2: Object-Oriented Programming (OOP) - Model Configuration

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

### Exercise 3: Inheritance and Polymorphism - Data Processor

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

### Exercise 4: Decorators - Function Timing

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

### Exercise 5: Context Managers - Custom File Handler

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
---

## ส่วนที่ 2: เฉลยแบบฝึกหัดเชิงปฏิบัติการ

### Exercise 1: Advanced Collections for Data Preprocessing

#### Solution Code:
```python
from collections import Counter, defaultdict

usage_data = [
    (101, 'Image_Recognition'), (102, 'Text_Summarization'), (101, 'Image_Recognition'),
    (103, 'Code_Generation'), (102, 'Text_Summarization'), (101, 'Code_Generation'),
    (104, 'Image_Recognition'), (103, 'Text_Summarization'), (101, 'Image_Recognition'),
    (105, 'Code_Generation'), (104, 'Text_Summarization'), (105, 'Image_Recognition')
]

# 1. Grouped Data by user_id
grouped_data = defaultdict(list)
for user_id, feature in usage_data:
    grouped_data[user_id].append(feature)

print("1. Grouped Data:")
for user_id, features in grouped_data.items():
    print(f"User {user_id}: {features}")

# 2. Top 3 Features
all_features = [feature for user_id, feature in usage_data]
feature_counts = Counter(all_features)
top_3_features = feature_counts.most_common(3)

print("\n2. Top 3 Features:")
print(top_3_features)
```

#### คำอธิบาย:
- **`defaultdict(list)`** ช่วยให้เราสามารถเพิ่มค่า (feature) เข้าไปใน List ที่เป็น Value ของ Dictionary ได้ทันทีโดยไม่ต้องตรวจสอบว่า Key (user_id) นั้นมีอยู่แล้วหรือไม่
- **`Counter`** เป็นวิธีที่ง่ายและมีประสิทธิภาพที่สุดในการนับความถี่ขององค์ประกอบใน List และ `most_common(3)` จะคืนค่า 3 อันดับแรก

---

### Exercise 2: Object-Oriented Programming (OOP) - Model Configuration

#### Solution Code:
```python
class AIModelConfig:
    def __init__(self, learning_rate=0.001, epochs=10):
        # Private Attributes
        self.__learning_rate = learning_rate
        self.__epochs = epochs

    @property
    def learning_rate(self):
        return self.__learning_rate

    @learning_rate.setter
    def learning_rate(self, value):
        if 0.0001 <= value <= 0.1:
            print(f"Setting learning_rate to {value}")
            self.__learning_rate = value
        else:
            print(f"WARNING: Invalid learning_rate {value}. Must be between 0.0001 and 0.1. Value remains {self.__learning_rate}")

    @property
    def epochs(self):
        return self.__epochs

    def display_config(self):
        print("--- AI Model Configuration ---")
        print(f"Learning Rate: {self.learning_rate}")
        print(f"Epochs: {self.epochs}")
        print("------------------------------")

# ทดสอบการใช้งาน
config = AIModelConfig()
config.display_config()

# 2. การพยายามตั้งค่าที่ถูกต้อง
config.learning_rate = 0.01
config.display_config()

# 3. การพยายามตั้งค่าที่ไม่ถูกต้อง
config.learning_rate = 0.5
config.display_config()
```

#### คำอธิบาย:
- การใช้ **`@property`** และ **`@<attribute>.setter`** ทำให้เราสามารถควบคุมการเข้าถึงและแก้ไข Private Attribute (`__learning_rate`) ได้อย่างปลอดภัย ซึ่งเป็นหัวใจของ **Encapsulation**

---

### Exercise 3: Inheritance and Polymorphism - Data Processor

#### Solution Code:
```python
class BaseProcessor:
    def process(self, data):
        print("Starting base processing...")
        return data

class NLPProcessor(BaseProcessor):
    def process(self, data):
        print("Applying NLP preprocessing...")
        # Polymorphism: Override the parent's method
        return data.lower()

class ImageProcessor(BaseProcessor):
    def process(self, data):
        print("Applying image resizing...")
        # Polymorphism: Override the parent's method
        return data # จำลองว่ามีการประมวลผลแล้วคืนค่าเดิม

# Input Data
text_data = "THIS IS A SAMPLE TEXT FOR NLP"
image_data = "image_file.jpg"

# สร้าง List ของ Object ที่สืบทอดมาจาก BaseProcessor
processors = [NLPProcessor(), ImageProcessor()]
data_to_process = [text_data, image_data]

print("--- Processing Data Polymorphically ---")
for i, processor in enumerate(processors):
    data = data_to_process[i]
    print(f"\nProcessor: {processor.__class__.__name__}")
    result = processor.process(data)
    print(f"Input: {data}")
    print(f"Output: {result}")
```

#### คำอธิบาย:
- **Inheritance:** `NLPProcessor` และ `ImageProcessor` สืบทอดคุณสมบัติจาก `BaseProcessor`
- **Polymorphism:** แม้ว่าเราจะเรียกใช้ `processor.process(data)` เหมือนกัน แต่ผลลัพธ์ที่ได้จะแตกต่างกันไปตาม Class ที่เรียกใช้ เนื่องจาก Method `process` ถูก **Override** ใน Class ลูก

---

### Exercise 4: Decorators - Function Timing

#### Solution Code:
```python
import time

def timer(func):
    """Decorator to measure the execution time of a function."""
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Function '{func.__name__}' executed in {execution_time:.4f} seconds.")
        return result
    return wrapper

@timer
def long_running_calculation(n):
    """Simulates a long calculation."""
    total = 0
    for i in range(n):
        total += i
    return total

# ทดสอบการใช้งาน
result = long_running_calculation(10000000)
print(f"Calculation Result: {result}")
```

#### คำอธิบาย:
- **`@timer`** ห่อหุ้มฟังก์ชัน `long_running_calculation` โดยอัตโนมัติ
- เมื่อ `long_running_calculation` ถูกเรียกใช้, โค้ดใน `wrapper` จะทำงานก่อนและหลังฟังก์ชันหลัก ทำให้สามารถวัดเวลาได้อย่างแม่นยำโดยไม่ต้องแก้ไขโค้ดของฟังก์ชันหลัก

---

### Exercise 5: Context Managers - Custom File Handler

#### Solution Code:
```python
import os

class SafeFileHandler:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None

    def __enter__(self):
        print(f"__enter__: Opening file '{self.filename}' in mode '{self.mode}'")
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            print(f"__exit__: Closing file '{self.filename}'")
            self.file.close()
        
        # หากมี Exception เกิดขึ้นในบล็อก with, exc_type จะไม่เป็น None
        if exc_type:
            print(f"An exception of type {exc_type.__name__} occurred.")
            # คืนค่า False เพื่อให้ Exception ถูกยกขึ้นต่อ (True เพื่อระงับ)
            return False 
        return True

# 1. ทดสอบการใช้งานปกติ
file_path = "test_log.txt"
with SafeFileHandler(file_path, 'w') as f:
    f.write("Log entry 1: Model training started.\n")
    f.write("Log entry 2: Data loaded successfully.\n")

# 2. ตรวจสอบสถานะของไฟล์ (ควรถูกปิดแล้ว)
print(f"\nIs file closed? {f.closed}")

# 3. ตรวจสอบเนื้อหาของไฟล์
with open(file_path, 'r') as f:
    content = f.read()
print(f"\nFile Content:\n{content}")

# 4. ลบไฟล์ที่สร้างขึ้น
os.remove(file_path)
```

#### คำอธิบาย:
- **`__enter__`** ถูกเรียกเมื่อเข้าสู่บล็อก `with` และคืนค่า Object ของไฟล์ที่เปิด
- **`__exit__`** ถูกเรียกเสมอเมื่อออกจากบล็อก `with` (ไม่ว่าจะสำเร็จหรือเกิด Exception) และรับประกันว่า `self.file.close()` จะถูกเรียกใช้ ซึ่งเป็นหัวใจของการจัดการทรัพยากรด้วย **Context Managers**

---
