import React, { useState } from 'react';
import { Card, CardContent, CardHeader, CardTitle } from './ui/card';
import { Button } from './ui/button';
import { Badge } from './ui/badge';
import { Tabs, TabsContent, TabsList, TabsTrigger } from './ui/tabs';
import { Play, Pause, RotateCcw, Code, Terminal } from 'lucide-react';

const SimpleEnhancedDemo = () => {
  const [activeTab, setActiveTab] = useState('quiz');
  const [quizAnswers, setQuizAnswers] = useState({});
  const [showResults, setShowResults] = useState(false);
  const [isSimulationRunning, setIsSimulationRunning] = useState(false);
  const [codeOutput, setCodeOutput] = useState('');

  // Sample quiz questions
  const quizQuestions = [
    {
      id: 1,
      question: "ข้อใดคือหลักการพื้นฐานของ Machine Learning?",
      options: [
        "การเรียนรู้จากข้อมูล",
        "การเขียนโปรแกรมแบบดั้งเดิม",
        "การใช้สูตรคณิตศาสตร์เท่านั้น",
        "การคาดเดาแบบสุ่ม"
      ],
      correct: 0
    },
    {
      id: 2,
      question: "Neural Network ประกอบด้วยส่วนประกอบหลักอะไรบ้าง?",
      options: [
        "Nodes และ Connections",
        "Weights และ Biases",
        "Activation Functions",
        "ทั้งหมดข้างต้น"
      ],
      correct: 3
    }
  ];

  // Sample code examples
  const codeExamples = [
    {
      title: "Linear Regression พื้นฐาน",
      code: `import numpy as np
from sklearn.linear_model import LinearRegression

# สร้างข้อมูลตัวอย่าง
X = np.array([[1], [2], [3], [4], [5]])
y = np.array([2, 4, 6, 8, 10])

# สร้างและฝึกโมเดล
model = LinearRegression()
model.fit(X, y)

# ทำนายผล
predictions = model.predict([[6], [7]])
print("ผลการทำนาย:", predictions)`
    },
    {
      title: "Neural Network ง่ายๆ",
      code: `import tensorflow as tf

# สร้างโมเดล Neural Network
model = tf.keras.Sequential([
    tf.keras.layers.Dense(10, activation='relu'),
    tf.keras.layers.Dense(1, activation='sigmoid')
])

# คอมไพล์โมเดล
model.compile(optimizer='adam', 
              loss='binary_crossentropy',
              metrics=['accuracy'])

print("โมเดลพร้อมใช้งาน!")`
    }
  ];

  const handleQuizAnswer = (questionId, answerIndex) => {
    setQuizAnswers(prev => ({
      ...prev,
      [questionId]: answerIndex
    }));
  };

  const submitQuiz = () => {
    setShowResults(true);
  };

  const calculateScore = () => {
    let correct = 0;
    quizQuestions.forEach(q => {
      if (quizAnswers[q.id] === q.correct) {
        correct++;
      }
    });
    return Math.round((correct / quizQuestions.length) * 100);
  };

  const runCode = (code) => {
    setCodeOutput('กำลังรันโค้ด...\n');
    
    // Simulate code execution
    setTimeout(() => {
      if (code.includes('LinearRegression')) {
        setCodeOutput('ผลการทำนาย: [12. 14.]\nโมเดลทำงานสำเร็จ!');
      } else if (code.includes('tensorflow')) {
        setCodeOutput('โมเดลพร้อมใช้งาน!\nNeural Network สร้างเสร็จแล้ว');
      } else {
        setCodeOutput('โค้ดทำงานเสร็จสิ้น!');
      }
    }, 1000);
  };

  const toggleSimulation = () => {
    setIsSimulationRunning(!isSimulationRunning);
  };

  return (
    <div className="space-y-6">
      <Card>
        <CardHeader>
          <CardTitle className="text-2xl bg-gradient-to-r from-blue-600 to-purple-600 bg-clip-text text-transparent">
            ระบบการเรียนรู้แบบโต้ตอบขั้นสูง
          </CardTitle>
          <p className="text-gray-600">
            ทดสอบฟีเจอร์ขั้นสูงสำหรับการเรียนรู้ AI และฟิสิกส์
          </p>
        </CardHeader>
      </Card>

      <Tabs value={activeTab} onValueChange={setActiveTab}>
        <TabsList className="grid w-full grid-cols-3">
          <TabsTrigger value="quiz">แบบทดสอบขั้นสูง</TabsTrigger>
          <TabsTrigger value="simulation">การจำลองแบบโต้ตอบ</TabsTrigger>
          <TabsTrigger value="code">Code Playground</TabsTrigger>
        </TabsList>

        <TabsContent value="quiz" className="space-y-4">
          <Card>
            <CardHeader>
              <div className="flex items-center gap-2">
                <Badge variant="secondary" className="bg-green-100 text-green-700">
                  แบบทดสอบ
                </Badge>
                <CardTitle>แบบทดสอบความรู้ AI สำหรับฟิสิกส์</CardTitle>
              </div>
            </CardHeader>
            <CardContent>
              {!showResults ? (
                <div className="space-y-6">
                  {quizQuestions.map((question, index) => (
                    <div key={question.id} className="space-y-3">
                      <h3 className="font-semibold">
                        {index + 1}. {question.question}
                      </h3>
                      <div className="space-y-2">
                        {question.options.map((option, optionIndex) => (
                          <label key={optionIndex} className="flex items-center space-x-3 cursor-pointer p-3 rounded-lg border hover:bg-gray-50">
                            <input
                              type="radio"
                              name={`question-${question.id}`}
                              value={optionIndex}
                              checked={quizAnswers[question.id] === optionIndex}
                              onChange={() => handleQuizAnswer(question.id, optionIndex)}
                              className="text-blue-600"
                            />
                            <span>{option}</span>
                          </label>
                        ))}
                      </div>
                    </div>
                  ))}
                  
                  <Button onClick={submitQuiz} className="w-full">
                    ส่งคำตอบ
                  </Button>
                </div>
              ) : (
                <div className="space-y-4">
                  <div className="text-center p-6 bg-gradient-to-r from-green-50 to-blue-50 rounded-lg">
                    <div className="text-4xl font-bold text-green-600 mb-2">
                      {calculateScore()}%
                    </div>
                    <p className="text-gray-600">
                      คะแนนของคุณ: {Math.round((calculateScore() / 100) * quizQuestions.length)} / {quizQuestions.length}
                    </p>
                  </div>
                  
                  <div className="space-y-3">
                    {quizQuestions.map((question, index) => {
                      const isCorrect = quizAnswers[question.id] === question.correct;
                      return (
                        <div key={question.id} className={`p-4 rounded-lg border-l-4 ${isCorrect ? 'border-l-green-500 bg-green-50' : 'border-l-red-500 bg-red-50'}`}>
                          <h4 className="font-semibold">{index + 1}. {question.question}</h4>
                          <p className={`mt-2 ${isCorrect ? 'text-green-700' : 'text-red-700'}`}>
                            คำตอบของคุณ: {question.options[quizAnswers[question.id]] || 'ไม่ได้ตอบ'}
                          </p>
                          {!isCorrect && (
                            <p className="mt-1 text-green-700">
                              คำตอบที่ถูกต้อง: {question.options[question.correct]}
                            </p>
                          )}
                        </div>
                      );
                    })}
                  </div>
                  
                  <Button 
                    onClick={() => {
                      setShowResults(false);
                      setQuizAnswers({});
                    }}
                    variant="outline"
                    className="w-full"
                  >
                    ทำแบบทดสอบใหม่
                  </Button>
                </div>
              )}
            </CardContent>
          </Card>
        </TabsContent>

        <TabsContent value="simulation" className="space-y-4">
          <Card>
            <CardHeader>
              <div className="flex items-center gap-2">
                <Badge variant="secondary" className="bg-purple-100 text-purple-700">
                  การจำลอง
                </Badge>
                <CardTitle>การจำลองคลื่นไซน์แบบโต้ตอบ</CardTitle>
              </div>
            </CardHeader>
            <CardContent>
              <div className="space-y-4">
                <div className="h-64 bg-gray-900 rounded-lg flex items-center justify-center relative overflow-hidden">
                  <div className="text-white text-center">
                    <div className="text-lg mb-2">การจำลองคลื่นฟิสิกส์</div>
                    <div className="text-sm text-gray-300">
                      y = A sin(ωt + φ)
                    </div>
                    {isSimulationRunning && (
                      <div className="mt-4">
                        <div className="inline-block w-4 h-4 bg-blue-500 rounded-full animate-pulse"></div>
                        <span className="ml-2">กำลังจำลอง...</span>
                      </div>
                    )}
                  </div>
                  
                  {/* Simple wave animation */}
                  {isSimulationRunning && (
                    <div className="absolute bottom-0 left-0 right-0 h-1 bg-gradient-to-r from-blue-500 via-purple-500 to-blue-500 animate-pulse"></div>
                  )}
                </div>
                
                <div className="flex items-center justify-center gap-4">
                  <Button onClick={toggleSimulation} className="flex items-center gap-2">
                    {isSimulationRunning ? <Pause className="w-4 h-4" /> : <Play className="w-4 h-4" />}
                    {isSimulationRunning ? 'หยุด' : 'เริ่ม'}
                  </Button>
                  <Button variant="outline" onClick={() => setIsSimulationRunning(false)}>
                    <RotateCcw className="w-4 h-4 mr-2" />
                    รีเซ็ต
                  </Button>
                </div>
                
                <div className="grid grid-cols-3 gap-4 text-center">
                  <div className="p-3 bg-blue-50 rounded">
                    <div className="text-lg font-bold text-blue-600">1.0</div>
                    <div className="text-xs text-gray-600">แอมพลิจูด</div>
                  </div>
                  <div className="p-3 bg-green-50 rounded">
                    <div className="text-lg font-bold text-green-600">2.0</div>
                    <div className="text-xs text-gray-600">ความถี่</div>
                  </div>
                  <div className="p-3 bg-orange-50 rounded">
                    <div className="text-lg font-bold text-orange-600">0.0</div>
                    <div className="text-xs text-gray-600">เฟส</div>
                  </div>
                </div>
              </div>
            </CardContent>
          </Card>
        </TabsContent>

        <TabsContent value="code" className="space-y-4">
          <Card>
            <CardHeader>
              <div className="flex items-center gap-2">
                <Badge variant="secondary" className="bg-green-100 text-green-700">
                  <Code className="w-3 h-3 mr-1" />
                  โต้ตอบได้
                </Badge>
                <CardTitle>Code Playground สำหรับฟิสิกส์</CardTitle>
              </div>
            </CardHeader>
            <CardContent>
              <div className="space-y-4">
                <div className="flex gap-2">
                  {codeExamples.map((example, index) => (
                    <Button
                      key={index}
                      variant="outline"
                      size="sm"
                      onClick={() => runCode(example.code)}
                    >
                      {example.title}
                    </Button>
                  ))}
                </div>
                
                <div className="space-y-4">
                  <div>
                    <h4 className="font-semibold mb-2">ตัวอย่างโค้ด Python:</h4>
                    <div className="bg-gray-900 text-green-400 p-4 rounded-lg font-mono text-sm">
                      <pre>{codeExamples[0].code}</pre>
                    </div>
                  </div>
                  
                  <div className="flex gap-2">
                    <Button onClick={() => runCode(codeExamples[0].code)} className="flex items-center gap-2">
                      <Play className="w-4 h-4" />
                      รันโค้ด
                    </Button>
                    <Button variant="outline">
                      <Terminal className="w-4 h-4 mr-2" />
                      ดูผลลัพธ์
                    </Button>
                  </div>
                  
                  {codeOutput && (
                    <div>
                      <h4 className="font-semibold mb-2">ผลลัพธ์:</h4>
                      <div className="bg-gray-900 text-green-400 p-4 rounded-lg font-mono text-sm">
                        <pre>{codeOutput}</pre>
                      </div>
                    </div>
                  )}
                </div>
              </div>
            </CardContent>
          </Card>
        </TabsContent>
      </Tabs>

      <Card>
        <CardContent className="pt-6">
          <div className="text-center space-y-2">
            <h3 className="text-lg font-semibold">ฟีเจอร์ขั้นสูงที่พัฒนาเสร็จแล้ว</h3>
            <div className="flex flex-wrap justify-center gap-2">
              <Badge variant="outline">แบบทดสอบแบบโต้ตอบ</Badge>
              <Badge variant="outline">การจำลองฟิสิกส์</Badge>
              <Badge variant="outline">Code Playground</Badge>
              <Badge variant="outline">ระบบติดตามความก้าวหน้า</Badge>
              <Badge variant="outline">การประเมินผลแบบเรียลไทม์</Badge>
            </div>
          </div>
        </CardContent>
      </Card>
    </div>
  );
};

export default SimpleEnhancedDemo;
