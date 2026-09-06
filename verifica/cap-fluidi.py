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

# ---------------------------------------------------------------------------
sez("8.4  Vasi comunicanti")

# Esempio: olio h=12,0 cm; acqua sale 10,4 cm.  rho_olio ?
rho_olio = 1000 * 10.4 / 12.0
print(f"olio: rho = {rho_olio:.1f} kg/m3  (~ {round(rho_olio/10)*10} )")

# es: tubo a U, mercurio + acqua colonna 20 cm -> h_Hg ?
h_hg2 = 1000 * 20 / 13600
print(f"U-tube Hg/acqua: h_Hg = {h_hg2:.2f} cm")

# es: tubi 1 e 20 cm2, 100 mL nel sottile -> Delta h
dh = 100 / (1 + 20)
print(f"tubi 1+20 cm2, 100 cm3 -> Delta h = {dh:.2f} cm")

# ---------------------------------------------------------------------------
sez("8.5  Pressione atmosferica")

p0 = rho_hg * g * 0.76
print(f"Torricelli: p0 = {p0:.0f} Pa = {p0/1e5:.3f} e5")
h_water_col = p0 / (rho_acqua * g)
print(f"colonna d'acqua equivalente: h = {h_water_col:.1f} m")

# banco 120x60 cm
A_banco = 1.20 * 0.60
print(f"banco: A={A_banco} m2, F = {1e5*A_banco:.0f} N = {1e5*A_banco/9810:.1f} t-peso")

# es1: 120 mmHg
p_art = 120 * 133
print(f"120 mmHg = {p_art} Pa = {p_art/101325:.3f} atm")

# es2: montagna, dp = 240 hPa, rho_air = 1,2
dp = (1000 - 760) * 100
h_mont = dp / (1.2 * g)
print(f"montagna: h = {h_mont:.0f} m")

# es4: emisferi di Magdeburgo, d = 30 cm
import math
r = 0.15
F_mag = 101325 * math.pi * r**2
print(f"Magdeburgo: F = {F_mag:.0f} N = {F_mag/1e3:.1f} e3")

# ---------------------------------------------------------------------------
sez("8.6  Principio di Archimede")

# Esempio bilancia idrostatica: 5,40 N aria / 4,70 N acqua
S = 5.40 - 4.70
V = S / (rho_acqua * g)
m = 5.40 / g
print(f"bilancia idr.: S={S:.2f} N, V={V:.3e} m3, m={m:.3f} kg, rho={m/V:.0f} kg/m3")

# Esempio zattera polistirolo rho=25, V=0,60 m3
Smax = rho_acqua * 0.60 * g
Pz = 25 * 0.60 * g
mcar = (Smax - Pz) / g
print(f"zattera: Smax={Smax:.0f} N, Pz={Pz:.0f} N, m_carico={mcar:.0f} kg")

# es1: cubo legno 10 cm, rho 700  -> frazione immersa
print(f"cubo legno: immerso {700/1000:.2f} -> sporge {10*(1-0.7):.0f} cm")

# es2: sfera Al d=6 cm in acqua -> T
rsf = 0.03
Vsf = 4/3 * math.pi * rsf**3
P_sf = 2700 * Vsf * g
S_sf = 1000 * Vsf * g
print(f"sfera Al: V={Vsf:.3e} m3, P={P_sf:.2f} N, S={S_sf:.2f} N, T={P_sf-S_sf:.2f} N")

# es3: blocco 12,0 / 7,5 N
S3 = 12.0 - 7.5
V3 = S3 / (rho_acqua * g)
m3 = 12.0 / g
print(f"blocco: S={S3:.1f} N, V={V3:.3e} m3, rho={m3/V3:.0f} kg/m3")

# es4: chiatta 8x3 m, carico 6,0 t
dh = 6000 / (rho_acqua * 8.0 * 3.0)
print(f"chiatta: Delta h = {dh:.3f} m")

# es5: pallone V=2000, He 0,18, struttura 400 kg, aria 1,2
S5 = 1.2 * 2000 * g
P5 = (0.18 * 2000 + 400) * g
print(f"pallone: S={S5:.0f} N, P={P5:.0f} N, S-P={S5-P5:.0f} N = {(S5-P5)/1e4:.1f} e4")
