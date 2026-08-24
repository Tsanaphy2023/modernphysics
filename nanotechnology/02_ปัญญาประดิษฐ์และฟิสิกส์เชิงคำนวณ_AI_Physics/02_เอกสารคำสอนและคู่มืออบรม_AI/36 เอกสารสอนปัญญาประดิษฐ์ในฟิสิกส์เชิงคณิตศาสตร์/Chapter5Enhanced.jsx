import React, { useState, useEffect } from 'react';
import { motion, AnimatePresence } from 'framer-motion';
import { 
  Brain, 
  Network, 
  Zap, 
  TrendingUp, 
  CheckCircle, 
  Clock, 
  BookOpen, 
  Play, 
  RotateCcw,
  Download,
  Copy,
  ChevronLeft,
  ChevronRight,
  FileText
} from 'lucide-react';
import { Button } from '@/components/ui/button.jsx';
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from '@/components/ui/card.jsx';
import { Badge } from '@/components/ui/badge.jsx';
import { Progress } from '@/components/ui/progress.jsx';
import { Tabs, TabsContent, TabsList, TabsTrigger } from '@/components/ui/tabs.jsx';
import CodePlayground from './CodePlayground';
import InteractiveSimulation from './InteractiveSimulation';
// Removed react-syntax-highlighter imports to fix build issues

const Chapter5Enhanced = () => {
  const [completedSections, setCompletedSections] = useState(new Set());
  const [activeTab, setActiveTab] = useState('content');
  const [quizAnswers, setQuizAnswers] = useState({});
  const [quizSubmitted, setQuizSubmitted] = useState(false);
  const [quizScore, setQuizScore] = useState(0);

  // Chapter 5 content structure
  const chapterInfo = {
    number: 5,
    title: "โครงข่ายประสาทเทียมและการเรียนรู้เชิงลึก",
    subtitle: "Neural Networks and Deep Learning",
    description: "สถาปัตยกรรมและหลักการทำงานของโครงข่ายประสาทเทียม พร้อมการประยุกต์ใช้ในปัญหาที่ซับซ้อนทางฟิสิกส์",
    duration: "5 ชั่วโมง",
    difficulty: "สูง",
    topics: 7,
    level: "ระดับสูง"
  };

  const sections = [
    {
      id: '5.1',
      title: 'โครงข่ายประสาทเทียมพื้นฐาน: Perceptron และ Multi-layer Perceptron',
      duration: '45 นาที',
      description: 'ศึกษาหลักการพื้นฐานของ Perceptron และการพัฒนาไปสู่ Multi-layer Perceptron สำหรับการแก้ปัญหาที่ซับซ้อน',
      keyPoints: [
        'หลักการทำงานของ Perceptron และข้อจำกัดในการแก้ปัญหา XOR',
        'สถาปัตยกรรมของ Multi-layer Perceptron และการเพิ่มชั้นซ่อนเร้น',
        'การเลือกจำนวนนิวรอนและชั้นที่เหมาะสมสำหรับปัญหาต่างๆ',
        'การประยุกต์ใช้ในการประมาณฟังก์ชันทางฟิสิกส์'
      ],
      applications: [
        'การประมาณฟังก์ชันพลังงานศักย์ในระบบโมเลกุล',
        'การทำนายคุณสมบัติของวัสดุจากโครงสร้างอะตอม',
        'การแก้สมการเชิงอนุพันธ์อย่างง่ายด้วย Neural Networks'
      ],
      content: (
        <>
          <p className="mb-4">
            <strong>Perceptron</strong> เป็นหน่วยประมวลผลพื้นฐานที่สุดในโครงข่ายประสาทเทียม ซึ่งจำลองการทำงานของเซลล์ประสาทชีวภาพ โดยรับอินพุตหลายค่า, คูณด้วยน้ำหนัก, รวมผลรวม, และส่งผ่านฟังก์ชันกระตุ้นเพื่อสร้างเอาต์พุต Perceptron สามารถใช้ในการจำแนกข้อมูลเชิงเส้นตรงได้
          </p>
          <p className="mb-4">
            <strong>Multi-layer Perceptron (MLP)</strong> หรือโครงข่ายประสาทเทียมแบบหลายชั้น เป็นการขยายแนวคิดของ Perceptron โดยมีชั้นอินพุต, ชั้นซ่อนเร้น (hidden layers) อย่างน้อยหนึ่งชั้น, และชั้นเอาต์พุต แต่ละชั้นประกอบด้วย Perceptron หลายตัวเชื่อมต่อกัน MLP สามารถเรียนรู้ความสัมพันธ์ที่ไม่เชิงเส้นที่ซับซ้อนในข้อมูลได้
          </p>
        </>
      )
    },
    {
      id: '5.2',
      title: 'อัลกอริทึมการแพร่กระจายย้อนกลับ (Backpropagation) และการหาค่าเหมาะสมที่สุด',
      duration: '50 นาที',
      description: 'เรียนรู้อัลกอริทึม Backpropagation และเทคนิคการหาค่าเหมาะสมที่สุดสำหรับการฝึกสอน Neural Networks',
      keyPoints: [
        'หลักการของ Chain Rule และการคำนวณ Gradient ย้อนหลัง',
        'อัลกอริทึม Gradient Descent และ variants (SGD, Adam, RMSprop)',
        'การตั้งค่า Learning Rate และ Batch Size ที่เหมาะสม',
        'การจัดการกับปัญหา Local Minima และ Saddle Points'
      ],
      applications: [
        'การฝึกสอนโมเดลสำหรับการทำนายสมบัติทางกายภาพ',
        'การปรับแต่งพารามิเตอร์ในการจำลองมอนติคาร์โล',
        'การหาค่าเหมาะสมที่สุดในการออกแบบการทดลอง'
      ],
      content: (
        <>
          <p className="mb-4">
            <strong>Backpropagation</strong> เป็นอัลกอริทึมหลักที่ใช้ในการฝึกโครงข่ายประสาทเทียม โดยจะคำนวณ Gradient ของฟังก์ชันความผิดพลาด (Loss Function) เทียบกับน้ำหนักของโครงข่ายประสาทเทียม ซึ่ง Gradient นี้จะถูกใช้โดย Optimizer เพื่อปรับปรุงน้ำหนักของโมเดลให้มีประสิทธิภาพดีขึ้น กระบวนการนี้ประกอบด้วยสองขั้นตอนหลัก:
          </p>
          <ul className="list-disc ml-6 mb-4">
            <li><strong>Forward Pass:</strong> อินพุตถูกส่งผ่านโครงข่ายเพื่อคำนวณเอาต์พุตและค่าความผิดพลาด</li>
            <li><strong>Backward Pass:</strong> Gradient ของความผิดพลาดจะถูกคำนวณย้อนกลับจากชั้นเอาต์พุตไปยังชั้นอินพุต เพื่ออัปเดตน้ำหนัก</li>
          </ul>
          <p className="mb-4">
            <strong>การหาค่าเหมาะสมที่สุด (Optimization)</strong> เป็นกระบวนการที่ใช้อัลกอริทึม เช่น Gradient Descent (และรูปแบบต่างๆ เช่น Stochastic Gradient Descent, Adam) เพื่อปรับน้ำหนักของโครงข่ายประสาทเทียมให้ค่า Loss Function มีค่าน้อยที่สุด
          </p>
        </>
      )
    },
    {
      id: '5.3',
      title: 'ฟังก์ชันกระตุ้น (Activation Functions) และการเลือกใช้ที่เหมาะสม',
      duration: '40 นาที',
      description: 'ศึกษาฟังก์ชันกระตุ้นต่างๆ และการเลือกใช้ที่เหมาะสมสำหรับปัญหาทางฟิสิกส์',
      keyPoints: [
        'ฟังก์ชันกระตุ้นแบบดั้งเดิม: Sigmoid, Tanh และข้อจำกัด',
        'ฟังก์ชัน ReLU และ variants (Leaky ReLU, ELU, Swish)',
        'การเลือกฟังก์ชันกระตุ้นตามลักษณะของปัญหา',
        'ผลกระทบของฟังก์ชันกระตุ้นต่อการฝึกสอนและประสิทธิภาพ'
      ],
      applications: [
        'การเลือกฟังก์ชันกระตุ้นสำหรับการทำนายพลังงาน',
        'การใช้ฟังก์ชันกระตุ้นในการจำลองระบบไดนามิก',
        'การประยุกต์ใช้ในการแก้สมการเชิงอนุพันธ์'
      ],
      content: (
        <>
          <p className="mb-4">
            <strong>ฟังก์ชันกระตุ้น (Activation Functions)</strong> เป็นส่วนสำคัญของเซลล์ประสาทเทียมที่กำหนดว่าเซลล์ประสาทควรจะกระตุ้นหรือไม่ โดยการนำผลรวมถ่วงน้ำหนักของอินพุตไปแปลงเป็นเอาต์พุต ฟังก์ชันกระตุ้นที่แตกต่างกันมีคุณสมบัติและประโยชน์ที่แตกต่างกัน:
          </p>
          <ul className="list-disc ml-6 mb-4">
            <li><strong>Sigmoid:</strong> บีบอัดค่าอินพุตให้อยู่ในช่วง (0, 1) เหมาะสำหรับชั้นเอาต์พุตของการจำแนกประเภทแบบไบนารี แต่มีปัญหา Vanishing Gradient</li>
            <li><strong>ReLU (Rectified Linear Unit):</strong> <code>f(x) = max(0, x)</code> เป็นที่นิยมเนื่องจากแก้ปัญหา Vanishing Gradient ได้ดีและคำนวณง่าย</li>
            <li><strong>Leaky ReLU, ELU, PReLU:</strong> เป็นรูปแบบที่พัฒนามาจาก ReLU เพื่อแก้ปัญหา Dying ReLU</li>
            <li><strong>Tanh (Hyperbolic Tangent):</strong> บีบอัดค่าอินพุตให้อยู่ในช่วง (-1, 1) คล้าย Sigmoid แต่มีค่าเฉลี่ยเป็นศูนย์ ทำให้การฝึกมีเสถียรภาพมากขึ้น</li>
            <li><strong>Softmax:</strong> ใช้สำหรับชั้นเอาต์พุตของการจำแนกประเภทแบบหลายคลาส โดยแปลงค่าให้เป็นความน่าจะเป็นที่รวมกันได้ 1</li>
          </ul>
          <h3 className="text-xl font-semibold mb-2">การเลือกใช้ที่เหมาะสม</h3>
          <p className="mb-4">
            การเลือกฟังก์ชันกระตุ้นขึ้นอยู่กับลักษณะของปัญหาและชั้นของโครงข่ายประสาทเทียม:
          </p>
          <ul className="list-disc ml-6 mb-4">
            <li><strong>ชั้นซ่อนเร้น:</strong> ReLU และรูปแบบต่างๆ (Leaky ReLU, ELU) มักเป็นตัวเลือกที่ดีที่สุด</li>
            <li><strong>ชั้นเอาต์พุต:</strong>
              <ul className="list-circle ml-6">
                <li><strong>Binary Classification:</strong> Sigmoid</li>
                <li><strong>Multi-class Classification:</strong> Softmax</li>
                <li><strong>Regression:</strong> Linear (ไม่มีฟังก์ชันกระตุ้น)</li>
              </ul>
            </li>
          </ul>
        </>
      )
    },
    {
      id: '5.4',
      title: 'เทคนิคการป้องกัน Overfitting: Dropout, Batch Normalization และ Regularization',
      duration: '45 นาที',
      description: 'เรียนรู้เทคนิคต่างๆ ในการป้องกัน Overfitting และปรับปรุงประสิทธิภาพการฝึกสอน',
      keyPoints: [
        'ปัญหา Overfitting และ Underfitting ในบริบทของฟิสิกส์',
        'เทคนิค Dropout และการใช้งานในระหว่างการฝึกสอน',
        'Batch Normalization และการปรับปรุงความเสถียรในการฝึกสอน',
        'L1, L2 Regularization และ Early Stopping'
      ],
      applications: [
        'การป้องกัน Overfitting ในการทำนายคุณสมบัติวัสดุ',
        'การใช้ Regularization ในการแก้ปัญหา Inverse Problems',
        'การประยุกต์ใช้ในการวิเคราะห์ข้อมูลการทดลอง'
      ],
      content: (
        <>
          <p className="mb-4">
            <strong>Overfitting</strong> เกิดขึ้นเมื่อแบบจำลองเรียนรู้ข้อมูลการฝึกมากเกินไป จนไม่สามารถทำงานได้ดีกับข้อมูลใหม่ที่ไม่เคยเห็นมาก่อน ใน Deep Learning มีหลายเทคนิคที่ใช้ในการป้องกัน Overfitting:
          </p>
          <ul className="list-disc ml-6 mb-4">
            <li><strong>Dropout:</strong> ระหว่างการฝึก แต่ละเซลล์ประสาทในชั้นที่กำหนดจะถูกปิดใช้งาน (dropped out) แบบสุ่มด้วยความน่าจะเป็นที่กำหนด ซึ่งช่วยลดการพึ่งพาเซลล์ประสาทใดเซลล์ประสาทหนึ่งมากเกินไป และบังคับให้โครงข่ายเรียนรู้คุณลักษณะที่แข็งแกร่งขึ้น</li>
            <li><strong>Batch Normalization:</strong> ปรับค่าเฉลี่ยและส่วนเบี่ยงเบนมาตรฐานของอินพุตในแต่ละชั้นให้เป็นมาตรฐาน ซึ่งช่วยให้การฝึกมีเสถียรภาพมากขึ้นและลดเวลาในการฝึก</li>
            <li><strong>Regularization (L1, L2):</strong> เพิ่มเทอมปรับโทษ (penalty term) เข้าไปใน Loss Function เพื่อจำกัดขนาดของน้ำหนักในแบบจำลอง ซึ่งช่วยลดความซับซ้อนของแบบจำลองและป้องกัน Overfitting</li>
          </ul>
        </>
      )
    },
    {
      id: '5.5',
      title: 'สถาปัตยกรรมของ Deep Neural Networks: การออกแบบและการปรับแต่ง',
      duration: '50 นาที',
      description: 'ศึกษาการออกแบบสถาปัตยกรรมของ Deep Networks และเทคนิคการปรับแต่งสำหรับปัญหาทางฟิสิกส์',
      keyPoints: [
        'หลักการออกแบบสถาปัตยกรรมสำหรับปัญหาต่างๆ',
        'การจัดการกับปัญหา Vanishing และ Exploding Gradients',
        'Residual Networks (ResNet) และ Skip Connections',
        'การเลือกขนาดและจำนวนชั้นที่เหมาะสม'
      ],
      applications: [
        'การออกแบบ Deep Networks สำหรับการจำลองระบบควอนตัม',
        'การใช้ ResNet ในการวิเคราะห์ข้อมูลสเปกตรัม',
        'การประยุกต์ใช้ในการแก้สมการเชิงอนุพันธ์ซับซ้อน'
      ],
      content: (
        <>
          <p className="mb-4">
            การออกแบบสถาปัตยกรรมของ Deep Neural Networks (DNNs) เป็นกระบวนการที่สำคัญและต้องอาศัยความเข้าใจในปัญหาและข้อมูล การออกแบบประกอบด้วยการเลือกจำนวนชั้นซ่อนเร้น, จำนวนเซลล์ประสาทในแต่ละชั้น, ฟังก์ชันกระตุ้น, และเทคนิคการป้องกัน Overfitting
          </p>
          <h3 className="text-xl font-semibold mb-2">หลักการออกแบบเบื้องต้น:</h3>
          <ul className="list-disc ml-6 mb-4">
            <li><strong>จำนวนชั้น:</strong> โดยทั่วไป ยิ่งมีชั้นลึกมากเท่าไหร่ โมเดลก็ยิ่งสามารถเรียนรู้คุณลักษณะที่ซับซ้อนได้มากขึ้น แต่ก็เสี่ยงต่อ Overfitting และใช้เวลาในการฝึกนานขึ้น</li>
            <li><strong>จำนวนเซลล์ประสาท:</strong> จำนวนเซลล์ประสาทในแต่ละชั้นควรเหมาะสมกับความซับซ้อนของข้อมูลและปัญหา</li>
            <li><strong>การเชื่อมต่อ:</strong> การเชื่อมต่อแบบ Feedforward เป็นพื้นฐาน แต่ก็มีสถาปัตยกรรมที่ซับซ้อนขึ้น เช่น Residual Connections (ใน ResNet) ที่ช่วยให้สามารถสร้างโครงข่ายที่ลึกมากได้</li>
          </ul>
        </>
      )
    },
    {
      id: '5.6',
      title: 'การประยุกต์ใช้ในฟิสิกส์: การประมาณฟังก์ชันคลื่น (Wave Function Approximation)',
      duration: '55 นาที',
      description: 'การใช้ Deep Learning ในการประมาณฟังก์ชันคลื่นและการแก้ปัญหาทางกลศาสตร์ควอนตัม',
      keyPoints: [
        'หลักการใช้ Neural Networks ในการประมาณฟังก์ชันคลื่น',
        'Variational Monte Carlo และ Neural Quantum States',
        'การจัดการกับ Antisymmetry และ Fermionic Systems',
        'การประเมินพลังงานและคุณสมบัติทางควอนตัม'
      ],
      applications: [
        'การหาสถานะพื้นฐานของระบบควอนตัมหลายอนุภาค',
        'การจำลองระบบสปินและแม่เหล็ก',
        'การประยุกต์ใช้ในการคำนวณโครงสร้างอิเล็กทรอนิกส์'
      ],
      content: (
        <>
          <p className="mb-4">
            Deep Learning ได้รับการประยุกต์ใช้อย่างกว้างขวางในฟิสิกส์ โดยเฉพาะอย่างยิ่งในการแก้ปัญหาที่เกี่ยวข้องกับกลศาสตร์ควอนตัม เช่น การประมาณฟังก์ชันคลื่นของระบบหลายอนุภาค (Many-body Quantum Systems) ซึ่งเป็นปัญหาที่ซับซ้อนทางคณิตศาสตร์
          </p>
        </>
      )
    },
    {
      id: '5.7',
      title: 'เทคนิคการฝึกสอนขั้นสูง: Adam Optimizer, Learning Rate Scheduling',
      duration: '40 นาที',
      description: 'เรียนรู้เทคนิคการฝึกสอนขั้นสูงและการปรับแต่งพารามิเตอร์สำหรับประสิทธิภาพสูงสุด',
      keyPoints: [
        'อัลกอริทึม Adam และการปรับแต่งพารามิเตอร์ β1, β2',
        'Learning Rate Scheduling: Step Decay, Exponential Decay, Cosine Annealing',
        'Warm-up Strategies และ Cyclical Learning Rates',
        'การใช้ Gradient Clipping และ Weight Initialization'
      ],
      applications: [
        'การฝึกสอนโมเดลขนาดใหญ่สำหรับการจำลองทางฟิสิกส์',
        'การปรับแต่งการฝึกสอนสำหรับข้อมูลฟิสิกส์ที่มีสัญญาณรบกวน',
        'การประยุกต์ใช้ในการแก้ปัญหา Optimization ที่ซับซ้อน'
      ],
      content: (
        <>
          <p className="mb-4">
            การฝึกสอน Deep Neural Networks ให้มีประสิทธิภาพนั้นมักจะต้องใช้เทคนิคการฝึกสอนขั้นสูงเพื่อช่วยให้โมเดลลู่เข้าสู่จุดเหมาะสมที่สุดได้เร็วขึ้นและมีเสถียรภาพมากขึ้น
          </p>
          <ul className="list-disc ml-6 mb-4">
            <li><strong>Adam Optimizer:</strong> เป็นหนึ่งใน Optimizer ที่ได้รับความนิยมมากที่สุด เนื่องจากเป็นการรวมข้อดีของ AdaGrad และ RMSProp เข้าด้วยกัน โดยจะปรับ Learning Rate สำหรับพารามิเตอร์แต่ละตัวแบบไดนามิก ทำให้การฝึกมีประสิทธิภาพและรวดเร็ว</li>
            <li><strong>Learning Rate Scheduling:</strong> เป็นเทคนิคที่ปรับ Learning Rate ระหว่างการฝึก โดยอาจจะลด Learning Rate ลงเมื่อ Loss เริ่มคงที่ หรือเพิ่มขึ้นในช่วงแรกเพื่อเร่งการลู่เข้า ซึ่งช่วยให้โมเดลสามารถหาจุดเหมาะสมที่สุดได้ดีขึ้นและหลีกเลี่ยงการติดอยู่ใน Local Minima</li>
          </ul>
        </>
      )
    }
  ];

  const quizQuestions = [
    {
      id: 1,
      question: "จงอธิบายความแตกต่างระหว่าง Perceptron และ Multi-layer Perceptron (MLP) ในแง่ของสถาปัตยกรรมและความสามารถในการเรียนรู้",
      options: [
        "a) Perceptron มีหลายชั้นซ่อนเร้น ส่วน MLP มีเพียงชั้นเดียว",
        "b) Perceptron สามารถเรียนรู้ความสัมพันธ์ที่ไม่เชิงเส้นได้ ส่วน MLP ไม่ได้",
        "c) Perceptron สามารถจำแนกข้อมูลเชิงเส้นตรงได้ ส่วน MLP สามารถเรียนรู้ความสัมพันธ์ที่ไม่เชิงเส้นที่ซับซ้อนได้",
        "d) ไม่มีข้อใดถูก"
      ],
      correct: 2,
      explanation: "Single-layer Perceptron ไม่สามารถแก้ปัญหาที่ไม่สามารถแยกเชิงเส้นได้ (linearly non-separable) เช่น ปัญหา XOR ซึ่งต้องใช้ Multi-layer Perceptron ที่มีชั้นซ่อนเร้น"
    },
    {
      id: 2,
      question: "อัลกอริทึมใดที่ใช้ในการคำนวณ Gradient ของฟังก์ชันความผิดพลาดเทียบกับน้ำหนักของโครงข่ายประสาทเทียม?",
      options: [
        "a) Forward Propagation",
        "b) Backpropagation",
        "c) Gradient Descent",
        "d) Adam Optimization"
      ],
      correct: 1,
      explanation: "Backpropagation เป็นอัลกอริทึมหลักที่ใช้ในการฝึกโครงข่ายประสาทเทียม โดยจะคำนวณ Gradient ของฟังก์ชันความผิดพลาด (Loss Function) เทียบกับน้ำหนักของโครงข่ายประสาทเทียม"
    },
    {
      id: 3,
      question: "ฟังก์ชันกระตุ้นใดที่มักใช้ในชั้นซ่อนเร้นของ Deep Neural Networks และช่วยแก้ปัญหา Vanishing Gradient ได้ดี?",
      options: [
        "a) Sigmoid",
        "b) Tanh", 
        "c) ReLU",
        "d) Softmax"
      ],
      correct: 2,
      explanation: "ReLU (Rectified Linear Unit) เป็นฟังก์ชันกระตุ้นที่นิยมใช้ในปัจจุบันเพราะช่วยแก้ปัญหา Vanishing Gradient และมีการคำนวณที่เร็ว"
    },
    {
      id: 4,
      question: "เทคนิคใดต่อไปนี้ที่ช่วยป้องกัน Overfitting โดยการปิดใช้งานเซลล์ประสาทบางส่วนแบบสุ่มระหว่างการฝึก?",
      options: [
        "a) Batch Normalization",
        "b) Regularization",
        "c) Dropout",
        "d) Learning Rate Scheduling"
      ],
      correct: 2,
      explanation: "Dropout เป็นเทคนิคที่ช่วยป้องกัน Overfitting โดยการปิดการทำงานของนิวรอนบางตัวแบบสุ่มในระหว่างการฝึกสอน ทำให้โมเดลไม่พึ่งพานิวรอนใดนิวรอนหนึ่งมากเกินไป"
    },
    {
      id: 5,
      question: "จงอธิบายว่าเหตุใด Adam Optimizer จึงเป็นที่นิยมในการฝึก Deep Neural Networks เมื่อเทียบกับ Stochastic Gradient Descent (SGD) แบบดั้งเดิม",
      options: [
        "a) Adam ปรับ Learning Rate สำหรับพารามิเตอร์แต่ละตัวแบบไดนามิก",
        "b) Adam ใช้หน่วยความจำน้อยกว่า SGD",
        "c) Adam มีความซับซ้อนในการคำนวณน้อยกว่า SGD",
        "d) Adam ไม่ต้องการการปรับแต่ง Hyperparameters"
      ],
      correct: 0,
      explanation: "Adam Optimizer เป็นที่นิยมเนื่องจากเป็นการรวมข้อดีของ AdaGrad และ RMSProp เข้าด้วยกัน โดยจะปรับ Learning Rate สำหรับพารามิเตอร์แต่ละตัวแบบไดนามิก ทำให้การฝึกมีประสิทธิภาพและรวดเร็ว"
    },
    {
      id: 6,
      question: "ในบริบทของการประมาณฟังก์ชันคลื่นในกลศาสตร์ควอนตัม การใช้ Deep Learning มีข้อดีอย่างไรเมื่อเทียบกับวิธีการคำนวณแบบดั้งเดิม?",
      options: [
        "a) ลดความแม่นยำในการคำนวณ",
        "b) สามารถจัดการกับระบบหลายอนุภาคที่ซับซ้อนได้ดีกว่า",
        "c) ใช้เวลาในการคำนวณนานกว่า",
        "d) ไม่สามารถประยุกต์ใช้กับปัญหาควอนตัมได้"
      ],
      correct: 1,
      explanation: "Deep Learning สามารถจัดการกับระบบหลายอนุภาคที่ซับซ้อนได้ดีกว่าวิธีการคำนวณแบบดั้งเดิม โดยเฉพาะในการประมาณฟังก์ชันคลื่น"
    },
    {
      id: 7,
      question: "หากคุณกำลังออกแบบโครงข่ายประสาทเทียมเพื่อจำแนกประเภทของอนุภาคฟิสิกส์จากข้อมูลการชนกันของอนุภาค คุณจะเลือกฟังก์ชันกระตุ้นใดสำหรับชั้นเอาต์พุต และเพราะเหตุใด?",
      options: [
        "a) Sigmoid เพราะเหมาะสำหรับการจำแนกหลายคลาส",
        "b) ReLU เพราะช่วยแก้ปัญหา Vanishing Gradient",
        "c) Softmax เพราะให้ความน่าจะเป็นสำหรับแต่ละคลาสและรวมกันได้ 1",
        "d) Tanh เพราะบีบอัดค่าให้อยู่ในช่วง (-1, 1)"
      ],
      correct: 2,
      explanation: "Softmax ใช้สำหรับชั้นเอาต์พุตของการจำแนกประเภทแบบหลายคลาส โดยแปลงค่าให้เป็นความน่าจะเป็นที่รวมกันได้ 1 ซึ่งเหมาะสำหรับการจำแนกประเภทอนุภาค"
    },
    {
      id: 8,
      question: "จงออกแบบสถาปัตยกรรม Deep Neural Network อย่างง่าย (ระบุจำนวนชั้น, จำนวนเซลล์ประสาทในแต่ละชั้น, ฟังก์ชันกระตุ้น) สำหรับการทำนายพลังงานของระบบโมเลกุล และอธิบายเหตุผลในการเลือกของคุณ",
      options: [
        "a) 1 ชั้นซ่อนเร้น (10 เซลล์, ReLU), ชั้นเอาต์พุต (1 เซลล์, Linear) - เหมาะสำหรับปัญหา Regression",
        "b) 3 ชั้นซ่อนเร้น (100, 50, 25 เซลล์, Sigmoid), ชั้นเอาต์พุต (1 เซลล์, Sigmoid) - เหมาะสำหรับปัญหา Binary Classification",
        "c) 2 ชั้นซ่อนเร้น (64, 32 เซลล์, Tanh), ชั้นเอาต์พุต (10 เซลล์, Softmax) - เหมาะสำหรับปัญหา Multi-class Classification",
        "d) ไม่มีข้อใดถูก"
      ],
      correct: 0,
      explanation: "สำหรับปัญหา Regression เช่น การทำนายพลังงานของระบบโมเลกุล ควรใช้ชั้นเอาต์พุตแบบ Linear และชั้นซ่อนเร้นที่ใช้ ReLU เพื่อประสิทธิภาพที่ดี"
    }
  ];

  const codeExamples = [
    {
      title: "การสร้าง MLP อย่างง่ายด้วย TensorFlow/Keras",
      language: "python",
      badge: "TensorFlow",
      code: `import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.datasets import make_moons
import matplotlib.pyplot as plt

# 1. สร้างข้อมูลตัวอย่างที่ไม่เชิงเส้น (เช่น ปัญหา Two Moons)
X, y = make_moons(n_samples=200, noise=0.15, random_state=42)

# 2. ปรับขนาดข้อมูล (Scaling)
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# 3. แบ่งข้อมูลเป็นชุดฝึกและชุดทดสอบ
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.3, random_state=42)

# 4. สร้างแบบจำลอง MLP
model = Sequential([
    Dense(10, activation='relu', input_shape=(X_train.shape[1],)), # Hidden layer 1
    Dense(10, activation='relu'),                                 # Hidden layer 2
    Dense(1, activation='sigmoid')                                  # Output layer for binary classification
])

# 5. คอมไพล์แบบจำลอง
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# 6. ฝึกแบบจำลอง
history = model.fit(X_train, y_train, epochs=100, batch_size=16, verbose=0, validation_split=0.2)

# 7. ประเมินประสิทธิภาพ
loss, accuracy = model.evaluate(X_test, y_test, verbose=0)
print(f"Test Accuracy: {accuracy:.4f}")

# 8. แสดงผลการจำแนก (Visualization)
def plot_decision_boundary(X, y, model, title):
    x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
    y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
    xx, yy = np.meshgrid(np.arange(x_min, x_max, 0.1),
                         np.arange(y_min, y_max, 0.1))
    
    Z = model.predict(np.c_[xx.ravel(), yy.ravel()])
    Z = (Z > 0.5).reshape(xx.shape)

    plt.contourf(xx, yy, Z, alpha=0.4)
    plt.scatter(X[:, 0], X[:, 1], c=y, s=20, edgecolor='k')
    plt.title(title)
    plt.show()

plot_decision_boundary(X_scaled, y, model, 'MLP Decision Boundary for Two Moons')

# ตัวอย่างการทำนายสำหรับข้อมูลใหม่
new_data = np.array([[-0.5, 0.5], [1.0, -0.5]])
new_data_scaled = scaler.transform(new_data)
predictions = model.predict(new_data_scaled)
print(f"Predictions for new data: {predictions.flatten() > 0.5}")`
    },
    {
      title: "การใช้ Neural Network เพื่อประมาณฟังก์ชันคลื่น (แนวคิด)",
      language: "python", 
      badge: "PyTorch",
      code: `import torch
import torch.nn as nn
import torch.optim as optim
import matplotlib.pyplot as plt

# สมมติ Hamiltonian ของระบบควอนตัม (ตัวอย่างง่ายๆ)
def hamiltonian(x):
    # H = -0.5 * d^2/dx^2 + 0.5 * x^2 (Harmonic Oscillator)
    # สำหรับการสาธิต เราจะใช้ฟังก์ชันพลังงานที่ง่ายกว่า
    return 0.5 * x**2

# สร้าง Neural Network เพื่อประมาณฟังก์ชันคลื่น (psi)
class WaveFunctionApproximator(nn.Module):
    def __init__(self):
        super(WaveFunctionApproximator, self).__init__()
        self.fc1 = nn.Linear(1, 64) # Input: position (x)
        self.fc2 = nn.Linear(64, 64)
        self.fc3 = nn.Linear(64, 1)  # Output: psi(x)

    def forward(self, x):
        x = torch.tanh(self.fc1(x))
        x = torch.tanh(self.fc2(x))
        return x # psi(x) - อาจต้องปรับให้เป็นค่าบวกและเป็น normalized

# ฟังก์ชัน Loss ที่อิงจาก Schrödinger Equation (แนวคิด)
def schrodinger_loss(model, x_points):
    x_points.requires_grad_(True)
    psi = model(x_points)

    # คำนวณอนุพันธ์อันดับหนึ่ง (d_psi/dx)
    d_psi_dx = torch.autograd.grad(psi, x_points, grad_outputs=torch.ones_like(psi), create_graph=True)[0]

    # คำนวณอนุพันธ์อันดับสอง (d^2_psi/dx^2)
    d2_psi_dx2 = torch.autograd.grad(d_psi_dx, x_points, grad_outputs=torch.ones_like(d_psi_dx), create_graph=True)[0]

    # Schrödinger Equation: H_op psi = E psi
    # สำหรับ Harmonic Oscillator: -0.5 * d^2_psi/dx^2 + 0.5 * x^2 * psi = E * psi
    # เราจะพยายามทำให้ (H_op psi - E psi)^2 มีค่าน้อยที่สุด
    # ในตัวอย่างนี้ เราจะใช้ variational principle: E = <psi|H|psi> / <psi|psi>
    # และพยายามลด E ลง

    # สำหรับการสาธิต เราจะใช้ loss ที่ง่ายกว่า: (H_op psi - E_target * psi)^2
    # โดย E_target คือพลังงานที่เราต้องการให้โมเดลประมาณได้ (เช่น ground state energy)
    E_target = 0.5 # Ground state energy for quantum harmonic oscillator

    # Approximate H_op psi
    H_psi = -0.5 * d2_psi_dx2 + 0.5 * x_points**2 * psi

    loss = torch.mean((H_psi - E_target * psi)**2)
    return loss

# สร้างโมเดลและ Optimizer
model = WaveFunctionApproximator()
optimizer = optim.Adam(model.parameters(), lr=0.01)

# จุดสำหรับฝึก (เช่น ตำแหน่ง x)
x_train = torch.linspace(-3, 3, 100).reshape(-1, 1)

# ฝึกโมเดล
epochs = 1000
for epoch in range(epochs):
    optimizer.zero_grad()
    loss = schrodinger_loss(model, x_train)
    loss.backward()
    optimizer.step()
    if (epoch + 1) % 100 == 0:
        print(f"Epoch {epoch+1}/{epochs}, Loss: {loss.item():.4f}")

# พล็อตผลลัพธ์ (เปรียบเทียบกับฟังก์ชันคลื่นจริงของ Harmonic Oscillator)
# (ต้องมีการคำนวณฟังก์ชันคลื่นจริงเพื่อเปรียบเทียบ)
# สำหรับการสาธิตนี้ เราจะพล็อตฟังก์ชันคลื่นที่ประมาณได้

plt.figure(figsize=(8, 6))
plt.plot(x_train.detach().numpy(), model(x_train).detach().numpy(), label='Approximate Wave Function')
plt.xlabel('Position (x)')
plt.ylabel('Psi(x)')
plt.title('Neural Network Approximation of Wave Function')
plt.grid(True)
plt.legend()
plt.show()`
    }
  ];

  const toggleSectionCompletion = (sectionId) => {
    const newCompleted = new Set(completedSections);
    if (newCompleted.has(sectionId)) {
      newCompleted.delete(sectionId);
    } else {
      newCompleted.add(sectionId);
    }
    setCompletedSections(newCompleted);
  };

  const handleQuizAnswer = (questionId, answerIndex) => {
    setQuizAnswers(prev => ({
      ...prev,
      [questionId]: answerIndex
    }));
  };

  const submitQuiz = () => {
    let score = 0;
    quizQuestions.forEach(q => {
      if (quizAnswers[q.id] === q.correct) {
        score++;
      }
    });
    setQuizScore(score);
    setQuizSubmitted(true);
  };

  const progressPercentage = (completedSections.size / sections.length) * 100;

  return (
    <div className="min-h-screen bg-gradient-to-br from-purple-50 via-pink-50 to-red-50 dark:from-gray-900 dark:via-purple-900 dark:to-pink-900">
      {/* Chapter Header */}
      <div className="bg-gradient-to-r from-purple-600 via-pink-600 to-red-600 text-white">
        <div className="container mx-auto px-6 py-8">
          <div className="flex items-center justify-between">
            <div className="flex items-center space-x-4">
              <div className="p-3 bg-white/20 rounded-lg backdrop-blur-sm">
                <Brain className="h-8 w-8" />
              </div>
              <div>
                <div className="flex items-center space-x-2 mb-2">
                  <Badge variant="secondary" className="bg-white/20 text-white border-white/30">
                    บทที่ {chapterInfo.number} • {chapterInfo.level}
                  </Badge>
                </div>
                <h1 className="text-3xl font-bold mb-2">{chapterInfo.title}</h1>
                <p className="text-lg text-white/90 mb-4">{chapterInfo.subtitle}</p>
                <p className="text-white/80 max-w-4xl">{chapterInfo.description}</p>
              </div>
            </div>
            <div className="text-right">
              <div className="text-4xl font-bold mb-2">{Math.round(progressPercentage)}%</div>
              <div className="text-white/80">ความคืบหน้า</div>
            </div>
          </div>
          
          <div className="mt-6 grid grid-cols-1 md:grid-cols-4 gap-4">
            <div className="flex items-center space-x-2">
              <Clock className="h-5 w-5 text-white/70" />
              <span>ระยะเวลา: {chapterInfo.duration}</span>
            </div>
            <div className="flex items-center space-x-2">
              <BookOpen className="h-5 w-5 text-white/70" />
              <span>หัวข้อ: {chapterInfo.topics} หัวข้อ</span>
            </div>
            <div className="flex items-center space-x-2">
              <TrendingUp className="h-5 w-5 text-white/70" />
              <span>เสร็จแล้ว: {completedSections.size}/{sections.length}</span>
            </div>
            <div className="flex items-center space-x-2">
              <Network className="h-5 w-5 text-white/70" />
              <span>ระดับ: {chapterInfo.difficulty}</span>
            </div>
          </div>
          
          <div className="mt-4">
            <Progress value={progressPercentage} className="h-2 bg-white/20" />
          </div>
        </div>
      </div>

      {/* Content Tabs */}
      <div className="container mx-auto px-6 py-8">
        <Tabs value={activeTab} onValueChange={setActiveTab} className="w-full">
          <TabsList className="grid w-full grid-cols-4 mb-8">
            <TabsTrigger value="content" className="flex items-center space-x-2">
              <BookOpen className="h-4 w-4" />
              <span>เนื้อหา</span>
            </TabsTrigger>
            <TabsTrigger value="simulations" className="flex items-center space-x-2">
              <Zap className="h-4 w-4" />
              <span>การจำลอง</span>
            </TabsTrigger>
            <TabsTrigger value="code" className="flex items-center space-x-2">
              <FileText className="h-4 w-4" />
              <span>โค้ดตัวอย่าง</span>
            </TabsTrigger>
            <TabsTrigger value="quiz" className="flex items-center space-x-2">
              <CheckCircle className="h-4 w-4" />
              <span>แบบทดสอบ</span>
            </TabsTrigger>
          </TabsList>

          {/* Content Tab */}
          <TabsContent value="content" className="space-y-6">
            <div className="grid gap-6">
              {sections.map((section, index) => (
                <motion.div
                  key={section.id}
                  initial={{ opacity: 0, y: 20 }}
                  animate={{ opacity: 1, y: 0 }}
                  transition={{ delay: index * 0.1 }}
                >
                  <Card className={`transition-all duration-300 ${
                    completedSections.has(section.id) 
                      ? 'border-green-500 bg-green-50 dark:bg-green-900/20' 
                      : 'hover:shadow-lg'
                  }`}>
                    <CardHeader>
                      <div className="flex items-start justify-between">
                        <div className="flex items-start space-x-4">
                          <div className={`w-10 h-10 rounded-full flex items-center justify-center text-white font-bold ${
                            completedSections.has(section.id) 
                              ? 'bg-green-500' 
                              : 'bg-purple-500'
                          }`}>
                            {completedSections.has(section.id) ? (
                              <CheckCircle className="h-5 w-5" />
                            ) : (
                              section.id
                            )}
                          </div>
                          <div className="flex-1">
                            <CardTitle className="text-xl mb-2">{section.title}</CardTitle>
                            <div className="flex items-center space-x-4 text-sm text-gray-600 dark:text-gray-300 mb-3">
                              <span className="flex items-center space-x-1">
                                <Clock className="h-4 w-4" />
                                <span>{section.duration}</span>
                              </span>
                            </div>
                            <CardDescription className="text-base">
                              {section.description}
                            </CardDescription>
                          </div>
                        </div>
                        <Button
                          onClick={() => toggleSectionCompletion(section.id)}
                          variant={completedSections.has(section.id) ? "default" : "outline"}
                          className={completedSections.has(section.id) ? "bg-green-500 hover:bg-green-600" : ""}
                        >
                          {completedSections.has(section.id) ? "เสร็จแล้ว" : "ทำเครื่องหมายเสร็จ"}
                        </Button>
                      </div>
                    </CardHeader>
                    <CardContent>
                      <div className="space-y-4">
                        {section.content}
                        <div>
                          <h4 className="font-semibold mb-2">จุดสำคัญ:</h4>
                          <ul className="list-disc list-inside space-y-1 text-gray-700 dark:text-gray-300">
                            {section.keyPoints.map((point, idx) => (
                              <li key={idx}>{point}</li>
                            ))}
                          </ul>
                        </div>
                        <div>
                          <h4 className="font-semibold mb-2">ตัวอย่างการประยุกต์ใช้:</h4>
                          <ul className="list-disc list-inside space-y-1 text-gray-700 dark:text-gray-300">
                            {section.applications.map((app, idx) => (
                              <li key={idx}>{app}</li>
                            ))}
                          </ul>
                        </div>
                      </div>
                    </CardContent>
                  </Card>
                </motion.div>
              ))}
            </div>
          </TabsContent>

          {/* Simulations Tab */}
          <TabsContent value="simulations" className="space-y-6">
            <div className="text-center mb-8">
              <h2 className="text-2xl font-bold mb-2">การจำลองแบบโต้ตอบ Neural Networks และ Deep Learning</h2>
              <p className="text-gray-600 dark:text-gray-300">สำรวจการทำงานของโครงข่ายประสาทเทียมและเทคนิคการเรียนรู้เชิงลึก</p>
            </div>

            <div className="grid gap-8">
              {/* Neural Network Architecture Simulation */}
              <Card>
                <CardHeader>
                  <div className="flex items-center space-x-2">
                    <Badge className="bg-purple-500">การจำลอง</Badge>
                    <CardTitle>สถาปัตยกรรม Neural Network แบบโต้ตอบ</CardTitle>
                  </div>
                  <CardDescription>
                    เข้าใจการทำงานของ Multi-layer Perceptron และการไหลของข้อมูล
                  </CardDescription>
                </CardHeader>
                <CardContent>
                  <InteractiveSimulation 
                    type="neural_network"
                    title="Neural Network Architecture"
                  />
                </CardContent>
              </Card>

              {/* Backpropagation Simulation */}
              <Card>
                <CardHeader>
                  <div className="flex items-center space-x-2">
                    <Badge className="bg-purple-500">การจำลอง</Badge>
                    <CardTitle>การจำลอง Backpropagation Algorithm</CardTitle>
                  </div>
                  <CardDescription>
                    เข้าใจกระบวนการ Backpropagation และการอัปเดต weights
                  </CardDescription>
                </CardHeader>
                <CardContent>
                  <InteractiveSimulation 
                    type="backpropagation"
                    title="Backpropagation Visualization"
                  />
                </CardContent>
              </Card>

              {/* Activation Functions Comparison */}
              <Card>
                <CardHeader>
                  <div className="flex items-center space-x-2">
                    <Badge className="bg-purple-500">การจำลอง</Badge>
                    <CardTitle>การเปรียบเทียบ Activation Functions</CardTitle>
                  </div>
                  <CardDescription>
                    เปรียบเทียบฟังก์ชันกระตุ้นต่างๆ และผลกระทบต่อการเรียนรู้
                  </CardDescription>
                </CardHeader>
                <CardContent>
                  <InteractiveSimulation 
                    type="activation_functions"
                    title="Activation Functions Comparison"
                  />
                </CardContent>
              </Card>
            </div>
          </TabsContent>

          {/* Code Examples Tab */}
          <TabsContent value="code" className="space-y-6">
            <div className="text-center mb-8">
              <h2 className="text-2xl font-bold mb-2">ตัวอย่างโค้ด Python</h2>
              <p className="text-gray-600 dark:text-gray-300">เรียนรู้และฝึกฝนการใช้ Neural Networks และ Deep Learning สำหรับฟิสิกส์</p>
            </div>

            <Card>
              <CardHeader>
                <div className="flex items-center space-x-2">
                  <div className="p-2 bg-purple-500 rounded-lg">
                    <Brain className="h-5 w-5 text-white" />
                  </div>
                  <div>
                    <CardTitle>Neural Networks และ Deep Learning สำหรับฟิสิกส์ - บทที่ 5</CardTitle>
                    <CardDescription>ตัวอย่างการใช้งาน Neural Networks ในการแก้ปัญหาทางฟิสิกส์</CardDescription>
                  </div>
                  <Badge className="bg-purple-500 text-white">Interactive</Badge>
                </div>
              </CardHeader>
              <CardContent>
                <CodePlayground 
                  examples={codeExamples}
                  defaultExample={0}
                />
              </CardContent>
            </Card>
          </TabsContent>

          {/* Quiz Tab */}
          <TabsContent value="quiz" className="space-y-6">
            <div className="text-center mb-8">
              <h2 className="text-2xl font-bold mb-2">แบบทดสอบบทที่ 5</h2>
              <p className="text-gray-600 dark:text-gray-300">ทดสอบความเข้าใจเกี่ยวกับ Neural Networks และ Deep Learning</p>
            </div>

            <Card>
              <CardHeader>
                <CardTitle>คำถามเกี่ยวกับ Neural Networks และ Deep Learning</CardTitle>
                <CardDescription>
                  {quizSubmitted 
                    ? `คุณได้คะแนน ${quizScore}/${quizQuestions.length} คะแนน (${Math.round((quizScore/quizQuestions.length)*100)}%)`
                    : "เลือกคำตอบที่ถูกต้องที่สุดสำหรับแต่ละคำถาม"
                  }
                </CardDescription>
              </CardHeader>
              <CardContent className="space-y-6">
                {quizQuestions.map((question, index) => (
                  <div key={question.id} className="space-y-4">
                    <h3 className="font-semibold">
                      {index + 1}. {question.question}
                    </h3>
                    <div className="space-y-2">
                      {question.options.map((option, optionIndex) => (
                        <label 
                          key={optionIndex}
                          className={`flex items-center space-x-3 p-3 rounded-lg border cursor-pointer transition-colors ${
                            quizSubmitted
                              ? optionIndex === question.correct
                                ? 'bg-green-100 border-green-500 dark:bg-green-900/20'
                                : quizAnswers[question.id] === optionIndex
                                ? 'bg-red-100 border-red-500 dark:bg-red-900/20'
                                : 'hover:bg-gray-50 dark:hover:bg-gray-800'
                              : quizAnswers[question.id] === optionIndex
                              ? 'bg-purple-100 border-purple-500 dark:bg-purple-900/20'
                              : 'hover:bg-gray-50 dark:hover:bg-gray-800'
                          }`}
                        >
                          <input
                            type="radio"
                            name={`question-${question.id}`}
                            value={optionIndex}
                            checked={quizAnswers[question.id] === optionIndex}
                            onChange={() => handleQuizAnswer(question.id, optionIndex)}
                            className="form-radio h-4 w-4 text-purple-600"
                            disabled={quizSubmitted}
                          />
                          <span>{option}</span>
                        </label>
                      ))}
                    </div>
                    {quizSubmitted && quizAnswers[question.id] !== undefined && (
                      <motion.div
                        initial={{ opacity: 0, height: 0 }}
                        animate={{ opacity: 1, height: 'auto' }}
                        transition={{ duration: 0.3 }}
                        className={`mt-2 p-3 rounded-lg ${
                          quizAnswers[question.id] === question.correct
                            ? 'bg-green-50 border-green-300 text-green-800 dark:bg-green-900/30 dark:text-green-200'
                            : 'bg-red-50 border-red-300 text-red-800 dark:bg-red-900/30 dark:text-red-200'
                        }`}
                      >
                        <p className="font-semibold">คำอธิบาย:</p>
                        <p>{question.explanation}</p>
                      </motion.div>
                    )}
                  </div>
                ))}
                <Button 
                  onClick={submitQuiz} 
                  className="w-full py-3 text-lg bg-purple-600 hover:bg-purple-700 text-white"
                  disabled={quizSubmitted}
                >
                  ส่งคำตอบ
                </Button>
                {quizSubmitted && (
                  <Button 
                    onClick={() => { setQuizSubmitted(false); setQuizAnswers({}); setQuizScore(0); }}
                    className="w-full py-3 text-lg mt-2 bg-gray-300 hover:bg-gray-400 text-gray-800"
                  >
                    ลองอีกครั้ง
                  </Button>
                )}
              </CardContent>
            </Card>
          </TabsContent>
        </Tabs>
      </div>
    </div>
  );
};

export default Chapter5Enhanced;

