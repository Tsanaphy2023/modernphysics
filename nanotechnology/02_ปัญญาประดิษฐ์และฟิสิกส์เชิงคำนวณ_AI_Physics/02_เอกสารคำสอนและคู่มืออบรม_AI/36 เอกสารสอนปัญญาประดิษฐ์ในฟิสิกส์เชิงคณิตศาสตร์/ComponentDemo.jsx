import React, { useState } from 'react'
import { motion } from 'framer-motion'
import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/card.jsx'
import { Button } from '@/components/ui/button.jsx'
import { Badge } from '@/components/ui/badge.jsx'
import { Tabs, TabsContent, TabsList, TabsTrigger } from '@/components/ui/tabs.jsx'
import CodePlayground from './CodePlayground.jsx'
import InteractiveSimulation from './InteractiveSimulation.jsx'
import ProgressTracker from './ProgressTracker.jsx'
import { Sparkles, Code, Activity, TrendingUp } from 'lucide-react'

const ComponentDemo = () => {
  const [activeDemo, setActiveDemo] = useState('playground')

  // Sample data for ProgressTracker
  const sampleProgress = {
    currentChapter: 1,
    completedSections: [
      'chapter-1-section-1',
      'chapter-1-section-2',
      'chapter-1-section-3'
    ],
    quizScores: {
      'chapter-1': 100,
      'chapter-2': 85
    },
    timeSpent: {
      'chapter-1': 120,
      'chapter-2': 90
    },
    achievements: [
      {
        title: "ผู้เรียนรู้อย่างต่อเนื่อง",
        description: "เรียนต่อเนื่อง 3 วันติดต่อกัน"
      },
      {
        title: "นักแก้ปัญหา",
        description: "ทำแบบทดสอบได้คะแนนเต็ม"
      }
    ]
  }

  // Sample code examples for CodePlayground
  const codeExamples = [
    {
      title: "Linear Regression",
      code: `import numpy as np
import matplotlib.pyplot as plt

# สร้างข้อมูลตัวอย่าง
x = np.linspace(0, 10, 100)
y = 2 * x + 1 + np.random.normal(0, 1, 100)

# คำนวณ Linear Regression
A = np.vstack([x, np.ones(len(x))]).T
m, c = np.linalg.lstsq(A, y, rcond=None)[0]

print(f"สมการเส้นตรง: y = {m:.2f}x + {c:.2f}")
print("กราฟจะแสดงข้อมูลและเส้นถดถอย")`
    },
    {
      title: "Neural Network",
      code: `import numpy as np

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def neural_network(X, W1, W2):
    # Hidden layer
    z1 = np.dot(X, W1)
    a1 = sigmoid(z1)
    
    # Output layer
    z2 = np.dot(a1, W2)
    output = sigmoid(z2)
    
    return output

# ตัวอย่างการใช้งาน
X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
W1 = np.random.randn(2, 3)
W2 = np.random.randn(3, 1)

result = neural_network(X, W1, W2)
print("ผลลัพธ์จาก Neural Network:")
print(result)`
    },
    {
      title: "Physics Simulation",
      code: `import numpy as np

# จำลองการเคลื่อนที่แบบโปรเจกไทล์
def projectile_motion(v0, angle, t):
    g = 9.81  # ความเร่งโน้มถ่วง
    
    # แปลงมุมเป็นเรเดียน
    angle_rad = np.radians(angle)
    
    # คำนวณตำแหน่ง
    x = v0 * np.cos(angle_rad) * t
    y = v0 * np.sin(angle_rad) * t - 0.5 * g * t**2
    
    return x, y

# ตัวอย่างการใช้งาน
v0 = 20  # ความเร็วต้น (m/s)
angle = 45  # มุมยิง (องศา)
t = np.linspace(0, 3, 100)

x, y = projectile_motion(v0, angle, t)
print(f"ระยะทางสูงสุด: {np.max(x):.2f} เมตร")
print(f"ความสูงสูงสุด: {np.max(y):.2f} เมตร")`
    }
  ]

  return (
    <motion.div
      initial={{ opacity: 0, y: 20 }}
      animate={{ opacity: 1, y: 0 }}
      transition={{ duration: 0.5 }}
      className="max-w-7xl mx-auto space-y-8"
    >
      {/* Header */}
      <Card className="bg-gradient-to-r from-blue-600 to-purple-600 text-white border-0">
        <CardContent className="p-8">
          <div className="flex items-center space-x-4 mb-4">
            <div className="p-3 bg-white/20 rounded-lg">
              <Sparkles className="h-8 w-8" />
            </div>
            <div>
              <h1 className="text-3xl font-bold mb-2">Interactive Components Demo</h1>
              <p className="text-xl opacity-90">ทดสอบคอมโพเนนต์แบบโต้ตอบสำหรับคอร์ส AI Physics</p>
            </div>
          </div>
        </CardContent>
      </Card>

      {/* Component Tabs */}
      <Tabs value={activeDemo} onValueChange={setActiveDemo} className="w-full">
        <TabsList className="grid w-full grid-cols-4">
          <TabsTrigger value="playground" className="flex items-center space-x-2">
            <Code className="h-4 w-4" />
            <span>Code Playground</span>
          </TabsTrigger>
          <TabsTrigger value="wave" className="flex items-center space-x-2">
            <Activity className="h-4 w-4" />
            <span>Wave Simulation</span>
          </TabsTrigger>
          <TabsTrigger value="neural" className="flex items-center space-x-2">
            <Activity className="h-4 w-4" />
            <span>Neural Network</span>
          </TabsTrigger>
          <TabsTrigger value="progress" className="flex items-center space-x-2">
            <TrendingUp className="h-4 w-4" />
            <span>Progress Tracker</span>
          </TabsTrigger>
        </TabsList>

        <TabsContent value="playground" className="mt-6">
          <div className="space-y-6">
            <div className="text-center">
              <h2 className="text-2xl font-bold text-gray-800 dark:text-gray-200 mb-2">
                Code Playground Demo
              </h2>
              <p className="text-gray-600 dark:text-gray-400">
                ทดลองเขียนและรันโค้ด Python สำหรับการเรียนรู้ AI และฟิสิกส์
              </p>
            </div>
            <CodePlayground
              title="AI Physics Code Playground"
              description="ทดลองเขียนโค้ด Python สำหรับ AI และฟิสิกส์"
              initialCode={codeExamples[0].code}
              examples={codeExamples}
            />
          </div>
        </TabsContent>

        <TabsContent value="wave" className="mt-6">
          <div className="space-y-6">
            <div className="text-center">
              <h2 className="text-2xl font-bold text-gray-800 dark:text-gray-200 mb-2">
                Wave Simulation Demo
              </h2>
              <p className="text-gray-600 dark:text-gray-400">
                การจำลองคลื่นแบบโต้ตอบพร้อมการควบคุมพารามิเตอร์
              </p>
            </div>
            <InteractiveSimulation
              title="การจำลองคลื่นไซน์"
              description="ศึกษาพฤติกรรมของคลื่นไซน์และการเปลี่ยนแปลงพารามิเตอร์"
              type="wave"
              parameters={{ amplitude: 1.5, frequency: 2, speed: 1 }}
            />
          </div>
        </TabsContent>

        <TabsContent value="neural" className="mt-6">
          <div className="space-y-6">
            <div className="text-center">
              <h2 className="text-2xl font-bold text-gray-800 dark:text-gray-200 mb-2">
                Neural Network Simulation Demo
              </h2>
              <p className="text-gray-600 dark:text-gray-400">
                การจำลองโครงข่ายประสาทเทียมแบบโต้ตอบ
              </p>
            </div>
            <InteractiveSimulation
              title="การจำลองโครงข่ายประสาทเทียม"
              description="ดูการส่งผ่านสัญญาณในโครงข่ายประสาทเทียม"
              type="neural_network"
              parameters={{ speed: 1.5 }}
            />
          </div>
        </TabsContent>

        <TabsContent value="progress" className="mt-6">
          <div className="space-y-6">
            <div className="text-center">
              <h2 className="text-2xl font-bold text-gray-800 dark:text-gray-200 mb-2">
                Progress Tracker Demo
              </h2>
              <p className="text-gray-600 dark:text-gray-400">
                ระบบติดตามความคืบหน้าการเรียนรู้แบบครอบคลุม
              </p>
            </div>
            <ProgressTracker {...sampleProgress} />
          </div>
        </TabsContent>
      </Tabs>

      {/* Features Overview */}
      <Card>
        <CardHeader>
          <CardTitle>คุณสมบัติของคอมโพเนนต์แบบโต้ตอบ</CardTitle>
        </CardHeader>
        <CardContent>
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
            <div className="space-y-3">
              <div className="p-3 bg-blue-100 dark:bg-blue-900/20 rounded-lg">
                <Code className="h-6 w-6 text-blue-600" />
              </div>
              <h3 className="font-semibold">Code Playground</h3>
              <p className="text-sm text-gray-600 dark:text-gray-400">
                เขียนและรันโค้ด Python แบบเรียลไทม์พร้อมตัวอย่างโค้ดสำเร็จรูป
              </p>
            </div>

            <div className="space-y-3">
              <div className="p-3 bg-purple-100 dark:bg-purple-900/20 rounded-lg">
                <Activity className="h-6 w-6 text-purple-600" />
              </div>
              <h3 className="font-semibold">Interactive Simulations</h3>
              <p className="text-sm text-gray-600 dark:text-gray-400">
                การจำลองปรากฏการณ์ทางฟิสิกส์แบบโต้ตอบพร้อมการควบคุมพารามิเตอร์
              </p>
            </div>

            <div className="space-y-3">
              <div className="p-3 bg-green-100 dark:bg-green-900/20 rounded-lg">
                <TrendingUp className="h-6 w-6 text-green-600" />
              </div>
              <h3 className="font-semibold">Progress Tracking</h3>
              <p className="text-sm text-gray-600 dark:text-gray-400">
                ติดตามความคืบหน้าการเรียนรู้แบบละเอียดพร้อมระบบความสำเร็จ
              </p>
            </div>

            <div className="space-y-3">
              <div className="p-3 bg-orange-100 dark:bg-orange-900/20 rounded-lg">
                <Sparkles className="h-6 w-6 text-orange-600" />
              </div>
              <h3 className="font-semibold">Modern UI/UX</h3>
              <p className="text-sm text-gray-600 dark:text-gray-400">
                ออกแบบด้วย Tailwind CSS และ Framer Motion สำหรับประสบการณ์ที่ดี
              </p>
            </div>
          </div>
        </CardContent>
      </Card>
    </motion.div>
  )
}

export default ComponentDemo
