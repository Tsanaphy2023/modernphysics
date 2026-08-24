# บทที่ 5: โครงข่ายประสาทเทียมและการเรียนรู้เชิงลึก (Deep Learning)

## วัตถุประสงค์การเรียนรู้
*   เข้าใจสถาปัตยกรรมและหลักการทำงานของโครงข่ายประสาทเทียม
*   เรียนรู้เทคนิคการฝึกสอนและการปรับปรุงประสิทธิภาพ
*   ประยุกต์ใช้ในการแก้ปัญหาที่ซับซ้อนทางฟิสิกส์

## 5.1 โครงข่ายประสาทเทียมพื้นฐาน: Perceptron และ Multi-layer Perceptron

**Perceptron** เป็นหน่วยประมวลผลพื้นฐานที่สุดในโครงข่ายประสาทเทียม ซึ่งจำลองการทำงานของเซลล์ประสาทชีวภาพ โดยรับอินพุตหลายค่า, คูณด้วยน้ำหนัก, รวมผลรวม, และส่งผ่านฟังก์ชันกระตุ้นเพื่อสร้างเอาต์พุต Perceptron สามารถใช้ในการจำแนกข้อมูลเชิงเส้นตรงได้

**Multi-layer Perceptron (MLP)** หรือโครงข่ายประสาทเทียมแบบหลายชั้น เป็นการขยายแนวคิดของ Perceptron โดยมีชั้นอินพุต, ชั้นซ่อนเร้น (hidden layers) อย่างน้อยหนึ่งชั้น, และชั้นเอาต์พุต แต่ละชั้นประกอบด้วย Perceptron หลายตัวเชื่อมต่อกัน MLP สามารถเรียนรู้ความสัมพันธ์ที่ไม่เชิงเส้นที่ซับซ้อนในข้อมูลได้

### ตัวอย่างโค้ด: การสร้าง MLP อย่างง่ายด้วย TensorFlow/Keras

```python
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.datasets import make_moons
import matplotlib.pyplot as plt

# 1. สร้างข้อมูลตัวอย่างที่ไม่เชิงเส้น (เช่น ปัญหา Two Moons)
X, y = make_moons(n_samples=200, noise=0.15, random_state=42)

# 2. ปรับขนาดข้อมูล (Scaling)
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# 3. แบ่งข้อมูลเป็นชุดฝึกและชุดทดสอบ
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.3, random_state=42)

# 4. สร้างแบบจำลอง MLP
model = Sequential([
    Dense(10, activation=\'relu\', input_shape=(X_train.shape[1],)), # Hidden layer 1
    Dense(10, activation=\'relu\'),                                 # Hidden layer 2
    Dense(1, activation=\'sigmoid\')                                  # Output layer for binary classification
])

# 5. คอมไพล์แบบจำลอง
model.compile(optimizer=\'adam\', loss=\'binary_crossentropy\', metrics=[\'accuracy\'])

# 6. ฝึกแบบจำลอง
history = model.fit(X_train, y_train, epochs=100, batch_size=16, verbose=0, validation_split=0.2)

# 7. ประเมินประสิทธิภาพ
loss, accuracy = model.evaluate(X_test, y_test, verbose=0)
print(f"Test Accuracy: {accuracy:.4f}")

# 8. แสดงผลการจำแนก (Visualization)
def plot_decision_boundary(X, y, model, title):
    x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
    y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
    xx, yy = np.meshgrid(np.arange(x_min, x_max, 0.1),
                         np.arange(y_min, y_max, 0.1))
    
    Z = model.predict(np.c_[xx.ravel(), yy.ravel()])
    Z = (Z > 0.5).reshape(xx.shape)

    plt.contourf(xx, yy, Z, alpha=0.4)
    plt.scatter(X[:, 0], X[:, 1], c=y, s=20, edgecolor=\'k\')
    plt.title(title)
    plt.show()

plot_decision_boundary(X_scaled, y, model, \'MLP Decision Boundary for Two Moons\')

# ตัวอย่างการทำนายสำหรับข้อมูลใหม่
new_data = np.array([[-0.5, 0.5], [1.0, -0.5]])
new_data_scaled = scaler.transform(new_data)
predictions = model.predict(new_data_scaled)
print(f"Predictions for new data: {predictions.flatten() > 0.5}")
```

## 5.2 อัลกอริทึมการแพร่กระจายย้อนกลับ (Backpropagation) และการหาค่าเหมาะสมที่สุด

**Backpropagation** เป็นอัลกอริทึมหลักที่ใช้ในการฝึกโครงข่ายประสาทเทียม โดยจะคำนวณ Gradient ของฟังก์ชันความผิดพลาด (Loss Function) เทียบกับน้ำหนักของโครงข่ายประสาทเทียม ซึ่ง Gradient นี้จะถูกใช้โดย Optimizer เพื่อปรับปรุงน้ำหนักของโมเดลให้มีประสิทธิภาพดีขึ้น กระบวนการนี้ประกอบด้วยสองขั้นตอนหลัก:
1.  **Forward Pass:** อินพุตถูกส่งผ่านโครงข่ายเพื่อคำนวณเอาต์พุตและค่าความผิดพลาด
2.  **Backward Pass:** Gradient ของความผิดพลาดจะถูกคำนวณย้อนกลับจากชั้นเอาต์พุตไปยังชั้นอินพุต เพื่ออัปเดตน้ำหนัก

**การหาค่าเหมาะสมที่สุด (Optimization)** เป็นกระบวนการที่ใช้อัลกอริทึม เช่น Gradient Descent (และรูปแบบต่างๆ เช่น Stochastic Gradient Descent, Adam) เพื่อปรับน้ำหนักของโครงข่ายประสาทเทียมให้ค่า Loss Function มีค่าน้อยที่สุด

## 5.3 ฟังก์ชันกระตุ้น (Activation Functions) และการเลือกใช้ที่เหมาะสม

**ฟังก์ชันกระตุ้น (Activation Functions)** เป็นส่วนสำคัญของเซลล์ประสาทเทียมที่กำหนดว่าเซลล์ประสาทควรจะ 

กระตุ้นหรือไม่ โดยการนำผลรวมถ่วงน้ำหนักของอินพุตไปแปลงเป็นเอาต์พุต ฟังก์ชันกระตุ้นที่แตกต่างกันมีคุณสมบัติและประโยชน์ที่แตกต่างกัน:

*   **Sigmoid:** บีบอัดค่าอินพุตให้อยู่ในช่วง (0, 1) เหมาะสำหรับชั้นเอาต์พุตของการจำแนกประเภทแบบไบนารี แต่มีปัญหา Vanishing Gradient
*   **ReLU (Rectified Linear Unit):** `f(x) = max(0, x)` เป็นที่นิยมเนื่องจากแก้ปัญหา Vanishing Gradient ได้ดีและคำนวณง่าย
*   **Leaky ReLU, ELU, PReLU:** เป็นรูปแบบที่พัฒนามาจาก ReLU เพื่อแก้ปัญหา Dying ReLU
*   **Tanh (Hyperbolic Tangent):** บีบอัดค่าอินพุตให้อยู่ในช่วง (-1, 1) คล้าย Sigmoid แต่มีค่าเฉลี่ยเป็นศูนย์ ทำให้การฝึกมีเสถียรภาพมากขึ้น
*   **Softmax:** ใช้สำหรับชั้นเอาต์พุตของการจำแนกประเภทแบบหลายคลาส โดยแปลงค่าให้เป็นความน่าจะเป็นที่รวมกันได้ 1

### การเลือกใช้ที่เหมาะสม
การเลือกฟังก์ชันกระตุ้นขึ้นอยู่กับลักษณะของปัญหาและชั้นของโครงข่ายประสาทเทียม:
*   **ชั้นซ่อนเร้น:** ReLU และรูปแบบต่างๆ (Leaky ReLU, ELU) มักเป็นตัวเลือกที่ดีที่สุด
*   **ชั้นเอาต์พุต:**
    *   **Binary Classification:** Sigmoid
    *   **Multi-class Classification:** Softmax
    *   **Regression:** Linear (ไม่มีฟังก์ชันกระตุ้น)

## 5.4 เทคนิคการป้องกัน Overfitting: Dropout, Batch Normalization และ Regularization

**Overfitting** เกิดขึ้นเมื่อแบบจำลองเรียนรู้ข้อมูลการฝึกมากเกินไป จนไม่สามารถทำงานได้ดีกับข้อมูลใหม่ที่ไม่เคยเห็นมาก่อน ใน Deep Learning มีหลายเทคนิคที่ใช้ในการป้องกัน Overfitting:

*   **Dropout:** ระหว่างการฝึก แต่ละเซลล์ประสาทในชั้นที่กำหนดจะถูก 

ปิดใช้งาน (dropped out) แบบสุ่มด้วยความน่าจะเป็นที่กำหนด ซึ่งช่วยลดการพึ่งพาเซลล์ประสาทใดเซลล์ประสาทหนึ่งมากเกินไป และบังคับให้โครงข่ายเรียนรู้คุณลักษณะที่แข็งแกร่งขึ้น
*   **Batch Normalization:** ปรับค่าเฉลี่ยและส่วนเบี่ยงเบนมาตรฐานของอินพุตในแต่ละชั้นให้เป็นมาตรฐาน ซึ่งช่วยให้การฝึกมีเสถียรภาพมากขึ้นและลดเวลาในการฝึก
*   **Regularization (L1, L2):** เพิ่มเทอมปรับโทษ (penalty term) เข้าไปใน Loss Function เพื่อจำกัดขนาดของน้ำหนักในแบบจำลอง ซึ่งช่วยลดความซับซ้อนของแบบจำลองและป้องกัน Overfitting

## 5.5 สถาปัตยกรรมของ Deep Neural Networks: การออกแบบและการปรับแต่ง

การออกแบบสถาปัตยกรรมของ Deep Neural Networks (DNNs) เป็นกระบวนการที่สำคัญและต้องอาศัยความเข้าใจในปัญหาและข้อมูล การออกแบบประกอบด้วยการเลือกจำนวนชั้นซ่อนเร้น, จำนวนเซลล์ประสาทในแต่ละชั้น, ฟังก์ชันกระตุ้น, และเทคนิคการป้องกัน Overfitting

### หลักการออกแบบเบื้องต้น:
*   **จำนวนชั้น:** โดยทั่วไป ยิ่งมีชั้นลึกมากเท่าไหร่ โมเดลก็ยิ่งสามารถเรียนรู้คุณลักษณะที่ซับซ้อนได้มากขึ้น แต่ก็เสี่ยงต่อ Overfitting และใช้เวลาในการฝึกนานขึ้น
*   **จำนวนเซลล์ประสาท:** จำนวนเซลล์ประสาทในแต่ละชั้นควรเหมาะสมกับความซับซ้อนของข้อมูลและปัญหา
*   **การเชื่อมต่อ:** การเชื่อมต่อแบบ Feedforward เป็นพื้นฐาน แต่ก็มีสถาปัตยกรรมที่ซับซ้อนขึ้น เช่น Residual Connections (ใน ResNet) ที่ช่วยให้สามารถสร้างโครงข่ายที่ลึกมากได้

## 5.6 การประยุกต์ใช้ในฟิสิกส์: การประมาณฟังก์ชันคลื่น (Wave Function Approximation)

Deep Learning ได้รับการประยุกต์ใช้อย่างกว้างขวางในฟิสิกส์ โดยเฉพาะอย่างยิ่งในการแก้ปัญหาที่เกี่ยวข้องกับกลศาสตร์ควอนตัม เช่น การประมาณฟังก์ชันคลื่นของระบบหลายอนุภาค (Many-body Quantum Systems) ซึ่งเป็นปัญหาที่ซับซ้อนทางคณิตศาสตร์

### ตัวอย่างโค้ด: การใช้ Neural Network เพื่อประมาณฟังก์ชันคลื่น (แนวคิด)

```python
import torch
import torch.nn as nn
import torch.optim as optim

# สมมติ Hamiltonian ของระบบควอนตัม (ตัวอย่างง่ายๆ)
def hamiltonian(x):
    # H = -0.5 * d^2/dx^2 + 0.5 * x^2 (Harmonic Oscillator)
    # สำหรับการสาธิต เราจะใช้ฟังก์ชันพลังงานที่ง่ายกว่า
    return 0.5 * x**2

# สร้าง Neural Network เพื่อประมาณฟังก์ชันคลื่น (psi)
class WaveFunctionApproximator(nn.Module):
    def __init__(self):
        super(WaveFunctionApproximator, self).__init__()
        self.fc1 = nn.Linear(1, 64) # Input: position (x)
        self.fc2 = nn.Linear(64, 64)
        self.fc3 = nn.Linear(64, 1)  # Output: psi(x)

    def forward(self, x):
        x = torch.tanh(self.fc1(x))
        x = torch.tanh(self.fc2(x))
        return x # psi(x) - อาจต้องปรับให้เป็นค่าบวกและเป็น normalized

# ฟังก์ชัน Loss ที่อิงจาก Schrödinger Equation (แนวคิด)
def schrodinger_loss(model, x_points):
    x_points.requires_grad_(True)
    psi = model(x_points)

    # คำนวณอนุพันธ์อันดับหนึ่ง (d_psi/dx)
    d_psi_dx = torch.autograd.grad(psi, x_points, grad_outputs=torch.ones_like(psi), create_graph=True)[0]

    # คำนวณอนุพันธ์อันดับสอง (d^2_psi/dx^2)
    d2_psi_dx2 = torch.autograd.grad(d_psi_dx, x_points, grad_outputs=torch.ones_like(d_psi_dx), create_graph=True)[0]

    # Schrödinger Equation: H_op psi = E psi
    # สำหรับ Harmonic Oscillator: -0.5 * d^2_psi/dx^2 + 0.5 * x^2 * psi = E * psi
    # เราจะพยายามทำให้ (H_op psi - E psi)^2 มีค่าน้อยที่สุด
    # ในตัวอย่างนี้ เราจะใช้ variational principle: E = <psi|H|psi> / <psi|psi>
    # และพยายามลด E ลง

    # สำหรับการสาธิต เราจะใช้ loss ที่ง่ายกว่า: (H_op psi - E_target * psi)^2
    # โดย E_target คือพลังงานที่เราต้องการให้โมเดลประมาณได้ (เช่น ground state energy)
    E_target = 0.5 # Ground state energy for quantum harmonic oscillator

    # Approximate H_op psi
    H_psi = -0.5 * d2_psi_dx2 + 0.5 * x_points**2 * psi

    loss = torch.mean((H_psi - E_target * psi)**2)
    return loss

# สร้างโมเดลและ Optimizer
model = WaveFunctionApproximator()
optimizer = optim.Adam(model.parameters(), lr=0.01)

# จุดสำหรับฝึก (เช่น ตำแหน่ง x)
x_train = torch.linspace(-3, 3, 100).reshape(-1, 1)

# ฝึกโมเดล
epochs = 1000
for epoch in range(epochs):
    optimizer.zero_grad()
    loss = schrodinger_loss(model, x_train)
    loss.backward()
    optimizer.step()
    if (epoch + 1) % 100 == 0:
        print(f

Epoch {epoch+1}/{epochs}, Loss: {loss.item():.4f}")

# พล็อตผลลัพธ์ (เปรียบเทียบกับฟังก์ชันคลื่นจริงของ Harmonic Oscillator)
# (ต้องมีการคำนวณฟังก์ชันคลื่นจริงเพื่อเปรียบเทียบ)
# สำหรับการสาธิตนี้ เราจะพล็อตฟังก์ชันคลื่นที่ประมาณได้

plt.figure(figsize=(8, 6))
plt.plot(x_train.detach().numpy(), model(x_train).detach().numpy(), label=\'Approximate Wave Function\')
plt.xlabel(\'Position (x)\')
plt.ylabel(\'Psi(x)\')
plt.title(\'Neural Network Approximation of Wave Function\')
plt.grid(True)
plt.legend()
plt.show()
```

## 5.7 เทคนิคการฝึกสอนขั้นสูง: Adam Optimizer, Learning Rate Scheduling

การฝึกสอน Deep Neural Networks ให้มีประสิทธิภาพนั้นมักจะต้องใช้เทคนิคการฝึกสอนขั้นสูงเพื่อช่วยให้โมเดลลู่เข้าสู่จุดเหมาะสมที่สุดได้เร็วขึ้นและมีเสถียรภาพมากขึ้น

*   **Adam Optimizer:** เป็นหนึ่งใน Optimizer ที่ได้รับความนิยมมากที่สุด เนื่องจากเป็นการรวมข้อดีของ AdaGrad และ RMSProp เข้าด้วยกัน โดยจะปรับ Learning Rate สำหรับพารามิเตอร์แต่ละตัวแบบไดนามิก ทำให้การฝึกมีประสิทธิภาพและรวดเร็ว
*   **Learning Rate Scheduling:** เป็นเทคนิคที่ปรับ Learning Rate ระหว่างการฝึก โดยอาจจะลด Learning Rate ลงเมื่อ Loss เริ่มคงที่ หรือเพิ่มขึ้นในช่วงแรกเพื่อเร่งการลู่เข้า ซึ่งช่วยให้โมเดลสามารถหาจุดเหมาะสมที่สุดได้ดีขึ้นและหลีกเลี่ยงการติดอยู่ใน Local Minima

## บทสรุป

บทนี้ได้สำรวจพื้นฐานของโครงข่ายประสาทเทียม ตั้งแต่ Perceptron ไปจนถึง Multi-layer Perceptron, กลไกการฝึกสอนด้วย Backpropagation, ความสำคัญของ Activation Functions, เทคนิคการป้องกัน Overfitting และเทคนิคการฝึกสอนขั้นสูง นอกจากนี้ยังได้เห็นตัวอย่างการประยุกต์ใช้ Deep Learning ในฟิสิกส์ โดยเฉพาะอย่างยิ่งในการประมาณฟังก์ชันคลื่น ซึ่งแสดงให้เห็นถึงศักยภาพอันมหาศาลของ Deep Learning ในการแก้ปัญหาที่ซับซ้อนทางฟิสิกส์เชิงคณิตศาสตร์

## แบบทดสอบบทที่ 5

1.  จงอธิบายความแตกต่างระหว่าง Perceptron และ Multi-layer Perceptron (MLP) ในแง่ของสถาปัตยกรรมและความสามารถในการเรียนรู้
    *   a) Perceptron มีหลายชั้นซ่อนเร้น ส่วน MLP มีเพียงชั้นเดียว
    *   b) Perceptron สามารถเรียนรู้ความสัมพันธ์ที่ไม่เชิงเส้นได้ ส่วน MLP ไม่ได้
    *   c) Perceptron สามารถจำแนกข้อมูลเชิงเส้นตรงได้ ส่วน MLP สามารถเรียนรู้ความสัมพันธ์ที่ไม่เชิงเส้นที่ซับซ้อนได้
    *   d) ไม่มีข้อใดถูก

2.  อัลกอริทึมใดที่ใช้ในการคำนวณ Gradient ของฟังก์ชันความผิดพลาดเทียบกับน้ำหนักของโครงข่ายประสาทเทียม?
    *   a) Forward Propagation
    *   b) Backpropagation
    *   c) Gradient Descent
    *   d) Adam Optimization

3.  ฟังก์ชันกระตุ้นใดที่มักใช้ในชั้นซ่อนเร้นของ Deep Neural Networks และช่วยแก้ปัญหา Vanishing Gradient ได้ดี?
    *   a) Sigmoid
    *   b) Tanh
    *   c) ReLU
    *   d) Softmax

4.  เทคนิคใดต่อไปนี้ที่ช่วยป้องกัน Overfitting โดยการปิดใช้งานเซลล์ประสาทบางส่วนแบบสุ่มระหว่างการฝึก?
    *   a) Batch Normalization
    *   b) Regularization
    *   c) Dropout
    *   d) Learning Rate Scheduling

5.  จงอธิบายว่าเหตุใด Adam Optimizer จึงเป็นที่นิยมในการฝึก Deep Neural Networks เมื่อเทียบกับ Stochastic Gradient Descent (SGD) แบบดั้งเดิม

6.  ในบริบทของการประมาณฟังก์ชันคลื่นในกลศาสตร์ควอนตัม การใช้ Deep Learning มีข้อดีอย่างไรเมื่อเทียบกับวิธีการคำนวณแบบดั้งเดิม?

7.  หากคุณกำลังออกแบบโครงข่ายประสาทเทียมเพื่อจำแนกประเภทของอนุภาคฟิสิกส์จากข้อมูลการชนกันของอนุภาค คุณจะเลือกฟังก์ชันกระตุ้นใดสำหรับชั้นเอาต์พุต และเพราะเหตุใด?

8.  จงออกแบบสถาปัตยกรรม Deep Neural Network อย่างง่าย (ระบุจำนวนชั้น, จำนวนเซลล์ประสาทในแต่ละชั้น, ฟังก์ชันกระตุ้น) สำหรับการทำนายพลังงานของระบบโมเลกุล และอธิบายเหตุผลในการเลือกของคุณ

