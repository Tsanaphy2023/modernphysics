# Module 6: Deployment & AI Coding Assistant - เฉลยแบบฝึกหัดเชิงปฏิบัติการ

---

### แบบฝึกหัดที่ 1: การสร้าง API Endpoint ด้วย FastAPI

**เฉลย:**

```python
# app.py
from fastapi import FastAPI
from pydantic import BaseModel

# 1. สร้าง Instance ของ FastAPI
app = FastAPI()

# กำหนด Schema สำหรับ Input Body
class PredictionInput(BaseModel):
    text: str

# 3. สร้าง API Endpoint GET /health
@app.get("/health")
def health_check():
    return {"status": "ok"}

# 4. สร้าง API Endpoint POST /predict
@app.post("/predict")
def predict(data: PredictionInput):
    # ในสถานการณ์จริง จะมีการโหลดโมเดลและทำนายผลที่นี่
    return {"result": f"Received: {data.text}"}

# 5. คำสั่งรัน Uvicorn Server (ไม่ต้องรันจริง)
# uvicorn app:app --reload --host 0.0.0.0 --port 8000
```

**คำอธิบาย:**
*   `FastAPI()` สร้างแอปพลิเคชัน API หลัก
*   `@app.get` และ `@app.post` ใช้สำหรับกำหนด Route และ HTTP Method
*   `PredictionInput(BaseModel)` ใช้ Pydantic ในการตรวจสอบความถูกต้องของข้อมูล Input ที่เป็น JSON

---

### แบบฝึกหัดที่ 2: การสร้าง Web Application ด้วย Streamlit

**เฉลย:**

```python
# streamlit_app.py
import streamlit as st

# 3. สร้าง Title
st.title("AI Model Deployment Demo")

# 4. สร้าง Text Input
user_input = st.text_input("Enter Text for Prediction")

# 5. สร้างปุ่ม "Predict"
if st.button("Predict"):
    # 6. แสดงผลลัพธ์เมื่อกดปุ่ม
    if user_input:
        st.write(f"Prediction Result: {user_input}")
    else:
        st.write("Please enter some text.")

# คำสั่งรัน Streamlit Server (ไม่ต้องรันจริง)
# streamlit run streamlit_app.py
```

**คำอธิบาย:**
*   Streamlit สร้าง UI Components โดยใช้คำสั่ง Python ตรงไปตรงมา
*   `st.button("Predict")` จะคืนค่า `True` เมื่อผู้ใช้คลิกปุ่ม ทำให้โค้ดภายใน `if` ถูกรัน

---

### แบบฝึกหัดที่ 3: การสร้าง Dockerfile สำหรับ Python Application

**เฉลย:**

```dockerfile
# Dockerfile
# 1. ใช้ Python 3.10 Slim เป็น Base Image
FROM python:3.10-slim

# 2. ตั้งค่า Working Directory
WORKDIR /app

# 3. คัดลอก requirements.txt และติดตั้ง Dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 4. คัดลอกไฟล์ app.py
COPY app.py .

# 5. กำหนด Port ที่จะเปิดเผย
EXPOSE 8000

# 6. กำหนด Command ที่จะรัน Uvicorn Server
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
```

**คำอธิบาย:**
*   `--no-cache-dir` ช่วยลดขนาดของ Docker Image
*   `EXPOSE 8000` เป็นการบอกว่า Container นี้จะใช้ Port 8000
*   `CMD` กำหนดคำสั่งเริ่มต้นเมื่อ Container ถูกรัน

---

### แบบฝึกหัดที่ 4: การใช้ AI Coding Assistant ในการ Refactoring

**เฉลย (โค้ดที่คาดหวังจาก AI Assistant):**

```python
from sklearn.metrics import precision_score, recall_score, f1_score
import numpy as np

def calculate_metrics_sklearn(y_true, y_pred):
    # แปลงเป็น numpy array เพื่อให้เข้ากันได้กับ sklearn
    y_true = np.array(y_true)
    y_pred = np.array(y_pred)
    
    # คำนวณ Precision, Recall, และ F1-score
    precision = precision_score(y_true, y_pred)
    recall = recall_score(y_true, y_pred)
    f1 = f1_score(y_true, y_pred)
    
    return precision, recall, f1

# ตัวอย่างการใช้งาน
y_true = [0, 1, 1, 0, 1, 1]
y_pred = [0, 1, 0, 0, 1, 0]
precision, recall, f1 = calculate_metrics_sklearn(y_true, y_pred)

print(f"Precision: {precision:.2f}")
print(f"Recall: {recall:.2f}")
print(f"F1-Score: {f1:.2f}")
```

**คำอธิบาย:**
*   AI Assistant จะใช้ฟังก์ชันมาตรฐานจาก `sklearn.metrics` ซึ่งเป็นวิธีปฏิบัติที่ดีที่สุด (Best Practice) ในการคำนวณ Metrics สำหรับ Machine Learning

---

### แบบฝึกหัดที่ 5: การออกแบบโครงสร้างโปรเจกต์ AI (Best Practices)

**เฉลย (Directory Tree):**

```
ai-project-name/
├── api/
│   ├── __init__.py
│   ├── main.py          # FastAPI application
│   └── Dockerfile
├── data/
│   ├── raw/
│   └── processed/
├── models/
│   └── best_model.pkl   # Trained model files
├── notebooks/
│   ├── 01_eda.ipynb
│   └── 02_experiment.ipynb
├── src/
│   ├── __init__.py
│   ├── data_processing.py
│   └── model_training.py
├── .gitignore
├── requirements.txt
└── README.md
```

**คำอธิบาย:**
*   **`src`**: เก็บโค้ด Python ที่สามารถนำกลับมาใช้ใหม่ได้ (Reusable Code) เช่น ฟังก์ชัน Data Processing และ Model Training
*   **`api`**: เก็บโค้ดสำหรับการ Deployment โดยเฉพาะ (FastAPI, Dockerfile)
*   **`models`**: เก็บโมเดลที่ผ่านการฝึกฝนแล้ว
*   **`data`**: แยกข้อมูลดิบและข้อมูลที่ประมวลผลแล้ว
*   **`notebooks`**: เก็บ Jupyter Notebooks สำหรับการทดลองและวิเคราะห์เบื้องต้น
*   โครงสร้างนี้ช่วยให้โปรเจกต์มีความเป็นระเบียบและง่ายต่อการจัดการในสภาพแวดล้อม Production (MLOps)
