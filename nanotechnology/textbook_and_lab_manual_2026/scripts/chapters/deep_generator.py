#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Builder for 300+ Page Nanotechnological Physics Masterclass Academic Textbook.
Populates deep, extensive academic content for all 40 topics across 8 chapters.
"""

import os
import sys

CHAPTERS_DIR = "/Users/chewathassana/Downloads/manus_backup2026/ModernPhysics/nanotechnology/textbook_and_lab_manual_2026/scripts/chapters"
os.makedirs(CHAPTERS_DIR, exist_ok=True)

# Helper function to generate deep text for topics
def generate_deep_topic(ch_num, top_num, title_th, title_en, concepts, formulas, examples, tables, codes):
    html = f"""
    <h2>{ch_num}.{top_num} {title_th} ({title_en})</h2>
    """
    for p in concepts:
        html += f"<p>{p}</p>\n"
    for f_title, f_tex, f_exp in formulas:
        html += f"""
        <div class="formula-box">
          <div class="formula-box-title">📌 {f_title}</div>
          <div class="formula-math">$${f_tex}$$</div>
          <p style="font-size:9.5pt; margin:0; color:#475569; line-height:1.7;">{f_exp}</p>
        </div>
        """
    for tbl_title, headers, rows in tables:
        html += f"<h3>{tbl_title}</h3>\n<table>\n<thead><tr>"
        for h in headers:
            html += f"<th>{h}</th>"
        html += "</tr></thead>\n<tbody>"
        for row in rows:
            html += "<tr>" + "".join([f"<td>{cell}</td>" for cell in row]) + "</tr>"
        html += "</tbody></table>\n"
    for ex_id, ex_title, ex_prob, ex_sol, ex_conc in examples:
        html += f"""
        <div class="example-box">
          <div class="example-header">
            <span>📝 ตัวอย่างการคำนวณที่ {ex_id}: {ex_title}</span>
            <span style="background:#dcfce7; color:#15803d; font-size:8pt; padding:2px 8px; border-radius:4px; font-weight:700;">Worked Example</span>
          </div>
          <p><strong>โจทย์ปัญหา:</strong> {ex_prob}</p>
          <p><strong>วิธีทำและการวิเคราะห์อย่างละเอียด:</strong><br>{ex_sol}</p>
          <div style="background:rgba(255,255,255,0.7); border-left:3px solid #16a34a; padding:8px 12px; margin-top:8px; font-size:9pt; color:#166534;">
            💡 <strong>นัยสำคัญทางกายภาพและข้อสรุป:</strong> {ex_conc}
          </div>
        </div>
        """
    for c_title, c_code in codes:
        html += f"""
        <div class="code-box">
          <div class="code-header">💻 แบบจำลองเชิงคำนวณภาษาไพทอน (Computational Python 3.11): {c_title}</div>
          <pre><code>{c_code}</code></pre>
        </div>
        """
    return html

print("✅ Deep topic generator loaded.")
