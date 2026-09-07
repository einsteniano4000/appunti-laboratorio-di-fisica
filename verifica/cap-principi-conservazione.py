#!/usr/bin/env python3
# Verifica dei numeri del capitolo "I princìpi di conservazione" (Unita' 10, Lez. 1-3).
# Python puro, niente numpy.  g = 9,81 m/s^2 (come nel resto della dispensa).

import math

g = 9.81

def sez(t): print("\n" + "=" * 68 + "\n" + t + "\n" + "=" * 68)


# ===========================================================================
sez("1  La conservazione dell'energia meccanica")

# es. svolto: tuffo h = 5,0 m
h = 5.0
print(f"tuffo h=5,0: v = sqrt(2 g h) = {math.sqrt(2*g*h):.4f} ~ 9,9 m/s")

# es. svolto: palla da demolizione L=15, alpha=45, m=200
L, m = 15.0, 200.0
h = L * (1 - math.cos(math.radians(45)))
print(f"palla demolizione: h = L(1-cos45) = {h:.4f} ~ 4,4 m")
print(f"  E_A = m g h = {m*g*h:.1f} ~ 8,6e3 J ; v_B = sqrt(2 g h) = {math.sqrt(2*g*h):.4f} ~ 9,3 m/s")

print("\n--- esercizi §1 ---")
print(f"sasso ponte 20 m: v = {math.sqrt(2*g*20):.4f} ~ 19,8 m/s")
h = 1.2
print(f"biglia 50 g da 1,2 m: E_m = m g h = {0.050*g*h:.4f} ~ 0,59 J ; v = {math.sqrt(2*g*h):.4f} ~ 4,9 m/s")
print(f"pendolo h=0,15: v = {math.sqrt(2*g*0.15):.4f} ~ 1,7 m/s")
h = 2.4
print(f"skate 55 kg da 2,4 m: E_m = {55*g*h:.1f} ~ 1,3e3 J ; v = {math.sqrt(2*g*h):.4f} ~ 6,9 m/s = {math.sqrt(2*g*h)*3.6:.1f} km/h")
k, s, mb = 2000.0, 0.050, 0.020
print(f"molla k=2000 s=5 cm biglia 20 g: v = s sqrt(k/m) = {s*math.sqrt(k/mb):.4f} ~ 16 m/s")
print(f"lancio su v0=12, m=2,0: h_max = v^2/2g = {12**2/(2*g):.4f} ~ 7,3 m")


# ===========================================================================
sez("2  Quando l'energia meccanica non si conserva")

# es. svolto: pallina piano incl liscio h=3,0 + orizz attrito k=0,20, m=1,0, d=5,0
m, h, k, d = 1.0, 3.0, 0.20, 5.0
Emi = m*g*h
La = -k*m*g*d
print(f"pallina: E_mi = m g h = {Emi:.4f} ~ 29,4 J ; L_a = -k m g d = {La:.4f} ~ -9,8 J ; E_mf = {Emi+La:.4f} ~ 19,6 J")

# es. svolto: montagne russe E0 = 50000, perde 10% per collina, 5a collina = dopo 4 passaggi
E0 = 50000.0
E5 = E0 * 0.90**4
print(f"montagne russe: E5 = 50000 * 0,9^4 = {E5:.1f} ~ 33000 J")

print("\n--- esercizi §2 ---")
print(f"pendolo 2,5 -> 1,5 J: L_a = {1.5-2.5:.1f} J")
print(f"paracadutista 70 kg per 100 m: dE_m = m g h = {70*g*100:.1f} ~ 69 kJ")
print(f"slitta attrito 30 N per 50 m: |L_a| = {30*50:.0f} J = 1,5 kJ")
# carrello 2,0 kg a 6,0, 10 m, k=0,050
m, v, k, d = 2.0, 6.0, 0.050, 10.0
EmA = 0.5*m*v**2
La = -k*m*g*d
print(f"carrello: E_mA = {EmA:.1f} J ; L_a = {La:.4f} ~ -9,8 J ; E_mB = {EmA+La:.4f} ~ 26 J")
# calciatore m=0,4, v0=25, entra a 2,2 m con v=18
Emi = 0.5*0.4*25**2
Emf = 0.5*0.4*18**2 + 0.4*g*2.2
print(f"calciatore: E_mi = {Emi:.1f} J ; E_mf = {Emf:.4f} ~ 73 J ; dissipati = {Emi-Emf:.4f} ~ 52 J")
# pattinatrice rampa 30, v=6,0, m=60, F_a=50
m, v, Fa = 60.0, 6.0, 50.0
Ec = 0.5*m*v**2
# Ec = m g (d/2) + Fa d  ->  d (m g /2 + Fa) = Ec
d = Ec / (m*g/2 + Fa)
print(f"pattinatrice: E_c = {Ec:.0f} J ; d = {d:.4f} m ; h = d/2 = {d/2:.4f} ~ 1,6 m")


# ===========================================================================
sez("3  La conservazione della quantita' di moto")

# esempio: sasso 50 g a 10 m/s
print(f"sasso 50 g a 10 m/s: p = {0.050*10:.2f} kg m/s")

# es. svolto: bambina 30 kg + pallone 0,5 kg a 6,0 m/s
m1, m2, v2 = 30.0, 0.50, 6.0
v1 = -m2*v2/m1
print(f"bambina+pallone: v1 = -m2 v2 / m1 = {v1:.4f} = -0,10 m/s")

# es. svolto: rinculo pistola 1,3 kg, proiettile 12 g a 320 m/s
M, mp, vp = 1.3, 0.012, 320.0
va = -mp*vp/M
print(f"rinculo: v_a = -m_p v_p / M = {va:.4f} ~ -3,0 m/s")

# es. svolto: due carrelli 2,0 (a 5,0) + 3,0 (fermo) -> agganciati
m1, v1, m2 = 2.0, 5.0, 3.0
vf = m1*v1/(m1+m2)
Eci = 0.5*m1*v1**2
Ecf = 0.5*(m1+m2)*vf**2
print(f"carrelli anelastico: v_f = {vf:.2f} m/s ; E_ci = {Eci:.1f} J, E_cf = {Ecf:.1f} J, persi {Eci-Ecf:.1f} J")

# es. svolto: pendolo balistico M=2,00, m=10,0 g, h=8,00 cm
M, m, h = 2.00, 0.0100, 0.0800
vs = math.sqrt(2*g*h)
vp = (M+m)/m * vs
print(f"pendolo balistico: v_s = sqrt(2 g h) = {vs:.4f} ~ 1,25 m/s ; v_p = (M+m)/m * v_s = {vp:.4f} ~ 252 m/s")

print("\n--- esercizi §3 ---")
print(f"fucile 4,0 kg, proiettile 20 g a 600: v_a = {-0.020*600/4.0:.2f} m/s")
print(f"carrelli 2,0 (5,0) + 3,0: v_f = {2.0*5.0/5.0:.1f} m/s")
print(f"pattinatori 50 (2,4) e 80: v_2 = {-50*2.4/80:.2f} m/s")
print(f"palla 0,5 kg rimbalza 4,0 m/s: dp = {0.5*(-4.0-4.0):.1f} kg m/s (modulo 4,0)")
print(f"auto/fuoristrada stessa p, m_f = 2 m_a: v_f = v_a/2 = {72/2:.0f} km/h")
print(f"vagoni 12 t (2,0) + 8 t: v_f = {12*2.0/20:.1f} m/s")


# ===========================================================================
sez("Problemi di riepilogo")

def P(n, s): print(f"{n:>2}. {s}")

# 1 sasso 0,80 kg da 12 m
h = 12.0
P(1, f"E_m = {0.80*g*h:.1f} ~ 94 J ; v = {math.sqrt(2*g*h):.4f} ~ 15,3 m/s ; E_c = {0.5*0.80*2*g*h:.1f} J")
# 2 biglia 0,90 m
P(2, "risale a 0,90 m")
# 3 pendolo 1,0 m, h=0,20
P(3, f"v_basso = {math.sqrt(2*g*0.20):.4f} ~ 2,0 ; a 0,10 m: v = {math.sqrt(2*g*0.10):.4f} ~ 1,4 m/s")
# 4 carrello 1,5 kg a 3,0, molla k=600
P(4, f"s = v sqrt(m/k) = {3.0*math.sqrt(1.5/600):.4f} ~ 0,15 m")
# 5 auto 1000 kg, 20 m/s, ferma in 40 m
P(5, f"F_a = 0,5 m v^2 / d = {0.5*1000*400/40:.0f} N")
# 6 slitta 25 kg da 8,0 m, arriva a 10 m/s
Emi = 25*g*8.0; Ecf = 0.5*25*100
P(6, f"E_mi = {Emi:.1f} J ; E_cf = {Ecf:.0f} J ; dissipati {Emi-Ecf:.1f} ~ 712 J")
# 7 pallina 1,0 kg da 2,5 m, k=0,30
P(7, f"d = h/k = {2.5/0.30:.4f} ~ 8,3 m")
# 8 montagne russe 80 kJ, -15% per collina, dopo 3
P(8, f"E_3 = 80 * 0,85^3 = {80*0.85**3:.4f} ~ 49 kJ")
# 9 proiettile 15 g a 400 m/s
P(9, f"p = {0.015*400:.1f} kg m/s ; E_c = {0.5*0.015*400**2:.0f} J")
# 10 tennis 58 g, 30 -> 40 m/s (rimbalzo), dt = 5,0 ms
dp = 0.058*(40-(-30))
P(10, f"dp = {dp:.4f} kg m/s ; F = dp/dt = {dp/0.0050:.1f} ~ 812 N")
# 11 ragazzo 40 kg da barca 160 kg a 2,0 m/s
P(11, f"v_barca = {-40*2.0/160:.2f} m/s")
# 12 carrello 3,0 (4,0) tampona 1,0 fermo, agganciati
vf = 3.0*4.0/4.0
Eci = 0.5*3.0*16; Ecf = 0.5*4.0*vf**2
P(12, f"v_f = {vf:.1f} m/s ; E_ci = {Eci:.0f} J, E_cf = {Ecf:.0f} J, dissipati {Eci-Ecf:.0f} J")
# 13 carrelli 1,5 (4,0) e 6,0 molla
P(13, f"v_2 = {-1.5*4.0/6.0:.2f} m/s (verso opposto)")
# 14 pendolo balistico M=1,50, m=8,0 g, h=6,0 cm
M, m, h = 1.50, 0.0080, 0.060
vs = math.sqrt(2*g*h)
vp = (M+m)/m*vs
P(14, f"v_s = {vs:.4f} ~ 1,08 m/s ; v_p = {vp:.4f} ~ 204 m/s")
# 15 auto 1200 (15) tampona 900 ferma, agganciate
vf = 1200*15/2100
Eci = 0.5*1200*15**2; Ecf = 0.5*2100*vf**2
P(15, f"v_f = {vf:.4f} ~ 8,6 m/s ; E_ci = {Eci/1000:.0f} kJ, E_cf = {Ecf/1000:.1f} kJ, persi {(Eci-Ecf)/1000:.1f} kJ")
# 16 molla k=800 s=10 cm, blocco 0,50 kg, k_attr=0,25
d = (0.5*800*0.10**2) / (0.25*0.50*g)
P(16, f"d = (1/2 k s^2)/(k_a m g) = {d:.4f} ~ 3,3 m")
# 17 carrello 20 kg (3,0) + sacco 5,0 kg verticale
P(17, f"v_f = {20*3.0/25:.2f} m/s")
# 18 pallina gomma 40 g da 1,8 m rimbalza a 1,3 m
P(18, f"dE_m = m g (1,3-1,8) = {0.040*g*(1.3-1.8):.4f} ~ -0,20 J (anelastico)")
# 19 carrello 2,0 da piano 1,5 m poi urto anelastico con 2,0 fermo
v = math.sqrt(2*g*1.5)
vf = 2.0*v/4.0
P(19, f"v ai piedi = {v:.4f} ~ 5,4 m/s ; v_f dopo urto = {vf:.4f} ~ 2,7 m/s")
