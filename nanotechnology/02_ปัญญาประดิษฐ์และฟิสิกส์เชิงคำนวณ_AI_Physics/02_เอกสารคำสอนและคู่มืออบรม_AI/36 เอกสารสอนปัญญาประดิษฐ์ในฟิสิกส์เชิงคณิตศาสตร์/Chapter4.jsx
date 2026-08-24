import { motion } from 'framer-motion'
import { Card, CardContent } from '@/components/ui/card.jsx'
import { Badge } from '@/components/ui/badge.jsx'
import { Button } from '@/components/ui/button.jsx'
import { BookOpen, ArrowRight, ArrowLeft, Construction } from 'lucide-react'

const Chapter4 = () => {
  return (
    <motion.div
      initial={{ opacity: 0, y: 20 }}
      animate={{ opacity: 1, y: 0 }}
      transition={{ duration: 0.5 }}
      className="max-w-4xl mx-auto space-y-8"
    >
      <Card className="bg-gradient-to-r from-indigo-600 to-purple-600 text-white border-0">
        <CardContent className="p-8">
          <div className="flex items-center space-x-4 mb-4">
            <div className="p-3 bg-white/20 rounded-lg">
              <BookOpen className="h-8 w-8" />
            </div>
            <div>
              <Badge className="bg-white/20 text-white mb-2">บทที่ 4</Badge>
              <h1 className="text-3xl font-bold mb-2">การเรียนรู้แบบไม่มีผู้สอน (Unsupervised Learning)</h1>
              <p className="text-xl opacity-90">Unsupervised Learning and Pattern Discovery</p>
            </div>
          </div>
        </CardContent>
      </Card>

      <Card className="border-2 border-dashed border-gray-300">
        <CardContent className="p-12 text-center">
          <Construction className="h-16 w-16 text-gray-400 mx-auto mb-4" />
          <h2 className="text-2xl font-bold text-gray-700 dark:text-gray-300 mb-4">
            เนื้อหาบทนี้กำลังพัฒนา
          </h2>
          <p className="text-gray-600 dark:text-gray-400 mb-6">
            บทที่ 4 จะมีเนื้อหาแบบโต้ตอบครบถ้วน รวมถึงการจำลอง แบบทดสอบ และ Code Playground
          </p>
        </CardContent>
      </Card>

      <div className="flex justify-between">
        <Button variant="outline">
          <ArrowLeft className="h-4 w-4 mr-2" />
          บทที่ 3: Supervised Learning
        </Button>
        <Button className="bg-blue-600 hover:bg-blue-700">
          บทที่ 5: Neural Networks
          <ArrowRight className="h-4 w-4 ml-2" />
        </Button>
      </div>
    </motion.div>
  )
}

export default Chapter4
