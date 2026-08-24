# แบบฝึกหัดและเฉลย Module 4: Machine Learning with Scikit-learn

## วัตถุประสงค์
เพื่อให้ผู้เรียนสามารถประยุกต์ใช้ Scikit-learn ในการสร้างโมเดล Machine Learning, ประเมินประสิทธิภาพ, และปรับแต่ง Hyperparameters ได้อย่างถูกต้อง

---

### การเตรียมการ
ก่อนเริ่มต้น ให้ติดตั้งไลบรารีที่จำเป็นและโหลดชุดข้อมูล Iris สำหรับปัญหา Classification และ Diabetes สำหรับปัญหา Regression

```python
import numpy as np
from sklearn.datasets import load_iris, load_diabetes
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression, LinearRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (
    accuracy_score, precision_score, recall_score, f1_score,
    mean_absolute_error, mean_squared_error, r2_score
)

# โหลดชุดข้อมูล
iris = load_iris()
X, y = iris.data, iris.target

diabetes = load_diabetes()
X_reg, y_reg = diabetes.data, diabetes.target
```

---

### แบบฝึกหัดที่ 1: การแบ่งข้อมูลและการปรับขนาด (Data Splitting and Scaling)

**โจทย์:**
คุณได้รับชุดข้อมูล (X, y) สำหรับปัญหา Classification (เช่น Iris Dataset)
1. ใช้ `train_test_split` เพื่อแบ่งข้อมูลออกเป็น Training (70%) และ Test (30%) โดยกำหนด `random_state=42`
2. ใช้ `StandardScaler` เพื่อปรับขนาดข้อมูล (Standardize) เฉพาะส่วน Training และ Test
3. แสดงขนาดของชุดข้อมูล X_train, X_test, y_train, และ y_test

**เฉลยแบบฝึกหัดที่ 1:**
```python
# 1. แบ่งข้อมูล
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

# 2. ปรับขนาดข้อมูล
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# 3. แสดงขนาดของชุดข้อมูล
print(f"X_train shape: {X_train_scaled.shape}")
print(f"X_test shape: {X_test_scaled.shape}")
print(f"y_train shape: {y_train.shape}")
print(f"y_test shape: {y_test.shape}")
```
**คำอธิบาย:** `StandardScaler` จะคำนวณค่าเฉลี่ยและส่วนเบี่ยงเบนมาตรฐานจาก **X_train** เท่านั้น (`fit_transform`) เพื่อป้องกัน Data Leakage และนำค่าที่ได้ไปใช้ปรับขนาด **X_test** (`transform`)

---

### แบบฝึกหัดที่ 2: การสร้างโมเดล Classification และการประเมินผล

**โจทย์:**
จากข้อมูลที่แบ่งและปรับขนาดแล้วในแบบฝึกหัดที่ 1:
1. สร้างโมเดล `LogisticRegression` และฝึกด้วยข้อมูล Training
2. ทำนายผลลัพธ์บนข้อมูล Test
3. คำนวณและแสดงผล **Accuracy**, **Precision**, **Recall**, และ **F1-Score** โดยใช้ฟังก์ชันจาก `sklearn.metrics`

**เฉลยแบบฝึกหัดที่ 2:**
```python
# 1. สร้างและฝึกโมเดล Logistic Regression
log_reg = LogisticRegression(random_state=42, max_iter=200)
log_reg.fit(X_train_scaled, y_train)

# 2. ทำนายผลลัพธ์
y_pred_log_reg = log_reg.predict(X_test_scaled)

# 3. คำนวณและแสดงผล Metrics
accuracy = accuracy_score(y_test, y_pred_log_reg)
precision = precision_score(y_test, y_pred_log_reg, average='weighted')
recall = recall_score(y_test, y_pred_log_reg, average='weighted')
f1 = f1_score(y_test, y_pred_log_reg, average='weighted')

print("--- Logistic Regression Metrics ---")
print(f"Accuracy: {accuracy:.4f}")
print(f"Precision: {precision:.4f}")
print(f"Recall: {recall:.4f}")
print(f"F1-Score: {f1:.4f}")
```
**คำอธิบาย:** `average='weighted'` ถูกใช้สำหรับปัญหา Multi-class (Iris มี 3 Class) เพื่อคำนวณค่าเฉลี่ยของ Metrics โดยให้น้ำหนักตามจำนวนตัวอย่างในแต่ละ Class

---

### แบบฝึกหัดที่ 3: การประเมินโมเดล Regression และการตีความ

**โจทย์:**
คุณได้รับชุดข้อมูล (X_reg, y_reg) สำหรับปัญหา Regression (เช่น Boston Housing Dataset)
1. สร้างโมเดล `LinearRegression` และฝึกด้วยข้อมูล Training (สมมติว่ามีการแบ่งข้อมูลแล้ว)
2. ทำนายผลลัพธ์บนข้อมูล Test
3. คำนวณและแสดงผล **Mean Absolute Error (MAE)**, **Root Mean Squared Error (RMSE)**, และ **R-squared (R²)**

**เฉลยแบบฝึกหัดที่ 3:**
```python
# แบ่งข้อมูล Regression
X_train_reg, X_test_reg, y_train_reg, y_test_reg = train_test_split(
    X_reg, y_reg, test_size=0.3, random_state=42
)

# 1. สร้างและฝึกโมเดล Linear Regression
lin_reg = LinearRegression()
lin_reg.fit(X_train_reg, y_train_reg)

# 2. ทำนายผลลัพธ์
y_pred_lin_reg = lin_reg.predict(X_test_reg)

# 3. คำนวณและแสดงผล Metrics
mae = mean_absolute_error(y_test_reg, y_pred_lin_reg)
mse = mean_squared_error(y_test_reg, y_pred_lin_reg)
rmse = np.sqrt(mse)
r2 = r2_score(y_test_reg, y_pred_lin_reg)

print("--- Linear Regression Metrics ---")
print(f"MAE: {mae:.2f}")
print(f"MSE: {mse:.2f}")
print(f"RMSE: {rmse:.2f}")
print(f"R-squared (R²): {r2:.4f}")
```
**คำอธิบาย:** **R²** บอกว่า Features สามารถอธิบายความแปรปรวนของ Target ได้กี่เปอร์เซ็นต์ (ค่าใกล้ 1.0 ดีที่สุด)

---

### แบบฝึกหัดที่ 4: การปรับแต่ง Hyperparameters ด้วย Grid Search CV

**โจทย์:**
คุณต้องการปรับแต่ง Hyperparameters สำหรับโมเดล `DecisionTreeClassifier`
1. กำหนด `param_grid` สำหรับ `max_depth` (ค่า: 3, 5, 7) และ `min_samples_split` (ค่า: 2, 5, 10)
2. ใช้ `GridSearchCV` พร้อม `cv=5` เพื่อค้นหา Hyperparameters ที่ดีที่สุดจากข้อมูล Training
3. แสดงผล **Best Parameters** และ **Best Score** ที่ได้จากการค้นหา

**เฉลยแบบฝึกหัดที่ 4:**
```python
# 1. กำหนด param_grid
param_grid = {
    'max_depth': [3, 5, 7],
    'min_samples_split': [2, 5, 10]
}

# 2. ใช้ GridSearchCV
# ใช้ข้อมูลที่ยังไม่ได้แบ่ง (X, y) เพื่อให้ GridSearchCV ทำ Cross-Validation ภายใน
dt_model = DecisionTreeClassifier(random_state=42)
grid_search = GridSearchCV(
    dt_model, param_grid, cv=5, scoring='accuracy'
)
grid_search.fit(X, y)

# 3. แสดงผล Best Parameters และ Best Score
print("--- Grid Search Results ---")
print(f"Best Parameters: {grid_search.best_params_}")
print(f"Best Score (Accuracy): {grid_search.best_score_:.4f}")
```
**คำอธิบาย:** `GridSearchCV` จะลองฝึกโมเดลทุกการรวมกันของ Hyperparameters ที่กำหนดใน `param_grid` โดยใช้ 5-Fold Cross-Validation

---

### แบบฝึกหัดที่ 5: การใช้ Ensemble Learning (Random Forest)

**โจทย์:**
คุณต้องการสร้างโมเดลที่มีประสิทธิภาพสูงขึ้นโดยใช้ Ensemble Learning
1. สร้างโมเดล `RandomForestClassifier` โดยกำหนด `n_estimators=100` และ `random_state=42`
2. ฝึกโมเดลด้วยข้อมูล Training (จากแบบฝึกหัดที่ 1)
3. คำนวณและแสดงผล **Accuracy** ของโมเดล Random Forest บนข้อมูล Test
4. เปรียบเทียบ Accuracy ที่ได้กับโมเดล Logistic Regression ในแบบฝึกหัดที่ 2

**เฉลยแบบฝึกหัดที่ 5:**
```python
# 1. สร้างโมเดล Random Forest
rf_model = RandomForestClassifier(n_estimators=100, random_state=42)

# 2. ฝึกโมเดล
rf_model.fit(X_train_scaled, y_train)

# 3. ทำนายและคำนวณ Accuracy
y_pred_rf = rf_model.predict(X_test_scaled)
accuracy_rf = accuracy_score(y_test, y_pred_rf)

print("--- Random Forest Results ---")
print(f"Random Forest Accuracy: {accuracy_rf:.4f}")

# 4. เปรียบเทียบกับ Logistic Regression (จากแบบฝึกหัดที่ 2)
# ต้องรันแบบฝึกหัดที่ 2 ก่อนเพื่อได้ y_pred_log_reg และ accuracy_log_reg
# สมมติว่ารันแล้ว:
# accuracy_log_reg = 0.9778 # ค่าที่ได้จากการรัน Ex 2

# print(f"Logistic Regression Accuracy (Ex 2): {accuracy_log_reg:.4f}")
# if accuracy_rf > accuracy_log_reg:
#     print("Random Forest มีประสิทธิภาพสูงกว่า Logistic Regression")
# else:
#     print("Logistic Regression มีประสิทธิภาพสูงกว่าหรือเท่ากับ Random Forest")
```
**คำอธิบาย:** `RandomForestClassifier` เป็น Ensemble Method ที่ใช้ Bagging เพื่อลด Variance และมักให้ผลลัพธ์ที่ดีกว่าโมเดลเดี่ยว (Single Model)
