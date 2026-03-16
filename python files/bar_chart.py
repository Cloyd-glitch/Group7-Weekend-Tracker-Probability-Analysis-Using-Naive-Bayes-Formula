import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import matplotlib.gridspec as gridspec
import numpy as np

# ── Likelihood / prior data ────────────────────────────────────────────────
tables = {
    "Class Priors": {
        "Great":    {"Great": 7/14, "Terrible": 7/14},
        "Terrible": {"Great": 7/14, "Terrible": 7/14},
    },
    "Worship": {
        "Attended":          {"Great": 1/7, "Terrible": 2/7},
        "Have not attended": {"Great": 6/7, "Terrible": 5/7},
    },
    "Location": {
        "Hometown":       {"Great": 5/7, "Terrible": 5/7},
        "BH / elsewhere": {"Great": 2/7, "Terrible": 2/7},
    },
    "Academic Load": {
        "Heavy":        {"Great": 6/7, "Terrible": 3/7},
        "Light / none": {"Great": 1/7, "Terrible": 4/7},
    },
    "Finances": {
        "Stable":        {"Great": 5/7, "Terrible": 1/7},
        "Broke / tipid": {"Great": 2/7, "Terrible": 6/7},
    },
}

# ── Final posterior scores (from docx Table 5) ────────────────────────────
#   P(yes) row  → Great:    0.031   Terrible: 0.004
#   P(no)  row  → Great:    0.006   Terrible: 0.049
posterior = {
    "P(yes) — Great":    0.031,
    "P(yes) — Terrible": 0.004,
    "P(no) — Great":     0.006,
    "P(no) — Terrible":  0.049,
}

# ── Colors ─────────────────────────────────────────────────────────────────
COLOR_G     = "#2ecc71"
COLOR_T     = "#e74c3c"
COLOR_BG    = "#1a1a2e"
COLOR_PANEL = "#16213e"
COLOR_AX    = "#e0e0e0"
COLOR_GRID  = "#2a2a4a"
ACCENT      = "#f0f0f0"

section_colors = {
    "Class Priors":  "#9b59b6",
    "Worship":       "#3498db",
    "Location":      "#1abc9c",
    "Academic Load": "#e67e22",
    "Finances":      "#e74c3c",
}

# ── Flatten rows ───────────────────────────────────────────────────────────
rows = []
separators = []
y = 0
for tname, cats in tables.items():
    separators.append((y, tname))
    for cat, vals in cats.items():
        rows.append((tname, cat, vals["Great"], vals["Terrible"]))
        y += 1

n          = len(rows)
categories = [r[1] for r in rows]
p_great    = np.array([r[2] for r in rows])
p_terrible = np.array([r[3] for r in rows])

# ── Layout: main diverging chart (left) + posterior panel (right) ──────────
fig = plt.figure(figsize=(16, 10), facecolor=COLOR_BG)
gs  = gridspec.GridSpec(1, 2, width_ratios=[3, 1], wspace=0.06)

ax  = fig.add_subplot(gs[0])   # diverging bars
axp = fig.add_subplot(gs[1])   # posterior panel

ax.set_facecolor(COLOR_PANEL)
axp.set_facecolor(COLOR_PANEL)

# ══════════════════════════════════════════════════════════════════════════
#  LEFT — diverging likelihood chart
# ══════════════════════════════════════════════════════════════════════════
ypos  = np.arange(n)
bar_h = 0.42

bars_g = ax.barh(ypos + bar_h/2,  p_great,    height=bar_h,
                 color=COLOR_G, alpha=0.88, zorder=3)
bars_t = ax.barh(ypos - bar_h/2, -p_terrible, height=bar_h,
                 color=COLOR_T, alpha=0.88, zorder=3)

# value labels
for i, (pg, pt) in enumerate(zip(p_great, p_terrible)):
    ax.text(pg + 0.015, ypos[i] + bar_h/2,
            f"{pg:.2f}", va="center", ha="left",
            color=COLOR_G, fontsize=8.5, fontweight="bold")
    ax.text(-pt - 0.015, ypos[i] - bar_h/2,
            f"{pt:.2f}", va="center", ha="right",
            color=COLOR_T, fontsize=8.5, fontweight="bold")

# category labels at center
for i, cat in enumerate(categories):
    ax.text(0, ypos[i], cat, va="center", ha="center",
            color=ACCENT, fontsize=9, fontweight="500",
            bbox=dict(boxstyle="round,pad=0.25", fc=COLOR_PANEL,
                      ec=COLOR_GRID, lw=0.8), zorder=5)

# section separators + right-side headers
for sep_y, tname in separators:
    color = section_colors[tname]
    # Horizontal rule
    ax.axhline(sep_y - 0.65, color=color, linewidth=0.9, alpha=0.55, zorder=2)
    # Section label flush left inside the plot
    ax.text(-1.07, sep_y - 0.55, f"[ {tname} ]",
            va="bottom", ha="left", color=color,
            fontsize=8.5, fontweight="bold",
            transform=ax.transData, zorder=5)

# center axis
ax.axvline(0, color=COLOR_AX, linewidth=1.2, zorder=4)

ax.set_xlim(-1.08, 1.08)
ax.set_ylim(-0.8, n - 0.2)
ax.invert_yaxis()

xticks = [-1, -0.75, -0.5, -0.25, 0, 0.25, 0.5, 0.75, 1]
ax.set_xticks(xticks)
ax.set_xticklabels([f"{abs(v):.2f}" for v in xticks],
                   color=COLOR_AX, fontsize=8)
ax.set_yticks([])
ax.xaxis.grid(True, color=COLOR_GRID, linewidth=0.6, zorder=1)
for spine in ax.spines.values():
    spine.set_visible(False)

ax.text(-0.54, -0.72, "◄  P( · | Terrible)",
        color=COLOR_T, fontsize=10, fontweight="bold",
        ha="center", va="center", transform=ax.transData)
ax.text( 0.54, -0.72, "P( · | Great )  ►",
        color=COLOR_G, fontsize=10, fontweight="bold",
        ha="center", va="center", transform=ax.transData)

# ══════════════════════════════════════════════════════════════════════════
#  RIGHT — final posterior panel
# ══════════════════════════════════════════════════════════════════════════
axp.set_xlim(0, 1)
axp.set_ylim(0, 1)
axp.set_xticks([])
axp.set_yticks([])
for spine in axp.spines.values():
    spine.set_edgecolor(COLOR_GRID)
    spine.set_linewidth(0.8)

# Panel title
axp.text(0.5, 0.97, "Final Posteriors",
         color=ACCENT, fontsize=10, fontweight="bold",
         ha="center", va="top", transform=axp.transAxes)
axp.text(0.5, 0.92, "P(y) × ∏ P(xᵢ | y)",
         color=COLOR_AX, fontsize=8, ha="center", va="top",
         transform=axp.transAxes, style="italic")

# ── P(yes) row ─────────────────────────────────────────────────────────────
axp.text(0.5, 0.83, "P(yes) — label = Great",
         color="#ffffff", fontsize=8.5, fontweight="bold",
         ha="center", va="center", transform=axp.transAxes)

# bars for P(yes)
bar_data_yes = [
    ("Great",    0.031, COLOR_G),
    ("Terrible", 0.004, COLOR_T),
]
bar_y_yes = [0.74, 0.66]
for (lbl, val, col), by in zip(bar_data_yes, bar_y_yes):
    bar_w = val / 0.06          # scale: max ~0.06
    rect = mpatches.FancyBboxPatch(
        (0.08, by - 0.03), bar_w * 0.84, 0.06,
        boxstyle="round,pad=0.005",
        linewidth=0, facecolor=col, alpha=0.85,
        transform=axp.transAxes, zorder=3
    )
    axp.add_patch(rect)
    axp.text(0.08 + bar_w * 0.84 + 0.03, by,
             f"{val:.3f}", color=col, fontsize=9, fontweight="bold",
             va="center", transform=axp.transAxes)
    axp.text(0.06, by, lbl, color=COLOR_AX, fontsize=8,
             va="center", ha="right", transform=axp.transAxes)

# fraction annotation
axp.text(0.5, 0.59,
         "7/14 × (1/7)(5/7)(6/7)(2/7)",
         color=COLOR_G, fontsize=7.2, ha="center",
         transform=axp.transAxes)
axp.text(0.5, 0.55,
         "7/14 × (2/7)(5/7)(3/7)(6/7)",
         color=COLOR_T, fontsize=7.2, ha="center",
         transform=axp.transAxes)

# divider
axp.axhline(0.51, color=COLOR_GRID, linewidth=0.8,
            xmin=0.05, xmax=0.95)

# ── P(no) row ──────────────────────────────────────────────────────────────
axp.text(0.5, 0.47, "P(no) — label = Terrible",
         color="#ffffff", fontsize=8.5, fontweight="bold",
         ha="center", va="center", transform=axp.transAxes)

bar_data_no = [
    ("Great",    0.006, COLOR_G),
    ("Terrible", 0.049, COLOR_T),
]
bar_y_no = [0.38, 0.30]
for (lbl, val, col), by in zip(bar_data_no, bar_y_no):
    bar_w = val / 0.06
    rect = mpatches.FancyBboxPatch(
        (0.08, by - 0.03), bar_w * 0.84, 0.06,
        boxstyle="round,pad=0.005",
        linewidth=0, facecolor=col, alpha=0.85,
        transform=axp.transAxes, zorder=3
    )
    axp.add_patch(rect)
    axp.text(0.08 + bar_w * 0.84 + 0.03, by,
             f"{val:.3f}", color=col, fontsize=9, fontweight="bold",
             va="center", transform=axp.transAxes)
    axp.text(0.06, by, lbl, color=COLOR_AX, fontsize=8,
             va="center", ha="right", transform=axp.transAxes)

axp.text(0.5, 0.22,
         "7/14 × (1/7)(5/7)(1/7)(5/7)",
         color=COLOR_G, fontsize=7.2, ha="center",
         transform=axp.transAxes)
axp.text(0.5, 0.18,
         "7/14 × (2/7)(5/7)(4/7)(6/7)",
         color=COLOR_T, fontsize=7.2, ha="center",
         transform=axp.transAxes)

# ── Decision banner ────────────────────────────────────────────────────────
decision_box = mpatches.FancyBboxPatch(
    (0.05, 0.04), 0.95, 0.10,
    boxstyle="round,pad=0.01",
    linewidth=1.2, edgecolor=COLOR_T,
    facecolor="#3d1a1a", alpha=0.95,
    transform=axp.transAxes,
)
axp.add_patch(decision_box)
axp.text(0.5, 0.115, "Predicted: Terrible",
         color="#e0dfdf", fontsize=9.5, fontweight="bold",
         ha="center", va="center", transform=axp.transAxes)
axp.text(0.512345, 0.055, "0.049 & 0.006 > 0.031 & 0.004 thus , Terrible wins",
         color="#ffffff", fontsize=7.5,
         ha="center", va="center", transform=axp.transAxes)


legend_handles = [
    mpatches.Patch(color=COLOR_G, label="P( · | Great )"),
    mpatches.Patch(color=COLOR_T, label="P( · | Terrible )"),
]
ax.legend(handles=legend_handles, loc="lower left",
          facecolor=COLOR_PANEL, edgecolor=COLOR_GRID,
          labelcolor=COLOR_AX, fontsize=9, framealpha=0.9)

fig.suptitle(
    "Naïve Bayes — Likelihoods, Priors & Final Posteriors",
    color=ACCENT, fontsize=14, fontweight="bold", y=0.99
)

import os
out = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                   "bar_chart.png")
plt.savefig(out, dpi=180, bbox_inches="tight", facecolor=COLOR_BG)
print(f" Saved → {out}")
plt.show()