# Module 5: Deep Learning with PyTorch - เฉลยแบบฝึกหัดเชิงปฏิบัติการ

---

### แบบฝึกหัดที่ 1: การจัดการ Tensor และ Autograd (PyTorch Fundamentals)

**เฉลย:**

```python
import torch

# 1. สร้าง PyTorch Tensor ขนาด (3, 4) ที่มีค่าสุ่ม และกำหนด requires_grad=True
tensor1 = torch.randn(3, 4, requires_grad=True)
print("Tensor 1:\n", tensor1)

# 2. สร้าง Tensor ที่สองขนาด (4, 1) ที่มีค่าเป็น 1 ทั้งหมด
tensor2 = torch.ones(4, 1)
print("\nTensor 2:\n", tensor2)

# 3. คำนวณผลคูณเมทริกซ์
result = tensor1 @ tensor2
print("\nResult (Matrix Multiplication):\n", result)

# 4. คำนวณผลรวมของ result ทั้งหมด
final_sum = result.sum()
print("\nFinal Sum:", final_sum)

# 5. ทำการ Backward Pass บน final_sum
final_sum.backward()

# 6. แสดงค่า Gradient ของ tensor1
print("\nGradient of Tensor 1 (d(final_sum)/d(tensor1)):\n", tensor1.grad)
```

**คำอธิบาย:**
*   `tensor1.grad` จะแสดงค่า Gradient ของ `final_sum` เทียบกับ `tensor1` ซึ่งเป็นผลลัพธ์จากการทำ Backward Pass
*   เนื่องจาก `final_sum` เป็นผลรวมของทุกองค์ประกอบใน `result` และ `result` คือผลคูณของ `tensor1` กับ `tensor2` (ซึ่งมีค่าเป็น 1 ทั้งหมด) ดังนั้น Gradient ของแต่ละองค์ประกอบใน `tensor1` จะเท่ากับค่าขององค์ประกอบที่สอดคล้องกันใน `tensor2` ซึ่งในกรณีนี้คือ 1

---

### แบบฝึกหัดที่ 2: การสร้าง Feedforward Neural Network (FFNN)

**เฉลย:**

```python
import torch.nn as nn

class SimpleFFNN(nn.Module):
    def __init__(self):
        super(SimpleFFNN, self).__init__()
        # 1. Hidden Layer: 10 -> 20, ใช้ ReLU
        self.fc1 = nn.Linear(10, 20)
        # 2. Output Layer: 20 -> 1
        self.fc2 = nn.Linear(20, 1)
        # Activation Function
        self.relu = nn.ReLU()

    def forward(self, x):
        # 1. Forward Pass ผ่าน Hidden Layer และ ReLU
        x = self.fc1(x)
        x = self.relu(x)
        # 2. Forward Pass ผ่าน Output Layer
        x = self.fc2(x)
        return x

# ทดสอบโครงสร้าง
model = SimpleFFNN()
print(model)
```

**คำอธิบาย:**
*   `nn.Module` เป็นคลาสพื้นฐานสำหรับโมเดล Neural Network ทั้งหมดใน PyTorch
*   `__init__` ใช้สำหรับกำหนด Layers และ Components ต่างๆ ของโมเดล
*   `forward(self, x)` กำหนดลำดับการทำงานของข้อมูล (Input `x`) ผ่าน Layers ต่างๆ

---

### แบบฝึกหัดที่ 3: การจำลอง Training Loop (Regression Task)

**เฉลย:**

```python
import torch
import torch.nn as nn
import torch.optim as optim

# ข้อมูลสมมติ
X = torch.randn(100, 10)
y = torch.randn(100, 1)

# โมเดลจากแบบฝึกหัดที่ 2
class SimpleFFNN(nn.Module):
    def __init__(self):
        super(SimpleFFNN, self).__init__()
        self.fc1 = nn.Linear(10, 20)
        self.fc2 = nn.Linear(20, 1)
        self.relu = nn.ReLU()
    def forward(self, x):
        x = self.fc1(x)
        x = self.relu(x)
        x = self.fc2(x)
        return x

model = SimpleFFNN()

# 1. กำหนด Loss Function และ Optimizer
criterion = nn.MSELoss()
optimizer = optim.Adam(model.parameters(), lr=0.01)

# 2. จำลอง Training Loop 5 Epochs
num_epochs = 5
for epoch in range(num_epochs):
    # 2.1 Zero Gradients
    optimizer.zero_grad()

    # 2.2 Forward Pass
    outputs = model(X)

    # 2.3 Calculate Loss
    loss = criterion(outputs, y)

    # 2.4 Backward Pass
    loss.backward()

    # 2.5 Optimizer Step
    optimizer.step()

    # 3. แสดงค่า Loss ในแต่ละ Epoch
    print(f'Epoch [{epoch+1}/{num_epochs}], Loss: {loss.item():.4f}')
```

**คำอธิบาย:**
*   `optimizer.zero_grad()`: ล้างค่า Gradient เก่าก่อนเริ่ม Backward Pass ใหม่
*   `criterion(outputs, y)`: คำนวณค่าความผิดพลาดระหว่างผลลัพธ์ที่ทำนาย (`outputs`) กับค่าจริง (`y`)
*   `loss.backward()`: คำนวณ Gradient ของ Loss เทียบกับ Weights ทั้งหมด
*   `optimizer.step()`: ปรับปรุง Weights ของโมเดลตามค่า Gradient ที่คำนวณได้

---

### แบบฝึกหัดที่ 4: การประยุกต์ใช้ Convolutional Layer (CNN)

**เฉลย:**

```python
import torch
import torch.nn as nn

# 1. สร้าง PyTorch Tensor ขนาด (1, 1, 5, 5)
input_tensor = torch.randn(1, 1, 5, 5)
print("Input Tensor Shape:", input_tensor.shape)

# 2. สร้าง Convolutional Layer
conv_layer = nn.Conv2d(
    in_channels=1,
    out_channels=1,
    kernel_size=3,
    stride=1,
    padding=0
)

# 3. ทำการ Forward Pass
output_tensor = conv_layer(input_tensor)

# 4. แสดงขนาดของ Output Tensor
print("Output Tensor Shape:", output_tensor.shape)
```

**คำอธิบาย:**
*   สูตรการคำนวณขนาด Output ของ Convolutional Layer คือ:
    $$O = \lfloor \frac{I - K + 2P}{S} \rfloor + 1$$
    เมื่อ $I=5$ (Input Size), $K=3$ (Kernel Size), $P=0$ (Padding), $S=1$ (Stride)
    $$O = \lfloor \frac{5 - 3 + 2(0)}{1} \rfloor + 1 = 2 + 1 = 3$$
*   ดังนั้น Output Tensor จะมีขนาด `(1, 1, 3, 3)` (Batch Size, Output Channels, Height, Width)

---

### แบบฝึกหัดที่ 5: การใช้ Pre-trained Model (Transfer Learning Concept)

**เฉลย:**

```python
import torch
import torchvision.models as models

# 1. นำเข้าโมเดล ResNet-18 ที่ถูก Pre-trained
model = models.resnet18(weights=models.ResNet18_Weights.IMAGENET1K_V1)

# 2. ตรึง Weights ของทุก Layer ในโมเดล (Freeze all parameters)
for param in model.parameters():
    param.requires_grad = False

# 3. เปลี่ยน Output Layer ให้มี Output Features เพียง 2 คลาส
num_ftrs = model.fc.in_features
model.fc = nn.Linear(num_ftrs, 2)

# 4. ตรวจสอบว่าเฉพาะ Weights ของ Output Layer ใหม่เท่านั้นที่ requires_grad=True
print("Requires Grad Status:")
for name, param in model.named_parameters():
    if 'fc' in name:
        # ตรวจสอบเฉพาะ Layer ที่ถูกเปลี่ยน
        print(f"Layer {name}: requires_grad={param.requires_grad}")
    else:
        # ตรวจสอบ Layer อื่นๆ (ควรเป็น False)
        if param.requires_grad:
             print(f"Layer {name}: requires_grad={param.requires_grad} (ERROR: Should be False)")
```

**คำอธิบาย:**
*   การตั้งค่า `param.requires_grad = False` จะป้องกันไม่ให้ Weights ของ Layer นั้นถูกปรับปรุงระหว่าง Training (Freezing)
*   เมื่อเราเปลี่ยน `model.fc` เป็น `nn.Linear(num_ftrs, 2)` ใหม่ Weights ของ Layer ใหม่นี้จะถูกสร้างขึ้นมาพร้อมกับค่าเริ่มต้นที่ `requires_grad=True` โดยอัตโนมัติ ทำให้เราสามารถฝึกเฉพาะ Layer สุดท้ายนี้ได้ (Transfer Learning)
