import os
import json
import pandas as pd
import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side

# Comprehensive dataset of 45 Flashcards covering ALL concepts, homework, and exact past exams
flashcards = [
    # =========================================================================
    # CHAPTER 6: THREE-PHASE CIRCUITS
    # =========================================================================
    {
        "id": "CH06-01",
        "chapter": "Chapter 6",
        "topic": "Star (Y) vs Delta (Δ) Voltage & Current Relations",
        "level": "Level 1 (Concept)",
        "exam_reference": "Lecture Slides & Formula Sheet",
        "question": "In a balanced 3-phase positive-sequence (abc) system, state the exact relationships between line quantities ($V_L, I_L$) and phase quantities ($V_p, I_p$) for both Y-connection and $\\Delta$-connection.",
        "formula": "Y: $V_L = \\sqrt{3}V_p\\angle +30^\\circ, I_L = I_p$\n$\\Delta$: $V_L = V_p, I_L = \\sqrt{3}I_p\\angle -30^\\circ$",
        "solution": "1. Star (Y) Connection:\n- Line voltage leads phase voltage by $30^\\circ$: $V_{ab} = \\sqrt{3}V_{an}\\angle +30^\\circ$\n- Line current equals phase current: $I_L = I_p$\n\n2. Delta (Δ) Connection:\n- Line voltage equals phase voltage: $V_L = V_p$\n- Line current lags phase current by $30^\\circ$: $I_a = \\sqrt{3}I_{ab}\\angle -30^\\circ$",
        "pitfall": "Do not confuse with negative sequence (acb) where line voltage leads by -30° (or lags by 30°). Remember: in Y, current is identical; in Δ, voltage is identical.",
        "mastered": False
    },
    {
        "id": "CH06-02",
        "chapter": "Chapter 6",
        "topic": "Delta to Wye (Δ ↔ Y) Impedance Conversion",
        "level": "Level 1 (Concept)",
        "exam_reference": "HW Ch.6 Problem 1 & 5",
        "question": "If a balanced $3\\phi$ load is connected in $\\Delta$ with impedance $Z_\\Delta = 60 + j30\\ \\Omega$, what is the equivalent impedance per phase when converted to a Wye (Y) connection ($Z_Y$)?",
        "formula": "$Z_Y = \\frac{Z_\\Delta}{3}$",
        "solution": "$$Z_Y = \\frac{Z_\\Delta}{3} = \\frac{60 + j30}{3} = 20 + j10\\ \\Omega$$\nConversely, if converting from Wye to Delta: $Z_\\Delta = 3 Z_Y$.",
        "pitfall": "A very common exam mistake is multiplying by 3 instead of dividing! A Delta load draws 3 times more current than a Wye load of the same impedance value, so equivalent Wye impedance must be 3 times smaller.",
        "mastered": False
    },
    {
        "id": "CH06-03",
        "chapter": "Chapter 6",
        "topic": "Three-Phase Power Formulas & Complex Power",
        "level": "Level 1 (Concept)",
        "exam_reference": "Formula Sheet & Lecture Slides",
        "question": "State the formulas for balanced $3\\phi$ Real Power ($P_{3\\phi}$), Reactive Power ($Q_{3\\phi}$), Apparent Power ($|S_{3\\phi}|$), and Complex Power ($S_{3\\phi}$) in terms of line values ($V_L, I_L$).",
        "formula": "$P_{3\\phi} = \\sqrt{3}V_L I_L \\cos\\theta\\quad [\\text{W}]$\n$Q_{3\\phi} = \\sqrt{3}V_L I_L \\sin\\theta\\quad [\\text{VAR}]$\n$|S_{3\\phi}| = \\sqrt{3}V_L I_L\\quad [\\text{VA}]$\n$S_{3\\phi} = \\sqrt{3}V_L I_L^* = P + jQ$",
        "solution": "When using Line values ($V_L, I_L$), always include the factor $\\sqrt{3}$.\nWhen using Phase values ($V_p, I_p$), use factor $3$:\n- $P = 3 V_p I_p \\cos\\theta$\n- $Q = 3 V_p I_p \\sin\\theta$\n- $S = 3 V_p I_p^*$\nwhere $\\theta = \\angle Z_p$ is the load phase impedance angle, and $PF = \\cos\\theta$.",
        "pitfall": "Never mix $\\sqrt{3}$ with phase quantities! It is either $\\sqrt{3}V_L I_L$ or $3 V_p I_p$.",
        "mastered": False
    },
    {
        "id": "CH06-04",
        "chapter": "Chapter 6",
        "topic": "Y-Connected Induction Motor Load Calculation",
        "level": "Level 2 (Past Exam / Calc)",
        "exam_reference": "HW Ch.6 Problem 4",
        "question": "A $3\\phi$, $12\\text{-hp}$ induction motor is Y-connected to a $3\\phi$ supply with line-to-line voltage $V_L = 380\\text{ V}, 50\\text{ Hz}$. The motor has $\\eta = 90\\%$ efficiency and a lagging power factor of $0.85$. Calculate: (1) Input real power ($P_{\\text{in}}$), (2) Line current ($I_L$), (3) Per-phase impedance magnitude ($|Z|$), resistance ($R$), and inductance ($L$). (1 hp = 746 W)",
        "formula": "$P_{\\text{out}} = 12 \\times 746\\text{ W}$\n$P_{\\text{in}} = P_{\\text{out}} / \\eta$\n$I_L = \\frac{P_{\\text{in}}}{\\sqrt{3} V_L \\cos\\theta}$\n$V_p = V_L / \\sqrt{3}$\n$Z = V_p / I_p$",
        "solution": "1. Input Power:\n$P_{\\text{out}} = 12 \\times 746 = 8,952\\text{ W}$\n$P_{\\text{in}} = 8,952 / 0.90 = 9,946.67\\text{ W}$ ($9.95\\text{ kW}$)\n\n2. Line Current:\n$$I_L = \\frac{9,946.67}{\\sqrt{3} \\times 380 \\times 0.85} = 17.78\\text{ A}$$\n\n3. Phase Impedance (Y-connection: $V_p = 380/\\sqrt{3} = 219.39\\text{ V}, I_p = I_L = 17.78\\text{ A}$):\n- $|Z| = 219.39 / 17.78 = 12.34\\ \\Omega$\n- $\\theta = \\arccos(0.85) = 31.79^\\circ$\n- $Z = 12.34\\angle 31.79^\\circ = 10.49 + j6.50\\ \\Omega$\n- Resistance: $R = 10.49\\ \\Omega$\n- Inductance: $X_L = 2\\pi f L = 6.50 \\implies L = 6.50 / (2\\pi \\times 50) = 20.7\\text{ mH}$.",
        "pitfall": "Always convert output mechanical horsepower to electrical input power using efficiency ($P_{\\text{in}} = P_{\\text{out}}/\\eta$) BEFORE calculating current!",
        "mastered": False
    },
    {
        "id": "CH06-05",
        "chapter": "Chapter 6",
        "topic": "Delta-Connected Motor Load Calculation",
        "level": "Level 2 (Past Exam / Calc)",
        "exam_reference": "HW Ch.6 Problem 5",
        "question": "A $3\\phi$, $10\\text{-hp}$ motor is $\\Delta$-connected to a $3\\phi$ supply with $V_L = 380\\text{ V}, 50\\text{ Hz}$, $\\eta = 85\\%$, and $PF = 0.8$ lagging. Find: (1) Line current ($I_L$), (2) Phase current ($I_p$), (3) Per-phase $\\Delta$ impedance ($Z_\\Delta$).",
        "formula": "$P_{\\text{in}} = (10 \\times 746) / 0.85 = 8,776.47\\text{ W}$\n$I_L = \\frac{P_{\\text{in}}}{\\sqrt{3} V_L \\cos\\theta}$\n$I_p = I_L / \\sqrt{3}, V_p = V_L = 380\\text{ V}$\n$Z_\\Delta = V_p / I_p$",
        "solution": "1. Input Power: $P_{\\text{in}} = 7,460 / 0.85 = 8,776.47\\text{ W}$\n\n2. Line Current:\n$$I_L = \\frac{8,776.47}{\\sqrt{3} \\times 380 \\times 0.8} = 16.67\\text{ A}$$\n\n3. Phase Quantities & Impedance:\n- Phase current: $I_p = I_L / \\sqrt{3} = 16.67 / \\sqrt{3} = 9.62\\text{ A}$\n- Phase voltage: $V_p = V_L = 380\\text{ V}$\n- Impedance magnitude: $|Z_\\Delta| = 380 / 9.62 = 39.5\\ \\Omega$\n- Angle: $\\theta = \\arccos(0.8) = 36.87^\\circ$\n- $Z_\\Delta = 39.5\\angle 36.87^\\circ = 31.6 + j23.7\\ \\Omega$\n($R_\\Delta = 31.6\\ \\Omega, X_{L\\Delta} = 23.7\\ \\Omega$).",
        "pitfall": "In Delta, $V_p = V_L$, but $I_p = I_L / \\sqrt{3}$. Do not divide voltage by $\\sqrt{3}$!",
        "mastered": False
    },
    {
        "id": "CH06-06",
        "chapter": "Chapter 6",
        "topic": "Two-Wattmeter Method for 3-Phase Power Measurement",
        "level": "Level 2 (Past Exam / Calc)",
        "exam_reference": "Lecture Slides & Jele Formula Sheet",
        "question": "Explain the Two-Wattmeter Method for measuring balanced 3-phase power. State the formulas for total active power ($P$), reactive power ($Q$), and power factor angle ($\\theta$) from meter readings $W_1$ and $W_2$.",
        "formula": "$P_{\\text{total}} = W_1 + W_2$\n$Q_{\\text{total}} = \\sqrt{3}(W_1 - W_2)$\n$\\tan\\theta = \\sqrt{3}\\frac{W_1 - W_2}{W_1 + W_2}$",
        "solution": "1. Total Real Power: $P = W_1 + W_2$\n2. Total Reactive Power: $Q = \\sqrt{3}(W_1 - W_2)$\n3. Power Factor Angle: $\\theta = \\arctan\\left(\\sqrt{3}\\frac{W_1 - W_2}{W_1 + W_2}\\right)$\n4. Power Factor: $PF = \\cos\\theta$\n\nSpecial Cases:\n- If $W_1 = W_2$: $\\theta = 0^\\circ \\implies PF = 1.0$ (purely resistive).\n- If $W_2 = 0$: $PF = 0.5$ ($\\\\theta = 60^\\circ$).\n- If $W_2 < 0$: $PF < 0.5$ (one wattmeter reading turns negative).",
        "pitfall": "If $PF < 0.5$, one wattmeter deflects backward. In calculations, you MUST preserve the negative sign (e.g. $W_1 + (-W_2)$).",
        "mastered": False
    },
    {
        "id": "CH06-07",
        "chapter": "Chapter 6",
        "topic": "Neutral Wire Current in Balanced vs Unbalanced Systems",
        "level": "Level 1 (Concept)",
        "exam_reference": "HW Ch.6 Problem 1, 2, 3",
        "question": "What is the neutral current $I_N$ in a balanced 4-wire Y-Y system? What causes current to flow in the neutral wire in an unbalanced system?",
        "formula": "$I_N = -(I_a + I_b + I_c)$",
        "solution": "1. Balanced System: $I_a + I_b + I_c = 0$, therefore neutral current is strictly ZERO ($I_N = 0$). No current returns through the neutral line.\n2. Unbalanced System: The phase currents do not sum to zero due to unequal load impedances ($Z_A \\neq Z_B \\neq Z_C$), so neutral current $I_N = -(I_a + I_b + I_c) \\neq 0$ carries the return unbalance current.",
        "pitfall": "If the neutral wire is disconnected in an unbalanced load, the neutral point shifts ($V_{Nn} \\neq 0$), causing severe overvoltage across the lighter load phase!",
        "mastered": False
    },

    # =========================================================================
    # CHAPTER 7: ELECTRICAL MACHINES (DC & AC)
    # =========================================================================
    {
        "id": "CH07-01",
        "chapter": "Chapter 7",
        "topic": "Right-Hand Rule for Magnetic Field around a Conductor",
        "level": "Level 1 (Concept)",
        "exam_reference": "Final Exam Problem 4.1 (Page 28)",
        "question": "Current flows upward along a straight vertical wire. Using the right-hand grip rule, sketch/state the direction of the magnetic field on the left and right sides of the wire.",
        "formula": "Right-Hand Grip Rule: Thumb = Current ($I$), Fingers = Field ($B$)",
        "solution": "Point right thumb upward along the current flow:\n- Left side of the wire: Magnetic field lines point OUT OF THE PAGE (represented by dots •).\n- Right side of the wire: Magnetic field lines point INTO THE PAGE (represented by crosses $\\times$).",
        "pitfall": "Direct 2-point exam question! Remember: Dot (•) = coming towards you / out of paper; Cross (×) = going away from you / into paper.",
        "mastered": False
    },
    {
        "id": "CH07-02",
        "chapter": "Chapter 7",
        "topic": "Lorentz Force on Current-Carrying Conductor in DC Motor",
        "level": "Level 1 (Concept)",
        "exam_reference": "Final Exam Problem 4.2 (Page 28)",
        "question": "State the formula and rule used to determine the electromagnetic force developed on a conductor in a DC motor armature.",
        "formula": "$\\vec{F} = I(\\vec{L} \\times \\vec{B}) \\implies F = B I L \\sin\\alpha$",
        "solution": "1. Formula: $F = B I L \\sin\\alpha$, where $B$ is flux density (Tesla), $I$ is conductor current (A), $L$ is active conductor length (m), and $\\alpha$ is the angle between wire and magnetic field (usually $90^\\circ$, so $F = BIL$).\n2. Direction: Determined by Fleming's Left-Hand Rule for Motors:\n- Thumb = Motion / Force ($F$)\n- First finger = Magnetic Field ($B$, North to South)\n- Second finger = Current ($I$, positive to negative).",
        "pitfall": "Use LEFT hand for motors (converting electrical to mechanical motion); use RIGHT hand for generators (inducing EMF).",
        "mastered": False
    },
    {
        "id": "CH07-03",
        "chapter": "Chapter 7",
        "topic": "DC Machine Stator and Rotor Structural Components",
        "level": "Level 1 (Concept)",
        "exam_reference": "Final Exam Problem 4.3 (Page 28)",
        "question": "What are the two main structural parts of a DC machine? Name at least 2 components found in each part.",
        "formula": "Machine = Stator (Stationary) + Rotor (Rotating)",
        "solution": "1. Stator (Stationary Part):\n- Frame / Yoke (cast iron outer housing and magnetic return path)\n- Main Field Poles & Pole Shoes (laminated sheet steel)\n- Field Windings (copper coils producing main flux $\\Phi$)\n- End covers and brush holders.\n\n2. Rotor / Armature (Rotating Part):\n- Armature Core (laminated silicon steel with slots)\n- Armature Windings (copper coils carrying load current)\n- Commutator (segmented copper bars with mica insulation)\n- Shaft, bearings, and cooling fan.",
        "pitfall": "Armature core is made of laminated silicon steel sheets specifically to minimize Eddy current losses and Hysteresis losses.",
        "mastered": False
    },
    {
        "id": "CH07-04",
        "chapter": "Chapter 7",
        "topic": "DC Machine Back EMF Formula & Physical Meaning",
        "level": "Level 1 (Concept)",
        "exam_reference": "Lecture Slides & Jele Formula Sheet",
        "question": "State the equation for induced armature back-EMF ($E_a$) in a DC machine and define all variables. How does it relate to motor speed?",
        "formula": "$E_a = K_a \\Phi \\omega_m = \\left(\\frac{p Z}{2\\pi a}\\right) \\Phi \\omega_m$",
        "solution": "- $E_a$ = Induced armature back EMF (V)\n- $K_a = \\frac{p Z}{2\\pi a}$ = Machine design constant ($p$ = poles, $Z$ = total conductors, $a$ = parallel paths)\n- $\\Phi$ = Magnetic flux per pole (Wb)\n- $\\omega_m$ = Mechanical angular velocity (rad/s) = $\\frac{2\\pi n}{60}$ ($n$ in rpm).\n\nPhysical Meaning: In a motor, $E_a$ opposes applied terminal voltage ($V_t$). As speed increases, $E_a$ increases, limiting armature current $I_a = (V_t - E_a)/R_a$.",
        "pitfall": "At starting ($n = 0$), $E_a = 0\\text{ V}$. Without starting resistors, inrush current $I_{\\text{start}} = V_t / R_a$ can reach 10-20 times rated current!",
        "mastered": False
    },
    {
        "id": "CH07-05",
        "chapter": "Chapter 7",
        "topic": "DC Machine Developed Torque & Converted Power",
        "level": "Level 1 (Concept)",
        "exam_reference": "Lecture Slides & Homework 7",
        "question": "State the formula for developed electromagnetic torque ($T_d$) in a DC motor and the relationship between developed mechanical power and electrical power.",
        "formula": "$T_d = K_a \\Phi I_a$\n$P_{\\text{developed}} = E_a I_a = T_d \\omega_m$",
        "solution": "1. Developed Torque: $T_d = K_a \\Phi I_a$ [$\\text{N}\\cdot\\text{m}$]. It is strictly proportional to field flux and armature current.\n2. Converted Power: $P_d = E_a I_a = T_d \\omega_m$ [W]. The internal electrical power converted equals mechanical power developed.\n3. Shaft Output Power: $P_{\\text{shaft}} = P_d - P_{\\text{rotational losses}}$.",
        "pitfall": "Do not confuse developed torque ($T_d$) with shaft torque ($T_{\\text{shaft}}$). Rotational losses (friction + windage) reduce output torque.",
        "mastered": False
    },
    {
        "id": "CH07-06",
        "chapter": "Chapter 7",
        "topic": "DC Shunt Motor Equivalent Circuit & Speed/Torque Calculation",
        "level": "Level 2 (Past Exam / Calc)",
        "exam_reference": "HW Ch.7 Problem 4 & Talui Homework Page 1",
        "question": "A 2-pole, 2.5 hp, 100 V DC shunt motor has $K_a = 153$, full-load total current $I_t = 25.0\\text{ A}$, armature resistance $R_a = 0.75\\ \\Omega$, field flux $\\Phi = 10.0\\text{ mWb}$, and field resistance $R_f = 440\\ \\Omega$. Calculate: (1) Armature current ($I_a$), (2) Back EMF ($E_a$), (3) Motor speed ($n$ in rpm), (4) Developed torque ($T_d$).",
        "formula": "$I_f = V_t / R_f$\n$I_a = I_t - I_f$\n$E_a = V_t - I_a R_a$\n$\\omega_m = E_a / (K_a \\Phi) \\implies n = \\frac{60 \\omega_m}{2\\pi}$\n$T_d = K_a \\Phi I_a$",
        "solution": "1. Field current: $I_f = 100 / 440 = 0.23\\text{ A}$\n2. Armature current: $I_a = I_t - I_f = 25.0 - 0.23 = 24.77\\text{ A}$\n3. Back EMF: $E_a = V_t - I_a R_a = 100 - (24.77 \\times 0.75) = 100 - 18.58 = 81.42\\text{ V}$\n4. Speed calculation:\n$$E_a = K_a \\Phi \\omega_m = 153 \\times (10 \\times 10^{-3}) \\times \\left(\\frac{2\\pi n}{60}\\right)$$\n$$81.42 = 1.53 \\times 0.10472 \\times n = 0.16022 \\times n \\implies n = 508.17\\text{ rpm}$$\n5. Developed Torque:\n$$T_d = K_a \\Phi I_a = 153 \\times (10 \\times 10^{-3}) \\times 24.77 = 37.9\\text{ N}\\cdot\\text{m}$$.",
        "pitfall": "Always subtract field current $I_f$ from total supply current $I_t$ before computing $I_a R_a$ drop! Field current does not flow through armature.",
        "mastered": False
    },
    {
        "id": "CH07-07",
        "chapter": "Chapter 7",
        "topic": "DC Series Motor Comparison & Runaway Hazard",
        "level": "Level 2 (Past Exam / Calc)",
        "exam_reference": "HW Ch.7 Problem 5 & Talui Homework Page 2-3",
        "question": "A 2.5 hp series motor has $K_a = 153, R_a = 0.75\\ \\Omega, \\Phi = 10.0\\text{ mWb}, R_f = 440\\ \\Omega$. Find the required terminal voltages: (a) $V_{t1}$ to give the same speed ($508.17\\text{ rpm}$) as Problem 4, (b) $V_{t2}$ to give the same torque ($37.9\\text{ N}\\cdot\\text{m}$) as Problem 4.",
        "formula": "$V_t = I_a(R_a + R_f) + E_a$\n(a) Same speed: $E_a = 81.42\\text{ V}, I_a = P / E_a = 1865 / 81.42 = 22.91\\text{ A}$\n(b) Same torque: $I_a = 24.77\\text{ A}, E_a = P / I_a = 1865 / 24.77 = 75.3\\text{ V}$",
        "solution": "(a) For same speed ($n = 508.17\\text{ rpm}$):\n$E_a = 81.42\\text{ V}$\n$I_a = P_e / E_a = 1865 / 81.42 = 22.91\\text{ A}$\n$$V_{t1} = I_a(R_f + R_a) + E_a = 22.91(440 + 0.75) + 81.42 = 10,181\\text{ V} = 10.18\\text{ kV}$$\n\n(b) For same torque ($T_d = 37.9\\text{ N}\\cdot\\text{m}$):\n$I_a = 24.77\\text{ A}$\n$E_a = P_e / I_a = 1865 / 24.77 = 75.3\\text{ V}$\n$$V_{t2} = I_a(R_f + R_a) + E_a = 24.77(440.75) + 75.3 = 10,993\\text{ V} \\approx 11.0\\text{ kV}$$\n\n(c) Can same speed and same torque happen simultaneously? NO, because speed and torque uniquely dictate $E_a$ and $I_a$.",
        "pitfall": "Why must a DC series motor never run at no load? Because $I_a \\to 0 \\implies \\Phi \\to 0 \\implies \\omega_m \\approx V_t / (K_a \\Phi) \\to \\infty$ (motor dangerously overspeeds and tears itself apart).",
        "mastered": False
    },
    {
        "id": "CH07-08",
        "chapter": "Chapter 7",
        "topic": "Squirrel Cage Induction Motor & Reversing Rotation",
        "level": "Level 1 (Concept)",
        "exam_reference": "Final Exam Problem 4.4 (Page 27)",
        "question": "What is a squirrel-cage rotor in a 3-phase induction motor? Explain its operating principle and describe how to reverse its direction of rotation.",
        "formula": "Swap any 2 supply lines (Phase A and Phase B)",
        "solution": "1. Structure: Rotor composed of thick copper or aluminum conductor bars embedded in a laminated steel core, permanently short-circuited at both ends by heavy conductive end-rings (resembling a squirrel exercise wheel).\n2. Operating Principle: 3-phase AC in stator windings produces a Rotating Magnetic Field (RMF). The RMF sweeps across the rotor bars, inducing an EMF and heavy circulating currents. Interaction between rotor currents and the RMF produces driving torque following Lenz's Law.\n3. Reversing Direction: Swap ANY TWO of the three incoming supply lines (e.g. swap A and B). This reverses the phase sequence from A-B-C to A-C-B, reversing the RMF rotation direction.",
        "pitfall": "Direct 8-point exam question! Never say 'reverse DC polarity' because this is an AC motor without brushes or commutators.",
        "mastered": False
    },
    {
        "id": "CH07-09",
        "chapter": "Chapter 7",
        "topic": "Synchronous Speed, Rotor Speed, and Slip",
        "level": "Level 1 (Concept)",
        "exam_reference": "Lecture Slides & Jele Formula Sheet",
        "question": "Define Synchronous Speed ($N_s$) and Slip ($s$) in a 3-phase induction motor. Why can an induction motor never run at synchronous speed under normal motoring conditions?",
        "formula": "$N_s = \\frac{120 f}{p}\\quad [\\text{rpm}]$\n$s = \\frac{N_s - N_r}{N_s} = \\frac{\\omega_s - \\omega_r}{\\omega_s}$",
        "solution": "1. Synchronous Speed: $N_s = \\frac{120 f}{p}$ is the rotational speed of the stator magnetic field ($f$ = grid frequency in Hz, $p$ = total poles).\n2. Slip: $s = \\frac{N_s - N_r}{N_s}$, typically $2\\% - 5\\%$ at rated full load.\n3. Why $N_r < N_s$: If the rotor ran at synchronous speed ($N_r = N_s$), the relative motion between rotor bars and magnetic field would become zero ($d\\Phi/dt = 0$). No EMF would be induced, zero rotor current would flow, and developed torque would drop to zero. The rotor must slip behind $N_s$ to produce torque.",
        "pitfall": "If $p$ is given as pole pairs $P$, the formula is $N_s = \\frac{60 f}{P}$. Always check whether the question specifies poles or pole pairs.",
        "mastered": False
    },

    # =========================================================================
    # CHAPTER 8: TRANSFORMERS
    # =========================================================================
    {
        "id": "CH08-01",
        "chapter": "Chapter 8",
        "topic": "Transformer Definition, Purpose & Structure",
        "level": "Level 1 (Concept)",
        "exam_reference": "Final Exam Problem 1.1 & 1.2 (Page 32)",
        "question": "What is an electrical transformer? What is its primary function and structure? Draw/describe its essential construction.",
        "formula": "Static machine transferring AC electrical energy via mutual induction.",
        "solution": "1. Definition & Purpose: A static electrical machine that transfers AC electrical power between circuits at the same frequency, stepping voltage up or down to minimize transmission loss or match load requirements.\n2. Structure: Consists of:\n- High-permeability laminated silicon steel core (provides closed magnetic circuit)\n- Primary winding ($N_1$ turns) connected to input AC source\n- Secondary winding ($N_2$ turns) connected to output load.",
        "pitfall": "A transformer changes voltage and current levels, but NEVER changes power frequency ($f_1 = f_2 = 50\\text{ Hz}$).",
        "mastered": False
    },
    {
        "id": "CH08-02",
        "chapter": "Chapter 8",
        "topic": "Working Principle & Induced EMF Equation",
        "level": "Level 1 (Concept)",
        "exam_reference": "Final Exam Problem 1.3 (Page 32)",
        "question": "Explain the working principle of a transformer and write Faraday's induced EMF formula including the derivation constant.",
        "formula": "$E_{\\text{rms}} = 4.44 f N \\Phi_m = \\sqrt{2}\\pi f N \\Phi_m$",
        "solution": "1. Working Principle: Mutual electromagnetic induction according to Faraday's law. When AC voltage $V_1$ is applied to the primary winding, it drives alternating current that establishes a time-varying magnetic flux $\\Phi(t) = \\Phi_m \\sin(\\omega t)$ in the core. This flux links both windings, inducing EMF $e_1 = -N_1 \\frac{d\\Phi}{dt}$ and $e_2 = -N_2 \\frac{d\\Phi}{dt}$.\n2. RMS EMF Equation: Since $\\frac{d}{dt}[\\sin(\\omega t)] = \\omega \\cos(\\omega t)$, peak value is $E_m = 2\\pi f N \\Phi_m$. Dividing by $\\sqrt{2}$ yields:\n$$E_{\\text{rms}} = \\frac{2\\pi}{\\sqrt{2}} f N \\Phi_m = \\sqrt{2}\\pi f N \\Phi_m = 4.44 f N \\Phi_m$$.",
        "pitfall": "Remember the constant 4.44 comes from $\\sqrt{2}\\pi \\approx 1.4142 \\times 3.1416 = 4.4428$.",
        "mastered": False
    },
    {
        "id": "CH08-03",
        "chapter": "Chapter 8",
        "topic": "Ideal Transformer 4 Essential Properties",
        "level": "Level 1 (Concept)",
        "exam_reference": "Final Exam Problem 1.4 (Page 32)",
        "question": "List the four fundamental assumptions/properties of an Ideal Transformer.",
        "formula": "1. Zero resistance, 2. Zero leakage, 3. Zero core loss, 4. Infinite permeability",
        "solution": "1. Zero winding resistance: $R_1 = 0, R_2 = 0$ (no $I^2R$ copper losses; $V_1 = E_1, V_2 = E_2$).\n2. Zero leakage flux: All magnetic flux is completely confined within the core and links 100% of both primary and secondary windings ($L_1 = 0, L_2 = 0$).\n3. Zero core loss: No hysteresis loss and no eddy current loss in the core ($P_{\\text{core}} = 0$, efficiency $\\eta = 100\\%$).\n4. Infinite core permeability: $\\mu_r \\to \\infty$, meaning zero magnetizing current is required to establish core flux.",
        "pitfall": "Direct 2-point exam question! Make sure to list all 4 properties clearly.",
        "mastered": False
    },
    {
        "id": "CH08-04",
        "chapter": "Chapter 8",
        "topic": "Power Losses in a Practical Transformer",
        "level": "Level 1 (Concept)",
        "exam_reference": "Final Exam Problem 1.5 (Page 32)",
        "question": "What types of power losses occur in a real transformer? Name the 2 primary loss categories and where they occur.",
        "formula": "$P_{\\text{loss}} = P_{\\text{copper}} + P_{\\text{core}} = (I_1^2 R_1 + I_2^2 R_2) + (P_h + P_e)$",
        "solution": "1. Copper Losses (Winding Losses): Occur in the copper windings due to Joule heating: $P_{\\text{cu}} = I_1^2 R_1 + I_2^2 R_2$. Variable loss proportional to $(I_{\\text{load}})^2$.\n2. Core / Iron Losses: Occur in the magnetic core, nearly constant at all load levels:\n- Hysteresis Loss: Energy lost in continuously reversing magnetic domains ($P_h \\propto f B_m^{1.6}$).\n- Eddy Current Loss: Circulating currents induced in the conductive iron core ($P_e \\propto f^2 B_m^2 t^2$). Minimized by using thin laminated sheets insulated by varnish.",
        "pitfall": "Core loss depends on voltage and frequency (constant 24/7); copper loss depends on load current squared.",
        "mastered": False
    },
    {
        "id": "CH08-05",
        "chapter": "Chapter 8",
        "topic": "Step-Down Transformer Parameter Calculation",
        "level": "Level 2 (Past Exam / Calc)",
        "exam_reference": "Final Exam Problem 1.6 (Page 31)",
        "question": "A single-phase transformer rated at $25\\text{ kVA}, 50\\text{ Hz}$ has primary winding $N_1 = 500\\text{ turns}$ and secondary winding $N_2 = 50\\text{ turns}$. The primary winding is connected to $V_1 = 3,000\\text{ V}$. Calculate: (a) Turns ratio ($a$), (b) Full-load rated primary and secondary currents ($I_1, I_2$), (c) Induced secondary voltage ($V_2$), (d) Maximum magnetic flux in core ($\\Phi_m$).",
        "formula": "$a = N_1 / N_2$\n$I_1 = S / V_1, I_2 = S / V_2$\n$V_2 = V_1 / a$\n$\\Phi_m = \\frac{V_1}{4.44 f N_1}$",
        "solution": "(a) Turns Ratio:\n$$a = \\frac{N_1}{N_2} = \\frac{500}{50} = 10$$\n\n(b) Rated Full-Load Currents:\n$$I_1 = \\frac{S_{\\text{rated}}}{V_1} = \\frac{25,000}{3,000} = 8.33\\text{ A}$$\n$$I_2 = a \\times I_1 = 10 \\times 8.33 = 83.33\\text{ A}$$\n\n(c) Secondary Voltage:\n$$V_2 = \\frac{V_1}{a} = \\frac{3,000}{10} = 300\\text{ V}$$\n\n(d) Maximum Magnetic Flux:\n$$\\Phi_m = \\frac{V_1}{4.44 f N_1} = \\frac{3,000}{4.44 \\times 50 \\times 500} = \\frac{3,000}{111,000} = 0.0270\\text{ Wb} = 27.0\\text{ mWb}$$.",
        "pitfall": "Exact problem from past exam page 31 (12 points total)! Write all steps and units clearly ($A, V, Wb$).",
        "mastered": False
    },
    {
        "id": "CH08-06",
        "chapter": "Chapter 8",
        "topic": "DC Voltage Connection to Transformer Primary Hazard",
        "level": "Level 2 (Past Exam / Calc)",
        "exam_reference": "HW Ch.8 Problem 4 & Talui Homework Page 5",
        "question": "What happens if a DC voltage (e.g. 200 V DC) is connected to the primary winding of a transformer? What will the secondary voltage and current be?",
        "formula": "$v_2 = -N_2 \\frac{d\\Phi}{dt} = 0$, $I_1 = \\frac{V_{\\text{dc}}}{R_1}$ (catastrophic overcurrent)",
        "solution": "1. Secondary Voltage: $V_2 = 0\\text{ V}$. Because DC voltage creates static, time-invariant magnetic flux ($\\frac{d\\Phi}{dt} = 0$), no voltage is induced in the secondary winding.\n2. Primary Hazard: On DC, inductive reactance is zero ($X_L = 2\\pi f L = 0$ since $f = 0$). There is no counter-EMF to oppose the source. Primary current is limited solely by tiny copper wire resistance $R_1$: $I_1 = V_{\\text{dc}} / R_1 \\gg I_{\\text{rated}}$. The primary winding rapidly overheats and burns out.",
        "pitfall": "Exam favorite concept! Always state: 1) Secondary output is zero, and 2) Primary winding burns out.",
        "mastered": False
    },

    # =========================================================================
    # CHAPTER 9: POWER SYSTEMS & ENERGY CONSERVATION
    # =========================================================================
    {
        "id": "CH09-01",
        "chapter": "Chapter 9",
        "topic": "Structure of Electrical Power System & Voltage Levels",
        "level": "Level 1 (Concept)",
        "exam_reference": "Final Exam Problem 5.3 (Page 25)",
        "question": "State the four stages of a power system and classify these standard Thai grid voltages: 500 kV, 22 kV, 380 V, and residential household voltage.",
        "formula": "Generation -> Transmission -> Distribution -> Utilization",
        "solution": "1. Generation: 10 - 20 kV (alternator terminals)\n2. Transmission: 115 kV, 230 kV, 500 kV\n3. Distribution: 22 kV, 24 kV, 33 kV\n4. Utilization: 380/400 V ($3\\phi$) and 220/230 V ($1\\phi$)\n\nClassifications for Exam Problem 5.3:\n- 500 kV: Extra High Voltage (EHV)\n- 22 kV: Medium Voltage (MV)\n- 380 V: Low / Utilization Voltage\n- Residential Household Voltage: 220 V (or modern 230 V).",
        "pitfall": "Why transmit at Extra High Voltage (500 kV)? Because $P = \\sqrt{3}V_L I_L \\cos\\theta$. Stepping up $V$ reduces line current $I$ proportionally, minimizing $I^2 R$ transmission wire loss by $(1/a)^2$.",
        "mastered": False
    },
    {
        "id": "CH09-02",
        "chapter": "Chapter 9",
        "topic": "Three Electricity Authorities in Thailand & Roles",
        "level": "Level 1 (Concept)",
        "exam_reference": "Lecture Slides & Jele Formula Sheet",
        "question": "Name the three state electricity authorities in Thailand and state their specific geographic responsibilities.",
        "formula": "EGAT (Generation/Transmission) | MEA (BKK+2) | PEA (74 Provinces)",
        "solution": "1. EGAT (Electricity Generating Authority of Thailand / กฟผ.): Responsible for power generation and nationwide high-voltage transmission grid (115-500 kV); sells wholesale power to MEA, PEA, and industrial direct clients.\n2. MEA (Metropolitan Electricity Authority / กฟน.): Distributes electricity in 3 central provinces: Bangkok, Nonthaburi, and Samut Prakan.\n3. PEA (Provincial Electricity Authority / กฟภ.): Distributes electricity across the remaining 74 provinces in Thailand.",
        "pitfall": "Guaranteed exam question! Remember MEA covers strictly Bangkok, Nonthaburi, and Samut Prakan.",
        "mastered": False
    },
    {
        "id": "CH09-03",
        "chapter": "Chapter 9",
        "topic": "Fuel Mix for Power Generation in Thailand",
        "level": "Level 1 (Concept)",
        "exam_reference": "Final Exam Problem 5.1 (Page 25)",
        "question": "What is the most widely used fuel source for electricity generation in Thailand, and what fuel source is used least?",
        "formula": "Most: Natural Gas (~55-60%) | Least: Fuel Oil / Heavy Fuel Oil",
        "solution": "- Most used: Natural Gas (ก๊าซธรรมชาติ) accounts for over 55-60% of total electrical energy in Thailand (Gulf of Thailand, Myanmar, and imported LNG).\n- Followed by: Coal / Lignite (Mae Moh power plant) and Renewable/Hydro imports from Lao PDR.\n- Least used: Heavy fuel oil (น้ำมันเตา) and diesel, due to extremely high operating costs and environmental impact.",
        "pitfall": "Do not answer solar or oil as the main source; it is overwhelmingly Natural Gas.",
        "mastered": False
    },
    {
        "id": "CH09-04",
        "chapter": "Chapter 9",
        "topic": "Base Load vs Peak Load Power Plants & Startup Times",
        "level": "Level 1 (Concept)",
        "exam_reference": "Final Exam Problem 5.2 (Page 25)",
        "question": "Compare Base Load and Peak Load power plants. Which plant type has the shortest startup time, and which has the longest?",
        "formula": "Base Load: Steam/Coal (6-8 hrs) | Peak Load: Hydro (<5 mins)",
        "solution": "1. Base Load Plants: Run continuously 24/7 to supply minimum baseline grid demand. High capital cost, low running cost.\n- Longest Startup Time: Steam thermal power plants (e.g. Mae Moh coal/lignite) take 6 - 8 hours to bring boilers up to operating pressure from cold start.\n\n2. Peak Load Plants: Dispatched quickly to handle rapid spikes in daily demand.\n- Shortest Startup Time: Hydroelectric power plants (โรงไฟฟ้าพลังน้ำ) can synchronize and deliver full load in less than 5 minutes. Gas turbines take 10 - 15 minutes.",
        "pitfall": "Direct 4-part exam question: Shortest = Hydro; Longest = Steam; Base = Steam/Coal; Peak = Hydro/Gas turbine.",
        "mastered": False
    },
    {
        "id": "CH09-05",
        "chapter": "Chapter 9",
        "topic": "Energy Conservation in Households and Industry",
        "level": "Level 1 (Concept)",
        "exam_reference": "Final Exam Problem 5.5 & 5.6 (Page 24)",
        "question": "State 2 practical methods to save electrical energy when using a household washing machine, and 3 methods to save energy in an industrial factory.",
        "formula": "Efficiency = Doing more work with less energy consumption",
        "solution": "1. Household Washing Machine (2 methods):\n- Wash full loads: Consolidate laundry to run at rated capacity rather than multiple partial loads.\n- Avoid hot water heating: Use cold water wash whenever possible (heating water consumes 80-90% of washer electricity).\n- Air dry clothing instead of using electric tumble dryers.\n\n2. Industrial Factory (3 methods):\n- Load scheduling: Shift non-essential high-power operations to Off-Peak tariff periods (TOU rate).\n- Transformer consolidation: De-energize or combine lightly loaded transformers to eliminate no-load core losses.\n- Voltage optimization & Power Factor correction: Install capacitor banks to raise PF $\\ge 0.95$, reducing line currents, $I^2R$ losses, and reactive power penalty fees.",
        "pitfall": "Direct 5-point exam question from page 24!",
        "mastered": False
    },

    # =========================================================================
    # CHAPTER 10: MEASURING INSTRUMENTS
    # =========================================================================
    {
        "id": "CH10-01",
        "chapter": "Chapter 10",
        "topic": "PMMC / Galvanometer Working Principle & Deflection Torque",
        "level": "Level 1 (Concept)",
        "exam_reference": "HW Ch.10 Problem 1 & Final Exam Problem 3.1",
        "question": "Explain the working principle of a PMMC (Permanent Magnet Moving Coil) instrument. State the deflecting torque formula and deflection angle relation.",
        "formula": "$T_d = B A N I = B I L d N$\n$T_c = K \\theta \\implies \\theta = \\frac{B A N}{K} I$",
        "solution": "1. Principle: Motor principle (Lorentz force). When current $I$ flows through the moving coil situated in the permanent magnetic field, a deflecting torque $T_d$ is exerted on the coil sides.\n2. Deflecting Torque: $T_d = B A N I$, where $B$ = magnetic flux density (T), $A$ = coil area ($m^2$), $N$ = turns, $I$ = current (A).\n3. Controlling Torque: Opposed by hair springs: $T_c = K \\theta$.\n4. Steady-State Deflection: At balance ($T_d = T_c$):\n$$\\theta = \\left(\\frac{B A N}{K}\\right) I$$\nDeflection $\\theta$ is linearly proportional to current $I$, giving PMMC a perfectly UNIFORM (linear) scale.",
        "pitfall": "PMMC responds strictly to DC average current. If pure sinusoidal AC is applied, average torque is zero and pointer merely vibrates around zero.",
        "mastered": False
    },
    {
        "id": "CH10-02",
        "chapter": "Chapter 10",
        "topic": "PMMC Torque & Deflection Calculation",
        "level": "Level 2 (Past Exam / Calc)",
        "exam_reference": "HW Ch.10 Problem 1 & Talui Homework Page 6",
        "question": "A moving-coil instrument has $N = 150\\text{ turns}$, coil area $A = 100\\text{ mm}^2$, air gap flux density $B = 0.15\\text{ T}$, and current $I = 5\\text{ mA}$. Spring constant $K = 2 \\times 10^{-6}\\text{ N}\\cdot\\text{m/deg}$. Calculate: (1) Deflecting torque ($T_d$), (2) Deflection angle ($\\theta$ in degrees and radians).",
        "formula": "$T_d = N B A I$\n$\\theta = T_d / K$",
        "solution": "1. Deflecting Torque:\n$A = 100\\text{ mm}^2 = 100 \\times 10^{-6}\\text{ m}^2 = 10^{-4}\\text{ m}^2$\n$$T_d = 150 \\times 0.15 \\times (100 \\times 10^{-6}) \\times (5 \\times 10^{-3}) = 1.125 \\times 10^{-5}\\text{ N}\\cdot\\text{m}$$\n\n2. Deflection Angle:\n$$\\theta = \\frac{T_d}{K} = \\frac{1.125 \\times 10^{-5}}{2 \\times 10^{-6}} = 5.625^\\circ$$\nIn radians:\n$$\\theta = 5.625 \\times \\frac{\\pi}{180} = 0.0982\\text{ rad}$$.",
        "pitfall": "Always convert coil area from $\\text{mm}^2$ to $\\text{m}^2$ by multiplying by $10^{-6}$! Never forget this conversion.",
        "mastered": False
    },
    {
        "id": "CH10-03",
        "chapter": "Chapter 10",
        "topic": "DC Ammeter Design with and without CDRX",
        "level": "Level 2 (Past Exam / Calc)",
        "exam_reference": "HW Ch.10 Problem 2 & Talui Homework Page 6",
        "question": "Design a DC ammeter with full scale $I = 100\\text{ mA}$ using a galvanometer with $I_g = 10\\text{ mA}$ and $R_g = 50\\ \\Omega$. Calculate shunt resistor $R_s$: (a) Without damping resistor, (b) With critical damping resistor CDRX = $400\\ \\Omega$ connected in series with coil.",
        "formula": "(a) $R_s = \\frac{I_g R_g}{I - I_g}$\n(b) $R_s = \\frac{I_g (R_g + \\text{CDRX})}{I - I_g}$",
        "solution": "(a) Without CDRX:\n$$R_s = \\frac{10\\text{ mA} \\times 50\\ \\Omega}{100\\text{ mA} - 10\\text{ mA}} = \\frac{0.5\\text{ V}}{0.09\\text{ A}} = 5.56\\ \\Omega$$\n\n(b) With CDRX = $400\\ \\Omega$ (connected in series with $R_g$):\nTotal meter branch resistance $R_{\\text{branch}} = R_g + \\text{CDRX} = 50 + 400 = 450\\ \\Omega$\n$$R_s = \\frac{I_g(R_g + \\text{CDRX})}{I - I_g} = \\frac{10\\text{ mA} \\times 450\\ \\Omega}{90\\text{ mA}} = \\frac{4.5\\text{ V}}{0.09\\text{ A}} = 50.0\\ \\Omega$$.",
        "pitfall": "In a DC ammeter, CDRX is connected in SERIES with the moving coil inside the meter branch; the shunt $R_s$ is in parallel with that entire branch.",
        "mastered": False
    },
    {
        "id": "CH10-04",
        "chapter": "Chapter 10",
        "topic": "DC Voltmeter Design with and without CDRX",
        "level": "Level 2 (Past Exam / Calc)",
        "exam_reference": "HW Ch.10 Problem 3 & Talui Homework Page 7",
        "question": "Design a DC voltmeter with full scale $V = 50\\text{ V}$ using a galvanometer with $I_g = 10\\text{ mA}$ and $R_g = 50\\ \\Omega$. Calculate series multiplier $R_s$: (a) Without damping resistor, (b) With critical damping resistor CDRX = $400\\ \\Omega$ connected in parallel across the coil.",
        "formula": "(a) $R_s = \\frac{V}{I_g} - R_g$\n(b) $R_s = \\frac{V - I_g R_g}{I_g + I_{\\text{cdrx}}}$",
        "solution": "(a) Without CDRX:\n$$R_s = \\frac{V}{I_g} - R_g = \\frac{50}{0.010} - 50 = 5,000 - 50 = 4,950\\ \\Omega$$\n\n(b) With CDRX = $400\\ \\Omega$ (connected in PARALLEL across the coil):\n- Voltage across coil at FSD: $V_g = I_g R_g = 10\\text{ mA} \\times 50\\ \\Omega = 0.5\\text{ V}$\n- Current through CDRX: $I_{\\text{cdrx}} = V_g / \\text{CDRX} = 0.5 / 400 = 1.25\\text{ mA}$\n- Total circuit current: $I_{\\text{tot}} = I_g + I_{\\text{cdrx}} = 10\\text{ mA} + 1.25\\text{ mA} = 11.25\\text{ mA}$\n- Required series multiplier:\n$$R_s = \\frac{V - V_g}{I_{\\text{tot}}} = \\frac{50 - 0.5}{0.01125} = \\frac{49.5}{0.01125} = 4,400\\ \\Omega$$\n*(Or via handwritten approach: $R_s = \\frac{50 - 0.5}{10\\text{ mA} + 1.25\\text{ mA}} = 4,400\\ \\Omega$)*.",
        "pitfall": "In a voltmeter, CDRX is placed in PARALLEL with the coil to damp oscillation, so the line must supply both coil current and CDRX current!",
        "mastered": False
    },
    {
        "id": "CH10-05",
        "chapter": "Chapter 10",
        "topic": "Multi-Range DC Ammeter Design with CDRX",
        "level": "Level 2 (Past Exam / Calc)",
        "exam_reference": "Final Exam Problem 3.5 (Page 29 - 12 Points)",
        "question": "Design a multi-range DC ammeter with ranges $I_1 = 1\\text{ mA}$, $I_2 = 50\\text{ mA}$, and $I_3 = 1\\text{ A}$ using a galvanometer with internal resistance $R_g = 100\\ \\Omega$, full-scale deflection current $I_g = 1\\ \\mu\\text{A}$, and damping resistor $\\text{CDRX} = 400\\ \\Omega$ in series with coil. Find shunt resistors $R_1, R_2, R_3$.",
        "formula": "$R_{\\text{branch}} = R_g + \\text{CDRX} = 500\\ \\Omega$\n$V_{\\text{branch}} = I_g \\times R_{\\text{branch}} = 1\\ \\mu\\text{A} \\times 500\\ \\Omega = 500\\ \\mu\\text{V} = 5 \\times 10^{-4}\\text{ V}$\n$R_s = \\frac{V_{\\text{branch}}}{I - I_g}$",
        "solution": "Total meter branch resistance: $R_{\\text{branch}} = 100 + 400 = 500\\ \\Omega$.\nBranch voltage at FSD: $V_m = 1\\times 10^{-6}\\text{ A} \\times 500\\ \\Omega = 5\\times 10^{-4}\\text{ V}$ ($0.5\\text{ mV}$).\n\n1. Range 1 ($I = 1\\text{ mA} = 10^{-3}\\text{ A}$):\n$$R_1 = \\frac{5 \\times 10^{-4}\\text{ V}}{10^{-3} - 10^{-6}} \\approx \\frac{5\\times 10^{-4}}{10^{-3}} = 0.5\\ \\Omega$$\n\n2. Range 2 ($I = 50\\text{ mA} = 50 \\times 10^{-3}\\text{ A}$):\n$$R_2 = \\frac{5 \\times 10^{-4}\\text{ V}}{50 \\times 10^{-3}} = 0.01\\ \\Omega$\n\n3. Range 3 ($I = 1\\text{ A}$):\n$$R_3 = \\frac{5 \\times 10^{-4}\\text{ V}}{1\\text{ A}} = 5 \\times 10^{-4}\\ \\Omega = 0.0005\\ \\Omega = 0.5\\text{ m}\\Omega$$.",
        "pitfall": "Exact 12-point exam problem! As measurement range increases, the required shunt resistance decreases proportionally.",
        "mastered": False
    },
    {
        "id": "CH10-06",
        "chapter": "Chapter 10",
        "topic": "Rectifier AC Voltmeter & Wattmeter Connection",
        "level": "Level 1 (Concept)",
        "exam_reference": "Final Exam Problem 3.2 & 3.4 (Page 30)",
        "question": "1. What is the operating principle of a Rectifier AC Voltmeter?\n2. In a Wattmeter, how must the current coil and potential coil be connected to measure load power?",
        "formula": "Rectifier converts AC to DC for PMMC. Current coil in series, Potential coil in parallel.",
        "solution": "1. Rectifier AC Voltmeter: Uses diode rectifiers (half-wave or full-wave bridge) to convert alternating voltage into unidirectional pulsating DC, which is then measured by a sensitive PMMC movement. The scale is calibrated to indicate RMS value (multiplying average by form factor $1.11$ for sine waves).\n\n2. Wattmeter Connection (Problem 3.4):\n- Current Coil (Terminals 1-2): Must be connected in SERIES with the load to carry full load current.\n- Potential / Voltage Coil (Terminals 3-5): Must be connected in PARALLEL across the load to sense load voltage.",
        "pitfall": "Never connect the current coil in parallel (it will cause a dead short circuit!) and never connect the voltage coil in series.",
        "mastered": False
    },
    {
        "id": "CH10-07",
        "chapter": "Chapter 10",
        "topic": "Energy Meter (Kilowatt-Hour Meter) Function",
        "level": "Level 1 (Concept)",
        "exam_reference": "Final Exam Problem 3.3 (Page 30)",
        "question": "What is an induction-type Energy Meter (Watt-hour meter) and what physical quantity and unit does it measure?",
        "formula": "$\\text{Energy} = \\int P(t) dt\\quad [\\text{kW}\\cdot\\text{h}]$",
        "solution": "1. Purpose: An integrating instrument that measures total electrical energy consumed over a period of time, commonly used by MEA/PEA for customer billing.\n2. Quantity & Unit: Measures active electrical energy in units of Kilowatt-hours ($\\text{kW}\\cdot\\text{h}$ or 'units').\n3. Principle: Eddy current induction motor principle driving a rotating aluminum disk geared to a register counter.",
        "pitfall": "A wattmeter measures instantaneous Power ($W$), while an energy meter measures cumulative Energy ($W \\cdot h$ or $kW \\cdot h$). Do not confuse the two!",
        "mastered": False
    },

    # =========================================================================
    # CHAPTER 11 / SUPPLEMENT: SEMICONDUCTOR DEVICES
    # =========================================================================
    {
        "id": "SEMI-01",
        "chapter": "Semiconductors",
        "topic": "Intrinsic vs Extrinsic, N-Type vs P-Type Semiconductors",
        "level": "Level 1 (Concept)",
        "exam_reference": "Final Exam Problem 4.a (Page 24)",
        "question": "Explain the difference between Intrinsic and Extrinsic semiconductors. Compare N-type and P-type semiconductors in terms of dopants and majority carriers.",
        "formula": "N-type: Group V dopant (electrons) | P-type: Group III dopant (holes)",
        "solution": "1. Intrinsic Semiconductor: Chemically pure semiconductor (e.g. pure Silicon Si, Germanium Ge) with equal concentrations of free electrons and holes ($n = p = n_i$). Very low electrical conductivity at room temperature.\n2. Extrinsic Semiconductor: Doped with impurity atoms to dramatically enhance conductivity:\n- N-type: Pure Si doped with Pentavalent atoms (Group V: Phosphorus P, Arsenic As, Antimony Sb with 5 valence electrons). Majority carriers = Electrons; Minority carriers = Holes.\n- P-type: Pure Si doped with Trivalent atoms (Group III: Boron B, Gallium Ga, Indium In with 3 valence electrons). Majority carriers = Holes; Minority carriers = Electrons.",
        "pitfall": "Exact 2-point exam question from page 24! Memory aid: P in Pentavalent gives Negative electrons; T in Trivalent gives Positive holes.",
        "mastered": False
    },
    {
        "id": "SEMI-02",
        "chapter": "Semiconductors",
        "topic": "MOSFET Definition, Properties & Uses",
        "level": "Level 1 (Concept)",
        "exam_reference": "Final Exam Problem 4.b (Page 24)",
        "question": "What is a MOSFET? State its essential electrical characteristics and its primary application/advantage in electronic circuits.",
        "formula": "Metal-Oxide-Semiconductor Field-Effect Transistor (Voltage-controlled)",
        "solution": "1. Definition: Metal-Oxide-Semiconductor Field-Effect Transistor, a unipolar transistor where current transport involves only majority carriers.\n2. Characteristics: Voltage-controlled device with extremely high input impedance ($10^{10} - 10^{15}\\ \\Omega$) due to the insulating $SiO_2$ gate oxide layer. Gate draws virtually zero DC current ($I_G \\approx 0$).\n3. Application / Benefit: Uses gate electric field to modulate and control current flow between Drain and Source. Widely used for high-speed switching, microprocessors (CMOS), and power converters.",
        "pitfall": "Exact question from page 24: State that it is a unipolar transistor whose output current is controlled by an electric field / voltage.",
        "mastered": False
    },
    {
        "id": "SEMI-03",
        "chapter": "Semiconductors",
        "topic": "Integrated Circuit (IC) Definition & Significance",
        "level": "Level 1 (Concept)",
        "exam_reference": "Final Exam Problem 4.c (Page 24)",
        "question": "What is an Integrated Circuit (IC)? What is its main function and significance in modern electronics?",
        "formula": "Microchip integrating transistors, diodes, resistors on single silicon die",
        "solution": "1. Definition: A miniaturized electronic circuit consisting of thousands to billions of interconnected semiconductor devices (transistors, diodes, resistors, capacitors) fabricated on a single tiny substrate of semiconductor material (silicon wafer).\n2. Significance: Enables massive reduction in physical size, weight, and power consumption, while offering dramatic improvements in reliability, operating speed, and mass-production cost.",
        "pitfall": "Exact 1-point question from past exam page 24.",
        "mastered": False
    },
    {
        "id": "SEMI-04",
        "chapter": "Semiconductors",
        "topic": "PN Junction Diode Biasing & Knee Voltages",
        "level": "Level 1 (Concept)",
        "exam_reference": "Lecture Slides Ch.11 & Jele Formula Sheet",
        "question": "Compare Forward Bias and Reverse Bias in a PN junction diode. State the barrier potential (knee voltage) values for Silicon (Si) and Germanium (Ge).",
        "formula": "Forward: P to +, N to - (conduction) | Reverse: P to -, N to + (blocking)\n$V_k(\\text{Si}) = 0.7\\text{ V}, V_k(\\text{Ge}) = 0.3\\text{ V}$",
        "solution": "1. Forward Bias: External positive connected to P-side (anode), negative to N-side (cathode). Overcomes internal barrier, depletion width shrinks, and heavy forward current flows once applied voltage exceeds knee voltage.\n2. Reverse Bias: Positive to N-side, negative to P-side. Depletion layer widens, blocking current except for tiny temperature-dependent reverse saturation leakage current ($I_0$).\n3. Knee Voltages:\n- Silicon (Si): $V_{\\text{knee}} = 0.7\\text{ V}$\n- Germanium (Ge): $V_{\\text{knee}} = 0.3\\text{ V}$.",
        "pitfall": "In almost all circuit analysis, Silicon diode forward voltage drop is taken as 0.7 V.",
        "mastered": False
    },
    {
        "id": "SEMI-05",
        "chapter": "Semiconductors",
        "topic": "BJT Transistor Terminal Currents & Gain Relations",
        "level": "Level 1 (Concept)",
        "exam_reference": "Lecture Slides Ch.11 & Jele Formula Sheet",
        "question": "State the fundamental KCL current relationship between Emitter ($I_e$), Collector ($I_c$), and Base ($I_b$) currents in a BJT, and the relationships with current gains $\\beta$ and $\\alpha$.",
        "formula": "$I_e = I_c + I_b$\n$I_c = \\beta I_b$\n$\\alpha = \\frac{\\beta}{\\beta + 1} = \\frac{I_c}{I_e}$",
        "solution": "1. Terminal Current Law (KCL): Emitter current is the sum of collector and base currents:\n$$I_e = I_c + I_b$$\n2. Common-Emitter DC Current Gain ($\\beta$ or $h_{FE}$):\n$$I_c = \\beta I_b$$\nTypically $\\beta$ ranges from $50$ to $300$.\n3. Common-Base DC Current Gain ($\\alpha$):\n$$\\alpha = \\frac{I_c}{I_e} = \\frac{\\beta}{\\beta + 1}$$\nTypically $\\alpha \\approx 0.98 - 0.998$ (slightly less than 1.0).",
        "pitfall": "Because base current $I_b$ is tiny (typically $\\mu\\text{A}$), $I_e \\approx I_c$ in many rough approximations, but NEVER forget $I_e = I_c + I_b$ in exact KCL equations.",
        "mastered": False
    }
]

# Write to Excel with professional styling
excel_path = r'c:\Users\thana\Desktop\Private-Flashcard\FunE_Master_Exam_Flashcards_Ch6_10.xlsx'
df = pd.DataFrame(flashcards)

# Rename columns for clarity in Google Sheets
df_export = df[['id', 'chapter', 'topic', 'level', 'exam_reference', 'question', 'formula', 'solution', 'pitfall', 'mastered']]
df_export.columns = [
    'Card ID', 'Chapter', 'Topic', 'Level / Difficulty', 'Exam Reference', 
    'Question / Problem', 'Formula / Key Concept', 'Step-by-Step Solution', 'Pitfall / Pro Tip', 'Mastered'
]

# Write with openpyxl
wb = openpyxl.Workbook()
ws = wb.active
ws.title = "Flashcards"

# Headers
headers = list(df_export.columns)
ws.append(headers)

# Rows
for row in df_export.itertuples(index=False):
    ws.append(list(row))

# Styling
header_fill = PatternFill(start_color="1E293B", end_color="1E293B", fill_type="solid")
header_font = Font(name="Segoe UI", size=11, bold=True, color="FFFFFF")
thin_border = Border(
    left=Side(style='thin', color='E2E8F0'),
    right=Side(style='thin', color='E2E8F0'),
    top=Side(style='thin', color='E2E8F0'),
    bottom=Side(style='thin', color='E2E8F0')
)

ws.row_dimensions[1].height = 28
for col_num, cell in enumerate(ws[1], 1):
    cell.fill = header_fill
    cell.font = header_font
    cell.alignment = Alignment(horizontal="center", vertical="center")

for row_num in range(2, len(df_export) + 2):
    ws.row_dimensions[row_num].height = 70
    is_even = (row_num % 2 == 0)
    row_fill = PatternFill(start_color="F8FAFC" if is_even else "FFFFFF", fill_type="solid")
    
    for col_num, cell in enumerate(ws[row_num], 1):
        cell.fill = row_fill
        cell.border = thin_border
        cell.font = Font(name="Segoe UI", size=10)
        
        # Specific alignments
        if col_num in [1, 2, 4, 10]:
            cell.alignment = Alignment(horizontal="center", vertical="top", wrap_text=True)
        else:
            cell.alignment = Alignment(horizontal="left", vertical="top", wrap_text=True)

# Set Column Widths
col_widths = {
    'A': 12, # Card ID
    'B': 18, # Chapter
    'C': 26, # Topic
    'D': 22, # Level
    'E': 26, # Exam Reference
    'F': 42, # Question
    'G': 32, # Formula
    'H': 46, # Solution
    'I': 34, # Pitfall
    'J': 12  # Mastered
}

for col_letter, width in col_widths.items():
    ws.column_dimensions[col_letter].width = width

ws.freeze_panes = "A2"
wb.save(excel_path)
print(f"Successfully generated {len(flashcards)} flashcards to {excel_path}")

# Also update JSON and JS files
json_path = r'c:\Users\thana\Desktop\Private-Flashcard\data\flashcards.json'
js_path = r'c:\Users\thana\Desktop\Private-Flashcard\data\flashcards.js'

# Format for web app
web_cards = []
for c in flashcards:
    web_cards.append({
        "id": c["id"],
        "chapter": c["chapter"],
        "topic": c["topic"],
        "difficulty": c["level"],
        "exam_reference": c["exam_reference"],
        "question": c["question"],
        "hint": f"Key Formula: {c['formula'].splitlines()[0]}" if c["formula"] else "Click to flip card for answer",
        "answer": f"<p class='font-semibold text-blue-600 dark:text-blue-400 mb-1'>Formula / Principle:</p><p class='mb-2'>{c['formula']}</p><p class='font-semibold text-emerald-600 dark:text-emerald-400 mb-1'>Step-by-Step Solution:</p><div class='mb-3 leading-relaxed whitespace-pre-line'>{c['solution']}</div><p class='font-semibold text-amber-600 dark:text-amber-400 mb-1'>Pitfall / Pro Tip:</p><p class='italic text-slate-500 dark:text-slate-400'>{c['pitfall']}</p>"
    })

with open(json_path, 'w', encoding='utf-8') as f:
    json.dump(web_cards, f, ensure_ascii=False, indent=2)

with open(js_path, 'w', encoding='utf-8') as f:
    f.write("const FLASHCARDS_DATA = " + json.dumps(web_cards, ensure_ascii=False, indent=2) + ";\n")

print("Updated data/flashcards.json and data/flashcards.js")
