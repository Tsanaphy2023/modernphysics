import React from 'react';
import { Accordion, AccordionContent, AccordionItem, AccordionTrigger } from "@/components/ui/accordion";
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { Label } from "@/components/ui/label";
import { Tabs, TabsContent, TabsList, TabsTrigger } from "@/components/ui/tabs";

const Chapter8Enhanced = () => {
  return (
    <div className="container mx-auto p-6 space-y-8">
      <h1 className="text-4xl font-bold text-center mb-10">บทที่ 8: การค้นพบสมการเชิงฟิสิกส์ด้วย AI (AI-driven Discovery of Physical Laws)</h1>

      <section className="space-y-4">
        <h2 className="text-3xl font-semibold">วัตถุประสงค์</h2>
        <ul className="list-disc list-inside space-y-2">
          <li>เรียนรู้แนวคิดของการใช้ AI ในการค้นหาสมการทางคณิตศาสตร์จากข้อมูล</li>
          <li>เข้าใจอัลกอริทึม Symbolic Regression และ Physics-Informed Neural Networks</li>
          <li>ประยุกต์ใช้ในการค้นพบกฎทางฟิสิกส์และการแก้สมการเชิงอนุพันธ์</li>
        </ul>
      </section>

      <section className="space-y-6">
        <h2 className="text-3xl font-semibold">8.1 การถดถอยเชิงสัญลักษณ์ (Symbolic Regression): หลักการและอัลกอริทึม</h2>
        <Card>
          <CardHeader>
            <CardTitle>ทฤษฎี</CardTitle>
          </CardHeader>
          <CardContent>
            <p>อธิบายแนวคิดของ Symbolic Regression ที่เป็นการค้นหาสมการคณิตศาสตร์ที่เหมาะสมที่สุดกับข้อมูล แทนที่จะเป็นการหาค่าพารามิเตอร์ของสมการที่กำหนดไว้แล้ว</p>
          </CardContent>
        </Card>
        <Card>
          <CardHeader>
            <CardTitle>อัลกอริทึม</CardTitle>
          </CardHeader>
          <CardContent>
            <p>แนะนำอัลกอริทึมพื้นฐาน เช่น Genetic Programming</p>
          </CardContent>
        </Card>
      </section>

      <section className="space-y-6">
        <h2 className="text-3xl font-semibold">8.2 Genetic Programming และ Evolutionary Algorithms สำหรับการค้นหาสมการ</h2>
        <Card>
          <CardHeader>
            <CardTitle>ทฤษฎี</CardTitle>
          </CardHeader>
          <CardContent>
            <p>อธิบายหลักการทำงานของ Genetic Programming ที่ใช้แนวคิดของการคัดเลือกทางธรรมชาติเพื่อพัฒนารุ่นของสมการที่ดีขึ้นเรื่อยๆ</p>
          </CardContent>
        </Card>
        <Card>
          <CardHeader>
            <CardTitle>ตัวอย่าง</CardTitle>
          </CardHeader>
          <CardContent>
            <p>แสดงตัวอย่างการใช้ Genetic Programming เพื่อค้นหาสมการการเคลื่อนที่ของวัตถุจากข้อมูลตำแหน่งและความเร็ว</p>
            <div className="bg-gray-100 p-4 rounded-md font-mono text-sm">
              <pre><code>
# ตัวอย่างโค้ด Genetic Programming (Conceptual)
# เนื่องจาก Genetic Programming มีความซับซ้อนและต้องใช้ไลบรารีเฉพาะ
# โค้ดนี้จึงเป็นแนวคิดเพื่อแสดงหลักการทำงาน

import numpy as np
from gplearn.genetic import SymbolicRegressor

# สร้างข้อมูลตัวอย่าง: y = 2*x^2 + 3*x + 1
x = np.linspace(-5, 5, 100).reshape(-1, 1)
y = 2 * x**2 + 3 * x + 1 + np.random.normal(0, 0.5, 100).reshape(-1, 1)

# กำหนดฟังก์ชันทางคณิตศาสตร์ที่ใช้ได้
function_set = ['add', 'sub', 'mul', 'div', 'sqrt', 'log', 'abs', 'neg', 'inv']

# สร้าง SymbolicRegressor model
est_gp = SymbolicRegressor(population_size=5000,
                           generations=20,
                           tournament_size=20,
                           stopping_criteria=0.01,
                           function_set=function_set,
                           metric='mse',
                           p_crossover=0.7,
                           p_subtree_mutation=0.1,
                           p_hoist_mutation=0.05,
                           p_point_mutation=0.1,
                           verbose=1,
                           random_state=0)

# ฝึกโมเดล
est_gp.fit(x, y)

# แสดงสมการที่ค้นพบ
print("\\nสมการที่ค้นพบ:", est_gp._program)

# ประเมินประสิทธิภาพ
y_pred = est_gp.predict(x)
mse = np.mean((y - y_pred)**2)
print("Mean Squared Error:", mse)
              </code></pre>
            </div>
          </CardContent>
        </Card>
      </section>

      <section className="space-y-6">
        <h2 className="text-3xl font-semibold">8.3 Physics-Informed Neural Networks (PINNs): การรวมความรู้ทางฟิสิกส์เข้ากับ AI</h2>
        <Card>
          <CardHeader>
            <CardTitle>ทฤษฎี</CardTitle>
          </CardHeader>
          <CardContent>
            <p>อธิบายแนวคิดของ PINNs ที่เป็นการนำสมการเชิงอนุพันธ์ทางฟิสิกส์มาเป็นส่วนหนึ่งของ Loss Function ในการฝึกสอน Neural Network</p>
          </CardContent>
        </Card>
        <Card>
          <CardHeader>
            <CardTitle>ข้อดี</CardTitle>
          </CardHeader>
          <CardContent>
            <p>ชี้ให้เห็นข้อดีของ PINNs ในการแก้ปัญหาที่มีข้อมูลน้อย แต่มีความรู้ทางฟิสิกส์ที่ชัดเจน</p>
            <div className="bg-gray-100 p-4 rounded-md font-mono text-sm">
              <pre><code>
# ตัวอย่างโค้ด PINNs (Conceptual)
# การใช้งาน PINNs มักจะใช้ไลบรารีเฉพาะทาง เช่น DeepXDE หรือ TensorFlow/PyTorch
# โค้ดนี้เป็นแนวคิดเพื่อแสดงหลักการ

import tensorflow as tf
import numpy as np

# สมมติสมการเชิงอนุพันธ์: du/dt = -k * u (การสลายตัวแบบเอกซ์โพเนนเชียล)
k = 0.1 # ค่าคงที่การสลายตัว

# สร้าง Neural Network
def create_nn():
    model = tf.keras.Sequential([
        tf.keras.layers.Dense(20, activation='tanh', input_shape=(1,)),
        tf.keras.layers.Dense(20, activation='tanh'),
        tf.keras.layers.Dense(1, activation=None)
    ])
    return model

model = create_nn()

# กำหนด Loss Function สำหรับ PINNs
def pinn_loss(t_data, u_data, t_physics):
    # Data loss (จากข้อมูลการสังเกต)
    u_pred_data = model(t_data)
    loss_data = tf.reduce_mean(tf.square(u_data - u_pred_data))

    # Physics-informed loss (จากสมการเชิงอนุพันธ์)
    with tf.GradientTape(persistent=True) as tape:
        tape.watch(t_physics)
        u_pred_physics = model(t_physics)
        du_dt = tape.gradient(u_pred_physics, t_physics)
    
    loss_physics = tf.reduce_mean(tf.square(du_dt + k * u_pred_physics))
    
    del tape
    return loss_data + loss_physics

# ข้อมูลการสังเกต (สมมติ)
t_obs = tf.constant(np.array([[0.0], [1.0], [2.0]]), dtype=tf.float32)
u_obs = tf.constant(np.array([[1.0], [0.9], [0.8]]), dtype=tf.float32)

# จุดสำหรับคำนวณ Physics-informed loss
t_physics = tf.constant(np.linspace(0, 5, 100).reshape(-1, 1), dtype=tf.float32)

# Optimizer
optimizer = tf.keras.optimizers.Adam(learning_rate=0.001)

# Training loop (Conceptual)
epochs = 1000
for epoch in range(epochs):
    with tf.GradientTape() as tape:
        loss = pinn_loss(t_obs, u_obs, t_physics)
    gradients = tape.gradient(loss, model.trainable_variables)
    optimizer.apply_gradients(zip(gradients, model.trainable_variables))
    if epoch % 100 == 0:
        print(f"Epoch {epoch}, Loss: {{loss.numpy():.4f}}")

print("\nPINNs training complete (conceptual).")
              </code></pre>
            </div>
          </CardContent>
        </Card>
      </section>

      <section className="space-y-6">
        <h2 className="text-3xl font-semibold">8.4 การแก้สมการเชิงอนุพันธ์ย่อย (PDEs) ด้วย Deep Learning</h2>
        <Card>
          <CardHeader>
            <CardTitle>ทฤษฎี</CardTitle>
          </CardHeader>
          <CardContent>
            <p>อธิบายวิธีการใช้ Deep Learning ในการประมาณผลเฉลยของ PDEs โดยตรง</p>
          </CardContent>
        </Card>
        <Card>
          <CardHeader>
            <CardTitle>ตัวอย่าง</CardTitle>
          </CardHeader>
          <CardContent>
            <p>แสดงตัวอย่างการแก้สมการความร้อน (Heat Equation) ด้วย Neural Network</p>
            <div className="bg-gray-100 p-4 rounded-md font-mono text-sm">
              <pre><code>
# ตัวอย่างโค้ดการแก้ Heat Equation ด้วย Deep Learning (Conceptual)
# การแก้ PDEs ด้วย DL มักใช้ PINNs หรือโครงข่ายที่ออกแบบมาเฉพาะ
# โค้ดนี้เป็นแนวคิดเพื่อแสดงหลักการ

import torch
import torch.nn as nn
import torch.optim as optim

# สร้าง Neural Network สำหรับประมาณผลเฉลย u(x, t)
class HeatEquationNN(nn.Module):
    def __init__(self):
        super(HeatEquationNN, self).__init__()
        self.net = nn.Sequential(
            nn.Linear(2, 50), # x, t เป็น input
            nn.Tanh(),
            nn.Linear(50, 50),
            nn.Tanh(),
            nn.Linear(50, 1) # u เป็น output
        )

    def forward(self, x, t):
        return self.net(torch.cat([x, t], axis=1))

model = HeatEquationNN()
optimizer = optim.Adam(model.parameters(), lr=0.001)

# Loss function ที่รวมเงื่อนไขขอบเขตและสมการ PDE
def heat_equation_loss(model, x_boundary, t_boundary, u_boundary, x_interior, t_interior):
    # Boundary condition loss (u(x,0) = sin(pi*x))
    u_pred_boundary = model(x_boundary, t_boundary)
    loss_boundary = torch.mean(torch.square(u_pred_boundary - u_boundary))

    # PDE loss (du/dt = d^2u/dx^2)
    x_interior.requires_grad_(True)
    t_interior.requires_grad_(True)
    u_pred_interior = model(x_interior, t_interior)

    grad_u = torch.autograd.grad(u_pred_interior, (x_interior, t_interior), grad_outputs=torch.ones_like(u_pred_interior), create_graph=True)
    du_dx = grad_u[0]
    du_dt = grad_u[1]

    d2u_dx2 = torch.autograd.grad(du_dx, x_interior, grad_outputs=torch.ones_like(du_dx), create_graph=True)[0]

    loss_pde = torch.mean(torch.square(du_dt - d2u_dx2))

    return loss_boundary + loss_pde

# สร้างข้อมูลสำหรับเงื่อนไขขอบเขตและภายในโดเมน (Conceptual)
x_b = torch.linspace(0, 1, 100).reshape(-1, 1)
t_b = torch.zeros_like(x_b)
u_b = torch.sin(torch.pi * x_b)

x_i = torch.rand(1000, 1)
t_i = torch.rand(1000, 1)

# Training loop (Conceptual)
epochs = 1000
for epoch in range(epochs):
    optimizer.zero_grad()
    loss = heat_equation_loss(model, x_b, t_b, u_b, x_i, t_i)
    loss.backward()
    optimizer.step()
    if epoch % 100 == 0:
        print(f"Epoch {epoch}, Loss: {{loss.item():.4f}}")

print("\nDeep Learning for PDEs training complete (conceptual).")
              </code></pre>
            </div>
          </CardContent>
        </Card>
      </section>

      <section className="space-y-6">
        <h2 className="text-3xl font-semibold">8.5 การค้นหาสมการเชิงอนุพันธ์จากข้อมูลการสังเกตการณ์ (SINDy Algorithm)</h2>
        <Card>
          <CardHeader>
            <CardTitle>ทฤษฎี</CardTitle>
          </CardHeader>
          <CardContent>
            <p>อธิบายหลักการของ SINDy (Sparse Identification of Nonlinear Dynamics) ที่ใช้การทำ Sparse Regression เพื่อค้นหาสมการเชิงอนุพันธ์ที่อธิบายพลวัตของระบบ</p>
          </CardContent>
        </Card>
        <Card>
          <CardHeader>
            <CardTitle>ตัวอย่าง</CardTitle>
          </CardHeader>
          <CardContent>
            <p>แสดงการใช้ SINDy เพื่อค้นหาสมการของระบบ Lorenz จากข้อมูลอนุกรมเวลา</p>
            <div className="bg-gray-100 p-4 rounded-md font-mono text-sm">
              <pre><code>
# ตัวอย่างโค้ด SINDy Algorithm (Conceptual)
# SINDy มักใช้ไลบรารี PySINDy

import numpy as np
from scipy.integrate import solve_ivp
from pysindy import SINDy

# สร้างข้อมูลจากระบบ Lorenz
def lorenz(t, x, sigma=10, rho=28, beta=8/3):
    return [sigma * (x[1] - x[0]),
            x[0] * (rho - x[2]) - x[1],
            x[0] * x[1] - beta * x[2]]

dt = 0.001
t_train = np.arange(0, 10, dt)
x0_train = [-8, 8, 27]
sol = solve_ivp(lorenz, (t_train[0], t_train[-1]), x0_train, t_eval=t_train)
x_train = sol.y.T

# สร้าง SINDy model
optimizer = SINDy(optimizer=pysindy.optimizers.STLSQ(threshold=0.1))
optimizer.fit(x_train, t=dt)
optimizer.print_equations()

print("\nSINDy algorithm complete (conceptual).")
              </code></pre>
            </div>
          </CardContent>
        </Card>
      </section>

      <section className="space-y-6">
        <h2 className="text-3xl font-semibold">8.6 การประยุกต์ใช้ในพลศาสตร์ของไหล กลศาสตร์ควอนตัม และเทอร์โมไดนามิกส์</h2>
        <ul className="list-disc list-inside space-y-2">
          <li><strong>พลศาสตร์ของไหล:</strong> การใช้ PINNs แก้สมการ Navier-Stokes</li>
          <li><strong>กลศาสตร์ควอนตัม:</strong> การใช้ PINNs แก้สมการ Schrödinger</li>
          <li><strong>เทอร์โมไดนามิกส์:</strong> การค้นหาสมการสถานะของสสาร</li>
        </ul>
      </section>

      <section className="space-y-6">
        <h2 className="text-3xl font-semibold">8.7 การประเมินและการตรวจสอบความถูกต้องของสมการที่ค้นพบ</h2>
        <Card>
          <CardHeader>
            <CardTitle>เทคนิค</CardTitle>
          </CardHeader>
          <CardContent>
            <p>อธิบายวิธีการตรวจสอบความถูกต้องของสมการที่ค้นพบ เช่น การเปรียบเทียบกับผลการทดลอง การวิเคราะห์ความเสถียร และการตรวจสอบความสอดคล้องกับหลักการพื้นฐานทางฟิสิกส์</p>
          </CardContent>
        </Card>
      </section>

      <section className="space-y-4">
        <h2 className="text-3xl font-semibold">ตัวอย่างงานวิจัย</h2>
        <p>การใช้ PINNs เพื่อแก้สมการนาเวียร์-สโตกส์ในพลศาสตร์ของไหลและสมการชเรอดิงเงอร์ในกลศาสตร์ควอนตัม</p>
      </section>

      <section className="space-y-4">
        <h2 className="text-3xl font-semibold">บทสรุป</h2>
        <p>สรุปแนวโน้มและอนาคตของการใช้ AI เป็นเครื่องมือในการสร้างทฤษฎีทางฟิสิกส์</p>
      </section>

      <section className="space-y-6">
        <h2 className="text-3xl font-semibold">คำถามท้ายบท</h2>
        <Accordion type="single" collapsible className="w-full">
          <AccordionItem value="item-1">
            <AccordionTrigger>1. เปรียบเทียบแนวทางการค้นพบกฎทางฟิสิกส์แบบดั้งเดิมกับแนวทางที่ใช้ Symbolic Regression</AccordionTrigger>
            <AccordionContent>
              <p>แนวทางดั้งเดิมมักอาศัยการสังเกต การทดลอง และการสร้างสมมติฐานทางทฤษฎีโดยมนุษย์ ซึ่งอาจใช้เวลานานและต้องอาศัยความเชี่ยวชาญสูง ในขณะที่ Symbolic Regression ใช้ AI ในการค้นหาสมการจากข้อมูลโดยอัตโนมัติ ซึ่งช่วยลดภาระงานและอาจค้นพบสมการที่มนุษย์คาดไม่ถึงได้</p>
            </AccordionContent>
          </AccordionItem>
          <AccordionItem value="item-2">
            <AccordionTrigger>2. อธิบายวิธีการใส่ "ความรู้ทางฟิสิกส์" เข้าไปในสถาปัตยกรรมของ PINNs</AccordionTrigger>
            <AccordionContent>
              <p>PINNs ใส่ความรู้ทางฟิสิกส์เข้าไปในกระบวนการเรียนรู้โดยการรวมสมการเชิงอนุพันธ์ (PDEs) ที่อธิบายปรากฏการณ์ทางฟิสิกส์เข้าเป็นส่วนหนึ่งของ Loss Function ของ Neural Network ทำให้โมเดลถูกบังคับให้เรียนรู้ผลเฉลยที่สอดคล้องกับกฎทางฟิสิกส์เหล่านั้น นอกเหนือจากการเรียนรู้จากข้อมูลที่มีอยู่</p>
            </AccordionContent>
          </AccordionItem>
          <AccordionItem value="item-3">
            <AccordionTrigger>3. ออกแบบการทดลองเพื่อใช้ SINDy Algorithm ในการค้นหาสมการที่อธิบายการเคลื่อนที่ของลูกตุ้ม</AccordionTrigger>
            <AccordionContent>
              <p>ในการใช้ SINDy Algorithm เพื่อค้นหาสมการการเคลื่อนที่ของลูกตุ้ม เราจะต้องรวบรวมข้อมูลอนุกรมเวลาของตำแหน่งและ/หรือความเร็วของลูกตุ้ม จากนั้นใช้ SINDy เพื่อสร้างไลบรารีของฟังก์ชันที่เป็นไปได้ (เช่น sin, cos, polynomial terms) และใช้ Sparse Regression เพื่อเลือกฟังก์ชันที่สำคัญที่สุดที่อธิบายพลวัตของระบบ ซึ่งจะนำไปสู่การค้นพบสมการเชิงอนุพันธ์ที่ควบคุมการเคลื่อนที่ของลูกตุ้ม</p>
            </AccordionContent>
          </AccordionItem>
        </Accordion>
      </section>
    </div>
  );
};

export default Chapter8Enhanced;

