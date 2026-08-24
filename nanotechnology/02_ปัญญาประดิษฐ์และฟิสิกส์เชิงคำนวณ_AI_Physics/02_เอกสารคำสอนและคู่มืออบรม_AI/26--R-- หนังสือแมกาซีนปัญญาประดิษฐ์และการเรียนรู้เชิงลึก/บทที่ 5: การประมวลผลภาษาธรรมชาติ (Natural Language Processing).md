# บทที่ 5: การประมวลผลภาษาธรรมชาติ (Natural Language Processing)

## 5.1 บทนำสู่ Natural Language Processing

### ความหมายและความสำคัญ

Natural Language Processing (NLP) คือสาขาหนึ่งของปัญญาประดิษฐ์ที่เน้นการสร้างความเข้าใจระหว่างคอมพิวเตอร์และภาษาของมนุษย์ โดยเป็นการผสมผสานระหว่างวิทยาการคอมพิวเตอร์ ปัญญาประดิษฐ์ และภาษาศาสตร์

**ทำไม NLP จึงสำคัญ?**
- ข้อมูลส่วนใหญ่ในโลกอยู่ในรูปแบบข้อความ (80% ของข้อมูลองค์กร)
- ช่วยให้คอมพิวเตอร์เข้าใจและตอบสนองต่อภาษามนุษย์
- เป็นพื้นฐานของ AI Assistant, Chatbot, และระบบแปลภาษา
- สำคัญในการวิเคราะห์ความรู้สึก (Sentiment Analysis)

### ความท้าทายของภาษาธรรมชาติ

**1. ความคลุมเครือ (Ambiguity)**
- คำเดียวกันมีความหมายหลายแบบ
- ตัวอย่าง: "ไก่" อาจหมายถึง สัตว์ หรือ อาหาร

**2. บริบท (Context)**
- ความหมายเปลี่ยนตามบริบท
- ตัวอย่าง: "เย็น" ในประโยค "อากาศเย็น" vs "น้ำเย็น"

**3. การใช้ภาษาอย่างสร้างสรรค์**
- สำนวน คำเปรียบเทียบ การเล่นคำ
- ภาษาท้องถิ่น และ slang

**4. ไวยากรณ์ที่ซับซ้อน**
- โครงสร้างประโยคที่หลากหลาย
- การใช้คำที่ไม่เป็นไปตามกฎ

## 5.2 องค์ประกอบพื้นฐานของ NLP

### 5.2.1 การประมวลผลระดับคำ (Word Level Processing)

**Tokenization**
การแบ่งข้อความเป็นหน่วยย่อยๆ (tokens)

```python
# ตัวอย่าง Tokenization
text = "การเกษตรอัจฉริยะใช้ AI ช่วยเพิ่มผลผลิต"
tokens = text.split()
print(tokens)
# Output: ['การเกษตรอัจฉริยะใช้', 'AI', 'ช่วยเพิ่มผลผลิต']

# สำหรับภาษาไทยต้องใช้เครื่องมือพิเศษ
import pythainlp
tokens = pythainlp.word_tokenize(text)
print(tokens)
# Output: ['การเกษตร', 'อัจฉริยะ', 'ใช้', 'AI', 'ช่วย', 'เพิ่ม', 'ผลผลิต']
```

**Stop Words Removal**
การกำจัดคำที่ไม่มีความหมายสำคัญ

```python
stop_words = ['และ', 'หรือ', 'แต่', 'ใน', 'บน', 'ที่', 'เป็น']
filtered_tokens = [word for word in tokens if word not in stop_words]
```

**Stemming และ Lemmatization**
การลดคำให้เหลือรากศัพท์

```python
# ตัวอย่าง Stemming (ภาษาอังกฤษ)
from nltk.stem import PorterStemmer
stemmer = PorterStemmer()
print(stemmer.stem("running"))  # run
print(stemmer.stem("better"))   # better
```

### 5.2.2 การแทนค่าคำด้วยตัวเลข (Word Representation)

**Bag of Words (BoW)**
```python
from sklearn.feature_extraction.text import CountVectorizer

documents = [
    "ข้าวโพดให้ผลผลิตดี",
    "ข้าวโพดต้องการน้ำมาก", 
    "ผลผลิตข้าวโพดเพิ่มขึ้น"
]

vectorizer = CountVectorizer()
bow_matrix = vectorizer.fit_transform(documents)
print(vectorizer.get_feature_names_out())
print(bow_matrix.toarray())
```

**TF-IDF (Term Frequency-Inverse Document Frequency)**
```python
from sklearn.feature_extraction.text import TfidfVectorizer

tfidf_vectorizer = TfidfVectorizer()
tfidf_matrix = tfidf_vectorizer.fit_transform(documents)
print(tfidf_matrix.toarray())
```

**Word Embeddings (Word2Vec, GloVe)**
```python
# ตัวอย่างการใช้ Word2Vec
from gensim.models import Word2Vec

# ข้อมูลตัวอย่าง
sentences = [
    ['ข้าวโพด', 'ให้', 'ผลผลิต', 'ดี'],
    ['ข้าวโพด', 'ต้องการ', 'น้ำ', 'มาก'],
    ['ผลผลิต', 'ข้าวโพด', 'เพิ่มขึ้น']
]

# สร้างโมเดล Word2Vec
model = Word2Vec(sentences, vector_size=100, window=5, min_count=1, workers=4)

# หาคำที่คล้ายกัน
similar_words = model.wv.most_similar('ข้าวโพด', topn=3)
print(similar_words)
```

## 5.3 เทคนิค NLP ขั้นสูง

### 5.3.1 Named Entity Recognition (NER)

การระบุและจำแนกเอนทิตี้ในข้อความ เช่น ชื่อคน สถานที่ องค์กร วันที่

```python
import spacy

# โหลดโมเดลภาษาไทย
nlp = spacy.load("th_core_news_sm")

text = "บริษัท เซียร์ส อะโกร จำกัด ตั้งอยู่ที่จังหวัดนครปฐม เริ่มปลูกข้าวโพดเมื่อปี 2020"
doc = nlp(text)

for ent in doc.ents:
    print(f"{ent.text} -> {ent.label_}")
```

### 5.3.2 Part-of-Speech Tagging (POS)

การระบุหน้าที่ทางไวยากรณ์ของคำ

```python
import pythainlp

text = "เกษตรกรปลูกข้าวในนาอย่างขยันขันแข็ง"
pos_tags = pythainlp.tag.pos_tag(text)
print(pos_tags)
# Output: [('เกษตรกร', 'NOUN'), ('ปลูก', 'VERB'), ('ข้าว', 'NOUN'), ...]
```

### 5.3.3 Sentiment Analysis

การวิเคราะห์ความรู้สึกหรือทัศนคติในข้อความ

```python
from textblob import TextBlob
from googletrans import Translator

# แปลเป็นภาษาอังกฤษก่อน (เพื่อใช้ TextBlob)
translator = Translator()
thai_text = "ผลผลิตปีนี้ดีมาก เกษตรกรมีความสุข"
english_text = translator.translate(thai_text, dest='en').text

# วิเคราะห์ความรู้สึก
blob = TextBlob(english_text)
sentiment = blob.sentiment

print(f"Polarity: {sentiment.polarity}")  # -1 (negative) to 1 (positive)
print(f"Subjectivity: {sentiment.subjectivity}")  # 0 (objective) to 1 (subjective)
```

### 5.3.4 Text Classification

การจำแนกประเภทข้อความ

```python
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer

# ข้อมูลตัวอย่าง
texts = [
    "ข้าวโพดเก็บเกี่ยวแล้ว ผลผลิตดี",
    "ฝนตกหนัก พืชผลเสียหาย", 
    "ใช้ปุ๋ยใหม่ ต้นข้าวโตดี",
    "แมลงศัตรูพืชระบาด ผลผลิตลดลง",
    "เทคโนโลยีใหม่ช่วยเพิ่มผลผลิต",
    "ภัยแล้งทำให้พืชแห้งตาย"
]

labels = ['positive', 'negative', 'positive', 'negative', 'positive', 'negative']

# สร้าง pipeline
pipeline = Pipeline([
    ('tfidf', TfidfVectorizer()),
    ('classifier', MultinomialNB())
])

# แบ่งข้อมูล
X_train, X_test, y_train, y_test = train_test_split(texts, labels, test_size=0.3, random_state=42)

# ฝึกโมเดล
pipeline.fit(X_train, y_train)

# ทดสอบ
test_text = "เกษตรกรมีความสุขกับผลผลิตปีนี้"
prediction = pipeline.predict([test_text])
print(f"ข้อความ: {test_text}")
print(f"ผลการทำนาย: {prediction[0]}")
```

## 5.4 การประยุกต์ใช้ NLP ในการเกษตร

### 5.4.1 ระบบแนะนำการเกษตรอัจฉริยะ

**Smart Farming Assistant Chatbot**

```python
import re
from datetime import datetime

class AgricultureChatbot:
    def __init__(self):
        self.knowledge_base = {
            'ข้าวโพด': {
                'ปลูก': 'ปลูกข้าวโพดควรเลือกพันธุ์ที่เหมาะกับสภาพดิน ปลูกในช่วงต้นฤดูฝน',
                'ปุ๋ย': 'ใช้ปุ๋ยคอก 2-3 ตัน/ไร่ ปุ๋ยเคมี 15-15-15 อัตรา 1 ถุง/ไร่',
                'โรค': 'โรคใบไหม้ ใช้ยาฆ่าเชื้อรา โรคใบจุด ฉีดยาป้องกัน',
                'เก็บเกี่ยว': 'เก็บเกี่ยวเมื่ออายุ 90-120 วัน เมล็ดแห้งแกร่ง'
            },
            'ข้าว': {
                'ปลูก': 'ปลูกข้าวในนาน้ำ เตรียมดินให้ละเอียด ใส่ปุ๋ยคอก',
                'น้ำ': 'รักษาระดับน้ำ 3-5 ซม. ในช่วงแรก เพิ่มเป็น 10 ซม. ตอนข้าวโต',
                'ปุ๋ย': 'ใส่ปุ๋ยยูเรีย 3 ครั้ง ครั้งละ 1 ถุง/ไร่',
                'โรค': 'โรคไหม้ใบ โรคใบจุดสีน้ำตาล ใช้ยาฆ่าเชื้อราป้องกัน'
            }
        }
        
        self.weather_advice = {
            'ฝน': 'ระวังโรคเชื้อรา เพิ่มการระบายน้ำ',
            'แล้ง': 'รดน้ำเพิ่ม ใช้วัสดุคลุมดิน',
            'ร้อน': 'รดน้ำช่วงเย็น หลีกเลี่ยงการทำงานกลางวัน'
        }
    
    def process_question(self, question):
        """ประมวลผลคำถามและให้คำตอบ"""
        question = question.lower()
        
        # ระบุพืชผล
        crop = None
        for crop_name in self.knowledge_base.keys():
            if crop_name in question:
                crop = crop_name
                break
        
        if not crop:
            return "กรุณาระบุชื่อพืชผลที่ต้องการสอบถาม เช่น ข้าวโพด หรือ ข้าว"
        
        # ระบุหัวข้อ
        topic = None
        crop_info = self.knowledge_base[crop]
        
        for topic_name in crop_info.keys():
            if topic_name in question:
                topic = topic_name
                break
        
        if topic:
            return f"เกี่ยวกับ{topic}ของ{crop}: {crop_info[topic]}"
        else:
            # ให้ข้อมูลทั่วไป
            info = f"ข้อมูลเกี่ยวกับ{crop}:\n"
            for key, value in crop_info.items():
                info += f"- {key}: {value}\n"
            return info
    
    def get_weather_advice(self, weather_condition):
        """ให้คำแนะนำตามสภาพอากาศ"""
        return self.weather_advice.get(weather_condition, "ไม่มีข้อมูลสำหรับสภาพอากาศนี้")

# ตัวอย่างการใช้งาน
chatbot = AgricultureChatbot()

questions = [
    "วิธีปลูกข้าวโพดยังไง",
    "ข้าวโพดใส่ปุ๋ยอะไร",
    "ข้าวเป็นโรคใบไหม้ทำยังไง",
    "เก็บเกี่ยวข้าวโพดเมื่อไหร่"
]

for q in questions:
    print(f"คำถาม: {q}")
    print(f"คำตอบ: {chatbot.process_question(q)}")
    print("-" * 50)
```

### 5.4.2 การวิเคราะห์ข้อมูลจากโซเชียลมีเดีย

**Social Media Sentiment Analysis for Agriculture**

```python
import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter

class AgriculturalSentimentAnalyzer:
    def __init__(self):
        self.positive_words = [
            'ดี', 'เยี่ยม', 'สุดยอด', 'ประสบความสำเร็จ', 'เพิ่มขึ้น', 
            'กำไร', 'คุณภาพสูง', 'สด', 'อร่อย', 'สวยงาม'
        ]
        
        self.negative_words = [
            'แย่', 'เสียหาย', 'ลดลง', 'ขาดทุน', 'เน่า', 'แห้งตาย',
            'โรค', 'ศัตรูพืช', 'ปัญหา', 'ยาก', 'ล้มเหลว'
        ]
        
        self.crop_keywords = {
            'ข้าว': ['ข้าว', 'นา', 'ข้าวหอมมะลิ', 'ข้าวเหนียว'],
            'ข้าวโพด': ['ข้าวโพด', 'ข้าวโพดหวาน', 'ข้าวโพดฟักทอง'],
            'มันสำปะหลัง': ['มันสำปะหลัง', 'มัน', 'แป้งมัน'],
            'อ้อย': ['อ้อย', 'น้ำตาลทราย']
        }
    
    def analyze_sentiment(self, text):
        """วิเคราะห์ความรู้สึกในข้อความ"""
        text = text.lower()
        
        positive_count = sum(1 for word in self.positive_words if word in text)
        negative_count = sum(1 for word in self.negative_words if word in text)
        
        if positive_count > negative_count:
            return 'positive'
        elif negative_count > positive_count:
            return 'negative'
        else:
            return 'neutral'
    
    def identify_crop(self, text):
        """ระบุพืชผลในข้อความ"""
        text = text.lower()
        
        for crop, keywords in self.crop_keywords.items():
            if any(keyword in text for keyword in keywords):
                return crop
        
        return 'other'
    
    def analyze_posts(self, posts):
        """วิเคราะห์โพสต์หลายๆ โพสต์"""
        results = []
        
        for post in posts:
            sentiment = self.analyze_sentiment(post)
            crop = self.identify_crop(post)
            
            results.append({
                'post': post,
                'sentiment': sentiment,
                'crop': crop
            })
        
        return results
    
    def generate_report(self, results):
        """สร้างรายงานการวิเคราะห์"""
        df = pd.DataFrame(results)
        
        # สถิติความรู้สึกโดยรวม
        sentiment_counts = df['sentiment'].value_counts()
        
        # สถิติตามพืชผล
        crop_sentiment = df.groupby(['crop', 'sentiment']).size().unstack(fill_value=0)
        
        return {
            'total_posts': len(results),
            'sentiment_distribution': sentiment_counts.to_dict(),
            'crop_sentiment': crop_sentiment.to_dict()
        }

# ตัวอย่างการใช้งาน
analyzer = AgriculturalSentimentAnalyzer()

# ข้อมูลโพสต์ตัวอย่าง
sample_posts = [
    "ปีนี้ข้าวโพดให้ผลผลิตดีมาก เกษตรกรมีความสุข",
    "ฝนตกหนัก ข้าวในนาเสียหายมาก",
    "ใช้เทคโนโลยีใหม่ปลูกมันสำปะหลัง ผลผลิตเพิ่มขึ้น 30%",
    "ราคาอ้อยตกต่ำ เกษตรกรขาดทุน",
    "โครงการส่งเสริมการเกษตรอัจฉริยะ ช่วยเกษตรกรได้มาก",
    "แมลงศัตรูพืชระบาด ข้าวโพดเสียหายหนัก"
]

# วิเคราะห์
results = analyzer.analyze_posts(sample_posts)
report = analyzer.generate_report(results)

print("=== รายงานการวิเคราะห์ความรู้สึก ===")
print(f"จำนวนโพสต์ทั้งหมด: {report['total_posts']}")
print(f"การกระจายความรู้สึก: {report['sentiment_distribution']}")
print(f"ความรู้สึกตามพืชผล: {report['crop_sentiment']}")
```

### 5.4.3 ระบบแปลภาษาสำหรับเกษตรกร

**Agricultural Translation System**

```python
from googletrans import Translator
import json

class AgriculturalTranslator:
    def __init__(self):
        self.translator = Translator()
        
        # พจนานุกรมศัพท์เกษตรพิเศษ
        self.agriculture_dict = {
            'en_to_th': {
                'fertilizer': 'ปุ๋ย',
                'pesticide': 'ยาฆ่าแมลง',
                'irrigation': 'การชลประทาน',
                'harvest': 'การเก็บเกี่ยว',
                'crop rotation': 'การหมุนเวียนพืชผล',
                'organic farming': 'เกษตรอินทรีย์',
                'greenhouse': 'โรงเรือน',
                'soil pH': 'ความเป็นกรด-ด่างของดิน',
                'nitrogen': 'ไนโตรเจน',
                'phosphorus': 'ฟอสฟอรัส',
                'potassium': 'โพแทสเซียม'
            },
            'th_to_en': {
                'ปุ๋ย': 'fertilizer',
                'ยาฆ่าแมลง': 'pesticide',
                'การชลประทาน': 'irrigation',
                'การเก็บเกี่ยว': 'harvest',
                'การหมุนเวียนพืชผล': 'crop rotation',
                'เกษตรอินทรีย์': 'organic farming',
                'โรงเรือน': 'greenhouse',
                'ความเป็นกรด-ด่างของดิน': 'soil pH',
                'ไนโตรเจน': 'nitrogen',
                'ฟอสฟอรัส': 'phosphorus',
                'โพแทสเซียม': 'potassium'
            }
        }
    
    def translate_with_context(self, text, source_lang, target_lang):
        """แปลภาษาพร้อมบริบทเกษตร"""
        
        # ตรวจสอบศัพท์เฉพาะทางก่อน
        dict_key = f"{source_lang}_to_{target_lang}"
        if dict_key in self.agriculture_dict:
            for term, translation in self.agriculture_dict[dict_key].items():
                if term.lower() in text.lower():
                    text = text.replace(term, f"[{translation}]")
        
        # แปลด้วย Google Translate
        try:
            result = self.translator.translate(text, src=source_lang, dest=target_lang)
            translated_text = result.text
            
            # แทนที่ศัพท์เฉพาะทางกลับ
            translated_text = translated_text.replace('[', '').replace(']', '')
            
            return {
                'original': text,
                'translated': translated_text,
                'source_lang': source_lang,
                'target_lang': target_lang,
                'confidence': result.extra_data.get('confidence', 0)
            }
        
        except Exception as e:
            return {
                'error': str(e),
                'original': text
            }
    
    def batch_translate(self, texts, source_lang, target_lang):
        """แปลข้อความหลายๆ ข้อความ"""
        results = []
        
        for text in texts:
            result = self.translate_with_context(text, source_lang, target_lang)
            results.append(result)
        
        return results

# ตัวอย่างการใช้งาน
translator = AgriculturalTranslator()

# ข้อความตัวอย่าง
texts_en = [
    "Apply fertilizer to increase crop yield",
    "Use organic farming methods for better soil health", 
    "Monitor soil pH levels regularly",
    "Harvest crops when they reach maturity"
]

texts_th = [
    "ใช้ปุ๋ยเพื่อเพิ่มผลผลิต",
    "ใช้วิธีเกษตรอินทรีย์เพื่อสุขภาพดินที่ดี",
    "ตรวจสอบระดับความเป็นกรด-ด่างของดินอย่างสม่ำเสมอ",
    "เก็บเกี่ยวพืชผลเมื่อสุกแก่แล้ว"
]

print("=== การแปลจากอังกฤษเป็นไทย ===")
en_to_th_results = translator.batch_translate(texts_en, 'en', 'th')
for result in en_to_th_results:
    if 'error' not in result:
        print(f"EN: {result['original']}")
        print(f"TH: {result['translated']}")
        print("-" * 50)

print("\n=== การแปลจากไทยเป็นอังกฤษ ===")
th_to_en_results = translator.batch_translate(texts_th, 'th', 'en')
for result in th_to_en_results:
    if 'error' not in result:
        print(f"TH: {result['original']}")
        print(f"EN: {result['translated']}")
        print("-" * 50)
```

## 5.5 โครงการปฏิบัติ: ระบบวิเคราะห์ข้อมูลข่าวเกษตร

### 5.5.1 วัตถุประสงค์โครงการ

สร้างระบบที่สามารถ:
1. รวบรวมข่าวเกษตรจากแหล่งต่างๆ
2. วิเคราะห์ความรู้สึกและแนวโน้ม
3. สกัดข้อมูลสำคัญ (ราคา, ผลผลิต, นโยบาย)
4. สร้างรายงานสรุปอัตโนมัติ

### 5.5.2 การออกแบบระบบ

```python
import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime, timedelta
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud
import re

class AgriculturalNewsAnalyzer:
    def __init__(self):
        self.news_sources = {
            'กรมส่งเสริมการเกษตร': 'https://www.doae.go.th',
            'กรมการข้าว': 'https://www.ricedept.go.th',
            'สำนักข่าวเกษตร': 'https://www.agriculture-news.com'
        }
        
        self.price_patterns = [
            r'ราคา[\s]*([ก-๙]+)[\s]*([0-9,]+)[\s]*บาท',
            r'([ก-๙]+)[\s]*ราคา[\s]*([0-9,]+)',
            r'([0-9,]+)[\s]*บาท[\s]*ต่อ[\s]*([ก-๙]+)'
        ]
        
        self.crop_keywords = [
            'ข้าว', 'ข้าวโพด', 'มันสำปะหลัง', 'อ้อย', 'ยางพารา',
            'ปาล์มน้ำมัน', 'ถั่วเหลือง', 'มะม่วง', 'ทุเรียน', 'ลิ้นจี่'
        ]
    
    def scrape_news(self, url, max_articles=10):
        """ดึงข่าวจากเว็บไซต์"""
        try:
            response = requests.get(url, timeout=10)
            soup = BeautifulSoup(response.content, 'html.parser')
            
            # หา articles (ปรับตาม structure ของแต่ละเว็บ)
            articles = soup.find_all(['article', 'div'], class_=['news-item', 'article', 'post'])
            
            news_data = []
            for i, article in enumerate(articles[:max_articles]):
                title = article.find(['h1', 'h2', 'h3', 'a'])
                content = article.find(['p', 'div'], class_=['content', 'summary', 'excerpt'])
                date = article.find(['time', 'span'], class_=['date', 'published'])
                
                if title:
                    news_data.append({
                        'title': title.get_text().strip(),
                        'content': content.get_text().strip() if content else '',
                        'date': date.get_text().strip() if date else datetime.now().strftime('%Y-%m-%d'),
                        'source': url
                    })
            
            return news_data
            
        except Exception as e:
            print(f"Error scraping {url}: {e}")
            return []
    
    def extract_prices(self, text):
        """สกัดข้อมูลราคาจากข้อความ"""
        prices = {}
        
        for pattern in self.price_patterns:
            matches = re.findall(pattern, text)
            for match in matches:
                if len(match) == 2:
                    crop, price = match
                    # ทำความสะอาดข้อมูล
                    price = re.sub(r'[,\s]', '', price)
                    if price.isdigit():
                        prices[crop.strip()] = int(price)
        
        return prices
    
    def analyze_trends(self, news_data):
        """วิเคราะห์แนวโน้มจากข่าว"""
        df = pd.DataFrame(news_data)
        
        # นับความถี่ของพืชผลในข่าว
        crop_mentions = {}
        for crop in self.crop_keywords:
            count = df['title'].str.contains(crop, case=False).sum()
            count += df['content'].str.contains(crop, case=False).sum()
            if count > 0:
                crop_mentions[crop] = count
        
        # วิเคราะห์ความรู้สึก (ใช้คำสำคัญ)
        positive_keywords = ['เพิ่ม', 'ดี', 'สูง', 'ประสบความสำเร็จ', 'กำไร']
        negative_keywords = ['ลด', 'ตก', 'เสียหาย', 'ปัญหา', 'ขาดทุน']
        
        sentiment_scores = []
        for _, row in df.iterrows():
            text = (row['title'] + ' ' + row['content']).lower()
            
            positive_count = sum(1 for word in positive_keywords if word in text)
            negative_count = sum(1 for word in negative_keywords if word in text)
            
            if positive_count > negative_count:
                sentiment_scores.append(1)
            elif negative_count > positive_count:
                sentiment_scores.append(-1)
            else:
                sentiment_scores.append(0)
        
        df['sentiment'] = sentiment_scores
        
        return {
            'crop_mentions': crop_mentions,
            'sentiment_distribution': pd.Series(sentiment_scores).value_counts().to_dict(),
            'daily_sentiment': df.groupby('date')['sentiment'].mean().to_dict()
        }
    
    def generate_wordcloud(self, news_data, output_path='agriculture_wordcloud.png'):
        """สร้าง Word Cloud จากข่าว"""
        all_text = ' '.join([item['title'] + ' ' + item['content'] for item in news_data])
        
        # กรองคำไทย
        thai_text = re.sub(r'[^\u0E00-\u0E7Fa-zA-Z\s]', '', all_text)
        
        wordcloud = WordCloud(
            font_path='NotoSansThai-Regular.ttf',  # ต้องมี font ภาษาไทย
            width=800, 
            height=400,
            background_color='white',
            max_words=100,
            colormap='viridis'
        ).generate(thai_text)
        
        plt.figure(figsize=(12, 6))
        plt.imshow(wordcloud, interpolation='bilinear')
        plt.axis('off')
        plt.title('คำที่ปรากฏบ่อยในข่าวเกษตร', fontsize=16, fontweight='bold')
        plt.tight_layout()
        plt.savefig(output_path, dpi=300, bbox_inches='tight')
        plt.show()
    
    def create_dashboard(self, analysis_results):
        """สร้าง Dashboard แสดงผล"""
        fig, axes = plt.subplots(2, 2, figsize=(15, 12))
        fig.suptitle('Dashboard การวิเคราะห์ข่าวเกษตร', fontsize=16, fontweight='bold')
        
        # 1. กราฟความถี่พืชผลในข่าว
        crop_data = analysis_results['crop_mentions']
        if crop_data:
            crops = list(crop_data.keys())
            counts = list(crop_data.values())
            
            axes[0, 0].bar(crops, counts, color='skyblue', alpha=0.7)
            axes[0, 0].set_title('ความถี่พืชผลในข่าว')
            axes[0, 0].set_xlabel('พืชผล')
            axes[0, 0].set_ylabel('จำนวนครั้งที่ปรากฏ')
            axes[0, 0].tick_params(axis='x', rotation=45)
        
        # 2. การกระจายความรู้สึก
        sentiment_data = analysis_results['sentiment_distribution']
        sentiment_labels = {-1: 'Negative', 0: 'Neutral', 1: 'Positive'}
        
        labels = [sentiment_labels[k] for k in sentiment_data.keys()]
        sizes = list(sentiment_data.values())
        colors = ['red', 'gray', 'green']
        
        axes[0, 1].pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90)
        axes[0, 1].set_title('การกระจายความรู้สึกในข่าว')
        
        # 3. แนวโน้มความรู้สึกรายวัน
        daily_sentiment = analysis_results['daily_sentiment']
        if daily_sentiment:
            dates = list(daily_sentiment.keys())
            sentiments = list(daily_sentiment.values())
            
            axes[1, 0].plot(dates, sentiments, marker='o', linewidth=2, markersize=6)
            axes[1, 0].set_title('แนวโน้มความรู้สึกรายวัน')
            axes[1, 0].set_xlabel('วันที่')
            axes[1, 0].set_ylabel('คะแนนความรู้สึกเฉลี่ย')
            axes[1, 0].tick_params(axis='x', rotation=45)
            axes[1, 0].grid(True, alpha=0.3)
        
        # 4. สถิติสรุป
        axes[1, 1].axis('off')
        summary_text = f"""
        สถิติสรุป:
        
        • จำนวนข่าวทั้งหมด: {sum(sentiment_data.values())}
        • พืชผลที่ถูกพูดถึงมากที่สุด: {max(crop_data.keys(), key=crop_data.get) if crop_data else 'ไม่มีข้อมูล'}
        • ความรู้สึกโดยรวม: {'Positive' if sentiment_data.get(1, 0) > sentiment_data.get(-1, 0) else 'Negative' if sentiment_data.get(-1, 0) > sentiment_data.get(1, 0) else 'Neutral'}
        
        แนวโน้ม:
        • ข่าวเชิงบวก: {sentiment_data.get(1, 0)} ข่าว
        • ข่าวเชิงลบ: {sentiment_data.get(-1, 0)} ข่าว
        • ข่าวเป็นกลาง: {sentiment_data.get(0, 0)} ข่าว
        """
        
        axes[1, 1].text(0.1, 0.9, summary_text, transform=axes[1, 1].transAxes,
                       fontsize=12, verticalalignment='top',
                       bbox=dict(boxstyle="round,pad=0.5", facecolor='lightblue', alpha=0.7))
        
        plt.tight_layout()
        plt.show()

# ตัวอย่างการใช้งาน
def run_news_analysis():
    analyzer = AgriculturalNewsAnalyzer()
    
    # สร้างข้อมูลตัวอย่าง (ในการใช้งานจริงจะดึงจากเว็บไซต์)
    sample_news = [
        {
            'title': 'ราคาข้าวโพดเพิ่มขึ้น 15 บาทต่อกิโลกรัม',
            'content': 'เกษตรกรมีความสุขกับราคาข้าวโพดที่สูงขึ้น ผลผลิตปีนี้ดีมาก',
            'date': '2024-01-15',
            'source': 'agriculture-news.com'
        },
        {
            'title': 'ฝนตกหนัก ข้าวในภาคเหนือเสียหาย',
            'content': 'เกษตรกรเดือดร้อน ข้าวเสียหายจากน้ำท่วม คาดผลผลิตลดลง 20%',
            'date': '2024-01-16',
            'source': 'doae.go.th'
        },
        {
            'title': 'โครงการเกษตรอัจฉริยะ ช่วยเพิ่มผลผลิตมันสำปะหลัง',
            'content': 'เทคโนโลยี AI ช่วยเกษตรกร ผลผลิตมันสำปะหลังเพิ่มขึ้น 30%',
            'date': '2024-01-17',
            'source': 'ricedept.go.th'
        }
    ]
    
    # วิเคราะห์
    results = analyzer.analyze_trends(sample_news)
    
    # แสดงผล
    analyzer.create_dashboard(results)
    
    # สร้าง Word Cloud (ถ้ามี font ภาษาไทย)
    try:
        analyzer.generate_wordcloud(sample_news)
    except:
        print("ไม่สามารถสร้าง Word Cloud ได้ (ต้องมี font ภาษาไทย)")

if __name__ == "__main__":
    run_news_analysis()
```

## 5.6 เครื่องมือและไลบรารี่สำหรับ NLP

### 5.6.1 ไลบรารี่ภาษาไทย

**PyThaiNLP**
```bash
pip install pythainlp
```

```python
import pythainlp

# Word Tokenization
text = "เกษตรอัจฉริยะใช้ปัญญาประดิษฐ์"
tokens = pythainlp.word_tokenize(text)
print(tokens)

# POS Tagging
pos_tags = pythainlp.tag.pos_tag(text)
print(pos_tags)

# Named Entity Recognition
ner_tags = pythainlp.tag.named_entity.ThaiNameTagger()
entities = ner_tags.get_ner(text)
print(entities)
```

### 5.6.2 ไลบรารี่สากล

**NLTK (Natural Language Toolkit)**
```python
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

# Download required data
nltk.download('vader_lexicon')

# Sentiment Analysis
sia = SentimentIntensityAnalyzer()
text = "The crop yield is excellent this year"
scores = sia.polarity_scores(text)
print(scores)
```

**spaCy**
```python
import spacy

# Load English model
nlp = spacy.load("en_core_web_sm")

text = "Farmers in Thailand grow rice and corn"
doc = nlp(text)

# Named Entity Recognition
for ent in doc.ents:
    print(f"{ent.text} -> {ent.label_}")

# Part-of-speech tagging
for token in doc:
    print(f"{token.text} -> {token.pos_}")
```

## 5.7 ความท้าทายและแนวทางแก้ไข

### 5.7.1 ความท้าทายในการประมวลผลภาษาไทย

**1. การตัดคำ (Word Segmentation)**
- ภาษาไทยไม่มีช่องว่างระหว่างคำ
- แก้ไข: ใช้ PyThaiNLP หรือ DeepCut

**2. ความคลุมเครือของคำ**
- คำเดียวกันมีความหมายหลายแบบ
- แก้ไข: ใช้ Context-aware models

**3. ภาษาถิ่นและสำนวน**
- แต่ละภูมิภาคมีภาษาถิ่นต่างกัน
- แก้ไข: สร้าง Domain-specific dictionary

### 5.7.2 การปรับปรุงประสิทธิภาพ

**1. Data Preprocessing**
```python
def preprocess_thai_text(text):
    # ทำความสะอาดข้อความ
    text = re.sub(r'[^\u0E00-\u0E7Fa-zA-Z0-9\s]', '', text)
    
    # Tokenization
    tokens = pythainlp.word_tokenize(text)
    
    # Remove stop words
    stop_words = pythainlp.corpus.thai_stopwords()
    tokens = [token for token in tokens if token not in stop_words]
    
    return tokens
```

**2. Model Fine-tuning**
```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification

# Load pre-trained Thai BERT
tokenizer = AutoTokenizer.from_pretrained("airesearch/wangchanberta-base-att-spm-uncased")
model = AutoModelForSequenceClassification.from_pretrained("airesearch/wangchanberta-base-att-spm-uncased")

# Fine-tune for agriculture domain
# (ต้องมีข้อมูลฝึกสอนเฉพาะด้าน)
```

## 5.8 แบบฝึกหัดและกิจกรรม

### กิจกรรมที่ 1: สร้าง Chatbot เกษตรกรรม
สร้าง chatbot ที่สามารถตอบคำถามเกี่ยวกับการเกษตร

### กิจกรรมที่ 2: วิเคราะห์ความรู้สึกในโซเชียลมีเดีย
วิเคราะห์โพสต์ Facebook/Twitter เกี่ยวกับเกษตรกรรม

### กิจกรรมที่ 3: ระบบแปลภาษาเฉพาะด้าน
สร้างระบบแปลศัพท์เกษตรจากอังกฤษเป็นไทย

### กิจกรรมที่ 4: การสกัดข้อมูลจากข่าว
สร้างระบบสกัดราคาสินค้าเกษตรจากข่าวออนไลน์

## 5.9 สรุปและแนวทางต่อไป

Natural Language Processing เป็นเทคโนโลยีที่มีศักยภาพสูงในการประยุกต์ใช้กับการเกษตร ตั้งแต่การสร้าง chatbot ให้คำปรึกษา การวิเคราะห์ข้อมูลจากโซเชียลมีเดีย ไปจนถึงการสร้างระบบแปลภาษาเฉพาะด้าน

**ประโยชน์หลัก:**
- ช่วยให้เกษตรกรเข้าถึงข้อมูลได้ง่ายขึ้น
- วิเคราะห์แนวโน้มตลาดจากข้อมูลข่าวสาร
- สร้างระบบสนับสนุนการตัดสินใจ
- เชื่อมโยงเกษตรกรกับเทคโนโลยีสมัยใหม่

**แนวทางพัฒนาต่อไป:**
- รวม NLP เข้ากับ IoT sensors
- พัฒนา Voice Assistant สำหรับเกษตรกร
- สร้างระบบแนะนำแบบ Personalized
- ประยุกต์ใช้กับ Precision Agriculture

การเรียนรู้ NLP จะเปิดโอกาสให้นักเรียนสามารถสร้างโซลูชันที่ช่วยแก้ปัญหาการเกษตรได้อย่างมีประสิทธิภาพ และเป็นพื้นฐานสำคัญสำหรับการพัฒนา AI ในอนาคต

