#!/usr/bin/env python3
# Verifica dei numeri del capitolo "Equilibrio dei fluidi".
# Python puro, niente numpy.  g = 9,81 N/kg.

g = 9.81

def sez(t): print("\n" + "=" * 60 + "\n" + t + "\n" + "=" * 60)

# ---------------------------------------------------------------------------
sez("8.1  La pressione")

# Esempio: mattone 25 N, facce 25x12 cm e 12x6 cm
F = 25.0
A1 = 0.25 * 0.12
A2 = 0.12 * 0.06
print(f"A1 = {A1:.4f} m^2   p1 = {F/A1:.0f} Pa")
print(f"A2 = {A2:.4f} m^2   p2 = {F/A2:.0f} Pa")
print(f"rapporto p2/p1 = {(F/A2)/(F/A1):.2f}")

# Esercizio: cassa 600 N, base 0,50 x 0,40 m
print(f"cassa: p = {600/(0.50*0.40):.0f} Pa")

# Esercizio: chiodo 40 N su 0,02 mm^2
A_chiodo = 0.02e-6            # m^2
p_chiodo = 40 / A_chiodo
print(f"chiodo: p = {p_chiodo:.3e} Pa = {p_chiodo/1e6:.0f} MPa")

# ---------------------------------------------------------------------------
sez("8.2  Legge di Stevino  p = rho g h")

rho_acqua = 1000.0
rho_hg = 13600.0

# Esempio: acqua a 10 m
p10 = rho_acqua * g * 10
print(f"acqua a 10 m: p = {p10:.0f} Pa = {p10/1e5:.3f} bar = {p10/101325:.2f} atm")

# Esempio: acquario 80x40 cm, h = 50 cm
p_ac = rho_acqua * g * 0.50
A_ac = 0.80 * 0.40
F_ac = p_ac * A_ac
print(f"acquario: p = {p_ac:.0f} Pa,  A = {A_ac:.2f} m^2,  F = {F_ac:.0f} N")
print(f"          (peso di {A_ac*0.50*1000:.0f} L = {A_ac*0.50*1000*g:.0f} N)")

# --- esercizi §8.2 ---
rho_mare = 1030.0
# 1) acqua di mare, p_rel = 2,5 bar
h1 = 2.5e5 / (rho_mare * g)
print(f"es1  mare, p_rel=2,5 bar  ->  h = {h1:.1f} m")

# 2) paratoia larga 0,60 alta 0,40, bordo inf al fondo, acqua a 1,8 m
h_centro = 1.8 - 0.40 / 2
p_centro = rho_acqua * g * h_centro
A_par = 0.60 * 0.40
F_par = p_centro * A_par
print(f"es2  paratoia: h_centro={h_centro} m, p={p_centro:.0f} Pa, A={A_par} m2, F={F_par:.0f} N")

# 3) 15 cm di mercurio = quanti m d'acqua (stessa pressione)?
h_w = 0.15 * rho_hg / rho_acqua
print(f"es3  15 cm Hg  ->  {h_w:.2f} m d'acqua")

# 4) serbatoio 40 kg, d=1,2 m, 3 piedini 15 cm2, gasolio rho=840, h=1,5 m
r = 1.2 / 2
V_oil = 3.14159265 * r**2 * 1.5
m_oil = 840 * V_oil
F_tot = (40 + m_oil) * g
A_piedi = 3 * 15e-4
p_piede = F_tot / A_piedi
print(f"es4  V_oil={V_oil:.3f} m3, m_oil={m_oil:.0f} kg, F_tot={F_tot:.0f} N, p={p_piede:.3e} Pa = {p_piede/1e6:.1f} MPa")

# ---------------------------------------------------------------------------
sez("8.3  Principio di Pascal / torchio idraulico")

# torchio: rapporto aree 50, F1=200
print(f"torchio A2/A1=50, F1=200 N -> F2 = {200*50} N")

# Esempio cric: A1=2, A2=50 cm2, F2=6000 N
F1 = 6000 * 2.0 / 50
print(f"cric: F1 = {F1:.0f} N")
n = (50 * 12) / (2.0 * 3.0)
print(f"cric: n pompate = {n:.0f}")

# es1: diametri 4,0 e 32 cm, carico 9,6 kN
ratio = (32 / 4.0) ** 2
print(f"es1  A2/A1 = {ratio:.0f}, F1 = {9600/ratio:.0f} N")

# es2: A1=5 cm2, F1=80 N, F2=12 kN
A2 = 5.0 * 12000 / 80
n2 = A2 * 25 / (5.0 * 40)
print(f"es2  A2 = {A2:.0f} cm2, n = {n2:.2f} -> {round(n2)} corse")
