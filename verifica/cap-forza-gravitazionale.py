#!/usr/bin/env python3
# Verifica dei numeri del capitolo "La forza gravitazionale" (Unita' 8, Lez. 7-8).
# Python puro, niente numpy.

import math

G = 6.67e-11
PI = math.pi
MT = 6.0e24      # massa Terra
RT = 6.4e6       # raggio Terra
g = 9.81

def sez(t): print("\n" + "=" * 68 + "\n" + t + "\n" + "=" * 68)


# ===========================================================================
sez("2  La legge di gravitazione universale")

# es. svolto: Terra-Luna
mL, d = 7.35e22, 3.84e8
F = G * MT * mL / d**2
print(f"Terra-Luna: F = {F:.4e} ~ 2,0e20 N")

# es. svolto: due sfere 1 kg a 20 cm
F = G * 1.0 * 1.0 / 0.20**2
print(f"due sfere 1 kg a 20 cm: F = {F:.4e} ~ 1,7e-9 N")

print("\n--- esercizi §2 ---")
# due navi 2,0e7 kg a 50 m
F = G * (2.0e7)**2 / 50**2
print(f"due navi: F = {F:.4e} ~ 11 N")
# distanza x3, poi massa x2
print(f"distanza x3 -> F x 1/9 ; poi massa x2 -> 2/9")
# tre sfere allineate A-B 3,0 m, B-C 2,0 m; forza su C
FBC = G * 1.0 * 1.0 / 2.0**2
FAC = G * 1.0 * 1.0 / 5.0**2
print(f"tre sfere: F_BC = {FBC:.4e} ; F_AC = {FAC:.4e} ; risultante (stesso verso) = {FBC+FAC:.4e} ~ 1,9e-11 N")


# ===========================================================================
sez("3  L'accelerazione di gravita'")

# es. svolto: Marte
MM, RM = 6.4e23, 3.4e6
gM = G * MM / RM**2
print(f"Marte: g = {gM:.4f} ~ 3,7 m/s^2  (Terra/Marte = {g/gM:.2f})")

# es. svolto: verifica Terra
print(f"Terra: g = G M/R^2 = {G*MT/RT**2:.4f} ~ 9,8 m/s^2")

print("\n--- esercizi §3 ---")
# Luna
ML, RL = 7.35e22, 1.74e6
gL = G * ML / RL**2
print(f"Luna: g = {gL:.4f} ~ 1,62 ; Terra/Luna = {g/gL:.2f}")
# pianeta M=2MT, R=2RT
print(f"pianeta 2M 2R: g = 2/4 * g_T = {0.5*g:.2f} m/s^2")
# altezza per g/2
h = RT * (math.sqrt(2) - 1)
print(f"g dimezzata: h = R(sqrt2 - 1) = {h:.4e} ~ 2,7e6 m")
# Sole
MS, RS = 2.0e30, 7.0e8
gS = G * MS / RS**2
print(f"Sole: g = {gS:.2f} ~ 272 m/s^2  (x{gS/g:.0f} Terra)")


# ===========================================================================
sez("4  Il moto dei satelliti")

# es. svolto: satellite h=500 km
h = 5.0e5
r = RT + h
v = math.sqrt(G * MT / r)
print(f"satellite h=500 km: r = {r:.2e} ; v = {v:.4e} ~ 7,6e3 m/s = {v/1000:.1f} km/s = {v*3.6:.0f} km/h")

# es. svolto: geostazionario h=35800 km
h = 3.58e7
r = RT + h
v = math.sqrt(G * MT / r)
T = 2 * PI * r / v
print(f"geostazionario: r = {r:.3e} ; v = {v:.4e} ~ 3,1e3 m/s ; T = {T:.4e} s = {T/3600:.2f} h")

print("\n--- esercizi §4 ---")
# h=800 km
r = RT + 8.0e5
print(f"h=800 km: r = {r:.2e} ; v = {math.sqrt(G*MT/r):.4e} ~ 7,5e3 m/s")
# ISS h=420 km
r = RT + 4.2e5
v = math.sqrt(G*MT/r)
print(f"ISS h=420 km: r = {r:.3e} ; v = {v:.4e} ~ 7,66e3 ; T = {2*PI*r/v:.4e} s = {2*PI*r/v/60:.1f} min")
# GPS r = 26600 km
r = 2.66e7
print(f"GPS r=26600 km: v = {math.sqrt(G*MT/r):.4e} ~ 3,9e3 m/s")
# satellite Luna h=100 km
r = RL + 1.0e5
print(f"orbita lunare h=100 km: r = {r:.3e} ; v = {math.sqrt(G*ML/r):.4e} ~ 1,6e3 m/s")


# ===========================================================================
sez("Problemi di riepilogo")

def P(n, s): print(f"{n:>2}. {s}")

# 2 due corpi 5 e 8 kg a 40 cm
P(2, f"F = G*5*8/0,16 = {G*5*8/0.16:.4e} ~ 1,7e-8 N")
# 3 F=6,0e-9, dimezzo r
P(3, f"F x4 = {6.0e-9*4:.2e} ~ 2,4e-8 N")
# 4 Terra attira 2,0 kg al suolo
P(4, f"F = G MT m / RT^2 = {G*MT*2.0/RT**2:.4f} ~ 19,6 N ; P = m g = {2.0*g:.2f} N  (differenza da arrotondamenti su MT, RT)")
# 5 pianeta M=MT, R=RT/2
P(5, f"g = 1/(0,5)^2 * g_T = {4*g:.1f} m/s^2")
# 6 Giove g=24,8, astronauta 120 kg
P(6, f"P_Terra = {120*g:.1f} N ; P_Giove = {120*24.8:.1f} N")
# 7 Venere M=4,87e24, R=6,05e6
P(7, f"g_Venere = {G*4.87e24/6.05e6**2:.4f} ~ 8,9 m/s^2")
# 8 satellite h=1200 km
r = RT + 1.2e6
v = math.sqrt(G*MT/r)
P(8, f"r = {r:.2e} ; v = {v:.4e} ~ 7,3e3 ; T = {2*PI*r/v:.4e} s = {2*PI*r/v/60:.1f} min")
# 9 v=6,0 km/s -> r
GM = 4.0e14
P(9, f"r = G MT / v^2 = {GM/(6.0e3)**2:.4e} ~ 1,1e7 m")
# 11 Sole-Terra
r = 1.5e11
F = G*2.0e30*MT/r**2
P(11, f"F = {F:.4e} ~ 3,6e22 N ; a_c = F/MT = {F/MT:.4e} ~ 5,9e-3 m/s^2")
# 12 due sfere, r=10 cm, F=6,67e-8 -> m
m = 0.10 * math.sqrt(6.67e-8 / G)
P(12, f"m = r sqrt(F/G) = 0,10*sqrt(1000) = {m:.4f} ~ 3,2 kg")
# 13 Marte r = 1,52 r_T -> T
P(13, f"T_M = 1,52^1,5 = {1.52**1.5:.4f} ~ 1,87 anni")
# 14 h per P/2
h = RT*(math.sqrt(2)-1)
P(14, f"h = R(sqrt2 - 1) = {h:.4e} ~ 2,65e6 m")
# 15 geostazionario v = 2 pi r / T
P(15, f"v = 2 pi * 4,22e7 / 86400 = {2*PI*4.22e7/86400:.4e} ~ 3,07e3 m/s")
