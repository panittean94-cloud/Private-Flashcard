# -*- coding: utf-8 -*-
"""
Script to create the complete bilingual 72-card dataset for FunE Final Exam.
Generates:
1. data/flashcards.json
2. data/flashcards.js
3. FunE_Master_Exam_Flashcards_Ch6_10_Master.xlsx
"""
import os
import json
import pandas as pd
import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side

def img_html(img_name, caption=""):
    cap = f"<div class='text-xs text-center text-slate-400 mt-1 mb-2'>{caption}</div>" if caption else ""
    return f"<div class='my-3 text-center'><img src='images/diagrams/{img_name}' alt='{caption}' class='rounded-lg border border-slate-300 dark:border-slate-700 max-h-60 mx-auto shadow-sm object-contain' />{cap}</div>"

# Import Part 1 (Ch6 & Ch7 cards)
from create_bilingual_part1 import cards as full_cards

# =========================================================================
# CHAPTER 8: TRANSFORMERS (Cards 26 - 37)
# =========================================================================
full_cards.append({
    "id": "CH08-01",
    "chapter": "Chapter 8",
    "topic": "Transformer Definition, Purpose & Structure",
    "topic_th": "นิยาม หน้าที่ และโครงสร้างหลักของหม้อแปลงไฟฟ้า (Transformer)",
    "level": "Level 1 (Concept)",
    "exam_reference": "Final Exam Problem 1.1 & 1.2 (Page 32 - 4 Points)",
    "question": "What is an electrical transformer? What is its primary function and structure? Draw/describe its essential construction.\n" + img_html('exam_p32_transformer_core.png', 'Exam Problem 1.2 Transformer Structure (Page 32)'),
    "question_th": "หม้อแปลงไฟฟ้าคืออะไร มีประโยชน์อย่างไร และมีรูปโครงสร้างอย่างไร? จงอธิบายและวาดโครงสร้างหลัก (ข้อสอบไฟนอลข้อ 1.1 และ 1.2 หน้า 32)\n" + img_html('exam_p32_transformer_core.png', 'ข้อสอบไฟนอลข้อ 1.2 จาก FunE-final.pdf หน้า 32'),
    "formula": "$$\\frac{V_1}{V_2} = \\frac{N_1}{N_2} = a,\\quad \\frac{I_1}{I_2} = \\frac{N_2}{N_1} = \\frac{1}{a}$$",
    "solution": "1. Definition & Function (ข้อ 1.1):\n- A static electrical machine with NO moving parts that transfers electrical energy between circuits through electromagnetic induction.\n- Purpose: Step-up (เพิ่มแรงดัน) or Step-down (ลดแรงดัน) AC voltage levels while keeping frequency constant.\n\n2. Structure (ข้อ 1.2):\n- Laminated ferromagnetic core (แกนเหล็กแผ่นซิลิคอนบางเรียงซ้อนกันเพื่อลดกระแสไหลวน Eddy Current)\n- Primary winding (ขดลวดปฐมภูมิ $N_1$ ต่อเข้าแหล่งจ่าย)\n- Secondary winding (ขดลวดทุติยภูมิ $N_2$ ต่อเข้าโหลด)",
    "solution_th": "1. นิยามและประโยชน์ (ข้อ 1.1):\n- เป็นเครื่องกลไฟฟ้าชนิด 'ไม่มีชิ้นส่วนเคลื่อนที่' (Static Machine) ที่ส่งถ่ายพลังงานไฟฟ้าระหว่างสองวงจรด้วยการเหนี่ยวนำแม่เหล็กไฟฟ้า\n- ประโยชน์: ใช้แปลงแรงดันไฟฟ้ากระแสสลับ (AC) ให้สูงขึ้น (Step-up) หรือต่ำลง (Step-down) โดยความถี่คงที่เสมอ\n\n2. รูปโครงสร้าง (ข้อ 1.2):\n- แกนเหล็ก (Laminated Core) ทำจากแผ่นเหล็กซิลิคอนอัดซ้อนกันเพื่อลดการสูญเสียจาก Eddy Current\n- ขดลวดปฐมภูมิ (Primary Winding $N_1$) ด้านรับไฟเข้า\n- ขดลวดทุติยภูมิ (Secondary Winding $N_2$) ด้านจ่ายไฟออกไปยังโหลด",
    "pitfall": "Transformers operate ONLY on Alternating Current (AC)! Never connect a transformer to a DC supply, as absence of changing flux ($d\\phi/dt=0$) induces zero back-EMF, causing excessive current that burns the primary winding.",
    "pitfall_th": "ข้อควรระวัง: หม้อแปลงไฟฟ้าทำงานได้กับ 'ไฟฟ้ากระแสสลับ (AC)' เท่านั้น! ห้ามต่อกับไฟ DC เด็ดขาด เพราะฟลักซ์ไม่เปลี่ยนแปลง ($d\\phi/dt=0$) ทำให้ไม่มีแรงดันต้านกลับ ขดลวดปฐมภูมิจะไหม้ทันที",
    "diagram": "images/diagrams/exam_p32_transformer_core.png",
    "mastered": False
})

full_cards.append({
    "id": "CH08-02",
    "chapter": "Chapter 8",
    "topic": "Single Phase 25 kVA Transformer Full Exam Problem",
    "topic_th": "การคำนวณหม้อแปลง 1 เฟส 25 kVA (ข้อสอบไฟนอลข้อ 1.6)",
    "level": "Level 2 (Past Exam / Calc)",
    "exam_reference": "Final Exam Problem 1.6 (Page 31 - 10 Points)",
    "question": "A single-phase transformer rated $25\\text{ kVA}$ has $N_1 = 500$ turns and $N_2 = 50$ turns. Primary winding is connected to $V_1 = 3,000\\text{ V}, 50\\text{ Hz}$. Calculate: (a) Turns ratio $a$, (b) Rated primary & secondary currents ($I_1, I_2$), (c) Induced secondary voltage $V_2$, (d) Maximum core flux $\\Phi_m$.\n" + img_html('exam_p31_prob16_transformer_calc.png', 'Exam Problem 1.6 (FunE-final.pdf Page 31)'),
    "question_th": "หม้อแปลงไฟฟ้า 1 เฟส ขนาดพิกัด $25\\text{ kVA}$ มีขดลวดปฐมภูมิ $N_1 = 500$ รอบ และขดลวดทุติยภูมิ $N_2 = 50$ รอบ ต่อปฐมภูมิเข้ากับแหล่งจ่าย $3,000\\text{ V}, 50\\text{ Hz}$ จงคำนวณหา: (ก) อัตราส่วนแรงดัน $a$ (ข) กระแสด้านปฐมภูมิและทุติยภูมิที่พิกัด ($I_1, I_2$) (ค) แรงดันเหนี่ยวนำด้านทุติยภูมิ $V_2$ (ง) ค่าสูงสุดของเส้นแรงแม่เหล็กในแกนเหล็ก $\\Phi_m$ (ข้อสอบไฟนอลข้อ 1.6)\n" + img_html('exam_p31_prob16_transformer_calc.png', 'ข้อสอบไฟนอลข้อ 1.6 จาก FunE-final.pdf หน้า 31'),
    "formula": "$$a = \\frac{N_1}{N_2},\\quad I_1 = \\frac{S}{V_1},\\quad I_2 = \\frac{S}{V_2}$$\n$$V_2 = \\frac{V_1}{a},\\quad V_1 = 4.44 f N_1 \\Phi_m$$",
    "solution": "1. (ก) Turns ratio ($a$):\n$$a = \\frac{N_1}{N_2} = \\frac{500}{50} = 10$$\n\n2. (ข) Rated currents:\n$$I_1 = \\frac{S}{V_1} = \\frac{25,000}{3,000} = 8.33\\text{ A} = \\frac{25}{3}\\text{ A}$$\n$$I_2 = a I_1 = 10 \\times 8.33 = 83.33\\text{ A} = \\frac{250}{3}\\text{ A}$$\n\n3. (ค) Secondary induced voltage ($V_2$):\n$$V_2 = \\frac{V_1}{a} = \\frac{3,000}{10} = 300\\text{ V}$$\n\n4. (ง) Maximum core flux ($\\Phi_m$):\n$$V_1 = 4.44 f N_1 \\Phi_m \\Rightarrow 3,000 = 4.44(50)(500)\\Phi_m$$\n$$\\Phi_m = \\frac{3,000}{111,000} = 0.027\\text{ Wb} = 27.0\\text{ mWb}$$",
    "solution_th": "1. (ก) อัตราส่วนแรงดัน (Turns Ratio $a$):\n$$a = \\frac{N_1}{N_2} = \\frac{500}{50} = 10$$\n\n2. (ข) กระแสพิกัดด้านปฐมภูมิและทุติยภูมิ:\n$$I_1 = \\frac{S}{V_1} = \\frac{25,000}{3,000} = 8.33\\text{ A}$$\n$$I_2 = a I_1 = 10 \\times 8.33 = 83.33\\text{ A}$$\n\n3. (ค) แรงดันเหนี่ยวนำด้านทุติยภูมิ ($V_2$):\n$$V_2 = \\frac{V_1}{a} = \\frac{3,000}{10} = 300\\text{ V}$$\n\n4. (ง) ค่าสูงสุดของเส้นแรงแม่เหล็กในแกนเหล็ก ($\\Phi_m$):\n$$V_1 = 4.44 f N_1 \\Phi_m \\Rightarrow 3,000 = 4.44(50)(500)\\Phi_m$$\n$$\\Phi_m = \\frac{3,000}{111,000} = 0.027\\text{ Wb} = 27.0\\text{ mWb}$$",
    "pitfall": "The constant 4.44 comes from $2\\pi/\\sqrt{2} \\approx 4.44288$. Flux $\\Phi_m$ is in Webers (Wb). Remember: $V_1$ uses $N_1$; $V_2$ uses $N_2$.",
    "pitfall_th": "ข้อควรระวัง: ค่าคงที่ 4.44 มาจาก $\\frac{2\\pi}{\\sqrt{2}} \\approx 4.44$ และ $\\Phi_m$ มีหน่วยเป็น Weber (Wb) หากใช้ $V_1$ ต้องคู่กับ $N_1$ เสมอ",
    "diagram": "images/diagrams/exam_p31_prob16_transformer_calc.png",
    "mastered": False
})

full_cards.append({
    "id": "CH08-03",
    "chapter": "Chapter 8",
    "topic": "Turns Ratio & Winding Calculations",
    "topic_th": "การคำนวณจำนวนรอบและกระแสของหม้อแปลง 1 เฟส",
    "level": "Level 2 (Past Exam / Calc)",
    "exam_reference": "HW Ch.8 Problem 2 (Page 1)",
    "question": "The primary and secondary voltages of a single-phase transformer are $V_1 = 140\\text{ V}$ and $V_2 = 80\\text{ V}$. Primary current is $I_1 = 8\\text{ A}$. Secondary winding has $N_2 = 800$ turns. Find: (1) Primary winding turns $N_1$, (2) Secondary current $I_2$, (3) Turns ratio $a$.",
    "question_th": "หม้อแปลงไฟฟ้า 1 เฟส มีแรงดันปฐมภูมิ $V_1 = 140\\text{ V}$ และแรงดันทุติยภูมิ $V_2 = 80\\text{ V}$ กระแสปฐมภูมิ $I_1 = 8\\text{ A}$ ขดลวดทุติยภูมิมี $N_2 = 800$ รอบ จงหา: (1) จำนวนรอบขดลวดปฐมภูมิ $N_1$ (2) กระแสในขดลวดทุติยภูมิ $I_2$ (3) อัตราส่วนหม้อแปลง $a$",
    "formula": "$$a = \\frac{V_1}{V_2} = \\frac{N_1}{N_2} = \\frac{I_2}{I_1}$$",
    "solution": "1. Turns Ratio ($a$):\n$$a = \\frac{V_1}{V_2} = \\frac{140}{80} = 1.75$$\n\n2. Primary turns ($N_1$):\n$$N_1 = a N_2 = 1.75 \\times 800 = 1,400\\text{ turns}$$\n\n3. Secondary current ($I_2$):\n$$I_2 = a I_1 = 1.75 \\times 8\\text{ A} = 14.0\\text{ A}$$",
    "solution_th": "1. อัตราส่วนจำนวนรอบ (Turns Ratio $a$):\n$$a = \\frac{V_1}{V_2} = \\frac{140}{80} = 1.75$$\n\n2. จำนวนรอบขดลวดปฐมภูมิ ($N_1$):\n$$N_1 = a N_2 = 1.75 \\times 800 = 1,400\\text{ รอบ}$$\n\n3. กระแสทุติยภูมิ ($I_2$):\n$$I_2 = a I_1 = 1.75 \\times 8\\text{ A} = 14.0\\text{ A}$$",
    "pitfall": "Voltage and turns are directly proportional ($V_1/V_2 = N_1/N_2$), but current is INVERSELY proportional ($I_1/I_2 = N_2/N_1$).",
    "pitfall_th": "ข้อควรระวัง: แรงดันและจำนวนรอบเป็นสัดส่วนตรงกัน ($V_1/V_2 = N_1/N_2$) แต่กระแสจะเป็น 'ส่วนกลับ' ($I_1/I_2 = N_2/N_1$) ด้านแรงดันต่ำกระแสจะสูง",
    "diagram": None,
    "mastered": False
})

full_cards.append({
    "id": "CH08-04",
    "chapter": "Chapter 8",
    "topic": "200 kVA Transformer Voltage, Current & Core Flux",
    "topic_th": "การคำนวณหม้อแปลง 200 kVA (กระแส, จำนวนรอบ, ฟลักซ์แกนเหล็ก)",
    "level": "Level 2 (Past Exam / Calc)",
    "exam_reference": "HW Ch.8 Problem 3 (Page 1)",
    "question": "A single-phase transformer rated $200\\text{ kVA}, 2200\\text{ V}/220\\text{ V}, 50\\text{ Hz}$ has primary winding $N_1 = 200$ turns. Find: (1) Rated primary and secondary currents ($I_1, I_2$), (2) Secondary turns $N_2$, (3) Maximum magnetic core flux $\\Phi_m$.",
    "question_th": "หม้อแปลงไฟฟ้า 1 เฟส พิกัด $200\\text{ kVA}, 2200\\text{ V}/220\\text{ V}, 50\\text{ Hz}$ มีขดลวดปฐมภูมิ $N_1 = 200$ รอบ จงหา: (1) กระแสพิกัดปฐมภูมิและทุติยภูมิ ($I_1, I_2$) (2) จำนวนรอบขดลวดทุติยภูมิ $N_2$ (3) ฟลักซ์แม่เหล็กสูงสุดในแกนเหล็ก $\\Phi_m$",
    "formula": "$$I_1 = \\frac{S}{V_1},\\quad I_2 = \\frac{S}{V_2}$$\n$$N_2 = \\frac{V_2}{V_1} N_1,\\quad \\Phi_m = \\frac{V_1}{4.44 f N_1}$$",
    "solution": "1. Rated Currents:\n$$I_1 = \\frac{200 \\times 10^3}{2,200} = 90.91\\text{ A}$$\n$$I_2 = \\frac{200 \\times 10^3}{220} = 909.09\\text{ A}$$\n\n2. Secondary turns ($N_2$):\n$$a = \\frac{2,200}{220} = 10 \\Rightarrow N_2 = \\frac{N_1}{10} = \\frac{200}{10} = 20\\text{ turns}$$\n\n3. Maximum flux ($\\Phi_m$):\n$$\\Phi_m = \\frac{2,200}{4.44 \\times 50 \\times 200} = \\frac{2,200}{44,400} = 0.0495\\text{ Wb} = 49.5\\text{ mWb}$$",
    "solution_th": "1. กระแสพิกัด:\n$$I_1 = \\frac{200,000}{2,200} = 90.91\\text{ A}$$\n$$I_2 = \\frac{200,000}{220} = 909.09\\text{ A}$$\n\n2. จำนวนรอบขดลวดทุติยภูมิ ($N_2$):\n$$a = \\frac{2,200}{220} = 10 \\quad\\Rightarrow\\quad N_2 = \\frac{200}{10} = 20\\text{ รอบ}$$\n\n3. ฟลักซ์แม่เหล็กสูงสุด ($\\Phi_m$):\n$$\\Phi_m = \\frac{2,200}{4.44 \\times 50 \\times 200} = 0.0495\\text{ Wb} = 49.5\\text{ mWb}$$",
    "pitfall": "Always double check: $V_2 = 4.44 f N_2 \\Phi_m$ must yield the EXACT same flux value: $220 / (4.44 \\times 50 \\times 20) = 49.5\\text{ mWb}$.",
    "pitfall_th": "ข้อควรระวัง: สามารถตรวจคำตอบได้ด้วยสมการด้านทุติยภูมิ $V_2 = 4.44 f N_2 \\Phi_m$ ซึ่งต้องให้ค่าฟลักซ์เท่ากันพอดี",
    "diagram": None,
    "mastered": False
})

full_cards.append({
    "id": "CH08-05",
    "chapter": "Chapter 8",
    "topic": "Transformer DC Connection Danger (Why Transformers Cannot Run on DC)",
    "topic_th": "อันตรายจากการป้อนไฟกระแสตรง (DC) ให้หม้อแปลงไฟฟ้า",
    "level": "Level 2 (Past Exam / Calc)",
    "exam_reference": "HW Ch.8 Problem 4.4 (Page 1)",
    "question": "A $25\\text{ kVA}, 500/40\\text{ turns}$ transformer is supplied at primary by $300\\text{ V}, 50\\text{ Hz}$. (1) If we change to connect a DC voltage of $200\\text{ V}$ to the primary winding, what will the secondary current $I_2$ be? (2) What happens physically to the transformer?",
    "question_th": "หม้อแปลงขนาด $25\\text{ kVA}, 500/40\\text{ รอบ}$ รับไฟ $300\\text{ V}, 50\\text{ Hz}$ (1) หากเปลี่ยนไปต่อไฟตรง (DC) ขนาด $200\\text{ V}$ ที่ขดลวดปฐมภูมิ กระแสในขดลวดทุติยภูมิ $I_2$ จะมีค่าเท่าใด? (2) และจะเกิดผลกระทบทางกายภาพอย่างไรกับหม้อแปลง?",
    "formula": "$$e_2 = -N_2 \\frac{d\\Phi}{dt} = 0\\quad (\\text{for steady DC})$$",
    "solution": "1. Secondary current ($I_2$):\n$$I_2 = 0\\text{ A}$$\nBecause DC voltage produces constant, steady magnetic flux ($\\frac{d\\Phi}{dt} = 0$), no voltage is induced in the secondary winding ($e_2 = 0\\text{ V}$), so $I_2 = 0\\text{ A}$.\n\n2. Physical Consequence to Transformer:\nWith no alternating flux, there is zero back-EMF ($e_1 = 0$). Primary current is limited only by tiny copper resistance $R_1$ ($< 0.1\\ \\Omega$):\n$$I_{1,\\text{DC}} = \\frac{200\\text{ V}}{R_1} \\gg 1,000\\text{ A}!$$\nThe primary winding will overheat instantly, burn its enamel insulation, and catch fire!",
    "solution_th": "1. กระแสด้านทุติยภูมิ ($I_2$):\n$$I_2 = 0\\text{ A}$$\nเนื่องจากไฟ DC มีค่าคงที่ ฟลักซ์แม่เหล็กจึงคงที่ไม่เปลี่ยนแปลงตามเวลา ($\\frac{d\\Phi}{dt} = 0$) ทำให้ไม่เกิดแรงดันเหนี่ยวนำที่ขดลวดทุติยภูมิเลย ($V_2 = 0\\text{ V}$)\n\n2. ผลกระทบทางกายภาพ:\nเมื่อไม่มีการเปลี่ยนแปลงฟลักซ์ จะไม่มี Back EMF ในขดลวดปฐมภูมิ กระแสไฟตรงจึงถูกจำกัดด้วยความต้านทานขดลวดทองแดง ($R_1$) ที่มีค่าน้อยมากเท่านั้น ($I_{1} = \\frac{200\\text{ V}}{R_1} > 1,000\\text{ A}$)\nส่งผลให้ขดลวดปฐมภูมิร้อนจัด ฉนวนไหม้ละลาย และเกิดไฟไหม้เสียหายทันที",
    "pitfall": "Classic trick question! Never write $I_2 = 200/a$. For DC, induced secondary voltage and current are ZERO, while primary burns.",
    "pitfall_th": "ข้อควรระวัง: ข้อสอบหลอกยอดฮิต! ห้ามนำสูตร $V_2 = V_1/a$ ไปใช้กับไฟ DC เด็ดขาด เพราะไฟ DC ด้านทุติยภูมิจะไม่มีไฟออก ($I_2 = 0$) ขณะที่ด้านปฐมภูมิจะไหม้",
    "diagram": None,
    "mastered": False
})

full_cards.append({
    "id": "CH08-06",
    "chapter": "Chapter 8",
    "topic": "Ideal Transformer 4 Fundamental Hypotheses",
    "topic_th": "คุณสมบัติ 4 ประการของหม้อแปลงไฟฟ้าในอุดมคติ (Ideal Transformer)",
    "level": "Level 1 (Concept)",
    "exam_reference": "Final Exam Problem 1.4 (Page 32 - 2 Points)",
    "question": "State the 4 fundamental properties/assumptions that define an Ideal Transformer (หม้อแปลงไฟฟ้าในอุดมคติ).",
    "question_th": "จงระบุคุณสมบัติ 4 ประการของหม้อแปลงไฟฟ้าในอุดมคติ (Ideal Transformer) ตามข้อสอบไฟนอลข้อ 1.4",
    "formula": "Ideal: $R_1=R_2=0,\\quad \\mu_r = \\infty,\\quad P_{\\text{loss}} = 0,\\quad \\Phi_{\\text{leakage}} = 0$",
    "solution": "1. Zero Winding Resistance: $R_1 = 0, R_2 = 0$ (No $I^2 R$ copper losses).\n2. Infinite Core Permeability: $\\mu_r \\to \\infty$, so zero reluctance and zero magnetizing current needed ($I_m = 0$).\n3. Zero Core Losses: No hysteresis loss and no eddy current loss ($P_{\\text{core}} = 0$).\n4. Zero Leakage Flux: All magnetic flux is perfectly confined within the core and links both windings completely ($X_1 = X_2 = 0$).",
    "solution_th": "1. ขดลวดไม่มีความต้านทาน: $R_1 = R_2 = 0$ (ไม่มีการสูญเสียในทองแดง $I^2 R$ Copper Loss)\n2. แกนเหล็กมีค่าความซาบซึมได้แม่เหล็กเป็นอนันต์: $\\mu_r \\to \\infty$ (ไม่ต้องใช้กระแสสร้างสนามแม่เหล็ก $I_m = 0$)\n3. ไม่มีการสูญเสียในแกนเหล็ก: ไม่มีทั้ง Hysteresis Loss และ Eddy Current Loss ($P_{\\text{core}} = 0$)\n4. ไม่มีเส้นแรงแม่เหล็กรั่วไหล: เส้นแรงแม่เหล็กทั้งหมดวิ่งผ่านเฉพาะในแกนเหล็กและคล้องผ่านขดลวดทั้งสองสมบูรณ์ ($X_1 = X_2 = 0$)",
    "pitfall": "Real transformers have losses (efficiency $95-99\\%$). An ideal transformer has $100\\%$ efficiency, so $S_{\\text{in}} = S_{\\text{out}}$ and $P_{\\text{in}} = P_{\\text{out}}$.",
    "pitfall_th": "ข้อควรระวัง: หม้อแปลงจริงมีประสิทธิภาพ $95-99\\%$ แต่หม้อแปลงในอุดมคติประสิทธิภาพคือ $100\\%$ ($P_{\\text{in}} = P_{\\text{out}}$)",
    "diagram": None,
    "mastered": False
})

full_cards.append({
    "id": "CH08-07",
    "chapter": "Chapter 8",
    "topic": "Transformer Losses: Core Loss vs Copper Loss",
    "topic_th": "การสูญเสียในหม้อแปลงไฟฟ้า: Core Loss เทียบกับ Copper Loss",
    "level": "Level 1 (Concept)",
    "exam_reference": "Final Exam Problem 1.5 (Page 32 - 2 Points)",
    "question": "What types of power losses occur in a real transformer? Contrast Core Loss (Iron Loss) with Copper Loss (Winding Loss) regarding their cause and load dependency.",
    "question_th": "หม้อแปลงไฟฟ้ามีการสูญเสียกำลังไฟฟ้าในรูปใดบ้าง? จงเปรียบเทียบระหว่าง Core Loss (Iron Loss) กับ Copper Loss ในแง่ของสาเหตุและความสัมพันธ์กับโหลด (ข้อสอบไฟนอลข้อ 1.5)",
    "formula": "$$P_{\\text{total loss}} = P_{\\text{core}} + P_{\\text{cu}}$$\n$$P_{\\text{core}} = P_h + P_e\\quad (\\text{constant 24/7})$$\n$$P_{\\text{cu}} = I_1^2 R_1 + I_2^2 R_2 \\propto I_L^2$$",
    "solution": "1. Core Loss (Iron Loss / การสูญเสียในแกนเหล็ก):\n- Hysteresis loss ($P_h \\propto f B_{\\max}^{1.6}$) + Eddy current loss ($P_e \\propto f^2 B_{\\max}^2 t^2$).\n- Constant 24/7: Depends only on applied voltage and frequency; independent of load current!\n\n2. Copper Loss ($I^2 R$ Loss / การสูญเสียในขดลวดทองแดง):\n- Caused by Joule heating in primary and secondary winding resistances.\n- Variable: Proportional to the square of load current ($P_{\\text{cu}} \\propto I_L^2$). Zero at no load!",
    "solution_th": "1. Core Loss หรือ Iron Loss (การสูญเสียในแกนเหล็ก):\n- ประกอบด้วย Hysteresis Loss (การกลับทิศโมเลกุลแม่เหล็ก) และ Eddy Current Loss (กระแสไหลวนในแกนเหล็ก)\n- เป็นค่าคงที่ตลอด 24 ชั่วโมง: ขึ้นอยู่กับแรงดันและความถี่ ไม่ขึ้นอยู่กับโหลด!\n\n2. Copper Loss (การสูญเสียในทองแดง):\n- เกิดจากความร้อน $I^2 R$ ในเนื้อขดลวดปฐมภูมิและทุติยภูมิ\n- แปรผันตามโหลด: แปรผันตรงกับกำลังสองของกระแสโหลด ($P_{\\text{cu}} \\propto I_L^2$) ขณะ No-Load ค่านี้จะเป็นศูนย์",
    "pitfall": "Maximum transformer efficiency occurs when Variable Loss equals Constant Loss: $P_{\\text{cu}} = P_{\\text{core}}$!",
    "pitfall_th": "ข้อควรระวัง: ข้อสอบชอบถามเงื่อนไขที่หม้อแปลงมีประสิทธิภาพสูงสุด (Maximum Efficiency) คำตอบคือ 'เมื่อ Copper Loss เท่ากับ Core Loss พอดี' ($P_{\\text{cu}} = P_{\\text{core}}$)",
    "diagram": None,
    "mastered": False
})

full_cards.append({
    "id": "CH08-08",
    "chapter": "Chapter 8",
    "topic": "Audio Transformer Impedance Matching for Maximum Power Transfer",
    "topic_th": "การแมตช์อิมพีแดนซ์ด้วยหม้อแปลงเพื่อส่งถ่ายกำลังสูงสุด (Impedance Matching)",
    "level": "Level 2 (Past Exam / Calc)",
    "exam_reference": "Ch07Transformer.pdf Example 1 (Page 18) & FunE P.7",
    "question": "A $10\\text{ V}$ audio source with internal source resistance $R_s = 1\\ \\Omega$ is connected to a speaker load $R_L = 9\\ \\Omega$. (a) Find power to the speaker without transformer. (b) If an ideal matching transformer with turns ratio $a = 1/3$ is inserted, find the new power transferred to the speaker.\n" + img_html('transformer_audio_matching.png', 'Audio Transformer Matching Circuit'),
    "question_th": "แหล่งจ่ายสัญญาณเสียง $10\\text{ V}$ มีความต้านทานภายใน $R_s = 1\\ \\Omega$ ต่อกับลำโพงโหลด $R_L = 9\\ \\Omega$ ดังรูป (ก) จงหากำลังไฟฟ้าที่ตัวลำโพงเมื่อต่อตรง (ข) หากนำหม้อแปลงที่มีอัตราส่วน $1:3$ ($a = 1/3$) มาต่อคั่นเพื่อแมตช์อิมพีแดนซ์ กำลังไฟฟ้าที่ลำโพงจะมีค่าเท่าใด?\n" + img_html('transformer_audio_matching.png', 'วงจรหม้อแปลงแมตช์อิมพีแดนซ์ลำโพงเสียง'),
    "formula": "$$R_L' = a^2 R_L = \\left(\\frac{N_1}{N_2}\\right)^2 R_L$$\nMaximum Power Transfer when $R_L' = R_s$",
    "solution": "1. Without Transformer:\n$$I = \\frac{10}{1 + 9} = 1.0\\text{ A}$$\n$$P_{\\text{speaker}} = I^2 R_L = (1.0)^2 \\times 9 = 9.0\\text{ W}$$\n\n2. With Transformer ($a = 1/3$):\nReflected load resistance seen by source:\n$$R_L' = a^2 R_L = \\left(\\frac{1}{3}\\right)^2 \\times 9 = \\frac{1}{9} \\times 9 = 1.0\\ \\Omega$$\nNotice $R_L' = R_s = 1.0\\ \\Omega$ (perfect Maximum Power Transfer match!).\nNew primary current:\n$$I_1 = \\frac{10}{1 + 1} = 5.0\\text{ A}$$\nPower delivered to reflected load (and thus speaker):\n$$P_{\\text{speaker}} = I_1^2 R_L' = (5.0)^2 \\times 1.0 = 25.0\\text{ W}$$\nPower increases dramatically from $9\\text{ W}$ to $25\\text{ W}$!",
    "solution_th": "1. เมื่อไม่มีหม้อแปลง (ต่อตรง):\n$$I = \\frac{10}{1 + 9} = 1.0\\text{ A}$$\n$$P_{\\text{speaker}} = I^2 R_L = (1.0)^2 \\times 9 = 9.0\\text{ W}$$\n\n2. เมื่อใส่หม้อแปลง ($a = 1/3$):\nอิมพีแดนซ์สมมูลที่สะท้อนกลับมายังด้านปฐมภูมิ:\n$$R_L' = a^2 R_L = \\left(\\frac{1}{3}\\right)^2 \\times 9 = 1.0\\ \\Omega$$\nจะเห็นว่า $R_L' = R_s = 1.0\\ \\Omega$ พอดี (เกิด Maximum Power Transfer!)\nกระแสใหม่จากแหล่งจ่าย:\n$$I_1 = \\frac{10}{1 + 1} = 5.0\\text{ A}$$\nกำลังไฟฟ้าที่ส่งไปยังลำโพง:\n$$P_{\\text{speaker}} = I_1^2 R_L' = (5.0)^2 \\times 1.0 = 25.0\\text{ W}$$\nกำลังไฟฟ้าเพิ่มขึ้นจาก $9\\text{ W}$ เป็น $25\\text{ W}$ อย่างมหาศาล!",
    "pitfall": "Reflected impedance scales as $a^2$: $Z_1 = a^2 Z_2$. In audio systems, transformers match unequal impedances to maximize transferred power.",
    "pitfall_th": "ข้อควรระวัง: อิมพีแดนซ์สะท้อนจะแปรผันตาม $a^2$ ($Z_1 = a^2 Z_2$) ในระบบเสียง หม้อแปลงทำหน้าที่แปลงค่าอิมพีแดนซ์ที่ไม่เท่ากันให้เท่ากันเพื่อถ่ายโอนกำลังงานสูงสุด",
    "diagram": "images/diagrams/transformer_audio_matching.png",
    "mastered": False
})

full_cards.append({
    "id": "CH08-09",
    "chapter": "Chapter 8",
    "topic": "Open-Circuit (No-Load) Test for Shunt Branch Parameters",
    "topic_th": "การทดสอบแบบเปิดวงจร (Open-Circuit Test) เพื่อหาพารามิเตอร์แกนเหล็ก",
    "level": "Level 1 (Concept)",
    "exam_reference": "Lecture Slides & Formula Sheet",
    "question": "In a transformer Open-Circuit Test: (1) Which winding is energized and which is left open? (2) Which equivalent circuit parameters are determined, and what does the wattmeter reading represent?",
    "question_th": "ในการทดสอบหม้อแปลงแบบเปิดวงจร (Open-Circuit Test): (1) ป้อนไฟเข้าด้านใดและเปิดวงจรด้านใด? (2) ใช้หาค่าพารามิเตอร์ใดในวงจรสมมูล และวัตต์มิเตอร์อ่านค่าการสูญเสียอะไร?",
    "formula": "$$P_{oc} \\approx P_{\\text{core}},\\quad R_c = \\frac{V_{oc}^2}{P_{oc}}$$\n$$I_c = \\frac{V_{oc}}{R_c},\\quad I_m = \\sqrt{I_{oc}^2 - I_c^2},\\quad X_m = \\frac{V_{oc}}{I_m}$$",
    "solution": "1. Connection:\n- Low Voltage (LV) side is energized at rated voltage.\n- High Voltage (HV) side is left completely OPEN for operator safety.\n\n2. Measured Values & Parameters:\n- Wattmeter measures Core Loss directly ($P_{oc} = P_{\\text{core}}$) because no-load current is tiny ($< 3-5\\%$), making winding $I^2 R$ negligible.\n- Yields shunt excitation branch parameters: Core resistance $R_c$ (modeling hysteresis & eddy losses) and magnetizing reactance $X_m$ (modeling core magnetization).",
    "solution_th": "1. การต่อวงจร:\n- ป้อนไฟพิกัดเข้าด้านแรงดันต่ำ (LV Side)\n- เปิดวงจรด้านแรงดันสูง (HV Side) ทิ้งไว้เพื่อความปลอดภัยของผู้ปฏิบัติงาน\n\n2. พารามิเตอร์ที่ได้:\n- วัตต์มิเตอร์อ่านค่า Core Loss โดยตรง ($P_{oc} \\approx P_{\\text{core}}$) เพราะกระแส No-load ต่ำมาก ($< 3-5\\%$) จึงตัด $I^2 R$ ในทองแดงทิ้งได้\n- ใช้คำนวณหาค่าในแขนขนาน (Shunt Branch): $R_c$ (แทนการสูญเสียในแกนเหล็ก) และ $X_m$ (แทนรีแอกแตนซ์สร้างฟลักซ์)",
    "pitfall": "Open-Circuit test yields CORE LOSS ($P_{\\text{core}}$) and shunt branch ($R_c, X_m$). Do NOT confuse with short-circuit test!",
    "pitfall_th": "ข้อควรระวัง: Open-Circuit Test ให้ค่า Core Loss และพารามิเตอร์แกนเหล็ก ($R_c, X_m$) ห้ามจำสับสนกับ Short-Circuit Test เด็ดขาด",
    "diagram": None,
    "mastered": False
})

full_cards.append({
    "id": "CH08-10",
    "chapter": "Chapter 8",
    "topic": "Short-Circuit Test for Series Winding Parameters",
    "topic_th": "การทดสอบแบบลัดวงจร (Short-Circuit Test) เพื่อหาค่าพารามิเตอร์ขดลวด",
    "level": "Level 1 (Concept)",
    "exam_reference": "Lecture Slides & Formula Sheet",
    "question": "In a transformer Short-Circuit Test: (1) Which winding is short-circuited and which is energized? (2) Which equivalent circuit parameters are determined, and what does the wattmeter reading represent?",
    "question_th": "ในการทดสอบหม้อแปลงแบบลัดวงจร (Short-Circuit Test): (1) ลัดวงจรด้านใดและป้อนไฟด้านใด? (2) ใช้หาค่าพารามิเตอร์ใดในวงจรสมมูล และวัตต์มิเตอร์อ่านค่าอะไร?",
    "formula": "$$P_{sc} \\approx P_{\\text{cu}},\\quad R_{eq} = \\frac{P_{sc}}{I_{sc}^2}$$\n$$Z_{eq} = \\frac{V_{sc}}{I_{sc}},\\quad X_{eq} = \\sqrt{Z_{eq}^2 - R_{eq}^2}$$",
    "solution": "1. Connection:\n- Low Voltage (LV) side is securely SHORT-CIRCUITED with a thick jumper bar.\n- High Voltage (HV) side is energized with a REDUCED voltage ($5-10\\%$ of rated) adjusted until rated current flows.\n\n2. Measured Values & Parameters:\n- Wattmeter measures Full-Load Copper Loss ($P_{sc} = P_{\\text{cu}}$) because applied voltage is so low that core flux and core loss are negligible.\n- Yields series equivalent parameters: Equivalent resistance $R_{eq} = R_1 + a^2 R_2$ and equivalent leakage reactance $X_{eq} = X_1 + a^2 X_2$.",
    "solution_th": "1. การต่อวงจร:\n- นำบัสบาร์ขนาดใหญ่มาลัดวงจร (Short-circuit) ด้านแรงดันต่ำ (LV Side)\n- ป้อนแรงดันต่ำมาก ($5-10\\%$ ของพิกัด) เข้าด้านแรงดันสูง (HV Side) แล้วค่อยๆ ปรับจนกระแสไหลเท่าพิกัด\n\n2. พารามิเตอร์ที่ได้:\n- วัตต์มิเตอร์อ่านค่า Copper Loss ขณะรับโหลดเต็มที่ ($P_{sc} = P_{\\text{cu}}$) เพราะแรงดันต่ำมาก ฟลักซ์และ Core loss จึงเป็นศูนย์\n- ใช้คำนวณหาค่าพารามิเตอร์อนุกรม: ความต้านทานสมมูล $R_{eq}$ และรีแอกแตนซ์รั่วไหล $X_{eq}$",
    "pitfall": "Short-Circuit test yields COPPER LOSS ($P_{\\text{cu}}$) and series parameters ($R_{eq}, X_{eq}$). Never apply full rated voltage during a short-circuit test!",
    "pitfall_th": "ข้อควรระวัง: Short-Circuit Test ให้ค่า Copper Loss และพารามิเตอร์อนุกรม ($R_{eq}, X_{eq}$) ห้ามป้อนแรงดันเต็มพิกัดขณะลัดวงจรเด็ดขาด เพราะกระแสจะลัดวงจรระเบิดทันที",
    "diagram": None,
    "mastered": False
})

full_cards.append({
    "id": "CH08-11",
    "chapter": "Chapter 8",
    "topic": "Transformer Voltage Regulation Formula & Power Factor Dependency",
    "topic_th": "สูตรการคุมค่าแรงดันของหม้อแปลง (Voltage Regulation) และอิทธิพลของ PF",
    "level": "Level 1 (Concept)",
    "exam_reference": "Lecture Slides & Final Exam",
    "question": "State the formula for Transformer Voltage Regulation ($VR\\%$). How does the power factor (lagging vs leading) affect voltage regulation, and can $VR\\%$ ever be negative?",
    "question_th": "จงเขียนสูตรการคุมค่าแรงดันของหม้อแปลง ($VR\\%$) และอธิบายว่าค่า Power Factor (Lagging vs Leading) ส่งผลต่อค่า $VR\\%$ อย่างไร และมีโอกาสที่ $VR\\%$ จะติดลบได้หรือไม่?",
    "formula": "$$VR\\% = \\frac{V_{NL} - V_{FL}}{V_{FL}} \\times 100\\%$$\nApprox: $$VR\\% \\approx \\frac{I_2 R_{eq2} \\cos\\theta \\pm I_2 X_{eq2} \\sin\\theta}{V_2} \\times 100\\%$$",
    "solution": "1. Formula:\n$$VR\\% = \\frac{V_{2,NL} - V_{2,FL}}{V_{2,FL}} \\times 100\\%$$\n\n2. Effect of Power Factor:\n- Lagging PF (Inductive load): (+) sign applies. Voltage drops under load ($V_{FL} < V_{NL}$), so $VR\\% > 0$ (positive).\n- Unity PF ($PF=1.0$): Small positive $VR\\%$.\n- Leading PF (Capacitive load): (-) sign applies. Due to capacitive Ferranti effect, terminal voltage rises under load ($V_{FL} > V_{NL}$), causing $VR\\% < 0$ (NEGATIVE)!",
    "solution_th": "1. สูตร Voltage Regulation:\n$$VR\\% = \\frac{V_{2,NL} - V_{2,FL}}{V_{2,FL}} \\times 100\\%$$\n\n2. อิทธิพลของค่า Power Factor:\n- โหลดแบบ Lagging (Inductive โหลดเหนี่ยวนำ): ใช้เครื่องหมายบวก แรงดันตกคร่อมโหลดจะลดลงเมื่อมีโหลด ($VR\\% > 0$)\n- โหลดแบบ $PF = 1.0$ (Resistive): มีค่าเป็นบวกเล็กน้อย\n- โหลดแบบ Leading (Capacitive โหลดเก็บประจุ): ใช้เครื่องหมายลบ เกิดปรากฏการณ์ดันแรงดันที่ขั้วสูงขึ้นขณะมีโหลด ($V_{FL} > V_{NL}$) ส่งผลให้ $VR\\%$ ติดลบได้ (Negative VR)!",
    "pitfall": "Negative voltage regulation ($VR\\% < 0$) happens ONLY with LEADING power factors (capacitive loads), meaning voltage at full load is HIGHER than at no load!",
    "pitfall_th": "ข้อควรระวัง: ค่า $VR\\%$ ติดลบได้เฉพาะเมื่อโหลดมี Power Factor แบบ Leading (โหลดตัวเก็บประจุ) เท่านั้น ซึ่งหมายความว่าแรงดันขณะจ่ายโหลดจะสูงกว่าขณะ No-Load",
    "diagram": None,
    "mastered": False
})

full_cards.append({
    "id": "CH08-12",
    "chapter": "Chapter 8",
    "topic": "Auto-Transformer Principle, Higher kVA Rating & Common Winding Risk",
    "topic_th": "หลักการของหม้อแปลงออโต้ (Auto-Transformer) และความเสี่ยงขดลวดร่วม",
    "level": "Level 1 (Concept)",
    "exam_reference": "Lecture Slides & Final Exam",
    "question": "What is an Auto-Transformer? Why does it possess a higher kVA power rating and higher efficiency than a conventional two-winding transformer of the same physical size, and what is its primary safety drawback?",
    "question_th": "หม้อแปลงออโต้ (Auto-Transformer) คืออะไร? เหตุใดจึงมีพิกัด kVA และประสิทธิภาพสูงกว่าหม้อแปลง 2 ขดลวดทั่วไปที่มีขนาดตัวเท่ากัน และมีข้อเสียร้ายแรงด้านความปลอดภัยอย่างไร?",
    "formula": "$$\\frac{S_{\\text{auto}}}{S_{\\text{2-w}}} = \\frac{1}{1 - 1/a_{\\text{auto}}}$$\nConducted power + Transformed power",
    "solution": "1. Construction & Principle:\nAn auto-transformer has a SINGLE continuous winding shared partly by both primary and secondary circuits (tapped common winding).\n\n2. Higher Rating & Efficiency:\nPower is transferred via two mechanisms simultaneously:\n- By electromagnetic induction (transformed power)\n- By direct electrical conduction (conducted power)\nBecause part of the energy flows conductively through the shared copper, magnetic core and windings can be much smaller and lighter, with lower $I^2 R$ and core losses.\n\n3. Safety Drawback:\nNO ELECTRICAL ISOLATION between primary (HV) and secondary (LV)! If the common ground connection opens, the full high voltage appears directly on the low voltage terminals, risking electrocution.",
    "solution_th": "1. โครงสร้างและหลักการ:\nหม้อแปลงออโต้มี 'ขดลวดเพียงขดเดียว' พันบนแกนเหล็ก โดยขดลวดปฐมภูมิและทุติยภูมิจะใช้เนื้อขดลวดส่วนหนึ่งร่วมกัน (Common Winding)\n\n2. พิกัดและประสิทธิภาพที่สูงกว่า:\nส่งถ่ายพลังงานได้ 2 ทางพร้อมกัน คือ ทางการเหนี่ยวนำแม่เหล็ก และ ทางการนำไฟฟ้าโดยตรง (Conduction) ทำให้ประหยัดขนาดแกนเหล็กและทองแดง มีการสูญเสียต่ำกว่ามาก\n\n3. ข้อเสียร้ายแรงด้านความปลอดภัย:\n'ไม่มีการแยกทางไฟฟ้าระหว่างขดลวด (No Galvanic Isolation)' ด้านแรงดันสูงและแรงดันต่ำเชื่อมถึงกันโดยตรง หากขดลวดร่วมขาด แรงดันสูงจากฝั่งปฐมภูมิจะรั่วข้ามไปยังฝั่งทุติยภูมิทันที",
    "pitfall": "Never use an autotransformer where human safety isolation from high voltage mains is required (e.g. medical equipment or bathroom supplies).",
    "pitfall_th": "ข้อควรระวัง: ห้ามใช้ Auto-transformer ในงานที่ต้องการการแยกทางไฟฟ้าเพื่อความปลอดภัย เช่น เครื่องมือแพทย์ หรือหม้อแปลงแยกขด (Isolation Transformer)",
    "diagram": None,
    "mastered": False
})

print(f"Loaded {len(full_cards)} cards up to Ch.8")
