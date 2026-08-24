# คู่มืออบรมเชิงปฏิบัติการ 24 ชั่วโมง: AI Coding & Python (Basic to Advanced)

**ผู้เขียน:** Manus AI
**ระยะเวลา:** 24 ชั่วโมง (6 โมดูล x 4 ชั่วโมง)
**วัตถุประสงค์:** เพื่อให้ผู้เข้ารับการอบรมสามารถใช้ภาษา Python ในการเขียนโค้ดได้อย่างมีประสิทธิภาพ ตั้งแต่พื้นฐานไปจนถึงการประยุกต์ใช้ในงานด้านปัญญาประดิษฐ์ (AI) และการวิเคราะห์ข้อมูล

---

## โมดูล 1: Python Fundamentals for AI (4 ชั่วโมง)

### 1.1 การติดตั้งและสภาพแวดล้อม
การเริ่มต้นที่ถูกต้องเป็นสิ่งสำคัญสำหรับงานด้าน AI และ Data Science เราจะใช้ **Anaconda** เพื่อจัดการสภาพแวดล้อมและแพ็กเกจต่างๆ และใช้ **VS Code** เป็นเครื่องมือในการเขียนโค้ด

**ขั้นตอนการติดตั้ง:**
1. ติดตั้ง Anaconda (แนะนำเวอร์ชันสำหรับ Python 3.x)
2. ติดตั้ง Visual Studio Code (VS Code)
3. ติดตั้งส่วนขยาย (Extensions) ที่จำเป็นใน VS Code เช่น Python, Jupyter

### 1.2 ไวยากรณ์พื้นฐานและชนิดข้อมูล
Python เป็นภาษาที่เน้นความอ่านง่าย (Readability) โดยใช้การเยื้อง (Indentation) แทนวงเล็บปีกกา

| ชนิดข้อมูล | คำอธิบาย | ตัวอย่าง |
| :--- | :--- | :--- |
| `int` | จำนวนเต็ม | `age = 30` |
| `float` | จำนวนทศนิยม | `pi = 3.14159` |
| `str` | ข้อความ (String) | `name = "Manus"` |
| `bool` | ค่าความจริง (True/False) | `is_ai = True` |

**ตัวอย่างโค้ด: การประกาศตัวแปรและการดำเนินการ**

```python
# การดำเนินการทางคณิตศาสตร์
a = 10
b = 3
result = a / b  # 3.333...
print(f"ผลหาร: {result}")

# การจัดการข้อความ
first_name = "AI"
last_name = "Coder"
full_name = first_name + " " + last_name
print(f"ชื่อเต็ม: {full_name}")
```

### 1.3 โครงสร้างควบคุม (Control Flow)
โครงสร้างควบคุมช่วยให้โปรแกรมตัดสินใจและทำซ้ำคำสั่งได้

**If-Else Statement:**

```python
score = 85
if score >= 80:
    print("ได้เกรด A")
elif score >= 70:
    print("ได้เกรด B")
else:
    print("ต้องปรับปรุง")
```

**Loops (For และ While):**

```python
# For Loop สำหรับวนซ้ำในรายการ
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(f"ผลไม้: {fruit}")

# While Loop สำหรับวนซ้ำตามเงื่อนไข
count = 0
while count < 3:
    print(f"นับ: {count}")
    count += 1
```

### 1.4 ฟังก์ชัน (Functions)
ฟังก์ชันคือกลุ่มของคำสั่งที่ทำงานเฉพาะอย่าง สามารถนำกลับมาใช้ใหม่ได้ (Reusability)

**ตัวอย่างโค้ด: การสร้างฟังก์ชัน**

```python
def calculate_bmi(weight_kg, height_m):
    """คำนวณค่าดัชนีมวลกาย (BMI)"""
    bmi = weight_kg / (height_m ** 2)
    return bmi

# การเรียกใช้ฟังก์ชัน
my_bmi = calculate_bmi(weight_kg=70, height_m=1.75)
print(f"ค่า BMI ของฉันคือ: {my_bmi:.2f}")
```

---

## โมดูล 2: Data Structures & Object-Oriented Programming (4 ชั่วโมง)

### 2.1 โครงสร้างข้อมูลขั้นสูง
โครงสร้างข้อมูลเหล่านี้เป็นพื้นฐานในการจัดการข้อมูลในงาน AI

| โครงสร้างข้อมูล | ลักษณะ | ตัวอย่าง |
| :--- | :--- | :--- |
| **List** | ลำดับที่เปลี่ยนแปลงได้ (Mutable), มีลำดับ | `[1, "a", True]` |
| **Tuple** | ลำดับที่ไม่เปลี่ยนแปลง (Immutable), มีลำดับ | `(10, 20, 30)` |
| **Dictionary** | คู่ของคีย์-ค่า (Key-Value), ไม่มีลำดับ | `{"name": "Manus", "age": 1}` |
| **Set** | กลุ่มของสมาชิกที่ไม่ซ้ำกัน, ไม่มีลำดับ | `{1, 2, 3}` |

**ตัวอย่างโค้ด: การใช้ Dictionary**

```python
# Dictionary สำหรับเก็บข้อมูลลูกค้า
customer = {
    "id": "C001",
    "name": "สมชาย",
    "orders": [101, 102]
}

print(f"ชื่อลูกค้า: {customer['name']}")
customer["city"] = "Bangkok" # เพิ่มข้อมูล
print(customer)
```

### 2.2 การจัดการไฟล์ (File I/O)
การอ่านและเขียนไฟล์เป็นสิ่งจำเป็นสำหรับการโหลดชุดข้อมูล

**ตัวอย่างโค้ด: การอ่านไฟล์อย่างปลอดภัย**

```python
try:
    # ใช้ 'with' เพื่อให้แน่ใจว่าไฟล์จะถูกปิดโดยอัตโนมัติ
    with open("data.txt", "r", encoding="utf-8") as file:
        content = file.read()
        print("เนื้อหาไฟล์:")
        print(content)
except FileNotFoundError:
    print("ข้อผิดพลาด: ไม่พบไฟล์ data.txt")
except Exception as e:
    print(f"เกิดข้อผิดพลาดอื่น: {e}")
```

### 2.3 แนวคิดการเขียนโปรแกรมเชิงวัตถุ (OOP)
OOP ช่วยให้โค้ดมีโครงสร้าง จัดการง่าย และนำกลับมาใช้ใหม่ได้ โดยมีแนวคิดหลักคือ **Class** และ **Object**

**ตัวอย่างโค้ด: การสร้าง Class**

```python
class AICoder:
    # Constructor
    def __init__(self, name, language="Python"):
        self.name = name
        self.language = language
        self.level = "Basic"

    # Method
    def code(self, task):
        print(f"{self.name} กำลังเขียนโค้ด {task} ด้วย {self.language}")

    # Method สำหรับการสืบทอด (Inheritance)
    def upgrade_level(self, new_level):
        self.level = new_level
        print(f"{self.name} ได้อัพเกรดเป็นระดับ {self.level}")

# การสร้าง Object (Instance)
coder1 = AICoder("Alice")
coder1.code("Data Preprocessing")

# การสืบทอด (Inheritance)
class DeepLearner(AICoder):
    def __init__(self, name):
        super().__init__(name, language="PyTorch") # เรียกใช้ Constructor ของ Class แม่

    def train_model(self):
        print(f"{self.name} กำลังฝึกโมเดล Deep Learning")

learner1 = DeepLearner("Bob")
learner1.code("Neural Network")
learner1.train_model()
```

### 2.4 การจัดการข้อผิดพลาด (Exception Handling)
การใช้ `try-except-finally` เพื่อจัดการกับข้อผิดพลาดที่อาจเกิดขึ้นระหว่างการรันโปรแกรม

**ตัวอย่างโค้ด:**

```python
def safe_division(numerator, denominator):
    try:
        result = numerator / denominator
    except ZeroDivisionError:
        print("ข้อผิดพลาด: ไม่สามารถหารด้วยศูนย์ได้")
        return None
    except TypeError:
        print("ข้อผิดพลาด: ชนิดข้อมูลไม่ถูกต้อง")
        return None
    else:
        # ทำงานเมื่อไม่มีข้อผิดพลาด
        return result
    finally:
        # ทำงานเสมอ ไม่ว่าจะเกิดข้อผิดพลาดหรือไม่
        print("สิ้นสุดการดำเนินการหาร")

print(safe_division(10, 2))
print(safe_division(10, 0))
```

---

## โมดูล 3: Python for Data Analysis (4 ชั่วโมง)

### 3.1 NumPy: การคำนวณเชิงตัวเลข
**NumPy** (Numerical Python) เป็นไลบรารีหลักสำหรับการทำงานกับ Array มิติเดียวและหลายมิติ ซึ่งเป็นพื้นฐานของข้อมูลในงาน AI

**ตัวอย่างโค้ด: การสร้าง Array และการดำเนินการ**

```python
import numpy as np

# สร้าง Array 1 มิติ
data_list = [1, 2, 3, 4, 5]
np_array = np.array(data_list)
print(f"Array: {np_array}")

# การดำเนินการแบบ Element-wise
new_array = np_array * 2 + 5
print(f"ผลลัพธ์: {new_array}")

# สร้าง Array 2 มิติ (Matrix)
matrix = np.array([[1, 2], [3, 4]])
print(f"Matrix:\n{matrix}")

# การ Indexing และ Slicing
print(f"สมาชิกแถวที่ 1 คอลัมน์ที่ 2: {matrix[0, 1]}") # 2
```

### 3.2 Pandas: การจัดการข้อมูล
**Pandas** เป็นไลบรารีที่ทรงพลังที่สุดสำหรับการจัดการข้อมูล โดยมีโครงสร้างข้อมูลหลักคือ **DataFrame** ซึ่งคล้ายกับตารางในฐานข้อมูลหรือสเปรดชีต

**ตัวอย่างโค้ด: การสร้าง DataFrame และการจัดการข้อมูล**

```python
import pandas as pd

# สร้าง DataFrame จาก Dictionary
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 30, 35, 40],
    'City': ['BKK', 'CNX', 'BKK', 'CNX'],
    'Salary': [50000, 60000, 75000, 90000]
}
df = pd.DataFrame(data)
print("DataFrame เบื้องต้น:")
print(df)

# การกรองข้อมูล (Filtering)
bkk_people = df[df['City'] == 'BKK']
print("\nคนที่อยู่ใน BKK:")
print(bkk_people)

# การเพิ่มคอลัมน์ใหม่
df['Bonus'] = df['Salary'] * 0.1
print("\nDataFrame พร้อม Bonus:")
print(df)
```

### 3.3 Matplotlib & Seaborn: การสร้างภาพข้อมูลเบื้องต้น
การสร้างภาพข้อมูล (Data Visualization) ช่วยให้เข้าใจชุดข้อมูลได้ง่ายขึ้น

**ตัวอย่างโค้ด: การสร้างกราฟแท่ง (Bar Plot)**

```python
import matplotlib.pyplot as plt
import seaborn as sns

# ตั้งค่าสไตล์ของกราฟ
sns.set_style("whitegrid")

# ข้อมูล
cities = df['City'].value_counts().index
counts = df['City'].value_counts().values

# สร้างกราฟแท่ง
plt.figure(figsize=(6, 4))
sns.barplot(x=cities, y=counts)
plt.title('จำนวนพนักงานในแต่ละเมือง')
plt.xlabel('เมือง')
plt.ylabel('จำนวน')
plt.show() # ในสภาพแวดล้อมจริงจะแสดงกราฟ
```

---

## โมดูล 4: Machine Learning Fundamentals with Scikit-learn (4 ชั่วโมง)

### 4.1 แนวคิด Machine Learning และ Data Preprocessing
**Machine Learning (ML)** คือการสอนให้คอมพิวเตอร์เรียนรู้จากข้อมูลโดยไม่ต้องเขียนโปรแกรมอย่างชัดเจน

**ประเภทของ ML:**
1. **Supervised Learning:** เรียนรู้จากข้อมูลที่มีป้ายกำกับ (Labeled Data) เช่น Classification, Regression
2. **Unsupervised Learning:** เรียนรู้จากข้อมูลที่ไม่มีป้ายกำกับ (Unlabeled Data) เช่น Clustering

**Data Preprocessing:** การเตรียมข้อมูลให้พร้อมสำหรับโมเดล ML

| เทคนิค | คำอธิบาย | เครื่องมือใน Scikit-learn |
| :--- | :--- | :--- |
| **Scaling** | ปรับขนาดข้อมูลให้อยู่ในช่วงเดียวกัน (เช่น 0-1) | `MinMaxScaler`, `StandardScaler` |
| **Encoding** | แปลงข้อมูลหมวดหมู่ (Categorical) เป็นตัวเลข | `OneHotEncoder`, `LabelEncoder` |
| **Train-Test Split** | แบ่งข้อมูลเป็นชุดฝึก (Train) และชุดทดสอบ (Test) | `train_test_split` |

### 4.2 การเรียนรู้แบบมีผู้สอน (Supervised Learning)
เราจะใช้ไลบรารี **Scikit-learn** ซึ่งเป็นมาตรฐานสำหรับการทำ ML ใน Python

**ตัวอย่างโค้ด: Linear Regression (การถดถอยเชิงเส้น)**

```python
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import numpy as np

# 1. เตรียมข้อมูล (สมมติข้อมูล)
X = np.array([1, 2, 3, 4, 5]).reshape(-1, 1) # ชั่วโมงการทำงาน
y = np.array([2, 4, 5, 4, 5]) # ผลผลิต

# 2. แบ่งข้อมูล
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# 3. สร้างและฝึกโมเดล
model = LinearRegression()
model.fit(X_train, y_train)

# 4. ทำนายและประเมินผล
y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
print(f"ค่า Mean Squared Error: {mse:.2f}")
```

### 4.3 การประเมินผลโมเดล (Model Evaluation)
การเลือกเมตริกที่เหมาะสมเป็นสิ่งสำคัญในการวัดประสิทธิภาพของโมเดล

| งาน | เมตริกที่ใช้บ่อย | คำอธิบาย |
| :--- | :--- | :--- |
| **Classification** | Accuracy, Precision, Recall, F1-Score, Confusion Matrix | วัดความถูกต้องของการจำแนกประเภท |
| **Regression** | MSE (Mean Squared Error), R-squared | วัดความคลาดเคลื่อนของการทำนายค่าตัวเลข |

**ตัวอย่างโค้ด: Confusion Matrix (สำหรับ Classification)**

```python
from sklearn.metrics import confusion_matrix, accuracy_score
from sklearn.tree import DecisionTreeClassifier

# สมมติข้อมูล (X_train, y_train, X_test, y_test)
# ... (โค้ดการเตรียมข้อมูล) ...

# ฝึกโมเดล Decision Tree
clf = DecisionTreeClassifier(random_state=42)
clf.fit(X_train, y_train)
y_pred_clf = clf.predict(X_test)

# ประเมินผล
accuracy = accuracy_score(y_test, y_pred_clf)
conf_matrix = confusion_matrix(y_test, y_pred_clf)

print(f"ความแม่นยำ (Accuracy): {accuracy:.2f}")
print("Confusion Matrix:\n", conf_matrix)
```

---

## โมดูล 5: Introduction to Deep Learning (4 ชั่วโมง)

### 5.1 โครงข่ายประสาทเทียม (Neural Networks)
**Deep Learning** คือส่วนหนึ่งของ Machine Learning ที่ใช้โครงข่ายประสาทเทียมที่มีหลายชั้น (Deep Neural Networks)

**ส่วนประกอบหลัก:**
- **Input Layer:** รับข้อมูลเข้า
- **Hidden Layers:** ทำการคำนวณที่ซับซ้อน
- **Output Layer:** ให้ผลลัพธ์
- **Activation Functions:** ฟังก์ชันที่กำหนดว่าเซลล์ประสาทควรถูกกระตุ้นหรือไม่ (เช่น ReLU, Sigmoid)

### 5.2 แนะนำ PyTorch/TensorFlow
ทั้งสองเป็นเฟรมเวิร์กหลักสำหรับ Deep Learning โดย **PyTorch** มักได้รับความนิยมในหมู่นักวิจัยเนื่องจากความเป็น Pythonic และ Dynamic Graph ในขณะที่ **TensorFlow** (โดยเฉพาะ Keras API) ใช้งานง่ายและเหมาะสำหรับการนำไปใช้งานจริง (Production)

เราจะเน้นที่ **PyTorch** สำหรับการเรียนรู้เชิงปฏิบัติการ

**ตัวอย่างโค้ด: การสร้าง Tensor ใน PyTorch**

```python
import torch

# สร้าง Tensor (คล้ายกับ NumPy Array)
x = torch.tensor([[1.0, 2.0], [3.0, 4.0]])
print(f"Tensor x:\n{x}")

# การดำเนินการ
y = x + 2
print(f"Tensor y (x+2):\n{y}")

# การสร้าง Tensor ที่ต้องการการคำนวณ Gradient (สำหรับ Backpropagation)
z = torch.ones(2, 2, requires_grad=True)
print(f"Tensor z:\n{z}")
```

### 5.3 การจำแนกภาพเบื้องต้น (MNIST Example)
การใช้โครงข่ายประสาทเทียมอย่างง่ายเพื่อจำแนกตัวเลขลายมือ (MNIST Dataset)

**แนวคิดหลัก:**
1. โหลดข้อมูล MNIST
2. สร้างโมเดล Neural Network (ประกอบด้วย Linear Layers และ Activation Functions)
3. กำหนด Loss Function (เช่น CrossEntropyLoss) และ Optimizer (เช่น SGD)
4. วนลูปฝึกโมเดล (Forward Pass, Calculate Loss, Backward Pass, Update Weights)

**ตัวอย่างโค้ด (แนวคิด):**

```python
import torch.nn as nn
import torch.optim as optim

# 1. สร้างโมเดล (สมมติว่ามี 784 input features และ 10 output classes)
class SimpleNN(nn.Module):
    def __init__(self):
        super(SimpleNN, self).__init__()
        self.fc1 = nn.Linear(784, 128) # Fully Connected Layer 1
        self.relu = nn.ReLU()
        self.fc2 = nn.Linear(128, 10)  # Output Layer (10 classes)

    def forward(self, x):
        x = self.fc1(x)
        x = self.relu(x)
        x = self.fc2(x)
        return x

# 2. กำหนด Loss และ Optimizer
model = SimpleNN()
criterion = nn.CrossEntropyLoss()
optimizer = optim.Adam(model.parameters(), lr=0.001)

# 3. ขั้นตอนการฝึก (ย่อ)
# for epoch in range(num_epochs):
#     for images, labels in data_loader:
#         optimizer.zero_grad()
#         outputs = model(images.view(-1, 784))
#         loss = criterion(outputs, labels)
#         loss.backward() # Backpropagation
#         optimizer.step() # Update weights
```

---

## โมดูล 6: AI-Powered Coding & Project Deployment (4 ชั่วโมง)

### 6.1 AI Assistant ในการเขียนโค้ด (AI-Powered Coding)
เครื่องมือ AI เช่น GitHub Copilot, ChatGPT, หรือ Manus AI สามารถช่วยเพิ่มประสิทธิภาพในการเขียนโค้ดได้อย่างมาก

**ประโยชน์หลัก:**
- **Code Generation:** สร้างฟังก์ชันหรือโค้ดบล็อกตามคำสั่งภาษาธรรมชาติ
- **Code Completion:** เติมเต็มโค้ดที่กำลังเขียน
- **Debugging & Testing:** ช่วยค้นหาข้อผิดพลาดและสร้าง Test Case

**แนวทางการใช้งานอย่างมีประสิทธิภาพ:**
1. **ให้บริบทที่ชัดเจน:** AI ทำงานได้ดีที่สุดเมื่อได้รับข้อมูลที่เพียงพอ (เช่น ชื่อฟังก์ชัน, ชนิดข้อมูลที่คาดหวัง)
2. **ตรวจสอบโค้ดเสมอ:** โค้ดที่สร้างโดย AI อาจมีข้อผิดพลาดหรือช่องโหว่ด้านความปลอดภัย
3. **เรียนรู้จากโค้ดที่สร้าง:** ใช้ AI เป็นเครื่องมือในการเรียนรู้ไวยากรณ์และ Best Practice ใหม่ๆ

### 6.2 โครงสร้างโปรเจกต์และการจัดการสภาพแวดล้อม
โปรเจกต์ Python ที่ดีควรมีโครงสร้างที่ชัดเจนและใช้ Virtual Environment

**โครงสร้างโปรเจกต์ที่แนะนำ:**

```
my_ai_project/
├── .venv/              # Virtual Environment
├── data/               # ข้อมูลดิบและข้อมูลที่ประมวลผลแล้ว
├── models/             # โมเดลที่ฝึกแล้ว
├── notebooks/          # Jupyter Notebooks สำหรับ EDA/ทดลอง
├── src/                # โค้ดหลักของแอปพลิเคชัน
│   ├── __init__.py
│   ├── data_loader.py
│   └── model_trainer.py
├── tests/              # Test files
├── requirements.txt    # รายการแพ็กเกจที่ต้องติดตั้ง
└── README.md
```

**การจัดการแพ็กเกจ:** ใช้ `pip freeze > requirements.txt` เพื่อบันทึกรายการแพ็กเกจ

### 6.3 แนวคิดการนำโปรเจกต์ไปใช้งาน (Deployment)
หลังจากสร้างโมเดล AI แล้ว ขั้นตอนต่อไปคือการนำไปใช้งานจริงเพื่อให้ผู้ใช้สามารถเข้าถึงได้

| เครื่องมือ | ลักษณะ | เหมาะสำหรับ |
| :--- | :--- | :--- |
| **FastAPI** | Web Framework ที่รวดเร็ว, สร้าง API Endpoint | การสร้าง API สำหรับโมเดล ML/DL |
| **Streamlit** | ไลบรารีสำหรับสร้าง Web App แบบง่ายด้วย Python เท่านั้น | การสร้าง Dashboard หรือ Demo สำหรับโมเดล |

**ตัวอย่างโค้ด (แนวคิด FastAPI):**

```python
# main.py (ต้องติดตั้ง: pip install fastapi uvicorn)
from fastapi import FastAPI
# สมมติว่ามีฟังก์ชันทำนายผลลัพธ์
# from model_loader import predict_model

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "AI Coder"}

@app.post("/predict")
def predict_data(data: dict):
    # result = predict_model(data)
    return {"prediction": "Sample Result"}

# รันด้วย: uvicorn main:app --reload
```

---

## แบบฝึกหัดและโครงการ (Project)

**โครงการสุดท้าย (Final Project):**
สร้างแอปพลิเคชันจำแนกประเภทดอกไม้ (Iris Dataset) โดยใช้ Scikit-learn และนำเสนอผลลัพธ์ผ่าน Streamlit App อย่างง่าย

**ขั้นตอน:**
1. โหลด Iris Dataset
2. ฝึกโมเดล Classification (เช่น Decision Tree)
3. บันทึกโมเดลที่ฝึกแล้ว
4. สร้างไฟล์ `app.py` ด้วย Streamlit เพื่อรับค่า Input จากผู้ใช้และแสดงผลการทำนาย

---
**หมายเหตุ:** คู่มือนี้เป็นฉบับร่างที่เน้นเนื้อหาและตัวอย่างโค้ด ในขั้นตอนต่อไปจะมีการเพิ่มภาพประกอบและจัดรูปแบบให้สมบูรณ์ยิ่งขึ้น
