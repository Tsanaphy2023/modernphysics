# บทที่ 3: การเรียนรู้แบบมีผู้สอน (Supervised Learning) และการประยุกต์ใช้

## วัตถุประสงค์การเรียนรู้
- เข้าใจหลักการทำงานของแบบจำลองการถดถอย (Regression) และการจำแนกประเภท (Classification)
- ประยุกต์ใช้แบบจำลองเพื่อวิเคราะห์ข้อมูลทางฟิสิกส์
- เรียนรู้เทคนิคการประเมินและปรับปรุงประสิทธิภาพของแบบจำลอง

## 3.1 ภาพรวมของการเรียนรู้แบบมีผู้สอน

การเรียนรู้แบบมีผู้สอน (Supervised Learning) เป็นแนวทางการเรียนรู้ของเครื่องที่ใช้ข้อมูลที่มีป้ายกำกับ (labeled data) ในการฝึกสอนแบบจำลอง เพื่อให้สามารถทำนายผลลัพธ์สำหรับข้อมูลใหม่ที่ไม่เคยเห็นมาก่อน

### ประเภทของปัญหา Supervised Learning

**1. การถดถอย (Regression)**
- ทำนายค่าต่อเนื่อง (continuous values)
- ตัวอย่าง: การทำนายอุณหภูมิ, ราคา, พลังงาน

**2. การจำแนกประเภท (Classification)**
- ทำนายหมวดหมู่หรือคลาส (discrete categories)
- ตัวอย่าง: การจำแนกประเภทอนุภาค, การวินิจฉัยโรค

### การแบ่งข้อมูล

ข้อมูลในการเรียนรู้แบบมีผู้สอนจะถูกแบ่งออกเป็น 3 ส่วน:

1. **Training Set (60-70%)**: ใช้สำหรับฝึกสอนแบบจำลอง
2. **Validation Set (15-20%)**: ใช้สำหรับปรับแต่งพารามิเตอร์
3. **Test Set (15-20%)**: ใช้สำหรับประเมินประสิทธิภาพสุดท้าย

### ปัญหา Overfitting และ Underfitting

**Overfitting**: แบบจำลองจำข้อมูลฝึกสอนได้ดีเกินไป แต่ทำงานได้แย่กับข้อมูลใหม่
**Underfitting**: แบบจำลองเรียนรู้ไม่เพียงพอ ทำงานได้แย่ทั้งข้อมูลฝึกสอนและข้อมูลใหม่

## 3.2 Linear Regression และการประยุกต์ใช้

Linear Regression เป็นอัลกอริทึมพื้นฐานสำหรับปัญหาการถดถอย ที่หาความสัมพันธ์เชิงเส้นระหว่างตัวแปรอิสระ (features) และตัวแปรตาม (target)

### สมการ Linear Regression

สำหรับตัวแปรเดียว:
```
y = β₀ + β₁x + ε
```

สำหรับหลายตัวแปร:
```
y = β₀ + β₁x₁ + β₂x₂ + ... + βₙxₙ + ε
```

โดยที่:
- y = ตัวแปรตาม
- x = ตัวแปรอิสระ
- β = สัมประสิทธิ์
- ε = ค่าความผิดพลาด

### วิธี Least Squares

การหาค่าสัมประสิทธิ์ที่ดีที่สุดโดยการลดค่า Sum of Squared Errors (SSE):

```
SSE = Σ(yᵢ - ŷᵢ)²
```

### การประเมินประสิทธิภาพ

**1. R-squared (R²)**
```
R² = 1 - (SSE/TSS)
```
โดยที่ TSS = Total Sum of Squares

**2. Root Mean Square Error (RMSE)**
```
RMSE = √(MSE) = √(SSE/n)
```

**3. Mean Absolute Error (MAE)**
```
MAE = Σ|yᵢ - ŷᵢ|/n
```

### การประยุกต์ใช้ในฟิสิกส์

1. **การหาความสัมพันธ์ระหว่างแรงและการเร่ง**
   - ตรวจสอบกฎข้อที่สองของนิวตัน: F = ma

2. **การวิเคราะห์ข้อมูลการสั่นของลูกตุ้ม**
   - หาความสัมพันธ์ระหว่างความยาวเชือกและคาบการสั่น

3. **การทำนายพลังงานจากตัวแปรทางฟิสิกส์**
   - ใช้ข้อมูลอุณหภูมิ, ความดัน, ปริมาตร ทำนายพลังงานภายใน

## 3.3 Polynomial Regression และ Feature Engineering

### Polynomial Regression

การขยายความสามารถของ Linear Regression ด้วยการเพิ่ม polynomial features:

```
y = β₀ + β₁x + β₂x² + β₃x³ + ... + βₙxⁿ
```

### Feature Engineering

**1. Polynomial Features**
```python
# สร้าง polynomial features
from sklearn.preprocessing import PolynomialFeatures
poly = PolynomialFeatures(degree=2)
X_poly = poly.fit_transform(X)
```

**2. Interaction Terms**
```python
# สร้าง interaction terms
X_interaction = X[:, 0] * X[:, 1]  # x₁ × x₂
```

**3. Feature Scaling**
```python
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
```

### การจัดการกับ Curse of Dimensionality

เมื่อจำนวน features เพิ่มขึ้น อาจเกิดปัญหา:
- Overfitting
- การคำนวณช้า
- ต้องการข้อมูลมากขึ้น

**วิธีแก้ไข:**
- Feature Selection
- Regularization (Ridge, Lasso)
- Dimensionality Reduction (PCA)

## 3.4 Logistic Regression และ Classification

Logistic Regression ใช้สำหรับปัญหา Classification โดยใช้ฟังก์ชัน Sigmoid

### ฟังก์ชัน Sigmoid

```
σ(z) = 1 / (1 + e^(-z))
```

โดยที่ z = β₀ + β₁x₁ + β₂x₂ + ... + βₙxₙ

### Maximum Likelihood Estimation

การหาค่าพารามิเตอร์ที่ดีที่สุดโดยการเพิ่มค่า likelihood:

```
L(β) = Π[p(xᵢ)^yᵢ × (1-p(xᵢ))^(1-yᵢ)]
```

### Multi-class Classification

**1. One-vs-Rest (OvR)**
- สร้างแบบจำลองแยกสำหรับแต่ละคลาส

**2. One-vs-One (OvO)**
- สร้างแบบจำลองสำหรับทุกคู่ของคลาส

**3. Multinomial Logistic Regression**
- ขยาย Logistic Regression สำหรับหลายคลาส

### การประเมินประสิทธิภาพ

**1. Confusion Matrix**
```
                Predicted
              0    1
Actual   0   TN   FP
         1   FN   TP
```

**2. Metrics**
- Accuracy = (TP + TN) / (TP + TN + FP + FN)
- Precision = TP / (TP + FP)
- Recall = TP / (TP + FN)
- F1-score = 2 × (Precision × Recall) / (Precision + Recall)

**3. ROC Curve และ AUC**
- ROC: Receiver Operating Characteristic
- AUC: Area Under the Curve

## 3.5 Support Vector Machines (SVM)

SVM เป็นอัลกอริทึมที่มีประสิทธิภาพสูงสำหรับทั้ง Classification และ Regression

### แนวคิด Maximum Margin

SVM หาเส้นแบ่ง (hyperplane) ที่มี margin สูงสุด:

```
margin = 2 / ||w||
```

โดยที่ w คือ weight vector

### Support Vectors

จุดข้อมูลที่อยู่บนขอบของ margin เรียกว่า Support Vectors ซึ่งเป็นจุดที่สำคัญที่สุดในการกำหนดเส้นแบ่ง

### Kernel Functions

สำหรับข้อมูลที่ไม่สามารถแยกเชิงเส้นได้ ใช้ Kernel functions:

**1. Linear Kernel**
```
K(x, x') = x · x'
```

**2. Polynomial Kernel**
```
K(x, x') = (γx · x' + r)^d
```

**3. RBF (Radial Basis Function) Kernel**
```
K(x, x') = exp(-γ||x - x'||²)
```

### SVM สำหรับ Regression (SVR)

SVR ใช้แนวคิดของ ε-insensitive loss function:
- ไม่มีการลงโทษสำหรับข้อผิดพลาดที่น้อยกว่า ε

## 3.6 Decision Trees และ Ensemble Methods

### Decision Trees

Decision Trees สร้างแบบจำลองในรูปของต้นไม้ตัดสินใจ

### Splitting Criteria

**1. สำหรับ Classification:**
- Gini Impurity: `Gini = 1 - Σpᵢ²`
- Entropy: `H = -Σpᵢlog₂(pᵢ)`
- Information Gain: `IG = H(parent) - Σ(nᵢ/n)H(child_i)`

**2. สำหรับ Regression:**
- Mean Squared Error (MSE)
- Mean Absolute Error (MAE)

### การป้องกัน Overfitting

**1. Pruning**
- Pre-pruning: หยุดการแบ่งก่อนเวลา
- Post-pruning: ตัดกิ่งหลังสร้างต้นไม้เสร็จ

**2. พารามิเตอร์ควบคุม**
- max_depth: ความลึกสูงสุด
- min_samples_split: จำนวนตัวอย่างขั้นต่ำสำหรับการแบ่ง
- min_samples_leaf: จำนวนตัวอย่างขั้นต่ำในใบ

### Ensemble Methods

**1. Bagging (Bootstrap Aggregating)**
- Random Forest: รวม Decision Trees หลายต้น
- ลดปัญหา Overfitting

**2. Boosting**
- AdaBoost: เพิ่มน้ำหนักให้ตัวอย่างที่ทำนายผิด
- Gradient Boosting: ปรับปรุงแบบจำลองแบบต่อเนื่อง

## 3.7 Model Evaluation และ Cross-Validation

### Cross-Validation

**1. K-Fold Cross-Validation**
```python
from sklearn.model_selection import cross_val_score
scores = cross_val_score(model, X, y, cv=5)
```

**2. Stratified K-Fold**
- รักษาสัดส่วนของแต่ละคลาส

**3. Leave-One-Out (LOO)**
- ใช้ตัวอย่างหนึ่งตัวสำหรับทดสอบ

### Learning Curves

การพล็อตประสิทธิภาพเทียบกับขนาดข้อมูล:
```python
from sklearn.model_selection import learning_curve
train_sizes, train_scores, val_scores = learning_curve(model, X, y)
```

### Validation Curves

การพล็อตประสิทธิภาพเทียบกับค่าพารามิเตอร์:
```python
from sklearn.model_selection import validation_curve
train_scores, val_scores = validation_curve(model, X, y, param_name, param_range)
```

## 3.8 การประยุกต์ใช้ในฟิสิกส์ขั้นสูง

### การวิเคราะห์ข้อมูลจาก Large Hadron Collider (LHC)

**1. การค้นหา Higgs Boson**
- ใช้ Machine Learning ในการจำแนกสัญญาณ Higgs จากสัญญาณรบกวน
- Features: พลังงาน, โมเมนตัม, มุมของอนุภาค

**2. การจำแนกประเภทเหตุการณ์**
- แยกแยะเหตุการณ์ที่น่าสนใจจากเหตุการณ์ธรรมดา
- ใช้ Neural Networks และ Boosted Decision Trees

### การประยุกต์ใช้ในดาราศาสตร์

**1. การจำแนกประเภทดาวฤกษ์**
- ใช้ข้อมูลสเปกตรัมในการจำแนกประเภท
- Features: ความเข้มของแสงที่ความยาวคลื่นต่างๆ

**2. การค้นหาดาวเคราะห์นอกระบบ**
- วิเคราะห์ข้อมูลความสว่างของดาวฤกษ์
- ตรวจจับการลดลงของความสว่างเมื่อดาวเคราะห์ผ่าน

### การวิเคราะห์ข้อมูลจากการทดลองควอนตัม

**1. การจำแนกสถานะควอนตัม**
- ใช้ Machine Learning ในการระบุสถานะของระบบควอนตัม
- ประยุกต์ใช้ในการพัฒนาคอมพิวเตอร์ควอนตัม

**2. การควบคุมระบบควอนตัม**
- ใช้ Reinforcement Learning ในการควบคุมระบบควอนตัม
- ปรับแต่งพารามิเตอร์เพื่อให้ได้สถานะที่ต้องการ

## สรุป

การเรียนรู้แบบมีผู้สอนเป็นเครื่องมือที่มีประสิทธิภาพสำหรับการวิเคราะห์ข้อมูลทางฟิสิกส์ อัลกอริทึมต่างๆ มีจุดแข็งและจุดอ่อนที่แตกต่างกัน:

- **Linear Regression**: เหมาะสำหรับความสัมพันธ์เชิงเส้น, ตีความได้ง่าย
- **Logistic Regression**: ดีสำหรับ Binary Classification, ให้ความน่าจะเป็น
- **SVM**: มีประสิทธิภาพสูง, ทำงานได้ดีกับข้อมูลมิติสูง
- **Decision Trees**: ตีความได้ง่าย, จัดการกับ Non-linear relationships ได้
- **Ensemble Methods**: ประสิทธิภาพสูง, ลดปัญหา Overfitting

การเลือกใช้อัลกอริทึมขึ้นอยู่กับลักษณะของข้อมูล, ความซับซ้อนของปัญหา, และความต้องการในการตีความผลลัพธ์

## แบบฝึกหัด

1. เปรียบเทียบความแตกต่างระหว่างปัญหาแบบ Regression และ Classification ในทางฟิสิกส์ พร้อมยกตัวอย่างเฉพาะ

2. อธิบายแนวคิดของ Bias-Variance Tradeoff และวิธีการจัดการในการฝึกสอนแบบจำลอง

3. จงออกแบบการทดลองเพื่อใช้ Random Forest ในการทำนายคุณสมบัติทางกายภาพของวัสดุจากโครงสร้างอะตอม

4. อธิบายวิธีการใช้ Cross-Validation ในการประเมินประสิทธิภาพของแบบจำลอง Machine Learning

5. ยกตัวอย่างการประยุกต์ใช้ SVM ในการวิเคราะห์ข้อมูลทางฟิสิกส์ พร้อมอธิบายเหตุผลในการเลือกใช้
