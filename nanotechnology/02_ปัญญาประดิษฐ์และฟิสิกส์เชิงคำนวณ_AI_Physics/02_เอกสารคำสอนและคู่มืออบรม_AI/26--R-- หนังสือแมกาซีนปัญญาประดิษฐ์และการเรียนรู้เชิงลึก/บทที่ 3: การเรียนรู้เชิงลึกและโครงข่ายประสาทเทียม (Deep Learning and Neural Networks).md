# บทที่ 3: การเรียนรู้เชิงลึกและโครงข่ายประสาทเทียม (Deep Learning and Neural Networks)

## 3.1 Deep Learning คืออะไร?

Deep Learning หรือการเรียนรู้เชิงลึก เป็นสาขาหนึ่งของ Machine Learning ที่ใช้โครงข่ายประสาทเทียม (Neural Networks) ที่มีหลายชั้น (Multiple Layers) เพื่อเรียนรู้รูปแบบที่ซับซ้อนจากข้อมูล

### คำนิยามของ Deep Learning

**Deep Learning** คือ วิธีการเรียนรู้ของเครื่องที่ใช้โครงข่ายประสาทเทียมที่มีความลึก (มากกว่า 3 ชั้น) เพื่อจำลองการทำงานของสมองมนุษย์ในการประมวลผลข้อมูล

### ความแตกต่างระหว่าง Machine Learning และ Deep Learning

#### Traditional Machine Learning:
- ต้องการการแยกคุณสมบัติ (Feature Extraction) ด้วยมือ
- ใช้อัลกอริทึมที่ค่อนข้างง่าย
- เหมาะสำหรับข้อมูลที่มีโครงสร้างชัดเจน
- ต้องการข้อมูลน้อยกว่า

#### Deep Learning:
- เรียนรู้คุณสมบัติจากข้อมูลเองโดยอัตโนมัติ
- ใช้โครงข่ายประสาทเทียมที่ซับซ้อน
- เหมาะสำหรับข้อมูลที่ไม่มีโครงสร้าง (ภาพ, เสียง, ข้อความ)
- ต้องการข้อมูลจำนวนมาก

### ทำไม Deep Learning จึงสำคัญ?

#### 1. ความสามารถในการเรียนรู้อัตโนมัติ
- ไม่ต้องกำหนดคุณสมบัติล่วงหน้า
- ระบบเรียนรู้รูปแบบที่ซับซ้อนได้เอง
- สามารถจัดการข้อมูลที่หลากหลาย

#### 2. ประสิทธิภาพที่สูง
- ให้ผลลัพธ์ที่แม่นยำมากในหลายงาน
- เหนือกว่าวิธีการแบบเดิมในหลายด้าน
- ปรับปรุงได้ต่อเนื่องเมื่อมีข้อมูลเพิ่ม

#### 3. การประยุกต์ใช้ที่กว้างขวาง
- Computer Vision (การมองเห็นของคอมพิวเตอร์)
- Natural Language Processing (การประมวลผลภาษาธรรมชาติ)
- Speech Recognition (การรู้จำเสียง)
- Robotics (หุ่นยนต์)

## 3.2 โครงข่ายประสาทเทียม (Neural Networks)

### 3.2.1 แรงบันดาลใจจากสมองมนุษย์

โครงข่ายประสาทเทียมได้แรงบันดาลใจมาจากการทำงานของเซลล์ประสาท (Neurons) ในสมองมนุษย์

#### เซลล์ประสาทในสมองมนุษย์:
- **Dendrites**: รับสัญญาณจากเซลล์อื่น
- **Cell Body**: ประมวลผลสัญญาณ
- **Axon**: ส่งสัญญาณออกไป
- **Synapses**: จุดเชื่อมต่อระหว่างเซลล์

#### Artificial Neuron (เซลล์ประสาทเทียม):
- **Inputs**: รับข้อมูลเข้า (เหมือน Dendrites)
- **Weights**: น้ำหนักของการเชื่อมต่อ (เหมือน Synapses)
- **Activation Function**: ฟังก์ชันกระตุ้น (เหมือน Cell Body)
- **Output**: ส่งผลลัพธ์ออก (เหมือน Axon)

### 3.2.2 โครงสร้างของ Neural Network

#### 1. Input Layer (ชั้นข้อมูลเข้า)
- รับข้อมูลจากภายนอก
- จำนวน Neuron = จำนวนคุณสมบัติของข้อมูล
- ไม่มีการประมวลผล เพียงส่งต่อข้อมูล

#### 2. Hidden Layer (ชั้นซ่อน)
- ประมวลผลข้อมูลจาก Input Layer
- สามารถมีได้หลายชั้น
- ยิ่งมีมากชั้น = Deep Network

#### 3. Output Layer (ชั้นผลลัพธ์)
- ให้ผลลัพธ์สุดท้าย
- จำนวน Neuron ขึ้นอยู่กับประเภทปัญหา
- Classification: จำนวน Class
- Regression: 1 Neuron

### 3.2.3 การทำงานของ Neuron

#### สมการของ Neuron:
```
Output = Activation_Function(Σ(Input_i × Weight_i) + Bias)
```

#### ตัวอย่างการคำนวณ:
```python
import numpy as np

def sigmoid(x):
    """Sigmoid activation function"""
    return 1 / (1 + np.exp(-x))

# ตัวอย่าง Neuron
inputs = np.array([0.5, 0.3, 0.2])  # ข้อมูลเข้า
weights = np.array([0.4, 0.7, -0.2])  # น้ำหนัก
bias = 0.1  # ค่าคงที่

# คำนวณ
weighted_sum = np.dot(inputs, weights) + bias
output = sigmoid(weighted_sum)

print(f"Weighted Sum: {weighted_sum:.3f}")
print(f"Output: {output:.3f}")
```

### 3.2.4 Activation Functions (ฟังก์ชันกระตุ้น)

#### 1. Sigmoid Function
- **สมการ**: σ(x) = 1/(1 + e^(-x))
- **ช่วงค่า**: 0 ถึง 1
- **ข้อดี**: เหมาะสำหรับ Binary Classification
- **ข้อเสีย**: Vanishing Gradient Problem

#### 2. ReLU (Rectified Linear Unit)
- **สมการ**: f(x) = max(0, x)
- **ช่วงค่า**: 0 ถึง ∞
- **ข้อดี**: คำนวณเร็ว, แก้ปัญหา Vanishing Gradient
- **ข้อเสีย**: Dead Neuron Problem

#### 3. Tanh (Hyperbolic Tangent)
- **สมการ**: tanh(x) = (e^x - e^(-x))/(e^x + e^(-x))
- **ช่วงค่า**: -1 ถึง 1
- **ข้อดี**: Zero-centered
- **ข้อเสีย**: ยังมี Vanishing Gradient

#### 4. Leaky ReLU
- **สมการ**: f(x) = max(0.01x, x)
- **ข้อดี**: แก้ปัญหา Dead Neuron
- **การใช้งาน**: ทางเลือกแทน ReLU

```python
import numpy as np
import matplotlib.pyplot as plt

def plot_activation_functions():
    x = np.linspace(-5, 5, 100)
    
    # Activation functions
    sigmoid = 1 / (1 + np.exp(-x))
    relu = np.maximum(0, x)
    tanh = np.tanh(x)
    leaky_relu = np.where(x > 0, x, 0.01 * x)
    
    # Plot
    fig, axes = plt.subplots(2, 2, figsize=(12, 10))
    fig.suptitle('Activation Functions', fontsize=16)
    
    axes[0,0].plot(x, sigmoid, 'b-', linewidth=2)
    axes[0,0].set_title('Sigmoid')
    axes[0,0].grid(True)
    
    axes[0,1].plot(x, relu, 'r-', linewidth=2)
    axes[0,1].set_title('ReLU')
    axes[0,1].grid(True)
    
    axes[1,0].plot(x, tanh, 'g-', linewidth=2)
    axes[1,0].set_title('Tanh')
    axes[1,0].grid(True)
    
    axes[1,1].plot(x, leaky_relu, 'm-', linewidth=2)
    axes[1,1].set_title('Leaky ReLU')
    axes[1,1].grid(True)
    
    plt.tight_layout()
    plt.show()

# plot_activation_functions()
```

## 3.3 การฝึกโครงข่ายประสาทเทียม

### 3.3.1 Forward Propagation (การส่งผ่านไปข้างหน้า)

เป็นกระบวนการส่งข้อมูลจาก Input Layer ไปยัง Output Layer

#### ขั้นตอน:
1. ข้อมูลเข้าสู่ Input Layer
2. คำนวณผ่านแต่ละ Hidden Layer
3. ได้ผลลัพธ์ที่ Output Layer
4. เปรียบเทียบกับคำตอบที่ถูกต้อง

```python
class SimpleNeuralNetwork:
    def __init__(self, input_size, hidden_size, output_size):
        # สุ่มน้ำหนักเริ่มต้น
        self.W1 = np.random.randn(input_size, hidden_size) * 0.5
        self.b1 = np.zeros((1, hidden_size))
        self.W2 = np.random.randn(hidden_size, output_size) * 0.5
        self.b2 = np.zeros((1, output_size))
    
    def sigmoid(self, x):
        return 1 / (1 + np.exp(-np.clip(x, -500, 500)))
    
    def forward(self, X):
        # Hidden Layer
        self.z1 = np.dot(X, self.W1) + self.b1
        self.a1 = self.sigmoid(self.z1)
        
        # Output Layer
        self.z2 = np.dot(self.a1, self.W2) + self.b2
        self.a2 = self.sigmoid(self.z2)
        
        return self.a2
```

### 3.3.2 Loss Function (ฟังก์ชันความผิดพลาด)

ใช้วัดความแตกต่างระหว่างผลลัพธ์ที่ทำนายและคำตอบที่ถูกต้อง

#### 1. Mean Squared Error (MSE) - สำหรับ Regression
```
MSE = (1/n) × Σ(y_true - y_pred)²
```

#### 2. Cross-Entropy Loss - สำหรับ Classification
```
Cross-Entropy = -Σ(y_true × log(y_pred))
```

### 3.3.3 Backpropagation (การส่งผ่านกลับ)

เป็นอัลกอริทึมสำหรับปรับปรุงน้ำหนักของโครงข่าย

#### หลักการ:
1. คำนวณ Error จาก Output Layer
2. ส่ง Error กลับไปยัง Hidden Layers
3. ปรับปรุงน้ำหนักตาม Gradient
4. ทำซ้ำจนกว่าจะได้ผลลัพธ์ที่ต้องการ

#### สมการการปรับปรุงน้ำหนัก:
```
Weight_new = Weight_old - Learning_Rate × Gradient
```

```python
def backward(self, X, y, output):
    m = X.shape[0]  # จำนวนตัวอย่าง
    
    # คำนวณ gradient สำหรับ output layer
    dz2 = output - y
    dW2 = (1/m) * np.dot(self.a1.T, dz2)
    db2 = (1/m) * np.sum(dz2, axis=0, keepdims=True)
    
    # คำนวณ gradient สำหรับ hidden layer
    dz1 = np.dot(dz2, self.W2.T) * self.a1 * (1 - self.a1)
    dW1 = (1/m) * np.dot(X.T, dz1)
    db1 = (1/m) * np.sum(dz1, axis=0, keepdims=True)
    
    return dW1, db1, dW2, db2

def update_weights(self, dW1, db1, dW2, db2, learning_rate):
    self.W1 -= learning_rate * dW1
    self.b1 -= learning_rate * db1
    self.W2 -= learning_rate * dW2
    self.b2 -= learning_rate * db2
```

### 3.3.4 Gradient Descent (การลดความชัน)

เป็นอัลกอริทึมสำหรับหาค่าน้ำหนักที่ทำให้ Loss Function มีค่าต่ำที่สุด

#### ประเภทของ Gradient Descent:

##### 1. Batch Gradient Descent
- ใช้ข้อมูลทั้งหมดในการคำนวณ Gradient
- **ข้อดี**: เสถียร, ลู่เข้าสู่ค่าที่แท้จริง
- **ข้อเสีย**: ช้า, ใช้หน่วยความจำมาก

##### 2. Stochastic Gradient Descent (SGD)
- ใช้ข้อมูลทีละตัวอย่าง
- **ข้อดี**: เร็ว, ใช้หน่วยความจำน้อย
- **ข้อเสีย**: ไม่เสถียร, อาจไม่ลู่เข้า

##### 3. Mini-batch Gradient Descent
- ใช้ข้อมูลเป็นกลุ่มย่อย (เช่น 32, 64, 128 ตัวอย่าง)
- **ข้อดี**: สมดุลระหว่างความเร็วและความเสถียร
- **การใช้งาน**: นิยมใช้มากที่สุด

## 3.4 ประเภทของ Deep Learning Networks

### 3.4.1 Feedforward Neural Networks (FNN)

เป็นโครงข่ายพื้นฐานที่ข้อมูลไหลในทิศทางเดียว

#### ลักษณะ:
- ข้อมูลไหลจาก Input → Hidden → Output
- ไม่มีการวนกลับ (No Loops)
- เหมาะสำหรับปัญหาทั่วไป

#### การใช้งานในการเกษตร:
- ทำนายผลผลิตจากข้อมูลสภาพอากาศ
- จำแนกคุณภาพดินจากค่าทางเคมี
- ประมาณราคาสินค้าเกษตร

### 3.4.2 Convolutional Neural Networks (CNN)

เป็นโครงข่ายที่เชี่ยวชาญด้านการประมวลผลภาพ

#### ส่วนประกอบหลัก:

##### 1. Convolutional Layer
- ใช้ Filter (Kernel) สแกนภาพ
- ตรวจจับคุณสมบัติเฉพาะ (edges, textures, patterns)
- แชร์น้ำหนักเดียวกันทั้งภาพ

##### 2. Pooling Layer
- ลดขนาดของ Feature Map
- Max Pooling: เลือกค่าสูงสุด
- Average Pooling: คำนวณค่าเฉลี่ย

##### 3. Fully Connected Layer
- เชื่อมต่อทุก Neuron กับชั้นถัดไป
- ทำการจำแนกขั้นสุดท้าย

#### การใช้งานในการเกษตร:
- ตรวจจับโรคพืชจากภาพใบไม้
- นับจำนวนผลไม้บนต้น
- แยกแยะวัชพืชจากพืชผล
- วิเคราะห์ภาพถ่ายดาวเทียม

```python
# ตัวอย่าง CNN สำหรับการจำแนกโรคพืช
import tensorflow as tf
from tensorflow.keras import layers, models

def create_plant_disease_cnn():
    model = models.Sequential([
        # Convolutional layers
        layers.Conv2D(32, (3, 3), activation='relu', input_shape=(224, 224, 3)),
        layers.MaxPooling2D((2, 2)),
        
        layers.Conv2D(64, (3, 3), activation='relu'),
        layers.MaxPooling2D((2, 2)),
        
        layers.Conv2D(128, (3, 3), activation='relu'),
        layers.MaxPooling2D((2, 2)),
        
        # Fully connected layers
        layers.Flatten(),
        layers.Dense(512, activation='relu'),
        layers.Dropout(0.5),
        layers.Dense(3, activation='softmax')  # 3 classes: healthy, disease1, disease2
    ])
    
    model.compile(
        optimizer='adam',
        loss='categorical_crossentropy',
        metrics=['accuracy']
    )
    
    return model

# สร้างโมเดล
# model = create_plant_disease_cnn()
# print(model.summary())
```

### 3.4.3 Recurrent Neural Networks (RNN)

เป็นโครงข่ายที่เหมาะสำหรับข้อมูลที่มีลำดับเวลา

#### ลักษณะพิเศษ:
- มี Memory เก็บข้อมูลจากอดีต
- เหมาะสำหรับ Time Series Data
- สามารถจัดการข้อมูลที่มีความยาวต่างกัน

#### ปัญหาของ RNN ธรรมดา:
- **Vanishing Gradient**: ข้อมูลเก่าหายไป
- **Exploding Gradient**: Gradient มีค่าสูงเกินไป

#### การแก้ไขด้วย LSTM และ GRU:

##### LSTM (Long Short-Term Memory)
- มี Gate ควบคุมการเก็บและลืมข้อมูล
- **Forget Gate**: ตัดสินใจว่าจะลืมข้อมูลใด
- **Input Gate**: ตัดสินใจว่าจะเก็บข้อมูลใหม่ใด
- **Output Gate**: ตัดสินใจว่าจะส่งออกข้อมูลใด

#### การใช้งานในการเกษตร:
- พยากรณ์สภาพอากาศ
- ทำนายราคาสินค้าเกษตร
- วิเคราะห์แนวโน้มการเจริญเติบโตของพืช
- ควบคุมระบบชลประทานอัตโนมัติ

```python
# ตัวอย่าง LSTM สำหรับพยากรณ์อุณหภูมิ
def create_weather_prediction_lstm():
    model = models.Sequential([
        layers.LSTM(50, return_sequences=True, input_shape=(30, 1)),  # 30 วันย้อนหลัง
        layers.LSTM(50, return_sequences=False),
        layers.Dense(25),
        layers.Dense(1)  # ทำนายอุณหภูมิวันถัดไป
    ])
    
    model.compile(
        optimizer='adam',
        loss='mean_squared_error',
        metrics=['mae']
    )
    
    return model
```

## 3.5 Deep Learning ในการเกษตร: กรณีศึกษาเชิงลึก

### 3.5.1 การตรวจจับโรคพืชด้วย CNN

#### ปัญหา:
โรคพืชเป็นปัญหาสำคัญที่ทำให้เกษตรกรสูญเสียผลผลิต การตรวจจับด้วยตาเปล่าต้องใช้ความเชี่ยวชาญและอาจไม่ทันเวลา

#### วิธีการแก้ไข:
ใช้ CNN วิเคราะห์ภาพใบไม้เพื่อตรวจจับโรคได้อย่างรวดเร็วและแม่นยำ

#### Dataset ที่ใช้:
- ภาพใบไม้สุขภาพดี: 1,000 ภาพ
- ภาพใบไม้ป่วย (โรค A): 800 ภาพ  
- ภาพใบไม้ป่วย (โรค B): 700 ภาพ

#### ขั้นตอนการพัฒนา:

##### 1. Data Preprocessing
```python
import cv2
import numpy as np
from sklearn.model_selection import train_test_split

def preprocess_plant_images(image_paths, labels):
    """เตรียมข้อมูลภาพใบไม้"""
    images = []
    processed_labels = []
    
    for img_path, label in zip(image_paths, labels):
        # อ่านภาพ
        img = cv2.imread(img_path)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        
        # ปรับขนาด
        img = cv2.resize(img, (224, 224))
        
        # Normalize
        img = img / 255.0
        
        images.append(img)
        processed_labels.append(label)
    
    return np.array(images), np.array(processed_labels)

# Data Augmentation เพื่อเพิ่มข้อมูล
from tensorflow.keras.preprocessing.image import ImageDataGenerator

datagen = ImageDataGenerator(
    rotation_range=20,
    width_shift_range=0.2,
    height_shift_range=0.2,
    horizontal_flip=True,
    zoom_range=0.2,
    fill_mode='nearest'
)
```

##### 2. Model Architecture
```python
def create_advanced_plant_disease_cnn():
    model = models.Sequential([
        # Block 1
        layers.Conv2D(32, (3, 3), activation='relu', input_shape=(224, 224, 3)),
        layers.Conv2D(32, (3, 3), activation='relu'),
        layers.MaxPooling2D((2, 2)),
        layers.Dropout(0.25),
        
        # Block 2
        layers.Conv2D(64, (3, 3), activation='relu'),
        layers.Conv2D(64, (3, 3), activation='relu'),
        layers.MaxPooling2D((2, 2)),
        layers.Dropout(0.25),
        
        # Block 3
        layers.Conv2D(128, (3, 3), activation='relu'),
        layers.Conv2D(128, (3, 3), activation='relu'),
        layers.MaxPooling2D((2, 2)),
        layers.Dropout(0.25),
        
        # Classifier
        layers.Flatten(),
        layers.Dense(512, activation='relu'),
        layers.Dropout(0.5),
        layers.Dense(3, activation='softmax')  # 3 classes
    ])
    
    return model
```

##### 3. Training และ Evaluation
```python
# สร้างและฝึกโมเดล
model = create_advanced_plant_disease_cnn()
model.compile(
    optimizer='adam',
    loss='categorical_crossentropy',
    metrics=['accuracy']
)

# ฝึกโมเดล
history = model.fit(
    datagen.flow(X_train, y_train, batch_size=32),
    steps_per_epoch=len(X_train) // 32,
    epochs=50,
    validation_data=(X_test, y_test),
    verbose=1
)

# ประเมินผล
test_loss, test_accuracy = model.evaluate(X_test, y_test, verbose=0)
print(f"Test Accuracy: {test_accuracy:.4f}")
```

#### ผลลัพธ์ที่คาดหวัง:
- ความแม่นยำ: 92-95%
- เวลาในการตรวจจับ: < 1 วินาที
- สามารถใช้งานบนมือถือได้

### 3.5.2 การพยากรณ์ผลผลิตด้วย LSTM

#### ปัญหา:
เกษตรกรต้องการทราบล่วงหน้าว่าจะได้ผลผลิตเท่าไหร่ เพื่อวางแผนการขายและการจัดการ

#### วิธีการแก้ไข:
ใช้ LSTM วิเคราะห์ข้อมูลอนุกรมเวลาเพื่อทำนายผลผลิต

#### ข้อมูลที่ใช้:
- ข้อมูลสภาพอากาศรายวัน (อุณหภูมิ, ฝน, ความชื้น)
- ข้อมูลการจัดการ (ปุ่ย, ยาฆ่าแมลง, การรดน้ำ)
- ข้อมูลดิน (pH, ธาตุอาหาร)
- ข้อมูลผลผลิตในอดีต

```python
def create_yield_prediction_model():
    """สร้างโมเดลทำนายผลผลิต"""
    
    # Input layers สำหรับข้อมูลต่างๆ
    weather_input = layers.Input(shape=(30, 4), name='weather')  # 30 วัน, 4 features
    soil_input = layers.Input(shape=(5,), name='soil')  # 5 soil features
    management_input = layers.Input(shape=(30, 3), name='management')  # 30 วัน, 3 features
    
    # LSTM สำหรับข้อมูลสภาพอากาศ
    weather_lstm = layers.LSTM(64, return_sequences=False)(weather_input)
    
    # LSTM สำหรับข้อมูลการจัดการ
    management_lstm = layers.LSTM(32, return_sequences=False)(management_input)
    
    # Dense สำหรับข้อมูลดิน
    soil_dense = layers.Dense(16, activation='relu')(soil_input)
    
    # รวมข้อมูลทั้งหมด
    combined = layers.concatenate([weather_lstm, management_lstm, soil_dense])
    
    # Hidden layers
    x = layers.Dense(128, activation='relu')(combined)
    x = layers.Dropout(0.3)(x)
    x = layers.Dense(64, activation='relu')(x)
    x = layers.Dropout(0.2)(x)
    
    # Output
    output = layers.Dense(1, activation='linear', name='yield')(x)
    
    model = models.Model(
        inputs=[weather_input, soil_input, management_input],
        outputs=output
    )
    
    return model

# สร้างและคอมไพล์โมเดล
model = create_yield_prediction_model()
model.compile(
    optimizer='adam',
    loss='mse',
    metrics=['mae']
)
```

### 3.5.3 การวิเคราะห์ภาพดาวเทียมด้วย CNN

#### ปัญหา:
การตรวจสอบพื้นที่เกษตรขนาดใหญ่ด้วยคนใช้เวลานานและมีต้นทุนสูง

#### วิธีการแก้ไข:
ใช้ CNN วิเคราะห์ภาพดาวเทียมเพื่อตรวจสอบสุขภาพพืช พื้นที่เพาะปลูก และการใช้ประโยชน์ที่ดิน

#### การประยุกต์ใช้:
1. **การตรวจสอบสุขภาพพืช**
   - วิเคราะห์ค่า NDVI (Normalized Difference Vegetation Index)
   - ตรวจจับพื้นที่ที่พืชเจริญเติบโตไม่ดี
   - ประเมินความเครียดของพืช

2. **การประมาณผลผลิต**
   - นับจำนวนต้นไม้จากภาพ
   - ประมาณขนาดของผลไม้
   - คาดการณ์ปริมาณผลผลิต

3. **การตรวจสอบการใช้ที่ดิน**
   - จำแนกประเภทการใช้ที่ดิน
   - ตรวจจับการเปลี่ยนแปลงของพื้นที่
   - ติดตามการขยายตัวของเมือง

```python
def create_satellite_analysis_cnn():
    """สร้างโมเดลวิเคราะห์ภาพดาวเทียม"""
    
    model = models.Sequential([
        # Encoder (Feature Extraction)
        layers.Conv2D(64, (3, 3), activation='relu', input_shape=(256, 256, 4)),  # RGB + NIR
        layers.Conv2D(64, (3, 3), activation='relu'),
        layers.MaxPooling2D((2, 2)),
        
        layers.Conv2D(128, (3, 3), activation='relu'),
        layers.Conv2D(128, (3, 3), activation='relu'),
        layers.MaxPooling2D((2, 2)),
        
        layers.Conv2D(256, (3, 3), activation='relu'),
        layers.Conv2D(256, (3, 3), activation='relu'),
        layers.MaxPooling2D((2, 2)),
        
        # Decoder (Segmentation)
        layers.Conv2DTranspose(256, (3, 3), strides=(2, 2), activation='relu'),
        layers.Conv2D(128, (3, 3), activation='relu'),
        
        layers.Conv2DTranspose(128, (3, 3), strides=(2, 2), activation='relu'),
        layers.Conv2D(64, (3, 3), activation='relu'),
        
        layers.Conv2DTranspose(64, (3, 3), strides=(2, 2), activation='relu'),
        layers.Conv2D(32, (3, 3), activation='relu'),
        
        # Output (Land Use Classification)
        layers.Conv2D(5, (1, 1), activation='softmax')  # 5 classes: crop, forest, water, urban, bare
    ])
    
    return model
```

## 3.6 เครื่องมือและไลบรารีสำหรับ Deep Learning

### 3.6.1 TensorFlow และ Keras

#### TensorFlow:
- พัฒนาโดย Google
- เป็น Low-level framework
- เหมาะสำหรับการวิจัยและการใช้งานขนาดใหญ่

#### Keras:
- High-level API ของ TensorFlow
- ใช้งานง่าย เหมาะสำหรับผู้เริ่มต้น
- มี Pre-trained models มากมาย

```python
# ตัวอย่างการใช้ Keras
import tensorflow as tf
from tensorflow import keras

# โหลด pre-trained model
base_model = keras.applications.VGG16(
    weights='imagenet',
    include_top=False,
    input_shape=(224, 224, 3)
)

# ปรับแต่งสำหรับงานเฉพาะ
model = keras.Sequential([
    base_model,
    keras.layers.GlobalAveragePooling2D(),
    keras.layers.Dense(128, activation='relu'),
    keras.layers.Dense(3, activation='softmax')  # 3 plant diseases
])

# Freeze base model
base_model.trainable = False

model.compile(
    optimizer='adam',
    loss='categorical_crossentropy',
    metrics=['accuracy']
)
```

### 3.6.2 PyTorch

#### ข้อดี:
- Dynamic computation graph
- เหมาะสำหรับการวิจัย
- Community ที่แข็งแกร่ง

#### ตัวอย่างการใช้:
```python
import torch
import torch.nn as nn
import torch.optim as optim

class PlantDiseaseNet(nn.Module):
    def __init__(self, num_classes=3):
        super(PlantDiseaseNet, self).__init__()
        
        self.features = nn.Sequential(
            nn.Conv2d(3, 64, kernel_size=3, padding=1),
            nn.ReLU(inplace=True),
            nn.MaxPool2d(kernel_size=2, stride=2),
            
            nn.Conv2d(64, 128, kernel_size=3, padding=1),
            nn.ReLU(inplace=True),
            nn.MaxPool2d(kernel_size=2, stride=2),
        )
        
        self.classifier = nn.Sequential(
            nn.Linear(128 * 56 * 56, 512),
            nn.ReLU(inplace=True),
            nn.Dropout(0.5),
            nn.Linear(512, num_classes)
        )
    
    def forward(self, x):
        x = self.features(x)
        x = x.view(x.size(0), -1)
        x = self.classifier(x)
        return x

# สร้างโมเดล
model = PlantDiseaseNet(num_classes=3)
criterion = nn.CrossEntropyLoss()
optimizer = optim.Adam(model.parameters(), lr=0.001)
```

### 3.6.3 Google Colab

#### ข้อดี:
- ใช้ GPU ฟรี
- ไม่ต้องติดตั้งอะไร
- แชร์งานได้ง่าย

#### การใช้งาน:
1. ไปที่ colab.research.google.com
2. สร้าง Notebook ใหม่
3. เปลี่ยนเป็น GPU Runtime
4. เริ่มเขียนโค้ด

## 3.7 ความท้าทายและข้อจำกัดของ Deep Learning

### 3.7.1 ความต้องการข้อมูลจำนวนมาก

#### ปัญหา:
- Deep Learning ต้องการข้อมูลหลายแสนถึงหลายล้านตัวอย่าง
- ข้อมูลการเกษตรมักมีจำกัด
- การติด Label ใช้เวลาและต้นทุนสูง

#### วิธีแก้ไข:
1. **Data Augmentation**: เพิ่มข้อมูลด้วยการแปลงภาพ
2. **Transfer Learning**: ใช้โมเดลที่ฝึกแล้ว
3. **Synthetic Data**: สร้างข้อมูลจำลอง
4. **Few-shot Learning**: เรียนรู้จากข้อมูลน้อย

### 3.7.2 การใช้ทรัพยากรคอมพิวเตอร์สูง

#### ปัญหา:
- ต้องการ GPU ที่มีประสิทธิภาพสูง
- ใช้เวลาฝึกนานหลายชั่วโมงหรือหลายวัน
- ใช้หน่วยความจำมาก

#### วิธีแก้ไข:
1. **Cloud Computing**: ใช้ AWS, Google Cloud, Azure
2. **Model Compression**: ลดขนาดโมเดล
3. **Quantization**: ลดความแม่นยำของตัวเลข
4. **Edge Computing**: ประมวลผลบนอุปกรณ์

### 3.7.3 Black Box Problem

#### ปัญหา:
- ไม่สามารถอธิบายได้ว่าโมเดลตัดสินใจอย่างไร
- ยากต่อการตรวจสอบความถูกต้อง
- เกษตรกรอาจไม่เชื่อถือ

#### วิธีแก้ไข:
1. **Explainable AI (XAI)**: สร้างโมเดลที่อธิบายได้
2. **Visualization**: แสดงส่วนที่โมเดลให้ความสำคัญ
3. **LIME/SHAP**: เครื่องมือสำหรับอธิบายโมเดล

## 3.8 กิจกรรมและแบบฝึกหัด

### กิจกรรมที่ 1: สร้าง Neural Network ง่ายๆ

**วัตถุประสงค์**: ให้นักเรียนเข้าใจการทำงานของ Neural Network

**อุปกรณ์**: คอมพิวเตอร์, Python, ข้อมูลการเกษตร

**ขั้นตอน**:
1. สร้าง Neural Network 3 ชั้น (Input-Hidden-Output)
2. ใช้ข้อมูลการทำนายผลผลิตข้าว
3. ฝึกโมเดลและดูการเปลี่ยนแปลงของ Loss
4. ทดสอบการทำนายกับข้อมูลใหม่
5. วิเคราะห์ผลลัพธ์

### กิจกรรมที่ 2: การจำแนกภาพใบไม้

**วัตถุประสงค์**: ให้นักเรียนเข้าใจ CNN และ Computer Vision

**อุปกรณ์**: มือถือ, คอมพิวเตอร์, ใบไม้ต่างๆ

**ขั้นตอน**:
1. ถ่ายภาพใบไม้ 3 ชนิด (ชนิดละ 50 ภาพ)
2. แบ่งข้อมูลเป็น Training และ Testing
3. สร้าง CNN ด้วย Keras
4. ฝึกโมเดลและประเมินความแม่นยำ
5. ทดสอบกับภาพใหม่

### กิจกรรมที่ 3: การพยากรณ์สภาพอากาศ

**วัตถุประสงค์**: ให้นักเรียนเข้าใจ RNN และ Time Series

**อุปกรณ์**: ข้อมูลสภาพอากาศ, Python

**ขั้นตอน**:
1. รวบรวมข้อมูลอุณหภูมิรายวัน 1 ปี
2. เตรียมข้อมูลสำหรับ LSTM
3. สร้างโมเดล LSTM
4. ฝึกโมเดลเพื่อทำนายอุณหภูมิวันถัดไป
5. ประเมินความแม่นยำของการทำนาย

### โครงงานกลุ่ม: ระบบตรวจจับโรคพืชอัจฉริยะ

**วัตถุประสงค์**: ประยุกต์ Deep Learning เพื่อแก้ปัญหาจริง

**ขั้นตอน**:
1. **การวิเคราะห์ปัญหา**: สำรวจโรคพืชที่พบบ่อยในชุมชน
2. **การรวบรวมข้อมูล**: ถ่ายภาพใบไม้สุขภาพดีและป่วย
3. **การสร้างโมเดล**: ใช้ CNN จำแนกโรคพืช
4. **การทดสอบ**: ทดสอบกับข้อมูลจริงในไร่
5. **การนำเสนอ**: สร้างแอปมือถือง่ายๆ

## สรุป

บทที่ 3 นี้เราได้เรียนรู้เกี่ยวกับ Deep Learning และ Neural Networks ซึ่งเป็นเทคโนโลยีที่กำลังปฏิวัติโลกการเกษตร เราได้ทำความเข้าใจกับโครงสร้างและการทำงานของโครงข่ายประสาทเทียม รวมถึงการประยุกต์ใช้ในงานต่างๆ

**จุดสำคัญที่ต้องจำ**:
- Deep Learning ใช้โครงข่ายประสาทเทียมหลายชั้นเรียนรู้รูปแบบซับซ้อน
- CNN เหมาะสำหรับการประมวลผลภาพ
- RNN/LSTM เหมาะสำหรับข้อมูลอนุกรมเวลา
- Deep Learning ต้องการข้อมูลจำนวนมากและทรัพยากรคอมพิวเตอร์สูง
- มีศักยภาพมากในการแก้ปัญหาการเกษตรที่ซับซ้อน

ในบทถัดไป เราจะเจาะลึกเข้าไปในโลกของ Computer Vision ซึ่งเป็นการประยุกต์ใช้ Deep Learning เพื่อให้คอมพิวเตอร์สามารถ "มองเห็น" และเข้าใจภาพได้เหมือนมนุษย์

