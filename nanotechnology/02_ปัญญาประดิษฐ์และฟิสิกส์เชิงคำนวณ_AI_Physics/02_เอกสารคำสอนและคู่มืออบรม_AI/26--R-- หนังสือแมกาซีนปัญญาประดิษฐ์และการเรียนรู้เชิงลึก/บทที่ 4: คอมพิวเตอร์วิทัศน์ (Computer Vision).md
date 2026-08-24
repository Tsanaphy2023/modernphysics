# บทที่ 4: คอมพิวเตอร์วิทัศน์ (Computer Vision)

## 4.1 คอมพิวเตอร์วิทัศน์คืออะไร?

Computer Vision หรือคอมพิวเตอร์วิทัศน์ เป็นสาขาหนึ่งของปัญญาประดิษฐ์ที่มุ่งเน้นให้คอมพิวเตอร์สามารถ "มองเห็น" "เข้าใจ" และ "ตีความ" ข้อมูลภาพได้เหมือนมนุษย์

### คำนิยามของ Computer Vision

**Computer Vision** คือ เทคโนโลยีที่ช่วยให้คอมพิวเตอร์สามารถประมวลผล วิเคราะห์ และเข้าใจเนื้อหาในภาพหรือวิดีโอได้ โดยใช้อัลกอริทึมและเทคนิคทางคณิตศาสตร์

### วิวัฒนาการของ Computer Vision

#### ยุค 1960s-1970s: จุดเริ่มต้น
- การประมวลผลภาพพื้นฐาน (Basic Image Processing)
- การตรวจจับขอบ (Edge Detection)
- การกรองภาพ (Image Filtering)

#### ยุค 1980s-1990s: การพัฒนาอัลกอริทึม
- การจดจำรูปแบบ (Pattern Recognition)
- การแยกส่วนภาพ (Image Segmentation)
- การสร้างแบบจำลอง 3 มิติ

#### ยุค 2000s-2010s: Machine Learning
- Support Vector Machines (SVM)
- Random Forest
- Feature Engineering

#### ยุค 2010s-ปัจจุบัน: Deep Learning
- Convolutional Neural Networks (CNN)
- Object Detection (YOLO, R-CNN)
- Image Segmentation (U-Net, Mask R-CNN)

### ความสำคัญของ Computer Vision ในการเกษตร

#### 1. การตรวจสอบคุณภาพผลผลิต
- ตรวจจับความสุกของผลไม้
- ประเมินขนาดและรูปร่าง
- ตรวจหาความเสียหาย

#### 2. การตรวจจับโรคและศัตรูพืช
- วิเคราะห์อาการบนใบไม้
- ตรวจจับแมลงศัตรูพืช
- ประเมินความรุนแรงของโรค

#### 3. การติดตามการเจริญเติบโต
- วัดความสูงของพืช
- นับจำนวนใบและกิ่ง
- ประเมินความหนาแน่นของพืช

#### 4. การจัดการทรัพยากร
- ตรวจสอบระดับน้ำ
- ประเมินความชื้นของดิน
- วิเคราะห์การใช้ปุ๋ย

## 4.2 หลักการพื้นฐานของ Computer Vision

### 4.2.1 ภาพดิจิทัล (Digital Images)

#### โครงสร้างของภาพดิจิทัล
ภาพดิจิทัลประกอบด้วย **พิกเซล (Pixels)** ที่เรียงตัวเป็นตาราง 2 มิติ

```python
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import cv2

# ตัวอย่างการสร้างภาพง่ายๆ
def create_simple_image():
    """สร้างภาพง่ายๆ เพื่อแสดงโครงสร้างพิกเซล"""
    
    # สร้างภาพ 8x8 พิกเซล
    image = np.zeros((8, 8, 3), dtype=np.uint8)
    
    # วาดรูปใบไม้ง่ายๆ
    # ลำต้น (สีน้ำตาล)
    image[6:8, 3:5] = [139, 69, 19]  # Brown
    
    # ใบไม้ (สีเขียว)
    image[2:6, 1:7] = [34, 139, 34]  # Forest Green
    
    # เส้นกลางใบ (สีเขียวเข้ม)
    image[2:6, 3:4] = [0, 100, 0]  # Dark Green
    
    return image

# แสดงภาพและโครงสร้างพิกเซล
simple_img = create_simple_image()

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

# แสดงภาพ
ax1.imshow(simple_img)
ax1.set_title('ภาพใบไม้ง่ายๆ (8×8 พิกเซล)')
ax1.grid(True, color='white', linewidth=2)
ax1.set_xticks(range(8))
ax1.set_yticks(range(8))

# แสดงค่า RGB ของแต่ละพิกเซล
ax2.imshow(simple_img)
for i in range(8):
    for j in range(8):
        r, g, b = simple_img[i, j]
        ax2.text(j, i, f'{r},{g},{b}', ha='center', va='center', 
                fontsize=6, color='white' if r+g+b < 200 else 'black')

ax2.set_title('ค่า RGB ของแต่ละพิกเซล')
ax2.set_xticks(range(8))
ax2.set_yticks(range(8))

plt.tight_layout()
# plt.show()
```

#### ประเภทของภาพดิจิทัล

##### 1. Grayscale Images (ภาพขาวดำ)
- มีค่าความเข้มแสง 0-255
- 0 = สีดำ, 255 = สีขาว
- ใช้หน่วยความจำน้อย

##### 2. RGB Images (ภาพสี)
- ประกอบด้วย 3 ช่อง: Red, Green, Blue
- แต่ละช่องมีค่า 0-255
- รวม 16.7 ล้านสี

##### 3. HSV Images
- Hue (สีสัน), Saturation (ความอิ่มตัว), Value (ความสว่าง)
- เหมาะสำหรับการแยกสี

```python
def demonstrate_color_spaces():
    """สาธิตการแปลงระบบสี"""
    
    # สร้างภาพตัวอย่าง (ใบไม้)
    original = np.zeros((100, 100, 3), dtype=np.uint8)
    
    # วาดใบไม้
    cv2.circle(original, (50, 50), 40, (34, 139, 34), -1)  # Green leaf
    cv2.ellipse(original, (50, 50), (35, 20), 45, 0, 360, (0, 100, 0), 2)  # Vein
    
    # แปลงเป็น Grayscale
    gray = cv2.cvtColor(original, cv2.COLOR_RGB2GRAY)
    
    # แปลงเป็น HSV
    hsv = cv2.cvtColor(original, cv2.COLOR_RGB2HSV)
    
    # แสดงผล
    fig, axes = plt.subplots(2, 2, figsize=(12, 10))
    
    axes[0,0].imshow(original)
    axes[0,0].set_title('Original (RGB)')
    
    axes[0,1].imshow(gray, cmap='gray')
    axes[0,1].set_title('Grayscale')
    
    axes[1,0].imshow(hsv[:,:,0], cmap='hsv')
    axes[1,0].set_title('HSV - Hue Channel')
    
    axes[1,1].imshow(hsv[:,:,2], cmap='gray')
    axes[1,1].set_title('HSV - Value Channel')
    
    for ax in axes.flat:
        ax.axis('off')
    
    plt.tight_layout()
    # plt.show()

# demonstrate_color_spaces()
```

### 4.2.2 การประมวลผลภาพพื้นฐาน

#### 1. Image Filtering (การกรองภาพ)

การกรองภาพใช้เพื่อลดสัญญาณรบกวน เพิ่มความคมชัด หรือเตรียมภาพสำหรับการวิเคราะห์

##### Gaussian Blur - ลดสัญญาณรบกวน
```python
def apply_gaussian_blur(image, kernel_size=5):
    """ใช้ Gaussian Blur เพื่อลดสัญญาณรบกวน"""
    return cv2.GaussianBlur(image, (kernel_size, kernel_size), 0)
```

##### Sharpening - เพิ่มความคมชัด
```python
def apply_sharpening(image):
    """เพิ่มความคมชัดของภาพ"""
    kernel = np.array([[-1,-1,-1],
                      [-1, 9,-1],
                      [-1,-1,-1]])
    return cv2.filter2D(image, -1, kernel)
```

#### 2. Edge Detection (การตรวจจับขอบ)

การตรวจจับขอบเป็นขั้นตอนสำคัญในการวิเคราะห์รูปร่างของวัตถุ

##### Sobel Edge Detection
```python
def sobel_edge_detection(image):
    """ตรวจจับขอบด้วย Sobel operator"""
    
    # แปลงเป็น grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    
    # Sobel X และ Y
    sobel_x = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3)
    sobel_y = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=3)
    
    # รวม gradient
    sobel_combined = np.sqrt(sobel_x**2 + sobel_y**2)
    
    return sobel_combined

# ตัวอย่างการใช้งาน
def edge_detection_demo():
    """สาธิตการตรวจจับขอบ"""
    
    # สร้างภาพใบไม้ตัวอย่าง
    image = np.zeros((200, 200, 3), dtype=np.uint8)
    
    # วาดใบไม้
    points = np.array([[100, 50], [150, 100], [100, 150], [50, 100]], np.int32)
    cv2.fillPoly(image, [points], (34, 139, 34))
    
    # เพิ่มเส้นกลางใบ
    cv2.line(image, (100, 50), (100, 150), (0, 100, 0), 3)
    
    # ตรวจจับขอบ
    edges = sobel_edge_detection(image)
    
    # แสดงผล
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
    
    ax1.imshow(image)
    ax1.set_title('ภาพต้นฉบับ')
    ax1.axis('off')
    
    ax2.imshow(edges, cmap='gray')
    ax2.set_title('การตรวจจับขอบ (Sobel)')
    ax2.axis('off')
    
    plt.tight_layout()
    # plt.show()

# edge_detection_demo()
```

##### Canny Edge Detection
```python
def canny_edge_detection(image, low_threshold=50, high_threshold=150):
    """ตรวจจับขอบด้วย Canny algorithm"""
    
    gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    
    # ลด noise ด้วย Gaussian blur
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    
    # Canny edge detection
    edges = cv2.Canny(blurred, low_threshold, high_threshold)
    
    return edges
```

#### 3. Morphological Operations (การดำเนินการทางสัณฐานวิทยา)

ใช้สำหรับการปรับปรุงรูปร่างของวัตถุในภาพ

##### Erosion และ Dilation
```python
def morphological_operations(image):
    """สาธิตการดำเนินการทางสัณฐานวิทยา"""
    
    # แปลงเป็น binary image
    gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    _, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
    
    # สร้าง kernel
    kernel = np.ones((5,5), np.uint8)
    
    # Erosion - ทำให้วัตถุเล็กลง
    erosion = cv2.erode(binary, kernel, iterations=1)
    
    # Dilation - ทำให้วัตถุใหญ่ขึ้น
    dilation = cv2.dilate(binary, kernel, iterations=1)
    
    # Opening - Erosion ตามด้วย Dilation
    opening = cv2.morphologyEx(binary, cv2.MORPH_OPEN, kernel)
    
    # Closing - Dilation ตามด้วย Erosion
    closing = cv2.morphologyEx(binary, cv2.MORPH_CLOSE, kernel)
    
    return binary, erosion, dilation, opening, closing
```

### 4.2.3 Feature Extraction (การสกัดคุณลักษณะ)

การสกัดคุณลักษณะเป็นกระบวนการแปลงภาพให้เป็นข้อมูลเชิงตัวเลขที่สามารถใช้ในการวิเคราะห์ได้

#### 1. Color Features (คุณลักษณะสี)

##### Color Histogram
```python
def extract_color_histogram(image, bins=256):
    """สกัดฮิสโตแกรมสี"""
    
    # คำนวณฮิสโตแกรมสำหรับแต่ละช่องสี
    hist_r = cv2.calcHist([image], [0], None, [bins], [0, 256])
    hist_g = cv2.calcHist([image], [1], None, [bins], [0, 256])
    hist_b = cv2.calcHist([image], [2], None, [bins], [0, 256])
    
    return hist_r.flatten(), hist_g.flatten(), hist_b.flatten()

def plot_color_histogram(image):
    """แสดงฮิสโตแกรมสี"""
    
    hist_r, hist_g, hist_b = extract_color_histogram(image)
    
    plt.figure(figsize=(12, 4))
    
    plt.subplot(1, 3, 1)
    plt.plot(hist_r, color='red', alpha=0.7)
    plt.title('Red Channel Histogram')
    plt.xlabel('Pixel Intensity')
    plt.ylabel('Frequency')
    
    plt.subplot(1, 3, 2)
    plt.plot(hist_g, color='green', alpha=0.7)
    plt.title('Green Channel Histogram')
    plt.xlabel('Pixel Intensity')
    plt.ylabel('Frequency')
    
    plt.subplot(1, 3, 3)
    plt.plot(hist_b, color='blue', alpha=0.7)
    plt.title('Blue Channel Histogram')
    plt.xlabel('Pixel Intensity')
    plt.ylabel('Frequency')
    
    plt.tight_layout()
    # plt.show()
```

##### Color Moments
```python
def extract_color_moments(image):
    """สกัด Color Moments (Mean, Std, Skewness)"""
    
    moments = []
    
    for channel in range(3):  # RGB channels
        channel_data = image[:, :, channel].flatten()
        
        # Mean (ค่าเฉลี่ย)
        mean = np.mean(channel_data)
        
        # Standard Deviation (ส่วนเบี่ยงเบนมาตรฐาน)
        std = np.std(channel_data)
        
        # Skewness (ความเบ้)
        skewness = np.mean(((channel_data - mean) / std) ** 3)
        
        moments.extend([mean, std, skewness])
    
    return np.array(moments)
```

#### 2. Texture Features (คุณลักษณะเนื้อผิว)

##### Local Binary Pattern (LBP)
```python
def local_binary_pattern(image, radius=1, n_points=8):
    """คำนวณ Local Binary Pattern"""
    
    gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    
    # สร้าง LBP
    lbp = np.zeros_like(gray)
    
    for i in range(radius, gray.shape[0] - radius):
        for j in range(radius, gray.shape[1] - radius):
            center = gray[i, j]
            binary_string = ""
            
            # ตรวจสอบ 8 จุดรอบๆ
            for angle in range(0, 360, 45):
                x = int(i + radius * np.cos(np.radians(angle)))
                y = int(j + radius * np.sin(np.radians(angle)))
                
                if gray[x, y] >= center:
                    binary_string += "1"
                else:
                    binary_string += "0"
            
            # แปลงเป็นเลขฐาน 10
            lbp[i, j] = int(binary_string, 2)
    
    return lbp

def extract_lbp_histogram(image, bins=256):
    """สกัดฮิสโตแกรม LBP"""
    
    lbp = local_binary_pattern(image)
    hist, _ = np.histogram(lbp.flatten(), bins=bins, range=(0, bins))
    
    return hist
```

##### Gray Level Co-occurrence Matrix (GLCM)
```python
from skimage.feature import graycomatrix, graycoprops

def extract_glcm_features(image, distances=[1], angles=[0, 45, 90, 135]):
    """สกัดคุณลักษณะจาก GLCM"""
    
    gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    
    # คำนวณ GLCM
    glcm = graycomatrix(gray, distances=distances, angles=np.radians(angles), 
                       levels=256, symmetric=True, normed=True)
    
    # สกัดคุณลักษณะ
    features = {}
    features['contrast'] = graycoprops(glcm, 'contrast').mean()
    features['dissimilarity'] = graycoprops(glcm, 'dissimilarity').mean()
    features['homogeneity'] = graycoprops(glcm, 'homogeneity').mean()
    features['energy'] = graycoprops(glcm, 'energy').mean()
    features['correlation'] = graycoprops(glcm, 'correlation').mean()
    
    return features
```

#### 3. Shape Features (คุณลักษณะรูปร่าง)

##### Contour Analysis
```python
def extract_shape_features(image):
    """สกัดคุณลักษณะรูปร่าง"""
    
    # แปลงเป็น binary image
    gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    _, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
    
    # หา contours
    contours, _ = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    if len(contours) == 0:
        return {}
    
    # เลือก contour ที่ใหญ่ที่สุด
    largest_contour = max(contours, key=cv2.contourArea)
    
    # คำนวณคุณลักษณะ
    features = {}
    
    # Area (พื้นที่)
    features['area'] = cv2.contourArea(largest_contour)
    
    # Perimeter (เส้นรอบรูป)
    features['perimeter'] = cv2.arcLength(largest_contour, True)
    
    # Aspect Ratio (อัตราส่วน)
    x, y, w, h = cv2.boundingRect(largest_contour)
    features['aspect_ratio'] = float(w) / h
    
    # Extent (ความกะทัดรัด)
    rect_area = w * h
    features['extent'] = float(features['area']) / rect_area
    
    # Solidity (ความทึบ)
    hull = cv2.convexHull(largest_contour)
    hull_area = cv2.contourArea(hull)
    features['solidity'] = float(features['area']) / hull_area
    
    # Circularity (ความเป็นวงกลม)
    features['circularity'] = 4 * np.pi * features['area'] / (features['perimeter'] ** 2)
    
    return features
```

## 4.3 Deep Learning สำหรับ Computer Vision

### 4.3.1 Convolutional Neural Networks (CNN) - ทบทวนเชิงลึก

CNN เป็นสถาปัตยกรรมที่เหมาะสมที่สุดสำหรับการประมวลผลภาพ เนื่องจากสามารถเรียนรู้คุณลักษณะของภาพได้อย่างอัตโนมัติ

#### โครงสร้างของ CNN

##### 1. Convolutional Layer
```python
def demonstrate_convolution():
    """สาธิตการทำงานของ Convolution"""
    
    # สร้างภาพตัวอย่าง
    image = np.array([
        [1, 1, 1, 0, 0],
        [0, 1, 1, 1, 0],
        [0, 0, 1, 1, 1],
        [0, 0, 1, 1, 0],
        [0, 1, 1, 0, 0]
    ], dtype=np.float32)
    
    # Filter สำหรับตรวจจับขอบแนวตั้ง
    vertical_filter = np.array([
        [-1, 0, 1],
        [-1, 0, 1],
        [-1, 0, 1]
    ], dtype=np.float32)
    
    # Filter สำหรับตรวจจับขอบแนวนอน
    horizontal_filter = np.array([
        [-1, -1, -1],
        [ 0,  0,  0],
        [ 1,  1,  1]
    ], dtype=np.float32)
    
    # ทำ convolution
    def convolve2d(image, kernel):
        result = np.zeros((3, 3))
        for i in range(3):
            for j in range(3):
                result[i, j] = np.sum(image[i:i+3, j:j+3] * kernel)
        return result
    
    vertical_result = convolve2d(image, vertical_filter)
    horizontal_result = convolve2d(image, horizontal_filter)
    
    # แสดงผล
    fig, axes = plt.subplots(2, 3, figsize=(15, 10))
    
    # แถวบน: Vertical edge detection
    axes[0, 0].imshow(image, cmap='gray')
    axes[0, 0].set_title('Original Image')
    
    axes[0, 1].imshow(vertical_filter, cmap='RdBu')
    axes[0, 1].set_title('Vertical Edge Filter')
    
    axes[0, 2].imshow(vertical_result, cmap='RdBu')
    axes[0, 2].set_title('Vertical Edges Detected')
    
    # แถวล่าง: Horizontal edge detection
    axes[1, 0].imshow(image, cmap='gray')
    axes[1, 0].set_title('Original Image')
    
    axes[1, 1].imshow(horizontal_filter, cmap='RdBu')
    axes[1, 1].set_title('Horizontal Edge Filter')
    
    axes[1, 2].imshow(horizontal_result, cmap='RdBu')
    axes[1, 2].set_title('Horizontal Edges Detected')
    
    for ax in axes.flat:
        ax.axis('off')
    
    plt.tight_layout()
    # plt.show()

# demonstrate_convolution()
```

##### 2. Pooling Layer
```python
def demonstrate_pooling():
    """สาธิตการทำงานของ Pooling"""
    
    # สร้าง feature map ตัวอย่าง
    feature_map = np.array([
        [1, 3, 2, 4],
        [5, 6, 1, 2],
        [3, 2, 4, 7],
        [1, 4, 6, 8]
    ], dtype=np.float32)
    
    # Max Pooling 2x2
    def max_pool_2x2(matrix):
        result = np.zeros((2, 2))
        for i in range(2):
            for j in range(2):
                pool_region = matrix[i*2:(i+1)*2, j*2:(j+1)*2]
                result[i, j] = np.max(pool_region)
        return result
    
    # Average Pooling 2x2
    def avg_pool_2x2(matrix):
        result = np.zeros((2, 2))
        for i in range(2):
            for j in range(2):
                pool_region = matrix[i*2:(i+1)*2, j*2:(j+1)*2]
                result[i, j] = np.mean(pool_region)
        return result
    
    max_pooled = max_pool_2x2(feature_map)
    avg_pooled = avg_pool_2x2(feature_map)
    
    # แสดงผล
    fig, axes = plt.subplots(1, 3, figsize=(15, 5))
    
    im1 = axes[0].imshow(feature_map, cmap='viridis')
    axes[0].set_title('Original Feature Map (4×4)')
    plt.colorbar(im1, ax=axes[0])
    
    im2 = axes[1].imshow(max_pooled, cmap='viridis')
    axes[1].set_title('Max Pooling (2×2)')
    plt.colorbar(im2, ax=axes[1])
    
    im3 = axes[2].imshow(avg_pooled, cmap='viridis')
    axes[2].set_title('Average Pooling (2×2)')
    plt.colorbar(im3, ax=axes[2])
    
    # เพิ่มค่าในแต่ละช่อง
    for i in range(4):
        for j in range(4):
            axes[0].text(j, i, f'{feature_map[i,j]:.0f}', ha='center', va='center', 
                        color='white', fontweight='bold')
    
    for i in range(2):
        for j in range(2):
            axes[1].text(j, i, f'{max_pooled[i,j]:.0f}', ha='center', va='center', 
                        color='white', fontweight='bold')
            axes[2].text(j, i, f'{avg_pooled[i,j]:.1f}', ha='center', va='center', 
                        color='white', fontweight='bold')
    
    plt.tight_layout()
    # plt.show()

# demonstrate_pooling()
```

### 4.3.2 สถาปัตยกรรม CNN ที่นิยม

#### 1. LeNet-5 (1998)
```python
import tensorflow as tf
from tensorflow.keras import layers, models

def create_lenet5():
    """สร้าง LeNet-5 architecture"""
    
    model = models.Sequential([
        layers.Conv2D(6, (5, 5), activation='tanh', input_shape=(32, 32, 1)),
        layers.AveragePooling2D((2, 2)),
        layers.Conv2D(16, (5, 5), activation='tanh'),
        layers.AveragePooling2D((2, 2)),
        layers.Flatten(),
        layers.Dense(120, activation='tanh'),
        layers.Dense(84, activation='tanh'),
        layers.Dense(10, activation='softmax')
    ])
    
    return model
```

#### 2. AlexNet (2012)
```python
def create_alexnet():
    """สร้าง AlexNet architecture (ปรับแต่ง)"""
    
    model = models.Sequential([
        layers.Conv2D(96, (11, 11), strides=4, activation='relu', input_shape=(224, 224, 3)),
        layers.MaxPooling2D((3, 3), strides=2),
        
        layers.Conv2D(256, (5, 5), padding='same', activation='relu'),
        layers.MaxPooling2D((3, 3), strides=2),
        
        layers.Conv2D(384, (3, 3), padding='same', activation='relu'),
        layers.Conv2D(384, (3, 3), padding='same', activation='relu'),
        layers.Conv2D(256, (3, 3), padding='same', activation='relu'),
        layers.MaxPooling2D((3, 3), strides=2),
        
        layers.Flatten(),
        layers.Dense(4096, activation='relu'),
        layers.Dropout(0.5),
        layers.Dense(4096, activation='relu'),
        layers.Dropout(0.5),
        layers.Dense(1000, activation='softmax')
    ])
    
    return model
```

#### 3. VGG-16 (2014)
```python
def create_vgg16():
    """สร้าง VGG-16 architecture"""
    
    model = models.Sequential([
        # Block 1
        layers.Conv2D(64, (3, 3), activation='relu', padding='same', input_shape=(224, 224, 3)),
        layers.Conv2D(64, (3, 3), activation='relu', padding='same'),
        layers.MaxPooling2D((2, 2), strides=(2, 2)),
        
        # Block 2
        layers.Conv2D(128, (3, 3), activation='relu', padding='same'),
        layers.Conv2D(128, (3, 3), activation='relu', padding='same'),
        layers.MaxPooling2D((2, 2), strides=(2, 2)),
        
        # Block 3
        layers.Conv2D(256, (3, 3), activation='relu', padding='same'),
        layers.Conv2D(256, (3, 3), activation='relu', padding='same'),
        layers.Conv2D(256, (3, 3), activation='relu', padding='same'),
        layers.MaxPooling2D((2, 2), strides=(2, 2)),
        
        # Block 4
        layers.Conv2D(512, (3, 3), activation='relu', padding='same'),
        layers.Conv2D(512, (3, 3), activation='relu', padding='same'),
        layers.Conv2D(512, (3, 3), activation='relu', padding='same'),
        layers.MaxPooling2D((2, 2), strides=(2, 2)),
        
        # Block 5
        layers.Conv2D(512, (3, 3), activation='relu', padding='same'),
        layers.Conv2D(512, (3, 3), activation='relu', padding='same'),
        layers.Conv2D(512, (3, 3), activation='relu', padding='same'),
        layers.MaxPooling2D((2, 2), strides=(2, 2)),
        
        # Classifier
        layers.Flatten(),
        layers.Dense(4096, activation='relu'),
        layers.Dense(4096, activation='relu'),
        layers.Dense(1000, activation='softmax')
    ])
    
    return model
```

#### 4. ResNet (2015)
```python
def residual_block(x, filters, stride=1):
    """สร้าง Residual Block"""
    
    # Shortcut connection
    shortcut = x
    
    # Main path
    x = layers.Conv2D(filters, (3, 3), strides=stride, padding='same')(x)
    x = layers.BatchNormalization()(x)
    x = layers.ReLU()(x)
    
    x = layers.Conv2D(filters, (3, 3), padding='same')(x)
    x = layers.BatchNormalization()(x)
    
    # Adjust shortcut if needed
    if stride != 1:
        shortcut = layers.Conv2D(filters, (1, 1), strides=stride)(shortcut)
        shortcut = layers.BatchNormalization()(shortcut)
    
    # Add shortcut
    x = layers.Add()([x, shortcut])
    x = layers.ReLU()(x)
    
    return x

def create_resnet18():
    """สร้าง ResNet-18 architecture"""
    
    inputs = layers.Input(shape=(224, 224, 3))
    
    # Initial convolution
    x = layers.Conv2D(64, (7, 7), strides=2, padding='same')(inputs)
    x = layers.BatchNormalization()(x)
    x = layers.ReLU()(x)
    x = layers.MaxPooling2D((3, 3), strides=2, padding='same')(x)
    
    # Residual blocks
    x = residual_block(x, 64)
    x = residual_block(x, 64)
    
    x = residual_block(x, 128, stride=2)
    x = residual_block(x, 128)
    
    x = residual_block(x, 256, stride=2)
    x = residual_block(x, 256)
    
    x = residual_block(x, 512, stride=2)
    x = residual_block(x, 512)
    
    # Global average pooling and classifier
    x = layers.GlobalAveragePooling2D()(x)
    outputs = layers.Dense(1000, activation='softmax')(x)
    
    model = models.Model(inputs, outputs)
    return model
```

## 4.4 การประยุกต์ใช้ Computer Vision ในการเกษตร

### 4.4.1 การตรวจจับและจำแนกโรคพืช

#### ปัญหาและความท้าทาย
- โรคพืชมีหลายชนิดและอาการที่คล้ายกัน
- การตรวจจับด้วยตาเปล่าต้องใช้ความเชี่ยวชาญ
- การแพร่กระจายของโรคเร็วมาก

#### วิธีการแก้ไขด้วย Computer Vision

##### 1. การเตรียมข้อมูล
```python
class PlantDiseaseDataset:
    """คลาสสำหรับจัดการข้อมูลโรคพืช"""
    
    def __init__(self, data_dir):
        self.data_dir = data_dir
        self.classes = ['healthy', 'bacterial_spot', 'early_blight', 'late_blight', 'leaf_mold']
        self.class_to_idx = {cls: idx for idx, cls in enumerate(self.classes)}
        
    def load_and_preprocess_image(self, image_path, target_size=(224, 224)):
        """โหลดและเตรียมภาพ"""
        
        # อ่านภาพ
        image = cv2.imread(image_path)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        
        # ปรับขนาด
        image = cv2.resize(image, target_size)
        
        # Normalize
        image = image.astype(np.float32) / 255.0
        
        return image
    
    def augment_image(self, image):
        """เพิ่มข้อมูลด้วย Data Augmentation"""
        
        # Random rotation
        if np.random.random() > 0.5:
            angle = np.random.randint(-30, 30)
            center = (image.shape[1]//2, image.shape[0]//2)
            matrix = cv2.getRotationMatrix2D(center, angle, 1.0)
            image = cv2.warpAffine(image, matrix, (image.shape[1], image.shape[0]))
        
        # Random flip
        if np.random.random() > 0.5:
            image = cv2.flip(image, 1)  # Horizontal flip
        
        # Random brightness
        if np.random.random() > 0.5:
            brightness = np.random.uniform(0.8, 1.2)
            image = np.clip(image * brightness, 0, 1)
        
        # Random noise
        if np.random.random() > 0.5:
            noise = np.random.normal(0, 0.02, image.shape)
            image = np.clip(image + noise, 0, 1)
        
        return image
```

##### 2. การสร้างโมเดล CNN
```python
def create_plant_disease_classifier():
    """สร้างโมเดลจำแนกโรคพืช"""
    
    model = models.Sequential([
        # Feature extraction layers
        layers.Conv2D(32, (3, 3), activation='relu', input_shape=(224, 224, 3)),
        layers.BatchNormalization(),
        layers.MaxPooling2D((2, 2)),
        
        layers.Conv2D(64, (3, 3), activation='relu'),
        layers.BatchNormalization(),
        layers.MaxPooling2D((2, 2)),
        
        layers.Conv2D(128, (3, 3), activation='relu'),
        layers.BatchNormalization(),
        layers.MaxPooling2D((2, 2)),
        
        layers.Conv2D(256, (3, 3), activation='relu'),
        layers.BatchNormalization(),
        layers.MaxPooling2D((2, 2)),
        
        # Classification layers
        layers.GlobalAveragePooling2D(),
        layers.Dense(512, activation='relu'),
        layers.Dropout(0.5),
        layers.Dense(256, activation='relu'),
        layers.Dropout(0.3),
        layers.Dense(5, activation='softmax')  # 5 classes
    ])
    
    # Compile model
    model.compile(
        optimizer='adam',
        loss='categorical_crossentropy',
        metrics=['accuracy', 'precision', 'recall']
    )
    
    return model

# Transfer Learning approach
def create_transfer_learning_model():
    """ใช้ Transfer Learning จาก pre-trained model"""
    
    # โหลด pre-trained VGG16
    base_model = tf.keras.applications.VGG16(
        weights='imagenet',
        include_top=False,
        input_shape=(224, 224, 3)
    )
    
    # Freeze base model
    base_model.trainable = False
    
    # เพิ่ม custom classifier
    model = models.Sequential([
        base_model,
        layers.GlobalAveragePooling2D(),
        layers.Dense(512, activation='relu'),
        layers.Dropout(0.5),
        layers.Dense(256, activation='relu'),
        layers.Dropout(0.3),
        layers.Dense(5, activation='softmax')
    ])
    
    model.compile(
        optimizer='adam',
        loss='categorical_crossentropy',
        metrics=['accuracy']
    )
    
    return model
```

##### 3. การฝึกและประเมินโมเดล
```python
def train_plant_disease_model():
    """ฝึกโมเดลจำแนกโรคพืช"""
    
    # สร้างโมเดล
    model = create_transfer_learning_model()
    
    # Callbacks
    callbacks = [
        tf.keras.callbacks.EarlyStopping(
            monitor='val_accuracy',
            patience=10,
            restore_best_weights=True
        ),
        tf.keras.callbacks.ReduceLROnPlateau(
            monitor='val_loss',
            factor=0.2,
            patience=5,
            min_lr=1e-7
        ),
        tf.keras.callbacks.ModelCheckpoint(
            'best_plant_disease_model.h5',
            monitor='val_accuracy',
            save_best_only=True
        )
    ]
    
    # Data generators (จำลอง)
    # train_generator = ... (ใช้ ImageDataGenerator)
    # val_generator = ... (ใช้ ImageDataGenerator)
    
    # ฝึกโมเดล
    # history = model.fit(
    #     train_generator,
    #     epochs=50,
    #     validation_data=val_generator,
    #     callbacks=callbacks
    # )
    
    return model

def evaluate_model_performance(model, test_data, test_labels):
    """ประเมินประสิทธิภาพของโมเดล"""
    
    # ทำนายผล
    predictions = model.predict(test_data)
    predicted_classes = np.argmax(predictions, axis=1)
    true_classes = np.argmax(test_labels, axis=1)
    
    # คำนวณ metrics
    from sklearn.metrics import classification_report, confusion_matrix
    
    # Classification report
    class_names = ['Healthy', 'Bacterial Spot', 'Early Blight', 'Late Blight', 'Leaf Mold']
    report = classification_report(true_classes, predicted_classes, 
                                 target_names=class_names, output_dict=True)
    
    # Confusion matrix
    cm = confusion_matrix(true_classes, predicted_classes)
    
    # แสดงผล
    plt.figure(figsize=(15, 5))
    
    # Confusion Matrix
    plt.subplot(1, 3, 1)
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', 
                xticklabels=class_names, yticklabels=class_names)
    plt.title('Confusion Matrix')
    plt.ylabel('True Label')
    plt.xlabel('Predicted Label')
    
    # Accuracy per class
    plt.subplot(1, 3, 2)
    accuracies = [report[cls]['f1-score'] for cls in class_names]
    plt.bar(class_names, accuracies, color='skyblue')
    plt.title('F1-Score per Class')
    plt.ylabel('F1-Score')
    plt.xticks(rotation=45)
    
    # Overall metrics
    plt.subplot(1, 3, 3)
    overall_metrics = ['Precision', 'Recall', 'F1-Score']
    overall_values = [
        report['weighted avg']['precision'],
        report['weighted avg']['recall'],
        report['weighted avg']['f1-score']
    ]
    plt.bar(overall_metrics, overall_values, color='lightgreen')
    plt.title('Overall Performance')
    plt.ylabel('Score')
    
    plt.tight_layout()
    plt.show()
    
    return report, cm
```

### 4.4.2 การนับและตรวจจับผลไม้

#### ความท้าทายในการนับผลไม้
- ผลไม้อาจบังกันหรือซ่อนอยู่ใต้ใบไม้
- ขนาดและสีที่แตกต่างกันตามระยะการเจริญเติบโต
- สภาพแสงที่เปลี่ยนแปลง

#### วิธีการแก้ไขด้วย Object Detection

##### 1. YOLO (You Only Look Once)
```python
def create_fruit_detection_yolo():
    """สร้างโมเดล YOLO สำหรับตรวจจับผลไม้"""
    
    # ใช้ YOLOv5 หรือ YOLOv8
    # ตัวอย่างการใช้ ultralytics
    
    from ultralytics import YOLO
    
    # โหลด pre-trained model
    model = YOLO('yolov8n.pt')
    
    # Fine-tune สำหรับผลไม้
    # model.train(data='fruit_dataset.yaml', epochs=100)
    
    return model

def detect_fruits_in_image(model, image_path):
    """ตรวจจับผลไม้ในภาพ"""
    
    # ทำนาย
    results = model(image_path)
    
    # ประมวลผลผลลัพธ์
    detections = []
    for result in results:
        boxes = result.boxes
        if boxes is not None:
            for box in boxes:
                # ข้อมูลของ bounding box
                x1, y1, x2, y2 = box.xyxy[0].cpu().numpy()
                confidence = box.conf[0].cpu().numpy()
                class_id = int(box.cls[0].cpu().numpy())
                
                detections.append({
                    'bbox': [x1, y1, x2, y2],
                    'confidence': confidence,
                    'class_id': class_id
                })
    
    return detections

def visualize_fruit_detection(image_path, detections, class_names):
    """แสดงผลการตรวจจับผลไม้"""
    
    # อ่านภาพ
    image = cv2.imread(image_path)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    
    # วาด bounding boxes
    for detection in detections:
        x1, y1, x2, y2 = detection['bbox']
        confidence = detection['confidence']
        class_id = detection['class_id']
        
        # วาดกรอบ
        cv2.rectangle(image, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), 2)
        
        # เขียนข้อความ
        label = f"{class_names[class_id]}: {confidence:.2f}"
        cv2.putText(image, label, (int(x1), int(y1)-10), 
                   cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
    
    # แสดงผล
    plt.figure(figsize=(12, 8))
    plt.imshow(image)
    plt.title(f'Fruit Detection - Found {len(detections)} fruits')
    plt.axis('off')
    plt.show()
    
    return len(detections)
```

##### 2. Mask R-CNN สำหรับ Instance Segmentation
```python
def create_fruit_segmentation_model():
    """สร้างโมเดล Mask R-CNN สำหรับแยกส่วนผลไม้"""
    
    import tensorflow as tf
    from tensorflow.keras.applications import ResNet50
    
    # สร้าง backbone (ResNet50)
    backbone = ResNet50(
        include_top=False,
        weights='imagenet',
        input_shape=(512, 512, 3)
    )
    
    # สร้าง Mask R-CNN architecture
    # (ในทางปฏิบัติจะใช้ library เช่น Detectron2)
    
    return backbone

def segment_fruits(image, model):
    """แยกส่วนผลไม้ในภาพ"""
    
    # ประมวลผลภาพ
    processed_image = preprocess_image_for_segmentation(image)
    
    # ทำนาย
    # masks, boxes, scores = model.predict(processed_image)
    
    # จำลองผลลัพธ์
    masks = np.random.rand(5, 512, 512) > 0.7  # 5 ผลไม้
    boxes = np.array([
        [100, 100, 200, 200],
        [250, 150, 350, 250],
        [400, 200, 500, 300],
        [150, 350, 250, 450],
        [350, 400, 450, 500]
    ])
    scores = np.array([0.95, 0.87, 0.92, 0.78, 0.83])
    
    return masks, boxes, scores

def visualize_fruit_segmentation(image, masks, boxes, scores, threshold=0.7):
    """แสดงผลการแยกส่วนผลไม้"""
    
    plt.figure(figsize=(15, 10))
    
    # แสดงภาพต้นฉบับ
    plt.subplot(2, 2, 1)
    plt.imshow(image)
    plt.title('Original Image')
    plt.axis('off')
    
    # แสดง bounding boxes
    plt.subplot(2, 2, 2)
    plt.imshow(image)
    for i, (box, score) in enumerate(zip(boxes, scores)):
        if score > threshold:
            x1, y1, x2, y2 = box
            rect = plt.Rectangle((x1, y1), x2-x1, y2-y1, 
                               fill=False, color='red', linewidth=2)
            plt.gca().add_patch(rect)
            plt.text(x1, y1-5, f'Fruit {i+1}: {score:.2f}', 
                    color='red', fontweight='bold')
    plt.title('Bounding Boxes')
    plt.axis('off')
    
    # แสดง masks
    plt.subplot(2, 2, 3)
    combined_mask = np.zeros_like(masks[0])
    colors = plt.cm.Set3(np.linspace(0, 1, len(masks)))
    
    for i, (mask, score) in enumerate(zip(masks, scores)):
        if score > threshold:
            combined_mask += mask * (i + 1)
    
    plt.imshow(image)
    plt.imshow(combined_mask, alpha=0.5, cmap='Set3')
    plt.title('Segmentation Masks')
    plt.axis('off')
    
    # แสดงสถิติ
    plt.subplot(2, 2, 4)
    valid_fruits = sum(1 for score in scores if score > threshold)
    fruit_sizes = []
    
    for i, (mask, score) in enumerate(zip(masks, scores)):
        if score > threshold:
            size = np.sum(mask)
            fruit_sizes.append(size)
    
    plt.bar(range(1, valid_fruits + 1), fruit_sizes, color='orange', alpha=0.7)
    plt.title('Fruit Sizes (pixels)')
    plt.xlabel('Fruit ID')
    plt.ylabel('Size (pixels)')
    
    plt.tight_layout()
    plt.show()
    
    return valid_fruits, fruit_sizes
```

### 4.4.3 การวิเคราะห์คุณภาพผลผลิต

#### การประเมินความสุกของผลไม้

##### 1. การวิเคราะห์สี
```python
def analyze_fruit_ripeness_by_color(image):
    """วิเคราะห์ความสุกจากสี"""
    
    # แปลงเป็น HSV
    hsv = cv2.cvtColor(image, cv2.COLOR_RGB2HSV)
    
    # กำหนดช่วงสีสำหรับความสุกต่างๆ (ตัวอย่าง: มะม่วง)
    # เขียว (ดิบ)
    green_lower = np.array([40, 50, 50])
    green_upper = np.array([80, 255, 255])
    
    # เหลือง (สุก)
    yellow_lower = np.array([20, 50, 50])
    yellow_upper = np.array([40, 255, 255])
    
    # แดง/ส้ม (สุกมาก)
    red_lower = np.array([0, 50, 50])
    red_upper = np.array([20, 255, 255])
    
    # สร้าง masks
    green_mask = cv2.inRange(hsv, green_lower, green_upper)
    yellow_mask = cv2.inRange(hsv, yellow_lower, yellow_upper)
    red_mask = cv2.inRange(hsv, red_lower, red_upper)
    
    # คำนวณเปอร์เซ็นต์
    total_pixels = image.shape[0] * image.shape[1]
    green_percent = np.sum(green_mask > 0) / total_pixels * 100
    yellow_percent = np.sum(yellow_mask > 0) / total_pixels * 100
    red_percent = np.sum(red_mask > 0) / total_pixels * 100
    
    # ประเมินความสุก
    if green_percent > 60:
        ripeness = "ดิบ"
        ripeness_score = 0.2
    elif yellow_percent > 40:
        ripeness = "สุกพอดี"
        ripeness_score = 0.8
    elif red_percent > 30:
        ripeness = "สุกมาก"
        ripeness_score = 1.0
    else:
        ripeness = "กำลังสุก"
        ripeness_score = 0.5
    
    return {
        'ripeness': ripeness,
        'score': ripeness_score,
        'color_distribution': {
            'green': green_percent,
            'yellow': yellow_percent,
            'red': red_percent
        },
        'masks': {
            'green': green_mask,
            'yellow': yellow_mask,
            'red': red_mask
        }
    }

def visualize_ripeness_analysis(image, analysis):
    """แสดงผลการวิเคราะห์ความสุก"""
    
    fig, axes = plt.subplots(2, 3, figsize=(15, 10))
    
    # ภาพต้นฉบับ
    axes[0, 0].imshow(image)
    axes[0, 0].set_title('Original Image')
    axes[0, 0].axis('off')
    
    # แสดง masks
    axes[0, 1].imshow(analysis['masks']['green'], cmap='Greens')
    axes[0, 1].set_title(f"Green Areas ({analysis['color_distribution']['green']:.1f}%)")
    axes[0, 1].axis('off')
    
    axes[0, 2].imshow(analysis['masks']['yellow'], cmap='Oranges')
    axes[0, 2].set_title(f"Yellow Areas ({analysis['color_distribution']['yellow']:.1f}%)")
    axes[0, 2].axis('off')
    
    axes[1, 0].imshow(analysis['masks']['red'], cmap='Reds')
    axes[1, 0].set_title(f"Red Areas ({analysis['color_distribution']['red']:.1f}%)")
    axes[1, 0].axis('off')
    
    # กราฟแสดงการกระจายสี
    axes[1, 1].bar(['Green', 'Yellow', 'Red'], 
                   [analysis['color_distribution']['green'],
                    analysis['color_distribution']['yellow'],
                    analysis['color_distribution']['red']],
                   color=['green', 'yellow', 'red'], alpha=0.7)
    axes[1, 1].set_title('Color Distribution')
    axes[1, 1].set_ylabel('Percentage (%)')
    
    # ผลการประเมิน
    axes[1, 2].text(0.5, 0.7, f"ความสุก: {analysis['ripeness']}", 
                    ha='center', va='center', fontsize=16, fontweight='bold',
                    transform=axes[1, 2].transAxes)
    axes[1, 2].text(0.5, 0.5, f"คะแนน: {analysis['score']:.1f}/1.0", 
                    ha='center', va='center', fontsize=14,
                    transform=axes[1, 2].transAxes)
    
    # Progress bar สำหรับความสุก
    progress_width = analysis['score']
    axes[1, 2].barh(0.3, progress_width, height=0.1, color='orange', alpha=0.7,
                    transform=axes[1, 2].transAxes)
    axes[1, 2].barh(0.3, 1.0, height=0.1, fill=False, edgecolor='black',
                    transform=axes[1, 2].transAxes)
    
    axes[1, 2].set_xlim(0, 1)
    axes[1, 2].set_ylim(0, 1)
    axes[1, 2].axis('off')
    axes[1, 2].set_title('Ripeness Assessment')
    
    plt.tight_layout()
    plt.show()
```

##### 2. การตรวจจับความเสียหาย
```python
def detect_fruit_defects(image):
    """ตรวจจับความเสียหายของผลไม้"""
    
    # แปลงเป็น grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    
    # ใช้ Gaussian blur เพื่อลด noise
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    
    # ตรวจจับขอบด้วย Canny
    edges = cv2.Canny(blurred, 50, 150)
    
    # หา contours
    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    # วิเคราะห์ความเสียหาย
    defects = []
    total_area = image.shape[0] * image.shape[1]
    
    for contour in contours:
        area = cv2.contourArea(contour)
        
        # กรองเฉพาะ contours ที่มีขนาดเหมาะสม
        if area > 100 and area < total_area * 0.1:
            # คำนวณคุณลักษณะ
            perimeter = cv2.arcLength(contour, True)
            circularity = 4 * np.pi * area / (perimeter ** 2) if perimeter > 0 else 0
            
            # จำแนกประเภทความเสียหาย
            if circularity > 0.7:
                defect_type = "จุดด่างดำ"
                severity = "เล็กน้อย" if area < 500 else "ปานกลาง"
            elif circularity > 0.3:
                defect_type = "รอยขีดข่วน"
                severity = "เล็กน้อย" if area < 1000 else "รุนแรง"
            else:
                defect_type = "รอยแตก"
                severity = "รุนแรง"
            
            defects.append({
                'contour': contour,
                'area': area,
                'type': defect_type,
                'severity': severity,
                'circularity': circularity
            })
    
    # คำนวณคะแนนคุณภาพ
    total_defect_area = sum(defect['area'] for defect in defects)
    defect_percentage = (total_defect_area / total_area) * 100
    
    if defect_percentage < 1:
        quality_grade = "A (ดีเยี่ยม)"
        quality_score = 0.95
    elif defect_percentage < 3:
        quality_grade = "B (ดี)"
        quality_score = 0.80
    elif defect_percentage < 7:
        quality_grade = "C (ปานกลาง)"
        quality_score = 0.60
    else:
        quality_grade = "D (ต่ำ)"
        quality_score = 0.30
    
    return {
        'defects': defects,
        'defect_count': len(defects),
        'defect_percentage': defect_percentage,
        'quality_grade': quality_grade,
        'quality_score': quality_score,
        'edges': edges
    }

def visualize_defect_detection(image, analysis):
    """แสดงผลการตรวจจับความเสียหาย"""
    
    fig, axes = plt.subplots(2, 2, figsize=(15, 12))
    
    # ภาพต้นฉบับ
    axes[0, 0].imshow(image)
    axes[0, 0].set_title('Original Image')
    axes[0, 0].axis('off')
    
    # แสดง edge detection
    axes[0, 1].imshow(analysis['edges'], cmap='gray')
    axes[0, 1].set_title('Edge Detection')
    axes[0, 1].axis('off')
    
    # แสดงความเสียหายที่ตรวจพบ
    result_image = image.copy()
    colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0)]
    
    for i, defect in enumerate(analysis['defects']):
        color = colors[i % len(colors)]
        cv2.drawContours(result_image, [defect['contour']], -1, color, 2)
        
        # เขียนข้อความ
        M = cv2.moments(defect['contour'])
        if M["m00"] != 0:
            cx = int(M["m10"] / M["m00"])
            cy = int(M["m01"] / M["m00"])
            cv2.putText(result_image, f"{defect['type']}", (cx-30, cy-10),
                       cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)
    
    axes[1, 0].imshow(result_image)
    axes[1, 0].set_title(f'Detected Defects ({analysis["defect_count"]} found)')
    axes[1, 0].axis('off')
    
    # สรุปผลการประเมิน
    axes[1, 1].text(0.5, 0.8, f"เกรดคุณภาพ: {analysis['quality_grade']}", 
                    ha='center', va='center', fontsize=16, fontweight='bold',
                    transform=axes[1, 1].transAxes)
    axes[1, 1].text(0.5, 0.6, f"คะแนน: {analysis['quality_score']:.2f}/1.00", 
                    ha='center', va='center', fontsize=14,
                    transform=axes[1, 1].transAxes)
    axes[1, 1].text(0.5, 0.4, f"ความเสียหาย: {analysis['defect_percentage']:.1f}%", 
                    ha='center', va='center', fontsize=12,
                    transform=axes[1, 1].transAxes)
    axes[1, 1].text(0.5, 0.2, f"จำนวนจุดเสียหาย: {analysis['defect_count']}", 
                    ha='center', va='center', fontsize=12,
                    transform=axes[1, 1].transAxes)
    
    axes[1, 1].set_xlim(0, 1)
    axes[1, 1].set_ylim(0, 1)
    axes[1, 1].axis('off')
    axes[1, 1].set_title('Quality Assessment')
    
    plt.tight_layout()
    plt.show()
```

### 4.4.4 การตรวจสอบด้วยโดรน (Drone-based Monitoring)

#### ข้อดีของการใช้โดรนในการเกษตร
- ครอบคลุมพื้นที่กว้าง
- ประหยัดเวลาและแรงงาน
- ได้ข้อมูลเรียลไทม์
- เข้าถึงพื้นที่ที่ยากลำบาก

#### การประมวลผลภาพจากโดรน

##### 1. การสร้างแผนที่ความสุขภาพพืช (NDVI)
```python
def calculate_ndvi(nir_image, red_image):
    """คำนวณ NDVI (Normalized Difference Vegetation Index)"""
    
    # แปลงเป็น float เพื่อหลีกเลี่ยง overflow
    nir = nir_image.astype(np.float32)
    red = red_image.astype(np.float32)
    
    # คำนวณ NDVI
    # NDVI = (NIR - Red) / (NIR + Red)
    ndvi = np.divide(nir - red, nir + red, 
                     out=np.zeros_like(nir), where=(nir + red) != 0)
    
    return ndvi

def create_health_map(rgb_image):
    """สร้างแผนที่สุขภาพพืชจากภาพ RGB"""
    
    # แยกช่องสี
    red = rgb_image[:, :, 0]
    green = rgb_image[:, :, 1]
    blue = rgb_image[:, :, 2]
    
    # ใช้ Green แทน NIR (สำหรับกล้อง RGB ธรรมดา)
    # หรือใช้สูตรอื่นๆ เช่น ExG (Excess Green)
    exg = 2 * green - red - blue
    
    # Normalize
    exg_normalized = (exg - exg.min()) / (exg.max() - exg.min())
    
    return exg_normalized

def analyze_crop_health(health_map, threshold_healthy=0.6, threshold_stressed=0.3):
    """วิเคราะห์สุขภาพพืชจากแผนที่"""
    
    # จำแนกระดับสุขภาพ
    healthy_mask = health_map > threshold_healthy
    stressed_mask = (health_map > threshold_stressed) & (health_map <= threshold_healthy)
    unhealthy_mask = health_map <= threshold_stressed
    
    # คำนวณเปอร์เซ็นต์
    total_pixels = health_map.size
    healthy_percent = np.sum(healthy_mask) / total_pixels * 100
    stressed_percent = np.sum(stressed_mask) / total_pixels * 100
    unhealthy_percent = np.sum(unhealthy_mask) / total_pixels * 100
    
    return {
        'healthy_percent': healthy_percent,
        'stressed_percent': stressed_percent,
        'unhealthy_percent': unhealthy_percent,
        'masks': {
            'healthy': healthy_mask,
            'stressed': stressed_mask,
            'unhealthy': unhealthy_mask
        }
    }

def visualize_drone_analysis(original_image, health_map, health_analysis):
    """แสดงผลการวิเคราะห์จากโดรน"""
    
    fig, axes = plt.subplots(2, 3, figsize=(18, 12))
    
    # ภาพต้นฉบับ
    axes[0, 0].imshow(original_image)
    axes[0, 0].set_title('Original Drone Image')
    axes[0, 0].axis('off')
    
    # แผนที่สุขภาพ
    im1 = axes[0, 1].imshow(health_map, cmap='RdYlGn')
    axes[0, 1].set_title('Crop Health Map')
    axes[0, 1].axis('off')
    plt.colorbar(im1, ax=axes[0, 1], shrink=0.6)
    
    # แผนที่จำแนกสุขภาพ
    classified_map = np.zeros_like(health_map)
    classified_map[health_analysis['masks']['healthy']] = 3  # เขียว
    classified_map[health_analysis['masks']['stressed']] = 2  # เหลือง
    classified_map[health_analysis['masks']['unhealthy']] = 1  # แดง
    
    im2 = axes[0, 2].imshow(classified_map, cmap='RdYlGn')
    axes[0, 2].set_title('Health Classification')
    axes[0, 2].axis('off')
    
    # สถิติสุขภาพพืช
    categories = ['Healthy', 'Stressed', 'Unhealthy']
    percentages = [
        health_analysis['healthy_percent'],
        health_analysis['stressed_percent'],
        health_analysis['unhealthy_percent']
    ]
    colors = ['green', 'yellow', 'red']
    
    axes[1, 0].pie(percentages, labels=categories, colors=colors, autopct='%1.1f%%')
    axes[1, 0].set_title('Crop Health Distribution')
    
    # กราฟแท่ง
    axes[1, 1].bar(categories, percentages, color=colors, alpha=0.7)
    axes[1, 1].set_title('Health Percentages')
    axes[1, 1].set_ylabel('Percentage (%)')
    
    # สรุปผลและคำแนะนำ
    if health_analysis['healthy_percent'] > 70:
        status = "สุขภาพดีมาก"
        recommendation = "ดูแลรักษาต่อไป"
        status_color = 'green'
    elif health_analysis['healthy_percent'] > 50:
        status = "สุขภาพดี"
        recommendation = "เฝ้าระวังพื้นที่เสี่ยง"
        status_color = 'orange'
    else:
        status = "ต้องดูแลเร่งด่วน"
        recommendation = "ตรวจสอบและรักษา"
        status_color = 'red'
    
    axes[1, 2].text(0.5, 0.7, f"สถานะ: {status}", 
                    ha='center', va='center', fontsize=14, fontweight='bold',
                    color=status_color, transform=axes[1, 2].transAxes)
    axes[1, 2].text(0.5, 0.5, f"คำแนะนำ: {recommendation}", 
                    ha='center', va='center', fontsize=12,
                    transform=axes[1, 2].transAxes, wrap=True)
    axes[1, 2].text(0.5, 0.3, f"พื้นที่สุขภาพดี: {health_analysis['healthy_percent']:.1f}%", 
                    ha='center', va='center', fontsize=10,
                    transform=axes[1, 2].transAxes)
    
    axes[1, 2].set_xlim(0, 1)
    axes[1, 2].set_ylim(0, 1)
    axes[1, 2].axis('off')
    axes[1, 2].set_title('Assessment & Recommendations')
    
    plt.tight_layout()
    plt.show()
```

##### 2. การตรวจจับวัชพืช
```python
def detect_weeds_in_field(image):
    """ตรวจจับวัชพืชในไร่"""
    
    # แปลงเป็น HSV
    hsv = cv2.cvtColor(image, cv2.COLOR_RGB2HSV)
    
    # กำหนดช่วงสีสำหรับพืชผล (เขียวเข้ม)
    crop_lower = np.array([40, 40, 40])
    crop_upper = np.array([80, 255, 255])
    
    # กำหนดช่วงสีสำหรับวัชพืช (เขียวอ่อน, เหลือง)
    weed_lower1 = np.array([20, 30, 30])
    weed_upper1 = np.array([40, 255, 255])
    
    weed_lower2 = np.array([80, 30, 30])
    weed_upper2 = np.array([120, 255, 255])
    
    # สร้าง masks
    crop_mask = cv2.inRange(hsv, crop_lower, crop_upper)
    weed_mask1 = cv2.inRange(hsv, weed_lower1, weed_upper1)
    weed_mask2 = cv2.inRange(hsv, weed_lower2, weed_upper2)
    weed_mask = cv2.bitwise_or(weed_mask1, weed_mask2)
    
    # ลด noise
    kernel = np.ones((3, 3), np.uint8)
    crop_mask = cv2.morphologyEx(crop_mask, cv2.MORPH_CLOSE, kernel)
    weed_mask = cv2.morphologyEx(weed_mask, cv2.MORPH_CLOSE, kernel)
    
    # หา contours สำหรับวัชพืช
    weed_contours, _ = cv2.findContours(weed_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    # กรองวัชพืชตามขนาด
    min_weed_area = 50
    max_weed_area = 5000
    
    valid_weeds = []
    for contour in weed_contours:
        area = cv2.contourArea(contour)
        if min_weed_area < area < max_weed_area:
            valid_weeds.append(contour)
    
    # คำนวณสถิติ
    total_area = image.shape[0] * image.shape[1]
    crop_area = np.sum(crop_mask > 0)
    weed_area = sum(cv2.contourArea(contour) for contour in valid_weeds)
    
    crop_percentage = (crop_area / total_area) * 100
    weed_percentage = (weed_area / total_area) * 100
    
    return {
        'weed_contours': valid_weeds,
        'weed_count': len(valid_weeds),
        'crop_percentage': crop_percentage,
        'weed_percentage': weed_percentage,
        'masks': {
            'crop': crop_mask,
            'weed': weed_mask
        }
    }

def create_weed_treatment_map(image, weed_analysis):
    """สร้างแผนที่การฉีดยาวัชพืช"""
    
    treatment_map = np.zeros((image.shape[0], image.shape[1]), dtype=np.uint8)
    
    # สร้างพื้นที่รอบๆ วัชพืชสำหรับการฉีดยา
    for contour in weed_analysis['weed_contours']:
        # สร้าง buffer รอบๆ วัชพืช
        mask = np.zeros((image.shape[0], image.shape[1]), dtype=np.uint8)
        cv2.fillPoly(mask, [contour], 255)
        
        # ขยายพื้นที่การฉีดยา
        kernel = np.ones((20, 20), np.uint8)
        expanded_mask = cv2.dilate(mask, kernel, iterations=1)
        
        treatment_map = cv2.bitwise_or(treatment_map, expanded_mask)
    
    return treatment_map

def visualize_weed_detection(image, weed_analysis, treatment_map):
    """แสดงผลการตรวจจับวัชพืช"""
    
    fig, axes = plt.subplots(2, 3, figsize=(18, 12))
    
    # ภาพต้นฉบับ
    axes[0, 0].imshow(image)
    axes[0, 0].set_title('Original Field Image')
    axes[0, 0].axis('off')
    
    # แสดง crop mask
    axes[0, 1].imshow(weed_analysis['masks']['crop'], cmap='Greens')
    axes[0, 1].set_title('Crop Areas')
    axes[0, 1].axis('off')
    
    # แสดง weed mask
    axes[0, 2].imshow(weed_analysis['masks']['weed'], cmap='Reds')
    axes[0, 2].set_title('Weed Areas')
    axes[0, 2].axis('off')
    
    # แสดงการตรวจจับวัชพืช
    result_image = image.copy()
    cv2.drawContours(result_image, weed_analysis['weed_contours'], -1, (255, 0, 0), 2)
    
    # เพิ่มหมายเลขวัชพืช
    for i, contour in enumerate(weed_analysis['weed_contours']):
        M = cv2.moments(contour)
        if M["m00"] != 0:
            cx = int(M["m10"] / M["m00"])
            cy = int(M["m01"] / M["m00"])
            cv2.putText(result_image, str(i+1), (cx, cy),
                       cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
    
    axes[1, 0].imshow(result_image)
    axes[1, 0].set_title(f'Detected Weeds ({weed_analysis["weed_count"]} found)')
    axes[1, 0].axis('off')
    
    # แผนที่การฉีดยา
    axes[1, 1].imshow(image)
    axes[1, 1].imshow(treatment_map, alpha=0.5, cmap='Reds')
    axes[1, 1].set_title('Treatment Map')
    axes[1, 1].axis('off')
    
    # สถิติและคำแนะนำ
    axes[1, 2].text(0.5, 0.8, f"จำนวนวัชพืช: {weed_analysis['weed_count']}", 
                    ha='center', va='center', fontsize=12, fontweight='bold',
                    transform=axes[1, 2].transAxes)
    axes[1, 2].text(0.5, 0.6, f"พื้นที่พืชผล: {weed_analysis['crop_percentage']:.1f}%", 
                    ha='center', va='center', fontsize=10,
                    transform=axes[1, 2].transAxes)
    axes[1, 2].text(0.5, 0.4, f"พื้นที่วัชพืช: {weed_analysis['weed_percentage']:.1f}%", 
                    ha='center', va='center', fontsize=10,
                    transform=axes[1, 2].transAxes)
    
    # คำแนะนำ
    if weed_analysis['weed_percentage'] > 5:
        recommendation = "ต้องฉีดยาเร่งด่วน"
        color = 'red'
    elif weed_analysis['weed_percentage'] > 2:
        recommendation = "ควรฉีดยาในพื้นที่เสี่ยง"
        color = 'orange'
    else:
        recommendation = "สถานการณ์ปกติ"
        color = 'green'
    
    axes[1, 2].text(0.5, 0.2, f"คำแนะนำ: {recommendation}", 
                    ha='center', va='center', fontsize=10, color=color,
                    transform=axes[1, 2].transAxes)
    
    axes[1, 2].set_xlim(0, 1)
    axes[1, 2].set_ylim(0, 1)
    axes[1, 2].axis('off')
    axes[1, 2].set_title('Analysis Summary')
    
    plt.tight_layout()
    plt.show()
```

## 4.5 เครื่องมือและไลบรารีสำหรับ Computer Vision

### 4.5.1 OpenCV
```python
# ตัวอย่างการใช้ OpenCV พื้นฐาน
import cv2
import numpy as np

def opencv_basic_operations():
    """สาธิตการใช้งาน OpenCV พื้นฐาน"""
    
    # อ่านภาพ
    # image = cv2.imread('path/to/image.jpg')
    
    # สร้างภาพตัวอย่าง
    image = np.zeros((300, 400, 3), dtype=np.uint8)
    cv2.rectangle(image, (50, 50), (350, 250), (0, 255, 0), -1)
    cv2.circle(image, (200, 150), 50, (255, 0, 0), -1)
    
    # การประมวลผลพื้นฐาน
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (15, 15), 0)
    edges = cv2.Canny(blurred, 50, 150)
    
    # หา contours
    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    # วาด contours
    result = image.copy()
    cv2.drawContours(result, contours, -1, (255, 255, 0), 2)
    
    return image, gray, edges, result
```

### 4.5.2 scikit-image
```python
from skimage import filters, segmentation, measure
from skimage.feature import local_binary_pattern

def skimage_operations():
    """สาธิตการใช้งาน scikit-image"""
    
    # สร้างภาพตัวอย่าง
    image = np.random.rand(200, 200)
    
    # การกรองภาพ
    gaussian_filtered = filters.gaussian(image, sigma=1)
    sobel_filtered = filters.sobel(image)
    
    # การแบ่งส่วนภาพ
    threshold = filters.threshold_otsu(image)
    binary = image > threshold
    
    # Watershed segmentation
    markers = measure.label(binary)
    segmented = segmentation.watershed(sobel_filtered, markers)
    
    # Local Binary Pattern
    lbp = local_binary_pattern(image, P=8, R=1, method='uniform')
    
    return gaussian_filtered, sobel_filtered, binary, segmented, lbp
```

### 4.5.3 PIL/Pillow
```python
from PIL import Image, ImageEnhance, ImageFilter

def pil_operations():
    """สาธิตการใช้งาน PIL/Pillow"""
    
    # สร้างภาพตัวอย่าง
    image = Image.new('RGB', (300, 200), color='green')
    
    # การปรับแต่งภาพ
    enhancer = ImageEnhance.Brightness(image)
    bright_image = enhancer.enhance(1.5)
    
    enhancer = ImageEnhance.Contrast(image)
    contrast_image = enhancer.enhance(2.0)
    
    # การกรองภาพ
    blurred = image.filter(ImageFilter.BLUR)
    sharpened = image.filter(ImageFilter.SHARPEN)
    
    # การหมุนและปรับขนาด
    rotated = image.rotate(45)
    resized = image.resize((150, 100))
    
    return bright_image, contrast_image, blurred, sharpened, rotated, resized
```

## 4.6 กิจกรรมและแบบฝึกหัด

### กิจกรรมที่ 1: การตรวจจับขอบในภาพใบไม้

**วัตถุประสงค์**: ให้นักเรียนเข้าใจหลักการตรวจจับขอบ

**อุปกรณ์**: คอมพิวเตอร์, Python, ภาพใบไม้

**ขั้นตอน**:
1. ถ่ายภาพใบไม้ 5 ชนิดต่างกัน
2. ใช้ Sobel และ Canny edge detection
3. เปรียบเทียบผลลัพธ์ของแต่ละวิธี
4. วิเคราะห์ความแตกต่างของขอบในแต่ละชนิดใบไม้

### กิจกรรมที่ 2: การจำแนกผลไม้ด้วย Color Features

**วัตถุประสงค์**: ให้นักเรียนเข้าใจการสกัดคุณลักษณะสี

**ขั้นตอน**:
1. รวบรวมภาพผลไม้ 3 ชนิด (ชนิดละ 20 ภาพ)
2. สกัด Color Histogram และ Color Moments
3. ใช้ Machine Learning จำแนกผลไม้
4. ประเมินความแม่นยำและวิเคราะห์ผลลัพธ์

### กิจกรรมที่ 3: การสร้าง CNN สำหรับตรวจจับโรคพืช

**วัตถุประสงค์**: ให้นักเรียนสร้างโมเดล Deep Learning

**ขั้นตอน**:
1. รวบรวมภาพใบไม้สุขภาพดีและป่วย
2. เตรียมข้อมูลและทำ Data Augmentation
3. สร้างโมเดล CNN ด้วย TensorFlow
4. ฝึกโมเดลและประเมินประสิทธิภาพ
5. ทดสอบกับภาพใหม่

### โครงงานกลุ่ม: ระบบตรวจสอบคุณภาพผลไม้อัตโนมัติ

**วัตถุประสงค์**: ประยุกต์ Computer Vision แก้ปัญหาจริง

**ขั้นตอน**:
1. **การวิเคราะห์ปัญหา**: สำรวจปัญหาการคัดแยกผลไม้ในชุมชน
2. **การออกแบบระบบ**: วางแผนระบบตรวจสอบคุณภาพ
3. **การพัฒนาโมเดล**: สร้างโมเดลตรวจจับความสุกและความเสียหาย
4. **การทดสอบ**: ทดสอบกับผลไม้จริง
5. **การนำเสนอ**: สร้างแอปพลิเคชันง่ายๆ

## สรุป

บทที่ 4 นี้เราได้เรียนรู้เกี่ยวกับ Computer Vision ซึ่งเป็นเทคโนโลยีที่ให้คอมพิวเตอร์สามารถ "มองเห็น" และเข้าใจภาพได้ เราได้ทำความเข้าใจกับหลักการพื้นฐาน เทคนิคการประมวลผลภาพ และการประยุกต์ใช้ในการเกษตร

**จุดสำคัญที่ต้องจำ**:
- Computer Vision ใช้อัลกอริทึมวิเคราะห์และตีความภาพ
- การประมวลผลภาพพื้นฐานรวมถึงการกรอง การตรวจจับขอบ และการสกัดคุณลักษณะ
- CNN เป็นสถาปัตยกรรมที่เหมาะสมที่สุดสำหรับงาน Computer Vision
- การประยุกต์ใช้ในการเกษตรครอบคลุมการตรวจจับโรค การนับผลไม้ การประเมินคุณภาพ และการตรวจสอบด้วยโดรน
- เครื่องมือสำคัญ ได้แก่ OpenCV, scikit-image, และ TensorFlow/PyTorch

ในบทถัดไป เราจะเจาะลึกเข้าไปในโลกของ Natural Language Processing ซึ่งจะช่วยให้คอมพิวเตอร์เข้าใจและประมวลผลภาษามนุษย์ได้

