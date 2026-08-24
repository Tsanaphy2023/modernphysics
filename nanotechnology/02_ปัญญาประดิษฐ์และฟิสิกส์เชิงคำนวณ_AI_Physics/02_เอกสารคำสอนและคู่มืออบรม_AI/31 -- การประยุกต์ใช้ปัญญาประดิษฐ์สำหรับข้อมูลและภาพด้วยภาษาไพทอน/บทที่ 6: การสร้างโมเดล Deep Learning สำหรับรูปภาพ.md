## บทที่ 6: การสร้างโมเดล Deep Learning สำหรับรูปภาพ

ในบทที่แล้ว เราได้เรียนรู้วิธีการจัดการและประมวลผลรูปภาพในเบื้องต้น ในบทนี้ เราจะก้าวเข้าสู่หัวใจของการประยุกต์ใช้ AI กับรูปภาพ นั่นคือการสร้าง **โมเดล Deep Learning** เพื่อให้คอมพิวเตอร์สามารถ "เรียนรู้" และ "เข้าใจ" เนื้อหาภายในภาพได้เอง โดยเทคโนโลยีที่เป็นพระเอกในงานนี้คือ **โครงข่ายประสาทเทียม (Neural Networks)** และสถาปัตยกรรมพิเศษที่ออกแบบมาสำหรับภาพโดยเฉพาะอย่าง **Convolutional Neural Networks (CNN)**

### แนะนำโครงข่ายประสาทเทียม (Neural Networks)

โครงข่ายประสาทเทียม (หรือที่เรียกสั้นๆ ว่า Neural Networks) เป็นอัลกอริทึมที่ได้รับแรงบันดาลใจมาจากการทำงานของสมองมนุษย์ ประกอบด้วยหน่วยประมวลผลเล็กๆ ที่เรียกว่า **นิวรอน (Neuron)** หรือ **โหนด (Node)** ซึ่งเชื่อมต่อกันเป็นเครือข่าย

โครงสร้างพื้นฐานของ Neural Network ประกอบด้วย 3 ส่วนหลัก:

1.  **Input Layer:** ชั้นสำหรับรับข้อมูลนำเข้า ในบริบทของรูปภาพ ก็คือค่าพิกเซลของภาพนั่นเอง
2.  **Hidden Layers:** ชั้นที่ซ่อนอยู่ระหว่าง Input และ Output เป็นส่วนที่การเรียนรู้ส่วนใหญ่เกิดขึ้น โมเดล Deep Learning จะมี Hidden Layer หลายชั้น (ยิ่งลึกหรือ "Deep" ก็คือมีชั้นมาก) เพื่อเรียนรู้คุณลักษณะ (features) ที่ซับซ้อนขึ้นเรื่อยๆ
3.  **Output Layer:** ชั้นสุดท้ายที่ให้ผลลัพธ์การทำนาย เช่น ถ้าเป็นโมเดลจำแนกประเภทสุนัขกับแมว Output Layer ก็อาจจะมี 2 นิวรอน แทนความน่าจะเป็นของแต่ละคลาส

![โครงสร้าง Neural Network](https://private-us-east-1.manuscdn.com/sessionFile/OO4QhUUsaoBTGAbGU9i0j2/sandbox/pRb06yRMC7k7XW9CBSc5bm-images_1760366739186_na1fn_L2hvbWUvdWJ1bnR1L2RpYWdyYW1zL25ldXJhbF9uZXR3b3JrX3N0cnVjdHVyZQ.png?Policy=eyJTdGF0ZW1lbnQiOlt7IlJlc291cmNlIjoiaHR0cHM6Ly9wcml2YXRlLXVzLWVhc3QtMS5tYW51c2Nkbi5jb20vc2Vzc2lvbkZpbGUvT080UWhVVXNhb0JUR0FiR1U5aTBqMi9zYW5kYm94L3BSYjA2eVJNQzdrN1hXOUNCU2M1Ym0taW1hZ2VzXzE3NjAzNjY3MzkxODZfbmExZm5fTDJodmJXVXZkV0oxYm5SMUwyUnBZV2R5WVcxekwyNWxkWEpoYkY5dVpYUjNiM0pyWDNOMGNuVmpkSFZ5WlEucG5nIiwiQ29uZGl0aW9uIjp7IkRhdGVMZXNzVGhhbiI6eyJBV1M6RXBvY2hUaW1lIjoxNzk4NzYxNjAwfX19XX0_&Key-Pair-Id=K2HSFNDJXOU9YS&Signature=aB7IfFw1OY66~3gTAyRwMhjVW5cDfDT6lab0OyRlcO8~StJemNc-pds3p2gXkdk5LQoZp2IBDKvf-~SS3PkcMJa32K9i4nA1UmDwppgRtvHd0MyuLYG6ZjVIsN~BPfRZowr5PFPzxweElpiACy8v3VVqeJR56SjX96BkeK6dlt0E0qmOj71Ne-kupy7YSOJEhqliTpIbrHu4CEWHQLnRbUTYOooDmWEaxFSw2KJXyGbAe6CJTVf6J297EuBsnbnXXve-wNPJJgzz7voT8aBi0CRYNmKdt8GJMjofahwJ~ZwRnuMHmhksaIq0avmHnn2V9~7StTOwuHgghy8rI-Kr2g__)
*ภาพที่ 6.1: แผนภาพแสดงโครงสร้างพื้นฐานของโครงข่ายประสาทเทียมที่มี 2 Hidden Layers*

### หลักการทำงานของ Convolutional Neural Networks (CNN)

แม้ว่า Neural Network ทั่วไปจะสามารถใช้กับรูปภาพได้ แต่ก็มีข้อจำกัดเมื่อภาพมีขนาดใหญ่มากๆ CNN จึงถูกออกแบบมาเพื่อแก้ปัญหานี้โดยเฉพาะ โดยเลียนแบบการทำงานของเปลือกสมองส่วนการมองเห็น (Visual Cortex) ของมนุษย์ หัวใจของ CNN ประกอบด้วย Layer พิเศษ 2 ชนิดคือ:

1.  **Convolution Layer:** ทำหน้าที่เหมือนเป็น "แว่นขยาย" ที่เลื่อนไปทั่วทั้งภาพเพื่อตรวจจับคุณลักษณะพื้นฐานต่างๆ เช่น เส้นขอบ, มุม, หรือสี โดยแว่นขยายนี้เรียกว่า **ฟิลเตอร์ (Filter)** หรือ **เคอร์เนล (Kernel)** ฟิลเตอร์แต่ละตัวจะเรียนรู้ที่จะมองหาคุณลักษณะที่แตกต่างกันไป ผลลัพธ์ที่ได้จากชั้นนี้เรียกว่า **Feature Map**

2.  **Pooling Layer:** ทำหน้าที่ลดขนาดของ Feature Map (Downsampling) เพื่อลดภาระการคำนวณและทำให้โมเดลสามารถมองเห็นภาพรวมที่กว้างขึ้น วิธีที่นิยมที่สุดคือ **Max Pooling** ซึ่งจะเลือกเอาเฉพาะค่าที่สว่างที่สุด (ค่าสูงสุด) จากแต่ละส่วนของ Feature Map มาใช้ต่อ

สถาปัตยกรรมของ CNN จะวาง Convolution Layer และ Pooling Layer สลับกันไปหลายๆ ชั้น เพื่อสกัดคุณลักษณะจากง่ายไปซับซ้อน (เช่น จากเส้นขอบ > ดวงตา/จมูก > ใบหน้า) จากนั้นจึงส่งต่อข้อมูลที่ถูกย่อยแล้วไปยัง **Fully Connected Layer** (ซึ่งก็คือ Neural Network แบบปกติ) เพื่อทำการจำแนกประเภทในขั้นตอนสุดท้าย

![สถาปัตยกรรม CNN](https://private-us-east-1.manuscdn.com/sessionFile/OO4QhUUsaoBTGAbGU9i0j2/sandbox/pRb06yRMC7k7XW9CBSc5bm-images_1760366739187_na1fn_L2hvbWUvdWJ1bnR1L2RpYWdyYW1zL2Nubl9hcmNoaXRlY3R1cmU.png?Policy=eyJTdGF0ZW1lbnQiOlt7IlJlc291cmNlIjoiaHR0cHM6Ly9wcml2YXRlLXVzLWVhc3QtMS5tYW51c2Nkbi5jb20vc2Vzc2lvbkZpbGUvT080UWhVVXNhb0JUR0FiR1U5aTBqMi9zYW5kYm94L3BSYjA2eVJNQzdrN1hXOUNCU2M1Ym0taW1hZ2VzXzE3NjAzNjY3MzkxODdfbmExZm5fTDJodmJXVXZkV0oxYm5SMUwyUnBZV2R5WVcxekwyTnVibDloY21Ob2FYUmxZM1IxY21VLnBuZyIsIkNvbmRpdGlvbiI6eyJEYXRlTGVzc1RoYW4iOnsiQVdTOkVwb2NoVGltZSI6MTc5ODc2MTYwMH19fV19&Key-Pair-Id=K2HSFNDJXOU9YS&Signature=q1V~jKmjp4gQeQjce5KnyFmPhbi3RA5OTxwikovVbtFUQ~Y8~S5Crxq4DFhZiEC0IjAx-8WjeCz2qgK2mraZXjvJTmoUnRViEDBEQgBobGCt9huCAo4BIySgEbFbitIHIso-RBYKHTlm0Oo3c93iSyQSYjLrMt-t-fB0y7Ib9tXkNhXI5xyvn5nh40HDKZ1lf-gTAoaWWd-XNd~MjcjaHFvcOQIV3JlB5AgXA5JT~byMf03JazMEqg7vUexeNK23AtE1gmB0DxsAStEYRQzOvnh2W6G0w~75FMMO6xM7HDytDMlrJMCsfKr~3l2D0-4~epeFJSInjNEGtBD49IABvw__)
*ภาพที่ 6.2: แผนภาพแสดงสถาปัตยกรรมโดยทั่วไปของ CNN สำหรับการจำแนกประเภทรูปภาพ*

### การสร้างโมเดลจำแนกรูปภาพ (Image Classification) ด้วย TensorFlow

**TensorFlow** (พัฒนาโดย Google) และ **PyTorch** (พัฒนาโดย Facebook) คือสองไลบรารีที่ได้รับความนิยมสูงสุดสำหรับการสร้างโมเดล Deep Learning ในที่นี้ เราจะแสดงตัวอย่างการสร้างโมเดล CNN อย่างง่ายด้วย **Keras API** ซึ่งเป็น API ระดับสูงที่ทำงานอยู่บน TensorFlow ทำให้การสร้างโมเดลเป็นไปอย่างง่ายและรวดเร็ว

**เป้าหมาย:** สร้างโมเดลเพื่อจำแนกรูปภาพจากชุดข้อมูล CIFAR-10 ซึ่งเป็นชุดข้อมูลมาตรฐานที่ประกอบด้วยรูปภาพขนาด 32x32 พิกเซล 10 ประเภท (เช่น เครื่องบิน, รถยนต์, นก, แมว, กวาง, สุนัข, กบ, ม้า, เรือ, รถบรรทุก)

```python
import tensorflow as tf
from tensorflow.keras import layers, models

# 1. สร้างโครงสร้างโมเดลแบบ Sequential
model = models.Sequential()

# 2. เพิ่ม Convolutional and Pooling Layers
# Input shape คือ (32, 32, 3) สำหรับภาพสีขนาด 32x32
model.add(layers.Conv2D(32, (3, 3), activation='relu', input_shape=(32, 32, 3)))
model.add(layers.MaxPooling2D((2, 2)))
model.add(layers.Conv2D(64, (3, 3), activation='relu'))
model.add(layers.MaxPooling2D((2, 2)))
model.add(layers.Conv2D(64, (3, 3), activation='relu'))

# 3. เพิ่ม Fully Connected Layers
model.add(layers.Flatten()) # แปลง Feature Map 2D ให้เป็น 1D
model.add(layers.Dense(64, activation='relu'))
model.add(layers.Dense(10)) # Output Layer มี 10 นิวรอนสำหรับ 10 คลาส

# 4. ดูสรุปโครงสร้างของโมเดล
model.summary()

# 5. คอมไพล์โมเดล
# กำหนด Optimizer, Loss Function, และ Metrics ที่จะใช้วัดผล
model.compile(optimizer='adam',
              loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
              metrics=['accuracy'])

# ตอนนี้โมเดลของเราพร้อมที่จะรับข้อมูลเพื่อทำการฝึกสอน (Training) แล้ว
```

**ผลลัพธ์จาก `model.summary()`:**

```
Model: "sequential"
_________________________________________________________________
 Layer (type)                Output Shape              Param #   
=================================================================
 conv2d (Conv2D)             (None, 30, 30, 32)        896       
                                                                 
 max_pooling2d (MaxPooling2D) (None, 15, 15, 32)        0         
                                                                 
 conv2d_1 (Conv2D)           (None, 13, 13, 64)        18496     
                                                                 
 max_pooling2d_1 (MaxPooling2D) (None, 6, 6, 64)         0         
                                                                 
 conv2d_2 (Conv2D)           (None, 4, 4, 64)          36928     
                                                                 
 flatten (Flatten)           (None, 1024)              0         
                                                                 
 dense (Dense)               (None, 64)                65600     
                                                                 
 dense_1 (Dense)             (None, 10)                650       
                                                                 
=================================================================
Total params: 122,570
Trainable params: 122,570
Non-trainable params: 0
_________________________________________________________________
```

จากโค้ดตัวอย่าง เราได้สร้างโมเดล CNN ที่พร้อมใช้งานแล้ว จะเห็นว่า Keras ทำให้เราสามารถสร้างสถาปัตยกรรมที่ซับซ้อนได้ด้วยโค้ดเพียงไม่กี่บรรทัด ในบทสุดท้าย เราจะนำโมเดลนี้ไปฝึกสอนกับข้อมูลจริง และสร้างเป็นโปรเจกต์ที่สมบูรณ์

