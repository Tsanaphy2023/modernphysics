# โมดูล 6: AI-Powered Coding & Project Deployment (ขยาย)

## 6.1 AI Assistant ในการเขียนโค้ด

### 6.1.1 Advanced Prompt Engineering สำหรับ AI Coding Assistant

การใช้ AI Coding Assistant (เช่น GitHub Copilot, Code Llama) อย่างมีประสิทธิภาพต้องอาศัยทักษะ **Prompt Engineering** เพื่อให้ได้โค้ดที่มีคุณภาพและตรงตามความต้องการ

**เทคนิค Prompt Engineering ขั้นสูง:**

| เทคนิค | คำอธิบาย | ตัวอย่าง Prompt |
| :--- | :--- | :--- |
| **Contextual Prompting** | ให้บริบทที่ชัดเจนเกี่ยวกับภาษา, ไลบรารี, และวัตถุประสงค์ของโค้ด | "Using Python and Pandas, write a function `clean_data(df)` that handles missing values by median imputation and removes duplicate rows." |
| **Role-Playing** | กำหนดบทบาทให้ AI เป็นผู้เชี่ยวชาญเฉพาะทาง | "Act as a Senior MLOps Engineer. Write a Dockerfile for a Python FastAPI application that serves a PyTorch model." |
| **Refactoring/Optimization** | ขอให้ AI ปรับปรุงโค้ดที่มีอยู่ | "Refactor the following Python function to use List Comprehension instead of a for loop, and add type hinting." |
| **Test-Driven Prompting** | ขอให้ AI สร้าง Test Case ก่อนหรือพร้อมกับโค้ด | "Write a Python function `calculate_accuracy(y_true, y_pred)` and include a `unittest` test case for it." |

## 6.2 โครงสร้างโปรเจกต์

### 6.2.1 Containerization: การใช้ Docker สำหรับแอปพลิเคชัน ML

**Docker** เป็นเครื่องมือสำคัญใน MLOps ที่ช่วยให้เราสามารถบรรจุ (Package) แอปพลิเคชันและสภาพแวดล้อมทั้งหมดไว้ใน **Container** เดียวกัน ทำให้สามารถนำไปใช้งาน (Deploy) บนเครื่องใดก็ได้โดยไม่มีปัญหาเรื่องความเข้ากันได้ของสภาพแวดล้อม

**ส่วนประกอบหลักของ Docker:**
1.  **Dockerfile:** ไฟล์ข้อความที่ระบุขั้นตอนการสร้าง Image
2.  **Image:** แม่แบบ (Template) ที่ใช้สร้าง Container
3.  **Container:** Instance ที่ทำงานจริงของ Image

**ตัวอย่าง Dockerfile สำหรับ FastAPI ML Application:**

```dockerfile
# 1. ใช้ Base Image ที่มี Python
FROM python:3.10-slim

# 2. กำหนด Working Directory ภายใน Container
WORKDIR /app

# 3. คัดลอกไฟล์ requirements.txt และติดตั้ง Dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 4. คัดลอกโค้ดแอปพลิเคชันทั้งหมด
COPY . .

# 5. กำหนด Environment Variable (ถ้ามี)
ENV PORT 8000

# 6. เปิด Port ที่แอปพลิเคชันจะรัน
EXPOSE 8000

# 7. คำสั่งเริ่มต้นเมื่อ Container ถูกรัน (ใช้ Uvicorn สำหรับ FastAPI)
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
```

**คำสั่ง Docker พื้นฐาน:**
*   `docker build -t my-ml-app .`: สร้าง Image
*   `docker run -d -p 80:8000 my-ml-app`: รัน Container
*   `docker ps`: ดู Container ที่กำลังทำงาน

## 6.3 แนวคิดการนำโปรเจกต์ไปใช้งาน (Deployment)

### 6.3.1 FastAPI: การสร้าง API Endpoint ที่ซับซ้อน

**FastAPI** เป็น Web Framework ที่รวดเร็วสำหรับการสร้าง API ด้วย Python โดยใช้ **Type Hinting** เพื่อกำหนดโครงสร้างข้อมูลและสร้างเอกสาร API (Swagger UI/ReDoc) โดยอัตโนมัติ

**การสร้าง API Endpoint สำหรับ Model Prediction:**

```python
from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np

# 1. โหลดโมเดลที่ฝึกมาแล้ว (สมมติว่ามีไฟล์ model.pkl)
# model = joblib.load("model.pkl")

app = FastAPI(title="ML Prediction API")

# 2. กำหนดโครงสร้างข้อมูล Input ด้วย Pydantic
class PredictionInput(BaseModel):
    feature_1: float
    feature_2: float
    feature_3: float

# 3. กำหนด API Endpoint (POST Method)
@app.post("/predict")
def predict_model(data: PredictionInput):
    # แปลง Pydantic Model เป็น NumPy Array
    input_data = np.array([
        data.feature_1,
        data.feature_2,
        data.feature_3
    ]).reshape(1, -1)

    # ทำนายผล (สมมติว่าโมเดลถูกโหลดแล้ว)
    # prediction = model.predict(input_data)[0]
    prediction = 42.0 # ค่าสมมติ

    return {"prediction": prediction, "status": "success"}

# รันด้วย Uvicorn: uvicorn main:app --reload
```

**การจัดการ Path/Query Parameters:**

```python
# Path Parameter (ส่วนหนึ่งของ URL)
@app.get("/items/{item_id}")
def read_item(item_id: int):
    return {"item_id": item_id}

# Query Parameter (หลังเครื่องหมาย ?)
@app.get("/search")
def search_items(query: str, limit: int = 10):
    return {"query": query, "limit": limit}
```

### 6.3.2 Streamlit: การสร้าง Interactive Dashboard ที่เชื่อมต่อกับโมเดล ML

**Streamlit** เป็นไลบรารีที่ช่วยให้ Data Scientist สามารถสร้าง Web Application หรือ Dashboard สำหรับแสดงผลโมเดล ML ได้อย่างรวดเร็ว โดยไม่ต้องมีความรู้ด้าน Web Development มากนัก

**ตัวอย่าง: Streamlit Dashboard สำหรับ Input ข้อมูล**

```python
import streamlit as st
# import joblib
# import numpy as np

# model = joblib.load("model.pkl") # โหลดโมเดล

st.title("ML Model Interactive Dashboard")
st.write("กรุณากรอกค่าคุณลักษณะเพื่อรับผลการทำนาย")

# 1. สร้าง Input Widgets
feature_1 = st.slider("Feature 1 (ความยาว)", 0.0, 10.0, 5.0)
feature_2 = st.number_input("Feature 2 (ความกว้าง)", min_value=0.0, max_value=10.0, value=5.0)

# 2. ปุ่มทำนาย
if st.button("ทำนายผล"):
    # 3. เตรียมข้อมูลสำหรับโมเดล
    input_data = np.array([[feature_1, feature_2]])

    # 4. ทำนายผล
    # prediction = model.predict(input_data)[0]
    prediction = feature_1 * 2 + feature_2 * 0.5 # สูตรสมมติ

    # 5. แสดงผลลัพธ์
    st.success(f"ผลการทำนาย: {prediction:.2f}")

# รันด้วย Streamlit: streamlit run app.py
```

## 6.4 MLOps Concepts: การติดตามโมเดล (Model Monitoring) และ CI/CD เบื้องต้น

**MLOps (Machine Learning Operations)** คือชุดของแนวทางปฏิบัติที่รวมเอา Machine Learning, DevOps, และ Data Engineering เข้าด้วยกัน เพื่อนำโมเดล ML ไปใช้งานจริงและดูแลรักษาอย่างมีประสิทธิภาพ

**1. Model Monitoring:**
การติดตามประสิทธิภาพของโมเดลที่ถูกนำไปใช้งานจริง เพื่อตรวจจับปัญหาที่อาจเกิดขึ้น

| ปัญหา | คำอธิบาย | การตรวจจับ |
| :--- | :--- | :--- |
| **Data Drift** | ลักษณะของข้อมูล Input เปลี่ยนไปจากข้อมูลที่ใช้ฝึกโมเดล | เปรียบเทียบสถิติ (Mean, Variance) ของข้อมูล Input ใน Production กับ Training Data |
| **Model Drift** | ประสิทธิภาพของโมเดลลดลงเมื่อเวลาผ่านไป | ติดตามเมตริก (Accuracy, F1-Score) บนข้อมูลจริงที่มี Label |

**2. CI/CD (Continuous Integration/Continuous Delivery) เบื้องต้น:**
การทำให้กระบวนการสร้าง, ทดสอบ, และนำไปใช้งานเป็นไปโดยอัตโนมัติ

*   **CI (Continuous Integration):** ทุกครั้งที่มีการเปลี่ยนแปลงโค้ด (เช่น Push ไปยัง Git) ระบบจะทำการทดสอบ (Unit Test, Integration Test) และสร้าง Artifact (เช่น Docker Image) โดยอัตโนมัติ
*   **CD (Continuous Delivery):** Artifact ที่ผ่านการทดสอบจะถูกนำไปใช้งานในสภาพแวดล้อม Staging หรือ Production โดยอัตโนมัติหรือกึ่งอัตโนมัติ

## 6.5 แบบฝึกหัดและเฉลย (โมดูล 6)

**แบบฝึกหัด 6.1: FastAPI Pydantic Model**
จงสร้าง Pydantic Model ชื่อ `User` ที่มี 3 Fields: `name` (str), `age` (int), และ `is_active` (bool, ค่าเริ่มต้นเป็น True)

**แบบฝึกหัด 6.2: Dockerfile**
จงเขียน Dockerfile ที่ใช้ Python 3.9-slim, ติดตั้งไลบรารี `requests` และ `pandas`, และรันไฟล์ `script.py` เป็นคำสั่งหลัก

**เฉลย 6.1:**
```python
from pydantic import BaseModel

class User(BaseModel):
    name: str
    age: int
    is_active: bool = True

# ตัวอย่างการใช้งาน
user_data = User(name="Alex", age=30)
print(user_data.model_dump())
# {'name': 'Alex', 'age': 30, 'is_active': True}
```

**เฉลย 6.2:**
```dockerfile
FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY script.py .
CMD ["python", "script.py"]
```
(โดยที่ `requirements.txt` มี `requests` และ `pandas`)
---
**หมายเหตุ:** เนื้อหาส่วนนี้เป็นส่วนขยายของโมดูล 6 ซึ่งจะถูกนำไปรวมกับเนื้อหาโมดูลอื่น ๆ ที่ขยายแล้ว เพื่อให้ได้คู่มือฉบับสมบูรณ์ 200-300 หน้า
