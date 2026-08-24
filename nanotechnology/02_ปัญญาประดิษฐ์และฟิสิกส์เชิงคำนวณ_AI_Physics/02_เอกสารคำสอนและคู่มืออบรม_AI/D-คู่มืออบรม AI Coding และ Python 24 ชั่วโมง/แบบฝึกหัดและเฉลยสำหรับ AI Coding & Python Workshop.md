# แบบฝึกหัดและเฉลยสำหรับ AI Coding & Python Workshop

## เฉลยโมดูล 2

### Solution 2.2: การออกแบบ Data Preprocessor ที่ยืดหยุ่นด้วย OOP
```python
from abc import ABC, abstractmethod

class BasePreprocessor(ABC):
    @abstractmethod
    def preprocess(self, data):
        pass

class MinMaxScaler(BasePreprocessor):
    def __init__(self, min_val=0, max_val=1):
        self.min_val = min_val
        self.max_val = max_val

    def preprocess(self, data):
        if not data:
            return []
        data_min = min(data)
        data_max = max(data)
        if data_max == data_min:
            return [self.min_val for _ in data] # Avoid division by zero
        scaled_data = [
            self.min_val + (x - data_min) * (self.max_val - self.min_val) / (data_max - data_min)
            for x in data
        ]
        return scaled_data

class StandardScaler(BasePreprocessor):
    def __init__(self, data=None):
        self.mean = 0
        self.std = 1
        if data:
            self.fit(data)

    def fit(self, data):
        if not data:
            raise ValueError("Data cannot be empty for fitting StandardScaler")
        import numpy as np
        self.mean = np.mean(data)
        self.std = np.std(data)
        if self.std == 0:
            self.std = 1 # Avoid division by zero

    def preprocess(self, data):
        if not data:
            return []
        if self.std == 0:
            # If std is 0, all values are the same, return 0 after centering
            return [0.0 for _ in data]
        standardized_data = [
            (x - self.mean) / self.std
            for x in data
        ]
        return standardized_data

class Pipeline:
    def __init__(self, preprocessors):
        if not all(isinstance(p, BasePreprocessor) for p in preprocessors):
            raise TypeError("All pipeline steps must be instances of BasePreprocessor")
        self.preprocessors = preprocessors

    def process(self, data):
        processed_data = list(data) # Create a mutable copy
        for preprocessor in self.preprocessors:
            processed_data = preprocessor.preprocess(processed_data)
        return processed_data

# Usage
data_to_process = [10, 20, 30, 40, 50]

# Initialize preprocessors
min_max_scaler = MinMaxScaler()
standard_scaler = StandardScaler(data_to_process) # Fit during initialization

# Create a pipeline
pipeline = Pipeline([min_max_scaler, standard_scaler])

# Process data
final_processed_data = pipeline.process(data_to_process)

print(f"Original Data: {data_to_process}")
print(f"MinMax Scaled then Standard Scaled Data: {final_processed_data}")

# Example with only one scaler
pipeline_minmax = Pipeline([min_max_scaler])
minmax_only_data = pipeline_minmax.process(data_to_process)
print(f"MinMax Scaled Only Data: {minmax_only_data}")
```

### Solution 2.3: การใช้งาน Caching Decorator สำหรับการทำนายโมเดล
```python
import time

def cache_predictions(func):
    cache = {}
    def wrapper(*args, **kwargs):
        # Create a hashable key from arguments
        key = (args, frozenset(kwargs.items()))
        if key in cache:
            print(f"Cache hit for {func.__name__} with args {args}, kwargs {kwargs}")
            return cache[key]
        else:
            print(f"Cache miss for {func.__name__} with args {args}, kwargs {kwargs}. Computing...")
            result = func(*args, **kwargs)
            cache[key] = result
            return result
    return wrapper

@cache_predictions
def predict_sentiment(text):
    print(f"Actually predicting sentiment for: \'{text}\'")
    time.sleep(0.5) # Simulate a delay
    if "good" in text.lower() or "great" in text.lower():
        return "Positive"
    elif "bad" in text.lower() or "terrible" in text.lower():
        return "Negative"
    else:
        return "Neutral"

# Demonstrate caching
print(predict_sentiment("This product is great!"))
print(predict_sentiment("This product is great!")) # Should be cached
print(predict_sentiment("I had a terrible experience."))
print(predict_sentiment("This product is good."))
print(predict_sentiment("I had a terrible experience.")) # Should be cached
```

### Solution 2.4: Custom Context Manager สำหรับการจัดการ API Key อย่างปลอดภัย
```python
import os
from contextlib import contextmanager

@contextmanager
def api_key_loader(key_name):
    original_value = os.environ.get(key_name) # Store original value
    try:
        api_key = os.environ.get(key_name)
        if not api_key:
            raise ValueError(f"API key \'{key_name}\' not found in environment variables.")
        print(f"API key \'{key_name}\' loaded successfully.")
        yield api_key
    finally:
        # Clean up: remove the key or restore original value
        if original_value is None:
            if key_name in os.environ:
                del os.environ[key_name]
                print(f"API key \'{key_name}\' removed from environment.")
        else:
            os.environ[key_name] = original_value
            print(f"API key \'{key_name}\' restored to original value.")

# Dummy function that uses the API key
def call_ai_service(api_key, prompt):
    print(f"Calling AI service with key: {api_key[:5]}... and prompt: \'{prompt}\'")
    # Simulate API call
    return f"AI response for \'{prompt}\'"

# --- Demonstration ---

# Test Case 1: Key exists and is used
os.environ["MY_OPENAI_KEY"] = "sk-1234567890abcdef"
with api_key_loader("MY_OPENAI_KEY") as key:
    response = call_ai_service(key, "Generate a Python function")
    print(f"Service Response: {response}")
print(f"After context: MY_OPENAI_KEY is {os.environ.get(\'MY_OPENAI_KEY\')}") # Should be restored

print("\n")

# Test Case 2: Key does not exist (should raise error)
if "NON_EXISTENT_KEY" in os.environ:
    del os.environ["NON_EXISTENT_KEY"]

try:
    with api_key_loader("NON_EXISTENT_KEY") as key:
        print("This should not be printed")
except ValueError as e:
    print(f"Caught expected error: {e}")
print(f"After context: NON_EXISTENT_KEY is {os.environ.get(\'NON_EXISTENT_KEY\')}") # Should be None

print("\n")

# Test Case 3: Key exists, but an error occurs inside the \'with\' block
os.environ["ANOTHER_API_KEY"] = "gh-fedcba9876543210"
try:
    with api_key_loader("ANOTHER_API_KEY") as key:
        print(f"Using key: {key[:5]}...")
        raise RuntimeError("Simulated error during service call")
except RuntimeError as e:
    print(f"Caught error outside context: {e}")
print(f"After context with error: ANOTHER_API_KEY is {os.environ.get(\'ANOTHER_API_KEY\')}") # Should be restored
```

### Solution 2.5: การสร้าง Configurable Feature Extractor ด้วย `namedtuple` และ OOP
```python
from abc import ABC, abstractmethod
from collections import namedtuple

# 1. Define a namedtuple for extracted features
FeatureSet = namedtuple(
    \'FeatureSet\',
    [\'numerical_features\', \'categorical_features\', \'text_features\']
)

# 2. Create an abstract base class BaseFeatureExtractor
class BaseFeatureExtractor(ABC):
    @abstractmethod
    def extract(self, data) -> FeatureSet:
        pass

# 3. Create a concrete class TextFeatureExtractor
class TextFeatureExtractor(BaseFeatureExtractor):
    def __init__(self, keywords_to_check=None):
        self.keywords_to_check = [k.lower() for k in keywords_to_check] if keywords_to_check else []

    def extract(self, text_data: str) -> FeatureSet:
        text_lower = text_data.lower()

        # Numerical features
        text_length = len(text_data)

        # Categorical features
        has_keywords = any(keyword in text_lower for keyword in self.keywords_to_check)

        # Text features (simplified for this example)
        first_10_chars = text_data[:10]

        return FeatureSet(
            numerical_features={\'length\': text_length},
            categorical_features={\'has_keywords\': has_keywords},
            text_features={\'first_10_chars\': first_10_chars}
        )

# 4. Create a concrete class NumericalFeatureExtractor
class NumericalFeatureExtractor(BaseFeatureExtractor):
    def extract(self, data: list) -> FeatureSet:
        if not data:
            return FeatureSet({}, {}, {})

        min_val = min(data)
        max_val = max(data)
        avg_val = sum(data) / len(data)

        return FeatureSet(
            numerical_features={
                \'min_value\': min_val,
                \'max_value\': max_val,
                \'average_value\': avg_val
            },
            categorical_features={},
            text_features={}
        )

# 5. Create a FeaturePipeline class
class FeaturePipeline:
    def __init__(self, extractors: list[BaseFeatureExtractor]):
        self.extractors = extractors

    def process(self, data) -> dict:
        combined_features = {
            \'numerical_features\': {},
            \'categorical_features\': {},
            \'text_features\': {}
        }
        for extractor in self.extractors:
            features = extractor.extract(data)
            combined_features[\'numerical_features\'].update(features.numerical_features)
            combined_features[\'categorical_features\'].update(features.categorical_features)
            combined_features[\'text_features\'].update(features.text_features)
        return combined_features

# Usage Example:
text_data_sample = "This is a sample document about machine learning and AI. It contains some important keywords."
numerical_data_sample = [10, 20, 30, 40, 50, 15, 25]

text_extractor = TextFeatureExtractor(keywords_to_check=["machine learning", "AI", "keywords"])
num_extractor = NumericalFeatureExtractor()

pipeline = FeaturePipeline([text_extractor, num_extractor])

# Process text data
text_features = pipeline.process(text_data_sample)
print("\nText Features:")
print(text_features)

# Process numerical data
num_features = pipeline.process(numerical_data_sample)
print("\nNumerical Features:")
print(num_features)

# Example with both extractors in a pipeline (conceptual, as data types differ)
# In a real scenario, you'd likely have separate pipelines or a more complex extractor
# that handles mixed data types.
# For demonstration, let's assume a single data point could have both text and numerical aspects
class MixedDataExtractor(BaseFeatureExtractor):
    def __init__(self, text_keywords=None):
        self.text_extractor = TextFeatureExtractor(text_keywords)
        self.num_extractor = NumericalFeatureExtractor()

    def extract(self, data: dict) -> FeatureSet:
        text_features = self.text_extractor.extract(data.get(\'text_field\', \'\'))
        num_features = self.num_extractor.extract(data.get(\'numerical_field\', []))

        return FeatureSet(
            numerical_features={**text_features.numerical_features, **num_features.numerical_features},
            categorical_features={**text_features.categorical_features, **num_features.categorical_features},
            text_features={**text_features.text_features, **num_features.text_features}
        )

mixed_extractor = MixedDataExtractor(text_keywords=["data", "analysis"])
mixed_data_sample = {
    \'text_field\': "This document discusses data analysis techniques.",
    \'numerical_field\': [1, 2, 3, 4, 5]
}
mixed_features = FeaturePipeline([mixed_extractor]).process(mixed_data_sample)
print("\nMixed Data Features:")
print(mixed_features)
```
```
```
## แบบฝึกหัดโมดูล 1

### แบบฝึกหัด 1.1: การจัดการ List
สร้าง list ของตัวเลขตั้งแต่ 1 ถึง 10 จากนั้นดำเนินการต่อไปนี้:
1.  เพิ่มเลข 11 ต่อท้าย
2.  ลบเลข 5 ออก
3.  แทรกเลข 0 ที่ตอนต้น
4.  พิมพ์ list สุดท้าย

### แบบฝึกหัด 1.2: การดำเนินการกับ Dictionary
สร้าง dictionary ที่แสดงเกรดของนักเรียน:
`grades = {'Math': 90, 'Science': 85, 'History': 78}`
1.  เพิ่มวิชาใหม่ 'Art' พร้อมเกรด 92
2.  อัปเดตเกรดวิชา 'Science' เป็น 88
3.  พิมพ์ชื่อทุกวิชา
4.  พิมพ์เกรดทั้งหมด

### แบบฝึกหัด 1.3: ฟังก์ชันที่รับอาร์กิวเมนต์ไม่จำกัดจำนวน
เขียนฟังก์ชัน Python `calculate_average(*args)` ที่รับอาร์กิวเมนต์ตัวเลขจำนวนเท่าใดก็ได้และคืนค่าเฉลี่ย ทดสอบฟังก์ชันด้วยตัวอย่างสองสามชุด

### แบบฝึกหัด 1.4: พื้นฐาน NumPy Array
1.  สร้าง NumPy array `arr1` จาก list `[1, 2, 3, 4, 5]`
2.  สร้าง NumPy array `arr2` ขนาด 2x3 ที่เต็มไปด้วยเลข 1
3.  คูณ `arr1` (หลังจากปรับรูปร่างเป็น 1x5) กับ `arr2` แบบ element-wise (คุณจะต้องพิจารณาการ broadcasting หรือการปรับรูปร่าง)

### แบบฝึกหัด 1.5: การกรอง Pandas DataFrame
ใช้ `df` DataFrame จากตัวอย่าง Pandas ในโมดูล:
1.  กรอง DataFrame เพื่อแสดงเฉพาะนักเรียนที่อายุมากกว่า 28 ปี
2.  เพิ่มคอลัมน์ใหม่ 'Score' ที่มีค่า `[80, 95, 70]`
3.  พิมพ์ DataFrame ที่เรียงลำดับตาม 'Score' จากมากไปน้อย
## เฉลยโมดูล 1

### เฉลย 1.1: การจัดการ List
```python
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
my_list.append(11)
my_list.remove(5)
my_list.insert(0, 0)
print(my_list)
```

### เฉลย 1.2: การดำเนินการกับ Dictionary
```python
grades = {"Math": 90, "Science": 85, "History": 78}
grades["Art"] = 92
grades["Science"] = 88
print("Subjects:", grades.keys())
print("Grades:", grades.values())
```

### เฉลย 1.3: ฟังก์ชันที่รับอาร์กิวเมนต์ไม่จำกัดจำนวน
```python
def calculate_average(*args):
    if not args:
        return 0
    return sum(args) / len(args)

print(calculate_average(1, 2, 3, 4, 5))
print(calculate_average(10, 20, 30))
```

### เฉลย 1.4: พื้นฐาน NumPy Array
```python
import numpy as np

arr1 = np.array([1, 2, 3, 4, 5])
arr2 = np.ones((1, 5)) # ปรับรูปร่าง arr2 ให้เข้ากับ arr1 สำหรับการคูณแบบ element-wise

# ในการคูณแบบ element-wise, arrays จำเป็นต้องสามารถ broadcast ได้
# ถ้า arr1 เป็น (5,) และ arr2 เป็น (1,5) จะทำงานได้
# ถ้า arr1 เป็น (5,) และ arr2 เป็น (2,3) จะไม่สามารถทำงานได้โดยตรงแบบ element-wise
# สมมติว่าความตั้งใจคือการคูณ array 1D กับ array 1xN

# แก้ไขสำหรับการคูณแบบ element-wise ด้วย broadcasting
result = arr1 * arr2
print("arr1:", arr1)
print("arr2:", arr2)
print("Element-wise multiplication:", result)

# หากความตั้งใจคือการคูณ arr1 (ปรับรูปร่างเป็น 1x5) กับ array 2x3 จะต้องมีการ broadcasting ที่ซับซ้อนมากขึ้นหรือการดำเนินการที่แตกต่างกัน
# สถานการณ์ที่เป็นไปได้มากกว่าสำหรับ arr2 ขนาด 2x3 คือการคูณเมทริกซ์หรือการดำเนินการอื่น ๆ
# เพื่อความเรียบง่าย เราจะยึดติดกับการคูณแบบ element-wise ด้วย arr2 ที่สามารถ broadcast ได้
```

### เฉลย 1.5: การกรอง Pandas DataFrame
```python
import pandas as pd

data = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [25, 30, 35],
    "City": ["New York", "Los Angeles", "Chicago"]
}
df = pd.DataFrame(data)

# กรองนักเรียนที่อายุมากกว่า 28 ปี
older_students = df[df["Age"] > 28]
print("Students older than 28:")
print(older_students)

# เพิ่มคอลัมน์ใหม่ 'Score'
df["Score"] = [80, 95, 70]
print("\nDataFrame with Score:")
print(df)

# เรียงลำดับตาม 'Score' จากมากไปน้อย
sorted_df = df.sort_values(by="Score", ascending=False)
print("\nDataFrame sorted by Score (descending):")
print(sorted_df)
```

## แบบฝึกหัดโมดูล 3

### แบบฝึกหัด 3.1: การทำความสะอาดและแปลงข้อมูล Pandas
โหลดข้อมูลต่อไปนี้ลงใน Pandas DataFrame สมมติว่าเป็นไฟล์ CSV:
`data = {"Name": ["Alice", "Bob", "Charlie", "David", "Eve"],
        "Age": [25, 30, None, 35, 28],
        "City": ["New York", "Los Angeles", "New York", "Chicago", None],
        "Salary": [70000, 80000, 60000, 90000, 75000]}`
1.  จัดการค่าที่ขาดหายไปของ 'Age' โดยการเติมด้วยค่าเฉลี่ยของอายุ
2.  จัดการค่าที่ขาดหายไปของ 'City' โดยการเติมด้วย 'Unknown'
3.  สร้างคอลัมน์ใหม่ 'Salary_USD' โดยการหาร 'Salary' ด้วย 30 (สมมติว่า 1 USD = 30 สกุลเงินท้องถิ่น)
4.  พิมพ์ DataFrame ที่ทำความสะอาดและแปลงแล้ว

### แบบฝึกหัด 3.2: การจัดกลุ่มและการรวมข้อมูล Pandas
ใช้ DataFrame จากแบบฝึกหัด 3.1 (หลังจากทำความสะอาดแล้ว):
1.  จัดกลุ่มข้อมูลตาม 'City' และคำนวณ 'Salary' เฉลี่ยสำหรับแต่ละเมือง
2.  ค้นหาเมืองที่มีเงินเดือนเฉลี่ยสูงสุด
3.  พิมพ์ผลลัพธ์

### แบบฝึกหัด 3.3: การพล็อตพื้นฐาน Matplotlib
ใช้ DataFrame ที่ทำความสะอาดแล้วจากแบบฝึกหัด 3.1:
1.  สร้างแผนภูมิแท่งแสดง 'Salary' เฉลี่ยสำหรับแต่ละ 'City'
2.  สร้างฮิสโตแกรมของ 'Age'
3.  เพิ่มชื่อเรื่องและป้ายกำกับที่เหมาะสมให้กับทั้งสองแผนภูมิ
4.  แสดงแผนภูมิ

### แบบฝึกหัด 3.4: Matplotlib Subplots และการปรับแต่ง
สร้างรูปภาพที่มีสอง subplots:
1.  subplot แรกควรเป็น scatter plot ของ 'Age' เทียบกับ 'Salary' จาก DataFrame ที่ทำความสะอาดแล้ว
2.  subplot ที่สองควรเป็น pie chart แสดงการกระจายตัวของนักเรียนในค่า 'City' ต่างๆ
3.  ปรับแต่งสี เพิ่ม legend ให้กับ pie chart และตรวจสอบให้แน่ใจว่าทั้งสองแผนภูมิมีชื่อเรื่อง
4.  บันทึกรูปภาพเป็น `plots.png`

## เฉลยโมดูล 3

### เฉลย 3.1: การทำความสะอาดและแปลงข้อมูล Pandas
```python
import pandas as pd

data = {"Name": ["Alice", "Bob", "Charlie", "David", "Eve"],
        "Age": [25, 30, None, 35, 28],
        "City": ["New York", "Los Angeles", "New York", "Chicago", None],
        "Salary": [70000, 80000, 60000, 90000, 75000]}
df = pd.DataFrame(data)

# 1. จัดการค่าที่ขาดหายไปของ 'Age' ด้วยค่าเฉลี่ย
df["Age"].fillna(df["Age"].mean(), inplace=True)

# 2. จัดการค่าที่ขาดหายไปของ 'City' ด้วย 'Unknown'
df["City"].fillna("Unknown", inplace=True)

# 3. สร้างคอลัมน์ 'Salary_USD'
df["Salary_USD"] = df["Salary"] / 30

print("Cleaned and Transformed DataFrame:")
print(df)
```

### เฉลย 3.2: การจัดกลุ่มและการรวมข้อมูล Pandas
```python
import pandas as pd

data = {"Name": ["Alice", "Bob", "Charlie", "David", "Eve"],
        "Age": [25, 30, None, 35, 28],
        "City": ["New York", "Los Angeles", "New York", "Chicago", None],
        "Salary": [70000, 80000, 60000, 90000, 75000]}
df = pd.DataFrame(data)

df["Age"].fillna(df["Age"].mean(), inplace=True)
df["City"].fillna("Unknown", inplace=True)

# 1. จัดกลุ่มตาม 'City' และคำนวณ 'Salary' เฉลี่ย
average_salary_by_city = df.groupby("City")["Salary"].mean().reset_index()
print("Average Salary by City:")
print(average_salary_by_city)

# 2. ค้นหาเมืองที่มีเงินเดือนเฉลี่ยสูงสุด
highest_salary_city = average_salary_by_city.loc[average_salary_by_city["Salary"].idxmax()]
print("\nCity with the highest average salary:")
print(highest_salary_city)
```

### เฉลย 3.3: การพล็อตพื้นฐาน Matplotlib
```python
import pandas as pd
import matplotlib.pyplot as plt

data = {"Name": ["Alice", "Bob", "Charlie", "David", "Eve"],
        "Age": [25, 30, None, 35, 28],
        "City": ["New York", "Los Angeles", "New York", "Chicago", None],
        "Salary": [70000, 80000, 60000, 90000, 75000]}
df = pd.DataFrame(data)

df["Age"].fillna(df["Age"].mean(), inplace=True)
df["City"].fillna("Unknown", inplace=True)

# 1. แผนภูมิแท่งของ Salary เฉลี่ยตาม City
average_salary_by_city = df.groupby("City")["Salary"].mean().reset_index()
plt.figure(figsize=(8, 6))
plt.bar(average_salary_by_city["City"], average_salary_by_city["Salary"], color="skyblue")
plt.xlabel("City")
plt.ylabel("Average Salary")
plt.title("Average Salary by City")
plt.grid(axis="y", linestyle="--")
plt.show()

# 2. ฮิสโตแกรมของ Age
plt.figure(figsize=(8, 6))
plt.hist(df["Age"], bins=5, color="lightcoral", edgecolor="black")
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.title("Distribution of Age")
plt.grid(axis="y", linestyle="--")
plt.show()
```

### เฉลย 3.4: Matplotlib Subplots และการปรับแต่ง
```python
import pandas as pd
import matplotlib.pyplot as plt

data = {"Name": ["Alice", "Bob", "Charlie", "David", "Eve"],
        "Age": [25, 30, None, 35, 28],
        "City": ["New York", "Los Angeles", "New York", "Chicago", None],
        "Salary": [70000, 80000, 60000, 90000, 75000]}
df = pd.DataFrame(data)

df["Age"].fillna(df["Age"].mean(), inplace=True)
df["City"].fillna("Unknown", inplace=True)

fig, axes = plt.subplots(1, 2, figsize=(14, 6))

# Subplot 1: Scatter plot ของ Age vs Salary
axes[0].scatter(df["Age"], df["Salary"], color="green", alpha=0.7)
axes[0].set_xlabel("Age")
axes[0].set_ylabel("Salary")
axes[0].set_title("Age vs Salary")
axes[0].grid(True, linestyle="--")

# Subplot 2: Pie chart ของการกระจายตัวของ City
city_counts = df["City"].value_counts()
colors = ["lightcoral", "skyblue", "lightgreen", "gold"]
axes[1].pie(city_counts, labels=city_counts.index, autopct="%1.1f%%", colors=colors, startangle=90)
axes[1].set_title("Distribution of Students by City")
axes[1].axis("equal")  # Equal aspect ratio ensures that pie is drawn as a circle.

plt.tight_layout()
plt.savefig("plots.png")
plt.show()
```

## แบบฝึกหัดโมดูล 4

### แบบฝึกหัด 4.1: Linear Regression พร้อม Feature Scaling
ใช้ข้อมูลต่อไปนี้:
`X = np.array([[10], [20], [30], [40], [50]])`
`y = np.array([15, 22, 35, 40, 50])`
1.  ใช้ `StandardScaler` กับ `X`
2.  แบ่งข้อมูลที่ปรับขนาดแล้วออกเป็นชุดฝึกอบรมและชุดทดสอบ
3.  ฝึกโมเดล `LinearRegression` บนข้อมูลการฝึกอบรมที่ปรับขนาดแล้ว
4.  ทำการทำนายบนข้อมูลทดสอบที่ปรับขนาดแล้ว
5.  ประเมินโมเดลโดยใช้ MSE และ R-squared

### แบบฝึกหัด 4.2: Logistic Regression สำหรับชุดข้อมูลที่กำหนดเอง
สร้างชุดข้อมูลอย่างง่ายสำหรับการจำแนกประเภทไบนารี:
`X = np.array([[1, 2], [1.5, 1.8], [5, 8], [8, 8], [1, 0.6], [9, 11]])`
`y = np.array([0, 0, 1, 1, 0, 1])`
1.  แบ่งข้อมูลออกเป็นชุดฝึกอบรมและชุดทดสอบ
2.  ฝึกโมเดล `LogisticRegression`
3.  ทำการทำนายบนชุดทดสอบ
4.  คำนวณและพิมพ์ค่าความแม่นยำ (accuracy), ความเที่ยงตรง (precision), การเรียกคืน (recall) และ F1-score

### แบบฝึกหัด 4.3: K-Means Clustering บนชุดข้อมูลที่กำหนดเอง
ใช้ข้อมูลต่อไปนี้:
`X = np.array([[1, 1], [1.5, 2], [5, 7], [8, 8], [1, 0.8], [9, 11], [0.5, 0.8], [7, 9]])`
1.  ใช้ K-Means clustering ด้วย `n_clusters=3`
2.  พิมพ์ป้ายกำกับคลัสเตอร์สำหรับแต่ละจุดข้อมูล
3.  พิมพ์พิกัดของจุดศูนย์กลางคลัสเตอร์
4.  (ไม่บังคับ) แสดงภาพคลัสเตอร์และจุดศูนย์กลาง
## เฉลยโมดูล 4

### เฉลย 4.1: Linear Regression พร้อม Feature Scaling
```python
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.preprocessing import StandardScaler
import numpy as np

X = np.array([[10], [20], [30], [40], [50]])
y = np.array([15, 22, 35, 40, 50])

# 1. ใช้ StandardScaler กับ X
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# 2. แบ่งข้อมูลที่ปรับขนาดแล้ว
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.4, random_state=42)

# 3. ฝึกโมเดล LinearRegression
model = LinearRegression()
model.fit(X_train, y_train)

# 4. ทำการทำนาย
y_pred = model.predict(X_test)

# 5. ประเมินโมเดล
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"Scaled Linear Regression MSE: {mse:.2f}")
print(f"Scaled Linear Regression R2: {r2:.2f}")
```

### เฉลย 4.2: Logistic Regression สำหรับชุดข้อมูลที่กำหนดเอง
```python
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
import numpy as np

X = np.array([[1, 2], [1.5, 1.8], [5, 8], [8, 8], [1, 0.6], [9, 11]])
y = np.array([0, 0, 1, 1, 0, 1])

# 1. แบ่งข้อมูล
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# 2. ฝึกโมเดล LogisticRegression
model = LogisticRegression(solver="liblinear", random_state=42)
model.fit(X_train, y_train)

# 3. ทำการทำนาย
y_pred = model.predict(X_test)

# 4. คำนวณและพิมพ์เมตริกซ์
accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred)

print(f"Accuracy: {accuracy:.2f}")
print(f"Precision: {precision:.2f}")
print(f"Recall: {recall:.2f}")
print(f"F1-Score: {f1:.2f}")
```

### เฉลย 4.3: K-Means Clustering บนชุดข้อมูลที่กำหนดเอง
```python
from sklearn.cluster import KMeans
import numpy as np
import matplotlib.pyplot as plt

X = np.array([[1, 1], [1.5, 2], [5, 7], [8, 8], [1, 0.8], [9, 11], [0.5, 0.8], [7, 9]])

# 1. ใช้ K-Means clustering ด้วย n_clusters=3
kmeans = KMeans(n_clusters=3, random_state=0, n_init=10) # n_init เพื่อระงับคำเตือน
kmeans.fit(X)

# 2. พิมพ์ป้ายกำกับคลัสเตอร์
labels = kmeans.labels_
print("Cluster Labels:", labels)

# 3. พิมพ์จุดศูนย์กลางคลัสเตอร์
centroids = kmeans.cluster_centers_
print("Cluster Centroids:\n", centroids)

# 4. (ไม่บังคับ) แสดงภาพคลัสเตอร์และจุดศูนย์กลาง
plt.scatter(X[:, 0], X[:, 1], c=labels, s=50, cmap="viridis")
plt.scatter(centroids[:, 0], centroids[:, 1], c="red", s=200, alpha=0.7, marker="X")
plt.title("K-Means Clustering on Custom Data")
plt.xlabel("Feature 1")
plt.ylabel("Feature 2")
plt.show()
```

## แบบฝึกหัดโมดูล 5

### แบบฝึกหัด 5.1: สร้างและฝึก Feedforward Network สำหรับ MNIST
1.  โหลดชุดข้อมูล MNIST จาก `tensorflow.keras.datasets`
2.  ประมวลผลข้อมูลล่วงหน้า: ปรับค่าพิกเซลให้เป็นมาตรฐานและเข้ารหัสป้ายกำกับแบบ one-hot
3.  สร้างโครงข่ายประสาทเทียมแบบ feedforward อย่างง่ายที่มีเลเยอร์ `Dense` ที่ซ่อนอยู่ตั้งแต่สองเลเยอร์ขึ้นไป
4.  คอมไพล์โมเดลด้วย optimizer, loss function และ metrics ที่เหมาะสม
5.  ฝึกโมเดลเป็นเวลาสองสาม epoch
6.  ประเมินประสิทธิภาพของโมเดลบนชุดทดสอบ

### แบบฝึกหัด 5.2: สร้างและฝึก Simple CNN สำหรับ Fashion MNIST
1.  โหลดชุดข้อมูล Fashion MNIST จาก `tensorflow.keras.datasets`
2.  ประมวลผลข้อมูลล่วงหน้า: ปรับค่าพิกเซลให้เป็นมาตรฐานและปรับรูปร่างสำหรับอินพุต CNN
3.  สร้าง CNN อย่างง่ายที่มีเลเยอร์ `Conv2D` อย่างน้อยหนึ่งเลเยอร์และเลเยอร์ `MaxPooling2D` อย่างน้อยหนึ่งเลเยอร์ ตามด้วยเลเยอร์ `Flatten` และ `Dense`
4.  คอมไพล์และฝึกโมเดล
5.  ประเมินประสิทธิภาพของโมเดลบนชุดทดสอบ
## เฉลยโมดูล 5

### เฉลย 5.1: สร้างและฝึก Feedforward Network สำหรับ MNIST
```python
import tensorflow as tf
from tensorflow.keras.datasets import mnist
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Flatten
from tensorflow.keras.utils import to_categorical

# 1. โหลดชุดข้อมูล MNIST
(x_train, y_train), (x_test, y_test) = mnist.load_data()

# 2. ประมวลผลข้อมูลล่วงหน้า
x_train = x_train.astype("float32") / 255
x_test = x_test.astype("float32") / 255

y_train = to_categorical(y_train, 10)
y_test = to_categorical(y_test, 10)

# 3. สร้างโครงข่ายประสาทเทียมแบบ feedforward
model = Sequential([
    Flatten(input_shape=(28, 28)),
    Dense(128, activation="relu"),
    Dense(64, activation="relu"),
    Dense(10, activation="softmax")
])

# 4. คอมไพล์โมเดล
model.compile(optimizer="adam",
              loss="categorical_crossentropy",
              metrics=["accuracy"])

# 5. ฝึกโมเดล
model.fit(x_train, y_train, epochs=5, batch_size=32, validation_split=0.1)

# 6. ประเมินโมเดล
loss, accuracy = model.evaluate(x_test, y_test)
print(f"\nTest Loss: {loss:.4f}")
print(f"Test Accuracy: {accuracy:.4f}")
```

### เฉลย 5.2: สร้างและฝึก Simple CNN สำหรับ Fashion MNIST
```python
import tensorflow as tf
from tensorflow.keras.datasets import fashion_mnist
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense
from tensorflow.keras.utils import to_categorical

# 1. โหลดชุดข้อมูล Fashion MNIST
(x_train, y_train), (x_test, y_test) = fashion_mnist.load_data()

# 2. ประมวลผลข้อมูลล่วงหน้า
x_train = x_train.reshape((x_train.shape[0], 28, 28, 1)).astype("float32") / 255
x_test = x_test.reshape((x_test.shape[0], 28, 28, 1)).astype("float32") / 255

y_train = to_categorical(y_train, 10)
y_test = to_categorical(y_test, 10)

# 3. สร้าง CNN อย่างง่าย
model = Sequential([
    Conv2D(32, (3, 3), activation="relu", input_shape=(28, 28, 1)),
    MaxPooling2D((2, 2)),
    Conv2D(64, (3, 3), activation="relu"),
    MaxPooling2D((2, 2)),
    Flatten(),
    Dense(64, activation="relu"),
    Dense(10, activation="softmax")
])

# 4. คอมไพล์และฝึกโมเดล
model.compile(optimizer="adam",
              loss="categorical_crossentropy",
              metrics=["accuracy"])

model.fit(x_train, y_train, epochs=5, batch_size=64, validation_split=0.1)

# 5. ประเมินโมเดล
loss, accuracy = model.evaluate(x_test, y_test)
print(f"\nTest Loss: {loss:.4f}")
print(f"Test Accuracy: {accuracy:.4f}")
```

## แบบฝึกหัดโมดูล 6

### แบบฝึกหัด 6.1: Dockerize บริการ AI ของ FastAPI อย่างง่าย
จาก `main.py` สำหรับบริการ FastAPI (ตามที่แสดงในเนื้อหาโมดูล) ให้สร้าง `Dockerfile` เพื่อทำ containerize Dockerfile ควรจะ:
1.  ใช้ Python base image
2.  ติดตั้ง dependencies ที่จำเป็น (`fastapi`, `uvicorn`, `joblib`, `pydantic`)
3.  คัดลอก `main.py` และ `model.pkl` จำลองลงใน container
4.  เปิดพอร์ต 8000
5.  กำหนดคำสั่งเพื่อรันแอปพลิเคชัน FastAPI ด้วย Uvicorn

### แบบฝึกหัด 6.2: ปรับปรุงแอป Streamlit ด้วยการโหลดโมเดล
แก้ไขตัวอย่าง `app.py` Streamlit เพื่อ:
1.  โหลด `model.pkl` จำลองจริง (คุณสามารถสร้างไฟล์จำลองได้โดยใช้ `joblib.dump(LinearRegression(), 'model.pkl')`)
2.  ใช้โมเดลที่โหลดมาเพื่อทำการทำนายแทนการคำนวณจำลอง
3.  แสดงผลการทำนายพร้อมป้ายกำกับที่ชัดเจน

### แบบฝึกหัด 6.3: Prompt Engineering สำหรับ AI Coding Assistants
**สถานการณ์:** คุณกำลังใช้ AI coding assistant เพื่อช่วยคุณเขียนฟังก์ชัน Python ที่คำนวณ factorial ของตัวเลข คุณต้องการให้ฟังก์ชันมีประสิทธิภาพและมีการจัดการข้อผิดพลาดสำหรับอินพุตที่ไม่ใช่จำนวนเต็มหรือไม่เป็นบวก

**งาน:** เขียน prompt โดยละเอียด (อย่างน้อย 3-4 ประโยค) ที่คุณจะให้กับ AI coding assistant เพื่อสร้างฟังก์ชันนี้ รวมถึงข้อกำหนดสำหรับประสิทธิภาพ การจัดการข้อผิดพลาด และ docstring

### แบบฝึกหัด 6.4: การสะท้อนโค้ดที่สร้างโดย AI
**สถานการณ์:** AI coding assistant ได้ให้ฟังก์ชัน Python ต่อไปนี้สำหรับการคำนวณ factorial:
```python
def factorial(n):
    if not isinstance(n, int) or n < 0:
        raise ValueError("Input must be a non-negative integer.")
    if n == 0:
        return 1
    else:
        res = 1
        for i in range(1, n + 1):
            res *= i
        return res
```

**งาน:**
1.  ระบุจุดแข็งหนึ่งข้อและจุดที่อาจปรับปรุงได้หนึ่งข้อในโค้ดที่สร้างโดย AI นี้
2.  แนะนำการแก้ไขเพื่อปรับปรุงจุดที่ระบุ
3.  (การสะท้อนตนเอง) เปรียบเทียบโค้ดที่ AI ปรับปรุงแล้วกับเวอร์ชันในอุดมคติของคุณเอง ระบุจุดแข็งและจุดอ่อนของผลลัพธ์ของ AI

### แบบฝึกหัด 6.5: การออกแบบ AI Agent สำหรับการวิเคราะห์ข้อมูลอัตโนมัติ (เชิงแนวคิด)
**สถานการณ์:** คุณต้องการทำให้งานวิเคราะห์ข้อมูลที่ทำซ้ำๆ เป็นไปโดยอัตโนมัติ: การโหลด CSV, การทำ EDA พื้นฐาน และการสร้างรายงานสรุป คุณจินตนาการถึง AI agent ที่สามารถทำงานนี้ได้ด้วยตนเอง

**งาน:**
1.  สรุปขั้นตอนระดับสูงที่ AI agent จะต้องดำเนินการเพื่อทำงานนี้
2.  ระบุเครื่องมือ (เชิงแนวคิด) ที่ agent จะต้องใช้
3.  อธิบายว่า agent จะใช้ chain of thought อย่างไรในการแยกย่อยและดำเนินการงาน รวมถึงวิธีจัดการกับปัญหาที่ไม่คาดคิดหรือความกำกวม

## เฉลยโมดูล 6

### เฉลย 6.1: Dockerize บริการ AI ของ FastAPI อย่างง่าย
**Dockerfile**
```dockerfile
# ใช้ Python runtime อย่างเป็นทางการเป็น base image
FROM python:3.9-slim-buster

# กำหนด working directory ใน container
WORKDIR /app

# คัดลอกเนื้อหาของไดเรกทอรีปัจจุบันไปยัง /app ใน container
COPY ./requirements.txt /app/requirements.txt
COPY ./main.py /app/main.py
COPY ./model.pkl /app/model.pkl

# ติดตั้งแพ็คเกจที่จำเป็นที่ระบุใน requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# เปิดพอร์ต 8000
EXPOSE 8000

# กำหนด environment variable สำหรับ FastAPI
ENV PYTHONPATH=/app

# รัน uvicorn server เมื่อ container เริ่มทำงาน
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
```

**requirements.txt**
```
fastapi
uvicorn
pydantic
scikit-learn # ถ้า model.pkl มาจาก sklearn
joblib
```

**main.py** (ตามที่ให้ไว้ในคำอธิบายแบบฝึกหัด)

**model.pkl** (การสร้างไฟล์จำลองเพื่อสาธิต)
```python
# รันสิ่งนี้หนึ่งครั้งเพื่อสร้าง model.pkl จำลอง
import joblib
from sklearn.linear_model import LinearRegression

dummy_model = LinearRegression()
joblib.dump(dummy_model, "model.pkl")
print("Dummy model.pkl created.")
```

**วิธีสร้างและรัน:**
```bash
# สร้าง dummy model.pkl (ถ้ายังไม่ได้สร้าง)
python -c "import joblib; from sklearn.linear_model import LinearRegression; joblib.dump(LinearRegression(), 'model.pkl')"

# สร้าง requirements.txt
echo -e "fastapi\nuvicorn\npydantic\nscikit-learn\njoblib" > requirements.txt

# สร้าง main.py
cat <<EOF > main.py
from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np
from sklearn.linear_model import LinearRegression

# โหลดโมเดลที่ฝึกไว้ล่วงหน้า (สมมติว่าบันทึกเป็น model.pkl)
model = joblib.load('model.pkl')

app = FastAPI()

class PredictionRequest(BaseModel):
    features: list[float]

class PredictionResponse(BaseModel):
    prediction: float

@app.post("/predict", response_model=PredictionResponse)
async def predict(request: PredictionRequest):
    # ในสถานการณ์จริง คุณจะใช้: model.predict([request.features])
    # สำหรับโมเดลจำลองนี้ เราจะคืนค่าผลรวมของ features เป็นการทำนาย
    input_array = [np.array(request.features)] # โมเดลคาดหวัง array 2D
    dummy_prediction = model.predict(input_array)[0] # สมมติว่า model.predict คืนค่าเป็น array
    return {"prediction": float(dummy_prediction)}
EOF

# สร้าง Docker image
docker build -t fastapi-ml-app .

# รัน Docker container
docker run -d --name ml-api -p 8000:8000 fastapi-ml-app

# ทดสอบ API (เช่น ใช้ curl หรือเบราว์เซอร์ไปที่ http://localhost:8000/docs)
# curl -X POST "http://localhost:8000/predict" -H "Content-Type: application/json" -d '{"features": [1.0, 2.0, 3.0]}'
```

### เฉลย 6.2: ปรับปรุงแอป Streamlit ด้วยการโหลดโมเดล
```python
import streamlit as st
import pandas as pd
import numpy as np
import joblib
from sklearn.linear_model import LinearRegression # จำเป็นสำหรับการสร้างโมเดลจำลอง

st.title("Simple ML Model Predictor")
st.write("Enter features to get a prediction from a trained model.")

# สร้าง model.pkl จำลองถ้าไม่มีอยู่เพื่อสาธิต
# ในแอปพลิเคชันจริง โมเดลนี้จะถูกฝึกไว้ล่วงหน้าและบันทึกไว้
try:
    model = joblib.load("model.pkl")
except FileNotFoundError:
    st.warning("ไม่พบ model.pkl กำลังสร้างโมเดล LinearRegression จำลอง")
    dummy_model = LinearRegression()
    # ฝึกโมเดลจำลองอย่างง่าย
    dummy_X = np.array([[1],[2],[3],[4],[5]])
    dummy_y = np.array([2,4,5,4,5])
    dummy_model.fit(dummy_X, dummy_y)
    joblib.dump(dummy_model, "model.pkl")
    model = dummy_model

# Input features
feature1 = st.slider("Feature 1", 0.0, 10.0, 5.0)
feature2 = st.slider("Feature 2", 0.0, 10.0, 5.0)

if st.button("Predict"):
    input_data = np.array([[feature1, feature2]])
    # ใช้โมเดลที่โหลดมาเพื่อทำการทำนาย
    prediction = model.predict(input_data)[0] # สมมติว่า model.predict คืนค่าเป็น array
    st.success(f"ค่าที่ทำนายได้คือ: {prediction:.2f}")
```

### เฉลย 6.3: Prompt Engineering สำหรับ AI Coding Assistants
**Prompt:**
"โปรดเขียนฟังก์ชัน Python ชื่อ `calculate_factorial` ที่คำนวณ factorial ของตัวเลขที่กำหนด ฟังก์ชันควรได้รับการปรับให้มีประสิทธิภาพ อาจใช้แนวทางแบบวนซ้ำ (iterative) ต้องมีการจัดการข้อผิดพลาดที่แข็งแกร่ง: ให้ raise `ValueError` หากอินพุตไม่ใช่จำนวนเต็มที่ไม่เป็นลบ นอกจากนี้ ให้จัดเตรียม docstring ที่ครอบคลุมซึ่งอธิบายวัตถุประสงค์ พารามิเตอร์ และข้อยกเว้นที่อาจเกิดขึ้น"

### เฉลย 6.4: การสะท้อนโค้ดที่สร้างโดย AI
**1. จุดแข็งและจุดที่อาจปรับปรุงได้:**
*   **จุดแข็ง:** โค้ดที่สร้างโดย AI จัดการกรณีพื้นฐาน (`n=0`) ได้อย่างถูกต้อง ใช้แนวทางแบบวนซ้ำซึ่งโดยทั่วไปมีประสิทธิภาพสำหรับ factorial และมีการจัดการข้อผิดพลาดที่ดีสำหรับอินพุตที่ไม่ใช่จำนวนเต็มหรือไม่เป็นบวก
*   **จุดที่อาจปรับปรุงได้:** การใช้ `else:` หลังจาก `if n == 0:` เป็นสิ่งซ้ำซ้อน บล็อก `else` จะเข้าถึงได้ก็ต่อเมื่อ `n` ไม่ใช่ 0 ดังนั้นการตรวจสอบ `if n == 0:` จะจัดการเงื่อนไข `else` โดยปริยาย

**2. คำแนะนำในการแก้ไข:**
ลบคำหลัก `else:` ก่อนบล็อก `res = 1` โค้ดจะยังคงทำงานเหมือนเดิม แต่จะกระชับและตรงไปตรงมามากขึ้นเล็กน้อย

```python
def factorial(n):
    if not isinstance(n, int) or n < 0:
        raise ValueError("Input must be a non-negative integer.")
    if n == 0:
        return 1
    
    res = 1
    for i in range(1, n + 1):
        res *= i
    return res
```

**3. การสะท้อนตนเอง:**
เวอร์ชันในอุดมคติของผมจะคล้ายกับเวอร์ชันที่ AI ปรับปรุงแล้วมาก ผลลัพธ์เริ่มต้นของ AI ค่อนข้างดีอยู่แล้ว แสดงให้เห็นถึงความเข้าใจในกรณีขอบและประสิทธิภาพ การซ้ำซ้อนเล็กน้อยในคำสั่ง `else` เป็นรูปแบบทั่วไป และแม้ว่าจะไม่ 'ผิด' อย่างเคร่งครัด การลบออกจะช่วยเพิ่มความกระชับ สิ่งนี้แสดงให้เห็นว่าผู้ช่วย AI สามารถสร้างโค้ดที่ใช้งานได้ดี แต่การตรวจสอบโดยมนุษย์ยังคงสามารถค้นหาการปรับปรุงสไตล์ที่ละเอียดอ่อนหรือการซ้ำซ้อนเล็กน้อยได้

### เฉลย 6.5: การออกแบบ AI Agent สำหรับการวิเคราะห์ข้อมูลอัตโนมัติ (เชิงแนวคิด)

**1. ขั้นตอนระดับสูงที่ AI agent จะต้องดำเนินการ:**
1.  **รับงาน:** ทำความเข้าใจคำขอ (เช่น โหลด CSV, ทำ EDA, สร้างรายงานสรุป)
2.  **การวางแผน:** สร้างแผนการดำเนินการทีละขั้นตอน รวมถึงการระบุเครื่องมือที่จำเป็นและลำดับการดำเนินการ
3.  **การดำเนินการ:** ดำเนินการตามแผน โดยใช้เครื่องมือที่เหมาะสม (เช่น Pandas สำหรับการโหลดและจัดการข้อมูล, Matplotlib/Seaborn สำหรับการสร้างภาพ, ไลบรารีการสร้างรายงานสำหรับรายงาน)
4.  **การตรวจสอบ:** ตรวจสอบผลลัพธ์ในแต่ละขั้นตอน (เช่น ตรวจสอบว่า CSV โหลดถูกต้อง, ตรวจสอบความถูกต้องของข้อมูล, ตรวจสอบคุณภาพของภาพ)
5.  **การจัดการข้อผิดพลาด:** หากเกิดข้อผิดพลาด ให้พยายามแก้ไข (เช่น หากไฟล์ไม่พบ ให้แจ้งผู้ใช้หรือลองเส้นทางอื่น หากข้อมูลมีค่าที่ขาดหายไป ให้ใช้กลยุทธ์การเติมค่าที่เหมาะสม)
6.  **การสร้างรายงาน:** รวบรวมผลลัพธ์ (ตาราง, กราฟ, สรุป) และสร้างรายงานสรุปในรูปแบบที่กำหนด (เช่น Markdown, PDF)
7.  **การนำเสนอผลลัพธ์:** ส่งมอบรายงานและข้อมูลเชิงลึกที่สำคัญให้กับผู้ใช้

**2. เครื่องมือ (เชิงแนวคิด) ที่ agent จะต้องใช้:**
*   **เครื่องมือเข้าถึงไฟล์:** สำหรับการอ่าน/เขียนไฟล์ (เช่น CSV, JSON)
*   **ไลบรารีการจัดการข้อมูล:** Pandas สำหรับการโหลด, ทำความสะอาด, แปลง และวิเคราะห์ข้อมูล
*   **ไลบรารีการสร้างภาพข้อมูล:** Matplotlib, Seaborn หรือ Plotly สำหรับการสร้างกราฟและแผนภูมิ
*   **ไลบรารีการสร้างรายงาน:** สำหรับการรวบรวมผลลัพธ์และสร้างรายงาน (เช่น FPDF2 สำหรับ PDF, Markdown สำหรับรายงานข้อความ)
*   **เครื่องมือการสื่อสาร:** สำหรับการโต้ตอบกับผู้ใช้ (เช่น การขอข้อมูลเพิ่มเติม, การแจ้งความคืบหน้า, การส่งมอบผลลัพธ์)
*   **เครื่องมือการประมวลผลภาษาธรรมชาติ (NLP):** สำหรับการทำความเข้าใจคำขอของผู้ใช้ที่ซับซ้อนมากขึ้นและสร้างรายงานที่เป็นธรรมชาติ

**3. วิธีที่ agent จะใช้ chain of thought เพื่อแยกย่อยและดำเนินการงาน รวมถึงวิธีจัดการกับปัญหาที่ไม่คาดคิดหรือความกำกวม:**
*   **การทำความเข้าใจคำขอ:** Agent จะวิเคราะห์คำขอของผู้ใช้เพื่อระบุวัตถุประสงค์หลัก (เช่น "วิเคราะห์ข้อมูลยอดขาย" หรือ "สร้างรายงานแนวโน้มลูกค้า") และข้อมูลที่เกี่ยวข้อง (เช่น "ไฟล์ CSV ชื่อ sales_data.csv")
*   **การสร้างแผนเริ่มต้น:** Agent จะสร้างแผนการดำเนินการเบื้องต้น เช่น:
    *   "โหลด `sales_data.csv` ด้วย Pandas"
    *   "ตรวจสอบข้อมูลด้วย `df.info()` และ `df.describe()`"
    *   "ระบุคอลัมน์ตัวเลขและคอลัมน์หมวดหมู่"
    *   "สร้างฮิสโตแกรมสำหรับคอลัมน์ตัวเลขและแผนภูมิแท่งสำหรับคอลัมน์หมวดหมู่"
    *   "สร้างรายงานสรุป"
*   **การดำเนินการทีละขั้นตอนพร้อมการตรวจสอบ:**
    *   **ขั้นตอนที่ 1: โหลดข้อมูล** Agent พยายามโหลด `sales_data.csv` หากไฟล์ไม่พบ Agent จะแจ้งผู้ใช้และขอเส้นทางไฟล์ที่ถูกต้อง (การจัดการข้อผิดพลาด)
    *   **ขั้นตอนที่ 2: การตรวจสอบข้อมูลเบื้องต้น** Agent จะรัน `df.info()` หากพบค่าที่ขาดหายไปจำนวนมากในคอลัมน์สำคัญ Agent อาจตัดสินใจที่จะเติมค่าเหล่านั้นหรือแจ้งผู้ใช้เพื่อขอคำแนะนำ (การจัดการข้อผิดพลาด/ความกำกวม)
    *   **ขั้นตอนที่ 3: การวิเคราะห์ข้อมูลเชิงสำรวจ (EDA)** Agent จะสร้างภาพข้อมูลเบื้องต้น หากกราฟบางกราฟดูไม่ชัดเจนหรือมีข้อมูลผิดปกติ Agent อาจปรับพารามิเตอร์การสร้างภาพหรือลองใช้กราฟประเภทอื่น (การจัดการความกำกวม/การปรับตัว)
    *   **ขั้นตอนที่ 4: การสร้างรายงาน** Agent จะรวบรวมข้อมูลเชิงลึกจาก EDA และสร้างรายงาน โดยอาจใช้ NLP เพื่อสรุปผลลัพธ์และสร้างข้อความอธิบายสำหรับกราฟแต่ละกราฟ
*   **การสะท้อนและการปรับปรุง:** หลังจากแต่ละขั้นตอน Agent จะสะท้อนว่าผลลัพธ์เป็นไปตามที่คาดหวังหรือไม่ หากไม่เป็นเช่นนั้น Agent จะปรับแผนและลองอีกครั้ง ตัวอย่างเช่น หากรายงานที่สร้างขึ้นขาดข้อมูลเชิงลึกที่สำคัญ Agent อาจกลับไปที่ขั้นตอน EDA เพื่อค้นหาข้อมูลเพิ่มเติม
*   **การโต้ตอบกับผู้ใช้:** ตลอดกระบวนการ Agent จะสื่อสารกับผู้ใช้เพื่อขอคำชี้แจงเมื่อจำเป็น แจ้งความคืบหน้า และนำเสนอผลลัพธ์สุดท้าย
