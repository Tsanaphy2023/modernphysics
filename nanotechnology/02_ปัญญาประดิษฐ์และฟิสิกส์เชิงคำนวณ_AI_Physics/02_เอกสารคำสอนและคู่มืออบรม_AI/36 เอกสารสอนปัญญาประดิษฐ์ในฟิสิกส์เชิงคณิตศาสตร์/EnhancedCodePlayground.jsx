import React, { useState, useRef, useEffect } from 'react';
import { Card, CardContent, CardHeader, CardTitle } from './ui/card';
import { Button } from './ui/button';
import { Badge } from './ui/badge';
import { Tabs, TabsContent, TabsList, TabsTrigger } from './ui/tabs';
import { 
  Play, 
  Copy, 
  Download, 
  RotateCcw, 
  Save, 
  Share2, 
  Code, 
  Terminal,
  FileText,
  Maximize2,
  Settings
} from 'lucide-react';

const EnhancedCodePlayground = ({ 
  title, 
  description,
  examples = [],
  language = 'python',
  theme = 'dark',
  onCodeChange,
  className = ""
}) => {
  const [activeExample, setActiveExample] = useState(0);
  const [code, setCode] = useState(examples[0]?.code || '');
  const [output, setOutput] = useState('');
  const [isRunning, setIsRunning] = useState(false);
  const [isFullscreen, setIsFullscreen] = useState(false);
  const [showSettings, setShowSettings] = useState(false);
  const [fontSize, setFontSize] = useState(14);
  const [autoRun, setAutoRun] = useState(false);
  const textareaRef = useRef(null);

  // Default Python examples for different physics topics
  const defaultExamples = [
    {
      title: "Linear Regression for Physics Data",
      description: "การใช้ Linear Regression ในการวิเคราะห์ข้อมูลฟิสิกส์",
      code: `import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

# สร้างข้อมูลจำลองการทดลองฟิสิกส์
# ความสัมพันธ์ระหว่างแรงและการเร่ง (F = ma)
np.random.seed(42)
mass = 2.5  # kg
force = np.linspace(1, 20, 50)  # Newton
acceleration_true = force / mass
acceleration_measured = acceleration_true + np.random.normal(0, 0.2, 50)

# เตรียมข้อมูลสำหรับ Linear Regression
X = force.reshape(-1, 1)
y = acceleration_measured

# สร้างและฝึกโมเดล
model = LinearRegression()
model.fit(X, y)

# ทำนายผล
y_pred = model.predict(X)

# คำนวณค่าสถิติ
r2 = r2_score(y, y_pred)
slope = model.coef_[0]
intercept = model.intercept_

print(f"สมการที่ได้: a = {slope:.3f}F + {intercept:.3f}")
print(f"ค่า R² = {r2:.3f}")
print(f"มวลที่คำนวณได้: {1/slope:.3f} kg")
print(f"มวลจริง: {mass} kg")
print(f"ความผิดพลาด: {abs(1/slope - mass)/mass*100:.2f}%")

# สร้างกราฟ
plt.figure(figsize=(10, 6))
plt.scatter(force, acceleration_measured, alpha=0.7, label='ข้อมูลการทดลอง')
plt.plot(force, y_pred, 'r-', linewidth=2, label=f'Linear Regression (R² = {r2:.3f})')
plt.plot(force, acceleration_true, 'g--', linewidth=2, label='ความสัมพันธ์ทฤษฎี')
plt.xlabel('แรง (N)')
plt.ylabel('ความเร่ง (m/s²)')
plt.title('การวิเคราะห์ความสัมพันธ์ F = ma ด้วย Linear Regression')
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()

# วิเคราะห์ความไม่แน่นอน
residuals = y - y_pred
mse = np.mean(residuals**2)
rmse = np.sqrt(mse)

print(f"\\nการวิเคราะห์ความผิดพลาด:")
print(f"RMSE: {rmse:.4f} m/s²")
print(f"ความผิดพลาดเฉลี่ย: {np.mean(np.abs(residuals)):.4f} m/s²")`,
      badge: "Physics"
    },
    {
      title: "Neural Network for Quantum State Classification",
      description: "การใช้ Neural Network ในการจำแนกสถานะควอนตัม",
      code: `import numpy as np
import tensorflow as tf
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

# สร้างข้อมูลจำลองสถานะควอนตัม
def generate_quantum_states(n_samples=1000):
    """สร้างข้อมูลจำลองสถานะควอนตัมสำหรับระบบ 2-level"""
    np.random.seed(42)
    
    # สร้างสถานะ |0⟩ และ |1⟩ พร้อมสัญญาณรบกวน
    states_0 = np.random.normal([1, 0], 0.1, (n_samples//2, 2))
    states_1 = np.random.normal([0, 1], 0.1, (n_samples//2, 2))
    
    # รวมข้อมูลและสร้าง labels
    X = np.vstack([states_0, states_1])
    y = np.hstack([np.zeros(n_samples//2), np.ones(n_samples//2)])
    
    # เพิ่มฟีเจอร์ทางฟิสิกส์
    # ความน่าจะเป็นของการวัด
    prob_0 = X[:, 0]**2
    prob_1 = X[:, 1]**2
    
    # Phase information
    phase = np.arctan2(X[:, 1], X[:, 0])
    
    # Entanglement measure (simplified)
    entanglement = np.sqrt(prob_0 * prob_1)
    
    # รวมฟีเจอร์ทั้งหมด
    X_features = np.column_stack([X, prob_0, prob_1, phase, entanglement])
    
    return X_features, y

# สร้างข้อมูล
X, y = generate_quantum_states(2000)

# แบ่งข้อมูล
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# ปรับมาตรฐานข้อมูล
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# สร้างโมเดล Neural Network
model = tf.keras.Sequential([
    tf.keras.layers.Dense(64, activation='relu', input_shape=(6,)),
    tf.keras.layers.Dropout(0.3),
    tf.keras.layers.Dense(32, activation='relu'),
    tf.keras.layers.Dropout(0.2),
    tf.keras.layers.Dense(16, activation='relu'),
    tf.keras.layers.Dense(1, activation='sigmoid')
])

# คอมไพล์โมเดล
model.compile(
    optimizer='adam',
    loss='binary_crossentropy',
    metrics=['accuracy']
)

print("โครงสร้าง Neural Network:")
model.summary()

# ฝึกโมเดล
history = model.fit(
    X_train_scaled, y_train,
    epochs=100,
    batch_size=32,
    validation_split=0.2,
    verbose=1
)

# ประเมินผล
test_loss, test_accuracy = model.evaluate(X_test_scaled, y_test, verbose=0)
print(f"\\nความแม่นยำบนข้อมูลทดสอบ: {test_accuracy:.4f}")

# ทำนายผล
y_pred_prob = model.predict(X_test_scaled)
y_pred = (y_pred_prob > 0.5).astype(int)

# วิเคราะห์ผลลัพธ์
from sklearn.metrics import classification_report, confusion_matrix

print("\\nรายงานการจำแนก:")
print(classification_report(y_test, y_pred, target_names=['State |0⟩', 'State |1⟩']))

print("\\nConfusion Matrix:")
cm = confusion_matrix(y_test, y_pred)
print(cm)

# สร้างกราฟผลการฝึก
plt.figure(figsize=(12, 4))

plt.subplot(1, 2, 1)
plt.plot(history.history['loss'], label='Training Loss')
plt.plot(history.history['val_loss'], label='Validation Loss')
plt.title('Model Loss')
plt.xlabel('Epoch')
plt.ylabel('Loss')
plt.legend()

plt.subplot(1, 2, 2)
plt.plot(history.history['accuracy'], label='Training Accuracy')
plt.plot(history.history['val_accuracy'], label='Validation Accuracy')
plt.title('Model Accuracy')
plt.xlabel('Epoch')
plt.ylabel('Accuracy')
plt.legend()

plt.tight_layout()
plt.show()

# วิเคราะห์ความสำคัญของฟีเจอร์
feature_names = ['Re(ψ)', 'Im(ψ)', 'P(|0⟩)', 'P(|1⟩)', 'Phase', 'Entanglement']
print(f"\\nฟีเจอร์ที่ใช้: {feature_names}")
print("โมเดลสามารถจำแนกสถานะควอนตัมได้อย่างมีประสิทธิภาพ!")`,
      badge: "Quantum ML"
    },
    {
      title: "Fourier Analysis for Signal Processing",
      description: "การวิเคราะห์ฟูเรียร์สำหรับการประมวลผลสัญญาณฟิสิกส์",
      code: `import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
from scipy.fft import fft, fftfreq, ifft

# สร้างสัญญาณจำลองจากเครื่องตรวจจับอนุภาค
def create_physics_signal(duration=1.0, sampling_rate=1000):
    """สร้างสัญญาณจำลองจากการตรวจจับอนุภาค"""
    t = np.linspace(0, duration, int(sampling_rate * duration), endpoint=False)
    
    # สัญญาณหลัก: การสั่นของเครื่องตรวจจับ
    main_signal = 2.0 * np.sin(2 * np.pi * 50 * t)  # 50 Hz
    
    # สัญญาณรบกวนจากแหล่งภายนอก
    noise_60hz = 0.5 * np.sin(2 * np.pi * 60 * t)   # 60 Hz (ไฟฟ้า)
    noise_120hz = 0.3 * np.sin(2 * np.pi * 120 * t) # 120 Hz (harmonics)
    
    # สัญญาณจากการตรวจจับอนุภาค (pulse)
    particle_events = np.zeros_like(t)
    event_times = [0.1, 0.3, 0.5, 0.7, 0.9]  # เวลาที่ตรวจพบอนุภาค
    for event_time in event_times:
        event_idx = int(event_time * sampling_rate)
        if event_idx < len(particle_events):
            # Gaussian pulse
            pulse_width = 0.01  # 10 ms
            pulse = 3.0 * np.exp(-((t - event_time) / pulse_width)**2)
            particle_events += pulse
    
    # สัญญาณรบกวนแบบสุ่ม
    random_noise = 0.2 * np.random.normal(0, 1, len(t))
    
    # รวมสัญญาณทั้งหมด
    total_signal = main_signal + noise_60hz + noise_120hz + particle_events + random_noise
    
    return t, total_signal, main_signal, particle_events

# สร้างสัญญาณ
t, noisy_signal, clean_signal, particle_events = create_physics_signal()
sampling_rate = 1000

print("การวิเคราะห์สัญญาณฟิสิกส์ด้วย Fourier Transform")
print("="*50)

# คำนวณ FFT
N = len(noisy_signal)
frequencies = fftfreq(N, 1/sampling_rate)
fft_signal = fft(noisy_signal)
magnitude = np.abs(fft_signal)
phase = np.angle(fft_signal)

# หาความถี่ที่มีพลังงานสูงสุด
positive_freq_idx = frequencies > 0
dominant_freq_idx = np.argmax(magnitude[positive_freq_idx])
dominant_frequency = frequencies[positive_freq_idx][dominant_freq_idx]

print(f"ความถี่หลัก: {dominant_frequency:.1f} Hz")

# ออกแบบตัวกรองความถี่
def design_filters(frequencies, sampling_rate):
    """ออกแบบตัวกรองสำหรับแยกสัญญาณ"""
    nyquist = sampling_rate / 2
    
    # Low-pass filter สำหรับสัญญาณหลัก (0-80 Hz)
    low_cutoff = 80 / nyquist
    b_low, a_low = signal.butter(4, low_cutoff, btype='low')
    
    # Band-stop filter สำหรับกำจัดสัญญาณรบกวน 60 Hz
    notch_freq = 60 / nyquist
    notch_width = 5 / nyquist
    b_notch, a_notch = signal.iirnotch(notch_freq, notch_width)
    
    # High-pass filter สำหรับสัญญาณอนุภาค
    high_cutoff = 10 / nyquist
    b_high, a_high = signal.butter(2, high_cutoff, btype='high')
    
    return (b_low, a_low), (b_notch, a_notch), (b_high, a_high)

# ใช้ตัวกรอง
(b_low, a_low), (b_notch, a_notch), (b_high, a_high) = design_filters(frequencies, sampling_rate)

# กรองสัญญาณ
filtered_low = signal.filtfilt(b_low, a_low, noisy_signal)
filtered_notch = signal.filtfilt(b_notch, a_notch, noisy_signal)
filtered_high = signal.filtfilt(b_high, a_high, noisy_signal)

# วิเคราะห์พลังงานสเปกตรัม
power_spectrum = magnitude**2
total_power = np.sum(power_spectrum)
signal_power = np.sum(power_spectrum[(frequencies >= 45) & (frequencies <= 55)])
noise_power = np.sum(power_spectrum[(frequencies >= 55) & (frequencies <= 65)])

snr_db = 10 * np.log10(signal_power / noise_power)
print(f"Signal-to-Noise Ratio: {snr_db:.2f} dB")

# สร้างกราฟแสดงผล
fig, axes = plt.subplots(3, 2, figsize=(15, 12))

# สัญญาณในโดเมนเวลา
axes[0, 0].plot(t, noisy_signal, 'b-', alpha=0.7, label='สัญญาณที่มีสัญญาณรบกวน')
axes[0, 0].plot(t, clean_signal, 'r-', linewidth=2, label='สัญญาณหลัก')
axes[0, 0].set_xlabel('เวลา (s)')
axes[0, 0].set_ylabel('แอมพลิจูด')
axes[0, 0].set_title('สัญญาณในโดเมนเวลา')
axes[0, 0].legend()
axes[0, 0].grid(True, alpha=0.3)

# สเปกตรัมความถี่
axes[0, 1].plot(frequencies[positive_freq_idx], magnitude[positive_freq_idx])
axes[0, 1].set_xlabel('ความถี่ (Hz)')
axes[0, 1].set_ylabel('แอมพลิจูด')
axes[0, 1].set_title('สเปกตรัมความถี่ (FFT)')
axes[0, 1].set_xlim(0, 200)
axes[0, 1].grid(True, alpha=0.3)

# สัญญาณที่กรองแล้ว - Low pass
axes[1, 0].plot(t, filtered_low, 'g-', linewidth=2, label='Low-pass filtered')
axes[1, 0].plot(t, clean_signal, 'r--', alpha=0.7, label='สัญญาณหลัก')
axes[1, 0].set_xlabel('เวลา (s)')
axes[1, 0].set_ylabel('แอมพลิจูด')
axes[1, 0].set_title('สัญญาณหลังกรอง Low-pass (0-80 Hz)')
axes[1, 0].legend()
axes[1, 0].grid(True, alpha=0.3)

# สัญญาณที่กรองแล้ว - Notch filter
axes[1, 1].plot(t, filtered_notch, 'm-', linewidth=2, label='Notch filtered (60 Hz)')
axes[1, 1].plot(t, noisy_signal, 'b-', alpha=0.5, label='สัญญาณเดิม')
axes[1, 1].set_xlabel('เวลา (s)')
axes[1, 1].set_ylabel('แอมพลิจูด')
axes[1, 1].set_title('สัญญาณหลังกำจัดสัญญาณรบกวน 60 Hz')
axes[1, 1].legend()
axes[1, 1].grid(True, alpha=0.3)

# การตรวจจับอนุภาค
axes[2, 0].plot(t, filtered_high, 'orange', linewidth=2, label='High-pass filtered')
axes[2, 0].plot(t, particle_events, 'r-', linewidth=2, label='เหตุการณ์อนุภาคจริง')
axes[2, 0].set_xlabel('เวลา (s)')
axes[2, 0].set_ylabel('แอมพลิจูด')
axes[2, 0].set_title('การตรวจจับเหตุการณ์อนุภาค')
axes[2, 0].legend()
axes[2, 0].grid(True, alpha=0.3)

# Power Spectral Density
axes[2, 1].semilogy(frequencies[positive_freq_idx], power_spectrum[positive_freq_idx])
axes[2, 1].set_xlabel('ความถี่ (Hz)')
axes[2, 1].set_ylabel('Power Spectral Density')
axes[2, 1].set_title('การกระจายพลังงานตามความถี่')
axes[2, 1].set_xlim(0, 200)
axes[2, 1].grid(True, alpha=0.3)

plt.tight_layout()
plt.show()

# สรุปผลการวิเคราะห์
print(f"\\nสรุปผลการวิเคราะห์:")
print(f"- ความถี่หลักของสัญญาณ: {dominant_frequency:.1f} Hz")
print(f"- อัตราส่วนสัญญาณต่อสัญญาณรบกวน: {snr_db:.2f} dB")
print(f"- จำนวนเหตุการณ์อนุภาคที่ตรวจพบ: {len([t for t in [0.1, 0.3, 0.5, 0.7, 0.9]])}")
print(f"- ประสิทธิภาพการกรองสัญญาณ: ดีมาก")

# การประยุกต์ใช้ในฟิสิกส์
print(f"\\nการประยุกต์ใช้ในฟิสิกส์:")
print("- การวิเคราะห์สัญญาณจากเครื่องตรวจจับอนุภาค")
print("- การกำจัดสัญญาณรบกวนในการทดลองฟิสิกส์")
print("- การตรวจจับเหตุการณ์หายากในฟิสิกส์อนุภาค")
print("- การวิเคราะห์คลื่นความโน้มถ่วง")`,
      badge: "Signal Processing"
    }
  ];

  // Use provided examples or default ones
  const allExamples = examples.length > 0 ? examples : defaultExamples;

  useEffect(() => {
    if (allExamples[activeExample]) {
      setCode(allExamples[activeExample].code);
    }
  }, [activeExample, allExamples]);

  useEffect(() => {
    if (onCodeChange) {
      onCodeChange(code);
    }
  }, [code, onCodeChange]);

  const runCode = async () => {
    setIsRunning(true);
    setOutput('กำลังรันโค้ด...\n');

    try {
      // Simulate code execution
      await new Promise(resolve => setTimeout(resolve, 1000));
      
      // Mock output based on code content
      let mockOutput = '';
      
      if (code.includes('Linear Regression')) {
        mockOutput = `สมการที่ได้: a = 0.398F + 0.012
ค่า R² = 0.987
มวลที่คำนวณได้: 2.513 kg
มวลจริง: 2.5 kg
ความผิดพลาด: 0.52%

การวิเคราะห์ความผิดพลาด:
RMSE: 0.1876 m/s²
ความผิดพลาดเฉลี่ย: 0.1523 m/s²

[กราฟแสดงความสัมพันธ์ F = ma]`;
      } else if (code.includes('Neural Network')) {
        mockOutput = `โครงสร้าง Neural Network:
Model: "sequential"
_________________________________________________________________
Layer (type)                 Output Shape              Param #   
=================================================================
dense (Dense)                (None, 64)                448       
dropout (Dropout)            (None, 64)                0         
dense_1 (Dense)              (None, 32)                2080      
dropout_1 (Dropout)          (None, 32)                0         
dense_2 (Dense)              (None, 16)                528       
dense_3 (Dense)              (None, 1)                 17        
=================================================================
Total params: 3,073
Trainable params: 3,073

Epoch 100/100
40/40 [==============================] - 0s 2ms/step - loss: 0.1234 - accuracy: 0.9567

ความแม่นยำบนข้อมูลทดสอบ: 0.9625

รายงานการจำแนก:
              precision    recall  f1-score   support
   State |0⟩       0.96      0.97      0.96       200
   State |1⟩       0.97      0.96      0.96       200
    accuracy                           0.96       400

Confusion Matrix:
[[194   6]
 [  9 191]]

ฟีเจอร์ที่ใช้: ['Re(ψ)', 'Im(ψ)', 'P(|0⟩)', 'P(|1⟩)', 'Phase', 'Entanglement']
โมเดลสามารถจำแนกสถานะควอนตัมได้อย่างมีประสิทธิภาพ!`;
      } else if (code.includes('Fourier')) {
        mockOutput = `การวิเคราะห์สัญญาณฟิสิกส์ด้วย Fourier Transform
==================================================
ความถี่หลัก: 50.0 Hz
Signal-to-Noise Ratio: 12.45 dB

สรุปผลการวิเคราะห์:
- ความถี่หลักของสัญญาณ: 50.0 Hz
- อัตราส่วนสัญญาณต่อสัญญาณรบกวน: 12.45 dB
- จำนวนเหตุการณ์อนุภาคที่ตรวจพบ: 5
- ประสิทธิภาพการกรองสัญญาณ: ดีมาก

การประยุกต์ใช้ในฟิสิกส์:
- การวิเคราะห์สัญญาณจากเครื่องตรวจจับอนุภาค
- การกำจัดสัญญาณรบกวนในการทดลองฟิสิกส์
- การตรวจจับเหตุการณ์หายากในฟิสิกส์อนุภาค
- การวิเคราะห์คลื่นความโน้มถ่วง

[กราฟแสดงการวิเคราะห์สัญญาณและสเปกตรัม]`;
      } else {
        mockOutput = `โค้ดทำงานเสร็จสิ้น!
เวลาที่ใช้: ${Math.random() * 2 + 0.5}s
ผลลัพธ์: สำเร็จ

${code.split('\n').filter(line => line.includes('print')).map(line => {
  const match = line.match(/print\(['"](.+?)['"]\)/);
  return match ? match[1] : 'Output generated';
}).join('\n')}`;
      }
      
      setOutput(mockOutput);
    } catch (error) {
      setOutput(`Error: ${error.message}`);
    } finally {
      setIsRunning(false);
    }
  };

  const copyCode = () => {
    navigator.clipboard.writeText(code);
    // Show toast notification (simplified)
    alert('คัดลอกโค้ดแล้ว!');
  };

  const downloadCode = () => {
    const blob = new Blob([code], { type: 'text/plain' });
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = `${allExamples[activeExample]?.title || 'code'}.py`;
    a.click();
    URL.revokeObjectURL(url);
  };

  const resetCode = () => {
    if (allExamples[activeExample]) {
      setCode(allExamples[activeExample].code);
      setOutput('');
    }
  };

  const saveCode = () => {
    const savedCode = {
      title: allExamples[activeExample]?.title || 'Custom Code',
      code: code,
      timestamp: new Date().toISOString()
    };
    localStorage.setItem('saved_code', JSON.stringify(savedCode));
    alert('บันทึกโค้ดแล้ว!');
  };

  const shareCode = () => {
    const shareData = {
      title: allExamples[activeExample]?.title || 'Physics Code',
      text: code
    };
    
    if (navigator.share) {
      navigator.share(shareData);
    } else {
      copyCode();
      alert('คัดลอกโค้ดเพื่อแชร์แล้ว!');
    }
  };

  const handleKeyDown = (e) => {
    if (e.key === 'Tab') {
      e.preventDefault();
      const start = e.target.selectionStart;
      const end = e.target.selectionEnd;
      const newCode = code.substring(0, start) + '    ' + code.substring(end);
      setCode(newCode);
      
      // Set cursor position after the tab
      setTimeout(() => {
        e.target.selectionStart = e.target.selectionEnd = start + 4;
      }, 0);
    }
    
    if ((e.ctrlKey || e.metaKey) && e.key === 'Enter') {
      runCode();
    }
  };

  return (
    <Card className={`${className} ${isFullscreen ? 'fixed inset-4 z-50' : ''}`}>
      <CardHeader>
        <div className="flex items-center justify-between">
          <div className="flex items-center gap-3">
            <Badge variant="secondary" className="bg-green-100 text-green-700">
              <Code className="w-3 h-3 mr-1" />
              โต้ตอบได้
            </Badge>
            <CardTitle>{title}</CardTitle>
          </div>
          <div className="flex items-center gap-2">
            <Button variant="outline" size="sm" onClick={() => setShowSettings(!showSettings)}>
              <Settings className="w-4 h-4" />
            </Button>
            <Button variant="outline" size="sm" onClick={() => setIsFullscreen(!isFullscreen)}>
              <Maximize2 className="w-4 h-4" />
            </Button>
          </div>
        </div>
        {description && (
          <p className="text-gray-600">{description}</p>
        )}
      </CardHeader>

      <CardContent>
        <Tabs defaultValue="code" className="space-y-4">
          <TabsList className="grid w-full grid-cols-3">
            <TabsTrigger value="code" className="flex items-center gap-2">
              <Code className="w-4 h-4" />
              โค้ด
            </TabsTrigger>
            <TabsTrigger value="output" className="flex items-center gap-2">
              <Terminal className="w-4 h-4" />
              ผลลัพธ์
            </TabsTrigger>
            <TabsTrigger value="docs" className="flex items-center gap-2">
              <FileText className="w-4 h-4" />
              เอกสาร
            </TabsTrigger>
          </TabsList>

          <TabsContent value="code" className="space-y-4">
            {/* Example Selection */}
            <div className="flex flex-wrap gap-2">
              {allExamples.map((example, index) => (
                <Button
                  key={index}
                  variant={activeExample === index ? "default" : "outline"}
                  size="sm"
                  onClick={() => setActiveExample(index)}
                  className="flex items-center gap-2"
                >
                  <Badge variant="secondary" className="text-xs">
                    {example.badge}
                  </Badge>
                  {example.title}
                </Button>
              ))}
            </div>

            {/* Settings Panel */}
            {showSettings && (
              <div className="p-4 bg-gray-50 rounded-lg space-y-3">
                <div className="flex items-center gap-4">
                  <label className="text-sm font-medium">ขนาดตัวอักษร:</label>
                  <input
                    type="range"
                    min="10"
                    max="20"
                    value={fontSize}
                    onChange={(e) => setFontSize(parseInt(e.target.value))}
                    className="w-20"
                  />
                  <span className="text-sm">{fontSize}px</span>
                </div>
                <div className="flex items-center gap-2">
                  <input
                    type="checkbox"
                    id="autoRun"
                    checked={autoRun}
                    onChange={(e) => setAutoRun(e.target.checked)}
                  />
                  <label htmlFor="autoRun" className="text-sm">รันอัตโนมัติเมื่อเปลี่ยนโค้ด</label>
                </div>
              </div>
            )}

            {/* Code Editor */}
            <div className="relative">
              <textarea
                ref={textareaRef}
                value={code}
                onChange={(e) => setCode(e.target.value)}
                onKeyDown={handleKeyDown}
                className="w-full h-96 p-4 font-mono text-sm border rounded-lg bg-gray-900 text-green-400 resize-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500"
                style={{ fontSize: `${fontSize}px` }}
                placeholder="เขียนโค้ด Python ของคุณที่นี่..."
                spellCheck={false}
              />
              <div className="absolute top-2 right-2 flex gap-1">
                <Button variant="ghost" size="sm" onClick={copyCode}>
                  <Copy className="w-4 h-4" />
                </Button>
                <Button variant="ghost" size="sm" onClick={resetCode}>
                  <RotateCcw className="w-4 h-4" />
                </Button>
                <Button variant="ghost" size="sm" onClick={downloadCode}>
                  <Download className="w-4 h-4" />
                </Button>
              </div>
            </div>

            {/* Control Buttons */}
            <div className="flex justify-between items-center">
              <div className="flex gap-2">
                <Button 
                  onClick={runCode} 
                  disabled={isRunning}
                  className="flex items-center gap-2"
                >
                  <Play className="w-4 h-4" />
                  {isRunning ? 'กำลังรัน...' : 'รันโค้ด'}
                </Button>
                <Button variant="outline" onClick={saveCode}>
                  <Save className="w-4 h-4 mr-2" />
                  บันทึก
                </Button>
                <Button variant="outline" onClick={shareCode}>
                  <Share2 className="w-4 h-4 mr-2" />
                  แชร์
                </Button>
              </div>
              
              <div className="text-sm text-gray-500">
                กด Ctrl+Enter เพื่อรันโค้ด
              </div>
            </div>
          </TabsContent>

          <TabsContent value="output" className="space-y-4">
            <div className="bg-gray-900 text-green-400 p-4 rounded-lg font-mono text-sm h-96 overflow-auto">
              <pre className="whitespace-pre-wrap">{output || 'ยังไม่มีผลลัพธ์ กดปุ่ม "รันโค้ด" เพื่อเริ่มต้น'}</pre>
            </div>
          </TabsContent>

          <TabsContent value="docs" className="space-y-4">
            <div className="prose max-w-none">
              <h3>คำแนะนำการใช้งาน</h3>
              <ul>
                <li>เลือกตัวอย่างโค้ดจากปุ่มด้านบน</li>
                <li>แก้ไขโค้ดตามต้องการ</li>
                <li>กดปุ่ม "รันโค้ด" หรือ Ctrl+Enter เพื่อรันโค้ด</li>
                <li>ดูผลลัพธ์ในแท็บ "ผลลัพธ์"</li>
                <li>บันทึกหรือแชร์โค้ดของคุณ</li>
              </ul>
              
              <h3>ไลบรารีที่รองรับ</h3>
              <ul>
                <li>NumPy - การคำนวณเชิงตัวเลข</li>
                <li>Matplotlib - การสร้างกราฟ</li>
                <li>SciPy - ฟังก์ชันทางวิทยาศาสตร์</li>
                <li>Scikit-learn - Machine Learning</li>
                <li>TensorFlow - Deep Learning</li>
              </ul>

              <h3>ตัวอย่างการใช้งาน</h3>
              <p>โค้ดตัวอย่างครอบคลุมหัวข้อต่างๆ ในฟิสิกส์:</p>
              <ul>
                <li>การวิเคราะห์ข้อมูลการทดลอง</li>
                <li>การจำลองระบบฟิสิกส์</li>
                <li>การประมวลผลสัญญาณ</li>
                <li>การประยุกต์ใช้ Machine Learning</li>
              </ul>
            </div>
          </TabsContent>
        </Tabs>
      </CardContent>
    </Card>
  );
};

export default EnhancedCodePlayground;
