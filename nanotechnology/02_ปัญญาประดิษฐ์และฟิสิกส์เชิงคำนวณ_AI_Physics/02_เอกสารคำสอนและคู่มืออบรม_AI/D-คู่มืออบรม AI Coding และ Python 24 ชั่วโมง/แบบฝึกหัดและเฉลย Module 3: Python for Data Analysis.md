# แบบฝึกหัดและเฉลย Module 3: Python for Data Analysis

## ส่วนที่ 1: แบบฝึกหัดเชิงปฏิบัติการ

### Exercise 1: NumPy Array Operations and Broadcasting

**โจทย์:**
คุณได้รับข้อมูลการใช้พลังงานรายวัน (kWh) ของเครื่องจักร 3 เครื่องในช่วง 7 วัน

1.  สร้าง NumPy Array 2 มิติ (3x7) ชื่อ `daily_consumption` จากข้อมูลด้านล่าง
2.  สร้าง Array 1 มิติ ชื่อ `machine_cost` ที่เก็บค่าใช้จ่ายต่อ kWh ของแต่ละเครื่อง (0.5, 0.6, 0.4 บาท/kWh)
3.  ใช้เทคนิค **Broadcasting** เพื่อคำนวณค่าใช้จ่ายรวมรายวัน (Total Cost) ของแต่ละเครื่อง
4.  คำนวณค่าใช้จ่ายรวมทั้งหมดในช่วง 7 วันของทุกเครื่อง

**Input Data:**
```python
import numpy as np
# Row: Machine 1, 2, 3
# Column: Day 1 to Day 7
consumption_data = [
    [10, 12, 15, 11, 13, 14, 16],
    [20, 22, 25, 21, 23, 24, 26],
    [5, 6, 7, 5, 8, 9, 10]
]
cost_per_kwh = [0.5, 0.6, 0.4]
```

---

### Exercise 2: Pandas Data Cleaning and Transformation

**โจทย์:**
คุณได้รับ DataFrame ที่มีข้อมูลยอดขายสินค้า โดยมีค่าที่ขาดหาย (NaN) และข้อมูลที่ไม่สอดคล้องกัน

1.  สร้าง DataFrame จากข้อมูลด้านล่าง
2.  ตรวจสอบและนับจำนวนค่า NaN ในแต่ละคอลัมน์
3.  จัดการค่า NaN ในคอลัมน์ 'Price' โดยการเติมด้วยค่า **มัธยฐาน (Median)** ของคอลัมน์นั้น
4.  จัดการค่า NaN ในคอลัมน์ 'Category' โดยการเติมด้วยค่า **'Unknown'**
5.  สร้างคอลัมน์ใหม่ชื่อ 'Revenue' โดยคำนวณจาก 'Quantity' * 'Price'

**Input Data:**
```python
import pandas as pd
import numpy as np
data = {
    'Product': ['A', 'B', 'C', 'D', 'E', 'F'],
    'Category': ['Electronics', 'Clothing', np.nan, 'Electronics', 'Clothing', np.nan],
    'Quantity': [10, 5, 12, 8, 15, 7],
    'Price': [100.5, 20.0, 50.0, np.nan, 30.0, 45.0]
}
```

---

### Exercise 3: Pandas Advanced Manipulation - GroupBy

**โจทย์:**
ใช้เทคนิค `groupby()` เพื่อวิเคราะห์ข้อมูลยอดขายที่ถูกทำความสะอาดแล้วจาก Exercise 2

1.  ใช้ DataFrame ที่ได้จากการทำความสะอาดใน Exercise 2
2.  คำนวณยอดรวมของ 'Revenue' และจำนวนสินค้าที่ขายได้รวม ('Quantity') สำหรับแต่ละ 'Category'
3.  คำนวณราคาเฉลี่ย ('Price') ของสินค้าในแต่ละ 'Category'
4.  แสดงผลลัพธ์ในรูปแบบ DataFrame ที่สรุปข้อมูลตาม 'Category'

---

### Exercise 4: Data Visualization - Univariate Analysis (Histogram & Box Plot)

**โจทย์:**
ใช้ Matplotlib และ Seaborn เพื่อวิเคราะห์การกระจายตัวของข้อมูล 'Price' (หลังการทำความสะอาด)

1.  ใช้ DataFrame ที่ได้จากการทำความสะอาดใน Exercise 2
2.  สร้าง **Histogram** ของคอลัมน์ 'Price' เพื่อดูการกระจายตัวของราคา
3.  สร้าง **Box Plot** ของคอลัมน์ 'Price' เพื่อระบุค่า Outliers (ถ้ามี)
4.  **หมายเหตุ:** เนื่องจากในสภาพแวดล้อมนี้ไม่สามารถแสดงกราฟได้โดยตรง ให้เขียนโค้ดที่ถูกต้องสำหรับการสร้างกราฟทั้งสอง

---

### Exercise 5: Data Visualization - Bivariate Analysis (Heatmap)

**โจทย์:**
ใช้ Seaborn เพื่อวิเคราะห์ความสัมพันธ์ระหว่างตัวแปรเชิงปริมาณใน DataFrame

1.  สร้าง DataFrame ที่มีตัวแปรเชิงปริมาณ 3 ตัว (Feature1, Feature2, Feature3)
2.  คำนวณ **Correlation Matrix** ของตัวแปรทั้งสาม
3.  สร้าง **Heatmap** จาก Correlation Matrix เพื่อแสดงความสัมพันธ์ระหว่างตัวแปร
4.  **หมายเหตุ:** เนื่องจากในสภาพแวดล้อมนี้ไม่สามารถแสดงกราฟได้โดยตรง ให้เขียนโค้ดที่ถูกต้องสำหรับการสร้าง Heatmap พร้อมการแสดงค่า Correlation บนกราฟ

**Input Data:**
```python
import pandas as pd
data_corr = {
    'Feature1': [10, 12, 15, 11, 13, 14, 16, 18, 20, 22],
    'Feature2': [5, 6, 7, 5, 8, 9, 10, 11, 12, 13],
    'Feature3': [100, 95, 90, 105, 88, 85, 80, 75, 70, 65]
}
```

---
---

## ส่วนที่ 2: เฉลยแบบฝึกหัดเชิงปฏิบัติการ

### Exercise 1: NumPy Array Operations and Broadcasting

#### Solution Code:
```python
import numpy as np

consumption_data = [
    [10, 12, 15, 11, 13, 14, 16],
    [20, 22, 25, 21, 23, 24, 26],
    [5, 6, 7, 5, 8, 9, 10]
]
cost_per_kwh = [0.5, 0.6, 0.4]

# 1. สร้าง NumPy Array 2 มิติ
daily_consumption = np.array(consumption_data)

# 2. สร้าง Array 1 มิติสำหรับค่าใช้จ่ายต่อ kWh
machine_cost = np.array(cost_per_kwh)
# ปรับรูปร่างให้เป็น (3, 1) เพื่อให้ Broadcasting ทำงานกับ Array (3, 7)
machine_cost = machine_cost.reshape(-1, 1) 

# 3. คำนวณค่าใช้จ่ายรวมรายวัน (Broadcasting)
daily_cost = daily_consumption * machine_cost

# 4. คำนวณค่าใช้จ่ายรวมทั้งหมด
total_cost = daily_cost.sum()

print("1. Daily Consumption Array (3x7):")
print(daily_consumption)
print("\n2. Machine Cost Array (3x1):")
print(machine_cost)
print("\n3. Daily Cost Array (Broadcasting):")
print(daily_cost)
print(f"\n4. Total Cost (7 days, 3 machines): {total_cost:.2f} บาท")
```

#### คำอธิบาย:
- **Broadcasting:** NumPy อนุญาตให้เราคูณ Array ที่มีรูปร่างต่างกันได้ โดย `machine_cost` (3x1) จะถูกขยาย (Broadcast) ไปตามคอลัมน์เพื่อให้สามารถคูณกับ `daily_consumption` (3x7) ได้อย่างถูกต้อง

---

### Exercise 2: Pandas Data Cleaning and Transformation

#### Solution Code:
```python
import pandas as pd
import numpy as np

data = {
    'Product': ['A', 'B', 'C', 'D', 'E', 'F'],
    'Category': ['Electronics', 'Clothing', np.nan, 'Electronics', 'Clothing', np.nan],
    'Quantity': [10, 5, 12, 8, 15, 7],
    'Price': [100.5, 20.0, 50.0, np.nan, 30.0, 45.0]
}
df = pd.DataFrame(data)

# 2. ตรวจสอบและนับจำนวนค่า NaN
# print("Missing Values Count:")
# print(df.isnull().sum())

# 3. จัดการค่า NaN ในคอลัมน์ 'Price' ด้วย Median
price_median = df['Price'].median()
df['Price'].fillna(price_median, inplace=True)

# 4. จัดการค่า NaN ในคอลัมน์ 'Category' ด้วย 'Unknown'
df['Category'].fillna('Unknown', inplace=True)

# 5. สร้างคอลัมน์ใหม่ชื่อ 'Revenue'
df['Revenue'] = df['Quantity'] * df['Price']

print("Cleaned DataFrame with Revenue:")
print(df)
```

#### คำอธิบาย:
- **`df.isnull().sum()`** ใช้เพื่อตรวจสอบจำนวนค่า NaN ในแต่ละคอลัมน์
- การเติมค่า NaN ในคอลัมน์ตัวเลข (Price) ด้วยค่ามัธยฐาน (Median) เป็นวิธีที่นิยมใช้เพื่อลดผลกระทบจาก Outliers
- การเติมค่า NaN ในคอลัมน์หมวดหมู่ (Category) ด้วย 'Unknown' ช่วยให้สามารถวิเคราะห์ข้อมูลในหมวดหมู่นี้ได้โดยไม่สูญเสียข้อมูล

---

### Exercise 3: Pandas Advanced Manipulation - GroupBy

#### Solution Code:
```python
# ใช้ DataFrame ที่ทำความสะอาดแล้วจาก Exercise 2
# (สมมติว่าโค้ด Exercise 2 ถูกรันมาก่อน)

# 1. คำนวณยอดรวมของ Revenue และ Quantity
summary_revenue_quantity = df.groupby('Category').agg({
    'Revenue': 'sum',
    'Quantity': 'sum'
})

# 2. คำนวณราคาเฉลี่ย (Price)
summary_price_mean = df.groupby('Category')['Price'].mean().reset_index(name='Average_Price')

# 3. รวมผลลัพธ์ทั้งหมด
summary_df = summary_revenue_quantity.merge(summary_price_mean, on='Category')

print("Summary DataFrame by Category:")
print(summary_df)
```

#### คำอธิบาย:
- **`groupby('Category').agg(...)`** ช่วยให้เราสามารถใช้ฟังก์ชันการรวม (Aggregation) หลายฟังก์ชันพร้อมกันกับหลายคอลัมน์ได้
- **`merge()`** ใช้เพื่อรวมผลลัพธ์จาก `groupby` สองชุดเข้าด้วยกันโดยใช้ 'Category' เป็น Key

---

### Exercise 4: Data Visualization - Univariate Analysis (Histogram & Box Plot)

#### Solution Code:
```python
import matplotlib.pyplot as plt
import seaborn as sns
# ใช้ DataFrame ที่ทำความสะอาดแล้วจาก Exercise 2

# 1. Histogram ของคอลัมน์ 'Price'
plt.figure(figsize=(8, 5))
sns.histplot(df['Price'], kde=True, bins=5, color='#FF6B35')
plt.title('Distribution of Product Prices (Histogram)')
plt.xlabel('Price (บาท)')
plt.ylabel('Frequency')
# plt.show() 

# 2. Box Plot ของคอลัมน์ 'Price'
plt.figure(figsize=(6, 4))
sns.boxplot(y=df['Price'], color='#4ECDC4')
plt.title('Box Plot of Product Prices')
plt.ylabel('Price (บาท)')
# plt.show() 
```

#### คำอธิบาย:
- **`sns.histplot`** ใช้เพื่อสร้าง Histogram พร้อมเส้น Kernel Density Estimate (KDE) เพื่อแสดงรูปร่างของการกระจายตัวของข้อมูล
- **`sns.boxplot`** ใช้เพื่อแสดงค่าสถิติ 5 ตัว (Min, Q1, Median, Q3, Max) และ Outliers ซึ่งช่วยในการระบุความผิดปกติของข้อมูล

---

### Exercise 5: Data Visualization - Bivariate Analysis (Heatmap)

#### Solution Code:
```python
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data_corr = {
    'Feature1': [10, 12, 15, 11, 13, 14, 16, 18, 20, 22],
    'Feature2': [5, 6, 7, 5, 8, 9, 10, 11, 12, 13],
    'Feature3': [100, 95, 90, 105, 88, 85, 80, 75, 70, 65]
}
df_corr = pd.DataFrame(data_corr)

# 1. คำนวณ Correlation Matrix
corr_matrix = df_corr.corr()

# 2. สร้าง Heatmap
plt.figure(figsize=(7, 6))
sns.heatmap(corr_matrix, 
            annot=True,        # แสดงค่า Correlation บน Heatmap
            cmap='coolwarm',   # ใช้โทนสีที่เหมาะสม
            fmt=".2f",         # แสดงทศนิยม 2 ตำแหน่ง
            linewidths=.5,     # เพิ่มเส้นแบ่ง
            center=0)          # กำหนดให้ 0 เป็นจุดศูนย์กลางของสี
plt.title('Correlation Heatmap of Features')
# plt.show() 

print("Correlation Matrix:")
print(corr_matrix)
```

#### คำอธิบาย:
- **`df_corr.corr()`** คำนวณค่าสัมประสิทธิ์สหสัมพันธ์ (Correlation Coefficient) ระหว่างทุกคู่ของตัวแปร
- **`sns.heatmap`** ใช้เพื่อแสดง Correlation Matrix โดยใช้สีเพื่อบ่งบอกความแรงและทิศทางของความสัมพันธ์ (สีแดง/ส้ม = สัมพันธ์เชิงบวก, สีน้ำเงิน = สัมพันธ์เชิงลบ)
- **`annot=True`** ทำให้แสดงค่าตัวเลขของ Correlation บน Heatmap ด้วย

---
