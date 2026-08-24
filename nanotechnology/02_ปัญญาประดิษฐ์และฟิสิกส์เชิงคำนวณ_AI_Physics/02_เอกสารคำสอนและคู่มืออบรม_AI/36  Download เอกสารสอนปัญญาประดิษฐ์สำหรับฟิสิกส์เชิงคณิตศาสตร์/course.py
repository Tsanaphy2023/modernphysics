from flask import Blueprint, render_template
import markdown
import os

course_bp = Blueprint('course', __name__)

@course_bp.route('/')
def course_home():
    # อ่านไฟล์ Markdown
    markdown_file_path = '/home/ubuntu/ai_physics_course_outline.md'
    
    try:
        with open(markdown_file_path, 'r', encoding='utf-8') as file:
            markdown_content = file.read()
        
        # แปลง Markdown เป็น HTML
        html_content = markdown.markdown(markdown_content, extensions=['tables', 'toc'])
        
        return render_template('course_content.html', content=html_content)
    except FileNotFoundError:
        return render_template('course_content.html', content="<h1>ไม่พบไฟล์เนื้อหารายวิชา</h1>")