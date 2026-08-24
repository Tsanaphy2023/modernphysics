import { motion } from 'framer-motion'
import { useNavigate } from 'react-router-dom'
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from '@/components/ui/card.jsx'
import { Button } from '@/components/ui/button.jsx'
import { Badge } from '@/components/ui/badge.jsx'
import { Progress } from '@/components/ui/progress.jsx'
import { 
  BookOpen, 
  Clock, 
  Target, 
  TrendingUp, 
  Brain, 
  Zap, 
  Microscope, 
  Atom,
  ChevronRight,
  Play,
  Download,
  Star
} from 'lucide-react'

const ChapterOverview = ({ courseData, currentChapter, setCurrentChapter }) => {
  const navigate = useNavigate()

  const getDifficultyColor = (difficulty) => {
    switch (difficulty) {
      case 'เริ่มต้น': return 'bg-green-500 text-white'
      case 'ปานกลาง': return 'bg-yellow-500 text-white'
      case 'สูง': return 'bg-orange-500 text-white'
      case 'สูงมาก': return 'bg-red-500 text-white'
      default: return 'bg-gray-500 text-white'
    }
  }

  const getChapterIcon = (chapterId) => {
    const icons = {
      1: BookOpen,
      2: Target,
      3: TrendingUp,
      4: Brain,
      5: Zap,
      6: Microscope,
      7: Atom,
      8: Brain,
      9: Star
    }
    return icons[chapterId] || BookOpen
  }

  const containerVariants = {
    hidden: { opacity: 0 },
    visible: {
      opacity: 1,
      transition: {
        staggerChildren: 0.1
      }
    }
  }

  const itemVariants = {
    hidden: { y: 20, opacity: 0 },
    visible: {
      y: 0,
      opacity: 1,
      transition: {
        duration: 0.5
      }
    }
  }

  return (
    <motion.div
      variants={containerVariants}
      initial="hidden"
      animate="visible"
      className="space-y-8"
    >
      {/* Hero Section */}
      <motion.div variants={itemVariants}>
        <Card className="bg-gradient-to-r from-blue-600 via-purple-600 to-indigo-600 text-white border-0">
          <CardContent className="p-8">
            <div className="grid md:grid-cols-2 gap-8 items-center">
              <div>
                <h1 className="text-4xl font-bold mb-4">
                  {courseData.title}
                </h1>
                <h2 className="text-xl opacity-90 mb-4">
                  {courseData.subtitle}
                </h2>
                <p className="text-lg opacity-80 mb-6 leading-relaxed">
                  {courseData.description}
                </p>
                <div className="flex flex-wrap gap-4">
                  <Button 
                    size="lg" 
                    className="bg-white text-blue-600 hover:bg-gray-100"
                    onClick={() => navigate('/chapter/1')}
                  >
                    <Play className="h-5 w-5 mr-2" />
                    เริ่มเรียน
                  </Button>
                  <Button 
                    size="lg" 
                    variant="outline" 
                    className="border-white text-white hover:bg-white hover:text-blue-600"
                  >
                    <Download className="h-5 w-5 mr-2" />
                    ดาวน์โหลด PDF
                  </Button>
                </div>
              </div>
              <div className="hidden md:block">
                <div className="relative">
                  <div className="absolute inset-0 bg-white/10 rounded-2xl backdrop-blur-sm"></div>
                  <div className="relative p-6 space-y-4">
                    <div className="flex items-center justify-between">
                      <span className="text-sm opacity-80">ความคืบหนา</span>
                      <span className="text-sm font-semibold">
                        {Math.round((currentChapter / courseData.chapters.length) * 100)}%
                      </span>
                    </div>
                    <Progress 
                      value={(currentChapter / courseData.chapters.length) * 100} 
                      className="h-3 bg-white/20"
                    />
                    <div className="grid grid-cols-3 gap-4 text-center">
                      <div>
                        <div className="text-2xl font-bold">{courseData.chapters.length}</div>
                        <div className="text-xs opacity-80">บทเรียน</div>
                      </div>
                      <div>
                        <div className="text-2xl font-bold">32</div>
                        <div className="text-xs opacity-80">ชั่วโมง</div>
                      </div>
                      <div>
                        <div className="text-2xl font-bold">150+</div>
                        <div className="text-xs opacity-80">แบบฝึกหัด</div>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </CardContent>
        </Card>
      </motion.div>

      {/* Learning Objectives */}
      <motion.div variants={itemVariants}>
        <Card>
          <CardHeader>
            <CardTitle className="flex items-center space-x-2">
              <Target className="h-6 w-6 text-blue-600" />
              <span>วัตถุประสงค์การเรียนรู้</span>
            </CardTitle>
            <CardDescription>
              เมื่อสิ้นสุดการเรียนการสอนในรายวิชานี้ นิสิตจะสามารถ:
            </CardDescription>
          </CardHeader>
          <CardContent>
            <div className="grid md:grid-cols-2 gap-4">
              {[
                "อธิบายหลักการพื้นฐานและทฤษฎีทางคณิตศาสตร์ของอัลกอริทึมปัญญาประดิษฐ์ที่สำคัญได้",
                "ประยุกต์ใช้แบบจำลองการเรียนรู้ของเครื่องเพื่อวิเคราะห์และแก้ปัญหาในสาขาฟิสิกส์เชิงคณิตศาสตร์",
                "ออกแบบและพัฒนาแบบจำลอง AI สำหรับการจำลองปรากฏการณ์ทางฟิสิกส์ การวิเคราะห์ข้อมูลขนาดใหญ่",
                "วิเคราะห์และประเมินผลความแม่นยำและข้อจำกัดของแบบจำลอง AI ในบริบทของงานวิจัยทางฟิสิกส์",
                "นำเสนอแนวคิดการวิจัยที่ผสมผสานระหว่าง AI และฟิสิกส์เชิงคณิตศาสตร์ได้อย่างเป็นระบบ"
              ].map((objective, index) => (
                <motion.div
                  key={index}
                  whileHover={{ scale: 1.02 }}
                  className="flex items-start space-x-3 p-4 rounded-lg bg-gray-50 dark:bg-gray-800"
                >
                  <div className="w-6 h-6 rounded-full bg-blue-600 text-white flex items-center justify-center text-sm font-bold mt-0.5">
                    {index + 1}
                  </div>
                  <p className="text-sm leading-relaxed">{objective}</p>
                </motion.div>
              ))}
            </div>
          </CardContent>
        </Card>
      </motion.div>

      {/* Chapter Grid */}
      <motion.div variants={itemVariants}>
        <div className="flex items-center justify-between mb-6">
          <h2 className="text-2xl font-bold text-gray-900 dark:text-white">
            โครงสร้างเนื้อหารายวิชา
          </h2>
          <Badge variant="secondary" className="text-sm">
            {courseData.chapters.length} บทเรียน
          </Badge>
        </div>
        
        <div className="grid gap-6">
          {courseData.chapters.map((chapter, index) => {
            const IconComponent = getChapterIcon(chapter.id)
            const isCompleted = currentChapter > index
            const isCurrent = currentChapter === index
            
            return (
              <motion.div
                key={chapter.id}
                variants={itemVariants}
                whileHover={{ scale: 1.02 }}
                whileTap={{ scale: 0.98 }}
              >
                <Card 
                  className={`cursor-pointer transition-all duration-300 ${
                    isCurrent 
                      ? 'border-blue-500 shadow-lg bg-blue-50 dark:bg-blue-900/20' 
                      : isCompleted
                      ? 'border-green-500 bg-green-50 dark:bg-green-900/20'
                      : 'hover:border-gray-300 dark:hover:border-gray-600 hover:shadow-md'
                  }`}
                  onClick={() => {
                    setCurrentChapter(index)
                    navigate(`/chapter/${chapter.id}`)
                  }}
                >
                  <CardContent className="p-6">
                    <div className="flex items-start space-x-4">
                      <div className={`p-3 rounded-xl ${
                        isCurrent 
                          ? 'bg-blue-600 text-white' 
                          : isCompleted
                          ? 'bg-green-600 text-white'
                          : 'bg-gray-100 dark:bg-gray-800 text-gray-600 dark:text-gray-300'
                      }`}>
                        <IconComponent className="h-6 w-6" />
                      </div>
                      
                      <div className="flex-1 min-w-0">
                        <div className="flex items-start justify-between">
                          <div className="flex-1">
                            <div className="flex items-center space-x-2 mb-2">
                              <h3 className="text-lg font-semibold text-gray-900 dark:text-white">
                                บทที่ {chapter.id}: {chapter.title}
                              </h3>
                              {isCompleted && (
                                <Badge className="bg-green-600 text-white">
                                  เสร็จสิ้น
                                </Badge>
                              )}
                              {isCurrent && (
                                <Badge className="bg-blue-600 text-white">
                                  กำลังเรียน
                                </Badge>
                              )}
                            </div>
                            <p className="text-sm text-gray-600 dark:text-gray-300 mb-2">
                              {chapter.subtitle}
                            </p>
                            <p className="text-sm text-gray-700 dark:text-gray-300 mb-4 leading-relaxed">
                              {chapter.description}
                            </p>
                            
                            <div className="flex flex-wrap gap-2 mb-4">
                              {chapter.topics.slice(0, 3).map((topic, topicIndex) => (
                                <Badge key={topicIndex} variant="outline" className="text-xs">
                                  {topic}
                                </Badge>
                              ))}
                              {chapter.topics.length > 3 && (
                                <Badge variant="outline" className="text-xs">
                                  +{chapter.topics.length - 3} เพิ่มเติม
                                </Badge>
                              )}
                            </div>
                            
                            <div className="flex items-center space-x-4 text-sm text-gray-600 dark:text-gray-300">
                              <div className="flex items-center space-x-1">
                                <Clock className="h-4 w-4" />
                                <span>{chapter.duration}</span>
                              </div>
                              <Badge className={getDifficultyColor(chapter.difficulty)}>
                                {chapter.difficulty}
                              </Badge>
                            </div>
                          </div>
                          
                          <ChevronRight className="h-5 w-5 text-gray-400 mt-1" />
                        </div>
                      </div>
                    </div>
                  </CardContent>
                </Card>
              </motion.div>
            )
          })}
        </div>
      </motion.div>

      {/* Course Features */}
      <motion.div variants={itemVariants}>
        <Card>
          <CardHeader>
            <CardTitle>คุณสมบัติพิเศษของหลักสูตร</CardTitle>
            <CardDescription>
              เรียนรู้ด้วยเทคโนโลยีล่าสุดและเครื่องมือที่ทันสมัย
            </CardDescription>
          </CardHeader>
          <CardContent>
            <div className="grid md:grid-cols-3 gap-6">
              {[
                {
                  icon: Brain,
                  title: "Interactive Simulations",
                  description: "จำลองปรากฏการณ์ทางฟิสิกส์แบบโต้ตอบได้"
                },
                {
                  icon: Zap,
                  title: "Code Playground",
                  description: "เขียนและทดสอบโค้ด Python แบบเรียลไทม์"
                },
                {
                  icon: Target,
                  title: "Adaptive Quizzes",
                  description: "แบบทดสอบที่ปรับระดับตามความสามารถ"
                }
              ].map((feature, index) => (
                <motion.div
                  key={index}
                  whileHover={{ y: -5 }}
                  className="text-center p-6 rounded-lg bg-gradient-to-br from-gray-50 to-gray-100 dark:from-gray-800 dark:to-gray-900"
                >
                  <feature.icon className="h-12 w-12 text-blue-600 mx-auto mb-4" />
                  <h3 className="font-semibold text-gray-900 dark:text-white mb-2">
                    {feature.title}
                  </h3>
                  <p className="text-sm text-gray-600 dark:text-gray-300">
                    {feature.description}
                  </p>
                </motion.div>
              ))}
            </div>
          </CardContent>
        </Card>
      </motion.div>
    </motion.div>
  )
}

export default ChapterOverview
