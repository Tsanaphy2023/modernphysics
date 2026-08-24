import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_classification, make_regression, make_blobs
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.cluster import KMeans
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, mean_squared_error
import seaborn as sns
from matplotlib.widgets import Button, Slider
import pandas as pd

class MLAlgorithmsDemo:
    def __init__(self):
        self.fig = None
        self.current_demo = 0
        self.demos = [
            self.linear_regression_demo,
            self.classification_demo,
            self.clustering_demo,
            self.decision_tree_demo
        ]
        self.demo_names = [
            "Linear Regression",
            "Classification (SVM)",
            "K-Means Clustering", 
            "Decision Tree"
        ]
        
    def linear_regression_demo(self):
        """สาธิต Linear Regression สำหรับทำนายผลผลิตข้าว"""
        if self.fig:
            plt.close(self.fig)
            
        self.fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))
        self.fig.suptitle('Linear Regression: ทำนายผลผลิตข้าวจากปริมาณปุ่ย', fontsize=16, fontweight='bold')
        
        # สร้างข้อมูลตัวอย่าง
        np.random.seed(42)
        fertilizer = np.random.uniform(10, 60, 50)
        noise = np.random.normal(0, 50, 50)
        yield_rice = 500 + 8 * fertilizer + noise
        
        # ฝึกโมเดล
        X = fertilizer.reshape(-1, 1)
        y = yield_rice
        model = LinearRegression()
        model.fit(X, y)
        
        # สร้างเส้นการทำนาย
        x_line = np.linspace(10, 60, 100).reshape(-1, 1)
        y_pred_line = model.predict(x_line)
        
        # กราฟที่ 1: ข้อมูลและเส้นแนวโน้ม
        ax1.scatter(fertilizer, yield_rice, alpha=0.6, color='green', s=60, label='ข้อมูลจริง')
        ax1.plot(x_line, y_pred_line, color='red', linewidth=2, label=f'เส้นแนวโน้ม (R² = {model.score(X, y):.3f})')
        ax1.set_xlabel('ปริมาณปุ่ย (กก./ไร่)')
        ax1.set_ylabel('ผลผลิตข้าว (กก./ไร่)')
        ax1.set_title('ความสัมพันธ์ระหว่างปุ่ยและผลผลิต')
        ax1.legend()
        ax1.grid(True, alpha=0.3)
        
        # กราฟที่ 2: การทำนาย
        test_fertilizer = [25, 35, 45]
        test_predictions = model.predict(np.array(test_fertilizer).reshape(-1, 1))
        
        bars = ax2.bar(['25 กก.', '35 กก.', '45 กก.'], test_predictions, 
                      color=['lightblue', 'lightgreen', 'lightcoral'], alpha=0.7)
        ax2.set_ylabel('ผลผลิตที่ทำนาย (กก./ไร่)')
        ax2.set_title('การทำนายผลผลิตสำหรับปริมาณปุ่ยต่างๆ')
        
        # เพิ่มค่าบนแท่งกราฟ
        for bar, pred in zip(bars, test_predictions):
            ax2.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 10,
                    f'{pred:.0f}', ha='center', va='bottom', fontweight='bold')
        
        # แสดงสมการ
        slope = model.coef_[0]
        intercept = model.intercept_
        equation_text = f'สมการ: ผลผลิต = {intercept:.1f} + {slope:.1f} × ปุ่ย'
        self.fig.text(0.5, 0.02, equation_text, ha='center', fontsize=12, 
                     bbox=dict(boxstyle="round,pad=0.3", facecolor='yellow', alpha=0.7))
        
        plt.tight_layout()
        
    def classification_demo(self):
        """สาธิต Classification สำหรับจำแนกคุณภาพผลไม้"""
        if self.fig:
            plt.close(self.fig)
            
        self.fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))
        self.fig.suptitle('Classification: จำแนกคุณภาพผลไม้', fontsize=16, fontweight='bold')
        
        # สร้างข้อมูลตัวอย่าง
        np.random.seed(42)
        
        # คุณภาพดี (สีเขียว)
        good_weight = np.random.normal(150, 20, 50)
        good_sugar = np.random.normal(12, 2, 50)
        
        # คุณภาพต่ำ (สีแดง)
        bad_weight = np.random.normal(100, 15, 50)
        bad_sugar = np.random.normal(8, 1.5, 50)
        
        # รวมข้อมูล
        X = np.vstack([
            np.column_stack([good_weight, good_sugar]),
            np.column_stack([bad_weight, bad_sugar])
        ])
        y = np.hstack([np.ones(50), np.zeros(50)])  # 1 = ดี, 0 = ต่ำ
        
        # ฝึกโมเดล SVM
        model = SVC(kernel='linear', random_state=42)
        model.fit(X, y)
        
        # สร้าง decision boundary
        h = 2
        x_min, x_max = X[:, 0].min() - 10, X[:, 0].max() + 10
        y_min, y_max = X[:, 1].min() - 2, X[:, 1].max() + 2
        xx, yy = np.meshgrid(np.arange(x_min, x_max, h),
                            np.arange(y_min, y_max, 0.1))
        
        Z = model.predict(np.c_[xx.ravel(), yy.ravel()])
        Z = Z.reshape(xx.shape)
        
        # กราฟที่ 1: ข้อมูลและ decision boundary
        ax1.contourf(xx, yy, Z, alpha=0.3, colors=['red', 'green'])
        scatter1 = ax1.scatter(X[y==1, 0], X[y==1, 1], c='green', marker='o', s=60, alpha=0.8, label='คุณภาพดี')
        scatter2 = ax1.scatter(X[y==0, 0], X[y==0, 1], c='red', marker='x', s=60, alpha=0.8, label='คุณภาพต่ำ')
        ax1.set_xlabel('น้ำหนัก (กรัม)')
        ax1.set_ylabel('ปริมาณน้ำตาล (%)')
        ax1.set_title('การจำแนกคุณภาพผลไม้')
        ax1.legend()
        ax1.grid(True, alpha=0.3)
        
        # กราฟที่ 2: ความแม่นยำ
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
        model_eval = SVC(kernel='linear', random_state=42)
        model_eval.fit(X_train, y_train)
        y_pred = model_eval.predict(X_test)
        accuracy = accuracy_score(y_test, y_pred)
        
        # Confusion Matrix
        from sklearn.metrics import confusion_matrix
        cm = confusion_matrix(y_test, y_pred)
        
        im = ax2.imshow(cm, interpolation='nearest', cmap='Blues')
        ax2.set_title(f'Confusion Matrix\n(ความแม่นยำ: {accuracy:.2%})')
        
        # เพิ่มข้อความในช่อง
        thresh = cm.max() / 2.
        for i in range(cm.shape[0]):
            for j in range(cm.shape[1]):
                ax2.text(j, i, format(cm[i, j], 'd'),
                        ha="center", va="center",
                        color="white" if cm[i, j] > thresh else "black",
                        fontsize=20, fontweight='bold')
        
        ax2.set_ylabel('ค่าจริง')
        ax2.set_xlabel('ค่าทำนาย')
        ax2.set_xticks([0, 1])
        ax2.set_yticks([0, 1])
        ax2.set_xticklabels(['คุณภาพต่ำ', 'คุณภาพดี'])
        ax2.set_yticklabels(['คุณภาพต่ำ', 'คุณภาพดี'])
        
        plt.tight_layout()
        
    def clustering_demo(self):
        """สาธิต K-Means Clustering สำหรับจัดกลุ่มเกษตรกร"""
        if self.fig:
            plt.close(self.fig)
            
        self.fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))
        self.fig.suptitle('K-Means Clustering: จัดกลุ่มเกษตรกร', fontsize=16, fontweight='bold')
        
        # สร้างข้อมูลตัวอย่าง
        np.random.seed(42)
        
        # กลุ่มที่ 1: เกษตรกรรายย่อย
        small_farm_size = np.random.normal(5, 2, 30)
        small_income = np.random.normal(100000, 30000, 30)
        
        # กลุ่มที่ 2: เกษตรกรรายกลาง
        medium_farm_size = np.random.normal(15, 3, 30)
        medium_income = np.random.normal(300000, 50000, 30)
        
        # กลุ่มที่ 3: เกษตรกรรายใหญ่
        large_farm_size = np.random.normal(30, 5, 30)
        large_income = np.random.normal(600000, 100000, 30)
        
        # รวมข้อมูล
        X = np.vstack([
            np.column_stack([small_farm_size, small_income]),
            np.column_stack([medium_farm_size, medium_income]),
            np.column_stack([large_farm_size, large_income])
        ])
        
        # K-Means Clustering
        kmeans = KMeans(n_clusters=3, random_state=42)
        clusters = kmeans.fit_predict(X)
        centers = kmeans.cluster_centers_
        
        # กราฟที่ 1: ผลการจัดกลุ่ม
        colors = ['red', 'blue', 'green']
        cluster_names = ['รายย่อย', 'รายกลาง', 'รายใหญ่']
        
        for i in range(3):
            mask = clusters == i
            ax1.scatter(X[mask, 0], X[mask, 1], c=colors[i], alpha=0.6, s=60, label=f'กลุ่ม {cluster_names[i]}')
        
        # แสดงจุดศูนย์กลาง
        ax1.scatter(centers[:, 0], centers[:, 1], c='black', marker='x', s=200, linewidths=3, label='จุดศูนย์กลาง')
        
        ax1.set_xlabel('ขนาดฟาร์ม (ไร่)')
        ax1.set_ylabel('รายได้ (บาท/ปี)')
        ax1.set_title('การจัดกลุ่มเกษตรกร')
        ax1.legend()
        ax1.grid(True, alpha=0.3)
        
        # กราฟที่ 2: ลักษณะของแต่ละกลุ่ม
        cluster_data = []
        for i in range(3):
            mask = clusters == i
            avg_size = np.mean(X[mask, 0])
            avg_income = np.mean(X[mask, 1])
            cluster_data.append([avg_size, avg_income/1000])  # แปลงเป็นพันบาท
        
        cluster_df = pd.DataFrame(cluster_data, 
                                columns=['ขนาดฟาร์มเฉลี่ย', 'รายได้เฉลี่ย (พันบาท)'],
                                index=['รายย่อย', 'รายกลาง', 'รายใหญ่'])
        
        # สร้าง bar chart
        x_pos = np.arange(len(cluster_names))
        width = 0.35
        
        bars1 = ax2.bar(x_pos - width/2, cluster_df['ขนาดฟาร์มเฉลี่ย'], width, 
                       label='ขนาดฟาร์ม (ไร่)', color='lightblue', alpha=0.7)
        bars2 = ax2.bar(x_pos + width/2, cluster_df['รายได้เฉลี่ย (พันบาท)'], width,
                       label='รายได้ (พันบาท)', color='lightgreen', alpha=0.7)
        
        ax2.set_xlabel('กลุ่มเกษตรกร')
        ax2.set_ylabel('ค่าเฉลี่ย')
        ax2.set_title('ลักษณะเฉลี่ยของแต่ละกลุ่ม')
        ax2.set_xticks(x_pos)
        ax2.set_xticklabels(cluster_names)
        ax2.legend()
        
        # เพิ่มค่าบนแท่งกราฟ
        for bars in [bars1, bars2]:
            for bar in bars:
                height = bar.get_height()
                ax2.text(bar.get_x() + bar.get_width()/2., height + height*0.01,
                        f'{height:.0f}', ha='center', va='bottom', fontsize=10)
        
        plt.tight_layout()
        
    def decision_tree_demo(self):
        """สาธิต Decision Tree สำหรับตัดสินใจการรดน้ำ"""
        if self.fig:
            plt.close(self.fig)
            
        self.fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 8))
        self.fig.suptitle('Decision Tree: ตัดสินใจการรดน้ำพืช', fontsize=16, fontweight='bold')
        
        # สร้างข้อมูลตัวอย่าง
        np.random.seed(42)
        n_samples = 100
        
        # สร้างข้อมูล: ความชื้นดิน, อุณหภูมิ, ความชื้นอากาศ
        soil_moisture = np.random.uniform(10, 80, n_samples)
        temperature = np.random.uniform(20, 40, n_samples)
        humidity = np.random.uniform(40, 90, n_samples)
        
        # สร้างกฎการตัดสินใจ (ควรรดน้ำหรือไม่)
        should_water = np.zeros(n_samples)
        for i in range(n_samples):
            if soil_moisture[i] < 30:  # ดินแห้ง
                if temperature[i] > 35:  # อากาศร้อน
                    should_water[i] = 2  # รดน้ำมาก
                else:
                    should_water[i] = 1  # รดน้ำปานกลาง
            elif soil_moisture[i] < 50:  # ดินชื้นปานกลาง
                if temperature[i] > 35 and humidity[i] < 60:
                    should_water[i] = 1  # รดน้ำปานกลาง
                else:
                    should_water[i] = 0  # ไม่ต้องรดน้ำ
            else:  # ดินชื้น
                should_water[i] = 0  # ไม่ต้องรดน้ำ
        
        # เตรียมข้อมูล
        X = np.column_stack([soil_moisture, temperature, humidity])
        y = should_water
        
        # สร้างและฝึก Decision Tree
        tree = DecisionTreeClassifier(max_depth=3, random_state=42)
        tree.fit(X, y)
        
        # กราฟที่ 1: แสดง Decision Tree
        plot_tree(tree, ax=ax1, 
                 feature_names=['ความชื้นดิน', 'อุณหภูมิ', 'ความชื้นอากาศ'],
                 class_names=['ไม่รดน้ำ', 'รดน้ำปานกลาง', 'รดน้ำมาก'],
                 filled=True, rounded=True, fontsize=8)
        ax1.set_title('โครงสร้าง Decision Tree')
        
        # กราฟที่ 2: ความสำคัญของตัวแปร
        feature_importance = tree.feature_importances_
        feature_names = ['ความชื้นดิน', 'อุณหภูมิ', 'ความชื้นอากาศ']
        
        bars = ax2.bar(feature_names, feature_importance, 
                      color=['brown', 'red', 'blue'], alpha=0.7)
        ax2.set_ylabel('ความสำคัญ')
        ax2.set_title('ความสำคัญของปัจจัยต่างๆ')
        ax2.set_ylim(0, 1)
        
        # เพิ่มค่าบนแท่งกราฟ
        for bar, importance in zip(bars, feature_importance):
            ax2.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.01,
                    f'{importance:.3f}', ha='center', va='bottom', fontweight='bold')
        
        plt.setp(ax2.get_xticklabels(), rotation=45, ha='right')
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
        print("=== การสาธิตอัลกอริทึม Machine Learning ===")
        print("ใช้ปุ่ม 'ถัดไป' และ 'ก่อนหน้า' เพื่อดูการสาธิตต่างๆ")
        print("\nการสาธิตที่มี:")
        for i, name in enumerate(self.demo_names, 1):
            print(f"{i}. {name}")
        
        self.show_current_demo()
        plt.show()

# Agricultural Data Simulator
class AgriculturalDataSimulator:
    def __init__(self):
        self.fig, self.axes = plt.subplots(2, 2, figsize=(15, 12))
        self.fig.suptitle('การจำลองข้อมูลการเกษตรด้วย Machine Learning', fontsize=16, fontweight='bold')
        
    def simulate_crop_yield_prediction(self):
        """จำลองการทำนายผลผลิต"""
        ax = self.axes[0, 0]
        
        # สร้างข้อมูลหลายตัวแปร
        np.random.seed(42)
        n_samples = 200
        
        # ตัวแปรอิสระ
        rainfall = np.random.normal(100, 30, n_samples)
        temperature = np.random.normal(28, 5, n_samples)
        fertilizer = np.random.uniform(20, 80, n_samples)
        
        # ตัวแปรตาม (ผลผลิต)
        yield_crop = (
            500 + 
            2 * rainfall + 
            10 * temperature + 
            5 * fertilizer + 
            np.random.normal(0, 100, n_samples)
        )
        
        # สร้างโมเดล Multiple Linear Regression
        from sklearn.linear_model import LinearRegression
        X = np.column_stack([rainfall, temperature, fertilizer])
        model = LinearRegression()
        model.fit(X, yield_crop)
        
        # ทำนาย
        y_pred = model.predict(X)
        
        # แสดงผล
        ax.scatter(yield_crop, y_pred, alpha=0.6, color='green')
        ax.plot([yield_crop.min(), yield_crop.max()], [yield_crop.min(), yield_crop.max()], 'r--', lw=2)
        ax.set_xlabel('ผลผลิตจริง (กก./ไร่)')
        ax.set_ylabel('ผลผลิตที่ทำนาย (กก./ไร่)')
        ax.set_title(f'การทำนายผลผลิต (R² = {model.score(X, yield_crop):.3f})')
        ax.grid(True, alpha=0.3)
        
    def simulate_pest_detection(self):
        """จำลองการตรวจจับศัตรูพืช"""
        ax = self.axes[0, 1]
        
        # สร้างข้อมูลการตรวจจับศัตรูพืช
        np.random.seed(42)
        
        # พื้นที่ปกติ
        normal_temp = np.random.normal(25, 3, 100)
        normal_humidity = np.random.normal(60, 10, 100)
        
        # พื้นที่มีศัตรูพืช
        pest_temp = np.random.normal(30, 2, 50)
        pest_humidity = np.random.normal(80, 8, 50)
        
        # รวมข้อมูล
        temp_all = np.concatenate([normal_temp, pest_temp])
        humidity_all = np.concatenate([normal_humidity, pest_humidity])
        labels = np.concatenate([np.zeros(100), np.ones(50)])
        
        # แสดงผล
        normal_mask = labels == 0
        pest_mask = labels == 1
        
        ax.scatter(temp_all[normal_mask], humidity_all[normal_mask], 
                  c='green', alpha=0.6, label='ปกติ', s=40)
        ax.scatter(temp_all[pest_mask], humidity_all[pest_mask], 
                  c='red', alpha=0.6, label='มีศัตรูพืช', s=40)
        
        ax.set_xlabel('อุณหภูมิ (°C)')
        ax.set_ylabel('ความชื้น (%)')
        ax.set_title('การตรวจจับศัตรูพืช')
        ax.legend()
        ax.grid(True, alpha=0.3)
        
    def simulate_irrigation_optimization(self):
        """จำลองการปรับปรุงระบบชลประทาน"""
        ax = self.axes[1, 0]
        
        # สร้างข้อมูลการใช้น้ำ
        days = np.arange(1, 31)
        
        # การใช้น้ำแบบเดิม (ไม่มี AI)
        traditional_water = np.random.normal(100, 20, 30)
        traditional_water = np.clip(traditional_water, 50, 150)
        
        # การใช้น้ำด้วย AI (ปรับตามสภาพอากาศ)
        weather_factor = np.sin(days * 0.2) * 20 + np.random.normal(0, 10, 30)
        ai_water = 80 + weather_factor
        ai_water = np.clip(ai_water, 30, 120)
        
        # แสดงผล
        ax.plot(days, traditional_water, 'r-o', label='วิธีเดิม', linewidth=2, markersize=4)
        ax.plot(days, ai_water, 'b-s', label='ด้วย AI', linewidth=2, markersize=4)
        ax.fill_between(days, traditional_water, alpha=0.3, color='red')
        ax.fill_between(days, ai_water, alpha=0.3, color='blue')
        
        ax.set_xlabel('วัน')
        ax.set_ylabel('ปริมาณน้ำ (ลิตร/ตร.ม.)')
        ax.set_title('การเปรียบเทียบการใช้น้ำ')
        ax.legend()
        ax.grid(True, alpha=0.3)
        
        # แสดงการประหยัด
        total_traditional = np.sum(traditional_water)
        total_ai = np.sum(ai_water)
        savings = ((total_traditional - total_ai) / total_traditional) * 100
        
        ax.text(0.02, 0.98, f'ประหยัดน้ำ: {savings:.1f}%', 
               transform=ax.transAxes, fontsize=12, fontweight='bold',
               bbox=dict(boxstyle="round,pad=0.3", facecolor='yellow', alpha=0.7),
               verticalalignment='top')
        
    def simulate_market_price_prediction(self):
        """จำลองการทำนายราคาตลาด"""
        ax = self.axes[1, 1]
        
        # สร้างข้อมูลราคาข้าว
        np.random.seed(42)
        days = np.arange(1, 101)
        
        # ราคาพื้นฐาน + แนวโน้ม + ความผันผวน
        base_price = 15
        trend = 0.02 * days
        seasonal = 2 * np.sin(days * 0.1) 
        noise = np.random.normal(0, 0.5, 100)
        
        actual_price = base_price + trend + seasonal + noise
        
        # ทำนายด้วย Moving Average
        window = 10
        predicted_price = np.convolve(actual_price, np.ones(window)/window, mode='same')
        
        # แสดงผล
        ax.plot(days, actual_price, 'g-', alpha=0.7, label='ราคาจริง', linewidth=1)
        ax.plot(days, predicted_price, 'r-', label='ราคาที่ทำนาย', linewidth=2)
        ax.fill_between(days, actual_price, predicted_price, alpha=0.2, color='gray')
        
        ax.set_xlabel('วัน')
        ax.set_ylabel('ราคาข้าว (บาท/กก.)')
        ax.set_title('การทำนายราคาข้าว')
        ax.legend()
        ax.grid(True, alpha=0.3)
        
        # คำนวณความแม่นยำ
        mse = np.mean((actual_price - predicted_price)**2)
        ax.text(0.02, 0.98, f'MSE: {mse:.2f}', 
               transform=ax.transAxes, fontsize=12, fontweight='bold',
               bbox=dict(boxstyle="round,pad=0.3", facecolor='lightblue', alpha=0.7),
               verticalalignment='top')
    
    def show(self):
        """แสดงการจำลองทั้งหมด"""
        self.simulate_crop_yield_prediction()
        self.simulate_pest_detection()
        self.simulate_irrigation_optimization()
        self.simulate_market_price_prediction()
        
        plt.tight_layout()
        plt.show()

if __name__ == "__main__":
    print("=== การสาธิตอัลกอริทึม Machine Learning สำหรับการเกษตร ===")
    print("\n1. การสาธิตอัลกอริทึมพื้นฐาน")
    print("2. การจำลองการใช้งานในการเกษตร")
    
    choice = input("\nเลือกการสาธิต (1 หรือ 2): ")
    
    if choice == "1":
        demo = MLAlgorithmsDemo()
        demo.start()
    elif choice == "2":
        print("\nกำลังสร้างการจำลองข้อมูลการเกษตร...")
        simulator = AgriculturalDataSimulator()
        simulator.show()
    else:
        print("ตัวเลือกไม่ถูกต้อง กำลังแสดงการสาธิตอัลกอริทึมพื้นฐาน...")
        demo = MLAlgorithmsDemo()
        demo.start()

