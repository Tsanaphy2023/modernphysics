import React, { useState, useEffect } from 'react'
import { motion, AnimatePresence } from 'framer-motion'
import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/card.jsx'
import { Button } from '@/components/ui/button.jsx'
import { Badge } from '@/components/ui/badge.jsx'
import { Progress } from '@/components/ui/progress.jsx'
import { Tabs, TabsContent, TabsList, TabsTrigger } from '@/components/ui/tabs.jsx'
import { 
  BookOpen, 
  ChevronDown, 
  ChevronRight, 
  Clock, 
  Target, 
  CheckCircle,
  Play,
  Code,
  Brain,
  Zap,
  ArrowRight,
  ArrowLeft,
  Download
} from 'lucide-react'

// Import our interactive components
import CodePlayground from './CodePlayground.jsx'
import InteractiveSimulation from './InteractiveSimulation.jsx'

const Chapter1Enhanced = () => {
  const [expandedSections, setExpandedSections] = useState({})
  const [completedSections, setCompletedSections] = useState(new Set())
  const [currentSection, setCurrentSection] = useState(0)
  const [chapterProgress, setChapterProgress] = useState(0)
  const [quizAnswers, setQuizAnswers] = useState({})
  const [quizSubmitted, setQuizSubmitted] = useState(false)
  const [quizScore, setQuizScore] = useState(0)

  // Chapter 1 content structure
  const chapterData = {
    id: 1,
    title: "บทนำสู่ปัญญาประดิษฐ์และฟิสิกส์เชิงคณิตศาสตร์",
    subtitle: "Introduction to AI and Mathematical Physics",
    description: "ภาพรวมและความสำคัญของการบูรณาการ AI ในงานวิจัยฟิสิกส์ พร้อมทบทวนแนวคิดหลักทางฟิสิกส์เชิงคณิตศาสตร์",
    duration: "2 ชั่วโมง",
    difficulty: "เริ่มต้น",
    estimatedReadingTime: 120,
    sections: [
      {
        id: "1.1",
        title: "ประวัติและวิวัฒนาการของ AI ในฟิสิกส์",
        subtitle: "History and Evolution of AI in Physics",
        readingTime: 20,
        content: {
          overview: "การพัฒนาของปัญญาประดิษฐ์ในสาขาฟิสิกส์เริ่มต้นจากความต้องการในการแก้ปัญหาที่ซับซ้อนและการประมวลผลข้อมูลขนาดใหญ่",
          keyPoints: [
            "ยุค 1950s-1960s: การเริ่มต้นของคอมพิวเตอร์ในการคำนวณทางฟิสิกส์",
            "ยุค 1980s-1990s: การพัฒนาอัลกอริทึมการเรียนรู้สำหรับการวิเคราะห์ข้อมูล",
            "ยุค 2000s-2010s: การประยุกต์ใช้ Machine Learning ในฟิสิกส์อนุภาค",
            "ยุค 2010s-ปัจจุบัน: Deep Learning และ AI ในการค้นพบทางวิทยาศาสตร์"
          ],
          examples: [
            "การใช้ Neural Networks ในการวิเคราะห์ข้อมูลจาก Large Hadron Collider (LHC)",
            "การประยุกต์ใช้ AI ในการทำนายโครงสร้างโปรตีน (AlphaFold)",
            "การใช้ Machine Learning ในการค้นหาคลื่นความโน้มถ่วง (LIGO)"
          ]
        }
      },
      {
        id: "1.2",
        title: "ความท้าทายในฟิสิกส์ยุคใหม่",
        subtitle: "Modern Physics Challenges",
        readingTime: 25,
        content: {
          overview: "ฟิสิกส์สมัยใหม่เผชิญกับปัญหาที่ซับซ้อนและต้องการเครื่องมือใหม่ในการแก้ไข",
          keyPoints: [
            "Big Data และการจัดการข้อมูลขนาดใหญ่จากการทดลอง",
            "ความซับซ้อนของระบบหลายอนุภาค (Many-body systems)",
            "การจำลองระบบควอนตัมขนาดใหญ่",
            "การค้นหารูปแบบในข้อมูลที่มีสัญญาณรบกวนสูง"
          ],
          examples: [
            "การวิเคราะห์ข้อมูลจากกล้องโทรทรรศน์อวกาศ",
            "การจำลองพลาสมาในเครื่องปฏิกรณ์ฟิวชัน",
            "การทำนายสภาพอากาศและการเปลี่ยนแปลงสภาพภูมิอากาศ"
          ]
        }
      },
      {
        id: "1.3",
        title: "หลักการทางคณิตศาสตร์พื้นฐาน",
        subtitle: "Fundamental Mathematical Principles",
        readingTime: 30,
        content: {
          overview: "ทบทวนแนวคิดทางคณิตศาสตร์ที่สำคัญสำหรับการเข้าใจ AI ในฟิสิกส์",
          keyPoints: [
            "พีชคณิตเชิงเส้นและการประยุกต์ใช้ในฟิสิกส์",
            "แคลคูลัสและสมการเชิงอนุพันธ์",
            "ทฤษฎีความน่าจะเป็นและสถิติ",
            "การวิเคราะห์ฟูเรียร์และการประมวลผลสัญญาณ"
          ],
          examples: [
            "การใช้เมทริกซ์ในการแก้ระบบสมการเชิงเส้น",
            "การประยุกต์ใช้ Fourier Transform ในการวิเคราะห์สัญญาณ",
            "การใช้สถิติในการวิเคราะห์ข้อมูลการทดลอง"
          ]
        }
      },
      {
        id: "1.4",
        title: "พื้นฐานการเรียนรู้ของเครื่อง",
        subtitle: "Machine Learning Fundamentals",
        readingTime: 25,
        content: {
          overview: "แนวคิดพื้นฐานของ Machine Learning และการประยุกต์ใช้ในฟิสิกส์",
          keyPoints: [
            "ประเภทของการเรียนรู้: Supervised, Unsupervised, Reinforcement",
            "อัลกอริทึมพื้นฐาน: Linear Regression, Classification, Clustering",
            "การประเมินประสิทธิภาพของโมเดล",
            "Overfitting และ Underfitting"
          ],
          examples: [
            "การใช้ Linear Regression ในการวิเคราะห์ข้อมูลการทดลอง",
            "การจำแนกประเภทอนุภาคด้วย Classification algorithms",
            "การจัดกลุ่มข้อมูลด้วย K-means clustering"
          ]
        }
      },
      {
        id: "1.5",
        title: "การประยุกต์ใช้ AI ในฟิสิกส์",
        subtitle: "AI Applications in Physics",
        readingTime: 15,
        content: {
          overview: "ตัวอย่างการประยุกต์ใช้ AI ในสาขาฟิสิกส์ต่างๆ",
          keyPoints: [
            "ฟิสิกส์อนุภาคและการค้นหาอนุภาคใหม่",
            "ฟิสิกส์ของวัสดุและการออกแบบวัสดุใหม่",
            "ดาราศาสตร์และการค้นหาดาวเคราะห์นอกระบบ",
            "ฟิสิกส์พลาสมาและพลังงานฟิวชัน"
          ],
          examples: [
            "การใช้ Deep Learning ในการค้นหา Higgs boson",
            "การทำนายสมบัติของวัสดุด้วย AI",
            "การค้นหาดาวเคราะห์นอกระบบด้วย Machine Learning"
          ]
        }
      },
      {
        id: "1.6",
        title: "เครื่องมือและภาษาโปรแกรม",
        subtitle: "Tools and Programming Languages",
        readingTime: 15,
        content: {
          overview: "เครื่องมือและภาษาโปรแกรมที่สำคัญสำหรับ AI ในฟิสิกส์",
          keyPoints: [
            "Python และไลบรารีสำคัญ: NumPy, SciPy, Matplotlib",
            "Machine Learning frameworks: scikit-learn, TensorFlow, PyTorch",
            "เครื่องมือการจำลอง: MATLAB, Mathematica",
            "การใช้ High-Performance Computing (HPC)"
          ],
          examples: [
            "การใช้ NumPy ในการคำนวณเชิงตัวเลข",
            "การสร้างโมเดล Neural Network ด้วย TensorFlow",
            "การใช้ Matplotlib ในการแสดงผลข้อมูล"
          ]
        }
      }
    ],
    quiz: {
      questions: [
        {
          id: 1,
          question: "ปัจจัยใดที่เป็นแรงผลักดันหลักในการนำ AI มาใช้ในฟิสิกส์ยุคใหม่?",
          options: [
            "ความต้องการในการลดต้นทุนการวิจัย",
            "Big Data และความซับซ้อนของระบบ",
            "การแข่งขันระหว่างประเทศ",
            "ความต้องการในการเผยแพร่งานวิจัย"
          ],
          correct: 1,
          explanation: "Big Data และความซับซ้อนของระบบเป็นแรงผลักดันหลักที่ทำให้ฟิสิกส์ยุคใหม่ต้องการเครื่องมือ AI เพื่อจัดการและวิเคราะห์ข้อมูลขนาดใหญ่และระบบที่ซับซ้อน"
        },
        {
          id: 2,
          question: "ประเภทการเรียนรู้ใดที่เหมาะสมสำหรับการจำแนกประเภทอนุภาคในฟิสิกส์อนุภาค?",
          options: [
            "Unsupervised Learning",
            "Supervised Learning", 
            "Reinforcement Learning",
            "Semi-supervised Learning"
          ],
          correct: 1,
          explanation: "Supervised Learning เหมาะสมสำหรับการจำแนกประเภทอนุภาค เพราะเรามีข้อมูลที่มีป้ายกำกับ (labeled data) ของอนุภาคแต่ละประเภทเพื่อฝึกโมเดล"
        },
        {
          id: 3,
          question: "ไลบรารีใดใน Python ที่เป็นพื้นฐานสำคัญสำหรับการคำนวณเชิงตัวเลขในฟิสิกส์?",
          options: [
            "Pandas",
            "NumPy",
            "Requests", 
            "Beautiful Soup"
          ],
          correct: 1,
          explanation: "NumPy เป็นไลบรารีพื้นฐานที่สำคัญที่สุดสำหรับการคำนวณเชิงตัวเลขใน Python โดยเฉพาะในสาขาฟิสิกส์ เพราะให้การสนับสนุนอาร์เรย์หลายมิติและฟังก์ชันทางคณิตศาสตร์"
        }
      ]
    }
  }

  // Code examples for the chapter
  const codeExamples = [
    {
      title: "Basic NumPy Operations",
      code: `import numpy as np
import matplotlib.pyplot as plt

# สร้างข้อมูลตัวอย่างสำหรับการทดลองฟิสิกส์
time = np.linspace(0, 10, 1000)  # เวลา 0-10 วินาที
frequency = 2.0  # ความถี่ 2 Hz
amplitude = 1.0  # แอมพลิจูด

# สร้างสัญญาณไซน์
signal = amplitude * np.sin(2 * np.pi * frequency * time)

# คำนวณค่าสถิติพื้นฐาน
mean_value = np.mean(signal)
std_value = np.std(signal)
max_value = np.max(signal)

print("Fixed f-string")
print("Fixed f-string")
print("Fixed f-string")

# การใช้ NumPy ในการคำนวณทางฟิสิกส์
print("\\nตัวอย่างการคำนวณทางฟิสิกส์:")
print("พลังงานจลน์ = 1/2 * m * v²")
mass = 2.0  # kg
velocity = np.array([10, 15, 20, 25])  # m/s
kinetic_energy = 0.5 * mass * velocity**2
print("Fixed f-string")`
    },
    {
      title: "Linear Regression for Physics Data",
      code: `import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# สร้างข้อมูลการทดลองฟิสิกส์ (ความสัมพันธ์เชิงเส้น)
# ตัวอย่าง: กฎของฮุก F = kx
displacement = np.linspace(0, 0.1, 50)  # การเคลื่อนที่ (m)
spring_constant = 100  # ค่าคงที่ของสปริง (N/m)

# เพิ่มสัญญาณรบกวนเพื่อจำลองข้อมูลจริง
noise = np.random.normal(0, 0.5, len(displacement))
force = spring_constant * displacement + noise

# ใช้ Linear Regression เพื่อหาค่าคงที่ของสปริง
X = displacement.reshape(-1, 1)
y = force

model = LinearRegression()
model.fit(X, y)

# ทำนายและคำนวณค่าคงที่ของสปริง
predicted_force = model.predict(X)
estimated_k = model.coef_[0]

print("Fixed f-string")
print("Fixed f-string")
print("Fixed f-string")

# คำนวณ R-squared
r_squared = model.score(X, y)
print("Fixed f-string")`
    },
    {
      title: "Fourier Analysis for Signal Processing",
      code: `import numpy as np
import matplotlib.pyplot as plt

# สร้างสัญญาณที่ประกอบด้วยหลายความถี่
sampling_rate = 1000  # Hz
duration = 2.0  # วินาที
t = np.linspace(0, duration, int(sampling_rate * duration))

# สร้างสัญญาณผสม
freq1, freq2, freq3 = 50, 120, 200  # Hz
signal = (np.sin(2 * np.pi * freq1 * t) + 
          0.5 * np.sin(2 * np.pi * freq2 * t) + 
          0.3 * np.sin(2 * np.pi * freq3 * t))

# เพิ่มสัญญาณรบกวน
noise = 0.1 * np.random.normal(0, 1, len(t))
noisy_signal = signal + noise

# ทำ Fourier Transform
fft_result = np.fft.fft(noisy_signal)
frequencies = np.fft.fftfreq(len(t), 1/sampling_rate)

# คำนวณ magnitude spectrum
magnitude = np.abs(fft_result)

# หาความถี่ที่มีแอมพลิจูดสูงสุด
positive_freq_idx = frequencies > 0
positive_frequencies = frequencies[positive_freq_idx]
positive_magnitude = magnitude[positive_freq_idx]

# หาจุดสูงสุด 3 จุดแรก
peak_indices = np.argsort(positive_magnitude)[-3:]
detected_frequencies = positive_frequencies[peak_indices]

print("ความถี่ที่ตรวจพบ:")
for i, freq in enumerate(sorted(detected_frequencies)):
    print("Fixed f-string")

print("Fixed f-string")`
    }
  ]

  // Toggle section expansion
  const toggleSection = (sectionId) => {
    setExpandedSections(prev => ({
      ...prev,
      [sectionId]: !prev[sectionId]
    }))
  }

  // Mark section as completed
  const markSectionCompleted = (sectionId) => {
    setCompletedSections(prev => new Set([...prev, sectionId]))
  }

  // Calculate progress
  useEffect(() => {
    const totalSections = chapterData.sections.length
    const completed = completedSections.size
    setChapterProgress((completed / totalSections) * 100)
  }, [completedSections])

  // Handle quiz submission
  const handleQuizSubmit = () => {
    let correct = 0
    chapterData.quiz.questions.forEach(question => {
      if (quizAnswers[question.id] === question.correct) {
        correct++
      }
    })
    setQuizScore((correct / chapterData.quiz.questions.length) * 100)
    setQuizSubmitted(true)
  }

  const handleQuizAnswer = (questionId, answerIndex) => {
    setQuizAnswers(prev => ({
      ...prev,
      [questionId]: answerIndex
    }))
  }

  return (
    <motion.div
      initial={{ opacity: 0, y: 20 }}
      animate={{ opacity: 1, y: 0 }}
      transition={{ duration: 0.5 }}
      className="max-w-6xl mx-auto space-y-8"
    >
      {/* Chapter Header */}
      <Card className="bg-gradient-to-r from-orange-600 to-red-600 text-white border-0 holo-card holo-glow">
        <CardContent className="p-8">
          <div className="flex items-start justify-between">
            <div className="flex-1">
              <div className="flex items-center space-x-3 mb-4">
                <div className="p-3 bg-white/20 rounded-lg">
                  <BookOpen className="h-8 w-8" />
                </div>
                <div>
                  <Badge className="bg-white/20 text-white border-white/30 mb-2">
                    บทที่ {chapterData.id} • {chapterData.difficulty}
                  </Badge>
                  <h1 className="text-3xl font-bold mb-2 holo-heading">{chapterData.title}</h1>
                  <p className="text-xl opacity-90 holo-subtitle">{chapterData.subtitle}</p>
                </div>
              </div>
              <p className="text-lg opacity-80 mb-6 holo-body">{chapterData.description}</p>
              
              <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
                <div className="flex items-center space-x-2">
                  <Clock className="h-5 w-5" />
                  <span>ระยะเวลา: {chapterData.duration}</span>
                </div>
                <div className="flex items-center space-x-2">
                  <Target className="h-5 w-5" />
                  <span>หัวข้อ: {chapterData.sections.length} หัวข้อ</span>
                </div>
                <div className="flex items-center space-x-2">
                  <CheckCircle className="h-5 w-5" />
                  <span>เสร็จแล้ว: {completedSections.size}/{chapterData.sections.length}</span>
                </div>
              </div>
            </div>
            
            <div className="ml-8">
              <div className="text-center">
                <div className="text-3xl font-bold mb-2">{Math.round(chapterProgress)}%</div>
                <div className="text-sm opacity-80">ความคืบหน้า</div>
                <Progress value={chapterProgress} className="w-24 h-2 mt-2 holo-progress" />
              </div>
            </div>
          </div>
        </CardContent>
      </Card>

      {/* Main Content Tabs */}
      <Tabs defaultValue="content" className="w-full">
        <TabsList className="grid w-full grid-cols-4 holo-tabs">
          <TabsTrigger value="content" className="holo-tab">เนื้อหา</TabsTrigger>
          <TabsTrigger value="interactive" className="holo-tab">การจำลอง</TabsTrigger>
          <TabsTrigger value="code" className="holo-tab">โค้ดตัวอย่าง</TabsTrigger>
          <TabsTrigger value="quiz" className="holo-tab">แบบทดสอบ</TabsTrigger>
        </TabsList>

        {/* Content Tab */}
        <TabsContent value="content" className="mt-6">
          <div className="space-y-6">
            {chapterData.sections.map((section, index) => (
              <motion.div
                key={section.id}
                initial={{ opacity: 0, y: 20 }}
                animate={{ opacity: 1, y: 0 }}
                transition={{ delay: index * 0.1 }}
              >
                <Card className={`border-2 holo-card ${
                  completedSections.has(section.id) 
                    ? 'border-green-300 bg-green-50 dark:bg-green-900/10' 
                    : 'border-orange-200 dark:border-orange-700'
                }`}>
                  <CardHeader 
                    className="cursor-pointer hover:bg-gray-50 dark:hover:bg-gray-800/50"
                    onClick={() => toggleSection(section.id)}
                  >
                    <div className="flex items-center justify-between">
                      <div className="flex items-center space-x-4">
                        <div className={`p-2 rounded-lg holo-glow ${
                          completedSections.has(section.id)
                            ? 'bg-green-600 text-white'
                            : 'bg-orange-600 text-white'
                        }`}>
                          {completedSections.has(section.id) ? (
                            <CheckCircle className="h-5 w-5" />
                          ) : (
                            <span className="text-sm font-bold">{section.id}</span>
                          )}
                        </div>
                        <div>
                          <CardTitle className="text-lg holo-accent">{section.title}</CardTitle>
                          <p className="text-sm text-gray-600 dark:text-gray-400 mt-1">
                            {section.subtitle} • {section.readingTime} นาที
                          </p>
                        </div>
                      </div>
                      <div className="flex items-center space-x-2">
                        {!completedSections.has(section.id) && (
                          <Button
                            size="sm"
                            onClick={(e) => {
                              e.stopPropagation()
                              markSectionCompleted(section.id)
                            }}
                            className="holo-button"
                          >
                            ทำเครื่องหมายเสร็จ
                          </Button>
                        )}
                        {expandedSections[section.id] ? (
                          <ChevronDown className="h-5 w-5" />
                        ) : (
                          <ChevronRight className="h-5 w-5" />
                        )}
                      </div>
                    </div>
                  </CardHeader>
                  
                  <AnimatePresence>
                    {expandedSections[section.id] && (
                      <motion.div
                        initial={{ height: 0, opacity: 0 }}
                        animate={{ height: "auto", opacity: 1 }}
                        exit={{ height: 0, opacity: 0 }}
                        transition={{ duration: 0.3 }}
                      >
                        <CardContent className="pt-0">
                          <div className="space-y-6">
                            {/* Overview */}
                            <div>
                              <h4 className="font-semibold text-orange-700 dark:text-orange-300 mb-3 holo-accent">
                                ภาพรวม
                              </h4>
                              <p className="text-gray-700 dark:text-gray-300 leading-relaxed">
                                {section.content.overview}
                              </p>
                            </div>

                            {/* Key Points */}
                            <div>
                              <h4 className="font-semibold text-orange-700 dark:text-orange-300 mb-3 holo-accent">
                                ประเด็นสำคัญ
                              </h4>
                              <div className="grid grid-cols-1 md:grid-cols-2 gap-3">
                                {section.content.keyPoints.map((point, idx) => (
                                  <div key={idx} className="flex items-start space-x-3 p-3 bg-orange-50 dark:bg-orange-900/20 rounded-lg holo-card">
                                    <div className="w-2 h-2 bg-orange-600 rounded-full mt-2 flex-shrink-0 holo-glow" />
                                    <span className="text-sm text-gray-700 dark:text-gray-300">
                                      {point}
                                    </span>
                                  </div>
                                ))}
                              </div>
                            </div>

                            {/* Examples */}
                            <div>
                              <h4 className="font-semibold text-orange-700 dark:text-orange-300 mb-3 holo-accent">
                                ตัวอย่างการประยุกต์ใช้
                              </h4>
                              <div className="space-y-3">
                                {section.content.examples.map((example, idx) => (
                                  <div key={idx} className="p-4 bg-green-50 dark:bg-green-900/20 rounded-lg border-l-4 border-green-500 holo-card">
                                    <p className="text-sm text-gray-700 dark:text-gray-300">
                                      {example}
                                    </p>
                                  </div>
                                ))}
                              </div>
                            </div>
                          </div>
                        </CardContent>
                      </motion.div>
                    )}
                  </AnimatePresence>
                </Card>
              </motion.div>
            ))}
          </div>
        </TabsContent>

        {/* Interactive Simulations Tab */}
        <TabsContent value="interactive" className="mt-6">
          <div className="space-y-8">
            <div className="text-center">
              <h2 className="text-2xl font-bold text-orange-700 dark:text-orange-300 mb-2 holo-heading">
                การจำลองแบบโต้ตอบ
              </h2>
              <p className="text-gray-600 dark:text-gray-400">
                ทดลองกับการจำลองทางฟิสิกส์เพื่อเข้าใจแนวคิดพื้นฐาน
              </p>
            </div>

            <InteractiveSimulation
              title="การจำลองคลื่นไซน์พื้นฐาน"
              description="ศึกษาพฤติกรรมของคลื่นไซน์และการเปลี่ยนแปลงพารามิเตอร์"
              type="wave"
              parameters={{ amplitude: 1, frequency: 1, speed: 1 }}
            />

            <InteractiveSimulation
              title="การจำลองระบบอนุภาค"
              description="ดูการเคลื่อนที่ของอนุภาคในระบบง่ายๆ"
              type="particle"
              parameters={{ particles: 20, speed: 1.5 }}
            />
          </div>
        </TabsContent>

        {/* Code Examples Tab */}
        <TabsContent value="code" className="mt-6">
          <div className="space-y-8">
            <div className="text-center">
              <h2 className="text-2xl font-bold text-gray-800 dark:text-gray-200 mb-2">
                ตัวอย่างโค้ด Python
              </h2>
              <p className="text-gray-600 dark:text-gray-400">
                ลองเขียนและรันโค้ด Python สำหรับการคำนวณทางฟิสิกส์
              </p>
            </div>

            <CodePlayground
              title="Python สำหรับฟิสิกส์ - บทที่ 1"
              description="ตัวอย่างการใช้ Python ในการคำนวณและวิเคราะห์ข้อมูลทางฟิสิกส์"
              initialCode={codeExamples[0].code}
              examples={codeExamples}
            />
          </div>
        </TabsContent>

        {/* Quiz Tab */}
        <TabsContent value="quiz" className="mt-6">
          <div className="space-y-6">
            <div className="text-center">
              <h2 className="text-2xl font-bold text-gray-800 dark:text-gray-200 mb-2">
                แบบทดสอบบทที่ 1
              </h2>
              <p className="text-gray-600 dark:text-gray-400">
                ทดสอบความเข้าใจในเนื้อหาที่เรียนมา
              </p>
            </div>

            <Card>
              <CardContent className="p-6">
                <div className="space-y-8">
                  {chapterData.quiz.questions.map((question, index) => (
                    <div key={question.id} className="space-y-4">
                      <h3 className="text-lg font-semibold text-gray-800 dark:text-gray-200">
                        {index + 1}. {question.question}
                      </h3>
                      
                      <div className="space-y-2">
                        {question.options.map((option, optionIndex) => (
                          <label
                            key={optionIndex}
                            className={`flex items-center space-x-3 p-3 rounded-lg cursor-pointer transition-colors ${
                              quizAnswers[question.id] === optionIndex
                                ? 'bg-blue-100 dark:bg-blue-900/30 border-2 border-blue-500'
                                : 'bg-gray-50 dark:bg-gray-800 hover:bg-gray-100 dark:hover:bg-gray-700 border-2 border-transparent'
                            }`}
                          >
                            <input
                              type="radio"
                              name={`question-${question.id}`}
                              value={optionIndex}
                              checked={quizAnswers[question.id] === optionIndex}
                              onChange={() => handleQuizAnswer(question.id, optionIndex)}
                              className="text-blue-600"
                            />
                            <span className="text-gray-700 dark:text-gray-300">
                              {option}
                            </span>
                          </label>
                        ))}
                      </div>

                      {quizSubmitted && (
                        <motion.div
                          initial={{ opacity: 0, y: 10 }}
                          animate={{ opacity: 1, y: 0 }}
                          className={`p-4 rounded-lg ${
                            quizAnswers[question.id] === question.correct
                              ? 'bg-green-100 dark:bg-green-900/30 border border-green-500'
                              : 'bg-red-100 dark:bg-red-900/30 border border-red-500'
                          }`}
                        >
                          <div className="flex items-start space-x-2">
                            {quizAnswers[question.id] === question.correct ? (
                              <CheckCircle className="h-5 w-5 text-green-600 mt-0.5" />
                            ) : (
                              <div className="h-5 w-5 rounded-full bg-red-600 flex items-center justify-center mt-0.5">
                                <span className="text-white text-xs">✕</span>
                              </div>
                            )}
                            <div>
                              <p className="font-medium text-gray-800 dark:text-gray-200">
                                {quizAnswers[question.id] === question.correct ? 'ถูกต้อง!' : 'ไม่ถูกต้อง'}
                              </p>
                              <p className="text-sm text-gray-600 dark:text-gray-400 mt-1">
                                {question.explanation}
                              </p>
                            </div>
                          </div>
                        </motion.div>
                      )}
                    </div>
                  ))}

                  {!quizSubmitted ? (
                    <div className="text-center">
                      <Button
                        onClick={handleQuizSubmit}
                        disabled={Object.keys(quizAnswers).length < chapterData.quiz.questions.length}
                        className="bg-blue-600 hover:bg-blue-700 text-white px-8 py-2"
                      >
                        ส่งคำตอบ
                      </Button>
                    </div>
                  ) : (
                    <motion.div
                      initial={{ opacity: 0, scale: 0.9 }}
                      animate={{ opacity: 1, scale: 1 }}
                      className="text-center p-6 bg-gradient-to-r from-blue-50 to-indigo-50 dark:from-blue-900/20 dark:to-indigo-900/20 rounded-lg"
                    >
                      <div className="text-4xl font-bold text-blue-600 mb-2">
                        {Math.round(quizScore)}%
                      </div>
                      <p className="text-lg text-gray-700 dark:text-gray-300 mb-4">
                        คะแนนของคุณ
                      </p>
                      <Badge className={`${
                        quizScore >= 80 ? 'bg-green-600' : 
                        quizScore >= 60 ? 'bg-yellow-600' : 'bg-red-600'
                      } text-white`}>
                        {quizScore >= 80 ? 'ยอดเยี่ยม' : 
                         quizScore >= 60 ? 'ดี' : 'ต้องปรับปรุง'}
                      </Badge>
                    </motion.div>
                  )}
                </div>
              </CardContent>
            </Card>
          </div>
        </TabsContent>
      </Tabs>

      {/* Navigation */}
      <Card>
        <CardContent className="p-6">
          <div className="flex items-center justify-between">
            <Button variant="outline" disabled>
              <ArrowLeft className="h-4 w-4 mr-2" />
              บทก่อนหน้า
            </Button>
            
            <div className="flex items-center space-x-4">
              <Button variant="outline">
                <Download className="h-4 w-4 mr-2" />
                ดาวน์โหลด PDF
              </Button>
              <Badge variant="secondary">
                บทที่ 1 จาก 9
              </Badge>
            </div>
            
            <Button>
              บทถัดไป
              <ArrowRight className="h-4 w-4 ml-2" />
            </Button>
          </div>
        </CardContent>
      </Card>
    </motion.div>
  )
}

export default Chapter1Enhanced
