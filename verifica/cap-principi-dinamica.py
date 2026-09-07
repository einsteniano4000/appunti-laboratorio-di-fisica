#!/usr/bin/env python3
# Verifica dei numeri del capitolo "I princìpi della dinamica" (Unita' 8, Lez. 1-6).
# Python puro, niente numpy.  g = 9,81 m/s^2 (come nel resto della dispensa).

import math

g = 9.81
PI = math.pi

def sez(t): print("\n" + "=" * 68 + "\n" + t + "\n" + "=" * 68)


# ===========================================================================
sez("2  Il secondo principio")

# es. svolto: F = m a
m, a = 3.0, 2.0
print(f"F = m a = {m*a:.1f} N ; stessa F su 6 kg -> a = {m*a/6.0:.1f} m/s^2")

# es. svolto: bob a due, 2*100 N, m = 180 kg, t = 4,0 s
F = 2 * 100.0
m = 180.0
a = F / m
print(f"bob: a = 200/180 = {a:.4f} ~ 1,1 m/s^2 ; v = a t = {a*4.0:.4f} ~ 4,4 m/s")

# es. svolto: peso astronauta 80 kg su Terra e Luna
m = 80.0
print(f"astronauta: P_T = {m*g:.1f} ~ 785 N ; P_L = {m*1.6:.1f} = 128 N")

print("\n--- esercizi §2 ---")
print(f"F=12 N su m=4,0 kg: a = {12/4.0:.1f} ; v(5 s) = {12/4.0*5:.0f} m/s")
print(f"auto 1200 kg, 0->25 m/s in 10 s: a = {25/10:.1f} ; F = {1200*25/10:.0f} N")
print(f"due forze perp 6 e 8 N su 2 kg: F_ris = {math.hypot(6,8):.0f} ; a = {math.hypot(6,8)/2.0:.1f}")
print(f"carrello a=3,0, massa doppia: a = {3.0/2:.1f} m/s^2")
print(f"pattinatore 60 kg, 0->4,0 in 2,0 s: a = {4.0/2.0:.1f} ; F = {60*4.0/2.0:.0f} N")
print(f"sasso 0,50 kg caduta: P = {0.50*g:.2f} N, a = g ; 2,0 kg: P = {2.0*g:.1f} N, a = g")


# ===========================================================================
sez("3  Il terzo principio")

# es. svolto: rinculo, proiettile 10 g, a = 2,0e5
mp, ap = 0.010, 2.0e5
print(f"rinculo: F = m a = {mp*ap:.0f} N")

print("\n--- esercizi §3 ---")
# persona 70 kg salta da barca 140 kg, barca a=1,0
F = 140 * 1.0
print(f"barca: F = {F:.0f} N ; persona a = {F/70:.1f} m/s^2")


# ===========================================================================
sez("4  Applicazioni dei tre principi")

# es. svolto: paracadutista P=980 N, h=24
P, h = 980.0, 24.0
vr = math.sqrt(P / h)
print(f"paracadutista: v_r = sqrt(980/24) = {vr:.4f} ~ 6,4 m/s")

# es. svolto: piano inclinato h/l=0,50, m=20 kg, Fa=4,0 N
hl, m, Fa = 0.50, 20.0, 4.0
a = g * hl - Fa / m
print(f"piano incl. h/l=0,5 attrito 4 N: a = {g*hl:.3f} - {Fa/m:.2f} = {a:.4f} ~ 4,7 m/s^2")

# es. svolto: sasso ruotato m=300 g, r=1,5 m, v=10 m/s
m, r, v = 0.30, 1.5, 10.0
print(f"sasso ruotato: F_c = m v^2/r = {m*v**2/r:.1f} N")

print("\n--- esercizi §4 ---")
# corpo 5 kg piano liscio l=4 h=1
P5 = 5.0 * g
print(f"5 kg piano l=4 h=1: P_par = {P5*1.0/4.0:.3f} ~ 12,3 N ; a = {g*1.0/4.0:.4f} ~ 2,45")
# cassa 15 kg scivolo l=5 h=3 attrito 12 N
print(f"cassa 15 kg l=5 h=3 attr 12: a = {g*0.60:.3f} - {12/15:.2f} = {g*0.60 - 12/15:.4f} ~ 5,1")
# auto 900 kg curva r=50 v=54 km/h
v = 54/3.6
print(f"auto curva: v = {v:.0f} m/s ; F_c = {900*v**2/50:.0f} N")
# pallina 95 g pista r=90 cm v=1,2
print(f"pallina 95 g: F_c = {0.095*1.2**2/0.90:.4f} ~ 0,15 N")
# secchio verticale r=1,0 m, v_min nel punto alto
print(f"secchio verticale r=1,0: v_min = sqrt(g r) = {math.sqrt(g*1.0):.4f} ~ 3,1 m/s")


# ===========================================================================
sez("5  Le forze apparenti")

# es. svolto: giostra m=60 kg, r=1,0 m, omega=0,50
m, r, w = 60.0, 1.0, 0.50
print(f"giostra: F_cf = m w^2 r = {m*w**2*r:.1f} N")

# es. svolto: bilancia in ascensore m=40 kg
m = 40.0
print(f"ascensore fermo: R = m g = {m*g:.1f} ~ 392 N ; sale a=1,0: R = m(g+a) = {m*(g+1.0):.1f} ~ 432 N")

print("\n--- esercizi §5 ---")
print(f"passeggero 70 kg treno frena 1,5: F_ap = {70*1.5:.0f} N (in avanti)")
print(f"centrifuga provetta 15 g, w=100, r=8 cm: F_cf = {0.015*100**2*0.080:.0f} N")
print(f"ascensore scende a=2,0, m=60: R = m(g-a) = {60*(g-2.0):.1f} ~ 469 N")


# ===========================================================================
sez("6  Il moto oscillatorio")

# es. svolto: oscillatore m=0,10 kg, k=400 N/m
m, k = 0.10, 400.0
T = 2 * PI * math.sqrt(m / k)
print(f"oscillatore: T = 2 pi sqrt(m/k) = {T:.4f} ~ 0,10 s")

# es. svolto: pendolo l=1,0 m
l = 1.0
T = 2 * PI * math.sqrt(l / g)
print(f"pendolo l=1,0: T = 2 pi sqrt(l/g) = {T:.4f} ~ 2,0 s")

print("\n--- esercizi §6 ---")
# oscillatore m=0,25 kg, k=100
m, k = 0.25, 100.0
T = 2 * PI * math.sqrt(m / k)
print(f"osc. m=0,25 k=100: T = {T:.4f} ~ 0,31 s ; f = {1/T:.4f} ~ 3,2 Hz")
# molle k e 4k
print(f"molle k e 4k: T2/T1 = 1/sqrt(4) = {1/math.sqrt(4):.2f} (meta')")
# pendolo l=2,0 m su Luna e Terra
print(f"pendolo l=2,0: T_Luna = {2*PI*math.sqrt(2.0/1.6):.4f} ~ 7,0 s ; T_Terra = {2*PI*math.sqrt(2.0/9.81):.4f} ~ 2,8 s ; rapporto {math.sqrt(9.81/1.6):.2f}")
# pendolo l=0,994 m, T=2,00 s -> g
l, T = 0.994, 2.00
print(f"pendolo l=0,994 T=2,00: g = 4 pi^2 l / T^2 = {4*PI**2*l/T**2:.4f} ~ 9,81")


# ===========================================================================
sez("Problemi di riepilogo")

def P(n, s): print(f"{n:>2}. {s}")

# 1 F=20 N su 8 kg per 6 s
a1 = 20/8.0
P(1, f"a = {a1:.1f} ; v = {a1*6:.0f} m/s ; ds = {0.5*a1*36:.0f} m")
# 2 ascensore 500 kg, a=1,2 sale
P(2, f"T = m(g+a) = 500*{g+1.2:.2f} = {500*(g+1.2):.1f} ~ 5505 N")
# 3 auto 1000 kg 0->100 km/h in 8 s
a3 = (100/3.6)/8.0
P(3, f"a = {a3:.3f} ~ 3,5 ; F = {1000*a3:.1f} ~ 3470 N")
# 4 corpo 3 kg: 10+5-3 = 12 N
P(4, f"F_ris = {10+5-3} N ; a = {(10+5-3)/3.0:.1f} m/s^2")
# 5 cassa 25 kg, spinta 80, attrito 30
a5 = (80-30)/25.0
P(5, f"a = {a5:.1f} ; v(4 s) = {a5*4:.1f} m/s")
# 6 blocco 40 kg appeso
P(6, f"fermo: {40*g:.1f} ; sale a=2: {40*(g+2):.1f} ; scende a=2: {40*(g-2):.1f} N")
# 7 pattinatori 50 e 75 kg, primo a=3,0
P(7, f"F = 50*3,0 = {50*3.0:.0f} N ; secondo a = {50*3.0/75:.1f} m/s^2")
# 8 corpo 10 kg piano liscio l=6 h=2,4
a8 = g*2.4/6.0
P(8, f"a = g h/l = {a8:.4f} ~ 3,92 ; v in fondo = sqrt(2 a l) = {math.sqrt(2*a8*6.0):.4f} ~ 6,9 m/s")
# 9 stesso piano con attrito 15 N
P(9, f"a = {a8:.3f} - {15/10:.1f} = {a8 - 15/10:.4f} ~ 2,4 m/s^2")
# 10 paracadutista P=800, v_r=5,5 -> h
P(10, f"h = P/v_r^2 = 800/{5.5**2:.2f} = {800/5.5**2:.3f} ~ 26,4")
# 11 sasso 0,20 kg fionda r=0,80, f=3,0 Hz
v11 = 2*PI*0.80*3.0
P(11, f"v = 2 pi r f = {v11:.4f} ~ 15,1 ; F_c = m v^2/r = {0.20*v11**2/0.80:.2f} ~ 57 N")
# 12 dosso r=40 m, v perde contatto
P(12, f"v = sqrt(g r) = {math.sqrt(g*40):.4f} ~ 19,8 m/s = {math.sqrt(g*40)*3.6:.1f} km/h")
# 13 giostra r=3,0 m, giro in 6,0 s, m=45
w13 = 2*PI/6.0
P(13, f"omega = {w13:.4f} ~ 1,05 ; F_cf = m w^2 r = {45*w13**2*3.0:.1f} ~ 148 N")
# 14 bilancia segna 660 N, m=55
P(14, f"a = R/m - g = 660/55 - {g:.2f} = {660/55 - g:.4f} ~ 2,2 m/s^2 (verso l'alto)")
# 15 oscillatore m=0,50 k=200
T15 = 2*PI*math.sqrt(0.50/200)
P(15, f"T = {T15:.4f} ~ 0,31 s ; massa doppia -> T = {T15*math.sqrt(2):.4f} ~ 0,44 s")
# 16 pendolo l=25 cm
T16 = 2*PI*math.sqrt(0.25/g)
P(16, f"T = {T16:.4f} ~ 1,0 s ; f = {1/T16:.4f} ~ 1,0 Hz")
# 17 lunghezza per T=1,0 s
P(17, f"l = g T^2 / (4 pi^2) = {g*1.0/(4*PI**2):.4f} ~ 0,25 m")
# 18 carrello 2,0 kg + pesetto 0,50 kg
P(18, f"a = m_p g / (m_c + m_p) = {0.50*g/2.5:.4f} ~ 1,96 m/s^2")
# 19 auto 1100 kg curva r=60, attrito max 8000 N
vmax = math.sqrt(8000*60/1100)
P(19, f"v_max = sqrt(F r / m) = {vmax:.4f} ~ 20,9 m/s = {vmax*3.6:.1f} km/h")
