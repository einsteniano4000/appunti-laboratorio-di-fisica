#!/usr/bin/env python3
# Verifica dei numeri del capitolo "Il momento angolare e l'energia dei fluidi"
# (Unita' 10, Lez. 4-5). Python puro, niente numpy.

from math import pi, sqrt

def sez(t): print("\n" + "=" * 68 + "\n" + t + "\n" + "=" * 68)
def P(n, s): print(f"{n:>2}. {s}")

g = 9.81
d = 1000.0          # densita' dell'acqua, kg/m^3

def rpm2rad(n): return n * 2 * pi / 60


# ===========================================================================
sez("18.1-18.3  Momento angolare")

# es. svolto: disco r=0,40 m, m=2,5 kg -> I
I_disco = 0.5 * 2.5 * 0.40**2
print(f"disco r=0,40 m=2,5: I = 1/2 m r^2 = {I_disco:.3f} kg m^2  (0,20)")

# es. svolto: I=0,01 kg m^2, w=20 rad/s -> L
print(f"disco I=0,01 w=20: L = I w = {0.01*20:.2f} kg m^2/s  (0,2)")

# es. svolto: centrifuga da ferma a 600 rpm in 8,0 s
w = rpm2rad(600)
print(f"centrifuga 600 rpm = {w:.2f} rad/s ; alpha = w/8,0 = {w/8.0:.2f} rad/s^2  (~7,9)")

# es. svolto: giostra - bambina m=30, r=3,0 ; I_g=400 ; w_i=0,52
I_b = 30 * 3.0**2
I_i = 400 + I_b
w_f = I_i * 0.52 / 400
print(f"giostra: I_bambina={I_b:.0f} ; I_i={I_i:.0f} ; w_f = I_i w_i / I_f = {w_f:.3f} rad/s  (0,87)")

# es. svolto: pattinatrice I_i=4,0 w_i=2,0 -> I_f=1,2
print(f"pattinatrice: w_f = 4,0*2,0/1,2 = {4.0*2.0/1.2:.2f} rad/s  (6,67)")

print("\n--- esercizi ---")
print(f" E1 anello m=0,50 r=0,20: I = m r^2 = {0.50*0.20**2:.3f} kg m^2")
I2 = 0.5*3.0*0.15**2
print(f" E2 mola m=3,0 r=0,15 w=40: I = {I2:.4f} ; L = {I2*40:.3f} kg m^2/s  (~1,4)")
print(f" E3 giostra 0->3,0 rad/s in 5,0 s: alpha = {3.0/5.0:.2f} rad/s^2")
print(f" E4 volano I=0,18 w=120: L = {0.18*120:.1f} ; stop in 30 s: alpha = {-120/30:.1f} rad/s^2")
print(f" E5 piattaforma I_i=5,0 w_i=3,0 -> I_f=8,0: w_f = {5.0*3.0/8.0:.3f} rad/s  (~1,9)")
print(f" E6 tuffatore raggomitolato: qualitativo (I diminuisce, L cost -> w aumenta)")
I_cd = 0.5*0.015*0.06**2
w_cd = rpm2rad(500)
print(f" E7 CD m=15 g d=12 cm 500 rpm: I = {I_cd:.3e} ; w = {w_cd:.2f} ; L = {I_cd*w_cd:.3e} kg m^2/s  (~1,4e-3)")


# ===========================================================================
sez("18.5-18.7  Energia dei fluidi")

# es. svolto: rubinetto A=1,2 cm^2, v=1,5 m/s -> Q
A = 1.2e-4
Q = A * 1.5
print(f"rubinetto A=1,2 cm^2 v=1,5: Q = A v = {Q:.2e} m^3/s = {Q*1000:.2f} L/s ; in 1 min {Q*1000*60:.1f} L")

# es. svolto: canna d=2,0 cm v=1,0 ; ugello d=0,80 cm
v2 = 1.0 * (1.0/0.40)**2
print(f"canna->ugello: v2 = v1 (r1/r2)^2 = 1,0*(1,0/0,40)^2 = {v2:.2f} m/s  (6,25)")

# es. svolto: Venturi - v1=2,0 p1=1,8e5 ; sezione dimezzata
v2 = 2.0 * 2
p2 = 1.8e5 + 0.5*d*(2.0**2 - v2**2)
print(f"Venturi: v2 = {v2:.1f} m/s ; p2 = p1 + 1/2 d (v1^2-v2^2) = {p2:.0f} Pa = {p2/1e5:.2f}e5  (1,74e5)")

# es. svolto: Torricelli h=10 m
print(f"Torricelli h=10: v = sqrt(2 g h) = {sqrt(2*g*10):.2f} m/s  (~14)")

# es. svolto: pompa - p1=1,5 bar v1=0,80 ; sezione dimezzata ; h2=3,0
v2 = 0.80 * 2
p2 = 1.5e5 + d*g*(0 - 3.0) + 0.5*d*(0.80**2 - v2**2)
print(f"pompa: v2 = {v2:.1f} m/s ; p2 = {p2:.0f} Pa = {p2/1000:.0f} kPa  (~120 kPa)")

print("\n--- esercizi ---")
print(f" E1 fiume A=340 v=0,85: Q = {340*0.85:.0f} m^3/s  (290)")
A = pi*0.010**2
print(f" E2 impianto Q=5,0 L/s tubo d=20 mm: A = {A:.3e} ; v = Q/A = {5.0e-3/A:.1f} m/s  (~16)")
p2 = 2.0e5 + d*g*(0 - 1.5)
print(f" E3 tubo sez. cost. sale 1,5 m, p1=2,0e5: p2 = {p2:.0f} Pa = {p2/1e5:.2f}e5")
print(f" E4 diga v=20 m/s: h = v^2/(2 g) = {20**2/(2*g):.1f} m  (~20)")
print(f" E5 tubo d 6,0->3,0 cm, v1=1,0: v2 = 1,0*(6,0/3,0)^2 = {1.0*(6.0/3.0)**2:.1f} m/s")
print(f" E6 tetto sollevato dal vento: qualitativo (Venturi: aria veloce sopra -> p minore)")
print(f" E7 serbatoio h=5,0: v = {sqrt(2*g*5.0):.2f} m/s ; h=1,25: v = {sqrt(2*g*1.25):.2f} m/s (dimezzata)")


# ===========================================================================
sez("18.8  Problemi di riepilogo")

P(1, f"anello r=0,30 m=1,2: I = m r^2 = {1.2*0.30**2:.3f} kg m^2  (~0,11)")
I2 = 0.5*4.0*0.25**2
P(2, f"disco m=4,0 r=0,25 w=30: I = {I2:.3f} ; L = {I2*30:.2f} kg m^2/s  (~3,8)")
a3 = 18/6.0
P(3, f"ruota 0->18 rad/s in 6,0 s: alpha = {a3:.1f} rad/s^2 ; M = I alpha = 0,50*{a3:.1f} = {0.5*a3:.2f} N m")
I4 = 2*(2.0*0.60**2)
P(4, f"2 masse 2,0 kg a 0,60 m: I = sum m r^2 = {I4:.2f} kg m^2  (~1,4)")
P(5, f"piattaforma I_i=10 w_i=2,0 -> I_f=4,0: w_f = {10*2.0/4.0:.1f} rad/s  (5,0)")
wf6 = 6.0*4.0/1.5
P(6, f"tuffatore I 6,0->1,5 w_i=4,0: w_f = {wf6:.1f} rad/s ; giri/s = {wf6/(2*pi):.2f}  (~2,5)")
wi7 = rpm2rad(200); wf7 = rpm2rad(500)
P(7, f"CD 200->500 rpm in 0,80 s: w_i={wi7:.2f} w_f={wf7:.2f} ; alpha = {(wf7-wi7)/0.80:.1f} rad/s^2  (~39)")
P(8, "ruote di reazione dei satelliti: qualitativo (L totale si conserva)")
Q9 = 1.5e-3/12
P(9, f"rubinetto 1,5 L in 12 s: Q = {Q9:.3e} m^3/s ; v = Q/A(0,50 cm^2) = {Q9/0.50e-4:.1f} m/s  (2,5)")
v10 = 1.2*(10/4.0)**2
Q10 = pi*0.05**2*1.2
P(10, f"tubo d 10->4,0 cm v1=1,2: v2 = {v10:.1f} m/s ; Q = A1 v1 = {Q10:.3e} m^3/s  (~9,4e-3)")
p11 = 2.2e5 + 0.5*d*(1.5**2 - 6.0**2)
P(11, f"Venturi v1=1,5 p1=2,2e5 v2=6,0: p2 = {p11:.0f} Pa = {p11/1e5:.2f}e5  (~2,0e5)")
v12 = sqrt(2*g*8.0)
P(12, f"serbatoio h=8,0: v = {v12:.2f} m/s ; Q = A(2,0 cm^2) v = {2.0e-4*v12:.3e} m^3/s  (~2,5e-3)")
P(13, "tubo orizzontale sez. cost.: p costante (senza attrito) -- qualitativo")
p14 = 3.0e5 - d*g*4.0
P(14, f"tubo sale 4,0 m sez. cost., p1=3,0e5: p2 = p1 - d g dh = {p14:.0f} Pa = {p14/1e5:.2f}e5  (~2,6e5)")
p15 = 2.0e5 - d*g*5.0
P(15, f"pompa p1=2,0 bar quota 0 -> quota 5,0 m, sez. uguale: p2 = {p15:.0f} Pa = {p15/1e5:.2f}e5 = {p15/1e5:.1f} bar")
A_cap = 3.0*30/0.03
P(16, f"sangue: A_cap = A_a v_a / v_cap = 3,0*30/0,03 = {A_cap:.0f} cm^2 = {A_cap/1e4:.2f} m^2")
P(17, f"annaffiatoio Q=0,20 L/s beccuccio 0,40 cm^2: v = {0.20e-3/0.40e-4:.1f} m/s  (5,0)")
L18 = 1.5*0.33**2*25
P(18, f"ruota bici m=1,5 r=0,33 w=25 (anello): L = m r^2 w = {L18:.2f} kg m^2/s  (~4,1) ; effetto giroscopico -- qualitativo")
wf19 = 0.020*50/(0.020+0.010)
P(19, f"disco I=0,020 w=50 + disco I=0,010 fermo, ruotano insieme: w_f = {wf19:.1f} rad/s  (~33)")
