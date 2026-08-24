import React from 'react';
import { useParams, Link } from 'react-router-dom';
import { motion } from 'framer-motion';
import { 
  BookOpen, 
  Brain, 
  Cpu, 
  Eye, 
  MessageSquare, 
  Bot, 
  Microscope, 
  Shield,
  ChevronRight,
  Sparkles,
  Zap,
  Leaf,
  Code,
  Play,
  Download
} from 'lucide-react';

// Import images
import chapter1Image from '../assets/chapter1_image.png';
import chapter2Image from '../assets/chapter2_image.png';
import chapter3Image from '../assets/chapter3_image.png';
import chapter4Image from '../assets/chapter4_image.png';
import chapter5Image from '../assets/chapter5_image.png';
import chapter6Image from '../assets/chapter6_image.png';
import chapter7Image from '../assets/chapter7_image.png';
import chapter8Image from '../assets/chapter8_image.png';

const chapters = [
  {
    id: 1,
    title: "บทนำปัญญาประดิษฐ์",
    subtitle: "Introduction to AI",
    description: "ทำความรู้จักกับโลกของปัญญาประดิษฐ์ ประวัติ และการประยุกต์ใช้ในชีวิตประจำวัน",
    icon: Brain,
    image: chapter1Image,
    color: "from-purple-500 to-pink-500"
  },
  {
    id: 2,
    title: "พื้นฐานการเรียนรู้ของเครื่อง",
    subtitle: "Machine Learning Fundamentals",
    description: "เรียนรู้หลักการพื้นฐานของ Machine Learning และอัลกอริทึมสำคัญ",
    icon: Cpu,
    image: chapter2Image,
    color: "from-blue-500 to-cyan-500"
  },
  {
    id: 3,
    title: "การเรียนรู้เชิงลึกและโครงข่ายประสาทเทียม",
    subtitle: "Deep Learning & Neural Networks",
    description: "ศึกษาโครงข่ายประสาทเทียมและการเรียนรู้เชิงลึกอย่างละเอียด",
    icon: Brain,
    image: chapter3Image,
    color: "from-indigo-500 to-purple-500"
  },
  {
    id: 4,
    title: "คอมพิวเตอร์วิทัศน์",
    subtitle: "Computer Vision",
    description: "การประมวลผลภาพและการมองเห็นของคอมพิวเตอร์ในการเกษตร",
    icon: Eye,
    image: chapter4Image,
    color: "from-green-500 to-teal-500"
  },
  {
    id: 5,
    title: "การประมวลผลภาษาธรรมชาติ",
    subtitle: "Natural Language Processing",
    description: "การทำความเข้าใจและประมวลผลภาษามนุษย์ด้วยคอมพิวเตอร์",
    icon: MessageSquare,
    image: chapter5Image,
    color: "from-orange-500 to-red-500"
  },
  {
    id: 6,
    title: "หุ่นยนต์และระบบอัตโนมัติในการเกษตร",
    subtitle: "Robotics & Automation",
    description: "การใช้หุ่นยนต์และระบบอัตโนมัติในการเกษตรสมัยใหม่",
    icon: Bot,
    image: chapter6Image,
    color: "from-cyan-500 to-blue-500"
  },
  {
    id: 7,
    title: "Project 3: วิเคราะห์คุณภาพดินด้วย AI",
    subtitle: "Soil Quality Analysis with AI",
    description: "โครงการปฏิบัติการวิเคราะห์คุณภาพดินด้วยเทคโนโลยี AI",
    icon: Microscope,
    image: chapter7Image,
    color: "from-amber-500 to-orange-500"
  },
  {
    id: 8,
    title: "จริยธรรมและอนาคตของ AI",
    subtitle: "Ethics & Future of AI",
    description: "การพิจารณาด้านจริยธรรมและแนวโน้มอนาคตของปัญญาประดิษฐ์",
    icon: Shield,
    image: chapter8Image,
    color: "from-rose-500 to-pink-500"
  }
];

const EnhancedChapterDetail = () => {
  const { id } = useParams();
  const chapter = chapters.find(ch => ch.id === parseInt(id));
  
  if (!chapter) {
    return (
      <div className="pt-16 min-h-screen bg-gradient-to-br from-gray-50 to-white flex items-center justify-center">
        <div className="text-center">
          <h1 className="text-2xl font-bold text-gray-900 mb-4">ไม่พบบทเรียนที่ต้องการ</h1>
          <Link to="/chapters" className="text-purple-600 hover:text-purple-700">
            กลับไปหน้าบทเรียน
          </Link>
        </div>
      </div>
    );
  }

  // Enhanced content based on detailed chapters
  const getEnhancedContent = (chapterId) => {
    const enhancedContent = {
      1: {
        sections: [
          "ประวัติศาสตร์ปัญญาประดิษฐ์: จากแนวคิดสู่ความเป็นจริง",
          "ประเภทของ AI: Narrow AI, General AI, Super AI",
          "การประยุกต์ใช้ AI ในชีวิตประจำวัน",
          "AI ในการเกษตร: Smart Farming, Precision Agriculture",
          "อนาคตของ AI และผลกระทบต่อสังคม",
          "การเตรียมตัวสำหรับยุค AI"
        ],
        interactiveFeatures: [
          "🕒 AI Timeline แบบโต้ตอบ - สำรวจประวัติศาสตร์ AI",
          "📊 กราฟแสดงผลกระทบของ AI ในอุตสาหกรรมต่างๆ",
          "🔍 การสาธิต Pattern Recognition แบบเรียลไทม์",
          "🌾 กรณีศึกษา AI ในการเกษตรไทย",
          "🎮 เกมจำลองการตัดสินใจของ AI"
        ],
        codeExamples: [
          "การสร้าง Simple AI Agent ด้วย Python",
          "การใช้ Machine Learning Library พื้นฐาน",
          "การประมวลผลข้อมูลเกษตรด้วย Pandas",
          "การสร้างกราฟแสดงแนวโน้มด้วย Matplotlib"
        ],
        pages: "15+"
      },
      2: {
        sections: [
          "ประเภทของ Machine Learning: Supervised, Unsupervised, Reinforcement",
          "อัลกอริทึมสำคัญ: Linear Regression, Decision Tree, K-Means, SVM",
          "การประเมินประสิทธิภาพโมเดล: Accuracy, Precision, Recall, F1-Score",
          "การประยุกต์ใช้ในการเกษตร: ทำนายผลผลิต, ตรวจจับโรคพืช",
          "เครื่องมือและไลบรารี่สำหรับ ML: Scikit-learn, Pandas, NumPy",
          "การเตรียมข้อมูลและ Feature Engineering"
        ],
        interactiveFeatures: [
          "📈 การสาธิต Linear Regression แบบโต้ตอบ",
          "🌳 การทำงานของ Decision Tree Visualizer",
          "🎯 K-Means Clustering Demo ด้วยข้อมูลจริง",
          "🌾 การทำนายผลผลิตข้าวโพดด้วย ML",
          "🔬 การตรวจจับศัตรูพืชด้วย Classification"
        ],
        codeExamples: [
          "การใช้ Scikit-learn สำหรับ Machine Learning",
          "การสร้างโมเดลทำนายผลผลิตข้าว",
          "การตรวจจับศัตรูพืชด้วย Image Classification",
          "การปรับปรุงระบบชลประทานด้วย ML"
        ],
        pages: "20+"
      },
      3: {
        sections: [
          "โครงสร้างและการทำงานของ Neural Networks",
          "Activation Functions: Sigmoid, ReLU, Tanh, Leaky ReLU",
          "การฝึกโมเดล: Forward Propagation และ Backpropagation",
          "ประเภท Networks: FNN, CNN, RNN, LSTM",
          "การประยุกต์ใช้ในการเกษตร: การตรวจจับโรคพืช, วิเคราะห์ภาพดาวเทียม",
          "เครื่องมือ: TensorFlow, Keras, PyTorch"
        ],
        interactiveFeatures: [
          "🧠 Neural Network Visualizer แบบ 3D",
          "⚡ การสาธิต Activation Functions แบบเปรียบเทียบ",
          "🔄 Training Process Animation พร้อมกราฟ Loss",
          "📷 CNN สำหรับการตรวจจับโรคพืชแบบเรียลไทม์",
          "📊 การเปรียบเทียบประสิทธิภาพ Network ต่างๆ"
        ],
        codeExamples: [
          "การสร้าง Neural Network ด้วย TensorFlow/Keras",
          "CNN สำหรับการจำแนกภาพใบไม้ที่เป็นโรค",
          "LSTM สำหรับทำนายผลผลิตตามฤดูกาล",
          "Transfer Learning สำหรับการเกษตร"
        ],
        pages: "25+"
      },
      4: {
        sections: [
          "หลักการประมวลผลภาพดิจิทัล",
          "การตรวจจับขอบและการสกัดคุณลักษณะ",
          "Color Spaces และการวิเคราะห์สี",
          "การตรวจจับและจำแนกวัตถุ",
          "การประยุกต์ใช้ในการเกษตร: การตรวจสอบด้วยโดรน, การนับผลไม้",
          "เครื่องมือ: OpenCV, PIL, scikit-image"
        ],
        interactiveFeatures: [
          "🖼️ Image Processing Demo แบบครบวงจร",
          "🔍 Edge Detection Comparison Tool",
          "🎨 Color Analysis Tool สำหรับวิเคราะห์ความสุกผลไม้",
          "🚁 Drone Monitoring Simulation",
          "📱 Real-time Object Detection Demo"
        ],
        codeExamples: [
          "การใช้ OpenCV สำหรับการประมวลผลภาพ",
          "การตรวจจับโรคพืชจากภาพใบไม้",
          "การนับผลไม้อัตโนมัติด้วย Computer Vision",
          "การวิเคราะห์ภาพดาวเทียมเพื่อการเกษตร"
        ],
        pages: "30+"
      },
      5: {
        sections: [
          "การประมวลผลภาษาธรรมชาติพื้นฐาน",
          "Tokenization, POS Tagging, Named Entity Recognition",
          "การวิเคราะห์ความรู้สึกและการจำแนกข้อความ",
          "การประยุกต์ใช้ในการเกษตร: Chatbot เกษตรกร, การวิเคราะห์ข่าว",
          "เครื่องมือ: NLTK, spaCy, PyThaiNLP",
          "การสร้างระบบแปลภาษาเฉพาะด้าน"
        ],
        interactiveFeatures: [
          "💬 Agricultural Chatbot GUI แบบใช้งานได้จริง",
          "📊 Sentiment Analysis Demo สำหรับข้อความภาษาไทย",
          "📰 News Analysis System แบบเรียลไทม์",
          "🔤 Text Preprocessing Tools แบบโต้ตอบ",
          "🌐 Translation System สำหรับศัพท์เกษตร"
        ],
        codeExamples: [
          "การสร้าง Chatbot ด้วย Python และ GUI",
          "การวิเคราะห์ความรู้สึกในข้อความภาษาไทย",
          "การสกัดข้อมูลจากข่าวเกษตรอัตโนมัติ",
          "ระบบแนะนำการเกษตรด้วย NLP"
        ],
        pages: "35+"
      },
      6: {
        sections: [
          "หลักการหุ่นยนต์และระบบอัตโนมัติ",
          "เซนเซอร์และการควบคุมในการเกษตร",
          "ระบบชลประทานอัตโนมัติ",
          "หุ่นยนต์เก็บเกี่ยวและปลูกพืช",
          "การบำรุงรักษาและการแก้ไขปัญหา"
        ],
        interactiveFeatures: [
          "🤖 Robot Simulation แบบ 3D",
          "💧 Irrigation System Controller",
          "📡 Sensor Data Visualization",
          "🚜 Autonomous Farming Vehicle Demo"
        ],
        codeExamples: [
          "การควบคุมหุ่นยนต์ด้วย Python",
          "ระบบชลประทานอัตโนมัติ",
          "การประมวลผลข้อมูลเซนเซอร์"
        ],
        pages: "20+"
      },
      7: {
        sections: [
          "การวิเคราะห์คุณภาพดินด้วย AI",
          "การเก็บและประมวลผลข้อมูลดิน",
          "การสร้างโมเดลทำนายคุณภาพดิน",
          "การแปลผลและให้คำแนะนำ"
        ],
        interactiveFeatures: [
          "🌱 Soil Analysis Simulator",
          "📊 Data Visualization Dashboard",
          "🔬 AI Model Training Interface"
        ],
        codeExamples: [
          "การวิเคราะห์ข้อมูลดินด้วย Python",
          "การสร้างโมเดล ML สำหรับคุณภาพดิน",
          "ระบบแนะนำการปรับปรุงดิน"
        ],
        pages: "25+"
      },
      8: {
        sections: [
          "จริยธรรมในการใช้ AI",
          "ความเป็นส่วนตัวและความปลอดภัย",
          "อนาคตของ AI ในการเกษตร",
          "การเตรียมตัวสำหรับยุคดิจิทัล"
        ],
        interactiveFeatures: [
          "⚖️ Ethics Decision Simulator",
          "🔮 Future Prediction Tool",
          "💼 Career Path Advisor"
        ],
        codeExamples: [
          "การประเมินความเสี่ยงของ AI",
          "ระบบตรวจสอบความเป็นธรรม"
        ],
        pages: "15+"
      }
    };
    
    return enhancedContent[chapterId] || {
      sections: ["เนื้อหาพื้นฐาน", "การประยุกต์ใช้", "ตัวอย่างและแบบฝึกหัด"],
      interactiveFeatures: ["การสาธิตแบบโต้ตอบ"],
      codeExamples: ["ตัวอย่างโค้ด Python"],
      pages: "20+"
    };
  };

  const enhancedContent = getEnhancedContent(parseInt(id));
  const Icon = chapter.icon;

  return (
    <motion.div
      initial={{ opacity: 0, y: 20 }}
      animate={{ opacity: 1, y: 0 }}
      transition={{ duration: 0.6 }}
      className="min-h-screen bg-gradient-to-br from-slate-50 to-blue-50 pt-20"
    >
      <div className="container mx-auto px-6 py-12">
        <div className="max-w-6xl mx-auto">
          {/* Navigation */}
          <motion.div
            initial={{ opacity: 0, x: -20 }}
            animate={{ opacity: 1, x: 0 }}
            transition={{ delay: 0.1, duration: 0.5 }}
            className="mb-8"
          >
            <Link 
              to="/chapters"
              className="inline-flex items-center text-purple-600 hover:text-purple-700 transition-colors"
            >
              <ChevronRight className="w-4 h-4 mr-1 rotate-180" />
              กลับไปหน้าบทเรียน
            </Link>
          </motion.div>

          {/* Main Content */}
          <motion.div
            initial={{ opacity: 0, scale: 0.9 }}
            animate={{ opacity: 1, scale: 1 }}
            transition={{ delay: 0.2, duration: 0.5 }}
            className="bg-white rounded-3xl shadow-2xl overflow-hidden"
          >
            {/* Header */}
            <div className={`h-64 bg-gradient-to-r ${chapter.color} flex items-center justify-center relative overflow-hidden`}>
              <div className="absolute inset-0 bg-black/20"></div>
              <div className="relative z-10 text-center text-white">
                <Icon size={80} className="mx-auto mb-4" />
                <h1 className="text-4xl font-bold mb-2">{chapter.title}</h1>
                <p className="text-xl opacity-90">{chapter.subtitle}</p>
                <div className="mt-4 inline-flex items-center bg-white/20 rounded-full px-4 py-2">
                  <BookOpen className="w-5 h-5 mr-2" />
                  <span className="font-medium">{enhancedContent.pages} หน้า</span>
                </div>
              </div>
            </div>
            
            {/* Content */}
            <div className="p-8">
              <div className="prose prose-lg max-w-none">
                <p className="text-gray-600 text-lg leading-relaxed mb-8">
                  {chapter.description}
                </p>
                
                {/* Enhanced Content Grid */}
                <div className="grid lg:grid-cols-2 gap-8 mb-8">
                  {/* Sections */}
                  <div className="bg-gradient-to-r from-blue-50 to-indigo-50 rounded-xl p-6">
                    <h3 className="text-xl font-semibold text-gray-800 mb-4 flex items-center">
                      <BookOpen className="w-6 h-6 text-blue-500 mr-2" />
                      เนื้อหาในบทนี้
                    </h3>
                    <ul className="space-y-3">
                      {enhancedContent.sections.map((section, index) => (
                        <li key={index} className="flex items-start text-gray-700">
                          <ChevronRight className="w-5 h-5 text-blue-500 mr-2 mt-0.5 flex-shrink-0" />
                          <span className="text-sm leading-relaxed">{section}</span>
                        </li>
                      ))}
                    </ul>
                  </div>

                  {/* Interactive Features */}
                  <div className="bg-gradient-to-r from-green-50 to-emerald-50 rounded-xl p-6">
                    <h3 className="text-xl font-semibold text-gray-800 mb-4 flex items-center">
                      <Zap className="w-6 h-6 text-green-500 mr-2" />
                      การจำลองแบบโต้ตอบ
                    </h3>
                    <ul className="space-y-3">
                      {enhancedContent.interactiveFeatures.map((feature, index) => (
                        <li key={index} className="flex items-start text-gray-700">
                          <Play className="w-5 h-5 text-green-500 mr-2 mt-0.5 flex-shrink-0" />
                          <span className="text-sm leading-relaxed">{feature}</span>
                        </li>
                      ))}
                    </ul>
                  </div>
                </div>

                {/* Code Examples */}
                <div className="bg-gradient-to-r from-purple-50 to-pink-50 rounded-xl p-6 mb-8">
                  <h3 className="text-xl font-semibold text-gray-800 mb-4 flex items-center">
                    <Code className="w-6 h-6 text-purple-500 mr-2" />
                    ตัวอย่างโค้ดและการทดลอง
                  </h3>
                  <ul className="space-y-3">
                    {enhancedContent.codeExamples.map((example, index) => (
                      <li key={index} className="flex items-start text-gray-700">
                        <ChevronRight className="w-5 h-5 text-purple-500 mr-2 mt-0.5 flex-shrink-0" />
                        <span className="text-sm leading-relaxed">{example}</span>
                      </li>
                    ))}
                  </ul>
                </div>
                
                {/* Enhanced Content Notice */}
                <div className="bg-yellow-50 border-l-4 border-yellow-400 p-6 mb-8">
                  <div className="flex">
                    <Sparkles className="w-6 h-6 text-yellow-400 mr-3 mt-1 flex-shrink-0" />
                    <div>
                      <h4 className="text-lg font-semibold text-yellow-800 mb-2">เนื้อหาเพิ่มเติม</h4>
                      <p className="text-yellow-700 leading-relaxed">
                        บทนี้ได้รับการปรับปรุงด้วยเนื้อหาเชิงลึกมากกว่า <strong>{enhancedContent.pages} หน้า</strong> 
                        พร้อมการจำลองแบบโต้ตอบ ตัวอย่างโค้ดที่ใช้งานได้จริง และกรณีศึกษาในการเกษตรไทย
                      </p>
                    </div>
                  </div>
                </div>

                {/* Agriculture Application Highlight */}
                <div className="bg-gradient-to-r from-green-100 to-blue-100 rounded-xl p-6 mb-8">
                  <div className="flex items-center mb-4">
                    <Leaf className="w-6 h-6 text-green-600 mr-2" />
                    <h4 className="text-lg font-semibold text-gray-800">การประยุกต์ใช้ในการเกษตรไทย</h4>
                  </div>
                  <p className="text-gray-700 leading-relaxed">
                    บทนี้มีการยกตัวอย่างการประยุกต์ใช้เทคโนโลยีในการเกษตรไทยอย่างละเอียด 
                    พร้อมโค้ดตัวอย่างที่สามารถนำไปปรับใช้ได้จริงในฟาร์มและการเกษตรสมัยใหม่ 
                    รวมถึงกรณีศึกษาจากเกษตรกรไทยที่ประสบความสำเร็จ
                  </p>
                </div>

                {/* Action Buttons */}
                <div className="flex flex-wrap gap-4 justify-center">
                  <button className="inline-flex items-center px-6 py-3 bg-gradient-to-r from-purple-600 to-pink-600 text-white font-semibold rounded-xl hover:from-purple-700 hover:to-pink-700 transform hover:scale-105 transition-all duration-200 shadow-lg hover:shadow-xl">
                    <Play className="w-5 h-5 mr-2" />
                    เริ่มเรียน
                  </button>
                  <button className="inline-flex items-center px-6 py-3 bg-gradient-to-r from-green-600 to-blue-600 text-white font-semibold rounded-xl hover:from-green-700 hover:to-blue-700 transform hover:scale-105 transition-all duration-200 shadow-lg hover:shadow-xl">
                    <Download className="w-5 h-5 mr-2" />
                    ดาวน์โหลดโค้ด
                  </button>
                </div>
              </div>
            </div>
          </motion.div>
        </div>
      </div>
    </motion.div>
  );
};

export default EnhancedChapterDetail;

