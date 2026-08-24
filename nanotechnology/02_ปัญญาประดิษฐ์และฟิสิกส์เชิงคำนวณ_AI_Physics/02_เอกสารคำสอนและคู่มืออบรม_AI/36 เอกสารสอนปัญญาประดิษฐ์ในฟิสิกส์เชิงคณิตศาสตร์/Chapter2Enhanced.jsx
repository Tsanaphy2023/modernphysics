import React, { useState, useEffect } from 'react';
import { motion } from 'framer-motion';
import { BookOpen, Clock, CheckCircle, Play, Download, Copy, RotateCcw } from 'lucide-react';
import CodePlayground from './CodePlayground';
import InteractiveSimulation from './InteractiveSimulation';

const Chapter2Enhanced = () => {
  const [activeTab, setActiveTab] = useState('content');
  const [completedSections, setCompletedSections] = useState(new Set());
  const [quizAnswers, setQuizAnswers] = useState({});
  const [quizSubmitted, setQuizSubmitted] = useState(false);
  const [quizScore, setQuizScore] = useState(0);

  const sections = [
    {
      id: '2.1',
      title: 'พีชคณิตเชิงเส้น: เวกเตอร์ เมทริกซ์ และการดำเนินการ',
      duration: '25 นาที',
      overview: 'ศึกษาพื้นฐานของพีชคณิตเชิงเส้น ซึ่งเป็นภาษาหลักในการจัดเก็บและประมวลผลข้อมูลในแบบจำลอง AI',
      keyPoints: [
        'เวกเตอร์และการดำเนินการเวกเตอร์ในปริภูมิหลายมิติ',
        'เมทริกซ์และการคูณเมทริกซ์สำหรับการแปลงข้อมูล',
        'การแยกค่าเอกพจน์ (SVD) และการประยุกต์ใช้ในการลดมิติ',
        'ค่าเจาะจง (Eigenvalues) และเวกเตอร์เจาะจง (Eigenvectors)'
      ],
      examples: [
        'การใช้เมทริกซ์ในการแปลงพิกัดในฟิสิกส์',
        'การประยุกต์ใช้ SVD ในการบีบอัดภาพและการลดมิติข้อมูล',
        'การวิเคราะห์องค์ประกอบหลัก (PCA) สำหรับข้อมูลฟิสิกส์'
      ]
    },
    {
      id: '2.2',
      title: 'แคลคูลัสหลายตัวแปรและการหาค่าเหมาะสมที่สุด',
      duration: '30 นาที',
      overview: 'เรียนรู้แนวคิดการหาค่าเหมาะสมที่สุด ซึ่งเป็นหัวใจของการฝึกสอนแบบจำลอง Machine Learning',
      keyPoints: [
        'อนุพันธ์ย่อย (Partial Derivatives) และเกรเดียนต์ (Gradient)',
        'อัลกอริทึม Gradient Descent และการประยุกต์ใช้',
        'เมทริกซ์เฮสเซียน (Hessian Matrix) และการวิเคราะห์ความโค้ง',
        'การหาค่าเหมาะสมที่สุดแบบมีเงื่อนไข (Constrained Optimization)'
      ],
      examples: [
        'การใช้ Gradient Descent ในการฝึกสอน Neural Networks',
        'การหาค่าพารามิเตอร์ที่เหมาะสมในแบบจำลองฟิสิกส์',
        'การประยุกต์ใช้ในการแก้ปัญหาการหาค่าต่ำสุดของพลังงาน'
      ]
    },
    {
      id: '2.3',
      title: 'ทฤษฎีความน่าจะเป็นและสถิติ',
      duration: '35 นาที',
      overview: 'ศึกษาพื้นฐานสำหรับการทำความเข้าใจความไม่แน่นอนในข้อมูลและการสร้างแบบจำลองเชิงสถิติ',
      keyPoints: [
        'ตัวแปรสุ่มและการแจกแจงความน่าจะเป็น',
        'ทฤษฎีบทเบย์ (Bayes\' Theorem) และการอนุมานเชิงสถิติ',
        'การประมาณค่าพารามิเตอร์: MLE และ MAP',
        'การทดสอบสมมติฐานและช่วงความเชื่อมั่น'
      ],
      examples: [
        'การใช้ Bayesian Inference ในการวิเคราะห์ข้อมูลการทดลอง',
        'การประมาณความไม่แน่นอนในการวัดทางฟิสิกส์',
        'การประยุกต์ใช้ในการวิเคราะห์ข้อผิดพลาดในการทดลอง'
      ]
    },
    {
      id: '2.4',
      title: 'การวิเคราะห์ฟูเรียร์และการแปลงเวฟเล็ต',
      duration: '30 นาที',
      overview: 'เครื่องมือทางคณิตศาสตร์สำหรับการประมวลผลสัญญาณและการวิเคราะห์ข้อมูลอนุกรมเวลา',
      keyPoints: [
        'การแปลงฟูเรียร์และการวิเคราะห์สเปกตรัม',
        'การแปลงเวฟเล็ตสำหรับสัญญาณไม่หยุดนิ่ง',
        'การประยุกต์ใช้ในการกรองสัญญาณรบกวน',
        'การวิเคราะห์ความถี่-เวลาในข้อมูลฟิสิกส์'
      ],
      examples: [
        'การวิเคราะห์สัญญาณจากเครื่องตรวจจับคลื่นความโน้มถ่วง',
        'การประมวลผลสัญญาณจากพัลซาร์และดาราศาสตร์',
        'การใช้ในการวิเคราะห์ความผันผวนในพลาสมา'
      ]
    },
    {
      id: '2.5',
      title: 'ทฤษฎีข้อมูลและเอนโทรปี',
      duration: '25 นาที',
      overview: 'การวัดปริมาณข้อมูล ความไม่แน่นอน และการบีบอัดข้อมูลในบริบทของฟิสิกส์',
      keyPoints: [
        'เอนโทรปีของชานนอนและการวัดข้อมูล',
        'ความสัมพันธ์ระหว่างเอนโทรปีข้อมูลและเทอร์โมไดนามิกส์',
        'การประยุกต์ใช้ในการบีบอัดข้อมูลและการเลือกคุณสมบัติ',
        'Information Gain และการวิเคราะห์ความหลากหลาย'
      ],
      examples: [
        'การใช้เอนโทรปีในการวิเคราะห์ระบบที่ซับซ้อน',
        'การประยุกต์ใช้ในการวัดความสัมพันธ์ระหว่างตัวแปร',
        'การใช้ในการออกแบบการทดลองที่มีประสิทธิภาพ'
      ]
    },
    {
      id: '2.6',
      title: 'เรขาคณิตเชิงอนุพันธ์และท่อร่วม',
      duration: '35 นาที',
      overview: 'แนวคิดสำคัญสำหรับการลดมิติข้อมูลแบบไม่เชิงเส้นและการทำความเข้าใจโครงสร้างข้อมูล',
      keyPoints: [
        'แนวคิดของท่อร่วม (Manifold) และเรขาคณิตเชิงอนุพันธ์',
        'เทคนิคการลดมิติแบบไม่เชิงเส้น: t-SNE, UMAP, Isomap',
        'การประยุกต์ใช้ในการวิเคราะห์ข้อมูลที่มีมิติสูง',
        'การค้นหาตัวแปรที่ซ่อนอยู่ในระบบฟิสิกส์'
      ],
      examples: [
        'การวิเคราะห์ข้อมูลจากพลศาสตร์โมเลกุล',
        'การศึกษาแผนภาพสถานะของสสาร',
        'การค้นพบตัวแปรสำคัญในระบบหลายอนุภาค'
      ]
    },
    {
      id: '2.7',
      title: 'ทฤษฎีกราฟและเครือข่าย',
      duration: '30 นาที',
      overview: 'พื้นฐานสำหรับ Graph Neural Networks และการวิเคราะห์ข้อมูลที่มีโครงสร้างเป็นเครือข่าย',
      keyPoints: [
        'แนวคิดพื้นฐานของทฤษฎีกราฟและเมทริกซ์ประชิด',
        'เมทริกซ์ลาปลาเซียนและการวิเคราะห์สเปกตรัม',
        'Graph Neural Networks และการประมวลผลข้อมูลกราฟ',
        'การประยุกต์ใช้ในฟิสิกส์ของวัสดุและอนุภาค'
      ],
      examples: [
        'การสร้างแบบจำลองโครงสร้างโมเลกุลและผลึก',
        'การวิเคราะห์ข้อมูลจากเครื่องตรวจจับอนุภาค',
        'การศึกษาปฏิสัมพันธ์ในระบบหลายอนุภาค'
      ]
    }
  ];

  const quizQuestions = [
    {
      id: 1,
      question: 'การแยกค่าเอกพจน์ (SVD) มีประโยชน์หลักในการประยุกต์ใช้ใดต่อไปนี้?',
      options: [
        'การลดมิติข้อมูลและการบีบอัดข้อมูล',
        'การคำนวณอนุพันธ์ของฟังก์ชัน',
        'การแก้สมการเชิงอนุพันธ์',
        'การคำนวณความน่าจะเป็น'
      ],
      correct: 0,
      explanation: 'SVD เป็นเทคนิคที่สำคัญในการลดมิติข้อมูลและการบีบอัดข้อมูล โดยสามารถแยกเมทริกซ์ออกเป็นองค์ประกอบที่สำคัญที่สุด ซึ่งใช้ในการวิเคราะห์องค์ประกอบหลัก (PCA) และการประมวลผลภาพ'
    },
    {
      id: 2,
      question: 'อัลกอริทึม Gradient Descent ใช้หลักการใดในการหาค่าเหมาะสมที่สุด?',
      options: [
        'การเคลื่อนที่ในทิศทางที่เพิ่มค่าฟังก์ชันต้นทุน',
        'การเคลื่อนที่ในทิศทางตรงข้ามกับเกรเดียนต์',
        'การสุ่มค่าพารามิเตอร์ใหม่ในแต่ละรอบ',
        'การใช้อนุพันธ์อันดับสองเท่านั้น'
      ],
      correct: 1,
      explanation: 'Gradient Descent ทำงานโดยการเคลื่อนที่ในทิศทางตรงข้ามกับเกรเดียนต์ (ทิศทางที่ฟังก์ชันเพิ่มขึ้นเร็วที่สุด) เพื่อหาจุดที่ฟังก์ชันต้นทุนมีค่าต่ำสุด'
    },
    {
      id: 3,
      question: 'เอนโทรปีของชานนอนวัดสิ่งใดในทฤษฎีข้อมูล?',
      options: [
        'ความเร็วในการประมวลผลข้อมูล',
        'ความไม่แน่นอนหรือปริมาณข้อมูลในระบบ',
        'ขนาดของไฟล์ข้อมูล',
        'จำนวนบิตที่ใช้ในการเก็บข้อมูล'
      ],
      correct: 1,
      explanation: 'เอนโทรปีของชานนอนเป็นการวัดความไม่แน่นอนหรือปริมาณข้อมูลที่มีอยู่ในระบบ ยิ่งเอนโทรปีสูง หมายถึงความไม่แน่นอนสูงและมีข้อมูลมาก'
    }
  ];

  const codeExamples = [
    {
      title: 'Matrix Operations with NumPy',
      description: 'พื้นฐานการดำเนินการเมทริกซ์สำหรับ Machine Learning',
      code: `import numpy as np
import matplotlib.pyplot as plt

# สร้างเมทริกซ์ตัวอย่าง
A = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])

B = np.array([[9, 8, 7],
              [6, 5, 4],
              [3, 2, 1]])

print("Matrix A:")
print(A)
print("\\nMatrix B:")
print(B)

# การคูณเมทริกซ์
C = np.dot(A, B)
print("\\nMatrix multiplication A @ B:")
print(C)

# การแยกค่าเอกพจน์ (SVD)
U, s, Vt = np.linalg.svd(A)
print("\\nSingular Value Decomposition:")
print("U shape:", U.shape)
print("Singular values:", s)
print("Vt shape:", Vt.shape)

# การหาค่าเจาะจงและเวกเตอร์เจาะจง
eigenvalues, eigenvectors = np.linalg.eig(A)
print("\\nEigenvalues:", eigenvalues)
print("Eigenvectors shape:", eigenvectors.shape)`
    },
    {
      title: 'Gradient Descent Implementation',
      description: 'การใช้งาน Gradient Descent สำหรับ Linear Regression',
      code: `import numpy as np
import matplotlib.pyplot as plt

# ฟังก์ชันต้นทุน (Mean Squared Error)
def cost_function(X, y, theta):
    m = len(y)
    predictions = X.dot(theta)
    sq_error = (predictions - y)**2
    return (1 / (2 * m)) * np.sum(sq_error)

# การคำนวณ Gradient
def gradient(X, y, theta):
    m = len(y)
    predictions = X.dot(theta)
    errors = np.subtract(predictions, y)
    grad = (1 / m) * X.transpose().dot(errors)
    return grad

# Gradient Descent Algorithm
def gradient_descent(X, y, theta, learning_rate, iterations):
    cost_history = np.zeros(iterations)
    theta_history = np.zeros((iterations, len(theta)))
    
    for i in range(iterations):
        theta = theta - learning_rate * gradient(X, y, theta)
        cost_history[i] = cost_function(X, y, theta)
        theta_history[i] = theta
    
    return theta, cost_history, theta_history

# สร้างข้อมูลตัวอย่าง
np.random.seed(42)
X = np.array([[1, 1], [1, 2], [1, 3], [1, 4], [1, 5]])
y = np.array([1, 2, 3, 4, 5]) + np.random.normal(0, 0.1, 5)

# พารามิเตอร์เริ่มต้น
theta = np.array([0.0, 0.0])
learning_rate = 0.01
iterations = 1000

# รัน Gradient Descent
final_theta, cost_hist, theta_hist = gradient_descent(X, y, theta, learning_rate, iterations)

print("Optimized parameters (theta):", final_theta)
print("Final cost:", cost_hist[-1])
print("Cost reduction:", cost_hist[0] - cost_hist[-1])`
    },
    {
      title: 'Fourier Analysis for Signal Processing',
      description: 'การวิเคราะห์ฟูเรียร์สำหรับการประมวลผลสัญญาณทางฟิสิกส์',
      code: `import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

# สร้างสัญญาณตัวอย่าง (สัญญาณผสมของหลายความถี่)
t = np.linspace(0, 1, 1000, False)
freq1, freq2, freq3 = 50, 120, 200  # Hz

# สัญญาณผสม
signal_clean = (np.sin(2*np.pi*freq1*t) + 
                0.5*np.sin(2*np.pi*freq2*t) + 
                0.3*np.sin(2*np.pi*freq3*t))

# เพิ่มสัญญาณรบกวน
noise = 0.2 * np.random.normal(size=t.shape)
signal_noisy = signal_clean + noise

print("Signal analysis:")
print(f"Signal length: {len(signal_noisy)} samples")
print(f"Sampling rate: {len(t)} Hz")
print(f"Frequencies in signal: {freq1}, {freq2}, {freq3} Hz")

# การแปลงฟูเรียร์
fft_result = np.fft.fft(signal_noisy)
frequencies = np.fft.fftfreq(len(t), t[1] - t[0])

# หาความถี่ที่มีแอมพลิจูดสูงสุด
magnitude = np.abs(fft_result)
peak_indices = signal.find_peaks(magnitude[:len(magnitude)//2], height=50)[0]
peak_frequencies = frequencies[peak_indices]

print(f"\\nDetected peak frequencies: {peak_frequencies} Hz")

# การกรองสัญญาณด้วย Low-pass filter
nyquist = 0.5 * len(t)
low_cutoff = 100 / nyquist
b, a = signal.butter(4, low_cutoff, btype='low')
filtered_signal = signal.filtfilt(b, a, signal_noisy)

print(f"Applied low-pass filter with cutoff: {100} Hz")
print(f"Signal-to-noise ratio improved: {np.var(signal_clean)/np.var(noise):.2f}")`
    }
  ];

  const handleSectionComplete = (sectionId) => {
    setCompletedSections(prev => new Set([...prev, sectionId]));
  };

  const handleQuizAnswer = (questionId, answerIndex) => {
    setQuizAnswers(prev => ({
      ...prev,
      [questionId]: answerIndex
    }));
  };

  const handleQuizSubmit = () => {
    let score = 0;
    quizQuestions.forEach(question => {
      if (quizAnswers[question.id] === question.correct) {
        score++;
      }
    });
    setQuizScore(score);
    setQuizSubmitted(true);
  };

  const progressPercentage = Math.round((completedSections.size / sections.length) * 100);

  const tabContent = {
    content: (
      <div className="space-y-6">
        <div className="grid gap-4">
          {sections.map((section) => (
            <motion.div
              key={section.id}
              className={`border rounded-lg p-6 transition-all duration-300 ${
                completedSections.has(section.id)
                  ? 'border-green-300 bg-green-50'
                  : 'border-gray-200 bg-white hover:border-blue-300'
              }`}
              whileHover={{ scale: 1.02 }}
              transition={{ type: "spring", stiffness: 300 }}
            >
              <div className="flex items-start justify-between">
                <div className="flex-1">
                  <div className="flex items-center gap-3 mb-3">
                    <div className={`w-8 h-8 rounded-full flex items-center justify-center text-sm font-bold ${
                      completedSections.has(section.id)
                        ? 'bg-green-500 text-white'
                        : 'bg-blue-500 text-white'
                    }`}>
                      {completedSections.has(section.id) ? <CheckCircle className="w-4 h-4" /> : section.id}
                    </div>
                    <div>
                      <h3 className="text-lg font-semibold text-gray-900">{section.title}</h3>
                      <div className="flex items-center gap-4 text-sm text-gray-600">
                        <span className="flex items-center gap-1">
                          <Clock className="w-4 h-4" />
                          {section.duration}
                        </span>
                      </div>
                    </div>
                  </div>
                  
                  <p className="text-gray-700 mb-4">{section.overview}</p>
                  
                  <div className="mb-4">
                    <h4 className="font-semibold text-gray-900 mb-2">จุดสำคัญ:</h4>
                    <ul className="list-disc list-inside space-y-1 text-gray-700">
                      {section.keyPoints.map((point, index) => (
                        <li key={index}>{point}</li>
                      ))}
                    </ul>
                  </div>
                  
                  <div className="mb-4">
                    <h4 className="font-semibold text-gray-900 mb-2">ตัวอย่างการประยุกต์ใช้:</h4>
                    <ul className="list-disc list-inside space-y-1 text-gray-700">
                      {section.examples.map((example, index) => (
                        <li key={index}>{example}</li>
                      ))}
                    </ul>
                  </div>
                </div>
                
                <button
                  onClick={() => handleSectionComplete(section.id)}
                  disabled={completedSections.has(section.id)}
                  className={`ml-4 px-4 py-2 rounded-lg font-medium transition-colors ${
                    completedSections.has(section.id)
                      ? 'bg-green-100 text-green-700 cursor-not-allowed'
                      : 'bg-blue-500 text-white hover:bg-blue-600'
                  }`}
                >
                  {completedSections.has(section.id) ? 'เสร็จแล้ว' : 'ทำเครื่องหมายเสร็จ'}
                </button>
              </div>
            </motion.div>
          ))}
        </div>
      </div>
    ),
    
    simulations: (
      <div className="space-y-6">
        <div className="text-center mb-8">
          <h3 className="text-2xl font-bold text-gray-900 mb-2">การจำลองแบบโต้ตอบทางคณิตศาสตร์</h3>
          <p className="text-gray-600">สำรวจแนวคิดทางคณิตศาสตร์ผ่านการจำลองแบบโต้ตอบ</p>
        </div>
        
        <div className="grid gap-6">
          <div className="bg-white rounded-lg border border-gray-200 p-6">
            <div className="flex items-center gap-2 mb-4">
              <div className="bg-purple-100 text-purple-700 px-3 py-1 rounded-full text-sm font-medium">
                การจำลอง
              </div>
              <h4 className="text-lg font-semibold">การแปลงฟูเรียร์แบบโต้ตอบ</h4>
            </div>
            <InteractiveSimulation 
              type="fourier"
              title="การวิเคราะห์ความถี่ของสัญญาณ"
              description="สำรวจการแปลงสัญญาณจากโดเมนเวลาไปยังโดเมนความถี่"
            />
          </div>
          
          <div className="bg-white rounded-lg border border-gray-200 p-6">
            <div className="flex items-center gap-2 mb-4">
              <div className="bg-green-100 text-green-700 px-3 py-1 rounded-full text-sm font-medium">
                การจำลอง
              </div>
              <h4 className="text-lg font-semibold">การหาค่าเหมาะสมที่สุดด้วย Gradient Descent</h4>
            </div>
            <InteractiveSimulation 
              type="optimization"
              title="การเคลื่อนที่ของ Gradient Descent"
              description="ดูการทำงานของอัลกอริทึม Gradient Descent ในการหาค่าต่ำสุด"
            />
          </div>
          
          <div className="bg-white rounded-lg border border-gray-200 p-6">
            <div className="flex items-center gap-2 mb-4">
              <div className="bg-blue-100 text-blue-700 px-3 py-1 rounded-full text-sm font-medium">
                การจำลอง
              </div>
              <h4 className="text-lg font-semibold">การลดมิติข้อมูลด้วย PCA</h4>
            </div>
            <InteractiveSimulation 
              type="pca"
              title="การวิเคราะห์องค์ประกอบหลัก"
              description="เข้าใจการลดมิติข้อมูลและการรักษาข้อมูลที่สำคัญ"
            />
          </div>
        </div>
      </div>
    ),
    
    code: (
      <div className="space-y-6">
        <div className="text-center mb-8">
          <h3 className="text-2xl font-bold text-gray-900 mb-2">ตัวอย่างโค้ด Python</h3>
          <p className="text-gray-600">ลองเขียนและรันโค้ดเพื่อเรียนรู้แนวคิดทางคณิตศาสตร์</p>
        </div>
        
        <CodePlayground 
          title="คณิตศาสตร์สำหรับ Machine Learning - บทที่ 2"
          description="ตัวอย่างโค้ดสำหรับการเรียนรู้แนวคิดทางคณิตศาสตร์ที่สำคัญ"
          examples={codeExamples}
          defaultCode={codeExamples[0].code}
        />
      </div>
    ),
    
    quiz: (
      <div className="space-y-6">
        <div className="text-center mb-8">
          <h3 className="text-2xl font-bold text-gray-900 mb-2">แบบทดสอบบทที่ 2</h3>
          <p className="text-gray-600">ทดสอบความเข้าใจในเนื้อหาที่เรียนมา</p>
        </div>
        
        <div className="space-y-6">
          {quizQuestions.map((question, index) => (
            <motion.div
              key={question.id}
              className="bg-white rounded-lg border border-gray-200 p-6"
              initial={{ opacity: 0, y: 20 }}
              animate={{ opacity: 1, y: 0 }}
              transition={{ delay: index * 0.1 }}
            >
              <h4 className="text-lg font-semibold mb-4">
                {question.id}. {question.question}
              </h4>
              
              <div className="space-y-3">
                {question.options.map((option, optionIndex) => (
                  <label
                    key={optionIndex}
                    className={`flex items-center p-3 rounded-lg border cursor-pointer transition-colors ${
                      quizAnswers[question.id] === optionIndex
                        ? 'border-blue-500 bg-blue-50'
                        : 'border-gray-200 hover:border-gray-300'
                    } ${
                      quizSubmitted
                        ? optionIndex === question.correct
                          ? 'border-green-500 bg-green-50'
                          : quizAnswers[question.id] === optionIndex && optionIndex !== question.correct
                          ? 'border-red-500 bg-red-50'
                          : 'border-gray-200 bg-gray-50'
                        : ''
                    }`}
                  >
                    <input
                      type="radio"
                      name={`question-${question.id}`}
                      value={optionIndex}
                      checked={quizAnswers[question.id] === optionIndex}
                      onChange={() => handleQuizAnswer(question.id, optionIndex)}
                      disabled={quizSubmitted}
                      className="mr-3"
                    />
                    <span className={quizSubmitted && optionIndex === question.correct ? 'font-semibold' : ''}>
                      {option}
                    </span>
                  </label>
                ))}
              </div>
              
              {quizSubmitted && (
                <div className="mt-4 p-4 bg-blue-50 rounded-lg">
                  <p className="text-sm text-blue-800">
                    <strong>คำอธิบาย:</strong> {question.explanation}
                  </p>
                </div>
              )}
            </motion.div>
          ))}
          
          {!quizSubmitted ? (
            <button
              onClick={handleQuizSubmit}
              disabled={Object.keys(quizAnswers).length < quizQuestions.length}
              className="w-full bg-blue-500 text-white py-3 px-6 rounded-lg font-medium hover:bg-blue-600 disabled:bg-gray-300 disabled:cursor-not-allowed transition-colors"
            >
              ส่งคำตอบ
            </button>
          ) : (
            <div className="text-center p-6 bg-green-50 rounded-lg">
              <h3 className="text-xl font-bold text-green-800 mb-2">
                คะแนนของคุณ: {quizScore}/{quizQuestions.length}
              </h3>
              <p className="text-green-700">
                {quizScore === quizQuestions.length
                  ? 'ยอดเยี่ยม! คุณตอบถูกทุกข้อ'
                  : quizScore >= quizQuestions.length * 0.7
                  ? 'ดีมาก! คุณมีความเข้าใจที่ดี'
                  : 'ควรทบทวนเนื้อหาเพิ่มเติม'}
              </p>
            </div>
          )}
        </div>
      </div>
    )
  };

  return (
    <div className="min-h-screen bg-gray-50">
      {/* Chapter Header */}
      <div className="bg-gradient-to-r from-green-600 to-blue-600 text-white">
        <div className="max-w-7xl mx-auto px-4 py-8">
          <div className="flex items-center justify-between">
            <div className="flex-1">
              <div className="flex items-center gap-3 mb-4">
                <BookOpen className="w-8 h-8" />
                <span className="bg-white/20 px-3 py-1 rounded-full text-sm font-medium">
                  บทที่ 2 • ระดับกลาง
                </span>
              </div>
              <h1 className="text-3xl font-bold mb-2">
                พื้นฐานทางคณิตศาสตร์สำหรับการเรียนรู้ของเครื่อง
              </h1>
              <p className="text-green-100 text-lg mb-4">
                Mathematical Foundations for Machine Learning
              </p>
              <p className="text-white/90 max-w-3xl">
                ศึกษาแนวคิดทางคณิตศาสตร์ที่สำคัญสำหรับการทำความเข้าใจและประยุกต์ใช้ Machine Learning ในฟิสิกส์ 
                รวมถึงพีชคณิตเชิงเส้น แคลคูลัส ทฤษฎีความน่าจะเป็น และเครื่องมือทางคณิตศาสตร์อื่นๆ
              </p>
              
              <div className="flex items-center gap-6 mt-6 text-sm">
                <div className="flex items-center gap-2">
                  <Clock className="w-4 h-4" />
                  <span>ระยะเวลา: 3.5 ชั่วโมง</span>
                </div>
                <div className="flex items-center gap-2">
                  <BookOpen className="w-4 h-4" />
                  <span>หัวข้อ: 7 หัวข้อ</span>
                </div>
                <div className="flex items-center gap-2">
                  <CheckCircle className="w-4 h-4" />
                  <span>เสร็จแล้ว: {completedSections.size}/7</span>
                </div>
              </div>
            </div>
            
            <div className="text-right">
              <div className="text-4xl font-bold mb-2">{progressPercentage}%</div>
              <div className="text-green-100">ความคืบหน้า</div>
              <div className="w-32 bg-white/20 rounded-full h-2 mt-2">
                <div 
                  className="bg-white rounded-full h-2 transition-all duration-500"
                  style={{ width: `${progressPercentage}%` }}
                />
              </div>
            </div>
          </div>
        </div>
      </div>

      {/* Tab Navigation */}
      <div className="bg-white border-b border-gray-200 sticky top-0 z-10">
        <div className="max-w-7xl mx-auto px-4">
          <div className="flex space-x-8">
            {[
              { id: 'content', label: 'เนื้อหา', icon: BookOpen },
              { id: 'simulations', label: 'การจำลอง', icon: Play },
              { id: 'code', label: 'โค้ดตัวอย่าง', icon: Copy },
              { id: 'quiz', label: 'แบบทดสอบ', icon: CheckCircle }
            ].map(tab => (
              <button
                key={tab.id}
                onClick={() => setActiveTab(tab.id)}
                className={`flex items-center gap-2 py-4 px-2 border-b-2 font-medium text-sm transition-colors ${
                  activeTab === tab.id
                    ? 'border-blue-500 text-blue-600'
                    : 'border-transparent text-gray-500 hover:text-gray-700 hover:border-gray-300'
                }`}
              >
                <tab.icon className="w-4 h-4" />
                {tab.label}
              </button>
            ))}
          </div>
        </div>
      </div>

      {/* Content */}
      <div className="max-w-7xl mx-auto px-4 py-8">
        {tabContent[activeTab]}
      </div>

      {/* Navigation */}
      <div className="bg-white border-t border-gray-200 py-6">
        <div className="max-w-7xl mx-auto px-4 flex items-center justify-between">
          <button className="flex items-center gap-2 px-4 py-2 text-gray-600 hover:text-gray-900 transition-colors">
            <span>← บทที่ 1</span>
          </button>
          
          <div className="flex items-center gap-4">
            <span className="text-sm text-gray-600">บทที่ 2 จาก 9</span>
            <button className="flex items-center gap-2 px-4 py-2 bg-blue-500 text-white rounded-lg hover:bg-blue-600 transition-colors">
              <Download className="w-4 h-4" />
              ดาวน์โหลด PDF
            </button>
          </div>
          
          <button className="flex items-center gap-2 px-4 py-2 text-gray-600 hover:text-gray-900 transition-colors">
            <span>บทที่ 3 →</span>
          </button>
        </div>
      </div>
    </div>
  );
};

export default Chapter2Enhanced;
