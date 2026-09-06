#!/usr/bin/env python3
# Verifica dei numeri della relazione svolta "Legge di Hooke" (cap. Relazioni di Laboratorio).
# Python puro, niente numpy.  g = 9,81 N/kg.

import math

g = 9.81

# --- Dati sperimentali (originali) --------------------------------------------
# massa (g), L1 (mm), L2 (mm)
dati = [
    (100.0, 150, 189),
    (200.0, 150, 231),
    (300.0, 149, 270),
    (400.0, 151, 310),
]
dm = 0.1        # g, sensibilita' bilancia
dL = 1.0        # mm, sensibilita' righello

print("  m(g)   L1     L2     x(mm)   P(N)     k(N/m)   Dx(mm)  Dk(N/m)")
ks = []
for m, L1, L2 in dati:
    x_mm = L2 - L1
    x = x_mm / 1000.0
    P = m / 1000.0 * g
    k = P / x
    dP = dm / 1000.0 * g
    dx = math.sqrt(dL**2 + dL**2)          # differenza di due misure indipendenti
    dk = k * (dP / P + (dx / x_mm))        # errori relativi (x_mm e dx stesse unita')
    ks.append(k)
    print(f"{m:6.1f} {L1:5d}  {L2:5d}  {x_mm:5.0f}   {P:6.3f}   {k:6.2f}   {dx:5.2f}   {dk:6.2f}")

kmed = sum(ks) / len(ks)
semidisp = (max(ks) - min(ks)) / 2
print()
print(f"k medio        = {kmed:.4f} N/m")
print(f"semidispersione= {semidisp:.4f} N/m")
print(f"k medio  in N/cm = {kmed/100:.4f}")
print(f"Dk      in N/cm = {semidisp/100:.4f}  -> arrotondato {round(semidisp/100, 3):.3f}")
print(f"RISULTATO: k = ({kmed/100:.3f} +- {semidisp/100:.3f}) N/cm"
      f"  ~  ({round(kmed/100,3):.3f} +- {round(semidisp/100,3):.3f}) N/cm")

print()
print("=" * 60)
print("Relazione 'attrito statico' -- metodo delle rette di max/min pendenza")
print("=" * 60)

# blocchetto di legno: forza di primo distacco Fpd al variare del peso Fp
# (dati di una simulazione: 5 punti)
attrito = [
    (2.45, 0.93, 0.02),
    (3.45, 1.29, 0.02),
    (4.40, 1.64, 0.03),
    (5.40, 2.00, 0.03),
    (6.38, 2.33, 0.03),
]
Fp1, Fpd1, e1 = attrito[0]
Fp5, Fpd5, e5 = attrito[-1]
A = (Fp1, Fpd1 + e1)   # estremo superiore primo punto
B = (Fp1, Fpd1 - e1)   # estremo inferiore primo punto
C = (Fp5, Fpd5 + e5)   # estremo superiore ultimo punto
D = (Fp5, Fpd5 - e5)   # estremo inferiore ultimo punto
print(f"A = {A}   B = {B}")
print(f"C = {C}   D = {D}")
bmax = (C[1] - B[1]) / (C[0] - B[0])   # B -> C
bmin = (D[1] - A[1]) / (D[0] - A[0])   # A -> D
Ks = (bmax + bmin) / 2
eKs = (bmax - bmin) / 2
print(f"b_max (B->C) = {bmax:.3f}")
print(f"b_min (A->D) = {bmin:.3f}")
print(f"Ks  = (b_max + b_min)/2 = {Ks:.4f}  -> {round(Ks,2):.2f}")
print(f"eKs = (b_max - b_min)/2 = {eKs:.4f}  -> {round(eKs,2):.2f}")
print(f"RISULTATO: Ks = ({round(Ks,2):.2f} +- {round(eKs,2):.2f})  (adimensionale)")
# rapporti Fpd/Fp punto per punto (controllo di coerenza)
print("Fpd/Fp per punto:", [round(fpd / fp, 3) for fp, fpd, _ in attrito])

print()
# --- controllo: retta di best fit P = k x (per l'origine) e con intercetta -----
xs = [(L2 - L1) / 1000.0 for _, L1, L2 in dati]
Ps = [m / 1000.0 * g for m, _, _ in dati]
n = len(xs)
Sx, Sy = sum(xs), sum(Ps)
Sxx = sum(v * v for v in xs)
Sxy = sum(a * b for a, b in zip(xs, Ps))
# fit y = A + B x
B = (n * Sxy - Sx * Sy) / (n * Sxx - Sx * Sx)
A = (Sy - B * Sx) / n
# fit y = B0 x (vincolato all'origine)
B0 = Sxy / Sxx
print()
print(f"best fit con intercetta : P = {A:+.3f} + {B:.2f} x   (k = {B:.2f} N/m)")
print(f"best fit per l'origine  : P = {B0:.2f} x            (k = {B0:.2f} N/m)")
