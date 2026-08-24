import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Button, TextBox
import pandas as pd
from collections import Counter, defaultdict
import re
from datetime import datetime, timedelta
import seaborn as sns
from wordcloud import WordCloud
import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox

class NLPAgriculturalDemo:
    def __init__(self):
        self.fig = None
        self.current_demo = 0
        self.demos = [
            self.text_preprocessing_demo,
            self.sentiment_analysis_demo,
            self.chatbot_demo,
            self.news_analysis_demo,
            self.translation_demo
        ]
        self.demo_names = [
            "Text Preprocessing",
            "Sentiment Analysis", 
            "Agricultural Chatbot",
            "News Analysis",
            "Translation System"
        ]
        
        # Agricultural vocabulary
        self.agriculture_vocab = {
            'crops': ['ข้าว', 'ข้าวโพด', 'มันสำปะหลัง', 'อ้อย', 'ยางพารา', 'ปาล์มน้ำมัน'],
            'tools': ['รถไถ', 'รถเกี่ยว', 'เครื่องสูบน้ำ', 'โดรน', 'เซนเซอร์'],
            'techniques': ['ปลูก', 'เก็บเกี่ยว', 'ใส่ปุ๋ย', 'รดน้ำ', 'กำจัดศัตรูพืช'],
            'problems': ['โรคพืช', 'แมลงศัตรูพืช', 'ภัยแล้ง', 'น้ำท่วม', 'ดินเสื่อมโทรม']
        }
        
        # Sentiment keywords
        self.positive_words = [
            'ดี', 'เยี่ยม', 'สุดยอด', 'ประสบความสำเร็จ', 'เพิ่มขึ้น', 'กำไร', 
            'คุณภาพสูง', 'สด', 'อร่อย', 'สวยงาม', 'มีประสิทธิภาพ', 'ช่วยได้'
        ]
        
        self.negative_words = [
            'แย่', 'เสียหาย', 'ลดลง', 'ขาดทุน', 'เน่า', 'แห้งตาย', 'โรค', 
            'ศัตรูพืช', 'ปัญหา', 'ยาก', 'ล้มเหลว', 'เสื่อมโทรม', 'ไม่ดี'
        ]
        
        # Knowledge base for chatbot
        self.knowledge_base = {
            'ข้าวโพด': {
                'ปลูก': 'ปลูกข้าวโพดควรเลือกพันธุ์ที่เหมาะกับสภาพดิน ปลูกในช่วงต้นฤดูฝน เตรียมดินให้ร่วนซุย',
                'ปุ๋ย': 'ใช้ปุ๋ยคอก 2-3 ตัน/ไร่ ปุ๋ยเคมี 15-15-15 อัตรา 1 ถุง/ไร่ แบ่งใส่ 3 ครั้ง',
                'โรค': 'โรคใบไหม้: ใช้ยาฆ่าเชื้อรา โรคใบจุด: ฉีดยาป้องกันทุก 15 วัน',
                'เก็บเกี่ยว': 'เก็บเกี่ยวเมื่ออายุ 90-120 วัน เมล็ดแห้งแกร่ง ความชื้น 14-16%'
            },
            'ข้าว': {
                'ปลูก': 'ปลูกข้าวในนาน้ำ เตรียมดินให้ละเอียด ใส่ปุ๋ยคอกก่อนไถ',
                'น้ำ': 'รักษาระดับน้ำ 3-5 ซม. ในช่วงแรก เพิ่มเป็น 10 ซม. ตอนข้าวโต',
                'ปุ๋ย': 'ใส่ปุ๋ยยูเรีย 3 ครั้ง ครั้งละ 1 ถุง/ไร่ ห่างกัน 15-20 วัน',
                'โรค': 'โรคไหม้ใบ: ใช้ยาฆ่าเชื้อรา โรคใบจุดสีน้ำตาล: ฉีดยาป้องกัน'
            },
            'มันสำปะหลัง': {
                'ปลูก': 'ปลูกในดินร่วนซุย ระบายน้ำดี ใช้ท่อนพันธุ์อายุ 8-12 เดือน',
                'ปุ๋ย': 'ใส่ปุ๋ยคอก 1-2 ตัน/ไร่ ปุ๋ยเคมี 15-7-18 อัตรา 1 ถุง/ไร่',
                'โรค': 'โรคใบด่าง: กำจัดแมลงพาหะ โรคเหี่ยวเหลือง: ใช้พันธุ์ต้านทาน',
                'เก็บเกี่ยว': 'เก็บเกี่ยวเมื่ออายุ 8-12 เดือน หัวมันแก่เต็มที่'
            }
        }
        
    def simple_tokenize(self, text):
        """Simple Thai tokenization (จำลอง)"""
        # ใช้ regex แบบง่ายสำหรับการสาธิต
        tokens = re.findall(r'[ก-๙]+|[a-zA-Z]+|\d+', text)
        return tokens
    
    def remove_stopwords(self, tokens):
        """Remove Thai stopwords"""
        stopwords = ['และ', 'หรือ', 'แต่', 'ใน', 'บน', 'ที่', 'เป็น', 'มี', 'ได้', 'จะ', 'ไป', 'มา', 'ให้', 'กับ']
        return [token for token in tokens if token not in stopwords]
    
    def analyze_sentiment(self, text):
        """Simple sentiment analysis"""
        text_lower = text.lower()
        
        positive_count = sum(1 for word in self.positive_words if word in text_lower)
        negative_count = sum(1 for word in self.negative_words if word in text_lower)
        
        if positive_count > negative_count:
            return 'positive', positive_count - negative_count
        elif negative_count > positive_count:
            return 'negative', negative_count - positive_count
        else:
            return 'neutral', 0
    
    def text_preprocessing_demo(self):
        """สาธิตการประมวลผลข้อความ"""
        if self.fig:
            plt.close(self.fig)
        
        self.fig, axes = plt.subplots(2, 3, figsize=(18, 12))
        self.fig.suptitle('การประมวลผลข้อความพื้นฐาน (Text Preprocessing)', fontsize=16, fontweight='bold')
        
        # ข้อความตัวอย่าง
        sample_texts = [
            "เกษตรกรปลูกข้าวโพดในไร่ได้ผลผลิตดีมาก",
            "การใช้ปุ๋ยเคมีและปุ๋ยอินทรีย์ช่วยเพิ่มผลผลิต",
            "โดรนช่วยตรวจสอบสุขภาพพืชได้อย่างมีประสิทธิภาพ"
        ]
        
        # 1. Original Text
        axes[0, 0].axis('off')
        axes[0, 0].set_title('ข้อความต้นฉบับ', fontweight='bold')
        text_display = '\n\n'.join([f"{i+1}. {text}" for i, text in enumerate(sample_texts)])
        axes[0, 0].text(0.05, 0.95, text_display, transform=axes[0, 0].transAxes,
                       fontsize=10, verticalalignment='top',
                       bbox=dict(boxstyle="round,pad=0.5", facecolor='lightblue', alpha=0.7))
        
        # 2. Tokenization
        axes[0, 1].axis('off')
        axes[0, 1].set_title('การแบ่งคำ (Tokenization)', fontweight='bold')
        
        tokenized_display = ""
        for i, text in enumerate(sample_texts):
            tokens = self.simple_tokenize(text)
            tokenized_display += f"{i+1}. {tokens}\n\n"
        
        axes[0, 1].text(0.05, 0.95, tokenized_display, transform=axes[0, 1].transAxes,
                       fontsize=9, verticalalignment='top',
                       bbox=dict(boxstyle="round,pad=0.5", facecolor='lightgreen', alpha=0.7))
        
        # 3. Stop Words Removal
        axes[0, 2].axis('off')
        axes[0, 2].set_title('การกำจัด Stop Words', fontweight='bold')
        
        filtered_display = ""
        for i, text in enumerate(sample_texts):
            tokens = self.simple_tokenize(text)
            filtered_tokens = self.remove_stopwords(tokens)
            filtered_display += f"{i+1}. {filtered_tokens}\n\n"
        
        axes[0, 2].text(0.05, 0.95, filtered_display, transform=axes[0, 2].transAxes,
                       fontsize=9, verticalalignment='top',
                       bbox=dict(boxstyle="round,pad=0.5", facecolor='lightyellow', alpha=0.7))
        
        # 4. Word Frequency
        all_tokens = []
        for text in sample_texts:
            tokens = self.simple_tokenize(text)
            filtered_tokens = self.remove_stopwords(tokens)
            all_tokens.extend(filtered_tokens)
        
        word_freq = Counter(all_tokens)
        top_words = word_freq.most_common(10)
        
        if top_words:
            words, counts = zip(*top_words)
            axes[1, 0].bar(words, counts, color='skyblue', alpha=0.7)
            axes[1, 0].set_title('ความถี่ของคำ')
            axes[1, 0].set_xlabel('คำ')
            axes[1, 0].set_ylabel('ความถี่')
            axes[1, 0].tick_params(axis='x', rotation=45)
        
        # 5. Agricultural Terms Detection
        agri_terms_count = defaultdict(int)
        for text in sample_texts:
            text_lower = text.lower()
            for category, terms in self.agriculture_vocab.items():
                for term in terms:
                    if term in text_lower:
                        agri_terms_count[category] += 1
        
        if agri_terms_count:
            categories = list(agri_terms_count.keys())
            counts = list(agri_terms_count.values())
            
            axes[1, 1].bar(categories, counts, color='lightcoral', alpha=0.7)
            axes[1, 1].set_title('ศัพท์เกษตรที่พบ')
            axes[1, 1].set_xlabel('หมวดหมู่')
            axes[1, 1].set_ylabel('จำนวน')
            axes[1, 1].tick_params(axis='x', rotation=45)
        
        # 6. Text Statistics
        axes[1, 2].axis('off')
        axes[1, 2].set_title('สถิติข้อความ', fontweight='bold')
        
        total_chars = sum(len(text) for text in sample_texts)
        total_words = len(all_tokens)
        unique_words = len(set(all_tokens))
        avg_word_length = np.mean([len(word) for word in all_tokens]) if all_tokens else 0
        
        stats_text = f"""
        จำนวนข้อความ: {len(sample_texts)}
        จำนวนตัวอักษรทั้งหมด: {total_chars}
        จำนวนคำทั้งหมด: {total_words}
        จำนวนคำที่ไม่ซ้ำ: {unique_words}
        ความยาวคำเฉลี่ย: {avg_word_length:.1f} ตัวอักษร
        
        ศัพท์เกษตรที่พบ:
        """
        
        for category, count in agri_terms_count.items():
            stats_text += f"• {category}: {count} คำ\n"
        
        axes[1, 2].text(0.05, 0.95, stats_text, transform=axes[1, 2].transAxes,
                       fontsize=10, verticalalignment='top',
                       bbox=dict(boxstyle="round,pad=0.5", facecolor='lightgray', alpha=0.7))
        
        plt.tight_layout()
    
    def sentiment_analysis_demo(self):
        """สาธิตการวิเคราะห์ความรู้สึก"""
        if self.fig:
            plt.close(self.fig)
        
        self.fig, axes = plt.subplots(2, 2, figsize=(15, 12))
        self.fig.suptitle('การวิเคราะห์ความรู้สึก (Sentiment Analysis)', fontsize=16, fontweight='bold')
        
        # ข้อความตัวอย่าง
        sample_reviews = [
            "ปีนี้ข้าวโพดให้ผลผลิตดีมาก เกษตรกรมีความสุข",
            "ฝนตกหนัก พืชผลเสียหายมาก เกษตรกรเดือดร้อน",
            "ใช้เทคโนโลยีใหม่ปลูกข้าว ผลผลิตเพิ่มขึ้น 30%",
            "ราคาข้าวตกต่ำ เกษตรกรขาดทุนหนัก",
            "โครงการส่งเสริมการเกษตรอัจฉริยะ ช่วยเกษตรกรได้มาก",
            "แมลงศัตรูพืชระบาด ข้าวโพดเสียหายหนัก ต้องใช้ยาเยอะ",
            "เกษตรอินทรีย์ให้ผลผลิตดี ปลอดภัยต่อสุขภาพ",
            "ภัยแล้งทำให้พืชแห้งตาย เกษตรกรไม่มีรายได้"
        ]
        
        # วิเคราะห์ความรู้สึก
        sentiments = []
        scores = []
        
        for review in sample_reviews:
            sentiment, score = self.analyze_sentiment(review)
            sentiments.append(sentiment)
            scores.append(score)
        
        # 1. แสดงผลการวิเคราะห์แต่ละข้อความ
        axes[0, 0].axis('off')
        axes[0, 0].set_title('ผลการวิเคราะห์ความรู้สึก', fontweight='bold')
        
        analysis_text = ""
        colors = {'positive': '🟢', 'negative': '🔴', 'neutral': '🟡'}
        
        for i, (review, sentiment, score) in enumerate(zip(sample_reviews, sentiments, scores)):
            color_icon = colors.get(sentiment, '⚪')
            analysis_text += f"{i+1}. {color_icon} {sentiment.upper()} (คะแนน: {score})\n"
            analysis_text += f"   \"{review[:50]}{'...' if len(review) > 50 else ''}\"\n\n"
        
        axes[0, 0].text(0.05, 0.95, analysis_text, transform=axes[0, 0].transAxes,
                       fontsize=8, verticalalignment='top',
                       bbox=dict(boxstyle="round,pad=0.5", facecolor='white', alpha=0.8))
        
        # 2. การกระจายความรู้สึก
        sentiment_counts = Counter(sentiments)
        labels = list(sentiment_counts.keys())
        sizes = list(sentiment_counts.values())
        colors_pie = ['green' if l == 'positive' else 'red' if l == 'negative' else 'gray' for l in labels]
        
        axes[0, 1].pie(sizes, labels=labels, colors=colors_pie, autopct='%1.1f%%', startangle=90)
        axes[0, 1].set_title('การกระจายความรู้สึก')
        
        # 3. คะแนนความรู้สึกแต่ละข้อความ
        x_pos = range(len(sample_reviews))
        bar_colors = ['green' if s == 'positive' else 'red' if s == 'negative' else 'gray' for s in sentiments]
        
        bars = axes[1, 0].bar(x_pos, scores, color=bar_colors, alpha=0.7)
        axes[1, 0].set_title('คะแนนความรู้สึกแต่ละข้อความ')
        axes[1, 0].set_xlabel('ข้อความที่')
        axes[1, 0].set_ylabel('คะแนนความรู้สึก')
        axes[1, 0].axhline(y=0, color='black', linestyle='-', alpha=0.3)
        
        # เพิ่มป้ายกำกับ
        for bar, sentiment in zip(bars, sentiments):
            height = bar.get_height()
            axes[1, 0].text(bar.get_x() + bar.get_width()/2., height + 0.1 if height >= 0 else height - 0.3,
                           sentiment[0].upper(), ha='center', va='bottom' if height >= 0 else 'top',
                           fontweight='bold')
        
        # 4. คำที่มีผลต่อความรู้สึก
        axes[1, 1].axis('off')
        axes[1, 1].set_title('คำที่มีผลต่อความรู้สึก', fontweight='bold')
        
        # นับคำ positive และ negative ที่พบ
        found_positive = []
        found_negative = []
        
        for review in sample_reviews:
            review_lower = review.lower()
            for word in self.positive_words:
                if word in review_lower:
                    found_positive.append(word)
            for word in self.negative_words:
                if word in review_lower:
                    found_negative.append(word)
        
        pos_freq = Counter(found_positive).most_common(5)
        neg_freq = Counter(found_negative).most_common(5)
        
        keyword_text = "คำเชิงบวกที่พบ:\n"
        for word, count in pos_freq:
            keyword_text += f"• {word}: {count} ครั้ง\n"
        
        keyword_text += "\nคำเชิงลบที่พบ:\n"
        for word, count in neg_freq:
            keyword_text += f"• {word}: {count} ครั้ง\n"
        
        keyword_text += f"\nสรุป:\n"
        keyword_text += f"• ข้อความเชิงบวก: {sentiment_counts.get('positive', 0)} ข้อความ\n"
        keyword_text += f"• ข้อความเชิงลบ: {sentiment_counts.get('negative', 0)} ข้อความ\n"
        keyword_text += f"• ข้อความเป็นกลาง: {sentiment_counts.get('neutral', 0)} ข้อความ"
        
        axes[1, 1].text(0.05, 0.95, keyword_text, transform=axes[1, 1].transAxes,
                       fontsize=10, verticalalignment='top',
                       bbox=dict(boxstyle="round,pad=0.5", facecolor='lightcyan', alpha=0.7))
        
        plt.tight_layout()
    
    def chatbot_demo(self):
        """สาธิต Agricultural Chatbot"""
        if self.fig:
            plt.close(self.fig)
        
        self.fig, axes = plt.subplots(2, 2, figsize=(15, 12))
        self.fig.suptitle('Agricultural Chatbot Demo', fontsize=16, fontweight='bold')
        
        # ตัวอย่างการสนทนา
        conversation = [
            ("user", "วิธีปลูกข้าวโพดยังไง"),
            ("bot", "ปลูกข้าวโพดควรเลือกพันธุ์ที่เหมาะกับสภาพดิน ปลูกในช่วงต้นฤดูฝน เตรียมดินให้ร่วนซุย"),
            ("user", "ข้าวโพดใส่ปุ๋ยอะไร"),
            ("bot", "ใช้ปุ๋ยคอก 2-3 ตัน/ไร่ ปุ๋ยเคมี 15-15-15 อัตรา 1 ถุง/ไร่ แบ่งใส่ 3 ครั้ง"),
            ("user", "เก็บเกี่ยวข้าวโพดเมื่อไหร่"),
            ("bot", "เก็บเกี่ยวเมื่ออายุ 90-120 วัน เมล็ดแห้งแกร่ง ความชื้น 14-16%"),
            ("user", "ข้าวเป็นโรคใบไหม้ทำยังไง"),
            ("bot", "โรคไหม้ใบ: ใช้ยาฆ่าเชื้อรา โรคใบจุดสีน้ำตาล: ฉีดยาป้องกัน")
        ]
        
        # 1. แสดงการสนทนา
        axes[0, 0].axis('off')
        axes[0, 0].set_title('ตัวอย่างการสนทนา', fontweight='bold')
        
        chat_display = ""
        for speaker, message in conversation:
            if speaker == "user":
                chat_display += f"👤 ผู้ใช้: {message}\n\n"
            else:
                chat_display += f"🤖 บอท: {message}\n\n"
        
        axes[0, 0].text(0.05, 0.95, chat_display, transform=axes[0, 0].transAxes,
                       fontsize=9, verticalalignment='top',
                       bbox=dict(boxstyle="round,pad=0.5", facecolor='lightblue', alpha=0.7))
        
        # 2. Knowledge Base Coverage
        axes[0, 1].axis('off')
        axes[0, 1].set_title('ฐานความรู้ของบอท', fontweight='bold')
        
        kb_display = "พืชผลที่รองรับ:\n"
        for crop in self.knowledge_base.keys():
            kb_display += f"• {crop}\n"
            topics = list(self.knowledge_base[crop].keys())
            kb_display += f"  หัวข้อ: {', '.join(topics)}\n\n"
        
        axes[0, 1].text(0.05, 0.95, kb_display, transform=axes[0, 1].transAxes,
                       fontsize=10, verticalalignment='top',
                       bbox=dict(boxstyle="round,pad=0.5", facecolor='lightgreen', alpha=0.7))
        
        # 3. Query Analysis
        user_queries = [msg for speaker, msg in conversation if speaker == "user"]
        
        # วิเคราะห์คำถาม
        query_analysis = {
            'crops_mentioned': defaultdict(int),
            'topics_mentioned': defaultdict(int),
            'question_types': defaultdict(int)
        }
        
        question_words = {
            'วิธี': 'how_to',
            'ยังไง': 'how_to', 
            'อะไร': 'what',
            'เมื่อไหร่': 'when',
            'ทำไง': 'how_to'
        }
        
        for query in user_queries:
            query_lower = query.lower()
            
            # ตรวจหาพืชผล
            for crop in self.knowledge_base.keys():
                if crop in query_lower:
                    query_analysis['crops_mentioned'][crop] += 1
            
            # ตรวจหาหัวข้อ
            for crop_info in self.knowledge_base.values():
                for topic in crop_info.keys():
                    if topic in query_lower:
                        query_analysis['topics_mentioned'][topic] += 1
            
            # ตรวจหาประเภทคำถาม
            for word, q_type in question_words.items():
                if word in query_lower:
                    query_analysis['question_types'][q_type] += 1
        
        # แสดงกราฟการวิเคราะห์คำถาม
        if query_analysis['crops_mentioned']:
            crops = list(query_analysis['crops_mentioned'].keys())
            counts = list(query_analysis['crops_mentioned'].values())
            
            axes[1, 0].bar(crops, counts, color='orange', alpha=0.7)
            axes[1, 0].set_title('พืชผลที่ถูกถามมากที่สุด')
            axes[1, 0].set_xlabel('พืชผล')
            axes[1, 0].set_ylabel('จำนวนครั้ง')
        
        # 4. Bot Performance Metrics
        axes[1, 1].axis('off')
        axes[1, 1].set_title('ประสิทธิภาพของบอท', fontweight='bold')
        
        # คำนวณเมตริก
        total_queries = len(user_queries)
        answered_queries = len([msg for speaker, msg in conversation if speaker == "bot"])
        response_rate = (answered_queries / total_queries * 100) if total_queries > 0 else 0
        
        # ความครอบคลุมของหัวข้อ
        total_topics = sum(len(topics) for topics in self.knowledge_base.values())
        covered_topics = len(query_analysis['topics_mentioned'])
        topic_coverage = (covered_topics / total_topics * 100) if total_topics > 0 else 0
        
        metrics_text = f"""
        📊 สถิติการทำงาน:
        
        • จำนวนคำถามทั้งหมด: {total_queries}
        • จำนวนคำตอบ: {answered_queries}
        • อัตราการตอบ: {response_rate:.1f}%
        
        📚 ความครอบคลุม:
        • หัวข้อทั้งหมด: {total_topics}
        • หัวข้อที่ถูกถาม: {covered_topics}
        • ความครอบคลุม: {topic_coverage:.1f}%
        
        🎯 ประเภทคำถามที่พบ:
        """
        
        for q_type, count in query_analysis['question_types'].items():
            type_name = {
                'how_to': 'วิธีการ',
                'what': 'คำถามเรื่องอะไร',
                'when': 'คำถามเรื่องเวลา'
            }.get(q_type, q_type)
            metrics_text += f"• {type_name}: {count} ครั้ง\n"
        
        axes[1, 1].text(0.05, 0.95, metrics_text, transform=axes[1, 1].transAxes,
                       fontsize=10, verticalalignment='top',
                       bbox=dict(boxstyle="round,pad=0.5", facecolor='lightyellow', alpha=0.7))
        
        plt.tight_layout()
    
    def news_analysis_demo(self):
        """สาธิตการวิเคราะห์ข่าว"""
        if self.fig:
            plt.close(self.fig)
        
        self.fig, axes = plt.subplots(2, 2, figsize=(15, 12))
        self.fig.suptitle('การวิเคราะห์ข่าวเกษตร (News Analysis)', fontsize=16, fontweight='bold')
        
        # ข้อมูลข่าวตัวอย่าง
        news_data = [
            {
                'title': 'ราคาข้าวโพดเพิ่มขึ้น 15 บาทต่อกิโลกรัม',
                'content': 'เกษตรกรมีความสุขกับราคาข้าวโพดที่สูงขึ้น ผลผลิตปีนี้ดีมาก',
                'date': '2024-01-15',
                'category': 'ราคา'
            },
            {
                'title': 'ฝนตกหนัก ข้าวในภาคเหนือเสียหาย',
                'content': 'เกษตรกรเดือดร้อน ข้าวเสียหายจากน้ำท่วม คาดผลผลิตลดลง 20%',
                'date': '2024-01-16',
                'category': 'ภัยธรรมชาติ'
            },
            {
                'title': 'โครงการเกษตรอัจฉริยะ ช่วยเพิ่มผลผลิตมันสำปะหลัง',
                'content': 'เทคโนโลยี AI ช่วยเกษตรกร ผลผลิตมันสำปะหลังเพิ่มขึ้น 30%',
                'date': '2024-01-17',
                'category': 'เทคโนโลยี'
            },
            {
                'title': 'ส่งออกข้าวไทยทำสถิติใหม่',
                'content': 'ข้าวไทยได้รับความนิยมในตลาดโลก ราคาดี คุณภาพสูง',
                'date': '2024-01-18',
                'category': 'การค้า'
            },
            {
                'title': 'เกษตรอินทรีย์เติบโตต่อเนื่อง',
                'content': 'ผู้บริโภคหันมาสนใจอาหารปลอดภัย เกษตรกรปรับเปลี่ยนวิธีการผลิต',
                'date': '2024-01-19',
                'category': 'เทรนด์'
            },
            {
                'title': 'แมลงศัตรูพืชระบาดในภาคอีสาน',
                'content': 'เกษตรกรต้องเพิ่มการใช้ยาฆ่าแมลง ต้นทุนการผลิตสูงขึ้น',
                'date': '2024-01-20',
                'category': 'ศัตรูพืช'
            }
        ]
        
        # 1. การกระจายหมวดหมู่ข่าว
        categories = [news['category'] for news in news_data]
        category_counts = Counter(categories)
        
        axes[0, 0].pie(category_counts.values(), labels=category_counts.keys(), 
                      autopct='%1.1f%%', startangle=90)
        axes[0, 0].set_title('การกระจายหมวดหมู่ข่าว')
        
        # 2. การวิเคราะห์ความรู้สึกในข่าว
        news_sentiments = []
        for news in news_data:
            text = news['title'] + ' ' + news['content']
            sentiment, score = self.analyze_sentiment(text)
            news_sentiments.append((sentiment, score))
        
        sentiments = [s[0] for s in news_sentiments]
        sentiment_counts = Counter(sentiments)
        
        colors = ['green' if s == 'positive' else 'red' if s == 'negative' else 'gray' for s in sentiment_counts.keys()]
        axes[0, 1].bar(sentiment_counts.keys(), sentiment_counts.values(), color=colors, alpha=0.7)
        axes[0, 1].set_title('ความรู้สึกในข่าว')
        axes[0, 1].set_ylabel('จำนวนข่าว')
        
        # 3. แนวโน้มข่าวตามวัน
        dates = [news['date'] for news in news_data]
        date_counts = Counter(dates)
        
        sorted_dates = sorted(date_counts.keys())
        daily_counts = [date_counts[date] for date in sorted_dates]
        
        axes[1, 0].plot(range(len(sorted_dates)), daily_counts, marker='o', linewidth=2, markersize=6)
        axes[1, 0].set_title('จำนวนข่าวรายวัน')
        axes[1, 0].set_xlabel('วันที่')
        axes[1, 0].set_ylabel('จำนวนข่าว')
        axes[1, 0].set_xticks(range(len(sorted_dates)))
        axes[1, 0].set_xticklabels([date.split('-')[2] for date in sorted_dates])
        axes[1, 0].grid(True, alpha=0.3)
        
        # 4. สรุปการวิเคราะห์
        axes[1, 1].axis('off')
        axes[1, 1].set_title('สรุปการวิเคราะห์', fontweight='bold')
        
        # หาคำที่ปรากฏบ่อย
        all_text = ' '.join([news['title'] + ' ' + news['content'] for news in news_data])
        words = self.simple_tokenize(all_text)
        filtered_words = self.remove_stopwords(words)
        word_freq = Counter(filtered_words).most_common(10)
        
        # หาพืชผลที่ถูกกล่าวถึง
        crop_mentions = defaultdict(int)
        for news in news_data:
            text = (news['title'] + ' ' + news['content']).lower()
            for category, crops in self.agriculture_vocab.items():
                if category == 'crops':
                    for crop in crops:
                        if crop in text:
                            crop_mentions[crop] += 1
        
        summary_text = f"""
        📰 สถิติข่าว:
        • จำนวนข่าวทั้งหมด: {len(news_data)}
        • หมวดหมู่ที่พบมากที่สุด: {max(category_counts, key=category_counts.get)}
        • ความรู้สึกโดยรวม: {max(sentiment_counts, key=sentiment_counts.get)}
        
        🌾 พืชผลที่ถูกกล่าวถึง:
        """
        
        for crop, count in sorted(crop_mentions.items(), key=lambda x: x[1], reverse=True)[:5]:
            summary_text += f"• {crop}: {count} ครั้ง\n"
        
        summary_text += f"\n🔤 คำที่ปรากฏบ่อย:\n"
        for word, count in word_freq[:5]:
            summary_text += f"• {word}: {count} ครั้ง\n"
        
        axes[1, 1].text(0.05, 0.95, summary_text, transform=axes[1, 1].transAxes,
                       fontsize=10, verticalalignment='top',
                       bbox=dict(boxstyle="round,pad=0.5", facecolor='lightcyan', alpha=0.7))
        
        plt.tight_layout()
    
    def translation_demo(self):
        """สาธิตระบบแปลภาษา"""
        if self.fig:
            plt.close(self.fig)
        
        self.fig, axes = plt.subplots(2, 2, figsize=(15, 12))
        self.fig.suptitle('ระบบแปลภาษาเกษตร (Translation System)', fontsize=16, fontweight='bold')
        
        # พจนานุกรมศัพท์เกษตร
        agri_dict = {
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
            'potassium': 'โพแทสเซียม',
            'yield': 'ผลผลิต',
            'seed': 'เมล็ดพันธุ์',
            'plant disease': 'โรคพืช'
        }
        
        # ข้อความตัวอย่างสำหรับแปล
        sample_texts = [
            "Apply fertilizer to increase crop yield",
            "Use organic farming methods for soil health",
            "Monitor plant disease and apply pesticide when necessary",
            "Proper irrigation system improves harvest quality"
        ]
        
        # 1. แสดงพจนานุกรมศัพท์เกษตร
        axes[0, 0].axis('off')
        axes[0, 0].set_title('พจนานุกรมศัพท์เกษตร', fontweight='bold')
        
        dict_display = "English → Thai\n" + "="*20 + "\n"
        for en_term, th_term in list(agri_dict.items())[:10]:
            dict_display += f"{en_term:<15} → {th_term}\n"
        
        if len(agri_dict) > 10:
            dict_display += f"\n... และอีก {len(agri_dict) - 10} คำ"
        
        axes[0, 0].text(0.05, 0.95, dict_display, transform=axes[0, 0].transAxes,
                       fontsize=10, verticalalignment='top', family='monospace',
                       bbox=dict(boxstyle="round,pad=0.5", facecolor='lightblue', alpha=0.7))
        
        # 2. ตัวอย่างการแปล
        axes[0, 1].axis('off')
        axes[0, 1].set_title('ตัวอย่างการแปล', fontweight='bold')
        
        translation_display = ""
        for i, text in enumerate(sample_texts):
            translation_display += f"{i+1}. EN: {text}\n"
            
            # แปลแบบง่าย (จำลอง)
            translated = text.lower()
            for en_term, th_term in agri_dict.items():
                if en_term in translated:
                    translated = translated.replace(en_term, f"[{th_term}]")
            
            translation_display += f"   TH: {translated}\n\n"
        
        axes[0, 1].text(0.05, 0.95, translation_display, transform=axes[0, 1].transAxes,
                       fontsize=9, verticalalignment='top',
                       bbox=dict(boxstyle="round,pad=0.5", facecolor='lightgreen', alpha=0.7))
        
        # 3. สถิติการใช้ศัพท์
        term_usage = defaultdict(int)
        for text in sample_texts:
            text_lower = text.lower()
            for en_term in agri_dict.keys():
                if en_term in text_lower:
                    term_usage[en_term] += 1
        
        if term_usage:
            terms = list(term_usage.keys())
            counts = list(term_usage.values())
            
            axes[1, 0].bar(terms, counts, color='orange', alpha=0.7)
            axes[1, 0].set_title('ความถี่การใช้ศัพท์เกษตร')
            axes[1, 0].set_xlabel('ศัพท์')
            axes[1, 0].set_ylabel('ความถี่')
            axes[1, 0].tick_params(axis='x', rotation=45)
        
        # 4. ประสิทธิภาพการแปล
        axes[1, 1].axis('off')
        axes[1, 1].set_title('ประสิทธิภาพการแปล', fontweight='bold')
        
        # คำนวณเมตริก
        total_words = sum(len(text.split()) for text in sample_texts)
        agri_terms_found = sum(term_usage.values())
        coverage = (agri_terms_found / total_words * 100) if total_words > 0 else 0
        
        # ความครอบคลุมของพจนานุกรม
        unique_terms_used = len(term_usage)
        dict_coverage = (unique_terms_used / len(agri_dict) * 100) if len(agri_dict) > 0 else 0
        
        metrics_text = f"""
        📊 สถิติการแปล:
        
        • จำนวนข้อความ: {len(sample_texts)}
        • จำนวนคำทั้งหมด: {total_words}
        • ศัพท์เกษตรที่พบ: {agri_terms_found}
        • ความครอบคลุม: {coverage:.1f}%
        
        📚 พจนานุกรม:
        • ศัพท์ทั้งหมด: {len(agri_dict)}
        • ศัพท์ที่ใช้: {unique_terms_used}
        • การใช้งาน: {dict_coverage:.1f}%
        
        🎯 ศัพท์ที่ใช้บ่อย:
        """
        
        for term, count in sorted(term_usage.items(), key=lambda x: x[1], reverse=True)[:3]:
            metrics_text += f"• {term}: {count} ครั้ง\n"
        
        axes[1, 1].text(0.05, 0.95, metrics_text, transform=axes[1, 1].transAxes,
                       fontsize=10, verticalalignment='top',
                       bbox=dict(boxstyle="round,pad=0.5", facecolor='lightyellow', alpha=0.7))
        
        plt.tight_layout()
    
    def setup_navigation(self):
        """ตั้งค่าปุ่มสำหรับเปลี่ยนการสาธิต"""
        if self.fig:
            # Previous button
            ax_prev = plt.axes([0.1, 0.01, 0.1, 0.05])
            self.btn_prev = Button(ax_prev, 'ก่อนหน้า')
            self.btn_prev.on_clicked(self.prev_demo)
            
            # Next button
            ax_next = plt.axes([0.8, 0.01, 0.1, 0.05])
            self.btn_next = Button(ax_next, 'ถัดไป')
            self.btn_next.on_clicked(self.next_demo)
            
            # Demo info
            demo_info = f"การสาธิต {self.current_demo + 1}/{len(self.demos)}: {self.demo_names[self.current_demo]}"
            self.fig.text(0.5, 0.01, demo_info, ha='center', fontsize=12, fontweight='bold')
    
    def prev_demo(self, event):
        """แสดงการสาธิตก่อนหน้า"""
        self.current_demo = (self.current_demo - 1) % len(self.demos)
        self.show_current_demo()
    
    def next_demo(self, event):
        """แสดงการสาธิตถัดไป"""
        self.current_demo = (self.current_demo + 1) % len(self.demos)
        self.show_current_demo()
    
    def show_current_demo(self):
        """แสดงการสาธิตปัจจุบัน"""
        self.demos[self.current_demo]()
        self.setup_navigation()
        plt.draw()
    
    def start(self):
        """เริ่มการสาธิต"""
        print("=== การสาธิต Natural Language Processing ===")
        print("ใช้ปุ่ม 'ถัดไป' และ 'ก่อนหน้า' เพื่อดูการสาธิตต่างๆ")
        print("\nการสาธิตที่มี:")
        for i, name in enumerate(self.demo_names, 1):
            print(f"{i}. {name}")
        
        self.show_current_demo()
        plt.show()

# Interactive Chatbot GUI
class AgriculturalChatbotGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Agricultural Chatbot - เกษตรบอท")
        self.root.geometry("800x600")
        
        # Knowledge base
        self.knowledge_base = {
            'ข้าวโพด': {
                'ปลูก': 'ปลูกข้าวโพดควรเลือกพันธุ์ที่เหมาะกับสภาพดิน ปลูกในช่วงต้นฤดูฝน เตรียมดินให้ร่วนซุย',
                'ปุ๋ย': 'ใช้ปุ๋ยคอก 2-3 ตัน/ไร่ ปุ๋ยเคมี 15-15-15 อัตรา 1 ถุง/ไร่ แบ่งใส่ 3 ครั้ง',
                'โรค': 'โรคใบไหม้: ใช้ยาฆ่าเชื้อรา โรคใบจุด: ฉีดยาป้องกันทุก 15 วัน',
                'เก็บเกี่ยว': 'เก็บเกี่ยวเมื่ออายุ 90-120 วัน เมล็ดแห้งแกร่ง ความชื้น 14-16%'
            },
            'ข้าว': {
                'ปลูก': 'ปลูกข้าวในนาน้ำ เตรียมดินให้ละเอียด ใส่ปุ๋ยคอกก่อนไถ',
                'น้ำ': 'รักษาระดับน้ำ 3-5 ซม. ในช่วงแรก เพิ่มเป็น 10 ซม. ตอนข้าวโต',
                'ปุ๋ย': 'ใส่ปุ๋ยยูเรีย 3 ครั้ง ครั้งละ 1 ถุง/ไร่ ห่างกัน 15-20 วัน',
                'โรค': 'โรคไหม้ใบ: ใช้ยาฆ่าเชื้อรา โรคใบจุดสีน้ำตาล: ฉีดยาป้องกัน'
            }
        }
        
        self.setup_gui()
        
    def setup_gui(self):
        """ตั้งค่า GUI"""
        # Title
        title_label = tk.Label(self.root, text="🌾 เกษตรบอท - ผู้ช่วยเกษตรกรอัจฉริยะ 🌾", 
                              font=("Arial", 16, "bold"), fg="green")
        title_label.pack(pady=10)
        
        # Chat display
        self.chat_frame = tk.Frame(self.root)
        self.chat_frame.pack(expand=True, fill="both", padx=10, pady=5)
        
        self.chat_display = scrolledtext.ScrolledText(self.chat_frame, 
                                                     font=("Arial", 11),
                                                     wrap=tk.WORD,
                                                     state=tk.DISABLED)
        self.chat_display.pack(expand=True, fill="both")
        
        # Input frame
        input_frame = tk.Frame(self.root)
        input_frame.pack(fill="x", padx=10, pady=5)
        
        self.input_entry = tk.Entry(input_frame, font=("Arial", 12))
        self.input_entry.pack(side="left", expand=True, fill="x", padx=(0, 5))
        self.input_entry.bind("<Return>", self.send_message)
        
        send_button = tk.Button(input_frame, text="ส่ง", 
                               command=self.send_message,
                               font=("Arial", 12),
                               bg="lightgreen")
        send_button.pack(side="right")
        
        # Quick buttons
        quick_frame = tk.Frame(self.root)
        quick_frame.pack(fill="x", padx=10, pady=5)
        
        quick_questions = [
            "วิธีปลูกข้าวโพด",
            "ข้าวใส่ปุ๋ยอะไร", 
            "เก็บเกี่ยวข้าวเมื่อไหร่",
            "ข้าวโพดเป็นโรค"
        ]
        
        for i, question in enumerate(quick_questions):
            btn = tk.Button(quick_frame, text=question,
                           command=lambda q=question: self.quick_question(q),
                           font=("Arial", 9))
            btn.pack(side="left", padx=2)
        
        # Welcome message
        self.add_message("บอท", "สวัสดีครับ! ผมคือเกษตรบอท พร้อมช่วยตอบคำถามเกี่ยวกับการเกษตร\nลองถามเกี่ยวกับ ข้าว, ข้าวโพด, การปลูก, ปุ๋ย, โรคพืช หรือการเก็บเกี่ยวได้เลยครับ")
    
    def add_message(self, sender, message):
        """เพิ่มข้อความในหน้าจอแชท"""
        self.chat_display.config(state=tk.NORMAL)
        
        timestamp = datetime.now().strftime("%H:%M")
        if sender == "ผู้ใช้":
            self.chat_display.insert(tk.END, f"[{timestamp}] 👤 {sender}: {message}\n\n")
        else:
            self.chat_display.insert(tk.END, f"[{timestamp}] 🤖 {sender}: {message}\n\n")
        
        self.chat_display.config(state=tk.DISABLED)
        self.chat_display.see(tk.END)
    
    def process_question(self, question):
        """ประมวลผลคำถามและให้คำตอบ"""
        question_lower = question.lower()
        
        # ระบุพืชผล
        crop = None
        for crop_name in self.knowledge_base.keys():
            if crop_name in question_lower:
                crop = crop_name
                break
        
        if not crop:
            return "กรุณาระบุชื่อพืชผลที่ต้องการสอบถาม เช่น ข้าวโพด หรือ ข้าว"
        
        # ระบุหัวข้อ
        topic = None
        crop_info = self.knowledge_base[crop]
        
        for topic_name in crop_info.keys():
            if topic_name in question_lower:
                topic = topic_name
                break
        
        if topic:
            return f"เกี่ยวกับ{topic}ของ{crop}:\n{crop_info[topic]}"
        else:
            # ให้ข้อมูลทั่วไป
            info = f"ข้อมูลเกี่ยวกับ{crop}:\n"
            for key, value in crop_info.items():
                info += f"• {key}: {value}\n"
            return info
    
    def send_message(self, event=None):
        """ส่งข้อความ"""
        message = self.input_entry.get().strip()
        if not message:
            return
        
        # แสดงข้อความของผู้ใช้
        self.add_message("ผู้ใช้", message)
        
        # ประมวลผลและตอบกลับ
        response = self.process_question(message)
        self.add_message("บอท", response)
        
        # ล้างช่องพิมพ์
        self.input_entry.delete(0, tk.END)
    
    def quick_question(self, question):
        """ส่งคำถามด่วน"""
        self.input_entry.delete(0, tk.END)
        self.input_entry.insert(0, question)
        self.send_message()
    
    def run(self):
        """เริ่มต้น GUI"""
        self.root.mainloop()

if __name__ == "__main__":
    print("=== การสาธิต Natural Language Processing ===")
    print("\n1. การสาธิต NLP พื้นฐาน")
    print("2. เกษตรบอท GUI")
    
    choice = input("\nเลือกการสาธิต (1 หรือ 2): ")
    
    if choice == "1":
        demo = NLPAgriculturalDemo()
        demo.start()
    elif choice == "2":
        print("\nกำลังเปิดเกษตรบอท GUI...")
        chatbot_gui = AgriculturalChatbotGUI()
        chatbot_gui.run()
    else:
        print("ตัวเลือกไม่ถูกต้อง กำลังแสดงการสาธิต NLP พื้นฐาน...")
        demo = NLPAgriculturalDemo()
        demo.start()

