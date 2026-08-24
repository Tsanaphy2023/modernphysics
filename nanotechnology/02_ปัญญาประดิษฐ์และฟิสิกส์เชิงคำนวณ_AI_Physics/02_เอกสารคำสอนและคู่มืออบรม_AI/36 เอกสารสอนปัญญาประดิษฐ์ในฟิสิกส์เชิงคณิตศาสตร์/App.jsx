import { useState, useEffect, useMemo, lazy, Suspense } from 'react'
import { BrowserRouter as Router, Routes, Route, Navigate } from 'react-router-dom'
import { motion, AnimatePresence } from 'framer-motion'
import { BookOpen, Menu, X, Home, Download, Search, Settings, User, Loader2 } from 'lucide-react'
import { Button } from '@/components/ui/button.jsx'
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from '@/components/ui/card.jsx'
import { Badge } from '@/components/ui/badge.jsx'
import { Progress } from '@/components/ui/progress.jsx'
import { Input } from '@/components/ui/input.jsx'
import { Sidebar } from '@/components/ui/sidebar.jsx'
import './App.css'

// Import course content and images
import courseOutline from './assets/ai_physics_course_outline.md?raw'

// Lazy load chapter components for better performance
const ChapterOverview = lazy(() => import('./components/ChapterOverview'))
const Chapter1Enhanced = lazy(() => import('./components/Chapter1Enhanced'))
const Chapter2Enhanced = lazy(() => import('./components/Chapter2Enhanced'))
const Chapter3Enhanced = lazy(() => import('./components/Chapter3Enhanced'))
const Chapter4Enhanced = lazy(() => import('./components/Chapter4Enhanced'))
const Chapter5Enhanced = lazy(() => import('./components/Chapter5Enhanced'))
const Chapter6Enhanced = lazy(() => import('./components/Chapter6Enhanced'))
const Chapter7Enhanced = lazy(() => import('./components/Chapter7Enhanced'))
const Chapter8Enhanced = lazy(() => import('./components/Chapter8Enhanced'))
const Chapter9Enhanced = lazy(() => import('./components/Chapter9Enhanced'))
const ComponentDemo = lazy(() => import('./components/ComponentDemo'))
const SimpleEnhancedDemo = lazy(() => import('./components/SimpleEnhancedDemo'))

// Loading component
const LoadingSpinner = () => (
    <div className="flex items-center justify-center min-h-[400px]">
    <div className="flex flex-col items-center space-y-4">
      <div className="holo-spinner"></div>
      <p className="text-gray-600 dark:text-gray-300">กำลังโหลด...</p>
    </div>
  </div>
)

// Course data structure - memoized for performance
const courseData = {
  title: "ปัญญาประดิษฐ์สำหรับฟิสิกส์เชิงคณิตศาสตร์",
  subtitle: "Artificial Intelligence for Mathematical Physics",
  description: "รายวิชานี้สำรวจการประยุกต์ใช้เทคนิคปัญญาประดิษฐ์ (AI) และการเรียนรู้ของเครื่อง (Machine Learning) เพื่อแก้ไขปัญหาที่ซับซ้อนในขอบเขตของฟิสิกส์เชิงคณิตศาสตร์",
  chapters: [
    {
      id: 1,
      title: "บทนำสู่ปัญญาประดิษฐ์และฟิสิกส์เชิงคณิตศาสตร์",
      subtitle: "Introduction to AI and Mathematical Physics",
      description: "ภาพรวมและความสำคัญของการบูรณาการ AI ในงานวิจัยฟิสิกส์ พร้อมทบทวนแนวคิดหลักทางฟิสิกส์เชิงคณิตศาสตร์",
      duration: "2 ชั่วโมง",
      difficulty: "เริ่มต้น",
      topics: ["ประวัติ AI ในฟิสิกส์", "ความท้าทายในฟิสิกส์ยุคใหม่", "หลักคณิตศาสตร์พื้นฐาน", "เครื่องมือและภาษาโปรแกรม"]
    },
    {
      id: 2,
      title: "พื้นฐานทางคณิตศาสตร์สำหรับการเรียนรู้ของเครื่อง",
      subtitle: "Mathematical Foundations for Machine Learning",
      description: "หลักการทางคณิตศาสตร์ที่เป็นรากฐานของอัลกอริทึม ML รวมถึงพีชคณิตเชิงเส้น แคลคูลัส และทฤษฎีความน่าจะเป็น",
      duration: "3 ชั่วโมง",
      difficulty: "ปานกลาง",
      topics: ["พีชคณิตเชิงเส้น", "แคลคูลัสหลายตัวแปร", "ทฤษฎีความน่าจะเป็น", "การวิเคราะห์ฟูเรียร์"]
    },
    {
      id: 3,
      title: "การเรียนรู้แบบมีผู้สอน (Supervised Learning)",
      subtitle: "Supervised Learning and Applications",
      description: "หลักการทำงานของแบบจำลองการถดถอยและการจำแนกประเภท พร้อมการประยุกต์ใช้ในการวิเคราะห์ข้อมูลทางฟิสิกส์",
      duration: "4 ชั่วโมง",
      difficulty: "ปานกลาง",
      topics: ["Linear Regression", "Classification", "Support Vector Machines", "Random Forest"]
    },
    {
      id: 4,
      title: "การเรียนรู้แบบไม่มีผู้สอน (Unsupervised Learning)",
      subtitle: "Unsupervised Learning and Pattern Discovery",
      description: "เทคนิคการลดมิติและการจัดกลุ่ม เพื่อค้นหารูปแบบที่ซ่อนอยู่ในข้อมูลฟิสิกส์",
      duration: "3 ชั่วโมง",
      difficulty: "ปานกลาง",
      topics: ["PCA", "t-SNE", "K-Means Clustering", "DBSCAN"]
    },
    {
      id: 5,
      title: "โครงข่ายประสาทเทียมและการเรียนรู้เชิงลึก",
      subtitle: "Neural Networks and Deep Learning",
      description: "สถาปัตยกรรมและหลักการทำงานของโครงข่ายประสาทเทียม พร้อมการประยุกต์ใช้ในปัญหาที่ซับซ้อนทางฟิสิกส์",
      duration: "5 ชั่วโมง",
      difficulty: "สูง",
      topics: ["Neural Networks", "Backpropagation", "Deep Learning", "Activation Functions"]
    },
    {
      id: 6,
      title: "การจำลองและการสร้างแบบจำลองด้วย AI",
      subtitle: "AI Simulation and Modeling",
      description: "การใช้ CNNs ในการวิเคราะห์ข้อมูลที่มีลักษณะเป็นโครงสร้างกริด และการประยุกต์ใช้ในฟิสิกส์อนุภาค",
      duration: "4 ชั่วโมง",
      difficulty: "สูง",
      topics: ["CNNs", "Image Processing", "Transfer Learning", "Feature Visualization"]
    },
    {
      id: 7,
      title: "การเรียนรู้เสริมกำลัง (Reinforcement Learning)",
      subtitle: "Reinforcement Learning and System Control",
      description: "หลักการของ RL และการประยุกต์ใช้ในการควบคุมระบบ การออกแบบการทดลอง และการหาค่าเหมาะสมที่สุด",
      duration: "4 ชั่วโมง",
      difficulty: "สูง",
      topics: ["Q-Learning", "Policy Gradient", "Actor-Critic", "Quantum Control"]
    },
    {
      id: 8,
      title: "การค้นพบสมการเชิงฟิสิกส์ด้วย AI",
      subtitle: "Physics Equation Discovery with AI",
      description: "การใช้ AI ในการค้นหาสมการทางคณิตศาสตร์จากข้อมูล รวมถึง Symbolic Regression และ Physics-Informed Neural Networks",
      duration: "4 ชั่วโมง",
      difficulty: "สูงมาก",
      topics: ["Symbolic Regression", "PINNs", "Equation Discovery", "Scientific Computing"]
    },
    {
      id: 9,
      title: "การประยุกต์ใช้ขั้นสูงและแนวโน้มอนาคต",
      subtitle: "Advanced Applications and Future Trends",
      description: "ฟิสิกส์ควอนตัมและปัญญาประดิษฐ์ จริยธรรมและผลกระทบทางสังคม และแนวโน้มอนาคตของ AI ในฟิสิกส์",
      duration: "3 ชั่วโมง",
      difficulty: "สูงมาก",
      topics: ["Quantum AI", "Ethics", "Future Trends", "Research Frontiers"]
    }
  ]
}

function App() {
  const [sidebarOpen, setSidebarOpen] = useState(false)
  const [currentChapter, setCurrentChapter] = useState(0)
  const [progress, setProgress] = useState(0)
  const [searchQuery, setSearchQuery] = useState('')
  const [darkMode, setDarkMode] = useState(() => {
    // Initialize dark mode from localStorage
    const saved = localStorage.getItem('darkMode')
    return saved ? JSON.parse(saved) : false
  })

  // Calculate overall progress - memoized for performance
  const calculatedProgress = useMemo(() => {
    const completedChapters = currentChapter
    const totalChapters = courseData.chapters.length
    return (completedChapters / totalChapters) * 100
  }, [currentChapter])

  useEffect(() => {
    setProgress(calculatedProgress)
  }, [calculatedProgress])

  // Toggle dark mode and persist to localStorage
  useEffect(() => {
    localStorage.setItem('darkMode', JSON.stringify(darkMode))
    if (darkMode) {
      document.documentElement.classList.add('dark')
    } else {
      document.documentElement.classList.remove('dark')
    }
  }, [darkMode])

  // Memoized difficulty color function
  const getDifficultyColor = useMemo(() => (difficulty) => {
    switch (difficulty) {
      case 'เริ่มต้น': return 'bg-green-500'
      case 'ปานกลาง': return 'bg-yellow-500'
      case 'สูง': return 'bg-orange-500'
      case 'สูงมาก': return 'bg-red-500'
      default: return 'bg-gray-500'
    }
  }, [])

  // Memoized filtered chapters for search
  const filteredChapters = useMemo(() => {
    if (!searchQuery) return courseData.chapters
    return courseData.chapters.filter(chapter =>
      chapter.title.toLowerCase().includes(searchQuery.toLowerCase()) ||
      chapter.subtitle.toLowerCase().includes(searchQuery.toLowerCase()) ||
      chapter.topics.some(topic => topic.toLowerCase().includes(searchQuery.toLowerCase()))
    )
  }, [searchQuery])

  // Handle window resize for responsive sidebar
  useEffect(() => {
    const handleResize = () => {
      if (window.innerWidth >= 1024) {
        setSidebarOpen(true)
      } else {
        setSidebarOpen(false)
      }
    }

    handleResize() // Set initial state
    window.addEventListener('resize', handleResize)
    return () => window.removeEventListener('resize', handleResize)
  }, [])

  const MainLayout = ({ children }) => (
    <div className="min-h-screen bg-gradient-to-br from-blue-50 via-indigo-50 to-purple-50 dark:from-gray-900 dark:via-blue-900 dark:to-indigo-900 holo-matrix">
      {/* Holographic Grid Background */}
      <div className="holo-grid-bg"></div>
      {/* Holographic Particles */}
      <div className="holo-particles">
        <div className="holo-particle"></div>
        <div className="holo-particle"></div>
        <div className="holo-particle"></div>
        <div className="holo-particle"></div>
        <div className="holo-particle"></div>
        <div className="holo-particle"></div>
        <div className="holo-particle"></div>
        <div className="holo-particle"></div>
        <div className="holo-particle"></div>
      </div>
      {/* Holographic Scan Lines */}
      <div className="holo-scanlines"></div>
      {/* Header */}
      <header className="sticky top-0 z-50 holo-nav backdrop-blur-md border-b border-gray-200 dark:border-gray-700">
        <div className="container mx-auto px-4 py-4">
          <div className="flex items-center justify-between">
            <div className="flex items-center space-x-4">
              <Button
                variant="ghost"
                size="sm"
                onClick={() => setSidebarOpen(!sidebarOpen)}
                className="lg:hidden"
                aria-label="Toggle sidebar"
              >
                {sidebarOpen ? <X className="h-5 w-5" /> : <Menu className="h-5 w-5" />}
              </Button>
              <div className="flex items-center space-x-3">
                <div className="p-2 bg-gradient-to-r from-orange-600 to-red-600 rounded-lg holo-glow">
                  <BookOpen className="h-6 w-6 text-white" />
                </div>
                <div>
                  <h1 className="text-xl font-bold text-gray-900 dark:text-white holo-text">
                    AI Physics Course
                  </h1>
                  <p className="text-sm text-gray-600 dark:text-gray-300">
                    Interactive Learning Platform
                  </p>
                </div>
              </div>
            </div>
            
            <div className="flex items-center space-x-4">
              <div className="hidden md:flex items-center space-x-2">
                <Search className="h-4 w-4 text-gray-400" />
                  <Input
                  placeholder="ค้นหาเนื้อหา..."
                  value={searchQuery}
                  onChange={(e) => setSearchQuery(e.target.value)}
                  className="w-64 holo-input holo-input-animated"
                />
              </div>
              <Button
                variant="ghost"
                size="sm"
                onClick={() => setDarkMode(!darkMode)}
                aria-label="Toggle dark mode"
                className="holo-button holo-button-interactive"
              >
                {darkMode ? '☀️' : '🌙'}
              </Button>
              <Button variant="ghost" size="sm" aria-label="Settings" className="holo-button holo-button-interactive">
                <Settings className="h-4 w-4" />
              </Button>
            </div>
          </div>
          
          {/* Progress Bar */}
          <div className="mt-4">
            <div className="flex items-center justify-between text-sm text-gray-600 dark:text-gray-300 mb-2">
              <span>ความคืบหนา</span>
              <span>{Math.round(progress)}%</span>
            </div>
            <div className="holo-progress h-2 rounded-full">
              <div className="holo-progress-bar" style={{width: `${progress}%`}}></div>
            </div>
          </div>
        </div>
      </header>

      <div className="flex">
        {/* Sidebar */}
        <AnimatePresence>
          {(sidebarOpen || window.innerWidth >= 1024) && (
            <motion.aside
              initial={{ x: -300, opacity: 0 }}
              animate={{ x: 0, opacity: 1 }}
              exit={{ x: -300, opacity: 0 }}
              transition={{ duration: 0.3 }}
              className="fixed lg:sticky top-[120px] left-0 z-40 w-80 h-[calc(100vh-120px)] holo-nav border-r border-gray-200 dark:border-gray-700 overflow-y-auto"
            >
              <div className="p-6">
                <div className="space-y-4">
                  {/* Course Overview */}
                  <Card className="holo-card holo-card-enhanced border-2 border-orange-200 dark:border-orange-800">
                    <CardHeader className="pb-3">
                      <CardTitle className="text-lg holo-text">ภาพรวมรายวิชา</CardTitle>
                    </CardHeader>
                    <CardContent>
                      <div className="space-y-2 text-sm">
                        <div className="flex justify-between">
                          <span>บทเรียนทั้งหมด:</span>
                          <span className="font-semibold">{courseData.chapters.length} บท</span>
                        </div>
                        <div className="flex justify-between">
                          <span>เวลาเรียนรวม:</span>
                          <span className="font-semibold">32 ชั่วโมง</span>
                        </div>
                        <div className="flex justify-between">
                          <span>ระดับความยาก:</span>
                          <Badge variant="secondary">ปานกลาง-สูง</Badge>
                        </div>
                      </div>
                    </CardContent>
                  </Card>

                  {/* Chapter List */}
                  <div className="space-y-2">
                    <h3 className="font-semibold text-gray-900 dark:text-white mb-3 holo-text">
                      รายการบทเรียน
                    </h3>
                    {filteredChapters.map((chapter, index) => (
                      <motion.div
                        key={chapter.id}
                        whileHover={{ scale: 1.02 }}
                        whileTap={{ scale: 0.98 }}
                      >
                        <Card 
                          className={`cursor-pointer transition-all duration-200 holo-card ${
                            currentChapter === index 
                              ? 'border-orange-500 bg-orange-50 dark:bg-orange-900/20' 
                              : 'hover:border-gray-300 dark:hover:border-gray-600'
                          }`}
                          onClick={() => setCurrentChapter(index)}
                        >
                          <CardContent className="p-4">
                            <div className="flex items-start space-x-3">
                              <div className={`w-8 h-8 rounded-full flex items-center justify-center text-white text-sm font-bold holo-glow ${
                                currentChapter >= index ? 'bg-orange-600' : 'bg-gray-400'
                              }`}>
                                {chapter.id}
                              </div>
                              <div className="flex-1 min-w-0">
                                <h4 className="font-medium text-sm text-gray-900 dark:text-white line-clamp-2">
                                  {chapter.title}
                                </h4>
                                <p className="text-xs text-gray-600 dark:text-gray-300 mt-1">
                                  {chapter.duration}
                                </p>
                                <div className="flex items-center space-x-2 mt-2">
                                  <div className={`w-2 h-2 rounded-full ${getDifficultyColor(chapter.difficulty)}`} />
                                  <span className="text-xs text-gray-500 dark:text-gray-400">
                                    {chapter.difficulty}
                                  </span>
                                </div>
                              </div>
                            </div>
                          </CardContent>
                        </Card>
                      </motion.div>
                    ))}
                  </div>

                  {/* Quick Actions */}
                  <Card className="holo-card holo-card-enhanced">
                    <CardHeader className="pb-3">
                      <CardTitle className="text-lg holo-text">เครื่องมือ</CardTitle>
                    </CardHeader>
                    <CardContent className="space-y-2">
                      <Button variant="outline" className="w-full justify-start holo-button holo-button-interactive" size="sm">
                        <Download className="h-4 w-4 mr-2" />
                        ดาวน์โหลด PDF
                      </Button>
                      <Button variant="outline" className="w-full justify-start holo-button holo-button-interactive" size="sm">
                        <BookOpen className="h-4 w-4 mr-2" />
                        บันทึกการเรียน
                      </Button>
                      <Button variant="outline" className="w-full justify-start holo-button holo-button-interactive" size="sm">
                        <User className="h-4 w-4 mr-2" />
                        โปรไฟล์ผู้เรียน
                      </Button>
                    </CardContent>
                  </Card>
                </div>
              </div>
            </motion.aside>
          )}
        </AnimatePresence>

        {/* Main Content */}
        <main className="flex-1 lg:ml-0">
          <div className="container mx-auto px-4 py-8">
            <Suspense fallback={<LoadingSpinner />}>
              {children}
            </Suspense>
          </div>
        </main>
      </div>
    </div>
  )

  return (
    <Router>
      <MainLayout>
        <Routes>
          <Route path="/" element={<ChapterOverview courseData={courseData} currentChapter={currentChapter} setCurrentChapter={setCurrentChapter} />} />
          <Route path="/chapter/1" element={<Chapter1Enhanced />} />
          <Route path="/chapter/2" element={<Chapter2Enhanced />} />
          <Route path="/chapter/3" element={<Chapter3Enhanced />} />
          <Route path="/chapter/4" element={<Chapter4Enhanced />} />
          <Route path="/chapter/5" element={<Chapter5Enhanced />} />
          <Route path="/chapter/6" element={<Chapter6Enhanced />} />
          <Route path="/chapter/7" element={<Chapter7Enhanced />} />
          <Route path="/chapter/8" element={<Chapter8Enhanced />} />
          <Route path="/chapter/9" element={<Chapter9Enhanced />} />
          <Route path="/demo" element={<ComponentDemo />} />
          <Route path="/enhanced" element={<SimpleEnhancedDemo />} />
          <Route path="*" element={<Navigate to="/" replace />} />
        </Routes>
      </MainLayout>
    </Router>
  )
}

export default App
