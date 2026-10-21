# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import os

out_dirs = [
    r"c:\Users\thana\Desktop\Private-Flashcard\images\ch08_guide",
    r"c:\Users\thana\Desktop\Fund E N'Manow\images\ch08_guide"
]
for d in out_dirs:
    os.makedirs(d, exist_ok=True)

# Configure Matplotlib to use Tahoma for Thai support on Windows
plt.rcParams['font.sans-serif'] = ['Tahoma', 'Microsoft Sans Serif', 'Arial']
plt.rcParams['axes.unicode_minus'] = False

# -------------------------------------------------------------
# 1. 4-LEVEL THAILAND POWER GRID FLOW SCHEMATIC
# -------------------------------------------------------------
fig, ax = plt.subplots(figsize=(11, 4.5), dpi=220)
ax.set_xlim(0, 11)
ax.set_ylim(0, 5)
ax.axis('off')
fig.patch.set_facecolor('#ffffff')

# Header
ax.text(5.5, 4.7, 'The 4 Levels of Thailand Electrical Power System (EGAT, MEA, PEA)', 
        ha='center', va='center', fontsize=12.5, fontweight='bold', color='#0f172a')

# 4 Stage Boxes
boxes_data = [
    (0.4, '1. GENERATION\n(โรงไฟฟ้า กฟผ. / IPP)', '10 - 20 kV\nHydro, Thermal, Gas,\nCombined Cycle, Solar', '#dbeafe', '#1e40af'),
    (3.0, '2. TRANSMISSION\n(สายส่งกำลัง กฟผ.)', '500 kV, 230 kV\n115 kV, 69 kV\nOverhead Steel Towers', '#fef3c7', '#b45309'),
    (5.8, '3. DISTRIBUTION\n(จำหน่าย กฟน. / กฟภ.)', 'กฟน. (MEA): 24 / 12 kV\nกฟภ. (PEA): 22 / 33 kV\nSubstations & Feeders', '#ecfdf5', '#047857'),
    (8.6, '4. UTILIZATION\n(ผู้ใช้ไฟฟ้าแรงต่ำ)', '3-Phase: 400 / 230 V\n1-Phase: 230 V\nบ้านพักอาศัย / อาคาร', '#f5f3ff', '#6d28d9')
]

for x, title, sub, bg, border in boxes_data:
    rect = patches.FancyBboxPatch((x, 1.2), 2.2, 3.0, boxstyle='round,pad=0.15', facecolor=bg, edgecolor=border, lw=2)
    ax.add_patch(rect)
    ax.text(x + 1.1, 3.6, title, ha='center', va='center', fontsize=9.5, fontweight='bold', color=border)
    ax.text(x + 1.1, 2.3, sub, ha='center', va='center', fontsize=8.2, color='#1e293b', linespacing=1.4)

# Arrows between stages
for arr_x in [2.65, 5.35, 8.15]:
    ax.annotate('', xy=(arr_x + 0.3, 2.7), xytext=(arr_x - 0.05, 2.7),
                arrowprops=dict(arrowstyle="->,head_width=0.4,head_length=0.6", lw=2.5, color='#475569'))

# Transformation labels under arrows
ax.text(2.78, 2.2, 'Step-Up\nTransformer', ha='center', va='center', fontsize=7.5, fontweight='bold', color='#475569')
ax.text(5.48, 2.2, 'Step-Down\nMain Sub.', ha='center', va='center', fontsize=7.5, fontweight='bold', color='#475569')
ax.text(8.28, 2.2, 'Distribution\nTransformer', ha='center', va='center', fontsize=7.5, fontweight='bold', color='#475569')

# Bottom Key Formula
ax.text(5.5, 0.45, r'$\mathrm{Why\ High\ Voltage?}\quad I_L = \frac{P}{\sqrt{3} V_L \cos\theta} \quad \rightarrow \quad P_{\mathrm{loss}} = 3 I_L^2 R_{\mathrm{line}} \propto \frac{1}{V_L^2} \quad (\mathrm{Increase\ } V \times 5 \rightarrow \mathrm{Loss\ drops\ } 25 \times!)$',
        ha='center', va='center', fontsize=9.5, fontweight='bold', color='#0f172a',
        bbox=dict(boxstyle='round,pad=0.35', facecolor='#f1f5f9', edgecolor='#cbd5e1'))

for d in out_dirs:
    fig.savefig(os.path.join(d, 'thailand_power_system_4_levels_schematic.png'), dpi=220, bbox_inches='tight')
plt.close()
print("Saved 4 levels schematic!")

# -------------------------------------------------------------
# 2. CONSUMER METERING & CONNECTION MODES SCHEMATIC
# -------------------------------------------------------------
fig, ax = plt.subplots(figsize=(11, 4.5), dpi=220)
ax.set_xlim(0, 11)
ax.set_ylim(0, 5)
ax.axis('off')
fig.patch.set_facecolor('#ffffff')

ax.text(5.5, 4.7, 'Electricity Consumer Connection & Metering Classifications', 
        ha='center', va='center', fontsize=12.5, fontweight='bold', color='#0f172a')

# Left Box: Low Voltage
rect_lv = patches.FancyBboxPatch((0.5, 0.8), 4.6, 3.5, boxstyle='round,pad=0.15', facecolor='#f8fafc', edgecolor='#3b82f6', lw=2)
ax.add_patch(rect_lv)
ax.text(2.8, 3.9, '1. Low Voltage Customers (ผู้ใช้ไฟแรงต่ำ)', ha='center', va='center', fontsize=10, fontweight='bold', color='#1d4ed8')
ax.text(2.8, 2.3, 
        '• 1-Phase 2-Wire: 230 V (บ้านพักอาศัยทั่วไป)\n'
        '  - ขนาดมิเตอร์: 5(15)A, 15(45)A, 30(100)A, 50(150)A\n'
        '  - ต่อไฟตรงผ่าน Watt-hour Meter ของ กฟน./กฟภ.\n'
        '• 3-Phase 4-Wire: 400/230 V (อาคารพาณิชย์/หอพัก/อพาร์ตเมนต์)\n'
        '  - โหลดเกิน 10 kW หรือมีแอร์/มอเตอร์ 3 เฟส\n'
        '  - ถ้ากระแส > 100A ต้องใช้ CT Metering (หม้อแปลงกระแส)',
        ha='center', va='center', fontsize=8.2, color='#1e293b', linespacing=1.45)

# Right Box: Medium Voltage
rect_mv = patches.FancyBboxPatch((5.9, 0.8), 4.6, 3.5, boxstyle='round,pad=0.15', facecolor='#fffbeb', edgecolor='#d97706', lw=2)
ax.add_patch(rect_mv)
ax.text(8.2, 3.9, '2. Medium Voltage Customers (ผู้ใช้ไฟแรงปานกลาง)', ha='center', va='center', fontsize=10, fontweight='bold', color='#b45309')
ax.text(8.2, 2.3, 
        '• โรงงานอุตสาหกรรม, ห้างสรรพสินค้า, โรงพยาบาล, มหาวิทยาลัย\n'
        '• รับไฟที่ระดับ 24 kV (MEA) หรือ 22 kV / 33 kV (PEA)\n'
        '• รูปแบบที่ 1: ติดตั้งหม้อแปลงของผู้ใช้ไฟเอง (Customer Substation)\n'
        '  - มี CT/PT Metering วัดด้านแรงสูง คิดค่าไฟอัตรา TOU\n'
        '• รูปแบบที่ 2: เชื่อมต่อด้วยสายใต้ดิน (Underground Cable System)\n'
        '  - ใช้ Riser Pole & Cable Head ลงสู่สถานีสวิตช์เกียร์ภายใน',
        ha='center', va='center', fontsize=8.2, color='#1e293b', linespacing=1.45)

for d in out_dirs:
    fig.savefig(os.path.join(d, 'consumer_connection_types_schematic.png'), dpi=220, bbox_inches='tight')
plt.close()
print("Saved consumer connection schematic!")
