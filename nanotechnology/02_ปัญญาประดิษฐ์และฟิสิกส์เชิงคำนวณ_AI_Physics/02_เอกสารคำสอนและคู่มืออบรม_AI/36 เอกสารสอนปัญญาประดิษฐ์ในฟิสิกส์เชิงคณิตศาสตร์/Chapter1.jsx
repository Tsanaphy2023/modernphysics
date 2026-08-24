import { useState, useEffect } from 'react'
import { motion, AnimatePresence } from 'framer-motion'
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from '@/components/ui/card.jsx'
import { Button } from '@/components/ui/button.jsx'
import { Badge } from '@/components/ui/badge.jsx'
import { Progress } from '@/components/ui/progress.jsx'
import { Tabs, TabsContent, TabsList, TabsTrigger } from '@/components/ui/tabs.jsx'
import { 
  BookOpen, 
  ChevronDown, 
  ChevronUp, 
  Play, 
  Pause, 
  RotateCcw,
  Lightbulb,
  Target,
  Clock,
  CheckCircle,
  Circle,
  ArrowRight,
  Brain,
  Atom,
  Zap,
  TrendingUp
} from 'lucide-react'

// Import chapter image
import aiPhysicsOverview from '../assets/ai_physics_course_images/chapter1/ai_physics_overview.png'
import aiPhysicsIntro from '../assets/ai_physics_course_images/chapter1/ai_physics_intro.png'
import bigDataPhysics from '../assets/ai_physics_course_images/chapter1/big_data_physics.png'
import mlToolsPhysics from '../assets/ai_physics_course_images/chapter1/ml_tools_physics.png'

const Chapter1 = () => {
  const [expandedSections, setExpandedSections] = useState(new Set(['1.1']))
  const [completedSections, setCompletedSections] = useState(new Set())
  const [currentSection, setCurrentSection] = useState('1.1')
  const [progress, setProgress] = useState(0)
  const [quizAnswers, setQuizAnswers] = useState({})
  const [showQuizResults, setShowQuizResults] = useState(false)

  const chapterData = {
    id: 1,
    title: "บทนำสู่ปัญญาประดิษฐ์และฟิสิกส์เชิงคณิตศาสตร์",
    subtitle: "Introduction to AI and Mathematical Physics",
    duration: "2 ชั่วโมง",
    difficulty: "เริ่มต้น",
    objectives: [
      "เข้าใจภาพรวมและความสำคัญของการบูรณาการ AI ในงานวิจัยฟิสิกส์",
      "ทบทวนแนวคิดหลักทางฟิสิกส์เชิงคณิตศาสตร์ที่เกี่ยวข้อง",
      "เข้าใจประวัติศาสตร์และวิวัฒนาการของ AI ในวิทยาศาสตร์"
    ],
    sections: [
      {
        id: '1.1',
        title: 'ประวัติและวิวัฒนาการของปัญญาประดิษฐ์ในวิทยาศาสตร์กายภาพ',
        content: `ปัญญาประดิษฐ์ (Artificial Intelligence) ได้เข้ามามีบทบาทสำคัญในวิทยาศาสตร์กายภาพตั้งแต่ทศวรรษ 1950 เมื่อนักวิทยาศาสตร์เริ่มใช้คอมพิวเตอร์ในการคำนวณปัญหาทางฟิสิกส์ที่ซับซ้อน

การพัฒนาที่สำคัญในประวัติศาสตร์:
• 1950s: การใช้คอมพิวเตอร์ในการจำลองมอนติคาร์โล
• 1960s: การพัฒนาอัลกอริทึมการหาค่าเหมาะสมที่สุด
• 1980s: การประยุกต์ใช้โครงข่ายประสาทเทียมในฟิสิกส์
• 2000s: การเริ่มต้นของ Machine Learning ในการวิเคราะห์ข้อมูลฟิสิกส์
• 2010s: Deep Learning และการปฏิวัติในการประมวลผลข้อมูลขนาดใหญ่

ในปัจจุบัน AI ได้กลายเป็นเครื่องมือที่ขาดไม่ได้สำหรับนักฟิสิกส์ในการ:
- วิเคราะห์ข้อมูลจากการทดลองขนาดใหญ่
- ค้นพบรูปแบบใหม่ในข้อมูล
- ทำนายพฤติกรรมของระบบที่ซับซ้อน
- ออกแบบการทดลองอัตโนมัติ`,
        image: aiPhysicsIntro,
        estimatedTime: 15
      },
      {
        id: '1.2',
        title: 'ความท้าทายในฟิสิกส์ยุคใหม่: ข้อมูลขนาดใหญ่และความซับซ้อนของระบบ',
        content: `ฟิสิกส์ในศตวรรษที่ 21 เผชิญกับความท้าทายใหม่ที่ต้องการเครื่องมือที่ทันสมัยในการแก้ปัญหา:

**ข้อมูลขนาดใหญ่ (Big Data):**
- Large Hadron Collider (LHC) ผลิตข้อมูล 50 petabytes ต่อปี
- กล้องโทรทรรศน์อวกาศสร้างข้อมูลภาพหลายล้านภาพต่อวัน
- การจำลองพลศาสตร์โมเลกุลสร้างข้อมูลระดับ terabytes

**ความซับซ้อนของระบบ:**
- ระบบหลายอนุภาค (Many-body systems)
- ปรากฏการณ์ที่เกิดขึ้น (Emergent phenomena)
- ระบบไม่เชิงเส้น (Nonlinear systems)
- ระบบควอนตัมที่มีการพันกัน (Quantum entanglement)

**ข้อจำกัดของวิธีการดั้งเดิม:**
- การคำนวณแบบวิเคราะห์ (Analytical methods) มีข้อจำกัดในระบบซับซ้อน
- การจำลองเชิงตัวเลข (Numerical simulations) ต้องการทรัพยากรคำนวณมาก
- การวิเคราะห์ข้อมูลแบบดั้งเดิมไม่สามารถจัดการกับข้อมูลขนาดใหญ่ได้

AI และ Machine Learning เสนอแนวทางใหม่ในการ:
- ประมวลผลข้อมูลขนาดใหญ่อย่างมีประสิทธิภาพ
- ค้นหารูปแบบที่ซ่อนอยู่ในข้อมูล
- สร้างแบบจำลองที่สามารถจับความซับซ้อนของระบบได้
- ทำนายพฤติกรรมของระบบโดยไม่ต้องเข้าใจกลไกทั้งหมด`,
        image: bigDataPhysics,
        estimatedTime: 20
      },
      {
        id: '1.3',
        title: 'ทบทวนหลักคณิตศาสตร์พื้นฐาน: พีชคณิตเชิงเส้น แคลคูลัสเวกเตอร์ และความน่าจะเป็น',
        content: `ก่อนที่จะเข้าสู่การศึกษา AI ในฟิสิกส์ เราต้องทบทวนหลักคณิตศาสตร์พื้นฐานที่จำเป็น:

**พีชคณิตเชิงเส้น (Linear Algebra):**
- เวกเตอร์และการดำเนินการเวกเตอร์
- เมทริกซ์และการคูณเมทริกซ์
- ค่าลักษณะเฉพาะ (Eigenvalues) และเวกเตอร์ลักษณะเฉพาะ (Eigenvectors)
- การแยกค่าเอกพจน์ (Singular Value Decomposition)

**แคลคูลัสเวกเตอร์:**
- การหาอนุพันธ์ย่อย (Partial derivatives)
- เกรเดียนต์ (Gradient)
- การหาค่าเหมาะสมที่สุด (Optimization)
- กฎลูกโซ่ (Chain rule) สำหรับฟังก์ชันหลายตัวแปร

**ทฤษฎีความน่าจะเป็นและสถิติ:**
- การแจกแจงความน่าจะเป็น (Probability distributions)
- ทฤษฎีบทเบย์ส (Bayes' theorem)
- การประมาณค่าพารามิเตอร์ (Parameter estimation)
- การทดสอบสมมติฐาน (Hypothesis testing)

**การประยุกต์ใช้ในฟิสิกส์:**
- สมการชเรอดิงเงอร์เป็นปัญหาค่าลักษณะเฉพาะ
- การหาค่าเหมาะสมที่สุดในการฟิตข้อมูล
- ความไม่แน่นอนในการวัดและการประมาณค่า
- การจำลองมอนติคาร์โลใช้ทฤษฎีความน่าจะเป็น`,
        estimatedTime: 25
      },
      {
        id: '1.4',
        title: 'แนวคิดพื้นฐานของการเรียนรู้ของเครื่อง: ข้อมูล แบบจำลอง และการทำนาย',
        content: `Machine Learning เป็นสาขาหนึ่งของ AI ที่เน้นการสร้างระบบที่สามารถเรียนรู้จากข้อมูลได้:

**องค์ประกอบหลักของ Machine Learning:**

1. **ข้อมูล (Data):**
   - ข้อมูลฝึก (Training data)
   - ข้อมูลทดสอบ (Test data)
   - คุณลักษณะ (Features)
   - ป้ายกำกับ (Labels) - สำหรับ Supervised Learning

2. **แบบจำลอง (Model):**
   - ฟังก์ชันทางคณิตศาสตร์ที่เชื่อมโยงข้อมูลเข้ากับผลลัพธ์
   - พารามิเตอร์ที่ปรับได้ (Learnable parameters)
   - สถาปัตยกรรมของแบบจำลอง (Model architecture)

3. **การทำนาย (Prediction):**
   - การใช้แบบจำลองที่ฝึกแล้วกับข้อมูลใหม่
   - การประเมินความแม่นยำ
   - การวัดความไม่แน่นอน

**ประเภทของ Machine Learning:**
- **Supervised Learning:** เรียนรู้จากข้อมูลที่มีป้ายกำกับ
- **Unsupervised Learning:** ค้นหารูปแบบในข้อมูลที่ไม่มีป้ายกำกับ
- **Reinforcement Learning:** เรียนรู้ผ่านการโต้ตอบกับสภาพแวดล้อม

**การประยุกต์ใช้ในฟิสิกส์:**
- การจำแนกอนุภาคในฟิสิกส์อนุภาค
- การทำนายคุณสมบัติของวัสดุ
- การค้นหาเฟสใหม่ของสสาร
- การควบคุมระบบควอนตัม`,
        estimatedTime: 30
      },
      {
        id: '1.5',
        title: 'การประยุกต์ใช้ AI ในสาขาฟิสิกส์ต่างๆ: ภาพรวมและตัวอย่าง',
        content: `AI ได้ถูกนำไปประยุกต์ใช้ในสาขาฟิสิกส์หลากหลาย:

**ฟิสิกส์อนุภาค (Particle Physics):**
- การค้นพบฮิกส์โบซอนที่ CERN ใช้ Machine Learning
- การจำแนกเหตุการณ์การชนกันของอนุภาค
- การปรับปรุงประสิทธิภาพของเครื่องตรวจจับ

**ดาราศาสตร์และฟิสิกส์อวกาศ:**
- การค้นหาดาวเคราะห์นอกระบบด้วย Deep Learning
- การจำแนกประเภทของกาแล็กซี
- การตรวจจับคลื่นความโน้มถ่วง

**ฟิสิกส์สสารควบแน่น:**
- การค้นหาเฟสใหม่ของสสาร
- การทำนายคุณสมบัติของวัสดุ 2D
- การศึกษาการเปลี่ยนเฟส

**ฟิสิกส์ควอนตัม:**
- การควบคุมระบบควอนตัม
- การปรับปรุงอัลกอริทึมควอนตัม
- การจำลองระบบควอนตัมหลายอนุภาค

**ฟิสิกส์พลาสมาและฟิวชัน:**
- การควบคุมพลาสมาในเครื่องปฏิกรณ์ฟิวชัน
- การทำนายการเกิด disruption
- การปรับปรุงประสิทธิภาพการกักเก็บ

**ตัวอย่างความสำเร็จที่โดดเด่น:**
1. **AlphaFold:** ทำนายโครงสร้างโปรตีนด้วยความแม่นยำสูง
2. **DeepMind for Fusion:** ควบคุมพลาสมาในโทคาแมค
3. **Kepler Space Telescope:** ค้นพบดาวเคราะห์นอกระบบหลายพันดวง`,
        image: mlToolsPhysics,
        estimatedTime: 25
      },
      {
        id: '1.6',
        title: 'เครื่องมือและภาษาโปรแกรมสำหรับ AI ในฟิสิกส์',
        content: `การเรียนรู้ AI ในฟิสิกส์ต้องการเครื่องมือและภาษาโปรแกรมที่เหมาะสม:

**ภาษาโปรแกรมหลัก:**

**Python:**
- ภาษาที่ได้รับความนิยมสูงสุดสำหรับ AI และ Data Science
- มีไลบรารีที่หลากหลายและชุมชนที่แข็งแกร่ง
- เรียนรู้ง่ายและมีความยืดหยุ่นสูง

**ไลบรารีสำคัญ:**
- **NumPy:** การคำนวณเชิงตัวเลขพื้นฐาน
- **SciPy:** ฟังก์ชันทางวิทยาศาสตร์ขั้นสูง
- **Matplotlib/Plotly:** การสร้างกราฟและการแสดงผล
- **Pandas:** การจัดการและวิเคราะห์ข้อมูล
- **Scikit-learn:** Machine Learning แบบดั้งเดิม
- **TensorFlow/PyTorch:** Deep Learning frameworks
- **JAX:** การคำนวณที่เร็วและการหาอนุพันธ์อัตโนมัติ

**เครื่องมือเฉพาะทางฟิสิกส์:**
- **QuTiP:** Quantum Toolbox in Python
- **PennyLane:** Quantum Machine Learning
- **MDAnalysis:** การวิเคราะห์พลศาสตร์โมเลกุล
- **Astropy:** ดาราศาสตร์และฟิสิกส์อวกาศ

**สภาพแวดล้อมการพัฒนา:**
- **Jupyter Notebook:** สำหรับการทดลองและการนำเสนอ
- **Google Colab:** การคำนวณบนคลาวด์ฟรี
- **VS Code:** IDE ที่ทันสมัยและมีประสิทธิภาพ

**ทรัพยากรการคำนวณ:**
- **GPU Computing:** สำหรับ Deep Learning
- **High-Performance Computing (HPC):** สำหรับการจำลองขนาดใหญ่
- **Cloud Computing:** AWS, Google Cloud, Azure`,
        estimatedTime: 20
      }
    ],
    quiz: [
      {
        id: 'q1',
        question: 'ข้อใดต่อไปนี้เป็นความท้าทายหลักของฟิสิกส์ในศตวรรษที่ 21?',
        options: [
          'การขาดแคลนนักวิทยาศาสตร์',
          'ข้อมูลขนาดใหญ่และความซับซ้อนของระบบ',
          'การขาดแคลนงบประมาณวิจัย',
          'การขาดเครื่องมือการทดลอง'
        ],
        correct: 1,
        explanation: 'ฟิสิกส์สมัยใหม่เผชิญกับข้อมูลขนาดใหญ่จากการทดลองและการจำลอง รวมถึงระบบที่มีความซับซ้อนสูงที่ต้องการเครื่องมือใหม่ในการวิเคราะห์'
      },
      {
        id: 'q2',
        question: 'ประเภทของ Machine Learning ใดที่เหมาะสมสำหรับการจำแนกอนุภาคในฟิสิกส์อนุภาค?',
        options: [
          'Unsupervised Learning',
          'Reinforcement Learning',
          'Supervised Learning',
          'Semi-supervised Learning'
        ],
        correct: 2,
        explanation: 'การจำแนกอนุภาคต้องการข้อมูลที่มีป้ายกำกับ (labeled data) เพื่อฝึกแบบจำลองให้รู้จักแต่ละประเภทของอนุภาค ซึ่งเป็นลักษณะของ Supervised Learning'
      },
      {
        id: 'q3',
        question: 'ไลบรารี Python ใดที่เหมาะสมที่สุดสำหรับการคำนวณเชิงตัวเลขพื้นฐานในฟิสิกส์?',
        options: [
          'Pandas',
          'Matplotlib',
          'NumPy',
          'Scikit-learn'
        ],
        correct: 2,
        explanation: 'NumPy เป็นไลบรารีพื้นฐานสำหรับการคำนวณเชิงตัวเลขใน Python ที่ให้การสนับสนุนสำหรับอาร์เรย์หลายมิติและฟังก์ชันทางคณิตศาสตร์'
      }
    ]
  }

  // Calculate progress based on completed sections
  useEffect(() => {
    const totalSections = chapterData.sections.length
    const completed = completedSections.size
    setProgress((completed / totalSections) * 100)
  }, [completedSections])

  const toggleSection = (sectionId) => {
    const newExpanded = new Set(expandedSections)
    if (newExpanded.has(sectionId)) {
      newExpanded.delete(sectionId)
    } else {
      newExpanded.add(sectionId)
    }
    setExpandedSections(newExpanded)
  }

  const markSectionComplete = (sectionId) => {
    const newCompleted = new Set(completedSections)
    newCompleted.add(sectionId)
    setCompletedSections(newCompleted)
  }

  const handleQuizAnswer = (questionId, answerIndex) => {
    setQuizAnswers(prev => ({
      ...prev,
      [questionId]: answerIndex
    }))
  }

  const submitQuiz = () => {
    setShowQuizResults(true)
  }

  const getQuizScore = () => {
    let correct = 0
    chapterData.quiz.forEach(question => {
      if (quizAnswers[question.id] === question.correct) {
        correct++
      }
    })
    return (correct / chapterData.quiz.length) * 100
  }

  return (
    <motion.div
      initial={{ opacity: 0, y: 20 }}
      animate={{ opacity: 1, y: 0 }}
      transition={{ duration: 0.5 }}
      className="max-w-4xl mx-auto space-y-8"
    >
      {/* Chapter Header */}
      <Card className="bg-gradient-to-r from-blue-600 to-purple-600 text-white border-0">
        <CardContent className="p-8">
          <div className="flex items-center space-x-4 mb-4">
            <div className="p-3 bg-white/20 rounded-lg">
              <BookOpen className="h-8 w-8" />
            </div>
            <div>
              <Badge className="bg-white/20 text-white mb-2">บทที่ 1</Badge>
              <h1 className="text-3xl font-bold mb-2">{chapterData.title}</h1>
              <p className="text-xl opacity-90">{chapterData.subtitle}</p>
            </div>
          </div>
          
          <div className="grid md:grid-cols-3 gap-4 mt-6">
            <div className="flex items-center space-x-2">
              <Clock className="h-5 w-5" />
              <span>{chapterData.duration}</span>
            </div>
            <div className="flex items-center space-x-2">
              <Target className="h-5 w-5" />
              <span>ระดับ: {chapterData.difficulty}</span>
            </div>
            <div className="flex items-center space-x-2">
              <TrendingUp className="h-5 w-5" />
              <span>ความคืบหนา: {Math.round(progress)}%</span>
            </div>
          </div>
          
          <Progress value={progress} className="mt-4 h-2 bg-white/20" />
        </CardContent>
      </Card>

      {/* Learning Objectives */}
      <Card>
        <CardHeader>
          <CardTitle className="flex items-center space-x-2">
            <Lightbulb className="h-6 w-6 text-yellow-500" />
            <span>วัตถุประสงค์การเรียนรู้</span>
          </CardTitle>
        </CardHeader>
        <CardContent>
          <div className="space-y-3">
            {chapterData.objectives.map((objective, index) => (
              <div key={index} className="flex items-start space-x-3">
                <div className="w-6 h-6 rounded-full bg-blue-600 text-white flex items-center justify-center text-sm font-bold mt-0.5">
                  {index + 1}
                </div>
                <p className="text-sm leading-relaxed">{objective}</p>
              </div>
            ))}
          </div>
        </CardContent>
      </Card>

      {/* Chapter Content */}
      <div className="space-y-6">
        {chapterData.sections.map((section, index) => (
          <motion.div
            key={section.id}
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ delay: index * 0.1 }}
          >
            <Card className={`${
              completedSections.has(section.id) 
                ? 'border-green-500 bg-green-50 dark:bg-green-900/20' 
                : currentSection === section.id
                ? 'border-blue-500 bg-blue-50 dark:bg-blue-900/20'
                : ''
            }`}>
              <CardHeader 
                className="cursor-pointer"
                onClick={() => toggleSection(section.id)}
              >
                <div className="flex items-center justify-between">
                  <div className="flex items-center space-x-3">
                    {completedSections.has(section.id) ? (
                      <CheckCircle className="h-6 w-6 text-green-600" />
                    ) : (
                      <Circle className="h-6 w-6 text-gray-400" />
                    )}
                    <div>
                      <CardTitle className="text-lg">{section.title}</CardTitle>
                      <CardDescription className="flex items-center space-x-4 mt-1">
                        <span className="flex items-center space-x-1">
                          <Clock className="h-4 w-4" />
                          <span>{section.estimatedTime} นาที</span>
                        </span>
                      </CardDescription>
                    </div>
                  </div>
                  {expandedSections.has(section.id) ? (
                    <ChevronUp className="h-5 w-5" />
                  ) : (
                    <ChevronDown className="h-5 w-5" />
                  )}
                </div>
              </CardHeader>
              
              <AnimatePresence>
                {expandedSections.has(section.id) && (
                  <motion.div
                    initial={{ height: 0, opacity: 0 }}
                    animate={{ height: 'auto', opacity: 1 }}
                    exit={{ height: 0, opacity: 0 }}
                    transition={{ duration: 0.3 }}
                  >
                    <CardContent className="pt-0">
                      {section.image && (
                        <div className="mb-6">
                          <img 
                            src={section.image} 
                            alt={section.title}
                            className="w-full rounded-lg shadow-md"
                          />
                        </div>
                      )}
                      
                      <div className="prose dark:prose-invert max-w-none">
                        <div className="whitespace-pre-line text-sm leading-relaxed">
                          {section.content}
                        </div>
                      </div>
                      
                      <div className="flex justify-between items-center mt-6 pt-4 border-t">
                        <Button
                          variant="outline"
                          onClick={() => setCurrentSection(section.id)}
                        >
                          ตั้งเป็นหัวข้อปัจจุบัน
                        </Button>
                        
                        {!completedSections.has(section.id) && (
                          <Button
                            onClick={() => markSectionComplete(section.id)}
                            className="bg-green-600 hover:bg-green-700"
                          >
                            <CheckCircle className="h-4 w-4 mr-2" />
                            ทำเครื่องหมายว่าเสร็จสิ้น
                          </Button>
                        )}
                      </div>
                    </CardContent>
                  </motion.div>
                )}
              </AnimatePresence>
            </Card>
          </motion.div>
        ))}
      </div>

      {/* Interactive Quiz */}
      <Card>
        <CardHeader>
          <CardTitle className="flex items-center space-x-2">
            <Brain className="h-6 w-6 text-purple-600" />
            <span>แบบทดสอบความเข้าใจ</span>
          </CardTitle>
          <CardDescription>
            ทดสอบความเข้าใจในเนื้อหาบทที่ 1
          </CardDescription>
        </CardHeader>
        <CardContent>
          <div className="space-y-6">
            {chapterData.quiz.map((question, qIndex) => (
              <div key={question.id} className="space-y-4">
                <h3 className="font-semibold">
                  {qIndex + 1}. {question.question}
                </h3>
                <div className="space-y-2">
                  {question.options.map((option, oIndex) => (
                    <label
                      key={oIndex}
                      className={`flex items-center space-x-3 p-3 rounded-lg border cursor-pointer transition-colors ${
                        quizAnswers[question.id] === oIndex
                          ? 'border-blue-500 bg-blue-50 dark:bg-blue-900/20'
                          : 'border-gray-200 hover:border-gray-300'
                      }`}
                    >
                      <input
                        type="radio"
                        name={question.id}
                        value={oIndex}
                        checked={quizAnswers[question.id] === oIndex}
                        onChange={() => handleQuizAnswer(question.id, oIndex)}
                        className="text-blue-600"
                      />
                      <span>{option}</span>
                    </label>
                  ))}
                </div>
                
                {showQuizResults && (
                  <motion.div
                    initial={{ opacity: 0, height: 0 }}
                    animate={{ opacity: 1, height: 'auto' }}
                    className={`p-4 rounded-lg ${
                      quizAnswers[question.id] === question.correct
                        ? 'bg-green-100 dark:bg-green-900/20 border border-green-500'
                        : 'bg-red-100 dark:bg-red-900/20 border border-red-500'
                    }`}
                  >
                    <p className="font-semibold mb-2">
                      {quizAnswers[question.id] === question.correct ? '✅ ถูกต้อง!' : '❌ ไม่ถูกต้อง'}
                    </p>
                    <p className="text-sm">{question.explanation}</p>
                    {quizAnswers[question.id] !== question.correct && (
                      <p className="text-sm mt-2">
                        <strong>คำตอบที่ถูกต้อง:</strong> {question.options[question.correct]}
                      </p>
                    )}
                  </motion.div>
                )}
              </div>
            ))}
            
            <div className="flex justify-between items-center pt-4 border-t">
              {!showQuizResults ? (
                <Button
                  onClick={submitQuiz}
                  disabled={Object.keys(quizAnswers).length < chapterData.quiz.length}
                  className="bg-purple-600 hover:bg-purple-700"
                >
                  ส่งคำตอบ
                </Button>
              ) : (
                <div className="flex items-center space-x-4">
                  <Badge className={`${
                    getQuizScore() >= 70 ? 'bg-green-600' : 'bg-red-600'
                  } text-white`}>
                    คะแนน: {Math.round(getQuizScore())}%
                  </Badge>
                  <Button
                    variant="outline"
                    onClick={() => {
                      setQuizAnswers({})
                      setShowQuizResults(false)
                    }}
                  >
                    <RotateCcw className="h-4 w-4 mr-2" />
                    ทำใหม่
                  </Button>
                </div>
              )}
            </div>
          </div>
        </CardContent>
      </Card>

      {/* Navigation */}
      <div className="flex justify-between">
        <Button variant="outline" disabled>
          บทก่อนหน้า
        </Button>
        <Button className="bg-blue-600 hover:bg-blue-700">
          บทถัดไป: พื้นฐานทางคณิตศาสตร์
          <ArrowRight className="h-4 w-4 ml-2" />
        </Button>
      </div>
    </motion.div>
  )
}

export default Chapter1
