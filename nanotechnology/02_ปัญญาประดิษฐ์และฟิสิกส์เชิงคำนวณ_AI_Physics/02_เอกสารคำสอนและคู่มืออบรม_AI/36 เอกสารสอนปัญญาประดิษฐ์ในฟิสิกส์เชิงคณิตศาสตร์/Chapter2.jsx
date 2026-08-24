import { motion } from 'framer-motion'
import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/card.jsx'
import { Badge } from '@/components/ui/badge.jsx'
import { Button } from '@/components/ui/button.jsx'
import { BookOpen, ArrowRight, ArrowLeft, Construction } from 'lucide-react'

const Chapter2 = () => {
  return (
    <motion.div
      initial={{ opacity: 0, y: 20 }}
      animate={{ opacity: 1, y: 0 }}
      transition={{ duration: 0.5 }}
      className="max-w-4xl mx-auto space-y-8"
    >
      {/* Chapter Header */}
      <Card className="bg-gradient-to-r from-green-600 to-teal-600 text-white border-0">
        <CardContent className="p-8">
          <div className="flex items-center space-x-4 mb-4">
            <div className="p-3 bg-white/20 rounded-lg">
              <BookOpen className="h-8 w-8" />
            </div>
            <div>
              <Badge className="bg-white/20 text-white mb-2">บทที่ 2</Badge>
              <h1 className="text-3xl font-bold mb-2">พื้นฐานทางคณิตศาสตร์สำหรับการเรียนรู้ของเครื่อง</h1>
              <p className="text-xl opacity-90">Mathematical Foundations for Machine Learning</p>
            </div>
          </div>
        </CardContent>
      </Card>

      {/* Coming Soon Notice */}
      <Card className="border-2 border-dashed border-gray-300">
        <CardContent className="p-12 text-center">
          <Construction className="h-16 w-16 text-gray-400 mx-auto mb-4" />
          <h2 className="text-2xl font-bold text-gray-700 dark:text-gray-300 mb-4">
            เนื้อหาบทนี้กำลังพัฒนา
          </h2>
          <p className="text-gray-600 dark:text-gray-400 mb-6">
            บทที่ 2 จะครอบคลุมเนื้อหาเกี่ยวกับพีชคณิตเชิงเส้น แคลคูลัส และทฤษฎีความน่าจะเป็น
            พร้อมการประยุกต์ใช้ในการเรียนรู้ของเครื่อง
          </p>
          <div className="space-y-2 text-sm text-gray-500">
            <p>• พีชคณิตเชิงเส้นและการดำเนินการเมทริกซ์</p>
            <p>• แคลคูลัสหลายตัวแปรและการหาค่าเหมาะสมที่สุด</p>
            <p>• ทฤษฎีความน่าจะเป็นและสถิติ</p>
            <p>• การวิเคราะห์ฟูเรียร์และการประมวลผลสัญญาณ</p>
          </div>
        </CardContent>
      </Card>

      {/* Navigation */}
      <div className="flex justify-between">
        <Button variant="outline">
          <ArrowLeft className="h-4 w-4 mr-2" />
          บทที่ 1: บทนำสู่ AI และฟิสิกส์
        </Button>
        <Button className="bg-blue-600 hover:bg-blue-700">
          บทที่ 3: Supervised Learning
          <ArrowRight className="h-4 w-4 ml-2" />
        </Button>
      </div>
    </motion.div>
  )
}

export default Chapter2
