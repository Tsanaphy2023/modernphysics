# Module 6: Deployment & AI Coding Assistant - แบบฝึกหัดเชิงปฏิบัติการ

## วัตถุประสงค์
เพื่อให้นักเรียนสามารถประยุกต์ใช้เครื่องมือสำหรับการนำโมเดล AI ไปใช้งานจริง (Deployment) และใช้ AI Coding Assistant ในการเพิ่มประสิทธิภาพการทำงาน

---

### แบบฝึกหัดที่ 1: การสร้าง API Endpoint ด้วย FastAPI

**โจทย์:**
1. ติดตั้ง FastAPI และ Uvicorn (หากยังไม่ได้ติดตั้ง)
2. สร้างไฟล์ `app.py`
3. สร้าง API Endpoint ที่เป็น `GET` ชื่อ `/health` ซึ่งคืนค่า JSON `{ "status": "ok" }`
4. สร้าง API Endpoint ที่เป็น `POST` ชื่อ `/predict` ซึ่งรับค่าเป็น JSON Body ที่มีฟิลด์ `text` (string) และคืนค่า JSON `{ "result": "Received: [ค่า text ที่รับมา]" }`
5. รัน Uvicorn Server (ไม่ต้องรันจริง แค่เขียนคำสั่ง)

**แนวคิดที่เกี่ยวข้อง:** `FastAPI`, `uvicorn`, `GET` method, `POST` method, `pydantic.BaseModel` (สำหรับ Body)

---

### แบบฝึกหัดที่ 2: การสร้าง Web Application ด้วย Streamlit

**โจทย์:**
1. ติดตั้ง Streamlit (หากยังไม่ได้ติดตั้ง)
2. สร้างไฟล์ `streamlit_app.py`
3. สร้าง Title ของแอปพลิเคชันเป็น "AI Model Deployment Demo"
4. สร้าง Text Input สำหรับให้ผู้ใช้ป้อนข้อความ (Label: "Enter Text for Prediction")
5. สร้างปุ่ม "Predict"
6. เมื่อผู้ใช้กดปุ่ม ให้แสดงข้อความ "Prediction Result: [ข้อความที่ผู้ใช้ป้อน]" ใต้ปุ่ม

**แนวคิดที่เกี่ยวข้อง:** `streamlit`, `st.title`, `st.text_input`, `st.button`, `st.write`

---

### แบบฝึกหัดที่ 3: การสร้าง Dockerfile สำหรับ Python Application

**โจทย์:**
สมมติว่าคุณมีไฟล์ `app.py` และ `requirements.txt` ที่มี `fastapi`, `uvicorn` อยู่
1. สร้าง `Dockerfile` ที่มีขั้นตอนดังนี้:
    *   ใช้ Python 3.10 Slim เป็น Base Image
    *   ตั้งค่า Working Directory เป็น `/app`
    *   คัดลอก `requirements.txt` และติดตั้ง Dependencies
    *   คัดลอกไฟล์ `app.py`
    *   กำหนด Port ที่จะเปิดเผย (Expose) เป็น 8000
    *   กำหนด Command ที่จะรัน Uvicorn Server (Host: 0.0.0.0, Port: 8000, App: app:app)

**แนวคิดที่เกี่ยวข้อง:** `Dockerfile`, `FROM`, `WORKDIR`, `COPY`, `RUN pip install`, `EXPOSE`, `CMD`

---

### แบบฝึกหัดที่ 4: การใช้ AI Coding Assistant ในการ Refactoring

**โจทย์:**
สมมติว่าคุณกำลังใช้ AI Coding Assistant (เช่น GitHub Copilot หรือ Gemini Code Assist)
**โค้ดเดิม:**
```python
def calculate_metrics(y_true, y_pred):
    tp = sum((y_true == 1) & (y_pred == 1))
    fp = sum((y_true == 0) & (y_pred == 1))
    fn = sum((y_true == 1) & (y_pred == 0))
    
    precision = tp / (tp + fp)
    recall = tp / (tp + fn)
    
    return precision, recall
```
**คำสั่งที่คุณจะป้อนให้ AI Assistant:**
"Refactor the following Python function to use `sklearn.metrics` for calculating precision and recall, and also add F1-score calculation."

**คำตอบที่คาดหวังจาก AI Assistant (เฉลย):**
ให้เขียนโค้ด Python ที่ใช้ `sklearn.metrics` เพื่อคำนวณ Precision, Recall, และ F1-score

**แนวคิดที่เกี่ยวข้อง:** AI-assisted Refactoring, `sklearn.metrics.precision_score`, `sklearn.metrics.recall_score`, `sklearn.metrics.f1_score`

---

### แบบฝึกหัดที่ 5: การออกแบบโครงสร้างโปรเจกต์ AI (Best Practices)

**โจทย์:**
จงออกแบบโครงสร้าง Directory ที่เหมาะสมสำหรับโปรเจกต์ Machine Learning ที่มีทั้งส่วน Training, Deployment (FastAPI), และ Notebooks สำหรับการทดลอง โดยให้มี Directory หลัก 5 ส่วนดังนี้:
1.  **`src`** (Source Code)
2.  **`models`** (Trained Models)
3.  **`data`** (Raw and Processed Data)
4.  **`notebooks`** (Jupyter Notebooks)
5.  **`api`** (Deployment Code - FastAPI)

**คำตอบที่คาดหวัง:**
ให้เขียนโครงสร้าง Directory Tree ที่แสดงถึงการจัดระเบียบไฟล์เหล่านี้

**แนวคิดที่เกี่ยวข้อง:** MLOps, Project Structure Best Practices, Separation of Concerns
