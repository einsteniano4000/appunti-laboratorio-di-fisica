#!/usr/bin/env python3
# Verifica dei numeri del capitolo "Il calore" (Unita' 11, Lez. 3-5).
# Python puro, niente numpy.

def sez(t): print("\n" + "=" * 68 + "\n" + t + "\n" + "=" * 68)
def P(n, s): print(f"{n:>2}. {s}")

# --- costanti e tabelle ---------------------------------------------------
g = 9.81

# calore specifico c  [J/(kg K)]  (tecnologico.pdf, Unita' 11, Tab. 1)
c = {"acqua": 4180, "alcol": 2430, "petrolio": 2140, "benzina": 2100,
     "olio": 1650, "alluminio": 880, "acciaio": 480, "ferro": 480,
     "rame": 390, "ottone": 376, "argento": 238, "mercurio": 138,
     "oro": 134, "piombo": 128, "ghiaccio": 2100, "aria": 1000}

# calore latente di fusione  [J/kg]
lf = {"ghiaccio": 334e3, "piombo": 23e3, "argento": 105e3, "alcol": 105e3,
      "mercurio": 12e3}
# calore latente di vaporizzazione  [J/kg]
lv = {"acqua": 2250e3, "alcol": 854e3, "mercurio": 272e3, "piombo": 871e3,
      "argento": 2336e3, "sudore": 2400e3}

# conducibilita' termica k  [W/(m K)]
kt = {"argento": 430, "rame": 390, "alluminio": 235, "bronzo": 190,
      "ottone": 120, "ferro": 67, "ghiaccio": 2.1, "vetro": 0.80,
      "mattoni": 0.60, "mattoni_forati": 0.50, "sughero": 0.045,
      "legno": 0.20, "gomma": 0.15}


def Q_cmdt(sost, m, dT):
    return c[sost] * m * dT

def T_eq(m1, c1, T1, m2, c2, T2):
    return (m1 * c1 * T1 + m2 * c2 * T2) / (m1 * c1 + m2 * c2)

def fourier_Q(k, A, dT, dt, d):
    return k * A * dT * dt / d

def fourier_P(k, A, dT, d):
    return k * A * dT / d


# ===========================================================================
sez("17.2  Capacita' termica e calore specifico")

# es. svolto 1: 2,0 kg acqua da 18 a 100 C
q = Q_cmdt("acqua", 2.0, 82)
print(f"es1  acqua 2,0 kg, dT=82: Q = 4180*2,0*82 = {q:.0f} J ~ {q:.2e}  (~6,9e5)")

# es. svolto 2: pentola acciaio 0,80 kg, C e Q per dT=80
C_pent = c["acciaio"] * 0.80
print(f"es2  pentola acciaio 0,80 kg: C = m c = {C_pent:.0f} J/K ; "
      f"Q(dT=80) = {C_pent*80:.0f} J ~ {C_pent*80:.2e}  (~3,1e4)")

# es. svolto 3: blocco 0,50 kg, dT da 20 a 110 (=90), assorbe 39,6 kJ -> c?
c_x = 39600 / (0.50 * 90)
print(f"es3  blocco 0,50 kg, dT=90, Q=39,6 kJ: c = Q/(m dT) = {c_x:.0f} J/(kg K) -> alluminio")

print("\n--- esercizi 17.2 ---")
print(f" E1  250 g acqua, dT=75: Q = {Q_cmdt('acqua',0.250,75):.0f} J ~ 7,8e4")
print(f" E2  piastra Al 0,60 kg, dT=160: Q = {Q_cmdt('alluminio',0.60,160):.0f} J ~ 8,4e4")
dT = 17000 / (1.5 * c["rame"])
print(f" E3  1,5 kg rame cede 17 kJ: dT = {dT:.1f} C ~ 29")
c_e4 = 1340 / (0.200 * 50)
print(f" E4  200 g metallo, dT=50, Q=1,34 kJ: c = {c_e4:.0f} -> oro")
print(f" E5  1,2 kg acqua da 70 a 37 C (dT=33): Q = {Q_cmdt('acqua',1.2,33):.0f} J ~ 1,7e5")
print(f" E6  acqua vs olio, rapporto c: {c['acqua']/c['olio']:.2f} -> olio ~2,5x piu' rapido")


# ===========================================================================
sez("17.3  L'equilibrio termico")

# es. svolto: 1,0 kg a 20 + 3,0 kg a 60  (acqua)
Te = T_eq(1.0, c["acqua"], 20, 3.0, c["acqua"], 60)
print(f"es1  1,0 kg@20 + 3,0 kg@60 acqua: Te = {Te:.1f} C  (50)")

# es. svolto: ferro 0,350 kg @70 in 2,0 kg acqua @25
Te = T_eq(0.350, c["ferro"], 70, 2.0, c["acqua"], 25)
print(f"es2  ferro 0,350 kg@70 + acqua 2,0 kg@25: Te = {Te:.2f} C ~ 26")

# es. svolto calorimetro: 0,150 kg acqua @20 ; oggetto 0,090 kg @100 ; Te=29
Qacq = c["acqua"] * 0.150 * (29 - 20)
c_ogg = Qacq / (0.090 * (100 - 29))
C_ogg = c_ogg * 0.090
print(f"es3  calorimetro: Q_acq acqua = {Qacq:.0f} J ; "
      f"c_ogg = {c_ogg:.0f} J/(kg K) ~ 8,8e2 ; C_ogg = {C_ogg:.0f} J/K ~ 79")

print("\n--- esercizi 17.3 ---")
print(f" E1  2,0 kg@80 + 3,0 kg@20 acqua: Te = {T_eq(2.0,c['acqua'],80,3.0,c['acqua'],20):.0f} C  (44)")
print(f" E2  40 L@60 + 20 L@18: Te = {T_eq(40,c['acqua'],60,20,c['acqua'],18):.0f} C  (46)")
Te = T_eq(0.50, c["alluminio"], 20, 1.0, c["acqua"], 90)
print(f" E3  pentola Al 0,50 kg@20 + acqua 1,0 kg@90: Te = {Te:.1f} C ~ 83")
Te = T_eq(0.200, c["acqua"], 85, 0.050, c["acqua"], 10)
print(f" E4  caffe 200 g@85 + latte 50 g@10 (c=acqua): Te = {Te:.0f} C  (70)")
Te = T_eq(0.500, c["rame"], 200, 2.0, c["acqua"], 15)
print(f" E5  rame 0,50 kg@200 + acqua 2,0 kg@15: Te = {Te:.1f} C ~ 19")
mc = 1.0 * (40 - 15) / (65 - 40)
print(f" E6  1,0 kg@15 + m@65 -> Te=40: m = {mc:.1f} kg  (1,0)")
Te = T_eq(0.200, c["acqua"], 18, 0.300, c["alluminio"], 90)
print(f" E7  calorimetro 200 g acqua@18 + Al 300 g@90: Te = {Te:.1f} C ~ 35")


# ===========================================================================
sez("17.4  I cambiamenti di stato")

# es. svolto: fondere 2,0 kg ghiaccio a 0 C
print(f"es1  fondere 2,0 kg ghiaccio: Q = lf*m = {lf['ghiaccio']*2.0:.0f} J ~ 6,7e5")

# es. svolto: 500 g ghiaccio -10 C -> acqua 20 C
Q1 = c["ghiaccio"] * 0.500 * 10
Q2 = lf["ghiaccio"] * 0.500
Q3 = c["acqua"] * 0.500 * 20
print(f"es2  0,5 kg ghiaccio -10->0->fus->20: Q1={Q1:.0f}  Q2={Q2:.0f}  Q3={Q3:.0f}  "
      f"tot={Q1+Q2+Q3:.0f} J ~ 2,2e5")

# es. svolto: sci, Fn=800 N, kr=0,10, fondere 1,0 kg neve a 0 C
Qs = lf["ghiaccio"] * 1.0
d = Qs / (800 * 0.10)
print(f"es3  sci Fn=800 kr=0,10: Q={Qs:.0f} J ; d = Q/(Fn kr) = {d:.0f} m ~ 4,2 km")

# es. svolto: evaporare 200 g acqua a 100 C
print(f"es4  evaporare 0,200 kg acqua: Q = lv*m = {lv['acqua']*0.200:.0f} J ~ 4,5e5")

# es. svolto: sudorazione 2,0 kg sudore, 80% evapora
Qsud = lv["sudore"] * 0.80 * 2.0
print(f"es5  sudore 2,0 kg all'80%: Q = {Qsud:.0f} J ~ 3,8e6")

print("\n--- esercizi 17.4 ---")
print(f" E1  fondere 500 g piombo: Q = {lf['piombo']*0.500:.0f} J ~ 1,2e4")
print(f" E2  evaporare 1,0 kg acqua a 100: Q = {lv['acqua']*1.0:.2e} J  (2,25e6)")
print(f" E3  fondere 30 g ghiaccio: Q = {lf['ghiaccio']*0.030:.0f} J ~ 1,0e4")
print(f" E4  200 g ghiaccio -18->0 C: Q = {c['ghiaccio']*0.200*18:.0f} J ~ 7,6e3")
Qtot = lf["ghiaccio"] * 0.100 + c["acqua"] * 0.100 * 100
print(f" E5  100 g ghiaccio 0 C -> acqua 100 C: Q = {Qtot:.0f} J ~ 7,5e4")
Qm = 0.60 * 200 * 20
dT = Qm / (0.050 * c["acciaio"])
print(f" E6  martello: Q = {Qm:.0f} J ; dT chiodo = {dT:.0f} C  (100)")
Q1 = c["acqua"] * 1.5 * 80
Q2 = lv["acqua"] * 0.50
t = (Q1 + Q2) / 2000
print(f" E7  2,0 kW: Q1={Q1:.0f} Q2={Q2:.0f} tot={Q1+Q2:.0f} ; t = {t:.0f} s ~ {t/60:.1f} min")


# ===========================================================================
sez("17.5  La propagazione del calore")

# es. svolto conduzione: mattoni A=12, d=0,20, k=0,60, dT=16, 1 ora
Q = fourier_Q(0.60, 12, 16, 3600, 0.20)
Pw = fourier_P(0.60, 12, 16, 0.20)
print(f"es1  parete mattoni: Q(1h) = {Q:.0f} J ~ 2,1e6 ; P = {Pw:.0f} W")

# es. svolto dispersione finestre (percentuale)
Av, dv, Am, dm, rap = 20, 0.004, 40, 0.20, 5
ratio = (Av / dv) / (Am * rap / dm)
print(f"es2  finestre: Qv/Qm = {ratio:.0f} -> Qv=5Qm ; Qtot=6Qm ; "
      f"finestre disperdono 5/6 = {5/6*100:.0f}%")

# es. svolto irraggiamento: 5,0 W a 300 K -> 350 K
P2 = 5.0 * (350 / 300) ** 4
print(f"es3  irraggiamento 5,0 W @300K -> @350K: P = {P2:.2f} W ~ 9,3")

print("\n--- esercizi 17.5 ---")
Q = fourier_Q(kt["mattoni_forati"], 15, 13, 3600, 0.25)
print(f" E1  parete forati A=15 d=0,25 k=0,50 dT=13, 1h: Q = {Q:.0f} J ~ 1,4e6")
Pw = fourier_P(kt["mattoni_forati"], 15, 13, 0.25)
print(f" E2  stessa parete: P = {Pw:.0f} W  (390)")
Pw = fourier_P(kt["sughero"], 8.0, 18, 0.050)
print(f" E3  sughero A=8,0 d=5,0 cm k=0,045 dT=18: P = {Pw:.1f} W ~ 130")
print(f" E4  piastrelle vs tappeto: qualitativo (conduzione)")
print(f" E5  termosifone in basso: qualitativo (convezione)")
P2 = 800 * (500 / 400) ** 4
print(f" E6  stufa 800 W @400K -> @500K: P = {P2:.0f} W ~ 2,0e3")
print(f" E7  thermos: qualitativo (vuoto + superfici lucide)")


# ===========================================================================
sez("Problemi di riepilogo")

P(1, f"300 g acqua 15->100: Q = {Q_cmdt('acqua',0.300,85):.0f} J ~ 1,1e5")
dT = 47000 / (2.0 * c["rame"])
P(2, f"2,0 kg rame assorbe 47 kJ da 25 C: dT = {dT:.1f} -> T = {25+dT:.0f} C  (~85)")
c_x = 1600 / (0.250 * 50)
P(3, f"250 g metallo 20->70, Q=1,60 kJ: c = {c_x:.0f} -> piombo")
P(4, f"C di 1,5 L acqua: C = m c = {1.5*c['acqua']:.0f} J/K")
P(5, f"1,0 kg@90 + 4,0 kg@15 acqua: Te = {T_eq(1.0,c['acqua'],90,4.0,c['acqua'],15):.0f} C  (30)")
Te = T_eq(0.80, c["ferro"], 250, 3.0, c["acqua"], 20)
P(6, f"ferro 0,80 kg@250 + acqua 3,0 L@20: Te = {Te:.1f} C ~ 27")
Te = T_eq(0.200, c["acqua"], 20, 0.250, c["ottone"], 95)
P(7, f"calorimetro 200 g acqua@20 + ottone 250 g@95: Te = {Te:.1f} C ~ 28")
mq = 0.70 * 1800 * 120 / (c["aria"] * 30)
P(8, f"phon 1,8 kW 70% aria dT=30 in 2 min: m_aria = {mq:.2f} kg  (~5,0)")
P(9, f"fondere 250 g ghiaccio: Q = {lf['ghiaccio']*0.250:.0f} J ~ 8,4e4")
mev = 300e3 / lv["acqua"]
P(10, f"400 g acqua @100, 300 kJ: m evaporata = {mev*1000:.0f} g  (~133)")
Qtot = c["ghiaccio"]*0.200*5 + lf["ghiaccio"]*0.200 + c["acqua"]*0.200*15
P(11, f"200 g ghiaccio -5 -> acqua 15 C: Q = {Qtot:.0f} J ~ 8,1e4")
t = c["acqua"]*2.0*85 / 1200
P(12, f"1,2 kW, 2,0 L acqua 15->100: t = {t:.0f} s ~ {t/60:.1f} min")
d = lf["ghiaccio"]*0.200 / (500 * 0.12)
P(13, f"slittino Fn=500 kr=0,12, fondere 200 g neve: d = {d:.0f} m ~ 1,1 km")
Q = fourier_Q(0.70, 25, 24, 12*3600, 0.30)
P(14, f"parete d=0,30 A=25 k=0,70 dT=24, 12 h: Q = {Q:.3e} J ~ 6,0e7")
Pw = fourier_P(0.70, 25, 24, 0.30)
P(15, f"stessa parete: P = {Pw:.0f} W  (1400)")
T = 500 * 2 ** 0.25
P(16, f"corpo 1,0 kW @500K, doppio: T = 500*2^(1/4) = {T:.0f} K  (~595)")
P(17, "coperta termica: qualitativo (riflette IR, riduce convezione)")
Qdisp = c["acqua"] * 1.5 * 20
Qfus = lf["ghiaccio"] * 1.0
mfusa = Qdisp / lf["ghiaccio"]
P(18, f"1,5 kg acqua@20 + 1,0 kg ghiaccio@0: Q_disp={Qdisp:.0f} < Q_fus={Qfus:.0f} -> "
      f"fonde {mfusa*1000:.0f} g ; stato finale acqua+ghiaccio a 0 C "
      f"(ghiaccio ~{1000-mfusa*1000:.0f} g, acqua ~{1500+mfusa*1000:.0f} g)")
dEc = 0.300 * g * 20
dT = dEc / (0.300 * c["alluminio"])
P(19, f"blocco Al 300 g cade da 20 m: dEc = {dEc:.1f} J ; dT = {dT:.2f} C  (~0,22)")
