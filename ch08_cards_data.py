# -*- coding: utf-8 -*-
"""
ch08_cards_data.py
15 Comprehensive Bilingual Master Flashcards for:
CHAPTER 8: POWER DISTRIBUTION SYSTEM (ระบบการจ่ายไฟฟ้ากำลัง)
Based on:
- Ch08PowerDistSystem.pdf (Assoc. Prof. Nararat Ruangchaijatupon, KKU)
- Past Final Exam Questions (Problems 5.1 to 5.6)
"""

ch08_cards = [
    # -------------------------------------------------------------------------
    # CH08-01
    # -------------------------------------------------------------------------
    {
        "id": "CH08-01",
        "chapter": "Chapter 8",
        "topic": "Structure of Electrical Power Systems: 4 Stages & EGAT Voltage Levels",
        "topic_th": "โครงสร้างระบบไฟฟ้ากำลัง 4 ขั้นตอน และระดับแรงดันสายส่ง กฟผ.",
        "level": "Level 1 (Concept)",
        "exam_reference": "Ch08 Slide 2, 7, 8 & Final Exam ข้อ 5.3 (หน้า 25)",
        "question": "State the 4 main stages of an electrical power system from generation to consumers. Explain why generators generate power at 10-20 kV, why voltage must be stepped up for transmission, and list EGAT's 4 standard transmission voltage levels.",
        "question_th": "จงระบุ 4 ขั้นตอนหลักของระบบไฟฟ้ากำลัง (Power System Stages) ตั้งแต่การผลิตจนถึงผู้ใช้ไฟฟ้า พร้อมอธิบายว่าเหตุใดเครื่องกำเนิดไฟฟ้าจึงผลิตแรงดันที่ระดับ 10-20 kV และทำไมต้องแปลงเป็นแรงดันสูงในสายส่ง และระบุระดับแรงดันสายส่งหลัก 4 ระดับของ กฟผ.",
        "formula": "$$\\text{Stages: Generation (10-20 kV)} \\longrightarrow \\text{Transmission (69-500 kV)} \\longrightarrow \\text{Distribution (12-33 kV)} \\longrightarrow \\text{Utilization (230/400 V)}$$\n\n$$\\text{EGAT Transmission Levels: } 500\\text{ kV (EHV)}, \\quad 230\\text{ kV (HV)}, \\quad 115\\text{ kV (HV)}, \\quad 69\\text{ kV (MV/HV)}$$",
        "solution": "1. Four Main Stages of Electrical Power System:\n- Generation System (ระบบการผลิต): Generates electricity at 10-20 kV. Limited to this range because of generator winding insulation limitations.\n- Transmission System (ระบบสายส่ง): Steps up voltage to Extra High Voltage (EHV) and High Voltage (HV) using step-up transformers to minimize line current, $I^2 R$ transmission losses, and voltage drop over long distances.\n- Distribution System (ระบบจำหน่าย): Substations step down high voltage to Medium Voltage (MV) (24/12 kV for MEA, 22/33 kV for PEA) for urban and regional distribution.\n- Utilization System (ระบบการใช้ไฟฟ้า): Distribution transformers step down MV to Low Voltage (LV) (3-phase 400/230 V, 1-phase 230 V) for consumers.\n\n2. EGAT's 4 High-Voltage Overhead Transmission Levels:\n- 500 kV, 3-phase 3-wire, 50 Hz (Extra High Voltage: EHV)\n- 230 kV, 3-phase 3-wire, 50 Hz (High Voltage: HV)\n- 115 kV, 3-phase 3-wire, 50 Hz (High Voltage: HV)\n- 69 kV, 3-phase 3-wire, 50 Hz (Medium Voltage / High Voltage)",
        "solution_th": "1. 4 ขั้นตอนหลักของระบบไฟฟ้ากำลัง:\n- 1. ระบบผลิต (Generation System): ผลิตไฟฟ้าที่แรงดัน $10-20\\text{ kV}$ สาเหตุที่ไม่ผลิตสูงกว่านี้เนื่องจาก 'ข้อจำกัดด้านฉนวนไฟฟ้า (Insulation Limitation)' ของขดลวดในเครื่องกำเนิด\n- 2. ระบบส่งไฟฟ้า (Transmission System): แปลงแรงดันขึ้นเป็นแรงดันสูงมาก (HV/EHV) เพื่อส่งข้ามระยะทางไกล ลดกระแส ลดการสูญเสีย $I^2 R$ และลดแรงดันตก\n- 3. ระบบจำหน่าย (Distribution System): สถานีไฟฟ้าย่อย (Substation) ลดแรงดันลงมาเป็นแรงดันปานกลาง (Medium Voltage: MV) ได้แก่ $24/12\\text{ kV}$ (กฟน.) หรือ $22/33\\text{ kV}$ (กฟภ.)\n- 4. ระบบการใช้ไฟฟ้า (Utilization System): หม้อแปลงจำหน่ายลดแรงดันลงเป็นแรงดันต่ำ (Low Voltage: LV) จ่ายแก่ผู้ใช้ไฟฟ้า ($400/230\\text{ V}$ 3 เฟส 4 สาย หรือ $230\\text{ V}$ 1 เฟส 2 สาย)\n\n2. 4 ระดับแรงดันสายส่งหลักของ กฟผ. (EGAT Overhead Lines):\n- $500\\text{ kV}$ 3 เฟส 3 สาย 50 Hz (แรงดันสูงพิเศษ: Extra High Voltage - EHV)\n- $230\\text{ kV}$ 3 เฟส 3 สาย 50 Hz (แรงดันสูง: High Voltage - HV)\n- $115\\text{ kV}$ 3 เฟส 3 สาย 50 Hz (แรงดันสูง: High Voltage - HV)\n- $69\\text{ kV}$ 3 เฟส 3 สาย 50 Hz (แรงดันปานกลาง/สูง: Medium/High Voltage)",
        "pitfall": "Generation voltage is strictly 10-20 kV due to generator insulation. Transmission step-up is mandatory before sending power over long distances to keep $I^2 R$ losses low.",
        "pitfall_th": "จุดสำคัญข้อสอบ: โรงไฟฟ้าผลิตที่ 10-20 kV เท่านั้นเพราะติดข้อจำกัดฉนวนของเครื่องปั่นไฟ การส่งระยะไกลจึงต้องผ่านหม้อแปลง Step-up เพิ่มแรงดันก่อนเสมอ",
        "diagram": "images/ch08_slide_7.png",
        "diagram_caption": "Slide 7: EGAT 4 High-Voltage Transmission Levels & Power Systems Structure",
        "diagram_caption_th": "สไลด์ที่ 7: โครงสร้าง 4 ขั้นตอนของระบบไฟฟ้า และระดับแรงดันสายส่ง 4 ระดับของ กฟผ.",
        "mastered": False
    },

    # -------------------------------------------------------------------------
    # CH08-02
    # -------------------------------------------------------------------------
    {
        "id": "CH08-02",
        "chapter": "Chapter 8",
        "topic": "Power Transmission Loss Formula & High-Voltage Economics",
        "topic_th": "สมการการสูญเสียในสายส่งและหลักการทางเศรษฐศาสตร์ของแรงดันสูง",
        "level": "Level 2 (Analysis)",
        "exam_reference": "Ch08 Slide 8, 38 & Final Exam Cheatsheet",
        "question": "Derive the mathematical relationship between transmission line voltage $V_L$, line current $I_L$, and $I^2 R$ power losses for transmitting real power $P$. Explain quantitatively why stepping up voltage by 10 times dramatically reduces conductor losses and cross-sectional material costs.",
        "question_th": "จงพิสูจน์ความสัมพันธ์ทางคณิตศาสตร์ระหว่างแรงดันสายส่ง $V_L$, กระแสในสาย $I_L$ และการสูญเสียกำลังไฟฟ้า ($I^2 R$) ในการส่งกำลังไฟฟ้า $P$ พร้อมอธิบายเชิงปริมาณว่าหากเพิ่มแรงดันขึ้น 10 เท่า จะช่วยลดกำลังสูญเสียและลดขนาดสายตัวนำได้อย่างไร",
        "formula": "$$I_L = \\frac{P}{\\sqrt{3}\\, V_L \\cos\\theta}$$\n\n$$P_{\\text{loss}} = 3 I_L^2 R_{\\text{line}} = 3 \\left(\\frac{P}{\\sqrt{3}\\, V_L \\cos\\theta}\\right)^2 R_{\\text{line}} = \\frac{P^2 R_{\\text{line}}}{V_L^2 \\cos^2\\theta}$$\n\n$$P_{\\text{loss}} \\propto \\frac{1}{V_L^2}, \\qquad \\Delta V = \\sqrt{3}\\, I_L (R\\cos\\theta + X\\sin\\theta) \\propto \\frac{1}{V_L}$$",
        "solution": "1. Derivation of Line Current:\nFor a balanced 3-phase line transmitting active power $P$ at power factor $\\cos\\theta$:\n$$P = \\sqrt{3}\\, V_L I_L \\cos\\theta \\implies I_L = \\frac{P}{\\sqrt{3}\\, V_L \\cos\\theta}$$\n\n2. Line Losses ($P_{\\text{loss}}$):\nTotal Joule heating loss across all 3 phases:\n$$P_{\\text{loss}} = 3 I_L^2 R_{\\text{line}} = \\frac{P^2 R_{\\text{line}}}{V_L^2 \\cos^2\\theta}$$\n\n3. Quantitative Impact of 10x Voltage Step-Up:\n- Line current $I_L$ decreases to $\\frac{1}{10}$ (10 times smaller).\n- Line power loss $P_{\\text{loss}}$ decreases by $10^2 = 100$ times (99% reduction in loss!).\n- Conductor cross-sectional area $A$ required to carry $I_L$ decreases proportionally, drastically cutting copper/aluminum conductor mass and tower structural weight.",
        "solution_th": "1. การพิสูจน์ความสัมพันธ์ของกระแส:\nจากสูตรกำลังไฟฟ้า 3 เฟส: $P = \\sqrt{3}\\, V_L I_L \\cos\\theta$\nจะได้กระแสไลน์: $I_L = \\frac{P}{\\sqrt{3}\\, V_L \\cos\\theta}$\n\n2. กำลังสูญเสียในสายส่ง ($P_{\\text{loss}}$):\n$$P_{\\text{loss}} = 3 I_L^2 R_{\\text{line}} = \\frac{P^2 R_{\\text{line}}}{V_L^2 \\cos^2\\theta}$$\nเห็นได้ชัดว่า กำลังสูญเสียแปรผกผันกับกำลังสองของแรงดัน ($P_{\\text{loss}} \\propto \\frac{1}{V_L^2}$)\n\n3. ผลเชิงปริมาณเมื่อเพิ่มแรงดันขึ้น 10 เท่า (เช่น จาก 22 kV เป็น 220 kV):\n- กระแสในสาย $I_L$ ลดลงเหลือ $\\frac{1}{10}$ (ลดลง 10 เท่า)\n- กำลังสูญเสียในสาย ($I^2 R$) ลดลงถึง $10^2 = 100$ เท่า (สูญเสียน้อยลง 99%!)\n- ขนาดพื้นที่หน้าตัดของสายตัวนำ ($A$) ลดลงได้มาก ส่งผลให้น้ำหนักสายเบาลง เสาสายส่งไม่ต้องรับน้ำหนักมาก ประหยัดงบประมาณมหาศาล",
        "pitfall": "Transmission losses depend inversely on the SQUARE of line voltage ($1/V_L^2$), while voltage drop $\\Delta V$ is inversely proportional to $V_L$.",
        "pitfall_th": "จุดควรจำ: กำลังสูญเสีย $P_{\\text{loss}}$ ลดลงตามกำลังสองของแรงดัน ($1/V_L^2$) ไม่ใช่แค่ลดลงแปรผันตรงธรรมดา",
        "diagram": None,
        "mastered": False
    },

    # -------------------------------------------------------------------------
    # CH08-03
    # -------------------------------------------------------------------------
    {
        "id": "CH08-03",
        "chapter": "Chapter 8",
        "topic": "Thailand Three Electricity Authorities & National Consumption Share",
        "topic_th": "3 การไฟฟ้าหลักของไทย (กฟผ. กฟน. กฟภ.) และสัดส่วนการใช้พลังงานไฟฟ้า",
        "level": "Level 1 (Concept)",
        "exam_reference": "Ch08 Slide 5, 6, 10, 11 & Final Exam ข้อ 5.1",
        "question": "Name the 3 state electricity authorities of Thailand, specify their jurisdictional boundaries and core roles, and present Thailand's national electricity consumption share and primary generation fuel mix.",
        "question_th": "จงระบุ 3 องค์กรการไฟฟ้าหลักของไทย อธิบายขอบเขตความรับผิดชอบและบทบาทของแต่ละองค์กร พร้อมทั้งระบุสัดส่วนการใช้ไฟฟ้าของประเทศและสัดส่วนเชื้อเพลิงหลักในการผลิตไฟฟ้า",
        "formula": "$$\\text{Consumption Share: PEA (กฟภ.) } 72\\%, \\quad \\text{MEA (กฟน.) } 27\\%, \\quad \\text{EGAT Direct Customers } 1\\%$$\n\n$$\\text{Fuel Mix: Natural Gas } 57\\%, \\quad \\text{Coal/Lignite } 18\\%, \\quad \\text{Import } 12\\%, \\quad \\text{Renewable } 9\\%, \\quad \\text{Hydro } 4\\%$$",
        "solution": "1. Three State Electricity Authorities:\n- EGAT (Electricity Generating Authority of Thailand / กฟผ.): Responsible for national bulk power generation and nationwide high-voltage transmission grid (500, 230, 115, 69 kV). Sells wholesale electricity to MEA and PEA; manages international power import/export with Laos, Malaysia, etc.\n- MEA (Metropolitan Electricity Authority / กฟน.): Distributes electricity strictly within 3 metropolitan provinces: Bangkok, Nonthaburi, and Samut Prakan.\n- PEA (Provincial Electricity Authority / กฟภ.): Distributes electricity to all remaining 74 provinces across Thailand.\n\n2. Electricity Consumption Share (2561 Data):\n- PEA: 72% (77,953 GWh)\n- MEA: 27% (29,935 GWh)\n- Direct EGAT Industrial Customers: 1% (874 GWh)\n\n3. Primary Fuel Mix for Power Generation in Thailand:\n- Natural Gas: 57% (Primary fuel)\n- Imported Coal & Lignite: 18%\n- Imported Electricity (e.g. hydro from Laos): 12%\n- Renewable Energy (Solar, Wind, Biomass): 9%\n- Domestic Hydro: 4%\n- Petroleum Oil: 0.1%",
        "solution_th": "1. 3 องค์กรการไฟฟ้าหลักของไทย:\n- กฟผ. (EGAT - การไฟฟ้าฝ่ายผลิตแห่งประเทศไทย): ผลิตไฟฟ้าและส่งจ่ายผ่านโครงข่ายสายส่งแรงดันสูงทั่วประเทศ ขายส่งให้ กฟน. และ กฟภ. และแลกเปลี่ยนซื้อขายไฟฟ้ากับประเทศเพื่อนบ้าน (ลาว, มาเลเซีย)\n- กฟน. (MEA - การไฟฟ้านครหลวง): รับผิดชอบจำหน่ายไฟฟ้าเฉพาะ 3 จังหวัด: กรุงเทพมหานคร, นนทบุรี และ สมุทรปราการ\n- กฟภ. (PEA - การไฟฟ้าส่วนภูมิภาค): รับผิดชอบจำหน่ายไฟฟ้าครอบคลุม 74 จังหวัดที่เหลือทั่วประเทศไทย\n\n2. สัดส่วนการใช้ไฟฟ้าของไทย (ข้อมูลปี 2561):\n- กฟภ. (PEA): 72% (77,953 GWh)\n- กฟน. (MEA): 27% (29,935 GWh)\n- ลูกค้าตรงของ กฟผ.: 1% (874 GWh)\n\n3. สัดส่วนเชื้อเพลิงหลักในการผลิตไฟฟ้าของไทย:\n- ก๊าซธรรมชาติ (Natural Gas): 57% (เชื้อเพลิงหลักอันดับ 1)\n- ถ่านหินนำเข้าและลิกไนต์ (Coal/Lignite): 18%\n- ไฟฟ้ารับซื้อจากต่างประเทศ (Import): 12%\n- พลังงานหมุนเวียน (Renewable): 9%\n- พลังน้ำในประเทศ (Hydro): 4%\n- น้ำมัน (Petroleum): 0.1%",
        "pitfall": "MEA covers ONLY 3 provinces (Bangkok, Nonthaburi, Samut Prakan). All other 74 provinces belong to PEA. Natural Gas is Thailand's primary fuel (57%).",
        "pitfall_th": "ข้อควรระวัง: กฟน. รับผิดชอบเพียง 3 จังหวัดเท่านั้น ที่เหลืออีก 74 จังหวัดเป็นของ กฟภ. ทั้งหมด และก๊าซธรรมชาติคือเชื้อเพลิงหลักของไทย (57%)",
        "diagram": None,
        "mastered": False
    },

    # -------------------------------------------------------------------------
    # CH08-04
    # -------------------------------------------------------------------------
    {
        "id": "CH08-04",
        "chapter": "Chapter 8",
        "topic": "Base Load vs Peak Load Power Plants: Comparison & Startup Times",
        "topic_th": "โรงไฟฟ้าฐาน (Base Load) vs โรงไฟฟ้ารับโหลดสูงสุด (Peak Load) และเวลาเริ่มเดินเครื่อง",
        "level": "Level 2 (Analysis)",
        "exam_reference": "Ch08 Slide 13, 21, 24 & Final Exam ข้อ 5.2 (หน้า 25)",
        "question": "Compare Base Load and Peak Load power plants regarding operating objectives, fuel types, capital vs fuel costs, and startup times, citing typical Thai power plant examples.",
        "question_th": "จงเปรียบเทียบโรงไฟฟ้าฐาน (Base Load) และโรงไฟฟ้ารับโหลดสูงสุด (Peak Load) ในประเด็น: วัตถุประสงค์การเดินเครื่อง, เชื้อเพลิง, ต้นทุนก่อสร้างเทียบต้นทุนเชื้อเพลิง, และระยะเวลาในการเริ่มเดินเครื่อง พร้อมยกตัวอย่างโรงไฟฟ้าในไทย",
        "formula": "$$\\text{Base Load: 24/7 continuous, High Capital Cost, Low Fuel Cost/kWh, Startup: 6-8 Hours (Mae Moh Lignite)}$$\n\n$$\\text{Peak Load: Fast response, Low Capital Cost, High Fuel Cost/kWh, Startup: < 5-15 Minutes (Hydro, Gas Turbine)}$$",
        "solution": "1. Base Load Power Plants (โรงไฟฟ้าฐาน):\n- Operating Objective: Run continuously 24 hours a day at constant rated output to cover minimum baseline electrical demand.\n- Economic Profile: High capital / construction cost, but low fuel cost per generated kWh.\n- Startup Time: Very slow (6 to 8 hours) due to thermal boiler expansion requirements.\n- Fuels & Examples: Lignite coal (Mae Moh Power Plant, Lampang), Nuclear, Combined-Cycle baseload.\n\n2. Peak Load Power Plants (โรงไฟฟ้ารับโหลดสูงสุด):\n- Operating Objective: Operated only during hours of peak demand (18:00 - 22:00) or emergency power deficits.\n- Economic Profile: Low capital construction cost, but high fuel / operating cost per kWh.\n- Startup Time: Extremely rapid (under 5 minutes for Hydro; ~15 minutes for Gas Turbine).\n- Fuels & Examples: Hydroelectric dam (Bhumibol, Ubolratana), Pumped-Storage Hydro (Lam Takhong), Open-Cycle Gas Turbine, Diesel.",
        "solution_th": "1. โรงไฟฟ้าฐาน (Base Load Power Plant):\n- วัตถุประสงค์: เดินเครื่องผลิตไฟฟ้าคงที่ตลอด 24 ชั่วโมง เพื่อรองรับความต้องการไฟฟ้าขั้นต่ำของประเทศ\n- ต้นทุน: ต้นทุนก่อสร้างเริ่มต้นสูงมาก (High Capital Cost) แต่ต้นทุนเชื้อเพลิงต่อหน่วยต่ำ (Low Operating/Fuel Cost)\n- เวลาเริ่มเดินเครื่อง (Startup Time): ช้ามาก (6 - 8 ชั่วโมง) เนื่องจากต้องต้มน้ำสร้างแรงดันไอน้ำในหม้อต้ม (Boiler)\n- เชื้อเพลิงและตัวอย่าง: ถ่านหินลิกไนต์ (โรงไฟฟ้าแม่เมาะ จ.ลำปาง), พลังงานนิวเคลียร์, ความร้อนร่วมฐาน\n\n2. โรงไฟฟ้ารับโหลดสูงสุด (Peak Load Power Plant):\n- วัตถุประสงค์: เดินเครื่องเฉพาะช่วงเวลาที่มีการใช้ไฟฟ้าสูงสุด (Peak Hours เช่น หัวค่ำ) หรือเมื่อเกิดเหตุฉุกเฉินในระบบ\n- ต้นทุน: ต้นทุนก่อสร้างต่ำกว่า แต่ต้นทุนเชื้อเพลิงต่อหน่วยแพงมาก (High Fuel Cost per kWh)\n- เวลาเริ่มเดินเครื่อง (Startup Time): รวดเร็วมาก (โรงไฟฟ้าพลังน้ำ < 5 นาที, กังหันก๊าซ ~15 นาที)\n- เชื้อเพลิงและตัวอย่าง: โรงไฟฟ้าพลังน้ำ (เขื่อนภูมิพล, เขื่อนอุบลรัตน์), พลังน้ำแบบสูบกลับ (ลำตะคอง), กังหันก๊าซ (น้ำพอง), โรงไฟฟ้าดีเซล",
        "pitfall": "Hydroelectric dams start in under 5 minutes and are ideal for Peak Load. Steam coal plants require 6-8 hours and can only serve as Base Load.",
        "pitfall_th": "ข้อสอบออกบ่อย: โรงไฟฟ้าพลังน้ำสตาร์ทได้เร็วสุด (< 5 นาที) เหมาะเป็น Peak Load ส่วนโรงไฟฟ้าไอน้ำถ่านหินสตาร์ทนานสุด (6-8 ชม.) เหมาะเป็น Base Load",
        "diagram": None,
        "mastered": False
    },

    # -------------------------------------------------------------------------
    # CH08-05
    # -------------------------------------------------------------------------
    {
        "id": "CH08-05",
        "chapter": "Chapter 8",
        "topic": "Five Types of EGAT Power Plants & Landmark Facilities in Thailand",
        "topic_th": "5 ประเภทโรงไฟฟ้าของ กฟผ. และโรงไฟฟ้าหลักที่เป็นจุดสังเกตในประเทศไทย",
        "level": "Level 1 (Concept)",
        "exam_reference": "Ch08 Slide 12-34 & Final Exam ข้อ 5.1",
        "question": "Name the 5 types of electrical power plants operated by EGAT, and describe the key landmark facilities in Thailand (Bhumibol Dam, Ubolratana Dam, Mae Moh, Nam Pong, and Bangpakong).",
        "question_th": "จงระบุประเภทโรงไฟฟ้าทั้ง 5 ชนิดของ กฟผ. พร้อมอธิบายข้อมูลสำคัญของโรงไฟฟ้าหลักที่เป็นจุดสังเกตในไทย (เขื่อนภูมิพล, เขื่อนอุบลรัตน์, แม่เมาะ, น้ำพอง, บางปะกง)",
        "formula": "$$\\text{1. Hydro (Bhumibol 7,312 MW, Ubolratana 2,263M m}^3\\text{, Lam Takhong Pumped Storage)}$$\n\n$$\\text{2. Steam/Thermal (Mae Moh 2,625 MW), \\quad 3. Gas/Diesel (Nam Pong 710 MW)}$$\n\n$$\\text{4. Combined Cycle (Bangpakong Pipeline 8 km), \\quad 5. Renewable (Solar, Wind, Biomass)}$$",
        "solution": "1. Five EGAT Power Plant Types:\n- 1) Hydro Power Plant (โรงไฟฟ้าพลังน้ำ): Rapid start (< 5 min), stores water in dam. Landmark dams:\n  - Bhumibol Dam (Tak): Thailand's first multi-purpose dam (formerly Yanhee Dam), only curved concrete arch dam in Thailand (radius 250 m, height 154 m, reservoir 13,462 million m$^3$, 8 generators, 7,312 MW).\n  - Ubolratana Dam (Khon Kaen): Built across Pong River, first hydroelectric dam in Northeastern Thailand (crest length 885 m, height 32 m, reservoir 2,263 million m$^3$).\n  - Lam Takhong Power Plant: Underground pumped-storage hydropower plant.\n- 2) Steam / Thermal Power Plant (โรงไฟฟ้าพลังความร้อน/ไอน้ำ): High capacity, 6-8 hr startup, base load. Landmark: Mae Moh Power Plant (Lampang) with 13 generators, 2,625 MW capacity using local lignite coal.\n- 3) Gas and Diesel Power Plant (โรงไฟฟ้ากังหันก๊าซและดีเซล): 15 min startup, peak load. Landmark: Nam Pong Power Plant (Khon Kaen, 710 MW using natural gas, 32 km from KKU downtown).\n- 4) Combined Cycle Power Plant (โรงไฟฟ้าพลังความร้อนร่วม): Combines Gas Turbine + Steam Turbine with Heat Recovery Steam Generator (HRSG). Landmark: Bangpakong Power Plant (supplied by 8 km heavy oil pipeline from Sriracha depot).\n- 5) Renewable Power Plant (โรงไฟฟ้าพลังงานหมุนเวียน): Solar, wind, biomass.",
        "solution_th": "1. 5 ประเภทโรงไฟฟ้าของ กฟผ. และโรงไฟฟ้าสำคัญในไทย:\n- 1) โรงไฟฟ้าพลังน้ำ (Hydro Power Plant): สตาร์ทเร็วมาก (< 5 นาที), จ่ายไฟช่วงพีค\n  - เขื่อนภูมิพล (จ.ตาก): เขื่อนอเนกประสงค์แห่งแรกของไทย (เดิมชื่อเขื่อนยันฮี), เป็น 'เขื่อนคอนกรีตโค้งแห่งเดียวในไทย' (รัศมี 250 ม., สูง 154 ม., ความจุ 13,462 ล้าน ลบ.ม., 8 เครื่องกำเนิด, 7,312 MW)\n  - เขื่อนอุบลรัตน์ (จ.ขอนแก่น): สร้างกั้นลำน้ำพอง, เป็น 'โรงไฟฟ้าพลังน้ำแห่งแรกในภาคอีสาน' (สันเขื่อนยาว 885 ม., สูง 32 ม., ความจุ 2,263 ล้าน ลบ.ม.)\n  - เขื่อนลำตะคองชลภาวัฒนา: โรงไฟฟ้าพลังน้ำแบบสูบกลับใต้ดิน\n- 2) โรงไฟฟ้าพลังความร้อน/ไอน้ำ (Steam/Thermal): เดินเครื่องฐาน สตาร์ท 6-8 ชม. โรงไฟฟ้าแม่เมาะ (จ.ลำปาง) 13 เครื่องกำเนิด รวม 2,625 MW ใช้ถ่านหินลิกไนต์\n- 3) โรงไฟฟ้ากังหันก๊าซและดีเซล (Gas & Diesel): สตาร์ทเร็ว 15 นาที จ่ายช่วงพีค โรงไฟฟ้าน้ำพอง (จ.ขอนแก่น, 710 MW ใช้ก๊าซธรรมชาติ ห่าง มข. 32 กม.) และโรงไฟฟ้าดีเซล 4 จังหวะ\n- 4) โรงไฟฟ้าพลังความร้อนร่วม (Combined Cycle): ใช้กังหันก๊าซทำงานร่วมกับกังหันไอน้ำ ประสิทธิภาพสูง โรงไฟฟ้าบางปะกง (รับน้ำมันเตา/ดีเซลผ่านท่อ 8 กม. จากคลังศรีราชา)\n- 5) โรงไฟฟ้าพลังงานหมุนเวียน (Renewable): แสงอาทิตย์ ลม ชีวมวล",
        "pitfall": "Bhumibol Dam is Thailand's ONLY curved concrete arch dam. Ubolratana Dam is the FIRST hydro dam in the Northeast (Isan), located right in Khon Kaen.",
        "pitfall_th": "จุดสำคัญในสไลด์: เขื่อนภูมิพลเป็นเขื่อนคอนกรีตโค้งแห่งเดียวในไทย ส่วนเขื่อนอุบลรัตน์เป็นโรงไฟฟ้าพลังน้ำแห่งแรกของภาคอีสาน ตั้งอยู่ที่ จ.ขอนแก่น",
        "diagram": None,
        "mastered": False
    },

    # -------------------------------------------------------------------------
    # CH08-06
    # -------------------------------------------------------------------------
    {
        "id": "CH08-06",
        "chapter": "Chapter 8",
        "topic": "Hydraulic Turbine Classifications: Pelton, Francis & Kaplan",
        "topic_th": "การจำแนกประเภทกังหันน้ำ: Pelton, Francis และ Kaplan ตามเฮดและอัตราการไหล",
        "level": "Level 1 (Concept)",
        "exam_reference": "Ch08 Slide 20 (Turbine Types)",
        "question": "Classify the 3 major types of hydraulic turbines (Pelton, Francis, Kaplan) by working principle, water head ($H$), flow rate ($Q$), and their engineering applications in hydroelectric dams.",
        "question_th": "จงจำแนกกังหันน้ำ 3 ชนิดหลัก (Pelton, Francis, Kaplan) ตามหลักการทำงาน, ความสูงหัวน้ำ (Head: $H$), อัตราการไหลของน้ำ (Flow: $Q$) และความเหมาะสมในการนำไปใช้งานในโรงไฟฟ้าพลังน้ำ",
        "formula": "$$\\text{Pelton (Impulse): High Head } (H > 300\\text{ m}), \\quad \\text{Low Flow Rate } (Q)$$\n\n$$\\text{Francis (Reaction): Medium Head } (30\\text{ m} \\le H \\le 300\\text{ m}), \\quad \\text{Medium Flow Rate } (Q)$$\n\n$$\\text{Kaplan (Propeller): Low Head } (H < 30\\text{ m}), \\quad \\text{High Flow Rate } (Q)$$",
        "solution": "1. Pelton Turbine (Impulse Turbine / กังหันแรงกระแทก):\n- Operating Principle: High-velocity water jets from nozzles strike cup-shaped buckets on the runner periphery in open air.\n- Operating Conditions: High Head ($H > 300\\text{ m}$) and Low Flow Rate ($Q$).\n- Typical Application: High mountainous dams with steep waterfalls.\n\n2. Francis Turbine (Reaction Turbine / กังหันแรงสะท้อน):\n- Operating Principle: Water enters the runner radially under pressure through wicket gates and discharges axially.\n- Operating Conditions: Medium Head ($30\\text{ m} \\le H \\le 300\\text{ m}$) and Medium Flow Rate ($Q$).\n- Typical Application: Most widely used turbine globally, applied in large multi-purpose dams (e.g. Bhumibol Dam, Srinagarind Dam).\n\n3. Kaplan Turbine (Propeller Reaction Turbine / กังหันแบบใบพัด):\n- Operating Principle: Axial-flow propeller runner with adjustable blades (pitch control) to maintain high efficiency over variable flow rates.\n- Operating Conditions: Low Head ($H < 30\\text{ m}$) and High Flow Rate ($Q$).\n- Typical Application: River run-of-river dams and low-head barrages (e.g. Chao Phraya Dam).",
        "solution_th": "1. กังหันเพลตัน (Pelton Turbine - กังหันแรงกระแทก Impulse):\n- หลักการ: น้ำพุ่งผ่านหัวฉีด (Nozzle) ด้วยความเร็วสูงเข้ากระแทกถ้วยรับน้ำ (Buckets) บนวงล้อ\n- สภาวะใช้งาน: ความสูงหัวน้ำสูงมาก ($H > 300\\text{ m}$) และอัตราการไหลต่ำ ($Q$ น้อย)\n- เหมาะสำหรับ: โรงไฟฟ้าบนภูเขาสูง\n\n2. กังหันฟรานซิส (Francis Turbine - กังหันแรงสะท้อน Reaction):\n- หลักการ: น้ำไหลผ่านใบนำน้ำเข้าสู่ใบพัดในแนวรัศมีและไหลออกในแนวแกนเพลาภายใต้แรงดัน\n- สภาวะใช้งาน: ความสูงหัวน้ำปานกลาง ($30 - 300\\text{ m}$) และอัตราการไหลปานกลาง\n- เหมาะสำหรับ: นิยมใช้งานมากที่สุดในโลก (เช่น เขื่อนภูมิพล เขื่อนศรีนครินทร์)\n\n3. กังหันแคปแลน (Kaplan Turbine - กังหันแบบใบพัดเรือ Reaction Propeller):\n- หลักการ: น้ำไหลผ่านใบพัดตามแนวแกน ใบพัดสามารถปรับมุมองศาได้เพื่อรักษาประสิทธิภาพเมื่อน้ำเปลี่ยนอัตราการไหล\n- สภาวะใช้งาน: ความสูงหัวน้ำต่ำ ($H < 30\\text{ m}$) แต่อัตราการไหลสูงมาก ($Q$ มหาศาล)\n- เหมาะสำหรับ: เขื่อนทดน้ำท้ายน้ำหรือเขื่อนระบายน้ำ (เช่น เขื่อนเจ้าพระยา)",
        "pitfall": "Pelton = High Head, Low Flow. Francis = Medium Head/Flow (most common). Kaplan = Low Head, High Flow (adjustable propeller).",
        "pitfall_th": "จำสูตรง่ายๆ: เพลตัน = เฮดสูงน้ำน้อย, ฟรานซิส = กลางๆ (ฮิตสุด), แคปแลน = เฮดเตี้ยแต่น้ำเยอะมาก (ใบพัดเรือ)",
        "diagram": "images/ch08_slide_20.png",
        "diagram_caption": "Slide 20: Three Hydraulic Turbine Types (Kaplan, Francis, Pelton)",
        "diagram_caption_th": "สไลด์ที่ 20: กังหันน้ำ 3 ชนิด (แคปแลน, ฟรานซิส, เพลตัน)",
        "mastered": False
    },

    # -------------------------------------------------------------------------
    # CH08-07
    # -------------------------------------------------------------------------
    {
        "id": "CH08-07",
        "chapter": "Chapter 8",
        "topic": "Solar Photovoltaic (PV) Power System Core Components",
        "topic_th": "5 องค์ประกอบหลักของระบบผลิตไฟฟ้าพลังงานแสงอาทิตย์ (Solar PV System)",
        "level": "Level 1 (Concept)",
        "exam_reference": "Ch08 Slide 33, 35, 36 (Solar PV System)",
        "question": "List the 5 primary components of a complete solar photovoltaic power plant, explain the role of each, and name notable solar demonstration plants in Thailand.",
        "question_th": "จงระบุ 5 ส่วนประกอบหลักของระบบโรงไฟฟ้าพลังงานแสงอาทิตย์ (Solar PV) พร้อมอธิบายหน้าที่ของแต่ละส่วน และยกตัวอย่างโรงไฟฟ้าแสงอาทิตย์นำร่องในประเทศไทย",
        "formula": "$$\\text{1. Solar PV Modules (DC) } \\longrightarrow \\text{2. DC/AC Inverter } \\longrightarrow \\text{AC Grid / Load (230/400 V)}$$\n\n$$\\text{Auxiliary: 3. Battery Storage (BESS), \\quad 4. Charge Controller, \\quad 5. SCADA / Data Acquisition}$$",
        "solution": "1. Five Primary Components of Solar PV System:\n- 1) Solar Cell Modules (แผงโซลาร์เซลล์): Converts incident sunlight directly into direct current (DC) electricity via the semiconductor photovoltaic effect.\n- 2) DC/AC Inverter (อินเวอร์เตอร์): Converts generated DC power into synchronized Alternating Current (AC) power at 50 Hz, 230/400 V matching grid standards.\n- 3) Battery Energy Storage (ระบบแบตเตอรี่กักเก็บพลังงาน): Stores excess generated electrical energy during daytime peak irradiance for nighttime or emergency power supply.\n- 4) Charge Controller & Protection Switchgear: Regulates battery charging/discharging voltage and current to prevent overcharging and damage.\n- 5) Control and Data Acquisition System (SCADA / ระบบตรวจวัด): Monitored parameters include solar irradiance, cell temperatures, DC/AC voltages, power output, and inverter conversion efficiency.\n\n2. Notable Solar PV Plants in Thailand (Ch08 Slide 33):\n- Klongchongklam (คลองช่องกล่ำ จ.สระแก้ว): 20 kW demonstration plant\n- Promthep Cape (แหลมพรหมเทพ จ.ภูเก็ต): 11.34 kW\n- Sankamphaeng (สันกำแพง จ.เชียงใหม่): 14 kW\n- Mae Hong Son (จ.แม่ฮ่องสอน): 500 kW",
        "solution_th": "1. 5 ส่วนประกอบหลักของโรงไฟฟ้าพลังงานแสงอาทิตย์ (Solar PV Plant):\n- 1) แผงเซลล์แสงอาทิตย์ (Solar Cell Module): เปลี่ยนพลังงานแสงอาทิตย์เป็นไฟฟ้ากระแสตรง (DC) ด้วยปรากฏการณ์โฟโตโวลตาอิก\n- 2) เครื่องแปลงกระแสไฟฟ้า (Power Inverter / DC-to-AC Converter): แปลงไฟ DC จากแผงเป็นไฟฟ้ากระแสสลับ (AC) 50 Hz แรงดัน $230/400\\text{ V}$ เพื่อส่งเข้ากริดหรือใช้งาน\n- 3) ระบบแบตเตอรี่กักเก็บพลังงาน (Battery Storage): สำรองพลังงานไฟฟ้าไว้ใช้ในช่วงเวลากลางคืนหรือช่วงที่แดดร่ม\n- 4) อุปกรณ์ควบคุมการประจุ (Charge Controller & Switchgear): ควบคุมการชาร์จแบตเตอรี่ ป้องกันการชาร์จหรือคายประจุเกินขนาด\n- 5) ระบบควบคุมและเก็บข้อมูล (Control & Data Acquisition System / SCADA): บันทึกข้อมูลรังสีแสง, อุณหภูมิแผง, แรงดัน, กระแส และประสิทธิภาพของอินเวอร์เตอร์\n\n2. ตัวอย่างโรงไฟฟ้าพลังงานแสงอาทิตย์นำร่องในไทย (สไลด์ที่ 33):\n- โครงการคลองช่องกล่ำ จ.สระแก้ว (20 kW)\n- โครงการแหลมพรหมเทพ จ.ภูเก็ต (11.34 kW)\n- โครงการสันกำแพง จ.เชียงใหม่ (14 kW)\n- โครงการโซลาร์เซลล์ จ.แม่ฮ่องสอน (500 kW)",
        "pitfall": "Inverters are DC-to-AC converters. The 5 components specified in slide 35 are: PV Module, DC/AC Inverter, Battery Storage, Charge Controller, and SCADA System.",
        "pitfall_th": "ข้อสอบสไลด์ 35 เน้น 5 องค์ประกอบ: แผงโมดูล, อินเวอร์เตอร์แปลง DC เป็น AC, แบตเตอรี่, ชุดควบคุม, และระบบบันทึกข้อมูล",
        "diagram": "images/ch08_slide_35.png",
        "diagram_caption": "Slide 35: Components of a Solar Power Plant",
        "diagram_caption_th": "สไลด์ที่ 35: องค์ประกอบ 5 ส่วนของโรงไฟฟ้าพลังงานแสงอาทิตย์",
        "mastered": False
    },

    # -------------------------------------------------------------------------
    # CH08-08
    # -------------------------------------------------------------------------
    {
        "id": "CH08-08",
        "chapter": "Chapter 8",
        "topic": "MEA Distribution System Architecture & Transformer Ratings",
        "topic_th": "โครงสร้างระบบจำหน่ายของการไฟฟ้านครหลวง (กฟน. MEA) และพิกัดหม้อแปลง",
        "level": "Level 2 (Analysis)",
        "exam_reference": "Ch08 Slide 41, 42, 43 (MEA Distribution System)",
        "question": "Detail the distribution system of the Metropolitan Electricity Authority (MEA), including service provinces, voltage levels, substation redundancy, power transformer capacities, feeder load limits, and secondary utilization voltages.",
        "question_th": "จงอธิบายโครงสร้างระบบจำหน่ายของการไฟฟ้านครหลวง (กฟน. MEA): เขตพื้นที่รับผิดชอบ, ระดับแรงดันสายส่งย่อย, การรับไฟ 2 วงจร, พิกัดหม้อแปลงสถานี, ขีดจำกัดโหลดสายป้อน และแรงดันส่งมอบระดับผู้ใช้ไฟฟ้า",
        "formula": "$$\\text{Subtransmission: } 69\\text{ or } 115\\text{ kV} \\xrightarrow{\\text{Substation}} \\text{Primary Distribution: } 24\\text{ kV (New) or } 12\\text{ kV (Legacy)}$$\n\n$$\\text{Substation Transformers: } 36/48/60\\text{ MVA (ONAN/ONAF1/ONAF2) with Tie CB}$$\n\n$$\\text{Feeder Capacity: } 15\\text{ MVA (at } 24\\text{ kV}), \\quad 8\\text{ MVA (at } 12\\text{ kV})$$\n\n$$\\text{Utilization: } 24/12\\text{ kV} \\longrightarrow 416/240\\text{ V rated} \\implies \\text{Delivered: } 380/220\\text{ V or } 400/230\\text{ V (3-phase 4-wire)}$$",
        "solution": "1. MEA Jurisdiction & Subtransmission:\n- Covers 3 provinces: Bangkok, Samut Prakan, and Nonthaburi.\n- Sub-transmission System: Receives bulk power from EGAT at 230, 115, or 69 kV.\n\n2. MEA Distribution Substations:\n- Stepping Down: Transforms 69 kV or 115 kV down to 24 kV (standard current system) or 12 kV (older legacy system).\n- Circuit Redundancy: Powered via 2 independent incoming circuits for continuous reliability.\n- Transformer Ratings: Uses 2 to 4 power transformers rated at 36/48/60 MVA (ONAN/ONAF1/ONAF2) per circuit, linked by a High-Voltage Tie Circuit Breaker (Tie CB).\n- Feeder Load Capacities: Maximum 8 MVA per feeder at 12 kV; maximum 15 MVA per feeder at 24 kV.\n\n3. MEA Utilization System (Low Voltage Delivery):\n- Distribution transformers step down 24 kV (or 12 kV) to secondary rated voltage of 416/240 V.\n- Standard voltage delivered to end consumers is 380/220 V (or 400/230 V), 3-phase 4-wire with neutral.",
        "solution_th": "1. ขอบเขตพื้นที่และระบบสายส่งย่อย กฟน.:\n- รับผิดชอบ 3 จังหวัด: กรุงเทพฯ, สมุทรปราการ และ นนทบุรี\n- ระบบสายส่งย่อย (Sub-transmission): รับไฟฟ้าจาก กฟผ. ที่ระดับแรงดัน 230, 115 หรือ 69 kV\n\n2. สถานีไฟฟ้าย่อยจำหน่ายของ กฟน. (สไลด์ที่ 41-42):\n- แปลงแรงดัน: ลดแรงดันจาก 69 หรือ 115 kV ลงเป็น 24 kV (ระบบมาตรฐานใหม่) หรือ 12 kV (ระบบเดิม)\n- ความเชื่อถือได้: รับไฟฟ้าผ่าน 2 วงจรคู่ขนาน (2 circuits) เพื่อความมั่นคงสูง\n- พิกัดหม้อแปลงสถานี: ใช้หม้อแปลงกำลัง 2-4 ลูกต่อวงจร พิกัด 36/48/60 MVA (ระบายความร้อนแบบ ONAN/ONAF1/ONAF2) มี Tie CB เชื่อมบัส\n- ขีดจำกัดโหลดสายป้อน: สูงสุด 8 MVA ที่ 12 kV และสูงสุด 15 MVA ที่ 24 kV\n\n3. ระบบการใช้ไฟฟ้าของผู้ใช้ไฟฟ้า กฟน. (สไลด์ที่ 43):\n- หม้อแปลงจำหน่ายลดแรงดันจาก 24 kV หรือ 12 kV ลงเป็นแรงดันพิกัด 416/240 V\n- จ่ายจริงให้ผู้ใช้ไฟฟ้าที่แรงดันมาตรฐาน 380/220 V (หรือ 400/230 V) แบบ 3 เฟส 4 สาย",
        "pitfall": "MEA uses 24 kV (new) and 12 kV (legacy) for medium voltage. Transformer rating is 36/48/60 MVA with Tie CB. Secondary rating is 416/240 V delivering 380/220 V.",
        "pitfall_th": "สไลด์ 41-43 เน้น: แรงดันปานกลาง กฟน. คือ 24 kV (และ 12 kV), หม้อแปลงสถานีขนาด 36/48/60 MVA และพิกัดหม้อแปลงจำหน่าย 416/240 V จ่ายจริง 380/220 V",
        "diagram": "images/ch08_slide_42.png",
        "diagram_caption": "Slide 42: Single Line Diagram of MEA Distribution System (69 kV / 24 kV)",
        "diagram_caption_th": "สไลด์ที่ 42: ไดอะแกรมเส้นเดี่ยว (Single Line Diagram) ระบบจำหน่าย กฟน. 69 kV / 24 kV",
        "mastered": False
    },

    # -------------------------------------------------------------------------
    # CH08-09
    # -------------------------------------------------------------------------
    {
        "id": "CH08-09",
        "chapter": "Chapter 8",
        "topic": "PEA Medium Voltage Distribution: 22 kV Solidly Grounded vs 33 kV Multigrounded",
        "topic_th": "ระบบจำหน่ายแรงดันปานกลาง กฟภ. (22 kV Solidly Grounded vs 33 kV Multigrounded)",
        "level": "Level 2 (Analysis)",
        "exam_reference": "Ch08 Slide 45, 46 (PEA Medium Voltage Systems)",
        "question": "Compare the two distinct Medium Voltage distribution systems used by PEA (22 kV Solidly Grounded vs 33 kV Multigrounded with Overhead Ground Wire) in terms of geographic coverage, line configuration, phase-to-ground voltage, and earthing method.",
        "question_th": "จงเปรียบเทียบระบบจำหน่ายแรงดันปานกลาง 2 ระบบของ กฟภ. (ระบบ 22 kV ต่อลงดินโดยตรง vs ระบบ 33 kV มัลติกราวด์มีสายนิวทรัลล่อฟ้า) ในด้านพื้นที่ใช้งาน, จำนวนสาย, แรงดันเทียบดิน และลักษณะการต่อลงดิน",
        "formula": "$$\\text{System 1: } 22\\text{ kV Conventional Solidly Grounded} \\implies \\text{3-Phase 3-Wire, } V_L = 22\\text{ kV (Central, North, Northeast, East)}$$\n\n$$\\text{System 2: } 33\\text{ kV Multigrounded with OHGW} \\implies \\text{3-Phase 4-Wire, } V_L = 33\\text{ kV}, \\quad V_p = \\frac{33}{\\sqrt{3}} \\approx 19\\text{ kV}$$\n\n$$\\text{(Used in South: Ranong southward, plus Chiang Rai & Phayao; grounded at every pole)}$$",
        "solution": "1. PEA 22 kV Conventional Solidly Grounded System (สไลด์ที่ 45):\n- Geographic Coverage: Standard system applied throughout Central, Northern, Northeastern (Isan), and Eastern regions of Thailand.\n- Line Configuration: 3-phase 3-wire system ($V_L = 22\\text{ kV}$) and 1-phase 2-wire branch lines.\n- Earthing Method: Solidly grounded at the substation transformer star neutral point.\n\n2. PEA 33 kV Multigrounded System with Overhead Ground Wire (สไลด์ที่ 46):\n- Geographic Coverage: Applied specifically in Southern Thailand (from Ranong province southward) and upper Northern border provinces (Chiang Rai, Phayao).\n- Line Configuration: 3-phase 4-wire system with Line-to-Line voltage $V_L = 33\\text{ kV}$ and Phase-to-Ground voltage $V_p = \\frac{33}{\\sqrt{3}} \\approx 19\\text{ kV}$.\n- Earthing & Ground Wire: The 4th overhead conductor serves as an Overhead Ground Wire (OHGW) / neutral, grounded at the substation star point and *grounded at every single utility pole*. This provides superior shielding against lightning strikes in high thunder-day coastal regions.",
        "solution_th": "1. ระบบ 22 kV ต่อลงดินโดยตรง (22 kV Conventional Solidly Grounded System - สไลด์ที่ 45):\n- พื้นที่ใช้งาน: ใช้งานทั่วไปในภาคกลาง, ภาคเหนือ, ภาคตะวันออกเฉียงเหนือ (อีสาน) และภาคตะวันออก\n- ลักษณะสาย: ระบบ 3 เฟส 3 สาย ($V_L = 22\\text{ kV}$) และ 1 เฟส 2 สาย\n- การต่อลงดิน: ต่อลงดินโดยตรงที่จุดสายนิวทรัลของหม้อแปลงสถานีไฟฟ้า\n\n2. ระบบ 33 kV มัลติกราวด์ มีสายนิวทรัลล่อฟ้า (33 kV Multigrounded System with Overhead Ground Wire - สไลด์ที่ 46):\n- พื้นที่ใช้งาน: ใช้งานเฉพาะใน 'ภาคใต้ตั้งแต่จังหวัดระนองลงไป' และใน จ.เชียงราย และ จ.พะเยา\n- ลักษณะสาย: ระบบ 3 เฟส 4 สาย แรงดันระหว่างสาย $V_L = 33\\text{ kV}$ และแรงดันเทียบดิน $V_p = \\frac{33}{\\sqrt{3}} \\approx 19\\text{ kV}$\n- การต่อลงดินและสายล่อฟ้า: สายเส้นที่ 4 (Overhead Ground Wire: OHGW) ทำหน้าที่เป็นทั้งสายนิวทรัลและสายล่อฟ้า โดย 'ต่อลงดินที่จุดสตาร์และต่อลงดินที่เสาทุกต้น' ช่วยป้องกันฟ้าผ่าได้อย่างยอดเยี่ยมในพื้นที่ภาคใต้ที่มีพายุฝนฟ้าคะนองบ่อย",
        "pitfall": "PEA uses 22 kV (3-phase 3-wire) for most of Thailand, but uses 33 kV (3-phase 4-wire with OHGW grounded at every pole) in the South (Ranong down) and Chiang Rai/Phayao.",
        "pitfall_th": "ข้อสอบจำแนกแม่นๆ: 22 kV ใช้ทั่วไป (3 เฟส 3 สาย) ส่วน 33 kV มัลติกราวด์ (3 เฟส 4 สาย มีสายดินล่อฟ้าที่เสาทุกต้น) ใช้ในภาคใต้ (ระนองลงไป) และเชียงราย/พะเยา",
        "diagram": "images/ch08_slide_45.png",
        "diagram_caption": "Slide 45 & 46: PEA 22 kV Solidly Grounded vs 33 kV Multigrounded System",
        "diagram_caption_th": "สไลด์ที่ 45 และ 46: ระบบจำหน่าย 22 kV ต่อลงดินโดยตรง เทียบกับ 33 kV มัลติกราวด์ กฟภ.",
        "mastered": False
    },

    # -------------------------------------------------------------------------
    # CH08-10
    # -------------------------------------------------------------------------
    {
        "id": "CH08-10",
        "chapter": "Chapter 8",
        "topic": "PEA Distribution Feeder Topologies: Radial vs Tie-Line Systems",
        "topic_th": "รูปแบบสายป้อนระบบจำหน่าย กฟภ. (แบบรัศมี Radial vs แบบเชื่อมโยง Tie-Line)",
        "level": "Level 2 (Analysis)",
        "exam_reference": "Ch08 Slide 47, 48 (PEA Feeder Topologies)",
        "question": "Contrast the Radial Line and Tie-Line feeder configurations used in PEA medium voltage networks, evaluating their construction complexity, capital cost, and reliability during feeder faults.",
        "question_th": "จงเปรียบเทียบรูปแบบสายป้อนระบบจำหน่ายแรงดันปานกลางของ กฟภ. ระหว่าง แบบรัศมี (Radial Line) และ แบบเชื่อมโยงระหว่างสายป้อน (Tie Line) ในประเด็น: ความซับซ้อน, ค่าก่อสร้าง, และความเชื่อถือได้เมื่อเกิดฟอลต์",
        "formula": "$$\\text{Radial Line: Simple Tree } \\longrightarrow \\text{Lowest Cost, Easy Protection, } \\textbf{Low Reliability}$$\n\n$$\\text{Tie Line: Interconnected Feeders with Tie CB } \\longrightarrow \\text{Higher Cost, Flexible Back-feed, } \\textbf{High Reliability}$$",
        "solution": "1. Radial Line Medium Voltage Distribution (ระบบสายป้อนแบบรัศมี / กิ่งไม้ - สไลด์ที่ 47):\n- Topology: Single feeder originates from the substation switchgear and branches outwards like tree branches to supply distribution transformers.\n- Advantages: Simplest layout, lowest construction cost, straightforward protection coordination (unidirectional fault current).\n- Disadvantages: Low reliability. Any short circuit or line break on the trunk feeder causes the upstream breaker to trip, interrupting power to all downstream customers without alternative supply path.\n\n2. Tie Line Medium Voltage Distribution (ระบบสายป้อนแบบเชื่อมโยงระหว่างสายป้อน - สไลด์ที่ 48):\n- Topology: Two or more feeders originating from different substations (Substation A and Substation B) or different busbars are connected via normally-open Tie Switches or Tie Circuit Breakers.\n- Advantages: High reliability. When a fault occurs on feeder A, the faulted section can be isolated via sectionalizing switches, and the remaining healthy portion can be back-fed by closing the Tie Switch to Substation B.\n- Disadvantages: Higher capital cost for tie lines, reclosers, automated switchgear, and complex bidirectional protection schemes.",
        "solution_th": "1. ระบบสายป้อนแบบรัศมี (Radial Line Distribution - สไลด์ที่ 47):\n- โครงสร้าง: สายป้อนแตกกิ่งก้านออกจากสถานีไฟฟ้าย่อยเพียงทิศทางเดียวเหมือนกิ่งไม้\n- ข้อดี: โครงสร้างไม่ซับซ้อน, ค่าก่อสร้างและอุปกรณ์ถูกที่สุด, การประสานรีเลย์ป้องกันทำได้ง่ายเพราะกระแสฟอลต์ไหลทิศทางเดียว\n- ข้อเสีย: ความเชื่อถือได้ต่ำ (Low Reliability) หากเกิดฟอลต์หรือสายขาดที่ต้นทาง เบรกเกอร์จะทริปตัดไฟ ทำให้ผู้ใช้ไฟฟ้าทั้งหมดที่อยู่ถัดไปดับทั้งหมดโดยไม่มีแหล่งจ่ายสำรอง\n\n2. ระบบสายป้อนแบบเชื่อมโยง (Tie Line Distribution - สไลด์ที่ 48):\n- โครงสร้าง: ปลายสายป้อนจากต่างสถานี (สถานี ก. และ สถานี ข.) หรือต่างวงจร จะถูกเชื่อมโยงกันผ่าน 'จุดต่อไลน์ (Tie Point / Tie Breaker)' ซึ่งปกติเปิดวงจรไว้ (Normally Open)\n- ข้อดี: ความเชื่อถือได้สูงมาก (High Reliability) หากเกิดฟอลต์บนสายป้อน ก. สามารถปลดสวิตช์แยกส่วนที่ชำรุดออก แล้วสับสวิตช์ Tie Line เพื่อดึงไฟฟ้าจากสถานี ข. มาจ่ายแทนได้ทันที\n- ข้อเสีย: ต้นทุนค่าก่อสร้างสูงกว่า และระบบควบคุมรีเลย์ป้องกันมีความซับซ้อนขึ้น",
        "pitfall": "Radial = Low cost, Low reliability (tree). Tie Line = Higher cost, High reliability (can switch power from adjacent substation during outages).",
        "pitfall_th": "สรุปแม่นๆ: แบบรัศมี (Radial) = ถูกสุด แต่ไฟดับทั้งแถบถ้าสายขาด; แบบ Tie Line = แพงกว่า มีสวิตช์เชื่อมสถานี ก. กับ ข. ดึงไฟข้ามสถานีได้เมื่อมีปัญหา",
        "diagram": "images/ch08_slide_47.png",
        "diagram_caption": "Slide 47 & 48: Radial Line vs Tie-Line Distribution Topologies",
        "diagram_caption_th": "สไลด์ที่ 47 และ 48: สายป้อนแบบรัศมี เทียบกับ แบบเชื่อมโยงระหว่างสถานี กฟภ.",
        "mastered": False
    },

    # -------------------------------------------------------------------------
    # CH08-11
    # -------------------------------------------------------------------------
    {
        "id": "CH08-11",
        "chapter": "Chapter 8",
        "topic": "PEA Low Voltage Distribution Systems (1-Phase vs 3-Phase Standard)",
        "topic_th": "ระบบจำหน่ายแรงดันต่ำของ กฟภ. (1 เฟส 2/3 สาย และ 3 เฟส 4 สาย 400/230 V)",
        "level": "Level 1 (Concept)",
        "exam_reference": "Ch08 Slide 49, 50 (PEA Low Voltage Distribution)",
        "question": "Describe PEA's Low Voltage distribution systems, explaining the configurations and specific use cases of 1-phase 2-wire, 1-phase 3-wire, and 3-phase 4-wire systems.",
        "question_th": "จงอธิบายระบบจำหน่ายแรงดันต่ำของ กฟภ. ทั้ง 1 เฟส 2 สาย (230 V), 1 เฟส 3 สาย (460/230 V ไฟถนน) และ 3 เฟส 4 สาย (400/230 V มาตรฐาน) พร้อมลักษณะการนำไปใช้งาน",
        "formula": "$$\\text{1-Phase 2-Wire: } 230\\text{ V (Standard Residential)}$$\n\n$$\\text{1-Phase 3-Wire: } 460/230\\text{ V (Center-tapped, Street Lighting)}$$\n\n$$\\text{3-Phase 4-Wire: } 400/230\\text{ V } (V_L = 400\\text{ V}, \\quad V_p = 230\\text{ V, Commercial \\& Motor Loads)}$$",
        "solution": "1. Single-Phase Low Voltage Systems (Ch08 Slide 49):\n- 1-Phase 2-Wire (230 V): Standard residential service. One phase wire and one neutral wire at 230 V, 50 Hz.\n- 1-Phase 3-Wire (460/230 V): Supplied by center-tapped single-phase distribution transformer. Phase-to-neutral is 230 V, while phase-to-phase across the outer legs is 460 V. Widely used for street lighting circuits to transmit power twice as far with acceptable voltage drop.\n\n2. Three-Phase Low Voltage System (Ch08 Slide 50):\n- 3-Phase 4-Wire (400/230 V standard): Secondary side of 22 kV or 33 kV distribution transformers connected in Wye (Star) with grounded neutral (N).\n- Line-to-Line Voltage: $V_L = 400\\text{ V}$\n- Phase-to-Neutral Voltage: $V_p = \\frac{400}{\\sqrt{3}} \\approx 230\\text{ V}$\n- Supplies 3-phase commercial facilities, workshops, water pumps, industrial induction motors, and balanced 3-phase distribution networks.",
        "solution_th": "1. ระบบจำหน่ายแรงดันต่ำ 1 เฟส (สไลด์ที่ 49):\n- 1 เฟส 2 สาย (แรงดัน 230 V): ระบบทั่วไปสำหรับบ้านพักอาศัย ประกอบด้วยสายไฟ 1 เส้น และสายนิวทรัล 1 เส้น\n- 1 เฟส 3 สาย (แรงดัน 460/230 V): จ่ายจากหม้อแปลง 1 เฟสแบบแท็ปกลาง (Center-tapped) แรงดันเทียบสายนิวทรัลเท่ากับ 230 V และแรงดันระหว่างสายขอบนอกเท่ากับ 460 V นิยมใช้สำหรับ 'วงจรไฟฟ้าแสงสว่างสาธารณะ/ไฟถนน (Street Light)' เพื่อส่งไฟฟ้าได้ระยะทางไกลขึ้นโดยแรงดันไม่ตก\n\n2. ระบบจำหน่ายแรงดันต่ำ 3 เฟส (สไลด์ที่ 50):\n- 3 เฟส 4 สาย (แรงดันมาตรฐาน 400/230 V): หม้อแปลงจำหน่ายลดแรงดันจาก 22 kV หรือ 33 kV ออกมาเป็นขดลวดสตาร์ (Star) ต่อสายนิวทรัลลงดิน\n- แรงดันระหว่างสาย (Line Voltage): $V_L = 400\\text{ V}$\n- แรงดันเฟสเทียบสายนิวทรัล (Phase Voltage): $V_p = \\frac{400}{\\sqrt{3}} \\approx 230\\text{ V}$\n- ใช้สำหรับจ่ายอาคารพาณิชย์, โรงงานขนาดเล็ก, มอเตอร์ 3 เฟส และร้านค้า",
        "pitfall": "1-phase 3-wire 460/230 V is specially used for street lighting circuits. Standard 3-phase low voltage in Thailand is 400/230 V (IEC standard).",
        "pitfall_th": "จุดสำคัญสไลด์ 49: ระบบ 1 เฟส 3 สาย 460/230 V ใช้สำหรับระบบไฟส่องสว่างถนน (Street light) ส่วนระบบ 3 เฟส 4 สายมาตรฐานคือ 400/230 V",
        "diagram": "images/ch08_slide_50.png",
        "diagram_caption": "Slide 50: PEA 3-Phase 4-Wire Low Voltage Distribution System (400/230 V)",
        "diagram_caption_th": "สไลด์ที่ 50: ระบบจำหน่ายแรงดันต่ำ 3 เฟส 4 สาย 400/230 V ของ กฟภ.",
        "mastered": False
    },

    # -------------------------------------------------------------------------
    # CH08-12
    # -------------------------------------------------------------------------
    {
        "id": "CH08-12",
        "chapter": "Chapter 8",
        "topic": "Electricity Service Connection, Demand Levels & Standard Meter Sizes",
        "topic_th": "เกณฑ์การจ่ายไฟตามขนาดโหลด พิกัดมิเตอร์มาตรฐาน และขอบเขตความรับผิดชอบ",
        "level": "Level 2 (Analysis)",
        "exam_reference": "Ch08 Slide 51-55 (Service Connection & Metering)",
        "question": "State the electricity service connection rules based on customer power demand, list standard meter ratings in Thailand, and define the point of delivery / boundary of responsibility between the utility and the consumer for Low Voltage vs Medium Voltage connections.",
        "question_th": "จงระบุเกณฑ์การจ่ายกระแสไฟฟ้าตามขนาดความต้องการกำลังไฟฟ้าของผู้ใช้, ระบุขนาดมิเตอร์มาตรฐานในไทย, และอธิบายจุดส่งมอบ / ขอบเขตความรับผิดชอบระหว่างการไฟฟ้าฯ กับผู้ใช้ไฟฟ้าสำหรับกรณีแรงดันต่ำและแรงดันปานกลาง",
        "formula": "$$\\text{Load } < 300\\text{ kVA} \\longrightarrow \\text{Low Voltage (230/400 V)}$$\n\n$$\\text{Load } > 300\\text{ kVA} \\longrightarrow \\text{Medium Voltage (12, 22, 24, or 33 kV with CT/VT)}$$\n\n$$\\text{Very Large Establishment } \\longrightarrow \\text{High Voltage (115 kV with Customer Dedicated Substation)}$$\n\n$$\\text{Meter Ratings (1-Phase 220V): } 5(15)\\text{ A}, \\quad 15(45)\\text{ A}, \\quad 30(100)\\text{ A}, \\quad 50(150)\\text{ A}$$\n\n$$\\text{Meter Ratings (3-Phase 380V): } 15(45)\\text{ A}, \\quad 30(100)\\text{ A}, \\quad 50(150)\\text{ A}, \\quad 200\\text{ A (CT)}, \\quad 400\\text{ A (CT)}$$",
        "solution": "1. Customer Connection Voltage based on Load Demand (Slide 51):\n- Load < 300 kVA: Supplied at Low Voltage (230/400 V) from utility pole distribution transformers.\n- Large Establishment (> 300 kVA): Supplied at Medium Voltage (12 kV, 22 kV, 24 kV, or 33 kV). Customer must install dedicated transformer.\n- Very Large Establishment: Supplied at High Voltage (115 kV). Customer must construct their own private substation.\n\n2. Standard Meter Sizes in Thailand (Slide 52):\n- 1-Phase 220 V: 5(15) A, 10(30) A, 15(45) A, 30(100) A, 50(150) A. (Number in parentheses is peak thermal withstand current).\n- 3-Phase 380/220 V: 15(45) A, 30(100) A, 50(150) A; loads above 150 A require Current Transformers (CT) with 200 A or 400 A meters.\n- MV 12 kV: 15 A (300 kVA) up to 750 A (15,000 kVA).\n- MV 24 kV: 10 A (400 kVA) up to 625 A (25,000 kVA).\n\n3. Points of Delivery & Boundaries of Responsibility (Slides 53-55):\n- Low Voltage: Utility owns and maintains lines up to the kWh meter on the pole. Customer is responsible for service entrance wires, main switch / MDB, and internal wiring.\n- Medium Voltage Case 1 (Overhead Line Connection): Utility installs Lightning Arresters (LA), CT, VT, and primary kWh meter. Utility responsibility ends at meter pole; customer owns and maintains transformer, drop-out fuses, and secondary distribution.\n- Medium Voltage Case 2 (Underground Cable Connection): High-voltage switchgear and underground cables transition power to customer transformer; utility metering is done via MV CT/VT.",
        "solution_th": "1. เกณฑ์การจ่ายกระแสไฟฟ้าตามขนาดความต้องการพลังไฟฟ้า (สไลด์ที่ 51):\n- โหลดขนาดเล็ก (< 300 kVA): จ่ายด้วยระบบแรงดันต่ำ (230/400 V) ผ่านหม้อแปลงจำหน่ายของการไฟฟ้าฯ\n- สถานประกอบการขนาดใหญ่ (> 300 kVA): จ่ายด้วยระบบแรงดันปานกลาง (12 kV, 22 kV, 24 kV หรือ 33 kV) โดยผู้ใช้ไฟฟ้าต้องติดตั้งหม้อแปลงของตนเอง\n- สถานประกอบการขนาดใหญ่พิเศษ: จ่ายด้วยระบบแรงดันสูง (115 kV) และผู้ใช้ไฟฟ้าต้องสร้างสถานีไฟฟ้าย่อยเฉพาะของตนเอง\n\n2. พิกัดขนาดมิเตอร์มาตรฐานในไทย (สไลด์ที่ 52):\n- 1 เฟส 220 V: 5(15) A, 10(30) A, 15(45) A, 30(100) A, 50(150) A (ตัวเลขในวงเล็บคือกระแสสูงสุดที่รับได้ต่อเนื่อง)\n- 3 เฟส 380/220 V: 15(45) A, 30(100) A, 50(150) A และหากใช้กระแสสูงกว่านี้ต้องใช้มิเตอร์ต่อร่วมกับ CT ขนาด 200 A, 400 A\n- แรงดันปานกลาง 12 kV: 15 A (300 kVA) ถึง 750 A (15,000 kVA)\n- แรงดันปานกลาง 24 kV: 10 A (400 kVA) ถึง 625 A (25,000 kVA)\n\n3. จุดส่งมอบและขอบเขตความรับผิดชอบ (สไลด์ที่ 53-55):\n- กรณีแรงดันต่ำ: การไฟฟ้าฯ รับผิดชอบถึงมิเตอร์ไฟฟ้าบนเสา; ผู้ใช้ไฟฟ้ารับผิดชอบตั้งแต่สายเมนเข้าอาคาร, แผงสวิตช์ประธาน (MDB) และระบบภายในทั้งหมด\n- กรณีแรงดันปานกลาง (สายอากาศ/สายใต้ดิน): การไฟฟ้าฯ ติดตั้งกับดักฟ้าผ่า (LA), CT, VT และมิเตอร์วัดหน่วยไฟฟ้าแรงสูง; ผู้ใช้ไฟฟ้ารับผิดชอบหม้อแปลงไฟฟ้า, สวิตช์ตัดตอนแรงสูง และระบบจำหน่ายภายใน",
        "pitfall": "Load boundary: < 300 kVA is Low Voltage; > 300 kVA is Medium Voltage. High Voltage requires a private substation (115 kV).",
        "pitfall_th": "เกณฑ์จำง่าย: โหลดต่ำกว่า 300 kVA รับแรงดันต่ำ; เกิน 300 kVA รับแรงดันปานกลาง; ถ้าโรงงานยักษ์ใหญ่รับแรงดันสูง 115 kV ต้องมีสถานีย่อยของตัวเอง",
        "diagram": "images/ch08_slide_54.png",
        "diagram_caption": "Slide 54: Medium Voltage Distribution Connection & Boundary of Responsibility",
        "diagram_caption_th": "สไลด์ที่ 54: การต่อระบบจำหน่ายแรงดันปานกลางและขอบเขตความรับผิดชอบ",
        "mastered": False
    },

    # -------------------------------------------------------------------------
    # CH08-13
    # -------------------------------------------------------------------------
    {
        "id": "CH08-13",
        "chapter": "Chapter 8",
        "topic": "Electrical Substations: Core Functions, Elements & AIS vs GIS Types",
        "topic_th": "สถานีไฟฟ้าย่อย (Substation): หน้าที่ อุปกรณ์หลัก และการเปรียบเทียบ AIS vs GIS",
        "level": "Level 1 (Concept)",
        "exam_reference": "Ch08 Slide 56-59 (Electrical Substations)",
        "question": "Explain the 4 primary functions of an electrical substation, list its core equipment, and compare Air-Insulated Substations (AIS / Outdoor) with Gas-Insulated Substations (GIS / Indoor, e.g. KKU Substation).",
        "question_th": "จงอธิบาย 4 หน้าที่หลักของสถานีไฟฟ้าย่อย (Electrical Substation), ระบุอุปกรณ์หลักภายในสถานี, และเปรียบเทียบข้อดี-ข้อจำกัดระหว่างสถานีลานโล่ง (AIS Outdoor) กับสถานีแบบใช้ก๊าซฉนวน (GIS Indoor เช่น สถานีไฟฟ้าย่อย มข.)",
        "formula": "$$\\text{Functions: 1. Voltage Transformation, 2. Switching, 3. Fault Clearance/Protection, 4. Voltage/VAR Control}$$\n\n$$\\text{Core Elements: Power Transformers, Circuit Breakers (}\\text{SF}_6\\text{/Vacuum), Disconnectors, CT/VT, Relays, LA, Grounding Grid}$$\n\n$$\\text{AIS (Outdoor): Air insulation, large footprint, lower initial cost, weather-exposed}$$\n\n$$\\text{GIS (Indoor): }\\text{SF}_6\\text{ gas (high dielectric strength), 85-90\\% smaller footprint, enclosed, silent (e.g. KKU Substation)}$$",
        "solution": "1. Four Primary Functions of Electrical Substations (Ch08 Slide 57):\n- 1) Voltage Transformation: Steps up voltage from generators to transmission grid or steps down from transmission to medium-voltage distribution circuits.\n- 2) Switching Operations: Connects and disconnects transmission lines, busbars, and feeders for power routing and load balancing.\n- 3) System Protection: Automatically clears short-circuit faults via circuit breakers and protective relays to safeguard equipment.\n- 4) Voltage Regulation and Reactive Power Support: Utilizes shunt capacitor banks and shunt reactors to maintain stable grid voltage.\n\n2. Seven Substation Classifications:\nTransmission substation, Distribution substation, Collector substation (for wind/solar), Converter substation (HVDC AC-to-DC), Switching station, Traction substation (electric rail/trains), Mobile substation.\n\n3. Core Equipment in a Substation (Slide 58):\n- Power Transformers (หม้อแปลงกำลัง)\n- Circuit Breakers (สวิตช์ตัดตอนอัตโนมัติ: $\\text{SF}_6$, vacuum, oil, air)\n- Disconnecting Switches / Isolators (ใบมีดตัดตอน)\n- Instrument Transformers (Current Transformers: CT, Potential/Voltage Transformers: PT/VT)\n- Protective Relays & SCADA Control Panels\n- Lightning Arresters (กับดักเสิร์จ/ฟ้าผ่า)\n- Grounding Grid (ตะแกรงระบบต่อลงดิน)\n\n4. Outdoor (AIS) vs Indoor (GIS) Substations (Slide 59):\n- Air-Insulated Substation (AIS / Outdoor): Uses atmospheric air as insulating medium. Requires large clearance distances, resulting in a large land footprint. Cheaper equipment, but exposed to weather, lightning, and atmospheric pollution.\n- Gas-Insulated Substation (GIS / Indoor): Encapsulates all conductors and switchgear inside grounded metal enclosures filled with Sulfur Hexafluoride ($\\text{SF}_6$) gas. $\\text{SF}_6$ has 2.5-3 times higher dielectric strength than air. Reduces land area requirements by 85-90%. Silent, safe, fireproof, protected from environment, ideal for densely populated urban centers and university campuses (e.g. KKU Indoor Substation).",
        "solution_th": "1. 4 หน้าที่หลักของสถานีไฟฟ้าย่อย (สไลด์ที่ 57):\n- 1) แปลงระดับแรงดันไฟฟ้า (Voltage Transformation): เพิ่มแรงดันจากโรงไฟฟ้าเข้าสายส่ง หรือลดแรงดันจากสายส่งเข้าสู่ระบบจำหน่าย\n- 2) สลับเปลี่ยนวงจร (Switching): เชื่อมต่อหรือตัดแยกสายส่งและสายป้อน เพื่อจัดสรรทิศทางการไหลของกำลังไฟฟ้า\n- 3) ป้องกันระบบ (Protection): ปลดวงจรเมื่อเกิดฟอลต์หรือกระแสลัดวงจรด้วยเซอร์กิตเบรกเกอร์และรีเลย์อย่างรวดเร็ว\n- 4) ควบคุมระดับแรงดันและกำลังไฟฟ้ารีแอกทีฟ (Voltage & Reactive Power Control): ปรับแรงดันด้วย Capacitor Bank หรือ Reactor\n\n2. 7 ประเภทของสถานีไฟฟ้าย่อย:\nสถานีสายส่ง (Transmission), สถานีระบบจำหน่าย (Distribution), สถานีรวบรวมไฟ (Collector - ฟาร์มโซลาร์/กังหันลม), สถานีแปลงกระแส (Converter - HVDC), สถานีตัดตอน (Switching Station), สถานีระบบรถไฟ (Traction), สถานีไฟฟ้าย่อยเคลื่อนที่ (Mobile Substation)\n\n3. อุปกรณ์หลักในสถานีไฟฟ้าย่อย (สไลด์ที่ 58):\n- หม้อแปลงไฟฟ้ากำลัง (Power Transformer)\n- เซอร์กิตเบรกเกอร์ (Circuit Breakers: ชนิดก๊าซ $\\text{SF}_6$, สุญญากาศ Vacuum, น้ำมัน)\n- สวิตช์ใบมีดตัดตอน (Disconnecting Switch / Isolator)\n- หม้อแปลงสำหรับเครื่องมือวัด (CT และ PT/VT)\n- รีเลย์ป้องกัน (Protection Relays) และระบบควบคุมตู้สวิตช์บอร์ด\n- กับดักฟ้าผ่า (Lightning Arrester: LA)\n- ลานต่อลงดิน (Grounding Grid)\n\n4. สถานีแบบลานโล่ง (AIS) vs สถานีแบบใช้ก๊าซฉนวนในอาคาร (GIS) (สไลด์ที่ 59):\n- แบบลานโล่ง (AIS - Air Insulated Substation): ใช้อากาศเป็นฉนวน ต้องมีระยะห่างมาก ทำให้ใช้พื้นที่กว้างขวาง ราคาอุปกรณ์ถูกกว่า แต่สัมผัสสภาพอากาศ ฝุ่น และฟ้าผ่าโดยตรง\n- แบบใช้ก๊าซฉนวนในร่ม (GIS - Gas Insulated Substation): บรรจุอุปกรณ์ในท่อโลหะปิดผนึกด้วยก๊าซซัลเฟอร์เฮกซะฟลูออไรด์ ($\\text{SF}_6$) ซึ่งเป็นฉนวนดีกว่าอากาศ 2.5-3 เท่า ลดพื้นที่ติดตั้งลงได้ถึง 85-90% เหมาะกับพื้นที่ในเมืองและในมหาวิทยาลัย (เช่น 'KKU Indoor Substation' สถานีไฟฟ้าย่อยในร่ม มหาวิทยาลัยขอนแก่น)",
        "pitfall": "GIS uses SF6 gas, reducing footprint by 85-90% compared to AIS. Slide 59 specifically showcases the KKU Indoor Substation as a prime example.",
        "pitfall_th": "จุดสำคัญสไลด์ 59: สถานี GIS ใช้ก๊าซ SF6 ประหยัดพื้นที่ได้ถึง 85-90% ปลอดภัย ไร้เสียงรบกวน โดยในสไลด์อาจารย์ยกตัวอย่าง KKU Indoor Substation (สถานีย่อย มข.) โดยตรง",
        "diagram": "images/ch08_slide_58.png",
        "diagram_caption": "Slide 58 & 59: Elements of Substations and KKU Indoor Substation",
        "diagram_caption_th": "สไลด์ที่ 58 และ 59: อุปกรณ์สถานีไฟฟ้าย่อย และสถานีย่อยในร่ม มหาวิทยาลัยขอนแก่น (KKU GIS)",
        "mastered": False
    },

    # -------------------------------------------------------------------------
    # CH08-14
    # -------------------------------------------------------------------------
    {
        "id": "CH08-14",
        "chapter": "Chapter 8",
        "topic": "Transmission Towers, Tower Footing Resistance & Lightning Protection",
        "topic_th": "ประเภทเสาสายส่ง ความต้านทานดินของเสา และการป้องกันฟ้าผ่าในระบบสายส่ง",
        "level": "Level 2 (Analysis)",
        "exam_reference": "Ch08 Slide 7, 38 & Final Exam ข้อ 5.3",
        "question": "Classify high-voltage transmission towers into Suspension, Tension, Dead-end, and Transposition towers. Define Tower Footing Resistance ($R_{\\text{tower}}$), state why it must be maintained $\\le 10\\;\\Omega$, and explain the Back Flashover phenomenon.",
        "question_th": "จงจำแนกประเภทเสาสายส่งไฟฟ้าแรงสูง (เสาแขวน, เสารั้ง, เสาปลายสาย, เสาสลับเฟส) อธิบายความต้านทานดินของเสา (Tower Footing Resistance) ว่าเหตุใดต้องต่ำกว่า $10\\;\\Omega$ และอธิบายปรากฏการณ์แบ็กแฟลชโอเวอร์ (Back Flashover)",
        "formula": "$$\\text{Suspension (เสาแขวน): Straight route} \\quad | \\quad \\text{Tension (เสารั้ง): Route angles/corners}$$\n\n$$\\text{Dead-end (เสาปลายสาย): Substation terminations} \\quad | \\quad \\text{Transposition (เสาสลับเฟส): Phase balance}$$\n\n$$R_{\\text{tower}} \\le 10\\;\\Omega, \\qquad V_{\\text{tower top}} = I_{\\text{lightning}} \\times R_{\\text{tower}} + L \\frac{di}{dt}$$",
        "solution": "1. Transmission Tower Classifications:\n- Suspension Towers (เสาแขวน): Used along straight paths. Insulators hang vertically to support the physical weight of conductors.\n- Tension / Angle Towers (เสารั้ง/เสามุม): Used at line bends and angles. Insulator strings are positioned horizontally under heavy mechanical tension.\n- Dead-end Towers (เสาปลายสาย): Heavy-duty termination towers situated just outside substations to withstand full one-sided mechanical tension.\n- Transposition Towers (เสาสลับเฟส): Rotates phase conductor spatial positions by 120 degrees at regular 1/3 distance intervals to balance line inductances, capacitances, and phase voltages.\n\n2. Tower Footing Resistance ($R_{\\text{tower}}$):\n- Definition: The electrical contact resistance between the steel tower footing ground grid and the earth mass.\n- Standard Requirement: Must be maintained strictly below $10\\;\\Omega$.\n\n3. Back Flashover Phenomenon:\n- When lightning strikes the overhead shield wire (OHGW) or tower peak, huge surge current ($I_{\\text{lightning}} \\approx 50-100\\text{ kA}$) flows down the steel tower to earth.\n- Tower top voltage surges to $V_{\\text{tower}} = I_{\\text{lightning}} \\times R_{\\text{tower}}$.\n- If $R_{\\text{tower}} > 10\\;\\Omega$, $V_{\\text{tower}}$ exceeds the impulse flashover rating of the insulator strings, causing an electrical arc to jump from the tower back into the phase conductors (Back Flashover), tripping circuit breakers.",
        "solution_th": "1. การจำแนกประเภทเสาสายส่งไฟฟ้าแรงสูง:\n- เสาแขวน (Suspension Tower): ใช้ตามแนวทางตรง พวงลูกถ้วยแขวนในแนวดิ่งเพื่อรับน้ำหนักสายตัวนำ\n- เสารั้ง / เสามุม (Tension / Angle Tower): ใช้บริเวณจุดหักเลี้ยวหรือมุมเลี้ยวของแนวสายส่ง พวงลูกถ้วยถูกดึงในแนวนอนเพื่อรับแรงดึงเชิงกล\n- เสาปลายสาย (Dead-end Tower): เสาโครงสร้างแข็งแรงพิเศษบริเวณจุดสิ้นสุดสายส่งก่อนเข้าสถานีไฟฟ้า รับแรงดึงด้านเดียวอย่างมหาศาล\n- เสาสลับเฟส (Transposition Tower): เสาสำหรับสลับตำแหน่งสายตัวนำทั้ง 3 เฟสทุกๆ $1/3$ ของระยะทาง เพื่อให้ค่าความเหนี่ยวนำและความจุไฟฟ้าสมมาตรกันทั้ง 3 เฟส\n\n2. ความต้านทานดินของเสา (Tower Footing Resistance $R_{\\text{tower}}$):\n- คือ ค่าความต้านทานสัมผัสระหว่างโครงสร้างเหล็กของฐานเสากับเนื้อดิน\n- มาตรฐานกำหนดให้ต้องต่ำกว่า $10\\;\\Omega$\n\n3. ปรากฏการณ์แบ็กแฟลชโอเวอร์ (Back Flashover):\n- เมื่อฟ้าผ่าลงสายล่อฟ้า (Overhead Ground Wire) หรือยอดเสาสายส่ง กระแสฟ้าผ่ามหาศาล ($50-100\\text{ kA}$) จะไหลผ่านโครงเสาลงดิน\n- เกิดแรงดันพุ่งสูงที่ยอดเสา $V_{\\text{tower}} = I_{\\text{lightning}} \\times R_{\\text{tower}}$\n- หากค่า $R_{\\text{tower}} > 10\\;\\Omega$ แรงดันยอดเสาจะสูงเกินค่าทนแรงดันวาบไฟของลูกถ้วยฉนวน ส่งผลให้ประกายไฟกระโดดข้ามลูกถ้วยจากเสากลับเข้าสู่สายตัวนำไฟฟ้า (Back Flashover) ทำให้เกิดไฟฟ้าลัดวงจรและระบบตัดไฟทันที",
        "pitfall": "Back Flashover occurs from tower to line when footing resistance is too high ($> 10\\;\\Omega$). Keep $R_{\\text{tower}} \\le 10\\;\\Omega$ with ground rods or counterpoise wires.",
        "pitfall_th": "ข้อสอบวิเคราะห์: ถ้าความต้านทานดินของเสาสูงเกิน $10\\;\\Omega$ ฟ้าผ่าลงสายดินแต่จะกระโดดข้ามลูกถ้วยย้อนกลับเข้าสายส่ง (Back Flashover) เกิดทริปตัดไฟ",
        "diagram": "images/diagrams/transmission_towers.png",
        "diagram_caption": "Transmission Towers (Suspension, Tension, Transposition)",
        "diagram_caption_th": "โครงสร้างเสาสายส่งไฟฟ้าแรงสูง (เสาแขวน, เสารั้ง, เสาสลับเฟส)",
        "mastered": False
    },

    # -------------------------------------------------------------------------
    # CH08-15
    # -------------------------------------------------------------------------
    {
        "id": "CH08-15",
        "chapter": "Chapter 8",
        "topic": "Engineering Energy Conservation: Residential vs Industrial Systems",
        "topic_th": "มาตรการการอนุรักษ์พลังงานเชิงวิศวกรรม: ภาคที่อยู่อาศัย vs โรงงานอุตสาหกรรม",
        "level": "Level 2 (Analysis)",
        "exam_reference": "Final Exam ข้อ 5.5 & 5.6 (หน้า 24 - 8 คะแนนเต็ม)",
        "question": "Propose 4 practical energy conservation measures for residential homes and 4 advanced engineering measures for industrial factories, detailing the underlying engineering principles (Power Factor correction, Inverter AC, VFD Affinity Laws).",
        "question_th": "จงเสนอ 4 มาตรการอนุรักษ์พลังงานสำหรับบ้านพักอาศัย และ 4 มาตรการทางวิศวกรรมสำหรับโรงงานอุตสาหกรรม พร้อมอธิบายหลักการทางวิศวกรรมที่รองรับ (การปรับปรุง Power Factor, แอร์อินเวอร์เตอร์, กฎความคล้ายคลึงของมอเตอร์ VFD)",
        "formula": "$$\\text{Residential AC: } P = \\frac{\\text{BTU/hr}}{\\text{SEER} \\times 3.412} \\implies \\text{High SEER Inverter + } 26^\\circ\\text{C with Fan (Saves 30-40\\%)}$$\n\n$$\\text{Industrial PF: } Q_C = P (\\tan\\theta_1 - \\tan\\theta_2) \\implies \\text{Eliminates Surcharges \\& Reduces } I^2 R$$\n\n$$\\text{Industrial Motor VFD: } P \\propto N^3 \\implies 20\\% \\text{ speed reduction cuts power by } 49\\%!$$",
        "solution": "1. Four Residential Energy Conservation Measures (Final Exam 5.5):\n- 1) Inverter Air Conditioning Optimization: Select high SEER inverter units; operate at 25-26°C supplemented by electric fans. Cuts AC electricity consumption by 30-40%.\n- 2) LED Lighting Conversion: Replace incandescent and fluorescent bulbs with LEDs, reducing lighting energy consumption by over 80% while reducing room heat load.\n- 3) Thermal Insulation: Install ceiling glass-wool insulation and solar reflective roof paint to prevent heat transfer into living spaces.\n- 4) Standby Power Elimination: Use master switch power strips to disconnect phantom loads (televisions, microwave ovens, chargers).\n\n2. Four Industrial Energy Conservation Measures (Final Exam 5.6):\n- 1) Power Factor (PF) Correction with Automatic Capacitor Banks: Elevates factory PF from ~0.75 to 0.95+. Eliminates reactive power penalty surcharges from PEA/MEA, reduces feeder $I^2 R$ loss, and frees transformer kVA capacity.\n- 2) Variable Frequency Drives (VFD) on Pumps and Fans: Governed by Affinity Laws ($P \\propto N^3$). Reducing pump or fan motor speed by 20% reduces required electrical power by $(0.8)^3 = 0.512$ (48.8% energy reduction!).\n- 3) Waste Heat Recovery: Install heat exchangers and economizers on boiler flue gas and furnace exhausts to preheat boiler feed water.\n- 4) Compressed Air System Optimization: Repair compressed air pipe leaks (typically wasting 20-30% of compressor energy), lower operating pressure, and install smart sequencing controllers.",
        "solution_th": "1. 4 มาตรการอนุรักษ์พลังงานในบ้านพักอาศัย (ข้อสอบไฟนอล ข้อ 5.5 - 4 คะแนน):\n- 1) การปรับปรุงระบบปรับอากาศ: เลือกใช้แอร์ระบบ Inverter เบอร์ 5 ค่า SEER สูง และปรับอุณหภูมิที่ 25-26°C ร่วมกับการเปิดพัดลม ประหยัดไฟแอร์ได้ถึง 30-40%\n- 2) เปลี่ยนหลอดไฟเป็นหลอด LED: ประหยัดพลังงานแสงสว่างได้มากกว่า 80% และลดความร้อนที่สะสมในห้อง\n- 3) ติดตั้งฉนวนกันความร้อน: ติดฉนวนใยแก้วใต้ฝ้าเพดาน ทาสีสะท้อนความร้อนที่หลังคา เพื่อลดภาระความร้อนเข้าสู่อาคาร\n- 4) ตัดกระแสไฟฟ้าสแตนด์บาย (Standby Power): ถอดปลั๊กหรือใช้รางปลั๊กแบบมีสวิตช์ปิดแยกอุปกรณ์ที่กินไฟตลอดเวลา (โทรทัศน์, ไมโครเวฟ, อะแดปเตอร์)\n\n2. 4 มาตรการอนุรักษ์พลังงานในโรงงานอุตสาหกรรม (ข้อสอบไฟนอล ข้อ 5.6 - 4 คะแนน):\n- 1) ปรับปรุงค่า Power Factor ด้วย Capacitor Bank: ปรับค่า PF จากเดิม (~0.75) ให้สูงกว่า 0.95 เพื่อยกเลิกค่าปรับเพาเวอร์แฟกเตอร์จากการไฟฟ้าฯ ลดกระแสไหลในสายส่ง และลดการสูญเสีย $I^2 R$\n- 2) ติดตั้งตัวปรับความเร็วรอบมอเตอร์ (VFD): ใช้กับปั๊มน้ำและพัดลม ตามกฎ Affinity Law กำลังไฟฟ้าแปรผันตามความเร็วรอบยกกำลังสาม ($P \\propto N^3$) หากลดความเร็วลงเพียง 20% จะประหยัดพลังงานได้ถึง 49%!\n- 3) นำความร้อนทิ้งกลับมาใช้ใหม่ (Waste Heat Recovery): ติดตั้ง Economizer นำความร้อนจากก๊าซไอเสียของหม้อต้มไอน้ำ (Boiler) มาอุ่นน้ำป้อน\n- 4) บำรุงรักษาระบบอัดอากาศ (Compressed Air System): ตรวจหาและอุดรอยรั่วท่อลม ซึ่งมักสูญเสียพลังงานสูงถึง 20-30% ของพลังงานที่ปั๊มลมใช้",
        "pitfall": "VFD Affinity Law: Power varies with the CUBE of speed ($P \\propto N^3$). A 20% speed drop halves power consumption! PF correction saves penalties and $I^2 R$ losses.",
        "pitfall_th": "จุดเน้นสูตรข้อสอบ: กฎของมอเตอร์ VFD กำลังงานแปรผันตามรอบยกกำลังสาม ($P \\propto N^3$) ลดรอบนิดเดียว ประหยัดพลังงานได้เกือบครึ่ง!",
        "diagram": "images/diagrams/exam_p24_prob55_56_energy_saving.png",
        "diagram_caption": "Final Exam Problems 5.5 & 5.6: Energy Conservation in Home and Factory",
        "diagram_caption_th": "ข้อสอบจริง ข้อ 5.5 และ 5.6: การอนุรักษ์พลังงานในบ้านและโรงงานอุตสาหกรรม",
        "mastered": False
    }
]
