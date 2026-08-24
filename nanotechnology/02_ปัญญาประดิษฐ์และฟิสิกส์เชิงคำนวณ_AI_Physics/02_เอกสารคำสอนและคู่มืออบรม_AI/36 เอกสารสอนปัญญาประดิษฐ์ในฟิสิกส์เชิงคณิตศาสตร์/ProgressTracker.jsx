import React, { useState, useEffect } from 'react'
import { motion } from 'framer-motion'
import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/card.jsx'
import { Badge } from '@/components/ui/badge.jsx'
import { Progress } from '@/components/ui/progress.jsx'
import { 
  BookOpen, 
  CheckCircle, 
  Clock, 
  Target, 
  TrendingUp, 
  Award,
  Star,
  Calendar,
  BarChart3
} from 'lucide-react'

const ProgressTracker = ({ 
  currentChapter = 1,
  completedSections = [],
  quizScores = {},
  timeSpent = {},
  achievements = []
}) => {
  const [overallProgress, setOverallProgress] = useState(0)
  const [weeklyGoal, setWeeklyGoal] = useState(70) // percentage
  const [studyStreak, setStudyStreak] = useState(3)

  const chapters = [
    { id: 1, title: "บทนำสู่ปัญญาประดิษฐ์และฟิสิกส์เชิงคณิตศาสตร์", sections: 6, estimatedTime: 120 },
    { id: 2, title: "พื้นฐานทางคณิตศาสตร์สำหรับการเรียนรู้ของเครื่อง", sections: 4, estimatedTime: 150 },
    { id: 3, title: "การเรียนรู้แบบมีผู้สอน (Supervised Learning)", sections: 5, estimatedTime: 180 },
    { id: 4, title: "การเรียนรู้แบบไม่มีผู้สอน (Unsupervised Learning)", sections: 4, estimatedTime: 160 },
    { id: 5, title: "โครงข่ายประสาทเทียมและการเรียนรู้เชิงลึก", sections: 6, estimatedTime: 200 },
    { id: 6, title: "การจำลองและการสร้างแบบจำลองด้วย AI", sections: 5, estimatedTime: 170 },
    { id: 7, title: "การเรียนรู้เสริมกำลัง (Reinforcement Learning)", sections: 4, estimatedTime: 160 },
    { id: 8, title: "การค้นพบสมการเชิงฟิสิกส์ด้วย AI", sections: 5, estimatedTime: 180 },
    { id: 9, title: "การประยุกต์ใช้ขั้นสูงและแนวโน้มอนาคต", sections: 4, estimatedTime: 140 }
  ]

  const totalSections = chapters.reduce((sum, chapter) => sum + chapter.sections, 0)
  const totalEstimatedTime = chapters.reduce((sum, chapter) => sum + chapter.estimatedTime, 0)

  useEffect(() => {
    const completed = completedSections.length
    const progress = (completed / totalSections) * 100
    setOverallProgress(progress)
  }, [completedSections, totalSections])

  const getChapterProgress = (chapterId) => {
    const chapter = chapters.find(c => c.id === chapterId)
    if (!chapter) return 0
    
    const chapterSections = completedSections.filter(section => 
      section.startsWith(`chapter-${chapterId}`)
    )
    return (chapterSections.length / chapter.sections) * 100
  }

  const getAverageQuizScore = () => {
    const scores = Object.values(quizScores)
    if (scores.length === 0) return 0
    return scores.reduce((sum, score) => sum + score, 0) / scores.length
  }

  const getTotalTimeSpent = () => {
    return Object.values(timeSpent).reduce((sum, time) => sum + time, 0)
  }

  const getEstimatedTimeRemaining = () => {
    const completedTime = getTotalTimeSpent()
    return Math.max(0, totalEstimatedTime - completedTime)
  }

  const getPerformanceLevel = () => {
    const avgScore = getAverageQuizScore()
    if (avgScore >= 90) return { level: "เยี่ยม", color: "text-green-600", bg: "bg-green-100" }
    if (avgScore >= 80) return { level: "ดี", color: "text-blue-600", bg: "bg-blue-100" }
    if (avgScore >= 70) return { level: "พอใช้", color: "text-yellow-600", bg: "bg-yellow-100" }
    return { level: "ต้องปรับปรุง", color: "text-red-600", bg: "bg-red-100" }
  }

  const performance = getPerformanceLevel()

  return (
    <motion.div
      initial={{ opacity: 0, y: 20 }}
      animate={{ opacity: 1, y: 0 }}
      transition={{ duration: 0.5 }}
      className="w-full max-w-6xl mx-auto space-y-6"
    >
      {/* Overall Progress Card */}
      <Card className="border-2 border-green-200 dark:border-green-800">
        <CardHeader className="bg-gradient-to-r from-green-50 to-emerald-50 dark:from-green-900/20 dark:to-emerald-900/20">
          <div className="flex items-center justify-between">
            <div className="flex items-center space-x-3">
              <div className="p-2 bg-green-600 rounded-lg">
                <TrendingUp className="h-5 w-5 text-white" />
              </div>
              <div>
                <CardTitle className="text-xl font-bold text-green-900 dark:text-green-100">
                  ความคืบหน้าการเรียน
                </CardTitle>
                <p className="text-sm text-green-700 dark:text-green-300 mt-1">
                  ติดตามผลการเรียนรู้และความก้าวหน้า
                </p>
              </div>
            </div>
            <Badge className={`${performance.bg} ${performance.color} border-0`}>
              {performance.level}
            </Badge>
          </div>
        </CardHeader>
        
        <CardContent className="p-6">
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
            {/* Overall Progress */}
            <div className="space-y-3">
              <div className="flex items-center space-x-2">
                <BookOpen className="h-5 w-5 text-blue-600" />
                <span className="font-semibold text-gray-800 dark:text-gray-200">
                  ความคืบหน้ารวม
                </span>
              </div>
              <div className="space-y-2">
                <Progress value={overallProgress} className="h-3" />
                <div className="flex justify-between text-sm text-gray-600 dark:text-gray-400">
                  <span>{completedSections.length}/{totalSections} หัวข้อ</span>
                  <span>{overallProgress.toFixed(1)}%</span>
                </div>
              </div>
            </div>

            {/* Quiz Performance */}
            <div className="space-y-3">
              <div className="flex items-center space-x-2">
                <Target className="h-5 w-5 text-purple-600" />
                <span className="font-semibold text-gray-800 dark:text-gray-200">
                  คะแนนเฉลี่ย
                </span>
              </div>
              <div className="space-y-2">
                <div className="text-2xl font-bold text-purple-600">
                  {getAverageQuizScore().toFixed(1)}%
                </div>
                <div className="text-sm text-gray-600 dark:text-gray-400">
                  จาก {Object.keys(quizScores).length} แบบทดสอบ
                </div>
              </div>
            </div>

            {/* Time Spent */}
            <div className="space-y-3">
              <div className="flex items-center space-x-2">
                <Clock className="h-5 w-5 text-orange-600" />
                <span className="font-semibold text-gray-800 dark:text-gray-200">
                  เวลาที่ใช้
                </span>
              </div>
              <div className="space-y-2">
                <div className="text-2xl font-bold text-orange-600">
                  {Math.floor(getTotalTimeSpent() / 60)}h {getTotalTimeSpent() % 60}m
                </div>
                <div className="text-sm text-gray-600 dark:text-gray-400">
                  เหลือ ~{Math.floor(getEstimatedTimeRemaining() / 60)}h
                </div>
              </div>
            </div>

            {/* Study Streak */}
            <div className="space-y-3">
              <div className="flex items-center space-x-2">
                <Calendar className="h-5 w-5 text-red-600" />
                <span className="font-semibold text-gray-800 dark:text-gray-200">
                  ความต่อเนื่อง
                </span>
              </div>
              <div className="space-y-2">
                <div className="text-2xl font-bold text-red-600">
                  {studyStreak} วัน
                </div>
                <div className="text-sm text-gray-600 dark:text-gray-400">
                  เรียนต่อเนื่อง
                </div>
              </div>
            </div>
          </div>
        </CardContent>
      </Card>

      {/* Chapter Progress */}
      <Card>
        <CardHeader>
          <CardTitle className="flex items-center space-x-2">
            <BarChart3 className="h-5 w-5" />
            <span>ความคืบหน้าแต่ละบท</span>
          </CardTitle>
        </CardHeader>
        <CardContent>
          <div className="space-y-4">
            {chapters.map((chapter) => {
              const progress = getChapterProgress(chapter.id)
              const isCurrentChapter = chapter.id === currentChapter
              const isCompleted = progress === 100
              const quizScore = quizScores[`chapter-${chapter.id}`]
              
              return (
                <motion.div
                  key={chapter.id}
                  initial={{ opacity: 0, x: -20 }}
                  animate={{ opacity: 1, x: 0 }}
                  transition={{ delay: chapter.id * 0.1 }}
                  className={`p-4 rounded-lg border-2 ${
                    isCurrentChapter 
                      ? 'border-blue-300 bg-blue-50 dark:bg-blue-900/20' 
                      : 'border-gray-200 dark:border-gray-700'
                  }`}
                >
                  <div className="flex items-center justify-between mb-3">
                    <div className="flex items-center space-x-3">
                      <div className={`p-2 rounded-lg ${
                        isCompleted 
                          ? 'bg-green-600 text-white' 
                          : isCurrentChapter 
                            ? 'bg-blue-600 text-white'
                            : 'bg-gray-300 text-gray-600'
                      }`}>
                        {isCompleted ? (
                          <CheckCircle className="h-4 w-4" />
                        ) : (
                          <span className="text-sm font-bold">{chapter.id}</span>
                        )}
                      </div>
                      <div>
                        <h3 className="font-semibold text-gray-800 dark:text-gray-200">
                          บทที่ {chapter.id}: {chapter.title}
                        </h3>
                        <p className="text-sm text-gray-600 dark:text-gray-400">
                          {chapter.sections} หัวข้อ • ~{chapter.estimatedTime} นาที
                        </p>
                      </div>
                    </div>
                    
                    <div className="flex items-center space-x-3">
                      {quizScore && (
                        <Badge variant={quizScore >= 80 ? "default" : "secondary"}>
                          Quiz: {quizScore}%
                        </Badge>
                      )}
                      {isCurrentChapter && (
                        <Badge className="bg-blue-600 text-white">
                          กำลังเรียน
                        </Badge>
                      )}
                    </div>
                  </div>
                  
                  <div className="space-y-2">
                    <Progress value={progress} className="h-2" />
                    <div className="flex justify-between text-sm text-gray-600 dark:text-gray-400">
                      <span>ความคืบหน้า</span>
                      <span>{progress.toFixed(0)}%</span>
                    </div>
                  </div>
                </motion.div>
              )
            })}
          </div>
        </CardContent>
      </Card>

      {/* Achievements */}
      {achievements.length > 0 && (
        <Card>
          <CardHeader>
            <CardTitle className="flex items-center space-x-2">
              <Award className="h-5 w-5" />
              <span>ความสำเร็จ</span>
            </CardTitle>
          </CardHeader>
          <CardContent>
            <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
              {achievements.map((achievement, index) => (
                <motion.div
                  key={index}
                  initial={{ opacity: 0, scale: 0.9 }}
                  animate={{ opacity: 1, scale: 1 }}
                  transition={{ delay: index * 0.1 }}
                  className="p-4 bg-gradient-to-r from-yellow-50 to-orange-50 dark:from-yellow-900/20 dark:to-orange-900/20 rounded-lg border border-yellow-200 dark:border-yellow-800"
                >
                  <div className="flex items-center space-x-3">
                    <Star className="h-6 w-6 text-yellow-600" />
                    <div>
                      <h4 className="font-semibold text-yellow-900 dark:text-yellow-100">
                        {achievement.title}
                      </h4>
                      <p className="text-sm text-yellow-700 dark:text-yellow-300">
                        {achievement.description}
                      </p>
                    </div>
                  </div>
                </motion.div>
              ))}
            </div>
          </CardContent>
        </Card>
      )}

      {/* Weekly Goal */}
      <Card>
        <CardHeader>
          <CardTitle className="flex items-center space-x-2">
            <Target className="h-5 w-5" />
            <span>เป้าหมายสัปดาห์นี้</span>
          </CardTitle>
        </CardHeader>
        <CardContent>
          <div className="space-y-4">
            <div className="flex justify-between items-center">
              <span className="text-gray-700 dark:text-gray-300">
                ความคืบหน้าต่อเป้าหมาย
              </span>
              <span className="font-semibold">
                {overallProgress.toFixed(0)}% / {weeklyGoal}%
              </span>
            </div>
            <Progress 
              value={Math.min((overallProgress / weeklyGoal) * 100, 100)} 
              className="h-3" 
            />
            <p className="text-sm text-gray-600 dark:text-gray-400">
              {overallProgress >= weeklyGoal 
                ? "🎉 ยินดีด้วย! คุณบรรลุเป้าหมายสัปดาห์นี้แล้ว" 
                : `เหลืออีก ${(weeklyGoal - overallProgress).toFixed(1)}% เพื่อบรรลุเป้าหมาย`
              }
            </p>
          </div>
        </CardContent>
      </Card>
    </motion.div>
  )
}

export default ProgressTracker
