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
