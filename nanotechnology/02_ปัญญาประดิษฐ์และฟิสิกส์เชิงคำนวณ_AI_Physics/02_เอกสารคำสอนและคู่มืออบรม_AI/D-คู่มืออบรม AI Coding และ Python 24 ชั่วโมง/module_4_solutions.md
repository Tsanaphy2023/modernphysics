# เฉลยแบบฝึกหัด Module 4: Machine Learning with Scikit-learn

## การเตรียมการ
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

### เฉลยแบบฝึกหัดที่ 1: การแบ่งข้อมูลและการปรับขนาด (Data Splitting and Scaling)

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

**คำอธิบาย:**
*   `train_test_split` ช่วยให้เราสามารถจำลองข้อมูลที่เราไม่เคยเห็นมาก่อน (Test Set) เพื่อประเมินประสิทธิภาพของโมเดล
*   `StandardScaler` จะคำนวณค่าเฉลี่ยและส่วนเบี่ยงเบนมาตรฐานจาก **X_train** เท่านั้น (`fit_transform`) เพื่อป้องกัน Data Leakage และนำค่าที่ได้ไปใช้ปรับขนาด **X_test** (`transform`)

---

### เฉลยแบบฝึกหัดที่ 2: การสร้างโมเดล Classification และการประเมินผล

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

**คำอธิบาย:**
*   `LogisticRegression` เป็นโมเดล Classification ที่ดีสำหรับชุดข้อมูลที่แยกได้เชิงเส้น (Linearly Separable)
*   `average='weighted'` ถูกใช้สำหรับปัญหา Multi-class (Iris มี 3 Class) เพื่อคำนวณค่าเฉลี่ยของ Metrics โดยให้น้ำหนักตามจำนวนตัวอย่างในแต่ละ Class

---

### เฉลยแบบฝึกหัดที่ 3: การประเมินโมเดล Regression และการตีความ

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

**คำอธิบาย:**
*   **MAE** บอกค่าความผิดพลาดเฉลี่ยในหน่วยเดียวกับ Target
*   **RMSE** ให้น้ำหนักกับความผิดพลาดที่รุนแรงกว่า (Outliers)
*   **R²** บอกว่า Features สามารถอธิบายความแปรปรวนของ Target ได้กี่เปอร์เซ็นต์ (ค่าใกล้ 1.0 ดีที่สุด)

---

### เฉลยแบบฝึกหัดที่ 4: การปรับแต่ง Hyperparameters ด้วย Grid Search CV

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

**คำอธิบาย:**
*   `GridSearchCV` จะลองฝึกโมเดลทุกการรวมกันของ Hyperparameters ที่กำหนดใน `param_grid`
*   `cv=5` หมายถึงการทำ 5-Fold Cross-Validation เพื่อให้ได้คะแนนประเมินที่เสถียรและเป็นกลาง

---

### เฉลยแบบฝึกหัดที่ 5: การใช้ Ensemble Learning (Random Forest)

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
accuracy_log_reg = accuracy_score(y_test, y_pred_log_reg) # ใช้ผลลัพธ์จาก Ex 2
print(f"Logistic Regression Accuracy (Ex 2): {accuracy_log_reg:.4f}")

if accuracy_rf > accuracy_log_reg:
    print("Random Forest มีประสิทธิภาพสูงกว่า Logistic Regression")
else:
    print("Logistic Regression มีประสิทธิภาพสูงกว่าหรือเท่ากับ Random Forest")
```

**คำอธิบาย:**
*   `RandomForestClassifier` เป็น Ensemble Method ที่ใช้ Bagging เพื่อลด Variance และมักให้ผลลัพธ์ที่ดีกว่าโมเดลเดี่ยว (Single Model) อย่าง Logistic Regression หรือ Decision Tree
*   การเปรียบเทียบผลลัพธ์ช่วยให้ผู้เรียนเห็นความสำคัญของการเลือกใช้โมเดลที่เหมาะสมกับปัญหาและชุดข้อมูล
