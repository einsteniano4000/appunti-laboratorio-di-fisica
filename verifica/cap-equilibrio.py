"""Verifica numerica di esempi ed esercizi del capitolo "Equilibrio dei corpi solidi".
Eseguire con:  python3 verifica/cap-equilibrio.py
"""
import math

g = 9.81

print("== 7.1 Equilibrio del punto materiale ==")
print("Esempio lampada 30 N su 2 fili -> ogni filo", 30 / 2, "N")
print("E: forze perp 6 e 8 N -> equilibrante", math.hypot(6, 8), "N")

print()
print("== 7.2 Equilibrio e attrito ==")
# Esempio slitta P=100 N, l=2.6 m, h=1.3 m
print("Esempio slitta: P_par =", 100 * 1.3 / 2.6, "N")
# Esempio cassa 5 kg su 20 deg, ks=0.5
P = 5 * g
Ppar = P * math.sin(math.radians(20))
Pperp = P * math.cos(math.radians(20))
print(f"Esempio cassa: P={P:.0f} N  P_par~{P*0.34:.0f}  P_perp~{P*0.94:.0f}  ks*P_perp~{0.5*P*0.94:.0f}"
      f"  -> {'ferma' if 0.34 < 0.5*0.94 else 'scivola'}")
print(f"  tan(20)={math.tan(math.radians(20)):.2f} < ks=0.50 -> ferma")
# Esercizi
print("E: piano l=3.0 h=1.5, P=80 N liscio -> F =", 80 * 1.5 / 3.0, "N")
print("E: ks=0.70 -> alpha0 =", round(math.degrees(math.atan(0.70))), "deg")
print("E: alpha0=22 deg -> ks = tan(22) =", round(math.tan(math.radians(22)), 2))

print()
print("== 7.3 Equilibrio del corpo rigido ==")
print("Esempio chiave: M = 100 N * 0.20 m =", 100 * 0.20, "N m")
print("Esempio altalena: b2 = 300*2.0/400 =", 300 * 2.0 / 400, "m")
print("E: porta F=30 N a 0.15 m -> M =", 30 * 0.15, "N m")
print("E: asta F1=250 a 0.80 m, b2=0.50 -> F2 =", 250 * 0.80 / 0.50, "N")
print("E: chiave dinamom. M_max=40, L=0.40 -> F_max =", 40 / 0.40, "N")

print()
print("== 7.4 Coppie di forze ==")
print("Esempio volante: M = 20 N * 0.36 m =", round(20 * 0.36, 1), "N m")
print("E: righello 5 N, b=0.20 m -> M =", 5 * 0.20, "N m")
print("E: tappo 8 N, d=0.040 m -> M =", 8 * 0.040, "N m")

print()
print("== 7.5 Macchine semplici e leve ==")
print("Esempio masso: Fm = 1000*0.20/1.0 =", 1000 * 0.20 / 1.0, "N  G =", 1.0 / 0.20)
print("Esempio avambraccio: Fm = 50*0.35/0.04 =", round(50 * 0.35 / 0.04),
      "N  G =", round(50 / (50 * 0.35 / 0.04), 2))
print("E: Fr=4500, G=6 -> Fm =", 4500 / 6, "N")
print("E: bm=0.90, br=0.30 -> G =", round(0.90 / 0.30))
print("E: carriola 800 N, br=0.30, bm=1.5 -> Fm =", 800 * 0.30 / 1.5, "N")
print("E: schiaccianoci Fm=40, bm=0.12, br=0.03 -> Fr =", 40 * 0.12 / 0.03, "N")

print()
print("== 7.6 Baricentro e stabilita' ==")
print("Esempio cassa base 40 cm, B a 60 cm -> tan a =", round(0.20 / 0.60, 2),
      "-> a =", round(math.degrees(math.atan(0.20 / 0.60))), "deg")
print("E armadio base 50 cm, B a 90 cm -> tan a =", round(0.25 / 0.90, 2),
      "-> a =", round(math.degrees(math.atan(0.25 / 0.90)), 1), "deg")

print()
print("== 7.7 Problemi di riepilogo ==")
print("P2  forze perp 5 e 12 -> equilibrante", math.hypot(5, 12), "N")
print("P4  piano l=4.0 h=1.0, P=60 -> F =", 60 * 1.0 / 4.0, "N")
print("P5  ks=0.45 -> alpha0 =", round(math.degrees(math.atan(0.45))), "deg")
print("P6  15 deg: tan =", round(math.tan(math.radians(15)), 2), "< 0.40 -> non scivola")
print("P7  cassa 20 kg su 25 deg liscio -> F =", round(20 * g * math.sin(math.radians(25))), "N")
print("P8  M = 25*0.30 =", 25 * 0.30, "N m")
print("P9  altalena b2 = 250*1.8/300 =", 250 * 1.8 / 300, "m")
print("P10 asta F = 400*0.25/1.0 =", 400 * 0.25 / 1.0, "N")
print("P11 coppia M = 6*0.30 =", round(6 * 0.30, 1), "N m")
print("P12 leva Fm = 3000/5 =", 3000 / 5, "N")
print("P13 carriola Fm = 900*0.35/1.4 =", round(900 * 0.35 / 1.4), "N")
print("P14 chiave F = 30/0.25 =", 30 / 0.25, "N")
print("P16 cassa 50x50 -> tan a = 1 -> a = 45 deg")
