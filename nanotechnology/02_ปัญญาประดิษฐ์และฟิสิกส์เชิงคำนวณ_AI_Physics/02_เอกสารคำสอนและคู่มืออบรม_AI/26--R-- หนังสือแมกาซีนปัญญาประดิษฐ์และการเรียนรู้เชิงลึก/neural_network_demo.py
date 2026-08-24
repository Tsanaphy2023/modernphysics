import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button
import matplotlib.patches as patches
from matplotlib.animation import FuncAnimation
import seaborn as sns

class NeuralNetworkVisualizer:
    def __init__(self):
        self.fig = None
        self.current_demo = 0
        self.demos = [
            self.neuron_demo,
            self.network_architecture_demo,
            self.activation_functions_demo,
            self.training_process_demo,
            self.cnn_demo
        ]
        self.demo_names = [
            "Single Neuron",
            "Network Architecture",
            "Activation Functions",
            "Training Process",
            "CNN Visualization"
        ]
        
    def neuron_demo(self):
        """สาธิตการทำงานของ Neuron เดี่ยว"""
        if self.fig:
            plt.close(self.fig)
            
        self.fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))
        self.fig.suptitle('การทำงานของ Neuron เดี่ยว', fontsize=16, fontweight='bold')
        
        # ข้อมูลตัวอย่าง
        inputs = np.array([0.5, 0.3, 0.2])
        weights = np.array([0.4, 0.7, -0.2])
        bias = 0.1
        
        # คำนวณ
        weighted_sum = np.dot(inputs, weights) + bias
        output = 1 / (1 + np.exp(-weighted_sum))  # Sigmoid
        
        # กราฟที่ 1: โครงสร้าง Neuron
        ax1.set_xlim(0, 10)
        ax1.set_ylim(0, 6)
        
        # Input nodes
        input_positions = [(1, 4.5), (1, 3), (1, 1.5)]
        input_labels = ['Input 1\n(0.5)', 'Input 2\n(0.3)', 'Input 3\n(0.2)']
        
        for i, (pos, label) in enumerate(zip(input_positions, input_labels)):
            circle = plt.Circle(pos, 0.3, color='lightblue', alpha=0.7)
            ax1.add_patch(circle)
            ax1.text(pos[0], pos[1], label, ha='center', va='center', fontsize=8, fontweight='bold')
        
        # Neuron
        neuron_pos = (6, 3)
        neuron = plt.Circle(neuron_pos, 0.5, color='orange', alpha=0.8)
        ax1.add_patch(neuron)
        ax1.text(neuron_pos[0], neuron_pos[1], f'Σ\n{weighted_sum:.2f}', ha='center', va='center', 
                fontsize=10, fontweight='bold')
        
        # Connections with weights
        colors = ['green' if w > 0 else 'red' for w in weights]
        for i, (input_pos, weight, color) in enumerate(zip(input_positions, weights, colors)):
            ax1.plot([input_pos[0] + 0.3, neuron_pos[0] - 0.5], 
                    [input_pos[1], neuron_pos[1]], 
                    color=color, linewidth=abs(weight)*5, alpha=0.7)
            
            # Weight labels
            mid_x = (input_pos[0] + neuron_pos[0]) / 2
            mid_y = (input_pos[1] + neuron_pos[1]) / 2
            ax1.text(mid_x, mid_y + 0.2, f'w={weight:.1f}', ha='center', va='center',
                    fontsize=8, bbox=dict(boxstyle="round,pad=0.2", facecolor='white', alpha=0.8))
        
        # Bias
        ax1.text(neuron_pos[0], neuron_pos[1] - 0.8, f'bias = {bias}', ha='center', va='center',
                fontsize=9, bbox=dict(boxstyle="round,pad=0.2", facecolor='yellow', alpha=0.7))
        
        # Output
        output_pos = (9, 3)
        output_circle = plt.Circle(output_pos, 0.3, color='lightgreen', alpha=0.8)
        ax1.add_patch(output_circle)
        ax1.text(output_pos[0], output_pos[1], f'Output\n{output:.3f}', ha='center', va='center',
                fontsize=9, fontweight='bold')
        
        # Connection to output
        ax1.plot([neuron_pos[0] + 0.5, output_pos[0] - 0.3], 
                [neuron_pos[1], output_pos[1]], 
                color='blue', linewidth=3, alpha=0.7)
        
        # Activation function label
        ax1.text(7.5, 3.5, 'Sigmoid', ha='center', va='center', fontsize=9,
                bbox=dict(boxstyle="round,pad=0.2", facecolor='lightcyan', alpha=0.8))
        
        ax1.set_title('โครงสร้างและการคำนวณของ Neuron')
        ax1.axis('off')
        
        # กราฟที่ 2: Sigmoid Function
        x = np.linspace(-5, 5, 100)
        sigmoid_y = 1 / (1 + np.exp(-x))
        
        ax2.plot(x, sigmoid_y, 'b-', linewidth=3, label='Sigmoid Function')
        ax2.axhline(y=0.5, color='gray', linestyle='--', alpha=0.5)
        ax2.axvline(x=0, color='gray', linestyle='--', alpha=0.5)
        
        # แสดงจุดที่คำนวณได้
        ax2.plot(weighted_sum, output, 'ro', markersize=10, label=f'Our Result ({weighted_sum:.2f}, {output:.3f})')
        
        ax2.set_xlabel('Input (Weighted Sum)')
        ax2.set_ylabel('Output')
        ax2.set_title('Sigmoid Activation Function')
        ax2.legend()
        ax2.grid(True, alpha=0.3)
        
        plt.tight_layout()
        
    def network_architecture_demo(self):
        """สาธิตสถาปัตยกรรมของ Neural Network"""
        if self.fig:
            plt.close(self.fig)
            
        self.fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 8))
        self.fig.suptitle('สถาปัตยกรรมของ Neural Network', fontsize=16, fontweight='bold')
        
        # กราฟที่ 1: Simple Network
        ax1.set_xlim(0, 10)
        ax1.set_ylim(0, 8)
        
        # Layer positions
        input_layer_x = 2
        hidden_layer_x = 5
        output_layer_x = 8
        
        # Input layer (3 neurons)
        input_positions = [(input_layer_x, 6), (input_layer_x, 4), (input_layer_x, 2)]
        for i, pos in enumerate(input_positions):
            circle = plt.Circle(pos, 0.3, color='lightblue', alpha=0.8)
            ax1.add_patch(circle)
            ax1.text(pos[0], pos[1], f'I{i+1}', ha='center', va='center', fontweight='bold')
        
        # Hidden layer (4 neurons)
        hidden_positions = [(hidden_layer_x, 6.5), (hidden_layer_x, 4.5), (hidden_layer_x, 2.5), (hidden_layer_x, 0.5)]
        for i, pos in enumerate(hidden_positions):
            circle = plt.Circle(pos, 0.3, color='orange', alpha=0.8)
            ax1.add_patch(circle)
            ax1.text(pos[0], pos[1], f'H{i+1}', ha='center', va='center', fontweight='bold')
        
        # Output layer (2 neurons)
        output_positions = [(output_layer_x, 5), (output_layer_x, 3)]
        for i, pos in enumerate(output_positions):
            circle = plt.Circle(pos, 0.3, color='lightgreen', alpha=0.8)
            ax1.add_patch(circle)
            ax1.text(pos[0], pos[1], f'O{i+1}', ha='center', va='center', fontweight='bold')
        
        # Connections
        # Input to Hidden
        for input_pos in input_positions:
            for hidden_pos in hidden_positions:
                ax1.plot([input_pos[0] + 0.3, hidden_pos[0] - 0.3], 
                        [input_pos[1], hidden_pos[1]], 
                        color='gray', alpha=0.3, linewidth=1)
        
        # Hidden to Output
        for hidden_pos in hidden_positions:
            for output_pos in output_positions:
                ax1.plot([hidden_pos[0] + 0.3, output_pos[0] - 0.3], 
                        [hidden_pos[1], output_pos[1]], 
                        color='gray', alpha=0.3, linewidth=1)
        
        # Layer labels
        ax1.text(input_layer_x, 7.5, 'Input Layer\n(3 neurons)', ha='center', va='center',
                fontsize=10, fontweight='bold', 
                bbox=dict(boxstyle="round,pad=0.3", facecolor='lightblue', alpha=0.5))
        ax1.text(hidden_layer_x, 7.5, 'Hidden Layer\n(4 neurons)', ha='center', va='center',
                fontsize=10, fontweight='bold',
                bbox=dict(boxstyle="round,pad=0.3", facecolor='orange', alpha=0.5))
        ax1.text(output_layer_x, 7.5, 'Output Layer\n(2 neurons)', ha='center', va='center',
                fontsize=10, fontweight='bold',
                bbox=dict(boxstyle="round,pad=0.3", facecolor='lightgreen', alpha=0.5))
        
        ax1.set_title('Simple Feedforward Neural Network')
        ax1.axis('off')
        
        # กราฟที่ 2: Deep Network
        ax2.set_xlim(0, 12)
        ax2.set_ylim(0, 8)
        
        layer_positions = [1, 3, 5, 7, 9, 11]
        layer_sizes = [3, 5, 4, 4, 3, 2]
        layer_colors = ['lightblue', 'orange', 'orange', 'orange', 'orange', 'lightgreen']
        layer_names = ['Input', 'Hidden 1', 'Hidden 2', 'Hidden 3', 'Hidden 4', 'Output']
        
        for layer_idx, (x_pos, size, color, name) in enumerate(zip(layer_positions, layer_sizes, layer_colors, layer_names)):
            y_positions = np.linspace(1, 7, size)
            
            for y_pos in y_positions:
                circle = plt.Circle((x_pos, y_pos), 0.2, color=color, alpha=0.8)
                ax2.add_patch(circle)
            
            # Layer label
            ax2.text(x_pos, 0.3, name, ha='center', va='center', fontsize=8, fontweight='bold',
                    rotation=45)
            
            # Connections to next layer
            if layer_idx < len(layer_positions) - 1:
                next_x = layer_positions[layer_idx + 1]
                next_size = layer_sizes[layer_idx + 1]
                next_y_positions = np.linspace(1, 7, next_size)
                
                for y1 in y_positions:
                    for y2 in next_y_positions:
                        ax2.plot([x_pos + 0.2, next_x - 0.2], [y1, y2], 
                                color='gray', alpha=0.1, linewidth=0.5)
        
        ax2.set_title('Deep Neural Network (6 layers)')
        ax2.axis('off')
        
        plt.tight_layout()
        
    def activation_functions_demo(self):
        """สาธิต Activation Functions ต่างๆ"""
        if self.fig:
            plt.close(self.fig)
            
        self.fig, axes = plt.subplots(2, 2, figsize=(15, 10))
        self.fig.suptitle('Activation Functions ในการเกษตร', fontsize=16, fontweight='bold')
        
        x = np.linspace(-5, 5, 100)
        
        # Sigmoid
        sigmoid = 1 / (1 + np.exp(-x))
        axes[0,0].plot(x, sigmoid, 'b-', linewidth=3, label='Sigmoid')
        axes[0,0].set_title('Sigmoid: เหมาะสำหรับ Binary Classification\n(เช่น พืชสุขภาพดี/ป่วย)')
        axes[0,0].grid(True, alpha=0.3)
        axes[0,0].legend()
        axes[0,0].set_ylim(-0.1, 1.1)
        
        # ReLU
        relu = np.maximum(0, x)
        axes[0,1].plot(x, relu, 'r-', linewidth=3, label='ReLU')
        axes[0,1].set_title('ReLU: เหมาะสำหรับ Hidden Layers\n(เช่น การประมวลผลภาพใบไม้)')
        axes[0,1].grid(True, alpha=0.3)
        axes[0,1].legend()
        
        # Tanh
        tanh = np.tanh(x)
        axes[1,0].plot(x, tanh, 'g-', linewidth=3, label='Tanh')
        axes[1,0].set_title('Tanh: เหมาะสำหรับ Normalized Data\n(เช่น ข้อมูลสภาพอากาศที่ปรับแล้ว)')
        axes[1,0].grid(True, alpha=0.3)
        axes[1,0].legend()
        axes[1,0].set_ylim(-1.1, 1.1)
        
        # Leaky ReLU
        leaky_relu = np.where(x > 0, x, 0.01 * x)
        axes[1,1].plot(x, leaky_relu, 'm-', linewidth=3, label='Leaky ReLU')
        axes[1,1].set_title('Leaky ReLU: แก้ปัญหา Dead Neurons\n(เช่น การวิเคราะห์ข้อมูลเซ็นเซอร์)')
        axes[1,1].grid(True, alpha=0.3)
        axes[1,1].legend()
        
        plt.tight_layout()
        
    def training_process_demo(self):
        """สาธิตกระบวนการฝึก Neural Network"""
        if self.fig:
            plt.close(self.fig)
            
        self.fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(15, 12))
        self.fig.suptitle('กระบวนการฝึก Neural Network สำหรับทำนายผลผลิต', fontsize=16, fontweight='bold')
        
        # สร้างข้อมูลตัวอย่าง
        np.random.seed(42)
        epochs = 100
        
        # Training loss curve
        initial_loss = 10.0
        loss_curve = []
        for epoch in range(epochs):
            # จำลอง loss ที่ลดลงแบบ exponential decay
            loss = initial_loss * np.exp(-epoch * 0.05) + np.random.normal(0, 0.1)
            loss_curve.append(max(loss, 0.1))  # ไม่ให้ติดลบ
        
        ax1.plot(range(epochs), loss_curve, 'b-', linewidth=2)
        ax1.set_xlabel('Epoch')
        ax1.set_ylabel('Loss')
        ax1.set_title('Training Loss: การลดลงของ Error')
        ax1.grid(True, alpha=0.3)
        
        # แสดงจุดสำคัญ
        milestones = [10, 30, 60, 90]
        for milestone in milestones:
            ax1.axvline(x=milestone, color='red', linestyle='--', alpha=0.5)
            ax1.text(milestone, loss_curve[milestone] + 0.5, f'Epoch {milestone}', 
                    rotation=90, ha='center', va='bottom', fontsize=8)
        
        # Accuracy curve
        accuracy_curve = []
        for epoch in range(epochs):
            # จำลอง accuracy ที่เพิ่มขึ้น
            acc = 0.5 + 0.4 * (1 - np.exp(-epoch * 0.03)) + np.random.normal(0, 0.01)
            accuracy_curve.append(min(acc, 0.95))  # ไม่ให้เกิน 95%
        
        ax2.plot(range(epochs), accuracy_curve, 'g-', linewidth=2, label='Training Accuracy')
        
        # Validation accuracy (ต่ำกว่าเล็กน้อย)
        val_accuracy = [acc - 0.05 + np.random.normal(0, 0.005) for acc in accuracy_curve]
        ax2.plot(range(epochs), val_accuracy, 'orange', linewidth=2, label='Validation Accuracy')
        
        ax2.set_xlabel('Epoch')
        ax2.set_ylabel('Accuracy')
        ax2.set_title('Model Accuracy: การปรับปรุงความแม่นยำ')
        ax2.legend()
        ax2.grid(True, alpha=0.3)
        
        # Weight evolution
        weight_history = []
        for epoch in range(epochs):
            # จำลองการเปลี่ยนแปลงของ weights
            if epoch == 0:
                weights = np.random.normal(0, 0.5, 5)
            else:
                # weights ค่อยๆ ปรับเข้าสู่ค่าที่เหมาะสม
                target_weights = np.array([0.8, -0.3, 0.6, 0.2, -0.4])
                weights = weights + 0.02 * (target_weights - weights) + np.random.normal(0, 0.01, 5)
            weight_history.append(weights.copy())
        
        weight_history = np.array(weight_history)
        
        for i in range(5):
            ax3.plot(range(epochs), weight_history[:, i], linewidth=2, label=f'Weight {i+1}')
        
        ax3.set_xlabel('Epoch')
        ax3.set_ylabel('Weight Value')
        ax3.set_title('Weight Evolution: การปรับค่า Weights')
        ax3.legend()
        ax3.grid(True, alpha=0.3)
        
        # Prediction vs Actual
        # สร้างข้อมูลทำนายผลผลิต
        actual_yield = np.random.normal(800, 100, 50)
        
        # จำลองการทำนายที่ดีขึ้นเรื่อยๆ
        early_predictions = actual_yield + np.random.normal(0, 150, 50)  # ทำนายไม่แม่นยำ
        final_predictions = actual_yield + np.random.normal(0, 50, 50)   # ทำนายแม่นยำขึ้น
        
        ax4.scatter(actual_yield, early_predictions, alpha=0.6, color='red', label='Early Training (Epoch 10)')
        ax4.scatter(actual_yield, final_predictions, alpha=0.6, color='blue', label='Final Model (Epoch 100)')
        
        # Perfect prediction line
        min_val, max_val = min(actual_yield.min(), early_predictions.min()), max(actual_yield.max(), early_predictions.max())
        ax4.plot([min_val, max_val], [min_val, max_val], 'k--', alpha=0.5, label='Perfect Prediction')
        
        ax4.set_xlabel('Actual Yield (kg/rai)')
        ax4.set_ylabel('Predicted Yield (kg/rai)')
        ax4.set_title('Prediction Improvement: การปรับปรุงการทำนาย')
        ax4.legend()
        ax4.grid(True, alpha=0.3)
        
        plt.tight_layout()
        
    def cnn_demo(self):
        """สาธิตการทำงานของ CNN"""
        if self.fig:
            plt.close(self.fig)
            
        self.fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(15, 12))
        self.fig.suptitle('Convolutional Neural Network สำหรับการตรวจจับโรคพืช', fontsize=16, fontweight='bold')
        
        # สร้างภาพตัวอย่าง (ใบไม้)
        np.random.seed(42)
        
        # Original image (8x8 สำหรับความง่าย)
        original_image = np.random.rand(8, 8)
        # เพิ่มรูปแบบที่เหมือนใบไม้
        for i in range(8):
            for j in range(8):
                if (i-4)**2 + (j-4)**2 < 9:  # วงกลมกลาง
                    original_image[i, j] = 0.8
                if abs(i-j) < 2:  # เส้นทแยงมุม (เส้นกลางใบ)
                    original_image[i, j] = 0.3
        
        im1 = ax1.imshow(original_image, cmap='Greens', interpolation='nearest')
        ax1.set_title('Input Image: ภาพใบไม้ (8×8)')
        ax1.set_xticks(range(8))
        ax1.set_yticks(range(8))
        plt.colorbar(im1, ax=ax1, shrink=0.6)
        
        # Convolution with edge detection filter
        edge_filter = np.array([[-1, -1, -1],
                               [-1,  8, -1],
                               [-1, -1, -1]])
        
        # Apply convolution
        conv_result = np.zeros((6, 6))
        for i in range(6):
            for j in range(6):
                conv_result[i, j] = np.sum(original_image[i:i+3, j:j+3] * edge_filter)
        
        im2 = ax2.imshow(conv_result, cmap='RdBu', interpolation='nearest')
        ax2.set_title('After Convolution: ตรวจจับขอบ (6×6)')
        ax2.set_xticks(range(6))
        ax2.set_yticks(range(6))
        plt.colorbar(im2, ax=ax2, shrink=0.6)
        
        # Max pooling (2x2)
        pooled_result = np.zeros((3, 3))
        for i in range(3):
            for j in range(3):
                pooled_result[i, j] = np.max(conv_result[i*2:(i+1)*2, j*2:(j+1)*2])
        
        im3 = ax3.imshow(pooled_result, cmap='RdBu', interpolation='nearest')
        ax3.set_title('After Max Pooling: ลดขนาด (3×3)')
        ax3.set_xticks(range(3))
        ax3.set_yticks(range(3))
        plt.colorbar(im3, ax=ax3, shrink=0.6)
        
        # Feature map visualization
        # สร้าง feature maps หลายตัว
        feature_maps = []
        filters = [
            np.array([[1, 0, -1], [1, 0, -1], [1, 0, -1]]),  # Vertical edges
            np.array([[1, 1, 1], [0, 0, 0], [-1, -1, -1]]),  # Horizontal edges
            np.array([[0, -1, 0], [-1, 4, -1], [0, -1, 0]])  # Center detection
        ]
        
        for filt in filters:
            feature_map = np.zeros((6, 6))
            for i in range(6):
                for j in range(6):
                    feature_map[i, j] = np.sum(original_image[i:i+3, j:j+3] * filt)
            feature_maps.append(feature_map)
        
        # แสดง feature maps
        combined_features = np.hstack(feature_maps)
        im4 = ax4.imshow(combined_features, cmap='viridis', interpolation='nearest')
        ax4.set_title('Multiple Feature Maps: คุณสมบัติต่างๆ')
        ax4.set_xlabel('Vertical Edges | Horizontal Edges | Center Detection')
        plt.colorbar(im4, ax=ax4, shrink=0.6)
        
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
        print("=== การสาธิต Neural Networks และ Deep Learning ===")
        print("ใช้ปุ่ม 'ถัดไป' และ 'ก่อนหน้า' เพื่อดูการสาธิตต่างๆ")
        print("\nการสาธิตที่มี:")
        for i, name in enumerate(self.demo_names, 1):
            print(f"{i}. {name}")
        
        self.show_current_demo()
        plt.show()

# Deep Learning Applications Simulator
class DeepLearningApplications:
    def __init__(self):
        self.fig, self.axes = plt.subplots(2, 2, figsize=(15, 12))
        self.fig.suptitle('การประยุกต์ใช้ Deep Learning ในการเกษตร', fontsize=16, fontweight='bold')
        
    def plant_disease_classification(self):
        """จำลองการจำแนกโรคพืช"""
        ax = self.axes[0, 0]
        
        # สร้างข้อมูลตัวอย่าง
        np.random.seed(42)
        
        # สร้าง confusion matrix
        classes = ['สุขภาพดี', 'โรค A', 'โรค B']
        confusion_matrix = np.array([
            [95, 3, 2],    # สุขภาพดี
            [5, 88, 7],    # โรค A  
            [2, 8, 90]     # โรค B
        ])
        
        # แสดง confusion matrix
        im = ax.imshow(confusion_matrix, cmap='Blues', interpolation='nearest')
        
        # เพิ่มข้อความในแต่ละช่อง
        for i in range(len(classes)):
            for j in range(len(classes)):
                text = ax.text(j, i, f'{confusion_matrix[i, j]}%',
                             ha="center", va="center", color="white" if confusion_matrix[i, j] > 50 else "black",
                             fontsize=12, fontweight='bold')
        
        ax.set_xticks(range(len(classes)))
        ax.set_yticks(range(len(classes)))
        ax.set_xticklabels(classes)
        ax.set_yticklabels(classes)
        ax.set_xlabel('ผลการทำนาย')
        ax.set_ylabel('ความจริง')
        ax.set_title('CNN: การจำแนกโรคพืช\n(ความแม่นยำ: 91%)')
        
        # คำนวณ accuracy
        accuracy = np.trace(confusion_matrix) / np.sum(confusion_matrix)
        ax.text(0.02, 0.98, f'Accuracy: {accuracy:.1%}', transform=ax.transAxes,
               fontsize=10, fontweight='bold', verticalalignment='top',
               bbox=dict(boxstyle="round,pad=0.3", facecolor='yellow', alpha=0.7))
        
    def yield_prediction_lstm(self):
        """จำลองการทำนายผลผลิตด้วย LSTM"""
        ax = self.axes[0, 1]
        
        # สร้างข้อมูลอนุกรมเวลา
        days = np.arange(1, 101)
        
        # ข้อมูลจริง (มีแนวโน้มและความผันผวน)
        trend = 0.5 * days
        seasonal = 50 * np.sin(days * 0.1)
        noise = np.random.normal(0, 10, 100)
        actual_yield = 500 + trend + seasonal + noise
        
        # การทำนายด้วย LSTM (ค่อนข้างแม่นยำ)
        lstm_prediction = actual_yield + np.random.normal(0, 15, 100)
        
        # การทำนายแบบเดิม (Linear regression)
        linear_prediction = 500 + 0.5 * days + np.random.normal(0, 25, 100)
        
        # แสดงผล
        ax.plot(days, actual_yield, 'g-', linewidth=2, label='ผลผลิตจริง', alpha=0.8)
        ax.plot(days, lstm_prediction, 'b--', linewidth=2, label='LSTM Prediction')
        ax.plot(days, linear_prediction, 'r:', linewidth=2, label='Linear Prediction')
        
        ax.fill_between(days, actual_yield, lstm_prediction, alpha=0.2, color='blue')
        ax.fill_between(days, actual_yield, linear_prediction, alpha=0.2, color='red')
        
        ax.set_xlabel('วัน')
        ax.set_ylabel('ผลผลิต (กก./ไร่)')
        ax.set_title('LSTM: การทำนายผลผลิต')
        ax.legend()
        ax.grid(True, alpha=0.3)
        
        # คำนวณ RMSE
        lstm_rmse = np.sqrt(np.mean((actual_yield - lstm_prediction)**2))
        linear_rmse = np.sqrt(np.mean((actual_yield - linear_prediction)**2))
        
        ax.text(0.02, 0.98, f'LSTM RMSE: {lstm_rmse:.1f}\nLinear RMSE: {linear_rmse:.1f}', 
               transform=ax.transAxes, fontsize=10, fontweight='bold', verticalalignment='top',
               bbox=dict(boxstyle="round,pad=0.3", facecolor='lightblue', alpha=0.7))
        
    def satellite_image_analysis(self):
        """จำลองการวิเคราะห์ภาพดาวเทียม"""
        ax = self.axes[1, 0]
        
        # สร้างภาพดาวเทียมจำลอง
        np.random.seed(42)
        
        # สร้างพื้นที่ต่างๆ
        image = np.zeros((50, 50, 3))
        
        # พื้นที่เกษตร (สีเขียว)
        for i in range(10, 30):
            for j in range(10, 40):
                if np.random.random() > 0.3:
                    image[i, j] = [0.2, 0.8, 0.3]
        
        # พื้นที่น้ำ (สีน้ำเงิน)
        for i in range(35, 45):
            for j in range(5, 25):
                image[i, j] = [0.1, 0.3, 0.9]
        
        # พื้นที่เมือง (สีเทา)
        for i in range(5, 15):
            for j in range(35, 45):
                image[i, j] = [0.6, 0.6, 0.6]
        
        # เพิ่ม noise
        noise = np.random.normal(0, 0.05, image.shape)
        image = np.clip(image + noise, 0, 1)
        
        ax.imshow(image)
        ax.set_title('CNN: การวิเคราะห์ภาพดาวเทียม')
        
        # เพิ่ม legend
        from matplotlib.patches import Patch
        legend_elements = [
            Patch(facecolor='green', alpha=0.7, label='พื้นที่เกษตร'),
            Patch(facecolor='blue', alpha=0.7, label='แหล่งน้ำ'),
            Patch(facecolor='gray', alpha=0.7, label='พื้นที่เมือง'),
            Patch(facecolor='brown', alpha=0.7, label='ที่ดินเปล่า')
        ]
        ax.legend(handles=legend_elements, loc='upper right', fontsize=8)
        
        # แสดงสถิติ
        stats_text = """การจำแนกพื้นที่:
• เกษตร: 45%
• น้ำ: 20%  
• เมือง: 15%
• อื่นๆ: 20%"""
        
        ax.text(0.02, 0.02, stats_text, transform=ax.transAxes, fontsize=8,
               verticalalignment='bottom',
               bbox=dict(boxstyle="round,pad=0.3", facecolor='white', alpha=0.8))
        
    def automated_irrigation_control(self):
        """จำลองระบบชลประทานอัตโนมัติ"""
        ax = self.axes[1, 1]
        
        # สร้างข้อมูลการควบคุมน้ำ
        hours = np.arange(0, 24, 0.5)
        
        # ข้อมูลสภาพแวดล้อม
        temperature = 25 + 10 * np.sin((hours - 6) * np.pi / 12) + np.random.normal(0, 1, len(hours))
        soil_moisture = 60 - 0.5 * temperature + np.random.normal(0, 2, len(hours))
        
        # การตัดสินใจของ AI
        irrigation_decision = np.zeros(len(hours))
        for i, (temp, moisture) in enumerate(zip(temperature, soil_moisture)):
            if moisture < 40 and temp > 30:
                irrigation_decision[i] = 3  # รดน้ำมาก
            elif moisture < 50 and temp > 25:
                irrigation_decision[i] = 2  # รดน้ำปานกลาง
            elif moisture < 60:
                irrigation_decision[i] = 1  # รดน้ำเล็กน้อย
            else:
                irrigation_decision[i] = 0  # ไม่รดน้ำ
        
        # แสดงผล
        ax2 = ax.twinx()
        
        # Temperature และ Soil Moisture
        line1 = ax.plot(hours, temperature, 'r-', linewidth=2, label='อุณหภูมิ (°C)')
        line2 = ax.plot(hours, soil_moisture, 'b-', linewidth=2, label='ความชื้นดิน (%)')
        
        # Irrigation decision
        colors = ['white', 'lightblue', 'blue', 'darkblue']
        for i in range(len(hours)-1):
            color = colors[int(irrigation_decision[i])]
            ax2.fill_between([hours[i], hours[i+1]], 0, 1, color=color, alpha=0.6)
        
        ax.set_xlabel('เวลา (ชั่วโมง)')
        ax.set_ylabel('อุณหภูมิ (°C) / ความชื้น (%)')
        ax2.set_ylabel('การรดน้ำ')
        ax.set_title('AI: ระบบชลประทานอัตโนมัติ')
        
        # Legend
        irrigation_labels = ['ไม่รดน้ำ', 'รดน้ำเล็กน้อย', 'รดน้ำปานกลาง', 'รดน้ำมาก']
        legend_elements = [Patch(facecolor=colors[i], alpha=0.6, label=irrigation_labels[i]) 
                          for i in range(4)]
        
        lines = line1 + line2
        labels = [l.get_label() for l in lines]
        ax.legend(lines + legend_elements[:2], labels + irrigation_labels[:2], loc='upper left', fontsize=8)
        ax2.legend(legend_elements[2:], irrigation_labels[2:], loc='upper right', fontsize=8)
        
        ax.grid(True, alpha=0.3)
        
    def show(self):
        """แสดงการจำลองทั้งหมด"""
        self.plant_disease_classification()
        self.yield_prediction_lstm()
        self.satellite_image_analysis()
        self.automated_irrigation_control()
        
        plt.tight_layout()
        plt.show()

if __name__ == "__main__":
    print("=== การสาธิต Deep Learning และ Neural Networks ===")
    print("\n1. การสาธิต Neural Network พื้นฐาน")
    print("2. การประยุกต์ใช้ Deep Learning ในการเกษตร")
    
    choice = input("\nเลือกการสาธิต (1 หรือ 2): ")
    
    if choice == "1":
        demo = NeuralNetworkVisualizer()
        demo.start()
    elif choice == "2":
        print("\nกำลังสร้างการจำลองการประยุกต์ใช้ Deep Learning...")
        simulator = DeepLearningApplications()
        simulator.show()
    else:
        print("ตัวเลือกไม่ถูกต้อง กำลังแสดงการสาธิต Neural Network พื้นฐาน...")
        demo = NeuralNetworkVisualizer()
        demo.start()

