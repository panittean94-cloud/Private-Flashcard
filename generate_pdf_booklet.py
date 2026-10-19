import os
import sys
import json
import subprocess
import shutil

sys.stdout.reconfigure(encoding='utf-8')

base_dir = r"c:\Users\thana\Desktop\Private-Flashcard"
json_path = os.path.join(base_dir, "data", "flashcards.json")
html_path = os.path.join(base_dir, "flashcards_booklet.html")
pdf_path = os.path.join(base_dir, "FunE_Final_Exam_Master_Flashcards_Ch6_10.pdf")
fund_e_pdf = os.path.join(r"c:\Users\thana\Desktop\Fund E N'Manow", "FunE_Final_Exam_Master_Flashcards_Ch6_10.pdf")

with open(json_path, 'r', encoding='utf-8') as f:
    cards = json.load(f)

print(f"Loaded {len(cards)} cards from {json_path}")

# Group cards by chapter
chapters_order = [
    "Chapter 6",
    "Chapter 7",
    "Chapter 8",
    "Chapter 9",
    "Chapter 10",
    "Semiconductors"
]

chapter_titles = {
    "Chapter 6": "Chapter 6: Three-Phase Circuits",
    "Chapter 7": "Chapter 7: Electrical Machines (DC & AC)",
    "Chapter 8": "Chapter 8: Transformers",
    "Chapter 9": "Chapter 9: Power Transmission Systems & Energy Conservation",
    "Chapter 10": "Chapter 10: Measuring Instruments & Sensors",
    "Semiconductors": "Chapter 11 / Supplement: Semiconductor & Electronic Devices"
}

chapter_subtitles = {
    "Chapter 6": "Balanced & Unbalanced Y-Y, Y-Δ, Complex Power, Neutral Shift, 2-Wattmeter Method",
    "Chapter 7": "Right-Hand Rule, Lorentz Force, DC Shunt/Series Motors & Generators, Induction & Synchronous",
    "Chapter 8": "Mutual Induction, Induced EMF Formula, 25 kVA Exam Problem, Audio Matching, Efficiency",
    "Chapter 9": "Thai Grid Voltage Stages, EGAT/MEA/PEA, Power Plants, Tower Classifications, Energy Conservation",
    "Chapter 10": "PMMC Principles, DC Ammeters & Voltmeters with CDRX, Ayrton Shunts, Ohmmeters, Wattmeters",
    "Semiconductors": "Diodes, Knee Voltages, LEDs, Solar PV Cells, BJT Terminal Currents, MOSFETs, Op-Amps"
}

cards_by_ch = {}
for ch in chapters_order:
    cards_by_ch[ch] = [c for c in cards if c['chapter'] == ch]

# Build HTML
cards_html = []
for ch in chapters_order:
    ch_cards = cards_by_ch[ch]
    cards_html.append(f"""
    <div class="chapter-divider">
      <div class="chapter-badge">PART {chapters_order.index(ch) + 1}</div>
      <h2 class="chapter-title">{chapter_titles[ch]}</h2>
      <p class="chapter-subtitle">{chapter_subtitles[ch]} ({len(ch_cards)} Flashcards)</p>
    </div>
    """)
    
    for c in ch_cards:
        is_calc = "Level 2" in c['difficulty']
        diff_class = "badge-calc" if is_calc else "badge-concept"
        diff_text = "🔴 Level 2 (Past Exam / Calc)" if is_calc else "🟢 Level 1 (Core Concept)"
        
        # Format answer text
        answer_body = c['answer']
        
        cards_html.append(f"""
        <div class="card-item">
          <div class="card-header">
            <div class="card-header-left">
              <span class="card-id">{c['id']}</span>
              <span class="card-chapter-tag">{c['chapter']}</span>
              <span class="card-diff-tag {diff_class}">{diff_text}</span>
            </div>
            <div class="card-header-right">
              <span class="card-ref-tag">📌 {c['exam_reference']}</span>
            </div>
          </div>
          
          <h3 class="card-topic">{c['topic']}</h3>
          
          <div class="card-question-box">
            <div class="section-label">QUESTION / EXAM PROBLEM:</div>
            <div class="card-question-text">{c['question']}</div>
          </div>
          
          <div class="card-answer-box">
            <div class="section-label-answer">FORMULA, SOLUTION & PRO TIPS:</div>
            <div class="card-answer-content">{answer_body}</div>
          </div>
        </div>
        """)

html_template = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <title>FunE Final Exam Master Flashcards (72 Cards)</title>
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/katex.min.css">
  <script src="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/katex.min.js"></script>
  <script src="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/contrib/auto-render.min.js"></script>
  <style>
    @page {{
      size: A4 portrait;
      margin: 12mm 12mm 12mm 12mm;
      @bottom-right {{
        content: "Page " counter(page);
        font-size: 8pt;
        color: #94a3b8;
      }}
    }}
    
    * {{
      box-sizing: border-box;
      -webkit-print-color-adjust: exact !important;
      print-color-adjust: exact !important;
    }}
    
    body {{
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
      font-size: 9pt;
      line-height: 1.45;
      color: #1e293b;
      background: #ffffff;
      margin: 0;
      padding: 0;
    }}

    /* Cover / Header Header */
    .cover-container {{
      border: 2px solid #2563eb;
      border-radius: 10px;
      padding: 16px 20px;
      margin-bottom: 20px;
      background: linear-gradient(135deg, #eff6ff 0%, #ffffff 100%);
      page-break-after: avoid;
    }}
    
    .cover-badge {{
      display: inline-block;
      background: #1e40af;
      color: #ffffff;
      font-size: 8pt;
      font-weight: 700;
      letter-spacing: 0.5px;
      padding: 3px 10px;
      border-radius: 9999px;
      text-transform: uppercase;
      margin-bottom: 8px;
    }}
    
    .cover-title {{
      font-size: 18pt;
      font-weight: 800;
      color: #0f172a;
      margin: 0 0 4px 0;
      letter-spacing: -0.5px;
    }}
    
    .cover-subtitle {{
      font-size: 11pt;
      font-weight: 600;
      color: #2563eb;
      margin: 0 0 10px 0;
    }}
    
    .cover-meta-grid {{
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 8px;
      padding-top: 10px;
      border-top: 1px solid #bfdbfe;
      font-size: 8pt;
    }}
    
    .meta-item strong {{
      color: #1e3a8a;
      display: block;
      font-size: 7.5pt;
      text-transform: uppercase;
    }}

    /* Chapter Divider */
    .chapter-divider {{
      background: #0f172a;
      color: #ffffff;
      padding: 10px 14px;
      border-radius: 8px;
      margin: 22px 0 14px 0;
      page-break-inside: avoid;
      page-break-after: avoid;
    }}
    
    .chapter-badge {{
      font-size: 7.5pt;
      font-weight: 700;
      color: #38bdf8;
      letter-spacing: 1px;
    }}
    
    .chapter-title {{
      font-size: 13pt;
      font-weight: 700;
      margin: 2px 0;
      color: #ffffff;
    }}
    
    .chapter-subtitle {{
      font-size: 8pt;
      color: #94a3b8;
      margin: 0;
    }}

    /* Flashcard Container */
    .card-item {{
      border: 1px solid #cbd5e1;
      border-radius: 8px;
      background: #ffffff;
      margin-bottom: 14px;
      page-break-inside: avoid;
      box-shadow: 0 1px 3px rgba(0,0,0,0.05);
      overflow: hidden;
    }}
    
    .card-header {{
      background: #f8fafc;
      border-bottom: 1px solid #e2e8f0;
      padding: 6px 12px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      font-size: 7.5pt;
    }}
    
    .card-header-left {{
      display: flex;
      align-items: center;
      gap: 6px;
    }}
    
    .card-id {{
      font-family: monospace;
      font-weight: 700;
      color: #0f172a;
      background: #e2e8f0;
      padding: 2px 6px;
      border-radius: 4px;
    }}
    
    .card-chapter-tag {{
      font-weight: 600;
      color: #475569;
    }}
    
    .card-diff-tag {{
      padding: 2px 7px;
      border-radius: 9999px;
      font-weight: 600;
    }}
    
    .badge-concept {{
      background: #dcfce7;
      color: #15803d;
    }}
    
    .badge-calc {{
      background: #fee2e2;
      color: #b91c1c;
    }}
    
    .card-ref-tag {{
      color: #4338ca;
      font-weight: 600;
      background: #e0e7ff;
      padding: 2px 8px;
      border-radius: 4px;
    }}
    
    .card-topic {{
      font-size: 10.5pt;
      font-weight: 700;
      color: #0f172a;
      margin: 8px 12px 6px 12px;
    }}
    
    .card-question-box {{
      padding: 6px 12px 8px 12px;
      background: #fdfdfd;
      border-bottom: 1px dashed #cbd5e1;
    }}
    
    .section-label {{
      font-size: 7pt;
      font-weight: 800;
      letter-spacing: 0.5px;
      color: #64748b;
      margin-bottom: 4px;
    }}
    
    .card-question-text {{
      font-size: 8.8pt;
      color: #1e293b;
    }}

    .card-question-text img, .card-answer-content img {{
      max-height: 160px;
      width: auto;
      max-width: 100%;
      display: block;
      margin: 8px auto;
      border: 1px solid #cbd5e1;
      border-radius: 6px;
      background: #ffffff;
    }}
    
    .card-answer-box {{
      padding: 8px 12px 10px 12px;
      background: #fafafa;
    }}
    
    .section-label-answer {{
      font-size: 7pt;
      font-weight: 800;
      letter-spacing: 0.5px;
      color: #059669;
      margin-bottom: 4px;
    }}
    
    .card-answer-content {{
      font-size: 8.5pt;
      line-height: 1.4;
    }}

    .card-answer-content p {{
      margin: 3px 0;
    }}

    /* KaTeX math adjustments */
    .katex {{
      font-size: 1.02em !important;
    }}
    
    .katex-display {{
      margin: 4px 0 !important;
    }}
  </style>
</head>
<body>

  <!-- Title / Cover Header -->
  <div class="cover-container">
    <div class="cover-badge">Faculty of Engineering • Khon Kaen University</div>
    <h1 class="cover-title">Fundamental Electrical Engineering (FunE)</h1>
    <div class="cover-subtitle">Final Exam Master Flashcards & Solved Problems Booklet (72 Cards)</div>
    
    <div class="cover-meta-grid">
      <div class="meta-item">
        <strong>Course & Instructor</strong>
        Assoc. Prof. Nararat Ruangchaijatupon
      </div>
      <div class="meta-item">
        <strong>Coverage</strong>
        Chapters 6, 7, 8, 9, 10 & Semiconductors
      </div>
      <div class="meta-item">
        <strong>Content Inclusions</strong>
        72 Cards • 22 Circuit Diagrams • Step-by-Step Solutions
      </div>
    </div>
  </div>

  <!-- Cards List -->
  {"".join(cards_html)}

  <script>
    document.addEventListener("DOMContentLoaded", function() {{
      renderMathInElement(document.body, {{
        delimiters: [
          {{left: '$$', right: '$$', display: true}},
          {{left: '$', right: '$', display: false}},
          {{left: '\\\\[', right: '\\\\]', display: true}},
          {{left: '\\\\(', right: '\\\\)', display: false}}
        ],
        throwOnError: false
      }});
    }});
  </script>
</body>
</html>
"""

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html_template)

print(f"Generated standalone booklet HTML: {html_path}")

# Run Edge Headless to compile into PDF
edge_path = r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe'
if not os.path.exists(edge_path):
    edge_path = r'C:\Program Files\Google\Chrome\Application\chrome.exe'

print(f"Invoking headless browser: {edge_path} ...")
cmd = [
    edge_path,
    '--headless=new',
    '--disable-gpu',
    '--virtual-time-budget=8000',
    '--no-pdf-header-footer',
    f'--print-to-pdf={pdf_path}',
    html_path
]

res = subprocess.run(cmd, capture_output=True, text=True)
if res.returncode == 0 and os.path.exists(pdf_path):
    pdf_size_mb = os.path.getsize(pdf_path) / (1024 * 1024)
    print(f"✅ SUCCESS: PDF compiled successfully!")
    print(f"File: {pdf_path} ({pdf_size_mb:.2f} MB)")
    
    # Copy to Fund E N'Manow
    shutil.copy2(pdf_path, fund_e_pdf)
    print(f"Copied PDF to: {fund_e_pdf}")
else:
    print(f"❌ Error during PDF compilation: returncode={res.returncode}")
    print(res.stderr)
