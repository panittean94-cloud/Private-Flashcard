# -*- coding: utf-8 -*-
"""
build_en_guides.py
Compiles English Mastery Guides for Ch06 and Ch08 into HTML, PDF, and Word (.docx).
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
edge_path = r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe'
if not os.path.exists(edge_path):
    edge_path = r'C:\Program Files\Google\Chrome\Application\chrome.exe'

css_styles = """
  @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=JetBrains+Mono:wght@400;500;600&display=swap');

  @page {
    size: A4 portrait;
    margin: 16mm 14mm 16mm 14mm;
    @top-left {
      content: "Faculty of Engineering, KKU • Fundamental Electrical Engineering";
      font-family: 'Inter', sans-serif;
      font-size: 7.5pt;
      font-weight: 500;
      color: #94a3b8;
    }
    @top-right {
      content: attr(data-header);
      font-family: 'Inter', sans-serif;
      font-size: 7.5pt;
      font-weight: 600;
      color: #2563eb;
    }
    @bottom-left {
      content: "Assoc. Prof. Dr. Nararat Ruangchaijatupon • Comprehensive Exam Guide";
      font-family: 'Inter', sans-serif;
      font-size: 7.5pt;
      color: #94a3b8;
    }
    @bottom-right {
      content: "Page " counter(page) " of " counter(pages);
      font-family: 'Inter', sans-serif;
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
    font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
    color: #1e293b;
    background: #ffffff;
    line-height: 1.65;
    font-size: 9.8pt;
    margin: 0;
    padding: 0;
  }

  .guide-header {
    background: linear-gradient(135deg, #0f172a 0%, #1e3a8a 55%, #0284c7 100%);
    color: #ffffff;
    border-radius: 12px;
    padding: 24px 22px 20px 22px;
    margin-bottom: 24px;
    box-shadow: 0 4px 14px rgba(15, 23, 42, 0.15);
    page-break-after: avoid;
  }

  .guide-header.ch08 {
    background: linear-gradient(135deg, #0f172a 0%, #78350f 45%, #b45309 80%, #d97706 100%);
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
    color: #38bdf8;
    font-size: 7.5pt;
    text-transform: uppercase;
    letter-spacing: 0.5px;
    margin-bottom: 2px;
  }
  .guide-header.ch08 .meta-col strong {
    color: #fde68a;
  }

  h1 {
    font-size: 16pt;
    font-weight: 800;
    color: #0f172a;
    border-bottom: 2px solid #2563eb;
    padding-bottom: 6px;
    margin-top: 28px;
    margin-bottom: 14px;
    page-break-after: avoid;
  }
  .ch08-theme h1 {
    border-bottom-color: #b45309;
  }

  h2 {
    font-size: 13pt;
    font-weight: 700;
    color: #1e3a8a;
    border-left: 5px solid #2563eb;
    padding-left: 10px;
    margin-top: 24px;
    margin-bottom: 12px;
    page-break-after: avoid;
  }
  .ch08-theme h2 {
    color: #92400e;
    border-left-color: #d97706;
  }

  h3 {
    font-size: 11pt;
    font-weight: 700;
    color: #0f172a;
    margin-top: 18px;
    margin-bottom: 8px;
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
    background: #1e3a8a;
    color: #ffffff;
    font-weight: 700;
    padding: 8px 10px;
    text-align: left;
    border: 1px solid #1e3a8a;
  }
  .ch08-theme th {
    background: #78350f;
    border-color: #78350f;
  }

  td {
    padding: 7px 10px;
    border: 1px solid #e2e8f0;
    vertical-align: top;
  }

  tr:nth-child(even) td {
    background: #f8fafc;
  }

  .math-display {
    background: #f8fafc;
    border: 1px solid #e2e8f0;
    border-left: 4px solid #0284c7;
    border-radius: 6px;
    padding: 8px 14px;
    margin: 12px 0;
    text-align: center;
    page-break-inside: avoid;
    break-inside: avoid;
    overflow-x: visible !important;
  }
  .ch08-theme .math-display {
    border-left-color: #d97706;
  }

  .math-inline {
    font-size: 1.02em;
  }

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

  .katex-display {
    margin: 6px 0 !important;
  }
  .katex {
    font-size: 1.03em !important;
  }
  .katex-mathml {
    display: none !important;
  }

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

def compile_guide(md_filename, html_filename, pdf_filename, docx_filename, is_ch08=False):
    src_md = os.path.join(base_dir, md_filename)
    with open(src_md, 'r', encoding='utf-8') as f:
        raw_md = f.read()

    # Pre-process math
    math_storage = []
    def stash_display(m):
        idx = len(math_storage)
        math_storage.append(('display', m.group(1).strip()))
        return f"\n\n@@MATH_DISPLAY_{idx}@@\n\n"

    def stash_inline(m):
        idx = len(math_storage)
        math_storage.append(('inline', m.group(1).strip()))
        return f"@@MATH_INLINE_{idx}@@"

    processed = re.sub(r'\$\$(.*?)\$\$', stash_display, raw_md, flags=re.DOTALL)
    processed = re.sub(r'(?<!\$)\$(?!\$)(.*?)(?<!\$)\$(?!\$)', stash_inline, processed)

    def convert_callouts(text):
        pat = re.compile(r'(?:^> ?\[!(NOTE|TIP|IMPORTANT|WARNING|CAUTION)\]\s*\n)((?:^>.*$\n?)+)', flags=re.MULTILINE)
        def repl(m):
            ctype = m.group(1).upper()
            content = "\n".join([re.sub(r'^>\s?', '', l) for l in m.group(2).splitlines()])
            return f'<div class="callout callout-{ctype.lower()}"><div class="callout-header"><span class="callout-badge">{ctype}</span></div><div class="callout-body">\n\n{content}\n\n</div></div>\n\n'
        return pat.sub(repl, text)

    processed = convert_callouts(processed)
    md = MarkdownIt().disable('linkify').enable('table')
    body = md.render(processed)

    for idx, (mtype, eq) in enumerate(math_storage):
        if mtype == 'display':
            body = body.replace(f'<p>@@MATH_DISPLAY_{idx}@@</p>', f'<div class="math-display">$${eq}$$</div>')
            body = body.replace(f'@@MATH_DISPLAY_{idx}@@', f'<div class="math-display">$${eq}$$</div>')
        else:
            body = body.replace(f'@@MATH_INLINE_{idx}@@', f'<span class="math-inline">${eq}$</span>')

    body = re.sub(r'<img\s+src="([^"]+)"\s+alt="([^"]*)"\s*\/?>', r'<figure class="guide-figure"><div class="img-wrapper"><img src="\1" alt="\2" /></div><figcaption>\2</figcaption></figure>', body)
    body = re.sub(r'<p>\s*(<figure[\s\S]*?<\/figure>)\s*<\/p>', r'\1', body)
    body = re.sub(r'<pre><code class="language-mermaid">([\s\S]*?)<\/code><\/pre>', r'<pre class="mermaid">\1</pre>', body)

    ch_class = "ch08" if is_ch08 else ""
    theme_class = "ch08-theme" if is_ch08 else ""
    header_title = "Chapter 8: Power Distribution Systems" if is_ch08 else "Chapter 6: Three-Phase AC Circuits"
    sub_title = "Power Distribution System & National Grid Final Exam Mastery Guide" if is_ch08 else "Three-Phase AC Circuits Comprehensive Final Exam Mastery Guide"
    meta_structure = "21 Diagrams • 5 Exam Problems • AIS vs GIS" if is_ch08 else "16 Diagrams • 5 Exam Problems • Full Mathematical Proofs"

    html_doc = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>{header_title} - Mastery Guide</title>
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/katex.min.css">
  <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/katex.min.js"></script>
  <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/contrib/auto-render.min.js"></script>
  <script src="https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.min.js"></script>
  <style>
{css_styles}
  </style>
</head>
<body class="{theme_class}">
  <div class="guide-header {ch_class}">
    <div class="header-badge">Faculty of Engineering • Khon Kaen University</div>
    <h1 class="header-title">{header_title}</h1>
    <div class="header-subtitle">{sub_title}</div>
    <div class="header-meta-row">
      <div class="meta-col">
        <strong>Course & Dept</strong>
        Fundamental Electrical Engineering (EE KKU)
      </div>
      <div class="meta-col">
        <strong>Instructor</strong>
        Assoc. Prof. Dr. Nararat Ruangchaijatupon
      </div>
      <div class="meta-col">
        <strong>Coverage</strong>
        {meta_structure}
      </div>
    </div>
  </div>

  {body}

  <script>
    mermaid.initialize({{
      startOnLoad: true,
      theme: 'neutral',
      flowchart: {{ curve: 'basis', htmlLabels: true }}
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
</html>"""

    # Save HTML
    priv_html = os.path.join(base_dir, html_filename)
    fund_html = os.path.join(fund_e_dir, html_filename)
    with open(priv_html, 'w', encoding='utf-8') as f:
        f.write(html_doc)
    shutil.copy2(priv_html, fund_html)
    print(f"Generated HTML: {priv_html}")

    # Compile PDF via Edge
    priv_pdf = os.path.join(base_dir, pdf_filename)
    fund_pdf = os.path.join(fund_e_dir, pdf_filename)
    cmd = [
        edge_path,
        '--headless=new',
        '--disable-gpu',
        '--virtual-time-budget=12000',
        '--run-all-compositor-stages-before-draw',
        '--no-pdf-header-footer',
        f'--print-to-pdf={priv_pdf}',
        priv_html
    ]
    res = subprocess.run(cmd, capture_output=True, text=True)
    if res.returncode == 0 and os.path.exists(priv_pdf):
        mb = os.path.getsize(priv_pdf) / (1024 * 1024)
        shutil.copy2(priv_pdf, fund_pdf)
        print(f"✅ Generated PDF: {priv_pdf} ({mb:.2f} MB)")
    else:
        print(f"❌ Error compiling {pdf_filename}:", res.stderr)

    # Compile Word (.docx) via Pandoc
    priv_docx = os.path.join(base_dir, docx_filename)
    fund_docx = os.path.join(fund_e_dir, docx_filename)
    pandoc_cmd = ['pandoc', '-f', 'markdown', '-t', 'docx', '-o', priv_docx, src_md]
    res_p = subprocess.run(pandoc_cmd, capture_output=True, text=True)
    if res_p.returncode == 0 and os.path.exists(priv_docx):
        shutil.copy2(priv_docx, fund_docx)
        print(f"✅ Generated Word (.docx): {priv_docx}")
    else:
        print(f"❌ Error compiling {docx_filename}:", res_p.stderr)

# 1. Compile Chapter 6 EN
print("=== COMPILING CHAPTER 6 ENGLISH MASTER GUIDE ===")
compile_guide("Ch06_Three_Phase_Comprehensive_Guide_EN.md", 
              "Ch06_Three_Phase_Comprehensive_Guide_EN.html", 
              "Ch06_Three_Phase_Comprehensive_Guide_EN.pdf", 
              "Ch06_Three_Phase_Comprehensive_Guide_EN.docx", 
              is_ch08=False)

# 2. Compile Chapter 8 EN
print("\n=== COMPILING CHAPTER 8 ENGLISH MASTER GUIDE ===")
compile_guide("Ch08_Power_Distribution_Comprehensive_Guide_EN.md", 
              "Ch08_Power_Distribution_Comprehensive_Guide_EN.html", 
              "Ch08_Power_Distribution_Comprehensive_Guide_EN.pdf", 
              "Ch08_Power_Distribution_Comprehensive_Guide_EN.docx", 
              is_ch08=True)

print("\nALL ENGLISH GUIDES BUILT AND COPIED SUCCESSFULLY!")
