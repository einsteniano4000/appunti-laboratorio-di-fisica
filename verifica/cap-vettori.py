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
