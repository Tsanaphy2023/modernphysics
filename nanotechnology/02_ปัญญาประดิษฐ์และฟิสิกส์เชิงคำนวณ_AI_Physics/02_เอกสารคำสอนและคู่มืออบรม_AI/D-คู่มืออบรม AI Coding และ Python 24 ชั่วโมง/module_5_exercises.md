# Module 5: Deep Learning with PyTorch - แบบฝึกหัดเชิงปฏิบัติการ

## วัตถุประสงค์
เพื่อให้นักเรียนสามารถประยุกต์ใช้แนวคิดพื้นฐานของ Deep Learning และ PyTorch ในการสร้างและฝึกฝนโมเดล Neural Network

---

### แบบฝึกหัดที่ 1: การจัดการ Tensor และ Autograd (PyTorch Fundamentals)

**โจทย์:**
1. สร้าง PyTorch Tensor ขนาด `(3, 4)` ที่มีค่าสุ่ม (Random) และกำหนดให้ `requires_grad=True`
2. สร้าง Tensor ที่สองขนาด `(4, 1)` ที่มีค่าเป็น 1 ทั้งหมด
3. คำนวณผลคูณเมทริกซ์ (Matrix Multiplication) ระหว่าง Tensor ทั้งสอง (`result = tensor1 @ tensor2`)
4. คำนวณผลรวมของ `result` ทั้งหมด (`final_sum = result.sum()`)
5. ทำการ Backward Pass บน `final_sum`
6. แสดงค่า Gradient ของ `tensor1`

**แนวคิดที่เกี่ยวข้อง:** `torch.rand`, `torch.ones`, `requires_grad`, Matrix Multiplication (`@`), `.sum()`, `.backward()`, `.grad`

---

### แบบฝึกหัดที่ 2: การสร้าง Feedforward Neural Network (FFNN)

**โจทย์:**
1. สร้างคลาส `SimpleFFNN` ที่สืบทอดจาก `nn.Module`
2. กำหนดโครงสร้างของ Network ให้มี 3 Layers:
    *   Input Layer: 10 Features
    *   Hidden Layer: 20 Neurons, ใช้ Activation Function เป็น ReLU
    *   Output Layer: 1 Neuron
3. เขียนเมธอด `forward` เพื่อกำหนดลำดับการทำงานของ Layers

**แนวคิดที่เกี่ยวข้อง:** `nn.Module`, `nn.Linear`, `nn.ReLU`, `forward` method

---

### แบบฝึกหัดที่ 3: การจำลอง Training Loop (Regression Task)

**โจทย์:**
สมมติว่าคุณมีโมเดล FFNN ที่สร้างไว้แล้ว และมีข้อมูลสมมติสำหรับงาน Regression:
*   Input Data (`X`): `torch.randn(100, 10)`
*   Target Data (`y`): `torch.randn(100, 1)`
1. กำหนด Loss Function เป็น Mean Squared Error (MSE) และ Optimizer เป็น Adam (Learning Rate = 0.01)
2. จำลอง Training Loop 5 Epochs:
    *   Zero Gradients
    *   Forward Pass
    *   Calculate Loss
    *   Backward Pass
    *   Optimizer Step
3. แสดงค่า Loss ในแต่ละ Epoch

**แนวคิดที่เกี่ยวข้อง:** `nn.MSELoss`, `optim.Adam`, `optimizer.zero_grad()`, `loss.backward()`, `optimizer.step()`

---

### แบบฝึกหัดที่ 4: การประยุกต์ใช้ Convolutional Layer (CNN)

**โจทย์:**
1. สร้าง PyTorch Tensor ขนาด `(1, 1, 5, 5)` เพื่อจำลองภาพขาวดำขนาด 5x5 (Batch Size=1, Channels=1)
2. สร้าง Convolutional Layer (`nn.Conv2d`) ที่มี:
    *   Input Channels: 1
    *   Output Channels: 1
    *   Kernel Size: 3x3
    *   Stride: 1
    *   Padding: 0
3. ทำการ Forward Pass Tensor ผ่าน Layer ที่สร้างขึ้น
4. แสดงขนาดของ Output Tensor

**แนวคิดที่เกี่ยวข้อง:** `nn.Conv2d`, Tensor Shape (N, C, H, W), Forward Pass

---

### แบบฝึกหัดที่ 5: การใช้ Pre-trained Model (Transfer Learning Concept)

**โจทย์:**
1. นำเข้าโมเดล ResNet-18 ที่ถูก Pre-trained บน ImageNet (`torchvision.models.resnet18(pretrained=True)`)
2. ตรึง Weights ของทุก Layer ในโมเดล (Freeze all parameters)
3. เปลี่ยน Output Layer (Fully Connected Layer) ของโมเดลให้มี Output Features เพียง 2 คลาส (สมมติว่าเป็นงาน Classification ใหม่)
4. ตรวจสอบว่าเฉพาะ Weights ของ Output Layer ใหม่เท่านั้นที่ `requires_grad=True`

**แนวคิดที่เกี่ยวข้อง:** `torchvision.models`, `resnet18`, `pretrained=True`, `param.requires_grad`, การปรับเปลี่ยน `fc` layer
