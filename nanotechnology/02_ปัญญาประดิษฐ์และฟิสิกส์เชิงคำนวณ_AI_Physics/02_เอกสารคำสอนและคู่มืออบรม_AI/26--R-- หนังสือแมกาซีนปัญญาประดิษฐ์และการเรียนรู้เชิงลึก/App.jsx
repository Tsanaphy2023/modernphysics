import React, { useState } from 'react';
import { BrowserRouter as Router, Routes, Route, Link, useLocation, useParams } from 'react-router-dom';
import { motion, AnimatePresence } from 'framer-motion';
import { 
  BookOpen, 
  Brain, 
  Cpu, 
  Eye, 
  MessageSquare, 
  Bot, 
  Microscope, 
  Shield,
  Menu,
  X,
  ChevronRight,
  Sparkles,
  Zap,
  Leaf
} from 'lucide-react';
import EnhancedChapterDetail from './components/EnhancedChapterDetail';
import './App.css';

// Import images
import bookCover from './assets/book_cover_final.png';
import chapter1Image from './assets/chapter1_image.png';
import chapter2Image from './assets/chapter2_image.png';
import chapter3Image from './assets/chapter3_image.png';
import chapter4Image from './assets/chapter4_image.png';
import chapter5Image from './assets/chapter5_image.png';
import chapter6Image from './assets/chapter6_image.png';
import chapter7Image from './assets/chapter7_image.png';
import chapter8Image from './assets/chapter8_image.png';

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
    description: "ดำดิ่งสู่โลกของ Deep Learning และโครงข่ายประสาทเทียม",
    icon: Zap,
    image: chapter3Image,
    color: "from-green-500 to-emerald-500"
  },
  {
    id: 4,
    title: "คอมพิวเตอร์วิทัศน์",
    subtitle: "Computer Vision",
    description: "การทำให้คอมพิวเตอร์สามารถ 'มองเห็น' และเข้าใจภาพได้",
    icon: Eye,
    image: chapter4Image,
    color: "from-orange-500 to-red-500"
  },
  {
    id: 5,
    title: "การประมวลผลภาษาธรรมชาติ",
    subtitle: "Natural Language Processing",
    description: "การทำให้คอมพิวเตอร์เข้าใจและประมวลผลภาษาของมนุษย์",
    icon: MessageSquare,
    image: chapter5Image,
    color: "from-indigo-500 to-purple-500"
  },
  {
    id: 6,
    title: "หุ่นยนต์และระบบอัตโนมัติในการเกษตร",
    subtitle: "Robotics & Automation in Agriculture",
    description: "การประยุกต์ใช้หุ่นยนต์และระบบอัตโนมัติในภาคการเกษตร",
    icon: Bot,
    image: chapter6Image,
    color: "from-teal-500 to-green-500"
  },
  {
    id: 7,
    title: "Project 3: วิเคราะห์คุณภาพดินด้วย AI",
    subtitle: "Soil Quality Analysis with AI",
    description: "โปรเจกต์การใช้ AI ในการวิเคราะห์และประเมินคุณภาพดิน",
    icon: Microscope,
    image: chapter7Image,
    color: "from-amber-500 to-orange-500"
  },
  {
    id: 8,
    title: "จริยธรรมและอนาคตของ AI",
    subtitle: "Ethics and Future of AI",
    description: "ประเด็นทางจริยธรรมและการมองอนาคตของปัญญาประดิษฐ์",
    icon: Shield,
    image: chapter8Image,
    color: "from-rose-500 to-pink-500"
  }
];

// Navigation Component
const Navigation = ({ isOpen, setIsOpen }) => {
  const location = useLocation();
  
  return (
    <>
      <nav className="fixed top-0 left-0 right-0 z-50 bg-white/80 backdrop-blur-md border-b border-gray-200">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="flex justify-between items-center h-16">
            <Link to="/" className="flex items-center space-x-2">
              <div className="w-8 h-8 bg-gradient-to-r from-purple-500 to-pink-500 rounded-lg flex items-center justify-center">
                <Brain className="w-5 h-5 text-white" />
              </div>
              <span className="font-bold text-xl bg-gradient-to-r from-purple-600 to-pink-600 bg-clip-text text-transparent">
                AI & Deep Learning
              </span>
            </Link>
            
            <div className="hidden md:flex items-center space-x-8">
              <Link 
                to="/" 
                className={`text-sm font-medium transition-colors hover:text-purple-600 ${
                  location.pathname === '/' ? 'text-purple-600' : 'text-gray-700'
                }`}
              >
                หน้าแรก
              </Link>
              <Link 
                to="/chapters" 
                className={`text-sm font-medium transition-colors hover:text-purple-600 ${
                  location.pathname === '/chapters' ? 'text-purple-600' : 'text-gray-700'
                }`}
              >
                บทเรียน
              </Link>
              <Link 
                to="/about" 
                className={`text-sm font-medium transition-colors hover:text-purple-600 ${
                  location.pathname === '/about' ? 'text-purple-600' : 'text-gray-700'
                }`}
              >
                เกี่ยวกับ
              </Link>
            </div>
            
            <button
              onClick={() => setIsOpen(!isOpen)}
              className="md:hidden p-2 rounded-md text-gray-700 hover:text-purple-600 hover:bg-gray-100"
            >
              {isOpen ? <X className="w-6 h-6" /> : <Menu className="w-6 h-6" />}
            </button>
          </div>
        </div>
        
        {/* Mobile menu */}
        <AnimatePresence>
          {isOpen && (
            <motion.div
              initial={{ opacity: 0, height: 0 }}
              animate={{ opacity: 1, height: 'auto' }}
              exit={{ opacity: 0, height: 0 }}
              className="md:hidden bg-white border-t border-gray-200"
            >
              <div className="px-4 py-2 space-y-1">
                <Link 
                  to="/" 
                  className="block px-3 py-2 text-sm font-medium text-gray-700 hover:text-purple-600 hover:bg-gray-50 rounded-md"
                  onClick={() => setIsOpen(false)}
                >
                  หน้าแรก
                </Link>
                <Link 
                  to="/chapters" 
                  className="block px-3 py-2 text-sm font-medium text-gray-700 hover:text-purple-600 hover:bg-gray-50 rounded-md"
                  onClick={() => setIsOpen(false)}
                >
                  บทเรียน
                </Link>
                <Link 
                  to="/about" 
                  className="block px-3 py-2 text-sm font-medium text-gray-700 hover:text-purple-600 hover:bg-gray-50 rounded-md"
                  onClick={() => setIsOpen(false)}
                >
                  เกี่ยวกับ
                </Link>
              </div>
            </motion.div>
          )}
        </AnimatePresence>
      </nav>
    </>
  );
};

// Hero Section Component
const HeroSection = () => {
  return (
    <section className="relative min-h-screen flex items-center justify-center overflow-hidden bg-gradient-to-br from-purple-50 via-pink-50 to-blue-50">
      {/* Animated background elements */}
      <div className="absolute inset-0">
        <div className="absolute top-20 left-10 w-72 h-72 bg-purple-300 rounded-full mix-blend-multiply filter blur-xl opacity-70 animate-blob"></div>
        <div className="absolute top-40 right-10 w-72 h-72 bg-yellow-300 rounded-full mix-blend-multiply filter blur-xl opacity-70 animate-blob animation-delay-2000"></div>
        <div className="absolute -bottom-8 left-20 w-72 h-72 bg-pink-300 rounded-full mix-blend-multiply filter blur-xl opacity-70 animate-blob animation-delay-4000"></div>
      </div>
      
      <div className="relative z-10 max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-20">
        <div className="grid lg:grid-cols-2 gap-12 items-center">
          <motion.div
            initial={{ opacity: 0, x: -50 }}
            animate={{ opacity: 1, x: 0 }}
            transition={{ duration: 0.8 }}
            className="text-center lg:text-left"
          >
            <motion.div
              initial={{ opacity: 0, y: 20 }}
              animate={{ opacity: 1, y: 0 }}
              transition={{ delay: 0.2, duration: 0.6 }}
              className="inline-flex items-center px-4 py-2 bg-gradient-to-r from-purple-100 to-pink-100 rounded-full text-sm font-medium text-purple-800 mb-6"
            >
              <Sparkles className="w-4 h-4 mr-2" />
              สำหรับนักเรียนมัธยมศึกษา
            </motion.div>
            
            <motion.h1
              initial={{ opacity: 0, y: 20 }}
              animate={{ opacity: 1, y: 0 }}
              transition={{ delay: 0.4, duration: 0.6 }}
              className="text-4xl md:text-6xl font-bold text-gray-900 mb-6"
            >
              <span className="bg-gradient-to-r from-purple-600 to-pink-600 bg-clip-text text-transparent">
                AI & Deep Learning
              </span>
              <br />
              <span className="text-2xl md:text-4xl text-gray-700">
                ปลดล็อกสมองกล พลิกโฉมโลกเกษตร
              </span>
            </motion.h1>
            
            <motion.p
              initial={{ opacity: 0, y: 20 }}
              animate={{ opacity: 1, y: 0 }}
              transition={{ delay: 0.6, duration: 0.6 }}
              className="text-xl text-gray-600 mb-8 leading-relaxed"
            >
              เรียนรู้ปัญญาประดิษฐ์และการเรียนรู้เชิงลึกจากพื้นฐานสู่ขั้นสูง 
              พร้อมการประยุกต์ใช้ในภาคการเกษตรสมัยใหม่
            </motion.p>
            
            <motion.div
              initial={{ opacity: 0, y: 20 }}
              animate={{ opacity: 1, y: 0 }}
              transition={{ delay: 0.8, duration: 0.6 }}
              className="flex flex-col sm:flex-row gap-4 justify-center lg:justify-start"
            >
              <Link
                to="/chapters"
                className="inline-flex items-center px-8 py-4 bg-gradient-to-r from-purple-600 to-pink-600 text-white font-semibold rounded-xl hover:from-purple-700 hover:to-pink-700 transform hover:scale-105 transition-all duration-200 shadow-lg hover:shadow-xl"
              >
                <BookOpen className="w-5 h-5 mr-2" />
                เริ่มเรียนรู้
                <ChevronRight className="w-5 h-5 ml-2" />
              </Link>
              <Link
                to="/about"
                className="inline-flex items-center px-8 py-4 bg-white text-gray-700 font-semibold rounded-xl border-2 border-gray-200 hover:border-purple-300 hover:text-purple-600 transform hover:scale-105 transition-all duration-200 shadow-lg hover:shadow-xl"
              >
                เกี่ยวกับหนังสือ
              </Link>
            </motion.div>
            
            <motion.div
              initial={{ opacity: 0, y: 20 }}
              animate={{ opacity: 1, y: 0 }}
              transition={{ delay: 1, duration: 0.6 }}
              className="mt-12 text-center lg:text-left"
            >
              <p className="text-sm text-gray-500 mb-4">ผู้แต่ง</p>
              <p className="text-lg font-semibold text-gray-800">ผศ.ดร.ชีวะ ทัศนา</p>
            </motion.div>
          </motion.div>
          
          <motion.div
            initial={{ opacity: 0, x: 50 }}
            animate={{ opacity: 1, x: 0 }}
            transition={{ duration: 0.8, delay: 0.2 }}
            className="relative"
          >
            <div className="relative z-10">
              <img
                src={bookCover}
                alt="AI & Deep Learning Book Cover"
                className="w-full max-w-md mx-auto rounded-2xl shadow-2xl transform hover:scale-105 transition-transform duration-300"
              />
            </div>
            
            {/* Floating elements */}
            <motion.div
              animate={{ y: [-10, 10, -10] }}
              transition={{ duration: 4, repeat: Infinity, ease: "easeInOut" }}
              className="absolute -top-4 -right-4 w-16 h-16 bg-gradient-to-r from-yellow-400 to-orange-400 rounded-full flex items-center justify-center shadow-lg"
            >
              <Leaf className="w-8 h-8 text-white" />
            </motion.div>
            
            <motion.div
              animate={{ y: [10, -10, 10] }}
              transition={{ duration: 3, repeat: Infinity, ease: "easeInOut", delay: 1 }}
              className="absolute -bottom-4 -left-4 w-12 h-12 bg-gradient-to-r from-green-400 to-blue-400 rounded-full flex items-center justify-center shadow-lg"
            >
              <Brain className="w-6 h-6 text-white" />
            </motion.div>
          </motion.div>
        </div>
      </div>
    </section>
  );
};

// Chapter Card Component
const ChapterCard = ({ chapter, index }) => {
  const Icon = chapter.icon;
  
  return (
    <motion.div
      initial={{ opacity: 0, y: 50 }}
      animate={{ opacity: 1, y: 0 }}
      transition={{ duration: 0.6, delay: index * 0.1 }}
      className="group relative bg-white rounded-2xl shadow-lg hover:shadow-2xl transition-all duration-300 overflow-hidden border border-gray-100 hover:border-purple-200"
    >
      <div className={`absolute inset-0 bg-gradient-to-br ${chapter.color} opacity-0 group-hover:opacity-5 transition-opacity duration-300`}></div>
      
      <div className="relative p-6">
        <div className="flex items-start space-x-4">
          <div className={`flex-shrink-0 w-12 h-12 bg-gradient-to-r ${chapter.color} rounded-xl flex items-center justify-center group-hover:scale-110 transition-transform duration-300`}>
            <Icon className="w-6 h-6 text-white" />
          </div>
          
          <div className="flex-1 min-w-0">
            <div className="flex items-center space-x-2 mb-2">
              <span className="text-sm font-medium text-gray-500">บทที่ {chapter.id}</span>
              <div className="w-1 h-1 bg-gray-300 rounded-full"></div>
              <span className="text-sm text-gray-400">{chapter.subtitle}</span>
            </div>
            
            <h3 className="text-lg font-bold text-gray-900 mb-3 group-hover:text-purple-600 transition-colors duration-300">
              {chapter.title}
            </h3>
            
            <p className="text-gray-600 text-sm leading-relaxed mb-4">
              {chapter.description}
            </p>
            
            <div className="flex items-center justify-between">
              <Link
                to={`/chapter/${chapter.id}`}
                className="inline-flex items-center text-sm font-medium text-purple-600 hover:text-purple-700 group-hover:translate-x-1 transition-all duration-200"
              >
                อ่านเพิ่มเติม
                <ChevronRight className="w-4 h-4 ml-1" />
              </Link>
              
              <div className="w-16 h-16 rounded-lg overflow-hidden opacity-80 group-hover:opacity-100 transition-opacity duration-300">
                <img
                  src={chapter.image}
                  alt={chapter.title}
                  className="w-full h-full object-cover"
                />
              </div>
            </div>
          </div>
        </div>
      </div>
    </motion.div>
  );
};

// Home Page Component
const HomePage = () => {
  return (
    <div className="pt-16">
      <HeroSection />
      
      {/* Features Section */}
      <section className="py-20 bg-white">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <motion.div
            initial={{ opacity: 0, y: 30 }}
            whileInView={{ opacity: 1, y: 0 }}
            transition={{ duration: 0.6 }}
            viewport={{ once: true }}
            className="text-center mb-16"
          >
            <h2 className="text-3xl md:text-4xl font-bold text-gray-900 mb-4">
              ทำไมต้องเรียน AI และ Deep Learning?
            </h2>
            <p className="text-xl text-gray-600 max-w-3xl mx-auto">
              ปัญญาประดิษฐ์กำลังเปลี่ยนแปลงโลก เรียนรู้เทคโนโลยีที่จะกำหนดอนาคต
            </p>
          </motion.div>
          
          <div className="grid md:grid-cols-3 gap-8">
            {[
              {
                icon: Brain,
                title: "เข้าใจง่าย",
                description: "เนื้อหาที่เขียนเพื่อนักเรียนมัธยมศึกษาโดยเฉพาะ พร้อมตัวอย่างที่เข้าใจง่าย"
              },
              {
                icon: Leaf,
                title: "ประยุกต์ใช้จริง",
                description: "เรียนรู้การใช้ AI ในการเกษตร ซึ่งเป็นอุตสาหกรรมสำคัญของประเทศ"
              },
              {
                icon: Zap,
                title: "ทันสมัย",
                description: "เนื้อหาที่ทันสมัยและเป็นปัจจุบัน พร้อมโค้ดตัวอย่างที่ใช้งานได้จริง"
              }
            ].map((feature, index) => (
              <motion.div
                key={index}
                initial={{ opacity: 0, y: 30 }}
                whileInView={{ opacity: 1, y: 0 }}
                transition={{ duration: 0.6, delay: index * 0.2 }}
                viewport={{ once: true }}
                className="text-center p-6 rounded-2xl bg-gradient-to-br from-gray-50 to-white border border-gray-100 hover:shadow-lg transition-shadow duration-300"
              >
                <div className="w-16 h-16 bg-gradient-to-r from-purple-500 to-pink-500 rounded-2xl flex items-center justify-center mx-auto mb-4">
                  <feature.icon className="w-8 h-8 text-white" />
                </div>
                <h3 className="text-xl font-bold text-gray-900 mb-3">{feature.title}</h3>
                <p className="text-gray-600">{feature.description}</p>
              </motion.div>
            ))}
          </div>
        </div>
      </section>
      
      {/* Chapters Preview */}
      <section className="py-20 bg-gradient-to-br from-gray-50 to-white">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <motion.div
            initial={{ opacity: 0, y: 30 }}
            whileInView={{ opacity: 1, y: 0 }}
            transition={{ duration: 0.6 }}
            viewport={{ once: true }}
            className="text-center mb-16"
          >
            <h2 className="text-3xl md:text-4xl font-bold text-gray-900 mb-4">
              สำรวจบทเรียนทั้ง 8 บท
            </h2>
            <p className="text-xl text-gray-600 max-w-3xl mx-auto">
              จากพื้นฐาน AI ไปจนถึงการประยุกต์ใช้ในการเกษตรสมัยใหม่
            </p>
          </motion.div>
          
          <div className="grid md:grid-cols-2 lg:grid-cols-2 gap-8">
            {chapters.slice(0, 4).map((chapter, index) => (
              <ChapterCard key={chapter.id} chapter={chapter} index={index} />
            ))}
          </div>
          
          <motion.div
            initial={{ opacity: 0, y: 30 }}
            whileInView={{ opacity: 1, y: 0 }}
            transition={{ duration: 0.6, delay: 0.4 }}
            viewport={{ once: true }}
            className="text-center mt-12"
          >
            <Link
              to="/chapters"
              className="inline-flex items-center px-8 py-4 bg-gradient-to-r from-purple-600 to-pink-600 text-white font-semibold rounded-xl hover:from-purple-700 hover:to-pink-700 transform hover:scale-105 transition-all duration-200 shadow-lg hover:shadow-xl"
            >
              ดูบทเรียนทั้งหมด
              <ChevronRight className="w-5 h-5 ml-2" />
            </Link>
          </motion.div>
        </div>
      </section>
    </div>
  );
};

// Chapters Page Component
const ChaptersPage = () => {
  return (
    <div className="pt-16 min-h-screen bg-gradient-to-br from-gray-50 to-white">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-20">
        <motion.div
          initial={{ opacity: 0, y: 30 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.6 }}
          className="text-center mb-16"
        >
          <h1 className="text-4xl md:text-5xl font-bold text-gray-900 mb-4">
            บทเรียนทั้งหมด
          </h1>
          <p className="text-xl text-gray-600 max-w-3xl mx-auto">
            เรียนรู้ AI และ Deep Learning ผ่านบทเรียน 8 บทที่ครอบคลุมและเข้าใจง่าย
          </p>
        </motion.div>
        
        <div className="grid md:grid-cols-2 gap-8">
          {chapters.map((chapter, index) => (
            <ChapterCard key={chapter.id} chapter={chapter} index={index} />
          ))}
        </div>
      </div>
    </div>
  );
};

// About Page Component
const AboutPage = () => {
  return (
    <div className="pt-16 min-h-screen bg-gradient-to-br from-gray-50 to-white">
      <div className="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 py-20">
        <motion.div
          initial={{ opacity: 0, y: 30 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.6 }}
          className="text-center mb-16"
        >
          <h1 className="text-4xl md:text-5xl font-bold text-gray-900 mb-4">
            เกี่ยวกับหนังสือ
          </h1>
          <p className="text-xl text-gray-600">
            AI & Deep Learning: ปลดล็อกสมองกล พลิกโฉมโลกเกษตร
          </p>
        </motion.div>
        
        <div className="grid md:grid-cols-2 gap-12 items-center mb-16">
          <motion.div
            initial={{ opacity: 0, x: -30 }}
            animate={{ opacity: 1, x: 0 }}
            transition={{ duration: 0.6, delay: 0.2 }}
          >
            <img
              src={bookCover}
              alt="Book Cover"
              className="w-full max-w-sm mx-auto rounded-2xl shadow-2xl"
            />
          </motion.div>
          
          <motion.div
            initial={{ opacity: 0, x: 30 }}
            animate={{ opacity: 1, x: 0 }}
            transition={{ duration: 0.6, delay: 0.4 }}
            className="space-y-6"
          >
            <div>
              <h2 className="text-2xl font-bold text-gray-900 mb-4">รายละเอียดหนังสือ</h2>
              <div className="space-y-3 text-gray-600">
                <p><span className="font-semibold">ชื่อหนังสือ:</span> AI & Deep Learning: ปลดล็อกสมองกล พลิกโฉมโลกเกษตร</p>
                <p><span className="font-semibold">ผู้แต่ง:</span> ผศ.ดร.ชีวะ ทัศนา</p>
                <p><span className="font-semibold">จำนวนบท:</span> 8 บท</p>
                <p><span className="font-semibold">จำนวนหน้า:</span> มากกว่า 200 หน้า</p>
                <p><span className="font-semibold">กลุ่มเป้าหมาย:</span> นักเรียนมัธยมศึกษา</p>
              </div>
            </div>
            
            <div>
              <h3 className="text-xl font-bold text-gray-900 mb-3">จุดเด่นของหนังสือ</h3>
              <ul className="space-y-2 text-gray-600">
                <li className="flex items-start">
                  <ChevronRight className="w-5 h-5 text-purple-500 mr-2 mt-0.5 flex-shrink-0" />
                  เนื้อหาเขียนเพื่อนักเรียนมัธยมศึกษาโดยเฉพาะ
                </li>
                <li className="flex items-start">
                  <ChevronRight className="w-5 h-5 text-purple-500 mr-2 mt-0.5 flex-shrink-0" />
                  ภาพประกอบและแผนผังที่เข้าใจง่าย
                </li>
                <li className="flex items-start">
                  <ChevronRight className="w-5 h-5 text-purple-500 mr-2 mt-0.5 flex-shrink-0" />
                  โค้ดตัวอย่างด้านการเกษตร
                </li>
                <li className="flex items-start">
                  <ChevronRight className="w-5 h-5 text-purple-500 mr-2 mt-0.5 flex-shrink-0" />
                  การประยุกต์ใช้ AI ในการเกษตรจริง
                </li>
              </ul>
            </div>
          </motion.div>
        </div>
        
        <motion.div
          initial={{ opacity: 0, y: 30 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.6, delay: 0.6 }}
          className="bg-white rounded-2xl p-8 shadow-lg border border-gray-100"
        >
          <h2 className="text-2xl font-bold text-gray-900 mb-6">เกี่ยวกับผู้แต่ง</h2>
          <div className="prose prose-lg text-gray-600">
            <p>
              <strong>ผศ.ดร.ชีวะ ทัศนา</strong> เป็นผู้เชี่ยวชาญด้านปัญญาประดิษฐ์และการประยุกต์ใช้ในภาคการเกษตร 
              ด้วยประสบการณ์ในการสอนและวิจัยมาอย่างยาวนาน ท่านได้เห็นความสำคัญของการนำเทคโนโลยี AI 
              มาใช้ในการพัฒนาการเกษตรไทยให้ทันสมัยและยั่งยืน
            </p>
            <p>
              หนังสือเล่มนี้เกิดจากความตั้งใจที่จะถ่ายทอดความรู้ด้าน AI ให้กับนักเรียนรุ่นใหม่ 
              เพื่อให้พวกเขาเตรียมพร้อมสำหรับอนาคตที่เทคโนโลยีจะมีบทบาทสำคัญมากขึ้น
            </p>
          </div>
        </motion.div>
      </div>
    </div>
  );
};

// Chapter Detail Page Component
const ChapterDetailPage = () => {
  const { id } = useParams();
  const chapter = chapters.find(c => c.id === parseInt(id));
  
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

  const Icon = chapter.icon;
  
  return (
    <div className="pt-16 min-h-screen bg-gradient-to-br from-gray-50 to-white">
      <div className="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 py-20">
        <motion.div
          initial={{ opacity: 0, y: 30 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.6 }}
          className="mb-8"
        >
          <Link 
            to="/chapters"
            className="inline-flex items-center text-purple-600 hover:text-purple-700 mb-8"
          >
            <ChevronRight className="w-4 h-4 mr-1 rotate-180" />
            กลับไปหน้าบทเรียน
          </Link>
          
          <div className="flex items-center space-x-4 mb-6">
            <div className={`w-16 h-16 bg-gradient-to-r ${chapter.color} rounded-2xl flex items-center justify-center`}>
              <Icon className="w-8 h-8 text-white" />
            </div>
            <div>
              <p className="text-sm font-medium text-gray-500">บทที่ {chapter.id}</p>
              <h1 className="text-3xl md:text-4xl font-bold text-gray-900">{chapter.title}</h1>
              <p className="text-lg text-gray-600">{chapter.subtitle}</p>
            </div>
          </div>
        </motion.div>
        
        <motion.div
          initial={{ opacity: 0, y: 30 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.6, delay: 0.2 }}
          className="bg-white rounded-2xl p-8 shadow-lg border border-gray-100 mb-8"
        >
          <img
            src={chapter.image}
            alt={chapter.title}
            className="w-full h-64 object-cover rounded-xl mb-6"
          />
          
          <div className="prose prose-lg max-w-none text-gray-600">
            <p className="text-xl leading-relaxed mb-6">
              {chapter.description}
            </p>
            
            <p>
              บทเรียนนี้จะพาคุณเข้าสู่โลกของ {chapter.title} อย่างละเอียดและเข้าใจง่าย 
              พร้อมด้วยตัวอย่างการประยุกต์ใช้ในภาคการเกษตรที่น่าสนใจ
            </p>
            
            <div className="bg-gradient-to-r from-purple-50 to-pink-50 rounded-xl p-6 my-8">
              <h3 className="text-xl font-bold text-gray-900 mb-4">สิ่งที่คุณจะได้เรียนรู้</h3>
              <ul className="space-y-2">
                <li className="flex items-start">
                  <ChevronRight className="w-5 h-5 text-purple-500 mr-2 mt-0.5 flex-shrink-0" />
                  แนวคิดพื้นฐานและหลักการสำคัญ
                </li>
                <li className="flex items-start">
                  <ChevronRight className="w-5 h-5 text-purple-500 mr-2 mt-0.5 flex-shrink-0" />
                  ตัวอย่างการประยุกต์ใช้ในการเกษตร
                </li>
                <li className="flex items-start">
                  <ChevronRight className="w-5 h-5 text-purple-500 mr-2 mt-0.5 flex-shrink-0" />
                  โค้ดตัวอย่างที่สามารถนำไปใช้ได้จริง
                </li>
                <li className="flex items-start">
                  <ChevronRight className="w-5 h-5 text-purple-500 mr-2 mt-0.5 flex-shrink-0" />
                  แผนผังและภาพประกอบที่เข้าใจง่าย
                </li>
              </ul>
            </div>
            
            <p>
              เนื้อหาในบทนี้ได้รับการออกแบบมาเพื่อให้นักเรียนมัธยมศึกษาสามารถเข้าใจและนำไปประยุกต์ใช้ได้จริง 
              พร้อมด้วยกิจกรรมและแบบฝึกหัดที่ช่วยเสริมสร้างความเข้าใจ
            </p>
          </div>
        </motion.div>
        
        {/* Navigation to other chapters */}
        <motion.div
          initial={{ opacity: 0, y: 30 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.6, delay: 0.4 }}
          className="flex justify-between items-center"
        >
          {chapter.id > 1 && (
            <Link
              to={`/chapter/${chapter.id - 1}`}
              className="flex items-center px-6 py-3 bg-white text-gray-700 rounded-xl border border-gray-200 hover:border-purple-300 hover:text-purple-600 transition-all duration-200"
            >
              <ChevronRight className="w-5 h-5 mr-2 rotate-180" />
              บทก่อนหน้า
            </Link>
          )}
          
          {chapter.id < chapters.length && (
            <Link
              to={`/chapter/${chapter.id + 1}`}
              className="flex items-center px-6 py-3 bg-gradient-to-r from-purple-600 to-pink-600 text-white rounded-xl hover:from-purple-700 hover:to-pink-700 transition-all duration-200 ml-auto"
            >
              บทถัดไป
              <ChevronRight className="w-5 h-5 ml-2" />
            </Link>
          )}
        </motion.div>
      </div>
    </div>
  );
};

// Main App Component
function App() {
  const [isMenuOpen, setIsMenuOpen] = useState(false);

  return (
    <Router>
      <div className="min-h-screen bg-white">
        <Navigation isOpen={isMenuOpen} setIsOpen={setIsMenuOpen} />
        
            <Routes>
              <Route path="/" element={<HomePage />} />
              <Route path="/chapters" element={<ChaptersPage />} />
              <Route path="/about" element={<AboutPage />} />
              <Route path="/chapter/:id" element={<EnhancedChapterDetail />} />
            </Routes>
      </div>
    </Router>
  );
}

export default App
