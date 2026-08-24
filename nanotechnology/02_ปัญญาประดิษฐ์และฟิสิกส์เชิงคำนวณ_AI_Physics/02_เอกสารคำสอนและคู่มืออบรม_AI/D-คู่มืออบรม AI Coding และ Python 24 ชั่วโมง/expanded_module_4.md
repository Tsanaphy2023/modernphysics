# โมดูล 4: Machine Learning Fundamentals with Scikit-learn (ขยาย)

## 4.1 แนวคิด Machine Learning และ Data Preprocessing

### 4.1.1 Feature Engineering: การสร้างคุณลักษณะใหม่จากข้อมูลเดิม

**Feature Engineering** คือกระบวนการสร้างคุณลักษณะ (Features) ใหม่จากข้อมูลดิบที่มีอยู่ เพื่อปรับปรุงประสิทธิภาพของโมเดล ML เป็นขั้นตอนที่ต้องใช้ความรู้เฉพาะทาง (Domain Knowledge) และความคิดสร้างสรรค์

**เทคนิค Feature Engineering ที่สำคัญ:**

| เทคนิค | คำอธิบาย | ตัวอย่างการประยุกต์ใช้ |
| :--- | :--- | :--- |
| **Binning/Discretization** | การแปลงตัวแปรต่อเนื่องให้เป็นตัวแปรหมวดหมู่ (Bins) | แปลงอายุ (Age) เป็นกลุ่ม (เช่น 0-18, 19-35, 36+) |
| **Interaction Features** | การรวมคุณลักษณะสองตัวหรือมากกว่าเข้าด้วยกัน | สร้างคอลัมน์ใหม่: `Area = Length * Width` |
| **Feature Extraction** | การดึงคุณลักษณะจากข้อมูลที่ไม่มีโครงสร้าง (เช่น ข้อความ, รูปภาพ) | การใช้ TF-IDF จากข้อความ, การใช้ PCA เพื่อลดมิติ |
| **One-Hot Encoding** | การแปลงตัวแปรหมวดหมู่ให้เป็นตัวเลข (Binary) | แปลงสี (แดง, เขียว, น้ำเงิน) เป็น 3 คอลัมน์ (Is_Red, Is_Green, Is_Blue) |

**ตัวอย่าง: Binning ด้วย Pandas**

```python
import pandas as pd
import numpy as np

df = pd.DataFrame({'Age': [15, 25, 35, 45, 55, 65]})

# กำหนดช่วงอายุ
bins = [0, 18, 35, 60, 100]
labels = ['Child', 'Young Adult', 'Adult', 'Senior']

# ใช้ pd.cut เพื่อทำการ Binning
df['Age_Group'] = pd.cut(df['Age'], bins=bins, labels=labels, right=False)
print(df)
```

## 4.2 การเรียนรู้แบบมีผู้สอน (Supervised Learning)

### 4.2.1 Advanced Classification: Support Vector Machine (SVM) และ Random Forest

นอกเหนือจาก Linear Regression และ Decision Tree พื้นฐาน โมเดลเหล่านี้เป็นที่นิยมในงาน Classification ที่ซับซ้อน

**1. Support Vector Machine (SVM):**
SVM ทำงานโดยการหา **Hyperplane** ที่ดีที่สุดเพื่อแยกข้อมูลสองคลาสออกจากกัน โดย Hyperplane นี้จะอยู่ห่างจากจุดข้อมูลที่ใกล้ที่สุด (Support Vectors) มากที่สุด

**ข้อดี:** มีประสิทธิภาพสูงในพื้นที่มิติสูง (High-Dimensional Spaces)
**ข้อเสีย:** ใช้เวลานานในการฝึกเมื่อชุดข้อมูลมีขนาดใหญ่

```python
from sklearn.svm import SVC
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

# โหลดชุดข้อมูล Iris
X, y = load_iris(return_X_y=True)
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42)

# สร้างและฝึกโมเดล SVM
svm_model = SVC(kernel='linear', C=1) # ใช้ Linear Kernel
svm_model.fit(X_train, y_train)
print(f"SVM Accuracy: {svm_model.score(X_test, y_test):.4f}")
```

**2. Random Forest:**
เป็นเทคนิค **Ensemble Learning** ที่สร้าง Decision Tree หลายต้น (Forest) และใช้ผลโหวต (Voting) จากทุกต้นเพื่อตัดสินใจผลลัพธ์สุดท้าย ช่วยลดปัญหา Overfitting และมีความแม่นยำสูง

```python
from sklearn.ensemble import RandomForestClassifier

# สร้างและฝึกโมเดล Random Forest
rf_model = RandomForestClassifier(n_estimators=100, random_state=42)
rf_model.fit(X_train, y_train)
print(f"Random Forest Accuracy: {rf_model.score(X_test, y_test):.4f}")
```

## 4.3 การประเมินผลโมเดล (Model Evaluation)

### 4.3.1 Model Selection: Cross-Validation และ Bias-Variance Tradeoff

**Cross-Validation (การตรวจสอบข้าม):**
เป็นเทคนิคที่ใช้ประเมินประสิทธิภาพของโมเดลอย่างน่าเชื่อถือ โดยการแบ่งชุดข้อมูลฝึกออกเป็น K ส่วน (K-Folds) และทำการฝึกและทดสอบ K ครั้ง

**K-Fold Cross-Validation:**
1.  แบ่งข้อมูลเป็น K ส่วนเท่าๆ กัน
2.  วนซ้ำ K ครั้ง: ใช้ K-1 ส่วนเป็นชุดฝึก และ 1 ส่วนเป็นชุดทดสอบ
3.  คำนวณค่าเฉลี่ยของเมตริกจากทั้ง K ครั้ง

```python
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LogisticRegression

# ใช้ Logistic Regression กับชุดข้อมูล Iris
log_reg = LogisticRegression(max_iter=200)

# ทำ 5-Fold Cross-Validation
scores = cross_val_score(log_reg, X, y, cv=5, scoring='accuracy')
print(f"Cross-Validation Scores: {scores}")
print(f"Mean Accuracy: {scores.mean():.4f}")
```

**Bias-Variance Tradeoff:**
เป็นแนวคิดหลักในการทำความเข้าใจว่าโมเดลเรียนรู้ข้อมูลได้ดีเพียงใด

| ปัญหา | ลักษณะ | สาเหตุ | ผลกระทบ |
| :--- | :--- | :--- | :--- |
| **High Bias (Underfitting)** | โมเดลเรียบง่ายเกินไป, ทำนายผิดพลาดทั้งในชุดฝึกและชุดทดสอบ | โมเดลไม่ซับซ้อนพอที่จะจับรูปแบบในข้อมูล | ประสิทธิภาพต่ำ |
| **High Variance (Overfitting)** | โมเดลซับซ้อนเกินไป, ทำงานได้ดีมากในชุดฝึก แต่แย่ในชุดทดสอบ | โมเดลจำ "เสียงรบกวน" (Noise) ในชุดฝึก | โมเดลไม่สามารถนำไปใช้กับข้อมูลใหม่ได้ |

### 4.3.2 Hyperparameter Tuning: Grid Search, Random Search, และ Pipeline

**Hyperparameter** คือพารามิเตอร์ที่ถูกกำหนด *ก่อน* การฝึกโมเดล (เช่น `n_estimators` ใน Random Forest, `C` ใน SVM) การหาค่า Hyperparameter ที่เหมาะสมที่สุดเรียกว่า **Hyperparameter Tuning**

**1. Grid Search:**
การค้นหาแบบครอบคลุม โดยการทดลองทุกชุดค่าที่เป็นไปได้ของ Hyperparameter ที่กำหนดไว้

```python
from sklearn.model_selection import GridSearchCV
from sklearn.neighbors import KNeighborsClassifier

# กำหนดช่วงของ Hyperparameter ที่ต้องการทดสอบ
param_grid = {
    'n_neighbors': [3, 5, 7, 9],
    'weights': ['uniform', 'distance']
}

knn = KNeighborsClassifier()

# ใช้ GridSearchCV พร้อม 5-Fold Cross-Validation
grid_search = GridSearchCV(knn, param_grid, cv=5, scoring='accuracy')
grid_search.fit(X_train, y_train)

print(f"Best Parameters: {grid_search.best_params_}")
print(f"Best Cross-Validation Score: {grid_search.best_score_:.4f}")
```

**2. Pipeline:**
การรวมขั้นตอนการประมวลผลข้อมูล (Preprocessing) และโมเดล (Estimator) เข้าด้วยกันเป็นขั้นตอนเดียว ช่วยให้โค้ดสะอาดขึ้นและป้องกัน **Data Leakage** (การที่ข้อมูลทดสอบรั่วไหลเข้าไปในขั้นตอนการฝึก)

```python
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

# สร้าง Pipeline: 1. Scaling ข้อมูล, 2. ฝึกโมเดล SVM
pipeline = Pipeline([
    ('scaler', StandardScaler()),
    ('svm', SVC(random_state=42))
])

# สามารถใช้ Pipeline ใน Grid Search ได้โดยตรง
param_grid_pipe = {
    'svm__C': [0.1, 1, 10],
    'svm__kernel': ['linear', 'rbf']
}

grid_search_pipe = GridSearchCV(pipeline, param_grid_pipe, cv=5)
grid_search_pipe.fit(X_train, y_train)
```

## 4.4 Unsupervised Learning: K-Means Clustering และ Dimensionality Reduction (PCA)

### 4.4.1 K-Means Clustering

**K-Means** เป็นอัลกอริทึม Clustering ที่พบบ่อยที่สุด ใช้ในการจัดกลุ่มข้อมูลที่ไม่มีป้ายกำกับ (Unlabeled Data) โดยการแบ่งข้อมูลออกเป็น K กลุ่ม (Clusters)

**หลักการ:**
1.  สุ่มเลือกจุดศูนย์กลาง (Centroids) K จุด
2.  กำหนดจุดข้อมูลแต่ละจุดให้อยู่ในกลุ่มที่ใกล้ Centroid ที่สุด
3.  คำนวณ Centroid ใหม่จากค่าเฉลี่ยของจุดข้อมูลในกลุ่มนั้น
4.  ทำซ้ำขั้นตอน 2 และ 3 จนกว่า Centroid จะไม่เปลี่ยนแปลง

```python
from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs
import matplotlib.pyplot as plt

# สร้างชุดข้อมูลสมมติ
X, y = make_blobs(n_samples=300, centers=4, random_state=42)

# สร้างและฝึกโมเดล K-Means (กำหนด K=4)
kmeans = KMeans(n_clusters=4, random_state=42, n_init=10)
kmeans.fit(X)

# การประเมินผล: ใช้ Elbow Method เพื่อหาค่า K ที่เหมาะสม
# (ต้องสร้างกราฟ Inertia เทียบกับ K)
```

### 4.4.2 Dimensionality Reduction (PCA)

**Principal Component Analysis (PCA)** เป็นเทคนิคที่ใช้ลดจำนวนมิติ (Features) ของชุดข้อมูล โดยการแปลงข้อมูลไปยังแกนใหม่ (Principal Components) ที่สามารถอธิบายความแปรปรวนของข้อมูลได้มากที่สุด

**ข้อดี:**
1.  ลดเวลาการฝึกโมเดล
2.  ช่วยให้สามารถสร้างภาพข้อมูลมิติสูง (เช่น 3 มิติ) ใน 2 มิติได้
3.  ลดปัญหา Overfitting

```python
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

# 1. Scaling ข้อมูลก่อน (สำคัญมากสำหรับ PCA)
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# 2. สร้างโมเดล PCA เพื่อลดเหลือ 2 มิติ
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X_scaled)

print(f"รูปร่างข้อมูลเดิม: {X.shape}")
print(f"รูปร่างข้อมูลหลัง PCA: {X_pca.shape}")
```

## 4.5 กรณีศึกษา: การสร้างโมเดลทำนาย (End-to-End Project)

**หัวข้อ:** การทำนายราคาบ้าน (Regression) โดยใช้ชุดข้อมูล Boston Housing (หรือชุดข้อมูลที่คล้ายกัน)

**ขั้นตอน End-to-End:**
1.  **Data Loading:** โหลดชุดข้อมูล
2.  **EDA:** วิเคราะห์ข้อมูลเบื้องต้น (Correlation Heatmap)
3.  **Data Preprocessing:** จัดการ Missing Data, Scaling ข้อมูลตัวเลข
4.  **Feature Engineering:** สร้าง Interaction Features (เช่น `Rooms_per_House = Total_Rooms / House_Age`)
5.  **Model Training:** ใช้ Pipeline เพื่อรวม Scaling, PCA (ลดมิติ), และ Linear Regression
6.  **Hyperparameter Tuning:** ใช้ Grid Search เพื่อหาค่า Hyperparameter ที่ดีที่สุดสำหรับโมเดล
7.  **Evaluation:** ประเมินผลด้วย R-squared และ MSE

## 4.6 แบบฝึกหัดและเฉลย (โมดูล 4)

**แบบฝึกหัด 4.1: Random Forest และ Cross-Validation**
จงใช้ชุดข้อมูล Iris:
1.  สร้างโมเดล `RandomForestClassifier`
2.  ใช้ `cross_val_score` เพื่อประเมินความแม่นยำของโมเดลด้วย 10-Fold Cross-Validation

**แบบฝึกหัด 4.2: K-Means Clustering**
จงใช้ชุดข้อมูล `make_blobs` (n_samples=200, centers=3, random_state=1)
1.  ฝึกโมเดล `KMeans` โดยกำหนด `n_clusters=3`
2.  ทำนายกลุ่มของข้อมูลและเก็บไว้ในตัวแปร `labels`

**เฉลย 4.1:**
```python
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_score
from sklearn.datasets import load_iris

X, y = load_iris(return_X_y=True)
rf = RandomForestClassifier(random_state=42)
scores = cross_val_score(rf, X, y, cv=10, scoring='accuracy')
print(f"10-Fold CV Mean Accuracy: {scores.mean():.4f}")
```

**เฉลย 4.2:**
```python
from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs

X, y_true = make_blobs(n_samples=200, centers=3, random_state=1)
kmeans = KMeans(n_clusters=3, random_state=1, n_init=10)
kmeans.fit(X)
labels = kmeans.predict(X)
# สามารถใช้ plt.scatter(X[:, 0], X[:, 1], c=labels) เพื่อแสดงผล
```
---
**หมายเหตุ:** เนื้อหาส่วนนี้เป็นส่วนขยายของโมดูล 4 ซึ่งจะถูกนำไปรวมกับเนื้อหาโมดูลอื่น ๆ ที่ขยายแล้ว เพื่อให้ได้คู่มือฉบับสมบูรณ์ 200-300 หน้า
