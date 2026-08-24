# เอกสารประกอบการอบรมเพิ่มเติม: เวิร์กชอปการเขียนโปรแกรม AI ด้วย Python (ฉบับวิชาการ)

**ผู้จัดทำ:** Manus AI  
**ขอบเขต:** ชุดแบบทดสอบขั้นสูง, แบบฝึกหัดเขียนโค้ดเชิงปฏิบัติการพร้อมเฉลย, และสคริปต์บรรยายสไลด์นำเสนอ

---

## 1. ชุดแบบทดสอบขั้นสูง (Advanced Quiz: PyTorch & FastAPI Deployment)

ชุดแบบทดสอบนี้ออกแบบมาเพื่อทดสอบความเข้าใจเชิงลึกในระดับเทคนิคขั้นสูง สำหรับผู้เข้าร่วมอบรมที่ต้องการวัดความเชี่ยวชาญในการพัฒนาโมเดล Deep Learning ด้วย PyTorch และการนำโมเดลไปใช้งานจริงด้วย FastAPI

### คำถามปรนัย (Multiple-Choice Questions)

1. **ใน PyTorch หากต้องการหยุดการคำนวณ Gradient (Autograd) สำหรับพารามิเตอร์บางตัวระหว่างการประเมินผล (Evaluation) เราควรใช้แนวทางใดเพื่อให้มีประสิทธิภาพสูงสุด?**
   * ก. เรียกใช้ `model.zero_grad()` ซ้ำๆ
   * ข. ใช้บริบทจัดการ `torch.no_grad()` หรือกำหนด `param.requires_grad = False`
   * ค. แปลง Tensor เป็น NumPy array โดยใช้ `.numpy()` เท่านั้น
   * ง. ใช้ฟังก์ชัน `torch.detach_grad()` บนทุก Tensor

2. **ข้อใดคือประโยชน์หลักของการใช้ Dependency Injection ใน FastAPI สำหรับการโหลดโมเดล AI ในระบบ Production?**
   * ก. ช่วยลดขนาดของไฟล์โค้ด Python
   * ข. ทำให้สามารถแชร์อินสแตนซ์ของโมเดลที่โหลดไว้แล้ว (Singleton) ข้าม Requests ได้อย่างมีประสิทธิภาพโดยไม่ต้องโหลดโมเดลใหม่ทุกครั้ง
   * ค. บังคับให้ใช้เฉพาะ Pydantic v1 เท่านั้น
   * ง. ช่วยเร่งความเร็วในการประมวลผลของ CPU บนระบบ Linux

3. **เมื่อสร้าง Custom Dataset ใน PyTorch เราจะต้องสืบทอด (Inherit) จากคลาสใด และต้องโอเวอร์ライド (Override) เมธอดใดบ้าง?**
   * ก. สืบทอดจาก `torch.nn.Module` และโอเวอร์ライド `forward()`
   * H. สืบทอดจาก `torch.utils.data.Dataset` และโอเวอร์ライド `__len__()` และ `__getitem__()`
   * ค. สืบทอดจาก `torch.utils.data.DataLoader` และโอเวอร์ライド `__iter__()`
   * ง. สืบทอดจาก `torch.optim.Optimizer` และโอเวอร์ライド `step()`

4. **พฤติกรรมของ FastAPI เมื่อรับคำขอ (Request) ที่มีข้อมูล JSON ไม่ตรงตาม Pydantic Model ที่กำหนดคืออะไร?**
   * ก. ละเลยข้อมูลที่ไม่ตรงและดำเนินการต่อ
   * ข. ส่งคืนสถานะ HTTP 400 Bad Request พร้อมรายละเอียดข้อผิดพลาด (Validation Error) โดยอัตโนมัติ
   * ค. แปลงข้อมูลให้อัตโนมัติ (Type Coercion) ทุกกรณีโดยไม่มีข้อยกเว้น
   * ง. ส่งคืนสถานะ HTTP 500 Internal Server Error

5. **ในสถาปัตยกรรม Transformer กลไกใดที่ช่วยให้โมเดลสามารถให้ความสำคัญกับส่วนต่างๆ ของประโยคอินพุตได้พร้อมกันอย่างมีประสิทธิภาพ?**
   * ก. Recurrent Hidden State
   * ข. Convolutional Kernel Pooling
   * ค. Self-Attention Mechanism
   * ง. Max-Pooling Layer

### เฉลยแบบทดสอบขั้นสูง
1. **ข** (`torch.no_grad()` ช่วยปิดการเก็บบันทึกประวัติการคำนวณกราฟ ช่วยประหยัดหน่วยความจำและเพิ่มความเร็วในการ Inference)
2. **ข** (Dependency Injection ช่วยให้การจัดการทรัพยากร เช่น การโหลดโมเดลขนาดใหญ่ ทำได้อย่างมีประสิทธิภาพและใช้ซ้ำได้)
3. **ข** (`Dataset` ต้องมี `__len__` เพื่อบอกขนาดข้อมูล และ `__getitem__` เพื่อดึงข้อมูลทีละตัวอย่างตาม Index)
4. **ข** (FastAPI ตรวจสอบข้อมูลผ่าน Pydantic และจัดการ Validation Error เป็น HTTP 400 ทันที)
5. **ค** (Self-Attention ช่วยคำนวณความสัมพันธ์ระหว่างคำทุกคู่ในประโยคได้พร้อมกันในขั้นตอนเดียว)

---

## 2. แบบฝึกหัดเขียนโค้ดเชิงปฏิบัติการพร้อมเฉลย (Comprehensive Coding Assignment)

### โจทย์ปัญหา: ระบบทำนายราคาบ้านอัจฉริยะ (Smart Housing Price Prediction Pipeline)

**วัตถุประสงค์:** พัฒนาไปป์ไลน์ตั้งแต่การจัดการข้อมูลด้วย OOP และ Pydantic, การสร้างโมเดล Deep Learning ด้วย PyTorch, จนถึงการสร้าง RESTful API ด้วย FastAPI

#### ส่วนที่ 1: การกำหนดโครงสร้างข้อมูลด้วย Pydantic และ OOP
จงสร้าง Pydantic Model สำหรับตรวจสอบความถูกต้องของข้อมูลบ้าน (House Features) และคลาส `HousingModelManager` ที่ใช้ห่อหุ้ม (Encapsulate) โมเดล PyTorch

```python
from pydantic import BaseModel, Field, field_validator
import torch
import torch.nn as nn

# 1. Pydantic Model สำหรับ Data Validation
class HouseInput(BaseModel):
    rooms: int = Field(..., gt=0, description="จำนวนห้องนอน ต้องมากกว่า 0")
    area_sqm: float = Field(..., gt=10.0, description="พื้นที่ตารางเมตร ต้องมากกว่า 10")
    location_score: float = Field(..., ge=1.0, le=10.0, description="คะแนนทำเล ระหว่าง 1-10")

    @field_validator('area_sqm')
    def validate_area(cls, v):
        if v > 10000:
            raise ValueError("พื้นที่บ้านใหญ่เกินความเป็นจริง")
        return v

# 2. PyTorch Neural Network Model
class PricePredictionNN(nn.Module):
    def __init__(self):
        super(PricePredictionNN, self).__init__()
        self.layer1 = nn.Linear(3, 16)
        self.relu = nn.ReLU()
        self.layer2 = nn.Linear(16, 1)

    def forward(self, x):
        x = self.relu(self.layer1(x))
        x = self.layer2(x)
        return x
```

#### ส่วนที่ 2: การสร้าง FastAPI Service
จงสร้าง FastAPI application ที่รับข้อมูลผ่าน Pydantic Model และทำการทำนายราคาโดยเรียกใช้โมเดล PyTorch ที่สร้างขึ้น

```python
from fastapi import FastAPI, HTTPException
import torch

app = FastAPI(title="Smart Housing API", version="1.0")

# โหลดโมเดล (จำลองการเตรียมโมเดลใน Production)
model = PricePredictionNN()
model.eval()

@app.post("/predict")
async def predict_price(house: HouseInput):
    try:
        # แปลงข้อมูลอินพุตเป็น PyTorch Tensor
        input_data = torch.tensor([[house.rooms, house.area_sqm, house.location_score]], dtype=torch.float32)
        
        with torch.no_grad():
            prediction = model(input_data)
            
        predicted_price = prediction.item() * 100000  # สมมติสูตรแปลงสเกลราคา
        
        return {
            "status": "success",
            "input_features": house.dict(),
            "predicted_price_thb": round(predicted_price, 2)
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
```

---

## 3. สคริปต์บรรยายสไลด์นำเสนอ (Presentation Script in Thai)

สคริปต์นี้จัดทำขึ้นสำหรับวิทยากรหรือผู้บรรยาย เพื่อใช้ประกอบการนำเสนอสไลด์ทั้ง 12 หน้า โดยเน้นน้ำเสียงที่เป็นทางการ เชิงวิชาการ และเข้าใจง่าย

*   **สไลด์ 1: หน้าปก (Title Slide)**
    *   **สคริปต์บรรยาย:** "สวัสดีครับ/ค่ะ ทุกท่าน ยินดีต้อนรับเข้าสู่การบรรยายพิเศษในโครงการ **เวิร์กชอปการเขียนโปรแกรม AI ด้วย Python (ฉบับวิชาการ)** จัดทำโดย Manus AI วันนี้เราจะมาเจาะลึกตั้งแต่รากฐานการเขียนโปรแกรมขั้นสูง ไปจนถึงการประยุกต์ใช้งานจริงในระดับอุตสาหกรรมครับ"

*   **สไลด์ 2: บทคัดย่อและบทนำสู่ AI สมัยใหม่ (Abstract & Introduction)**
    *   **สคริปต์บรรยาย:** "ในสไลด์นี้เราจะเห็นภาพรวมของหลักสูตร ซึ่งออกแบบมาตามมาตรฐานวิชาการระดับอุดมศึกษา เพื่อให้ผู้เรียนมีความเข้าใจทั้งในส่วนของทฤษฎีเบื้องหลังอัลกอริทึม และทักษะการปฏิบัติงานจริงผ่านเครื่องมือสมัยใหม่"

*   **สไลด์ 3: การวิเคราะห์โครงสร้างข้อมูล (Big O Analysis)**
    *   **สคริปต์บรรยาย:** "หัวใจสำคัญของการเขียนโค้ดที่มีประสิทธิภาพคือความเข้าใจเรื่อง Big O Notation ครับ การเลือกโครงสร้างข้อมูลระหว่าง List, Tuple, Dictionary หรือ Set ส่งผลอย่างมากต่อ Time Complexity เมื่อชุดข้อมูลในระบบ AI ของเรามีขนาดใหญ่ขึ้นในระดับ Big Data"

*   **สไลด์ 4: สี่เสาหลักของ OOP สำหรับวิศวกรรม AI (The Four Pillars of OOP)**
    *   **สคริปต์บรรยาย:** "การสร้างสถาปัตยกรรมซอฟต์แวร์ AI ที่ดีต้องอาศัยหลักการ OOP ทั้ง 4 ประการ ได้แก่ Encapsulation เพื่อซ่อนความซับซ้อนของโมเดล, Inheritance เพื่อขยายความสามารถ, Polymorphism เพื่อสร้าง Pipeline ที่ยืดหยุ่น, และ Abstraction ผ่าน ABCs เพื่อกำหนดมาตรฐานที่ชัดเจน"

*   **สไลด์ 5: Magic Methods & Modern Data Management**
    *   **สคริปต์บรรยาย:** "นอกจาก OOP ปกติแล้ว Python ยังมี Magic Methods เช่น `__call__` ที่ช่วยให้เราเรียกใช้งานคลาสโมเดลได้เหมือนฟังก์ชัน รวมถึงการใช้ Dataclasses และ Pydantic เพื่อตรวจสอบความถูกต้องของข้อมูล Configuration ในระบบ AI ได้อย่างแม่นยำ"

*   **สไลด์ 6: วิทยาการข้อมูลด้วย NumPy และ Pandas**
    *   **สคริปต์บรรยาย:** "ในส่วนของการจัดการข้อมูลเชิงวิทยาศาสตร์ NumPy มอบประสิทธิภาพผ่าน N-dimensional Arrays และ Vectorization ส่วน Pandas ช่วยให้เราทำ Exploratory Data Analysis และ Data Cleaning ได้อย่างรวดเร็วผ่าน DataFrames"

*   **สไลด์ 7: กระบวนการทำงานของ Machine Learning (Scikit-learn)**
    *   **สคริปต์บรรยาย:** "กระบวนการทำงานของ Machine Learning ตั้งแต่การเก็บรวบรวมข้อมูล, Preprocessing, Model Training จนถึง Evaluation มีความสำคัญมาก โดย Scikit-learn ได้ออกแบบ API ให้มีความสอดคล้องผ่านเมธอด `.fit()`, `.transform()`, และ `.predict()`"

*   **สไลด์ 8: Deep Learning และ Neural Networks ด้วย PyTorch**
    *   **สคริปต์บรรยาย:** "เมื่อก้าวสู่ Deep Learning PyTorch กลายเป็นเครื่องมือหลักที่เราเลือกใช้ ด้วยระบบ Tensors ที่รันบน GPU, ระบบ Autograd สำหรับคำนวณอนุพันธ์อัตโนมัติ และโครงสร้าง `nn.Module` ที่ยืดหยุ่นสูง"

*   **สไลด์ 9: Generative AI และอนาคตของ Transformers**
    *   **สคริปต์บรรยาย:** "เรากำลังอยู่ในยุคทองของ Generative AI และ Large Language Models สถาปัตยกรรม Transformer ที่มีกลไก Self-Attention ช่วยให้โมเดลสามารถประมวลผลภาษาธรรมชาติและสร้างเนื้อหาได้อย่างทรงพลัง"

*   **สไลด์ 10: การนำโมเดลไปใช้งานจริงด้วย FastAPI และ Docker**
    *   **สคริปต์บรรยาย:** "โมเดลที่ดีต้องสามารถนำไปใช้งานจริงได้ FastAPI ช่วยให้เราสร้าง RESTful API ที่มีความเร็วสูงพร้อมเอกสารประกอบอัตโนมัติ และเมื่อนำไปห่อหุ้มด้วย Docker Container เราก็จะได้ระบบที่มีความเสถียรและพกพาสะดวก"

*   **สไลด์ 11: ผู้ช่วยเขียนโค้ด AI และ AI Agents สมัยใหม่**
    *   **สคริปต์บรรยาย:** "ในปัจจุบัน นักพัฒนาสามารถเพิ่มผลผลิตผ่าน AI Coding Assistants และก้าวไปอีกขั้นด้วยแนวคิด AI Agents ที่สามารถวางแผน ดำเนินการ และปรับเปลี่ยนเวิร์กโฟลว์การพัฒนาซอฟต์แวร์ได้แบบอัตโนมัติ"

*   **สไลด์ 12: สรุปบทเรียนและช่วงถาม-ตอบ (Summary & Q&A)**
    *   **สคริปต์บรรยาย:** "สรุปแล้ว หลักสูตรนี้ได้ปูพื้นฐานตั้งแต่รากฐาน Python, OOP, Data Science, Deep Learning ไปจนถึง MLOps หวังว่าทุกท่านจะได้รับความรู้และสามารถนำไปต่อยอดในการพัฒนาโปรเจกต์ AI ของตนเองได้ครับ ขอบคุณมากครับ และเชิญซักถามข้อสงสัยได้เลยครับ"

---
