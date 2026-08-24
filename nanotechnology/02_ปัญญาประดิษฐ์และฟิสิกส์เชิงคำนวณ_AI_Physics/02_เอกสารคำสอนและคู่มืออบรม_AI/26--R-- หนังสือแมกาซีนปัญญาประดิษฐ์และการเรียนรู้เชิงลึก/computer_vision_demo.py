import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button
import cv2
from PIL import Image, ImageEnhance
import seaborn as sns
from sklearn.cluster import KMeans
import matplotlib.patches as patches

class ComputerVisionDemo:
    def __init__(self):
        self.fig = None
        self.current_demo = 0
        self.demos = [
            self.image_processing_demo,
            self.edge_detection_demo,
            self.color_analysis_demo,
            self.feature_extraction_demo,
            self.object_detection_demo
        ]
        self.demo_names = [
            "Image Processing Basics",
            "Edge Detection",
            "Color Analysis",
            "Feature Extraction", 
            "Object Detection"
        ]
        
    def create_sample_leaf_image(self, size=(200, 200)):
        """สร้างภาพใบไม้ตัวอย่าง"""
        image = np.zeros((*size, 3), dtype=np.uint8)
        
        # สร้างรูปร่างใบไม้
        center_x, center_y = size[1] // 2, size[0] // 2
        
        # วาดใบไม้ (ellipse)
        cv2.ellipse(image, (center_x, center_y), (60, 80), 0, 0, 360, (34, 139, 34), -1)
        
        # เส้นกลางใบ
        cv2.line(image, (center_x, center_y - 70), (center_x, center_y + 70), (0, 100, 0), 3)
        
        # เส้นใบย่อย
        for i in range(-3, 4):
            if i != 0:
                start_x = center_x
                start_y = center_y + i * 20
                end_x = center_x + (30 if i % 2 == 0 else -30)
                end_y = start_y
                cv2.line(image, (start_x, start_y), (end_x, end_y), (0, 100, 0), 1)
        
        # เพิ่ม noise เล็กน้อย
        noise = np.random.normal(0, 10, image.shape).astype(np.int16)
        image = np.clip(image.astype(np.int16) + noise, 0, 255).astype(np.uint8)
        
        return image
    
    def create_sample_fruit_image(self, size=(200, 200)):
        """สร้างภาพผลไม้ตัวอย่าง"""
        image = np.zeros((*size, 3), dtype=np.uint8)
        
        # วาดผลไม้ (วงกลม)
        center_x, center_y = size[1] // 2, size[0] // 2
        
        # ผลไม้หลัก (สีส้ม)
        cv2.circle(image, (center_x, center_y), 50, (255, 165, 0), -1)
        
        # เงา
        cv2.ellipse(image, (center_x + 15, center_y + 15), (20, 30), 45, 0, 360, (200, 120, 0), -1)
        
        # จุดเด่น
        cv2.circle(image, (center_x - 15, center_y - 15), 8, (255, 200, 100), -1)
        
        return image
    
    def image_processing_demo(self):
        """สาธิตการประมวลผลภาพพื้นฐาน"""
        if self.fig:
            plt.close(self.fig)
            
        self.fig, axes = plt.subplots(3, 3, figsize=(15, 12))
        self.fig.suptitle('การประมวลผลภาพพื้นฐาน', fontsize=16, fontweight='bold')
        
        # สร้างภาพตัวอย่าง
        original = self.create_sample_leaf_image()
        
        # 1. ภาพต้นฉบับ
        axes[0, 0].imshow(original)
        axes[0, 0].set_title('ภาพต้นฉบับ')
        axes[0, 0].axis('off')
        
        # 2. Grayscale
        gray = cv2.cvtColor(original, cv2.COLOR_RGB2GRAY)
        axes[0, 1].imshow(gray, cmap='gray')
        axes[0, 1].set_title('Grayscale')
        axes[0, 1].axis('off')
        
        # 3. HSV
        hsv = cv2.cvtColor(original, cv2.COLOR_RGB2HSV)
        axes[0, 2].imshow(hsv)
        axes[0, 2].set_title('HSV Color Space')
        axes[0, 2].axis('off')
        
        # 4. Gaussian Blur
        blurred = cv2.GaussianBlur(original, (15, 15), 0)
        axes[1, 0].imshow(blurred)
        axes[1, 0].set_title('Gaussian Blur')
        axes[1, 0].axis('off')
        
        # 5. Sharpening
        kernel_sharpen = np.array([[-1,-1,-1],
                                  [-1, 9,-1],
                                  [-1,-1,-1]])
        sharpened = cv2.filter2D(original, -1, kernel_sharpen)
        axes[1, 1].imshow(sharpened)
        axes[1, 1].set_title('Sharpened')
        axes[1, 1].axis('off')
        
        # 6. Brightness adjustment
        bright = cv2.convertScaleAbs(original, alpha=1.5, beta=30)
        axes[1, 2].imshow(bright)
        axes[1, 2].set_title('Brightness Enhanced')
        axes[1, 2].axis('off')
        
        # 7. Histogram Equalization
        gray_eq = cv2.equalizeHist(gray)
        axes[2, 0].imshow(gray_eq, cmap='gray')
        axes[2, 0].set_title('Histogram Equalized')
        axes[2, 0].axis('off')
        
        # 8. Morphological Operations
        kernel = np.ones((5,5), np.uint8)
        _, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
        opening = cv2.morphologyEx(binary, cv2.MORPH_OPEN, kernel)
        axes[2, 1].imshow(opening, cmap='gray')
        axes[2, 1].set_title('Morphological Opening')
        axes[2, 1].axis('off')
        
        # 9. Color Histogram
        colors = ('r', 'g', 'b')
        axes[2, 2].set_title('Color Histogram')
        for i, color in enumerate(colors):
            hist = cv2.calcHist([original], [i], None, [256], [0, 256])
            axes[2, 2].plot(hist, color=color, alpha=0.7)
        axes[2, 2].set_xlabel('Pixel Intensity')
        axes[2, 2].set_ylabel('Frequency')
        
        plt.tight_layout()
        
    def edge_detection_demo(self):
        """สาธิตการตรวจจับขอบ"""
        if self.fig:
            plt.close(self.fig)
            
        self.fig, axes = plt.subplots(2, 3, figsize=(15, 10))
        self.fig.suptitle('การตรวจจับขอบ (Edge Detection)', fontsize=16, fontweight='bold')
        
        # สร้างภาพตัวอย่าง
        original = self.create_sample_leaf_image()
        gray = cv2.cvtColor(original, cv2.COLOR_RGB2GRAY)
        
        # 1. ภาพต้นฉบับ
        axes[0, 0].imshow(original)
        axes[0, 0].set_title('ภาพต้นฉบับ')
        axes[0, 0].axis('off')
        
        # 2. Sobel X
        sobel_x = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3)
        sobel_x = np.absolute(sobel_x)
        axes[0, 1].imshow(sobel_x, cmap='gray')
        axes[0, 1].set_title('Sobel X (ขอบแนวตั้ง)')
        axes[0, 1].axis('off')
        
        # 3. Sobel Y
        sobel_y = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=3)
        sobel_y = np.absolute(sobel_y)
        axes[0, 2].imshow(sobel_y, cmap='gray')
        axes[0, 2].set_title('Sobel Y (ขอบแนวนอน)')
        axes[0, 2].axis('off')
        
        # 4. Sobel Combined
        sobel_combined = np.sqrt(sobel_x**2 + sobel_y**2)
        axes[1, 0].imshow(sobel_combined, cmap='gray')
        axes[1, 0].set_title('Sobel Combined')
        axes[1, 0].axis('off')
        
        # 5. Canny Edge Detection
        canny = cv2.Canny(gray, 50, 150)
        axes[1, 1].imshow(canny, cmap='gray')
        axes[1, 1].set_title('Canny Edge Detection')
        axes[1, 1].axis('off')
        
        # 6. Laplacian
        laplacian = cv2.Laplacian(gray, cv2.CV_64F)
        laplacian = np.absolute(laplacian)
        axes[1, 2].imshow(laplacian, cmap='gray')
        axes[1, 2].set_title('Laplacian')
        axes[1, 2].axis('off')
        
        plt.tight_layout()
        
    def color_analysis_demo(self):
        """สาธิตการวิเคราะห์สี"""
        if self.fig:
            plt.close(self.fig)
            
        self.fig, axes = plt.subplots(2, 3, figsize=(15, 10))
        self.fig.suptitle('การวิเคราะห์สี สำหรับการประเมินความสุกของผลไม้', fontsize=16, fontweight='bold')
        
        # สร้างภาพผลไม้ในระยะการสุกต่างๆ
        fruits = []
        ripeness_levels = ['ดิบ', 'กำลังสุก', 'สุกพอดี']
        colors = [(34, 139, 34), (255, 215, 0), (255, 140, 0)]  # เขียว, เหลือง, ส้ม
        
        for i, (ripeness, color) in enumerate(zip(ripeness_levels, colors)):
            fruit_img = np.zeros((150, 150, 3), dtype=np.uint8)
            cv2.circle(fruit_img, (75, 75), 60, color, -1)
            
            # เพิ่มความสมจริง
            cv2.circle(fruit_img, (60, 60), 15, tuple(int(c*1.2) if c*1.2 <= 255 else 255 for c in color), -1)
            
            fruits.append(fruit_img)
            
            # แสดงผลไม้
            axes[0, i].imshow(fruit_img)
            axes[0, i].set_title(f'ผลไม้ {ripeness}')
            axes[0, i].axis('off')
            
            # วิเคราะห์สี
            hsv = cv2.cvtColor(fruit_img, cv2.COLOR_RGB2HSV)
            
            # คำนวณ Color Histogram
            colors_rgb = ('r', 'g', 'b')
            axes[1, i].set_title(f'Color Histogram - {ripeness}')
            for j, color_name in enumerate(colors_rgb):
                hist = cv2.calcHist([fruit_img], [j], None, [256], [0, 256])
                axes[1, i].plot(hist, color=color_name, alpha=0.7, linewidth=2)
            axes[1, i].set_xlabel('Pixel Intensity')
            axes[1, i].set_ylabel('Frequency')
            axes[1, i].grid(True, alpha=0.3)
        
        plt.tight_layout()
        
    def feature_extraction_demo(self):
        """สาธิตการสกัดคุณลักษณะ"""
        if self.fig:
            plt.close(self.fig)
            
        self.fig, axes = plt.subplots(2, 3, figsize=(15, 10))
        self.fig.suptitle('การสกัดคุณลักษณะ (Feature Extraction)', fontsize=16, fontweight='bold')
        
        # สร้างภาพตัวอย่าง
        original = self.create_sample_leaf_image()
        gray = cv2.cvtColor(original, cv2.COLOR_RGB2GRAY)
        
        # 1. ภาพต้นฉบับ
        axes[0, 0].imshow(original)
        axes[0, 0].set_title('ภาพต้นฉบับ')
        axes[0, 0].axis('off')
        
        # 2. Binary Image และ Contours
        _, binary = cv2.threshold(gray, 50, 255, cv2.THRESH_BINARY)
        contours, _ = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        
        contour_img = original.copy()
        if contours:
            largest_contour = max(contours, key=cv2.contourArea)
            cv2.drawContours(contour_img, [largest_contour], -1, (255, 0, 0), 3)
            
            # คำนวณคุณลักษณะรูปร่าง
            area = cv2.contourArea(largest_contour)
            perimeter = cv2.arcLength(largest_contour, True)
            
            # Bounding rectangle
            x, y, w, h = cv2.boundingRect(largest_contour)
            cv2.rectangle(contour_img, (x, y), (x+w, y+h), (0, 255, 0), 2)
            
            # คำนวณ aspect ratio
            aspect_ratio = float(w) / h
            
            # Circularity
            circularity = 4 * np.pi * area / (perimeter ** 2) if perimeter > 0 else 0
            
        axes[0, 1].imshow(contour_img)
        axes[0, 1].set_title('Contour Analysis')
        axes[0, 1].axis('off')
        
        # 3. Local Binary Pattern (จำลอง)
        lbp = np.zeros_like(gray)
        for i in range(1, gray.shape[0]-1):
            for j in range(1, gray.shape[1]-1):
                center = gray[i, j]
                binary_string = ""
                
                # ตรวจสอบ 8 จุดรอบๆ
                neighbors = [
                    gray[i-1, j-1], gray[i-1, j], gray[i-1, j+1],
                    gray[i, j+1], gray[i+1, j+1], gray[i+1, j],
                    gray[i+1, j-1], gray[i, j-1]
                ]
                
                for neighbor in neighbors:
                    binary_string += "1" if neighbor >= center else "0"
                
                lbp[i, j] = int(binary_string, 2)
        
        axes[0, 2].imshow(lbp, cmap='gray')
        axes[0, 2].set_title('Local Binary Pattern')
        axes[0, 2].axis('off')
        
        # 4. Color Moments
        color_moments = []
        for channel in range(3):
            channel_data = original[:, :, channel].flatten()
            mean = np.mean(channel_data)
            std = np.std(channel_data)
            skewness = np.mean(((channel_data - mean) / std) ** 3) if std > 0 else 0
            color_moments.extend([mean, std, skewness])
        
        # แสดงกราฟ Color Moments
        moment_names = ['R_mean', 'R_std', 'R_skew', 'G_mean', 'G_std', 'G_skew', 'B_mean', 'B_std', 'B_skew']
        axes[1, 0].bar(range(len(color_moments)), color_moments, 
                      color=['red', 'red', 'red', 'green', 'green', 'green', 'blue', 'blue', 'blue'],
                      alpha=0.7)
        axes[1, 0].set_title('Color Moments')
        axes[1, 0].set_xticks(range(len(moment_names)))
        axes[1, 0].set_xticklabels(moment_names, rotation=45)
        
        # 5. Shape Features
        if contours:
            shape_features = {
                'Area': area,
                'Perimeter': perimeter,
                'Aspect Ratio': aspect_ratio,
                'Circularity': circularity
            }
            
            feature_names = list(shape_features.keys())
            feature_values = list(shape_features.values())
            
            axes[1, 1].bar(feature_names, feature_values, color='skyblue', alpha=0.7)
            axes[1, 1].set_title('Shape Features')
            axes[1, 1].tick_params(axis='x', rotation=45)
        
        # 6. Texture Analysis (GLCM จำลอง)
        # สร้างข้อมูล GLCM features จำลอง
        glcm_features = {
            'Contrast': np.random.uniform(0.1, 0.8),
            'Homogeneity': np.random.uniform(0.3, 0.9),
            'Energy': np.random.uniform(0.1, 0.5),
            'Correlation': np.random.uniform(0.5, 0.95)
        }
        
        feature_names = list(glcm_features.keys())
        feature_values = list(glcm_features.values())
        
        axes[1, 2].bar(feature_names, feature_values, color='lightgreen', alpha=0.7)
        axes[1, 2].set_title('Texture Features (GLCM)')
        axes[1, 2].tick_params(axis='x', rotation=45)
        
        plt.tight_layout()
        
    def object_detection_demo(self):
        """สาธิตการตรวจจับวัตถุ"""
        if self.fig:
            plt.close(self.fig)
            
        self.fig, axes = plt.subplots(2, 2, figsize=(15, 12))
        self.fig.suptitle('การตรวจจับวัตถุ (Object Detection) ในการเกษตร', fontsize=16, fontweight='bold')
        
        # สร้างภาพไร่จำลอง
        field_image = np.ones((300, 400, 3), dtype=np.uint8) * 139  # สีน้ำตาลของดิน
        
        # เพิ่มพืชผล (วงกลมเขียว)
        crops = [(100, 80), (200, 90), (300, 85), (150, 150), (250, 160), (350, 155)]
        crop_boxes = []
        
        for i, (x, y) in enumerate(crops):
            cv2.circle(field_image, (x, y), 25, (34, 139, 34), -1)  # พืชผล
            crop_boxes.append([x-25, y-25, x+25, y+25])
        
        # เพิ่มวัชพืช (วงกลมเหลือง)
        weeds = [(120, 200), (280, 220), (180, 250)]
        weed_boxes = []
        
        for x, y in weeds:
            cv2.circle(field_image, (x, y), 15, (255, 255, 0), -1)  # วัชพืช
            weed_boxes.append([x-15, y-15, x+15, y+15])
        
        # 1. ภาพต้นฉบับ
        axes[0, 0].imshow(field_image)
        axes[0, 0].set_title('ภาพไร่ต้นฉบับ')
        axes[0, 0].axis('off')
        
        # 2. การตรวจจับด้วย Color Segmentation
        hsv = cv2.cvtColor(field_image, cv2.COLOR_RGB2HSV)
        
        # Mask สำหรับพืชผล (สีเขียว)
        crop_lower = np.array([40, 50, 50])
        crop_upper = np.array([80, 255, 255])
        crop_mask = cv2.inRange(hsv, crop_lower, crop_upper)
        
        # Mask สำหรับวัชพืช (สีเหลือง)
        weed_lower = np.array([20, 50, 50])
        weed_upper = np.array([40, 255, 255])
        weed_mask = cv2.inRange(hsv, weed_lower, weed_upper)
        
        # รวม masks
        combined_mask = cv2.bitwise_or(crop_mask, weed_mask)
        axes[0, 1].imshow(combined_mask, cmap='gray')
        axes[0, 1].set_title('Color Segmentation')
        axes[0, 1].axis('off')
        
        # 3. การตรวจจับด้วย Contour Detection
        detection_result = field_image.copy()
        
        # หา contours สำหรับพืชผล
        crop_contours, _ = cv2.findContours(crop_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        for i, contour in enumerate(crop_contours):
            if cv2.contourArea(contour) > 100:  # กรองขนาดเล็ก
                x, y, w, h = cv2.boundingRect(contour)
                cv2.rectangle(detection_result, (x, y), (x+w, y+h), (0, 255, 0), 2)
                cv2.putText(detection_result, f'Crop {i+1}', (x, y-5),
                           cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
        
        # หา contours สำหรับวัชพืช
        weed_contours, _ = cv2.findContours(weed_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        for i, contour in enumerate(weed_contours):
            if cv2.contourArea(contour) > 50:  # กรองขนาดเล็ก
                x, y, w, h = cv2.boundingRect(contour)
                cv2.rectangle(detection_result, (x, y), (x+w, y+h), (255, 0, 0), 2)
                cv2.putText(detection_result, f'Weed {i+1}', (x, y-5),
                           cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)
        
        axes[1, 0].imshow(detection_result)
        axes[1, 0].set_title(f'Object Detection\n(พืชผล: {len(crop_contours)}, วัชพืช: {len(weed_contours)})')
        axes[1, 0].axis('off')
        
        # 4. สถิติและการวิเคราะห์
        total_crops = len([c for c in crop_contours if cv2.contourArea(c) > 100])
        total_weeds = len([c for c in weed_contours if cv2.contourArea(c) > 50])
        
        # คำนวณพื้นที่
        crop_area = sum(cv2.contourArea(c) for c in crop_contours if cv2.contourArea(c) > 100)
        weed_area = sum(cv2.contourArea(c) for c in weed_contours if cv2.contourArea(c) > 50)
        total_area = field_image.shape[0] * field_image.shape[1]
        
        crop_percentage = (crop_area / total_area) * 100
        weed_percentage = (weed_area / total_area) * 100
        
        # แสดงสถิติ
        categories = ['พืชผล', 'วัชพืช']
        counts = [total_crops, total_weeds]
        percentages = [crop_percentage, weed_percentage]
        
        # กราฟจำนวน
        ax_stats = axes[1, 1]
        bars = ax_stats.bar(categories, counts, color=['green', 'red'], alpha=0.7)
        ax_stats.set_title('สถิติการตรวจจับ')
        ax_stats.set_ylabel('จำนวน')
        
        # เพิ่มค่าบนแท่งกราฟ
        for bar, count, percentage in zip(bars, counts, percentages):
            height = bar.get_height()
            ax_stats.text(bar.get_x() + bar.get_width()/2., height + 0.1,
                         f'{count}\n({percentage:.1f}%)',
                         ha='center', va='bottom', fontweight='bold')
        
        # คำแนะนำ
        if weed_percentage > 5:
            recommendation = "ต้องกำจัดวัชพืชเร่งด่วน"
            rec_color = 'red'
        elif weed_percentage > 2:
            recommendation = "ควรเฝ้าระวังวัชพืช"
            rec_color = 'orange'
        else:
            recommendation = "สถานการณ์ปกติ"
            rec_color = 'green'
        
        ax_stats.text(0.5, -0.15, f"คำแนะนำ: {recommendation}",
                     transform=ax_stats.transAxes, ha='center', va='top',
                     fontsize=12, fontweight='bold', color=rec_color,
                     bbox=dict(boxstyle="round,pad=0.3", facecolor='lightgray', alpha=0.7))
        
        plt.tight_layout()
    
    def setup_navigation(self):
        """ตั้งค่าปุ่มสำหรับเปลี่ยนการสาธิต"""
        if self.fig:
            # Previous button
            ax_prev = plt.axes([0.1, 0.01, 0.1, 0.05])
            self.btn_prev = Button(ax_prev, 'ก่อนหน้า')
            self.btn_prev.on_clicked(self.prev_demo)
            
            # Next button
            ax_next = plt.axes([0.8, 0.01, 0.1, 0.05])
            self.btn_next = Button(ax_next, 'ถัดไป')
            self.btn_next.on_clicked(self.next_demo)
            
            # Demo info
            demo_info = f"การสาธิต {self.current_demo + 1}/{len(self.demos)}: {self.demo_names[self.current_demo]}"
            self.fig.text(0.5, 0.01, demo_info, ha='center', fontsize=12, fontweight='bold')
    
    def prev_demo(self, event):
        """แสดงการสาธิตก่อนหน้า"""
        self.current_demo = (self.current_demo - 1) % len(self.demos)
        self.show_current_demo()
    
    def next_demo(self, event):
        """แสดงการสาธิตถัดไป"""
        self.current_demo = (self.current_demo + 1) % len(self.demos)
        self.show_current_demo()
    
    def show_current_demo(self):
        """แสดงการสาธิตปัจจุบัน"""
        self.demos[self.current_demo]()
        self.setup_navigation()
        plt.draw()
    
    def start(self):
        """เริ่มการสาธิต"""
        print("=== การสาธิต Computer Vision ===")
        print("ใช้ปุ่ม 'ถัดไป' และ 'ก่อนหน้า' เพื่อดูการสาธิตต่างๆ")
        print("\nการสาธิตที่มี:")
        for i, name in enumerate(self.demo_names, 1):
            print(f"{i}. {name}")
        
        self.show_current_demo()
        plt.show()

# Agricultural Computer Vision Applications
class AgricultureVisionApplications:
    def __init__(self):
        self.fig, self.axes = plt.subplots(2, 2, figsize=(15, 12))
        self.fig.suptitle('การประยุกต์ใช้ Computer Vision ในการเกษตร', fontsize=16, fontweight='bold')
        
    def plant_disease_detection(self):
        """จำลองการตรวจจับโรคพืช"""
        ax = self.axes[0, 0]
        
        # สร้างภาพใบไม้ที่มีโรค
        diseased_leaf = np.zeros((150, 150, 3), dtype=np.uint8)
        
        # ใบไม้สีเขียว
        cv2.ellipse(diseased_leaf, (75, 75), (60, 40), 0, 0, 360, (34, 139, 34), -1)
        
        # จุดโรค (สีน้ำตาล)
        disease_spots = [(60, 60), (90, 80), (70, 90), (85, 65)]
        for x, y in disease_spots:
            cv2.circle(diseased_leaf, (x, y), np.random.randint(5, 12), (139, 69, 19), -1)
        
        # แสดงผล
        ax.imshow(diseased_leaf)
        ax.set_title('การตรวจจับโรคพืช')
        
        # เพิ่มกรอบรอบจุดโรค
        for i, (x, y) in enumerate(disease_spots):
            rect = patches.Rectangle((x-15, y-15), 30, 30, 
                                   linewidth=2, edgecolor='red', facecolor='none')
            ax.add_patch(rect)
            ax.text(x-10, y-20, f'โรค {i+1}', color='red', fontweight='bold', fontsize=8)
        
        ax.axis('off')
        
        # สถิติ
        ax.text(0.02, 0.98, f'จุดโรคที่พบ: {len(disease_spots)}\nความรุนแรง: ปานกลาง\nแนะนำ: ฉีดยาฆ่าเชื้อรา', 
               transform=ax.transAxes, fontsize=9, verticalalignment='top',
               bbox=dict(boxstyle="round,pad=0.3", facecolor='yellow', alpha=0.7))
        
    def fruit_counting(self):
        """จำลองการนับผลไม้"""
        ax = self.axes[0, 1]
        
        # สร้างภาพต้นไม้ที่มีผลไม้
        tree_image = np.ones((150, 150, 3), dtype=np.uint8) * 50  # พื้นหลังเขียวเข้ม
        
        # ใบไม้
        for _ in range(20):
            x, y = np.random.randint(10, 140, 2)
            cv2.circle(tree_image, (x, y), np.random.randint(8, 15), (34, 139, 34), -1)
        
        # ผลไม้ (สีส้ม)
        fruits = [(40, 50), (80, 45), (120, 60), (60, 90), (100, 85), (30, 110), (110, 120)]
        
        for i, (x, y) in enumerate(fruits):
            cv2.circle(tree_image, (x, y), 12, (255, 165, 0), -1)
            # เพิ่มหมายเลข
            cv2.putText(tree_image, str(i+1), (x-5, y+5),
                       cv2.FONT_HERSHEY_SIMPLEX, 0.4, (255, 255, 255), 1)
        
        ax.imshow(tree_image)
        ax.set_title('การนับผลไม้')
        ax.axis('off')
        
        # สถิติ
        ax.text(0.02, 0.98, f'ผลไม้ที่นับได้: {len(fruits)}\nผลไม้สุก: {len(fruits)-2}\nผลไม้ดิบ: 2', 
               transform=ax.transAxes, fontsize=9, verticalalignment='top',
               bbox=dict(boxstyle="round,pad=0.3", facecolor='lightblue', alpha=0.7))
        
    def quality_assessment(self):
        """จำลองการประเมินคุณภาพ"""
        ax = self.axes[1, 0]
        
        # สร้างผลไม้ 3 เกรด
        fruits = []
        grades = ['A', 'B', 'C']
        colors = [(255, 140, 0), (255, 165, 0), (255, 200, 100)]  # ส้มเข้ม, ส้ม, ส้มอ่อน
        
        for i, (grade, color) in enumerate(zip(grades, colors)):
            fruit = np.zeros((50, 50, 3), dtype=np.uint8)
            cv2.circle(fruit, (25, 25), 20, color, -1)
            
            # เพิ่มความเสียหายตามเกรด
            if grade == 'B':
                cv2.circle(fruit, (30, 20), 3, (139, 69, 19), -1)  # จุดเล็ก
            elif grade == 'C':
                cv2.circle(fruit, (30, 20), 5, (139, 69, 19), -1)  # จุดใหญ่
                cv2.circle(fruit, (20, 30), 3, (139, 69, 19), -1)  # จุดเพิ่ม
            
            fruits.append(fruit)
        
        # แสดงผลไม้ทั้ง 3 เกรด
        combined = np.hstack(fruits)
        ax.imshow(combined)
        ax.set_title('การประเมินคุณภาพผลไม้')
        
        # เพิ่มป้ายเกรด
        positions = [25, 75, 125]
        for pos, grade in zip(positions, grades):
            ax.text(pos, 45, f'เกรด {grade}', ha='center', va='center',
                   fontweight='bold', color='white',
                   bbox=dict(boxstyle="round,pad=0.2", facecolor='black', alpha=0.7))
        
        ax.axis('off')
        
    def drone_monitoring(self):
        """จำลองการตรวจสอบด้วยโดรน"""
        ax = self.axes[1, 1]
        
        # สร้างแผนที่สุขภาพพืชจากโดรน
        field_map = np.random.rand(100, 100)
        
        # เพิ่มพื้นที่ที่มีปัญหา
        field_map[20:40, 30:50] *= 0.3  # พื้นที่เครียด
        field_map[60:80, 10:30] *= 0.5  # พื้นที่ปานกลาง
        
        # แสดงแผนที่ด้วยสี
        im = ax.imshow(field_map, cmap='RdYlGn', vmin=0, vmax=1)
        ax.set_title('แผนที่สุขภาพพืชจากโดรน')
        
        # เพิ่ม colorbar
        cbar = plt.colorbar(im, ax=ax, shrink=0.6)
        cbar.set_label('ระดับสุขภาพพืช')
        
        # เพิ่มจุดที่ต้องสนใจ
        problem_areas = [(35, 40), (70, 20)]
        for i, (x, y) in enumerate(problem_areas):
            ax.plot(y, x, 'ro', markersize=8)
            ax.text(y+2, x, f'ปัญหา {i+1}', color='red', fontweight='bold')
        
        ax.set_xlabel('ตำแหน่ง X (เมตร)')
        ax.set_ylabel('ตำแหน่ง Y (เมตร)')
        
    def show(self):
        """แสดงการจำลองทั้งหมด"""
        self.plant_disease_detection()
        self.fruit_counting()
        self.quality_assessment()
        self.drone_monitoring()
        
        plt.tight_layout()
        plt.show()

# Interactive Color Analysis Tool
class ColorAnalysisTool:
    def __init__(self):
        self.fig, self.axes = plt.subplots(2, 3, figsize=(15, 10))
        self.fig.suptitle('เครื่องมือวิเคราะห์สีแบบโต้ตอบ', fontsize=16, fontweight='bold')
        
        # สร้างภาพตัวอย่าง
        self.original_image = self.create_fruit_image()
        self.current_image = self.original_image.copy()
        
        # แสดงภาพต้นฉบับ
        self.axes[0, 0].imshow(self.original_image)
        self.axes[0, 0].set_title('ภาพต้นฉบับ')
        self.axes[0, 0].axis('off')
        
        # สร้าง sliders
        self.create_sliders()
        self.update_analysis()
        
    def create_fruit_image(self):
        """สร้างภาพผลไม้สำหรับการวิเคราะห์"""
        image = np.zeros((200, 200, 3), dtype=np.uint8)
        
        # ผลไม้หลัก
        cv2.circle(image, (100, 100), 80, (255, 140, 0), -1)
        
        # เงา
        cv2.ellipse(image, (120, 120), (30, 40), 45, 0, 360, (200, 100, 0), -1)
        
        # จุดเด่น
        cv2.circle(image, (80, 80), 15, (255, 200, 100), -1)
        
        # จุดเสียหาย
        cv2.circle(image, (110, 90), 8, (139, 69, 19), -1)
        cv2.circle(image, (90, 110), 5, (139, 69, 19), -1)
        
        return image
    
    def create_sliders(self):
        """สร้าง sliders สำหรับปรับค่า"""
        # Brightness slider
        ax_brightness = plt.axes([0.2, 0.02, 0.3, 0.03])
        self.brightness_slider = Slider(ax_brightness, 'Brightness', 0.5, 2.0, valinit=1.0)
        self.brightness_slider.on_changed(self.update_image)
        
        # Contrast slider
        ax_contrast = plt.axes([0.6, 0.02, 0.3, 0.03])
        self.contrast_slider = Slider(ax_contrast, 'Contrast', 0.5, 3.0, valinit=1.0)
        self.contrast_slider.on_changed(self.update_image)
        
    def update_image(self, val):
        """อัปเดตภาพตาม slider values"""
        brightness = self.brightness_slider.val
        contrast = self.contrast_slider.val
        
        # ปรับ brightness และ contrast
        self.current_image = cv2.convertScaleAbs(self.original_image, 
                                               alpha=contrast, beta=(brightness-1)*50)
        
        self.update_analysis()
        
    def update_analysis(self):
        """อัปเดตการวิเคราะห์"""
        # แสดงภาพที่ปรับแล้ว
        self.axes[0, 1].clear()
        self.axes[0, 1].imshow(self.current_image)
        self.axes[0, 1].set_title('ภาพที่ปรับแล้ว')
        self.axes[0, 1].axis('off')
        
        # วิเคราะห์สี
        self.analyze_colors()
        
        plt.draw()
        
    def analyze_colors(self):
        """วิเคราะห์สีของภาพ"""
        # Color histogram
        self.axes[0, 2].clear()
        colors = ('r', 'g', 'b')
        for i, color in enumerate(colors):
            hist = cv2.calcHist([self.current_image], [i], None, [256], [0, 256])
            self.axes[0, 2].plot(hist, color=color, alpha=0.7)
        self.axes[0, 2].set_title('Color Histogram')
        self.axes[0, 2].set_xlabel('Pixel Intensity')
        self.axes[0, 2].set_ylabel('Frequency')
        
        # HSV analysis
        hsv = cv2.cvtColor(self.current_image, cv2.COLOR_RGB2HSV)
        
        # แสดง Hue channel
        self.axes[1, 0].clear()
        self.axes[1, 0].imshow(hsv[:,:,0], cmap='hsv')
        self.axes[1, 0].set_title('Hue Channel')
        self.axes[1, 0].axis('off')
        
        # แสดง Saturation channel
        self.axes[1, 1].clear()
        self.axes[1, 1].imshow(hsv[:,:,1], cmap='gray')
        self.axes[1, 1].set_title('Saturation Channel')
        self.axes[1, 1].axis('off')
        
        # Color clustering
        self.axes[1, 2].clear()
        self.perform_color_clustering()
        
    def perform_color_clustering(self):
        """ทำ color clustering"""
        # Reshape image for clustering
        data = self.current_image.reshape((-1, 3))
        data = np.float32(data)
        
        # K-means clustering
        criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 20, 1.0)
        k = 5
        _, labels, centers = cv2.kmeans(data, k, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)
        
        # แสดงสีหลัก
        centers = np.uint8(centers)
        
        # สร้างแท่งสี
        color_bar = np.zeros((50, 250, 3), dtype=np.uint8)
        for i, color in enumerate(centers):
            start_x = i * 50
            end_x = (i + 1) * 50
            color_bar[:, start_x:end_x] = color
        
        self.axes[1, 2].imshow(color_bar)
        self.axes[1, 2].set_title('สีหลัก (K-means)')
        self.axes[1, 2].axis('off')
        
        # แสดงเปอร์เซ็นต์ของแต่ละสี
        unique, counts = np.unique(labels, return_counts=True)
        percentages = counts / len(labels) * 100
        
        for i, (color, percent) in enumerate(zip(centers, percentages)):
            self.axes[1, 2].text(i*50 + 25, 60, f'{percent:.1f}%', 
                               ha='center', va='center', fontweight='bold')
    
    def show(self):
        """แสดงเครื่องมือ"""
        plt.show()

if __name__ == "__main__":
    print("=== การสาธิต Computer Vision ===")
    print("\n1. การสาธิต Computer Vision พื้นฐาน")
    print("2. การประยุกต์ใช้ในการเกษตร")
    print("3. เครื่องมือวิเคราะห์สีแบบโต้ตอบ")
    
    choice = input("\nเลือกการสาธิต (1, 2, หรือ 3): ")
    
    if choice == "1":
        demo = ComputerVisionDemo()
        demo.start()
    elif choice == "2":
        print("\nกำลังสร้างการจำลองการประยุกต์ใช้ Computer Vision...")
        simulator = AgricultureVisionApplications()
        simulator.show()
    elif choice == "3":
        print("\nกำลังเปิดเครื่องมือวิเคราะห์สีแบบโต้ตอบ...")
        tool = ColorAnalysisTool()
        tool.show()
    else:
        print("ตัวเลือกไม่ถูกต้อง กำลังแสดงการสาธิต Computer Vision พื้นฐาน...")
        demo = ComputerVisionDemo()
        demo.start()

