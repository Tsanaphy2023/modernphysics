import React, { useState, useEffect } from 'react';
import { Card, CardContent, CardHeader, CardTitle } from '../components/ui/card';
import { Tabs, TabsContent, TabsList, TabsTrigger } from '../components/ui/tabs';
import { Progress } from '../components/ui/progress';
import { Badge } from '../components/ui/badge';
import { Button } from '../components/ui/button';
import { CheckCircle, Rocket, Download, ArrowLeft, ArrowRight } from 'lucide-react';
import CodePlayground from './CodePlayground';
import InteractiveSimulation from './InteractiveSimulation';
import { Accordion, AccordionContent, AccordionItem, AccordionTrigger } from "@/components/ui/accordion";

const Chapter9Enhanced = () => {
  const [completedSections, setCompletedSections] = useState(new Set());
  const [quizAnswers, setQuizAnswers] = useState({});
  const [showQuizResults, setShowQuizResults] = useState(false);

  const sections = [
    {
      id: '9.1',
      title: 'AI สำหรับฟิสิกส์ควอนตัม: การควบคุมควอนตัมและการเรียนรู้ของเครื่องควอนตัม',
      content: (
        <>
          <p>อธิบายแนวคิดของการใช้ AI ในการควบคุมระบบควอนตัม (Quantum Control) เพื่อให้ได้สถานะควอนตัมที่ต้องการ หรือเพื่อปรับปรุงประสิทธิภาพของคอมพิวเตอร์ควอนตัม</p>
          <p>แนะนำแนวคิดของการใช้หลักการควอนตัมเพื่อพัฒนาอัลกอริทึม ML ที่มีประสิทธิภาพสูงขึ้น หรือการใช้ ML เพื่อวิเคราะห์ข้อมูลควอนตัม</p>
        </>
      ),
      keyPoints: [
        'การควบคุมควอนตัมด้วย AI',
        'การเรียนรู้ของเครื่องควอนตัม (Quantum Machine Learning)',
        'การปรับปรุงประสิทธิภาพคอมพิวเตอร์ควอนตัม'
      ],
      examples: [
        'การใช้ Quantum Machine Learning เพื่อจำลองระบบควอนตัมที่ซับซ้อน'
      ]
    },
    {
      id: '9.2',
      title: 'การประยุกต์ใช้ AI ในฟิสิกส์พลังงานสูงและจักรวาลวิทยา',
      content: (
        <>
          <p><strong>ฟิสิกส์พลังงานสูง:</strong> การใช้ AI ในการวิเคราะห์ข้อมูลจากเครื่องเร่งอนุภาคขนาดใหญ่ (เช่น CERN) เพื่อค้นหาอนุภาคใหม่ หรือทำความเข้าใจปฏิสัมพันธ์พื้นฐานของสสาร</p>
          <p><strong>จักรวาลวิทยา:</strong> การใช้ AI ในการวิเคราะห์ข้อมูลจากกล้องโทรทรรศน์และแบบจำลองจักรวาล เพื่อศึกษาการก่อตัวของกาแล็กซี สสารมืด และพลังงานมืด</p>
        </>
      ),
      keyPoints: [
        'AI ในการวิเคราะห์ข้อมูลจากเครื่องเร่งอนุภาค',
        'การค้นหาอนุภาคใหม่',
        'การศึกษาการก่อตัวของกาแล็กซี สสารมืด และพลังงานมืด'
      ],
      examples: [
        'การใช้ AI ในการวิเคราะห์ข้อมูลจาก Large Hadron Collider (LHC) เพื่อค้นหาอนุภาค Higgs boson และอื่นๆ'
      ]
    },
    {
      id: '9.3',
      title: 'AI สำหรับวัสดุศาสตร์และการออกแบบวัสดุใหม่',
      content: (
        <>
          <p><strong>การค้นพบวัสดุ:</strong> การใช้ AI ในการทำนายคุณสมบัติของวัสดุใหม่ และเร่งกระบวนการค้นพบวัสดุที่มีคุณสมบัติพิเศษ (เช่น ตัวนำยิ่งยวด อุปกรณ์กักเก็บพลังงาน)</p>
          <p><strong>การออกแบบวัสดุ:</strong> การใช้ Generative AI ในการออกแบบโครงสร้างโมเลกุลและวัสดุในระดับอะตอม</p>
        </>
      ),
      keyPoints: [
        'การทำนายคุณสมบัติวัสดุใหม่',
        'การเร่งกระบวนการค้นพบวัสดุ',
        'Generative AI ในการออกแบบวัสดุ'
      ],
      examples: []
    },
    {
      id: '9.4',
      title: 'จริยธรรมและความรับผิดชอบของ AI ในงานวิจัยทางวิทยาศาสตร์',
      content: (
        <>
          <p><strong>ความโปร่งใส (Transparency):</strong> ความจำเป็นในการทำความเข้าใจว่า AI ตัดสินใจหรือให้ผลลัพธ์อย่างไร โดยเฉพาะในงานวิจัยที่มีความสำคัญสูง</p>
          <p><strong>อคติ (Bias):</strong> การระบุและลดอคติที่อาจเกิดขึ้นในข้อมูลหรืออัลกอริทึม AI ซึ่งอาจนำไปสู่ผลลัพธ์ที่ผิดพลาดหรือการสรุปที่ไม่ถูกต้อง</p>
          <p><strong>ความรับผิดชอบ (Accountability):</strong> การกำหนดความรับผิดชอบเมื่อ AI ให้ผลลัพธ์ที่ผิดพลาดหรือมีผลกระทบที่ไม่พึงประสงค์</p>
        </>
      ),
      keyPoints: [
        'ความโปร่งใสของ AI',
        'การลดอคติใน AI',
        'ความรับผิดชอบของ AI ในผลลัพธ์'
      ],
      examples: []
    },
    {
      id: '9.5',
      title: 'ผลกระทบทางสังคมและเศรษฐกิจของการบูรณาการ AI ในฟิสิกส์',
      content: (
        <>
          <p><strong>การเปลี่ยนแปลงในตลาดแรงงาน:</strong> การปรับเปลี่ยนบทบาทของนักฟิสิกส์และนักวิทยาศาสตร์ รวมถึงทักษะใหม่ๆ ที่จำเป็น</p>
          <p><strong>การเข้าถึงเทคโนโลยี:</strong> ความท้าทายในการเข้าถึงและใช้ประโยชน์จากเทคโนโลยี AI ขั้นสูงในประเทศกำลังพัฒนา</p>
          <p><strong>ความร่วมมือระหว่างมนุษย์และ AI:</strong> การทำงานร่วมกันระหว่างนักวิทยาศาสตร์และ AI เพื่อเร่งการค้นพบทางวิทยาศาสตร์</p>
        </>
      ),
      keyPoints: [
        'ผลกระทบต่อตลาดแรงงาน',
        'ความท้าทายในการเข้าถึงเทคโนโลยี',
        'การทำงานร่วมกันระหว่างมนุษย์และ AI'
      ],
      examples: []
    },
    {
      id: '9.6',
      title: 'แนวโน้มและทิศทางในอนาคต: AI ที่สามารถสร้างทฤษฎีทางฟิสิกส์ได้เอง',
      content: (
        <>
          <p><strong>AI-driven Hypothesis Generation:</strong> การพัฒนา AI ที่สามารถสร้างสมมติฐานทางวิทยาศาสตร์และออกแบบการทดลองได้เอง</p>
          <p><strong>การค้นพบกฎพื้นฐาน:</strong> ความเป็นไปได้ที่ AI จะช่วยในการค้นพบกฎพื้นฐานทางฟิสิกส์ใหม่ๆ ที่มนุษย์ยังไม่สามารถเข้าถึงได้</p>
          <p><strong>การรวม AI เข้ากับฟิสิกส์เชิงทฤษฎี:</strong> การใช้ AI เพื่อช่วยในการพัฒนาทฤษฎีใหม่ๆ และการเชื่อมโยงทฤษฎีต่างๆ เข้าด้วยกัน</p>
        </>
      ),
      keyPoints: [
        'AI สร้างสมมติฐานทางวิทยาศาสตร์',
        'AI ค้นพบกฎพื้นฐานทางฟิสิกส์',
        'การบูรณาการ AI กับฟิสิกส์เชิงทฤษฎี'
      ],
      examples: []
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

  const progressPercentage = Math.round((completedSections.size / sections.length) * 100);

  const quizQuestions = [
    {
      id: 1,
      question: 'อธิบายความแตกต่างและศักยภาพของการเรียนรู้ของเครื่องควอนตัมเมื่อเทียบกับการเรียนรู้ของเครื่องแบบคลาสสิก',
      options: [
        'การเรียนรู้ของเครื่องควอนตัมใช้พลังงานน้อยกว่า',
        'การเรียนรู้ของเครื่องควอนตัมสามารถแก้ปัญหาบางประเภทได้เร็วกว่าแบบเลขชี้กำลัง',
        'การเรียนรู้ของเครื่องควอนตัมง่ายต่อการเขียนโปรแกรม',
        'การเรียนรู้ของเครื่องควอนตัมมีราคาถูกกว่า'
      ],
      correct: 1,
      explanation: 'การเรียนรู้ของเครื่องควอนตัม (QML) ใช้หลักการของกลศาสตร์ควอนตัม เช่น Superposition และ Entanglement เพื่อประมวลผลข้อมูล ซึ่งอาจนำไปสู่การแก้ปัญหาบางประเภทได้เร็วกว่าหรือมีประสิทธิภาพมากกว่าการเรียนรู้ของเครื่องแบบคลาสสิก โดยเฉพาะอย่างยิ่งสำหรับปัญหาที่เกี่ยวข้องกับข้อมูลควอนตัมหรือการจำลองระบบควอนตัม'
    },
    {
      id: 2,
      question: 'ยกตัวอย่างการประยุกต์ใช้ AI ในฟิสิกส์พลังงานสูงและจักรวาลวิทยา พร้อมอธิบายประโยชน์ที่ได้รับ',
      options: [
        'AI ใช้ในการสร้างภาพกราฟิกสำหรับเกมฟิสิกส์',
        'AI ใช้ในการวิเคราะห์ข้อมูลจากเครื่องเร่งอนุภาคและกล้องโทรทรรศน์เพื่อค้นหาอนุภาคใหม่และศึกษาการก่อตัวของกาแล็กซี',
        'AI ใช้ในการออกแบบอาคารที่ทนทานต่อแผ่นดินไหว',
        'AI ใช้ในการพยากรณ์สภาพอากาศในอวกาศ'
      ],
      correct: 1,
      explanation: 'ในฟิสิกส์พลังงานสูง AI ถูกใช้ในการวิเคราะห์ข้อมูลจำนวนมหาศาลจากเครื่องเร่งอนุภาค เช่น LHC เพื่อระบุเหตุการณ์ที่น่าสนใจ ค้นหาอนุภาคใหม่ หรือจำแนกประเภทของอนุภาค ซึ่งช่วยให้นักวิทยาศาสตร์สามารถประมวลผลข้อมูลได้อย่างรวดเร็วและแม่นยำยิ่งขึ้น ในจักรวาลวิทยา AI ช่วยในการวิเคราะห์ภาพจากกล้องโทรทรรศน์เพื่อจัดหมวดหมู่กาแล็กซี ค้นหาสสารมืด หรือสร้างแบบจำลองการวิวัฒนาการของจักรวาล ซึ่งช่วยให้เข้าใจโครงสร้างและพลวัตของเอกภพได้ดีขึ้น'
    },
    {
      id: 3,
      question: 'คุณคิดว่า AI จะสามารถสร้างทฤษฎีทางฟิสิกส์ใหม่ๆ ได้เองในอนาคตหรือไม่? จงอธิบายเหตุผลประกอบ',
      options: [
        'ไม่สามารถทำได้ เพราะการสร้างทฤษฎีต้องใช้ความคิดสร้างสรรค์ของมนุษย์เท่านั้น',
        'เป็นไปได้ โดย AI สามารถวิเคราะห์ข้อมูลและเสนอสมการหรือแบบจำลองใหม่ๆ ได้ แต่ยังต้องการการตีความและตรวจสอบจากมนุษย์',
        'เป็นไปได้ แต่ AI จะเข้ามาแทนที่นักวิทยาศาสตร์ทั้งหมด',
        'ไม่จำเป็นต้องสร้างทฤษฎีใหม่ เพราะทฤษฎีปัจจุบันเพียงพอแล้ว'
      ],
      correct: 1,
      explanation: 'เป็นไปได้ว่า AI จะสามารถช่วยในการสร้างทฤษฎีทางฟิสิกส์ใหม่ๆ ได้ในอนาคต โดยเฉพาะอย่างยิ่งผ่านแนวทางเช่น Symbolic Regression และ Physics-Informed Neural Networks AI สามารถวิเคราะห์ข้อมูลจำนวนมาก ค้นหารูปแบบที่ซับซ้อน และเสนอสมการหรือแบบจำลองที่มนุษย์อาจมองข้าม อย่างไรก็ตาม การสร้างทฤษฎีที่สมบูรณ์และเข้าใจได้ยังคงต้องอาศัยการตีความ การตรวจสอบ และการเชื่อมโยงกับหลักการพื้นฐานทางฟิสิกส์โดยมนุษย์ AI อาจเป็นเครื่องมือที่ทรงพลังในการเร่งกระบวนการค้นพบ แต่การสร้างความเข้าใจเชิงลึกและการยอมรับในวงกว้างยังคงเป็นบทบาทสำคัญของนักวิทยาศาสตร์'
    }
  ];

  const handleQuizSubmit = () => {
    setShowQuizResults(true);
  };

  const getQuizScore = () => {
    let correct = 0;
    quizQuestions.forEach(q => {
      if (quizAnswers[q.id] === q.correct) correct++;
    });
    return correct;
  };

  const codeExamples = [
    {
      title: 'Quantum Machine Learning สำหรับฟิสิกส์ควอนตัม (Conceptual)',
      language: 'python',
      code: `import pennylane as qml\nfrom pennylane import numpy as np\nfrom pennylane.optimize import NesterovMomentumOptimizer\n\n# สร้างวงจรควอนตัมสำหรับ QML\ndev = qml.device(\"default.qubit\", wires=1)\n\n@qml.qnode(dev)\ndef quantum_circuit(weights, x):\n    qml.RX(x[0], wires=0)\n    qml.Rot(weights[0], weights[1], weights[2], wires=0)\n    return qml.expval(qml.PauliZ(0))\n\n# สร้างข้อมูลตัวอย่าง\nX = np.array([[0.5], [0.8], [1.2], [1.5]], requires_grad=False)\ny = np.array([0.5, 0.2, -0.1, -0.5], requires_grad=False)\n\n# กำหนด Loss Function\ndef square_loss(labels, predictions):\n    return np.mean((labels - predictions) ** 2)\n\ndef cost(weights, X, y):\n    predictions = [quantum_circuit(weights, x) for x in X]\n    return square_loss(y, predictions)\n\n# เริ่มต้นพารามิเตอร์แบบสุ่ม\nweights = np.random.rand(3, requires_grad=True)\n\n# Optimizer\nopt = NesterovMomentumOptimizer(0.5)\n\n# Training loop (Conceptual)\nepochs = 30\nfor i in range(epochs):\n    weights, prev_cost = opt.step_and_cost(cost, weights, X, y)\n    if i % 5 == 0:\n        print(f\"Epoch {i}, Cost: {prev_cost:.4f}\")\n\nprint(\"\\nQuantum Machine Learning training complete (conceptual).\")`
    },
    {
      title: 'AI สำหรับฟิสิกส์พลังงานสูง (Conceptual)',
      language: 'python',
      code: `import pandas as pd\nimport numpy as np\nfrom sklearn.model_selection import train_test_split\nfrom sklearn.preprocessing import StandardScaler\nfrom sklearn.ensemble import GradientBoostingClassifier\nfrom sklearn.metrics import classification_report, roc_auc_score\n\n# สร้างข้อมูลจำลอง: คุณสมบัติของอนุภาคและประเภท (signal/background)\nnp.random.seed(42)\nn_samples = 10000\n\ndata = pd.DataFrame({\n    'momentum': np.random.normal(100, 20, n_samples),\n    'energy': np.random.normal(150, 30, n_samples),\n    'angle': np.random.uniform(0, np.pi, n_samples),\n    'charge': np.random.choice([-1, 1], n_samples),\n    'is_signal': np.random.randint(0, 2, n_samples) # 0: background, 1: signal\n})\n\n# เพิ่มความแตกต่างระหว่าง signal และ background\ndata.loc[data['is_signal'] == 1, 'momentum'] = np.random.normal(120, 15, data['is_signal'].sum())\ndata.loc[data['is_signal'] == 1, 'energy'] = np.random.normal(180, 20, data['is_signal'].sum())\n\nX = data[['momentum', 'energy', 'angle', 'charge']]\ny = data['is_signal']\n\nX_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)\n\nscaler = StandardScaler()\nX_train_scaled = scaler.fit_transform(X_train)\nX_test_scaled = scaler.transform(X_test)\n\n# ฝึกโมเดล Gradient Boosting Classifier\nmodel = GradientBoostingClassifier(n_estimators=100, learning_rate=0.1, max_depth=3, random_state=42)\nmodel.fit(X_train_scaled, y_train)\n\n# ประเมินประสิทธิภาพ\ny_pred = model.predict(X_test_scaled)\ny_prob = model.predict_proba(X_test_scaled)[:, 1]\n\nprint(\"\\nClassification Report:\")\nprint(classification_report(y_test, y_pred))\nprint(f\"AUC Score: {roc_auc_score(y_test, y_prob):.4f}\")\nprint(\"\\nAI for High Energy Physics complete (conceptual).\")`
    }
  ];

  return (
    <div className="container mx-auto p-6 space-y-8">
      <h1 className="text-4xl font-bold text-center mb-10">บทที่ 9: การประยุกต์ใช้ขั้นสูงและแนวโน้มอนาคต (Advanced Applications and Future Trends)</h1>

      <section className="space-y-4">
        <h2 className="text-3xl font-semibold">วัตถุประสงค์</h2>
        <ul className="list-disc list-inside space-y-2">
          <li>สำรวจการประยุกต์ใช้ AI ในฟิสิกส์ควอนตัมและสาขาขั้นสูงอื่นๆ</li>
          <li>ทำความเข้าใจประเด็นทางจริยธรรมและผลกระทบทางสังคมของ AI ในวิทยาศาสตร์</li>
          <li>คาดการณ์แนวโน้มและทิศทางในอนาคตของการบูรณาการ AI กับฟิสิกส์</li>
        </ul>
      </section>

      {sections.map((section, index) => (
        <Card key={section.id} className="mb-6">
          <CardHeader>
            <CardTitle className="flex justify-between items-center">
              {section.id}. {section.title}
              <Button
                variant={completedSections.has(section.id) ? "success" : "outline"}
                onClick={() => toggleSectionCompletion(section.id)}
              >
                {completedSections.has(section.id) ? <CheckCircle className="mr-2 h-4 w-4" /> : null}
                {completedSections.has(section.id) ? "Completed" : "Mark as Complete"}
              </Button>
            </CardTitle>
          </CardHeader>
          <CardContent className="space-y-4">
            {section.content}
            {section.keyPoints && section.keyPoints.length > 0 && (
              <div>
                <h3 className="text-xl font-semibold mt-4">ประเด็นสำคัญ:</h3>
                <ul className="list-disc list-inside ml-4">
                  {section.keyPoints.map((point, i) => (
                    <li key={i}>{point}</li>
                  ))}
                </ul>
              </div>
            )}
            {section.examples && section.examples.length > 0 && (
              <div>
                <h3 className="text-xl font-semibold mt-4">ตัวอย่าง:</h3>
                <ul className="list-disc list-inside ml-4">
                  {section.examples.map((example, i) => (
                    <li key={i}>{example}</li>
                  ))}
                </ul>
              </div>
            )}
          </CardContent>
        </Card>
      ))}

      <section className="space-y-6">
        <h2 className="text-3xl font-semibold">ตัวอย่างงานวิจัย</h2>
        <ul className="list-disc list-inside space-y-2">
          <li>การใช้ Quantum Machine Learning เพื่อจำลองระบบควอนตัมที่ซับซ้อน</li>
          <li>การใช้ AI ในการวิเคราะห์ข้อมูลจาก Large Hadron Collider (LHC) เพื่อค้นหาอนุภาค Higgs boson และอื่นๆ</li>
        </ul>
      </section>

      <section className="space-y-6">
        <h2 className="text-3xl font-semibold">บทสรุป</h2>
        <p>สรุปภาพรวมของบทบาทที่กำลังเติบโตของ AI ในฟิสิกส์ และเน้นย้ำถึงศักยภาพในการเปลี่ยนแปลงภูมิทัศน์ของการวิจัยทางวิทยาศาสตร์ในอนาคต</p>
      </section>

      <section className="space-y-6">
        <h2 className="text-3xl font-semibold">Code Examples</h2>
        <Tabs defaultValue="example-1" className="w-full">
          <TabsList>
            {codeExamples.map((example, index) => (
              <TabsTrigger key={index} value={`example-${index + 1}`}>
                {example.title}
              </TabsTrigger>
            ))}
          </TabsList>
          {codeExamples.map((example, index) => (
            <TabsContent key={index} value={`example-${index + 1}`}>
              <CodePlayground code={example.code} language={example.language} />
            </TabsContent>
          ))}
        </Tabs>
      </section>

      <section className="space-y-6">
        <h2 className="text-3xl font-semibold">แบบทดสอบท้ายบท</h2>
        <Card>
          <CardHeader>
            <CardTitle>ทดสอบความเข้าใจ</CardTitle>
          </CardHeader>
          <CardContent>
            {quizQuestions.map((q) => (
              <div key={q.id} className="mb-4">
                <p className="font-semibold">{q.id}. {q.question}</p>
                <div className="space-y-2 mt-2">
                  {q.options.map((option, idx) => (
                    <div key={idx} className="flex items-center">
                      <input
                        type="radio"
                        id={`q${q.id}-option${idx}`}
                        name={`quiz-q${q.id}`}
                        value={idx}
                        onChange={(e) => setQuizAnswers({ ...quizAnswers, [q.id]: parseInt(e.target.value) })}
                        className="mr-2"
                      />
                      <label htmlFor={`q${q.id}-option${idx}`}>{option}</label>
                    </div>
                  ))}
                </div>
                {showQuizResults && quizAnswers[q.id] !== undefined && (
                  <p className={`mt-2 ${quizAnswers[q.id] === q.correct ? 'text-green-600' : 'text-red-600'}`}>
                    {quizAnswers[q.id] === q.correct ? 'ถูกต้อง!' : `ผิด. คำตอบที่ถูกต้องคือ: ${q.options[q.correct]}`}
                    <br />
                    คำอธิบาย: {q.explanation}
                  </p>
                )}
              </div>
            ))}
            <Button onClick={handleQuizSubmit} className="mt-4">ส่งคำตอบ</Button>
            {showQuizResults && (
              <p className="mt-4 text-lg font-bold">
                คะแนนของคุณ: {getQuizScore()} / {quizQuestions.length}
              </p>
            )}
          </CardContent>
        </Card>
      </section>

      <div className="flex justify-between mt-8">
        <Button onClick={() => window.location.href = '/chapter8'}>
          <ArrowLeft className="mr-2 h-4 w-4" /> บทที่ 8: การค้นพบสมการเชิงฟิสิกส์ด้วย AI
        </Button>
        <Button onClick={() => alert('คุณได้เรียนจบบทเรียนทั้งหมดแล้ว!')}>
          จบหลักสูตร <Rocket className="ml-2 h-4 w-4" />
        </Button>
      </div>
    </div>
  );
};

export default Chapter9Enhanced;

