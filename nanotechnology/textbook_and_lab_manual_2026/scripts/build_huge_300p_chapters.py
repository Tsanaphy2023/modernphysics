#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Autonomous Generator for Huge 350+ Page Masterclass Nanotechnological Physics Textbook.
Populates all 40 topics with extensive academic text, derivations, 80 worked examples,
40 Python simulations, 40 tables, and 160 problems across 8 chapters.
Author: Asst. Prof. Dr. Chewa Thassana, Rambhai Barni Rajabhat University
"""

import os
import sys

CHAPTERS_DIR = "/Users/chewathassana/Downloads/manus_backup2026/ModernPhysics/nanotechnology/textbook_and_lab_manual_2026/scripts/chapters"
os.makedirs(CHAPTERS_DIR, exist_ok=True)

def create_topic_html(ch, sec, title_th, title_en, intro_p, subtopics, formulas, tables, examples, labs, cases, py_codes):
    h = f"""
    <div class="topic-section">
      <h2>{ch}.{sec} {title_th}</h2>
      <div class="topic-en-title">({title_en})</div>
      
      <div class="topic-intro">
    """
    for p in intro_p:
        h += f"    <p>{p}</p>\n"
    h += "  </div>\n"
        
    for sub_title, sub_body in subtopics:
        h += f"""
      <div class="subtopic-block">
        <h3>{sub_title}</h3>
        """
        for p in sub_body:
            h += f"    <p>{p}</p>\n"
        h += "  </div>\n"
            
    if formulas:
        h += "  <div class=\"formula-group\">\n"
        for f_title, f_tex, f_desc in formulas:
            h += f"""
        <div class="equation-box">
          <div class="equation-header">📌 สมการฟิสิกส์หลัก: {f_title}</div>
          <div class="formula-math">$${f_tex}$$</div>
          <p style="font-size:9.5pt; margin:4px 0 0 0; color:#334155; line-height:1.75; text-indent:0;"><strong>คำอธิบายตัวแปรและนัยสำคัญ:</strong> {f_desc}</p>
        </div>
            """
        h += "  </div>\n"
        
    if tables:
        for t_title, headers, rows in tables:
            h += f"""
      <div class="table-block">
        <h3>📊 {t_title}</h3>
        <table class="data-table">
          <thead><tr>
            """
            for head in headers:
                h += f"<th>{head}</th>"
            h += "</tr></thead>\n<tbody>"
            for r in rows:
                h += "<tr>" + "".join([f"<td>{c}</td>" for c in r]) + "</tr>"
            h += "</tbody></table>\n</div>\n"
        
    if examples:
        h += "  <div class=\"examples-group\">\n"
        for ex_num, ex_title, ex_prob, ex_sol, ex_conc in examples:
            h += f"""
        <div class="example-box">
          <div class="example-header">
            <span>📝 ตัวอย่างการคำนวณที่ {ex_num}: {ex_title}</span>
            <span style="background:#dcfce7; color:#15803d; font-size:8.5pt; padding:3px 10px; border-radius:4px; font-weight:700;">Step-by-Step Worked Solution</span>
          </div>
          <p style="text-indent:0; margin-bottom:10px;"><strong>โจทย์ปัญหา (Problem Statement):</strong><br>{ex_prob}</p>
          <div style="background:rgba(255,255,255,0.85); border:1px solid #e2e8f0; padding:12px 16px; border-radius:6px; margin:12px 0;">
            <strong style="color:#1e3a8a;">การวิเคราะห์และการคำนวณอย่างละเอียด:</strong><br>
            <p style="text-indent:0; margin:6px 0 0 0; line-height:1.85;">{ex_sol}</p>
          </div>
          <div style="background:#f0fdf4; border-left:4px solid #16a34a; padding:10px 14px; margin-top:10px; font-size:9.5pt; color:#166534; border-radius:0 6px 6px 0;">
            💡 <strong>นัยสำคัญทางกายภาพและการประยุกต์ใช้งาน (Physical Insight):</strong><br>
            <span style="color:#14532d;">{ex_conc}</span>
          </div>
        </div>
            """
        h += "  </div>\n"
        
    if py_codes:
        h += "  <div class=\"code-group\">\n"
        for item in py_codes:
            if isinstance(item, (tuple, list)):
                if len(item) == 3:
                    py_title, py_code_or_file, py_code_or_desc = item
                    if py_code_or_file.endswith('.py') or '\n' in py_code_or_desc:
                        py_code = py_code_or_desc
                        py_desc = f"สคริปต์ {py_code_or_file} สำหรับคำนวณและจำลองเชิงตัวเลขในแบบจำลอง {py_title}"
                    else:
                        py_code = py_code_or_file
                        py_desc = py_code_or_desc
                elif len(item) == 2:
                    py_title, py_code = item
                    py_desc = f"สคริปต์ไพทอนสำหรับการคำนวณและจำลองเชิงตัวเลข"
                else:
                    continue
            else:
                continue
                
            h += f"""
        <div class="code-box">
          <div class="code-header">💻 แบบจำลองเชิงคำนวณภาษาไพทอน (Computational Python 3.11): {py_title}</div>
          <pre><code>{py_code}</code></pre>
        </div>
        <p style="font-size:9.5pt; color:#475569; margin-top:-6px; margin-bottom:18px; text-indent:0;"><em>คำอธิบายอัลกอริทึมการจำลอง:</em> {py_desc}</p>
            """
        h += "  </div>\n"
        
    if labs:
        h += "  <div class=\"lab-connection-block\">\n"
        h += "    <h3>🔬 การเชื่อมโยงสู่ห้องปฏิบัติการเสมือนจริงและเทคนิคการทดลอง (Virtual Lab Connection)</h3>\n"
        for item in labs:
            if isinstance(item, (tuple, list)):
                h += f"    <div style='background:#f0fdf4; border:1px solid #bbf7d0; border-left:5px solid #16a34a; padding:12px 16px; margin-bottom:14px; border-radius:6px;'><strong style='color:#166534; font-size:10.5pt;'>{item[0]}</strong><p style='margin:6px 0 0 0; color:#14532d; text-indent:0; line-height:1.8;'>{item[1]}</p></div>\n"
            else:
                h += f"    <p>{item}</p>\n"
        h += "  </div>\n"
            
    if cases:
        h += "  <div class=\"cases-block\">\n"
        h += "    <h3>🌐 กรณีศึกษางานวิจัยแนวหน้าและนวัตกรรมอุตสาหกรรม (Frontier Case Studies)</h3>\n"
        for item in cases:
            if isinstance(item, (tuple, list)):
                h += f"    <div style='background:#eff6ff; border:1px solid #bfdbfe; border-left:5px solid #2563eb; padding:12px 16px; margin-bottom:14px; border-radius:6px;'><strong style='color:#1e40af; font-size:10.5pt;'>{item[0]}</strong><p style='margin:6px 0 0 0; color:#1e3a8a; text-indent:0; line-height:1.8;'>{item[1]}</p></div>\n"
            else:
                h += f"    <p>{item}</p>\n"
        h += "  </div>\n"
        
    # Self-assessment checkpoint at end of each topic
    h += f"""
      <div class="checkpoint-box" style="background:#fefce8; border:1px solid #fef08a; border-left:5px solid #eab308; padding:14px 18px; margin:24px 0 35px 0; border-radius:6px; page-break-inside:avoid;">
        <strong style="color:#854d0e; font-size:10pt;">🎯 จุดตรวจประเมินความเข้าใจและคำถามทบทวนประจำหัวข้อ {ch}.{sec} (Concept Checkpoint)</strong>
        <ul style="margin:8px 0 0 0; padding-left:20px; color:#713f12; font-size:9.5pt; line-height:1.8;">
          <li>จงอธิบายแนวคิดรวบยอดหลักของ {title_th} และความแตกต่างจากพฤติกรรมในระดับมหภาค</li>
          <li>พารามิเตอร์ใดเป็นปัจจัยวิกฤตที่ควบคุมสมบัติทางฟิสิกส์ในหัวข้อนี้ และมีผลกระทบอย่างไร?</li>
          <li>เชื่อมโยงหลักการฟิสิกส์ในหัวข้อนี้เข้ากับการประยุกต์ใช้จริงในเทคโนโลยีสมัยใหม่</li>
        </ul>
      </div>
    </div>
    """
    return h

def write_chapter_py(ch_num, badge, title_th, title_en, diagram_svg, diagram_cap, topics_html, summary_points, p1, p2, p3):
    sum_items = "".join([f"<li style='margin-bottom:8px;'>{p}</li>" for p in summary_points])
    p1_items = "".join([f"<li style='margin-bottom:8px;'>{q}</li>" for q in p1])
    p2_items = "".join([f"<li style='margin-bottom:8px;'>{q}</li>" for q in p2])
    p3_items = "".join([f"<li style='margin-bottom:8px;'>{q}</li>" for q in p3])

    code = f"""# -*- coding: utf-8 -*-
\"\"\"
Chapter {ch_num}: {title_th}
{title_en}
\"\"\"

def get_chapter_{ch_num}():
    return r\"\"\"
    <div class="chapter-container">
      <div class="chapter-hero">
        <div class="chapter-badge">{badge}</div>
        <h1 class="chapter-title">{title_th}</h1>
        <p class="chapter-subtitle">{title_en}</p>
      </div>

      <div class="diagram-wrap">
        <img src="../assets/diagrams/{diagram_svg}" alt="{title_th}">
        <div class="caption">ภาพที่ {ch_num}.1 {diagram_cap}</div>
      </div>

      {topics_html}

      <div class="summary-box">
        <h3 style="color:#1e40af; margin-top:0; font-size:13pt;">📋 สรุปสาระสำคัญประจำบทที่ {ch_num} (Chapter {ch_num} Key Takeaways)</h3>
        <ul style="margin:0; padding-left:22px; font-size:10pt; line-height:1.95; color:#1e293b;">
          {sum_items}
        </ul>
      </div>

      <div class="problems-section">
        <h3 style="color:#0f172a; margin-top:0; font-size:14pt; border-bottom:2px solid #cbd5e1; padding-bottom:8px;">
          📚 แบบฝึกหัดและโจทย์ปัญหาท้ายบทที่ {ch_num} (End-of-Chapter Problems)
        </h3>
        
        <h4 style="color:#1e3a8a; font-size:11.5pt; margin-top:18px;">ตอนที่ 1: คำถามเชิงมโนทัศน์และการวิเคราะห์เชิงฟิสิกส์ (Conceptual & Analytical Questions)</h4>
        <ol style="padding-left:22px; font-size:10pt; line-height:1.9; color:#334155;">
          {p1_items}
        </ol>

        <h4 style="color:#166534; font-size:11.5pt; margin-top:22px;">ตอนที่ 2: โจทย์ปัญหาการคำนวณเชิงตัวเลขและการพิสูจน์ (Quantitative & Numerical Problems)</h4>
        <ol style="padding-left:22px; font-size:10pt; line-height:1.9; color:#334155;">
          {p2_items}
        </ol>

        <h4 style="color:#7c2d12; font-size:11.5pt; margin-top:22px;">ตอนที่ 3: โจทย์ประยุกต์ การออกแบบเชิงวิศวกรรม และการจำลอง (Applied Design & Modeling Problems)</h4>
        <ol style="padding-left:22px; font-size:10pt; line-height:1.9; color:#334155;">
          {p3_items}
        </ol>
      </div>
    </div>
    \"\"\"
"""
    fname = os.path.join(CHAPTERS_DIR, f"ch0{ch_num}.py")
    with open(fname, "w", encoding="utf-8") as f:
        f.write(code)
    print(f"✅ Populated Chapter {ch_num}: {fname} ({len(code)} bytes)")

print("✅ Chapter generator helpers ready.")
