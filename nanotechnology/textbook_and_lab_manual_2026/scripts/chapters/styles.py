# CSS & Page Geometry for 300+ Page Masterclass Academic Textbook (Springer/MIT Style)
CSS_STYLES = """
@page {
  size: A4 portrait;
  margin-top: 25.4mm;
  margin-bottom: 25.4mm;
}

@page :left {
  margin-left: 25.4mm;
  margin-right: 38.1mm; /* Gutter 1.5 in */
  @top-left {
    content: "นาโนเทคโนโลยีเชิงฟิสิกส์ (Nanotechnological Physics)";
    font-family: 'Sarabun', sans-serif;
    font-size: 8.5pt;
    color: #64748b;
  }
  @top-right {
    content: counter(page);
    font-family: 'JetBrains Mono', monospace;
    font-size: 9pt;
    font-weight: 700;
    color: #0284c7;
  }
}

@page :right {
  margin-left: 38.1mm; /* Gutter 1.5 in */
  margin-right: 25.4mm;
  @top-left {
    content: counter(page);
    font-family: 'JetBrains Mono', monospace;
    font-size: 9pt;
    font-weight: 700;
    color: #0284c7;
  }
  @top-right {
    content: string(chapter-title);
    font-family: 'Sarabun', sans-serif;
    font-size: 8.5pt;
    color: #64748b;
  }
}

* { box-sizing: border-box; }
body {
  font-family: 'Sarabun', -apple-system, sans-serif;
  font-size: 10pt;
  line-height: 1.85;
  color: #1e293b;
  background: #ffffff;
  margin: 0;
  padding: 0;
}

.chapter-container {
  break-before: right;
  page-break-before: right;
  margin-bottom: 30px;
}

.chapter-hero {
  background: linear-gradient(135deg, #091328 0%, #1e293b 100%);
  border-left: 7px solid #0ea5e9;
  border-radius: 14px;
  padding: 28px 32px;
  color: #ffffff;
  margin-bottom: 30px;
  page-break-inside: avoid;
}

.chapter-badge {
  display: inline-block;
  background: rgba(14, 165, 233, 0.2);
  border: 1px solid #0ea5e9;
  color: #38bdf8;
  font-family: 'JetBrains Mono', monospace;
  font-size: 8.5pt;
  font-weight: 700;
  padding: 3px 12px;
  border-radius: 9999px;
  margin-bottom: 12px;
  text-transform: uppercase;
}

.chapter-title {
  font-size: 20pt;
  font-weight: 800;
  color: #ffffff;
  line-height: 1.35;
  margin: 0 0 10px 0;
}

.chapter-subtitle {
  font-size: 11pt;
  color: #94a3b8;
  margin: 0;
}

h2 {
  font-size: 13.5pt;
  font-weight: 700;
  color: #0369a1;
  border-bottom: 1.5px solid #e2e8f0;
  padding-bottom: 6px;
  margin-top: 30px;
  margin-bottom: 14px;
  break-after: avoid;
  page-break-after: avoid;
}

h3 {
  font-size: 11.5pt;
  font-weight: 700;
  color: #0f172a;
  margin-top: 22px;
  margin-bottom: 10px;
  break-after: avoid;
  page-break-after: avoid;
}

h4 {
  font-size: 10.5pt;
  font-weight: 700;
  color: #334155;
  margin-top: 18px;
  margin-bottom: 8px;
  break-after: avoid;
}

p {
  margin: 0 0 14px 0;
  text-align: justify;
  text-justify: inter-word;
}

.formula-box {
  background: #f8fafc;
  border: 1px solid #cbd5e1;
  border-left: 5px solid #0284c7;
  border-radius: 10px;
  padding: 16px 20px;
  margin: 22px 0;
  page-break-inside: avoid;
}

.formula-box-title {
  font-weight: 700;
  color: #0369a1;
  font-size: 10pt;
  margin-bottom: 8px;
}

.formula-math {
  text-align: center;
  font-size: 11.5pt;
  margin: 12px 0;
  color: #0f172a;
}

.example-box {
  background: #f0fdf4;
  border: 1px solid #bbf7d0;
  border-left: 5px solid #16a34a;
  border-radius: 10px;
  padding: 18px 22px;
  margin: 24px 0;
  page-break-inside: avoid;
}

.example-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  font-weight: 700;
  color: #15803d;
  margin-bottom: 10px;
  border-bottom: 1px solid #dcfce7;
  padding-bottom: 6px;
}

.code-box {
  background: #0f172a;
  border: 1px solid #334155;
  border-radius: 10px;
  padding: 14px 18px;
  margin: 20px 0;
  color: #f8fafc;
  font-family: 'JetBrains Mono', monospace;
  font-size: 8.5pt;
  line-height: 1.6;
  page-break-inside: avoid;
}

.code-header {
  color: #38bdf8;
  font-weight: 700;
  font-size: 8.5pt;
  border-bottom: 1px solid #334155;
  padding-bottom: 6px;
  margin-bottom: 10px;
}

.diagram-wrap {
  text-align: center;
  margin: 26px 0;
  page-break-inside: avoid;
}

.diagram-wrap img {
  max-width: 92%;
  height: auto;
  border-radius: 10px;
  box-shadow: 0 4px 15px rgba(0,0,0,0.08);
  border: 1px solid #e2e8f0;
}

.caption {
  font-size: 9pt;
  color: #64748b;
  margin-top: 8px;
  font-style: italic;
}

table {
  width: 100%;
  border-collapse: collapse;
  margin: 18px 0;
  font-size: 9pt;
  page-break-inside: avoid;
}

th {
  background: #0f172a;
  color: #ffffff;
  font-weight: 600;
  padding: 9px 11px;
  text-align: left;
  border: 1px solid #334155;
}

td {
  padding: 8px 11px;
  border: 1px solid #e2e8f0;
  vertical-align: top;
}

tr:nth-child(even) {
  background: #f8fafc;
}

.summary-box {
  background: #fdf4ff;
  border: 1px solid #f0abfc;
  border-left: 5px solid #c084fc;
  border-radius: 10px;
  padding: 18px 22px;
  margin: 24px 0;
  page-break-inside: avoid;
}

.exercise-box {
  background: #fffbeb;
  border: 1px solid #fde68a;
  border-left: 5px solid #f59e0b;
  border-radius: 10px;
  padding: 20px 24px;
  margin: 26px 0;
  page-break-inside: avoid;
}

.cover-page {
  page-break-before: always;
  page-break-after: always;
  height: 100vh;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  text-align: center;
  padding: 40px;
  background: linear-gradient(135deg, #020617 0%, #091328 100%);
  color: #ffffff;
}

.toc-page {
  page-break-before: always;
  page-break-after: always;
  padding: 10px 0;
}
"""
