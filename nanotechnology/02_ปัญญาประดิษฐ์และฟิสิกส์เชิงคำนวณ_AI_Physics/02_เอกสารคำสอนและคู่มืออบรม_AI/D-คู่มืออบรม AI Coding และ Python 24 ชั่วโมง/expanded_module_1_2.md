# โมดูล 1: Python Fundamentals for AI (ขยาย)

## 1.1 การติดตั้งและสภาพแวดล้อม

### 1.1.1 การจัดการ Virtual Environment (venv/conda) อย่างละเอียด

ในงานด้าน AI และ Data Science การจัดการสภาพแวดล้อมเป็นสิ่งสำคัญอย่างยิ่ง เนื่องจากแต่ละโปรเจกต์อาจต้องการไลบรารีและเวอร์ชัน Python ที่แตกต่างกัน **Virtual Environment** ช่วยให้เราสามารถแยกสภาพแวดล้อมของแต่ละโปรเจกต์ออกจากกันได้อย่างสมบูรณ์

**ความสำคัญของ Virtual Environment:**
1.  **การแยกโปรเจกต์:** ป้องกันความขัดแย้งของเวอร์ชันไลบรารีระหว่างโปรเจกต์
2.  **ความสามารถในการทำซ้ำ (Reproducibility):** สามารถแชร์ไฟล์ `requirements.txt` เพื่อให้ผู้อื่นสร้างสภาพแวดล้อมที่เหมือนกันได้

**การใช้งาน `venv` (สำหรับ Python มาตรฐาน):**

```bash
# 1. สร้าง Virtual Environment ชื่อ .venv
python3 -m venv .venv

# 2. เปิดใช้งาน (Activate)
source .venv/bin/activate  # สำหรับ Linux/macOS
.venv\Scripts\activate     # สำหรับ Windows

# 3. ติดตั้งไลบรารี
pip install numpy pandas scikit-learn

# 4. บันทึกรายการไลบรารี
pip freeze > requirements.txt

# 5. ปิดใช้งาน (Deactivate)
deactivate
```

**การใช้งาน `conda` (สำหรับ Anaconda):**

```bash
# 1. สร้างสภาพแวดล้อมชื่อ ai_env ด้วย Python 3.11
conda create -n ai_env python=3.11

# 2. เปิดใช้งาน
conda activate ai_env

# 3. ติดตั้งไลบรารี
conda install numpy pandas scikit-learn

# 4. ปิดใช้งาน
conda deactivate
```

## 1.2 ไวยากรณ์พื้นฐานและชนิดข้อมูล

### 1.2.1 F-Strings และการจัดรูปแบบข้อความขั้นสูง

**F-Strings (Formatted String Literals)** เป็นวิธีที่ทันสมัยและมีประสิทธิภาพที่สุดในการจัดรูปแบบข้อความใน Python 3.6 ขึ้นไป

**ตัวอย่าง: การจัดรูปแบบตัวเลขสำหรับ Data Science**

```python
# สมมติผลลัพธ์การคำนวณ
accuracy = 0.954321
loss = 0.000123456
pi = 3.1415926535

# 1. การกำหนดจำนวนทศนิยม
print(f"ความแม่นยำ: {accuracy:.2f}")  # ผลลัพธ์: ความแม่นยำ: 0.95
print(f"ค่า Pi: {pi:.4f}")          # ผลลัพธ์: ค่า Pi: 3.1416

# 2. การจัดรูปแบบทางวิทยาศาสตร์ (Scientific Notation)
print(f"ค่า Loss: {loss:.2e}")      # ผลลัพธ์: ค่า Loss: 1.23e-04

# 3. การจัดรูปแบบตัวเลขขนาดใหญ่ด้วยเครื่องหมายคอมมา
population = 7800000000
print(f"ประชากรโลก: {population:,}") # ผลลัพธ์: ประชากรโลก: 7,800,000,000
```

## 1.3 โครงสร้างควบคุม

### 1.3.1 List Comprehensions และ Dictionary Comprehensions

Comprehensions เป็นคุณสมบัติที่ทรงพลังของ Python ที่ช่วยให้เราสร้าง List, Dictionary, หรือ Set ได้อย่างรวดเร็วและกระชับ ซึ่งช่วยเพิ่มประสิทธิภาพในการจัดการข้อมูลขนาดใหญ่

**ตัวอย่าง: List Comprehension**

```python
# วิธีดั้งเดิม (ใช้ For Loop)
squares = []
for x in range(10):
    squares.append(x**2)
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# วิธีใช้ List Comprehension (กระชับกว่า)
squares_comp = [x**2 for x in range(10)]

# การใช้เงื่อนไข (Conditional Comprehension)
even_squares = [x**2 for x in range(10) if x % 2 == 0]
# ผลลัพธ์: [0, 4, 16, 36, 64]
```

**ตัวอย่าง: Dictionary Comprehension**

```python
# สร้าง Dictionary จาก List
names = ["Alice", "Bob", "Charlie"]
name_lengths = {name: len(name) for name in names}
# ผลลัพธ์: {'Alice': 5, 'Bob': 3, 'Charlie': 7}
```

## 1.4 ฟังก์ชัน (Functions)

### 1.4.1 Lambda Functions และการใช้งานร่วมกับ `map`, `filter`, `reduce`

**Lambda Function** คือฟังก์ชันขนาดเล็กที่ไม่ระบุชื่อ (Anonymous Function) ที่สามารถมีได้เพียงนิพจน์เดียว (Single Expression) มักใช้ร่วมกับฟังก์ชันที่ต้องการฟังก์ชันอื่นเป็นอาร์กิวเมนต์ เช่น `map` และ `filter`

**ไวยากรณ์:** `lambda arguments: expression`

**ตัวอย่าง: การใช้ `lambda` ร่วมกับ `map` และ `filter`**

```python
data = [10, 25, 40, 55, 70]

# 1. ใช้ map เพื่อแปลงข้อมูล (เพิ่ม 5 ให้ทุกตัว)
# map(function, iterable)
mapped_data = list(map(lambda x: x + 5, data))
print(f"Map Result: {mapped_data}") # [15, 30, 45, 60, 75]

# 2. ใช้ filter เพื่อกรองข้อมูล (เลือกเฉพาะตัวเลขที่มากกว่า 30)
# filter(function, iterable)
filtered_data = list(filter(lambda x: x > 30, data))
print(f"Filter Result: {filtered_data}") # [40, 55, 70]

# 3. ใช้ reduce (ต้อง import จาก functools)
from functools import reduce
# reduce(function, iterable) - ใช้ฟังก์ชันกับคู่ของสมาชิกสะสม
sum_data = reduce(lambda x, y: x + y, data)
print(f"Reduce Result (Sum): {sum_data}") # 200
```

## 1.5 การดีบัก (Debugging) ใน VS Code และการเขียน Test Case เบื้องต้น

### 1.5.1 การดีบักใน VS Code

การดีบักเป็นทักษะสำคัญในการเขียนโค้ด AI เพื่อค้นหาข้อผิดพลาดทางตรรกะ (Logical Errors)

**ขั้นตอนการดีบัก:**
1.  **ตั้ง Breakpoint:** คลิกที่ขอบซ้ายของบรรทัดโค้ดที่ต้องการหยุดการทำงาน
2.  **เริ่ม Debugging:** กด F5 หรือคลิกที่ไอคอน Run and Debug
3.  **ตรวจสอบตัวแปร:** ดูค่าของตัวแปรในหน้าต่าง Variables
4.  **ควบคุมการทำงาน:** ใช้ปุ่ม **Step Over** (F10), **Step Into** (F11), **Step Out** (Shift+F11)

### 1.5.2 การเขียน Test Case เบื้องต้นด้วย `unittest`

การทดสอบโค้ด (Unit Testing) ช่วยให้มั่นใจว่าฟังก์ชันที่เราเขียนทำงานได้ถูกต้องตามที่คาดหวัง

```python
import unittest

# ฟังก์ชันที่เราต้องการทดสอบ
def add_numbers(a, b):
    return a + b

# Class สำหรับการทดสอบ
class TestMathFunctions(unittest.TestCase):

    def test_add_positive_numbers(self):
        # ทดสอบการบวกเลขบวก
        self.assertEqual(add_numbers(2, 3), 5)

    def test_add_negative_numbers(self):
        # ทดสอบการบวกเลขลบ
        self.assertEqual(add_numbers(-1, -1), -2)

# วิธีรัน Test (ใน Terminal): python -m unittest your_file_name.py
```

## 1.6 แบบฝึกหัดและเฉลย (โมดูล 1)

**แบบฝึกหัด 1.1: List Comprehension**
จงใช้ List Comprehension เพื่อสร้าง List ของตัวเลขที่หารด้วย 3 ลงตัว จากช่วง 1 ถึง 50

**แบบฝึกหัด 1.2: Lambda และ Map**
จงใช้ `map` และ `lambda` เพื่อแปลง List ของอุณหภูมิจากเซลเซียสเป็นฟาเรนไฮต์ (สูตร: F = C * 9/5 + 32)

```python
celsius_temps = [0, 10, 20, 30, 40]
```

**เฉลย 1.1:**
```python
result = [x for x in range(1, 51) if x % 3 == 0]
# [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48]
```

**เฉลย 1.2:**
```python
fahrenheit_temps = list(map(lambda c: c * 9/5 + 32, celsius_temps))
# [32.0, 50.0, 68.0, 86.0, 104.0]
```

---

# โมดูล 2: Data Structures & Object-Oriented Programming (ขยาย)

## 2.1 โครงสร้างข้อมูลขั้นสูง

### 2.1.1 โครงสร้างข้อมูลเฉพาะทางจาก `collections`

ไลบรารี `collections` มีโครงสร้างข้อมูลพิเศษที่ช่วยเพิ่มประสิทธิภาพในการจัดการข้อมูลในสถานการณ์เฉพาะ

**1. `Counter`:** ใช้เพื่อนับจำนวนครั้งที่สมาชิกปรากฏใน List (มีประโยชน์มากในการวิเคราะห์ข้อความ)

```python
from collections import Counter

data = ["apple", "banana", "apple", "orange", "banana", "apple"]
word_counts = Counter(data)
print(word_counts)
# ผลลัพธ์: Counter({'apple': 3, 'banana': 2, 'orange': 1})

# หา 2 คำที่พบบ่อยที่สุด
print(word_counts.most_common(2))
# ผลลัพธ์: [('apple', 3), ('banana', 2)]
```

**2. `NamedTuple`:** ใช้สร้าง Tuple ที่สามารถเข้าถึงสมาชิกด้วยชื่อแทนการใช้ Index ทำให้โค้ดอ่านง่ายขึ้น (มีประโยชน์ในการเก็บ Record ข้อมูล)

```python
from collections import namedtuple

# กำหนดโครงสร้างของ Record
Point = namedtuple('Point', ['x', 'y'])

# สร้าง Object
p1 = Point(x=10, y=20)

# เข้าถึงข้อมูลด้วยชื่อ
print(f"ค่า x: {p1.x}")
print(f"ค่า y: {p1.y}")
```

## 2.2 การจัดการไฟล์ (File I/O)

### 2.2.1 การจัดการไฟล์ JSON/CSV และการใช้ `pathlib`

ในงาน AI/ML เรามักต้องจัดการกับไฟล์ข้อมูลที่มีโครงสร้าง เช่น JSON และ CSV

**1. การจัดการไฟล์ JSON:**

```python
import json

data = {
    "model_name": "LinearRegression",
    "hyperparameters": {"learning_rate": 0.01, "epochs": 100}
}

# เขียนไฟล์ JSON
with open("config.json", "w") as f:
    json.dump(data, f, indent=4)

# อ่านไฟล์ JSON
with open("config.json", "r") as f:
    loaded_data = json.load(f)
    print(loaded_data["model_name"])
```

**2. การใช้ `pathlib` (จัดการเส้นทางไฟล์อย่างทันสมัย):**

`pathlib` ช่วยให้การจัดการเส้นทางไฟล์เป็นไปอย่างง่ายดายและเป็นอิสระจากระบบปฏิบัติการ

```python
from pathlib import Path

# สร้าง Path Object
data_dir = Path("data")
model_file = data_dir / "trained_model.pkl"

# ตรวจสอบว่า Directory มีอยู่หรือไม่
if not data_dir.exists():
    data_dir.mkdir()

# แสดงเส้นทางไฟล์
print(f"เส้นทางไฟล์โมเดล: {model_file}")
# ผลลัพธ์: data/trained_model.pkl
```

## 2.3 แนวคิดการเขียนโปรแกรมเชิงวัตถุ (OOP)

### 2.3.1 หลักการ OOP 4 ข้อ (Encapsulation, Polymorphism, Abstraction) อย่างละเอียด

การประยุกต์ใช้ OOP ในงาน AI ช่วยให้เราสามารถสร้าง Class สำหรับ Model, Dataset, และ Trainer ได้อย่างเป็นระบบ

**1. Encapsulation (การห่อหุ้ม):** การรวมข้อมูล (Attributes) และเมธอด (Methods) ที่ทำงานกับข้อมูลนั้นไว้ใน Class เดียวกัน และซ่อนรายละเอียดภายในที่ไม่จำเป็น

```python
class ModelConfig:
    def __init__(self, lr, epochs):
        # ใช้ _ เพื่อบ่งบอกว่าเป็น Private Attribute (ตามธรรมเนียม)
        self._learning_rate = lr
        self._epochs = epochs

    def get_config(self):
        return f"LR: {self._learning_rate}, Epochs: {self._epochs}"
```

**2. Inheritance (การสืบทอด):** การสร้าง Class ใหม่ (Subclass) จาก Class ที่มีอยู่แล้ว (Superclass) เพื่อนำคุณสมบัติเดิมมาใช้และเพิ่มคุณสมบัติใหม่ (ดูตัวอย่างในฉบับร่างเดิม)

**3. Polymorphism (พหุสัณฐาน):** การที่ Object ต่างชนิดกันสามารถตอบสนองต่อเมธอดชื่อเดียวกันได้แตกต่างกัน

```python
class RegressionModel:
    def train(self):
        print("Training Linear Regression Model...")

class ClassificationModel:
    def train(self):
        print("Training Decision Tree Classifier...")

def start_training(model):
    # Polymorphism: ฟังก์ชันนี้เรียกเมธอด train() โดยไม่สนใจว่า model เป็น Class ใด
    model.train()

start_training(RegressionModel())
start_training(ClassificationModel())
```

**4. Abstraction (นามธรรม):** การซ่อนรายละเอียดการทำงานที่ซับซ้อน และแสดงเฉพาะส่วนที่จำเป็นต่อผู้ใช้ (มักใช้ร่วมกับ Abstract Base Class)

## 2.4 Decorators และการใช้งาน

**Decorator** คือฟังก์ชันที่รับฟังก์ชันอื่นเป็นอาร์กิวเมนต์ และส่งคืนฟังก์ชันใหม่ที่ถูกปรับปรุงแล้ว (Wrapper Function) มีประโยชน์ในการเพิ่มฟังก์ชันการทำงานเสริม เช่น การวัดเวลาการทำงาน, การตรวจสอบสิทธิ์, หรือการบันทึก Log

**ตัวอย่าง: Decorator สำหรับวัดเวลาการทำงาน**

```python
import time

def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"ฟังก์ชัน {func.__name__} ใช้เวลา: {end_time - start_time:.4f} วินาที")
        return result
    return wrapper

@timer
def data_preprocessing(data_size):
    """สมมติว่าเป็นฟังก์ชันประมวลผลข้อมูลที่ใช้เวลานาน"""
    time.sleep(data_size * 0.01)
    return f"ประมวลผลข้อมูลขนาด {data_size} เสร็จสิ้น"

data_preprocessing(100)
# ผลลัพธ์: ฟังก์ชัน data_preprocessing ใช้เวลา: 1.00xx วินาที
```

## 2.5 Context Managers (`with` statement) และการสร้าง Custom Context Manager

**Context Manager** คือ Object ที่จัดการทรัพยากรอย่างปลอดภัย โดยรับประกันว่าทรัพยากรจะถูกจัดสรรและปล่อยคืนอย่างถูกต้อง แม้ว่าจะเกิดข้อผิดพลาดก็ตาม (เช่น การเปิด/ปิดไฟล์)

**การสร้าง Custom Context Manager (ใช้ `contextlib`):**

```python
from contextlib import contextmanager

@contextmanager
def timer_context(name):
    start_time = time.time()
    print(f"[{name}] เริ่มต้นการทำงาน...")
    try:
        yield # ส่วนนี้คือโค้ดที่อยู่ภายในบล็อก 'with'
    finally:
        end_time = time.time()
        print(f"[{name}] สิ้นสุดการทำงาน. ใช้เวลา: {end_time - start_time:.4f} วินาที")

# การใช้งาน
with timer_context("Model Training"):
    time.sleep(0.5)
    print("กำลังฝึกโมเดล...")
```

## 2.6 แบบฝึกหัดและเฉลย (โมดูล 2)

**แบบฝึกหัด 2.1: Counter และ NamedTuple**
จงใช้ `Counter` เพื่อนับความถี่ของตัวเลขใน List และใช้ `NamedTuple` เพื่อสร้าง Record สำหรับเก็บข้อมูลผู้ใช้ (ชื่อ, อีเมล, คะแนน)

```python
scores = [80, 95, 80, 70, 95, 95, 80]
```

**แบบฝึกหัด 2.2: Decorator**
จงสร้าง Decorator ชื่อ `log_call` ที่จะพิมพ์ข้อความ "Function [ชื่อฟังก์ชัน] ถูกเรียกใช้" ทุกครั้งที่ฟังก์ชันนั้นถูกเรียก

**เฉลย 2.1:**
```python
from collections import Counter, namedtuple
scores_count = Counter(scores)
# Counter({95: 3, 80: 3, 70: 1})

User = namedtuple('User', ['name', 'email', 'score'])
user1 = User(name="Somsak", email="somsak@mail.com", score=95)
```

**เฉลย 2.2:**
```python
def log_call(func):
    def wrapper(*args, **kwargs):
        print(f"Function {func.__name__} ถูกเรียกใช้")
        return func(*args, **kwargs)
    return wrapper

@log_call
def calculate_loss(predictions, actuals):
    return sum((p - a)**2 for p, a in zip(predictions, actuals))

calculate_loss([1, 2, 3], [1.1, 2.1, 3.1])
# ผลลัพธ์:
# Function calculate_loss ถูกเรียกใช้
# 0.030000000000000006
```

---
**หมายเหตุ:** เนื้อหาส่วนนี้เป็นส่วนขยายของโมดูล 1 และ 2 ซึ่งจะถูกนำไปรวมกับเนื้อหาโมดูล 3-6 ที่จะขยายในขั้นตอนต่อไป เพื่อให้ได้คู่มือฉบับสมบูรณ์ 200-300 หน้า
