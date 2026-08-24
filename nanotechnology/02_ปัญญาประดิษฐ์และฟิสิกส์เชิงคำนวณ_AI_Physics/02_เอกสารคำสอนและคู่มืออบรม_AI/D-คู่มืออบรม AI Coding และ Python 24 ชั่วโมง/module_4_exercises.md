# แบบฝึกหัด Module 4: Machine Learning with Scikit-learn

## วัตถุประสงค์
เพื่อให้ผู้เรียนสามารถประยุกต์ใช้ Scikit-learn ในการสร้างโมเดล Machine Learning, ประเมินประสิทธิภาพ, และปรับแต่ง Hyperparameters ได้อย่างถูกต้อง

---

### แบบฝึกหัดที่ 1: การแบ่งข้อมูลและการปรับขนาด (Data Splitting and Scaling)

**โจทย์:**
คุณได้รับชุดข้อมูล (X, y) สำหรับปัญหา Classification (เช่น Iris Dataset)
1. ใช้ `train_test_split` เพื่อแบ่งข้อมูลออกเป็น Training (70%) และ Test (30%) โดยกำหนด `random_state=42`
2. ใช้ `StandardScaler` เพื่อปรับขนาดข้อมูล (Standardize) เฉพาะส่วน Training และ Test
3. แสดงขนาดของชุดข้อมูล X_train, X_test, y_train, และ y_test

**แนวคิดหลัก:** การเตรียมข้อมูลให้พร้อมก่อนการฝึกโมเดล

---

### แบบฝึกหัดที่ 2: การสร้างโมเดล Classification และการประเมินผล

**โจทย์:**
จากข้อมูลที่แบ่งและปรับขนาดแล้วในแบบฝึกหัดที่ 1:
1. สร้างโมเดล `LogisticRegression` และฝึกด้วยข้อมูล Training
2. ทำนายผลลัพธ์บนข้อมูล Test
3. คำนวณและแสดงผล **Accuracy**, **Precision**, **Recall**, และ **F1-Score** โดยใช้ฟังก์ชันจาก `sklearn.metrics`

**แนวคิดหลัก:** การฝึกโมเดล Classification และการใช้ Metrics ประเมินผล

---

### แบบฝึกหัดที่ 3: การประเมินโมเดล Regression และการตีความ

**โจทย์:**
คุณได้รับชุดข้อมูล (X_reg, y_reg) สำหรับปัญหา Regression (เช่น Boston Housing Dataset)
1. สร้างโมเดล `LinearRegression` และฝึกด้วยข้อมูล Training (สมมติว่ามีการแบ่งข้อมูลแล้ว)
2. ทำนายผลลัพธ์บนข้อมูล Test
3. คำนวณและแสดงผล **Mean Absolute Error (MAE)**, **Root Mean Squared Error (RMSE)**, และ **R-squared (R²)**

**แนวคิดหลัก:** การฝึกโมเดล Regression และการใช้ Metrics ประเมินผล

---

### แบบฝึกหัดที่ 4: การปรับแต่ง Hyperparameters ด้วย Grid Search CV

**โจทย์:**
คุณต้องการปรับแต่ง Hyperparameters สำหรับโมเดล `DecisionTreeClassifier`
1. กำหนด `param_grid` สำหรับ `max_depth` (ค่า: 3, 5, 7) และ `min_samples_split` (ค่า: 2, 5, 10)
2. ใช้ `GridSearchCV` พร้อม `cv=5` เพื่อค้นหา Hyperparameters ที่ดีที่สุดจากข้อมูล Training
3. แสดงผล **Best Parameters** และ **Best Score** ที่ได้จากการค้นหา

**แนวคิดหลัก:** การใช้ Cross-Validation และ Grid Search เพื่อหา Hyperparameters ที่เหมาะสม

---

### แบบฝึกหัดที่ 5: การใช้ Ensemble Learning (Random Forest)

**โจทย์:**
คุณต้องการสร้างโมเดลที่มีประสิทธิภาพสูงขึ้นโดยใช้ Ensemble Learning
1. สร้างโมเดล `RandomForestClassifier` โดยกำหนด `n_estimators=100` และ `random_state=42`
2. ฝึกโมเดลด้วยข้อมูล Training (จากแบบฝึกหัดที่ 1)
3. คำนวณและแสดงผล **Accuracy** ของโมเดล Random Forest บนข้อมูล Test
4. เปรียบเทียบ Accuracy ที่ได้กับโมเดล Logistic Regression ในแบบฝึกหัดที่ 2

**แนวคิดหลัก:** การใช้ Ensemble Methods เพื่อปรับปรุงประสิทธิภาพโมเดล
