# -*- coding: utf-8 -*-
"""
generate_ch06_extra_diagrams.py
Creates crisp, professional schematic diagrams for:
1. Two-Wattmeter Method (W1 and W2 connections)
2. Power Factor Correction with Delta-connected Capacitor Bank
"""

import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
import os

out_dir = r"c:\Users\thana\Desktop\Private-Flashcard\images\ch06_guide"
os.makedirs(out_dir, exist_ok=True)

# -------------------------------------------------------------
# 1. TWO-WATTMETER METHOD SCHEMATIC
# -------------------------------------------------------------
fig, ax = plt.subplots(figsize=(10, 5.5), dpi=200)
ax.set_xlim(0, 10)
ax.set_ylim(0, 6)
ax.axis('off')

# Background
fig.patch.set_facecolor('#ffffff')

# Title
ax.text(5, 5.6, 'Two-Wattmeter Method for 3-Phase Power Measurement', 
        ha='center', va='center', fontsize=14, fontweight='bold', color='#0f172a')

# Source labels
ax.text(0.5, 4.5, 'Source\nPhase A', ha='center', va='center', fontsize=10, fontweight='bold', color='#1e3a8a')
ax.text(0.5, 3.0, 'Source\nPhase B', ha='center', va='center', fontsize=10, fontweight='bold', color='#1e3a8a')
ax.text(0.5, 1.5, 'Source\nPhase C', ha='center', va='center', fontsize=10, fontweight='bold', color='#1e3a8a')

# Lines A, B, C
# Line A
ax.plot([1.2, 2.8], [4.5, 4.5], color='#1e293b', lw=2)
# Current Coil 1 (W1)
rect_cc1 = patches.Rectangle((2.8, 4.2), 1.2, 0.6, facecolor='#dbeafe', edgecolor='#1e40af', lw=2)
ax.add_patch(rect_cc1)
ax.text(3.4, 4.5, 'CC 1', ha='center', va='center', fontsize=9, fontweight='bold', color='#1e40af')
ax.plot([4.0, 7.5], [4.5, 4.5], color='#1e293b', lw=2)
ax.text(2.0, 4.7, 'Ia →', fontsize=10, fontweight='bold', color='#b91c1c')

# Line B (Straight through)
ax.plot([1.2, 7.5], [3.0, 3.0], color='#1e293b', lw=2)
ax.text(2.0, 3.2, 'Ib →', fontsize=10, fontweight='bold', color='#b91c1c')

# Line C
ax.plot([1.2, 4.8], [1.5, 1.5], color='#1e293b', lw=2)
# Current Coil 2 (W2)
rect_cc2 = patches.Rectangle((4.8, 1.2), 1.2, 0.6, facecolor='#dbeafe', edgecolor='#1e40af', lw=2)
ax.add_patch(rect_cc2)
ax.text(5.4, 1.5, 'CC 2', ha='center', va='center', fontsize=9, fontweight='bold', color='#1e40af')
ax.plot([6.0, 7.5], [1.5, 1.5], color='#1e293b', lw=2)
ax.text(2.0, 1.7, 'Ic →', fontsize=10, fontweight='bold', color='#b91c1c')

# Potential Coils (PC1 and PC2)
# PC 1 (from Line A to Line B)
ax.plot([3.4, 3.4], [4.2, 3.8], color='#047857', lw=1.5, ls='--')
rect_pc1 = patches.Rectangle((3.1, 3.3), 0.6, 0.5, facecolor='#dcfce7', edgecolor='#047857', lw=1.5)
ax.add_patch(rect_pc1)
ax.text(3.4, 3.55, 'PC 1', ha='center', va='center', fontsize=8, fontweight='bold', color='#047857')
ax.plot([3.4, 3.4], [3.3, 3.0], color='#047857', lw=1.5, ls='--')
ax.plot(3.4, 3.0, 'o', color='#047857', markersize=5)
ax.text(2.5, 3.8, 'Vab', fontsize=10, fontweight='bold', color='#047857')

# Wattmeter 1 circle badge
circle1 = patches.Circle((3.4, 4.95), 0.35, facecolor='#3b82f6', edgecolor='#1d4ed8', lw=1.5)
ax.add_patch(circle1)
ax.text(3.4, 4.95, 'W1', ha='center', va='center', fontsize=9, fontweight='bold', color='#ffffff')

# PC 2 (from Line C to Line B)
ax.plot([5.4, 5.4], [1.8, 2.2], color='#047857', lw=1.5, ls='--')
rect_pc2 = patches.Rectangle((5.1, 2.2), 0.6, 0.5, facecolor='#dcfce7', edgecolor='#047857', lw=1.5)
ax.add_patch(rect_pc2)
ax.text(5.4, 2.45, 'PC 2', ha='center', va='center', fontsize=8, fontweight='bold', color='#047857')
ax.plot([5.4, 5.4], [2.7, 3.0], color='#047857', lw=1.5, ls='--')
ax.plot(5.4, 3.0, 'o', color='#047857', markersize=5)
ax.text(6.0, 2.2, 'Vcb', fontsize=10, fontweight='bold', color='#047857')

# Wattmeter 2 circle badge
circle2 = patches.Circle((5.4, 0.75), 0.35, facecolor='#3b82f6', edgecolor='#1d4ed8', lw=1.5)
ax.add_patch(circle2)
ax.text(5.4, 0.75, 'W2', ha='center', va='center', fontsize=9, fontweight='bold', color='#ffffff')

# Load Box
rect_load = patches.Rectangle((7.5, 1.0), 1.8, 4.0, facecolor='#f8fafc', edgecolor='#64748b', lw=2, ls='--')
ax.add_patch(rect_load)
ax.text(8.4, 3.0, '3-Phase\nBalanced\nor\nUnbalanced\nLoad', ha='center', va='center', fontsize=10, fontweight='bold', color='#334155')

# Key Formulas on plot
ax.text(5.0, 0.2, r'$P_{\mathrm{total}} = W_1 + W_2 \qquad Q_{\mathrm{total}} = \sqrt{3}(W_1 - W_2) \qquad \tan\theta = \sqrt{3}\frac{W_1 - W_2}{W_1 + W_2}$', 
        ha='center', va='center', fontsize=10, fontweight='bold', color='#0f172a',
        bbox=dict(boxstyle='round,pad=0.4', facecolor='#f1f5f9', edgecolor='#94a3b8'))

plt.tight_layout()
p1_path = os.path.join(out_dir, 'two_wattmeter_method_schematic.png')
plt.savefig(p1_path, dpi=200, bbox_inches='tight')
plt.close()
print('Saved', p1_path)

# -------------------------------------------------------------
# 2. POWER FACTOR CORRECTION WITH DELTA CAPACITOR BANK
# -------------------------------------------------------------
fig, ax = plt.subplots(figsize=(10, 5.5), dpi=200)
ax.set_xlim(0, 10)
ax.set_ylim(0, 6)
ax.axis('off')
fig.patch.set_facecolor('#ffffff')

ax.text(5, 5.6, 'Power Factor Correction using Delta-Connected Capacitors', 
        ha='center', va='center', fontsize=14, fontweight='bold', color='#0f172a')

# 3-Phase Supply
ax.plot([0.8, 3.5], [4.5, 4.5], color='#1e293b', lw=2)
ax.plot([0.8, 3.5], [3.0, 3.0], color='#1e293b', lw=2)
ax.plot([0.8, 3.5], [1.5, 1.5], color='#1e293b', lw=2)

ax.text(0.5, 4.5, 'Line A', ha='right', va='center', fontsize=10, fontweight='bold', color='#1e3a8a')
ax.text(0.5, 3.0, 'Line B', ha='right', va='center', fontsize=10, fontweight='bold', color='#1e3a8a')
ax.text(0.5, 1.5, 'Line C', ha='right', va='center', fontsize=10, fontweight='bold', color='#1e3a8a')

# T-junctions to Delta Capacitor Bank
ax.plot(3.5, 4.5, 'o', color='#1e293b', markersize=6)
ax.plot(3.5, 3.0, 'o', color='#1e293b', markersize=6)
ax.plot(3.5, 1.5, 'o', color='#1e293b', markersize=6)

# Lines continue to Load
ax.plot([3.5, 7.5], [4.5, 4.5], color='#1e293b', lw=2)
ax.plot([3.5, 7.5], [3.0, 3.0], color='#1e293b', lw=2)
ax.plot([3.5, 7.5], [1.5, 1.5], color='#1e293b', lw=2)

# Inductive Motor Load Box
rect_motor = patches.Rectangle((7.5, 1.0), 1.8, 4.0, facecolor='#fef3c7', edgecolor='#d97706', lw=2)
ax.add_patch(rect_motor)
ax.text(8.4, 3.0, 'Inductive\nLoad (Motors)\n\n$P, \\; Q_{\\mathrm{old}}$\n$\\mathrm{pf}_1 = \\cos\\theta_1$\n(Lagging)', 
        ha='center', va='center', fontsize=9.5, fontweight='bold', color='#92400e')

# Delta Capacitor Box
rect_cap_box = patches.Rectangle((3.8, 1.0), 2.8, 4.0, facecolor='#ecfdf5', edgecolor='#059669', lw=2, ls='--')
ax.add_patch(rect_cap_box)
ax.text(5.2, 4.7, 'Delta Capacitor Bank', ha='center', va='center', fontsize=10, fontweight='bold', color='#047857')

# Delta connection inside
# Node A_cap (4.5, 4.0), Node B_cap (4.5, 2.0), Node C_cap (5.9, 3.0)
ax.plot([3.5, 4.5], [4.5, 4.0], color='#047857', lw=1.5)
ax.plot([3.5, 4.5], [3.0, 2.2], color='#047857', lw=1.5)
ax.plot([3.5, 5.9], [1.5, 1.5], color='#047857', lw=1.5)
ax.plot([5.9, 5.9], [1.5, 3.0], color='#047857', lw=1.5)

# C1 between A and B
ax.plot([4.5, 4.5], [4.0, 3.3], color='#047857', lw=1.5)
ax.plot([4.2, 4.8], [3.3, 3.3], color='#047857', lw=2)
ax.plot([4.2, 4.8], [3.1, 3.1], color='#047857', lw=2)
ax.plot([4.5, 4.5], [3.1, 2.2], color='#047857', lw=1.5)
ax.text(4.0, 3.2, 'CΔ', fontsize=9, fontweight='bold', color='#047857')

# C2 between A and C
ax.plot([4.5, 5.0], [4.0, 3.6], color='#047857', lw=1.5)
# capacitor symbol slanted
ax.plot([5.0, 5.9], [3.6, 3.0], color='#047857', lw=1.5)
ax.text(5.2, 3.8, 'CΔ', fontsize=9, fontweight='bold', color='#047857')

# C3 between B and C
ax.plot([4.5, 5.0], [2.2, 2.5], color='#047857', lw=1.5)
ax.plot([5.0, 5.9], [2.5, 3.0], color='#047857', lw=1.5)
ax.text(5.2, 2.2, 'CΔ', fontsize=9, fontweight='bold', color='#047857')

# Bottom formulas
ax.text(5.0, 0.3, r'$Q_C = P(\tan\theta_1 - \tan\theta_2) \qquad C_\Delta = \frac{Q_C / 3}{\omega V_L^2} = \frac{C_Y}{3} \quad (V_C = V_L)$', 
        ha='center', va='center', fontsize=10, fontweight='bold', color='#0f172a',
        bbox=dict(boxstyle='round,pad=0.4', facecolor='#f1f5f9', edgecolor='#94a3b8'))

plt.tight_layout()
p2_path = os.path.join(out_dir, 'pf_correction_delta_cap_schematic.png')
plt.savefig(p2_path, dpi=200, bbox_inches='tight')
plt.close()
print('Saved', p2_path)
