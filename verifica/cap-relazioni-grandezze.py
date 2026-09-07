#!/usr/bin/env python3
# Verifica dei numeri del capitolo "Relazioni tra grandezze".
# Python puro, niente numpy.

import math

def sez(t): print("\n" + "=" * 64 + "\n" + t + "\n" + "=" * 64)

# ===========================================================================
sez("Proporzionalita' diretta  y = k x")

# circonferenza C = 2 pi r
print("circonferenza C = 2 pi r:")
for r in (1, 2, 3, 4, 5):
    C = 2 * math.pi * r
    print(f"  r={r} cm -> C={C:.2f} cm   C/r={C/r:.4f}")

# volume nel cilindro, area di base fissa A = 20 cm^2
A = 20.0
print(f"\nvolume nel cilindro (A base = {A:.0f} cm^2):")
for h in (2, 4, 6, 8, 10):
    print(f"  h={h} cm -> V={A*h:.0f} cm^3   V/h={A*h/h:.0f}")

# massa e volume, ferro rho = 7,87 g/cm^3
rho = 7.87
print(f"\nmassa/volume ferro (rho={rho} g/cm^3):")
for V in (10, 20, 30, 40):
    print(f"  V={V} cm^3 -> m={rho*V:.1f} g")

# --- esercizi ---
print("\n--- esercizi diretta ---")
print(f"perimetro quadrato l=3,5 cm -> P = {4*3.5} cm ; l tale che P=30 -> l={30/4} cm")
print(f"molla k=25 N/m: F per dx=8,0 cm -> {25*0.08:.1f} N ; dx per F=5,0 N -> {5.0/25*100:.0f} cm")
print(f"alluminio rho=2,70 g/cm^3: m di 50 cm^3 -> {2.70*50:.0f} g ; V di 216 g -> {216/2.70:.0f} cm^3")

# ===========================================================================
sez("Proporzionalita' inversa  y = k/x  (x y = k)")

# rettangolo area fissa A = 24 cm^2
A = 24.0
print(f"rettangolo area {A:.0f} cm^2:")
for b in (2, 3, 4, 6, 8, 12):
    print(f"  b={b} -> h={A/b:.1f}   b*h={b*A/b:.0f}")

# percorso fisso d = 120 km
d = 120.0
print(f"\npercorso {d:.0f} km a velocita' diversa:")
for v in (40, 60, 80, 120):
    print(f"  v={v} km/h -> t={d/v:.2f} h   v*t={v*d/v:.0f}")

print("\n--- esercizi inversa ---")
print(f"12 operai in 15 giorni -> 1 lavoro; con 20 operai: t = {12*15/20:.0f} giorni (uomini*giorni={12*15})")
print(f"gas: p1 V1 = p2 V2; 1,0 bar a 3,0 L compresso a 1,2 L -> p = {1.0*3.0/1.2:.1f} bar")
print(f"rettangolo area 36 m^2, base 9 m -> altezza {36/9:.0f} m ; base per altezza 3 m -> {36/3:.0f} m")

# ===========================================================================
sez("Proporzionalita' quadratica  y = k x^2")

# area quadrato
print("area quadrato A = l^2:")
for l in (1, 2, 3, 4, 5):
    print(f"  l={l} -> A={l**2}   A/l^2={l**2/l**2}")

# area cerchio
print("\narea cerchio A = pi r^2:")
for r in (1, 2, 3, 4):
    print(f"  r={r} -> A={math.pi*r**2:.2f}   A/r^2={math.pi*r**2/r**2:.4f}")

print("\n--- esercizi quadratica ---")
print(f"piastrella lato 20 -> 40 cm: area da {20**2} a {40**2} cm^2 (x{40**2/20**2:.0f})")
print(f"cerchio r da 5 a 15 cm: area x{ (15/5)**2:.0f}")
print(f"pizza d=30 vs d=45 cm: area x{(45/30)**2:.2f} -> prezzo equo {8.0*(45/30)**2:.1f} euro se quella da 30 costa 8")

# ===========================================================================
sez("Inversamente proporzionale al quadrato: h = 4V/(pi d^2)")

V = 750.0  # cm^3
print(f"stesso liquido V = {V:.0f} cm^3 in cilindri di diametro d:")
for dcm in (5, 10, 15):
    Abase = math.pi * (dcm/2)**2
    h = V / Abase
    print(f"  d={dcm} cm -> A_base={Abase:.2f} cm^2 -> h={h:.2f} cm   h*d^2={h*dcm**2:.1f}")
print(f"  raddoppiando d (5->10): h da {V/(math.pi*2.5**2):.1f} a {V/(math.pi*5**2):.2f}  (rapporto {(V/(math.pi*2.5**2))/(V/(math.pi*5**2)):.1f})")

print("\n--- esercizi inv. quadrato ---")
V2 = 1000.0
d1, d2 = 8.0, 4.0
h1 = V2/(math.pi*(d1/2)**2); h2 = V2/(math.pi*(d2/2)**2)
print(f"1 L in cilindro d=8 -> h={h1:.2f} cm ; in d=4 -> h={h2:.2f} cm (x{h2/h1:.0f})")

# ===========================================================================
sez("Problemi di riepilogo")

print(f"triangolo equil.: P=3l, k=3  ({3*6}=18 ok)")
print(f"1 rubinetto 40 min -> 2 rubinetti {40/2:.0f} min, 4 rubinetti {40/4:.0f} min")
print(f"A4 5,0 g -> A3 (area doppia) {5.0*2:.0f} g")
Abase = 25.0
h_i = 200/Abase; h_f = 250/Abase
print(f"cilindro base 25: 200 cm^3 -> h={h_i:.0f} cm ; +50 -> h={h_f:.0f} cm ; sale di {h_f-h_i:.0f} cm")
# bici 18 min a 15 km/h -> distanza; poi v per 12 min
dist = 15 * (18/60)
v_new = dist / (12/60)
print(f"bici: d={dist:.2f} km ; v per 12 min = {v_new:.1f} km/h")
print(f"cubo spigolo x2 -> volume x{2**3}")
print(f"foto 10x15 -> 30x45: area x{(3)**2}, perimetro x{3}")
print(f"gas 5,0 L a 1,0 bar -> 4,0 bar: V = {5.0*1.0/4.0:.2f} L")
# succo 0,90 L in d=6 -> h ; poi d=18
V = 900.0
h6 = V/(math.pi*3**2); h18 = V/(math.pi*9**2)
print(f"succo 0,90 L: d=6 -> h={h6:.1f} cm ; d=18 -> h={h18:.1f} cm (rapporto {h6/h18:.0f})")
print(f"y=100/x^2: x=1..5 -> {[round(100/x**2,2) for x in (1,2,3,4,5)]}")
print(f"candela 1/9 luminosita': distanza x sqrt(9)=3 -> da 2 m a {2*3:.0f} m")
# chitarra f inv L: 65 cm -> 330 Hz ; L per 440 Hz
L = 65 * 330 / 440
print(f"chitarra: L per 440 Hz = {L:.2f} cm  (f*L = {330*65} = {440*L:.0f})")
xs2 = [2,3,5,8]; ys2 = [8,18,50,128]
print(f"x={xs2} y={ys2}: y/x^2 = {[y/x**2 for x,y in zip(xs2,ys2)]} -> quadratica k=2 ; y(10)={2*100}")

# ===========================================================================
sez("Riconoscere la relazione da una tabella")

# tabella mista di test
xs = [1, 2, 3, 4, 5]
print("y = 3x :   ", [3*x for x in xs], " y/x:", [3*x/x for x in xs])
print("y = 12/x : ", [round(12/x, 2) for x in xs], " x*y:", [round(x*12/x, 2) for x in xs])
print("y = 2x^2 : ", [2*x**2 for x in xs], " y/x^2:", [2*x**2/x**2 for x in xs])
