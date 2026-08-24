# โมดูล 3: Python for Data Analysis (ขยาย)

## 3.1 NumPy: การคำนวณเชิงตัวเลข

### 3.1.1 Advanced NumPy: Broadcasting และ Linear Algebra Operations

**Broadcasting** คือกลไกที่ NumPy ใช้ในการดำเนินการทางคณิตศาสตร์กับ Array ที่มีรูปร่าง (Shape) แตกต่างกัน โดยไม่ต้องคัดลอกข้อมูลซ้ำ ซึ่งช่วยให้โค้ดกระชับและมีประสิทธิภาพ

**กฎการ Broadcasting:**
1.  ถ้า Array ทั้งสองมีมิติ (Dimension) ไม่เท่ากัน Array ที่มีมิติน้อยกว่าจะถูก "ขยาย" ให้มีมิติเท่ากับ Array ที่มีมิติมากกว่า
2.  ถ้าขนาดของมิติไม่ตรงกัน Array ที่มีขนาดเป็น 1 จะถูก "ยืด" ให้มีขนาดเท่ากับมิติของ Array อื่น

**ตัวอย่าง: Broadcasting**

```python
import numpy as np

# Array 2 มิติ (3x3)
A = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])

# Array 1 มิติ (3,)
B = np.array([10, 20, 30])

# การบวก: B จะถูก Broadcast ให้เป็น 3x3 โดยทำซ้ำในแต่ละแถว
C = A + B
print("ผลลัพธ์ Broadcasting (A + B):\n", C)
# [[11, 22, 33],
#  [14, 25, 36],
#  [17, 28, 39]]
```

**Linear Algebra Operations (การดำเนินการพีชคณิตเชิงเส้น):**

NumPy มีฟังก์ชันที่จำเป็นสำหรับการคำนวณทางพีชคณิตเชิงเส้น ซึ่งเป็นหัวใจสำคัญของอัลกอริทึม ML/DL

| ฟังก์ชัน | คำอธิบาย |
| :--- | :--- |
| `np.dot(A, B)` | การคูณเมทริกซ์ (Dot Product) |
| `np.linalg.inv(A)` | การหาเมทริกซ์ผกผัน (Inverse Matrix) |
| `np.linalg.eig(A)` | การหา Eigenvalues และ Eigenvectors |
| `np.transpose(A)` | การสลับแถวเป็นคอลัมน์ (Transpose) |

**ตัวอย่าง: Dot Product**

```python
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

# การคูณเมทริกซ์ (Matrix Multiplication)
C = np.dot(A, B)
print("ผลลัพธ์ Dot Product (A @ B):\n", C)
# [[19, 22],
#  [43, 50]]
```

## 3.2 Pandas: การจัดการข้อมูล

### 3.2.1 Advanced Pandas: MultiIndex, GroupBy, Pivot Tables, Merge/Join อย่างละเอียด

**MultiIndex (Hierarchical Indexing):** การใช้ Index หลายระดับ ทำให้สามารถจัดการข้อมูลที่มีมิติซับซ้อนได้ง่ายขึ้น

```python
# สร้าง MultiIndex
index = pd.MultiIndex.from_tuples([('A', 1), ('A', 2), ('B', 1), ('B', 2)], names=['Group', 'Sub'])
s = pd.Series([10, 20, 30, 40], index=index)
print("MultiIndex Series:\n", s)

# การเข้าถึงข้อมูล
print("\nเข้าถึง Group A:\n", s.loc['A'])
```

**GroupBy (การจัดกลุ่ม):** การจัดกลุ่มข้อมูลตามคอลัมน์ที่กำหนด และใช้ฟังก์ชันรวม (Aggregation) เช่น `sum()`, `mean()`, `count()`

```python
# สมมติ DataFrame df จากโมดูลก่อนหน้า
# df = pd.DataFrame({'Name': ['Alice', 'Bob', 'Charlie', 'David'], 'Age': [25, 30, 35, 40], 'City': ['BKK', 'CNX', 'BKK', 'CNX'], 'Salary': [50000, 60000, 75000, 90000]})

# หาค่าเฉลี่ยเงินเดือนตามเมือง
city_salary_mean = df.groupby('City')['Salary'].mean()
print("\nค่าเฉลี่ยเงินเดือนตามเมือง:\n", city_salary_mean)
```

**Pivot Tables (ตารางสรุปแกนหมุน):** คล้ายกับ GroupBy แต่จัดรูปแบบข้อมูลให้อยู่ในรูปแบบตาราง 2 มิติ (แถวและคอลัมน์)

```python
# สร้าง Pivot Table: แถวคือ City, คอลัมน์คือ Age (จัดกลุ่มเป็นช่วง), ค่าคือ Salary
df['Age_Group'] = pd.cut(df['Age'], bins=[20, 30, 40], labels=['20-30', '30-40'])
pivot_table = df.pivot_table(values='Salary', index='City', columns='Age_Group', aggfunc='mean')
print("\nPivot Table (ค่าเฉลี่ยเงินเดือน):\n", pivot_table)
```

**Merge/Join (การรวมข้อมูล):** การรวม DataFrame สองชุดเข้าด้วยกันตามคีย์ที่กำหนด (คล้ายกับ SQL JOIN)

```python
df_info = pd.DataFrame({'ID': [1, 2, 3], 'Name': ['A', 'B', 'C']})
df_data = pd.DataFrame({'ID': [2, 3, 4], 'Score': [90, 85, 70]})

# Inner Join (รวมเฉพาะ ID ที่มีอยู่ในทั้งสองตาราง)
merged_df = pd.merge(df_info, df_data, on='ID', how='inner')
print("\nMerged DataFrame (Inner Join):\n", merged_df)
```

### 3.2.2 Data Cleaning ขั้นสูง: การจัดการ Missing Data (Imputation) และ Outliers

**Missing Data (ข้อมูลสูญหาย):**

| วิธีการจัดการ | ฟังก์ชัน Pandas | คำอธิบาย |
| :--- | :--- | :--- |
| **การลบ** | `df.dropna()` | ลบแถวหรือคอลัมน์ที่มีค่า NaN |
| **การแทนที่ (Imputation)** | `df.fillna()` | แทนที่ค่า NaN ด้วยค่าคงที่, ค่าเฉลี่ย (`mean`), ค่ามัธยฐาน (`median`), หรือค่าฐานนิยม (`mode`) |

**ตัวอย่าง: การแทนที่ด้วยค่ามัธยฐาน (Median Imputation)**

```python
# สมมติว่าคอลัมน์ 'Salary' มีค่า NaN
df_with_nan = df.copy()
df_with_nan.loc[0, 'Salary'] = np.nan

# แทนที่ NaN ด้วยค่ามัธยฐานของคอลัมน์
median_salary = df_with_nan['Salary'].median()
df_filled = df_with_nan['Salary'].fillna(median_salary)
print("\nSalary หลัง Imputation:\n", df_filled)
```

**Outliers (ค่าผิดปกติ):**

ค่าผิดปกติอาจส่งผลกระทบอย่างมากต่อโมเดล ML วิธีการตรวจจับที่พบบ่อยคือ **Interquartile Range (IQR)**

**ขั้นตอนการตรวจจับ Outlier ด้วย IQR:**
1.  คำนวณ Q1 (Quartile 1 - เปอร์เซ็นไทล์ที่ 25) และ Q3 (Quartile 3 - เปอร์เซ็นไทล์ที่ 75)
2.  คำนวณ IQR = Q3 - Q1
3.  กำหนดขอบเขต: **Lower Bound** = Q1 - 1.5 * IQR, **Upper Bound** = Q3 + 1.5 * IQR
4.  ค่าใดๆ ที่อยู่นอกขอบเขตนี้ถือเป็น Outlier

## 3.3 Matplotlib & Seaborn: การสร้างภาพข้อมูลเบื้องต้น

### 3.3.1 Advanced Visualization: Subplots, Customizing Styles, การสร้าง Heatmap

**Subplots (กราฟย่อย):** การแสดงกราฟหลายๆ รูปใน Figure เดียวกันเพื่อเปรียบเทียบข้อมูล

```python
fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(10, 4))

# กราฟที่ 1: Histogram ของ Age
axes[0].hist(df['Age'], bins=5, color='skyblue')
axes[0].set_title('การกระจายตัวของอายุ')

# กราฟที่ 2: Scatter Plot ของ Age vs Salary
axes[1].scatter(df['Age'], df['Salary'], color='red')
axes[1].set_title('อายุเทียบกับเงินเดือน')

plt.tight_layout() # ปรับระยะห่างระหว่างกราฟ
plt.show()
```

**Heatmap (แผนที่ความร้อน):** ใช้แสดงความสัมพันธ์ (Correlation) ระหว่างตัวแปรต่างๆ ในชุดข้อมูล

```python
# คำนวณ Correlation Matrix
correlation_matrix = df[['Age', 'Salary']].corr()

# สร้าง Heatmap ด้วย Seaborn
plt.figure(figsize=(6, 5))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Correlation Heatmap')
plt.show()
```

## 3.4 Interactive Visualization: แนะนำ Plotly/Bokeh

สำหรับงานที่ต้องการการโต้ตอบกับผู้ใช้ (เช่น Dashboard) ไลบรารี Plotly และ Bokeh เป็นทางเลือกที่ดี

**Plotly:** สามารถสร้างกราฟที่สวยงามและโต้ตอบได้ง่าย โดยเฉพาะอย่างยิ่งเมื่อใช้ร่วมกับ Dash หรือ Streamlit

**ตัวอย่าง: Plotly Scatter Plot (แนวคิด)**

```python
import plotly.express as px

# สมมติว่า df คือ DataFrame ที่มีข้อมูล
fig = px.scatter(df, x="Age", y="Salary", color="City", title="Interactive Scatter Plot")
# fig.show() # จะแสดงกราฟในเบราว์เซอร์
```

## 3.5 กรณีศึกษา: การวิเคราะห์ชุดข้อมูลจริง (Titanic Data)

**ขั้นตอนการวิเคราะห์ข้อมูลเบื้องต้น (EDA) บนชุดข้อมูล Titanic:**
1.  **การโหลดข้อมูล:** โหลดไฟล์ `titanic.csv` เข้าสู่ Pandas DataFrame
2.  **การสำรวจข้อมูล:** ใช้ `df.head()`, `df.info()`, `df.describe()` เพื่อทำความเข้าใจโครงสร้างข้อมูล
3.  **การจัดการ Missing Data:** ตรวจสอบคอลัมน์ที่มีค่าว่าง (เช่น `Age`, `Cabin`, `Embarked`) และตัดสินใจว่าจะลบหรือแทนที่
4.  **การวิเคราะห์เชิงสถิติ:** ใช้ GroupBy เพื่อหาอัตราการรอดชีวิต (`Survived`) ตามเพศ (`Sex`) และชั้นโดยสาร (`Pclass`)
5.  **การสร้างภาพข้อมูล:** สร้าง Bar Plot เพื่อแสดงอัตราการรอดชีวิตตามกลุ่มต่างๆ และ Histogram เพื่อดูการกระจายตัวของอายุ

## 3.6 แบบฝึกหัดและเฉลย (โมดูล 3)

**แบบฝึกหัด 3.1: Pandas GroupBy และ Merge**
1.  สร้าง DataFrame ชื่อ `sales` (คอลัมน์: `Product`, `Region`, `Revenue`)
2.  ใช้ `GroupBy` เพื่อหาผลรวมรายได้ (`Revenue`) ของแต่ละ `Region`
3.  สร้าง DataFrame ชื่อ `targets` (คอลัมน์: `Region`, `Target`)
4.  ใช้ `Merge` เพื่อรวม `sales` และ `targets` เข้าด้วยกัน

**แบบฝึกหัด 3.2: Data Cleaning**
สมมติว่าคุณมี DataFrame ที่มีคอลัมน์ `Price` ที่มีค่า NaN อยู่ 30% จงเขียนโค้ดเพื่อแทนที่ค่า NaN เหล่านั้นด้วยค่าเฉลี่ยของคอลัมน์ `Price`

**เฉลย 3.1:**
```python
sales = pd.DataFrame({
    'Product': ['A', 'B', 'A', 'C', 'B'],
    'Region': ['North', 'South', 'North', 'East', 'South'],
    'Revenue': [100, 150, 200, 50, 100]
})
targets = pd.DataFrame({
    'Region': ['North', 'South', 'East'],
    'Target': [300, 200, 100]
})

# 2. GroupBy
regional_revenue = sales.groupby('Region')['Revenue'].sum().reset_index()

# 4. Merge
merged_targets = pd.merge(regional_revenue, targets, on='Region', how='left')
print(merged_targets)
```

**เฉลย 3.2:**
```python
# สมมติ DataFrame
df_price = pd.DataFrame({'Price': [10, 20, np.nan, 40, np.nan, 60]})

# คำนวณค่าเฉลี่ย
mean_price = df_price['Price'].mean()

# แทนที่ NaN
df_price['Price_Filled'] = df_price['Price'].fillna(mean_price)
print(df_price)
```
---
**หมายเหตุ:** เนื้อหาส่วนนี้เป็นส่วนขยายของโมดูล 3 ซึ่งจะถูกนำไปรวมกับเนื้อหาโมดูลอื่น ๆ ที่ขยายแล้ว เพื่อให้ได้คู่มือฉบับสมบูรณ์ 200-300 หน้า
