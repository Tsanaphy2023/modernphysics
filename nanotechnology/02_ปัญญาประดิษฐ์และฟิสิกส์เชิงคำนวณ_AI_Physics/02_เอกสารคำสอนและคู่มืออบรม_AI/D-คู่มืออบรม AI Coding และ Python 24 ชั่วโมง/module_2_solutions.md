# เฉลยแบบฝึกหัดเชิงปฏิบัติการ Module 2: Data Structures & Object-Oriented Programming

## Exercise 1: Advanced Collections for Data Preprocessing

### Solution Code:
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

### Expected Output:
```
1. Grouped Data:
User 101: ['Image_Recognition', 'Image_Recognition', 'Code_Generation', 'Image_Recognition']
User 102: ['Text_Summarization', 'Text_Summarization']
User 103: ['Code_Generation', 'Text_Summarization']
User 104: ['Image_Recognition', 'Text_Summarization']
User 105: ['Code_Generation', 'Image_Recognition']

2. Top 3 Features:
[('Image_Recognition', 5), ('Text_Summarization', 4), ('Code_Generation', 3)]
```

### คำอธิบาย:
- **`defaultdict(list)`** ช่วยให้เราสามารถเพิ่มค่า (feature) เข้าไปใน List ที่เป็น Value ของ Dictionary ได้ทันทีโดยไม่ต้องตรวจสอบว่า Key (user_id) นั้นมีอยู่แล้วหรือไม่
- **`Counter`** เป็นวิธีที่ง่ายและมีประสิทธิภาพที่สุดในการนับความถี่ขององค์ประกอบใน List และ `most_common(3)` จะคืนค่า 3 อันดับแรก

---

## Exercise 2: Object-Oriented Programming (OOP) - Model Configuration

### Solution Code:
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

### Expected Output:
```
--- AI Model Configuration ---
Learning Rate: 0.001
Epochs: 10
------------------------------
Setting learning_rate to 0.01
--- AI Model Configuration ---
Learning Rate: 0.01
Epochs: 10
------------------------------
WARNING: Invalid learning_rate 0.5. Must be between 0.0001 and 0.1. Value remains 0.01
--- AI Model Configuration ---
Learning Rate: 0.01
Epochs: 10
------------------------------
```

### คำอธิบาย:
- การใช้ **`@property`** และ **`@<attribute>.setter`** ทำให้เราสามารถควบคุมการเข้าถึงและแก้ไข Private Attribute (`__learning_rate`) ได้อย่างปลอดภัย ซึ่งเป็นหัวใจของ **Encapsulation**

---

## Exercise 3: Inheritance and Polymorphism - Data Processor

### Solution Code:
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

### Expected Output:
```
--- Processing Data Polymorphically ---

Processor: NLPProcessor
Applying NLP preprocessing...
Input: THIS IS A SAMPLE TEXT FOR NLP
Output: this is a sample text for nlp

Processor: ImageProcessor
Applying image resizing...
Input: image_file.jpg
Output: image_file.jpg
```

### คำอธิบาย:
- **Inheritance:** `NLPProcessor` และ `ImageProcessor` สืบทอดคุณสมบัติจาก `BaseProcessor`
- **Polymorphism:** แม้ว่าเราจะเรียกใช้ `processor.process(data)` เหมือนกัน แต่ผลลัพธ์ที่ได้จะแตกต่างกันไปตาม Class ที่เรียกใช้ เนื่องจาก Method `process` ถูก **Override** ใน Class ลูก

---

## Exercise 4: Decorators - Function Timing

### Solution Code:
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

### Expected Output (เวลาอาจแตกต่างกันไป):
```
Function 'long_running_calculation' executed in 0.5xxx seconds.
Calculation Result: 49999995000000
```

### คำอธิบาย:
- **`@timer`** ห่อหุ้มฟังก์ชัน `long_running_calculation` โดยอัตโนมัติ
- เมื่อ `long_running_calculation` ถูกเรียกใช้, โค้ดใน `wrapper` จะทำงานก่อนและหลังฟังก์ชันหลัก ทำให้สามารถวัดเวลาได้อย่างแม่นยำโดยไม่ต้องแก้ไขโค้ดของฟังก์ชันหลัก

---

## Exercise 5: Context Managers - Custom File Handler

### Solution Code:
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

### Expected Output:
```
__enter__: Opening file 'test_log.txt' in mode 'w'
__exit__: Closing file 'test_log.txt'

Is file closed? True

File Content:
Log entry 1: Model training started.
Log entry 2: Data loaded successfully.
```

### คำอธิบาย:
- **`__enter__`** ถูกเรียกเมื่อเข้าสู่บล็อก `with` และคืนค่า Object ของไฟล์ที่เปิด
- **`__exit__`** ถูกเรียกเสมอเมื่อออกจากบล็อก `with` (ไม่ว่าจะสำเร็จหรือเกิด Exception) และรับประกันว่า `self.file.close()` จะถูกเรียกใช้ ซึ่งเป็นหัวใจของการจัดการทรัพยากรด้วย **Context Managers**

---
