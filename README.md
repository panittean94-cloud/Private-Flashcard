# ⚡ Private-Flashcard: Fundamental of Electrical Engineering (Final Exam Prep)

> **Curated Exam Flashcard System for KKU Electrical Engineering (Chapters 6 – 10)**  
> Prepared for the Final Exam (Assoc. Prof. Nararat Ruangchaijatupon).

---

## 🌟 Key Features

1. **Interactive Web Application (`index.html`)**:
   - 3D Flashcard Flip Animation (Spacebar or click to flip).
   - Rendered with **KaTeX** for clean mathematical formulas ($E_a = K_a \Phi \omega_m$, $\sqrt{3} V_L I_L \cos\theta$, etc.).
   - Filter by **Chapter** (Ch.6 3-Phase, Ch.7 Machines, Ch.8 Transformers, Ch.9 Power Systems, Ch.10 Instruments, Semiconductors).
   - Filter by **Difficulty**:
     - 🟢 **Level 1 (Concept)**: Fundamental rules, formulas, and theory.
     - 🔴 **Level 2 (Past Exam / Calc)**: Step-by-step solutions to homework and actual past exam papers.
   - Self-grading system (`Need Review` vs `Mastered`) with **persistent LocalStorage**.
   - Keyboard shortcuts: `Space` (flip), `←`/`→` (navigate), `1` (need review), `2` (mastered).
   - Instant search bar for formulas, terms (e.g., *BANI*, *CDRX*, *Shunt*, *Bhumibol*).

2. **Google Sheets Integration (`Code.gs`)**:
   - Includes full Google Apps Script backend to initialize, store, and edit cards right inside Google Sheets.
   - Real-time two-way synchronization with the web app.

---

## 🚀 How to Run the Web Flashcards

### Option A: Local Browser (No installation needed)
Simply double-click `index.html` to open it in Chrome, Edge, or Safari! All data and KaTeX render offline or via lightweight CDN.

### Option B: Deploy to GitHub Pages
1. Push this repository to GitHub (`main` branch).
2. Go to **Settings > Pages**.
3. Under **Branch**, select `main` and `/ (root)`, then click **Save**.
4. Your flashcards will be live on the web at `https://<username>.github.io/Private-Flashcard/`!

---

## 📊 Google Sheets Setup Guide (`Code.gs`)

1. Open [Google Sheets](https://sheets.new) and create a new spreadsheet.
2. In the menu, go to **Extensions > Apps Script**.
3. Delete any default code in `Code.gs` and paste the contents of `Code.gs` from this repository.
4. Click the **Save** icon (disk).
5. Refresh your Google Sheet. You will see a new menu: **⚡ FunE Flashcard System**.
6. Click **⚡ FunE Flashcard System > 🚀 Setup & Populate All Exam Cards** (authorize permissions if prompted).
   - All 27 exam cards with questions, answers, and hints will immediately populate into the sheet!
7. To connect with the web app:
   - In Apps Script, click **Deploy > New deployment**.
   - Select **Web app**.
   - Set **Execute as**: *Me*, and **Who has access**: *Anyone*.
   - Copy the deployed Web App URL.
   - In `index.html`, click the ⚙️ gear icon and paste the URL.

---

## 📚 Exam Syllabus Coverage

| Chapter | Topic | Key Exam Highlights |
| :--- | :--- | :--- |
| **Chapter 6** | Three-Phase Circuits | Y vs $\Delta$ relations, $\sqrt{3} \angle \pm 30^\circ$, $Z_Y = Z_\Delta / 3$, 3-phase power ($S, P, Q$), 12-hp motor calculations |
| **Chapter 7** | Electric Machinery | Stator vs Rotor, Back EMF ($E_a = K_a \Phi \omega_m$), Torque ($T_d = K_a \Phi I_a$), DC Shunt & Series motors, no-load series hazard, synchronous speed & slip, reversing 3-phase motor |
| **Chapter 8** | Electrical Transformers | Mutual induction principle, turns ratio ($a = N_1/N_2 = V_1/V_2 = I_2/I_1$), impedance reflection ($Z_1 = a^2 Z_2$), EMF eq ($E = 4.44 f N \Phi_m$), DC connection burnout hazard, 25 kVA calculations |
| **Chapter 9** | Power Systems & Energy Conservation | 4 stages (Gen, Trans, Dist, Util), EGAT vs MEA vs PEA, Hydro (fast startup, peak) vs Steam (slow startup, base), Thailand fuels (Natural gas primary), industrial energy saving |
| **Chapter 10** | Measuring Instruments | PMMC operation ($T_d = BANI, T_c = K\theta$), DC Ammeter with/without CDRX, DC Voltmeter with/without CDRX, Multi-range ammeter design (12-point exam problem) |
| **Bonus** | Semiconductors | N-type (Group 5, electrons) vs P-type (Group 3, holes), Si ($0.7\text{ V}$) vs Ge ($0.3\text{ V}$), Half-wave ($0.318 V_m$) vs Full-wave ($0.636 V_m$), filter capacitor |

---
*Created for Khon Kaen University (KKU) Engineering Students.*
