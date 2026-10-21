# -*- coding: utf-8 -*-
"""
build_ch08_pdf_guide.py
Compiles Ch08_Power_Distribution_Comprehensive_Guide.md into a publication-grade PDF
using MarkdownIt, KaTeX, Mermaid.js, and Microsoft Edge Headless.
"""

import os
import sys
import re
import subprocess
import shutil
from markdown_it import MarkdownIt

sys.stdout.reconfigure(encoding='utf-8')

base_dir = r"c:\Users\thana\Desktop\Private-Flashcard"
fund_e_dir = r"c:\Users\thana\Desktop\Fund E N'Manow"
md_source_path = os.path.join(fund_e_dir, "Ch08_Power_Distribution_Comprehensive_Guide.md")

if not os.path.exists(md_source_path):
    md_source_path = os.path.join(base_dir, "Ch08_Power_Distribution_Comprehensive_Guide.md")

with open(md_source_path, 'r', encoding='utf-8') as f:
    raw_md = f.read()

print(f"Loaded Markdown source: {len(raw_md)} chars from {md_source_path}")

# Sync MD to both directories
dest_priv = os.path.join(base_dir, "Ch08_Power_Distribution_Comprehensive_Guide.md")
dest_fund = os.path.join(fund_e_dir, "Ch08_Power_Distribution_Comprehensive_Guide.md")
if os.path.abspath(md_source_path) != os.path.abspath(dest_priv):
    shutil.copy2(md_source_path, dest_priv)
if os.path.abspath(md_source_path) != os.path.abspath(dest_fund):
    shutil.copy2(md_source_path, dest_fund)

# -------------------------------------------------------------
# 1. MATH & MERMAID PRE-PROCESSING
# -------------------------------------------------------------
math_storage = []

def stash_display_math(match):
    idx = len(math_storage)
    math_storage.append(('display', match.group(1).strip()))
    return f"\n\n@@MATH_DISPLAY_{idx}@@\n\n"

def stash_inline_math(match):
    idx = len(math_storage)
    math_storage.append(('inline', match.group(1).strip()))
    return f"@@MATH_INLINE_{idx}@@"

# Stash $$ ... $$ (display math)
processed_md = re.sub(r'\$\$(.*?)\$\$', stash_display_math, raw_md, flags=re.DOTALL)

# Stash $ ... $ (inline math)
processed_md = re.sub(r'(?<!\$)\$(?!\$)(.*?)(?<!\$)\$(?!\$)', stash_inline_math, processed_md)

# Convert GitHub alert callouts: > [!NOTE], > [!WARNING], > [!TIP], > [!IMPORTANT]
def convert_callouts(text):
    callout_pattern = re.compile(r'(?:^> ?\[!(NOTE|TIP|IMPORTANT|WARNING|CAUTION)\]\s*\n)((?:^>.*$\n?)+)', flags=re.MULTILINE)
    
    def replace_callout(m):
        c_type = m.group(1).upper()
        content = m.group(2)
        cleaned_lines = [re.sub(r'^>\s?', '', l) for l in content.splitlines()]
        cleaned_text = "\n".join(cleaned_lines)
        return f'<div class="callout callout-{c_type.lower()}"><div class="callout-header"><span class="callout-badge">{c_type}</span></div><div class="callout-body">\n\n{cleaned_text}\n\n</div></div>\n\n'
    
    return callout_pattern.sub(replace_callout, text)

processed_md = convert_callouts(processed_md)

# Process Markdown using markdown-it
md = MarkdownIt().disable('linkify').enable('table')
html_body = md.render(processed_md)

# -------------------------------------------------------------
# 2. RESTORE MATH & ENHANCE HTML
# -------------------------------------------------------------
# Restore display math
for idx, (mtype, eq) in enumerate(math_storage):
    if mtype == 'display':
        html_body = html_body.replace(f'<p>@@MATH_DISPLAY_{idx}@@</p>', f'<div class="math-display">$${eq}$$</div>')
        html_body = html_body.replace(f'@@MATH_DISPLAY_{idx}@@', f'<div class="math-display">$${eq}$$</div>')
    else:
        html_body = html_body.replace(f'@@MATH_INLINE_{idx}@@', f'<span class="math-inline">${eq}$</span>')

# Wrap images with figure tags and captions
def enhance_images(src, alt):
    return f'''
    <figure class="guide-figure">
      <div class="img-wrapper">
        <img src="{src}" alt="{alt}" loading="eager" />
      </div>
      <figcaption>{alt}</figcaption>
    </figure>
    '''

html_body = re.sub(r'<img\s+src="([^"]+)"\s+alt="([^"]*)"\s*\/?>', lambda m: enhance_images(m.group(1), m.group(2)), html_body)

# Clean up any figure inside paragraph tags
html_body = re.sub(r'<p>\s*(<figure[\s\S]*?<\/figure>)\s*<\/p>', r'\1', html_body)

# Convert mermaid codeblocks to <pre class="mermaid">
html_body = re.sub(r'<pre><code class="language-mermaid">([\s\S]*?)<\/code><\/pre>', r'<pre class="mermaid">\1</pre>', html_body)

# -------------------------------------------------------------
# 3. CSS & PAGE TEMPLATE
# -------------------------------------------------------------
css_styles = """
  @import url('https://fonts.googleapis.com/css2?family=Sarabun:ital,wght@0,300;0,400;0,500;0,600;0,700;0,800;1,400&family=JetBrains+Mono:wght@400;500;600&family=Inter:wght@400;500;600;700;800&display=swap');

  @page {
    size: A4 portrait;
    margin: 16mm 14mm 16mm 14mm;
    @top-left {
      content: "คณะวิศวกรรมศาสตร์ มข. • Fundamental Electrical Engineering";
      font-family: 'Sarabun', 'Inter', sans-serif;
      font-size: 7.5pt;
      font-weight: 500;
      color: #94a3b8;
    }
    @top-right {
      content: "บทที่ 8: ระบบการจ่ายไฟฟ้ากำลัง (Power Distribution System)";
      font-family: 'Sarabun', 'Inter', sans-serif;
      font-size: 7.5pt;
      font-weight: 600;
      color: #b45309;
    }
    @bottom-left {
      content: "รศ.ดร. นรารัตน์ เรืองชัยจตุพร • คู่มือติวสอบไฟนอลฉบับสมบูรณ์";
      font-family: 'Sarabun', 'Inter', sans-serif;
      font-size: 7.5pt;
      color: #94a3b8;
    }
    @bottom-right {
      content: "หน้า " counter(page) " จาก " counter(pages);
      font-family: 'Inter', 'Sarabun', sans-serif;
      font-size: 8pt;
      font-weight: 600;
      color: #475569;
    }
  }

  * {
    box-sizing: border-box;
    -webkit-print-color-adjust: exact !important;
    print-color-adjust: exact !important;
  }

  body {
    font-family: 'Sarabun', 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
    color: #1e293b;
    background: #ffffff;
    line-height: 1.65;
    font-size: 9.8pt;
    margin: 0;
    padding: 0;
  }

  /* Cover / Hero Header */
  .guide-header {
    background: linear-gradient(135deg, #0f172a 0%, #78350f 45%, #b45309 80%, #d97706 100%);
    color: #ffffff;
    border-radius: 12px;
    padding: 24px 22px 20px 22px;
    margin-bottom: 24px;
    box-shadow: 0 4px 14px rgba(15, 23, 42, 0.15);
    page-break-after: avoid;
  }

  .header-badge {
    display: inline-block;
    padding: 3px 12px;
    background: rgba(255, 255, 255, 0.18);
    border: 1px solid rgba(255, 255, 255, 0.35);
    border-radius: 9999px;
    font-size: 8.5pt;
    font-weight: 600;
    letter-spacing: 0.5px;
    margin-bottom: 10px;
    text-transform: uppercase;
  }

  .header-title {
    font-size: 19pt;
    font-weight: 800;
    line-height: 1.25;
    margin: 0 0 8px 0;
    letter-spacing: -0.5px;
    color: #ffffff;
  }

  .header-subtitle {
    font-size: 10.5pt;
    font-weight: 400;
    opacity: 0.95;
    margin: 0 0 16px 0;
    line-height: 1.45;
  }

  .header-meta-row {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 12px;
    background: rgba(0, 0, 0, 0.28);
    padding: 10px 14px;
    border-radius: 8px;
    border: 1px solid rgba(255, 255, 255, 0.12);
    font-size: 8.2pt;
  }

  .meta-col strong {
    display: block;
    color: #fde68a;
    font-size: 7.5pt;
    text-transform: uppercase;
    letter-spacing: 0.5px;
    margin-bottom: 2px;
  }

  /* Headings */
  h1 {
    font-size: 16pt;
    font-weight: 800;
    color: #0f172a;
    border-bottom: 2px solid #b45309;
    padding-bottom: 6px;
    margin-top: 28px;
    margin-bottom: 14px;
    page-break-after: avoid;
  }

  h2 {
    font-size: 13pt;
    font-weight: 700;
    color: #92400e;
    border-left: 5px solid #d97706;
    padding-left: 10px;
    margin-top: 24px;
    margin-bottom: 12px;
    page-break-after: avoid;
  }

  h3 {
    font-size: 11pt;
    font-weight: 700;
    color: #0f172a;
    margin-top: 18px;
    margin-bottom: 8px;
    page-break-after: avoid;
  }

  h4 {
    font-size: 10pt;
    font-weight: 700;
    color: #334155;
    margin-top: 14px;
    margin-bottom: 6px;
    page-break-after: avoid;
  }

  p {
    margin: 0 0 10px 0;
    text-align: justify;
  }

  ul, ol {
    margin-top: 4px;
    margin-bottom: 12px;
    padding-left: 22px;
  }

  li {
    margin-bottom: 4px;
  }

  /* Figures & Captions */
  .guide-figure {
    margin: 16px auto;
    padding: 10px;
    background: #ffffff;
    border: 1px solid #cbd5e1;
    border-radius: 10px;
    text-align: center;
    page-break-inside: avoid;
    break-inside: avoid;
    box-shadow: 0 2px 6px rgba(0, 0, 0, 0.04);
    max-width: 96%;
  }

  .img-wrapper {
    display: flex;
    justify-content: center;
    align-items: center;
    background: #f8fafc;
    border-radius: 6px;
    padding: 8px;
  }

  .guide-figure img {
    max-width: 100%;
    max-height: 250px;
    object-fit: contain;
    border-radius: 4px;
    display: block;
    margin: 0 auto;
  }

  .guide-figure figcaption {
    font-size: 8.5pt;
    font-weight: 600;
    color: #475569;
    margin-top: 8px;
    line-height: 1.4;
    padding: 0 8px;
  }

  /* Tables */
  table {
    width: 100%;
    border-collapse: collapse;
    margin: 16px 0;
    font-size: 8.8pt;
    page-break-inside: avoid;
    break-inside: avoid;
    border: 1px solid #cbd5e1;
    border-radius: 6px;
    overflow: hidden;
  }

  th {
    background: #78350f;
    color: #ffffff;
    font-weight: 700;
    padding: 8px 10px;
    text-align: left;
    border: 1px solid #78350f;
  }

  td {
    padding: 7px 10px;
    border: 1px solid #e2e8f0;
    vertical-align: top;
  }

  tr:nth-child(even) td {
    background: #fdfaf6;
  }

  /* Math Blocks */
  .math-display {
    background: #f8fafc;
    border: 1px solid #e2e8f0;
    border-left: 4px solid #d97706;
    border-radius: 6px;
    padding: 8px 14px;
    margin: 12px 0;
    text-align: center;
    page-break-inside: avoid;
    break-inside: avoid;
    overflow-x: visible !important;
  }

  .math-inline {
    font-size: 1.02em;
  }

  /* Callout Boxes */
  .callout {
    border-radius: 8px;
    padding: 10px 14px;
    margin: 14px 0;
    page-break-inside: avoid;
    break-inside: avoid;
    border-left: 5px solid;
    font-size: 9.2pt;
    line-height: 1.55;
  }

  .callout-header {
    margin-bottom: 6px;
  }

  .callout-badge {
    display: inline-block;
    padding: 2px 7px;
    font-size: 7.5pt;
    font-weight: 700;
    border-radius: 4px;
    text-transform: uppercase;
    letter-spacing: 0.5px;
  }

  .callout-note {
    background: #eff6ff;
    border-left-color: #3b82f6;
    color: #1e3a8a;
  }
  .callout-note .callout-badge {
    background: #3b82f6;
    color: #ffffff;
  }

  .callout-tip {
    background: #ecfdf5;
    border-left-color: #10b981;
    color: #065f46;
  }
  .callout-tip .callout-badge {
    background: #10b981;
    color: #ffffff;
  }

  .callout-important {
    background: #f5f3ff;
    border-left-color: #8b5cf6;
    color: #5b21b6;
  }
  .callout-important .callout-badge {
    background: #8b5cf6;
    color: #ffffff;
  }

  .callout-warning, .callout-caution {
    background: #fffbeb;
    border-left-color: #f59e0b;
    color: #92400e;
  }
  .callout-warning .callout-badge, .callout-caution .callout-badge {
    background: #f59e0b;
    color: #ffffff;
  }

  /* Code & Pre */
  code {
    font-family: 'JetBrains Mono', monospace;
    font-size: 8.8pt;
    background: #f1f5f9;
    padding: 2px 5px;
    border-radius: 4px;
    color: #0f172a;
  }

  pre {
    background: #0f172a;
    color: #f8fafc;
    padding: 12px 14px;
    border-radius: 8px;
    font-family: 'JetBrains Mono', monospace;
    font-size: 8.5pt;
    line-height: 1.5;
    overflow-x: auto;
    page-break-inside: avoid;
  }

  pre.mermaid {
    background: #ffffff !important;
    color: #1e293b !important;
    text-align: center;
    border: 1px solid #cbd5e1;
    border-radius: 8px;
    padding: 14px;
    margin: 16px 0;
  }

  /* KaTeX Printing Critical Fix */
  .katex-display {
    margin: 6px 0 !important;
  }
  .katex {
    font-size: 1.03em !important;
  }
  .katex-mathml {
    display: none !important;
  }

  /* Strictly prevent radical bar stretching across the entire page */
  .katex .hide-tail,
  span.hide-tail {
    overflow: hidden !important;
    position: relative !important;
  }

  hr {
    border: 0;
    height: 1px;
    background: #e2e8f0;
    margin: 22px 0;
  }
"""

# Construct full HTML
html_document = f"""<!DOCTYPE html>
<html lang="th">
<head>
  <meta charset="UTF-8">
  <title>Chapter 8: Power Distribution System Comprehensive Mastery Guide</title>
  
  <!-- KaTeX Math CSS & JS -->
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/katex.min.css">
  <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/katex.min.js"></script>
  <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/contrib/auto-render.min.js"></script>
  
  <!-- Mermaid.js for Diagrams -->
  <script src="https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.min.js"></script>
  
  <style>
{css_styles}
  </style>
</head>
<body>

  <!-- Cover Header -->
  <div class="guide-header">
    <div class="header-badge">Faculty of Engineering • Khon Kaen University</div>
    <h1 class="header-title">คัมภีร์เจาะลึกบทที่ 8: ระบบการจ่ายไฟฟ้ากำลัง</h1>
    <div class="header-subtitle">Power Distribution System & National Grid Final Exam Comprehensive Mastery Guide</div>
    
    <div class="header-meta-row">
      <div class="meta-col">
        <strong>วิชา & ภาควิชา</strong>
        Fundamental Electrical Engineering (EE KKU)
      </div>
      <div class="meta-col">
        <strong>อาจารย์ผู้สอน</strong>
        รศ.ดร. นรารัตน์ เรืองชัยจตุพร
      </div>
      <div class="meta-col">
        <strong>โครงสร้างเนื้อหา</strong>
        21 รูปไดอะแกรมแท้ • 5 ข้อสอบจริง • สรุป 3 การไฟฟ้า และ AIS vs GIS
      </div>
    </div>
  </div>

  <!-- Content -->
  {html_body}

  <!-- KaTeX & Mermaid Initialization -->
  <script>
    mermaid.initialize({{
      startOnLoad: true,
      theme: 'neutral',
      flowchart: {{
        curve: 'basis',
        htmlLabels: true
      }}
    }});

    document.addEventListener("DOMContentLoaded", function() {{
      if (typeof renderMathInElement === 'function') {{
        renderMathInElement(document.body, {{
          delimiters: [
            {{left: '$$', right: '$$', display: true}},
            {{left: '$', right: '$', display: false}},
            {{left: '\\\\[', right: '\\\\]', display: true}},
            {{left: '\\\\(', right: '\\\\)', display: false}}
          ],
          throwOnError: false,
          output: 'html'
        }});
      }}
    }});
  </script>
</body>
</html>
"""

# Save HTML in Private-Flashcard
html_priv_path = os.path.join(base_dir, "Ch08_Power_Distribution_Comprehensive_Guide.html")
with open(html_priv_path, 'w', encoding='utf-8') as f:
    f.write(html_document)
print(f"Saved HTML to: {html_priv_path}")

# Save HTML in Fund E N'Manow
html_fund_path = os.path.join(fund_e_dir, "Ch08_Power_Distribution_Comprehensive_Guide.html")
with open(html_fund_path, 'w', encoding='utf-8') as f:
    f.write(html_document)
print(f"Saved HTML to: {html_fund_path}")

# Run Microsoft Edge Headless to compile PDF
pdf_priv_path = os.path.join(base_dir, "Ch08_Power_Distribution_Comprehensive_Guide.pdf")
pdf_fund_path = os.path.join(fund_e_dir, "Ch08_Power_Distribution_Comprehensive_Guide.pdf")

edge_path = r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe'
if not os.path.exists(edge_path):
    edge_path = r'C:\Program Files\Google\Chrome\Application\chrome.exe'

print(f"\nCompiling PDF via {edge_path} ...")
cmd = [
    edge_path,
    '--headless=new',
    '--disable-gpu',
    '--virtual-time-budget=12000',
    '--run-all-compositor-stages-before-draw',
    '--no-pdf-header-footer',
    f'--print-to-pdf={pdf_priv_path}',
    html_priv_path
]

res = subprocess.run(cmd, capture_output=True, text=True)
if res.returncode == 0 and os.path.exists(pdf_priv_path):
    size_mb = os.path.getsize(pdf_priv_path) / (1024 * 1024)
    print(f"✅ SUCCESS: Generated PDF at {pdf_priv_path} ({size_mb:.2f} MB)")
    shutil.copy2(pdf_priv_path, pdf_fund_path)
    print(f"✅ Copied PDF to {pdf_fund_path}")
else:
    print(f"❌ Error compiling PDF: code {res.returncode}")
    print(res.stderr)
