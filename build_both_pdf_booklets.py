# -*- coding: utf-8 -*-
"""
build_both_pdf_booklets.py
Generates both:
1. FunE_Final_Exam_Flashcards_TH_ENG_Ch6_10.pdf (Thai with English Technical Transliteration)
2. FunE_Final_Exam_Master_Flashcards_Ch6_10.pdf (English Master Booklet)
"""

import os
import sys
import json
import subprocess
import shutil

sys.stdout.reconfigure(encoding='utf-8')

base_dir = r"c:\Users\thana\Desktop\Private-Flashcard"
fund_e_dir = r"c:\Users\thana\Desktop\Fund E N'Manow"
json_path = os.path.join(base_dir, "data", "flashcards.json")

with open(json_path, 'r', encoding='utf-8') as f:
    cards = json.load(f)

print(f"Loaded {len(cards)} cards from {json_path}")

chapters_order = [
    "Chapter 6",
    "Chapter 7",
    "Chapter 8",
    "Chapter 9",
    "Chapter 10"
]

chapter_meta = {
    "Chapter 6": {
        "title_en": "Chapter 6: Three-Phase Circuits",
        "title_th": "บทที่ 6: วงจรไฟฟ้ากระแสสลับ 3 เฟส (Three-Phase Circuits)",
        "sub_en": "Balanced & Unbalanced Y-Y, Y-Δ, Complex Power, Neutral Shift, 2-Wattmeter Method",
        "sub_th": "ระบบ Y-Y สมดุล/ไม่สมดุล, โหลดเดลตา Y-Δ, กำลังไฟฟ้าเชิงซ้อน, แรงดันจุดนิวทรัลเลื่อน, การวัดกำลังด้วย 2 วัตต์มิเตอร์"
    },
    "Chapter 7": {
        "title_en": "Chapter 7: Electric Machinery & Transformers",
        "title_th": "บทที่ 7: เครื่องจักรกลไฟฟ้าและหม้อแปลงไฟฟ้า (Machinery & Transformers)",
        "sub_en": "Right-Hand Rule, DC Shunt/Series Motors & Generators, Induction Motors, Slip, Power Transformers & Tests",
        "sub_th": "กฎมือขวา, มอเตอร์กระแสตรงชันต์/อนุกรม, เจเนอเรเตอร์, มอเตอร์เหนี่ยวนำ, สลิป, หม้อแปลง 1 เฟส, 25 kVA, การทดสอบ OC/SC"
    },
    "Chapter 8": {
        "title_en": "Chapter 8: Power Distribution System",
        "title_th": "บทที่ 8: ระบบการจ่ายไฟฟ้ากำลัง (Power Distribution System)",
        "sub_en": "EGAT 4 Voltage Levels, EGAT 5 Power Plant Types, MEA & PEA Networks, Service Connections & Substations",
        "sub_th": "4 ระดับแรงดันสายส่ง, 5 ประเภทโรงไฟฟ้า กฟผ., ระบบจำหน่าย กฟน./กฟภ., มิเตอร์และการต่อไฟ, สถานีไฟฟ้าย่อย"
    },
    "Chapter 9": {
        "title_en": "Chapter 9: Electrical Measuring Instruments & Sensors",
        "title_th": "บทที่ 9: เครื่องมือวัดและเซนเซอร์ทางไฟฟ้า (Measuring Instruments & Sensors)",
        "sub_en": "PMMC Principles, DC Ammeters & Voltmeters with CDRX, Ayrton Shunts, Ohmmeters, Wattmeters, Accuracy",
        "sub_th": "มิเตอร์ PMMC, การออกแบบแอมมิเตอร์/โวลต์มิเตอร์ร่วมกับ CDRX, ชันต์แอร์ตัน, โอห์มมิเตอร์, วัตต์มิเตอร์, ความแม่นยำ"
    },
    "Chapter 10": {
        "title_en": "Chapter 10: Semiconductor & Electronic Devices",
        "title_th": "บทที่ 10: อุปกรณ์สารกึ่งตัวนำและวงจรอิเล็กทรอนิกส์ (Semiconductor & Electronic Devices)",
        "sub_en": "Intrinsic/Extrinsic, PN Diodes, Zener Regulators, Solar Cells, BJTs, MOSFETs, Rectifiers, Op-Amps",
        "sub_th": "สาร N-Type/P-Type, ไดโอดรอยต่อ PN, วงจรซีเนอร์คุมแรงดัน, เซลล์แสงอาทิตย์, ทรานซิสเตอร์ BJT, มอสเฟต, ออปแอมป์"
    }
}

cards_by_ch = {}
for ch in chapters_order:
    cards_by_ch[ch] = [c for c in cards if c['chapter'] == ch]

def format_equation_block(formula_str):
    if not formula_str:
        return ""
    # Split equations separated by double newlines or single newlines
    blocks = formula_str.split("\n\n")
    html_blocks = []
    for b in blocks:
        b_clean = b.strip()
        if b_clean:
            html_blocks.append(f'<div class="formula-line">{b_clean}</div>')
    return "\n".join(html_blocks)

def format_text_lines(text):
    if not text:
        return ""
    paragraphs = text.split("\n\n")
    html_p = []
    for p in paragraphs:
        lines = p.split("\n")
        joined_lines = "<br/>".join(lines)
        html_p.append(f'<p class="card-p">{joined_lines}</p>')
    return "\n".join(html_p)

# Common CSS Stylesheet for PDF
css_styles = """
  @import url('https://fonts.googleapis.com/css2?family=Sarabun:wght@300;400;500;600;700;800&family=JetBrains+Mono:wght@400;500;600&family=Inter:wght@400;500;600;700&display=swap');
  
  @page {
    size: A4 portrait;
    margin: 12mm 10mm 14mm 10mm;
    @bottom-right {
      content: "Page " counter(page) " of " counter(pages);
      font-family: 'Inter', 'Sarabun', sans-serif;
      font-size: 8pt;
      color: #64748b;
    }
  }

  * {
    box-sizing: border-box;
    -webkit-print-color-adjust: exact !important;
    print-color-adjust: exact !important;
  }

  body {
    font-family: 'Inter', 'Sarabun', sans-serif;
    color: #1e293b;
    background: #ffffff;
    line-height: 1.55;
    font-size: 9.5pt;
    margin: 0;
    padding: 0;
  }

  /* Cover Header */
  .cover-container {
    text-align: center;
    padding: 24px 16px 20px 16px;
    background: linear-gradient(135deg, #0f172a 0%, #1e3a8a 50%, #0369a1 100%);
    color: #ffffff;
    border-radius: 12px;
    margin-bottom: 22px;
    page-break-after: avoid;
    box-shadow: 0 4px 12px rgba(15, 23, 42, 0.15);
  }

  .cover-badge {
    display: inline-block;
    padding: 4px 12px;
    background: rgba(255, 255, 255, 0.15);
    border: 1px solid rgba(255, 255, 255, 0.3);
    border-radius: 9999px;
    font-size: 8.5pt;
    font-weight: 600;
    letter-spacing: 0.5px;
    margin-bottom: 10px;
    text-transform: uppercase;
  }

  .cover-title {
    font-size: 19pt;
    font-weight: 800;
    margin: 0 0 6px 0;
    letter-spacing: -0.5px;
    line-height: 1.25;
  }

  .cover-subtitle {
    font-size: 11pt;
    font-weight: 500;
    opacity: 0.92;
    margin-bottom: 14px;
  }

  .cover-meta-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 10px;
    background: rgba(0, 0, 0, 0.25);
    padding: 10px 14px;
    border-radius: 8px;
    font-size: 8pt;
    text-align: left;
    border: 1px solid rgba(255, 255, 255, 0.1);
  }

  .meta-item strong {
    display: block;
    color: #38bdf8;
    font-size: 7.5pt;
    text-transform: uppercase;
    letter-spacing: 0.5px;
    margin-bottom: 2px;
  }

  /* Chapter Divider */
  .chapter-divider {
    background: #f1f5f9;
    border-left: 6px solid #2563eb;
    padding: 12px 14px;
    margin: 22px 0 14px 0;
    border-radius: 0 8px 8px 0;
    page-break-inside: avoid;
    page-break-after: avoid;
  }

  .chapter-badge {
    display: inline-block;
    padding: 2px 7px;
    background: #2563eb;
    color: #ffffff;
    font-size: 7.5pt;
    font-weight: 700;
    border-radius: 4px;
    margin-bottom: 4px;
    letter-spacing: 0.5px;
  }

  .chapter-title {
    font-size: 13pt;
    font-weight: 700;
    color: #0f172a;
    margin: 0 0 3px 0;
  }

  .chapter-subtitle {
    font-size: 8.5pt;
    color: #64748b;
    margin: 0;
  }

  /* Flashcard Item */
  .card-item {
    border: 1px solid #cbd5e1;
    border-radius: 10px;
    padding: 12px 14px;
    margin-bottom: 15px;
    background: #ffffff;
    page-break-inside: avoid;
    box-shadow: 0 1px 3px rgba(0, 0, 0, 0.05);
  }

  .card-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    border-bottom: 1px solid #e2e8f0;
    padding-bottom: 6px;
    margin-bottom: 8px;
  }

  .card-header-left {
    display: flex;
    align-items: center;
    gap: 6px;
  }

  .card-id {
    font-family: 'JetBrains Mono', monospace;
    font-size: 8.5pt;
    font-weight: 700;
    color: #ffffff;
    background: #0f172a;
    padding: 2px 7px;
    border-radius: 4px;
  }

  .card-chapter-tag {
    font-size: 8pt;
    font-weight: 600;
    color: #1e40af;
    background: #dbeafe;
    padding: 2px 7px;
    border-radius: 4px;
  }

  .card-diff-tag {
    font-size: 7.5pt;
    font-weight: 600;
    padding: 2px 7px;
    border-radius: 9999px;
  }

  .badge-concept {
    background: #dcfce7;
    color: #15803d;
  }

  .badge-calc {
    background: #fee2e2;
    color: #b91c1c;
  }

  .card-ref-tag {
    font-size: 7.5pt;
    color: #475569;
    background: #f1f5f9;
    padding: 2px 8px;
    border-radius: 4px;
    font-weight: 500;
  }

  .card-topic {
    font-size: 11pt;
    font-weight: 700;
    color: #0f172a;
    margin: 0 0 8px 0;
    line-height: 1.35;
  }

  /* Question Box */
  .card-question-box {
    background: #f8fafc;
    border: 1px solid #e2e8f0;
    border-radius: 6px;
    padding: 9px 12px;
    margin-bottom: 9px;
  }

  .section-label {
    font-size: 7.5pt;
    font-weight: 700;
    color: #475569;
    text-transform: uppercase;
    letter-spacing: 0.5px;
    margin-bottom: 4px;
    display: flex;
    align-items: center;
    gap: 4px;
  }

  .card-question-text {
    font-size: 9.5pt;
    font-weight: 500;
    color: #1e293b;
    line-height: 1.55;
    white-space: pre-line;
  }

  /* Diagram Box */
  .card-diagram-box {
    text-align: center;
    margin: 8px 0;
    padding: 6px;
    background: #ffffff;
    border: 1px solid #e2e8f0;
    border-radius: 6px;
  }

  .card-diagram-img {
    max-height: 160px;
    max-width: 95%;
    object-contain: contain;
    margin: 0 auto;
    display: block;
    border-radius: 4px;
  }

  .card-diagram-caption {
    font-size: 7.5pt;
    color: #64748b;
    margin-top: 4px;
    font-weight: 500;
    font-style: italic;
  }

  /* Formula Box - Separated equation lines */
  .card-formula-box {
    background: #eff6ff;
    border-left: 4px solid #3b82f6;
    border-radius: 4px;
    padding: 8px 12px;
    margin-bottom: 9px;
  }

  .card-formula-box .section-label {
    color: #1d4ed8;
  }

  .formula-line {
    margin: 4px 0;
    line-height: 1.6;
    overflow-x: visible !important;
  }

  /* Solution Box */
  .card-solution-box {
    background: #f0fdf4;
    border-left: 4px solid #10b981;
    border-radius: 4px;
    padding: 8px 12px;
    margin-bottom: 9px;
  }

  .card-solution-box .section-label {
    color: #047857;
  }

  .card-solution-content {
    font-size: 9pt;
    color: #0f172a;
    line-height: 1.55;
  }

  .card-p {
    margin: 0 0 6px 0;
  }
  .card-p:last-child {
    margin-bottom: 0;
  }

  /* Pitfall Box */
  .card-pitfall-box {
    background: #fffbeb;
    border-left: 4px solid #f59e0b;
    border-radius: 4px;
    padding: 7px 11px;
    font-size: 8.5pt;
    color: #92400e;
    line-height: 1.5;
  }

  .card-pitfall-box .section-label {
    color: #b45309;
  }

  /* KaTeX Math Tweaks */
  .katex-display {
    margin: 4px 0 !important;
  }
  .katex {
    font-size: 1.02em !important;
  }
  .katex-mathml {
    display: none !important;
  }

  /* Fix KaTeX square root (radical) stretching: hide-tail MUST remain overflow: hidden */
  .katex .hide-tail,
  span.hide-tail {
    overflow: hidden !important;
    position: relative !important;
  }
"""

def generate_booklet_html(lang="th"):
    is_th = (lang == "th")
    
    doc_title = "FunE Final Exam Master Flashcards (Bilingual TH / ENG)" if is_th else "FunE Final Exam Master Flashcards (English Master)"
    badge_text = "คณะวิศวกรรมศาสตร์ • มหาวิทยาลัยขอนแก่น" if is_th else "Faculty of Engineering • Khon Kaen University"
    main_title = "Fundamental Electrical Engineering (FunE)"
    sub_title = f"โพยสรุปและข้อสอบไฟนอลวิชาฟันอี {len(cards)} ข้อ ครบทุกบท (ภาษาไทย ทับศัพท์ ENG)" if is_th else f"Final Exam Master Flashcards & Solved Problems Booklet ({len(cards)} Cards)"
    
    meta_prof_label = "อาจารย์ผู้สอน & ภาควิชา" if is_th else "Course & Instructor"
    meta_prof = "รศ.ดร. นรารัตน์ เรืองชัยจตุพร (วิศวกรรมไฟฟ้า)" if is_th else "Assoc. Prof. Nararat Ruangchaijatupon"
    
    meta_cov_label = "เนื้อหาที่ครอบคลุม" if is_th else "Coverage"
    meta_cov = "บทที่ 6, 7, 8, 9 และ 10 ครบตามสไลด์ อ.นรารัตน์ (100% Complete)" if is_th else "Chapters 6, 7, 8, 9 & 10 (100% Complete Syllabus)"
    
    meta_inc_label = "องค์ประกอบในเล่ม" if is_th else "Content Inclusions"
    meta_inc = f"{len(cards)} การ์ดโจทย์ • ไดอะแกรมแท้จากสไลด์และข้อสอบ • สมการแยกบรรทัดละเอียด" if is_th else f"{len(cards)} Cards • Authentic Slide & Exam Diagrams • Line-by-Line Math"

    cards_html = []
    
    for ch_idx, ch in enumerate(chapters_order):
        ch_cards = cards_by_ch[ch]
        ch_title = chapter_meta[ch]["title_th"] if is_th else chapter_meta[ch]["title_en"]
        ch_sub = chapter_meta[ch]["sub_th"] if is_th else chapter_meta[ch]["sub_en"]
        
        cards_html.append(f"""
        <div class="chapter-divider">
          <div class="chapter-badge">PART {ch_idx + 1}</div>
          <h2 class="chapter-title">{ch_title}</h2>
          <p class="chapter-subtitle">{ch_sub} ({len(ch_cards)} Flashcards)</p>
        </div>
        """)
        
        for c in ch_cards:
            is_calc = ("Level 2" in c.get('level', '')) or ("Level 3" in c.get('level', ''))
            diff_class = "badge-calc" if is_calc else "badge-concept"
            if is_th:
                diff_text = "🔴 ข้อสอบจริง / คำนวณ" if is_calc else "🟢 แนวคิดสำคัญ (Concept)"
            else:
                diff_text = "🔴 Level 2 (Exam / Calc)" if is_calc else "🟢 Level 1 (Core Concept)"
            
            topic = c.get('topic_th', c['topic']) if is_th else c['topic']
            question = c.get('question_th', c['question']) if is_th else c['question']
            solution = c.get('solution_th', c['solution']) if is_th else c['solution']
            pitfall = c.get('pitfall_th', c['pitfall']) if is_th else c['pitfall']
            
            q_label = "📌 คำถาม / โจทย์ข้อสอบจริง (PROBLEM / QUESTION):" if is_th else "📌 PROBLEM / QUESTION:"
            formula_label = "📐 สูตรสำคัญ & นิยาม (FORMULAS & DEFINITIONS):" if is_th else "📐 KEY FORMULAS & DEFINITIONS:"
            sol_label = "📝 เฉลยละเอียดและวิธีคิด (STEP-BY-STEP SOLUTION):" if is_th else "📝 STEP-BY-STEP MODEL SOLUTION:"
            pit_label = "⚠️ จุดระวังข้อสอบ & เทคนิคตัดคะแนน (EXAM PITFALL & TIPS):" if is_th else "⚠️ EXAM PITFALL & CAUTION:"

            # Format formula
            formula_html = ""
            if c.get('formula'):
                formula_html = f"""
                <div class="card-formula-box">
                  <div class="section-label">{formula_label}</div>
                  <div class="card-formula-content">
                    {format_equation_block(c['formula'])}
                  </div>
                </div>
                """
            
            # Format diagram
            diagram_html = ""
            if c.get('diagram'):
                diag_caption = c.get('diagram_caption_th' if is_th else 'diagram_caption', 'Diagram')
                diagram_html = f"""
                <div class="card-diagram-box">
                  <img src="{c['diagram']}" alt="{diag_caption}" class="card-diagram-img" />
                  <div class="card-diagram-caption">รูปประกอบ: {diag_caption}</div>
                </div>
                """

            # Format solution
            solution_html = ""
            if solution:
                solution_html = f"""
                <div class="card-solution-box">
                  <div class="section-label">{sol_label}</div>
                  <div class="card-solution-content">
                    {format_text_lines(solution)}
                  </div>
                </div>
                """

            # Format pitfall
            pitfall_html = ""
            if pitfall:
                pitfall_html = f"""
                <div class="card-pitfall-box">
                  <div class="section-label">{pit_label}</div>
                  <div class="card-pitfall-content">
                    {format_text_lines(pitfall)}
                  </div>
                </div>
                """

            cards_html.append(f"""
            <div class="card-item">
              <div class="card-header">
                <div class="card-header-left">
                  <span class="card-id">{c['id']}</span>
                  <span class="card-chapter-tag">{c['chapter']}</span>
                  <span class="card-diff-tag {diff_class}">{diff_text}</span>
                </div>
                <div class="card-header-right">
                  <span class="card-ref-tag">📌 {c.get('exam_reference', 'Final Exam')}</span>
                </div>
              </div>
              
              <h3 class="card-topic">{topic}</h3>
              
              <div class="card-question-box">
                <div class="section-label">{q_label}</div>
                <div class="card-question-text">{question}</div>
              </div>
              
              {diagram_html}
              {formula_html}
              {solution_html}
              {pitfall_html}
            </div>
            """)

    return f"""<!DOCTYPE html>
<html lang="{lang}">
<head>
  <meta charset="UTF-8">
  <title>{doc_title}</title>
  
  <!-- KaTeX CSS & JS for Math Rendering -->
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/katex.min.css">
  <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/katex.min.js"></script>
  <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/contrib/auto-render.min.js"></script>
  
  <style>
{css_styles}
  </style>
</head>
<body>

  <!-- Cover Banner -->
  <div class="cover-container">
    <div class="cover-badge">{badge_text}</div>
    <h1 class="cover-title">{main_title}</h1>
    <div class="cover-subtitle">{sub_title}</div>
    
    <div class="cover-meta-grid">
      <div class="meta-item">
        <strong>{meta_prof_label}</strong>
        {meta_prof}
      </div>
      <div class="meta-item">
        <strong>{meta_cov_label}</strong>
        {meta_cov}
      </div>
      <div class="meta-item">
        <strong>{meta_inc_label}</strong>
        {meta_inc}
      </div>
    </div>
  </div>

  <!-- Cards -->
  {"".join(cards_html)}

  <script>
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

# Compile both booklets
def build_pdf(html_content, html_filename, pdf_filename):
    html_file = os.path.join(base_dir, html_filename)
    pdf_file = os.path.join(base_dir, pdf_filename)
    fund_e_pdf_file = os.path.join(fund_e_dir, pdf_filename)
    
    with open(html_file, 'w', encoding='utf-8') as f:
        f.write(html_content)
    print(f"Generated HTML booklet: {html_file}")
    
    edge_path = r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe'
    if not os.path.exists(edge_path):
        edge_path = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
    
    print(f"Compiling PDF using {edge_path} -> {pdf_filename} ...")
    cmd = [
        edge_path,
        '--headless=new',
        '--disable-gpu',
        '--virtual-time-budget=9000',
        '--no-pdf-header-footer',
        f'--print-to-pdf={pdf_file}',
        html_file
    ]
    
    res = subprocess.run(cmd, capture_output=True, text=True)
    if res.returncode == 0 and os.path.exists(pdf_file):
        mb = os.path.getsize(pdf_file) / (1024 * 1024)
        print(f"✅ SUCCESS: {pdf_filename} ({mb:.2f} MB)")
        shutil.copy2(pdf_file, fund_e_pdf_file)
        print(f"Copied to: {fund_e_pdf_file}")
    else:
        print(f"❌ Error compiling {pdf_filename}: returncode={res.returncode}")
        print(res.stderr)

# 1. Build Thai Booklet
print("=== BUILDING THAI BOOKLET (FunE_Final_Exam_Flashcards_TH_ENG_Ch6_10.pdf) ===")
th_html = generate_booklet_html(lang="th")
build_pdf(th_html, "flashcards_booklet_th.html", "FunE_Final_Exam_Flashcards_TH_ENG_Ch6_10.pdf")

# 2. Build English Booklet
print("\n=== BUILDING ENGLISH BOOKLET (FunE_Final_Exam_Master_Flashcards_Ch6_10.pdf) ===")
en_html = generate_booklet_html(lang="en")
build_pdf(en_html, "flashcards_booklet.html", "FunE_Final_Exam_Master_Flashcards_Ch6_10.pdf")

# 3. Copy Excel to Fund E N'Manow
excel_src = os.path.join(base_dir, "FunE_Master_Exam_Flashcards_Ch6_10_Master.xlsx")
excel_dest = os.path.join(fund_e_dir, "FunE_Master_Exam_Flashcards_Ch6_10_Master.xlsx")
if os.path.exists(excel_src):
    try:
        shutil.copy2(excel_src, excel_dest)
        print(f"\nCopied master Excel to: {excel_dest}")
    except PermissionError:
        print(f"\nNotice: {excel_dest} is currently open in Excel. Saved locally at {excel_src}")

print("\nALL PDF BOOKLETS BUILT AND COPIED SUCCESSFULLY!")
