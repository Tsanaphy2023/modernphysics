## บทที่ 4: การสร้างโมเดล Machine Learning สำหรับข้อมูล

หลังจากที่เราได้เตรียมและทำความสะอาดข้อมูลด้วย Pandas ในบทที่ 3 แล้ว ขั้นตอนต่อไปที่น่าตื่นเต้นที่สุดคือการนำข้อมูลเหล่านั้นมา "สอน" ให้คอมพิวเตอร์เรียนรู้และสร้างแบบจำลองการทำนาย หรือที่เรียกว่า **โมเดล Machine Learning** ในบทนี้ เราจะใช้ไลบรารี **Scikit-learn** ซึ่งเป็นเหมือนกล่องเครื่องมือสารพัดประโยชน์สำหรับสร้างโมเดล ML ใน Python

### Workflow ของโปรเจกต์ Machine Learning

ก่อนจะลงมือสร้างโมเดล เราควรทำความเข้าใจภาพรวมของกระบวนการทั้งหมดก่อน ซึ่งโดยทั่วไปแล้วจะมีขั้นตอนดังนี้:

![Machine Learning Workflow](https://private-us-east-1.manuscdn.com/sessionFile/OO4QhUUsaoBTGAbGU9i0j2/sandbox/pRb06yRMC7k7XW9CBSc5bm-images_1760366739226_na1fn_L2hvbWUvdWJ1bnR1L2RpYWdyYW1zL21sX3dvcmtmbG93.png?Policy=eyJTdGF0ZW1lbnQiOlt7IlJlc291cmNlIjoiaHR0cHM6Ly9wcml2YXRlLXVzLWVhc3QtMS5tYW51c2Nkbi5jb20vc2Vzc2lvbkZpbGUvT080UWhVVXNhb0JUR0FiR1U5aTBqMi9zYW5kYm94L3BSYjA2eVJNQzdrN1hXOUNCU2M1Ym0taW1hZ2VzXzE3NjAzNjY3MzkyMjZfbmExZm5fTDJodmJXVXZkV0oxYm5SMUwyUnBZV2R5WVcxekwyMXNYM2R2Y210bWJHOTMucG5nIiwiQ29uZGl0aW9uIjp7IkRhdGVMZXNzVGhhbiI6eyJBV1M6RXBvY2hUaW1lIjoxNzk4NzYxNjAwfX19XX0_&Key-Pair-Id=K2HSFNDJXOU9YS&Signature=oPL6UJvXSBPV16v5wpS2EKnsRffJ4wBfNQ4ld1~yrIc-jS7vRwpB5T~iFK5v7rvWggbFj3kM7ePSOg0S5~DQs6NCwdmxcmXBaC2i-isRqLCe5UwoBJpmXGxZmA5K0AuoOysnjPECDAml0bXG-O5GhRowPzUZys6MJao3MKmhJcOmInOysRUqALDxKOjO4xwYBzLeLq47MrywPuptetyddYyuDYCM6KgeBLcWWFlfDihzPqEwXXMafPMo~NwPesfKDJIRQj8eNcPpTBUEwxee0K1DEsCvCkJTHupQLQcMh9knI6YzrxpJV0vJ~kBqNB07AixOiA8IvfywARtDVFSPWg__)
*ภาพที่ 4.1: แผนภาพแสดงขั้นตอนการทำงานของโปรเจกต์ Machine Learning*

1.  **เตรียมข้อมูล (Data Preparation):** คือสิ่งที่เราทำในบทที่ 3
2.  **แบ่งข้อมูล (Data Splitting):** เราจะไม่ใช้ข้อมูลทั้งหมดในการสอนโมเดล แต่จะแบ่งข้อมูลออกเป็น 2 ส่วนหลัก คือ
    *   **ชุดข้อมูลสำหรับสอน (Training Set):** ใช้สำหรับ "สอน" หรือ "ฝึก" โมเดล (ประมาณ 70-80% ของข้อมูลทั้งหมด)
    *   **ชุดข้อมูลสำหรับทดสอบ (Test Set):** ใช้สำหรับ "วัดผล" หรือ "ประเมิน" ประสิทธิภาพของโมเดลกับข้อมูลที่ไม่เคยเห็นมาก่อน (ประมาณ 20-30%)
3.  **เลือกและสร้างโมเดล (Model Selection & Training):** เลือกอัลกอริทึมที่เหมาะสมกับปัญหาและนำ Training Set ไปสอนโมเดล
4.  **ประเมินผลโมเดล (Model Evaluation):** นำ Test Set มาให้โมเดลทำนายและเปรียบเทียบผลลัพธ์กับคำตอบที่แท้จริง เพื่อวัดว่าโมเดลของเราทำงานได้ดีแค่ไหน

### โมเดลการจำแนกประเภท (Classification)

**Classification** คือการทำนายผลลัพธ์ที่เป็นหมวดหมู่หรือไม่ต่อเนื่อง (discrete categories) เช่น "ใช่/ไม่ใช่", "สแปม/ไม่ใช่สแปม", "แมว/สุนัข/นก"

**ตัวอย่าง: การวิเคราะห์ลูกค้าที่จะยกเลิกบริการ (Customer Churn)**

สมมติว่าเราเป็นบริษัทโทรคมนาคม และต้องการทำนายว่าลูกค้าคนไหนมีแนวโน้มจะยกเลิกบริการ (Churn) เพื่อที่จะได้หาทางรักษาลูกค้าไว้ก่อน

**1. เตรียมและแบ่งข้อมูล**

```python
import pandas as pd
from sklearn.model_selection import train_test_split

# สมมติว่า df คือ DataFrame ที่มีข้อมูลลูกค้าและคอลัมน์ 'Churn' (Yes/No)
# X คือข้อมูลคุณลักษณะของลูกค้า (เช่น อายุ, แพ็กเกจ, ระยะเวลาที่ใช้บริการ)
# y คือเป้าหมายที่เราต้องการทำนาย (Churn)
X = df.drop('Churn', axis=1)
y = df['Churn']

# แบ่งข้อมูลเป็น Training set (80%) และ Test set (20%)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
```

**2. สร้างและฝึกสอนโมเดล**

เราจะลองใช้โมเดล **Decision Tree** ซึ่งเป็นโมเดลที่เข้าใจง่ายและเห็นภาพได้ชัดเจน

```python
from sklearn.tree import DecisionTreeClassifier

# สร้างโมเดล Decision Tree
model = DecisionTreeClassifier(random_state=42)

# ฝึกสอนโมเดลด้วย Training set
model.fit(X_train, y_train)
```

### โมเดลการทำนายค่าต่อเนื่อง (Regression)

**Regression** คือการทำนายผลลัพธ์ที่เป็นค่าตัวเลขต่อเนื่อง (continuous values) เช่น ราคา, อุณหภูมิ, ยอดขาย

**ตัวอย่าง: การทำนายราคาบ้าน**

เป้าหมายของเราคือการสร้างโมเดลที่สามารถทำนายราคาบ้าน (price) โดยพิจารณาจากคุณสมบัติต่างๆ ของบ้าน (เช่น ขนาดพื้นที่, จำนวนห้องนอน, ทำเล)

**1. เตรียมและแบ่งข้อมูล** (เหมือนกับ Classification)

```python
# สมมติว่า df_house คือ DataFrame ที่มีข้อมูลบ้านและคอลัมน์ 'price'
# X คือคุณสมบัติของบ้าน, y คือราคาบ้าน
X_house = df_house.drop('price', axis=1)
y_house = df_house['price']

X_train_h, X_test_h, y_train_h, y_test_h = train_test_split(X_house, y_house, test_size=0.2, random_state=42)
```

**2. สร้างและฝึกสอนโมเดล**

เราจะใช้โมเดลพื้นฐานที่ทรงพลังอย่าง **Linear Regression**

```python
from sklearn.linear_model import LinearRegression

# สร้างโมเดล Linear Regression
model_linear = LinearRegression()

# ฝึกสอนโมเดล
model_linear.fit(X_train_h, y_train_h)
```

### การประเมินประสิทธิภาพของโมเดล

หลังจากฝึกสอนโมเดลแล้ว เราจะรู้ได้อย่างไรว่าโมเดลของเราดีแค่ไหน? เราจะใช้ Test Set ที่แบ่งไว้มาวัดผล

**การประเมินโมเดล Classification:**

เราจะใช้ `model.predict()` กับ `X_test` และเปรียบเทียบผลกับ `y_test`

```python
from sklearn.metrics import accuracy_score, confusion_matrix

# ให้โมเดลทำนายผลจาก Test set
y_pred = model.predict(X_test)

# วัดความแม่นยำ (Accuracy)
accuracy = accuracy_score(y_test, y_pred)
print(f'Accuracy: {accuracy:.2f}')

# แสดง Confusion Matrix เพื่อดูว่าโมเดลทายถูก/ผิดในแต่ละคลาสอย่างไร
print(confusion_matrix(y_test, y_pred))
```

**การประเมินโมเดล Regression:**

ตัวชี้วัดสำหรับ Regression จะแตกต่างออกไป โดยจะวัดว่าค่าที่โมเดลทำนายใกล้เคียงกับค่าจริงแค่ไหน

```python
from sklearn.metrics import mean_squared_error
import numpy as np

# ให้โมเดลทำนายราคาบ้านจาก Test set
y_pred_h = model_linear.predict(X_test_h)

# คำนวณค่า Mean Squared Error (MSE)
mse = mean_squared_error(y_test_h, y_pred_h)
# คำนวณค่า Root Mean Squared Error (RMSE) เพื่อให้หน่วยกลับมาเหมือนเดิม
rmse = np.sqrt(mse)
print(f'RMSE: {rmse:.2f}')
```

ในบทนี้ เราได้เห็นภาพรวมของการสร้างโมเดล Machine Learning ตั้งแต่การแบ่งข้อมูล, การเลือกโมเดลสำหรับปัญหา Classification และ Regression, ไปจนถึงการวัดผลโมเดลด้วยเมตริกต่างๆ ในส่วนต่อไปของหนังสือ เราจะเปลี่ยนจากการทำงานกับข้อมูลตารางไปสู่โลกของข้อมูลรูปภาพ ซึ่งต้องอาศัยเทคนิคที่แตกต่างและทรงพลังยิ่งขึ้นอย่าง Deep Learning

