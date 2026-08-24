import React, { useState } from 'react';
import { motion } from 'framer-motion';
import { Lightbulb, BookOpen, Code, HelpCircle, CheckCircle, XCircle } from 'lucide-react';
import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/card';
import { Button } from '@/components/ui/button';
import { Tabs, TabsContent, TabsList, TabsTrigger } from '@/components/ui/tabs';
import { Accordion, AccordionContent, AccordionItem, AccordionTrigger } from '@/components/ui/accordion';
import { Alert, AlertDescription, AlertTitle } from '@/components/ui/alert';

const Chapter7Enhanced = () => {
  const [quizSubmitted, setQuizSubmitted] = useState(false);
  const [answers, setAnswers] = useState({});
  const [score, setScore] = useState(0);

  const quizQuestions = [
    {
      id: 1,
      question: "อะไรคือความแตกต่างหลักระหว่าง Value-based และ Policy-based methods ใน Reinforcement Learning?",
      options: [
        "Value-based เรียนรู้ Q-function โดยตรง ส่วน Policy-based เรียนรู้ Policy โดยตรง",
        "Value-based ใช้สำหรับ Environment ที่มี State Space ขนาดเล็ก ส่วน Policy-based ใช้สำหรับขนาดใหญ่",
        "Value-based ไม่ต้องการ Reward Function ส่วน Policy-based ต้องการ",
        "ไม่มีความแตกต่างกันมากนัก ทั้งสองวิธีใช้หลักการเดียวกัน"
      ],
      correctAnswer: "Value-based เรียนรู้ Q-function โดยตรง ส่วน Policy-based เรียนรู้ Policy โดยตรง"
    },
    {
      id: 2,
      question: "สมการ Bellman Equation มีความสำคัญอย่างไรใน Reinforcement Learning?",
      options: [
        "ใช้อธิบายความสัมพันธ์ระหว่าง State และ Action โดยตรง",
        "ใช้อธิบายความสัมพันธ์ระหว่าง Value Function ของสถานะปัจจุบันกับสถานะถัดไป",
        "ใช้ในการคำนวณ Reward ที่ Agent จะได้รับในอนาคตเท่านั้น",
        "ใช้ในการกำหนด Policy ที่ Agent ควรจะใช้"
      ],
      correctAnswer: "ใช้อธิบายความสัมพันธ์ระหว่าง Value Function ของสถานะปัจจุบันกับสถานะถัดไป"
    },
    {
      id: 3,
      question: "Deep Q-Networks (DQN) แตกต่างจาก Q-Learning แบบดั้งเดิมอย่างไร?",
      options: [
        "DQN ใช้ Deep Neural Network เพื่อประมาณ Q-function",
        "DQN ไม่จำเป็นต้องมี Environment ในการเรียนรู้",
        "DQN เป็นอัลกอริทึมแบบ Policy-based",
        "DQN ใช้สำหรับปัญหาที่มี State Space ขนาดเล็กเท่านั้น"
      ],
      correctAnswer: "DQN ใช้ Deep Neural Network เพื่อประมาณ Q-function"
    },
    {
      id: 4,
      question: "ข้อใดไม่ใช่การประยุกต์ใช้ Reinforcement Learning ในฟิสิกส์?",
      options: [
        "การควบคุมระบบควอนตัม",
        "การออกแบบการทดลองอัตโนมัติ",
        "การหาค่าเหมาะสมที่สุดของพารามิเตอร์ในการจำลองทางฟิสิกส์",
        "การจำแนกประเภทของภาพกาแล็กซี"
      ],
      correctAnswer: "การจำแนกประเภทของภาพกาแล็กซี"
    },
    {
      id: 5,
      question: "หากต้องการควบคุมหุ่นยนต์สำรวจดาวอังคารด้วย RL ข้อใดคือ Reward Function ที่เหมาะสมที่สุด?",
      options: [
        "ให้ Reward สูงเมื่อถึงจุดหมาย, Penalty เมื่อชนสิ่งกีดขวาง",
        "ให้ Reward คงที่ทุกๆ การเคลื่อนที่",
        "ให้ Penalty เมื่อหุ่นยนต์หยุดนิ่ง",
        "ให้ Reward เมื่อใช้พลังงานน้อยที่สุด"
      ],
      correctAnswer: "ให้ Reward สูงเมื่อถึงจุดหมาย, Penalty เมื่อชนสิ่งกีดขวาง"
    }
  ];

  const handleAnswerChange = (questionId, selectedOption) => {
    setAnswers({ ...answers, [questionId]: selectedOption });
  };

  const handleSubmitQuiz = () => {
    let currentScore = 0;
    quizQuestions.forEach(q => {
      if (answers[q.id] === q.correctAnswer) {
        currentScore += 1;
      }
    });
    setScore(currentScore);
    setQuizSubmitted(true);
  };

  const renderQuizResult = () => {
    return (
      <Alert className="mt-4">
        <AlertTitle className="text-lg font-bold">ผลคะแนนของคุณ: {score} / {quizQuestions.length}</AlertTitle>
        <AlertDescription>
          {score === quizQuestions.length ? (
            <p className="text-green-600">ยอดเยี่ยม! คุณตอบถูกทุกข้อ</p>
          ) : (
            <p className="text-red-600">ลองทบทวนเนื้อหาและทำแบบทดสอบอีกครั้ง</p>
          )}
          <h4 className="font-semibold mt-4">เฉลย:</h4>
          {quizQuestions.map(q => (
            <div key={q.id} className="mt-2">
              <p className="font-medium">{q.id}. {q.question}</p>
              <p className={answers[q.id] === q.correctAnswer ? "text-green-600" : "text-red-600"}>
                คำตอบของคุณ: {answers[q.id] || "ไม่ได้ตอบ"}
                {answers[q.id] !== q.correctAnswer && <span className="ml-2">(คำตอบที่ถูกต้อง: {q.correctAnswer})</span>}
              </p>
            </div>
          ))}
        </AlertDescription>
      </Alert>
    );
  };

  return (
    <motion.div
      initial={{ opacity: 0, y: 20 }}
      animate={{ opacity: 1, y: 0 }}
      transition={{ duration: 0.5 }}
      className="space-y-8 p-6 bg-white rounded-lg shadow-md dark:bg-gray-800"
    >
      <h1 className="text-4xl font-bold text-gray-900 dark:text-white mb-4">บทที่ 7: การเรียนรู้เสริมกำลัง (Reinforcement Learning) และการควบคุมระบบ</h1>
      <p className="text-lg text-gray-700 dark:text-gray-300">สำรวจหลักการพื้นฐานของ Reinforcement Learning (RL) และการประยุกต์ใช้ในการควบคุมระบบฟิสิกส์ที่ซับซ้อน รวมถึงการออกแบบการทดลองอัตโนมัติ</p>

      <Tabs defaultValue="content" className="w-full">
        <TabsList className="grid w-full grid-cols-3">
          <TabsTrigger value="content"><BookOpen className="mr-2" /> เนื้อหา</TabsTrigger>
          <TabsTrigger value="code"><Code className="mr-2" /> ตัวอย่างโค้ด</TabsTrigger>
          <TabsTrigger value="quiz"><HelpCircle className="mr-2" /> แบบทดสอบ</TabsTrigger>
        </TabsList>

        <TabsContent value="content" className="mt-4">
          <Card>
            <CardHeader>
              <CardTitle>หลักการพื้นฐานของ Reinforcement Learning</CardTitle>
            </CardHeader>
            <CardContent className="space-y-4 text-gray-700 dark:text-gray-300">
              <p><strong>Reinforcement Learning (RL)</strong> เป็นสาขาหนึ่งของ Machine Learning ที่เกี่ยวข้องกับวิธีการที่ <strong>Agent</strong> (ตัวแทน) ควรจะกระทำใน <strong>Environment</strong> (สภาพแวดล้อม) เพื่อเพิ่ม <strong>Reward</strong> (รางวัล) สะสมสูงสุด Agent เรียนรู้จากการลองผิดลองถูก โดยการสังเกต <strong>State</strong> (สถานะ) ของ Environment, เลือก <strong>Action</strong> (การกระทำ), ได้รับ Reward และเปลี่ยนไปสู่ State ใหม่</p>
              <h3 className="text-xl font-semibold text-gray-900 dark:text-white">องค์ประกอบหลัก:</h3>
              <ul className="list-disc list-inside space-y-1">
                <li><strong>Agent:</strong> ผู้เรียนรู้หรือผู้ตัดสินใจ</li>
                <li><strong>Environment:</strong> โลกที่ Agent โต้ตอบด้วย</li>
                <li><strong>State (S):</strong> สถานการณ์ปัจจุบันของ Environment</li>
                <li><strong>Action (A):</strong> การกระทำที่ Agent สามารถทำได้ในแต่ละ State</li>
                <li><strong>Reward (R):</strong> สัญญาณตอบรับที่เป็นตัวเลขที่ Agent ได้รับหลังจากทำการ Action</li>
                <li><strong>Policy (π):</strong> กลยุทธ์ที่ Agent ใช้ในการเลือก Action จาก State ที่กำหนด</li>
                <li><strong>Value Function (V/Q):</strong> การประมาณค่าของ Reward ที่คาดว่าจะได้รับในอนาคตจาก State หรือ State-Action Pair หนึ่งๆ</li>
              </ul>
              <Alert>
                <Lightbulb className="h-4 w-4" />
                <AlertTitle>ตัวอย่าง</AlertTitle>
                <AlertDescription>การควบคุมหุ่นยนต์สำรวจดาวอังคารให้เคลื่อนที่ไปยังจุดที่ต้องการโดยหลีกเลี่ยงอุปสรรคและเก็บตัวอย่างแร่ธาตุ</AlertDescription>
              </Alert>

              <h2 className="text-2xl font-bold text-gray-900 dark:text-white mt-6">7.2 Markov Decision Process (MDP) และ Bellman Equation</h2>
              <p><strong>Markov Decision Process (MDP)</strong> เป็นกรอบทางคณิตศาสตร์สำหรับการสร้างแบบจำลองสถานการณ์ใน RL โดยมีคุณสมบัติ Markovian คือ สถานะในอนาคตขึ้นอยู่กับสถานะปัจจุบันและ Action ที่เลือกเท่านั้น ไม่ขึ้นอยู่กับประวัติก่อนหน้า</p>
              <p><strong>Bellman Equation</strong> เป็นสมการพื้นฐานใน RL ที่อธิบายความสัมพันธ์ระหว่าง Value Function ของสถานะปัจจุบันกับ Value Function ของสถานะถัดไป โดยพิจารณา Reward ที่ได้รับทันทีและ Reward ที่คาดว่าจะได้รับในอนาคต</p>
              <h3 className="text-xl font-semibold text-gray-900 dark:text-white">Bellman Expectation Equation (สำหรับ Value Function):</h3>
              <div className="overflow-x-auto">
                <p className="text-center text-xl font-mono p-4 bg-gray-100 dark:bg-gray-700 rounded-md">
                  $V^{`\pi`}(s) = \sum_a \pi(a|s) \sum_{`s′, r`} P(s′, r|s, a) [r + \gamma V^{`\pi`}(s′)]$
                </p>
              </div>
              <h3 className="text-xl font-semibold text-gray-900 dark:text-white">Bellman Optimality Equation (สำหรับ Optimal Value Function):</h3>
              <div className="overflow-x-auto">
                <p className="text-center text-xl font-mono p-4 bg-gray-100 dark:bg-gray-700 rounded-md">
                  $V^*(s) = \max_a \sum_{`s′, r`} P(s′, r|s, a) [r + \gamma V^*(s′)]$
                </p>
              </div>
              <p>โดยที่ $\gamma$ คือ Discount Factor (0 ≤ $\gamma$ ≤ 1) ที่ลดทอนค่าของ Reward ในอนาคต</p>
              <Alert>
                <Lightbulb className="h-4 w-4" />
                <AlertTitle>ตัวอย่าง</AlertTitle>
                <AlertDescription>การใช้ MDP เพื่อสร้างแบบจำลองการควบคุมอุณหภูมิในเครื่องปฏิกรณ์นิวเคลียร์</AlertDescription>
              </Alert>

              <h2 className="text-2xl font-bold text-gray-900 dark:text-white mt-6">7.3 อัลกอริทึม Value-based: Q-Learning และ Deep Q-Networks (DQN)</h2>
              <p><strong>Value-based Algorithms</strong> มุ่งเน้นการประมาณค่า Value Function (เช่น Q-value) ของแต่ละ State-Action Pair และเลือก Action ที่มี Q-value สูงสุด</p>
              <h3 className="text-xl font-semibold text-gray-900 dark:text-white">Q-Learning:</h3>
              <p>เป็นอัลกอริทึม RL แบบ Off-policy ที่เรียนรู้ Q-function โดยตรงจากประสบการณ์ โดยไม่ต้องรู้แบบจำลองของ Environment</p>
              <h4 className="text-lg font-semibold text-gray-900 dark:text-white">สมการอัปเดต Q-value:</h4>
              <div className="overflow-x-auto">
                <p className="text-center text-xl font-mono p-4 bg-gray-100 dark:bg-gray-700 rounded-md">
                  $Q(s, a) \leftarrow Q(s, a) + \alpha [r + \gamma \max_{`a′`} Q(s′, a′) - Q(s, a)]$
                </p>
              </div>
              <p>โดยที่ $\alpha$ คือ Learning Rate</p>
              <h3 className="text-xl font-semibold text-gray-900 dark:text-white">Deep Q-Networks (DQN):</h3>
              <p>ขยายแนวคิดของ Q-Learning โดยใช้ Deep Neural Network เพื่อประมาณ Q-function ซึ่งมีประโยชน์มากสำหรับ Environment ที่มี State Space ขนาดใหญ่ เช่น การเล่นเกม Atari</p>
              <Alert>
                <Lightbulb className="h-4 w-4" />
                <AlertTitle>ตัวอย่าง</AlertTitle>
                <AlertDescription>การใช้ DQN เพื่อควบคุมการเคลื่อนที่ของยานสำรวจในสภาพแวดล้อมที่ซับซ้อน</AlertDescription>
              </Alert>

              <h2 className="text-2xl font-bold text-gray-900 dark:text-white mt-6">7.4 อัลกอริทึม Policy-based: Policy Gradient และ Actor-Critic Methods</h2>
              <p><strong>Policy-based Algorithms</strong> มุ่งเน้นการเรียนรู้ Policy โดยตรง ซึ่งเป็นฟังก์ชันที่แมป State ไปยัง Action โดยตรง โดยไม่ต้องประมาณ Value Function</p>
              <h3 className="text-xl font-semibold text-gray-900 dark:text-white">Policy Gradient:</h3>
              <p>อัลกอริทึมที่ปรับปรุง Policy โดยการไล่ตาม Gradient ของ Reward ที่คาดว่าจะได้รับ</p>
              <h3 className="text-xl font-semibold text-gray-900 dark:text-white">Actor-Critic Methods:</h3>
              <p>ผสมผสานแนวคิดของ Value-based และ Policy-based โดยมีสองส่วนหลัก:</p>
              <ul className="list-disc list-inside space-y-1">
                <li><strong>Actor:</strong> เรียนรู้ Policy (คล้าย Policy-based)</li>
                <li><strong>Critic:</strong> เรียนรู้ Value Function เพื่อช่วยประเมิน Action ที่ Actor เลือก (คล้าย Value-based)</li>
              </ul>
              <Alert>
                <Lightbulb className="h-4 w-4" />
                <AlertTitle>ตัวอย่าง</AlertTitle>
                <AlertDescription>การใช้ Policy Gradient เพื่อควบคุมแขนกลให้หยิบจับวัตถุที่มีรูปร่างและน้ำหนักต่างกัน</AlertDescription>
              </Alert>

              <h2 className="text-2xl font-bold text-gray-900 dark:text-white mt-6">7.5 การประยุกต์ใช้ในการควบคุมระบบควอนตัม (Quantum Control)</h2>
              <p>RL มีศักยภาพในการควบคุมระบบควอนตัมที่ซับซ้อน ซึ่งเป็นสิ่งสำคัญในการพัฒนา Quantum Computing และ Quantum Technologies</p>
              <ul className="list-disc list-inside space-y-1">
                <li><strong>การควบคุมสปินของคิวบิต:</strong> การใช้ RL เพื่อหาลำดับพัลส์เลเซอร์ที่เหมาะสมในการควบคุมสถานะของคิวบิต</li>
                <li><strong>การออกแบบพัลส์:</strong> การหาพัลส์แม่เหล็กไฟฟ้าที่เหมาะสมที่สุดเพื่อกระตุ้นการเปลี่ยนสถานะควอนตัม</li>
              </ul>
              <Alert>
                <Lightbulb className="h-4 w-4" />
                <AlertTitle>ตัวอย่าง</AlertTitle>
                <AlertDescription>การใช้ RL เพื่อลดข้อผิดพลาดในการดำเนินการควอนตัม (Quantum Gate Error)</AlertDescription>
              </Alert>

              <h2 className="text-2xl font-bold text-gray-900 dark:text-white mt-6">7.6 การออกแบบการทดลองอัตโนมัติ (Autonomous Experimental Design)</h2>
              <p>RL สามารถช่วยในการออกแบบและดำเนินการทดลองทางฟิสิกส์ได้อย่างอัตโนมัติ โดย Agent จะเรียนรู้ที่จะเลือกพารามิเตอร์การทดลองที่เหมาะสมที่สุดเพื่อบรรลุเป้าหมายที่กำหนด</p>
              <ul className="list-disc list-inside space-y-1">
                <li><strong>การค้นหาวัสดุใหม่:</strong> การใช้ RL เพื่อแนะนำองค์ประกอบและเงื่อนไขการสังเคราะห์วัสดุใหม่ที่มีคุณสมบัติเฉพาะ</li>
                <li><strong>การปรับแต่งเครื่องมือ:</strong> การใช้ RL เพื่อปรับแต่งพารามิเตอร์ของเครื่องมือทดลอง เช่น กล้องจุลทรรศน์อิเล็กตรอน หรือเครื่องเร่งอนุภาค</li>
              </ul>
              <Alert>
                <Lightbulb className="h-4 w-4" />
                <AlertTitle>ตัวอย่าง</AlertTitle>
                <AlertDescription>การใช้ RL เพื่อเร่งกระบวนการค้นพบวัสดุตัวนำยิ่งยวดอุณหภูมิสูง</AlertDescription>
              </Alert>

              <h2 className="text-2xl font-bold text-gray-900 dark:text-white mt-6">7.7 การหาค่าเหมาะสมที่สุดของพารามิเตอร์ในการจำลองทางฟิสิกส์</h2>
              <p>RL สามารถนำมาใช้เพื่อหาค่าพารามิเตอร์ที่เหมาะสมที่สุดในแบบจำลองทางฟิสิกส์ที่ซับซ้อน ซึ่งอาจมี State Space ขนาดใหญ่และฟังก์ชันวัตถุประสงค์ที่ซับซ้อน</p>
              <ul className="list-disc list-inside space-y-1">
                <li><strong>การปรับแต่งแบบจำลองสภาพภูมิอากาศ:</strong> การใช้ RL เพื่อหาพารามิเตอร์ที่เหมาะสมที่สุดสำหรับแบบจำลองสภาพภูมิอากาศเพื่อการพยากรณ์ที่แม่นยำยิ่งขึ้น</li>
                <li><strong>การออกแบบโครงสร้าง:</strong> การใช้ RL เพื่อออกแบบโครงสร้างของอุปกรณ์ทางฟิสิกส์ เช่น เสาอากาศ หรือเลนส์ เพื่อให้ได้ประสิทธิภาพสูงสุด</li>
              </ul>
              <Alert>
                <Lightbulb className="h-4 w-4" />
                <AlertTitle>ตัวอย่าง</AlertTitle>
                <AlertDescription>การใช้ RL เพื่อหาพารามิเตอร์ที่เหมาะสมที่สุดสำหรับการจำลองการชนกันของกาแล็กซี</AlertDescription>
              </Alert>
            </CardContent>
          </Card>
        </TabsContent>

        <TabsContent value="code" className="mt-4">
          <Card>
            <CardHeader>
              <CardTitle>ตัวอย่างโค้ด: Q-Learning สำหรับการควบคุมระบบควอนตัมอย่างง่าย</CardTitle>
            </CardHeader>
            <CardContent>
              <div className="bg-gray-900 rounded-md p-4 overflow-x-auto">
                <pre className="text-white text-sm">
                  <code className="language-python">
{`import numpy as np

class QuantumEnv:
    def __init__(self):
        self.state = 0  # 0: Ground state, 1: Excited state
        self.actions = [0, 1] # 0: Apply pulse A, 1: Apply pulse B
        self.num_states = 2
        self.num_actions = 2

    def step(self, action):
        reward = 0
        done = False
        if self.state == 0: # Current state is Ground state
            if action == 0: # Apply pulse A (try to excite)
                if np.random.rand() < 0.7: # 70% chance to go to excited state
                    self.state = 1
                    reward = 1 # Reward for reaching excited state
                else:
                    self.state = 0
                    reward = -0.5 # Penalty for failing to excite
            elif action == 1: # Apply pulse B (do nothing effectively)
                self.state = 0
                reward = -0.1 # Small penalty for wasted action
        elif self.state == 1: # Current state is Excited state
            if action == 0: # Apply pulse A (try to de-excite)
                if np.random.rand() < 0.8: # 80% chance to go to ground state
                    self.state = 0
                    reward = 0.5 # Reward for de-exciting
                else:
                    self.state = 1
                    reward = -0.5 # Penalty for failing to de-excite
            elif action == 1: # Apply pulse B (try to maintain excited state)
                if np.random.rand() < 0.9: # 90% chance to stay excited
                    self.state = 1
                    reward = 0.2 # Small reward for maintaining state
                else:
                    self.state = 0
                    reward = -1 # Large penalty for losing excited state
        
        # End episode after a few steps or if a goal is reached (simplified for this example)
        # For simplicity, we\'ll let it run for a fixed number of steps in the training loop
        return self.state, reward, done, {}

    def reset(self):
        self.state = 0 # Always start in ground state
        return self.state

# Q-Learning Algorithm
def q_learning(env, num_episodes=1000, learning_rate=0.1, discount_factor=0.99, epsilon=0.1):
    q_table = np.zeros((env.num_states, env.num_actions))

    for episode in range(num_episodes):
        state = env.reset()
        done = False
        total_reward = 0

        for t in range(100): # Max 100 steps per episode
            # Epsilon-greedy strategy
            if np.random.rand() < epsilon:
                action = np.random.choice(env.actions) # Explore
            else:
                action = np.argmax(q_table[state, :]) # Exploit

            next_state, reward, done, _ = env.step(action)
            total_reward += reward

            # Q-value update
            q_table[state, action] = q_table[state, action] + \
                                     learning_rate * (reward + discount_factor * np.max(q_table[next_state, :]) - q_table[state, action])
            state = next_state
            if done: # Not used in this simplified env, but good practice
                break
        
        if episode % 100 == 0:
            print(f"Episode {episode}: Total Reward = {{total_reward:.2f}}")

    return q_table

# Run Q-Learning
env = QuantumEnv()
print("Training Q-Learning agent...")
optimal_q_table = q_learning(env)
print("Training complete!")
print("Optimal Q-table:")
print(optimal_q_table)

# Test the learned policy
print("\nTesting learned policy...")
state = env.reset()
for t in range(10):
    action = np.argmax(optimal_q_table[state, :])
    next_state, reward, _, _ = env.step(action)
    print(f"Step {t+1}: State {state} -> Action {action} -> Next State {next_state}, Reward {{reward:.2f}}")
    state = next_state`}
                  </code>
                </pre>
              </div>
            </CardContent>
          </Card>
        </TabsContent>

        <TabsContent value="quiz" className="mt-4">
          <Card>
            <CardHeader>
              <CardTitle>แบบทดสอบบทที่ 7</CardTitle>
            </CardHeader>
            <CardContent>
              <form onSubmit={(e) => { e.preventDefault(); handleSubmitQuiz(); }} className="space-y-6">
                {quizQuestions.map(q => (
                  <div key={q.id} className="border p-4 rounded-md dark:border-gray-700">
                    <p className="font-semibold mb-3 text-gray-900 dark:text-white">{q.id}. {q.question}</p>
                    <div className="space-y-2">
                      {q.options.map((option, index) => (
                        <div key={index} className="flex items-center">
                          <input
                            type="radio"
                            id={`question${q.id}-option${index}`}
                            name={`question${q.id}`}
                            value={option}
                            onChange={() => handleAnswerChange(q.id, option)}
                            checked={answers[q.id] === option}
                            className="form-radio h-4 w-4 text-blue-600"
                            disabled={quizSubmitted}
                          />
                          <label htmlFor={`question${q.id}-option${index}`} className="ml-3 text-gray-700 dark:text-gray-300">
                            {option}
                          </label>
                        </div>
                      ))}
                    </div>
                  </div>
                ))}
                {!quizSubmitted && (
                  <Button type="submit" className="w-full">
                    ส่งคำตอบ
                  </Button>
                )}
              </form>
              {quizSubmitted && renderQuizResult()}
            </CardContent>
          </Card>
        </TabsContent>
      </Tabs>

      <Card>
        <CardHeader>
          <CardTitle>บทสรุป</CardTitle>
        </CardHeader>
        <CardContent className="text-gray-700 dark:text-gray-300">
          <p>บทนี้ได้นำเสนอหลักการพื้นฐานของ Reinforcement Learning (RL) รวมถึงองค์ประกอบสำคัญอย่าง Agent, Environment, Reward, State และ Action นอกจากนี้ยังได้สำรวจกรอบทางคณิตศาสตร์อย่าง Markov Decision Process (MDP) และ Bellman Equation ซึ่งเป็นรากฐานของอัลกอริทึม RL ต่างๆ อัลกอริทึม Value-based เช่น Q-Learning และ Deep Q-Networks (DQN) รวมถึงอัลกอริทึม Policy-based อย่าง Policy Gradient และ Actor-Critic Methods ได้ถูกอธิบายพร้อมตัวอย่างการประยุกต์ใช้ในฟิสิกส์ เช่น การควบคุมระบบควอนตัม การออกแบบการทดลองอัตโนมัติ และการหาค่าเหมาะสมที่สุดของพารามิเตอร์ในการจำลองทางฟิสิกส์ RL เป็นเครื่องมือที่มีประสิทธิภาพในการแก้ปัญหาการควบคุมและการตัดสินใจในสภาพแวดล้อมที่ซับซ้อน และมีบทบาทสำคัญในการขับเคลื่อนการวิจัยและพัฒนาในสาขาฟิสิกส์เชิงคณิตศาสตร์</p>
        </CardContent>
      </Card>
    </motion.div>
  );
};

export default Chapter7Enhanced;

