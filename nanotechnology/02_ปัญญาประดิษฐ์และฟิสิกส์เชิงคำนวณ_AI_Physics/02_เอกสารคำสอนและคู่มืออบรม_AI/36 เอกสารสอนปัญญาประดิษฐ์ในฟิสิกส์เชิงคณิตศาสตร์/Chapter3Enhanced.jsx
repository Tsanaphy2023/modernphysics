import React, { useState, useEffect } from 'react';
import { motion } from 'framer-motion';
import { BookOpen, Clock, CheckCircle, Play, Download, Copy, RotateCcw, TrendingUp, Target, BarChart3 } from 'lucide-react';
import CodePlayground from './CodePlayground';
import InteractiveSimulation from './InteractiveSimulation';

const Chapter3Enhanced = () => {
  const [activeTab, setActiveTab] = useState('content');
  const [completedSections, setCompletedSections] = useState(new Set());
  const [quizAnswers, setQuizAnswers] = useState({});
  const [quizSubmitted, setQuizSubmitted] = useState(false);
  const [quizScore, setQuizScore] = useState(0);

  const sections = [
    {
      id: '3.1',
      title: 'ภาพรวมของการเรียนรู้แบบมีผู้สอน',
      duration: '30 นาที',
      overview: 'ทำความเข้าใจหลักการพื้นฐานของ Supervised Learning และการประยุกต์ใช้ในการแก้ปัญหาทางฟิสิกส์',
      keyPoints: [
        'ความแตกต่างระหว่าง Regression และ Classification',
        'การแบ่งข้อมูลเป็น Training, Validation และ Test sets',
        'แนวคิดของ Overfitting และ Underfitting',
        'การประเมินประสิทธิภาพของแบบจำลอง',
        'ประเภทของปัญหา Supervised Learning ในฟิสิกส์',
        'การเตรียมข้อมูลและ Feature Engineering'
      ],
      examples: [
        'การทำนายอุณหภูมิจากข้อมูลสภาพอากาศ (Regression)',
        'การจำแนกประเภทอนุภาคจากข้อมูล detector (Classification)',
        'การวิเคราะห์ข้อมูลการทดลองในฟิสิกส์อนุภาค',
        'การทำนายพลังงานจากตัวแปรทางฟิสิกส์',
        'การจำแนกสถานะของระบบควอนตัม'
      ],
      detailedContent: `
        การเรียนรู้แบบมีผู้สอน (Supervised Learning) เป็นแนวทางการเรียนรู้ของเครื่องที่ใช้ข้อมูลที่มีป้ายกำกับ (labeled data) ในการฝึกสอนแบบจำลอง เพื่อให้สามารถทำนายผลลัพธ์สำหรับข้อมูลใหม่ที่ไม่เคยเห็นมาก่อน

        **ประเภทของปัญหา Supervised Learning:**

        1. **การถดถอย (Regression)**: ทำนายค่าต่อเนื่อง เช่น อุณหภูมิ, ราคา, พลังงาน
        2. **การจำแนกประเภท (Classification)**: ทำนายหมวดหมู่หรือคลาส เช่น ประเภทอนุภาค, การวินิจฉัยโรค

        **การแบ่งข้อมูล:**
        - Training Set (60-70%): ใช้สำหรับฝึกสอนแบบจำลอง
        - Validation Set (15-20%): ใช้สำหรับปรับแต่งพารามิเตอร์
        - Test Set (15-20%): ใช้สำหรับประเมินประสิทธิภาพสุดท้าย

        **ปัญหา Overfitting และ Underfitting:**
        - Overfitting: แบบจำลองจำข้อมูลฝึกสอนได้ดีเกินไป แต่ทำงานได้แย่กับข้อมูลใหม่
        - Underfitting: แบบจำลองเรียนรู้ไม่เพียงพอ ทำงานได้แย่ทั้งข้อมูลฝึกสอนและข้อมูลใหม่
      `
    },
    {
      id: '3.2',
      title: 'Linear Regression และการประยุกต์ใช้',
      duration: '45 นาที',
      overview: 'ศึกษาอัลกอริทึม Linear Regression และการใช้งานในการวิเคราะห์ข้อมูลทางฟิสิกส์',
      keyPoints: [
        'สมการ Linear Regression และการหาค่าพารามิเตอร์',
        'วิธี Least Squares และ Normal Equation',
        'การใช้ Regularization (Ridge และ Lasso)',
        'การประเมินผลด้วย R-squared และ RMSE',
        'Gradient Descent Algorithm',
        'การจัดการกับ Multicollinearity'
      ],
      examples: [
        'การหาความสัมพันธ์ระหว่างแรงและการเร่ง',
        'การวิเคราะห์ข้อมูลการสั่นของลูกตุ้ม',
        'การทำนายพลังงานจากตัวแปรทางฟิสิกส์',
        'การวิเคราะห์ข้อมูลสเปกตรัม',
        'การศึกษาความสัมพันธ์ระหว่างตัวแปรทางฟิสิกส์'
      ],
      detailedContent: `
        Linear Regression เป็นอัลกอริทึมพื้นฐานสำหรับปัญหาการถดถอย ที่หาความสัมพันธ์เชิงเส้นระหว่างตัวแปรอิสระ (features) และตัวแปรตาม (target)

        **สมการ Linear Regression:**
        
        สำหรับตัวแปรเดียว: y = β₀ + β₁x + ε
        สำหรับหลายตัวแปร: y = β₀ + β₁x₁ + β₂x₂ + ... + βₙxₙ + ε

        **วิธี Least Squares:**
        การหาค่าสัมประสิทธิ์ที่ดีที่สุดโดยการลดค่า Sum of Squared Errors (SSE):
        SSE = Σ(yᵢ - ŷᵢ)²

        **การประเมินประสิทธิภาพ:**
        - R-squared (R²): วัดสัดส่วนของความแปรปรวนที่อธิบายได้
        - RMSE: Root Mean Square Error
        - MAE: Mean Absolute Error

        **Regularization:**
        - Ridge Regression: เพิ่ม L2 penalty
        - Lasso Regression: เพิ่ม L1 penalty
        - Elastic Net: รวม L1 และ L2 penalty
      `
    },
    {
      id: '3.3',
      title: 'Polynomial Regression และ Feature Engineering',
      duration: '40 นาที',
      overview: 'การขยายความสามารถของ Linear Regression ด้วย Polynomial features และเทคนิค Feature Engineering',
      keyPoints: [
        'การสร้าง Polynomial features และ Interaction terms',
        'เทคนิค Feature Scaling และ Normalization',
        'การเลือก Features ที่เหมาะสม',
        'การจัดการกับ Curse of Dimensionality',
        'Cross-validation สำหรับเลือก degree ที่เหมาะสม',
        'การใช้ Regularization กับ Polynomial Regression'
      ],
      examples: [
        'การสร้างแบบจำลองการเคลื่อนที่แบบโค้ง',
        'การวิเคราะห์ข้อมูลสเปกตรัมด้วย Polynomial fitting',
        'การประยุกต์ใช้ในการวิเคราะห์สัญญาณฟิสิกส์',
        'การสร้างแบบจำลองพฤติกรรมของระบบไม่เชิงเส้น',
        'การวิเคราะห์ข้อมูลการทดลองที่มีความซับซ้อน'
      ],
      detailedContent: `
        Polynomial Regression ขยายความสามารถของ Linear Regression ด้วยการเพิ่ม polynomial features

        **สมการ Polynomial Regression:**
        y = β₀ + β₁x + β₂x² + β₃x³ + ... + βₙxⁿ

        **Feature Engineering:**
        1. **Polynomial Features**: สร้าง x², x³, x⁴, ...
        2. **Interaction Terms**: สร้าง x₁×x₂, x₁×x₃, ...
        3. **Feature Scaling**: StandardScaler, MinMaxScaler
        4. **Feature Selection**: SelectKBest, RFE

        **การจัดการกับ Curse of Dimensionality:**
        - เมื่อจำนวน features เพิ่มขึ้น อาจเกิดปัญหา Overfitting
        - ใช้ Regularization (Ridge, Lasso) เพื่อควบคุม
        - Cross-validation สำหรับเลือก degree ที่เหมาะสม

        **การประยุกต์ใช้ในฟิสิกส์:**
        - การสร้างแบบจำลองการเคลื่อนที่แบบโค้ง
        - การวิเคราะห์ข้อมูลสเปกตรัม
        - การศึกษาพฤติกรรมไม่เชิงเส้นของระบบฟิสิกส์
      `
    },
    {
      id: '3.4',
      title: 'Logistic Regression และ Classification',
      duration: '50 นาที',
      overview: 'หลักการของ Logistic Regression สำหรับปัญหา Classification และการประยุกต์ใช้ในฟิสิกส์',
      keyPoints: [
        'ฟังก์ชัน Sigmoid และ Logistic function',
        'Maximum Likelihood Estimation สำหรับ Logistic Regression',
        'การจัดการกับ Multi-class Classification',
        'การประเมินผลด้วย Confusion Matrix และ ROC Curve',
        'Decision Boundary และการตีความผลลัพธ์',
        'การจัดการกับ Imbalanced Data'
      ],
      examples: [
        'การจำแนกประเภทสัญญาณจาก particle detector',
        'การแยกแยะสถานะของระบบควอนตัม',
        'การจำแนกประเภทดาวฤกษ์จากข้อมูลสเปกตรัม',
        'การตรวจจับสัญญาณ Gravitational Waves',
        'การจำแนกประเภทกาแล็กซี'
      ],
      detailedContent: `
        Logistic Regression ใช้สำหรับปัญหา Classification โดยใช้ฟังก์ชัน Sigmoid

        **ฟังก์ชัน Sigmoid:**
        σ(z) = 1 / (1 + e^(-z))
        โดยที่ z = β₀ + β₁x₁ + β₂x₂ + ... + βₙxₙ

        **Maximum Likelihood Estimation:**
        การหาค่าพารามิเตอร์ที่ดีที่สุดโดยการเพิ่มค่า likelihood:
        L(β) = Π[p(xᵢ)^yᵢ × (1-p(xᵢ))^(1-yᵢ)]

        **Multi-class Classification:**
        1. One-vs-Rest (OvR): สร้างแบบจำลองแยกสำหรับแต่ละคลาส
        2. One-vs-One (OvO): สร้างแบบจำลองสำหรับทุกคู่ของคลาส
        3. Multinomial Logistic Regression: ขยายสำหรับหลายคลาส

        **การประเมินประสิทธิภาพ:**
        - Confusion Matrix: แสดงการทำนายที่ถูกและผิด
        - Accuracy, Precision, Recall, F1-score
        - ROC Curve และ AUC: วัดประสิทธิภาพการแยกแยะ
      `
    },
    {
      id: '3.5',
      title: 'Support Vector Machines (SVM)',
      duration: '55 นาที',
      overview: 'อัลกอริทึม SVM สำหรับ Classification และ Regression พร้อมการใช้ Kernel tricks',
      keyPoints: [
        'แนวคิดของ Maximum Margin Classifier',
        'การใช้ Kernel functions (Linear, Polynomial, RBF)',
        'การจัดการกับข้อมูลที่ไม่สามารถแยกเชิงเส้นได้',
        'SVM สำหรับ Regression (SVR)',
        'Support Vectors และความสำคัญ',
        'การปรับแต่งพารามิเตอร์ C และ gamma'
      ],
      examples: [
        'การจำแนกประเภทอนุภาคด้วย SVM',
        'การวิเคราะห์ข้อมูลภาพจากกล้องโทรทรรศน์',
        'การประยุกต์ใช้ในการวิเคราะห์ข้อมูลจีโนม',
        'การตรวจจับสัญญาณในข้อมูลฟิสิกส์',
        'การจำแนกประเภทวัสดุจากคุณสมบัติทางฟิสิกส์'
      ],
      detailedContent: `
        SVM เป็นอัลกอริทึมที่มีประสิทธิภาพสูงสำหรับทั้ง Classification และ Regression

        **แนวคิด Maximum Margin:**
        SVM หาเส้นแบ่ง (hyperplane) ที่มี margin สูงสุด:
        margin = 2 / ||w||

        **Support Vectors:**
        จุดข้อมูลที่อยู่บนขอบของ margin เรียกว่า Support Vectors ซึ่งเป็นจุดที่สำคัญที่สุดในการกำหนดเส้นแบ่ง

        **Kernel Functions:**
        1. Linear Kernel: K(x, x') = x · x'
        2. Polynomial Kernel: K(x, x') = (γx · x' + r)^d
        3. RBF Kernel: K(x, x') = exp(-γ||x - x'||²)

        **SVM สำหรับ Regression (SVR):**
        SVR ใช้แนวคิดของ ε-insensitive loss function ไม่มีการลงโทษสำหรับข้อผิดพลาดที่น้อยกว่า ε
      `
    },
    {
      id: '3.6',
      title: 'Decision Trees และ Ensemble Methods',
      duration: '50 นาที',
      overview: 'อัลกอริทึม Decision Trees และการปรับปรุงประสิทธิภาพด้วย Ensemble methods',
      keyPoints: [
        'การสร้าง Decision Trees และ Splitting criteria',
        'การป้องกัน Overfitting ด้วย Pruning',
        'Random Forest และ Bagging',
        'Gradient Boosting และ AdaBoost',
        'Feature Importance และการตีความ',
        'การปรับแต่งพารามิเตอร์ของ Ensemble Methods'
      ],
      examples: [
        'การตัดสินใจในการวิเคราะห์ข้อมูลการทดลอง',
        'การจำแนกประเภทสภาพอากาศจากข้อมูลเซ็นเซอร์',
        'การประยุกต์ใช้ในการวิเคราะห์ข้อมูลทางการแพทย์',
        'การวิเคราะห์ข้อมูลจากการทดลองฟิสิกส์',
        'การจำแนกประเภทสัญญาณในระบบควบคุม'
      ],
      detailedContent: `
        Decision Trees สร้างแบบจำลองในรูปของต้นไม้ตัดสินใจ

        **Splitting Criteria:**
        สำหรับ Classification:
        - Gini Impurity: Gini = 1 - Σpᵢ²
        - Entropy: H = -Σpᵢlog₂(pᵢ)
        - Information Gain: IG = H(parent) - Σ(nᵢ/n)H(child_i)

        สำหรับ Regression:
        - Mean Squared Error (MSE)
        - Mean Absolute Error (MAE)

        **การป้องกัน Overfitting:**
        1. Pruning: ตัดกิ่งที่ไม่จำเป็น
        2. พารามิเตอร์ควบคุม: max_depth, min_samples_split

        **Ensemble Methods:**
        1. Bagging (Random Forest): รวม Decision Trees หลายต้น
        2. Boosting (AdaBoost, Gradient Boosting): ปรับปรุงแบบจำลองแบบต่อเนื่อง
      `
    },
    {
      id: '3.7',
      title: 'Model Evaluation และ Cross-Validation',
      duration: '40 นาที',
      overview: 'เทคนิคการประเมินประสิทธิภาพของแบบจำลองและการป้องกัน Overfitting',
      keyPoints: [
        'K-Fold Cross-Validation และ Stratified sampling',
        'Metrics สำหรับ Regression: MAE, MSE, R-squared',
        'Metrics สำหรับ Classification: Accuracy, Precision, Recall, F1-score',
        'การใช้ Learning Curves และ Validation Curves',
        'Grid Search และ Random Search สำหรับ Hyperparameter Tuning',
        'การจัดการกับ Data Leakage'
      ],
      examples: [
        'การประเมินแบบจำลองการทำนายสภาพอากาศ',
        'การวิเคราะห์ประสิทธิภาพของ detector ในฟิสิกส์อนุภาค',
        'การเปรียบเทียบอัลกอริทึมต่างๆ ในงานวิจัย',
        'การประเมินแบบจำลองการทำนายคุณสมบัติวัสดุ',
        'การวิเคราะห์ความเสถียรของแบบจำลอง'
      ],
      detailedContent: `
        การประเมินประสิทธิภาพของแบบจำลองเป็นขั้นตอนสำคัญในการพัฒนา Machine Learning

        **Cross-Validation:**
        1. K-Fold Cross-Validation: แบ่งข้อมูลเป็น K ส่วน
        2. Stratified K-Fold: รักษาสัดส่วนของแต่ละคลาส
        3. Leave-One-Out (LOO): ใช้ตัวอย่างหนึ่งตัวสำหรับทดสอบ

        **Learning Curves:**
        การพล็อตประสิทธิภาพเทียบกับขนาดข้อมูล เพื่อดูว่าแบบจำลองต้องการข้อมูลเพิ่มหรือไม่

        **Validation Curves:**
        การพล็อตประสิทธิภาพเทียบกับค่าพารามิเตอร์ เพื่อหาค่าที่เหมาะสม

        **Hyperparameter Tuning:**
        - Grid Search: ทดสอบทุกการผสมผสานของพารามิเตอร์
        - Random Search: สุ่มเลือกการผสมผสานของพารามิเตอร์
      `
    },
    {
      id: '3.8',
      title: 'การประยุกต์ใช้ในฟิสิกส์ขั้นสูง',
      duration: '45 นาที',
      overview: 'กรณีศึกษาการประยุกต์ใช้ Supervised Learning ในงานวิจัยฟิสิกส์ขั้นสูง',
      keyPoints: [
        'การวิเคราะห์ข้อมูลจาก Large Hadron Collider (LHC)',
        'การประยุกต์ใช้ในดาราศาสตร์และฟิสิกส์อวกาศ',
        'การใช้ในการวิเคราะห์ข้อมูลจากการทดลองควอนตัม',
        'การพัฒนาเครื่องมือวิเคราะห์ข้อมูลสำหรับงานวิจัย',
        'การใช้ AI ในการออกแบบการทดลอง',
        'การประยุกต์ใช้ในฟิสิกส์วัสดุและนาโนเทคโนโลยี'
      ],
      examples: [
        'การค้นหา Higgs Boson ด้วย Machine Learning',
        'การจำแนกประเภท Gravitational Waves',
        'การวิเคราะห์ข้อมูลจาก Cosmic Microwave Background',
        'การทำนายคุณสมบัติของวัสดุใหม่',
        'การควบคุมระบบควอนตัมด้วย AI'
      ],
      detailedContent: `
        การประยุกต์ใช้ Supervised Learning ในฟิสิกส์ขั้นสูงแสดงให้เห็นถึงพลังของ AI ในการขับเคลื่อนการค้นพบทางวิทยาศาสตร์

        **การวิเคราะห์ข้อมูลจาก LHC:**
        - ใช้ Machine Learning ในการจำแนกสัญญาณ Higgs จากสัญญาณรบกวน
        - Features: พลังงาน, โมเมนตัม, มุมของอนุภาค
        - ใช้ Neural Networks และ Boosted Decision Trees

        **การประยุกต์ใช้ในดาราศาสตร์:**
        - การจำแนกประเภทดาวฤกษ์จากข้อมูลสเปกตรัม
        - การค้นหาดาวเคราะห์นอกระบบ
        - การวิเคราะห์ข้อมูลจาก Cosmic Microwave Background

        **การวิเคราะห์ข้อมูลจากการทดลองควอนตัม:**
        - การจำแนกสถานะควอนตัม
        - การควบคุมระบบควอนตัมด้วย Reinforcement Learning
        - การพัฒนาคอมพิวเตอร์ควอนตัม

        **การพัฒนาเครื่องมือวิเคราะห์ข้อมูล:**
        - การสร้างซอฟต์แวร์วิเคราะห์ข้อมูลเฉพาะทาง
        - การพัฒนาอัลกอริทึมสำหรับข้อมูลฟิสิกส์
        - การบูรณาการ AI เข้ากับเครื่องมือวิจัยที่มีอยู่
      `
    }
  ];

  const quizQuestions = [
    {
      id: 1,
      question: 'ความแตกต่างหลักระหว่าง Regression และ Classification คืออะไร?',
      options: [
        'Regression ทำนายค่าต่อเนื่อง, Classification ทำนายหมวดหมู่',
        'Regression ใช้ข้อมูลตัวเลข, Classification ใช้ข้อมูลข้อความ',
        'Regression เร็วกว่า Classification',
        'ไม่มีความแตกต่าง'
      ],
      correct: 0,
      explanation: 'Regression ใช้สำหรับทำนายค่าต่อเนื่อง (เช่น อุณหภูมิ, ราคา) ในขณะที่ Classification ใช้สำหรับทำนายหมวดหมู่หรือคลาส (เช่น ประเภทอนุภาค, การวินิจฉัยโรค)'
    },
    {
      id: 2,
      question: 'ฟังก์ชัน Sigmoid ใน Logistic Regression มีประโยชน์อย่างไร?',
      options: [
        'ทำให้การคำนวณเร็วขึ้น',
        'แปลงค่าใดๆ ให้อยู่ระหว่าง 0 และ 1',
        'ลดความซับซ้อนของแบบจำลอง',
        'เพิ่มความแม่นยำของการทำนาย'
      ],
      correct: 1,
      explanation: 'ฟังก์ชัน Sigmoid แปลงค่าใดๆ ให้อยู่ระหว่าง 0 และ 1 ทำให้สามารถตีความเป็นความน่าจะเป็นได้ และเหมาะสำหรับปัญหา Binary Classification'
    },
    {
      id: 3,
      question: 'Support Vector Machine (SVM) หาอะไรในการสร้างแบบจำลอง?',
      options: [
        'จุดที่มีค่าผิดพลาดน้อยที่สุด',
        'เส้นแบ่งที่มี margin สูงสุด',
        'ค่าเฉลี่ยของข้อมูล',
        'จำนวน features ที่เหมาะสม'
      ],
      correct: 1,
      explanation: 'SVM หาเส้นแบ่ง (hyperplane) ที่มี margin สูงสุด คือระยะห่างจากเส้นแบ่งไปยังจุดข้อมูลที่ใกล้ที่สุดของแต่ละคลาสมากที่สุด'
    },
    {
      id: 4,
      question: 'Cross-Validation ช่วยป้องกันปัญหาใดในการสร้างแบบจำลอง?',
      options: [
        'การคำนวณช้า',
        'Overfitting',
        'ข้อมูลไม่เพียงพอ',
        'การใช้ memory มาก'
      ],
      correct: 1,
      explanation: 'Cross-Validation ช่วยประเมินประสิทธิภาพของแบบจำลองอย่างเป็นกลางและป้องกัน Overfitting โดยการทดสอบแบบจำลองกับข้อมูลที่ไม่เคยเห็นมาก่อน'
    },
    {
      id: 5,
      question: 'Regularization ใน Linear Regression มีวัตถุประสงค์หลักเพื่ออะไร?',
      options: [
        'เพิ่มความเร็วในการคำนวณ',
        'ป้องกัน Overfitting',
        'เพิ่มจำนวน features',
        'ลดขนาดของข้อมูล'
      ],
      correct: 1,
      explanation: 'Regularization (Ridge, Lasso) เพิ่ม penalty term เพื่อควบคุมความซับซ้อนของแบบจำลองและป้องกัน Overfitting'
    },
    {
      id: 6,
      question: 'ใน Decision Trees, Gini Impurity วัดอะไร?',
      options: [
        'ความเร็วในการคำนวณ',
        'ความบริสุทธิ์ของการแบ่งข้อมูล',
        'จำนวนใบของต้นไม้',
        'ความลึกของต้นไม้'
      ],
      correct: 1,
      explanation: 'Gini Impurity วัดความบริสุทธิ์ของการแบ่งข้อมูล ค่าต่ำหมายถึงข้อมูลในกลุ่มนั้นมีคลาสเดียวกันเป็นส่วนใหญ่'
    },
    {
      id: 7,
      question: 'Random Forest ปรับปรุงประสิทธิภาพจาก Decision Tree เดี่ยวอย่างไร?',
      options: [
        'ใช้ข้อมูลน้อยลง',
        'รวมผลลัพธ์จากหลายต้นไม้',
        'คำนวณเร็วกว่า',
        'ใช้ features น้อยลง'
      ],
      correct: 1,
      explanation: 'Random Forest ใช้ Ensemble method โดยรวมผลลัพธ์จาก Decision Trees หลายต้น ทำให้ลดปัญหา Overfitting และเพิ่มความแม่นยำ'
    },
    {
      id: 8,
      question: 'ในการประยุกต์ใช้ Machine Learning กับข้อมูลจาก LHC, ความท้าทายหลักคืออะไร?',
      options: [
        'ข้อมูลมีขนาดเล็ก',
        'ข้อมูลมีขนาดใหญ่มากและมีสัญญาณรบกวนสูง',
        'ไม่มีข้อมูลเพียงพอ',
        'ข้อมูลไม่มีความซับซ้อน'
      ],
      correct: 1,
      explanation: 'ข้อมูลจาก LHC มีขนาดใหญ่มาก (petabytes) และมีสัญญาณรบกวนสูง ต้องใช้เทคนิค ML ขั้นสูงในการแยกสัญญาณที่สำคัญออกจากสัญญาณรบกวน'
    }
  ];

  const codeExamples = [
    {
      title: 'Linear Regression สำหรับข้อมูลฟิสิกส์',
      description: 'การสร้างแบบจำลอง Linear Regression สำหรับวิเคราะห์ความสัมพันธ์ระหว่างแรงและการเร่ง',
      code: `import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score, mean_squared_error

# สร้างข้อมูลตัวอย่าง: ความสัมพันธ์ระหว่างแรงและการเร่ง
np.random.seed(42)
force = np.linspace(1, 10, 100)  # แรง (N)
acceleration = 2 * force + np.random.normal(0, 0.5, 100)  # การเร่ง (m/s²)

# เตรียมข้อมูล
X = force.reshape(-1, 1)
y = acceleration

# แบ่งข้อมูล
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# สร้างและฝึกแบบจำลอง
model = LinearRegression()
model.fit(X_train, y_train)

# ทำนายผล
y_pred = model.predict(X_test)

# ประเมินผล
r2 = r2_score(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)

print(f"Linear Regression Results:")
print(f"Coefficient (slope): {model.coef_[0]:.3f}")
print(f"Intercept: {model.intercept_:.3f}")
print(f"R-squared: {r2:.3f}")
print(f"RMSE: {rmse:.3f}")

# สมการที่ได้
print(f"\\nEquation: acceleration = {model.coef_[0]:.3f} * force + {model.intercept_:.3f}")
print("This follows Newton's second law: F = ma, so a = F/m")`
    },
    {
      title: 'Logistic Regression สำหรับการจำแนกอนุภาค',
      description: 'การใช้ Logistic Regression ในการจำแนกประเภทอนุภาค (electron vs muon)',
      code: `import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix, roc_auc_score
from sklearn.preprocessing import StandardScaler

# สร้างข้อมูลตัวอย่าง: การจำแนกอนุภาค (electron vs muon)
np.random.seed(42)
n_samples = 1000

# Features: พลังงาน, โมเมนตัม, มุม
energy_electron = np.random.normal(50, 15, n_samples//2)
momentum_electron = np.random.normal(45, 12, n_samples//2)
angle_electron = np.random.normal(0.5, 0.2, n_samples//2)

energy_muon = np.random.normal(60, 18, n_samples//2)
momentum_muon = np.random.normal(55, 15, n_samples//2)
angle_muon = np.random.normal(0.7, 0.25, n_samples//2)

# รวมข้อมูล
X = np.vstack([
    np.column_stack([energy_electron, momentum_electron, angle_electron]),
    np.column_stack([energy_muon, momentum_muon, angle_muon])
])

y = np.hstack([np.zeros(n_samples//2), np.ones(n_samples//2)])  # 0: electron, 1: muon

# แบ่งข้อมูล
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Standardize features
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# สร้างและฝึกแบบจำลอง
model = LogisticRegression(random_state=42)
model.fit(X_train_scaled, y_train)

# ทำนายผล
y_pred = model.predict(X_test_scaled)
y_pred_proba = model.predict_proba(X_test_scaled)[:, 1]

# ประเมินผล
accuracy = model.score(X_test_scaled, y_test)
auc = roc_auc_score(y_test, y_pred_proba)

print("Logistic Regression Results:")
print(f"Accuracy: {accuracy:.3f}")
print(f"AUC: {auc:.3f}")
print("\\nClassification Report:")
print(classification_report(y_test, y_pred, target_names=['Electron', 'Muon']))
print("\\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred))`
    },
    {
      title: 'SVM สำหรับการจำแนกข้อมูลที่ซับซ้อน',
      description: 'การใช้ Support Vector Machine กับ RBF kernel สำหรับข้อมูลที่ไม่สามารถแยกเชิงเส้นได้',
      code: `import numpy as np
import matplotlib.pyplot as plt
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.metrics import classification_report, accuracy_score
from sklearn.preprocessing import StandardScaler

# สร้างข้อมูลตัวอย่าง: การจำแนกสัญญาณฟิสิกส์ที่ซับซ้อน
np.random.seed(42)
n_samples = 800

# สร้างข้อมูลแบบ non-linear
theta = np.linspace(0, 2*np.pi, n_samples//2)
r1 = 2 + 0.5 * np.sin(5*theta) + np.random.normal(0, 0.2, n_samples//2)
r2 = 4 + 0.3 * np.cos(7*theta) + np.random.normal(0, 0.2, n_samples//2)

x1_class1 = r1 * np.cos(theta)
y1_class1 = r1 * np.sin(theta)
x1_class2 = r2 * np.cos(theta)
y1_class2 = r2 * np.sin(theta)

X = np.vstack([
    np.column_stack([x1_class1, y1_class1]),
    np.column_stack([x1_class2, y1_class2])
])

y = np.hstack([np.zeros(n_samples//2), np.ones(n_samples//2)])

# แบ่งข้อมูล
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Standardize features
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Grid Search สำหรับหาพารามิเตอร์ที่ดีที่สุด
param_grid = {
    'C': [0.1, 1, 10, 100],
    'gamma': ['scale', 'auto', 0.001, 0.01, 0.1, 1]
}

svm = SVC(kernel='rbf', random_state=42)
grid_search = GridSearchCV(svm, param_grid, cv=5, scoring='accuracy')
grid_search.fit(X_train_scaled, y_train)

# ใช้แบบจำลองที่ดีที่สุด
best_svm = grid_search.best_estimator_
y_pred = best_svm.predict(X_test_scaled)

# ประเมินผล
accuracy = accuracy_score(y_test, y_pred)

print("SVM Results:")
print(f"Best parameters: {grid_search.best_params_}")
print(f"Best cross-validation score: {grid_search.best_score_:.3f}")
print(f"Test accuracy: {accuracy:.3f}")
print("\\nClassification Report:")
print(classification_report(y_test, y_pred))

# แสดงจำนวน Support Vectors
print(f"\\nNumber of support vectors: {best_svm.n_support_}")
print(f"Total support vectors: {len(best_svm.support_vectors_)}")`
    },
    {
      title: 'Random Forest สำหรับการวิเคราะห์ข้อมูลการทดลอง',
      description: 'การใช้ Random Forest ในการวิเคราะห์ข้อมูลการทดลองฟิสิกส์และการประเมิน Feature Importance',
      code: `import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.metrics import classification_report, accuracy_score
import matplotlib.pyplot as plt

# สร้างข้อมูลตัวอย่าง: การทดลองฟิสิกส์อนุภาค
np.random.seed(42)
n_samples = 1000

# Features: พลังงาน, โมเมนตัม, มุม, ความเข้ม, เวลา
features = {
    'energy': np.random.exponential(50, n_samples),
    'momentum': np.random.gamma(2, 25, n_samples),
    'angle': np.random.uniform(0, np.pi, n_samples),
    'intensity': np.random.lognormal(3, 1, n_samples),
    'time': np.random.normal(100, 20, n_samples)
}

# สร้าง target ที่ซับซ้อน (การจำแนกประเภทเหตุการณ์)
def create_target(row):
    if row['energy'] > 60 and row['momentum'] > 40 and row['intensity'] > 15:
        return 2  # Signal
    elif row['energy'] > 30 and row['momentum'] > 20:
        return 1  # Background
    else:
        return 0  # Noise

df = pd.DataFrame(features)
df['target'] = df.apply(create_target, axis=1)

X = df.drop('target', axis=1)
y = df['target']

# แบ่งข้อมูล
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# สร้างและฝึก Random Forest
rf = RandomForestClassifier(
    n_estimators=100,
    max_depth=10,
    min_samples_split=5,
    min_samples_leaf=2,
    random_state=42
)

rf.fit(X_train, y_train)

# ทำนายผล
y_pred = rf.predict(X_test)

# Cross-validation
cv_scores = cross_val_score(rf, X_train, y_train, cv=5)

# ประเมินผล
accuracy = accuracy_score(y_test, y_pred)

print("Random Forest Results:")
print(f"Test accuracy: {accuracy:.3f}")
print(f"Cross-validation scores: {cv_scores}")
print(f"Mean CV score: {cv_scores.mean():.3f} (+/- {cv_scores.std() * 2:.3f})")

print("\\nClassification Report:")
print(classification_report(y_test, y_pred, target_names=['Noise', 'Background', 'Signal']))

# Feature Importance
feature_importance = pd.DataFrame({
    'feature': X.columns,
    'importance': rf.feature_importances_
}).sort_values('importance', ascending=False)

print("\\nFeature Importance:")
print(feature_importance)

# Out-of-bag score
rf_oob = RandomForestClassifier(
    n_estimators=100,
    oob_score=True,
    random_state=42
)
rf_oob.fit(X_train, y_train)
print(f"\\nOut-of-bag score: {rf_oob.oob_score_:.3f}")`
    }
  ];

  const handleSectionComplete = (sectionId) => {
    setCompletedSections(prev => new Set([...prev, sectionId]));
  };

  const handleQuizAnswer = (questionId, answerIndex) => {
    setQuizAnswers(prev => ({
      ...prev,
      [questionId]: answerIndex
    }));
  };

  const handleQuizSubmit = () => {
    let score = 0;
    quizQuestions.forEach(question => {
      if (quizAnswers[question.id] === question.correct) {
        score++;
      }
    });
    setQuizScore(score);
    setQuizSubmitted(true);
  };

  const progressPercentage = Math.round((completedSections.size / sections.length) * 100);

  const tabContent = {
    content: (
      <div className="space-y-6">
        <div className="grid gap-4">
          {sections.map((section) => (
            <motion.div
              key={section.id}
              className={`border rounded-lg p-6 transition-all duration-300 ${
                completedSections.has(section.id)
                  ? 'border-green-300 bg-green-50'
                  : 'border-gray-200 bg-white hover:border-blue-300'
              }`}
              whileHover={{ scale: 1.02 }}
              transition={{ type: "spring", stiffness: 300 }}
            >
              <div className="flex items-start justify-between">
                <div className="flex-1">
                  <div className="flex items-center gap-3 mb-3">
                    <div className={`w-8 h-8 rounded-full flex items-center justify-center text-sm font-bold ${
                      completedSections.has(section.id)
                        ? 'bg-green-500 text-white'
                        : 'bg-purple-500 text-white'
                    }`}>
                      {completedSections.has(section.id) ? <CheckCircle className="w-4 h-4" /> : section.id}
                    </div>
                    <div>
                      <h3 className="text-lg font-semibold text-gray-900">{section.title}</h3>
                      <div className="flex items-center gap-4 text-sm text-gray-600">
                        <span className="flex items-center gap-1">
                          <Clock className="w-4 h-4" />
                          {section.duration}
                        </span>
                      </div>
                    </div>
                  </div>
                  
                  <p className="text-gray-700 mb-4">{section.overview}</p>
                  
                  <div className="mb-4">
                    <h4 className="font-semibold text-gray-900 mb-2">จุดสำคัญ:</h4>
                    <ul className="list-disc list-inside space-y-1 text-gray-700">
                      {section.keyPoints.map((point, index) => (
                        <li key={index}>{point}</li>
                      ))}
                    </ul>
                  </div>
                  
                  <div className="mb-4">
                    <h4 className="font-semibold text-gray-900 mb-2">ตัวอย่างการประยุกต์ใช้:</h4>
                    <ul className="list-disc list-inside space-y-1 text-gray-700">
                      {section.examples.map((example, index) => (
                        <li key={index}>{example}</li>
                      ))}
                    </ul>
                  </div>
                </div>
                
                <button
                  onClick={() => handleSectionComplete(section.id)}
                  disabled={completedSections.has(section.id)}
                  className={`ml-4 px-4 py-2 rounded-lg font-medium transition-colors ${
                    completedSections.has(section.id)
                      ? 'bg-green-100 text-green-700 cursor-not-allowed'
                      : 'bg-purple-500 text-white hover:bg-purple-600'
                  }`}
                >
                  {completedSections.has(section.id) ? 'เสร็จแล้ว' : 'ทำเครื่องหมายเสร็จ'}
                </button>
              </div>
            </motion.div>
          ))}
        </div>
      </div>
    ),
    
    simulations: (
      <div className="space-y-6">
        <div className="text-center mb-8">
          <h3 className="text-2xl font-bold text-gray-900 mb-2">การจำลองแบบโต้ตอบ Supervised Learning</h3>
          <p className="text-gray-600">สำรวจอัลกอริทึม Machine Learning ผ่านการจำลองแบบโต้ตอบ</p>
        </div>
        
        <div className="grid gap-6">
          <div className="bg-white rounded-lg border border-gray-200 p-6">
            <div className="flex items-center gap-2 mb-4">
              <div className="bg-purple-100 text-purple-700 px-3 py-1 rounded-full text-sm font-medium">
                การจำลอง
              </div>
              <h4 className="text-lg font-semibold">Linear Regression แบบโต้ตอบ</h4>
            </div>
            <InteractiveSimulation 
              type="linear_regression"
              title="การฝึกสอนแบบจำลอง Linear Regression"
              description="ดูการทำงานของ Gradient Descent ในการหาเส้นตรงที่เหมาะสมที่สุด"
            />
          </div>
          
          <div className="bg-white rounded-lg border border-gray-200 p-6">
            <div className="flex items-center gap-2 mb-4">
              <div className="bg-blue-100 text-blue-700 px-3 py-1 rounded-full text-sm font-medium">
                การจำลอง
              </div>
              <h4 className="text-lg font-semibold">Logistic Regression Decision Boundary</h4>
            </div>
            <InteractiveSimulation 
              type="logistic_regression"
              title="การแบ่งคลาสด้วย Logistic Regression"
              description="เข้าใจการทำงานของ Sigmoid function และ Decision boundary"
            />
          </div>
          
          <div className="bg-white rounded-lg border border-gray-200 p-6">
            <div className="flex items-center gap-2 mb-4">
              <div className="bg-green-100 text-green-700 px-3 py-1 rounded-full text-sm font-medium">
                การจำลอง
              </div>
              <h4 className="text-lg font-semibold">Support Vector Machine Visualization</h4>
            </div>
            <InteractiveSimulation 
              type="svm"
              title="การหา Maximum Margin ด้วย SVM"
              description="ดูการทำงานของ SVM ในการหาเส้นแบ่งที่มี margin สูงสุด"
            />
          </div>
          
          <div className="bg-white rounded-lg border border-gray-200 p-6">
            <div className="flex items-center gap-2 mb-4">
              <div className="bg-orange-100 text-orange-700 px-3 py-1 rounded-full text-sm font-medium">
                การจำลอง
              </div>
              <h4 className="text-lg font-semibold">Decision Tree Building Process</h4>
            </div>
            <InteractiveSimulation 
              type="decision_tree"
              title="การสร้าง Decision Tree แบบขั้นตอน"
              description="เข้าใจกระบวนการแบ่งข้อมูลและการสร้างต้นไม้ตัดสินใจ"
            />
          </div>
        </div>
      </div>
    ),
    
    code: (
      <div className="space-y-6">
        <div className="text-center mb-8">
          <h3 className="text-2xl font-bold text-gray-900 mb-2">ตัวอย่างโค้ด Python</h3>
          <p className="text-gray-600">ลองเขียนและรันโค้ดเพื่อเรียนรู้อัลกอริทึม Supervised Learning</p>
        </div>
        
        <CodePlayground 
          title="Supervised Learning สำหรับฟิสิกส์ - บทที่ 3"
          description="ตัวอย่างโค้ดสำหรับการเรียนรู้อัลกอริทึม Machine Learning ที่สำคัญ"
          examples={codeExamples}
          defaultCode={codeExamples[0].code}
        />
      </div>
    ),
    
    quiz: (
      <div className="space-y-6">
        <div className="text-center mb-8">
          <h3 className="text-2xl font-bold text-gray-900 mb-2">แบบทดสอบบทที่ 3</h3>
          <p className="text-gray-600">ทดสอบความเข้าใจในเนื้อหาที่เรียนมา</p>
        </div>
        
        <div className="space-y-6">
          {quizQuestions.map((question, index) => (
            <motion.div
              key={question.id}
              className="bg-white rounded-lg border border-gray-200 p-6"
              initial={{ opacity: 0, y: 20 }}
              animate={{ opacity: 1, y: 0 }}
              transition={{ delay: index * 0.1 }}
            >
              <h4 className="text-lg font-semibold mb-4">
                {question.id}. {question.question}
              </h4>
              
              <div className="space-y-3">
                {question.options.map((option, optionIndex) => (
                  <label
                    key={optionIndex}
                    className={`flex items-center p-3 rounded-lg border cursor-pointer transition-colors ${
                      quizAnswers[question.id] === optionIndex
                        ? 'border-purple-500 bg-purple-50'
                        : 'border-gray-200 hover:border-gray-300'
                    } ${
                      quizSubmitted
                        ? optionIndex === question.correct
                          ? 'border-green-500 bg-green-50'
                          : quizAnswers[question.id] === optionIndex && optionIndex !== question.correct
                          ? 'border-red-500 bg-red-50'
                          : 'border-gray-200 bg-gray-50'
                        : ''
                    }`}
                  >
                    <input
                      type="radio"
                      name={`question-${question.id}`}
                      value={optionIndex}
                      checked={quizAnswers[question.id] === optionIndex}
                      onChange={() => handleQuizAnswer(question.id, optionIndex)}
                      disabled={quizSubmitted}
                      className="mr-3"
                    />
                    <span className={quizSubmitted && optionIndex === question.correct ? 'font-semibold' : ''}>
                      {option}
                    </span>
                  </label>
                ))}
              </div>
              
              {quizSubmitted && (
                <div className="mt-4 p-4 bg-blue-50 rounded-lg">
                  <p className="text-sm text-blue-800">
                    <strong>คำอธิบาย:</strong> {question.explanation}
                  </p>
                </div>
              )}
            </motion.div>
          ))}
          
          {!quizSubmitted ? (
            <button
              onClick={handleQuizSubmit}
              disabled={Object.keys(quizAnswers).length < quizQuestions.length}
              className="w-full bg-purple-500 text-white py-3 px-6 rounded-lg font-medium hover:bg-purple-600 disabled:bg-gray-300 disabled:cursor-not-allowed transition-colors"
            >
              ส่งคำตอบ
            </button>
          ) : (
            <div className="text-center p-6 bg-green-50 rounded-lg">
              <h3 className="text-xl font-bold text-green-800 mb-2">
                คะแนนของคุณ: {quizScore}/{quizQuestions.length}
              </h3>
              <p className="text-green-700">
                {quizScore === quizQuestions.length
                  ? 'ยอดเยี่ยม! คุณตอบถูกทุกข้อ'
                  : quizScore >= quizQuestions.length * 0.7
                  ? 'ดีมาก! คุณมีความเข้าใจที่ดี'
                  : 'ควรทบทวนเนื้อหาเพิ่มเติม'}
              </p>
            </div>
          )}
        </div>
      </div>
    )
  };

  return (
    <div className="min-h-screen bg-gray-50">
      {/* Chapter Header */}
      <div className="bg-gradient-to-r from-purple-600 to-pink-600 text-white">
        <div className="max-w-7xl mx-auto px-4 py-8">
          <div className="flex items-center justify-between">
            <div className="flex-1">
              <div className="flex items-center gap-3 mb-4">
                <TrendingUp className="w-8 h-8" />
                <span className="bg-white/20 px-3 py-1 rounded-full text-sm font-medium">
                  บทที่ 3 • ระดับปานกลาง
                </span>
              </div>
              <h1 className="text-3xl font-bold mb-2">
                การเรียนรู้แบบมีผู้สอน (Supervised Learning)
              </h1>
              <p className="text-purple-100 text-lg mb-4">
                Supervised Learning and Applications in Physics
              </p>
              <p className="text-white/90 max-w-3xl">
                ศึกษาอัลกอริทึมการเรียนรู้แบบมีผู้สอนที่สำคัญ รวมถึง Linear Regression, Logistic Regression, 
                SVM และ Decision Trees พร้อมการประยุกต์ใช้ในการวิเคราะห์ข้อมูลทางฟิสิกส์
              </p>
              
              <div className="flex items-center gap-6 mt-6 text-sm">
                <div className="flex items-center gap-2">
                  <Clock className="w-4 h-4" />
                  <span>ระยะเวลา: 5 ชั่วโมง</span>
                </div>
                <div className="flex items-center gap-2">
                  <BookOpen className="w-4 h-4" />
                  <span>หัวข้อ: 8 หัวข้อ</span>
                </div>
                <div className="flex items-center gap-2">
                  <CheckCircle className="w-4 h-4" />
                  <span>เสร็จแล้ว: {completedSections.size}/8</span>
                </div>
              </div>
            </div>
            
            <div className="text-right">
              <div className="text-4xl font-bold mb-2">{progressPercentage}%</div>
              <div className="text-purple-100">ความคืบหน้า</div>
              <div className="w-32 bg-white/20 rounded-full h-2 mt-2">
                <div 
                  className="bg-white rounded-full h-2 transition-all duration-500"
                  style={{ width: `${progressPercentage}%` }}
                />
              </div>
            </div>
          </div>
        </div>
      </div>

      {/* Tab Navigation */}
      <div className="bg-white border-b border-gray-200 sticky top-0 z-10">
        <div className="max-w-7xl mx-auto px-4">
          <div className="flex space-x-8">
            {[
              { id: 'content', label: 'เนื้อหา', icon: BookOpen },
              { id: 'simulations', label: 'การจำลอง', icon: Play },
              { id: 'code', label: 'โค้ดตัวอย่าง', icon: Copy },
              { id: 'quiz', label: 'แบบทดสอบ', icon: CheckCircle }
            ].map(tab => (
              <button
                key={tab.id}
                onClick={() => setActiveTab(tab.id)}
                className={`flex items-center gap-2 py-4 px-2 border-b-2 font-medium text-sm transition-colors ${
                  activeTab === tab.id
                    ? 'border-purple-500 text-purple-600'
                    : 'border-transparent text-gray-500 hover:text-gray-700 hover:border-gray-300'
                }`}
              >
                <tab.icon className="w-4 h-4" />
                {tab.label}
              </button>
            ))}
          </div>
        </div>
      </div>

      {/* Content */}
      <div className="max-w-7xl mx-auto px-4 py-8">
        {tabContent[activeTab]}
      </div>

      {/* Navigation */}
      <div className="bg-white border-t border-gray-200 py-6">
        <div className="max-w-7xl mx-auto px-4 flex items-center justify-between">
          <button className="flex items-center gap-2 px-4 py-2 text-gray-600 hover:text-gray-900 transition-colors">
            <span>← บทที่ 2</span>
          </button>
          
          <div className="flex items-center gap-4">
            <span className="text-sm text-gray-600">บทที่ 3 จาก 9</span>
            <button className="flex items-center gap-2 px-4 py-2 bg-purple-500 text-white rounded-lg hover:bg-purple-600 transition-colors">
              <Download className="w-4 h-4" />
              ดาวน์โหลด PDF
            </button>
          </div>
          
          <button className="flex items-center gap-2 px-4 py-2 text-gray-600 hover:text-gray-900 transition-colors">
            <span>บทที่ 4 →</span>
          </button>
        </div>
      </div>
    </div>
  );
};

export default Chapter3Enhanced;
