
from fractions import Fraction

# ─────────────────────────────────────────────────────────────────────────────
# RAW COUNTS (directly from each frequency table in the docx)
# Columns → Great (Yes=1) | Terrible (No=0)
# ─────────────────────────────────────────────────────────────────────────────

TOTAL_GREAT    = 7
TOTAL_TERRIBLE = 7
TOTAL          = 14

tables = {
    "Worship": {
        "Attended":      {"Great": 1, "Terrible": 2},
        "Have not":      {"Great": 6, "Terrible": 5},
    },
    "Location": {
        "Hometown":      {"Great": 5, "Terrible": 5},
        "BH/Elsewhere":  {"Great": 2, "Terrible": 2},
    },
    "AcadLoad": {
        "Heavy":         {"Great": 6, "Terrible": 3},
        "Light/None":    {"Great": 1, "Terrible": 4},
    },
    "Finances": {
        "Stable":        {"Great": 5, "Terrible": 1},
        "Broke/Tipid":   {"Great": 2, "Terrible": 6},
    },
}

# Mapping: feature value for each new instance per table
# Instance to classify (from the whiteboard example):
#   Worship   = Attended  (Yes)
#   Location  = Hometown  (Yes)
#   AcadLoad  = Heavy     (Yes)
#   Finances  = Broke     (No)
instance = {
    "Worship":  "Attended",
    "Location": "Hometown",
    "AcadLoad": "Heavy",
    "Finances": "Broke/Tipid",
}

def frac(num, den):
    #Return a Fraction and its decimal string.
    f = Fraction(num, den)
    return f, float(f)



print("  NAIVE BAYES — FULL TABLE-BY-TABLE CALCULATION")
print("  Formula: P(y|x) ∝ P(y) × ∏ P(xi | y)")



# TABLE 5 
print("\n")
print("TABLE 5 — CLASS PRIORS")

P_great_f,    P_great    = frac(TOTAL_GREAT,    TOTAL)
P_terrible_f, P_terrible = frac(TOTAL_TERRIBLE, TOTAL)

print(f"\n  {'Class':<20} {'Count':>6}   {'P(class)':>12}   {'Decimal':>8}")
print(f"  {'-'*20}  {'-'*6}   {'-'*12}   {'-'*8}")
print(f"  {'Great (Yes)':<20} {TOTAL_GREAT:>6}   "
      f"{'P(Great)':>5} = {TOTAL_GREAT}/{TOTAL}   {P_great:>8.4f}")
print(f"  {'Terrible (No)':<20} {TOTAL_TERRIBLE:>6}   "
      f"{'P(Terr.)':>5} = {TOTAL_TERRIBLE}/{TOTAL}   {P_terrible:>8.4f}")
print(f"  {'Total':<20} {TOTAL:>6}")
print(f"\n  ∴  P(Great)    = {TOTAL_GREAT}/{TOTAL} = {P_great:.4f}")
print(f"     P(Terrible) = {TOTAL_TERRIBLE}/{TOTAL} = {P_terrible:.4f}")

# ─────────────────────────────────────────────────────────────────────────────
# TABLES 1–4  (LIKELIHOODS)
# ─────────────────────────────────────────────────────────────────────────────
likelihoods_great    = {}
likelihoods_terrible = {}

table_numbers = {"Worship": 1, "Location": 2, "AcadLoad": 3, "Finances": 4}
table_labels  = {
    "Worship":  "TABLE 1 — WORSHIP SERVICE  (Attended / Have not attended)",
    "Location": "TABLE 2 — LOCATION         (Hometown / BH or Elsewhere)",
    "AcadLoad": "TABLE 3 — ACADEMIC LOAD    (Heavy / Light or None)",
    "Finances": "TABLE 4 — FINANCES         (Stable / Broke or Tipid)",
}

for feature, rows in tables.items():
    print("\n")
    print(table_labels[feature])
 

    header = f"  {'Category':<20} {'Gr.Count':>8}  {'P(.|Great)':>12}  {'Te.Count':>8}  {'P(.|Terr.)':>12}"
    print("\n" + header)
    print("  " + "-" * (len(header) - 2))

    for category, counts in rows.items():
        g_count = counts["Great"]
        t_count = counts["Terrible"]
        p_g_f, p_g = frac(g_count, TOTAL_GREAT)
        p_t_f, p_t = frac(t_count, TOTAL_TERRIBLE)

        print(f"  {category:<20} {g_count:>8}  "
              f"{g_count}/{TOTAL_GREAT} = {p_g:>6.4f}  "
              f"{t_count:>8}  "
              f"{t_count}/{TOTAL_TERRIBLE} = {p_t:>6.4f}")

        # Store the likelihood for the instance value
        inst_val = instance[feature]
        if category == inst_val:
            likelihoods_great[feature]    = (g_count, TOTAL_GREAT, p_g)
            likelihoods_terrible[feature] = (t_count, TOTAL_TERRIBLE, p_t)

    # totals row
    total_g = sum(r["Great"]    for r in rows.values())
    total_t = sum(r["Terrible"] for r in rows.values())
    print(f"  {'Total':<20} {total_g:>8}  {'':>18}  {total_t:>8}")

    # Identify which category is being used for classification
    inst_val = instance[feature]
    g_n, g_d, g_p = likelihoods_great[feature]
    t_n, t_d, t_p = likelihoods_terrible[feature]
    print(f"\n  Instance value → '{inst_val}'")
    print(f"    P({inst_val} | Great)    = {g_n}/{g_d} = {g_p:.4f}")
    print(f"    P({inst_val} | Terrible) = {t_n}/{t_d} = {t_p:.4f}")

print("\n")
print("  FINAL POSTERIOR CALCULATION")
print("  Instance: Worship=Attended, Location=Hometown,")
print("            AcadLoad=Heavy, Finances=Broke/Tipid")

print("\n  ── Step 1: Write out the formula ───────────────────────")
print("  P(Great | x)    ∝ P(Great)    × P(Worship|Gr) × P(Location|Gr)")
print("                              × P(AcadLoad|Gr) × P(Finances|Gr)")
print("  P(Terrible | x) ∝ P(Terrible) × P(Worship|Te) × P(Location|Te)")
print("                              × P(AcadLoad|Te) × P(Finances|Te)")

# Collect individual likelihoods
feat_order = ["Worship", "Location", "AcadLoad", "Finances"]
g_liks = [likelihoods_great[f][2]    for f in feat_order]
t_liks = [likelihoods_terrible[f][2] for f in feat_order]

g_fracs = [f"{likelihoods_great[f][0]}/{likelihoods_great[f][1]}"    for f in feat_order]
t_fracs = [f"{likelihoods_terrible[f][0]}/{likelihoods_terrible[f][1]}" for f in feat_order]

print("\n  ── Step 2: Substitute values ───────────────────────────")
print(f"\n  P(Great | x)    = {TOTAL_GREAT}/{TOTAL}")
for i, f in enumerate(feat_order):
    inst_val = instance[f]
    print(f"                  × P({inst_val:<12} | Great)    = {g_fracs[i]}")

print(f"\n  P(Terrible | x) = {TOTAL_TERRIBLE}/{TOTAL}")
for i, f in enumerate(feat_order):
    inst_val = instance[f]
    print(f"                  × P({inst_val:<12} | Terrible) = {t_fracs[i]}")

print("\n  ── Step 3: Multiply ────────────────────────────────────")
posterior_great    = P_great    * 1.0
posterior_terrible = P_terrible * 1.0
for g, t in zip(g_liks, t_liks):
    posterior_great    *= g
    posterior_terrible *= t

g_lik_str = " × ".join(g_fracs)
t_lik_str = " × ".join(t_fracs)

print(f"\n  P(Great | x)    = {TOTAL_GREAT}/{TOTAL} × {g_lik_str}")
print(f"                  = {P_great:.4f} × {' × '.join(f'{v:.4f}' for v in g_liks)}")
print(f"                  = {posterior_great:.6f}")

print(f"\n  P(Terrible | x) = {TOTAL_TERRIBLE}/{TOTAL} × {t_lik_str}")
print(f"                  = {P_terrible:.4f} × {' × '.join(f'{v:.4f}' for v in t_liks)}")
print(f"                  = {posterior_terrible:.6f}")

print("\n  ── Step 4: Normalize ───────────────────────────────────")
total_posterior = posterior_great + posterior_terrible
norm_great    = posterior_great    / total_posterior
norm_terrible = posterior_terrible / total_posterior

print(f"\n  Total = {posterior_great:.6f} + {posterior_terrible:.6f} = {total_posterior:.6f}")
print(f"\n  P(Great | x)    = {posterior_great:.6f} / {total_posterior:.6f} = {norm_great:.4f}  ({norm_great*100:.2f}%)")
print(f"  P(Terrible | x) = {posterior_terrible:.6f} / {total_posterior:.6f} = {norm_terrible:.4f}  ({norm_terrible*100:.2f}%)")

print("\n  ── Step 5: Decision ────────────────────────────────────")
winner = "Great " if posterior_great > posterior_terrible else "Terrible"
print(f"\n  {'P(Great)':>20} = {posterior_great:.6f}")
print(f"  {'P(Terrible)':>20} = {posterior_terrible:.6f}")
if posterior_great > posterior_terrible:
    print(f"\n  Since P(Great) > P(Terrible),")
else:
    print(f"\n  Since P(Terrible) > P(Great),")
print(f"  ∴  Predicted class → {winner}")
print("\n")