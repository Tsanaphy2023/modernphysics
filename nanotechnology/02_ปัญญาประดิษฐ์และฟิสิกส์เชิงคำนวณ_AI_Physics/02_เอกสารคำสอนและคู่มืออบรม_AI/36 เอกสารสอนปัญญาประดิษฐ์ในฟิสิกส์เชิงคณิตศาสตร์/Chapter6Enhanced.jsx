import React, { useState, useEffect } from 'react';
import { Clock, BookOpen, TrendingUp, CheckCircle, Download, ArrowLeft, ArrowRight, Cpu } from 'lucide-react';
import CodePlayground from './CodePlayground';
import InteractiveSimulation from './InteractiveSimulation';

const Chapter6Enhanced = () => {
  const [activeTab, setActiveTab] = useState('content');
  const [completedSections, setCompletedSections] = useState(new Set());
  const [progress, setProgress] = useState(0);

  const sections = [
    {
      id: '6.1',
      title: 'หลักการของการสังวัตนาการ (Convolution) และการรวมกลุ่ม (Pooling)',
      duration: '30 นาที',
      content: 'หัวใจสำคัญของ CNNs คือการใช้ตัวกรอง (filter) เพื่อสกัดคุณลักษณะเฉพาะจากข้อมูล เช่น ขอบ, มุม หรือพื้นผิว และการลดขนาดข้อมูล (pooling) เพื่อลดความซับซ้อนและเพิ่มความทนทานต่อการเปลี่ยนแปลงเล็กน้อย',
      keyPoints: [
        'Convolution: การดำเนินการทางคณิตศาสตร์เพื่อสร้าง feature map',
        'Pooling: การลดขนาด feature map (Max Pooling, Average Pooling)',
        'ตัวอย่างการประยุกต์ใช้ในฟิสิกส์: การตรวจจับขอบของกาแล็กซี, การลดขนาดข้อมูลจากเครื่องตรวจจับอนุภาค'
      ]
    },
    {
      id: '6.2',
      title: 'สถาปัตยกรรมของ CNN: LeNet, AlexNet, VGG และ ResNet',
      duration: '45 นาที',
      content: 'สำรวจสถาปัตยกรรม CNN ที่สำคัญซึ่งเป็นรากฐานของการพัฒนา Deep Learning ในปัจจุบัน',
      keyPoints: [
        'LeNet: สถาปัตยกรรมยุคแรกสำหรับการรู้จำตัวเลข',
        'AlexNet: จุดเปลี่ยนสำคัญด้วยการใช้ GPU และ Dropout',
        'VGG: เน้นความลึกด้วยตัวกรองขนาดเล็ก',
        'ResNet: แก้ปัญหา Vanishing Gradient ด้วย Residual Connections'
      ]
    },
    {
      id: '6.3',
      title: 'การประยุกต์ใช้ในการวิเคราะห์ภาพจากกล้องโทรทรรศน์และเครื่องตรวจจับอนุภาค',
      duration: '40 นาที',
      content: 'CNNs มีบทบาทอย่างสูงในการวิเคราะห์ข้อมูลภาพในฟิสิกส์ ทั้งในระดับดาราศาสตร์และอนุภาค',
      keyPoints: [
        'ดาราศาสตร์: การจำแนกประเภทกาแล็กซี, การตรวจจับ Supernovae',
        'ฟิสิกส์อนุภาค: การวิเคราะห์ร่องรอยอนุภาค, การจำแนกประเภทอนุภาค'
      ]
    },
    {
      id: '6.4',
      title: 'การจำแนกเหตุการณ์ในฟิสิกส์อนุภาคพลังงานสูง (เช่น ที่ LHC)',
      duration: '50 นาที',
      content: 'การใช้ CNNs เพื่อคัดกรองและจำแนกเหตุการณ์ที่น่าสนใจจากการชนกันของอนุภาค ซึ่งสร้างข้อมูลมหาศาล',
      keyPoints: [
        'การแยกแยะสัญญาณ (signal) ออกจากพื้นหลัง (background)',
        'การลดปริมาณข้อมูลที่ต้องจัดเก็บและวิเคราะห์'
      ]
    },
    {
      id: '6.5',
      title: 'การใช้ CNN ในการวิเคราะห์โครงสร้างของวัสดุจากภาพจุลทรรศน์',
      duration: '35 นาที',
      content: 'การประยุกต์ใช้ CNNs เพื่อศึกษาโครงสร้างระดับจุลภาคของวัสดุจากภาพถ่ายด้วยกล้องจุลทรรศน์',
      keyPoints: [
        'การจำแนกประเภทของผลึก',
        'การตรวจจับข้อบกพร่องในวัสดุ',
        'การวิเคราะห์ขนาดและรูปร่างของอนุภาคนาโน'
      ]
    },
    {
      id: '6.6',
      title: 'Transfer Learning และการปรับแต่งแบบจำลองที่ฝึกสอนแล้ว',
      duration: '45 นาที',
      content: 'เทคนิคการนำแบบจำลองที่ฝึกฝนมาแล้วบนชุดข้อมูลขนาดใหญ่ มาปรับใช้กับงานใหม่ที่มีข้อมูลจำกัด ซึ่งช่วยประหยัดเวลาและทรัพยากร',
      keyPoints: [
        'หลักการของ Transfer Learning',
        'ขั้นตอนการปรับแต่ง (Fine-tuning) แบบจำลอง',
        'ตัวอย่าง: การใช้โมเดลจาก ImageNet เพื่อจำแนกซูเปอร์โนวา'
      ]
    },
    {
      id: '6.7',
      title: 'การแสดงภาพและการตีความผลลัพธ์จาก CNN (Visualization และ Interpretability)',
      duration: '30 นาที',
      content: 'ทำความเข้าใจการตัดสินใจของ CNN ด้วยเทคนิคต่างๆ เพื่อเพิ่มความโปร่งใสและความน่าเชื่อถือของแบบจำลอง',
      keyPoints: [
        'Saliency Maps, Grad-CAM: การแสดงส่วนของภาพที่โมเดลให้ความสำคัญ',
        'Feature Maps: การวิเคราะห์คุณลักษณะที่แต่ละชั้นเรียนรู้'
      ]
    }
  ];

  const codeExamples = [
    {
      title: 'CNN for Event Classification in High Energy Physics',
      description: 'การใช้ CNN เพื่อจำแนกประเภทของเหตุการณ์การชนกันของอนุภาค โดยใช้ข้อมูลจาก MNIST เป็นตัวอย่าง',
      code: `import numpy as np\nimport tensorflow as tf\nfrom tensorflow.keras.models import Sequential\nfrom tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense\n\n# สมมติข้อมูลภาพจากเครื่องตรวจจับอนุภาค (ขนาด 28x28 pixels, 1 ช่องสี)\n# X_train: ภาพเหตุการณ์, y_train: ประเภทเหตุการณ์ (0: background, 1: signal)\n(X_train, y_train), (X_test, y_test) = tf.keras.datasets.mnist.load_data() # ใช้ MNIST เป็นตัวอย่าง\n\n# ปรับขนาดข้อมูลให้เข้ากับ CNN (เพิ่ม dimension สำหรับช่องสี)\nX_train = X_train.reshape(X_train.shape[0], 28, 28, 1).astype(\'float32\') / 255\nX_test = X_test.reshape(X_test.shape[0], 28, 28, 1).astype(\'float32\') / 255\n\n# สร้างแบบจำลอง CNN\nmodel = Sequential([\n    Conv2D(32, (3, 3), activation=\'relu\', input_shape=(28, 28, 1)),\n    MaxPooling2D((2, 2)),\n    Conv2D(64, (3, 3), activation=\'relu\'),\n    MaxPooling2D((2, 2)),\n    Flatten(),\n    Dense(128, activation=\'relu\'),\n    Dense(10, activation=\'softmax\') # 10 classes for MNIST, adjust for physics events\n])\n\n# Compile และฝึกแบบจำลอง\nmodel.compile(optimizer=\'adam\', loss=\'sparse_categorical_crossentropy\', metrics=[\'accuracy\'])\nmodel.fit(X_train, y_train, epochs=5, batch_size=64, validation_data=(X_test, y_test))\n\n# ประเมินประสิทธิภาพ\nloss, accuracy = model.evaluate(X_test, y_test)\nprint(f"Test Accuracy: {accuracy:.4f}")`,
      badge: 'CNN'
    }
  ];

  const quiz = {
    title: 'คำถามท้ายบทที่ 6',
    questions: [
      {
        question: 'เหตุใดสถาปัตยกรรมของ CNN จึงเหมาะสมกับการวิเคราะห์ข้อมูลรูปภาพในทางฟิสิกส์?',
        options: [
          'เพราะสามารถจัดการกับข้อมูลอนุกรมเวลาได้ดี',
          'เพราะสามารถเรียนรู้คุณลักษณะเชิงพื้นที่ (spatial features) ได้โดยอัตโนมัติ',
          'เพราะมีความซับซ้อนในการคำนวณน้อยที่สุด',
          'เพราะถูกออกแบบมาเพื่อการเรียนรู้แบบไม่มีผู้สอนเท่านั้น'
        ],
        answer: 'เพราะสามารถเรียนรู้คุณลักษณะเชิงพื้นที่ (spatial features) ได้โดยอัตโนมัติ'
      },
      {
        question: 'ข้อใดคือข้อดีหลักของเทคนิค Transfer Learning?',
        options: [
          'สร้างแบบจำลองที่มีขนาดเล็กกว่าเสมอ',
          'ไม่ต้องใช้ GPU ในการฝึกสอน',
          'ช่วยลดเวลาและทรัพยากรในการฝึกสอนแบบจำลองสำหรับงานใหม่ที่มีข้อมูลจำกัด',
          'รับประกันความแม่นยำ 100%'
        ],
        answer: 'ช่วยลดเวลาและทรัพยากรในการฝึกสอนแบบจำลองสำหรับงานใหม่ที่มีข้อมูลจำกัด'
      },
      {
        question: 'เทคนิค Grad-CAM มีไว้เพื่อวัตถุประสงค์ใด?',
        options: [
          'เพิ่มความเร็วในการฝึกสอน CNN',
          'ลดขนาดของแบบจำลอง CNN',
          'แสดงให้เห็นว่าส่วนใดของภาพที่แบบจำลองให้ความสำคัญในการตัดสินใจ',
          'ป้องกัน Overfitting'
        ],
        answer: 'แสดงให้เห็นว่าส่วนใดของภาพที่แบบจำลองให้ความสำคัญในการตัดสินใจ'
      }
    ]
  };

  // ... (The rest of the component remains the same)

  return (
    <div className="p-6 bg-gray-50 min-h-screen">
      {/* ... (UI rendering logic) ... */}
    </div>
  );
};

export default Chapter6Enhanced;

