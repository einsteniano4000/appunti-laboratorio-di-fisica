#!/usr/bin/env python3
# Verifica dei numeri del capitolo "Lavoro ed energia" (Unita' 9).
# Python puro, niente numpy.

import math

g = 9.81

def sez(t): print("\n" + "=" * 68 + "\n" + t + "\n" + "=" * 68)
def ck(nome, val, atteso, tol=0.02):
    ok = abs(val - atteso) <= max(tol * abs(atteso), 1e-9)
    print(f"  [{'OK ' if ok else 'ERR'}] {nome}: {val:.4g}  (atteso {atteso:.4g})")


# ===========================================================================
sez("14.1  Il lavoro")

# es. svolto 104: spinta obliqua F=25 N, alpha=60, s=8,0 m
L = 25 * 8.0 * math.cos(math.radians(60))
ck("es. spinta obliqua L", L, 100)

# es. svolto 105: cassa, fune 250 N // , s=6,0 m, attrito 40 N
Lf = 250 * 6.0
La = -40 * 6.0
ck("L fune", Lf, 1500)
ck("L attrito", La, -240)
ck("L tot", Lf + La, 1260)
ck("L risultante", (250 - 40) * 6.0, 1260)

print("\n--- esercizi 14.1 ---")
# 357: F=60 N //, s=4,0 m; poi alpha=60
ck("357 L //", 60 * 4.0, 240)
ck("357 L a 60 gradi", 60 * 4.0 * math.cos(math.radians(60)), 120)

# 358: slitta s=12 m, F=120 N a 60, attrito 15 N
Lb = 120 * 12 * math.cos(math.radians(60))
La = -15 * 12
ck("358 L bambino", Lb, 720)
ck("358 L attrito", La, -180)
ck("358 L tot", Lb + La, 540)

# 359: piano inclinato h=4,0 l=30 m=25 kg attrito 25 N, v costante
m, h, l, Fa = 25, 4.0, 30, 25
Ppar = m * g * h / l
F = Ppar + Fa
L = F * l
ck("359 P_par", Ppar, 32.7, tol=0.03)
ck("359 F uomo", F, 57.7, tol=0.03)
ck("359 L uomo", L, 1731, tol=0.03)   # ~1,7e3 J

# 360: vassoio, lavoro nullo
ck("360 L", 8.0 * 10 * math.cos(math.radians(90)), 0, tol=1e-6)

# 361: attrito 12 N su 3,0 m
ck("361 L attrito", -12 * 3.0, -36)

# 362: 30 sollevamenti bilanciere 40 kg di 0,50 m
ck("362 L tot", 30 * 40 * g * 0.50, 5886, tol=0.03)  # ~5,9e3 J


# ===========================================================================
sez("14.2  Potenza e rendimento")

# es. due gru: L = 500*4,0; t = 25 s e 8,0 s
L = 500 * 4.0
ck("L (una gru)", L, 2000)
ck("P1 (25 s)", L / 25, 80)
ck("P2 (8,0 s)", L / 8.0, 250)

# es. auto: v=72 km/h -> 20 m/s, F=1500 N
v = 72 / 3.6
ck("v 72 km/h", v, 20)
ck("P auto", 1500 * v, 30000)

# es. montacarichi rendimento: Pa=5,0 kW, Pu=4,0 kW
ck("r montacarichi", 4.0 / 5.0, 0.80)
ck("P persa", 5.0 - 4.0, 1.0)

print("\n--- esercizi 14.2 ---")
# es: gru 600 kg, 18 m, 7,0 s
L = 600 * g * 18
ck("gru L", L, 1.06e5, tol=0.02)
ck("gru P", L / 7.0, 1.5e4, tol=0.02)

# es: auto 120 km/h, P=27 kW -> F
v = 120 / 3.6
ck("v 120 km/h", v, 33.33, tol=0.01)
ck("F attrito", 27000 / v, 810, tol=0.03)

# es: motore 2,0 kW, r=80%
ck("Pu motore", 0.80 * 2.0, 1.6)
E = 0.4e3 * 10 * 60
ck("E dissipata 10 min", E, 2.4e5)

# es: r=72%, Pu=400 W
ck("Pa", 400 / 0.72, 5.6e2, tol=0.02)

# es: 90 kW in HP
ck("HP", 90000 / 745.7, 121, tol=0.02)

# es: montacarichi 4000 N, 45 m, 40 s
L = 4000 * 45
ck("montac. L", L, 1.8e5)
ck("montac. P", L / 40, 4.5e3)

# es: 20 trazioni, 70 kg, 0,30 m, 40 s
L = 20 * 70 * g * 0.30
ck("trazioni L", L, 4120, tol=0.02)
ck("trazioni P", L / 40, 103, tol=0.02)


# ===========================================================================
sez("14.3  L'energia cinetica")

# es. auto 1000 kg a 108 km/h
v = 108 / 3.6
ck("v 108 km/h", v, 30)
Ec = 0.5 * 1000 * v**2
ck("Ec auto", Ec, 4.5e5)
ck("Ec a 54 km/h (1/4)", 0.5 * 1000 * (v/2)**2, 1.125e5)

# es. lavoro dei freni: 1000 kg da 30 m/s, s = 50 m
Ltot = 0 - 0.5 * 1000 * 30**2
ck("L freni", Ltot, -4.5e5)
ck("F frenante media", 4.5e5 / 50, 9.0e3)

# spazio di frenata: v = 25 m/s, k = 0,70 e 0,40
v = 90 / 3.6
ck("v 90 km/h", v, 25)
ck("s asciutto (k=0,70)", v**2 / (2 * 0.70 * g), 46, tol=0.03)
ck("s bagnato (k=0,40)", v**2 / (2 * 0.40 * g), 80, tol=0.03)

print("\n--- esercizi 14.3 ---")
ck("pallone Ec", 0.5 * 0.430 * 25**2, 134, tol=0.02)
dEc = 0.5 * 1200 * ((90/3.6)**2 - (36/3.6)**2)
ck("auto dEc", dEc, 3.15e5)
ck("biglia v", math.sqrt(2 * 0.60 / 0.030), 6.3, tol=0.02)
Lattr = -0.5 * 5.0 * 8.0**2
ck("blocco L attr", Lattr, -160)
ck("blocco F attr", 160 / 5.0, 32)
ck("blocco k", 32 / (5.0 * g), 0.65, tol=0.02)
v1, v2 = 100/3.6, 130/3.6
s1, s2 = v1**2/(2*0.65*g), v2**2/(2*0.65*g)
ck("s1 (100 km/h)", s1, 60, tol=0.03)
ck("s2 (130 km/h)", s2, 102, tol=0.03)
ck("aumento s", s2 - s1, 42, tol=0.05)
ck("freccia v", math.sqrt(2 * 45 / 0.025), 60)


# ===========================================================================
sez("14.4  L'energia potenziale")

# es. masso 200 kg, h = 15 m
ck("Ep masso (strada)", 200 * g * 15, 2.9e4, tol=0.02)
ck("Ep masso (burrone, h=40)", 200 * g * 40, 7.8e4, tol=0.02)

# es. cassa con attrito: P = 100 W, t = 15 s, m = 20 kg, h = 6,0 m
L = 100 * 15
dEp = 20 * g * 6.0
ck("cassa L macchina", L, 1500)
ck("cassa dEp", dEp, 1177, tol=0.01)
ck("cassa E dissipata", L - dEp, 3.2e2, tol=0.05)

print("\n--- esercizi 14.4 ---")
ck("cemento Ep suolo", 25 * g * 9.0, 2.2e3, tol=0.02)
ck("cemento Ep 1o piano", 25 * g * 6.0, 1.5e3, tol=0.02)
ck("cassa L peso (3 modi)", -18 * g * 2.5, -4.4e2, tol=0.02)
ck("secchio h", 900 / 120, 7.5)
ck("ascensore dEp", 260 * g * 15, 3.8e4, tol=0.02)


# ===========================================================================
sez("14.5  Lavoro ed energia nei corpi elastici")

# es. flipper: k = 800 N/m, s = 4,0 cm, m = 30 g
Ee = 0.5 * 800 * 0.040**2
ck("flipper Ee", Ee, 0.64)
ck("flipper v", math.sqrt(2 * Ee / 0.030), 6.5, tol=0.02)

print("\n--- esercizi 14.5 ---")
ck("molla Ee (8 cm)", 0.5 * 500 * 0.080**2, 1.6)
Ee = 0.5 * 300 * 0.050**2
ck("fucile Ee", Ee, 0.375)
ck("fucile v", math.sqrt(2 * Ee / 0.010), 8.7, tol=0.02)
ck("molla 1 s (E=2 J, k=200)", math.sqrt(2 * 2.0 / 200), 0.14, tol=0.03)
ck("molla 2 s (E=2 J, k=800)", math.sqrt(2 * 2.0 / 800), 0.071, tol=0.03)


# ===========================================================================
sez("14.6  I mille volti dell'energia")

# 1 kWh
ck("1 kWh in J", 1000 * 3600, 3.6e6)

# es. forno 2,2 kW per 40 min
ck("forno E (kWh)", 2.2 * 40/60, 1.5, tol=0.03)
ck("forno E (J)", 2200 * 2400, 5.28e6)

print("\n--- esercizi 14.6 ---")
E = 1000 * g * 18
ck("auto terrazza E (J)", E, 1.77e5, tol=0.02)
ck("auto terrazza E (kWh)", E / 3.6e6, 0.049, tol=0.03)
Eps = 1500 * g * 220
ck("centrale Ep/s", Eps, 3.24e6, tol=0.02)
ck("centrale P (88%)", 0.88 * Eps, 2.8e6, tol=0.03)


# ===========================================================================
sez("Problemi di riepilogo")

ck("P2 operaio L //", 180 * 7.5, 1350)
ck("P2 operaio L a 30 gradi", 180 * 7.5 * math.cos(math.radians(30)), 1169, tol=0.01)
ck("P3 gru L", 350 * g * 12, 4.1e4, tol=0.02)
ck("P3 gru P", 350 * g * 12 / 8.0, 5.2e3, tol=0.02)
ck("P4 tapis F", 1500 / 0.80, 1.9e3, tol=0.02)
ck("P5 pompa L", 600 * g * 15, 8.8e4, tol=0.02)
ck("P5 pompa P", 600 * g * 15 / 120, 7.4e2, tol=0.02)
ck("P6 montac. E assorbita", 2500 * 9.0 / 0.75, 3.0e4)
ck("P7a auto Ec", 0.5 * 1200 * (90/3.6)**2, 3.8e5, tol=0.02)
ck("P7b TIR Ec", 0.5 * 15000 * (72/3.6)**2, 3.0e6)
ck("P7c proiettile Ec", 0.5 * 0.012 * 350**2, 735)
ck("P8 baseball v", math.sqrt(2 * 108 / 0.145), 38.6, tol=0.02)
ck("P8 baseball v km/h", math.sqrt(2 * 108 / 0.145) * 3.6, 139, tol=0.02)
ck("P9 auto Ltot", 0.5 * 900 * ((108/3.6)**2 - (36/3.6)**2), 3.6e5)
ck("P10 blocco F attr", 0.5 * 4.0 * 6.0**2 / 3.0, 24)
ck("P10 blocco k", (0.5 * 4.0 * 6.0**2 / 3.0) / (4.0 * g), 0.61, tol=0.02)
ck("P11 s frenata", (100/3.6)**2 / (2 * 0.65 * g), 60, tol=0.03)
ck("P12 freccia v", math.sqrt(2 * 45 / 0.025), 60)
ck("P13 sabbia Ep", 30 * g * 8.0, 2.4e3, tol=0.02)
ck("P14 cassa F_par", 18 * g * 2.5 / 6.0, 73.6, tol=0.02)
ck("P14 cassa L forza", 18 * g * 2.5 / 6.0 * 6.0, 441, tol=0.02)
ck("P15 secchio h", 900 / 120, 7.5)
L = 100 * 15
dEp = 20 * g * 6.0
ck("P16 E dissipata", L - dEp, 3.2e2, tol=0.05)
ck("P16 rendimento", dEp / L, 0.78, tol=0.02)
ck("P17 molla Ee", 0.5 * 500 * 0.080**2, 1.6)
ck("P17 molla Ee doppia", 0.5 * 500 * 0.160**2, 6.4)
Ee = 0.5 * 300 * 0.050**2
ck("P18 dardo v", math.sqrt(2 * Ee / 0.010), 8.7, tol=0.02)
ck("P19 forno kWh", 2.2 * 40/60, 1.5, tol=0.03)
ck("P19 forno J", 1.5 * 3.6e6, 5.3e6, tol=0.03)
ck("P20 centrale P", 0.88 * 1500 * g * 220, 2.8e6, tol=0.03)

print("\nTutte le verifiche completate.")
