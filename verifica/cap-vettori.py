"""Verifica numerica di esempi ed esercizi del capitolo "Grandezze vettoriali e forze".
Eseguire con:  python3 verifica/cap-vettori.py
"""
import math


def risultante_perp(a, b):
    """Modulo e angolo (dal primo vettore) della somma di due vettori perpendicolari."""
    return math.hypot(a, b), math.degrees(math.atan2(b, a))


print("== Sezione 2: operazioni con i vettori ==")

# Esempio: spostamenti collineari
print("Esempio collineari: 8 m E poi 3 m E ->", 8 + 3, "m E")
print("Esempio collineari: 8 m E poi 3 m O ->", 8 - 3, "m E")

# Esempio: spostamenti perpendicolari 40 m E + 30 m N
R, ang = risultante_perp(40, 30)
print(f"Esempio perpendicolari 40 E + 30 N: R = {R:.1f} m, angolo da E = {ang:.1f} deg")

# Esempio: forze perpendicolari 6 N + 8 N
R, ang = risultante_perp(6, 8)
print(f"Esempio forze 6 N + 8 N perp.: R = {R:.1f} N, angolo dal primo = {ang:.1f} deg")

print()
print("== Esercizi proposti ==")

# E2: a = 12 (E), b = 5 (O), stessa retta
print("E2: |a+b| =", 12 - 5, "m verso E ;  |a-b| =", 12 + 5, "m verso E")

# E3: spostamenti perpendicolari 60 m e 80 m
R, ang = risultante_perp(60, 80)
print(f"E3: R = {R:.0f} m, angolo dal primo = {ang:.1f} deg")

# E4: v = 3 m/s, -2 v
print("E4: |-2 v| =", 2 * 3, "m/s, verso opposto a v")

# E5: forze perpendicolari 9 N e 12 N
R, ang = risultante_perp(9, 12)
print(f"E5: R = {R:.0f} N, angolo dal primo = {ang:.1f} deg")

print()
print("== Sezione 3: scomposizione ==")
# Esempio: v = 10 m, alpha = 30 deg
vy = 10 / 2
vx = math.sqrt(10 ** 2 - vy ** 2)
print(f"Esempio v=10 m a 30 deg: vy = {vy} m, vx = sqrt(75) = {vx:.2f} m")
# Esercizi
print("E(comp): vx=9, vy=12 -> v =", math.hypot(9, 12), "m")
print("E(60 deg, v=20): vx = 20/2 =", 20 / 2, "m ; vy =", math.sqrt(20 ** 2 - 10 ** 2), "m")
print("E(45 deg, F=50): Fx = Fy = 50/sqrt2 =", 50 / math.sqrt(2), "N")

print()
print("== Sezione 4: le forze ==")
g = 9.81
gm = 1.6
print(f"Esempio persona 70 kg: P_Terra = {70*g:.0f} N ; P_Luna = {70*gm:.0f} N")
print(f"E: 2.0 kg -> {2.0*g:.1f} N ;  0.5 kg -> {0.5*g:.1f} N")
print(f"E: oggetto 58.9 N -> m = {58.9/g:.2f} kg ; P_Luna = {58.9/g*gm:.1f} N")
