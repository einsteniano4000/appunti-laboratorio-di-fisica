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

print()
print("== Sezione 5: legge di Hooke ==")
print("Esempio k=200 N/m, F=5 N -> s =", 5 / 200, "m =", 5 / 200 * 100, "cm")
print("E: F=20 N, s=0.04 m -> k =", 20 / 0.04, "N/m")
print("E: k=150, m=1.2 kg -> F =", 1.2 * g, "N ; s =", 1.2 * g / 150 * 100, "cm")
print("E: k1=80, k2=240 -> rapporto allungamenti =", 240 / 80)

print()
print("== Sezione 6: operazioni sulle forze / piano inclinato ==")
print(f"Esempio m=5 kg, alpha=30: P={5*g:.1f} N  Ppar={5*g*math.sin(math.radians(30)):.1f}  Pperp={5*g*math.cos(math.radians(30)):.1f}")
print(f"E: m=10 kg, 30 deg -> Ppar={10*g*0.5:.1f} N  Pperp={10*g*math.cos(math.radians(30)):.1f} N")
print(f"E: P=20 N, 45 deg -> Ppar=Pperp={20/math.sqrt(2):.2f} N")
print("E: forze 15 dx + 6 sx ->", 15 - 6, "N dx ;  40 e 30 perp ->", math.hypot(40, 30), "N")

print()
print("== Sezione 7: attrito ==")
print(f"Esempio cassa 20 kg: Fp={20*g:.0f} N  Fas_max={0.5*20*g:.0f}  Fad={0.4*20*g:.0f}")
print("E: Fp=50 N, ks=0.6 -> Fas_max =", 0.6 * 50, "N ; forza 25 N < 30 -> fermo")
print(f"E: auto 1000 kg, kd=0.7 -> Fad = {0.7*1000*g:.0f} N")
print(f"E: P=80 N orizz. Fp=80 ; su 60 deg Fp = 80*cos60 = {80*math.cos(math.radians(60)):.0f} N")

print()
print("== Problemi di riepilogo ==")
print("R1  60+30 perp ->", round(math.hypot(60, 30)), "cm")
print("R2  nave 60 E + 160 N ->", round(math.hypot(60, 160)), "km")
print("R3  quarto cerchio r=20 -> corda =", round(20 * math.sqrt(2)), "cm")
print("R4  vettore 20, vx=12 -> vy =", math.sqrt(20 ** 2 - 12 ** 2),
      " angolo =", round(math.degrees(math.acos(12 / 20))))
print("R5  puck 7 E + 8 N ->", round(math.hypot(7, 8), 1), "m")
print("R7  due forze perp 12 e 16 -> R =", math.hypot(12, 16),
      " angolo =", round(math.degrees(math.atan2(16, 12))))
print("R8  sollev. 180 kg -> P_Terra =", round(180 * g), "N (~1.77 kN) ; P_Luna =", round(180 * 1.6), "N")
print("R9  dinamometro 2.0 N / 0.080 m -> k =", 2.0 / 0.080, "N/m")
print("R10 molla k=400, s_max=0.050 m -> P_max =", 400 * 0.050, "N")
print("R11 panca 60 kg / 4 -> F =", round(60 * g / 4), "N")
print("R12 lampadario 20 N, filo a 30 deg: lungo filo =", round(20 * math.cos(math.radians(30))),
      " perp =", round(20 * math.sin(math.radians(30))))
print("R13 montacarichi 2500 N / (20*g) =", 2500 / (20 * g), "-> 12 sacchi")
print("R14 rampa 60 m a 30 deg -> h =", 60 * math.sin(math.radians(30)), "m")
Pc = 25 * g
print("R15 cassa 25 kg su 20 deg -> P =", round(Pc), " Ppar =", round(Pc * 0.34),
      " Pperp =", round(Pc * 0.94))
print("R16 sciatore 65 kg, ks=0.10 -> Fas_max =", round(0.10 * 65 * g), "N")
Fp = 120 * g
print("R17a armadio 120 kg, ks=0.5 -> F =", round(0.5 * Fp), "N")
print("R17b mmax =", 500 / (0.5 * g), "kg -> togliere", round(120 - 500 / (0.5 * g)), "kg")
print("R18 bimbo 30 kg su molla k=5000 -> s =", round(30 * g / 5000 * 100, 1), "cm")
print("R19 libro 400 g, ks=0.5 -> F = m g / ks =", round(0.400 * g / 0.5, 1), "N")
