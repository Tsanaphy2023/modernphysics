# แบบฝึกหัดเชิงปฏิบัติการ Module 3: Python for Data Analysis

## Exercise 1: NumPy Array Operations and Broadcasting

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

## Exercise 2: Pandas Data Cleaning and Transformation

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

## Exercise 3: Pandas Advanced Manipulation - GroupBy

**โจทย์:**
ใช้เทคนิค `groupby()` เพื่อวิเคราะห์ข้อมูลยอดขายที่ถูกทำความสะอาดแล้วจาก Exercise 2

1.  ใช้ DataFrame ที่ได้จากการทำความสะอาดใน Exercise 2
2.  คำนวณยอดรวมของ 'Revenue' และจำนวนสินค้าที่ขายได้รวม ('Quantity') สำหรับแต่ละ 'Category'
3.  คำนวณราคาเฉลี่ย ('Price') ของสินค้าในแต่ละ 'Category'
4.  แสดงผลลัพธ์ในรูปแบบ DataFrame ที่สรุปข้อมูลตาม 'Category'

---

## Exercise 4: Data Visualization - Univariate Analysis (Histogram & Box Plot)

**โจทย์:**
ใช้ Matplotlib และ Seaborn เพื่อวิเคราะห์การกระจายตัวของข้อมูล 'Price' (หลังการทำความสะอาด)

1.  ใช้ DataFrame ที่ได้จากการทำความสะอาดใน Exercise 2
2.  สร้าง **Histogram** ของคอลัมน์ 'Price' เพื่อดูการกระจายตัวของราคา
3.  สร้าง **Box Plot** ของคอลัมน์ 'Price' เพื่อระบุค่า Outliers (ถ้ามี)
4.  **หมายเหตุ:** เนื่องจากในสภาพแวดล้อมนี้ไม่สามารถแสดงกราฟได้โดยตรง ให้เขียนโค้ดที่ถูกต้องสำหรับการสร้างกราฟทั้งสอง

---

## Exercise 5: Data Visualization - Bivariate Analysis (Heatmap)

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
