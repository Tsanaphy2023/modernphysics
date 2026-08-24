import React, { useState, useEffect } from 'react';
import { Card, CardContent, CardHeader, CardTitle } from './ui/card';
import { Button } from './ui/button';
import { Progress } from './ui/progress';
import { Badge } from './ui/badge';
import { CheckCircle, XCircle, Clock, Trophy, RotateCcw, BookOpen } from 'lucide-react';

const AdvancedQuizSystem = ({ 
  chapterNumber, 
  questions, 
  onComplete,
  allowRetake = true,
  timeLimit = null 
}) => {
  const [currentQuestion, setCurrentQuestion] = useState(0);
  const [answers, setAnswers] = useState({});
  const [showResults, setShowResults] = useState(false);
  const [timeRemaining, setTimeRemaining] = useState(timeLimit);
  const [quizStarted, setQuizStarted] = useState(false);
  const [quizCompleted, setQuizCompleted] = useState(false);

  // Timer effect
  useEffect(() => {
    if (quizStarted && !quizCompleted && timeLimit && timeRemaining > 0) {
      const timer = setInterval(() => {
        setTimeRemaining(prev => {
          if (prev <= 1) {
            handleSubmitQuiz();
            return 0;
          }
          return prev - 1;
        });
      }, 1000);

      return () => clearInterval(timer);
    }
  }, [quizStarted, quizCompleted, timeRemaining]);

  const formatTime = (seconds) => {
    const mins = Math.floor(seconds / 60);
    const secs = seconds % 60;
    return `${mins}:${secs.toString().padStart(2, '0')}`;
  };

  const handleAnswerChange = (questionId, answer) => {
    setAnswers(prev => ({
      ...prev,
      [questionId]: answer
    }));
  };

  const handleSubmitQuiz = () => {
    setShowResults(true);
    setQuizCompleted(true);
    if (onComplete) {
      const score = calculateScore();
      onComplete(score, answers);
    }
  };

  const calculateScore = () => {
    let correct = 0;
    questions.forEach(q => {
      if (q.type === 'multiple_choice' || q.type === 'true_false') {
        if (answers[q.id] === q.correct) correct++;
      } else if (q.type === 'multiple_select') {
        const userAnswers = answers[q.id] || [];
        const correctAnswers = q.correct;
        if (userAnswers.length === correctAnswers.length && 
            userAnswers.every(ans => correctAnswers.includes(ans))) {
          correct++;
        }
      } else if (q.type === 'fill_blank') {
        const userAnswer = (answers[q.id] || '').toLowerCase().trim();
        const correctAnswer = q.correct.toLowerCase().trim();
        if (userAnswer === correctAnswer) correct++;
      }
    });
    return Math.round((correct / questions.length) * 100);
  };

  const resetQuiz = () => {
    setCurrentQuestion(0);
    setAnswers({});
    setShowResults(false);
    setQuizCompleted(false);
    setQuizStarted(false);
    setTimeRemaining(timeLimit);
  };

  const startQuiz = () => {
    setQuizStarted(true);
    setTimeRemaining(timeLimit);
  };

  const renderQuestion = (question) => {
    switch (question.type) {
      case 'multiple_choice':
        return (
          <div className="space-y-3">
            {question.options.map((option, index) => (
              <label key={index} className="flex items-center space-x-3 cursor-pointer p-3 rounded-lg border hover:bg-gray-50 transition-colors">
                <input
                  type="radio"
                  name={`question-${question.id}`}
                  value={index}
                  checked={answers[question.id] === index}
                  onChange={(e) => handleAnswerChange(question.id, parseInt(e.target.value))}
                  className="text-blue-600"
                />
                <span className="flex-1">{option}</span>
              </label>
            ))}
          </div>
        );

      case 'multiple_select':
        return (
          <div className="space-y-3">
            <p className="text-sm text-gray-600 mb-3">เลือกได้หลายข้อ</p>
            {question.options.map((option, index) => (
              <label key={index} className="flex items-center space-x-3 cursor-pointer p-3 rounded-lg border hover:bg-gray-50 transition-colors">
                <input
                  type="checkbox"
                  value={index}
                  checked={(answers[question.id] || []).includes(index)}
                  onChange={(e) => {
                    const currentAnswers = answers[question.id] || [];
                    if (e.target.checked) {
                      handleAnswerChange(question.id, [...currentAnswers, index]);
                    } else {
                      handleAnswerChange(question.id, currentAnswers.filter(ans => ans !== index));
                    }
                  }}
                  className="text-blue-600"
                />
                <span className="flex-1">{option}</span>
              </label>
            ))}
          </div>
        );

      case 'true_false':
        return (
          <div className="space-y-3">
            {['จริง', 'เท็จ'].map((option, index) => (
              <label key={index} className="flex items-center space-x-3 cursor-pointer p-3 rounded-lg border hover:bg-gray-50 transition-colors">
                <input
                  type="radio"
                  name={`question-${question.id}`}
                  value={index}
                  checked={answers[question.id] === index}
                  onChange={(e) => handleAnswerChange(question.id, parseInt(e.target.value))}
                  className="text-blue-600"
                />
                <span className="flex-1">{option}</span>
              </label>
            ))}
          </div>
        );

      case 'fill_blank':
        return (
          <div className="space-y-3">
            <input
              type="text"
              placeholder="พิมพ์คำตอบของคุณ..."
              value={answers[question.id] || ''}
              onChange={(e) => handleAnswerChange(question.id, e.target.value)}
              className="w-full p-3 border rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500"
            />
          </div>
        );

      case 'drag_drop':
        return (
          <div className="space-y-4">
            <p className="text-sm text-gray-600">ลากและวางคำตอบให้ถูกต้อง</p>
            <div className="grid grid-cols-2 gap-4">
              <div className="space-y-2">
                <h4 className="font-semibold">ตัวเลือก</h4>
                {question.options.map((option, index) => (
                  <div
                    key={index}
                    className="p-2 bg-blue-100 rounded cursor-move border"
                    draggable
                    onDragStart={(e) => e.dataTransfer.setData('text/plain', index)}
                  >
                    {option}
                  </div>
                ))}
              </div>
              <div className="space-y-2">
                <h4 className="font-semibold">ตำแหน่งที่ถูกต้อง</h4>
                {question.dropZones.map((zone, index) => (
                  <div
                    key={index}
                    className="p-4 border-2 border-dashed border-gray-300 rounded min-h-[50px] flex items-center justify-center"
                    onDragOver={(e) => e.preventDefault()}
                    onDrop={(e) => {
                      e.preventDefault();
                      const optionIndex = parseInt(e.dataTransfer.getData('text/plain'));
                      const currentAnswers = answers[question.id] || {};
                      handleAnswerChange(question.id, {
                        ...currentAnswers,
                        [index]: optionIndex
                      });
                    }}
                  >
                    {answers[question.id] && answers[question.id][index] !== undefined
                      ? question.options[answers[question.id][index]]
                      : zone
                    }
                  </div>
                ))}
              </div>
            </div>
          </div>
        );

      default:
        return <div>ประเภทคำถามไม่รองรับ</div>;
    }
  };

  const renderResults = () => {
    const score = calculateScore();
    const correctCount = Math.round((score / 100) * questions.length);

    return (
      <div className="space-y-6">
        <Card className="bg-gradient-to-r from-blue-50 to-green-50">
          <CardHeader className="text-center">
            <div className="flex justify-center mb-4">
              <Trophy className="w-16 h-16 text-yellow-500" />
            </div>
            <CardTitle className="text-3xl">ผลลัพธ์การทดสอบ</CardTitle>
            <div className="text-6xl font-bold text-blue-600 my-4">{score}%</div>
            <p className="text-lg text-gray-600">
              ตอบถูก {correctCount} จาก {questions.length} ข้อ
            </p>
          </CardHeader>
        </Card>

        <div className="space-y-4">
          {questions.map((question, index) => {
            const isCorrect = (() => {
              if (question.type === 'multiple_choice' || question.type === 'true_false') {
                return answers[question.id] === question.correct;
              } else if (question.type === 'multiple_select') {
                const userAnswers = answers[question.id] || [];
                const correctAnswers = question.correct;
                return userAnswers.length === correctAnswers.length && 
                       userAnswers.every(ans => correctAnswers.includes(ans));
              } else if (question.type === 'fill_blank') {
                const userAnswer = (answers[question.id] || '').toLowerCase().trim();
                const correctAnswer = question.correct.toLowerCase().trim();
                return userAnswer === correctAnswer;
              }
              return false;
            })();

            return (
              <Card key={question.id} className={`border-l-4 ${isCorrect ? 'border-l-green-500 bg-green-50' : 'border-l-red-500 bg-red-50'}`}>
                <CardHeader>
                  <div className="flex items-start justify-between">
                    <div className="flex-1">
                      <div className="flex items-center gap-2 mb-2">
                        {isCorrect ? (
                          <CheckCircle className="w-5 h-5 text-green-600" />
                        ) : (
                          <XCircle className="w-5 h-5 text-red-600" />
                        )}
                        <Badge variant={isCorrect ? "success" : "destructive"}>
                          {isCorrect ? 'ถูกต้อง' : 'ไม่ถูกต้อง'}
                        </Badge>
                      </div>
                      <CardTitle className="text-lg">{index + 1}. {question.question}</CardTitle>
                    </div>
                  </div>
                </CardHeader>
                <CardContent>
                  <div className="space-y-3">
                    <div>
                      <p className="font-semibold text-gray-700">คำตอบของคุณ:</p>
                      <p className={isCorrect ? 'text-green-600' : 'text-red-600'}>
                        {(() => {
                          if (question.type === 'multiple_choice') {
                            return answers[question.id] !== undefined ? question.options[answers[question.id]] : 'ไม่ได้ตอบ';
                          } else if (question.type === 'true_false') {
                            return answers[question.id] !== undefined ? (answers[question.id] === 0 ? 'จริง' : 'เท็จ') : 'ไม่ได้ตอบ';
                          } else if (question.type === 'fill_blank') {
                            return answers[question.id] || 'ไม่ได้ตอบ';
                          } else if (question.type === 'multiple_select') {
                            const userAnswers = answers[question.id] || [];
                            return userAnswers.map(idx => question.options[idx]).join(', ') || 'ไม่ได้ตอบ';
                          }
                          return 'ไม่ได้ตอบ';
                        })()}
                      </p>
                    </div>
                    
                    {!isCorrect && (
                      <div>
                        <p className="font-semibold text-gray-700">คำตอบที่ถูกต้อง:</p>
                        <p className="text-green-600">
                          {(() => {
                            if (question.type === 'multiple_choice') {
                              return question.options[question.correct];
                            } else if (question.type === 'true_false') {
                              return question.correct === 0 ? 'จริง' : 'เท็จ';
                            } else if (question.type === 'fill_blank') {
                              return question.correct;
                            } else if (question.type === 'multiple_select') {
                              return question.correct.map(idx => question.options[idx]).join(', ');
                            }
                            return '';
                          })()}
                        </p>
                      </div>
                    )}
                    
                    {question.explanation && (
                      <div className="bg-blue-50 p-3 rounded-lg">
                        <p className="font-semibold text-blue-800">คำอธิบาย:</p>
                        <p className="text-blue-700">{question.explanation}</p>
                      </div>
                    )}
                  </div>
                </CardContent>
              </Card>
            );
          })}
        </div>

        {allowRetake && (
          <div className="flex justify-center gap-4">
            <Button onClick={resetQuiz} variant="outline" className="flex items-center gap-2">
              <RotateCcw className="w-4 h-4" />
              ทำแบบทดสอบใหม่
            </Button>
            <Button className="flex items-center gap-2">
              <BookOpen className="w-4 h-4" />
              ทบทวนเนื้อหา
            </Button>
          </div>
        )}
      </div>
    );
  };

  if (!quizStarted) {
    return (
      <Card>
        <CardHeader className="text-center">
          <CardTitle className="text-2xl">แบบทดสอบบทที่ {chapterNumber}</CardTitle>
          <div className="space-y-4 mt-6">
            <div className="grid grid-cols-1 md:grid-cols-3 gap-4 text-center">
              <div className="p-4 bg-blue-50 rounded-lg">
                <div className="text-2xl font-bold text-blue-600">{questions.length}</div>
                <div className="text-sm text-gray-600">จำนวนข้อ</div>
              </div>
              {timeLimit && (
                <div className="p-4 bg-orange-50 rounded-lg">
                  <div className="text-2xl font-bold text-orange-600">{formatTime(timeLimit)}</div>
                  <div className="text-sm text-gray-600">เวลาที่กำหนด</div>
                </div>
              )}
              <div className="p-4 bg-green-50 rounded-lg">
                <div className="text-2xl font-bold text-green-600">70%</div>
                <div className="text-sm text-gray-600">คะแนนผ่าน</div>
              </div>
            </div>
            
            <div className="bg-yellow-50 p-4 rounded-lg">
              <h3 className="font-semibold text-yellow-800 mb-2">คำแนะนำ:</h3>
              <ul className="text-sm text-yellow-700 space-y-1">
                <li>• อ่านคำถามให้ละเอียดก่อนตอบ</li>
                <li>• สามารถย้อนกลับไปแก้ไขคำตอบได้</li>
                {timeLimit && <li>• ระวังเวลาที่กำหนด</li>}
                <li>• คลิก "ส่งคำตอบ" เมื่อทำเสร็จแล้ว</li>
              </ul>
            </div>
          </div>
        </CardHeader>
        <CardContent className="text-center">
          <Button onClick={startQuiz} size="lg" className="px-8">
            เริ่มทำแบบทดสอบ
          </Button>
        </CardContent>
      </Card>
    );
  }

  if (showResults) {
    return renderResults();
  }

  const progress = ((currentQuestion + 1) / questions.length) * 100;
  const question = questions[currentQuestion];

  return (
    <div className="space-y-6">
      {/* Header with progress and timer */}
      <Card>
        <CardHeader>
          <div className="flex justify-between items-center">
            <div>
              <CardTitle>แบบทดสอบบทที่ {chapterNumber}</CardTitle>
              <p className="text-gray-600">ข้อ {currentQuestion + 1} จาก {questions.length}</p>
            </div>
            {timeLimit && (
              <div className="flex items-center gap-2">
                <Clock className="w-5 h-5 text-orange-500" />
                <span className={`font-mono text-lg ${timeRemaining < 60 ? 'text-red-600' : 'text-orange-600'}`}>
                  {formatTime(timeRemaining)}
                </span>
              </div>
            )}
          </div>
          <Progress value={progress} className="mt-4" />
        </CardHeader>
      </Card>

      {/* Question */}
      <Card>
        <CardHeader>
          <div className="flex items-start gap-3">
            <Badge variant="outline">{question.type === 'multiple_choice' ? 'เลือกตอบ' : 
                                   question.type === 'multiple_select' ? 'เลือกหลายข้อ' :
                                   question.type === 'true_false' ? 'จริง/เท็จ' :
                                   question.type === 'fill_blank' ? 'เติมคำ' :
                                   question.type === 'drag_drop' ? 'ลาก-วาง' : 'อื่นๆ'}</Badge>
            <CardTitle className="flex-1">{question.question}</CardTitle>
          </div>
          {question.image && (
            <div className="mt-4">
              <img src={question.image} alt="Question illustration" className="max-w-full h-auto rounded-lg" />
            </div>
          )}
        </CardHeader>
        <CardContent>
          {renderQuestion(question)}
        </CardContent>
      </Card>

      {/* Navigation */}
      <div className="flex justify-between">
        <Button
          variant="outline"
          onClick={() => setCurrentQuestion(prev => Math.max(0, prev - 1))}
          disabled={currentQuestion === 0}
        >
          ข้อก่อนหน้า
        </Button>

        <div className="flex gap-2">
          {currentQuestion < questions.length - 1 ? (
            <Button
              onClick={() => setCurrentQuestion(prev => Math.min(questions.length - 1, prev + 1))}
            >
              ข้อถัดไป
            </Button>
          ) : (
            <Button onClick={handleSubmitQuiz} className="bg-green-600 hover:bg-green-700">
              ส่งคำตอบ
            </Button>
          )}
        </div>
      </div>

      {/* Question navigation dots */}
      <div className="flex justify-center gap-2 flex-wrap">
        {questions.map((_, index) => (
          <button
            key={index}
            onClick={() => setCurrentQuestion(index)}
            className={`w-8 h-8 rounded-full text-sm font-medium transition-colors ${
              index === currentQuestion
                ? 'bg-blue-600 text-white'
                : answers[questions[index].id] !== undefined
                ? 'bg-green-100 text-green-700 border border-green-300'
                : 'bg-gray-100 text-gray-600 border border-gray-300'
            }`}
          >
            {index + 1}
          </button>
        ))}
      </div>
    </div>
  );
};

export default AdvancedQuizSystem;
