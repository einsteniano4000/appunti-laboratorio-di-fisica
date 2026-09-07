#!/usr/bin/env python3
# Verifica dei numeri del capitolo "Temperatura e dilatazione termica" (Unita' 11, Lez. 1-2).
# Python puro, niente numpy.

def sez(t): print("\n" + "=" * 68 + "\n" + t + "\n" + "=" * 68)

def C2K(c): return c + 273.15
def K2C(k): return k - 273.15
def C2F(c): return 9/5*c + 32
def F2C(f): return 5/9*(f - 32)

# coefficienti di dilatazione lineare (1/C)
lam = {"Al": 2.4e-5, "Ag": 1.9e-5, "Fe": 1.2e-5, "Cu": 1.7e-5,
       "vetro": 0.9e-5, "pyrex": 0.3e-5, "cemento": 1.0e-5, "ottone": 2.0e-5}
# coefficienti di dilatazione volumica dei liquidi (1/C)
kliq = {"mercurio": 1.8e-4, "acqua": 2.1e-4, "alcol": 1.1e-3,
        "glicerina": 5.0e-4, "benzina": 9.5e-4}


# ===========================================================================
sez("1  La temperatura")

print(f"20 C -> {C2K(20):.2f} K")
print(f"37 C -> {C2F(37):.1f} F")
print(f"55 F -> {F2C(55):.2f} C ~ 13")
print(f"25 C -> {C2F(25):.0f} F")
print("Celsius = Fahrenheit quando: T = 9/5 T + 32 -> -4/5 T = 32 -> T =", 32/(-4/5), "(-40)")

print("\n--- esercizi §1 ---")
for c in (0, 25, -18, 100):
    print(f"  {c} C = {C2K(c):.2f} K")
for k in (300, 195, 0):
    print(f"  {k} K = {K2C(k):.2f} C")
# Roma/Londra
print(f"Roma max 37 C -> min {37-9} C ; Londra max {K2C(295):.2f} C -> min {K2C(295)-9:.2f} C ; escursione 9 K")
print(f"Sole 5800 K = {K2C(5800):.0f} C")
print(f"68 F = {F2C(68):.1f} C = {C2K(F2C(68)):.2f} K")


# ===========================================================================
sez("2  La dilatazione termica")

def dl(sost, l0, dT): return lam[sost] * l0 * dT
def dV(k, V0, dT): return k * V0 * dT

# es. svolto: binario acciaio 25 m, 10->45 C
print(f"binario Fe 25 m, dT=35: dl = {dl('Fe', 25, 35):.4e} m ~ 1,1 cm")

# es. svolto: tondino acciaio 2,50 m, allungare di 5,0 mm
dT = 5.0e-3 / (lam['Fe'] * 2.50)
print(f"tondino Fe: dT = dl/(lam l0) = {dT:.1f} C ; T finale = {20+dT:.0f} C")

# es. svolto: sfera Al D=100,0 mm, anello 100,5 mm
dT = 0.5 / (lam['Al'] * 100.0)
print(f"sfera-anello: dT = 0,5/(lam*100) = {dT:.1f} C ; T = {20+dT:.0f} C (~228)")

# es. svolto: termometro mercurio 0,20 mL = 200 mm^3, A=0,040 mm^2, dT=8,0
dVm_mm3 = dV(kliq['mercurio'], 200.0, 8.0)
h = dVm_mm3 / 0.040
print(f"termometro Hg: dV = {dVm_mm3:.4f} mm^3 ~ 0,29 ; h = dV/A = {h:.4f} mm ~ 7,2  (0,20 mL = 200 mm^3)")

print("\n--- esercizi §2 ---")
print(f"cavo Cu 80 m, dT=25: dl = {dl('Cu', 80, 25):.4e} m = {dl('Cu',80,25)*100:.1f} cm")
print(f"impalcatura Fe 24,00 m, dT=30: dl = {dl('Fe', 24.00, 30):.4e} m ; altezza {24.00+dl('Fe',24.00,30):.4f} m")
print(f"cubo Al lato 1,000 m, dT=200: dl = {dl('Al', 1.000, 200):.4e} m ; lato {1.000+dl('Al',1.000,200):.4f} m")
print(f"sfera ottone V0=800 cm^3, dT=100, k=6,0e-5: dV = {dV(6.0e-5, 800, 100):.2f} cm^3 ; V = {800+dV(6.0e-5,800,100):.1f}")
print(f"ponte cemento 120 m, dT=50: dl = {dl('cemento', 120, 50):.4e} m = {dl('cemento',120,50)*100:.1f} cm")
dVa = dV(kliq['alcol'], 500, 15); dVc = dV(3*lam['pyrex'], 500, 15)
print(f"pyrex+alcol 500 cm^3, dT=15: dV_alcol = {dVa:.2f} ; dV_cavita = {dVc:.3f} ; trabocca {dVa-dVc:.2f} cm^3")


# ===========================================================================
sez("Problemi di riepilogo")

def P(n, s): print(f"{n:>2}. {s}")

P(1, f"68 F = {F2C(68):.0f} C = {C2K(F2C(68)):.2f} K")
P(2, f"20 C = {C2K(20):.2f} K ; 220 C = {C2K(220):.2f} K ; dT = 200 K")
P(3, "termometro +2: lettura 52 -> reale 50 C")
P(4, f"binario Fe 30 m, dT=35: dl = {dl('Fe', 30, 35):.4e} m ~ 1,3 cm")
P(5, f"filo Fe 2,0 m, dT=-50: dl = {dl('Fe', 2.0, -50):.4e} m = {dl('Fe',2.0,-50)*1000:.1f} mm")
dA = 2*lam['Al'] * 2500 * 100
P(6, f"lastra Al 50 cm lato (A0=2500 cm^2), dT=100: dA = 2 lam A0 dT = {dA:.1f} cm^2 ; A = {2500+dA:.0f}")
P(7, f"pendolo acciaio 0,994 m, dT=15: dl = {dl('Fe', 0.994, 15):.4e} m ; l cresce -> T cresce -> ritarda")
P(8, f"serbatoio benzina 60 L, dT=25: dV = {dV(kliq['benzina'], 60, 25):.3f} L ~ 1,4")
dT9 = 1.0e-3 / ((lam['Al'] - lam['Fe']) * 1.00)
P(9, f"Al vs Fe, 1,0 mm diff su 1,00 m: dT = 1e-3/((lam_Al-lam_Fe)*1) = {dT9:.1f} C")
P(10, f"foro Cu 20,00 mm, dT=200: dD = {dl('Cu', 20.00, 200):.4f} mm ; D = {20.00+dl('Cu',20.00,200):.3f} mm")
P(11, "vetro comune lam 3x pyrex -> shock termico rompe il vetro comune")
dT12 = 0.02 / (lam['Fe'] * 49.98)
P(12, f"cilindro-foro acciaio 50,00 vs 49,98 mm: dT = 0,02/(lam*49,98) = {dT12:.1f} C (scaldare piastra a ~53 o raffreddare cilindro a ~-13)")
P(13, "bimetallo Fe/ottone: ottone si allunga di piu -> si incurva -> termostato")
dr14 = 3*lam['Fe'] * 1 * 500
P(14, f"densita Fe 7,87 a dT=500: dV/V0 = 3 lam dT = {dr14:.4f} ; rho = 7,87/{1+dr14:.4f} = {7.87/(1+dr14):.3f} g/cm^3")
P(15, f"tubo Cu 12 m, dT=40: dl = {dl('Cu', 12, 40):.4e} m ~ 8 mm")
dVw = dV(kliq['acqua'], 2.000, 60); dVr = dV(3*lam['Al'], 2.000, 60)
P(16, f"recipiente Al 2,000 L + acqua, dT=60: dV_acqua = {dVw*1000:.1f} mL ; dV_recip = {dVr*1000:.1f} mL ; trabocca {(dVw-dVr)*1000:.1f} mL")
P(17, "gas in recipiente rigido scaldato: molecole piu veloci -> piu urti -> p aumenta")
dT18 = 0.05 / (lam['Fe'] * 60.00)
P(18, f"anello acciaio 60,00 su albero 60,05 mm: dT = 0,05/(lam*60) = {dT18:.1f} C ; T ~ {20+dT18:.0f} C")
P(19, "zero assoluto 0 K = -273,15 C ; limite non raggiungibile")
dT20 = 0.90e-3 / (lam['ottone'] * 1.50)
P(20, f"barra ottone 1,50 m allunga 0,90 mm: dT = {dT20:.1f} C ; T = {25+dT20:.0f} C")
