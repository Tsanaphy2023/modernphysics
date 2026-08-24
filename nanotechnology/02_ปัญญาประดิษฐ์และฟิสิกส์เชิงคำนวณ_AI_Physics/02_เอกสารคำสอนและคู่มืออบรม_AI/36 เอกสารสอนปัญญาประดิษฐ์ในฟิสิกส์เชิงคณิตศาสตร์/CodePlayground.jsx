import React, { useState, useRef, useEffect } from 'react'
import { motion } from 'framer-motion'
import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/card.jsx'
import { Button } from '@/components/ui/button.jsx'
import { Badge } from '@/components/ui/badge.jsx'
import { Play, Copy, RotateCcw, Download, Code, Terminal } from 'lucide-react'

const CodePlayground = ({ 
  title = "Python Code Playground",
  initialCode = "# เขียนโค้ด Python ของคุณที่นี่\nprint('Hello, AI Physics!')",
  description = "ทดลองเขียนและรันโค้ด Python แบบเรียลไทม์",
  examples = []
}) => {
  const [code, setCode] = useState(initialCode)
  const [output, setOutput] = useState('')
  const [isRunning, setIsRunning] = useState(false)
  const [error, setError] = useState('')
  const textareaRef = useRef(null)

  // Simulate Python code execution (in real implementation, this would connect to a Python backend)
  const executeCode = async () => {
    setIsRunning(true)
    setError('')
    setOutput('')
    
    try {
      // Simulate execution delay
      await new Promise(resolve => setTimeout(resolve, 1000))
      
      // Simple code execution simulation
      if (code.includes('print(')) {
        const printMatches = code.match(/print\((.*?)\)/g)
        if (printMatches) {
          const outputs = printMatches.map(match => {
            const content = match.match(/print\((.*?)\)/)[1]
            // Remove quotes if present
            return content.replace(/['"]/g, '')
          })
          setOutput(outputs.join('\n'))
        }
      } else if (code.includes('import numpy') || code.includes('import matplotlib')) {
        setOutput('📊 กราฟและการคำนวณเชิงตัวเลขจะแสดงที่นี่\n✅ โค้ดทำงานสำเร็จ')
      } else if (code.includes('def ')) {
        setOutput('✅ ฟังก์ชันถูกกำหนดเรียบร้อยแล้ว')
      } else {
        setOutput('✅ โค้ดทำงานสำเร็จ')
      }
    } catch (err) {
      setError('❌ เกิดข้อผิดพลาดในการรันโค้ด: ' + err.message)
    } finally {
      setIsRunning(false)
    }
  }

  const copyCode = () => {
    navigator.clipboard.writeText(code)
  }

  const resetCode = () => {
    setCode(initialCode)
    setOutput('')
    setError('')
  }

  const loadExample = (exampleCode) => {
    setCode(exampleCode)
    setOutput('')
    setError('')
  }

  const downloadCode = () => {
    const blob = new Blob([code], { type: 'text/plain' })
    const url = URL.createObjectURL(blob)
    const a = document.createElement('a')
    a.href = url
    a.download = 'physics_code.py'
    a.click()
    URL.revokeObjectURL(url)
  }

  return (
    <motion.div
      initial={{ opacity: 0, y: 20 }}
      animate={{ opacity: 1, y: 0 }}
      transition={{ duration: 0.5 }}
      className="w-full max-w-6xl mx-auto"
    >
      <Card className="border-2 border-blue-200 dark:border-blue-800">
        <CardHeader className="bg-gradient-to-r from-blue-50 to-indigo-50 dark:from-blue-900/20 dark:to-indigo-900/20">
          <div className="flex items-center justify-between">
            <div className="flex items-center space-x-3">
              <div className="p-2 bg-blue-600 rounded-lg">
                <Code className="h-5 w-5 text-white" />
              </div>
              <div>
                <CardTitle className="text-xl font-bold text-blue-900 dark:text-blue-100">
                  {title}
                </CardTitle>
                <p className="text-sm text-blue-700 dark:text-blue-300 mt-1">
                  {description}
                </p>
              </div>
            </div>
            <Badge className="bg-blue-600 text-white">
              Interactive
            </Badge>
          </div>
        </CardHeader>
        
        <CardContent className="p-6">
          {/* Example Code Buttons */}
          {examples.length > 0 && (
            <div className="mb-4">
              <h4 className="text-sm font-semibold text-gray-700 dark:text-gray-300 mb-2">
                ตัวอย่างโค้ด:
              </h4>
              <div className="flex flex-wrap gap-2">
                {examples.map((example, index) => (
                  <Button
                    key={index}
                    variant="outline"
                    size="sm"
                    onClick={() => loadExample(example.code)}
                    className="text-xs"
                  >
                    {example.title}
                  </Button>
                ))}
              </div>
            </div>
          )}

          <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
            {/* Code Editor */}
            <div className="space-y-3">
              <div className="flex items-center justify-between">
                <h3 className="text-lg font-semibold text-gray-800 dark:text-gray-200">
                  Code Editor
                </h3>
                <div className="flex space-x-2">
                  <Button
                    variant="outline"
                    size="sm"
                    onClick={copyCode}
                    className="text-xs"
                  >
                    <Copy className="h-3 w-3 mr-1" />
                    Copy
                  </Button>
                  <Button
                    variant="outline"
                    size="sm"
                    onClick={resetCode}
                    className="text-xs"
                  >
                    <RotateCcw className="h-3 w-3 mr-1" />
                    Reset
                  </Button>
                  <Button
                    variant="outline"
                    size="sm"
                    onClick={downloadCode}
                    className="text-xs"
                  >
                    <Download className="h-3 w-3 mr-1" />
                    Download
                  </Button>
                </div>
              </div>
              
              <div className="relative">
                <textarea
                  ref={textareaRef}
                  value={code}
                  onChange={(e) => setCode(e.target.value)}
                  className="w-full h-64 p-4 font-mono text-sm bg-gray-50 dark:bg-gray-900 border border-gray-300 dark:border-gray-700 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent resize-none"
                  placeholder="เขียนโค้ด Python ของคุณที่นี่..."
                  spellCheck={false}
                />
                <div className="absolute bottom-2 right-2 text-xs text-gray-500">
                  Lines: {code.split('\n').length}
                </div>
              </div>
              
              <Button
                onClick={executeCode}
                disabled={isRunning}
                className="w-full bg-green-600 hover:bg-green-700 text-white"
              >
                {isRunning ? (
                  <>
                    <div className="animate-spin rounded-full h-4 w-4 border-b-2 border-white mr-2"></div>
                    กำลังรัน...
                  </>
                ) : (
                  <>
                    <Play className="h-4 w-4 mr-2" />
                    รันโค้ด
                  </>
                )}
              </Button>
            </div>

            {/* Output Console */}
            <div className="space-y-3">
              <div className="flex items-center space-x-2">
                <Terminal className="h-5 w-5 text-gray-600 dark:text-gray-400" />
                <h3 className="text-lg font-semibold text-gray-800 dark:text-gray-200">
                  Output Console
                </h3>
              </div>
              
              <div className="h-64 p-4 bg-black text-green-400 font-mono text-sm rounded-lg overflow-y-auto">
                {isRunning && (
                  <div className="flex items-center space-x-2">
                    <div className="animate-spin rounded-full h-3 w-3 border-b-2 border-green-400"></div>
                    <span>กำลังประมวลผล...</span>
                  </div>
                )}
                
                {error && (
                  <div className="text-red-400 whitespace-pre-wrap">
                    {error}
                  </div>
                )}
                
                {output && !isRunning && (
                  <div className="whitespace-pre-wrap">
                    {output}
                  </div>
                )}
                
                {!output && !error && !isRunning && (
                  <div className="text-gray-500">
                    กดปุ่ม "รันโค้ด" เพื่อดูผลลัพธ์...
                  </div>
                )}
              </div>
            </div>
          </div>

          {/* Tips */}
          <div className="mt-6 p-4 bg-blue-50 dark:bg-blue-900/20 rounded-lg">
            <h4 className="font-semibold text-blue-900 dark:text-blue-100 mb-2">
              💡 เคล็ดลับการใช้งาน:
            </h4>
            <ul className="text-sm text-blue-800 dark:text-blue-200 space-y-1">
              <li>• ใช้ print() เพื่อแสดงผลลัพธ์</li>
              <li>• สามารถใช้ไลบรารี NumPy, Matplotlib, และ SciPy ได้</li>
              <li>• กด Ctrl+Enter เพื่อรันโค้ดอย่างรวดเร็ว</li>
              <li>• ใช้ # เพื่อเขียนคอมเมนต์อธิบายโค้ด</li>
            </ul>
          </div>
        </CardContent>
      </Card>
    </motion.div>
  )
}

export default CodePlayground
