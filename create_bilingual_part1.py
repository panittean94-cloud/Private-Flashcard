# -*- coding: utf-8 -*-
"""
Full Bilingual Dataset Creator for Chapters 6 - 10
Thai (using English technical transliteration) + English
"""
import os
import json
import pandas as pd
import openpyxl

def img_html(img_name, caption=""):
    cap = f"<div class='text-xs text-center text-slate-400 mt-1 mb-2'>{caption}</div>" if caption else ""
    return f"<div class='my-3 text-center'><img src='images/diagrams/{img_name}' alt='{caption}' class='rounded-lg border border-slate-300 dark:border-slate-700 max-h-60 mx-auto shadow-sm object-contain' />{cap}</div>"

cards = []

# =========================================================================
# CHAPTER 6: THREE-PHASE CIRCUITS (Cards 1 - 10)
# =========================================================================
cards.append({
    "id": "CH06-01",
    "chapter": "Chapter 6",
    "topic": "Star (Y) vs Delta (Δ) Voltage & Current Relations",
    "topic_th": "ความสัมพันธ์แรงดันและกระแสของ Star (Y) และ Delta (Δ)",
    "level": "Level 1 (Concept)",
    "exam_reference": "Lecture Slides & Formula Sheet",
    "question": "In a balanced 3-phase positive-sequence ($abc$) system, state the exact relationships between line quantities ($V_L, I_L$) and phase quantities ($V_p, I_p$) for both Y-connection and $\\Delta$-connection.",
    "question_th": "ในระบบไฟฟ้า 3 เฟสแบบสมดุล (Balanced 3-Phase System) ที่มีลำดับเฟสบวก (Positive Sequence $abc$) จงระบุความสัมพันธ์ระหว่างค่า Line ($V_L, I_L$) กับค่า Phase ($V_p, I_p$) ของทั้งการต่อแบบ Star (Y) และ Delta (Δ)",
    "formula": "$$\\text{Star (Y): } V_L = \\sqrt{3}\\, V_p \\angle +30^\\circ, \\quad I_L = I_p$$\n\n$$\\text{Delta (}\\Delta\\text{): } V_L = V_p, \\quad I_L = \\sqrt{3}\\, I_p \\angle -30^\\circ$$",
    "solution": "1. Star (Y) Connection:\n- Line Voltage leads Phase Voltage by $30^\\circ$:\n$$V_{ab} = \\sqrt{3}\\, V_{an} \\angle +30^\\circ$$\n- Line Current equals Phase Current:\n$$I_L = I_p$$\n\n2. Delta (Δ) Connection:\n- Line Voltage equals Phase Voltage:\n$$V_L = V_p$$\n- Line Current lags Phase Current by $30^\\circ$:\n$$I_a = \\sqrt{3}\\, I_{ab} \\angle -30^\\circ$$",
    "solution_th": "1. การต่อแบบ Star (Y):\n- Line Voltage นำหน้า (leads) Phase Voltage อยู่ $30^\\circ$:\n$$V_{ab} = \\sqrt{3}\\, V_{an} \\angle +30^\\circ$$\n- Line Current เท่ากับ Phase Current โดยตรง:\n$$I_L = I_p$$\n\n2. การต่อแบบ Delta (Δ):\n- Line Voltage เท่ากับ Phase Voltage โดยตรง:\n$$V_L = V_p$$\n- Line Current ตามหลัง (lags) Phase Current อยู่ $30^\\circ$:\n$$I_a = \\sqrt{3}\\, I_{ab} \\angle -30^\\circ$$",
    "pitfall": "In negative sequence (acb), line voltage leads by -30° (or lags by 30°). Remember: in Y, currents are identical; in Δ, voltages are identical.",
    "pitfall_th": "ข้อควรระวัง: หากเป็นลำดับเฟสลบ (Negative Sequence $acb$) มุมจะกลับทิศทางเป็น $-30^\\circ$ ทันที! ท่องจำง่ายๆ: ในวงจร Y กระแสเท่ากัน ($I_L = I_p$); ในวงจร $\\Delta$ แรงดันเท่ากัน ($V_L = V_p$)",
    "diagram": None,
    "mastered": False
})

cards.append({
    "id": "CH06-02",
    "chapter": "Chapter 6",
    "topic": "Delta to Wye (Δ ↔ Y) Impedance Conversion",
    "topic_th": "การแปลงค่าอิมพีแดนซ์ Delta เป็น Wye (Δ ↔ Y Impedance Conversion)",
    "level": "Level 1 (Concept)",
    "exam_reference": "HW Ch.6 Problem 1 & 5",
    "question": "If a balanced $3\\phi$ load is connected in $\\Delta$ with impedance $Z_\\Delta = 60 + j30\\ \\Omega$, what is the equivalent impedance per phase when converted to a Wye (Y) connection ($Z_Y$)?",
    "question_th": "ถ้าโหลด 3 เฟสแบบสมดุล (Balanced 3Φ Load) ต่อแบบ Delta (Δ) มีค่า Impedance $Z_\\Delta = 60 + j30\\ \\Omega$ จงหาค่า Impedance สมมูลต่อเฟสเมื่อแปลงเป็นการต่อแบบ Wye (Y) หรือ $Z_Y$",
    "formula": "$Z_Y = \\frac{Z_\\Delta}{3}\\quad \\Leftrightarrow\\quad Z_\\Delta = 3 Z_Y$",
    "solution": "$$Z_Y = \\frac{Z_\\Delta}{3} = \\frac{60 + j30}{3} = 20 + j10\\ \\Omega$$\nConversely, converting from Wye to Delta: $Z_\\Delta = 3 Z_Y$.",
    "solution_th": "$$Z_Y = \\frac{Z_\\Delta}{3} = \\frac{60 + j30}{3} = 20 + j10\\ \\Omega$$\nในทางกลับกัน หากแปลงจาก Wye ไปเป็น Delta จะใช้สูตร: $Z_\\Delta = 3 Z_Y$",
    "pitfall": "Multiplying by 3 instead of dividing is a classic mistake! Delta load draws 3 times more current than Wye load of the same impedance, so equivalent Wye impedance must be 3 times smaller.",
    "pitfall_th": "ข้อควรระวัง: อย่าจำสับสนระหว่างคูณ 3 กับหาร 3! โหลดแบบ Delta จะกินกระแสมากกว่า Wye ถึง 3 เท่า ดังนั้นเมื่อแปลงเป็น Wye อิมพีแดนซ์สมมูลต้องเล็กลง (หาร 3)",
    "diagram": None,
    "mastered": False
})

cards.append({
    "id": "CH06-03",
    "chapter": "Chapter 6",
    "topic": "Three-Phase Power Formulas & Complex Power",
    "topic_th": "สูตรกำลังไฟฟ้า 3 เฟส (Real, Reactive, Complex Power)",
    "level": "Level 1 (Concept)",
    "exam_reference": "Formula Sheet & Lecture Slides",
    "question": "State the formulas for balanced $3\\phi$ Real Power ($P_{3\\phi}$), Reactive Power ($Q_{3\\phi}$), Apparent Power ($|S_{3\\phi}|$), and Complex Power ($S_{3\\phi}$) in terms of line values ($V_L, I_L$).",
    "question_th": "จงเขียนสูตรคำนวณ Real Power ($P_{3\\phi}$), Reactive Power ($Q_{3\\phi}$), Apparent Power ($|S_{3\\phi}|$) และ Complex Power ($S_{3\\phi}$) ของระบบ 3 เฟสสมดุล ในรูปของปริมาณ Line ($V_L, I_L$)",
    "formula": "$P_{3\\phi} = \\sqrt{3}V_L I_L \\cos\\theta\\quad [\\text{W}]$\n$Q_{3\\phi} = \\sqrt{3}V_L I_L \\sin\\theta\\quad [\\text{VAR}]$\n$|S_{3\\phi}| = \\sqrt{3}V_L I_L\\quad [\\text{VA}]$\n$S_{3\\phi} = \\sqrt{3}V_L I_L^* = P + jQ$",
    "solution": "When using Line values ($V_L, I_L$), always include the factor $\\sqrt{3}$.\nWhen using Phase values ($V_p, I_p$), use factor $3$:\n- $P = 3 V_p I_p \\cos\\theta$\n- $Q = 3 V_p I_p \\sin\\theta$\n- $S = 3 V_p I_p^*$\nwhere $\\theta = \\angle Z_p$ is the load phase impedance angle, and $PF = \\cos\\theta$.",
    "solution_th": "เมื่อใช้ค่า Line ($V_L, I_L$) ต้องมีตัวคูณ $\\sqrt{3}$ เสมอ:\n- $P = \\sqrt{3} V_L I_L \\cos\\theta$\n- $Q = \\sqrt{3} V_L I_L \\sin\\theta$\n- $S = \\sqrt{3} V_L I_L^*$\nแต่ถ้าใช้ค่า Phase ($V_p, I_p$) ให้ใช้ตัวคูณ $3$:\n- $P = 3 V_p I_p \\cos\\theta$\nโดยที่ $\\theta$ คือมุมอิมพีแดนซ์ของโหลด และ Power Factor ($PF$) เท่ากับ $\\cos\\theta$",
    "pitfall": "Never mix $\\sqrt{3}$ with phase quantities! It is either $\\sqrt{3}V_L I_L$ or $3 V_p I_p$.",
    "pitfall_th": "ข้อควรระวัง: ห้ามนำ $\\sqrt{3}$ ไปคูณกับค่า Phase เด็ดขาด! กฎเหล็กคือ 'Line คู่ $\\sqrt{3}$ ส่วน Phase คู่ $3$'",
    "diagram": None,
    "mastered": False
})

cards.append({
    "id": "CH06-04",
    "chapter": "Chapter 6",
    "topic": "Balanced 4-Wire Y-Y System Full Calculation",
    "topic_th": "การคำนวณวงจร 3 เฟสสมดุลแบบ Y-Y (Balanced Y-Y Calculation)",
    "level": "Level 2 (Past Exam / Calc)",
    "exam_reference": "HW Ch.6 Problem 1 (Page 1)",
    "question": "In the balanced Y-Y circuit shown below, source phase voltages are $V_{an} = 220\\angle 0^\\circ\\text{ V}$, $V_{bn} = 220\\angle -120^\\circ\\text{ V}$, $V_{cn} = 220\\angle -240^\\circ\\text{ V}$. Line impedance $Z_{\\text{line}} = 10 + j5\\ \\Omega$. Balanced load impedance $Z_L = 20 + j50\\ \\Omega$. Find: (1) Line voltages $V_{ab}, V_{bc}, V_{ca}$, (2) Line currents $I_{aA}, I_{bB}, I_{cC}$, (3) Neutral current $I_{Nn}$, (4) Total $3\\phi$ complex power $S$.\n" + img_html('hw6_fig1_yy_balanced.png', 'Fig. 1: Balanced Y-Y System with Line Impedance'),
    "question_th": "จากวงจร balanced Y-Y ดังรูป แหล่งจ่ายมี Phase Voltage คือ $V_{an} = 220\\angle 0^\\circ\\text{ V}$, $V_{bn} = 220\\angle -120^\\circ\\text{ V}$, $V_{cn} = 220\\angle -240^\\circ\\text{ V}$ ค่า Line Impedance คือ $Z_{\\text{line}} = 10 + j5\\ \\Omega$ และ Load Impedance สมดุลคือ $Z_L = 20 + j50\\ \\Omega$ จงหา: (1) Line Voltages $V_{ab}, V_{bc}, V_{ca}$ (2) Line Currents $I_{aA}, I_{bB}, I_{cC}$ (3) Neutral Current $I_{Nn}$ (4) Total $3\\phi$ Complex Power $S$\n" + img_html('hw6_fig1_yy_balanced.png', 'รูปที่ 1: วงจร Balanced Y-Y พร้อม Line Impedance จากการบ้านบทที่ 6'),
    "formula": "$V_{ab} = \\sqrt{3}V_{an}\\angle +30^\\circ$\n$I_{aA} = \\frac{V_{an}}{Z_{\\text{line}} + Z_L}$\n$I_{Nn} = 0$\n$S_{3\\phi} = 3 V_{an} I_{aA}^*$",
    "solution": "1. Line Voltages:\n- $V_{ab} = \\sqrt{3}(220)\\angle (0^\\circ + 30^\\circ) = 381.05\\angle 30^\\circ\\text{ V}$\n- $V_{bc} = 381.05\\angle -90^\\circ\\text{ V}$\n- $V_{ca} = 381.05\\angle -210^\\circ\\text{ V}$\n\n2. Per-phase total impedance:\n$$Z_{\\text{total}} = (10 + j5) + (20 + j50) = 30 + j55\\ \\Omega = 62.65\\angle 61.39^\\circ\\ \\Omega$$\n\n3. Line Currents:\n- $I_{aA} = \\frac{220\\angle 0^\\circ}{62.65\\angle 61.39^\\circ} = 3.51\\angle -61.39^\\circ\\text{ A}$\n- $I_{bB} = 3.51\\angle -181.39^\\circ\\text{ A}$\n- $I_{cC} = 3.51\\angle 58.61^\\circ\\text{ A}$\n\n4. Neutral Current:\nIn a balanced system, $I_{Nn} = 0\\text{ A}$, $V_{Nn} = 0\\text{ V}$.\n\n5. Total $3\\phi$ Power:\n$$S = 3 \\times 220 \\times 3.51\\angle +61.39^\\circ = 2,316.6\\angle 61.39^\\circ\\text{ VA} = 1,109\\text{ W} + j2,034\\text{ VAR}$$",
    "solution_th": "1. คำนวณ Line Voltages:\n- $V_{ab} = \\sqrt{3}(220)\\angle (0^\\circ + 30^\\circ) = 381.05\\angle 30^\\circ\\text{ V}$\n- $V_{bc} = 381.05\\angle -90^\\circ\\text{ V}$\n- $V_{ca} = 381.05\\angle -210^\\circ\\text{ V}$\n\n2. คำนวณ Impedance รวมต่อเฟส:\n$$Z_{\\text{total}} = (10 + j5) + (20 + j50) = 30 + j55\\ \\Omega = 62.65\\angle 61.39^\\circ\\ \\Omega$$\n\n3. คำนวณ Line Currents:\n- $I_{aA} = \\frac{220\\angle 0^\\circ}{62.65\\angle 61.39^\\circ} = 3.51\\angle -61.39^\\circ\\text{ A}$\n- $I_{bB} = 3.51\\angle -181.39^\\circ\\text{ A}$\n- $I_{cC} = 3.51\\angle 58.61^\\circ\\text{ A}$\n\n4. คำนวณกระแสสายนิวทรัล (Neutral Current):\nในวงจรที่สมดุล กระแสทั้ง 3 เฟสจะหักล้างกันพอดี: $I_{Nn} = 0\\text{ A}$ และ $V_{Nn} = 0\\text{ V}$\n\n5. คำนวณ Complex Power รวม:\n$$S = 3 \\times 220 \\times 3.51\\angle +61.39^\\circ = 2,316.6\\angle 61.39^\\circ\\text{ VA} = 1,109\\text{ W} + j2,034\\text{ VAR}$$",
    "pitfall": "Always remember to conjugate the current ($I^*$) when calculating complex power: $S = V I^*$. The angle of $S$ equals the angle of $Z$.",
    "pitfall_th": "ข้อควรระวัง: เมื่อหา Complex Power ต้องสังยุคกระแส ($I^*$) เสมอ: $S = V I^*$ ซึ่งมุมของ $S$ จะต้องเท่ากับมุมของอิมพีแดนซ์ $Z$",
    "diagram": "images/diagrams/hw6_fig1_yy_balanced.png",
    "mastered": False
})

cards.append({
    "id": "CH06-05",
    "chapter": "Chapter 6",
    "topic": "Unbalanced 4-Wire Y-Y System with Neutral Wire",
    "topic_th": "วงจร Unbalanced 4-Wire Y-Y พร้อมสายนิวทรัล (มี $Z_{nN}$)",
    "level": "Level 2 (Past Exam / Calc)",
    "exam_reference": "HW Ch.6 Problem 2 (Page 2)",
    "question": "In the 4-wire Y-Y system shown below, the source is balanced $220\\text{ V}$ rms, line impedance $Z_{\\text{line}} = 10 + j5\\ \\Omega$, neutral line impedance $Z_{nN} = 10 + j5\\ \\Omega$, and the load is UNBALANCED: $Z_A = 20 + j50\\ \\Omega$, $Z_B = 10 + j50\\ \\Omega$, $Z_C = 20 + j20\\ \\Omega$. How do you solve for the Neutral Shift Voltage ($V_{Nn}$) and line currents?\n" + img_html('hw6_fig2_yy_unbalanced.png', 'Fig. 2: Unbalanced 4-Wire Y-Y with Neutral Impedance ZnN'),
    "question_th": "จากวงจร 4-Wire Y-Y ที่โหลดไม่สมดุล (Unbalanced Load) ดังรูป แหล่งจ่าย $220\\text{ V}$ rms มี Line Impedance $Z_{\\text{line}} = 10 + j5\\ \\Omega$ มี Neutral Line Impedance $Z_{nN} = 10 + j5\\ \\Omega$ และโหลดไม่สมดุล: $Z_A = 20 + j50\\ \\Omega, Z_B = 10 + j50\\ \\Omega, Z_C = 20 + j20\\ \\Omega$ จงระบุขั้นตอนการหา Neutral Shift Voltage ($V_{Nn}$) และ Line Currents\n" + img_html('hw6_fig2_yy_unbalanced.png', 'รูปที่ 2: วงจร Unbalanced 4-Wire Y-Y พร้อมสายนิวทรัล ZnN'),
    "formula": "$$V_{Nn} = \\frac{\\frac{V_{an}}{Z_a'} + \\frac{V_{bn}}{Z_b'} + \\frac{V_{cn}}{Z_c'}}{\\frac{1}{Z_a'} + \\frac{1}{Z_b'} + \\frac{1}{Z_c'} + \\frac{1}{Z_{nN}}}$$",
    "solution": "1. Millman's / Node Voltage at Neutral node N:\nLet node n be the reference ($0\\text{ V}$).\nTotal phase branch impedances:\n- $Z_a' = (10+j5) + (20+j50) = 30 + j55\\ \\Omega$\n- $Z_b' = (10+j5) + (10+j50) = 20 + j55\\ \\Omega$\n- $Z_c' = (10+j5) + (20+j20) = 30 + j25\\ \\Omega$\n- $Z_{nN} = 10 + j5\\ \\Omega$\n\n2. Solve for $V_{Nn}$ using KCL at node N:\n$$\\frac{V_N - V_{an}}{Z_a'} + \\frac{V_N - V_{bn}}{Z_b'} + \\frac{V_N - V_{cn}}{Z_c'} + \\frac{V_N}{Z_{nN}} = 0$$\n\n3. Calculate Line Currents:\n- $I_{aA} = \\frac{V_{an} - V_{Nn}}{Z_a'}$\n- $I_{bB} = \\frac{V_{bn} - V_{Nn}}{Z_b'}$\n- $I_{cC} = \\frac{V_{cn} - V_{Nn}}{Z_c'}$\n- $I_{Nn} = \\frac{V_{Nn}}{Z_{nN}} = I_{aA} + I_{bB} + I_{cC}$",
    "solution_th": "1. ใช้การวิเคราะห์ Node Voltage (ทฤษฎี Millman) ที่จุด Neutral N:\nกำหนดให้จุด n เป็นจุดอ้างอิง ($0\\text{ V}$)\nรวม Impedance ของแต่ละเฟส:\n- $Z_a' = (10+j5) + (20+j50) = 30 + j55\\ \\Omega$\n- $Z_b' = (10+j5) + (10+j50) = 20 + j55\\ \\Omega$\n- $Z_c' = (10+j5) + (20+j20) = 30 + j25\\ \\Omega$\n- $Z_{nN} = 10 + j5\\ \\Omega$\n\n2. ตั้งสมการ KCL หาแรงดัน $V_{Nn}$:\n$$\\frac{V_{Nn} - V_{an}}{Z_a'} + \\frac{V_{Nn} - V_{bn}}{Z_b'} + \\frac{V_{Nn} - V_{cn}}{Z_c'} + \\frac{V_{Nn}}{Z_{nN}} = 0$$\n\n3. คำนวณหากระแส Line และกระแสนิวทรัล:\n- $I_{aA} = \\frac{V_{an} - V_{Nn}}{Z_a'}$\n- $I_{bB} = \\frac{V_{bn} - V_{Nn}}{Z_b'}$\n- $I_{cC} = \\frac{V_{cn} - V_{Nn}}{Z_c'}$\n- $I_{Nn} = \\frac{V_{Nn}}{Z_{nN}} = I_{aA} + I_{bB} + I_{cC}$",
    "pitfall": "Do NOT assume $V_{Nn} = 0$! In an unbalanced system, current flows through the neutral wire, causing a non-zero neutral shift voltage $V_{Nn} \\neq 0$.",
    "pitfall_th": "ข้อควรระวัง: ห้ามสมมุติว่า $V_{Nn} = 0$ เด็ดขาด! เมื่อโหลดไม่สมดุล จะเกิดแรงดันเลื่อนจุดนิวทรัล (Neutral Shift) ทำให้แรงดันที่ตกคร่อมโหลดแต่ละเฟสไม่เท่ากัน",
    "diagram": "images/diagrams/hw6_fig2_yy_unbalanced.png",
    "mastered": False
})

cards.append({
    "id": "CH06-06",
    "chapter": "Chapter 6",
    "topic": "Unbalanced 3-Wire Y-Y System (NO Neutral Wire)",
    "topic_th": "วงจร Unbalanced 3-Wire Y-Y แบบไม่มีสายนิวทรัล (Floating Neutral)",
    "level": "Level 2 (Past Exam / Calc)",
    "exam_reference": "HW Ch.6 Problem 3 (Page 2)",
    "question": "In the 3-wire Y-Y system shown below (NO neutral wire), the load is unbalanced ($Z_A \\neq Z_B \\neq Z_C$). How is the neutral shift voltage $V_{Nn}$ calculated, and what happens to the neutral impedance term in the Millman formula?\n" + img_html('hw6_fig3_yy_neutral_z.png', 'Fig. 3: Unbalanced 3-Wire Y-Y System (No Neutral Wire)'),
    "question_th": "ในระบบ 3-Wire Y-Y ที่ไม่มีสายนิวทรัล (No Neutral Wire) ดังรูป โหลดไม่สมดุล ($Z_A \\neq Z_B \\neq Z_C$) จงอธิบายวิธีหา Neutral Shift Voltage $V_{Nn}$ และพจน์ $Z_{nN}$ ในสูตร Millman จะเปลี่ยนไปอย่างไร?\n" + img_html('hw6_fig3_yy_neutral_z.png', 'รูปที่ 3: วงจร Unbalanced 3-Wire Y-Y ที่ไม่มีสายนิวทรัล'),
    "formula": "$$V_{Nn} = \\frac{\\frac{V_{an}}{Z_a'} + \\frac{V_{bn}}{Z_b'} + \\frac{V_{cn}}{Z_c'}}{\\frac{1}{Z_a'} + \\frac{1}{Z_b'} + \\frac{1}{Z_c'}}$$\n$$I_{aA} + I_{bB} + I_{cC} = 0$$",
    "solution": "1. Floating Neutral Point:\nBecause there is no neutral conductor, $Z_{nN} = \\infty$, meaning the admittance term $\\frac{1}{Z_{nN}} = 0$.\n\n2. Node Voltage equation at N:\n$$V_{Nn} = \\frac{V_{an} Y_a' + V_{bn} Y_b' + V_{cn} Y_c'}{Y_a' + Y_b' + Y_c'}$$\nwhere $Y_x' = \\frac{1}{Z_x'}$.\n\n3. Zero Neutral Current:\nWithout a neutral path, $I_{Nn} = 0$ strictly holds, which means:\n$$I_{aA} + I_{bB} + I_{cC} = 0$$",
    "solution_th": "1. จุดนิวทรัลลอย (Floating Neutral):\nเนื่องจากไม่มีสายเชื่อมต่อนิวทรัล ค่า $Z_{nN} = \\infty$ ส่งผลให้ค่า Admittance $\\frac{1}{Z_{nN}} = 0$\n\n2. สมการ Node Voltage ที่จุด N จึงเหลือเพียง:\n$$V_{Nn} = \\frac{V_{an} Y_a' + V_{bn} Y_b' + V_{cn} Y_c'}{Y_a' + Y_b' + Y_c'}$$\n\n3. กระแสรวมเป็นศูนย์:\nเมื่อไม่มีทางเดินของกระแสนิวทรัล ผลบวกของกระแสไลน์ทั้งสามต้องเท่ากับศูนย์เสมอ:\n$$I_{aA} + I_{bB} + I_{cC} = 0$$",
    "pitfall": "Even though $I_{Nn} = 0$ (no physical wire), $V_{Nn}$ is NOT zero! The neutral point floats and shifts severely, subjecting some phases to dangerous overvoltages.",
    "pitfall_th": "ข้อควรระวัง: ถึงแม้จะไม่มีสายนิวทรัล ($I_{Nn} = 0$) แต่แรงดันจุดนิวทรัล $V_{Nn}$ ไม่เป็นศูนย์! จุด N จะลอยและเลื่อนไป ทำให้โหลดบางเฟสรับแรงดันเกิน (Overvoltage) จนเสียหายได้",
    "diagram": "images/diagrams/hw6_fig3_yy_neutral_z.png",
    "mastered": False
})

cards.append({
    "id": "CH06-07",
    "chapter": "Chapter 6",
    "topic": "3-Phase Motor Input Power, Efficiency & Line Current",
    "topic_th": "การคำนวณกำลังไฟฟ้า ประสิทธิภาพ และกระแสไลน์ของมอเตอร์ 3 เฟส",
    "level": "Level 2 (Past Exam / Calc)",
    "exam_reference": "HW Ch.6 Problem 4 (12 HP Y-Motor)",
    "question": "A $3\\phi, 12\\text{-hp}$ induction motor is connected in Y to a balanced $380\\text{ V}, 50\\text{ Hz}$ supply. The motor has efficiency $\\eta = 90\\%$ and $PF = 0.85$ lagging. Calculate: (1) Input electrical power $P_{\\text{in}}$, (2) Line current $I_L$, (3) Total complex power $S$, (4) Equivalent impedance per phase $Z_Y$.",
    "question_th": "มอเตอร์เหนี่ยวนำ 3 เฟส ขนาด 12 แรงม้า (12 hp) ต่อแบบ Y กับระบบไฟ $380\\text{ V}, 50\\text{ Hz}$ มอเตอร์มี Efficiency $\\eta = 90\\%$ และ Power Factor $PF = 0.85$ lagging จงคำนวณหา: (1) กำลังไฟฟ้าขาเข้า $P_{\\text{in}}$ (2) กระแสไลน์ $I_L$ (3) Complex Power รวม $S$ (4) Impedance ต่อเฟส $Z_Y$",
    "formula": "$$P_{\\text{out}} = 12 \\times 746\\text{ W} = 8,952\\text{ W}$$\n$$P_{\\text{in}} = \\frac{P_{\\text{out}}}{\\eta}$$\n$$I_L = \\frac{P_{\\text{in}}}{\\sqrt{3} V_L \\cdot PF}$$\n$$S = \\frac{P_{\\text{in}}}{PF}\\angle \\arccos(PF)$$",
    "solution": "1. Convert output power to Watts:\n$$P_{\\text{out}} = 12 \\times 746 = 8,952\\text{ W}$$\n\n2. Input Electrical Real Power:\n$$P_{\\text{in}} = \\frac{8,952}{0.90} = 9,946.67\\text{ W} \\approx 9.95\\text{ kW}$$\n\n3. Line Current ($I_L$):\n$$I_L = \\frac{9,946.67}{\\sqrt{3} \\times 380 \\times 0.85} = \\frac{9,946.67}{559.45} = 17.78\\text{ A}$$\n\n4. Complex Power ($S$):\n$$\\theta = \\arccos(0.85) = 31.79^\\circ$$\n$$|S| = \\frac{9.946}{0.85} = 11.70\\text{ kVA}$$\n$$S = 11.70\\angle 31.79^\\circ\\text{ kVA} = 9.95\\text{ kW} + j6.16\\text{ kVAR}$$\n\n5. Per-Phase Impedance ($Z_Y$):\n$$V_p = \\frac{380}{\\sqrt{3}} = 219.39\\text{ V}$$\n$$Z_Y = \\frac{V_p}{I_L} = \\frac{219.39}{17.78}\\angle 31.79^\\circ = 12.34\\angle 31.79^\\circ\\ \\Omega = 10.49 + j6.50\\ \\Omega$$\n($R = 10.49\\ \\Omega$, $L = \\frac{6.50}{2\\pi \\times 50} = 20.7\\text{ mH}$)",
    "solution_th": "1. แปลงกำลัง Output จากแรงม้าเป็นวัตต์:\n$$P_{\\text{out}} = 12 \\times 746 = 8,952\\text{ W}$$\n\n2. คำนวณ Input Electrical Power:\n$$P_{\\text{in}} = \\frac{8,952}{0.90} = 9,946.67\\text{ W} \\approx 9.95\\text{ kW}$$\n\n3. คำนวณ Line Current ($I_L$):\n$$I_L = \\frac{9,946.67}{\\sqrt{3} \\times 380 \\times 0.85} = 17.78\\text{ A}$$\n\n4. คำนวณ Complex Power ($S$):\n$$\\theta = \\arccos(0.85) = 31.79^\\circ$$\n$$|S| = \\frac{9.95}{0.85} = 11.70\\text{ kVA}$$\n$$S = 11.70\\angle 31.79^\\circ\\text{ kVA} = 9.95\\text{ kW} + j6.16\\text{ kVAR}$$\n\n5. คำนวณ Impedance ต่อเฟส ($Z_Y$):\n$$V_p = \\frac{380}{\\sqrt{3}} = 219.39\\text{ V}$$\n$$Z_Y = \\frac{V_p}{I_L} = 12.34\\angle 31.79^\\circ\\ \\Omega = 10.49 + j6.50\\ \\Omega$$\n(ได้ $R = 10.49\\ \\Omega$ และ $L = \\frac{6.50}{2\\pi \\times 50} = 20.7\\text{ mH}$)",
    "pitfall": "Remember: $1\\text{ hp} = 746\\text{ W}$. Horsepower is ALWAYS mechanical output power at the shaft ($P_{\\text{out}}$), never electrical input power ($P_{\\text{in}}$)!",
    "pitfall_th": "ข้อควรระวัง: $1\\text{ hp} = 746\\text{ W}$ และแรงม้า (hp) คือกำลังกลทาง Output ที่เพลาเสมอ! ห้ามนำไปคิดเป็น $P_{\\text{in}}$ ตรงๆ ต้องหารประสิทธิภาพ $\\eta$ ก่อน",
    "diagram": None,
    "mastered": False
})

cards.append({
    "id": "CH06-08",
    "chapter": "Chapter 6",
    "topic": "Delta-Connected 3-Phase Motor Analysis",
    "topic_th": "การคำนวณมอเตอร์ 3 เฟสที่ต่อแบบ Delta (Δ-Connected Motor)",
    "level": "Level 2 (Past Exam / Calc)",
    "exam_reference": "HW Ch.6 Problem 5 (10 HP Δ-Motor)",
    "question": "A $3\\phi, 10\\text{-hp}$ induction motor is connected in $\\Delta$ to a $380\\text{ V}, 50\\text{ Hz}$ supply. $\\eta = 85\\%, PF = 0.80$ lagging. Find: (1) Input power $P_{\\text{in}}$, (2) Line current $I_L$, (3) Phase winding current $I_\\Delta$, (4) Phase impedance $Z_\\Delta$.",
    "question_th": "มอเตอร์เหนี่ยวนำ 3 เฟส ขนาด 10 แรงม้า (10 hp) ขดลวดต่อแบบ Delta (Δ) เข้ากับไฟ $380\\text{ V}, 50\\text{ Hz}$ มี $\\eta = 85\\%, PF = 0.80$ lagging จงหา: (1) $P_{\\text{in}}$ (2) Line current $I_L$ (3) Phase current ในขดลวด $I_\\Delta$ (4) Phase impedance $Z_\\Delta$",
    "formula": "$$P_{\\text{in}} = \\frac{10 \\times 746}{0.85}$$\n$$I_L = \\frac{P_{\\text{in}}}{\\sqrt{3} V_L PF}$$\n$$I_\\Delta = \\frac{I_L}{\\sqrt{3}}$$\n$$Z_\\Delta = \\frac{V_L}{I_\\Delta}$$",
    "solution": "1. Input Power:\n$$P_{\\text{in}} = \\frac{7,460\\text{ W}}{0.85} = 8,776.47\\text{ W} = 8.78\\text{ kW}$$\n\n2. Line Current:\n$$I_L = \\frac{8,776.47}{\\sqrt{3} \\times 380 \\times 0.80} = 16.67\\text{ A}$$\n\n3. Delta Phase Current:\nIn $\\Delta$, line current divides: $I_\\Delta = \\frac{I_L}{\\sqrt{3}} = \\frac{16.67}{1.732} = 9.62\\text{ A}$\n\n4. Impedance per phase ($Z_\\Delta$):\nIn $\\Delta$, $V_p = V_L = 380\\text{ V}$.\n$$|Z_\\Delta| = \\frac{V_p}{I_\\Delta} = \\frac{380}{9.62} = 39.50\\ \\Omega$$\n$$\\theta = \\arccos(0.8) = 36.87^\\circ$$\n$$Z_\\Delta = 39.50\\angle 36.87^\\circ\\ \\Omega = 31.60 + j23.70\\ \\Omega$$",
    "solution_th": "1. คำนวณ Input Power:\n$$P_{\\text{in}} = \\frac{7,460\\text{ W}}{0.85} = 8,776.47\\text{ W} = 8.78\\text{ kW}$$\n\n2. คำนวณ Line Current:\n$$I_L = \\frac{8,776.47}{\\sqrt{3} \\times 380 \\times 0.80} = 16.67\\text{ A}$$\n\n3. คำนวณ Phase Current ในขดลวด Delta:\nในวงจร Delta กระแสไลน์จะแยกไหล: $I_\\Delta = \\frac{I_L}{\\sqrt{3}} = \\frac{16.67}{\\sqrt{3}} = 9.62\\text{ A}$\n\n4. คำนวณ Impedance ต่อเฟส ($Z_\\Delta$):\nใน Delta แรงดันเฟสเท่ากับแรงดันไลน์: $V_p = V_L = 380\\text{ V}$\n$$|Z_\\Delta| = \\frac{380}{9.62} = 39.50\\ \\Omega$$\n$$Z_\\Delta = 39.50\\angle 36.87^\\circ\\ \\Omega = 31.60 + j23.70\\ \\Omega$$",
    "pitfall": "In a Delta load, $V_p = V_L = 380\\text{ V}$, but $I_p = I_L / \\sqrt{3}$. Do not divide voltage by $\\sqrt{3}$ for a Delta load!",
    "pitfall_th": "ข้อควรระวัง: โหลดแบบ Delta แรงดันขดลวดจะเท่ากับแรงดันไลน์ ($V_p = 380\\text{ V}$) เต็มๆ ห้ามนำแรงดันไปหาร $\\sqrt{3}$!",
    "diagram": None,
    "mastered": False
})

cards.append({
    "id": "CH06-09",
    "chapter": "Chapter 6",
    "topic": "Two-Wattmeter Method for 3-Phase Power Measurement",
    "topic_th": "วิธีการวัดกำลังไฟฟ้า 3 เฟสด้วยวัตต์มิเตอร์ 2 ตัว (Two-Wattmeter Method)",
    "level": "Level 1 (Concept)",
    "exam_reference": "Final Exam & Lecture Notes",
    "question": "In the two-wattmeter method measuring a balanced 3-phase load, state the equations for total real power ($P_{\\text{total}}$), total reactive power ($Q_{\\text{total}}$), and the load power factor angle ($\\theta$) in terms of wattmeter readings $W_1$ and $W_2$.",
    "question_th": "ในการวัดกำลังไฟฟ้า 3 เฟสด้วยวัตต์มิเตอร์ 2 ตัว (Two-Wattmeter Method) จงระบุสูตรการหา Real Power รวม ($P_{\\text{total}}$), Reactive Power รวม ($Q_{\\text{total}}$) และมุม Power Factor ($\\theta$) จากค่าที่อ่านได้จากวัตต์มิเตอร์ $W_1$ และ $W_2$",
    "formula": "$$P_{\\text{total}} = W_1 + W_2$$\n$$Q_{\\text{total}} = \\sqrt{3}(W_1 - W_2)$$\n$$\\tan\\theta = \\sqrt{3}\\frac{W_1 - W_2}{W_1 + W_2}$$",
    "solution": "1. Total Active Power is simply the algebraic sum:\n$$P = W_1 + W_2$$\n\n2. Total Reactive Power is proportional to the difference:\n$$Q = \\sqrt{3}(W_1 - W_2)$$\n\n3. Phase angle of the load:\n$$\\theta = \\arctan\\left(\\sqrt{3}\\frac{W_1 - W_2}{W_1 + W_2}\\right)$$\n$$PF = \\cos\\theta$$\n\nSpecial Cases:\n- If $PF = 1.0$: $W_1 = W_2$\n- If $PF = 0.5$: One wattmeter reads zero ($W_2 = 0$)\n- If $PF < 0.5$: One wattmeter reads NEGATIVE!",
    "solution_th": "1. กำลังไฟฟ้าจริงรวม (Active Power) คือผลบวกทางพีชคณิต:\n$$P = W_1 + W_2$$\n\n2. กำลังไฟฟ้ารีแอกทีฟรวม (Reactive Power) ได้จากผลต่างคูณ $\\sqrt{3}$:\n$$Q = \\sqrt{3}(W_1 - W_2)$$\n\n3. หามุมและค่า Power Factor:\n$$\\tan\\theta = \\sqrt{3}\\frac{W_1 - W_2}{W_1 + W_2} \\quad\\Rightarrow\\quad PF = \\cos\\theta$$\n\nกรณีพิเศษที่ออกข้อสอบบ่อย:\n- ถ้า $PF = 1.0$ (Pure Resistive): $W_1 = W_2$\n- ถ้า $PF = 0.5$: วัตต์มิเตอร์ตัวหนึ่งจะอ่านได้ศูนย์พอดี ($W_2 = 0$)\n- ถ้า $PF < 0.5$: วัตต์มิเตอร์ตัวหนึ่งจะอ่านค่าติดลบ (เข็มตีกลับ)",
    "pitfall": "When $PF < 0.5$, one wattmeter reads negative! On an analog meter, reverse the current coil connections to read the value, then treat that reading as a negative number in $W_1 + W_2$.",
    "pitfall_th": "ข้อควรระวัง: หาก $PF < 0.5$ วัตต์มิเตอร์ตัวหนึ่งจะอ่านค่าติดลบ! ในห้องสอบหรือห้องแล็บต้องสลับขั้ว Current Coil เพื่อให้อ่านค่าได้ แล้วนำค่านั้นมาติดลบในสูตร",
    "diagram": None,
    "mastered": False
})

cards.append({
    "id": "CH06-10",
    "chapter": "Chapter 6",
    "topic": "Power Factor Correction with Delta Capacitors",
    "topic_th": "การปรับปรุง Power Factor ด้วยตัวเก็บประจุต่อแบบ Delta (Capacitor Bank)",
    "level": "Level 2 (Past Exam / Calc)",
    "exam_reference": "Lecture Slides & Final Review",
    "question": "A balanced $3\\phi$ inductive load of $30\\text{ kW}$ operates at $380\\text{ V}, 50\\text{ Hz}$ with $PF_1 = 0.65$ lagging. What total reactive power $Q_C$ must a capacitor bank supply to improve the power factor to $PF_2 = 0.95$ lagging, and what is the capacitance per phase if connected in Delta ($C_\\Delta$)?",
    "question_th": "โหลดอุปนัย 3 เฟสสมดุลขนาด $30\\text{ kW}$ ต่อกับระบบ $380\\text{ V}, 50\\text{ Hz}$ มี $PF_1 = 0.65$ lagging จงหา Reactive Power รวม $Q_C$ ที่ Capacitor Bank ต้องจ่ายเพื่อปรับปรุงให้ได้ $PF_2 = 0.95$ lagging และหาค่าความจุต่อเฟสเมื่อต่อแบบ Delta ($C_\\Delta$)",
    "formula": "$$Q_C = P(\\tan\\theta_1 - \\tan\\theta_2)$$\n$$C_\\Delta = \\frac{Q_{C,\\text{phase}}}{\\omega V_L^2} = \\frac{Q_C / 3}{2\\pi f V_L^2}$$",
    "solution": "1. Find power factor angles:\n- $\\theta_1 = \\arccos(0.65) = 49.46^\\circ \\Rightarrow \\tan\\theta_1 = 1.169$\n- $\\theta_2 = \\arccos(0.95) = 18.19^\\circ \\Rightarrow \\tan\\theta_2 = 0.329$\n\n2. Required 3-phase Reactive Power from Capacitors:\n$$Q_C = 30\\text{ kW} \\times (1.169 - 0.329) = 30 \\times 0.840 = 25.20\\text{ kVAR}$$\n\n3. Delta connection per-phase capacitance:\nEach branch sees full line voltage $V_L = 380\\text{ V}$ and supplies $Q_{C1} = \\frac{25,200}{3} = 8,400\\text{ VAR}$:\n$$C_\\Delta = \\frac{8,400}{2\\pi(50)(380)^2} = \\frac{8,400}{314.16 \\times 144,400} = 1.85 \\times 10^{-4}\\text{ F} = 185\\ \\mu\\text{F}$$",
    "solution_th": "1. หามุม $\\theta$ ของ Power Factor เดิมและใหม่:\n- $\\theta_1 = \\arccos(0.65) = 49.46^\\circ \\Rightarrow \\tan\\theta_1 = 1.169$\n- $\\theta_2 = \\arccos(0.95) = 18.19^\\circ \\Rightarrow \\tan\\theta_2 = 0.329$\n\n2. คำนวณ Reactive Power รวม $Q_C$ ที่ต้องชดเชย:\n$$Q_C = 30\\text{ kW} \\times (1.169 - 0.329) = 25.20\\text{ kVAR}$$\n\n3. คำนวณค่าคาปาซิแตนซ์ต่อเฟสเมื่อต่อแบบ Delta ($C_\\Delta$):\nใน Delta แต่ละแขนรับแรงดันไลน์ $V_L = 380\\text{ V}$ เต็มๆ และจ่ายกำลัง $Q_{C1} = \\frac{25,200}{3} = 8,400\\text{ VAR}$:\n$$C_\\Delta = \\frac{8,400}{2\\pi(50)(380)^2} = 185\\ \\mu\\text{F}$$",
    "pitfall": "Capacitors connected in Delta require 3 times LESS capacitance than Wye-connected capacitors ($C_\\Delta = C_Y / 3$) for the same reactive power, saving massive physical space and cost!",
    "pitfall_th": "ข้อควรระวัง: การต่อ Capacitor แบบ Delta จะใช้ค่าความจุน้อยกว่าแบบ Wye ถึง 3 เท่า ($C_\\Delta = \\frac{C_Y}{3}$) จึงนิยมต่อแบบ Delta ในภาคอุตสาหกรรมเพื่อประหยัดขนาดและต้นทุน",
    "diagram": None,
    "mastered": False
})

# =========================================================================
# CHAPTER 7: ELECTRIC MACHINERY (Cards 11 - 25)
# =========================================================================
cards.append({
    "id": "CH07-01",
    "chapter": "Chapter 7",
    "topic": "Right-Hand Grip Rule for Magnetic Field around a Conductor",
    "topic_th": "กฎมือขวาสำหรับทิศทางสนามแม่เหล็กรอบตัวนำ (Right-Hand Grip Rule)",
    "level": "Level 1 (Concept)",
    "exam_reference": "Final Exam Problem 4.1 (Page 28 - 2 Points)",
    "question": "Current flows upward along a straight vertical wire as shown below. Using the right-hand grip rule, sketch/state the direction of the magnetic field ($\vec{B}$) on both sides of the wire.\n" + img_html('exam_p28_prob41_right_hand.png', 'Exam Problem 4.1 (FunE-final.pdf Page 28)'),
    "question_th": "เมื่อมีกระแสไฟฟ้าไหลผ่านเส้นลวดตัวนำในทิศทางขึ้นดังรูป จงใช้กฎมือขวา (Right-Hand Grip Rule) เขียนทิศทางของสนามแม่เหล็กที่เกิดขึ้นจากกระแสไฟฟ้านี้ (ข้อสอบไฟนอลข้อ 4.1)\n" + img_html('exam_p28_prob41_right_hand.png', 'ข้อสอบไฟนอลข้อ 4.1 จาก FunE-final.pdf หน้า 28'),
    "formula": "Thumb = Current ($I$)\nFingers curl = Magnetic field ($\\vec{B}$)",
    "solution": "1. Align the right thumb with current flow pointing UPWARD.\n2. Curled fingers point:\n- Out of the page on the LEFT side (represented by dots $\\bullet$)\n- Into the page on the RIGHT side (represented by crosses $\\times$)",
    "solution_th": "1. ให้นิ้วหัวแม่มือขวาชี้ไปตามทิศทางของกระแสไฟฟ้า ($I$) ซึ่งชี้ขึ้นด้านบน\n2. ปลายนิ้วทั้งสี่ที่กำรอบเส้นลวดจะแสดงทิศทางของเส้นแรงสนามแม่เหล็ก ($\\vec{B}$):\n- ด้านซ้ายของลวด: สนามแม่เหล็กพุ่งออกจากระนาบกระดาษ แทนด้วยจุด (Dots $\\bullet$)\n- ด้านขวาของลวด: สนามแม่เหล็กพุ่งพุ่งทิ่มเข้าหาระนาบกระดาษ แทนด้วยกากบาท (Crosses $\\times$)",
    "pitfall": "Always use the RIGHT hand! Left-hand grip reverses all field directions.",
    "pitfall_th": "ข้อควรระวัง: ต้องใช้มือขวาเสมอ! หากเผลอใช้มือซ้าย ทิศทางจุดและกากบาทจะสลับข้างกันทันที",
    "diagram": "images/diagrams/exam_p28_prob41_right_hand.png",
    "mastered": False
})

cards.append({
    "id": "CH07-02",
    "chapter": "Chapter 7",
    "topic": "DC Motor Magnetic Force on Wire (Lorentz Force Rule)",
    "topic_th": "แรงแม่เหล็กกระทำต่อขดลวดใน DC Motor (Lorentz Force Rule)",
    "level": "Level 1 (Concept)",
    "exam_reference": "Final Exam Problem 4.2 (Page 28 - 3 Points)",
    "question": "In the DC motor setup shown below, the upper permanent magnet pole is North (N) and the lower is South (S). Current is applied to the loop. State: (1) Current direction, (2) Direction of magnetic field $\\vec{B}$, (3) Direction of resulting force $\\vec{F}$ on each coil side.\n" + img_html('exam_p28_prob42_motor_force.png', 'Exam Problem 4.2 (FunE-final.pdf Page 28)'),
    "question_th": "จากรูปการทดสอบแรงที่เกิดขึ้นใน DC Motor ถ้าแม่เหล็กถาวรด้านบนเป็นขั้วเหนือ (N) ด้านล่างเป็นขั้วใต้ (S) มีแหล่งจ่ายกระแสดังรูป จงเขียน: (1) ทิศทางการไหลของกระแสไฟฟ้า (2) ทิศทางของสนามแม่เหล็กถาวร (3) ทิศทางแรงที่เกิดขึ้นที่เส้นลวด (ข้อสอบไฟนอลข้อ 4.2)\n" + img_html('exam_p28_prob42_motor_force.png', 'ข้อสอบไฟนอลข้อ 4.2 จาก FunE-final.pdf หน้า 28'),
    "formula": "$$\\vec{F} = I(\\vec{L} \\times \\vec{B})$$",
    "solution": "1. Magnetic field $\\vec{B}$ points from North to South (DOWNWARD).\n2. Current flows from (+) terminal through the coil to (-) terminal.\n3. By Fleming's Left-Hand Rule (or $\\vec{L} \\times \\vec{B}$):\n- The two opposite coil sides experience opposing forces forming a clockwise or counterclockwise torque that rotates the rotor shaft.",
    "solution_th": "1. ทิศทางสนามแม่เหล็กถาวร $\\vec{B}$: พุ่งจากขั้วเหนือ (N) ด้านบน ลงสู่ขั้วใต้ (S) ด้านล่างเสมอ (ชี้ลง)\n2. ทิศทางกระแสไฟฟ้า: ไหลออกจากขั้วบวก (+) ผ่านขดลวดแล้วกลับเข้าขั้วลบ (-)\n3. ทิศทางแรงลัพธ์ $\\vec{F}$ บนเส้นลวด: ใช้กฎมือซ้ายของเฟลมมิ่ง (สำหรับ Motor) หรือ $\\vec{F} = I(\\vec{L} \\times \\vec{B})$ ทำให้เกิดแรงคู่ควบในทิศทางตรงกันข้ามกัน ผลักให้ขดลวดหมุนรอบแกน",
    "pitfall": "For motors, use Fleming's LEFT-hand rule. For generators, use Fleming's RIGHT-hand rule.",
    "pitfall_th": "ข้อควรระวัง: ท่องจำสูตรมือ: 'มอเตอร์ใช้มือซ้าย (Left-Hand) ไดนาโม/เครื่องกำเนิดไฟฟ้าใช้มือขวา (Right-Hand)'",
    "diagram": "images/diagrams/exam_p28_prob42_motor_force.png",
    "mastered": False
})

cards.append({
    "id": "CH07-03",
    "chapter": "Chapter 7",
    "topic": "DC Machine Stator vs Rotor & Electromagnet Pole Polarities",
    "topic_th": "โครงสร้าง Stator/Rotor และการระบุขั้วแม่เหล็ก N-S ในมอเตอร์",
    "level": "Level 1 (Concept)",
    "exam_reference": "Final Exam Problem 4.3 (Page 28 - 3 Points)",
    "question": "What are the two primary structural parts of an electric motor? For the electromagnet core shown below, identify the magnetic poles (N and S) established by the coil current.\n" + img_html('exam_p28_prob43_motor_poles.png', 'Exam Problem 4.3 (FunE-final.pdf Page 28)'),
    "question_th": "โครงสร้างมอเตอร์ประกอบด้วย 2 ส่วนหลักคืออะไร? และจากรูปขดลวดแม่เหล็กไฟฟ้าด้านล่าง ถ้ากระแสไหลตามที่ระบุ จงเขียนขั้ว N และ S ของแม่เหล็กไฟฟ้าลงในรูป (ข้อสอบไฟนอลข้อ 4.3)\n" + img_html('exam_p28_prob43_motor_poles.png', 'ข้อสอบไฟนอลข้อ 4.3 จาก FunE-final.pdf หน้า 28'),
    "formula": "$$\\text{Right-Hand Solenoid Rule: Fingers} \\rightarrow \\vec{I}_{\\text{curl}}, \\quad \\text{Thumb} \\rightarrow \\text{North Pole (N)}$$\n\n$$\\vec{F} = I (\\vec{L} \\times \\vec{B})$$",
    "solution": "1. The two essential parts are:\n- Stator (ส่วนที่อยู่กับที่): Stationary field frame providing magnetic flux $\\vec{B}$.\n- Rotor / Armature (ส่วนที่หมุนเคลื่อนที่): Rotating shaft carrying current coils that generate torque $\\vec{\\tau}$.\n\n2. Solenoid Pole Identification:\nUsing the right-hand coil rule, curl four fingers in the direction current wraps around the iron pole pieces. The thumb points toward the North pole (N) where magnetic flux emerges:\n$$\\text{Current direction: } \\vec{I} \\implies \\text{Magnetic dipole: } \\vec{m} \\parallel \\text{Thumb (N)}$$",
    "solution_th": "1. โครงสร้างหลัก 2 ส่วนของมอเตอร์:\n- Stator (ส่วนที่อยู่กับที่): สร้างสนามแม่เหล็กหลัก $\\vec{B}$\n- Rotor หรือ Armature (ส่วนที่หมุน): ตัดกับเส้นแรงแม่เหล็กเพื่อสร้างแรงบิดหมุน $\\vec{\\tau}$\n\n2. การระบุขั้วแม่เหล็ก N-S:\nใช้กฎมือขวาสำหรับโซเลนอยด์ (กำมือนิ้วทั้งสี่ตามทิศทางกระแส $\\vec{I}$ ที่พันรอบแกนเหล็ก) นิ้วหัวแม่มือจะชี้ไปยังทิศทางของขั้วเหนือ (N Pole) ที่เส้นแรงแม่เหล็กพุ่งออกเสมอ:\n$$\\text{ทิศทางกระแส: } \\vec{I} \\implies \\text{ขั้วเหนือ (N Pole): ตามทิศนิ้วหัวแม่มือ}$$",
    "pitfall": "Do not confuse the armature core with the stator frame. Stator provides the stationary B-field; rotor carries the torque-producing coils.",
    "pitfall_th": "ข้อควรระวัง: ห้ามสับสนระหว่าง Stator กับ Rotor: Stator คือโครงสร้างภายนอกที่อยู่นิ่ง ส่วน Rotor คือแกนเพลาภายในที่หมุน",
    "diagram": "images/diagrams/exam_p28_prob43_motor_poles.png",
    "mastered": False
})

cards.append({
    "id": "CH07-04",
    "chapter": "Chapter 7",
    "topic": "3-Phase Induction Motor & Squirrel-Cage Rotor Operation",
    "topic_th": "หลักการทำงานของ 3-Phase Induction Motor และโรเตอร์กรงกระรอก",
    "level": "Level 1 (Concept)",
    "exam_reference": "Final Exam Problem 4.4 (Page 27 - 8 Points)",
    "question": "Referring to the 3-phase induction motor diagram below: (1) What is a Squirrel-Cage Rotor and how does it work? (2) Explain the operating principle of a 3-phase induction motor. (3) How do you reverse its direction of rotation?\n" + img_html('exam_p27_prob44_induction_motor.png', 'Exam Problem 4.4 (FunE-final.pdf Page 27)'),
    "question_th": "จากรูป 3-Phase Induction Motor ดังกล่าว: (1) กรงกระรอก (Squirrel-Cage Rotor) คืออะไร มีหลักการทำงานอย่างไร? (2) จงอธิบายหลักการทำงานของมอเตอร์เหนี่ยวนำ 3 เฟส (3) การกลับทิศทางการหมุนของมอเตอร์ทำได้อย่างไร? (ข้อสอบไฟนอลข้อ 4.4)\n" + img_html('exam_p27_prob44_induction_motor.png', 'ข้อสอบไฟนอลข้อ 4.4 จาก FunE-final.pdf หน้า 27'),
    "formula": "$$n_s = \\frac{120 f}{P}$$\n$$s = \\frac{n_s - n_r}{n_s}$$",
    "solution": "1. Squirrel-Cage Rotor (โรเตอร์แบบกรงกระรอก):\nConsists of conducting aluminum/copper bars embedded in laminated iron core, short-circuited at both ends by end-rings. When the rotating magnetic field sweeps across the bars, it induces currents producing torque.\n\n2. Operating Principle:\n3-phase stator currents produce a Constant-Magnitude Rotating Magnetic Field (RMF) spinning at synchronous speed $n_s = 120f/P$. By Faraday-Lenz law, this field cuts rotor bars, inducing voltage and rotor currents. The interaction generates Lorentz torque, pulling the rotor in the direction of the rotating field.\n\n3. Direction Reversal:\nSwap ANY TWO supply phase lines (e.g., swap A and B, keeping C fixed). This reverses the phase sequence and rotates the RMF in the opposite direction.",
    "solution_th": "1. กรงกระรอก (Squirrel-Cage Rotor):\nคือแท่งตัวนำทองแดงหรืออะลูมิเนียมฝังในร่องแกนเหล็ก แล้วลัดวงจรหัวท้ายด้วยวงแหวน (End Rings) เมื่อสนามแม่เหล็กหมุนตัดผ่าน จะเกิดกระแสเหนี่ยวนำไหลวนจนเกิดแรงบิดหมุน\n\n2. หลักการทำงานของ 3-Phase Induction Motor:\nกระแส 3 เฟสใน Stator สร้างสนามแม่เหล็กหมุน (Rotating Magnetic Field) ที่หมุนด้วยความเร็วซิงโครนัส $n_s = 120f/P$ สนามแม่เหล็กนี้จะตัดกับแท่งตัวนำ Rotor เกิดแรงดันเหนี่ยวนำและกระแสไหล ทำให้เกิดแรงผลักฉุดให้ Rotor หมุนตามสนามแม่เหล็ก\n\n3. การกลับทิศทางการหมุน:\nทำได้ง่ายมากโดยการ 'สลับสายเมนคู่ใดคู่หนึ่ง' (เช่น สลับคู่ Phase A กับ B โดยคงสาย Phase C ไว้เดิม) ลำดับเฟสจะกลับทิศ ทำให้ทิศทางสนามแม่เหล็กหมุนกลับด้านทันที",
    "pitfall": "The rotor can NEVER reach synchronous speed ($n_r < n_s$). If $n_r = n_s$, relative velocity is zero, no voltage is induced, and torque drops to zero!",
    "pitfall_th": "ข้อควรระวัง: โรเตอร์ของ Induction Motor ไม่มีทางหมุนเร็วเท่าความเร็วซิงโครนัสได้ ($n_r < n_s$ เสมอ) เพราะถ้าเร็วเท่ากัน จะไม่มีการตัดเส้นแรงแม่เหล็ก แรงดันเหนี่ยวนำและทอร์กจะกลายเป็นศูนย์ทันที",
    "diagram": "images/diagrams/exam_p27_prob44_induction_motor.png",
    "mastered": False
})

cards.append({
    "id": "CH07-05",
    "chapter": "Chapter 7",
    "topic": "DC Generator Principle & Commutator Rectification",
    "topic_th": "หลักการทำงานของเครื่องกำเนิดไฟฟ้ากระแสตรง (DC Generator)",
    "level": "Level 1 (Concept)",
    "exam_reference": "Final Exam Problem 4.5 (Page 26 - 4 Points)",
    "question": "What machine is shown in the diagram below and how does it work? Explain how the split-ring commutator converts induced AC into pulsating DC at the output terminals.\n" + img_html('exam_p26_prob45_generator.png', 'Exam Problem 4.5 (FunE-final.pdf Page 26)'),
    "question_th": "รูปด้านล่างคืออุปกรณ์อะไร และมีหลักการทำงานอย่างไร? จงอธิบายการทำงานของ Split-ring Commutator ในการแปลงแรงดันสลับให้เป็นกระแสตรงพัลส์ (ข้อสอบไฟนอลข้อ 4.5)\n" + img_html('exam_p26_prob45_generator.png', 'ข้อสอบไฟนอลข้อ 4.5 จาก FunE-final.pdf หน้า 26'),
    "formula": "$$e = B\\ell v \\sin\\theta$$\n$$E_a = k_a \\phi \\omega_m$$",
    "solution": "1. Identification:\nSingle-phase DC Generator with split-ring commutator.\n\n2. Principle of Operation:\nMechanical power drives the coil rotating in the magnetic field between permanent magnet poles. By Faraday's Law, an alternating electromotive force ($e = B\\ell v$) is induced inside the rotating coil.\n\n3. Commutator Action:\nThe split-ring commutator mechanically reverses coil connections to the external stationary carbon brushes every half revolution, rectifying the internal alternating AC into unidirectional pulsating DC.",
    "solution_th": "1. ระบุชื่ออุปกรณ์:\nเครื่องกำเนิดไฟฟ้ากระแสตรง (Single-phase DC Generator) พร้อมชุดคอมมิวเตเตอร์แบบผ่าซีก (Split-ring Commutator)\n\n2. หลักการทำงาน:\nพลังงานกลจากภายนอกหมุนขับขดลวดอาร์เมเจอร์ในช่องว่างสนามแม่เหล็ก ตามกฎของฟาราเดย์จะเกิดแรงดันไฟฟ้าเหนี่ยวนำกระแสสลับ ($e = B\\ell v$) ภายในขดลวด\n\n3. การทำงานของคอมมิวเตเตอร์:\nวงแหวนผ่าซีก (Split-ring) และแปรงถ่าน (Carbon Brushes) ทำหน้าที่เป็นสวิตช์กลไก สลับขั้วต่อทุกๆ ครึ่งรอบการหมุน ทำให้กระแสที่ส่งออกไปยังโหลดภายนอกไหลในทิศทางเดียวเสมอ (Unidirectional Pulsating DC)",
    "pitfall": "Inside ANY rotating DC armature, the induced voltage is ALWAYS AC! The commutator is what converts internal AC into external DC.",
    "pitfall_th": "ข้อควรระวัง: แรงดันที่เกิดขึ้นภายในขดลวดอาร์เมเจอร์ของเครื่องกล DC ทุกชนิดเป็น 'ไฟฟ้ากระแสสลับ (AC)' เสมอ! คอมมิวเตเตอร์ทำหน้าที่เป็นตัวแปลงกลไกให้เป็น DC ภายนอก",
    "diagram": "images/diagrams/exam_p26_prob45_generator.png",
    "mastered": False
})

cards.append({
    "id": "CH07-06",
    "chapter": "Chapter 7",
    "topic": "DC Shunt Motor Equivalent Circuit, Speed & Torque",
    "topic_th": "วงจรสมมูล การคำนวณความเร็วรอบ และทอร์กของ DC Shunt Motor",
    "level": "Level 2 (Past Exam / Calc)",
    "exam_reference": "HW Ch.7 Problem 4 & Talui Homework Page 1",
    "question": "A 2-pole, $2.5\\text{-hp}, 100\\text{ VDC}$ shunt motor has design constant $k_a = 153$. At full load, $I_t = 25.0\\text{ A}, R_a = 0.75\\ \\Omega, \\phi = 10.0\\text{ mWb}, R_f = 440\\ \\Omega$. Draw the equivalent circuit, and calculate: (1) Back EMF $E_a$, (2) Rotational speed $n$ [rpm], (3) Developed torque $\\tau_d$ [N·m].\n" + img_html('hw7_p4_shunt_circuit.png', 'DC Shunt Motor Equivalent Circuit (HW Ch.7 Prob 4)'),
    "question_th": "ดีซีชันต์มอเตอร์ (DC Shunt Motor) 2 poles ขนาด $2.5\\text{ hp}, 100\\text{ VDC}$ มีค่าคงที่ $k_a = 153$ ขณะ Full Load กินกระแสรวม $I_t = 25.0\\text{ A}, R_a = 0.75\\ \\Omega, \\phi = 10.0\\text{ mWb}, R_f = 440\\ \\Omega$ จงวาดวงจรสมมูลและคำนวณ: (1) Back EMF $E_a$ (2) ความเร็วรอบ $n$ (rpm) (3) Developed Torque $\\tau_d$ (N·m)\n" + img_html('hw7_p4_shunt_circuit.png', 'วงจรสมมูล DC Shunt Motor จากการบ้านบทที่ 7 ข้อ 4'),
    "formula": "$$I_f = \\frac{V_t}{R_f},\\quad I_a = I_t - I_f$$\n$$E_a = V_t - I_a R_a = k_a \\phi \\omega_m$$\n$$\\omega_m = \\frac{2\\pi n}{60},\\quad \\tau_d = k_a \\phi I_a$$",
    "solution": "1. Field current & Armature current:\n$$I_f = \\frac{V_t}{R_f} = \\frac{100}{440} = 0.23\\text{ A}$$\n$$I_a = I_t - I_f = 25.0 - 0.23 = 24.77\\text{ A}$$\n\n2. Back EMF ($E_a$):\n$$E_a = V_t - I_a R_a = 100 - (24.77 \\times 0.75) = 100 - 18.58 = 81.42\\text{ V}$$\n\n3. Speed ($n$):\n$$E_a = k_a \\phi \\omega_m \\Rightarrow 81.42 = 153 \\times (10 \\times 10^{-3}) \\times \\omega_m$$\n$$\\omega_m = \\frac{81.42}{1.53} = 53.22\\text{ rad/s}$$\n$$n = \\frac{60 \\times \\omega_m}{2\\pi} = \\frac{60 \\times 53.22}{2\\pi} = 508.17\\text{ rpm}$$\n\n4. Developed Torque ($\\tau_d$):\n$$\\tau_d = k_a \\phi I_a = 153 \\times (10 \\times 10^{-3}) \\times 24.77 = 37.90\\text{ N}\\cdot\\text{m}$$",
    "solution_th": "1. คำนวณกระแสฟิลด์ ($I_f$) และกระแสอาร์เมเจอร์ ($I_a$):\n$$I_f = \\frac{V_t}{R_f} = \\frac{100}{440} = 0.23\\text{ A}$$\n$$I_a = I_t - I_f = 25.0 - 0.23 = 24.77\\text{ A}$$\n\n2. คำนวณหาแรงดันต้านกลับ (Back EMF $E_a$):\n$$E_a = V_t - I_a R_a = 100 - (24.77 \\times 0.75) = 81.42\\text{ V}$$\n\n3. คำนวณหาความเร็วรอบ $n$ (rpm):\n$$E_a = k_a \\phi \\omega_m \\Rightarrow 81.42 = 153 \\times (10 \\times 10^{-3}) \\times \\omega_m$$\n$$\\omega_m = 53.22\\text{ rad/s} \\quad\\Rightarrow\\quad n = \\frac{60 \\times 53.22}{2\\pi} = 508.17\\text{ rpm}$$\n\n4. คำนวณหาทอร์กที่เพลา (Developed Torque $\\tau_d$):\n$$\\tau_d = k_a \\phi I_a = 153 \\times (10 \\times 10^{-3}) \\times 24.77 = 37.90\\text{ N}\\cdot\\text{m}$$",
    "pitfall": "In a Shunt motor, $I_t = I_a + I_f$. Do NOT use total line current $I_t$ in $V_t - I R_a$; only $I_a$ passes through the armature resistance!",
    "pitfall_th": "ข้อควรระวัง: ในดีซีชันต์มอเตอร์ กระแสรวมคือ $I_t = I_a + I_f$ ห้ามนำกระแสรวม $I_t$ ไปคิดแรงดันตกคร่อมอาร์เมเจอร์ ($I_a R_a$) เด็ดขาด ต้องลบกระแสฟิลด์ $I_f$ ออกก่อนเสมอ",
    "diagram": "images/diagrams/hw7_p4_shunt_circuit.png",
    "mastered": False
})

cards.append({
    "id": "CH07-07",
    "chapter": "Chapter 7",
    "topic": "DC Series Motor Circuit & Terminal Voltage Calculation",
    "topic_th": "วงจรสมมูล และการคำนวณ Terminal Voltage ของ DC Series Motor",
    "level": "Level 2 (Past Exam / Calc)",
    "exam_reference": "HW Ch.7 Problem 5 & Talui Homework Page 2",
    "question": "A 2-pole, $2.5\\text{-hp}$ DC Series motor has $k_a = 153, R_a = 0.75\\ \\Omega, R_f = 440\\ \\Omega, \\phi = 10.0\\text{ mWb}$. Find: (a) Terminal voltage $V_{t1}$ giving the SAME SPEED ($n = 508.17\\text{ rpm}$) as Problem 4, (b) Terminal voltage $V_{t2}$ giving the SAME TORQUE ($\\tau_d = 37.9\\text{ N}\\cdot\\text{m}$) as Problem 4.\n" + img_html('hw7_p5_series_circuit.png', 'DC Series Motor Equivalent Circuit (HW Ch.7 Prob 5)'),
    "question_th": "ดีซีซีรีส์มอเตอร์ (DC Series Motor) 2 poles ขนาด $2.5\\text{ hp}$ มี $k_a = 153, R_a = 0.75\\ \\Omega, R_f = 440\\ \\Omega, \\phi = 10.0\\text{ mWb}$ จงหา: (a) $V_{t1}$ ที่ทำให้ได้ความเร็วรอบเท่ากับข้อ 4 ($n = 508.17\\text{ rpm}$) (b) $V_{t2}$ ที่ทำให้ได้ทอร์กเท่ากับข้อ 4 ($\\tau_d = 37.9\\text{ N}\\cdot\\text{m}$)\n" + img_html('hw7_p5_series_circuit.png', 'วงจรสมมูล DC Series Motor จากการบ้านบทที่ 7 ข้อ 5'),
    "formula": "Series connection: $I_t = I_a = I_f$\n$$V_t = E_a + I_a(R_a + R_f)$$",
    "solution": "1. Part (a) Same Speed ($n = 508.17\\text{ rpm}$):\n$E_a = k_a \\phi \\omega_m = 81.42\\text{ V}$.\nFrom power $P_e = E_a I_a = 1,865\\text{ W} \\Rightarrow I_a = \\frac{1,865}{81.42} = 22.91\\text{ A}$.\n$$V_{t1} = E_a + I_a(R_a + R_f) = 81.42 + 22.91(0.75 + 440) = 81.42 + 10,097.6 = 10.18\\text{ kV}$$\n\n2. Part (b) Same Torque ($\\tau_d = 37.9\\text{ N}\\cdot\\text{m}$):\nFrom $\\tau_d = k_a \\phi I_a \\Rightarrow I_a = 24.77\\text{ A}$.\n$P_e = E_a I_a = 1,865\\text{ W} \\Rightarrow E_a = \\frac{1,865}{24.77} = 75.30\\text{ V}$.\n$$V_{t2} = E_a + I_a(R_a + R_f) = 75.30 + 24.77(440.75) = 11.00\\text{ kV}$$",
    "solution_th": "1. ข้อ (a) เมื่อต้องการความเร็วเท่าเดิม ($n = 508.17\\text{ rpm}$):\nได้แรงดัน $E_a = k_a \\phi \\omega_m = 81.42\\text{ V}$\nหากำลังกล $P_e = E_a I_a = 1,865\\text{ W} \\Rightarrow I_a = \\frac{1,865}{81.42} = 22.91\\text{ A}$\nคำนวณ $V_{t1}$ จาก KVL:\n$$V_{t1} = E_a + I_a(R_a + R_f) = 81.42 + 22.91(440.75) = 10.18\\text{ kV}$$\n\n2. ข้อ (b) เมื่อต้องการทอร์กเท่าเดิม ($\\tau_d = 37.9\\text{ N}\\cdot\\text{m}$):\nจาก $\\tau_d = k_a \\phi I_a \\Rightarrow I_a = 24.77\\text{ A}$\nจาก $P_e = 1,865\\text{ W} \\Rightarrow E_a = \\frac{1,865}{24.77} = 75.30\\text{ V}$\n$$V_{t2} = 75.30 + 24.77(440.75) = 11.00\\text{ kV}$$",
    "pitfall": "In a Series motor, the field winding is in series with the armature ($I_a = I_f = I_t$). The total circuit resistance is $R_a + R_f$.",
    "pitfall_th": "ข้อควรระวัง: ในซีรีส์มอเตอร์ ขดลวดฟิลด์ต่ออนุกรมกับอาร์เมเจอร์ ($I_a = I_f = I_t$) ความต้านทานรวมในวงจรจึงเป็น $R_a + R_f$",
    "diagram": "images/diagrams/hw7_p5_series_circuit.png",
    "mastered": False
})

cards.append({
    "id": "CH07-08",
    "chapter": "Chapter 7",
    "topic": "DC Shunt Motor Speed Control via Armature Resistance",
    "topic_th": "การควบคุมความเร็วรอบ DC Shunt Motor ด้วยความต้านทานอนุกรม",
    "level": "Level 2 (Past Exam / Calc)",
    "exam_reference": "FunE-final.pdf Page 5 (Example 3)",
    "question": "A $220\\text{ V}$ DC shunt motor has $R_a = 0.5\\ \\Omega, R_f = 110\\ \\Omega$. At full load, $I_t = 42\\text{ A}$ and speed $n_1 = 1,200\\text{ rpm}$. If an external resistor $R_{\\text{ext}} = 1.0\\ \\Omega$ is inserted in series with the armature while torque remains constant, calculate the new motor speed $n_2$.",
    "question_th": "ดีซีชันต์มอเตอร์ $220\\text{ V}$ มี $R_a = 0.5\\ \\Omega, R_f = 110\\ \\Omega$ ขณะ Full load กินกระแส $I_t = 42\\text{ A}$ และความเร็วรอบ $n_1 = 1,200\\text{ rpm}$ หากนำความต้านทานภายนอก $R_{\\text{ext}} = 1.0\\ \\Omega$ มาต่ออนุกรมกับขดลวดอาร์เมเจอร์ โดยที่โหลดมีทอร์กคงที่ จงคำนวณหาความเร็วรอบใหม่ $n_2$",
    "formula": "$$E_{a1} = V_t - I_{a1} R_a$$\n$$E_{a2} = V_t - I_{a2}(R_a + R_{\\text{ext}})$$\n$$\\frac{n_2}{n_1} = \\frac{E_{a2}}{E_{a1}}\\quad (\\text{when }\\phi\\text{ is constant})$$",
    "solution": "1. Initial condition:\n$$I_f = \\frac{220}{110} = 2.0\\text{ A}$$\n$$I_{a1} = 42 - 2 = 40.0\\text{ A}$$\n$$E_{a1} = 220 - (40 \\times 0.5) = 220 - 20 = 200\\text{ V}$$\n\n2. New condition with $R_{\\text{ext}} = 1.0\\ \\Omega$:\nConstant torque and constant flux $\\Rightarrow I_{a2} = I_{a1} = 40.0\\text{ A}$.\n$$E_{a2} = 220 - 40(0.5 + 1.0) = 220 - 60 = 160\\text{ V}$$\n\n3. Calculate new speed:\n$$\\frac{n_2}{1200} = \\frac{160}{200} = 0.80 \\Rightarrow n_2 = 1,200 \\times 0.80 = 960\\text{ rpm}$$",
    "solution_th": "1. สภาวะเริ่มต้น:\n$$I_f = \\frac{220}{110} = 2.0\\text{ A}$$\n$$I_{a1} = 42 - 2 = 40.0\\text{ A}$$\n$$E_{a1} = 220 - (40 \\times 0.5) = 200\\text{ V}$$\n\n2. สภาวะใหม่เมื่อต่อ $R_{\\text{ext}} = 1.0\\ \\Omega$:\nเนื่องจากทอร์กและฟลักซ์คงที่ $\\Rightarrow I_{a2} = I_{a1} = 40.0\\text{ A}$\n$$E_{a2} = 220 - 40(0.5 + 1.0) = 220 - 60 = 160\\text{ V}$$\n\n3. หาความเร็วรอบใหม่:\n$$\\frac{n_2}{1,200} = \\frac{160}{200} = 0.80 \\quad\\Rightarrow\\quad n_2 = 960\\text{ rpm}$$",
    "pitfall": "Adding armature resistance can ONLY reduce speed below base speed ($n < n_{\\text{base}}$). To run above base speed, field weakening (reducing $I_f$) is required.",
    "pitfall_th": "ข้อควรระวัง: การเพิ่มความต้านทานในวงจรอาร์เมเจอร์ทำได้เฉพาะ 'ลดความเร็วรอบให้ต่ำกว่าพิกัด' ($n < n_{\\text{base}}$) เท่านั้น หากต้องการเร่งความเร็วให้สูงกว่าพิกัด ต้องลดกระแสฟิลด์ (Field Weakening)",
    "diagram": None,
    "mastered": False
})

cards.append({
    "id": "CH07-09",
    "chapter": "Chapter 7",
    "topic": "DC Shunt Generator Voltage Regulation & KVL",
    "topic_th": "สมการ KVL และ Voltage Regulation ของ DC Shunt Generator",
    "level": "Level 2 (Past Exam / Calc)",
    "exam_reference": "FunE-final.pdf Page 4 (Example 2)",
    "question": "A DC shunt generator driven at $1,800\\text{ rpm}$ produces no-load terminal voltage $V_t = 115\\text{ V}$. When connected to a load, $I_a = 40\\text{ A}$ and terminal voltage drops to $V_t = 100\\text{ V}$. Find: (1) Armature resistance $R_a$, (2) Voltage regulation ($VR\\%$), (3) Counter-torque $\\tau_d$ at full load if $\\phi = 10\\text{ mWb}$.",
    "question_th": "เครื่องกำเนิดไฟฟ้าดีซีชันต์ หมุนด้วยความเร็ว $1,800\\text{ rpm}$ วัดแรงดันที่ขั้วขณะ No-load ได้ $V_t = 115\\text{ V}$ เมื่อต่อจ่ายโหลด วัดกระแสอาร์เมเจอร์ได้ $I_a = 40\\text{ A}$ และแรงดันขั้วลดลงเหลือ $V_t = 100\\text{ V}$ จงหา: (1) ความต้านทานอาร์เมเจอร์ $R_a$ (2) เปอร์เซ็นต์การคุมค่าแรงดัน ($VR\\%$) (3) ทอร์กต้านทางกล $\\tau_d$ เมื่อ $\\phi = 10\\text{ mWb}$",
    "formula": "Generator KVL: $$E_a = V_t + I_a R_a$$\n$$VR\\% = \\frac{V_{NL} - V_{FL}}{V_{FL}} \\times 100\\%$$",
    "solution": "1. Armature Resistance ($R_a$):\nAt no load ($I_a = 0$), $E_a = V_{NL} = 115\\text{ V}$.\nAt full load: $115 = 100 + (40 \\times R_a) \\Rightarrow R_a = \\frac{15}{40} = 0.375\\ \\Omega$.\n\n2. Voltage Regulation:\n$$VR\\% = \\frac{115 - 100}{100} \\times 100\\% = 15.0\\%$$\n\n3. Counter Torque ($\\tau_d$):\n$$\\omega_m = \\frac{2\\pi(1,800)}{60} = 60\\pi = 188.5\\text{ rad/s}$$\n$$P_e = E_a I_a = 115 \\times 40 = 4,600\\text{ W}$$\n$$\\tau_d = \\frac{P_e}{\\omega_m} = \\frac{4,600}{188.5} = 24.40\\text{ N}\\cdot\\text{m}$$",
    "solution_th": "1. ความต้านทานอาร์เมเจอร์ ($R_a$):\nขณะ No-load ($I_a = 0$) จะได้ $E_a = V_{NL} = 115\\text{ V}$\nขณะจ่ายโหลด: $115 = 100 + (40 \\times R_a) \\Rightarrow R_a = \\frac{15}{40} = 0.375\\ \\Omega$\n\n2. เปอร์เซ็นต์การคุมแรงดัน ($VR\\%$):\n$$VR\\% = \\frac{115 - 100}{100} \\times 100\\% = 15.0\\%$$\n\n3. ทอร์กต้านทางกล (Counter Torque $\\tau_d$):\n$$\\omega_m = \\frac{2\\pi(1,800)}{60} = 188.5\\text{ rad/s}$$\n$$P_e = E_a I_a = 115 \\times 40 = 4,600\\text{ W} \\quad\\Rightarrow\\quad \\tau_d = \\frac{4,600}{188.5} = 24.40\\text{ N}\\cdot\\text{m}$$",
    "pitfall": "Generator KVL has a PLUS sign ($E_a = V_t + I_a R_a$), while Motor KVL has a MINUS sign ($E_a = V_t - I_a R_a$)! In a generator, internal generated EMF is higher than terminal voltage.",
    "pitfall_th": "ข้อควรระวัง: เครื่องกำเนิดไฟฟ้าใช้เครื่องหมายบวก ($E_a = V_t + I_a R_a$) เพราะสร้างแรงดันส่งออกภายนอก ส่วนมอเตอร์ใช้เครื่องหมายลบ ($E_a = V_t - I_a R_a$)",
    "diagram": None,
    "mastered": False
})

cards.append({
    "id": "CH07-10",
    "chapter": "Chapter 7",
    "topic": "Induction Motor Synchronous Speed, Rotor Speed & Slip",
    "topic_th": "ความเร็วซิงโครนัส ความเร็วโรเตอร์ และค่าสลิป (Slip) ของมอเตอร์เหนี่ยวนำ",
    "level": "Level 1 (Concept)",
    "exam_reference": "Lecture Slides & Final Exam",
    "question": "A 4-pole, $50\\text{ Hz}$ three-phase induction motor runs at $1,440\\text{ rpm}$ at full load. Calculate: (1) Synchronous speed $n_s$, (2) Fractional slip $s$ and percent slip $s\\%$, (3) Rotor current frequency $f_r$, (4) Rotor speed at locked rotor ($s=1$).",
    "question_th": "มอเตอร์เหนี่ยวนำ 3 เฟส ขนาด 4 poles, $50\\text{ Hz}$ ขณะรับโหลดเต็มที่หมุนด้วยความเร็ว $1,440\\text{ rpm}$ จงคำนวณหา: (1) Synchronous Speed $n_s$ (2) Fractional Slip $s$ และ Percent Slip $s\\%$ (3) ความถี่ของกระแสในโรเตอร์ $f_r$ (4) ความเร็วโรเตอร์ขณะหยุดนิ่งถูกล็อกเพลา ($s=1$)",
    "formula": "$$n_s = \\frac{120 f}{P}$$\n$$s = \\frac{n_s - n_r}{n_s}$$\n$$f_r = s f$$",
    "solution": "1. Synchronous Speed:\n$$n_s = \\frac{120 \\times 50}{4} = 1,500\\text{ rpm}$$\n\n2. Slip ($s$):\n$$s = \\frac{1,500 - 1,440}{1,500} = \\frac{60}{1,500} = 0.04 = 4.0\\%$$\n\n3. Rotor Current Frequency ($f_r$):\n$$f_r = s \\times f = 0.04 \\times 50\\text{ Hz} = 2.0\\text{ Hz}$$\n\n4. At Locked-Rotor:\n$n_r = 0$, slip $s = 1.0$, and rotor frequency equals line frequency ($f_r = 50\\text{ Hz}$).",
    "solution_th": "1. ความเร็วซิงโครนัส (Synchronous Speed):\n$$n_s = \\frac{120 \\times 50}{4} = 1,500\\text{ rpm}$$\n\n2. ค่าสลิป (Slip $s$):\n$$s = \\frac{1,500 - 1,440}{1,500} = 0.04 = 4.0\\%$$\n\n3. ความถี่กระแสในขดลวดโรเตอร์ ($f_r$):\n$$f_r = s \\times f = 0.04 \\times 50\\text{ Hz} = 2.0\\text{ Hz}$$\n\n4. ขณะโรเตอร์ถูกล็อก (Locked-Rotor):\nความเร็วเพลา $n_r = 0$, ค่าสลิป $s = 1.0$ และความถี่โรเตอร์จะเท่ากับความถี่แหล่งจ่าย ($50\\text{ Hz}$)",
    "pitfall": "Rotor electrical frequency is $s f$, NOT $f$! At normal running speed, slip is small ($2-5\\%$), so rotor frequency is tiny ($1-2.5\\text{ Hz}$).",
    "pitfall_th": "ข้อควรระวัง: ความถี่ไฟฟ้าในโรเตอร์คือ $f_r = s f$ ไม่ใช่ $50\\text{ Hz}$! ในสภาวะทำงานปกติ สลิปมีค่าเพียง $2-5\\%$ ความถี่ในโรเตอร์จึงต่ำมากเพียง $1-2.5\\text{ Hz}$",
    "diagram": None,
    "mastered": False
})

cards.append({
    "id": "CH07-11",
    "chapter": "Chapter 7",
    "topic": "Induction Motor Power Flow: Air-Gap, Copper Loss & Mech Power",
    "topic_th": "แผนผังการไหลของกำลังงานใน Induction Motor ($P_{\\text{ag}} : P_{\\text{rcu}} : P_{\\text{conv}}$)",
    "level": "Level 1 (Concept)",
    "exam_reference": "Lecture Slides & Final Exam",
    "question": "State the universal proportional power relationship between Air-gap Power ($P_{\\text{ag}}$), Rotor Copper Loss ($P_{\\text{rcu}}$), and Converted Mechanical Power ($P_{\\text{conv}}$) in an induction motor.",
    "question_th": "จงระบุอัตราส่วนความสัมพันธ์กำลังงานสากลระหว่าง กำลังงานส่งผ่านช่องว่างอากาศ ($P_{\\text{ag}}$), การสูญเสียในทองแดงโรเตอร์ ($P_{\\text{rcu}}$) และกำลังกลที่เปลี่ยนรูปได้ ($P_{\\text{conv}}$) ในมอเตอร์เหนี่ยวนำ",
    "formula": "$$P_{\\text{ag}} : P_{\\text{rcu}} : P_{\\text{conv}} = 1 : s : (1-s)$$\n$$P_{\\text{rcu}} = s P_{\\text{ag}}$$\n$$P_{\\text{conv}} = (1-s)P_{\\text{ag}}$$",
    "solution": "1. Total air-gap power crosses the stator-rotor gap: $P_{\\text{ag}}$.\n2. Fraction $s$ is dissipated as rotor $I^2 R$ heat: $P_{\\text{rcu}} = s P_{\\text{ag}}$.\n3. Fraction $(1-s)$ is converted into mechanical power: $P_{\\text{conv}} = (1-s)P_{\\text{ag}}$.\n4. Internal developed torque is: $\\tau_d = \\frac{P_{\\text{ag}}}{\\omega_s} = \\frac{P_{\\text{conv}}}{\\omega_m}$.",
    "solution_th": "1. กำลังไฟฟ้าที่ส่งผ่านช่องว่างอากาศเข้าสู่โรเตอร์คือ $P_{\\text{ag}}$\n2. ส่วนที่สูญเสียเป็นความร้อนในตัวนำโรเตอร์คิดเป็นสัดส่วน $s$: $P_{\\text{rcu}} = s P_{\\text{ag}}$\n3. ส่วนที่เหลือเปลี่ยนเป็นกำลังกลขับเพลาคิดเป็นสัดส่วน $(1-s)$: $P_{\\text{conv}} = (1-s) P_{\\text{ag}}$\n4. ทอร์กขับเคลื่อนภายในคำนวณได้จาก: $\\tau_d = \\frac{P_{\\text{ag}}}{\\omega_s} = \\frac{P_{\\text{conv}}}{\\omega_m}$",
    "pitfall": "Rotor copper loss is DIRECTLY proportional to slip! High slip means high rotor heating and very poor electrical efficiency.",
    "pitfall_th": "ข้อควรระวัง: การสูญเสียในทองแดงโรเตอร์แปรผันตรงกับสลิป ($s$) เสมอ! สลิปยิ่งสูง มอเตอร์ยิ่งร้อนจัดและประสิทธิภาพยิ่งต่ำลง",
    "diagram": None,
    "mastered": False
})

cards.append({
    "id": "CH07-12",
    "chapter": "Chapter 7",
    "topic": "Synchronous Motor Operation, V-Curve & Power Factor Correction",
    "topic_th": "หลักการทำงานของ Synchronous Motor, เส้นโค้ง V-Curve และการปรับปรุง PF",
    "level": "Level 1 (Concept)",
    "exam_reference": "Lecture Slides & Final Exam",
    "question": "Why does a Synchronous Motor rotate at exactly synchronous speed with zero slip ($s=0$)? How does varying its DC field excitation current ($I_f$) allow it to act as a Synchronous Condenser to correct facility power factor?",
    "question_th": "เหตุใด Synchronous Motor จึงหมุนที่ความเร็วซิงโครนัสพอดีโดยไม่มีสลิป ($s=0$)? และการปรับกระแสกระตุ้นสนามแม่เหล็ก ($I_f$) ทำให้มอเตอร์ทำหน้าที่เป็น Synchronous Condenser ปรับปรุง Power Factor ได้อย่างไร?",
    "formula": "$$n_r = n_s = \\frac{120f}{P}$$\nNormal excitation: $PF = 1.0$\nOver-excitation: Leading $PF$ (supplies Q)\nUnder-excitation: Lagging $PF$ (draws Q)",
    "solution": "1. Constant Synchronous Speed:\nThe rotor's DC-excited poles lock magnetically into synchronism with the stator's rotating magnetic field. As long as load does not exceed pull-out torque, it runs at precisely $n_s$.\n\n2. V-Curve & Power Factor Control:\n- Under-excited ($I_f$ small): Motor draws lagging reactive power ($Q > 0$).\n- Normal excitation: Motor operates at unity power factor ($PF = 1.0$), minimum stator current.\n- Over-excited ($I_f$ large): Motor draws leading reactive power (acts as a capacitor, supplying VARs to the grid to correct factory power factor).",
    "solution_th": "1. หมุนที่ความเร็วคงที่เสมอ:\nขั้วแม่เหล็กที่ Rotor ถูกกระตุ้นด้วยไฟกระแสตรง (DC) จะถูกดูดยึดเชิงแม่เหล็ก (Magnetic Lock) ไปกับสนามแม่เหล็กหมุนของ Stator ทำให้หมุนที่ความเร็ว $n_s$ คงที่ตลอดเวลา\n\n2. การควบคุม Power Factor ด้วยกราฟ V-Curve:\n- กระตุ้นต่ำ (Under-excited): มอเตอร์กินกระแสล้าหลัง (Lagging PF กิน Q)\n- กระตุ้นพอดี (Normal excitation): ทำงานที่ $PF = 1.0$ กระแส Stator ต่ำสุด\n- กระตุ้นเกิน (Over-excited): มอเตอร์กินกระแสนำหน้า (Leading PF จ่าย Q เสมือน Capacitor) นิยมใช้ในโรงงานขนาดใหญ่เพื่อปรับปรุงค่า Power Factor ของระบบ",
    "pitfall": "Synchronous motors are NOT inherently self-starting from a dead stop because the stator RMF moves past stationary rotor poles too fast for inertia to catch up. They require damper (amortisseur) windings to start as an induction motor first.",
    "pitfall_th": "ข้อควรระวัง: มอเตอร์ซิงโครนัส 'ไม่สามารถสตาร์ทตัวเองได้โดยตรง' เพราะสนามแม่เหล็กหมุนผ่านไปเร็วเกินกว่าความเฉื่อยของเพลา จึงต้องมีขดลวดแดมเปอร์ (Damper Winding) สตาร์ทแบบ Induction ก่อน",
    "diagram": None,
    "mastered": False
})

cards.append({
    "id": "CH07-13",
    "chapter": "Chapter 7",
    "topic": "DC Motor Starting Current & Starting Resistor Design",
    "topic_th": "กระแสขณะสตาร์ทของ DC Motor และการต่อตัวต้านทานสตาร์ท (Starting Resistor)",
    "level": "Level 1 (Concept)",
    "exam_reference": "Lecture Slides & Final Review",
    "question": "Why is the starting current of a DC motor dangerously high (10 to 20 times rated current) if started directly on full voltage? How does an external starting resistor protect the motor?",
    "question_th": "เหตุใดกระแสขณะสตาร์ท (Starting Current) ของ DC Motor จึงสูงมากผิดปกติ (สูงกว่าพิกัด 10-20 เท่า) หากต่อตรงเข้ากับไฟเต็มพิกัด? และตัวต้านทานสตาร์ทช่วยปกป้องมอเตอร์ได้อย่างไร?",
    "formula": "At start ($n=0$): $E_a = 0$\n$$I_{\\text{start}} = \\frac{V_t}{R_a}$$\nWith starter: $$I_{\\text{start}} = \\frac{V_t}{R_a + R_{\\text{start}}}$$",
    "solution": "1. Why Starting Current is Enormous:\nAt standstill ($n = 0$), back EMF $E_a = k_a \\phi \\omega_m = 0\\text{ V}$. Because armature resistance $R_a$ is designed to be tiny ($< 0.5\\ \\Omega$) for high efficiency:\n$$I_{\\text{start}} = \\frac{V_t - 0}{R_a} = \\frac{220\\text{ V}}{0.5\\ \\Omega} = 440\\text{ A}!$$\nThis burns the armature coils and melts commutator brushes.\n\n2. Protection via Starting Resistor:\nA multi-step starting resistance $R_{\\text{start}}$ is placed in series with the armature to limit starting current to $1.5 - 2.0 \\times I_{\\text{rated}}$. As the motor accelerates and builds up $E_a$, resistance steps are cut out.",
    "solution_th": "1. สาเหตุที่กระแสสตาร์ทสูงมหาศาล:\nขณะหยุดนิ่ง ($n = 0$) ค่า Back EMF $E_a = 0\\text{ V}$ และเนื่องจากความต้านทาน $R_a$ ถูกออกแบบให้ต่ำมาก ($< 0.5\\ \\Omega$) เพื่อประสิทธิภาพ:\n$$I_{\\text{start}} = \\frac{220\\text{ V}}{0.5\\ \\Omega} = 440\\text{ A}!$$\nกระแสจะสูงเกินพิกัดจนทำให้อาร์เมเจอร์ไหม้และหน้าสัมผัสแปรงถ่านละลาย\n\n2. การป้องกันด้วย Starting Resistor:\nต่อตัวต้านทานภายนอก $R_{\\text{start}}$ อนุกรมกับอาร์เมเจอร์เพื่อจำกัดกระแสสตาร์ทให้อยู่ที่ $1.5 - 2.0$ เท่าของพิกัด เมื่อมอเตอร์หมุนเร็วขึ้นจนสร้าง $E_a$ ได้แล้ว จึงค่อยๆ ปลดตัวต้านทานออกทีละสเต็ป",
    "pitfall": "Never start a DC motor under full voltage without starting resistance (except tiny sub-fractional HP motors).",
    "pitfall_th": "ข้อควรระวัง: ห้ามสตาร์ทมอเตอร์ DC ขนาดกลางและใหญ่ด้วยแรงดันเต็มพิกัดโดยไม่มีชุดสตาร์ทเตอร์เด็ดขาด เพราะเบรกเกอร์จะทริปหรือขดลวดไหม้ทันที",
    "diagram": None,
    "mastered": False
})

cards.append({
    "id": "CH07-14",
    "chapter": "Chapter 7",
    "topic": "Danger of Open Field Circuit in DC Shunt Motor",
    "topic_th": "อันตรายจากการขาดของวงจรฟิลด์ใน DC Shunt Motor (Runaway Condition)",
    "level": "Level 1 (Concept)",
    "exam_reference": "Lecture Slides & Exam Pitfalls",
    "question": "What happens if the shunt field circuit of a running DC shunt motor accidentally breaks or becomes open-circuited ($I_f = 0$)? Explain the physical mechanism.",
    "question_th": "จะเกิดอะไรขึ้นหากขดลวดสนามแม่เหล็ก (Shunt Field) ของ DC Shunt Motor ขาดจากวงจร ($I_f = 0$) ขณะที่มอเตอร์กำลังทำงานอยู่? จงอธิบายกลไกทางกายภาพ",
    "formula": "$$n = \\frac{V_t - I_a R_a}{k_a \\phi}$$\nAs $\\phi \\to \\phi_{\\text{residual}} \\approx 0 \\Rightarrow n \\to \\infty$",
    "solution": "1. Field current drops to zero ($I_f = 0$), so magnetic flux drops to residual magnetism ($\\phi \\to \\phi_{\\text{residual}} \\approx 0$).\n2. Back EMF collapses: $E_a \\approx 0$, causing armature current $I_a = \\frac{V_t - E_a}{R_a}$ to soar to destructive levels.\n3. Because $n \\propto \\frac{1}{\\phi}$, the motor accelerates uncontrollably to catastrophic runaway speed ($n \\to \\infty$), resulting in mechanical disintegration (throwing armature windings and bearings exploding).",
    "solution_th": "1. เมื่อวงจรฟิลด์ขาด กระแสฟิลด์จะเป็นศูนย์ ($I_f = 0$) ฟลักซ์แม่เหล็กจะลดฮวบเหลือเพียงฟลักซ์ตกค้างเล็กน้อย ($\\phi \\to 0$)\n2. ค่า Back EMF พังทลาย ($E_a \\approx 0$) ทำให้กระแสอาร์เมเจอร์พุ่งสูงขึ้นอย่างมหาศาล\n3. จากสมการความเร็ว $n \\propto \\frac{1}{\\phi}$ มอเตอร์จะเร่งความเร็วรอบสูงขึ้นเรื่อยๆ จนควบคุมไม่ได้ (เรียกว่า Runaway) จนขดลวดอาร์เมเจอร์หลุดกระจายและเพลาพังทลายจากแรงเหวี่ยงหนีศูนย์กลาง",
    "pitfall": "Never install a fuse or switch in the field winding of a DC shunt motor! An open field causes motor destruction.",
    "pitfall_th": "ข้อควรระวัง: ห้ามติดฟิวส์หรือสวิตช์ตัดตอนในวงจรขดลวดฟิลด์ของ DC Shunt Motor เป็นอันขาด เพราะหากฟิวส์ขาด มอเตอร์จะหมุนด้วยความเร็วรอบเกินพิกัดจนระเบิด",
    "diagram": None,
    "mastered": False
})

cards.append({
    "id": "CH07-15",
    "chapter": "Chapter 7",
    "topic": "DC Series Motor Prohibition Against No-Load Operation",
    "topic_th": "ข้อห้ามการเดินเครื่อง DC Series Motor โดยไม่มีโหลด (No-Load Warning)",
    "level": "Level 1 (Concept)",
    "exam_reference": "Lecture Slides & Safety Rules",
    "question": "Why is it strictly forbidden to run a DC Series Motor without a mechanical load (or with a belt drive that could snap)?",
    "question_th": "เหตุใดจึงมีข้อห้ามเด็ดขาดไม่ให้เดินเครื่อง DC Series Motor ขณะไม่มีโหลด (No-Load) หรือห้ามใช้สายพานขับเคลื่อน?",
    "formula": "Series motor: $\\phi \\propto I_a$\n$$n \\propto \\frac{V_t - I_a(R_a + R_f)}{k_a \\phi} \\approx \\frac{V_t}{k' I_a}$$\nAs $I_a \\to 0 \\Rightarrow n \\to \\infty$",
    "solution": "1. In a series motor, field current equals armature current ($I_f = I_a$).\n2. At no load, torque required is near zero, so armature current drops close to zero ($I_a \\to 0$).\n3. This causes magnetic flux to drop to residual levels ($\\phi \\to 0$).\n4. Speed $n \\propto \\frac{1}{\\phi} \\propto \\frac{1}{I_a}$ races towards dangerous infinity ($n \\to \\infty$), destroying the machine by centrifugal force.",
    "solution_th": "1. ในดีซีซีรีส์มอเตอร์ ขดลวดฟิลด์ต่ออนุกรมกับอาร์เมเจอร์ ($I_f = I_a$)\n2. ขณะไม่มีโหลด มอเตอร์ไม่ต้องการทอร์ก กระแส $I_a$ จึงลดลงเกือบเป็นศูนย์\n3. ส่งผลให้ฟลักซ์แม่เหล็ก $\\phi$ ลดลงเกือบเป็นศูนย์ตามไปด้วย\n4. ความเร็วรอบ $n \\propto \\frac{1}{\\phi}$ จะพุ่งสูงขึ้นอย่างรวดเร็วอย่างไร้ขีดจำกัดจนทำลายตัวเอง จึงต้องต่อเพลาเข้ากับโหลดโดยตรง (Direct Gear Coupling) เสมอ",
    "pitfall": "Series motors MUST ALWAYS be solidly coupled (gears/direct shaft) to their load, NEVER belt-driven!",
    "pitfall_th": "ข้อควรระวัง: มอเตอร์ซีรีส์ต้องต่อตรงผ่านเพลาหรือเฟืองเกียร์เท่านั้น ห้ามใช้สายพานขับเด็ดขาด เพราะหากสายพานหลุดหรือขาด มอเตอร์จะเร่งรอบจนระเบิด",
    "diagram": None,
    "mastered": False
})

print(f"Loaded {len(cards)} cards up to Ch.7")
