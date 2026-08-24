# โมดูล 2: โครงสร้างข้อมูลและการเขียนโปรแกรมเชิงวัตถุสำหรับ AI สมัยใหม่ (4 ชั่วโมง)

## ภาพรวม
โมดูลนี้จะช่วยให้เข้าใจโครงสร้างข้อมูลขั้นสูงของ Python และหลักการเขียนโปรแกรมเชิงวัตถุ (OOP) อย่างลึกซึ้ง โดยเน้นการประยุกต์ใช้ในโครงการ AI และวิทยาการข้อมูลสมัยใหม่ เราจะสำรวจว่าการจัดระเบียบข้อมูลที่มีประสิทธิภาพและการออกแบบโค้ดที่แข็งแกร่งมีส่วนช่วยให้โซลูชัน AI สามารถปรับขนาดและบำรุงรักษาได้ง่ายขึ้นได้อย่างไร

## วัตถุประสงค์การเรียนรู้
เมื่อจบโมดูลนี้ ผู้เข้าร่วมจะสามารถ:
*   ใช้โครงสร้างข้อมูลในตัวขั้นสูงและโมดูล `collections` เพื่อการจัดการข้อมูลที่มีประสิทธิภาพ
*   ประยุกต์ใช้หลักการ OOP (Encapsulation, Inheritance, Polymorphism, Abstraction) เพื่อออกแบบโค้ด AI ที่เป็นโมดูลาร์และนำกลับมาใช้ใหม่ได้
*   ใช้งานเมธอดพิเศษ (`__init__`, `__str__`, `__len__` เป็นต้น) สำหรับกำหนดพฤติกรรมของคลาสที่กำหนดเอง
*   ทำความเข้าใจและประยุกต์ใช้ Decorators เพื่อเพิ่มประสิทธิภาพการทำงานของฟังก์ชันโดยไม่ต้องแก้ไขโค้ดเดิม
*   ใช้งาน Context Managers เพื่อการจัดการทรัพยากรอย่างปลอดภัยใน Data Pipelines
*   ออกแบบลำดับชั้นของคลาสที่รองรับสถาปัตยกรรมโมเดล AI ที่ยืดหยุ่นและขยายได้

## 2.1 โครงสร้างข้อมูลขั้นสูงและโมดูล `collections` (1 ชั่วโมง)

### 2.1.1 ทบทวนโครงสร้างข้อมูลพื้นฐาน
*   **Lists, Tuples, Dictionaries, Sets:** ทบทวนคุณลักษณะ กรณีการใช้งาน และข้อควรพิจารณาด้านประสิทธิภาพ
*   **เมื่อใดควรใช้อะไร:** ตารางการตัดสินใจสำหรับการเลือกโครงสร้างข้อมูลที่เหมาะสมตามความต้องการของ AI/วิทยาการข้อมูล

### 2.1.2 โมดูล `collections` สำหรับการจัดการข้อมูลที่ดียิ่งขึ้น
*   **`defaultdict`:** ทำให้การดำเนินการกับ Dictionary ง่ายขึ้นสำหรับการนับและการจัดกลุ่มข้อมูล
    *   **ตัวอย่าง:** การนับความถี่ของคำในข้อมูลข้อความสำหรับการประมวลผลล่วงหน้าของ NLP
    *   **ตัวอย่าง:** การจัดกลุ่มจุดข้อมูลตามหมวดหมู่ในชุดข้อมูล
```python
from collections import defaultdict

# Example 1: Counting word frequencies
text = "the quick brown fox jumps over the lazy dog the quick brown fox jumps over the lazy dog."
words = text.split()
word_counts = defaultdict(int)
for word in words:
    word_counts[word] += 1
print(dict(word_counts))

# Example 2: Grouping data points
data_points = [('A', 10), ('B', 20), ('A', 15), ('C', 25), ('B', 12)]
grouped_data = defaultdict(list)
for category, value in data_points:
    grouped_data[category].append(value)
print(dict(grouped_data))
```

*   **`Counter`:** คอนเทนเนอร์ประสิทธิภาพสูงสำหรับการนับวัตถุที่สามารถแฮชได้
    *   **ตัวอย่าง:** การวิเคราะห์ความถี่ของคุณลักษณะในชุดข้อมูล
    *   **ตัวอย่าง:** การค้นหาองค์ประกอบที่พบบ่อยที่สุดในรายการป้ายกำกับ
```python
from collections import Counter

# Example 1: Counting elements in a list
labels = ['cat', 'dog', 'cat', 'bird', 'dog', 'cat']
label_counts = Counter(labels)
print(label_counts)
print(label_counts.most_common(1))

# Example 2: Counting characters in a string
sentence = "hello world"
char_counts = Counter(sentence)
print(char_counts)
```

*   **`OrderedDict`:** คลาสย่อยของ Dictionary ที่จดจำลำดับการเพิ่มรายการ
    *   **กรณีการใช้งาน:** การรักษาลำดับในการตั้งค่าคอนฟิกูเรชันหรือรายการคุณลักษณะที่ลำดับมีความสำคัญ

*   **`deque` (Double-ended Queue):** คอนเทนเนอร์ที่คล้าย List ซึ่งมีการเพิ่มและลบข้อมูลที่ปลายทั้งสองด้านได้อย่างรวดเร็ว
    *   **กรณีการใช้งาน:** การใช้งานอัลกอริทึม Sliding Window สำหรับการประมวลผลข้อมูลแบบเรียลไทม์หรือการวิเคราะห์สตรีม
```python
from collections import deque

# Example: Sliding window average
data_stream = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
window_size = 3
window = deque(maxlen=window_size)
averages = []

for item in data_stream:
    window.append(item)
    if len(window) == window_size:
        averages.append(sum(window) / window_size)

print(f"Data Stream: {data_stream}")
print(f"Sliding Window Averages (size {window_size}): {averages}")
```

*   **`namedtuple`:** ฟังก์ชันโรงงานสำหรับสร้างคลาสย่อยของ Tuple ที่มีฟิลด์ที่มีชื่อ
    *   **กรณีการใช้งาน:** การแสดงบันทึกข้อมูลที่มีโครงสร้าง (เช่น จุดข้อมูล, การอ่านค่าเซ็นเซอร์) ในลักษณะที่อ่านง่ายกว่า Tuple ทั่วไป โดยไม่มีค่าใช้จ่ายเพิ่มเติมของคลาสเต็มรูปแบบ
```python
from collections import namedtuple

# Define a namedtuple for a data point
DataPoint = namedtuple('DataPoint', ['id', 'feature1', 'feature2', 'label'])

# Create instances of DataPoint
dp1 = DataPoint(id=1, feature1=0.5, feature2=1.2, label='A')
dp2 = DataPoint(id=2, feature1=0.8, feature2=0.9, label='B')

print(dp1)
print(f"ID: {dp1.id}, Feature 1: {dp1.feature1}")
```

### 2.1.3 การดำเนินการกับ Set ขั้นสูง
*   **Frozenset:** Set เวอร์ชันที่ไม่สามารถเปลี่ยนแปลงได้
*   **Set Comprehensions:** วิธีที่กระชับในการสร้าง Set
*   **การประยุกต์ใช้:** การค้นหาองค์ประกอบที่ไม่ซ้ำกันอย่างมีประสิทธิภาพ, การตรวจสอบการเป็นสมาชิก, และการดำเนินการทางคณิตศาสตร์ของ Set (Union, Intersection, Difference) ใน Feature Engineering หรือ Data Validation

## 2.2 การเขียนโปรแกรมเชิงวัตถุ (OOP) สำหรับ AI (1.5 ชั่วโมง)

### 2.2.1 สี่เสาหลักของ OOP ทบทวน
*   **Encapsulation:** การรวมข้อมูลและเมธอดที่ดำเนินการกับข้อมูลเข้าไว้ในหน่วยเดียว (คลาส)
    *   **การซ่อนข้อมูล (Data Hiding):** การใช้ข้อตกลง (`_private`, `__mangled`) และคุณสมบัติ (`@property`) เพื่อควบคุมการเข้าถึงแอตทริบิวต์
    *   **ตัวอย่าง:** การออกแบบคลาส `FeatureProcessor` ที่การแปลงข้อมูลภายในถูกห่อหุ้มไว้
```python
class FeatureProcessor:
    def __init__(self, data):
        self._raw_data = data  # Convention for protected attribute
        self._processed_data = None

    @property
    def raw_data(self):
        return self._raw_data

    @property
    def processed_data(self):
        if self._processed_data is None:
            self._processed_data = self._process_data()
        return self._processed_data

    def _process_data(self):
        # Simulate some data processing
        return [x * 2 for x in self._raw_data]

# Usage
processor = FeatureProcessor([1, 2, 3])
print(f"Raw Data: {processor.raw_data}")
print(f"Processed Data: {processor.processed_data}")
# processor._raw_data = [4, 5, 6] # This would be discouraged
```

*   **Inheritance:** การสร้างคลาสใหม่ (Derived Classes) จากคลาสที่มีอยู่ (Base Classes) โดยสืบทอดแอตทริบิวต์และเมธอดของคลาสเหล่านั้น
    *   **กรณีการใช้งาน:** การสร้างลำดับชั้นของโมเดล AI (เช่น `BaseModel` -> `ClassificationModel` -> `ImageClassifier`) เพื่อนำฟังก์ชันการทำงานทั่วไปกลับมาใช้ใหม่
    *   **Method Overriding:** การปรับแต่งเมธอดที่สืบทอดมา
```python
class BaseModel:
    def __init__(self, name):
        self.name = name

    def train(self, data):
        raise NotImplementedError("Subclasses must implement this method")

    def predict(self, features):
        raise NotImplementedError("Subclasses must implement this method")

class ImageClassifier(BaseModel):
    def __init__(self, name, num_classes):
        super().__init__(name)
        self.num_classes = num_classes

    def train(self, data):
        print(f"Training {self.name} Image Classifier on {len(data)} samples for {self.num_classes} classes.")
        # Actual training logic here

    def predict(self, features):
        print(f"Predicting with {self.name} Image Classifier.")
        # Actual prediction logic here
        return [0, 1, 0] # Dummy prediction

class TextClassifier(BaseModel):
    def __init__(self, name, vocab_size):
        super().__init__(name)
        self.vocab_size = vocab_size

    def train(self, data):
        print(f"Training {self.name} Text Classifier on {len(data)} samples with vocab size {self.vocab_size}.")
        # Actual training logic here

    def predict(self, features):
        print(f"Predicting with {self.name} Text Classifier.")
        # Actual prediction logic here
        return [1] # Dummy prediction

# Usage
image_model = ImageClassifier("ResNet50", 1000)
text_model = TextClassifier("BERT", 30000)

image_model.train(["image_data_1", "image_data_2"])
print(image_model.predict(["image_features_1"]))

text_model.train(["text_data_1"])
print(text_model.predict(["text_features_1"]))
```

*   **Polymorphism:** ความสามารถของวัตถุที่แตกต่างกันในการตอบสนองต่อการเรียกเมธอดเดียวกันในแบบของตนเอง
    *   **กรณีการใช้งาน:** การประมวลผลรายการโมเดล AI ที่หลากหลาย โดยแต่ละโมเดลมีเมธอด `train()` หรือ `predict()` ของตนเอง
```python
def run_model_pipeline(models, data):
    for model in models:
        model.train(data)
        # model.predict(data) # Could also predict here

models = [ImageClassifier("VGG16", 100), TextClassifier("GPT-2", 50000)]
run_model_pipeline(models, ["some_data"])
```

*   **Abstraction:** การซ่อนรายละเอียดการใช้งานที่ซับซ้อนและแสดงเฉพาะคุณสมบัติที่จำเป็นของวัตถุ
    *   **Abstract Base Classes (ABCs):** การใช้โมดูล `abc` เพื่อกำหนดอินเทอร์เฟซสำหรับส่วนประกอบ AI
    *   **กรณีการใช้งาน:** การทำให้แน่ใจว่าโมเดล AI ที่กำหนดเองทั้งหมดเป็นไปตามอินเทอร์เฟซทั่วไป (เช่น มีเมธอด `fit` และ `predict`)
```python
from abc import ABC, abstractmethod

class AbstractAIModel(ABC):
    @abstractmethod
    def fit(self, X, y):
        pass

    @abstractmethod
    def predict(self, X):
        pass

class CustomClassifier(AbstractAIModel):
    def fit(self, X, y):
        print("Custom Classifier: Fitting data...")
        # Implementation for fitting

    def predict(self, X):
        print("Custom Classifier: Predicting...")
        # Implementation for prediction
        return [0, 1, 0]

# model = AbstractAIModel() # This would raise an error
classifier = CustomClassifier()
classifier.fit([1,2,3], [0,1,0])
print(classifier.predict([4,5,6]))
```

### 2.2.2 เมธอดพิเศษ (Magic/Dunder Methods)
*   **`__init__`:** Constructor สำหรับการเริ่มต้นวัตถุ
*   **`__str__` และ `__repr__`:** การแสดงผลสตริงสำหรับผู้ใช้และนักพัฒนา
*   **`__len__`, `__getitem__`, `__setitem__`:** การใช้งานพฤติกรรมคล้ายคอนเทนเนอร์สำหรับชุดข้อมูลที่กำหนดเองหรือชุดคุณลักษณะ
*   **`__call__`:** การทำให้ Instance สามารถเรียกใช้งานได้ มีประโยชน์สำหรับการสร้างเลเยอร์ที่กำหนดเองหรือฟังก์ชันการแปลงใน Deep Learning
```python
class Dataset:
    def __init__(self, data):
        self._data = data

    def __len__(self):
        return len(self._data)

    def __getitem__(self, idx):
        return self._data[idx]

    def __str__(self):
        return f"Dataset with {len(self)} items"

    def __repr__(self):
        return f"<Dataset object with {len(self)} items>"

class Scaler:
    def __init__(self, scale_factor):
        self.scale_factor = scale_factor

    def __call__(self, x):
        return x * self.scale_factor

# Usage
my_dataset = Dataset([10, 20, 30, 40])
print(my_dataset) # Uses __str__
print(repr(my_dataset)) # Uses __repr__

scaler = Scaler(2)
scaled_value = scaler(5) # Calls __call__
print(f"Scaled value: {scaled_value}")
```

### 2.2.3 Dataclasses และ Pydantic สำหรับ Model Configuration
*   **Dataclasses (Python 3.7+):** ลด Boilerplate Code ในคลาสที่ใช้เก็บข้อมูล
    *   **ประโยชน์:** การสร้างคลาสสำหรับกำหนดค่าโมเดล (Model Configuration) หรือพารามิเตอร์ได้อย่างรวดเร็วและอ่านง่าย
    *   **ตัวอย่าง:** การกำหนดค่าสำหรับโมเดลการเรียนรู้เชิงลึก
```python
from dataclasses import dataclass

@dataclass
class ModelConfig:
    model_name: str
    learning_rate: float = 0.001
    num_epochs: int = 10
    batch_size: int = 32
    optimizer: str = "Adam"

# Usage
config = ModelConfig(model_name="ResNet50", num_epochs=20)
print(config)

# Accessing attributes
print(f"Model Name: {config.model_name}")
print(f"Learning Rate: {config.learning_rate}")
```

*   **Pydantic (สำหรับ Data Validation และ Settings Management):** การบังคับใช้ Type Hinting และการตรวจสอบข้อมูลรันไทม์
    *   **ประโยชน์:** การจัดการการกำหนดค่าที่ซับซ้อน, การตรวจสอบอินพุต API, และการโหลดการตั้งค่าจากตัวแปรสภาพแวดล้อมหรือไฟล์
    *   **ตัวอย่าง:** การกำหนดค่าสำหรับบริการ AI ที่ต้องมีการตรวจสอบความถูกต้องของข้อมูล
```python
from pydantic import BaseModel, Field
from typing import Optional

class AIServiceConfig(BaseModel):
    api_key: str = Field(..., env="AI_API_KEY")
    model_version: str = "v1.0"
    debug_mode: bool = False
    max_requests_per_minute: Optional[int] = 100

# Usage (assuming AI_API_KEY is set in environment variables)
# from os import environ
# environ["AI_API_KEY"] = "your_secret_key"

try:
    service_config = AIServiceConfig(model_version="v2.0")
    print(service_config)
except Exception as e:
    print(f"Error loading config: {e}")

# Accessing attributes
# print(f"API Key: {service_config.api_key}")
```

## 2.3 Advanced Pythonic Practices for AI (1 ชั่วโมง)

### 2.3.1 Decorators สำหรับการปรับปรุงฟังก์ชัน
*   **แนวคิด:** ฟังก์ชันที่รับฟังก์ชันอื่นเป็นอาร์กิวเมนต์และส่งคืนฟังก์ชันใหม่ที่ปรับปรุงแล้ว
*   **กรณีการใช้งานใน AI:**
    *   **Logging:** การบันทึกการทำงานของฟังก์ชันโมเดลหรือ Data Preprocessing
    *   **Timing:** การวัดประสิทธิภาพของฟังก์ชัน (เช่น เวลาในการฝึกโมเดล)
    *   **Caching:** การแคชผลลัพธ์ของฟังก์ชันที่มีค่าใช้จ่ายสูง (เช่น การโหลดชุดข้อมูล)
    *   **Permission/Authentication:** การควบคุมการเข้าถึงฟังก์ชันในระบบ AI
```python
import time

def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Function {func.__name__} took {end_time - start_time:.4f} seconds")
        return result
    return wrapper

@timer
def train_model(epochs):
    print(f"Training model for {epochs} epochs...")
    time.sleep(2) # Simulate training time
    print("Training complete.")

@timer
def preprocess_data(data_size):
    print(f"Preprocessing {data_size} MB of data...")
    time.sleep(1.5) # Simulate preprocessing time
    return f"Processed data of size {data_size} MB"

train_model(10)
processed_result = preprocess_data(100)
print(processed_result)
```

### 2.3.2 Context Managers (`with` Statement)
*   **แนวคิด:** การจัดการทรัพยากรอย่างปลอดภัย (เช่น ไฟล์, การเชื่อมต่อฐานข้อมูล, ล็อก) โดยรับประกันว่าทรัพยากรจะถูกจัดสรรและปล่อยอย่างถูกต้อง
*   **กรณีการใช้งานใน AI:**
    *   **การจัดการไฟล์:** การอ่าน/เขียนชุดข้อมูล, โมเดลที่บันทึกไว้
    *   **การจัดการล็อก:** การควบคุมการเข้าถึงทรัพยากรที่ใช้ร่วมกัน (เช่น GPU Memory)
    *   **การจัดการเซสชัน:** การจัดการเซสชันการฝึกอบรมโมเดลหรือการเชื่อมต่อ API
```python
import threading

# Custom Context Manager for managing a lock (e.g., for GPU memory access)
class GPUMemoryLock:
    def __init__(self, device_id):
        self.device_id = device_id
        self.lock = threading.Lock()
        print(f"GPU Memory Lock for device {self.device_id} initialized.")

    def __enter__(self):
        print(f"Acquiring lock for GPU device {self.device_id}...")
        self.lock.acquire()
        print(f"Lock acquired for GPU device {self.device_id}.")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.lock.release()
        print(f"Lock released for GPU device {self.device_id}.")
        if exc_type:
            print(f"An exception occurred: {exc_val}")
        return False # Propagate exception if any

# Usage
def perform_gpu_task(device):
    with GPUMemoryLock(device) as gpu:
        print(f"Performing intensive task on GPU device {gpu.device_id}...")
        time.sleep(1) # Simulate GPU computation
    print(f"Task on GPU device {device} completed.")

perform_gpu_task(0)
perform_gpu_task(1)

# Example with file handling (built-in context manager)
with open("data.txt", "w") as f:
    f.write("This is some data for AI processing.")
print("File 'data.txt' written and closed safely.")
```

### 2.3.3 Generators และ Iterators สำหรับข้อมูลขนาดใหญ่
*   **แนวคิด:** การประมวลผลข้อมูลแบบ Lazy Evaluation เพื่อลดการใช้หน่วยความจำ โดยเฉพาะอย่างยิ่งสำหรับชุดข้อมูลขนาดใหญ่ที่อาจไม่พอดีกับหน่วยความจำทั้งหมด
*   **กรณีการใช้งานใน AI:**
    *   **การโหลดชุดข้อมูล:** การโหลดตัวอย่างข้อมูลทีละน้อยสำหรับการฝึกโมเดล Deep Learning (Data Batching)
    *   **การประมวลผลสตรีม:** การประมวลผลข้อมูลที่เข้ามาอย่างต่อเนื่องโดยไม่ต้องเก็บทั้งหมดไว้ในหน่วยความจำ
```python
def data_loader(filepath, batch_size):
    with open(filepath, 'r') as f:
        batch = []
        for line in f:
            batch.append(line.strip())
            if len(batch) == batch_size:
                yield batch
                batch = []
        if batch: # Yield any remaining data
            yield batch

# Create a dummy data file
with open("large_data.txt", "w") as f:
    for i in range(1, 101):
        f.write(f"data_point_{i}\n")

# Usage
for i, batch in enumerate(data_loader("large_data.txt", batch_size=10)):
    print(f"Processing batch {i+1}: {batch}")
    # Simulate model training with the batch
    time.sleep(0.1)
```

## 2.4 การออกแบบสถาปัตยกรรม AI ที่ปรับขนาดได้ (0.5 ชั่วโมง)

### 2.4.1 หลักการออกแบบสำหรับ AI ที่ปรับขนาดได้
*   **Modular Design:** การแบ่งระบบ AI ออกเป็นส่วนประกอบอิสระที่สามารถพัฒนา ทดสอบ และปรับใช้แยกกันได้
*   **Loose Coupling:** การลดการพึ่งพาระหว่างส่วนประกอบ เพื่อให้สามารถเปลี่ยนแปลงส่วนหนึ่งได้โดยไม่กระทบส่วนอื่นมากนัก
*   **High Cohesion:** การทำให้ส่วนประกอบแต่ละส่วนมีความรับผิดชอบที่ชัดเจนและมุ่งเน้นไปที่งานเดียว

### 2.4.2 Design Patterns ที่เกี่ยวข้องกับ AI
*   **Strategy Pattern:** การกำหนดตระกูลของอัลกอริทึม, ห่อหุ้มแต่ละอัลกอริทึม, และทำให้พวกมันสามารถสับเปลี่ยนกันได้
    *   **กรณีการใช้งาน:** การสลับระหว่างอัลกอริทึมการปรับขนาดข้อมูล (Scaling Algorithms) หรือฟังก์ชันการเปิดใช้งาน (Activation Functions) ในโมเดล AI
*   **Factory Pattern:** การจัดหาวิธีการสร้างวัตถุในคลาสแม่ แต่ปล่อยให้คลาสย่อยตัดสินใจว่าจะสร้างวัตถุประเภทใด
    *   **กรณีการใช้งาน:** การสร้างอินสแตนซ์ของโมเดล AI ที่แตกต่างกันตามการกำหนดค่าโดยไม่ต้องระบุคลาสที่แน่นอน
*   **Observer Pattern:** การกำหนดการพึ่งพาระหว่างวัตถุแบบหนึ่งต่อหลาย โดยที่เมื่อวัตถุหนึ่งเปลี่ยนสถานะ วัตถุอื่น ๆ ที่ขึ้นอยู่กับมันจะได้รับการแจ้งเตือนและอัปเดตโดยอัตโนมัติ
    *   **กรณีการใช้งาน:** การตรวจสอบสถานะการฝึกอบรมโมเดล, การแจ้งเตือนเมื่อเมตริกประสิทธิภาพถึงเกณฑ์ที่กำหนด

## สรุปโมดูล 2
โมดูลนี้ได้สำรวจโครงสร้างข้อมูลขั้นสูงของ Python, หลักการ OOP, และแนวปฏิบัติ Pythonic ที่สำคัญสำหรับการสร้างระบบ AI ที่แข็งแกร่งและปรับขนาดได้ การทำความเข้าใจและประยุกต์ใช้แนวคิดเหล่านี้จะช่วยให้นักพัฒนา AI สามารถเขียนโค้ดที่มีประสิทธิภาพ, บำรุงรักษาได้ง่าย, และพร้อมสำหรับการใช้งานจริงในโครงการ AI ที่ซับซ้อน

# โมดูล 1: พื้นฐาน Python สำหรับ AI (4 ชั่วโมง)

## ภาพรวม
โมดูลนี้จะปูพื้นฐานที่แข็งแกร่งในภาษา Python ซึ่งเป็นสิ่งจำเป็นสำหรับผู้เริ่มต้นในสาขา AI และวิทยาการข้อมูล เราจะครอบคลุมแนวคิดหลักของ Python ตั้งแต่โครงสร้างข้อมูลพื้นฐานไปจนถึงการควบคุมการไหลของโปรแกรม และแนะนำไลบรารีที่สำคัญสำหรับการคำนวณเชิงตัวเลขและการจัดการข้อมูล

## วัตถุประสงค์การเรียนรู้
เมื่อจบโมดูลนี้ ผู้เข้าร่วมจะสามารถ:
*   เขียนโปรแกรม Python พื้นฐานได้อย่างคล่องแคล่ว
*   ใช้โครงสร้างข้อมูลพื้นฐานของ Python (Lists, Tuples, Dictionaries, Sets) ได้อย่างมีประสิทธิภาพ
*   ควบคุมการไหลของโปรแกรมโดยใช้เงื่อนไขและลูป
*   สร้างและใช้งานฟังก์ชันเพื่อจัดระเบียบโค้ด
*   ทำความเข้าใจและใช้งานไลบรารี NumPy สำหรับการคำนวณเชิงตัวเลข
*   ทำความเข้าใจและใช้งานไลบรารี Pandas สำหรับการจัดการและวิเคราะห์ข้อมูล

## 1.1 พื้นฐาน Python (1 ชั่วโมง)

### 1.1.1 การติดตั้งและสภาพแวดล้อม
*   **Anaconda/Miniconda:** การติดตั้งและการจัดการสภาพแวดล้อม Python
*   **Jupyter Notebook/Lab:** การใช้งานสภาพแวดล้อมการพัฒนาแบบโต้ตอบ
*   **VS Code:** การตั้งค่าสำหรับ Python Development

### 1.1.2 ตัวแปรและประเภทข้อมูล
*   **ตัวเลข (Integers, Floats):** การดำเนินการทางคณิตศาสตร์
*   **สตริง (Strings):** การจัดการสตริง, F-strings
*   **บูลีน (Booleans):** True/False, การดำเนินการเชิงตรรกะ
*   **NoneType:** การแสดงค่าว่าง

### 1.1.3 การดำเนินการพื้นฐาน
*   **การดำเนินการทางคณิตศาสตร์:** +, -, *, /, //, %, **
*   **การดำเนินการเปรียบเทียบ:** ==, !=, <, >, <=, >=
*   **การดำเนินการเชิงตรรกะ:** and, or, not

## 1.2 โครงสร้างข้อมูลพื้นฐาน (1 ชั่วโมง)

### 1.2.1 Lists
*   **การสร้างและเข้าถึง:** `my_list = [1, 2, 3]`, `my_list[0]`
*   **การดำเนินการ:** `append()`, `extend()`, `insert()`, `remove()`, `pop()`, `sort()`
*   **List Comprehensions:** การสร้าง List อย่างกระชับ
```python
# Example: List Comprehensions
squares = [x**2 for x in range(10) if x % 2 == 0]
print(squares)
```

### 1.2.2 Tuples
*   **การสร้างและเข้าถึง:** `my_tuple = (1, 2, 3)`, `my_tuple[0]`
*   **คุณสมบัติ:** ไม่สามารถเปลี่ยนแปลงได้ (Immutable)
*   **การใช้งาน:** การส่งคืนค่าหลายค่าจากฟังก์ชัน, คีย์ Dictionary

### 1.2.3 Dictionaries
*   **การสร้างและเข้าถึง:** `my_dict = {'key': 'value'}`, `my_dict['key']`
*   **การดำเนินการ:** `keys()`, `values()`, `items()`, `update()`
*   **Dictionary Comprehensions:** การสร้าง Dictionary อย่างกระชับ
```python
# Example: Dictionary Comprehensions
sq_dict = {x: x**2 for x in range(5)}
print(sq_dict)
```

### 1.2.4 Sets
*   **การสร้างและเข้าถึง:** `my_set = {1, 2, 3}`
*   **คุณสมบัติ:** ไม่มีการเรียงลำดับ, ไม่ซ้ำกัน
*   **การดำเนินการ:** `add()`, `remove()`, `union()`, `intersection()`, `difference()`
*   **การใช้งาน:** การค้นหาองค์ประกอบที่ไม่ซ้ำกัน, การตรวจสอบการเป็นสมาชิกอย่างรวดเร็ว

## 1.3 การควบคุมการไหลของโปรแกรมและฟังก์ชัน (1 ชั่วโมง)

### 1.3.1 เงื่อนไข (`if`, `elif`, `else`)
*   **การใช้งาน:** การตัดสินใจตามเงื่อนไข

### 1.3.2 ลูป (`for`, `while`)
*   **`for` loop:** การวนซ้ำผ่าน Iterable (List, Tuple, String, Range)
*   **`while` loop:** การวนซ้ำตราบเท่าที่เงื่อนไขเป็นจริง
*   **`break`, `continue`, `pass`:** การควบคุมลูป

### 1.3.3 ฟังก์ชัน
*   **การกำหนดฟังก์ชัน:** `def my_function(arg1, arg2):`
*   **อาร์กิวเมนต์:** Positional, Keyword, Default, Arbitrary (`*args`, `**kwargs`)
*   **Docstrings:** การเขียนเอกสารประกอบฟังก์ชัน
*   **Lambda Functions:** ฟังก์ชันนิรนามขนาดเล็ก

## 1.4 การแนะนำไลบรารีที่สำคัญสำหรับ AI (1 ชั่วโมง)

### 1.4.1 NumPy (Numerical Python)
*   **`ndarray`:** อาร์เรย์ N มิติสำหรับการคำนวณเชิงตัวเลขที่มีประสิทธิภาพ
*   **การดำเนินการพื้นฐาน:** การสร้างอาร์เรย์, การเข้าถึง, การดำเนินการทางคณิตศาสตร์แบบ Element-wise
*   **การใช้งานใน AI:** การจัดการข้อมูลตัวเลข, เวกเตอร์, เมทริกซ์
```python
import numpy as np

# Example: NumPy array operations
arr = np.array([[1, 2], [3, 4]])
print(arr * 2)
print(arr.T) # Transpose
```

### 1.4.2 Pandas (Panel Data)
*   **`Series` และ `DataFrame`:** โครงสร้างข้อมูลหลักสำหรับการจัดการข้อมูลแบบตาราง
*   **การโหลดข้อมูล:** `read_csv()`, `read_excel()`
*   **การสำรวจข้อมูล:** `head()`, `info()`, `describe()`, `shape`
*   **การเลือกข้อมูล:** `loc`, `iloc`
*   **การจัดการข้อมูล:** การจัดการค่าที่หายไป, การกรอง, การจัดกลุ่ม
*   **การใช้งานใน AI:** การเตรียมข้อมูล, การวิเคราะห์ข้อมูลเชิงสำรวจ (EDA)
```python
import pandas as pd

# Example: Pandas DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'Los Angeles', 'Chicago']
}
df = pd.DataFrame(data)
print(df)
print(df[df['Age'] > 28])
```

## สรุปโมดูล 1
โมดูลนี้ได้วางรากฐานที่แข็งแกร่งใน Python ซึ่งเป็นภาษาโปรแกรมที่สำคัญสำหรับ AI ผู้เข้าร่วมได้เรียนรู้พื้นฐานของ Python, โครงสร้างข้อมูล, การควบคุมการไหลของโปรแกรม, ฟังก์ชัน, และการแนะนำไลบรารี NumPy และ Pandas ซึ่งเป็นเครื่องมือที่จำเป็นสำหรับการเริ่มต้นเส้นทางใน AI และวิทยาการข้อมูล

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

        # Text features
        words = text_lower.split()
        # For simplicity, let\'s just take the first 5 unique words as top_words
        top_words = list(set(words))[:5]

        return FeatureSet(
            numerical_features={\'text_length\': text_length},
            categorical_features={\'has_keywords\': has_keywords},
            text_features={\'top_words\': top_words}
        )

# --- Demonstration ---

# Usage
extractor = TextFeatureExtractor(keywords_to_check=["AI", "Python", "Machine Learning"])

text1 = "Python is great for AI and Machine Learning projects."
features1 = extractor.extract(text1)

print("Features for Text 1:")
print(f"  Numerical: {features1.numerical_features}")
print(f"  Categorical: {features1.categorical_features}")
print(f"  Text: {features1.text_features}")

text2 = "This is a simple text without any AI keywords."
features2 = extractor.extract(text2)

print("\nFeatures for Text 2:")
print(f"  Numerical: {features2.numerical_features}")
print(f"  Categorical: {features2.categorical_features}")
print(f"  Text: {features2.text_features}")

text3 = "AI is transforming the world, and Python is at its core. Machine Learning is key."
features3 = extractor.extract(text3)

print("\nFeatures for Text 3:")
print(f"  Numerical: {features3.numerical_features}")
print(f"  Categorical: {features3.categorical_features}")
print(f"  Text: {features3.text_features}")
```

## สรุปโมดูล 2
โมดูลนี้ได้สำรวจโครงสร้างข้อมูลขั้นสูงของ Python, หลักการ OOP, และแนวปฏิบัติ Pythonic ที่สำคัญสำหรับการสร้างระบบ AI ที่แข็งแกร่งและปรับขนาดได้ การทำความเข้าใจและประยุกต์ใช้แนวคิดเหล่านี้จะช่วยให้นักพัฒนา AI สามารถเขียนโค้ดที่มีประสิทธิภาพ, บำรุงรักษาได้ง่าย, และพร้อมสำหรับการใช้งานจริงในโครงการ AI ที่ซับซ้อน

# โมดูล 3: Python สำหรับการวิเคราะห์ข้อมูลสำหรับ AI สมัยใหม่ (4 ชั่วโมง)

## ภาพรวม
โมดูลนี้มุ่งเน้นไปที่เทคนิคการจัดการข้อมูล การวิเคราะห์ และการแสดงภาพข้อมูลขั้นสูง โดยใช้ไลบรารี Python เช่น NumPy, Pandas และ Matplotlib/Seaborn เราจะเน้นการจัดการข้อมูลอย่างมีประสิทธิภาพสำหรับชุดข้อมูลขนาดใหญ่ การเตรียมข้อมูลสำหรับโมเดล Machine Learning และการดึงข้อมูลเชิงลึกที่นำไปใช้ได้จริง โดยให้ความสำคัญกับคุณภาพของข้อมูลและการประมวลผลล่วงหน้าสำหรับแอปพลิเคชัน AI

## วัตถุประสงค์การเรียนรู้
เมื่อจบโมดูลนี้ ผู้เข้าร่วมจะสามารถ:
*   ดำเนินการคำนวณเชิงตัวเลขประสิทธิภาพสูงด้วย NumPy รวมถึงการจัดการอาร์เรย์ขั้นสูงและการ Broadcasting
*   เชี่ยวชาญ Pandas สำหรับการโหลด การทำความสะอาด การแปลง และการรวมข้อมูลของชุดข้อมูลที่ซับซ้อน
*   ประยุกต์ใช้เทคนิคการทำความสะอาดข้อมูลและการประมวลผลล่วงหน้าขั้นสูงที่สำคัญสำหรับการฝึกโมเดล AI ที่แข็งแกร่ง
*   สร้างภาพข้อมูลเชิงลึกและมีคุณภาพระดับตีพิมพ์โดยใช้ Matplotlib และ Seaborn
*   เข้าใจความสำคัญของคุณภาพข้อมูลและการวิเคราะห์ข้อมูลเชิงสำรวจ (EDA) ในวงจรชีวิตการพัฒนา AI

## 3.1 NumPy: การคำนวณเชิงตัวเลขประสิทธิภาพสูง (1 ชั่วโมง)

### 3.1.1 การสร้างและจัดการอาร์เรย์ขั้นสูง
*   **`np.arange`, `np.linspace`, `np.logspace`:** การสร้างลำดับด้วยความแม่นยำ
*   **`np.zeros`, `np.ones`, `np.full`, `np.empty`:** การสร้างอาร์เรย์ของค่าเฉพาะอย่างมีประสิทธิภาพ
*   **`np.eye`, `np.identity`:** การสร้างเมทริกซ์เอกลักษณ์
*   **การปรับรูปร่างและการสลับแกน:** `reshape()`, `flatten()`, `ravel()`, แอตทริบิวต์ `T`
*   **การรวมและการแยก:** `np.concatenate()`, `np.vstack()`, `np.hstack()`, `np.split()`

### 3.1.2 Vectorization และ Broadcasting
*   **Vectorized Operations:** การดำเนินการกับอาร์เรย์ทั้งหมดโดยไม่มีลูปที่ชัดเจนเพื่อความเร็วและความกระชับ
    *   **ตัวอย่าง:** การดำเนินการแบบ Element-wise, ฟังก์ชันทางคณิตศาสตร์ (`np.sin`, `np.exp`)
*   **Broadcasting Rules:** การทำความเข้าใจว่า NumPy จัดการการดำเนินการกับอาร์เรย์ที่มีรูปร่างต่างกันอย่างไร
    *   **ตัวอย่าง:** การเพิ่ม Scalar เข้ากับอาร์เรย์, การเพิ่มอาร์เรย์ 1 มิติเข้ากับอาร์เรย์ 2 มิติ
```python
import numpy as np

# Vectorized operations
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
print(f"Element-wise addition: {arr1 + arr2}")
print(f"Element-wise multiplication: {arr1 * arr2}")
print(f"Sine of arr1: {np.sin(arr1)}")

# Broadcasting
A = np.array([[1, 2, 3], [4, 5, 6]]) # Shape (2, 3)
b = np.array([10, 20, 30])          # Shape (3,)
print(f"\nBroadcasting A + b:\n{A + b}")

c = np.array([[10], [20]])          # Shape (2, 1)
print(f"\nBroadcasting A + c:\n{A + c}")
```

### 3.1.3 Advanced Indexing และ Slicing
*   **Boolean Indexing:** การเลือก Element ตามเงื่อนไข Boolean
    *   **กรณีการใช้งาน:** การกรองข้อมูลตามเกณฑ์ (เช่น การเลือกจุดข้อมูลทั้งหมดที่ Feature สูงกว่าเกณฑ์)
*   **Fancy Indexing:** การเลือก Element ที่ไม่ต่อเนื่องโดยใช้อาร์เรย์จำนวนเต็ม
    *   **กรณีการใช้งาน:** การสุ่มตัวอย่างแถวหรือคอลัมน์, การจัดเรียงข้อมูลใหม่

### 3.1.4 ข้อควรพิจารณาด้านประสิทธิภาพ
*   **Memory Layout:** อาร์เรย์แบบ C-contiguous เทียบกับ Fortran-contiguous
*   **เมื่อใดควรใช้ NumPy:** ข้อดีเหนือ Python Lists สำหรับงานเชิงตัวเลข

## 3.2 Pandas: การจัดการและวิเคราะห์ข้อมูล (1.5 ชั่วโมง)

### 3.2.1 DataFrame และ Series เจาะลึก
*   **การสร้าง DataFrames:** จาก Dictionaries, Lists of Dictionaries, CSV, Excel, ฐานข้อมูล SQL
*   **MultiIndex (Hierarchical Indexing):** การจัดการข้อมูลตารางที่ซับซ้อนด้วยระดับการ Index หลายระดับ
    *   **กรณีการใช้งาน:** ข้อมูลอนุกรมเวลาที่มีเซ็นเซอร์หลายตัว, ข้อมูลการทดลองที่มีการวัดซ้ำ
*   **การเลือกขั้นสูง:** `loc`, `iloc`, `at`, `iat` สำหรับการเข้าถึงข้อมูลที่แม่นยำ

### 3.2.2 การทำความสะอาดและการประมวลผลข้อมูลขั้นสูง
*   **การจัดการข้อมูลที่ขาดหายไป:** `isnull()`, `notnull()`, `dropna()`, `fillna()` ด้วยกลยุทธ์ขั้นสูง (เช่น forward-fill, backward-fill, interpolation, mean/median/mode imputation)
    *   **กรณีการใช้งาน:** การเตรียมชุดข้อมูลจริงสำหรับโมเดล ML ซึ่งค่าที่ขาดหายไปเป็นเรื่องปกติ
*   **ข้อมูลซ้ำซ้อน:** `duplicated()`, `drop_duplicates()`
*   **การแปลงประเภทข้อมูล:** `astype()`, `to_numeric()`, `to_datetime()`, `to_timedelta()`
*   **การดำเนินการกับสตริง:** เมธอดสตริงแบบ Vectorized (Accessor `.str`) สำหรับการทำความสะอาดข้อมูลข้อความ
*   **ข้อมูลเชิงหมวดหมู่:** `Categorical` dtype เพื่อประสิทธิภาพหน่วยความจำและการดำเนินการเฉพาะ

### 3.2.3 การแปลงและการรวมข้อมูล
*   **`apply()`, `map()`, `applymap()`:** การใช้ฟังก์ชันที่กำหนดเองกับ Series, DataFrames หรือแบบ Element-wise
    *   **กรณีการใช้งาน:** การทำ Feature Engineering ที่กำหนดเอง, การแปลงข้อมูลที่ซับซ้อน
*   **`groupby()`: การรวมขั้นสูง:** การจัดกลุ่มข้อมูลตามหนึ่งคอลัมน์หรือมากกว่า และการใช้ฟังก์ชันรวม (`agg()`, `transform()`, `filter()`)
    *   **ตัวอย่าง:** การคำนวณสถิติเฉพาะกลุ่ม, การทำให้ข้อมูลเป็นมาตรฐานภายในกลุ่ม
```python
import pandas as pd

data = {
    \'City\': [\'New York\', \'New York\', \'London\', \'London\', \'Paris\', \'Paris\'],
    \'Month\': [\'Jan\', \'Feb\', \'Jan\', \'Feb\', \'Jan\', \'Feb\'],
    \'Temperature\': [5, 7, 3, 4, 8, 10],
    \'Humidity\': [60, 65, 80, 75, 70, 72]
}
df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)

# Group by City and calculate mean temperature and max humidity
agg_data = df.groupby(\'City\').agg(
    avg_temp=(\'Temperature\', \'mean\'),
    max_humidity=(\'Humidity\', \'max\')
)
print("\nAggregated Data (mean temp, max humidity by City):")
print(agg_data)

# Using transform to get group-wise mean temperature back to original DataFrame size
df[\'Avg_Temp_City\'] = df.groupby(\'City\')[\'Temperature\'].transform(\'mean\')
print("\nDataFrame with group-wise mean temperature:")
print(df)

# Using filter to select groups where mean temperature is > 6
filtered_df = df.groupby(\'City\').filter(lambda x: x[\'Temperature\'].mean() > 6)
print("\nDataFrame filtered by City (mean temp > 6):")
print(filtered_df)
```

*   **`pivot_table()` และ `crosstab()`:** การปรับรูปร่างข้อมูลเพื่อการวิเคราะห์และการรายงานที่ดีขึ้น
    *   **กรณีการใช้งาน:** การสร้างตาราง Contingency, การสรุปข้อมูลในหลายมิติ
*   **Merging และ Joining:** `pd.merge()`, `pd.concat()` สำหรับการรวม DataFrames

### 3.2.4 การวิเคราะห์อนุกรมเวลาด้วย Pandas
*   **DatetimeIndex:** การทำงานกับข้อมูลที่มีการประทับเวลา
*   **Resampling:** การเปลี่ยนความถี่ของข้อมูลอนุกรมเวลา (เช่น รายวันเป็นรายสัปดาห์)
*   **Rolling Windows:** การคำนวณค่าเฉลี่ยเคลื่อนที่หรือสถิติอื่น ๆ ในช่วงเวลาที่กำหนด

## 3.3 การแสดงภาพข้อมูลเพื่อข้อมูลเชิงลึก (1 ชั่วโมง)

### 3.3.1 Matplotlib: รากฐาน
*   **Figure และ Axes Objects:** การทำความเข้าใจอินเทอร์เฟซเชิงวัตถุสำหรับการควบคุมที่ละเอียด
*   **Subplots และ Grids:** `plt.subplots()`, `GridSpec` สำหรับเลย์เอาต์ที่ซับซ้อน
*   **การปรับแต่ง:** ชื่อเรื่อง, ป้ายกำกับ, คำอธิบาย, คำอธิบายประกอบ, สี, เครื่องหมาย, รูปแบบเส้น
*   **การบันทึกพล็อต:** `fig.savefig()` ด้วยรูปแบบและความละเอียดที่หลากหลาย

### 3.3.2 Seaborn: การแสดงภาพข้อมูลทางสถิติ
*   **Relationship Plots:** `scatterplot()`, `lineplot()`
*   **Distribution Plots:** `histplot()`, `kdeplot()`, `boxplot()`, `violinplot()`
*   **Categorical Plots:** `barplot()`, `countplot()`, `swarmplot()`
*   **Regression Plots:** `regplot()`, `lmplot()`
*   **Matrix Plots:** `heatmap()` สำหรับ Correlation Matrices, `clustermap()`
*   **Facet Grids:** `FacetGrid`, `PairGrid` สำหรับการแสดงภาพความสัมพันธ์ในชุดข้อมูลย่อย
    *   **กรณีการใช้งาน:** การสำรวจว่าความสัมพันธ์ระหว่าง Features เปลี่ยนแปลงไปอย่างไรในหมวดหมู่ที่แตกต่างกัน
```python
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd

# Sample data for demonstration
np.random.seed(42)
data = {
    \'Feature1\': np.random.rand(100),
    \'Feature2\': np.random.randn(100),
    \'Category\': np.random.choice([\'A\', \'B\', \'C\'], 100),
    \'Target\': np.random.randint(0, 2, 100)
}
df = pd.DataFrame(data)

# 1. Heatmap for Correlation Matrix
plt.figure(figsize=(8, 6))
sns.heatmap(df[[\'Feature1\', \'Feature2\', \'Target\']].corr(), annot=True, cmap=\'coolwarm\')
plt.title(\'Correlation Matrix of Numerical Features\')
plt.show()

# 2. PairPlot for pairwise relationships across categories
sns.pairplot(df, hue=\'Category\', vars=[\'Feature1\', \'Feature2\'])
plt.suptitle(\'Pairwise Relationships by Category\', y=1.02) # Adjust suptitle position
plt.show()

# 3. Boxplot of Feature1 by Category
plt.figure(figsize=(8, 6))
sns.boxplot(x=\'Category\', y=\'Feature1\', data=df)
plt.title(\'Distribution of Feature1 by Category\')
plt.show()

# 4. JointPlot for bivariate distribution and individual distributions
sns.jointplot(x=\'Feature1\', y=\'Feature2\', data=df, kind=\'kde\', fill=True)
plt.suptitle(\'Joint Distribution of Feature1 and Feature2\', y=1.02)
plt.show()
```

### 3.3.3 การแสดงภาพแบบโต้ตอบ (แนะนำสั้นๆ)
*   **Plotly / Bokeh / Altair:** การกล่าวถึงเครื่องมือสำหรับการสร้างพล็อตแบบโต้ตอบสำหรับ Web Dashboards หรือการวิเคราะห์เชิงสำรวจ
    *   **กรณีการใช้งาน:** การสร้าง Dashboard แบบโต้ตอบสำหรับการตรวจสอบประสิทธิภาพโมเดล AI หรือการสำรวจชุดข้อมูลที่ซับซ้อน

## แบบฝึกหัดสำหรับโมดูล 3

### แบบฝึกหัด 3.1: การดำเนินการกับ NumPy Array ขั้นสูง
**สถานการณ์:** คุณมีชุดข้อมูลที่แสดงการอ่านค่าเซ็นเซอร์จากอุปกรณ์หลายเครื่องในช่วงเวลาหนึ่ง แต่ละแถวคือ Time Step และแต่ละคอลัมน์คือเซ็นเซอร์ บางเซ็นเซอร์อาจมีข้อมูลที่ขาดหายไปหรือค่าผิดปกติ

**งาน:**
1.  สร้าง NumPy Array `sensor_data` ที่มีรูปร่าง `(100, 5)` ด้วยค่าจำนวนเต็มสุ่มระหว่าง 0 ถึง 100 จำลองค่าที่ขาดหายไปโดยการแทนที่ Element สุ่ม 10 ตัวด้วย `-1`
2.  แทนที่ค่า `-1` ทั้งหมด (ข้อมูลที่ขาดหายไป) ด้วยค่าเฉลี่ยของคอลัมน์เซ็นเซอร์นั้น ๆ (ไม่รวมค่า `-1`)
3.  ทำให้แต่ละคอลัมน์เซ็นเซอร์เป็นมาตรฐาน (Feature Scaling) เพื่อให้ค่าอยู่ในช่วง 0 ถึง 1
4.  คำนวณ Variance ของแต่ละเซ็นเซอร์หลังจากการทำให้เป็นมาตรฐาน

### แบบฝึกหัด 3.2: การทำความสะอาดและการแปลงข้อมูลด้วย Pandas
**สถานการณ์:** คุณได้รับไฟล์ CSV ดิบที่มีข้อมูลการทำธุรกรรมของลูกค้า ข้อมูลไม่เป็นระเบียบและจำเป็นต้องทำความสะอาดอย่างมากก่อนที่จะนำไปใช้ในการวิเคราะห์หรือ Machine Learning

**งาน:**
1.  โหลดข้อมูล CSV (จำลอง) ที่ให้มาลงใน Pandas DataFrame
2.  ระบุและจัดการค่าที่ขาดหายไป: เติมค่า `Age` ที่ขาดหายไปด้วย Median และ `ProductCategory` ที่ขาดหายไปด้วย \'Unknown\'
3.  แปลงคอลัมน์ `TransactionDate` เป็นวัตถุ Datetime
4.  สร้างคอลัมน์ใหม่ `TransactionMonth` (เช่น \'Jan\', \'Feb\')
5.  ทำความสะอาดคอลัมน์ `ProductName`: แปลงเป็นตัวพิมพ์เล็ก, ลบช่องว่างนำหน้า/ต่อท้าย, และแทนที่คำผิดที่พบบ่อย (เช่น \'Appel\' -> \'Apple\')
6.  คำนวณ `Revenue` ทั้งหมดสำหรับแต่ละ `ProductCategory`

**ข้อมูล CSV จำลอง (บันทึกเป็น `transactions.csv`):**
```csv
CustomerID,TransactionID,TransactionDate,ProductName,ProductCategory,Price,Quantity,Age,Gender
1,T001,2023-01-15,Laptop,Electronics,1200,1,30,Male
2,T002,2023-01-16,Mouse,Electronics,25,2,25,Female
3,T003,2023-01-15,Keyboard,Electronics,75,1,,
4,T004,2023-02-01,Appel,Fruits,2,5,40,Female
5,T005,2023-02-02,Banana,Fruits,1,10,35,Male
6,T006,2023-02-03,Laptop,Electronics,1150,1,30,Male
7,T007,2023-03-01,Orange,,1.5,8,28,Female
8,T008,2023-03-02,Milk,Dairy,3,2,,
9,T009,2023-03-03,Bread,Bakery,2.5,1,50,Male
10,T010,2023-01-20,Laptop,Electronics,1250,1,22,Female
```

### แบบฝึกหัด 3.3: Pandas GroupBy และ Pivot Tables ขั้นสูง
**สถานการณ์:** การใช้ข้อมูลการทำธุรกรรมที่ทำความสะอาดแล้วจากแบบฝึกหัด 3.2 คุณต้องการดำเนินการรวมข้อมูลที่ซับซ้อนมากขึ้นและปรับรูปร่างข้อมูลเพื่อรับข้อมูลเชิงลึกที่ลึกซึ้งยิ่งขึ้น

**งาน:**
1.  โหลดข้อมูล `transactions.csv` (สมมติว่าได้รับการทำความสะอาดแล้วตามแบบฝึกหัด 3.2 หรือดำเนินการทำความสะอาดซ้ำอีกครั้ง)
2.  คำนวณ `Price` เฉลี่ยและ `Quantity` ทั้งหมดที่ขายได้สำหรับแต่ละ `ProductCategory` และ `Gender`
3.  สร้าง Pivot Table ที่แสดง `Quantity` ทั้งหมดที่ขายได้สำหรับแต่ละ `ProductCategory` (แถว) ในแต่ละ `TransactionMonth` (คอลัมน์)
4.  ใช้ `groupby().filter()` เพื่อเลือกเฉพาะ `ProductCategory` ที่มี `Price` เฉลี่ยมากกว่า 100

### แบบฝึกหัด 3.4: การแสดงภาพการกระจายและความสัมพันธ์ของข้อมูล
**สถานการณ์:** คุณมีชุดข้อมูลราคาบ้านที่มี Features ต่างๆ คุณต้องการแสดงภาพการกระจายของ Features หลักและความสัมพันธ์กับตัวแปรเป้าหมาย (ราคา)

**งาน:**
1.  สร้างชุดข้อมูลจำลอง 100 แถวและ 4 คอลัมน์: `SquareFootage` (Normal สุ่ม, Mean 1500, Std 300), `NumBedrooms` (Int สุ่ม 2-5), `Neighborhood` (Choice สุ่ม \'A\', \'B\', \'C\'), `Price` (การรวมเชิงเส้นของ Features + Noise)
2.  สร้าง Histogram ของ `SquareFootage` และ `Price` โดยใช้ Matplotlib เพื่อแสดงการกระจายของข้อมูล
3.  สร้าง Box Plot ของ `Price` ตาม `Neighborhood` โดยใช้ Seaborn เพื่อเปรียบเทียบการกระจายราคาในแต่ละย่าน
4.  สร้าง Scatter Plot ของ `SquareFootage` เทียบกับ `Price` โดยใช้สีตาม `NumBedrooms` โดยใช้ Seaborn เพื่อแสดงภาพความสัมพันธ์
5.  สร้าง Correlation Heatmap ของ Features เชิงตัวเลขทั้งหมด

### แบบฝึกหัด 3.5: การวิเคราะห์อนุกรมเวลาด้วย Pandas
**สถานการณ์:** คุณมีข้อมูลราคาหุ้นรายวันของบริษัทและต้องการวิเคราะห์แนวโน้มและความผันผวน

**งาน:**
1.  สร้าง DataFrame จำลองที่มีคอลัมน์ `Date` (วันที่รายวันเป็นเวลา 1 ปี) และคอลัมน์ `ClosePrice` (ราคาหุ้นจำลองที่มีแนวโน้มและ Noise)
2.  ตั้งค่าคอลัมน์ `Date` เป็น Index ของ DataFrame และตรวจสอบให้แน่ใจว่าเป็น `DatetimeIndex`
3.  คำนวณค่าเฉลี่ยเคลื่อนที่ 7 วันของ `ClosePrice` และเพิ่มเป็นคอลัมน์ใหม่ `RollingMean7`
4.  Resample ข้อมูลรายวันเป็นความถี่รายเดือน โดยคำนวณ `ClosePrice` เฉลี่ยสำหรับแต่ละเดือน
5.  พล็อต `ClosePrice` และ `RollingMean7` ดั้งเดิมบนแผนภูมิเดียวกันโดยใช้ Matplotlib

## เฉลยสำหรับโมดูล 3

### เฉลย 3.1: การดำเนินการกับ NumPy Array ขั้นสูง
```python
import numpy as np

# 1. Create a NumPy array sensor_data of shape (100, 5) with random integer values between 0 and 100.
#    Simulate some missing values by replacing 10 random elements with -1.
np.random.seed(42) # for reproducibility
sensor_data = np.random.randint(0, 101, size=(100, 5)).astype(float) # Use float to allow -1 and later mean values

# Simulate 10 missing values
missing_indices = np.random.choice(sensor_data.size, 10, replace=False)
sensor_data.flat[missing_indices] = -1

print("Original sensor_data (first 5 rows, with some -1 for missing values):\n", sensor_data[:5])

# 2. Replace all -1 values (missing data) with the mean of their respective sensor column (excluding -1s).
for col in range(sensor_data.shape[1]):
    col_data = sensor_data[:, col]
    valid_data = col_data[col_data != -1]
    if len(valid_data) > 0:
        col_mean = np.mean(valid_data)
        sensor_data[col_data == -1, col] = col_mean
    else:
        # Handle case where entire column is -1 (unlikely with random data, but good practice)
        sensor_data[col_data == -1, col] = 0 # or some other sensible default

print("\nSensor_data after filling missing values (first 5 rows):\n", sensor_data[:5])

# 3. Normalize each sensor column (feature scaling) so that its values range from 0 to 1.
normalized_sensor_data = np.zeros_like(sensor_data)
for col in range(sensor_data.shape[1]):
    col_data = sensor_data[:, col]
    data_min = np.min(col_data)
    data_max = np.max(col_data)
    if data_max == data_min:
        normalized_sensor_data[:, col] = 0 # All values are the same, normalize to 0
    else:
        normalized_sensor_data[:, col] = (col_data - data_min) / (data_max - data_min)

print("\nNormalized sensor_data (first 5 rows):\n", normalized_sensor_data[:5])

# 4. Calculate the variance of each sensor after normalization.
variances = np.var(normalized_sensor_data, axis=0)
print("\nVariance of each sensor after normalization:\n", variances)
```

### เฉลย 3.2: การทำความสะอาดและการแปลงข้อมูลด้วย Pandas
```python
import pandas as pd
import numpy as np

# Dummy CSV Data (save as `transactions.csv`)
csv_data = """
CustomerID,TransactionID,TransactionDate,ProductName,ProductCategory,Price,Quantity,Age,Gender
1,T001,2023-01-15,Laptop,Electronics,1200,1,30,Male
2,T002,2023-01-16,Mouse,Electronics,25,2,25,Female
3,T003,2023-01-15,Keyboard,Electronics,75,1,,
4,T004,2023-02-01,Appel,Fruits,2,5,40,Female
5,T005,2023-02-02,Banana,Fruits,1,10,35,Male
6,T006,2023-02-03,Laptop,Electronics,1150,1,30,Male
7,T007,2023-03-01,Orange,,1.5,8,28,Female
8,T008,2023-03-02,Milk,Dairy,3,2,,
9,T009,2023-03-03,Bread,Bakery,2.5,1,50,Male
10,T010,2023-01-20,Laptop,Electronics,1250,1,22,Female
"""

# Create a dummy CSV file
with open("transactions.csv", "w") as f:
    f.write(csv_data)

# 1. Load the provided (dummy) CSV data into a Pandas DataFrame.
df = pd.read_csv("transactions.csv")
print("Original DataFrame:\n", df)

# 2. Identify and handle missing values:
#    fill missing Age with the median, and missing ProductCategory with \'Unknown\'.
df[\'Age\'].fillna(df[\'Age\'].median(), inplace=True)
df[\'ProductCategory\'].fillna(\'Unknown\', inplace=True)
print("\nDataFrame after handling missing values:\n", df)

# 3. Convert the TransactionDate column to datetime objects.
df[\'TransactionDate\'] = pd.to_datetime(df[\'TransactionDate\'])
print("\nDataFrame with TransactionDate as datetime:\n", df.info())

# 4. Create a new column TransactionMonth (e.g., \'Jan\', \'Feb\').
df[\'TransactionMonth\'] = df[\'TransactionDate\'].dt.strftime(\'%b\')
print("\nDataFrame with TransactionMonth:\n", df)

# 5. Clean the ProductName column:
#    convert to lowercase, remove leading/trailing spaces, and replace common typos.
df[\'ProductName\'] = df[\'ProductName\'].str.lower().str.strip()
df[\'ProductName\'].replace({\'appel\': \'apple\'}, inplace=True)
print("\nDataFrame after cleaning ProductName:\n", df)

# 6. Calculate the total Revenue for each ProductCategory.
df[\'Revenue\'] = df[\'Price\'] * df[\'Quantity\']
revenue_by_category = df.groupby(\'ProductCategory\')[\'Revenue\'].sum().reset_index()
print("\nTotal Revenue by ProductCategory:\n", revenue_by_category)
```

### เฉลย 3.3: Pandas GroupBy และ Pivot Tables ขั้นสูง
```python
import pandas as pd
import numpy as np

# Re-create dummy CSV data and clean it as per Exercise 3.2 for consistency
csv_data = """
CustomerID,TransactionID,TransactionDate,ProductName,ProductCategory,Price,Quantity,Age,Gender
1,T001,2023-01-15,Laptop,Electronics,1200,1,30,Male
2,T002,2023-01-16,Mouse,Electronics,25,2,25,Female
3,T003,2023-01-15,Keyboard,Electronics,75,1,,
4,T004,2023-02-01,Appel,Fruits,2,5,40,Female
5,T005,2023-02-02,Banana,Fruits,1,10,35,Male
6,T006,2023-02-03,Laptop,Electronics,1150,1,30,Male
7,T007,2023-03-01,Orange,,1.5,8,28,Female
8,T008,2023-03-02,Milk,Dairy,3,2,,
9,T009,2023-03-03,Bread,Bakery,2.5,1,50,Male
10,T010,2023-01-20,Laptop,Electronics,1250,1,22,Female
"""
with open("transactions.csv", "w") as f:
    f.write(csv_data)

df = pd.read_csv("transactions.csv")
df[\'Age\'].fillna(df[\'Age\'].median(), inplace=True)
df[\'ProductCategory\'].fillna(\'Unknown\', inplace=True)
df[\'TransactionDate\'] = pd.to_datetime(df[\'TransactionDate\'])
df[\'TransactionMonth\'] = df[\'TransactionDate\'].dt.strftime(\'%b\')
df[\'ProductName\'] = df[\'ProductName\'].str.lower().str.strip()
df[\'ProductName\'].replace({\'appel\': \'apple\'}, inplace=True)
df[\'Revenue\'] = df[\'Price\'] * df[\'Quantity\']

print("Cleaned DataFrame (first 5 rows):\n", df.head())

# 2. Calculate the average Price and total Quantity sold for each ProductCategory and Gender combination.
agg_by_category_gender = df.groupby([\'ProductCategory\', \'Gender\']).agg(
    AveragePrice=(\'Price\', \'mean\'),
    TotalQuantitySold=(\'Quantity\', \'sum\')
).reset_index()
print("\nAverage Price and Total Quantity Sold by ProductCategory and Gender:\n", agg_by_category_gender)

# 3. Create a pivot table showing the total Quantity sold for each ProductCategory (rows) across different TransactionMonth (columns).
pivot_table_quantity = pd.pivot_table(df, values=\'Quantity\', index=\'ProductCategory\', columns=\'TransactionMonth\', aggfunc=\'sum\', fill_value=0)
print("\nPivot Table: Total Quantity Sold by ProductCategory and Month:\n", pivot_table_quantity)

# 4. Use groupby().filter() to select only those ProductCategorys that have an average Price greater than 100.
filtered_categories_df = df.groupby(\'ProductCategory\').filter(lambda x: x[\'Price\'].mean() > 100)
print("\nDataFrame filtered for ProductCategorys with average Price > 100:\n", filtered_categories_df)
```

### เฉลย 3.4: การแสดงภาพการกระจายและความสัมพันธ์ของข้อมูล
```python
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd

# 1. Generate a dummy dataset
np.random.seed(42)
num_samples = 100

square_footage = np.random.normal(loc=1500, scale=300, size=num_samples)
num_bedrooms = np.random.randint(2, 6, size=num_samples) # 2, 3, 4, 5
neighborhood = np.random.choice([\'A\', \'B\', \'C\'], size=num_samples)

# Price as a linear combination of features + noise
price = 50 * square_footage + 20000 * num_bedrooms + np.random.normal(loc=0, scale=50000, size=num_samples)
price[neighborhood == \'B\'] += 50000 # Neighborhood B is more expensive
price[neighborhood == \'C\'] -= 30000 # Neighborhood C is less expensive
price = np.maximum(100000, price) # Ensure prices are not too low

housing_df = pd.DataFrame({
    \'SquareFootage\': square_footage,
    \'NumBedrooms\': num_bedrooms,
    \'Neighborhood\': neighborhood,
    \'Price\': price
})

print("Dummy Housing Dataset (first 5 rows):\n", housing_df.head())

# 2. Create a histogram of SquareFootage and Price using Matplotlib
plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1) # 1 row, 2 columns, 1st plot
sns.histplot(housing_df[\'SquareFootage\'], kde=True)
plt.title(\'Distribution of Square Footage\')
plt.xlabel(\'Square Footage\')
plt.ylabel(\'Frequency\')

plt.subplot(1, 2, 2) # 1 row, 2 columns, 2nd plot
sns.histplot(housing_df[\'Price\'], kde=True, color=\'orange\')
plt.title(\'Distribution of Price\')
plt.xlabel(\'Price\')
plt.ylabel(\'Frequency\')

plt.tight_layout()
plt.show()

# 3. Create a box plot of Price by Neighborhood using Seaborn
plt.figure(figsize=(8, 6))
sns.boxplot(x=\'Neighborhood\', y=\'Price\', data=housing_df)
plt.title(\'Price Distribution by Neighborhood\')
plt.xlabel(\'Neighborhood\')
plt.ylabel(\'Price\')
plt.show()

# 4. Generate a scatter plot of SquareFootage vs. Price, colored by NumBedrooms using Seaborn
plt.figure(figsize=(10, 7))
sns.scatterplot(x=\'SquareFootage\', y=\'Price\', hue=\'NumBedrooms\', size=\'NumBedrooms\', data=housing_df, palette=\'viridis\', sizes=(20, 200))
plt.title(\'Housing Price vs. Square Footage by Number of Bedrooms\')
plt.xlabel(\'Square Footage\')
plt.ylabel(\'Price\')
plt.legend(title=\'Num Bedrooms\')
plt.show()

# 5. Create a correlation heatmap of all numerical features.
correlation_matrix = housing_df[["SquareFootage", "NumBedrooms", "Price"]].corr()
plt.figure(figsize=(7, 6))
sns.heatmap(correlation_matrix, annot=True, cmap=\'coolwarm\', fmt=\'.2f\')
plt.title(\'Correlation Matrix of Numerical Features\')
plt.show()
```

### เฉลย 3.5: การวิเคราะห์อนุกรมเวลาด้วย Pandas
```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 1. Create a dummy DataFrame with a Date column and a ClosePrice column.
np.random.seed(42)
start_date = pd.to_datetime(\'2023-01-01\')
dates = pd.date_range(start=start_date, periods=365, freq=\'D\')

# Simulate stock prices with a trend and noise
base_price = 100
trend = np.linspace(0, 50, 365) # Upward trend over the year
noise = np.random.normal(0, 5, 365) # Daily fluctuations
close_price = base_price + trend + noise
close_price = np.maximum(50, close_price) # Ensure price doesn\'t go below 50

stock_df = pd.DataFrame({
    \'Date\': dates,
    \'ClosePrice\': close_price
})

print("Dummy Stock Data (first 5 rows):\n", stock_df.head())

# 2. Set the Date column as the DataFrame index and ensure it\'s a DatetimeIndex.
stock_df.set_index(\'Date\', inplace=True)
stock_df.index = pd.to_datetime(stock_df.index)
print("\nStock Data with DatetimeIndex (first 5 rows):\n", stock_df.head())
print("Index type:", type(stock_df.index))

# 3. Calculate the 7-day rolling mean of ClosePrice and add it as a new column RollingMean7.
stock_df[\'RollingMean7\'] = stock_df[\'ClosePrice\'].rolling(window=7).mean()
print("\nStock Data with 7-day Rolling Mean (first 10 rows):\n", stock_df.head(10))

# 4. Resample the daily data to monthly frequency, calculating the mean ClosePrice for each month.
monthly_mean_price = stock_df[\'ClosePrice\'].resample(\'M\').mean()
print("\nMonthly Mean Close Price:\n", monthly_mean_price)

# 5. Plot the original ClosePrice and RollingMean7 on the same chart using Matplotlib.
plt.figure(figsize=(14, 7))
plt.plot(stock_df.index, stock_df[\'ClosePrice\'], label=\'Daily Close Price\', alpha=0.7)
plt.plot(stock_df.index, stock_df[\'RollingMean7\'], label=\'7-Day Rolling Mean\', color=\'red\')
plt.title(\'Stock Close Price and 7-Day Rolling Mean\')
plt.xlabel(\'Date\')
plt.ylabel(\'Price\')
plt.legend()
plt.grid(True)
plt.show()
```

## สรุปโมดูล 3
โมดูลนี้ได้ให้ความรู้เชิงลึกเกี่ยวกับการวิเคราะห์ข้อมูลด้วย Python โดยเน้นที่ไลบรารี NumPy และ Pandas สำหรับการจัดการข้อมูลและการประมวลผลเชิงตัวเลขที่มีประสิทธิภาพ ผู้เข้าร่วมได้เรียนรู้เทคนิคการทำความสะอาดข้อมูล การแปลงข้อมูล และการรวมข้อมูลที่จำเป็นสำหรับการเตรียมชุดข้อมูลสำหรับโมเดล AI นอกจากนี้ยังได้สำรวจการแสดงภาพข้อมูลด้วย Matplotlib และ Seaborn เพื่อดึงข้อมูลเชิงลึกจากข้อมูล การทำความเข้าใจแนวคิดเหล่านี้เป็นสิ่งสำคัญสำหรับการสร้างรากฐานที่แข็งแกร่งในการพัฒนา AI ที่ขับเคลื่อนด้วยข้อมูล

# โมดูล 4: Machine Learning ด้วย Scikit-learn สำหรับ AI สมัยใหม่ (4 ชั่วโมง)

## ภาพรวม
โมดูลนี้จะให้ความเข้าใจที่ครอบคลุมเกี่ยวกับแนวคิด Machine Learning แบบดั้งเดิมและการนำไปใช้งานจริงโดยใช้ Scikit-learn เราจะครอบคลุมขั้นตอนการทำงานของ ML ทั้งหมด ตั้งแต่การประมวลผลข้อมูลล่วงหน้าและการเลือกโมเดลไปจนถึงการปรับแต่ง Hyperparameter และการประเมินผลที่แข็งแกร่ง จะเน้นที่การทำความเข้าใจข้อจำกัดของโมเดล การตีความผลลัพธ์ และการเตรียมข้อมูลสำหรับแอปพลิเคชัน AI ขั้นสูง

## วัตถุประสงค์การเรียนรู้
เมื่อจบโมดูลนี้ ผู้เข้าร่วมจะสามารถ:
*   เข้าใจและประยุกต์ใช้แนวคิดพื้นฐานของ Machine Learning รวมถึงประเภทของปัญหา (Supervised, Unsupervised) และขั้นตอนการทำงานของ ML
*   ดำเนินการ Preprocessing ข้อมูลที่จำเป็น เช่น Feature Scaling, Encoding Categorical Variables และ Feature Engineering
*   สร้างและฝึกโมเดล Machine Learning แบบ Supervised (Regression, Classification) โดยใช้ Scikit-learn
*   สร้างและฝึกโมเดล Machine Learning แบบ Unsupervised (Clustering, Dimensionality Reduction) โดยใช้ Scikit-learn
*   ประเมินประสิทธิภาพของโมเดลอย่างถูกต้องโดยใช้เมตริกที่เหมาะสมและเทคนิค Cross-validation
*   ปรับแต่ง Hyperparameter ของโมเดลเพื่อประสิทธิภาพสูงสุด

## 4.1 พื้นฐาน Machine Learning และ Scikit-learn (1 ชั่วโมง)

### 4.1.1 ประเภทของ Machine Learning
*   **Supervised Learning:** การเรียนรู้ภายใต้การกำกับดูแล (Regression, Classification)
    *   **กรณีการใช้งาน:** การทำนายราคาบ้าน, การจำแนกอีเมลสแปม
*   **Unsupervised Learning:** การเรียนรู้แบบไม่มีการกำกับดูแล (Clustering, Dimensionality Reduction)
    *   **กรณีการใช้งาน:** การแบ่งกลุ่มลูกค้า, การลดมิติข้อมูลเพื่อการแสดงภาพ
*   **Reinforcement Learning:** การเรียนรู้แบบเสริมกำลัง (แนะนำสั้นๆ)

### 4.1.2 ขั้นตอนการทำงานของ Machine Learning
1.  **การรวบรวมข้อมูล (Data Collection)**
2.  **การทำความสะอาดข้อมูล (Data Cleaning)**
3.  **การสำรวจข้อมูล (Exploratory Data Analysis - EDA)**
4.  **การประมวลผลข้อมูลล่วงหน้า (Data Preprocessing)**
5.  **การเลือกโมเดล (Model Selection)**
6.  **การฝึกโมเดล (Model Training)**
7.  **การประเมินโมเดล (Model Evaluation)**
8.  **การปรับแต่ง Hyperparameter (Hyperparameter Tuning)**
9.  **การปรับใช้โมเดล (Model Deployment)**

### 4.1.3 การแนะนำ Scikit-learn
*   **โครงสร้าง API ที่สอดคล้องกัน:** `fit()`, `predict()`, `transform()`
*   **โมดูลหลัก:** `preprocessing`, `model_selection`, `linear_model`, `ensemble`, `cluster`, `decomposition`

## 4.2 การประมวลผลข้อมูลล่วงหน้าสำหรับ ML (1 ชั่วโมง)

### 4.2.1 การจัดการค่าที่ขาดหายไป
*   **`SimpleImputer`:** การเติมค่าที่ขาดหายไปด้วย Mean, Median, Mode หรือค่าคงที่
*   **กลยุทธ์ขั้นสูง:** การใช้โมเดล ML เพื่อทำนายค่าที่ขาดหายไป (เช่น `IterativeImputer`)

### 4.2.2 การเข้ารหัสตัวแปรเชิงหมวดหมู่ (Categorical Encoding)
*   **`OneHotEncoder`:** การแปลงตัวแปรเชิงหมวดหมู่เป็นรูปแบบ Binary Vector
*   **`LabelEncoder`:** การแปลงตัวแปรเชิงหมวดหมู่เป็นตัวเลข (สำหรับ Target Variable)
*   **`OrdinalEncoder`:** การแปลงตัวแปรเชิงหมวดหมู่เป็นตัวเลขตามลำดับ (สำหรับ Feature)

### 4.2.3 การปรับขนาด Feature (Feature Scaling)
*   **`StandardScaler`:** การทำให้ข้อมูลเป็นมาตรฐาน (Mean = 0, Std Dev = 1)
*   **`MinMaxScaler`:** การปรับขนาดข้อมูลให้อยู่ในช่วงที่กำหนด (เช่น 0 ถึง 1)
*   **`RobustScaler`:** การปรับขนาดที่ทนทานต่อ Outliers

### 4.2.4 Feature Engineering (แนะนำสั้นๆ)
*   **การสร้าง Features ใหม่:** จาก Features ที่มีอยู่ (เช่น Polynomial Features, Interaction Features)
*   **`PolynomialFeatures`:** การสร้าง Features พหุนาม

### 4.2.5 การแบ่งชุดข้อมูล
*   **`train_test_split`:** การแบ่งข้อมูลเป็นชุดฝึกและชุดทดสอบ
*   **Cross-validation:** `KFold`, `StratifiedKFold` สำหรับการประเมินโมเดลที่แข็งแกร่ง

## 4.3 โมเดล Supervised Learning (1 ชั่วโมง)

### 4.3.1 Regression
*   **`LinearRegression`:** โมเดลเชิงเส้นพื้นฐาน
*   **`Ridge`, `Lasso`:** Regularized Linear Models สำหรับการจัดการ Overfitting
*   **`DecisionTreeRegressor`:** โมเดลต้นไม้ตัดสินใจ
*   **`RandomForestRegressor`:** Ensemble Model สำหรับ Regression
*   **เมตริกการประเมิน:** `mean_squared_error`, `r2_score`

### 4.3.2 Classification
*   **`LogisticRegression`:** โมเดลเชิงเส้นสำหรับการจำแนก
*   **`SVC` (Support Vector Classifier):** โมเดล Support Vector Machine
*   **`DecisionTreeClassifier`:** โมเดลต้นไม้ตัดสินใจ
*   **`RandomForestClassifier`:** Ensemble Model สำหรับ Classification
*   **เมตริกการประเมิน:** `accuracy_score`, `precision_score`, `recall_score`, `f1_score`, `confusion_matrix`, `roc_auc_score`

## 4.4 โมเดล Unsupervised Learning (0.5 ชั่วโมง)

### 4.4.1 Clustering
*   **`KMeans`:** อัลกอริทึมการจัดกลุ่มที่ได้รับความนิยม
*   **`DBSCAN`:** การจัดกลุ่มตามความหนาแน่น
*   **เมตริกการประเมิน:** `silhouette_score`

### 4.4.2 Dimensionality Reduction
*   **`PCA` (Principal Component Analysis):** การลดมิติเชิงเส้น
*   **`TSNE`, `UMAP` (แนะนำสั้นๆ):** การลดมิติสำหรับการแสดงภาพ

## 4.5 การปรับแต่งโมเดลและการประเมินผล (0.5 ชั่วโมง)

### 4.5.1 Hyperparameter Tuning
*   **`GridSearchCV`:** การค้นหาแบบ Exhaustive Search สำหรับ Hyperparameter ที่ดีที่สุด
*   **`RandomizedSearchCV`:** การค้นหาแบบสุ่มสำหรับ Hyperparameter ที่ดีที่สุด

### 4.5.2 Pipelines
*   **`Pipeline`:** การรวมขั้นตอนการประมวลผลข้อมูลและโมเดลเข้าด้วยกัน
*   **ประโยชน์:** ลดข้อผิดพลาด, ทำให้โค้ดสะอาดขึ้น, อำนวยความสะดวกในการทำ Cross-validation

## สรุปโมดูล 4
โมดูลนี้ได้ให้ความรู้ที่แข็งแกร่งเกี่ยวกับ Machine Learning ด้วย Scikit-learn ผู้เข้าร่วมได้เรียนรู้ขั้นตอนการทำงานของ ML ตั้งแต่การประมวลผลข้อมูลล่วงหน้า การสร้างและฝึกโมเดล Supervised และ Unsupervised ไปจนถึงการประเมินและปรับแต่งโมเดล การทำความเข้าใจแนวคิดและเครื่องมือเหล่านี้เป็นสิ่งสำคัญสำหรับการสร้างและปรับใช้โซลูชัน AI ที่มีประสิทธิภาพในโลกแห่งความเป็นจริง

### เฉลย 4.1: ขั้นตอนการทำงานของการจำแนกประเภทพร้อมการประมวลผลข้อมูลล่วงหน้า
```python
import numpy as np
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.impute import SimpleImputer
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
import pandas as pd

# 1. Generate synthetic dataset with missing values
X, y = make_classification(n_samples=1000, n_features=10, n_informative=5, n_redundant=5, random_state=42)

# Introduce some missing values
missing_mask = np.random.rand(*X.shape) < 0.05 # 5% missing values
X[missing_mask] = np.nan

# Simulate categorical features (convert some numerical to object type)
X_df = pd.DataFrame(X, columns=[f\"feature_{i}\" for i in range(X.shape[1])])
X_df[\"feature_0\"] = X_df[\"feature_0\"].apply(lambda x: \"CatA\" if x > 0 else \"CatB\" if x < 0 else np.nan)
X_df[\"feature_1\"] = X_df[\"feature_1\"].apply(lambda x: \"TypeX\" if x > 0.5 else \"TypeY\" if x < -0.5 else np.nan)

# Identify numerical and categorical features
numerical_features = [f\"feature_{i}\" for i in range(2, 10)] # Features 2-9 are numerical
categorical_features = [\"feature_0\", \"feature_1\"]

# 2. Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X_df, y, test_size=0.2, random_state=42)

# 3. Create a preprocessing pipeline
numerical_transformer = Pipeline(steps=[
    (\"imputer\", SimpleImputer(strategy=\"mean\")),
    (\"scaler\", StandardScaler())
])

categorical_transformer = Pipeline(steps=[
    (\"imputer\", SimpleImputer(strategy=\"most_frequent\")),
    (\"onehot\", OneHotEncoder(handle_unknown=\"ignore\"))
])

preprocessor = ColumnTransformer(
    transformers=[
        (\"num\", numerical_transformer, numerical_features),
        (\"cat\", categorical_transformer, categorical_features)
    ])

# 4. Train a LogisticRegression model within this pipeline
model_pipeline = Pipeline(steps=[
    (\"preprocessor\", preprocessor),
    (\"classifier\", LogisticRegression(random_state=42))
])

model_pipeline.fit(X_train, y_train)

# 5. Evaluate the model
y_pred = model_pipeline.predict(X_test)

print(f\"Accuracy: {accuracy_score(y_test, y_pred):.4f}\")
print(f\"Precision: {precision_score(y_test, y_pred):.4f}\")
print(f\"Recall: {recall_score(y_test, y_pred):.4f}\")
print(f\"F1-Score: {f1_score(y_test, y_pred):.4f}\")
```

### เฉลย 4.2: การปรับแต่ง Hyperparameter สำหรับ Random Forest Classifier
```python
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# 1. Load the Iris dataset
iris = load_iris()
X, y = iris.data, iris.target

# 2. Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 3. Perform GridSearchCV
param_grid = {
    \"n_estimators\": [50, 100, 200],
    \"max_depth\": [None, 10, 20],
    \"min_samples_split\": [2, 5, 10]
}

rf = RandomForestClassifier(random_state=42)
grid_search = GridSearchCV(estimator=rf, param_grid=param_grid, cv=5, scoring=\"accuracy\", n_jobs=-1)
grid_search.fit(X_train, y_train)

# 4. Report the best parameters and score
print(f\"Best parameters: {grid_search.best_params_}\")
print(f\"Best cross-validation accuracy: {grid_search.best_score_:.4f}\")

# 5. Train with best parameters and evaluate on test set
best_rf = grid_search.best_estimator_
y_pred = best_rf.predict(X_test)
print(f\"Test set accuracy with best parameters: {accuracy_score(y_test, y_pred):.4f}\")
```

### เฉลย 4.3: การเปรียบเทียบโมเดล Regression และ Cross-Validation
```python
from sklearn.datasets import make_regression
from sklearn.model_selection import cross_val_score, KFold
from sklearn.linear_model import LinearRegression, Ridge
from sklearn.ensemble import RandomForestRegressor
import numpy as np

# 1. Generate a synthetic regression dataset
X, y = make_regression(n_samples=1000, n_features=10, n_informative=5, random_state=42)

# Initialize models
models = {
    \"Linear Regression\": LinearRegression(),
    \"Ridge Regression\": Ridge(random_state=42),
    \"Random Forest Regressor\": RandomForestRegressor(random_state=42)
}

# Define cross-validation strategy
kf = KFold(n_splits=5, shuffle=True, random_state=42)

print(\"Regression Model Comparison with 5-Fold Cross-Validation:\")
for name, model in models.items():
    # Evaluate using negative mean squared error
    mse_scores = cross_val_score(model, X, y, cv=kf, scoring=\"neg_mean_squared_error\", n_jobs=-1)
    rmse_scores = np.sqrt(-mse_scores) # Convert neg_mse to RMSE

    # Evaluate using R-squared
    r2_scores = cross_val_score(model, X, y, cv=kf, scoring=\"r2\", n_jobs=-1)

    print(f\"\n--- {name} ---\")
    print(f\"  Mean RMSE: {np.mean(rmse_scores):.4f} (Std: {np.std(rmse_scores):.4f})\")
    print(f\"  Mean R-squared: {np.mean(r2_scores):.4f} (Std: {np.std(r2_scores):.4f})\")
```

### เฉลย 4.4: การทำความเข้าใจความสำคัญของ Feature ด้วยโมเดล Tree-based
```python
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

# 1. Load the Wine dataset
wine = load_wine()
X, y = wine.data, wine.target
feature_names = wine.feature_names

# 2. Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 3. Train a RandomForestClassifier
rf_model = RandomForestClassifier(n_estimators=100, random_state=42)
rf_model.fit(X_train, y_train)

# 4. Extract and print feature importances
importances = rf_model.feature_importances_
feature_importance_df = pd.DataFrame({
    \"Feature\": feature_names,
    \"Importance\": importances
}).sort_values(by=\"Importance\", ascending=False)

print(\"Feature Importances:\n\", feature_importance_df)

# 5. Visualize the feature importances
plt.figure(figsize=(10, 7))
sns.barplot(x=\"Importance\", y=\"Feature\", data=feature_importance_df, palette=\"viridis\")
plt.title(\"Feature Importances from RandomForestClassifier\")
plt.xlabel(\"Importance\")
plt.ylabel(\"Feature Name\")
plt.tight_layout()
plt.show()
```

### เฉลย 4.5: ฟังก์ชันการประเมินที่กำหนดเองและข้อมูลที่ไม่สมดุล
```python
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import precision_score, recall_score, f1_score, make_scorer
import numpy as np

# 1. Generate an imbalanced dataset
X, y = make_classification(n_samples=1000, n_features=2, n_informative=2, n_redundant=0,
                           n_clusters_per_class=1, weights=[0.95, 0.05], flip_y=0, random_state=42)

print(f\"Class distribution: {np.bincount(y)}\")

# 2. Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

# 3. Train a LogisticRegression model
model = LogisticRegression(random_state=42)
model.fit(X_train, y_train)

# 4. Calculate and report precision, recall, and f1-score for the positive class (class 1)
y_pred = model.predict(X_test)

precision = precision_score(y_test, y_pred, pos_label=1)
recall = recall_score(y_test, y_pred, pos_label=1)
f1 = f1_score(y_test, y_pred, pos_label=1)

print(f\"\n--- Initial Model Evaluation ---\")
print(f\"Precision (Class 1): {precision:.4f}\")
print(f\"Recall (Class 1): {recall:.4f}\")
print(f\"F1-Score (Class 1): {f1:.4f}\")

# 5. Create a custom scoring function for GridSearchCV that optimizes for recall of the positive class
custom_recall_scorer = make_scorer(recall_score, pos_label=1)

# 6. Perform GridSearchCV optimizing for custom recall scorer
param_grid = {
    \"C\": [0.01, 0.1, 1, 10, 100],
    \"solver\": [\"liblinear\", \"lbfgs\"]
}

grid_search = GridSearchCV(estimator=LogisticRegression(random_state=42), param_grid=param_grid,
                           cv=5, scoring=custom_recall_scorer, n_jobs=-1)
grid_search.fit(X_train, y_train)

print(f\"\n--- GridSearchCV with Custom Recall Scorer ---\")
print(f\"Best parameters: {grid_search.best_params_}\")
print(f\"Best cross-validation recall (Class 1): {grid_search.best_score_:.4f}\")

# Evaluate the best model on the test set
best_model = grid_search.best_estimator_
y_pred_best = best_model.predict(X_test)

precision_best = precision_score(y_test, y_pred_best, pos_label=1)
recall_best = recall_score(y_test, y_pred_best, pos_label=1)
f1_best = f1_score(y_test, y_pred_best, pos_label=1)

print(f\"Test set Precision (Class 1) with best model: {precision_best:.4f}\")
print(f\"Test set Recall (Class 1) with best model: {recall_best:.4f}\")
print(f\"Test set F1-Score (Class 1) with best model: {f1_best:.4f}\")
```

## สรุปโมดูล 4
โมดูล 4 ได้เจาะลึกเข้าไปในโลกของ Machine Learning โดยใช้ Scikit-learn ซึ่งครอบคลุมขั้นตอนการทำงานที่จำเป็นตั้งแต่การเตรียมข้อมูลไปจนถึงการประเมินและการเลือกโมเดล เราได้สำรวจอัลกอริทึมการเรียนรู้แบบ Supervised ที่หลากหลายสำหรับการจำแนกประเภท (Logistic Regression, Decision Trees, Random Forests, SVM, KNN) และ Regression (Linear Regression, Ridge, Lasso, Random Forest Regressors) โดยทำความเข้าใจหลักการพื้นฐานและการประยุกต์ใช้จริง จุดเน้นที่สำคัญคือการประเมินประสิทธิภาพของโมเดลอย่างแข็งแกร่งโดยใช้เมตริกที่เหมาะสม (Accuracy, Precision, Recall, F1-score, ROC-AUC สำหรับการจำแนกประเภท; MAE, MSE, RMSE, R-squared สำหรับ Regression) และบทบาทสำคัญของ Cross-validation สำหรับการประมาณค่าประสิทธิภาพที่เชื่อถือได้ สุดท้าย เราได้เจาะลึกเทคนิคการปรับแต่ง Hyperparameter เช่น Grid Search และ Random Search และหารือเกี่ยวกับแนวคิดพื้นฐานของ Bias-Variance Trade-off ซึ่งช่วยให้ผู้เข้าร่วมมีความรู้ในการสร้าง ปรับแต่ง และตีความโมเดล Machine Learning ที่มีประสิทธิภาพสำหรับปัญหา AI ที่หลากหลาย

# โมดูล 5: Deep Learning ด้วย PyTorch สำหรับ AI สมัยใหม่ (4 ชั่วโมง)

## ภาพรวม
โมดูลนี้จะแนะนำผู้เข้าร่วมสู่โลกที่น่าตื่นเต้นของ Deep Learning โดยเน้นการนำไปใช้งานจริงโดยใช้ PyTorch ซึ่งเป็นไลบรารี Machine Learning แบบ Open-source ชั้นนำ เราจะครอบคลุมแนวคิดพื้นฐานของโครงข่ายประสาทเทียม สร้างและฝึกสถาปัตยกรรม Deep Learning ที่หลากหลาย และสำรวจหัวข้อขั้นสูงที่เกี่ยวข้องกับแอปพลิเคชัน AI สมัยใหม่ รวมถึง Transfer Learning และการแนะนำโมเดล Generative

## วัตถุประสงค์การเรียนรู้
เมื่อจบโมดูลนี้ ผู้เข้าร่วมจะสามารถ:
*   เข้าใจแนวคิดหลักของ Deep Learning และโครงข่ายประสาทเทียม
*   ทำงานกับ PyTorch Tensors และดำเนินการ Tensor ที่จำเป็น
*   สร้างและฝึก Feedforward Neural Networks (FFNNs) สำหรับงานจำแนกประเภทและ Regression
*   ใช้งาน Convolutional Neural Networks (CNNs) สำหรับงานประมวลผลภาพ
*   ประยุกต์ใช้เทคนิค Transfer Learning เพื่อใช้ประโยชน์จากโมเดลที่ได้รับการฝึกอบรมล่วงหน้า
*   เข้าใจพื้นฐานของ Recurrent Neural Networks (RNNs) และการประยุกต์ใช้ในข้อมูลลำดับ
*   เข้าใจหลักการของโมเดล Generative (GANs, VAEs) และศักยภาพใน AI

## 5.1 บทนำสู่ Deep Learning และพื้นฐาน PyTorch (1 ชั่วโมง)

### 5.1.1 Deep Learning คืออะไร?
*   **คำจำกัดความ:** โครงข่ายประสาทเทียมที่มีหลายชั้น
*   **ทำไมต้อง Deep Learning?** ข้อดีเหนือ ML แบบดั้งเดิมสำหรับข้อมูลที่ซับซ้อน (รูปภาพ, ข้อความ, เสียง)
*   **แอปพลิเคชันหลัก:** Computer Vision, Natural Language Processing, Speech Recognition, Generative AI

### 5.1.2 พื้นฐานสถาปัตยกรรมโครงข่ายประสาทเทียม
*   **Neurons (Perceptrons):** หน่วยการสร้างพื้นฐาน
*   **Layers:** Input, Hidden, Output layers
*   **Weights และ Biases:** พารามิเตอร์ที่เรียนรู้ระหว่างการฝึก
*   **Activation Functions:** Non-linearities (ReLU, Sigmoid, Tanh, Softmax)
*   **Forward Pass:** การไหลของข้อมูลผ่านโครงข่าย

### 5.1.3 PyTorch Tensors
*   **คำจำกัดความ:** อาร์เรย์หลายมิติ คล้ายกับ NumPy Arrays แต่มีความสามารถในการเร่งความเร็วด้วย GPU และการหาอนุพันธ์อัตโนมัติ
*   **การสร้าง Tensors:** `torch.tensor()`, `torch.zeros()`, `torch.ones()`, `torch.rand()`, `torch.randn()`
*   **การดำเนินการกับ Tensor:** การคำนวณ, การ Slicing, การปรับรูปร่าง (`view()`, `reshape()`), การรวม (`torch.cat()`)
*   **CPU เทียบกับ GPU:** การย้าย Tensors ระหว่างอุปกรณ์ (`.to()`, `.cuda()`)
```python
import torch

# Creating tensors
x = torch.tensor([[1, 2], [3, 4]])
y = torch.ones(2, 2)
z = torch.rand(2, 2)

print(f\"x:\n{x}\")
print(f\"y:\n{y}\")
print(f\"z:\n{z}\")

# Tensor operations
print(f\"\nx + y:\n{x + y}\")
print(f\"x * z:\n{x * z}\") # Element-wise multiplication
print(f\"Matrix multiplication: {x.matmul(z)}\")

# Reshaping
print(f\"\nx.view(4): {x.view(4)}\")

# CPU vs GPU
if torch.cuda.is_available():
    device = torch.device(\"cuda\")
    x_gpu = x.to(device)
    print(f\"\nx on GPU:\n{x_gpu}\")
else:
    print(\"\nCUDA not available, running on CPU.\")
```

### 5.1.4 Autograd: การหาอนุพันธ์อัตโนมัติ
*   **`requires_grad=True`:** การติดตามการดำเนินการสำหรับการคำนวณ Gradient
*   **Computation Graph:** วิธีที่ PyTorch สร้างกราฟของการดำเนินการ
*   **`.backward()`:** การคำนวณ Gradients
*   **`.grad` attribute:** การเข้าถึง Gradients
*   **`torch.no_grad()`:** การปิดใช้งานการคำนวณ Gradient สำหรับ Inference
```python
import torch

x = torch.tensor(2.0, requires_grad=True)
y = x**2 + 3*x + 1

print(f\"x: {x}\")
print(f\"y: {y}\")

y.backward() # Compute gradients

print(f\"Gradient of y with respect to x: {x.grad}\") # Should be 2*x + 3 = 2*2 + 3 = 7

# Example with multiple variables
a = torch.tensor(3.0, requires_grad=True)
b = torch.tensor(4.0, requires_grad=True)
c = a * b
d = c + a**2

d.backward()

print(f\"\nGradient of d with respect to a: {a.grad}\") # Should be b + 2*a = 4 + 2*3 = 10
print(f\"Gradient of d with respect to b: {b.grad}\") # Should be a = 3

# Disabling gradient tracking
print(\"\n--- No Grad Context ---\")
with torch.no_grad():
    e = x**2
    print(f\"e: {e}\")
    print(f\"e.requires_grad: {e.requires_grad}\") # Should be False
```

## 5.2 การสร้างและฝึกโครงข่ายประสาทเทียม (1.5 ชั่วโมง)

### 5.2.1 Feedforward Neural Networks (FFNNs)
*   **สถาปัตยกรรม:** Input Layer, Hidden Layers, Output Layer
*   **`torch.nn` Module:** การสร้าง Layers (Linear, ReLU)
*   **`torch.optim` Module:** Optimizers (SGD, Adam)
*   **Loss Functions:** `nn.CrossEntropyLoss` (Classification), `nn.MSELoss` (Regression)
*   **ขั้นตอนการฝึก:** Forward Pass, คำนวณ Loss, Backward Pass, ปรับ Weights
*   **ตัวอย่าง:** การสร้าง FFNN สำหรับการจำแนกตัวเลขจาก MNIST
```python
import torch
import torch.nn as nn
import torch.optim as optim
from torchvision import datasets, transforms
from torch.utils.data import DataLoader

# 1. Data Loading and Preprocessing
transform = transforms.Compose([
    transforms.ToTensor(),
    transforms.Normalize((0.1307,), (0.3081,))
])

train_dataset = datasets.MNIST(\".\", train=True, download=True, transform=transform)
test_dataset = datasets.MNIST(\".\", train=False, download=True, transform=transform)

train_loader = DataLoader(train_dataset, batch_size=64, shuffle=True)
test_loader = DataLoader(test_dataset, batch_size=1000, shuffle=False)

# 2. Define the Feedforward Neural Network
class FFNN(nn.Module):
    def __init__(self):
        super(FFNN, self).__init__()
        self.fc1 = nn.Linear(28 * 28, 128) # 28x28 pixels input
        self.relu = nn.ReLU()
        self.fc2 = nn.Linear(128, 10) # 10 output classes (digits 0-9)

    def forward(self, x):
        x = x.view(-1, 28 * 28) # Flatten the image
        x = self.fc1(x)
        x = self.relu(x)
        x = self.fc2(x)
        return x

model = FFNN()

# 3. Loss Function and Optimizer
criterion = nn.CrossEntropyLoss()
optimizer = optim.Adam(model.parameters(), lr=0.001)

# 4. Training the Model
num_epochs = 5
for epoch in range(num_epochs):
    model.train()
    for batch_idx, (data, target) in enumerate(train_loader):
        optimizer.zero_grad()
        output = model(data)
        loss = criterion(output, target)
        loss.backward()
        optimizer.step()
        if batch_idx % 100 == 0:
            print(f\"Epoch {epoch+1}/{num_epochs}, Batch {batch_idx}/{len(train_loader)}, Loss: {loss.item():.4f}\")

# 5. Evaluating the Model
model.eval()
correct = 0
total = 0
with torch.no_grad():
    for data, target in test_loader:
        output = model(data)
        _, predicted = torch.max(output.data, 1)
        total += target.size(0)
        correct += (predicted == target).sum().item()

print(f\"\nAccuracy of the FFNN on the 10000 test images: {100 * correct / total:.2f}%\")
```

### 5.2.2 Convolutional Neural Networks (CNNs)
*   **แนวคิด:** เหมาะสำหรับข้อมูลภาพ โดยใช้ Convolutional Layers เพื่อตรวจจับรูปแบบเชิงพื้นที่
*   **Convolutional Layer:** Filters, Stride, Padding
*   **Pooling Layer:** Max Pooling, Average Pooling สำหรับการลดมิติ
*   **Use Case:** Image Classification, Object Detection, Image Segmentation
*   **ตัวอย่าง:** การสร้าง CNN อย่างง่ายสำหรับ MNIST
```python
import torch
import torch.nn as nn
import torch.optim as optim
from torchvision import datasets, transforms
from torch.utils.data import DataLoader

# Data Loading and Preprocessing (same as FFNN example)
transform = transforms.Compose([
    transforms.ToTensor(),
    transforms.Normalize((0.1307,), (0.3081,))
])

train_dataset = datasets.MNIST(\".\", train=True, download=True, transform=transform)
test_dataset = datasets.MNIST(\".\", train=False, download=True, transform=transform)

train_loader = DataLoader(train_dataset, batch_size=64, shuffle=True)
test_loader = DataLoader(test_dataset, batch_size=1000, shuffle=False)

# Define the Convolutional Neural Network
class CNN(nn.Module):
    def __init__(self):
        super(CNN, self).__init__()
        self.conv1 = nn.Conv2d(1, 32, kernel_size=3, stride=1, padding=1) # Input channel 1 (grayscale), 32 output channels
        self.relu1 = nn.ReLU()
        self.pool1 = nn.MaxPool2d(kernel_size=2, stride=2)
        self.conv2 = nn.Conv2d(32, 64, kernel_size=3, stride=1, padding=1)
        self.relu2 = nn.ReLU()
        self.pool2 = nn.MaxPool2d(kernel_size=2, stride=2)
        self.fc = nn.Linear(64 * 7 * 7, 10) # 64 channels, 7x7 image size after pooling, 10 output classes

    def forward(self, x):
        x = self.pool1(self.relu1(self.conv1(x)))
        x = self.pool2(self.relu2(self.conv2(x)))
        x = x.view(-1, 64 * 7 * 7) # Flatten for fully connected layer
        x = self.fc(x)
        return x

model_cnn = CNN()

# Loss Function and Optimizer
criterion_cnn = nn.CrossEntropyLoss()
optimizer_cnn = optim.Adam(model_cnn.parameters(), lr=0.001)

# Training the Model
num_epochs_cnn = 5
for epoch in range(num_epochs_cnn):
    model_cnn.train()
    for batch_idx, (data, target) in enumerate(train_loader):
        optimizer_cnn.zero_grad()
        output = model_cnn(data)
        loss = criterion_cnn(output, target)
        loss.backward()
        optimizer_cnn.step()
        if batch_idx % 100 == 0:
            print(f\"CNN Epoch {epoch+1}/{num_epochs_cnn}, Batch {batch_idx}/{len(train_loader)}, Loss: {loss.item():.4f}\")

# Evaluating the Model
model_cnn.eval()
correct_cnn = 0
total_cnn = 0
with torch.no_grad():
    for data, target in test_loader:
        output = model_cnn(data)
        _, predicted = torch.max(output.data, 1)
        total_cnn += target.size(0)
        correct_cnn += (predicted == target).sum().item()

print(f\"\nAccuracy of the CNN on the 10000 test images: {100 * correct_cnn / total_cnn:.2f}%\")
```

### 5.2.3 Recurrent Neural Networks (RNNs) (แนะนำสั้นๆ)
*   **แนวคิด:** เหมาะสำหรับข้อมูลลำดับ (Sequential Data) เช่น ข้อความ, อนุกรมเวลา
*   **ปัญหา:** Vanishing/Exploding Gradients
*   **Variants:** LSTM (Long Short-Term Memory), GRU (Gated Recurrent Unit) เพื่อแก้ไขปัญหา
*   **Use Case:** Natural Language Processing (NLP), Speech Recognition, Time Series Prediction

## 5.3 หัวข้อขั้นสูงใน Deep Learning (1 ชั่วโมง)

### 5.3.1 Transfer Learning
*   **แนวคิด:** การใช้โมเดลที่ได้รับการฝึกอบรมล่วงหน้าบนชุดข้อมูลขนาดใหญ่ (เช่น ImageNet) และปรับแต่งสำหรับงานเฉพาะ
*   **ประโยชน์:** ลดเวลาการฝึก, ต้องการข้อมูลน้อยลง, ประสิทธิภาพดีขึ้น
*   **กลยุทธ์:** Feature Extraction, Fine-tuning
*   **ตัวอย่าง:** การใช้โมเดล ResNet ที่ได้รับการฝึกอบรมล่วงหน้าสำหรับ Image Classification
```python
import torch
import torch.nn as nn
import torch.optim as optim
from torchvision import models, transforms, datasets
from torch.utils.data import DataLoader

# 1. Data Loading and Preprocessing for a custom dataset (e.g., small image dataset)
# For demonstration, we'll use a subset of MNIST and pretend it's a new dataset
# In a real scenario, you'd load your own custom image dataset

transform_transfer = transforms.Compose([
    transforms.Resize(224), # ResNet expects 224x224 input
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]) # ImageNet normalization
])

# Using MNIST as a dummy custom dataset (will convert to 3 channels)
class MNIST3Channel(datasets.MNIST):
    def __getitem__(self, index):
        img, target = super().__getitem__(index)
        return img.repeat(3, 1, 1), target # Convert to 3 channels

train_dataset_transfer = MNIST3Channel(\".\", train=True, download=True, transform=transform_transfer)
test_dataset_transfer = MNIST3Channel(\".\", train=False, download=True, transform=transform_transfer)

# Reduce dataset size for faster demonstration
train_dataset_transfer.data = train_dataset_transfer.data[:1000]
train_dataset_transfer.targets = train_dataset_transfer.targets[:1000]
test_dataset_transfer.data = test_dataset_transfer.data[:200]
test_dataset_transfer.targets = test_dataset_transfer.targets[:200]

train_loader_transfer = DataLoader(train_dataset_transfer, batch_size=32, shuffle=True)
test_loader_transfer = DataLoader(test_dataset_transfer, batch_size=32, shuffle=False)

# 2. Load a pre-trained model (e.g., ResNet18)
model_ft = models.resnet18(pretrained=True)

# Freeze all parameters in the network
for param in model_ft.parameters():
    param.requires_grad = False

# Replace the last fully connected layer with a new one for our number of classes (10 for MNIST)
num_ftrs = model_ft.fc.in_features
model_ft.fc = nn.Linear(num_ftrs, 10) # 10 classes for MNIST

# Move model to GPU if available
device = torch.device(\"cuda:0\" if torch.cuda.is_available() else \"cpu\")
model_ft = model_ft.to(device)

# 3. Loss Function and Optimizer (only optimizing the new fc layer)
criterion_transfer = nn.CrossEntropyLoss()
optimizer_transfer = optim.Adam(model_ft.fc.parameters(), lr=0.001)

# 4. Training the Model (Feature Extraction)
num_epochs_transfer = 3
for epoch in range(num_epochs_transfer):
    model_ft.train()
    running_loss = 0.0
    for inputs, labels in train_loader_transfer:
        inputs, labels = inputs.to(device), labels.to(device)

        optimizer_transfer.zero_grad()
        outputs = model_ft(inputs)
        loss = criterion_transfer(outputs, labels)
        loss.backward()
        optimizer_transfer.step()
        running_loss += loss.item() * inputs.size(0)
    epoch_loss = running_loss / len(train_dataset_transfer)
    print(f\"Transfer Learning Epoch {epoch+1}/{num_epochs_transfer}, Loss: {epoch_loss:.4f}\")

# 5. Evaluating the Model
model_ft.eval()
correct_transfer = 0
total_transfer = 0
with torch.no_grad():
    for inputs, labels in test_loader_transfer:
        inputs, labels = inputs.to(device), labels.to(device)
        outputs = model_ft(inputs)
        _, predicted = torch.max(outputs.data, 1)
        total_transfer += labels.size(0)
        correct_transfer += (predicted == labels).sum().item()

print(f\"\nAccuracy of Transfer Learning model on test images: {100 * correct_transfer / total_transfer:.2f}%\")
```

### 5.3.2 Generative AI: GANs และ VAEs (แนะนำสั้นๆ)
*   **Generative Adversarial Networks (GANs):** การสร้างข้อมูลใหม่ที่เหมือนจริงผ่านการแข่งขันระหว่าง Generator และ Discriminator
    *   **Use Case:** การสร้างภาพเหมือนจริง, การขยายข้อมูล (Data Augmentation)
*   **Variational Autoencoders (VAEs):** การเรียนรู้การแสดงข้อมูลที่มีประสิทธิภาพและสร้างข้อมูลใหม่จาก Latent Space
    *   **Use Case:** การสร้างภาพ, การลดมิติ, การตรวจจับความผิดปกติ

## สรุปโมดูล 5
โมดูลนี้ได้แนะนำพื้นฐานของ Deep Learning และ PyTorch ซึ่งเป็นเครื่องมือที่ทรงพลังสำหรับการสร้างโมเดล AI ที่ซับซ้อน ผู้เข้าร่วมได้เรียนรู้การทำงานกับ Tensors, การสร้างและฝึก FFNNs และ CNNs สำหรับงานจำแนกประเภทและประมวลผลภาพ นอกจากนี้ยังได้สำรวจเทคนิค Transfer Learning เพื่อใช้ประโยชน์จากโมเดลที่ได้รับการฝึกอบรมล่วงหน้า และทำความเข้าใจแนวคิดเบื้องต้นของ Generative AI เช่น GANs และ VAEs ความรู้เหล่านี้เป็นรากฐานที่สำคัญสำหรับการพัฒนาแอปพลิเคชัน AI ที่ล้ำสมัย
    print(f\"e: {e}\")
    print(f\"e.requires_grad: {e.requires_grad}\") # Should be False
```

## 5.2 การสร้างและฝึกโครงข่ายประสาทเทียม (1.5 ชั่วโมง)

### 5.2.1 วงจรการฝึกมาตรฐาน
*   **การโหลดข้อมูล:** `torch.utils.data.Dataset` และ `DataLoader`
*   **การกำหนดโมเดล:** `torch.nn.Module` สำหรับการสร้างโครงข่ายประสาทเทียม
*   **ฟังก์ชัน Loss:** การหาปริมาณข้อผิดพลาด (`torch.nn.CrossEntropyLoss`, `torch.nn.MSELoss`)
*   **Optimizer:** การอัปเดตน้ำหนักโมเดล (`torch.optim.SGD`, `torch.optim.Adam`)
*   **Forward Pass:** ข้อมูลอินพุตผ่านโมเดล
*   **Backward Pass:** คำนวณ Gradients
*   **Optimizer Step:** อัปเดตน้ำหนัก
*   **Epochs:** การวนซ้ำทั้งชุดข้อมูล

### 5.2.2 Feedforward Neural Networks (FFNNs)
*   **สถาปัตยกรรม:** Input Layer, Hidden Layers, Output Layer
*   **การสร้างด้วย `torch.nn.Sequential` และ `torch.nn.Linear`:** การสร้างที่ง่ายและเป็นโมดูล
*   **การฝึกสำหรับการจำแนกประเภท:** ตัวอย่างกับชุดข้อมูลอย่างง่าย (เช่น MNIST, FashionMNIST)
*   **การฝึกสำหรับ Regression:** ตัวอย่างกับชุดข้อมูลสังเคราะห์
```python
import torch
import torch.nn as nn
import torch.optim as optim
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# 1. Generate synthetic data
X, y = make_classification(n_samples=1000, n_features=20, n_informative=10, n_redundant=10, n_classes=2, random_state=42)

# Scale features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Split data
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

# Convert to PyTorch tensors
X_train_tensor = torch.tensor(X_train, dtype=torch.float32)
y_train_tensor = torch.tensor(y_train, dtype=torch.long) # Long for CrossEntropyLoss
X_test_tensor = torch.tensor(X_test, dtype=torch.float32)
y_test_tensor = torch.tensor(y_test, dtype=torch.long)

# 2. Define the FFNN model
class SimpleFFNN(nn.Module):
    def __init__(self, input_size, hidden_size, num_classes):
        super(SimpleFFNN, self).__init__()
        self.fc1 = nn.Linear(input_size, hidden_size)
        self.relu = nn.ReLU()
        self.fc2 = nn.Linear(hidden_size, num_classes)

    def forward(self, x):
        out = self.fc1(x)
        out = self.relu(out)
        out = self.fc2(out)
        return out

input_size = X_train.shape[1]
hidden_size = 64
num_classes = 2
model = SimpleFFNN(input_size, hidden_size, num_classes)

# 3. Loss and Optimizer
criterion = nn.CrossEntropyLoss()
optimizer = optim.Adam(model.parameters(), lr=0.001)

# 4. Training loop
num_epochs = 100
batch_size = 32

for epoch in range(num_epochs):
    # Shuffle and create mini-batches (simplified for demonstration)
    for i in range(0, len(X_train_tensor), batch_size):
        inputs = X_train_tensor[i:i+batch_size]
        labels = y_train_tensor[i:i+batch_size]

        # Forward pass
        outputs = model(inputs)
        loss = criterion(outputs, labels)

        # Backward and optimize
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

    if (epoch+1) % 10 == 0:
        print (f\"Epoch [{epoch+1}/{num_epochs}], Loss: {loss.item():.4f}\")

# 5. Evaluation
model.eval() # Set model to evaluation mode
with torch.no_grad():
    outputs = model(X_test_tensor)
    _, predicted = torch.max(outputs.data, 1)
    total = y_test_tensor.size(0)
    correct = (predicted == y_test_tensor).sum().item()
    print(f\"\nAccuracy of the model on the test set: {100 * correct / total:.2f}%\")
```

## 5.3 Convolutional Neural Networks (CNNs) สำหรับ Computer Vision (1 ชั่วโมง)

### 5.3.1 บทนำสู่ CNNs
*   **แรงจูงใจ:** ทำไม CNNs ถึงมีประสิทธิภาพสำหรับข้อมูลภาพ
*   **Convolutional Layer:** Filters, Feature Maps, Stride, Padding
*   **Pooling Layer:** Downsampling (Max Pooling, Average Pooling)
*   **Activation Functions:** ReLU เป็นมาตรฐาน
*   **Fully Connected Layers:** สำหรับการจำแนกประเภทในตอนท้าย

### 5.3.2 การสร้าง CNN อย่างง่ายด้วย PyTorch
*   **`torch.nn.Conv2d`:** การกำหนด Convolutional Layers
*   **`torch.nn.MaxPool2d`:** การกำหนด Pooling Layers
*   **ตัวอย่าง:** การจำแนกภาพบนชุดข้อมูลขนาดเล็ก (เช่น CIFAR-10)
```python
import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
from torchvision import datasets, transforms
from torch.utils.data import DataLoader

# 1. Data Loading and Preprocessing (CIFAR-10 example)
transform = transforms.Compose([
    transforms.ToTensor(),
    transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5)) # Normalize image to [-1, 1]
])

train_dataset = datasets.CIFAR10(root=\".\\data\", train=True, download=True, transform=transform)
test_dataset = datasets.CIFAR10(root=\".\\data\", train=False, download=True, transform=transform)

train_loader = DataLoader(train_dataset, batch_size=64, shuffle=True)
test_loader = DataLoader(test_dataset, batch_size=64, shuffle=False)

classes = (
    \"plane\", \"car\", \"bird\", \"cat\", \"deer\", \"dog\", \"frog\", \"horse\", \"ship\", \"truck\"
)

# 2. Define a Simple CNN
class SimpleCNN(nn.Module):
    def __init__(self):
        super(SimpleCNN, self).__init__()
        self.conv1 = nn.Conv2d(3, 6, 5) # 3 input channels (RGB), 6 output channels, 5x5 kernel
        self.pool = nn.MaxPool2d(2, 2) # 2x2 pooling window, stride 2
        self.conv2 = nn.Conv2d(6, 16, 5)
        self.fc1 = nn.Linear(16 * 5 * 5, 120) # 16 feature maps, each 5x5 after pooling
        self.fc2 = nn.Linear(120, 84)
        self.fc3 = nn.Linear(84, 10) # 10 output classes

    def forward(self, x):
        x = self.pool(F.relu(self.conv1(x)))
        x = self.pool(F.relu(self.conv2(x)))
        x = x.view(-1, 16 * 5 * 5) # Flatten the tensor for fully connected layers
        x = F.relu(self.fc1(x))
        x = F.relu(self.fc2(x))
        x = self.fc3(x)
        return x

model_cnn = SimpleCNN()

# 3. Loss and Optimizer
criterion_cnn = nn.CrossEntropyLoss()
optimizer_cnn = optim.SGD(model_cnn.parameters(), lr=0.001, momentum=0.9)

# 4. Training loop
num_epochs_cnn = 5

print(\"\nStarting CNN Training...\")
for epoch in range(num_epochs_cnn):
    running_loss = 0.0
    for i, data in enumerate(train_loader, 0):
        inputs, labels = data

        optimizer_cnn.zero_grad()

        outputs = model_cnn(inputs)
        loss = criterion_cnn(outputs, labels)
        loss.backward()
        optimizer_cnn.step()

        running_loss += loss.item()
        if i % 200 == 199: # Print every 200 mini-batches
            print(f\"Epoch [{epoch + 1}, {i + 1}] loss: {running_loss / 200:.3f}\")
            running_loss = 0.0

print(\"Finished CNN Training.\")

# 5. Evaluation
correct = 0
total = 0
with torch.no_grad():
    for data in test_loader:
        images, labels = data
        outputs = model_cnn(images)
        _, predicted = torch.max(outputs.data, 1)
        total += labels.size(0)
        correct += (predicted == labels).sum().item()

print(f\"Accuracy of the CNN on the 10000 test images: {100 * correct / total:.2f}%\")
```

### 5.3.3 Transfer Learning
*   **แนวคิด:** การนำโมเดลที่ได้รับการฝึกอบรมล่วงหน้า (เช่น ResNet, VGG) บนชุดข้อมูลขนาดใหญ่ (เช่น ImageNet) มาใช้เป็นจุดเริ่มต้นสำหรับงานใหม่
*   **Fine-tuning:** การปรับเปลี่ยนเลเยอร์สุดท้ายของโมเดลที่ได้รับการฝึกอบรมล่วงหน้า
*   **Feature Extraction:** การใช้โมเดลที่ได้รับการฝึกอบรมล่วงหน้าเป็นตัวดึง Feature แบบคงที่
*   **กรณีการใช้งาน:** เร่งการฝึก, ปรับปรุงประสิทธิภาพบนชุดข้อมูลขนาดเล็ก

## 5.4 แนวคิด Deep Learning ขั้นสูง (0.5 ชั่วโมง)

### 5.4.1 Recurrent Neural Networks (RNNs) (โดยย่อ)
*   **แนวคิด:** โครงข่ายที่ออกแบบมาสำหรับข้อมูลลำดับ (Sequential Data) เช่น ข้อความ, อนุกรมเวลา
*   **ปัญหา:** Vanishing/Exploding Gradients
*   **Variants:** LSTM (Long Short-Term Memory), GRU (Gated Recurrent Unit) เพื่อแก้ไขปัญหา
*   **แอปพลิเคชัน:** Natural Language Processing (NLP), Speech Recognition

### 5.4.2 Generative Models (โดยย่อ)
*   **Generative Adversarial Networks (GANs):** การสร้างข้อมูลใหม่ที่เหมือนจริงผ่านการแข่งขันระหว่าง Generator และ Discriminator
    *   **กรณีการใช้งาน:** การสร้างภาพเหมือนจริง, การขยายข้อมูล (Data Augmentation)
*   **Variational Autoencoders (VAEs):** การเรียนรู้การแสดงข้อมูลที่มีประสิทธิภาพและสร้างข้อมูลใหม่จาก Latent Space
    *   **กรณีการใช้งาน:** การสร้างภาพ, การลดมิติ, การตรวจจับความผิดปกติ

### 5.4.3 Attention Mechanisms และ Transformers (โดยย่อ)
*   **แนวคิด:** การมุ่งเน้นไปที่ส่วนที่เกี่ยวข้องของลำดับอินพุต
*   **Transformers:** สถาปัตยกรรมที่ปฏิวัติ NLP (เช่น BERT, GPT)
*   **Self-Attention:** ส่วนประกอบสำคัญของ Transformers

## แบบฝึกหัดสำหรับโมดูล 5

### แบบฝึกหัด 5.1: การดำเนินการ PyTorch Tensor และ Autograd
**สถานการณ์:** คุณกำลังทำงานกับชุดข้อมูลขนาดเล็กของการอ่านค่าเซ็นเซอร์และจำเป็นต้องดำเนินการจัดการ Tensor พื้นฐานและทำความเข้าใจวิธีการคำนวณ Gradients

**งาน:**
1.  สร้าง PyTorch Tensor `data_tensor` ที่มีรูปร่าง `(3, 4)` พร้อมค่าจำนวนเต็มสุ่มระหว่าง 1 ถึง 10 ตรวจสอบให้แน่ใจว่าต้องการ Gradients
2.  ดำเนินการดังต่อไปนี้:
    *   คำนวณค่ากำลังสองแบบ Element-wise ของ `data_tensor`
    *   คำนวณผลรวมของ Element ทั้งหมดใน Tensor ที่ยกกำลังสอง
    *   ดำเนินการคูณเมทริกซ์กับ Tensor อื่น `weights_tensor` ที่มีรูปร่าง `(4, 2)` (ค่าสุ่ม ไม่ต้องใช้ Grad)
3.  คำนวณ Gradients ของผลรวมสุดท้ายเทียบกับ `data_tensor`
4.  สาธิตวิธีการปิดใช้งานการติดตาม Gradient ชั่วคราวสำหรับการดำเนินการเฉพาะ

### แบบฝึกหัด 5.2: การสร้างและฝึก Feedforward Neural Network
**สถานการณ์:** คุณต้องจำแนกชุดข้อมูลสังเคราะห์โดยใช้ Feedforward Neural Network อย่างง่าย

**งาน:**
1.  สร้างชุดข้อมูลการจำแนกประเภทไบนารีสังเคราะห์โดยใช้ `sklearn.datasets.make_moons` ที่มี 1000 ตัวอย่าง, `noise=0.1` และ `random_state=42`
2.  แบ่งข้อมูลออกเป็นชุดฝึกและชุดทดสอบ (แบ่ง 80/20)
3.  แปลงข้อมูลเป็น PyTorch Tensors
4.  กำหนดโมเดล FFNN อย่างง่ายโดยใช้ `torch.nn.Module` ด้วย:
    *   Input Layer ที่ตรงกับจำนวน Features
    *   Hidden Layer หนึ่งชั้นที่มี 64 Neurons และ ReLU Activation
    *   Output Layer หนึ่งชั้นที่มี 1 Neuron (สำหรับการจำแนกประเภทไบนารี ตามด้วย Sigmoid ใน Loss หรือ Prediction)
5.  กำหนด `BCEWithLogitsLoss` เป็นฟังก์ชัน Loss และ `Adam` เป็น Optimizer

### แบบฝึกหัด 5.3: การสร้างและฝึก Convolutional Neural Network (CNN)
**สถานการณ์:** คุณต้องการสร้าง CNN เพื่อจำแนกภาพจากชุดข้อมูลขนาดเล็ก

**งาน:**
1.  โหลดชุดข้อมูล CIFAR-10 โดยใช้ `torchvision.datasets`
2.  กำหนด CNN อย่างง่ายโดยใช้ `torch.nn.Module` ที่มี:
    *   Convolutional Layers สองชั้น ตามด้วย ReLU และ Max Pooling
    *   Fully Connected Layers สองชั้น
3.  กำหนด `CrossEntropyLoss` เป็นฟังก์ชัน Loss และ `SGD` เป็น Optimizer
4.  ฝึกโมเดลเป็นเวลา 5 Epochs
5.  ประเมินความแม่นยำของโมเดลบนชุดทดสอบ

### แบบฝึกหัด 5.4: Transfer Learning สำหรับ Image Classification
**สถานการณ์:** คุณมีชุดข้อมูลภาพขนาดเล็กและต้องการใช้ประโยชน์จากโมเดลที่ได้รับการฝึกอบรมล่วงหน้าเพื่อปรับปรุงประสิทธิภาพ

**งาน:**
1.  โหลดโมเดล ResNet18 ที่ได้รับการฝึกอบรมล่วงหน้าจาก `torchvision.models`
2.  ตรึงพารามิเตอร์ทั้งหมดของโมเดลที่ได้รับการฝึกอบรมล่วงหน้า
3.  แทนที่ Output Layer สุดท้ายด้วย Linear Layer ใหม่ที่ตรงกับจำนวนคลาสในชุดข้อมูลของคุณ (สมมติว่า 10 คลาส)
4.  ฝึกเฉพาะ Output Layer ใหม่เป็นเวลา 3 Epochs โดยใช้ชุดข้อมูล MNIST (แปลงเป็น 3 ช่องสัญญาณเพื่อจำลองข้อมูลภาพ)
5.  ประเมินความแม่นยำของโมเดลบนชุดทดสอบ

## เฉลยสำหรับโมดูล 5

### เฉลย 5.1: การดำเนินการ PyTorch Tensor และ Autograd
```python
import torch

# 1. Create a PyTorch tensor data_tensor
data_tensor = torch.randint(1, 11, (3, 4), dtype=torch.float32, requires_grad=True)
print(f\"Original data_tensor:\n{data_tensor}\")

# 2. Perform operations
squared_tensor = data_tensor**2
print(f\"\nSquared tensor:\n{squared_tensor}\")

sum_squared = torch.sum(squared_tensor)
print(f\"\nSum of squared elements: {sum_squared}\")

weights_tensor = torch.rand(4, 2) # No grad required for weights
matrix_mult_result = data_tensor.matmul(weights_tensor)
print(f\"\nMatrix multiplication result:\n{matrix_mult_result}\")

# 3. Compute gradients of the final sum with respect to data_tensor
sum_squared.backward()
print(f\"\nGradient of sum_squared with respect to data_tensor:\n{data_tensor.grad}\")

# 4. Demonstrate how to temporarily disable gradient tracking
print(\"\n--- Demonstrating torch.no_grad() ---\")
with torch.no_grad():
    new_op_result = data_tensor * 2
    print(f\"Result of operation in no_grad context:\n{new_op_result}\")
    print(f\"Requires grad for new_op_result: {new_op_result.requires_grad}\")

# Note: data_tensor.grad remains the same as no new backward pass was performed on it
print(f\"data_tensor.grad after no_grad context (unchanged):\n{data_tensor.grad}\")
```

### เฉลย 5.2: การสร้างและฝึก Feedforward Neural Network
```python
import torch
import torch.nn as nn
import torch.optim as optim
from sklearn.datasets import make_moons
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from torch.utils.data import DataLoader, TensorDataset

# 1. Generate synthetic binary classification dataset
X, y = make_moons(n_samples=1000, noise=0.1, random_state=42)

# 2. Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Scale features (important for neural networks)
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# 3. Convert the data to PyTorch tensors
X_train_tensor = torch.tensor(X_train_scaled, dtype=torch.float32)
y_train_tensor = torch.tensor(y_train, dtype=torch.float32).unsqueeze(1) # Unsqueeze for BCEWithLogitsLoss
X_test_tensor = torch.tensor(X_test_scaled, dtype=torch.float32)
y_test_tensor = torch.tensor(y_test, dtype=torch.float32).unsqueeze(1)

# Create DataLoader
train_dataset = TensorDataset(X_train_tensor, y_train_tensor)
train_loader = DataLoader(train_dataset, batch_size=32, shuffle=True)

# 4. Define a simple FFNN model
class SimpleFFNN(nn.Module):
    def __init__(self, input_size, hidden_size, output_size):
        super(SimpleFFNN, self).__init__()
        self.fc1 = nn.Linear(input_size, hidden_size)
        self.relu = nn.ReLU()
        self.fc2 = nn.Linear(hidden_size, output_size)

    def forward(self, x):
        out = self.fc1(x)
        out = self.relu(out)
        out = self.fc2(out)
        return out

input_size = X_train.shape[1] # 2 features
hidden_size = 64
output_size = 1 # For binary classification
model = SimpleFFNN(input_size, hidden_size, output_size)

# 5. Define BCEWithLogitsLoss as the loss function and Adam as the optimizer
criterion = nn.BCEWithLogitsLoss() # Combines Sigmoid and BCELoss for numerical stability
optimizer = optim.Adam(model.parameters(), lr=0.01)

# Training loop
num_epochs = 100
for epoch in range(num_epochs):
    for inputs, labels in train_loader:
        optimizer.zero_grad()
        outputs = model(inputs)
        loss = criterion(outputs, labels)
        loss.backward()
        optimizer.step()

    if (epoch + 1) % 10 == 0:
        print(f\"Epoch [{epoch+1}/{num_epochs}], Loss: {loss.item():.4f}\")

# Evaluation
model.eval()
with torch.no_grad():
    outputs = model(X_test_tensor)
    predicted = (torch.sigmoid(outputs) > 0.5).float() # Apply sigmoid and threshold
    accuracy = (predicted == y_test_tensor).float().mean()
    print(f\"\nAccuracy of the FFNN on the test set: {accuracy.item():.4f}\")
```

### เฉลย 5.3: การสร้างและฝึก Convolutional Neural Network (CNN)
```python
import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
from torchvision import datasets, transforms
from torch.utils.data import DataLoader

# 1. Load the CIFAR-10 dataset
transform = transforms.Compose([
    transforms.ToTensor(),
    transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))
])

train_dataset = datasets.CIFAR10(root=\".\\data\", train=True, download=True, transform=transform)
test_dataset = datasets.CIFAR10(root=\".\\data\", train=False, download=True, transform=transform)

train_loader = DataLoader(train_dataset, batch_size=64, shuffle=True)
test_loader = DataLoader(test_dataset, batch_size=64, shuffle=False)

# 2. Define a simple CNN
class SimpleCNN(nn.Module):
    def __init__(self):
        super(SimpleCNN, self).__init__()
        self.conv1 = nn.Conv2d(3, 6, 5) # 3 input channels (RGB), 6 output channels, 5x5 kernel
        self.pool = nn.MaxPool2d(2, 2) # 2x2 pooling window, stride 2
        self.conv2 = nn.Conv2d(6, 16, 5)
        self.fc1 = nn.Linear(16 * 5 * 5, 120)
        self.fc2 = nn.Linear(120, 84)
        self.fc3 = nn.Linear(84, 10) # 10 output classes for CIFAR-10

    def forward(self, x):
        x = self.pool(F.relu(self.conv1(x)))
        x = self.pool(F.relu(self.conv2(x)))
        x = x.view(-1, 16 * 5 * 5)
        x = F.relu(self.fc1(x))
        x = F.relu(self.fc2(x))
        x = self.fc3(x)
        return x

model_cnn = SimpleCNN()

# 3. Define CrossEntropyLoss as the loss function and SGD as the optimizer
criterion_cnn = nn.CrossEntropyLoss()
optimizer_cnn = optim.SGD(model_cnn.parameters(), lr=0.001, momentum=0.9)

# 4. Train the model for 5 Epochs
num_epochs_cnn = 5

print(\"\nStarting CNN Training...\")
for epoch in range(num_epochs_cnn):
    running_loss = 0.0
    for i, data in enumerate(train_loader, 0):
        inputs, labels = data

        optimizer_cnn.zero_grad()

        outputs = model_cnn(inputs)
        loss = criterion_cnn(outputs, labels)
        loss.backward()
        optimizer_cnn.step()

        running_loss += loss.item()
        if i % 200 == 199: # Print every 200 mini-batches
            print(f\"Epoch [{epoch + 1}, {i + 1}] loss: {running_loss / 200:.3f}\")
            running_loss = 0.0

print(\"Finished CNN Training.\")

# 5. Evaluate the model accuracy on the test set
model_cnn.eval()
correct = 0
total = 0
with torch.no_grad():
    for data in test_loader:
        images, labels = data
        outputs = model_cnn(images)
        _, predicted = torch.max(outputs.data, 1)
        total += labels.size(0)
        correct += (predicted == labels).sum().item()

print(f\"Accuracy of the CNN on the 10000 test images: {100 * correct / total:.2f}%\")
```

### เฉลย 5.4: Transfer Learning สำหรับ Image Classification
```python
import torch
import torch.nn as nn
import torch.optim as optim
from torchvision import models, transforms, datasets
from torch.utils.data import DataLoader

# 1. Data Loading and Preprocessing for a custom dataset (e.g., small image dataset)
# For demonstration, we\'ll use a subset of MNIST and pretend it\'s a new dataset
# In a real scenario, you\'d load your own custom image dataset

transform_transfer = transforms.Compose([
    transforms.Resize(224), # ResNet expects 224x224 input
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]) # ImageNet normalization
])

# Using MNIST as a dummy custom dataset (will convert to 3 channels)
class MNIST3Channel(datasets.MNIST):
    def __getitem__(self, index):
        img, target = super().__getitem__(index)
        return img.repeat(3, 1, 1), target # Convert to 3 channels

train_dataset_transfer = MNIST3Channel(\".\\data\", train=True, download=True, transform=transform_transfer)
test_dataset_transfer = MNIST3Channel(\".\\data\", train=False, download=True, transform=transform_transfer)

# Reduce dataset size for faster demonstration
train_dataset_transfer.data = train_dataset_transfer.data[:1000]
train_dataset_transfer.targets = train_dataset_transfer.targets[:1000]
test_dataset_transfer.data = test_dataset_transfer.data[:200]
test_dataset_transfer.targets = test_dataset_transfer.targets[:200]

train_loader_transfer = DataLoader(train_dataset_transfer, batch_size=32, shuffle=True)
test_loader_transfer = DataLoader(test_dataset_transfer, batch_size=32, shuffle=False)

# 2. Load a pre-trained model (e.g., ResNet18)
model_ft = models.resnet18(pretrained=True)

# Freeze all parameters in the network
for param in model_ft.parameters():
    param.requires_grad = False

# Replace the last fully connected layer with a new one for our number of classes (10 for MNIST)
num_ftrs = model_ft.fc.in_features
model_ft.fc = nn.Linear(num_ftrs, 10) # 10 classes for MNIST

# Move model to GPU if available
device = torch.device(\"cuda:0\" if torch.cuda.is_available() else \"cpu\")
model_ft = model_ft.to(device)

# 3. Loss Function and Optimizer (only optimizing the new fc layer)
criterion_transfer = nn.CrossEntropyLoss()
optimizer_transfer = optim.Adam(model_ft.fc.parameters(), lr=0.001)

# 4. Training the Model (Feature Extraction)
num_epochs_transfer = 3
for epoch in range(num_epochs_transfer):
    model_ft.train()
    running_loss = 0.0
    for inputs, labels in train_loader_transfer:
        inputs, labels = inputs.to(device), labels.to(device)

        optimizer_transfer.zero_grad()
        outputs = model_ft(inputs)
        loss = criterion_transfer(outputs, labels)
        loss.backward()
        optimizer_transfer.step()
        running_loss += loss.item() * inputs.size(0)
    epoch_loss = running_loss / len(train_dataset_transfer)
    print(f\"Transfer Learning Epoch {epoch+1}/{num_epochs_transfer}, Loss: {epoch_loss:.4f}\")

# 5. Evaluating the Model
model_ft.eval()
correct_transfer = 0
total_transfer = 0
with torch.no_grad():
    for inputs, labels in test_loader_transfer:
        inputs, labels = inputs.to(device), labels.to(device)
        outputs = model_ft(inputs)
        _, predicted = torch.max(outputs.data, 1)
        total_transfer += labels.size(0)
        correct_transfer += (predicted == labels).sum().item()

print(f\"\nAccuracy of Transfer Learning model on test images: {100 * correct_transfer / total_transfer:.2f}%\")
```

### เฉลย 5.3: การสร้างและฝึก Convolutional Neural Network (CNN)
```python
import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
from torchvision import datasets, transforms
from torch.utils.data import DataLoader

# 1. Load the FashionMNIST dataset
transform = transforms.Compose([
    transforms.ToTensor(),
    transforms.Normalize((0.5,), (0.5,)) # Normalize to [-1, 1] for grayscale images
])

train_dataset = datasets.FashionMNIST(root=\".\\data\", train=True, download=True, transform=transform)
test_dataset = datasets.FashionMNIST(root=\".\\data\", train=False, download=True, transform=transform)

train_loader = DataLoader(train_dataset, batch_size=64, shuffle=True)
test_loader = DataLoader(test_dataset, batch_size=64, shuffle=False)

# 2. Define a simple CNN model
class FashionCNN(nn.Module):
    def __init__(self):
        super(FashionCNN, self).__init__()
        self.conv1 = nn.Conv2d(1, 16, kernel_size=3, padding=1) # Input channel 1 (grayscale), 16 output channels
        self.pool = nn.MaxPool2d(2, 2)
        self.conv2 = nn.Conv2d(16, 32, kernel_size=3, padding=1)
        self.fc1 = nn.Linear(32 * 7 * 7, 128) # After two pooling layers, 28x28 -> 14x14 -> 7x7
        self.fc2 = nn.Linear(128, 10) # 10 output classes for FashionMNIST

    def forward(self, x):
        x = self.pool(F.relu(self.conv1(x)))
        x = self.pool(F.relu(self.conv2(x)))
        x = x.view(-1, 32 * 7 * 7) # Flatten for fully connected layers
        x = F.relu(self.fc1(x))
        x = self.fc2(x)
        return x

model_fashion_cnn = FashionCNN()

# 3. Define CrossEntropyLoss and Adam optimizer
criterion_fashion = nn.CrossEntropyLoss()
optimizer_fashion = optim.Adam(model_fashion_cnn.parameters(), lr=0.001)

# 4. Train the CNN for 5 epochs
num_epochs_fashion = 5

print(\"\nStarting FashionMNIST CNN Training...\")
for epoch in range(num_epochs_fashion):
    running_loss = 0.0
    for i, data in enumerate(train_loader, 0):
        inputs, labels = data

        optimizer_fashion.zero_grad()

        outputs = model_fashion_cnn(inputs)
        loss = criterion_fashion(outputs, labels)
        loss.backward()
        optimizer_fashion.step()

        running_loss += loss.item()
        if i % 200 == 199: # Print every 200 mini-batches
            print(f\"Epoch [{epoch + 1}, {i + 1}] loss: {running_loss / 200:.3f}\")
            running_loss = 0.0

print(\"Finished FashionMNIST CNN Training.\")

# 5. Evaluate the model accuracy on the test set
model_fashion_cnn.eval()
correct = 0
total = 0
with torch.no_grad():
    for data in test_loader:
        images, labels = data
        outputs = model_fashion_cnn(images)
        _, predicted = torch.max(outputs.data, 1)
        total += labels.size(0)
        correct += (predicted == labels).sum().item()

print(f\"Accuracy of the FashionMNIST CNN on the 10000 test images: {100 * correct / total:.2f}%\")
```

### เฉลย 5.4: Transfer Learning สำหรับ Image Classification
```python
import torch
import torch.nn as nn
import torch.optim as optim
from torchvision import models, transforms
from torch.utils.data import Dataset, DataLoader
import random

# 4. Define a dummy CatDogDataset
class DummyCatDogDataset(Dataset):
    def __init__(self, num_samples=100, transform=None):
        self.num_samples = num_samples
        self.transform = transform
        # Simulate 224x224 RGB images
        self.data = [torch.randn(3, 224, 224) for _ in range(num_samples)]
        # 0 for cat, 1 for dog
        self.labels = [random.randint(0, 1) for _ in range(num_samples)]

    def __len__(self):
        return self.num_samples

    def __getitem__(self, idx):
        img = self.data[idx]
        label = self.labels[idx]
        if self.transform:
            img = self.transform(img)
        return img, label

# Transformations for ResNet
transform_resnet = transforms.Compose([
    transforms.Resize(224),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
])

# Create dummy datasets and loaders
train_dataset_catdog = DummyCatDogDataset(num_samples=200, transform=transform_resnet)
test_dataset_catdog = DummyCatDogDataset(num_samples=50, transform=transform_resnet)

train_loader_catdog = DataLoader(train_dataset_catdog, batch_size=16, shuffle=True)
test_loader_catdog = DataLoader(test_dataset_catdog, batch_size=16, shuffle=False)

# 1. Load a pre-trained ResNet18 model
model_resnet = models.resnet18(pretrained=True)

# 2. Freeze all parameters in the feature extractor part of the model
for param in model_resnet.parameters():
    param.requires_grad = False

# 3. Replace the final fully connected layer to output 2 classes (cat/dog)
num_ftrs_resnet = model_resnet.fc.in_features
model_resnet.fc = nn.Linear(num_ftrs_resnet, 2) # 2 classes: cat or dog

# Move model to GPU if available
device = torch.device(\"cuda:0\" if torch.cuda.is_available() else \"cpu\")
model_resnet = model_resnet.to(device)

# 5. Define CrossEntropyLoss and Adam optimizer (only optimizing the new final layer)
criterion_resnet = nn.CrossEntropyLoss()
optimizer_resnet = optim.Adam(model_resnet.fc.parameters(), lr=0.001)

# 6. Train the modified model for a few epochs
num_epochs_resnet = 5

print(\"\nStarting Transfer Learning (ResNet) Training...\")
for epoch in range(num_epochs_resnet):
    model_resnet.train()
    running_loss = 0.0
    for inputs, labels in train_loader_catdog:
        inputs, labels = inputs.to(device), labels.to(device)

        optimizer_resnet.zero_grad()
        outputs = model_resnet(inputs)
        loss = criterion_resnet(outputs, labels)
        loss.backward()
        optimizer_resnet.step()
        running_loss += loss.item() * inputs.size(0)
    epoch_loss = running_loss / len(train_dataset_catdog)
    print(f\"Transfer Learning Epoch {epoch+1}/{num_epochs_resnet}, Loss: {epoch_loss:.4f}\")

# 7. Evaluate the model on a test set
model_resnet.eval()
correct_resnet = 0
total_resnet = 0
with torch.no_grad():
    for inputs, labels in test_loader_catdog:
        inputs, labels = inputs.to(device), labels.to(device)
        outputs = model_resnet(inputs)
        _, predicted = torch.max(outputs.data, 1)
        total_resnet += labels.size(0)
        correct_resnet += (predicted == labels).sum().item()

print(f\"\nAccuracy of Transfer Learning (ResNet) model on test images: {100 * correct_resnet / total_resnet:.2f}%\")
```

### เฉลย 5.5: การสำรวจโมเดล Generative อย่างง่าย (แนวคิด VAE)
```python
import torch
import torch.nn as nn
import torch.optim as optim
from torchvision import datasets, transforms
from torch.utils.data import DataLoader

# 1. Data Loading and Preprocessing (Flattened MNIST)
transform_ae = transforms.Compose([
    transforms.ToTensor(),
    transforms.Normalize((0.1307,), (0.3081,)),
    transforms.Lambda(lambda x: x.view(-1)) # Flatten the image
])

train_dataset_ae = datasets.MNIST(\".\\data\", train=True, download=True, transform=transform_ae)
train_loader_ae = DataLoader(train_dataset_ae, batch_size=64, shuffle=True)

# 1. Define Encoder and Decoder classes
class Encoder(nn.Module):
    def __init__(self, input_dim, hidden_dim, latent_dim):
        super(Encoder, self).__init__()
        self.fc1 = nn.Linear(input_dim, hidden_dim)
        self.relu = nn.ReLU()
        self.fc2 = nn.Linear(hidden_dim, latent_dim) # Output latent representation

    def forward(self, x):
        h = self.relu(self.fc1(x))
        return self.fc2(h)

class Decoder(nn.Module):
    def __init__(self, latent_dim, hidden_dim, output_dim):
        super(Decoder, self).__init__()
        self.fc1 = nn.Linear(latent_dim, hidden_dim)
        self.relu = nn.ReLU()
        self.fc2 = nn.Linear(hidden_dim, output_dim) # Reconstruct input
        self.sigmoid = nn.Sigmoid() # Output pixel values between 0 and 1

    def forward(self, z):
        h = self.relu(self.fc1(z))
        return self.sigmoid(self.fc2(h))

# 2. Combine them into an Autoencoder class
class Autoencoder(nn.Module):
    def __init__(self, input_dim, hidden_dim, latent_dim):
        super(Autoencoder, self).__init__()
        self.encoder = Encoder(input_dim, hidden_dim, latent_dim)
        self.decoder = Decoder(latent_dim, hidden_dim, input_dim)

    def forward(self, x):
        latent = self.encoder(x)
        reconstructed = self.decoder(latent)
        return reconstructed

# Model parameters
input_dim = 28 * 28 # For MNIST images
hidden_dim = 256
latent_dim = 20 # Compressed representation size

model_ae = Autoencoder(input_dim, hidden_dim, latent_dim)

# 3. Use MSELoss as the reconstruction loss
criterion_ae = nn.MSELoss()
optimizer_ae = optim.Adam(model_ae.parameters(), lr=0.001)

# 4. Train the autoencoder
num_epochs_ae = 10

print(\"\nStarting Autoencoder Training...\")
for epoch in range(num_epochs_ae):
    for batch_idx, (data, _) in enumerate(train_loader_ae):
        # data is already flattened by the transform
        optimizer_ae.zero_grad()
        reconstruction = model_ae(data)
        loss = criterion_ae(reconstruction, data) # Compare reconstruction with original data
        loss.backward()
        optimizer_ae.step()

    print(f\"Epoch [{epoch+1}/{num_epochs_ae}], Loss: {loss.item():.4f}\")

print(\"Finished Autoencoder Training.\")

# Optional: Visualize reconstruction (requires matplotlib and more setup)
# For simplicity, we just train and observe loss decrease.
```

# โมดูล 6: การปรับใช้และผู้ช่วยเขียนโค้ด AI สำหรับ AI สมัยใหม่ (4 ชั่วโมง)

## ภาพรวม
โมดูลนี้มุ่งเน้นไปที่ขั้นตอนสุดท้ายที่สำคัญของวงจรการพัฒนา AI: การปรับใช้โมเดลเข้าสู่การผลิตและการใช้ประโยชน์จากผู้ช่วยเขียนโค้ด AI เพื่อเพิ่มประสิทธิภาพการทำงาน เราจะสำรวจกลยุทธ์การปรับใช้ที่ทันสมัย การใช้คอนเทนเนอร์ด้วย Docker และแนวทางปฏิบัติในการรวมโมเดล AI เข้ากับแอปพลิเคชัน นอกจากนี้ เราจะเจาะลึกเทคนิคขั้นสูงสำหรับการใช้ผู้ช่วยเขียนโค้ด AI อย่างมีประสิทธิภาพ รวมถึง Prompt Engineering สำหรับการสร้างโค้ด การปรับโครงสร้างโค้ด และการดีบัก และแนะนำแนวคิดของ AI Agents สำหรับเวิร์กโฟลว์การพัฒนาแบบอัตโนมัติ

## วัตถุประสงค์การเรียนรู้
เมื่อจบโมดูลนี้ ผู้เข้าร่วมจะสามารถ:
*   เข้าใจกลยุทธ์ต่างๆ สำหรับการปรับใช้โมเดล AI ตั้งแต่ API อย่างง่ายไปจนถึง Serverless Functions
*   สร้างคอนเทนเนอร์แอปพลิเคชัน AI โดยใช้ Docker เพื่อสภาพแวดล้อมที่สอดคล้องกันและทำซ้ำได้
*   สร้างและปรับใช้ RESTful APIs สำหรับโมเดล AI โดยใช้ FastAPI
*   สร้างเว็บแอปพลิเคชันแบบโต้ตอบสำหรับโมเดล AI โดยใช้ Streamlit
*   เชี่ยวชาญเทคนิคขั้นสูงสำหรับการใช้ผู้ช่วยเขียนโค้ด AI (เช่น GitHub Copilot, Cursor) สำหรับการสร้างโค้ด การปรับโครงสร้างโค้ด และการดีบัก
*   ประยุกต์ใช้หลักการ Prompt Engineering เพื่อเพิ่มประโยชน์สูงสุดของผู้ช่วยเขียนโค้ด AI
*   เข้าใจสาขาที่กำลังเกิดขึ้นของ AI Agents และศักยภาพในการทำงานอัตโนมัติของงานพัฒนา
*   นำแนวทางปฏิบัติที่ดีที่สุดสำหรับโครงสร้างโปรเจกต์และการควบคุมเวอร์ชันในโปรเจกต์ AI ไปใช้

## 6.1 กลยุทธ์การปรับใช้โมเดล AI สมัยใหม่ (1 ชั่วโมง)

### 6.1.1 บทนำสู่ MLOps
*   **แนวคิด:** การเชื่อมช่องว่างระหว่างการพัฒนา ML และการดำเนินงาน
*   **เสาหลักสำคัญ:** การทดลอง, การจัดการข้อมูล, การฝึกโมเดล, การควบคุมเวอร์ชัน, การปรับใช้, การตรวจสอบ

### 6.1.2 ตัวเลือกการปรับใช้
*   **RESTful APIs:** การเปิดเผยโมเดลเป็นบริการเว็บ
    *   **ข้อดี:** ไม่ขึ้นกับภาษา, ปรับขนาดได้, เป็นที่ยอมรับอย่างกว้างขวาง
    *   **ข้อเสีย:** ต้องมีการจัดการเซิร์ฟเวอร์
*   **Serverless Functions (เช่น AWS Lambda, Google Cloud Functions):** ขับเคลื่อนด้วยเหตุการณ์, จ่ายตามการใช้งาน
    *   **ข้อดี:** ปรับขนาดอัตโนมัติ, คุ้มค่าสำหรับปริมาณงานที่ไม่ต่อเนื่อง
    *   **ข้อเสีย:** Cold Starts, การผูกติดกับผู้ให้บริการ
*   **Edge Deployment:** การปรับใช้โมเดลโดยตรงบนอุปกรณ์ (เช่น มือถือ, IoT)
    *   **ข้อดี:** Latency ต่ำ, ความสามารถในการทำงานแบบออฟไลน์, ความเป็นส่วนตัว
    *   **ข้อเสีย:** ข้อจำกัดด้านทรัพยากร, ต้องมีการปรับแต่งโมเดล
*   **Batch Prediction:** การประมวลผลชุดข้อมูลขนาดใหญ่ออฟไลน์
    *   **ข้อดี:** เหมาะสำหรับงานที่ต้องการการประมวลผลจำนวนมาก, ไม่ต้องการการตอบสนองแบบเรียลไทม์
    *   **ข้อเสีย:** ไม่เหมาะสำหรับแอปพลิเคชันที่ต้องการการตอบสนองทันที

### เฉลย 5.5: การสำรวจโมเดล Generative อย่างง่าย (แนวคิด VAE)
```python
import torch
import torch.nn as nn
import torch.optim as optim
from torchvision import datasets, transforms
from torch.utils.data import DataLoader

# 1. Data Loading and Preprocessing (Flattened MNIST)
transform_ae = transforms.Compose([
    transforms.ToTensor(),
    transforms.Normalize((0.1307,), (0.3081,)),
    transforms.Lambda(lambda x: x.view(-1)) # Flatten the image
])

train_dataset_ae = datasets.MNIST(\".\\data\", train=True, download=True, transform=transform_ae)
train_loader_ae = DataLoader(train_dataset_ae, batch_size=64, shuffle=True)

# 1. Define Encoder and Decoder classes
class Encoder(nn.Module):
    def __init__(self, input_dim, hidden_dim, latent_dim):
        super(Encoder, self).__init__()
        self.fc1 = nn.Linear(input_dim, hidden_dim)
        self.relu = nn.ReLU()
        self.fc2 = nn.Linear(hidden_dim, latent_dim) # Output latent representation

    def forward(self, x):
        h = self.relu(self.fc1(x))
        return self.fc2(h)

class Decoder(nn.Module):
    def __init__(self, latent_dim, hidden_dim, output_dim):
        super(Decoder, self).__init__()
        self.fc1 = nn.Linear(latent_dim, hidden_dim)
        self.relu = nn.ReLU()
        self.fc2 = nn.Linear(hidden_dim, output_dim) # Reconstruct input
        self.sigmoid = nn.Sigmoid() # Output pixel values between 0 and 1

    def forward(self, z):
        h = self.relu(self.fc1(z))
        return self.sigmoid(self.fc2(h))

# 2. Combine them into an Autoencoder class
class Autoencoder(nn.Module):
    def __init__(self, input_dim, hidden_dim, latent_dim):
        super(Autoencoder, self).__init__()
        self.encoder = Encoder(input_dim, hidden_dim, latent_dim)
        self.decoder = Decoder(latent_dim, hidden_dim, input_dim)

    def forward(self, x):
        latent = self.encoder(x)
        reconstructed = self.decoder(latent)
        return reconstructed

# Model parameters
input_dim = 28 * 28 # For MNIST images
hidden_dim = 256
latent_dim = 20 # Compressed representation size

model_ae = Autoencoder(input_dim, hidden_dim, latent_dim)

# 3. Use MSELoss as the reconstruction loss
criterion_ae = nn.MSELoss()
optimizer_ae = optim.Adam(model_ae.parameters(), lr=0.001)

# 4. Train the autoencoder
num_epochs_ae = 10

print(\"\nStarting Autoencoder Training...\")
for epoch in range(num_epochs_ae):
    for batch_idx, (data, _) in enumerate(train_loader_ae):
        # data is already flattened by the transform
        optimizer_ae.zero_grad()
        reconstruction = model_ae(data)
        loss = criterion_ae(reconstruction, data) # Compare reconstruction with original data
        loss.backward()
        optimizer_ae.step()

    print(f\"Epoch [{epoch+1}/{num_epochs_ae}], Loss: {loss.item():.4f}\")

print(\"Finished Autoencoder Training.\")

# Optional: Visualize reconstruction (requires matplotlib and more setup)
# For simplicity, we just train and observe loss decrease.
```

## สรุปโมดูล 5
โมดูลนี้ได้แนะนำพื้นฐานของ Deep Learning และ PyTorch ซึ่งเป็นเครื่องมือที่ทรงพลังสำหรับการสร้างโมเดล AI ที่ซับซ้อน ผู้เข้าร่วมได้เรียนรู้การทำงานกับ Tensors, การสร้างและฝึก FFNNs และ CNNs สำหรับงานจำแนกประเภทและประมวลผลภาพ นอกจากนี้ยังได้สำรวจเทคนิค Transfer Learning เพื่อใช้ประโยชน์จากโมเดลที่ได้รับการฝึกอบรมล่วงหน้า และทำความเข้าใจแนวคิดเบื้องต้นของ Generative AI เช่น GANs และ VAEs ความรู้เหล่านี้เป็นรากฐานที่สำคัญสำหรับการพัฒนาแอปพลิเคชัน AI ที่ล้ำสมัย

# โมดูล 6: การปรับใช้และผู้ช่วยเขียนโค้ด AI สำหรับ AI สมัยใหม่ (4 ชั่วโมง)

## ภาพรวม
โมดูลนี้มุ่งเน้นไปที่ขั้นตอนสุดท้ายที่สำคัญของวงจรการพัฒนา AI: การปรับใช้โมเดลเข้าสู่การผลิตและการใช้ประโยชน์จากผู้ช่วยเขียนโค้ด AI เพื่อเพิ่มประสิทธิภาพการทำงาน เราจะสำรวจกลยุทธ์การปรับใช้ที่ทันสมัย การใช้คอนเทนเนอร์ด้วย Docker และแนวทางปฏิบัติในการรวมโมเดล AI เข้ากับแอปพลิเคชัน นอกจากนี้ เราจะเจาะลึกเทคนิคขั้นสูงสำหรับการใช้ผู้ช่วยเขียนโค้ด AI อย่างมีประสิทธิภาพ รวมถึง Prompt Engineering สำหรับการสร้างโค้ด การปรับโครงสร้างโค้ด และการดีบัก และแนะนำแนวคิดของ AI Agents สำหรับเวิร์กโฟลว์การพัฒนาแบบอัตโนมัติ

## วัตถุประสงค์การเรียนรู้
เมื่อจบโมดูลนี้ ผู้เข้าร่วมจะสามารถ:
*   เข้าใจกลยุทธ์ต่างๆ สำหรับการปรับใช้โมเดล AI ตั้งแต่ API อย่างง่ายไปจนถึง Serverless Functions
*   สร้างคอนเทนเนอร์แอปพลิเคชัน AI โดยใช้ Docker เพื่อสภาพแวดล้อมที่สอดคล้องกันและทำซ้ำได้
*   สร้างและปรับใช้ RESTful APIs สำหรับโมเดล AI โดยใช้ FastAPI
*   สร้างเว็บแอปพลิเคชันแบบโต้ตอบสำหรับโมเดล AI โดยใช้ Streamlit
*   เชี่ยวชาญเทคนิคขั้นสูงสำหรับการใช้ผู้ช่วยเขียนโค้ด AI (เช่น GitHub Copilot, Cursor) สำหรับการสร้างโค้ด การปรับโครงสร้างโค้ด และการดีบัก
*   ประยุกต์ใช้หลักการ Prompt Engineering เพื่อเพิ่มประโยชน์สูงสุดของผู้ช่วยเขียนโค้ด AI
*   เข้าใจสาขาที่กำลังเกิดขึ้นของ AI Agents และศักยภาพในการทำงานอัตโนมัติของงานพัฒนา
*   นำแนวทางปฏิบัติที่ดีที่สุดสำหรับโครงสร้างโปรเจกต์และการควบคุมเวอร์ชันในโปรเจกต์ AI ไปใช้

## 6.1 กลยุทธ์การปรับใช้โมเดล AI สมัยใหม่ (1 ชั่วโมง)

### 6.1.1 บทนำสู่ MLOps
*   **แนวคิด:** การเชื่อมช่องว่างระหว่างการพัฒนา ML และการดำเนินงาน
*   **เสาหลักสำคัญ:** การทดลอง, การจัดการข้อมูล, การฝึกโมเดล, การควบคุมเวอร์ชัน, การปรับใช้, การตรวจสอบ

### 6.1.2 ตัวเลือกการปรับใช้
*   **RESTful APIs:** การเปิดเผยโมเดลเป็นบริการเว็บ
    *   **ข้อดี:** ไม่ขึ้นกับภาษา, ปรับขนาดได้, เป็นที่ยอมรับอย่างกว้างขวาง
    *   **ข้อเสีย:** ต้องมีการจัดการเซิร์ฟเวอร์
*   **Serverless Functions (เช่น AWS Lambda, Google Cloud Functions):** ขับเคลื่อนด้วยเหตุการณ์, จ่ายตามการใช้งาน
    *   **ข้อดี:** ปรับขนาดอัตโนมัติ, คุ้มค่าสำหรับปริมาณงานที่ไม่ต่อเนื่อง
    *   **ข้อเสีย:** Cold Starts, การผูกติดกับผู้ให้บริการ
*   **Edge Deployment:** การปรับใช้โมเดลโดยตรงบนอุปกรณ์ (เช่น มือถือ, IoT)
    *   **ข้อดี:** Latency ต่ำ, ความสามารถในการทำงานแบบออฟไลน์, ความเป็นส่วนตัว
    *   **ข้อเสีย:** ข้อจำกัดด้านทรัพยากร, ต้องมีการปรับแต่งโมเดล
*   **Batch Prediction:** การประมวลผลชุดข้อมูลขนาดใหญ่ออฟไลน์
    *   **ข้อดี:** เหมาะสำหรับงานที่ต้องการการประมวลผลจำนวนมาก, ไม่ต้องการการตอบสนองแบบเรียลไทม์
    *   **ข้อเสีย:** ไม่เหมาะสำหรับแอปพลิเคชันที่ต้องการการตอบสนองทันที

### 6.1.3 Containerization ด้วย Docker
*   **ทำไมต้อง Docker?** การทำซ้ำได้, การแยก, การพกพา
*   **Dockerfile:** การสร้างอิมเมจที่กำหนดเองสำหรับแอปพลิเคชัน AI
    *   **การเลือก Base Image:** เวอร์ชัน Python, การรองรับ GPU
    *   **Dependencies:** `requirements.txt`
    *   **Application Code:** การคัดลอกและการตั้งค่าไดเรกทอรีการทำงาน
    *   **Entrypoint และ Command:** การกำหนดวิธีการทำงานของคอนเทนเนอร์
*   **คำสั่ง Docker:** `build`, `run`, `ps`, `stop`, `rm`, `exec`
*   **Docker Compose (โดยย่อ):** การจัดการแอปพลิเคชันหลายคอนเทนเนอร์
```dockerfile
# Example Dockerfile for a Python AI application

# Use an official Python runtime as a parent image
FROM python:3.9-slim-buster

# Set the working directory in the container
WORKDIR /app

# Install any needed packages specified in requirements.txt
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the current directory contents into the container at /app
COPY . .

# Make port 8000 available to the world outside this container
EXPOSE 8000

# Run the application
CMD [\"python\", \"app.py\"]
```

## 6.2 การสร้าง AI APIs ด้วย FastAPI (1 ชั่วโมง)

### 6.2.1 บทนำสู่ FastAPI
*   **แนวคิด:** Web Framework ที่ทันสมัยและรวดเร็ว (ประสิทธิภาพสูง) สำหรับการสร้าง APIs ด้วย Python 3.7+
*   **คุณสมบัติหลัก:** การรองรับ Asynchronous, การตรวจสอบข้อมูลอัตโนมัติ (Pydantic), เอกสารประกอบ API แบบโต้ตอบอัตโนมัติ (Swagger UI, ReDoc)
*   **กรณีการใช้งาน:** การให้บริการโมเดล Machine Learning เป็น Microservices

### 6.2.2 แอปพลิเคชัน FastAPI พื้นฐาน
*   **การติดตั้ง:** `pip install fastapi uvicorn`
*   **`@app.get`, `@app.post`:** การกำหนด Endpoint ของ API
*   **Request และ Response Models (Pydantic):** การรับรองความสมบูรณ์ของข้อมูล
*   **การรัน API:** `uvicorn main:app --reload`
```python
# main.py for FastAPI
from fastapi import FastAPI
from pydantic import BaseModel

# Assume this is our pre-trained ML model
class SimpleModel:
    def predict(self, data):
        # In a real scenario, load your actual ML model here
        # For demonstration, a dummy prediction
        return {\"prediction\": sum(data) / len(data) if data else 0.0}

model = SimpleModel()

app = FastAPI(title=\"AI Model API\", description=\"A simple API to serve an AI model.\")

class PredictionRequest(BaseModel):
    data: list[float]

class PredictionResponse(BaseModel):
    prediction: float

@app.get(\"/health\")
async def health_check():
    return {\"status\": \"ok\", \"message\": \"API is running\"}

@app.post(\"/predict\", response_model=PredictionResponse)
async def get_prediction(request: PredictionRequest):
    prediction_result = model.predict(request.data)
    return PredictionResponse(prediction=prediction_result[\"prediction\"])

# To run this:
# 1. Save as main.py
# 2. pip install fastapi uvicorn pydantic
# 3. uvicorn main:app --reload
```

### 6.2.3 การรวมโมเดล ML
*   **การโหลดโมเดล:** `joblib`, `pickle`, `torch.load`, `tf.keras.models.load_model`
*   **Asynchronous Endpoints:** การจัดการการทำนายที่ใช้เวลานานโดยไม่บล็อก
*   **การจัดการข้อผิดพลาด:** Custom Exceptions และ Responses

## 6.3 การสร้าง AI Demos แบบโต้ตอบด้วย Streamlit (1 ชั่วโมง)

### 6.3.1 บทนำสู่ Streamlit
*   **แนวคิด:** Framework แอปพลิเคชัน Open-source สำหรับทีม Machine Learning และ Data Science
*   **คุณสมบัติหลัก:** เปลี่ยนสคริปต์ข้อมูลให้เป็นเว็บแอปที่แชร์ได้ในไม่กี่นาที ไม่จำเป็นต้องมีประสบการณ์ Front-end
*   **กรณีการใช้งาน:** การสร้าง Prototype อย่างรวดเร็ว, Interactive Dashboards, การสาธิตโมเดล

### 6.3.2 แอปพลิเคชัน Streamlit พื้นฐาน
*   **การติดตั้ง:** `pip install streamlit`
*   **Widgets:** `st.slider`, `st.text_input`, `st.button`, `st.selectbox`
*   **การแสดงข้อมูล:** `st.write`, `st.dataframe`, `st.pyplot`
*   **การรันแอป:** `streamlit run app.py`
```python
# app.py for Streamlit
import streamlit as st
import numpy as np
import pandas as pd

st.set_page_config(page_title=\"Simple AI Demo\", layout=\"centered\")

st.title(\"✨ Interactive AI Model Demo\")
st.markdown(\"This is a simple demonstration of an AI model using Streamlit.\")

# Simulate a simple AI model
def simulate_model_prediction(input_value):
    # A dummy model: if input > 50, predict \'High\', else \'Low\'
    if input_value > 50:
        return \"High Confidence\"
    else:
        return \"Low Confidence\"

st.header(\"Model Input\")
input_slider = st.slider(\"Select an input value\", 0, 100, 50)

if st.button(\"Get Prediction\"):
    prediction = simulate_model_prediction(input_slider)
    st.success(f\"The model predicts: **{prediction}**\")

st.header(\"Data Visualization\")
# Generate some dummy data for visualization
data = pd.DataFrame({
    \"x\": np.random.randn(100),
    \"y\": np.random.randn(100)
})
st.line_chart(data)

st.sidebar.header(\"About\")
st.sidebar.info(\"This app demonstrates basic Streamlit features for AI model interaction.\")

# To run this:
# 1. Save as app.py
# 2. pip install streamlit numpy pandas
# 3. streamlit run app.py
```

## 6.4 AI Coding Assistants & Agentic Workflows (1 ชั่วโมง)

### 6.4.1 วิวัฒนาการของผู้ช่วยเขียนโค้ด AI
*   **Code Completion:** คำแนะนำพื้นฐาน (เช่น Tabnine, Copilot รุ่นเก่า)
*   **Code Generation:** การสร้างฟังก์ชัน, คลาส, สคริปต์ทั้งหมดจาก Prompt ภาษาธรรมชาติ (เช่น GitHub Copilot, Cursor, Code Llama)
*   **Code Refactoring & Debugging:** คำแนะนำที่ขับเคลื่อนด้วย AI สำหรับการปรับปรุงคุณภาพโค้ดและการแก้ไขข้อผิดพลาด
*   **AI-Driven Development (AIDD):** กระบวนทัศน์ที่ AI ช่วยเหลืออย่างแข็งขันตลอดวงจรการพัฒนาซอฟต์แวร์ทั้งหมด

### 6.4.2 การเชี่ยวชาญผู้ช่วยเขียนโค้ด AI
*   **Prompt Engineering สำหรับโค้ด:**
    *   **ความชัดเจนและความเฉพาะเจาะจง:** ระบุข้อกำหนดที่ชัดเจน, อินพุตที่ต้องการ, เอาต์พุต และข้อจำกัด
    *   **บริบทเป็นสิ่งสำคัญ:** รวม Snippets โค้ดที่เกี่ยวข้อง, Function Signatures และ Comments
    *   **การปรับปรุงซ้ำๆ:** เริ่มต้นแบบกว้างๆ จากนั้นปรับปรุง Prompt ตามเอาต์พุต AI เริ่มต้น
    *   **ตัวอย่าง:** การให้ตัวอย่างการใช้งาน, รูปแบบเอาต์พุตที่ต้องการ
    *   **ข้อจำกัดเชิงลบ:** การระบุสิ่งที่ไม่ควรทำ
*   **เครื่องมือและคุณสมบัติ:**
    *   **Chat Interfaces:** การโต้ตอบกับ AI สำหรับการสร้างโค้ด, การอธิบาย, การดีบัก
    *   **Inline Suggestions:** การเติมโค้ดอัตโนมัติแบบเรียลไทม์
    *   **Terminal Integration:** การใช้ AI เพื่อสร้างคำสั่ง Shell
    *   **Test Generation:** การสร้าง Unit Test โดยใช้ AI

### 6.4.3 AI Agents และเวิร์กโฟลว์แบบอัตโนมัติ
*   **แนวคิด:** ระบบ AI ที่สามารถรับรู้สภาพแวดล้อม, ตัดสินใจ และดำเนินการเพื่อให้บรรลุเป้าหมาย ซึ่งมักจะเกี่ยวข้องกับหลายขั้นตอนและการใช้เครื่องมือ
*   **ส่วนประกอบของ AI Agent:**
    *   **LLM (Large Language Model):** \"สมอง\" สำหรับการให้เหตุผลและการวางแผน
    *   **Memory:** ระยะสั้น (Context Window) และระยะยาว (Vector Databases, Knowledge Graphs)
    *   **Tools:** การเข้าถึง External APIs, Code Interpreters, Web Browsers
    *   **Planning & Reflection:** ความสามารถในการแบ่งงาน, ดำเนินการตามขั้นตอน และเรียนรู้จากความล้มเหลว
*   **Agentic Frameworks (เช่น LangChain Agents, CrewAI):** การสร้างเวิร์กโฟลว์อัจฉริยะแบบหลายขั้นตอน
    *   **กรณีการใช้งาน:** การสร้างโค้ดอัตโนมัติ, การทดสอบ, การปรับใช้, Pipeline การวิเคราะห์ข้อมูล

### 6.4.4 แนวทางปฏิบัติที่ดีที่สุดสำหรับโครงสร้างโปรเจกต์ AI และการควบคุมเวอร์ชัน
*   **Modular Design:** การแยกส่วนประกอบ (ข้อมูล, โมเดล, การฝึก, การปรับใช้)
*   **Version Control (Git):** แนวทางปฏิบัติที่ดีที่สุดสำหรับการ Branching, Merging และการพัฒนาร่วมกัน
*   **Environment Management:** `conda`, `venv`, `pipenv` สำหรับสภาพแวดล้อมที่ทำซ้ำได้
*   **Configuration Management:** การใช้ `YAML`, `JSON` หรือ `dataclasses` สำหรับการจัดการ Hyperparameters และการตั้งค่า
*   **Testing:** Unit Tests, Integration Tests, Model Validation Tests

## แบบฝึกหัดสำหรับโมดูล 6

### แบบฝึกหัด 6.1: การสร้าง Simple FastAPI Model Serving API
**สถานการณ์:** คุณมีโมเดล Machine Learning ที่ได้รับการฝึกอบรม (Dummy) และต้องการเปิดเผยเป็น RESTful API โดยใช้ FastAPI

**งาน:**
1.  สร้างไฟล์ `main.py` สำหรับแอปพลิเคชัน FastAPI ของคุณ
2.  กำหนดโมเดล Pydantic `PredictionRequest` ที่ยอมรับรายการ Features ตัวเลข (เช่น `features: list[float]`)
3.  กำหนดโมเดล Pydantic `PredictionResponse` ที่ส่งคืนการทำนายเดียว (เช่น `prediction: float`)
4.  ใช้ฟังก์ชัน `predict` Dummy ที่จำลองการทำนายโมเดล (เช่น ส่งคืนผลรวมของ Features)
5.  สร้าง Endpoint POST `/predict` ที่รับ `PredictionRequest`, เรียกใช้ฟังก์ชัน `predict` Dummy ของคุณ และส่งคืน `PredictionResponse`
6.  เพิ่ม Endpoint GET `/health` ที่ส่งคืน `{\"status\": \"ok\"}`
7.  (ไม่บังคับ) รันแอปพลิเคชันโดยใช้ `uvicorn main:app --reload` และทดสอบโดยใช้เครื่องมือเช่น `curl` หรือ Postman/Insomnia

### แบบฝึกหัด 6.2: การสร้าง Interactive Streamlit Dashboard สำหรับการสำรวจโมเดล
**สถานการณ์:** คุณต้องการสร้าง User Interface บนเว็บที่ใช้งานง่ายเพื่อโต้ตอบกับโมเดล Machine Learning (Dummy) และแสดงภาพผลลัพธ์

**งาน:**
1.  สร้างไฟล์ `app.py` สำหรับแอปพลิเคชัน Streamlit ของคุณ
2.  เพิ่มชื่อและคำอธิบายสั้นๆ สำหรับแอปของคุณ
3.  ใช้ Sidebar พร้อมข้อมูลบางอย่างเกี่ยวกับแอป
4.  สร้าง Widget Slider (`st.slider`) สำหรับ Feature อินพุตตัวเลข (เช่น \"Feature X Value\" จาก 0 ถึง 100)
5.  สร้างปุ่ม (`st.button`) ที่เมื่อคลิกแล้ว จะเรียกใช้การทำนายโมเดล Dummy (เช่น ถ้าอินพุต > 50, เอาต์พุต \"High\", มิฉะนั้น \"Low\") แสดงการทำนายโดยใช้ `st.write` หรือ `st.success`
6.  เพิ่มการแสดงภาพข้อมูลอย่างง่าย (เช่น `st.line_chart` หรือ `st.bar_chart`) โดยใช้ข้อมูลที่สร้างขึ้นแบบสุ่มเพื่อสาธิตความสามารถในการแสดงภาพของ Streamlit
7.  (ไม่บังคับ) รันแอปพลิเคชันโดยใช้ `streamlit run app.py`

### แบบฝึกหัด 6.3: การสร้างคอนเทนเนอร์แอปพลิเคชัน AI ด้วย Docker
**สถานการณ์:** คุณมีสคริปต์ Python อย่างง่ายที่ใช้โมเดล Machine Learning และต้องการแพ็คเกจลงใน Docker Container เพื่อการปรับใช้และการทำซ้ำที่ง่ายดาย

**งาน:**
1.  สร้างไฟล์ `model_app.py` พร้อมสคริปต์ Python อย่างง่ายที่:
    *   นำเข้า `sklearn` (เช่น `from sklearn.linear_model import LogisticRegression`)
    *   พิมพ์ข้อความเช่น \"Model application is running!\"
    *   (ไม่บังคับ) จำลองการโหลดโมเดลและการทำนาย
2.  สร้างไฟล์ `requirements.txt` ที่ระบุ `scikit-learn`
3.  สร้าง `Dockerfile` ที่:
    *   ใช้ Base Image Python 3.9
    *   ตั้งค่า Working Directory เป็น `/app`
    *   คัดลอก `requirements.txt` และติดตั้ง Dependencies
    *   คัดลอก `model_app.py`
    *   ตั้งค่า Command เพื่อรัน `python model_app.py`
4.  สร้าง Docker Image (`docker build -t my-ml-app .`)
5.  รัน Docker Container (`docker run my-ml-app`) ตรวจสอบว่าสคริปต์ทำงานสำเร็จ

### แบบฝึกหัด 6.4: Prompt Engineering สำหรับ AI Coding Assistant (Refactoring)
**สถานการณ์:** คุณมีโค้ด Python ที่ทำงานได้แต่สามารถปรับปรุงได้ในแง่ของความสามารถในการอ่าน, ประสิทธิภาพ และการปฏิบัติตามแนวทางปฏิบัติที่ดีที่สุด คุณต้องการใช้ AI Coding Assistant เพื่อช่วยในการ Refactor

**งาน:**
1.  ใช้ Snippet โค้ด Python ต่อไปนี้:
    ```python
    def calculate_average_and_filter(data_list, threshold):
        total = 0
        count = 0
        filtered_items = []
        for item in data_list:
            total += item
            count += 1
            if item > threshold:
                filtered_items.append(item)
        if count == 0:
            average = 0
        else:
            average = total / count
        return average, filtered_items
    ```
2.  สร้าง Prompt สำหรับ AI Coding Assistant (เช่น GitHub Copilot Chat, Cursor) เพื่อขอให้ Refactor ฟังก์ชันนี้ Prompt ของคุณควรรวมคำแนะนำเพื่อ:
    *   ปรับปรุงความสามารถในการอ่านและความกระชับ
    *   ใช้ฟังก์ชัน Python Built-in (เช่น `sum`, `len`, List Comprehensions) เมื่อเหมาะสม
    *   เพิ่ม Type Hints

### แบบฝึกหัด 6.5: การสร้าง AI Agent อย่างง่าย (แนวคิด)
**สถานการณ์:** คุณต้องการทำความเข้าใจแนวคิดพื้นฐานของ AI Agent โดยการออกแบบ Agent อย่างง่ายที่สามารถดำเนินการหลายขั้นตอนเพื่อบรรลุเป้าหมาย

**งาน:**
1.  กำหนดเป้าหมายสำหรับ Agent (เช่น \"ค้นหาข้อมูลเกี่ยวกับสภาพอากาศปัจจุบันในเมืองหนึ่งๆ และรายงานอุณหภูมิ\" หรือ \"เขียนฟังก์ชัน Python เพื่อคำนวณ Fibonacci Sequence\")
2.  ระบุ \"เครื่องมือ\" ที่ Agent จะต้องใช้ (เช่น Web Search Tool, Code Interpreter Tool)
3.  อธิบายขั้นตอนการทำงานของ Agent (Planning, Action, Observation, Reflection) สำหรับเป้าหมายที่กำหนด
4.  (ไม่บังคับ) เขียน Pseudocode หรือโครงสร้าง Python อย่างง่ายเพื่อแสดงการทำงานของ Agent

## เฉลยสำหรับโมดูล 6

### เฉลย 6.1: การสร้าง Simple FastAPI Model Serving API
```python
from fastapi import FastAPI
from pydantic import BaseModel

# 1. Create a main.py file for your FastAPI application.
# This code would be saved as main.py

# Dummy model prediction function
def dummy_predict(features: list[float]) -> float:
    if not features:
        return 0.0
    return sum(features) / len(features)

# 2. Define a PredictionRequest Pydantic model
class PredictionRequest(BaseModel):
    features: list[float]

# 3. Define a PredictionResponse Pydantic model
class PredictionResponse(BaseModel):
    prediction: float

app = FastAPI(title=\"Simple ML Model API\")

# 6. Add a /health GET endpoint
@app.get(\"/health\")
async def health_check():
    return {\"status\": \"ok\", \"message\": \"API is healthy\"}

# 5. Create a /predict POST endpoint
@app.post(\"/predict\", response_model=PredictionResponse)
async def predict_endpoint(request: PredictionRequest):
    prediction_value = dummy_predict(request.features)
    return PredictionResponse(prediction=prediction_value)

# To run this application:
# 1. Save the code above as main.py
# 2. Install dependencies: pip install fastapi uvicorn pydantic
# 3. Run the server: uvicorn main:app --reload
# 4. Test with curl or Postman:
#    curl -X POST \"http://127.0.0.1:8000/predict\" \\
#         -H \"Content-Type: application/json\" \\
#         -d \"{\\\"features\\\": [1.0, 2.0, 3.0, 4.0, 5.0]}\"
#    curl http://127.0.0.1:8000/health
```

### เฉลย 6.2: การสร้าง Interactive Streamlit Dashboard สำหรับการสำรวจโมเดล
```python
import streamlit as st
import numpy as np
import pandas as pd

# 1. Create an app.py file for your Streamlit application.
# This code would be saved as app.py

st.set_page_config(page_title=\"Model Explorer\", layout=\"wide\")

# 2. Add a title and a brief description for your app.
st.title(\"✨ ML Model Interactive Explorer\")
st.markdown(\"Explore a dummy machine learning model and visualize its behavior.\")

# Dummy model prediction function
def dummy_model_prediction(input_feature: float) -> str:
    if input_feature > 70:
        return \"High Risk\"
    elif input_feature > 30:
        return \"Medium Risk\"
    else:
        return \"Low Risk\"

# 3. Implement a sidebar with some information about the app.
st.sidebar.header(\"About This App\")
st.sidebar.info(
    \"This interactive Streamlit application demonstrates how to build a simple UI \\
    for a machine learning model. Adjust the input feature and see the prediction!\"
)
st.sidebar.markdown(\"Developed by AI Workshop Team\")

st.header(\"Model Input & Prediction\")

# 4. Create a slider widget for a numerical input feature
input_value = st.slider(
    \"Select Input Feature Value (0-100)\",
    min_value=0,
    max_value=100,
    value=50,
    step=1
)

# 5. Create a button that, when clicked, triggers a dummy model prediction
if st.button(\"Get Model Prediction\"):
    prediction = dummy_model_prediction(input_value)
    if \"High\" in prediction:
        st.error(f\"Prediction: **{prediction}**\")
    elif \"Medium\" in prediction:
        st.warning(f\"Prediction: **{prediction}**\")
    else:
        st.success(f\"Prediction: **{prediction}**\")

st.header(\"Data Visualization\")

# 6. Add a simple data visualization
st.subheader(\"Simulated Data Distribution\")

# Generate some dummy data for visualization
np.random.seed(42)
data_viz = pd.DataFrame({
    \"Feature 1\": np.random.randn(100).cumsum(),
    \"Feature 2\": np.random.randn(100).cumsum()
})

st.line_chart(data_viz)
st.write(\"This chart shows a simulated trend of two features over time.\")

# To run this application:
# 1. Save the code above as app.py
# 2. Install dependencies: pip install streamlit numpy pandas
# 3. Run the app: streamlit run app.py
```

### เฉลย 6.3: การสร้างคอนเทนเนอร์แอปพลิเคชัน AI ด้วย Docker

**1. `model_app.py`:**
```python
# model_app.py
from sklearn.linear_model import LogisticRegression
import numpy as np
import joblib

print(\"Model application is starting up!\")

# Simulate a simple model training and saving
X = np.array([[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7]])
y = np.array([0, 0, 0, 1, 1, 1])

model = LogisticRegression()
model.fit(X, y)

# Save the model
joblib.dump(model, \"logistic_regression_model.pkl\")
print(\"Dummy model trained and saved as logistic_regression_model.pkl\")

# Simulate loading the model and making a prediction
loaded_model = joblib.load(\"logistic_regression_model.pkl\")
sample_data = np.array([[2.5, 3.5]])
prediction = loaded_model.predict(sample_data)

print(f\"Prediction for {sample_data}: {prediction[0]}\")
print(\"Model application finished successfully!\")
```

**2. `requirements.txt`:**
```
scikit-learn
numpy
joblib
```

**3. `Dockerfile`:**
```dockerfile
# Dockerfile

# Use an official Python runtime as a parent image
FROM python:3.9-slim-buster

# Set the working directory in the container
WORKDIR /app

# Install any needed packages specified in requirements.txt
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the current directory contents into the container at /app
COPY model_app.py .

# Run the application
CMD [\"python\", \"model_app.py\"]
```

**4. Build the Docker image:**
เปิด Terminal ในไดเรกทอรีที่มีไฟล์ทั้งสามนี้และรัน:
```bash
docker build -t my-ml-app .
```

**5. Run the Docker container:**
```bash
docker run my-ml-app
```

**ผลลัพธ์ที่คาดหวังใน Terminal:**
```
Model application is starting up!
Dummy model trained and saved as logistic_regression_model.pkl
Prediction for [[2.5 3.5]]: 0
Model application finished successfully!
```

### เฉลย 6.4: Prompt Engineering สำหรับ AI Coding Assistant (Refactoring)

**Prompt ตัวอย่างสำหรับ AI Coding Assistant:**

```
Refactor the following Python function to improve readability, conciseness, and efficiency. 
Use built-in Python functions like `sum()`, `len()`, and list comprehensions where appropriate. 
Also, add type hints for all parameters and the return value.

```python
def calculate_average_and_filter(data_list, threshold):
    total = 0
    count = 0
    filtered_items = []
    for item in data_list:
        total += item
        count += 1
        if item > threshold:
            filtered_items.append(item)
    if count == 0:
        average = 0
    else:
        average = total / count
    return average, filtered_items
```
```

**ผลลัพธ์ที่คาดหวังจาก AI Coding Assistant (ตัวอย่าง):**

```python
from typing import List, Tuple

def calculate_average_and_filter(data_list: List[float], threshold: float) -> Tuple[float, List[float]]:
    if not data_list:
        return 0.0, []

    # Calculate total and count using built-in functions
    total = sum(data_list)
    count = len(data_list)
    average = total / count

    # Filter items using a list comprehension
    filtered_items = [item for item in data_list if item > threshold]

    return average, filtered_items
```

### เฉลย 6.5: การสร้าง AI Agent อย่างง่าย (แนวคิด)

**เป้าหมายของ Agent:** \"ค้นหาข้อมูลเกี่ยวกับสภาพอากาศปัจจุบันในกรุงเทพฯ และรายงานอุณหภูมิและความชื้น\"

**เครื่องมือที่ Agent จะต้องใช้:**
*   **Web Search Tool:** สำหรับค้นหาข้อมูลสภาพอากาศ (เช่น Google Search)
*   **Weather API Tool (สมมติ):** API ที่สามารถดึงข้อมูลสภาพอากาศตามเมืองได้

**ขั้นตอนการทำงานของ Agent (Planning, Action, Observation, Reflection):**

1.  **Planning:**
    *   **เป้าหมายย่อย 1:** ระบุเมืองที่ต้องการค้นหาสภาพอากาศ (กรุงเทพฯ)
    *   **เป้าหมายย่อย 2:** ค้นหาข้อมูลสภาพอากาศปัจจุบันสำหรับเมืองนั้น
    *   **เป้าหมายย่อย 3:** แยกอุณหภูมิและความชื้นจากข้อมูลที่ได้
    *   **เป้าหมายย่อย 4:** รายงานผลลัพธ์

2.  **Action (ตัวอย่าง):**
    *   **Action 1:** ใช้ Web Search Tool ด้วย Query: \"สภาพอากาศปัจจุบันกรุงเทพฯ\"
    *   **Observation 1:** ได้รับผลการค้นหาจาก Google ซึ่งอาจมีลิงก์ไปยังเว็บไซต์พยากรณ์อากาศ หรือแสดงข้อมูลโดยตรงใน Snippet
    *   **Reflection 1:** หากข้อมูลเพียงพอจาก Snippet ให้ดำเนินการต่อ หากไม่ ให้เลือก URL ที่เกี่ยวข้องที่สุดและใช้ Browser Tool เพื่อเข้าถึง

    *   **Action 2 (ทางเลือก):** หากจำเป็น, ใช้ Browser Tool เพื่อเข้าถึงเว็บไซต์พยากรณ์อากาศ (เช่น `https://www.accuweather.com/th/th/bangkok/318849/current-weather/318849`)
    *   **Observation 2:** ได้รับเนื้อหา HTML ของหน้าเว็บสภาพอากาศ
    *   **Reflection 2:** วิเคราะห์เนื้อหา HTML เพื่อค้นหาอุณหภูมิและความชื้น หรือใช้ Weather API Tool หากมี

    *   **Action 3 (ทางเลือกที่ดีกว่า):** ใช้ Weather API Tool ด้วย Parameter: `city=\"Bangkok\"`
    *   **Observation 3:** ได้รับข้อมูล JSON จาก API ที่มี `temperature` และ `humidity`
    *   **Reflection 3:** ตรวจสอบว่าข้อมูลที่ได้มาถูกต้องและครบถ้วน

3.  **Reporting:**
    *   **Action 4:** รายงานผลลัพธ์: \"สภาพอากาศปัจจุบันในกรุงเทพฯ คือ อุณหภูมิ [อุณหภูมิที่ได้] องศาเซลเซียส และความชื้น [ความชื้นที่ได้]%\"

**Pseudocode/โครงสร้าง Python อย่างง่าย:**

```python
class AIAgent:
    def __init__(self):
        self.tools = {
            \"web_search\": self._web_search_tool,
            \"weather_api\": self._weather_api_tool,
            # ... other tools
        }
        self.memory = [] # To store observations and thoughts

    def _web_search_tool(self, query: str) -> str:
        # Simulate web search API call
        print(f\"Searching web for: {query}\")
        if \"สภาพอากาศปัจจุบันกรุงเทพฯ\" in query:
            return \"ผลการค้นหาสภาพอากาศ: อุณหภูมิ 32C, ความชื้น 75% (จากเว็บไซต์ AccuWeather)\"
        return \"No relevant results.\"

    def _weather_api_tool(self, city: str) -> dict:
        # Simulate weather API call
        print(f\"Calling weather API for: {city}\")
        if city == \"Bangkok\":
            return {\"city\": \"Bangkok\", \"temperature_celsius\": 32, \"humidity_percent\": 75}
        return {\"error\": \"City not found.\"}

    def run(self, goal: str):
        print(f\"Agent Goal: {goal}\")
        self.memory.append(f\"Goal: {goal}\")

        # Planning Phase
        plan = self._plan_task(goal)
        print(f\"Generated Plan: {plan}\")
        self.memory.append(f\"Plan: {plan}\")

        for step in plan:
            print(f\"Executing Step: {step[\"description\"]}\")
            action_result = self._execute_action(step[\"action\"], step[\"params\"])
            print(f\"Observation: {action_result}\")
            self.memory.append(f\"Observation: {action_result}\")
            # In a real agent, there would be a reflection step here
            # to adjust the plan based on observation

            if \"temperature_celsius\" in action_result and \"humidity_percent\" in action_result:
                print(f\"\nFinal Report: สภาพอากาศปัจจุบันใน {action_result[\"city\"]} คือ อุณหภูมิ {action_result[\"temperature_celsius\"]} องศาเซลเซียส และความชื้น {action_result[\"humidity_percent\"]}%\")
                return

    def _plan_task(self, goal: str) -> List[Dict]:
        # Simplified planning: hardcoded for this example
        if \"สภาพอากาศปัจจุบันในเมืองหนึ่งๆ\" in goal:
            return [
                {\"description\": \"Call weather API for Bangkok\", \"action\": \"weather_api\", \"params\": {\"city\": \"Bangkok\"}}
            ]
        return []

    def _execute_action(self, tool_name: str, params: Dict):
        if tool_name in self.tools:
            return self.tools[tool_name](**params)
        return {\"error\": f\"Tool {tool_name} not found.\"}

# Example Usage:
# agent = AIAgent()
# agent.run(\"ค้นหาข้อมูลเกี่ยวกับสภาพอากาศปัจจุบันในกรุงเทพฯ และรายงานอุณหภูมิและความชื้น\")
```

## สรุปโมดูล 6
โมดูลนี้ได้ให้ความรู้ที่ครอบคลุมเกี่ยวกับการปรับใช้โมเดล AI และการใช้ประโยชน์จากผู้ช่วยเขียนโค้ด AI ผู้เข้าร่วมได้เรียนรู้กลยุทธ์การปรับใช้ที่หลากหลาย รวมถึง RESTful APIs และ Serverless Functions พร้อมทั้งทำความเข้าใจถึงความสำคัญของ Containerization ด้วย Docker เราได้สำรวจวิธีการสร้าง API ที่มีประสิทธิภาพด้วย FastAPI และพัฒนา Interactive Web Applications ด้วย Streamlit เพื่อสาธิตโมเดล AI นอกจากนี้ โมดูลยังได้เจาะลึกถึงการใช้ AI Coding Assistants อย่างเชี่ยวชาญผ่าน Prompt Engineering และแนะนำแนวคิดที่กำลังเกิดขึ้นของ AI Agents สำหรับเวิร์กโฟลว์การพัฒนาแบบอัตโนมัติ ความรู้และทักษะเหล่านี้เป็นสิ่งสำคัญสำหรับนักพัฒนา AI ในการนำโมเดลไปใช้งานจริง เพิ่มประสิทธิภาพการทำงาน และสร้างโซลูชัน AI ที่แข็งแกร่งและปรับขนาดได้

### เฉลย 6.4: Prompt Engineering สำหรับ AI Coding Assistant (Refactoring)

**Prompt ตัวอย่างสำหรับ AI Coding Assistant:**

```
Refactor the following Python function to improve readability, conciseness, and efficiency. 
Use built-in Python functions like `sum()`, `len()`, and list comprehensions where appropriate. 
Also, add type hints for all parameters and the return value.

```python
def calculate_average_and_filter(data_list, threshold):
    total = 0
    count = 0
    filtered_items = []
    for item in data_list:
        total += item
        count += 1
        if item > threshold:
            filtered_items.append(item)
    if count == 0:
        average = 0
    else:
        average = total / count
    return average, filtered_items
```
```

**ผลลัพธ์ที่คาดหวังจาก AI Coding Assistant (ตัวอย่าง):**

```python
from typing import List, Tuple

def calculate_average_and_filter(data_list: List[float], threshold: float) -> Tuple[float, List[float]]:
    if not data_list:
        return 0.0, []

    # Calculate total and count using built-in functions
    total = sum(data_list)
    count = len(data_list)
    average = total / count

    # Filter items using a list comprehension
    filtered_items = [item for item in data_list if item > threshold]

    return average, filtered_items
```

### เฉลย 6.5: การสร้าง AI Agent อย่างง่าย (แนวคิด)

**เป้าหมายของ Agent:** \"ค้นหาข้อมูลเกี่ยวกับสภาพอากาศปัจจุบันในกรุงเทพฯ และรายงานอุณหภูมิและความชื้น\"

**เครื่องมือที่ Agent จะต้องใช้:**
*   **Web Search Tool:** สำหรับค้นหาข้อมูลสภาพอากาศ (เช่น Google Search)
*   **Weather API Tool (สมมติ):** API ที่สามารถดึงข้อมูลสภาพอากาศตามเมืองได้

**ขั้นตอนการทำงานของ Agent (Planning, Action, Observation, Reflection):**

1.  **Planning:**
    *   **เป้าหมายย่อย 1:** ระบุเมืองที่ต้องการค้นหาสภาพอากาศ (กรุงเทพฯ)
    *   **เป้าหมายย่อย 2:** ค้นหาข้อมูลสภาพอากาศปัจจุบันสำหรับเมืองนั้น
    *   **เป้าหมายย่อย 3:** แยกอุณหภูมิและความชื้นจากข้อมูลที่ได้
    *   **เป้าหมายย่อย 4:** รายงานผลลัพธ์

2.  **Action (ตัวอย่าง):**
    *   **Action 1:** ใช้ Web Search Tool ด้วย Query: \"สภาพอากาศปัจจุบันกรุงเทพฯ\"
    *   **Observation 1:** ได้รับผลการค้นหาจาก Google ซึ่งอาจมีลิงก์ไปยังเว็บไซต์พยากรณ์อากาศ หรือแสดงข้อมูลโดยตรงใน Snippet
    *   **Reflection 1:** หากข้อมูลเพียงพอจาก Snippet ให้ดำเนินการต่อ หากไม่ ให้เลือก URL ที่เกี่ยวข้องที่สุดและใช้ Browser Tool เพื่อเข้าถึง

    *   **Action 2 (ทางเลือก):** หากจำเป็น, ใช้ Browser Tool เพื่อเข้าถึงเว็บไซต์พยากรณ์อากาศ (เช่น `https://www.accuweather.com/th/th/bangkok/318849/current-weather/318849`)
    *   **Observation 2:** ได้รับเนื้อหา HTML ของหน้าเว็บสภาพอากาศ
    *   **Reflection 2:** วิเคราะห์เนื้อหา HTML เพื่อค้นหาอุณหภูมิและความชื้น หรือใช้ Weather API Tool หากมี

    *   **Action 3 (ทางเลือกที่ดีกว่า):** ใช้ Weather API Tool ด้วย Parameter: `city=\"Bangkok\"`
    *   **Observation 3:** ได้รับข้อมูล JSON จาก API ที่มี `temperature` และ `humidity`
    *   **Reflection 3:** ตรวจสอบว่าข้อมูลที่ได้มาถูกต้องและครบถ้วน

3.  **Reporting:**
    *   **Action 4:** รายงานผลลัพธ์: \"สภาพอากาศปัจจุบันในกรุงเทพฯ คือ อุณหภูมิ [อุณหภูมิที่ได้] องศาเซลเซียส และความชื้น [ความชื้นที่ได้]%\"

**Pseudocode/โครงสร้าง Python อย่างง่าย:**

```python
class AIAgent:
    def __init__(self):
        self.tools = {
            \"web_search\": self._web_search_tool,
            \"weather_api\": self._weather_api_tool,
            # ... other tools
        }
        self.memory = [] # To store observations and thoughts

    def _web_search_tool(self, query: str) -> str:
        # Simulate web search API call
        print(f\"Searching web for: {query}\")
        if \"สภาพอากาศปัจจุบันกรุงเทพฯ\" in query:
            return \"ผลการค้นหาสภาพอากาศ: อุณหภูมิ 32C, ความชื้น 75% (จากเว็บไซต์ AccuWeather)\"
        return \"No relevant results.\"

    def _weather_api_tool(self, city: str) -> dict:
        # Simulate weather API call
        print(f\"Calling weather API for: {city}\")
        if city == \"Bangkok\":
            return {\"city\": \"Bangkok\", \"temperature_celsius\": 32, \"humidity_percent\": 75}
        return {\"error\": \"City not found.\"}

    def run(self, goal: str):
        print(f\"Agent Goal: {goal}\")
        self.memory.append(f\"Goal: {goal}\")

        # Planning Phase
        plan = self._plan_task(goal)
        print(f\"Generated Plan: {plan}\")
        self.memory.append(f\"Plan: {plan}\")

        for step in plan:
            print(f\"Executing Step: {step[\"description\"]}\")
            action_result = self._execute_action(step[\"action\"], step[\"params\"])
            print(f\"Observation: {action_result}\")
            self.memory.append(f\"Observation: {action_result}\")
            # In a real agent, there would be a reflection step here
            # to adjust the plan based on observation

            if \"temperature_celsius\" in action_result and \"humidity_percent\" in action_result:
                print(f\"\nFinal Report: สภาพอากาศปัจจุบันใน {action_result[\"city\"]} คือ อุณหภูมิ {action_result[\"temperature_celsius\"]} องศาเซลเซียส และความชื้น {action_result[\"humidity_percent\"]}%\")
                return

    def _plan_task(self, goal: str) -> List[Dict]:
        # Simplified planning: hardcoded for this example
        if \"สภาพอากาศปัจจุบันในเมืองหนึ่งๆ\" in goal:
            return [
                {\"description\": \"Call weather API for Bangkok\", \"action\": \"weather_api\", \"params\": {\"city\": \"Bangkok\"}}
            ]
        return []

    def _execute_action(self, tool_name: str, params: Dict):
        if tool_name in self.tools:
            return self.tools[tool_name](**params)
        return {\"error\": f\"Tool {tool_name} not found.\"}

# Example Usage:
# agent = AIAgent()
# agent.run(\"ค้นหาข้อมูลเกี่ยวกับสภาพอากาศปัจจุบันในกรุงเทพฯ และรายงานอุณหภูมิและความชื้น\")
```

## สรุปโมดูล 6
โมดูลนี้ได้ให้ความรู้ที่ครอบคลุมเกี่ยวกับการปรับใช้โมเดล AI และการใช้ประโยชน์จากผู้ช่วยเขียนโค้ด AI ผู้เข้าร่วมได้เรียนรู้กลยุทธ์การปรับใช้ที่หลากหลาย รวมถึง RESTful APIs และ Serverless Functions พร้อมทั้งทำความเข้าใจถึงความสำคัญของ Containerization ด้วย Docker เราได้สำรวจวิธีการสร้าง API ที่มีประสิทธิภาพด้วย FastAPI และพัฒนา Interactive Web Applications ด้วย Streamlit เพื่อสาธิตโมเดล AI นอกจากนี้ โมดูลยังได้เจาะลึกถึงการใช้ AI Coding Assistants อย่างเชี่ยวชาญผ่าน Prompt Engineering และแนะนำแนวคิดที่กำลังเกิดขึ้นของ AI Agents สำหรับเวิร์กโฟลว์การพัฒนาแบบอัตโนมัติ ความรู้และทักษะเหล่านี้เป็นสิ่งสำคัญสำหรับนักพัฒนา AI ในการนำโมเดลไปใช้งานจริง เพิ่มประสิทธิภาพการทำงาน และสร้างโซลูชัน AI ที่แข็งแกร่งและปรับขนาดได้
