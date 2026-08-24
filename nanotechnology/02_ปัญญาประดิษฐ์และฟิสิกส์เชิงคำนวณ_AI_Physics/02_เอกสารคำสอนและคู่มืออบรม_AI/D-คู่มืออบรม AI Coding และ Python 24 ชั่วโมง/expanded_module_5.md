# โมดูล 5: Introduction to Deep Learning (ขยาย)

## 5.1 โครงข่ายประสาทเทียม (Neural Networks)

### 5.1.1 การทำงานของ Backpropagation และ Gradient Descent อย่างละเอียด

**Deep Learning** คือการเรียนรู้ของโครงข่ายประสาทเทียม (Neural Networks) ที่มีหลายชั้น (Layers) หัวใจสำคัญของการฝึกโมเดลเหล่านี้คือกลไกการปรับน้ำหนัก (Weights) และไบแอส (Biases) ซึ่งประกอบด้วย **Gradient Descent** และ **Backpropagation**

**1. Gradient Descent (การลดระดับความชัน):**
เป็นอัลกอริทึมที่ใช้ในการหาค่าต่ำสุดของฟังก์ชันต้นทุน (Loss Function) โดยการปรับพารามิเตอร์ของโมเดลไปในทิศทางตรงกันข้ามกับความชัน (Gradient) ของฟังก์ชันต้นทุน

**สูตรการปรับน้ำหนัก (Weight Update):**
$$W_{new} = W_{old} - \eta \frac{\partial L}{\partial W}$$
โดยที่:
*   $W_{new}$ คือ น้ำหนักใหม่
*   $W_{old}$ คือ น้ำหนักเดิม
*   $\eta$ (eta) คือ **Learning Rate** (อัตราการเรียนรู้) ซึ่งกำหนดขนาดของขั้นตอนในการปรับน้ำหนัก
*   $\frac{\partial L}{\partial W}$ คือ Gradient (ความชัน) ของ Loss Function ($L$) เทียบกับน้ำหนัก ($W$)

**2. Backpropagation (การแพร่กระจายย้อนกลับ):**
เป็นกลไกที่ใช้ในการคำนวณ Gradient ($\frac{\partial L}{\partial W}$) อย่างมีประสิทธิภาพ โดยการใช้กฎลูกโซ่ (Chain Rule) ของแคลคูลัส เพื่อส่งผ่านความผิดพลาด (Error) จากชั้นสุดท้าย (Output Layer) ย้อนกลับไปยังชั้นแรก (Input Layer)

**ขั้นตอนโดยสรุป:**
1.  **Forward Pass:** ข้อมูลถูกส่งผ่านโครงข่ายประสาทเทียมจาก Input ไป Output เพื่อคำนวณค่าทำนาย ($\hat{y}$) และ Loss ($L$)
2.  **Backward Pass (Backpropagation):** คำนวณ Gradient ของ Loss เทียบกับพารามิเตอร์ทั้งหมดในแต่ละชั้น โดยเริ่มจากชั้น Output ย้อนกลับไป
3.  **Parameter Update:** ใช้ Gradient Descent เพื่อปรับปรุงพารามิเตอร์

## 5.2 แนะนำ PyTorch

### 5.2.1 PyTorch DataLoaders และ Datasets: การจัดการข้อมูลขนาดใหญ่

PyTorch ใช้แนวคิดของ **Dataset** และ **DataLoader** เพื่อจัดการข้อมูลอย่างมีประสิทธิภาพ โดยเฉพาะอย่างยิ่งเมื่อต้องทำงานกับชุดข้อมูลขนาดใหญ่

**1. Dataset:**
เป็น Class ที่ใช้ในการโหลดและจัดเก็บข้อมูล โดยต้องสืบทอด (Inherit) มาจาก `torch.utils.data.Dataset` และต้องมี 2 เมธอดหลัก:
*   `__len__`: คืนค่าจำนวนตัวอย่างทั้งหมดในชุดข้อมูล
*   `__getitem__`: คืนค่าตัวอย่างข้อมูลและป้ายกำกับ (Label) ที่ Index ที่กำหนด

**2. DataLoader:**
เป็น Iterator ที่ห่อหุ้ม Dataset ไว้ ทำหน้าที่ในการ:
*   **Batching:** แบ่งข้อมูลออกเป็นชุดย่อย (Mini-batches) เพื่อป้อนเข้าสู่โมเดล
*   **Shuffling:** สุ่มลำดับข้อมูลในแต่ละ Epoch
*   **Parallel Loading:** โหลดข้อมูลแบบขนานโดยใช้หลาย Process (Workers)

**ตัวอย่าง: การสร้าง Custom Dataset และ DataLoader**

```python
import torch
from torch.utils.data import Dataset, DataLoader
import numpy as np

# 1. Custom Dataset
class CustomDataset(Dataset):
    def __init__(self, data, labels):
        self.data = torch.tensor(data, dtype=torch.float32)
        self.labels = torch.tensor(labels, dtype=torch.long)

    def __len__(self):
        return len(self.labels)

    def __getitem__(self, idx):
        return self.data[idx], self.labels[idx]

# ข้อมูลสมมติ
X = np.random.rand(100, 10) # 100 ตัวอย่าง, 10 Features
y = np.random.randint(0, 2, 100) # 100 Labels (0 หรือ 1)

# 2. สร้าง Dataset และ DataLoader
dataset = CustomDataset(X, y)
dataloader = DataLoader(dataset, batch_size=16, shuffle=True, num_workers=2)

# การวนซ้ำเพื่อฝึกโมเดล
for batch_idx, (data, target) in enumerate(dataloader):
    # data คือ batch ของข้อมูล, target คือ batch ของ label
    # ... โค้ดสำหรับ Forward Pass และ Backpropagation ...
    if batch_idx == 0:
        print(f"Batch 0 - Data Shape: {data.shape}, Target Shape: {target.shape}")
        break
```

## 5.3 Convolutional Neural Networks (CNN)

### 5.3.1 Convolutional Neural Networks (CNN) และการประยุกต์ใช้กับ CIFAR-10

**Convolutional Neural Networks (CNN)** เป็นโครงข่ายประสาทเทียมที่ออกแบบมาเพื่อประมวลผลข้อมูลที่มีโครงสร้างแบบกริด (Grid-like Structure) เช่น รูปภาพ (2D Grid) และ Time Series (1D Grid)

**ส่วนประกอบหลักของ CNN:**
1.  **Convolutional Layer:** ใช้ **Filter** (หรือ Kernel) เพื่อสกัดคุณลักษณะ (Features) จากภาพ
2.  **Pooling Layer:** ลดขนาดมิติของ Feature Map เพื่อลดจำนวนพารามิเตอร์และป้องกัน Overfitting (เช่น Max Pooling)
3.  **Fully Connected Layer:** ชั้นสุดท้ายที่ทำหน้าที่จำแนกประเภท (Classification)

**ตัวอย่าง: การสร้าง CNN อย่างง่ายด้วย PyTorch**

```python
import torch.nn as nn
import torch.nn.functional as F

class SimpleCNN(nn.Module):
    def __init__(self):
        super(SimpleCNN, self).__init__()
        # 1. Convolutional Layer 1: Input 3 Channels (RGB), Output 6 Channels, Kernel Size 5
        self.conv1 = nn.Conv2d(3, 6, 5)
        # 2. Pooling Layer: Max Pooling, Kernel Size 2, Stride 2
        self.pool = nn.MaxPool2d(2, 2)
        # 3. Convolutional Layer 2: Input 6 Channels, Output 16 Channels, Kernel Size 5
        self.conv2 = nn.Conv2d(6, 16, 5)
        # 4. Fully Connected Layer: 16 * 5 * 5 (ขนาด Feature Map หลัง Pooling) -> 120
        self.fc1 = nn.Linear(16 * 5 * 5, 120)
        self.fc2 = nn.Linear(120, 84)
        self.fc3 = nn.Linear(84, 10) # Output 10 Classes (สำหรับ CIFAR-10)

    def forward(self, x):
        # -> conv1 -> ReLU -> pool
        x = self.pool(F.relu(self.conv1(x)))
        # -> conv2 -> ReLU -> pool
        x = self.pool(F.relu(self.conv2(x)))
        # Flatten (แปลง 2D Feature Map เป็น 1D Vector)
        x = torch.flatten(x, 1)
        # -> fc1 -> ReLU -> fc2 -> ReLU -> fc3
        x = F.relu(self.fc1(x))
        x = F.relu(self.fc2(x))
        x = self.fc3(x)
        return x

# model = SimpleCNN()
# print(model)
```

## 5.4 Transfer Learning: การใช้ Pre-trained Model (เช่น ResNet) ใน PyTorch

**Transfer Learning** คือเทคนิคการนำโมเดลที่ถูกฝึกมาแล้วด้วยชุดข้อมูลขนาดใหญ่ (เช่น ImageNet) มาใช้เป็นจุดเริ่มต้นในการฝึกโมเดลสำหรับงานใหม่ที่มีชุดข้อมูลขนาดเล็กกว่า

**ข้อดี:**
1.  ลดเวลาและทรัพยากรในการฝึกโมเดล
2.  ได้ประสิทธิภาพที่ดีกว่าการฝึกโมเดลตั้งแต่เริ่มต้น

**ขั้นตอนการทำ Transfer Learning:**
1.  โหลดโมเดลที่ถูกฝึกมาแล้ว (Pre-trained Model) เช่น ResNet-18
2.  **Freezing:** ตรึงน้ำหนักของชั้น Convolutional Layers ส่วนใหญ่ไว้ (ไม่ให้มีการปรับปรุง)
3.  **Replacing:** แทนที่ชั้นสุดท้าย (Fully Connected Layer) ด้วยชั้นใหม่ที่เหมาะสมกับจำนวน Class ของงานใหม่
4.  **Fine-Tuning:** ฝึกเฉพาะชั้นใหม่และอาจจะฝึกชั้นสุดท้ายของ Convolutional Layers ด้วย Learning Rate ที่ต่ำ

**ตัวอย่าง: Transfer Learning ด้วย ResNet-18**

```python
import torchvision.models as models

# 1. โหลด ResNet-18 ที่ถูกฝึกมาแล้ว
model_ft = models.resnet18(weights='ResNet18_Weights.DEFAULT')

# 2. Freezing พารามิเตอร์ทั้งหมด
for param in model_ft.parameters():
    param.requires_grad = False

# 3. แทนที่ Fully Connected Layer (fc)
num_ftrs = model_ft.fc.in_features
# สมมติว่างานใหม่มี 5 Classes
model_ft.fc = nn.Linear(num_ftrs, 5)

# ตอนนี้มีเพียงพารามิเตอร์ใน model_ft.fc เท่านั้นที่จะถูกฝึก
```

## 5.5 Recurrent Neural Networks (RNN) และแนวคิดเบื้องต้นสำหรับ Sequence Data

**Recurrent Neural Networks (RNN)** เป็นโครงข่ายประสาทเทียมที่ออกแบบมาเพื่อประมวลผลข้อมูลลำดับ (Sequence Data) เช่น ข้อความ (Text), เสียง (Audio), และ Time Series

**หลักการ:**
RNN มี **Hidden State** ที่ทำหน้าที่เป็น "หน่วยความจำ" (Memory) โดยจะรับ Input ปัจจุบันและ Hidden State ก่อนหน้า เพื่อสร้าง Output ปัจจุบันและ Hidden State ใหม่

**ปัญหาของ RNN:**
RNN พื้นฐานมีปัญหา **Vanishing Gradient** (Gradient ลดลงจนหายไป) เมื่อต้องประมวลผลลำดับที่ยาวมาก ทำให้ไม่สามารถเรียนรู้ความสัมพันธ์ระยะยาวได้

**ทางแก้:**
*   **Long Short-Term Memory (LSTM):** ใช้โครงสร้าง **Gate** (Input, Forget, Output Gate) เพื่อควบคุมการไหลของข้อมูลเข้าและออกจากหน่วยความจำ (Cell State)
*   **Gated Recurrent Unit (GRU):** เป็นรูปแบบที่ง่ายกว่า LSTM แต่ให้ประสิทธิภาพใกล้เคียงกัน

**ตัวอย่าง: การใช้ LSTM ใน PyTorch**

```python
class LSTMModel(nn.Module):
    def __init__(self, input_size, hidden_size, output_size):
        super(LSTMModel, self).__init__()
        self.hidden_size = hidden_size
        # LSTM Layer
        self.lstm = nn.LSTM(input_size, hidden_size, batch_first=True)
        # Fully Connected Layer
        self.fc = nn.Linear(hidden_size, output_size)

    def forward(self, x):
        # x shape: (batch_size, seq_len, input_size)
        # h0, c0 คือ Hidden State และ Cell State เริ่มต้น (มักเป็นศูนย์)
        h0 = torch.zeros(1, x.size(0), self.hidden_size).to(x.device)
        c0 = torch.zeros(1, x.size(0), self.hidden_size).to(x.device)

        # out shape: (batch_size, seq_len, hidden_size)
        out, _ = self.lstm(x, (h0, c0))

        # ใช้ Hidden State ของ Time Step สุดท้ายสำหรับ Classification
        out = self.fc(out[:, -1, :])
        return out

# สมมติ: Input Size 10, Hidden Size 20, Output Size 2
# model = LSTMModel(10, 20, 2)
```

## 5.6 แบบฝึกหัดและเฉลย (โมดูล 5)

**แบบฝึกหัด 5.1: การสร้าง Dataset และ DataLoader**
จงสร้าง Dataset และ DataLoader สำหรับชุดข้อมูลสมมติที่มี 500 ตัวอย่าง แต่ละตัวอย่างมี 5 Features และ 3 Classes โดยกำหนด `batch_size=32` และ `shuffle=True`

**แบบฝึกหัด 5.2: การใช้ CNN (แนวคิด)**
จงอธิบายว่าทำไม CNN จึงเหมาะสมกับงาน Image Classification มากกว่าโครงข่ายประสาทเทียมแบบ Fully Connected (MLP)

**เฉลย 5.1:**
```python
from torch.utils.data import TensorDataset, DataLoader
import torch

X_data = torch.randn(500, 5) # 500 ตัวอย่าง, 5 Features
y_labels = torch.randint(0, 3, (500,)) # 3 Classes

# TensorDataset รวมข้อมูลและ Label
dataset = TensorDataset(X_data, y_labels)

# DataLoader
dataloader = DataLoader(dataset, batch_size=32, shuffle=True)

# ตรวจสอบจำนวน Batch
# print(len(dataloader)) # 500 / 32 = 16 batches (15 เต็ม + 1 เศษ)
```

**เฉลย 5.2:**
CNN มีความเหมาะสมกับงาน Image Classification มากกว่า MLP เนื่องจาก:
1.  **Parameter Sharing:** CNN ใช้ Filter ชุดเดียวกันในการสกัดคุณลักษณะทั่วทั้งภาพ ทำให้ลดจำนวนพารามิเตอร์ลงอย่างมาก เมื่อเทียบกับ MLP ที่แต่ละ Neuron ในชั้นแรกต้องเชื่อมต่อกับทุก Pixel
2.  **Sparsity of Connections:** แต่ละ Neuron ใน Convolutional Layer จะเชื่อมต่อกับพื้นที่เล็กๆ ของ Input เท่านั้น (Local Receptive Field) ซึ่งสอดคล้องกับธรรมชาติของภาพที่ Feature สำคัญมักอยู่รวมกันเป็นกลุ่ม
3.  **Translation Invariance:** CNN สามารถจดจำ Feature ได้แม้ว่า Feature นั้นจะถูกเลื่อนตำแหน่งไปในส่วนต่างๆ ของภาพ ซึ่งเป็นคุณสมบัติที่สำคัญมากในการจำแนกวัตถุในภาพถ่ายจริง
4.  **Hierarchy of Features:** CNN สามารถเรียนรู้ Feature ที่ซับซ้อนขึ้นเรื่อยๆ ในแต่ละชั้น (เช่น ขอบ -> รูปร่าง -> วัตถุ)
---
**หมายเหตุ:** เนื้อหาส่วนนี้เป็นส่วนขยายของโมดูล 5 ซึ่งจะถูกนำไปรวมกับเนื้อหาโมดูลอื่น ๆ ที่ขยายแล้ว เพื่อให้ได้คู่มือฉบับสมบูรณ์ 200-300 หน้า
