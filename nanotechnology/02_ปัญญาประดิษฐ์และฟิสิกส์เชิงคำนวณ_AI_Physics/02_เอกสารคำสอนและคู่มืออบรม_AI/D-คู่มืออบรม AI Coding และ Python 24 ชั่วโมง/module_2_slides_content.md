# Module 2: Data Structures & Object-Oriented Programming

## 1. Title Slide
### Module 2: Data Structures & Object-Oriented Programming
#### AI Coding & Python: Basic to Advanced (24 Hours Workshop)

## 2. Module Overview: Key Learning Objectives
### วัตถุประสงค์หลักของโมดูล 2
*   **โครงสร้างข้อมูลขั้นสูง:** เข้าใจและใช้ `collections` (Counter, defaultdict)
*   **OOP Core Concepts:** เข้าใจหลักการ Encapsulation, Inheritance, Polymorphism, Abstraction
*   **Advanced Python Features:** สามารถใช้ Decorators และ Context Managers ได้อย่างมีประสิทธิภาพ
*   **การประยุกต์ใช้:** สร้างโค้ดที่มีโครงสร้างดี, จัดการข้อมูลอย่างเป็นระบบ, และนำไปใช้ในโปรเจกต์ AI

## 3. Advanced Data Structures: collections
![Data Structures](/home/ubuntu/slide_3_data_structures.png)
### การใช้ `defaultdict` และ `Counter`
*   **`defaultdict`:** สร้าง Dictionary ที่มีค่าเริ่มต้นอัตโนมัติ (ลดการใช้ `if key in dict`)
    *   *ตัวอย่าง:* การจัดกลุ่มข้อมูล (Grouping)
*   **`Counter`:** นับความถี่ขององค์ประกอบใน List หรือ String ได้อย่างรวดเร็ว
    *   *ตัวอย่าง:* การนับคำ (Word Count) ใน Natural Language Processing (NLP)

```python
from collections import Counter, defaultdict
# Counter Example
word_list = ['python', 'ai', 'python', 'ml', 'ai']
counts = Counter(word_list) # {'python': 2, 'ai': 2, 'ml': 1}
# defaultdict Example
grouped = defaultdict(list)
grouped['A'].append(1) # ไม่ต้องเช็คว่า 'A' มีอยู่หรือไม่
```

## 4. Named Tuples: โครงสร้างข้อมูลที่อ่านง่าย
![Named Tuples](/home/ubuntu/slide_4_named_tuples.png)
### การใช้ `namedtuple` เพื่อความชัดเจนของโค้ด
*   **วัตถุประสงค์:** สร้าง Tuple ที่มีชื่อฟิลด์ (Field Names) ทำให้เข้าถึงข้อมูลได้ด้วยชื่อแทน Index
*   **ข้อดี:** โค้ดอ่านง่ายขึ้น, ป้องกันข้อผิดพลาดจากการจำ Index ผิด, มีน้ำหนักเบากว่า Class ทั่วไป

```python
from collections import namedtuple
Point = namedtuple('Point', ['x', 'y'])
p = Point(x=10, y=20)
print(f"X: {p.x}, Y: {p.y}") # เข้าถึงด้วยชื่อ
```

## 5. OOP: Core Concepts
![OOP Pillars](/home/ubuntu/slide_5_oop_pillars.png)
### หลักการ 4 ข้อของ Object-Oriented Programming
| หลักการ | คำอธิบาย | การประยุกต์ใช้ใน AI |
| :--- | :--- | :--- |
| **Encapsulation** | การรวมข้อมูล (Attributes) และฟังก์ชัน (Methods) เข้าด้วยกัน และซ่อนรายละเอียดภายใน | การสร้าง Class `ModelConfig` เพื่อรวม Hyperparameters |
| **Inheritance** | การสืบทอดคุณสมบัติจาก Class แม่ (Parent) ไปยัง Class ลูก (Child) | การสร้าง Class `CNNModel` ที่สืบทอดจาก `BaseModel` |
| **Polymorphism** | การที่ Object ต่างชนิดกันสามารถตอบสนองต่อ Method เดียวกันได้ในรูปแบบที่แตกต่างกัน | การใช้ Method `fit()` ใน Scikit-learn ที่ทำงานต่างกันในแต่ละ Algorithm |
| **Abstraction** | การแสดงเฉพาะส่วนที่จำเป็นต่อผู้ใช้ และซ่อนความซับซ้อนภายใน | การใช้ Class `DataLoader` โดยไม่ต้องรู้รายละเอียดการโหลดข้อมูล |

## 6. OOP: Encapsulation & Properties
![Encapsulation](/home/ubuntu/slide_6_encapsulation.png)
### การควบคุมการเข้าถึงข้อมูลด้วย `@property`
*   **Encapsulation:** ป้องกันการเข้าถึงหรือแก้ไขข้อมูลโดยตรง
*   **Private Attributes:** ใช้ `__` (Double Underscore) นำหน้าชื่อ Attribute (Python จะทำการ Name Mangling)
*   **`@property` Decorator:** ใช้สร้าง Getter/Setter Method เพื่อควบคุมการอ่านและเขียน Attribute

```python
class Circle:
    def __init__(self, radius):
        self.__radius = radius # Private Attribute
    
    @property
    def radius(self):
        return self.__radius
    
    @radius.setter
    def radius(self, value):
        if value > 0:
            self.__radius = value
```

## 7. OOP: Inheritance & Polymorphism
![Inheritance](/home/ubuntu/slide_7_inheritance.png)
### การสืบทอดและการเขียนทับ Method
*   **Inheritance:** Class ลูกสืบทอด Attributes และ Methods จาก Class แม่
*   **Polymorphism:** Class ลูกสามารถเขียนทับ (Override) Method ของ Class แม่ได้

```python
class Animal:
    def speak(self):
        return "..."

class Dog(Animal):
    def speak(self): # Method Overriding
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

animals = [Dog(), Cat()]
for animal in animals:
    print(animal.speak()) # Polymorphism
```

## 8. Magic Methods (Dunder Methods)
![Magic Methods](/home/ubuntu/slide_8_magic_methods.png)
### Method พิเศษที่กำหนดพฤติกรรมของ Object
*   **`__init__(self, ...)`:** Constructor, ถูกเรียกเมื่อสร้าง Object
*   **`__str__(self)`:** กำหนดรูปแบบการแสดงผลเมื่อใช้ `print(object)`
*   **`__len__(self)`:** กำหนดค่าที่คืนกลับเมื่อใช้ฟังก์ชัน `len(object)`

```python
class DataList:
    def __init__(self, data):
        self.data = data
    
    def __len__(self):
        return len(self.data)
    
    def __str__(self):
        return f"DataList with {len(self)} items"

dl = DataList([1, 2, 3])
print(len(dl)) # Calls __len__
print(dl)      # Calls __str__
```

## 9. Decorators: Introduction
![Decorators](/home/ubuntu/slide_9_decorators.png)
### Decorators คืออะไร?
*   **นิยาม:** ฟังก์ชันที่รับฟังก์ชันอื่นเป็น Input และคืนค่าเป็นฟังก์ชันใหม่
*   **Syntax:** ใช้เครื่องหมาย `@` นำหน้าชื่อฟังก์ชัน
*   **วัตถุประสงค์:** เพิ่มฟังก์ชันการทำงานให้กับฟังก์ชันเดิมโดยไม่ต้องแก้ไขโค้ดต้นฉบับ (เช่น Logging, Timing, Authorization)

```python
def my_decorator(func):
    def wrapper():
        print("Before function call")
        func()
        print("After function call")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

# say_hello() จะถูกห่อหุ้มด้วย wrapper
```

## 10. Decorators: Use Cases
![Decorator Use Cases](/home/ubuntu/slide_10_decorator_use_cases.png)
### การประยุกต์ใช้ Decorators ในงาน AI/ML
*   **Timing:** วัดเวลาการทำงานของฟังก์ชัน (สำคัญในการวัดประสิทธิภาพโมเดล)
*   **Logging:** บันทึกการทำงานของฟังก์ชัน
*   **Caching:** เก็บผลลัพธ์ของฟังก์ชันที่ถูกเรียกซ้ำ (เช่น `@functools.lru_cache`)
*   **Authorization:** ตรวจสอบสิทธิ์ก่อนเข้าถึงฟังก์ชัน

## 11. Context Managers: The `with` Statement
![Context Managers](/home/ubuntu/slide_11_context_managers.png)
### การจัดการทรัพยากรอย่างปลอดภัย
*   **วัตถุประสงค์:** รับประกันว่าทรัพยากร (เช่น ไฟล์, การเชื่อมต่อฐานข้อมูล) จะถูกเปิดและปิดอย่างถูกต้องเสมอ แม้เกิดข้อผิดพลาด
*   **Method หลัก:**
    *   `__enter__`: ถูกเรียกเมื่อเข้าสู่บล็อก `with` (คืนค่าทรัพยากร)
    *   `__exit__`: ถูกเรียกเมื่อออกจากบล็อก `with` (ทำความสะอาดทรัพยากร)

```python
# การจัดการไฟล์ (ตัวอย่างคลาสสิก)
with open('data.txt', 'r') as f:
    content = f.read()
# f จะถูกปิดโดยอัตโนมัติเมื่อออกจากบล็อก
```

## 12. Summary & Q&A
### สรุปประเด็นสำคัญของโมดูล 2
*   **Data Structures:** ใช้ `collections` เพื่อจัดการข้อมูลที่ซับซ้อนอย่างมีประสิทธิภาพ
*   **OOP:** ใช้หลักการ OOP เพื่อสร้างโค้ดที่มีโครงสร้าง, จัดการง่าย, และนำกลับมาใช้ใหม่ได้
*   **Decorators & Context Managers:** ใช้ฟีเจอร์ขั้นสูงของ Python เพื่อเพิ่มความสามารถและจัดการทรัพยากรอย่างปลอดภัย
### คำถามและคำตอบ (Q&A)
#### เตรียมพร้อมสำหรับโมดูลถัดไป: Python for Data Analysis
