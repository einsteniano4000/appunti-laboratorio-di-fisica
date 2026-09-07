#!/usr/bin/env python3
# Verifica dei numeri del capitolo "Il moto nel piano" (cinematica, Unita' 7).
# Python puro, niente numpy.  g = 9,81 m/s^2 (come nel resto della dispensa).

import math

g = 9.81
PI = math.pi

def sez(t): print("\n" + "=" * 68 + "\n" + t + "\n" + "=" * 68)


# ===========================================================================
sez("1  Il moto circolare uniforme")

# es. svolto: trenino r = 2,50 m, T = 10,0 s
r, T = 2.50, 10.0
v = 2 * PI * r / T
ac = v**2 / r
print(f"trenino: v = 2 pi r / T = {v:.4f} m/s ~ {v:.2f} ; a_c = v^2/r = {ac:.4f} ~ {ac:.2f} m/s^2")

# es. svolto: cavallo giostra r = 4,0 m, T = 8,0 s
r, T = 4.0, 8.0
v = 2 * PI * r / T
print(f"cavallo giostra: v = {v:.4f} m/s ~ {v:.1f} = {v*3.6:.1f} km/h ; a_c = {v**2/r:.3f}")

# es. svolto: disco rigido 5400 rpm
f = 5400 / 60
print(f"disco 5400 rpm: f = {f:.1f} Hz ; T = 1/f = {1/f:.5f} s ~ {1000/f:.1f} ms")

# es. svolto: lancetta dei secondi r = 8,0 mm, T = 60 s
r, T = 8.0e-3, 60.0
f = 1 / T
v = 2 * PI * r / T
print(f"lancetta secondi: f = {f:.5f} Hz ~ 0,017 ; v = {v:.3e} m/s ~ 8,4e-4")

# es. svolto: a_c trenino
print(f"a_c trenino (v=1,57 r=2,50): {1.57**2/2.50:.4f} ~ 0,99")

print("\n--- esercizi §1 ---")
# automobilina r = 25 cm, T = 1,0 s
r, T = 0.25, 1.0
v = 2 * PI * r / T
print(f"automobilina: v = {v:.4f} ~ 1,57 m/s ; a_c = {v**2/r:.3f} ~ 9,9 m/s^2")
# elica 2400 rpm
f = 2400 / 60
print(f"elica 2400 rpm: f = {f:.1f} Hz ; T = {1/f:.4f} s")
# ruota bici d = 60 cm, v = 36 km/h
r = 0.30; v = 36 / 3.6
Tg = 2 * PI * r / v
print(f"ruota bici: T = 2 pi r / v = {Tg:.4f} s ~ 0,19")
# sasso corda L = 0,80 m, f = 2,0 Hz
r, f = 0.80, 2.0
v = 2 * PI * r * f
print(f"sasso corda: v = 2 pi r f = {v:.4f} ~ 10,1 m/s ; a_c = {v**2/r:.2f} ~ 126 m/s^2")
# lavatrice d = 40 cm, 1200 rpm
r = 0.20; f = 1200 / 60
v = 2 * PI * r * f
print(f"lavatrice: f = {f:.0f} Hz ; a_c = {v**2/r:.4g} ~ 3,2e3 m/s^2")
# Terra attorno al Sole
r, T = 1.5e11, 3.15e7
v = 2 * PI * r / T
print(f"Terra: v = {v:.4g} m/s ~ 2,99e4 = {v/1000:.1f} km/s ; a_c = {v**2/r:.4g} ~ 5,9e-3")


# ===========================================================================
sez("2  La velocita' angolare")

# 1 rad in gradi
print(f"1 rad = {360/(2*PI):.2f} gradi ~ 57,3")

# es. svolto: 60 gradi -> rad ; 2,0 rad -> gradi
print(f"60 gradi = pi/3 = {PI/3:.4f} rad ~ 1,05")
print(f"2,0 rad = {180*2.0/PI:.2f} gradi ~ 114,6")

# es. svolto: 90 gradi (pi/2) in 4,0 s
w = (PI/2) / 4.0
print(f"quarto di giro: omega = (pi/2)/4,0 = {w:.4f} rad/s ~ 0,39")

# es. svolto: piattaforma T = 0,10 s, r_A = 10 cm, r_B = 20 cm
T = 0.10
w = 2 * PI / T
print(f"piattaforma: omega = 2 pi / T = {w:.4f} rad/s ~ 63")
print(f"  v_A = omega r_A = {w*0.10:.4f} ~ 6,3 m/s ; v_B = {w*0.20:.4f} ~ 13 m/s")

print("\n--- esercizi §2 ---")
for deg in (30, 45, 120):
    print(f"{deg} gradi = {PI*deg/180:.4f} rad")
print(f"1,5 rad = {180*1.5/PI:.2f} gradi ~ 85,9")
# motore 1500 rpm
w = 2 * PI * (1500 / 60)
print(f"motore 1500 rpm: omega = {w:.3f} rad/s ~ 157")
# giostra T = 12 s, bambino r = 3,5 m
w = 2 * PI / 12
print(f"giostra T=12: omega = {w:.4f} ~ 0,52 rad/s ; v = omega*3,5 = {w*3.5:.3f} ~ 1,8 m/s")
# disco r = 20 cm, a_c max = g
r = 0.20
w = math.sqrt(g / r)
print(f"disco a_c<=g: omega_max = sqrt(g/r) = {w:.4f} ~ 7,0 rad/s")
# satellite r = 7,0e6 m, T = 2,0 h
r = 7.0e6; T = 2.0 * 3600
w = 2 * PI / T
v = w * r
print(f"satellite: T = {T:.0f} s ; omega = {w:.4g} ~ 8,7e-4 ; v = {v:.4g} ~ 6,1e3 m/s")
# pale elicottero L = 3,0 m, 540 rpm
r = 3.0; f = 540 / 60
w = 2 * PI * f
print(f"pale elicottero: omega = {w:.3f} ~ 56,5 rad/s ; v = {w*r:.2f} ~ 170 m/s")


# ===========================================================================
sez("3  Il moto armonico")

# es. svolto: molla A = 10 cm, omega = 1,25 rad/s, t = 1,0 s
A, w, t = 10.0, 1.25, 1.0
print(f"molla: cos(1,25) = {math.cos(1.25):.4f} ; s = {A*math.cos(w*t):.4f} cm ~ 3,2")

# grafico: cosinusoide ampiezza 10 cm
print("cosinusoide A=10: valori a 0, T/4, T/2, 3T/4, T:",
      [round(10*math.cos(x), 3) for x in (0, PI/2, PI, 3*PI/2, 2*PI)])

print("\n--- esercizi §3 ---")
# T = 2,00 s
print(f"T=2,00 s: omega = 2 pi / T = {2*PI/2.0:.4f} ~ 3,14 rad/s")
# A = 15 cm, T = 0,80 s
w = 2 * PI / 0.80
print(f"A=15 T=0,80: omega = {w:.4f} ~ 7,85 rad/s ; tabella s:",
      [round(15*math.cos(x), 2) for x in (0, PI/2, PI, 3*PI/2, 2*PI)])
# A = 8,0 cm, omega = 5,0 rad/s, t = 0,50 s
A, w, t = 8.0, 5.0, 0.50
print(f"A=8,0 omega=5,0 t=0,50: cos(2,5) = {math.cos(w*t):.4f} ; s = {A*math.cos(w*t):.4f} ~ -6,4 cm  (segno negativo: superato il centro)")
# corda violino f = 440 Hz
f = 440
print(f"violino: omega = 2 pi f = {2*PI*f:.1f} ~ 2765 rad/s ; T = {1/f:.3e} s ~ 2,3e-3")
# A = 6,0 cm, omega = 10 rad/s, a_max
A, w = 0.060, 10.0
print(f"a_max = omega^2 A = {w**2 * A:.3f} ~ 6,0 m/s^2")


# ===========================================================================
sez("4  Il moto parabolico")

# es. svolto: biglia tavolo h = 0,80 m, v0 = 2,0 m/s
h, v0 = 0.80, 2.0
t = math.sqrt(2 * h / g)
print(f"biglia tavolo: t = sqrt(2h/g) = {t:.4f} s ~ 0,40 ; x = v0 t = {v0*t:.4f} ~ 0,81 m")

# es. svolto: pallone v0 = 22 m/s, alpha = 30
v0 = 22.0
vx = v0 * math.cos(math.radians(30))
vy = v0 * math.sin(math.radians(30))
hmax = vy**2 / (2 * g)
tvolo = 2 * vy / g
sx = 2 * vx * vy / g
print(f"pallone 22 @30: vx = {vx:.4f} ~ 19,1 ; vy = {vy:.4f} = 11,0")
print(f"  h = vy^2/2g = {hmax:.4f} ~ 6,2 m ; t_volo = 2 vy/g = {tvolo:.4f} ~ 2,2 s ; gittata = {sx:.4f} ~ 42,8 m")

print("\n--- esercizi §4 ---")
# mela tavolo h = 0,85 m, v = 0,40 m/s
h, v0 = 0.85, 0.40
t = math.sqrt(2 * h / g)
print(f"mela: t = {t:.4f} ~ 0,42 s ; x = {v0*t:.4f} ~ 0,17 m")
# aereo 360 km/h, quota 500 m
h, v0 = 500.0, 360 / 3.6
t = math.sqrt(2 * h / g)
print(f"aereo: t = {t:.4f} ~ 10,1 s ; x = {v0*t:.4f} ~ 1,0e3 m")
# arciere v0 = 75 m/s, bersaglio 50 m
v0, sx = 75.0, 50.0
t = sx / v0
print(f"arciere: t = {t:.4f} ~ 0,67 s ; y = 0,5 g t^2 = {0.5*g*t**2:.4f} ~ 2,2 m")
# calciatore v0 = 18 m/s @45, sin=cos~0,71
v0 = 18.0
vx = vy = v0 * 0.71
print(f"calciatore 18 @45: vx=vy = {vx:.4f} ~ 12,7 ; h = {vy**2/(2*g):.4f} ~ 8,3 m (esatto {v0*math.sin(math.radians(45)):.3f}->{(v0*math.sin(math.radians(45)))**2/(2*g):.3f}) ; sx = {2*vx*vy/g:.3f} ~ 33 m")
# biglia orizz. v = 15 m/s, t = 2,0 s
v0, t = 15.0, 2.0
print(f"biglia 15, t=2,0: h = 0,5 g t^2 = {0.5*g*t**2:.4f} ~ 19,6 m ; x = {v0*t:.1f} = 30 m")
# pallavolo v0 = 9,0 m/s @60, sin60~0,87
v0 = 9.0
vy = v0 * 0.87
print(f"pallavolo 9,0 @60: vy = {vy:.4f} ~ 7,8 ; h = {vy**2/(2*g):.4f} ~ 3,1 m")


# ===========================================================================
sez("5  La composizione dei moti")

# es. svolto: nuotatore L = 60 m, v' = 1,5 m/s, corrente 1,2 m/s
L, vr, vc = 60.0, 1.5, 1.2
t = L / vr
d = vc * t
vass = math.hypot(vr, vc)
print(f"nuotatore: t = L/v' = {t:.1f} s ; d = vc t = {d:.1f} m ; v = sqrt(1,5^2+1,2^2) = {vass:.4f} ~ 1,9 m/s")

# biglia sul vagone (testo): 10+15 = 25 ; -10+15 = 5 ; velocita 1,0+1,5 = 2,5
print("biglia vagone: 25 m / 5 m ; 2,5 m/s")

print("\n--- esercizi §5 ---")
print(f"vagone 5,0 + biglia 2,0: {5.0+2.0} m/s ; verso opposto {5.0-2.0} m/s")
# vagone 10 m in 2 s, biglia 5 m perpend.
ds = math.hypot(10.0, 5.0)
print(f"vagone 10 perp biglia 5: ds = {ds:.4f} ~ 11,2 m ; v = ds/2,0 = {ds/2.0:.4f} ~ 5,6 m/s")
# motoscafo v' = 10, fiume 300 m, corrente 4,0
L, vr, vc = 300.0, 10.0, 4.0
t = L / vr
print(f"motoscafo: t = {t:.0f} s ; d = {vc*t:.0f} m ; v = {math.hypot(vr,vc):.4f} ~ 10,8 m/s")
# passeggero 1,5 m/s su treno 90 km/h
print(f"passeggero: 25 + 1,5 = {25+1.5} m/s = {(25+1.5)*3.6:.1f} km/h ~ 95,4")
# aereo 200 km/h N, vento 60 km/h E
print(f"aereo+vento: v = sqrt(200^2+60^2) = {math.hypot(200,60):.3f} ~ 209 km/h")
# cannone su vagone v0 = 300 @45, vagone 20
v0 = 300.0
vx = v0 * 0.71 + 20
vy = v0 * 0.71
print(f"cannone: vx = 212 + 20 = {vx:.1f} ~ 232 ; vy = {vy:.1f} ~ 212 m/s")


# ===========================================================================
sez("Problemi di riepilogo")

def P(n, s): print(f"{n:>2}. {s}")

# 1 ruota panoramica d = 60 m, T = 4 min
r, T = 30.0, 4*60
v = 2*PI*r/T
P(1, f"v = {v:.4f} ~ 0,79 m/s ; a_c = {v**2/r:.5f} ~ 0,021 m/s^2")
# 2 circonf r = 50 cm, f = 3,0 Hz
r, f = 0.50, 3.0
w = 2*PI*f; v = w*r
P(2, f"T = {1/f:.4f} ~ 0,33 s ; omega = {w:.4f} ~ 18,8 ; v = {v:.4f} ~ 9,4 ; a_c = {v**2/r:.2f} ~ 178")
# 3 disco 3000 rpm, r = 12 cm
w = 2*PI*(3000/60); r = 0.12
P(3, f"omega = {w:.3f} ~ 314 rad/s ; v = {w*r:.4f} ~ 38 m/s")
# 4 pulegge r1 = 5 cm r2 = 15 cm, omega1 = 20 rad/s
v = 20*0.05
P(4, f"v = {v:.2f} m/s ; omega2 = v/0,15 = {v/0.15:.4f} ~ 6,7 rad/s")
# 5 bambino giostra r = 2,5 m, arco 4,0 m in 5,0 s
v = 4.0/5.0
P(5, f"v = {v:.2f} m/s ; omega = v/2,5 = {v/2.5:.3f} ~ 0,32 rad/s")
# 6 auto curva r = 80 m, v = 72 km/h
v = 72/3.6; r = 80.0
ac = v**2/r
P(6, f"a_c = {ac:.3f} = 5,0 m/s^2 ; /g = {ac/g:.3f} ~ 0,51")
# 7 moto armonico A = 12 cm, f = 2,5 Hz, t = 0,050 s
w = 2*PI*2.5
P(7, f"omega = {w:.4f} ~ 15,7 ; s(0,050) = 12*cos({w*0.050:.4f}) = {12*math.cos(w*0.050):.4f} ~ 8,5 cm")
# 8 peso molla A = 8,0 cm, T = 0,60 s
w = 2*PI/0.60
P(8, f"omega = {w:.4f} ~ 10,5 ; a_max = omega^2 A = {w**2*0.08:.4f} ~ 8,8 m/s^2")
# 9 sasso orizz. torre 45 m, v = 12 m/s
h, v0 = 45.0, 12.0
t = math.sqrt(2*h/g)
P(9, f"t = {t:.4f} ~ 3,0 s ; x = {v0*t:.4f} ~ 36 m")
# 10 due biglie tavolo 1,0 m, v = 1,0 e 2,0
h = 1.0
t = math.sqrt(2*h/g)
P(10, f"t = {t:.4f} ~ 0,45 s ; x1 = {1.0*t:.4f} ~ 0,45 ; x2 = {2.0*t:.4f} ~ 0,90 m")
# 11 pallone v0 = 25 @30, cos30~0,87
v0 = 25.0
vx = v0*0.87; vy = v0*0.5
P(11, f"vx = {vx:.3f} ~ 21,7 ; vy = {vy:.1f} ; h = {vy**2/(2*g):.4f} ~ 8,0 ; t_volo = {2*vy/g:.4f} ~ 2,5 ; sx = {2*vx*vy/g:.3f} ~ 55 m")
# 12 proiettile 45, gittata 400 m -> v0
sx = 400.0
v0 = math.sqrt(g*sx)
P(12, f"v0 = sqrt(g sx) = {v0:.4f} ~ 63 m/s")
# 13 barca canale 80 m in 40 s, deriva 30 m
L, t, d = 80.0, 40.0, 30.0
vr = L/t; vc = d/t
P(13, f"v' = {vr:.2f} m/s ; v_t = {vc:.3f} ~ 0,75 ; v = {math.hypot(vr,vc):.4f} ~ 2,1 m/s")
# 14 nuotatore vuole arrivare di fronte: fiume 60, v'=1,5, vt=1,2
comp_util = math.sqrt(1.5**2 - 1.2**2)
P(14, f"comp controcorrente = 1,2 ; comp utile = sqrt(1,5^2-1,2^2) = {comp_util:.4f} ~ 0,9 ; t = 60/{comp_util:.3f} = {60/comp_util:.2f} ~ 67 s")
# 15 aereo A/R 400 km, v_aria 200 km/h, vento 100
P(15, f"senza vento: {2*400/200:.0f} h ; con vento: {400/300 + 400/100:.4f} h = 5 h 20 min")
# 16 centrifuga 10000 rpm, r = 8,0 cm
w = 2*PI*(10000/60); r = 0.08
v = w*r; ac = w**2*r
P(16, f"omega = {w:.3f} ~ 1047 ; v = {v:.3f} ~ 84 m/s ; a_c = {ac:.4g} ~ 8,8e4 = {ac/g:.0f} g")
# 17 a_c = 40 m/s^2, r = 2,5 m
r, ac = 2.5, 40.0
v = math.sqrt(ac*r); w = v/r
P(17, f"v = sqrt(a_c r) = {v:.2f} m/s ; omega = {w:.2f} rad/s ; T = {2*PI/w:.4f} ~ 1,6 s")
# 18 martello r = 1,9 m, v = 25 m/s
r, v = 1.9, 25.0
ac = v**2/r; f = v/(2*PI*r)
P(18, f"a_c = {ac:.3f} ~ 329 m/s^2 ; f = v/(2 pi r) = {f:.4f} ~ 2,1 Hz")
# 19 biglia orizz. tavolo 0,80 m, cade a 1,2 m
h, x = 0.80, 1.2
t = math.sqrt(2*h/g)
v0 = x/t
vfin = math.hypot(v0, g*t)
P(19, f"t = {t:.4f} ~ 0,40 s ; v0 = x/t = {v0:.4f} ~ 3,0 m/s ; v_finale = {vfin:.4f} ~ 4,9 m/s")
