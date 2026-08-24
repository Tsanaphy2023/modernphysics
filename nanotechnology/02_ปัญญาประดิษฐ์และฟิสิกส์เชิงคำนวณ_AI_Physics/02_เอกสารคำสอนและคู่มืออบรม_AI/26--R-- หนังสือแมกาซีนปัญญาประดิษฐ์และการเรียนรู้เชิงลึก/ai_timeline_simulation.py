import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.widgets import Button
import numpy as np

class AITimelineSimulation:
    def __init__(self):
        self.fig, self.ax = plt.subplots(figsize=(15, 10))
        self.fig.suptitle('ไทม์ไลน์ประวัติศาสตร์ปัญญาประดิษฐ์', fontsize=16, fontweight='bold')
        
        # Timeline data
        self.events = [
            {'year': 1943, 'event': 'McCulloch-Pitts Neuron', 'description': 'แบบจำลองโครงข่ายประสาทเทียมแรก', 'color': '#FF6B6B'},
            {'year': 1950, 'event': 'Turing Test', 'description': 'Alan Turing เสนอการทดสอบความฉลาดของเครื่อง', 'color': '#4ECDC4'},
            {'year': 1956, 'event': 'Dartmouth Conference', 'description': 'จุดเริ่มต้นของ AI เป็นสาขาวิชา', 'color': '#45B7D1'},
            {'year': 1957, 'event': 'Perceptron', 'description': 'Frank Rosenblatt สร้างโครงข่ายประสาทเทียมแรก', 'color': '#96CEB4'},
            {'year': 1970, 'event': 'AI Winter 1', 'description': 'ยุคฤดูหนาวของ AI ครั้งแรก', 'color': '#FFEAA7'},
            {'year': 1980, 'event': 'Expert Systems', 'description': 'ระบบผู้เชี่ยวชาญได้รับความนิยม', 'color': '#DDA0DD'},
            {'year': 1986, 'event': 'Backpropagation', 'description': 'อัลกอริทึมการเรียนรู้ที่สำคัญ', 'color': '#98D8C8'},
            {'year': 1997, 'event': 'Deep Blue vs Kasparov', 'description': 'คอมพิวเตอร์ชนะแชมป์หมากรุกโลก', 'color': '#F7DC6F'},
            {'year': 2011, 'event': 'IBM Watson', 'description': 'Watson ชนะในเกมโชว์ Jeopardy!', 'color': '#BB8FCE'},
            {'year': 2016, 'event': 'AlphaGo', 'description': 'AI ชนะแชมป์หมากล้อมโลก', 'color': '#85C1E9'},
            {'year': 2022, 'event': 'ChatGPT', 'description': 'AI สนทนาที่เปลี่ยนโลก', 'color': '#F8C471'}
        ]
        
        self.current_event = 0
        self.setup_timeline()
        self.setup_buttons()
        
    def setup_timeline(self):
        self.ax.clear()
        self.ax.set_xlim(1940, 2030)
        self.ax.set_ylim(-2, 3)
        
        # Draw timeline line
        self.ax.plot([1940, 2030], [0, 0], 'k-', linewidth=3, alpha=0.3)
        
        # Draw all events
        for i, event in enumerate(self.events):
            x = event['year']
            y = 0.5 if i % 2 == 0 else -0.5
            
            # Event marker
            if i <= self.current_event:
                alpha = 1.0
                marker_size = 150 if i == self.current_event else 100
            else:
                alpha = 0.3
                marker_size = 50
                
            self.ax.scatter(x, 0, s=marker_size, c=event['color'], alpha=alpha, zorder=3)
            
            # Event label
            if i <= self.current_event:
                self.ax.annotate(f"{event['year']}\n{event['event']}", 
                               xy=(x, 0), xytext=(x, y),
                               ha='center', va='center' if y > 0 else 'center',
                               fontsize=8 if i != self.current_event else 10,
                               fontweight='bold' if i == self.current_event else 'normal',
                               bbox=dict(boxstyle="round,pad=0.3", facecolor=event['color'], alpha=0.7),
                               arrowprops=dict(arrowstyle='->', color='black', alpha=0.5))
        
        # Show current event description
        if self.current_event < len(self.events):
            current = self.events[self.current_event]
            self.ax.text(0.02, 0.98, f"เหตุการณ์ปัจจุบัน: {current['event']} ({current['year']})\n{current['description']}", 
                        transform=self.ax.transAxes, fontsize=12, fontweight='bold',
                        verticalalignment='top',
                        bbox=dict(boxstyle="round,pad=0.5", facecolor='lightblue', alpha=0.8))
        
        self.ax.set_xlabel('ปี (ค.ศ.)', fontsize=12)
        self.ax.set_title('การพัฒนาปัญญาประดิษฐ์ตลอดประวัติศาสตร์', fontsize=14)
        self.ax.grid(True, alpha=0.3)
        self.ax.set_yticks([])
        
    def setup_buttons(self):
        # Previous button
        ax_prev = plt.axes([0.1, 0.02, 0.1, 0.05])
        self.btn_prev = Button(ax_prev, 'ก่อนหน้า')
        self.btn_prev.on_clicked(self.prev_event)
        
        # Next button
        ax_next = plt.axes([0.8, 0.02, 0.1, 0.05])
        self.btn_next = Button(ax_next, 'ถัดไป')
        self.btn_next.on_clicked(self.next_event)
        
        # Reset button
        ax_reset = plt.axes([0.45, 0.02, 0.1, 0.05])
        self.btn_reset = Button(ax_reset, 'รีเซ็ต')
        self.btn_reset.on_clicked(self.reset_timeline)
        
    def prev_event(self, event):
        if self.current_event > 0:
            self.current_event -= 1
            self.setup_timeline()
            plt.draw()
            
    def next_event(self, event):
        if self.current_event < len(self.events) - 1:
            self.current_event += 1
            self.setup_timeline()
            plt.draw()
            
    def reset_timeline(self, event):
        self.current_event = 0
        self.setup_timeline()
        plt.draw()
        
    def show(self):
        plt.tight_layout()
        plt.show()

# AI Impact Visualization
class AIImpactVisualization:
    def __init__(self):
        self.fig, ((self.ax1, self.ax2), (self.ax3, self.ax4)) = plt.subplots(2, 2, figsize=(15, 12))
        self.fig.suptitle('ผลกระทบของ AI ในด้านต่างๆ', fontsize=16, fontweight='bold')
        
    def create_visualizations(self):
        # 1. AI Applications by Industry
        industries = ['การเกษตร', 'การแพทย์', 'การเงิน', 'การขนส่ง', 'การศึกษา', 'บันเทิง']
        adoption_rates = [65, 78, 85, 72, 58, 90]
        colors = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#96CEB4', '#FFEAA7', '#DDA0DD']
        
        bars = self.ax1.bar(industries, adoption_rates, color=colors, alpha=0.8)
        self.ax1.set_title('อัตราการใช้ AI ในอุตสาหกรรมต่างๆ (%)', fontweight='bold')
        self.ax1.set_ylabel('เปอร์เซ็นต์การใช้งาน')
        self.ax1.set_ylim(0, 100)
        
        # Add value labels on bars
        for bar, rate in zip(bars, adoption_rates):
            self.ax1.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 1, 
                         f'{rate}%', ha='center', va='bottom', fontweight='bold')
        
        plt.setp(self.ax1.get_xticklabels(), rotation=45, ha='right')
        
        # 2. AI Job Market Growth
        years = np.array([2020, 2021, 2022, 2023, 2024, 2025])
        ai_jobs = np.array([100, 125, 160, 200, 250, 315])  # Index: 2020 = 100
        
        self.ax2.plot(years, ai_jobs, marker='o', linewidth=3, markersize=8, color='#FF6B6B')
        self.ax2.fill_between(years, ai_jobs, alpha=0.3, color='#FF6B6B')
        self.ax2.set_title('การเติบโตของตลาดงาน AI', fontweight='bold')
        self.ax2.set_xlabel('ปี')
        self.ax2.set_ylabel('ดัชนีการเติบโต (2020 = 100)')
        self.ax2.grid(True, alpha=0.3)
        
        # Add annotations
        for year, jobs in zip(years, ai_jobs):
            self.ax2.annotate(f'{jobs}', xy=(year, jobs), xytext=(5, 5), 
                            textcoords='offset points', fontweight='bold')
        
        # 3. AI Skills Demand
        skills = ['Python', 'Machine Learning', 'Deep Learning', 'Data Analysis', 'Statistics', 'Computer Vision']
        demand_scores = [95, 88, 82, 90, 75, 70]
        
        y_pos = np.arange(len(skills))
        bars = self.ax3.barh(y_pos, demand_scores, color='#4ECDC4', alpha=0.8)
        self.ax3.set_yticks(y_pos)
        self.ax3.set_yticklabels(skills)
        self.ax3.set_xlabel('คะแนนความต้องการ (0-100)')
        self.ax3.set_title('ทักษะ AI ที่ต้องการในตลาดงาน', fontweight='bold')
        
        # Add value labels
        for i, (bar, score) in enumerate(zip(bars, demand_scores)):
            self.ax3.text(score + 1, i, f'{score}', va='center', fontweight='bold')
        
        # 4. AI in Agriculture Benefits
        categories = ['ประหยัดน้ำ', 'เพิ่มผลผลิต', 'ลดต้นทุน', 'ตรวจจับโรค', 'คาดการณ์สภาพอากาศ']
        benefits = [30, 25, 35, 40, 20]  # Percentage improvement
        
        wedges, texts, autotexts = self.ax4.pie(benefits, labels=categories, autopct='%1.1f%%',
                                               colors=['#96CEB4', '#FFEAA7', '#DDA0DD', '#F7DC6F', '#BB8FCE'],
                                               startangle=90)
        self.ax4.set_title('ประโยชน์ของ AI ในการเกษตร', fontweight='bold')
        
        # Make percentage text bold
        for autotext in autotexts:
            autotext.set_fontweight('bold')
            autotext.set_color('white')
    
    def show(self):
        self.create_visualizations()
        plt.tight_layout()
        plt.show()

# Simple AI Concept Demonstrator
class AIConceptDemo:
    def __init__(self):
        self.fig, self.ax = plt.subplots(figsize=(12, 8))
        self.fig.suptitle('การสาธิตแนวคิด AI พื้นฐาน', fontsize=16, fontweight='bold')
        
    def demonstrate_pattern_recognition(self):
        """Demonstrate simple pattern recognition concept"""
        self.ax.clear()
        
        # Generate sample data
        np.random.seed(42)
        
        # Class 1: Healthy plants (green)
        healthy_x = np.random.normal(3, 0.8, 50)
        healthy_y = np.random.normal(7, 0.8, 50)
        
        # Class 2: Diseased plants (red)
        diseased_x = np.random.normal(7, 0.8, 50)
        diseased_y = np.random.normal(3, 0.8, 50)
        
        # Plot the data
        self.ax.scatter(healthy_x, healthy_y, c='green', alpha=0.6, s=60, label='พืชสุขภาพดี')
        self.ax.scatter(diseased_x, diseased_y, c='red', alpha=0.6, s=60, label='พืชป่วย')
        
        # Draw decision boundary (simple linear)
        x_line = np.linspace(0, 10, 100)
        y_line = 10 - x_line
        self.ax.plot(x_line, y_line, 'k--', linewidth=2, label='เส้นแบ่งการตัดสินใจ')
        
        # Add new sample to classify
        new_sample_x, new_sample_y = 5, 6
        self.ax.scatter(new_sample_x, new_sample_y, c='blue', s=200, marker='*', 
                       label='ตัวอย่างใหม่', edgecolors='black', linewidth=2)
        
        self.ax.set_xlabel('ความเข้มของสีเขียว (Green Intensity)')
        self.ax.set_ylabel('ขนาดใบ (Leaf Size)')
        self.ax.set_title('การจำแนกพืชสุขภาพดี vs พืชป่วย ด้วย AI')
        self.ax.legend()
        self.ax.grid(True, alpha=0.3)
        self.ax.set_xlim(0, 10)
        self.ax.set_ylim(0, 10)
        
        # Add explanation text
        explanation = """
        AI เรียนรู้จากข้อมูลตัวอย่าง:
        • จุดสีเขียว = พืชสุขภาพดี
        • จุดสีแดง = พืชป่วย
        • เส้นประ = เส้นแบ่งการตัดสินใจ
        • ดาวสีน้ำเงิน = ตัวอย่างใหม่ที่ต้องจำแนก
        
        AI จะตัดสินใจว่าตัวอย่างใหม่เป็นพืชสุขภาพดี
        เพราะอยู่ในพื้นที่สีเขียว
        """
        
        self.ax.text(0.02, 0.98, explanation, transform=self.ax.transAxes, 
                    fontsize=10, verticalalignment='top',
                    bbox=dict(boxstyle="round,pad=0.5", facecolor='lightblue', alpha=0.8))
    
    def show(self):
        self.demonstrate_pattern_recognition()
        plt.tight_layout()
        plt.show()

if __name__ == "__main__":
    print("=== การจำลองประวัติศาสตร์ AI ===")
    print("กำลังสร้างไทม์ไลน์แบบโต้ตอบ...")
    
    # Create and show timeline
    timeline = AITimelineSimulation()
    timeline.show()
    
    print("\n=== การแสดงผลกระทบของ AI ===")
    print("กำลังสร้างกราฟแสดงผลกระทบ...")
    
    # Create and show impact visualization
    impact_viz = AIImpactVisualization()
    impact_viz.show()
    
    print("\n=== การสาธิตแนวคิด AI ===")
    print("กำลังสาธิตการจำแนกรูปแบบ...")
    
    # Create and show concept demo
    concept_demo = AIConceptDemo()
    concept_demo.show()
    
    print("\nการจำลองเสร็จสมบูรณ์!")
    print("นักเรียนสามารถใช้การจำลองเหล่านี้เพื่อเข้าใจแนวคิด AI ได้ดีขึ้น")

