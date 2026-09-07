#!/usr/bin/env python3
# Verifica dei numeri del capitolo "Il moto rettilineo" (cinematica, Unita' 6).
# Python puro, niente numpy.  g = 9,81 N/kg (per la caduta libera si usa g = 9,81 m/s^2;
# il libro usa 9,8 -- qui teniamo 9,81 come nel resto della dispensa, salvo dove indicato).

import math

g = 9.81

def sez(t): print("\n" + "=" * 64 + "\n" + t + "\n" + "=" * 64)

# ===========================================================================
sez("1  Lo studio del moto: spazio percorso e spostamento")

# Esempio: pista di atletica, giro da 400 m
print(f"giro intero:  spazio = 400 m, spostamento = 0 m")
print(f"mezzo giro (pista vista come cerchio): spazio = 200 m")
R_pista = 400 / (2 * math.pi)
print(f"  raggio equivalente R = {R_pista:.2f} m, diametro (spostamento) = {2*R_pista:.1f} m")

# Esempio svolto nel testo: 60 m verso est, poi 80 m verso nord
sp1, sp2 = 60.0, 80.0
perc = sp1 + sp2
spo = math.hypot(sp1, sp2)
print(f"60 m E + 80 m N:  spazio percorso = {perc:.0f} m, spostamento = {spo:.0f} m")

# Esempio: semicirconferenza raggio 25 m
R = 25.0
print(f"semicirconferenza R={R}:  spazio = pi*R = {math.pi*R:.1f} m, spostamento = 2R = {2*R:.0f} m")

# --- esercizi §1 ---
print("\n--- esercizi §1 ---")

# es: tre lati di un quadrato di lato 50 m
L = 50.0
print(f"es tre lati quadrato L={L}: spazio = {3*L:.0f} m, spostamento = {math.hypot(L,L):.1f} m")

# es: 120 m verso est, poi 50 m verso sud
e, s = 120.0, 50.0
print(f"es 120 E + 50 S: spazio = {e+s:.0f} m, spostamento = {math.hypot(e,s):.0f} m")

# es: atleta mezzo giro pista circolare R = 30 m
R2 = 30.0
print(f"es mezzo giro R={R2}: spazio = {math.pi*R2:.1f} m, spostamento = {2*R2:.0f} m")

# es formula inversa: spostamento di modulo 18 m lungo una semicirconferenza -> R e spazio
mod = 18.0
Rinv = mod / 2
print(f"es inversa: spostamento {mod} m su semicirconf. -> R = {Rinv:.0f} m, spazio = {math.pi*Rinv:.2f} m")

# es: nuotatore, vasca da 25 m, percorre 3 vasche
Lv = 25.0
print(f"es 3 vasche da {Lv} m: spazio = {3*Lv:.0f} m, spostamento = {Lv:.0f} m (dispari -> una vasca)")

# ===========================================================================
sez("2  La velocita' media")

def kmh_to_ms(v): return v / 3.6
def ms_to_kmh(v): return v * 3.6

# conversioni base
for v in (90, 108, 36, 72):
    print(f"{v} km/h = {kmh_to_ms(v):.4g} m/s")
for v in (15, 25, 5):
    print(f"{v} m/s = {ms_to_kmh(v):.4g} km/h")

# esempio grafico spazio-tempo (camminatore originale)
t = [0, 5, 10, 15, 20, 25, 30, 35]
s = [0, 8, 16, 24, 24, 24, 34, 44]
print("\ncamminatore: t", t)
print("             s", s)
vm_tot = (s[-1] - s[0]) / (t[-1] - t[0])
print(f"v_media complessiva = {s[-1]}/{t[-1]} = {vm_tot:.3f} m/s = {ms_to_kmh(vm_tot):.2f} km/h")
print("velocita' medie nei singoli intervalli da 5 s:")
for i in range(len(t) - 1):
    ds = s[i+1] - s[i]; dt = t[i+1] - t[i]
    print(f"  {t[i]:>2}-{t[i+1]:>2} s:  ds={ds:>2} m  ->  v = {ds/dt:.2f} m/s")

# esempio svolto 1: due fasi
d1, tmin1 = 9.0e3, 6.0        # m, min
d2, tmin2 = 3.0e3, 12.0
dtot = d1 + d2
ttot = (tmin1 + tmin2) * 60
vm = dtot / ttot
print(f"\nes.svolto due fasi: {dtot:.0f} m in {ttot:.0f} s -> v_m = {vm:.2f} m/s = {ms_to_kmh(vm):.1f} km/h")

# esempio svolto 2: lettura grafico -> gia' coperto sopra

# --- esercizi §2 ---
print("\n--- esercizi §2 ---")

# es: 108 km/h in m/s ; 15 m/s in km/h
print(f"es conv: 108 km/h = {kmh_to_ms(108):.0f} m/s ; 15 m/s = {ms_to_kmh(15):.0f} km/h")

# es: treno 210 km in 1 h 45 min
d = 210e3
tt = (1*60 + 45) * 60
print(f"es treno: {d/1e3:.0f} km in {tt:.0f} s -> v_m = {ms_to_kmh(d/tt):.0f} km/h = {d/tt:.1f} m/s")

# es inversa: v_m = 6,0 m/s, spazio 2,4 km -> tempo
tt2 = 2.4e3 / 6.0
print(f"es inversa tempo: 2,4 km a 6,0 m/s -> {tt2:.0f} s = {int(tt2//60)} min {int(tt2%60)} s")

# es inversa: 20 min a 90 km/h -> spazio
sp = kmh_to_ms(90) * 20 * 60
print(f"es inversa spazio: 20 min a 90 km/h -> {sp:.0f} m = {sp/1e3:.0f} km")

# es andata e ritorno
La = 800.0
ta, tr = 10*60, 12*60
vm_ar = 2*La / (ta + tr)
print(f"es andata/ritorno: 1600 m in {ta+tr:.0f} s -> v_m = {vm_ar:.3f} m/s = {ms_to_kmh(vm_ar):.2f} km/h")
va, vr = La/ta, La/tr
print(f"  (v andata = {va:.3f} m/s, v ritorno = {vr:.3f} m/s, media aritmetica {0.5*(va+vr):.3f} != {vm_ar:.3f})")

# es due velocisti 100 m
for T in (12.5, 11.0):
    print(f"  100 m in {T} s -> v = {100/T:.2f} m/s = {ms_to_kmh(100/T):.1f} km/h")
print(f"  differenza v = {100/11.0 - 100/12.5:.2f} m/s")

# ===========================================================================
sez("3  Il moto rettilineo uniforme")

# esempio ciclista v = 6 m/s, casi s0 = 0 e s0 = 20
v = 6.0
for s0 in (0.0, 20.0):
    print(f"s0={s0}: " + "  ".join(f"t={t}->s={s0+v*t:.0f}" for t in (0,2,4,6,8,10)))
print(f"pendenza fra t=2 e t=5: ds={v*5-v*2:.0f} m, dt=3 s -> v={ (v*5-v*2)/3:.1f} m/s")

# esempio svolto 1: auto s0 = 400 m, v = 15 m/s
s0, v = 400.0, 15.0
print(f"\nes.svolto auto: s = {s0:.0f} + {v:.0f} t")
print(f"  t=30 s -> s = {s0+v*30:.0f} m")
print(f"  s=1000 m -> t = {(1000-s0)/v:.0f} s")

# esempio svolto 2: auto s=30t, moto s=200+20t
tinc = 200 / (30 - 20)
print(f"es.svolto auto/moto: incontro a t = {tinc:.0f} s, s = {30*tinc:.0f} m")

# esempio svolto 3: pendenza negativa s = 100 - 4t
print(f"es.svolto s=100-4t: passa per O a t = {100/4:.0f} s")

# --- esercizi §3 ---
print("\n--- esercizi §3 ---")

# es legge oraria s = 4,0 t
print("es s=4,0 t:  v=4,0 m/s ; t=10 -> s=40 m ; s=90 -> t=22,5 s")
assert 4.0*10 == 40 and 90/4.0 == 22.5

# es auto 25 m/s, 300 m prima di un cartello -> s = 25 t (origine all'auto), cartello a 300 m
v = 25.0
print(f"es auto 25 m/s: raggiunge cartello a 300 m in t = {300/v:.0f} s ; dopo 20 s ha fatto {v*20:.0f} m")

# es ciclista in fuga
d = 1200.0
vg = kmh_to_ms(45); vf = kmh_to_ms(36)
tcatch = d / (vg - vf)
print(f"es fuga: closing = {vg-vf:.2f} m/s, t = {tcatch:.0f} s = {int(tcatch//60)} min {int(tcatch%60)} s")

# es due treni che si avvicinano
d = 12000.0
vc = kmh_to_ms(90) + kmh_to_ms(126)
print(f"es treni: closing = {vc:.0f} m/s = {ms_to_kmh(vc):.0f} km/h, t = {d/vc:.0f} s")

# es legge oraria s = 12 + 3 t
print("es s=12+3t:  s0=12 m ; v=3 m/s ; s=54 -> t = ", (54-12)/3, "s")

# es radar
c = 3.0e8
techo = 60e-6
print(f"es radar: distanza = c*t/2 = {c*techo/2:.0f} m = {c*techo/2/1e3:.1f} km")

# ===========================================================================
sez("4  L'accelerazione")

# esempio metropolitana: 0->12 m/s in 10 s; costante 30 s; 12->0 in 6 s
seg = [((0,0),(10,12)), ((10,12),(40,12)), ((40,12),(46,0))]
for (t1,v1),(t2,v2) in seg:
    print(f"  {t1:>2}-{t2:>2} s:  dv={v2-v1:+.0f} m/s, dt={t2-t1} s -> a = {(v2-v1)/(t2-t1):+.2f} m/s^2")

# esempio svolto 1: 0 -> 100 km/h in 8,0 s
dv = kmh_to_ms(100)
print(f"\nes.svolto 0->100 km/h in 8,0 s: dv={dv:.2f} m/s, a = {dv/8.0:.2f} m/s^2")

# esempio svolto 2: 90 km/h -> 0 in 5,0 s
dv = 0 - kmh_to_ms(90)
print(f"es.svolto frenata 90 km/h->0 in 5,0 s: dv={dv:.1f} m/s, a = {dv/5.0:.1f} m/s^2")

# --- esercizi §4 ---
print("\n--- esercizi §4 ---")
print(f"es da ferma a 30 m/s in 12 s: a = {30/12:.2f} m/s^2")
print(f"es a=1,5 m/s^2 in 10 s: dv = {1.5*10:.0f} m/s")
print(f"es da 5 a 23 m/s con a=2,0: t = {(23-5)/2.0:.1f} s")
print(f"es 108 km/h -> 0 con a=-6,0: t = {kmh_to_ms(108)/6.0:.1f} s")
print(f"es treno 144->72 km/h in 20 s: a = {(kmh_to_ms(72)-kmh_to_ms(144))/20:.2f} m/s^2")
aA = kmh_to_ms(100)/7.0; aB = kmh_to_ms(100)/11.0
print(f"es ripresa A/B: a_A = {aA:.2f}, a_B = {aB:.2f} m/s^2, rapporto {aA/aB:.2f}")

# ===========================================================================
sez("5  Il moto rettilineo uniformemente accelerato")

# esempio tabella a = 0,5 m/s^2 da fermo
a = 0.5
print("a=0,5 da fermo: " + "  ".join(f"t={t}->v={a*t}" for t in (0,1,2,3,4,10)))

# esempi svolti
print(f"\nes1: da fermo a=2,0, dopo 6 s: v = {2.0*6:.0f} m/s")
v0, a = 8.0, 1.5
print(f"es2: v0=8,0 a=1,5: dopo 10 s v = {v0+a*10:.0f} m/s ; v=30 -> t = {(30-v0)/a:.2f} s")
print(f"es3: caduta libera da fermo, dopo 2,0 s: v = {g*2.0:.2f} m/s")
h, l = 1.5, 12.0
a_pi = g*h/l
print(f"es4: piano incl. h=1,5 l=12: a = {a_pi:.3f} m/s^2 ; dopo 4,0 s v = {a_pi*4.0:.2f} m/s")
print(f"es5: frenata v0=30 a=-5: si ferma a t = {30/5:.0f} s")

# --- esercizi §5 ---
print("\n--- esercizi §5 ---")
print(f"es da fermo a=1,2 dopo 4,0 s: v = {1.2*4.0:.1f} m/s")
print(f"es v0=30 a=-3,0 dopo 3,0 s: v = {30-3.0*3.0:.0f} m/s")
print(f"es caduta libera v=24,5 m/s: t = {24.5/g:.2f} s")
print(f"es da v0=6,0 a v=42 con a=2,0: t = {(42-6.0)/2.0:.0f} s")
print(f"es mela tocca terra a 5,2 m/s: t = {5.2/g:.2f} s")
h2, l2 = 2.0, 20.0
print(f"es piano incl. h=2,0 l=20: a = {g*h2/l2:.3f} m/s^2 ; dopo 3,0 s v = {g*h2/l2*3.0:.2f} m/s")
print(f"es biglia a=g/3, raggiunge 4,0 m/s: t = {4.0/(g/3):.2f} s")
print(f"es rampa lunga 18 m, a=g/3 -> h/l=1/3 -> h = {18/3:.1f} m")
print(f"es sasso su a v0=15: si ferma a t = {15/g:.2f} s")
vf1 = kmh_to_ms(160) + 9.0*3.0
print(f"es F1: 160 km/h + a=9,0 per 3,0 s -> v = {vf1:.1f} m/s = {ms_to_kmh(vf1):.0f} km/h")

# ===========================================================================
sez("6  Leggi orarie e grafici")

# esempi svolti
print(f"es1 MRU: v=20 per 8 s -> area = {20*8:.0f} m")
a = 3.0
print(f"es2 MRUA da fermo a=3,0 dopo 5,0 s: ds = 1/2 a t^2 = {0.5*a*25:.1f} m (v={a*5:.0f}, triang {0.5*(a*5)*5:.1f})")
print(f"es3 caduta libera 3,0 s: ds = {0.5*g*9:.1f} m")
print(f"es4 treno v0=10 a=0,5 dopo 20 s: s = {10*20 + 0.5*0.5*400:.0f} m")
v0, a = 25.0, -5.0
tst = v0/abs(a)
print(f"es5 frenata v0=25 a=-5: t={tst:.0f} s, ds = {v0*tst + 0.5*a*tst**2:.1f} m")

# --- esercizi §6 ---
print("\n--- esercizi §6 ---")
print(f"es MRU v=15 per 12 s: ds = {15*12:.0f} m")
print(f"es MRUA da fermo a=2,0 in 6,0 s: ds = {0.5*2.0*36:.0f} m")
print(f"es caduta 2,0 s: {0.5*g*4:.2f} m ; 4,0 s: {0.5*g*16:.2f} m (rapporto {(0.5*g*16)/(0.5*g*4):.0f})")
a_inv = 2*50/25
print(f"es MRUA da fermo 50 m in 5,0 s: a = {a_inv:.1f} m/s^2")
import math
tcad = math.sqrt(2*45/g)
print(f"es sasso da 45 m: t = {tcad:.2f} s, v arrivo = {g*tcad:.1f} m/s")
print(f"es camion s=10t+0,25 t^2: v0=10 m/s, a={2*0.25:.2f} m/s^2, s(10)= {10*10 + 0.25*100:.0f} m")
v0, a = kmh_to_ms(108), 6.0
tf = v0/a
print(f"es frenata 108 km/h a=-6,0: t = {tf:.1f} s, ds = {v0*tf - 0.5*a*tf**2:.0f} m")
print(f"es pozzo: sasso cade 2,0 s -> profondita' = {0.5*g*4:.1f} m")
v0 = 20.0
tsu = v0/g
print(f"es sasso su v0=20: t_salita = {tsu:.2f} s, h = {v0*tsu - 0.5*g*tsu**2:.1f} m (= v0^2/2g = {v0**2/(2*g):.1f})")

# ===========================================================================
sez("6.4  Il lancio verticale e la caduta dei gravi")

# esempio svolto A: lancio verticale v0 = 18 m/s
v0 = 18.0
ts = v0/g
hmax = v0*ts - 0.5*g*ts**2
print(f"lancio v0=18: t_salita={ts:.2f} s, h_max={hmax:.2f} m (v0^2/2g={v0**2/(2*g):.2f}), "
      f"t_volo={2*ts:.2f} s, v_ritorno={-(v0 - g*(2*ts)):.1f} m/s (modulo {abs(v0-g*2*ts):.1f})")

# esempio svolto B: caduta da h = 12 m
h = 12.0
tc = (2*h/g)**0.5
print(f"caduta h=12: t={tc:.2f} s, v_impatto = g t = {g*tc:.1f} m/s = {ms_to_kmh(g*tc):.0f} km/h")

# --- esercizi §6.4 ---
print("\n--- esercizi §6.4 ---")
v0 = 25.0
print(f"es lancio v0=25: t_salita={v0/g:.2f} s, h_max={v0**2/(2*g):.2f} m")
tc = 1.8
print(f"es caduta t=1,8 s: h={0.5*g*tc**2:.2f} m, v_impatto={g*tc:.1f} m/s")
tvolo = 4.0
v0 = g*(tvolo/2)
print(f"es ricade dopo 4,0 s: v0={v0:.1f} m/s, h_max={v0**2/(2*g):.1f} m")
vimp = 30.0
tc = vimp/g
print(f"es elicottero, v_suolo=30: t={tc:.2f} s, quota h={0.5*g*tc**2:.1f} m")
# es lancio verso il basso: ponte h=20, v0=5,0 -> 4.905 t^2 + 5 t - 20 = 0
import math
A, B, C = 0.5*g, 5.0, -20.0
tw = (-B + math.sqrt(B*B - 4*A*C)) / (2*A)
print(f"es lancio in basso h=20 v0=5,0: t={tw:.2f} s, v_impatto = {5.0 + g*tw:.1f} m/s")

# ===========================================================================
sez("6.5  Una formula senza il tempo:  v^2 = v0^2 + 2 a ds")

# esempio svolto: frenata v0=30, a=-5 -> ds
v0, a = 30.0, -5.0
ds = -(v0**2) / (2*a)
print(f"es.svolto frenata v0=30 a=-5: ds = -v0^2/2a = {ds:.0f} m  (t_arresto = {v0/abs(a):.1f} s)")

# --- esercizi §6.5 ---
print("\n--- esercizi §6.5 ---")
print(f"es aereo: ds = 60^2/(2*3,0) = {60**2/(2*3.0):.0f} m")
print(f"es sasso 45 m: v = sqrt(2 g 45) = {math.sqrt(2*g*45):.2f} m/s")
print(f"es carabina: a = 380^2/(2*0,60) = {380**2/(2*0.60):.3e} m/s^2")
print(f"es treno 12->30 in 525 m: a = (30^2-12^2)/(2*525) = {(30**2-12**2)/(2*525):.3f} m/s^2")

# ===========================================================================
sez("9.7  Problemi di riepilogo")

def P(n, s): print(f"{n:>2}. {s}")

# 1 spazio/spostamento: 300 N + 400 E + 300 S
P(1, f"spazio = {300+400+300} m ; spostamento = {math.hypot(400,0):.0f} m (400 E)")
# 2 v media due fasi
P(2, f"52 km in 1,0 h -> v_m = {52/1.0:.0f} km/h")
# 3 confronto
P(3, f"A=90 km/h ; B=26 m/s = {ms_to_kmh(26):.1f} km/h -> B piu' veloce")
# 4 MRU distanza fra auto e camion dopo 40 s
P(4, f"(20-15)*40 = {(20-15)*40} m")
# 5 s = 500 - 25 t
P(5, f"s0=500 m, v=-25 m/s (verso O) ; passa per O a t = {500/25:.0f} s")
# 6 incontro versi opposti
t6 = 600/(12+8)
P(6, f"12 t = 600 - 8 t -> t = {t6:.0f} s, x = {12*t6:.0f} m")
# 7 accelerazione 108->72 km/h in 8 s
P(7, f"a = ({kmh_to_ms(72):.1f}-{kmh_to_ms(30*3.6):.1f})/8 ...  a = {(kmh_to_ms(72)-kmh_to_ms(108))/8:.2f} m/s^2")
# 8 MRUA da fermo a=2,5, 6 s
P(8, f"v = {2.5*6:.0f} m/s ; s = {0.5*2.5*36:.0f} m")
# 9 spazio di frenata timeless
P(9, f"ds = 25^2/(2*6,25) = {25**2/(2*6.25):.0f} m")
# 10 caduta libera 3 s
P(10, f"v = {g*3:.1f} m/s ; s = {0.5*g*9:.1f} m")
# 11 caduta da 30 m
t11 = math.sqrt(2*30/g)
P(11, f"t = {t11:.2f} s ; v = {g*t11:.1f} m/s")
# 12 lancio verticale v0=22
P(12, f"h_max = 22^2/(2 g) = {22**2/(2*g):.1f} m ; t_volo = 2*22/g = {2*22/g:.2f} s")
# 13 piano inclinato l=3,0 h=0,45
a13 = g*0.45/3.0
P(13, f"a = g*0,45/3,0 = {a13:.2f} m/s^2 ; v dopo 1,5 s = {a13*1.5:.2f} m/s ; v in fondo = sqrt(2 a 3,0) = {math.sqrt(2*a13*3.0):.2f} m/s")
# 14 trapezio 5->25 in 10 s
P(14, f"area = (5+25)/2*10 = {(5+25)/2*10:.0f} m")
# 15 MRUA 100 m in 8 s da fermo
a15 = 2*100/64
P(15, f"a = 2*100/8^2 = {a15:.3f} m/s^2 ; v = a t = {a15*8:.0f} m/s")
# 16 reazione + frenata
P(16, f"reazione 30*0,8 = {30*0.8:.0f} m ; frenata 30^2/(2*7,5) = {30**2/(2*7.5):.0f} m ; totale {30*0.8 + 30**2/(2*7.5):.0f} m")
# 17 due fasi MRUA
v17 = 0.8*15; s17a = 0.5*0.8*15**2
P(17, f"v = {v17:.0f} m/s ; s(15 s) = {s17a:.0f} m ; s(60 s) = {s17a + v17*45:.0f} m")
# 18 lancio in basso da 25 m, v0=8
A18,B18,C18 = 0.5*g, 8.0, -25.0
t18 = (-B18 + math.sqrt(B18**2 - 4*A18*C18))/(2*A18)
P(18, f"t = {t18:.2f} s ; v = {8.0 + g*t18:.1f} m/s")
# 19 caduta libera == rampa
v19 = math.sqrt(2*g*2.0)
P(19, f"rampa: v = sqrt(2 g 2,0) = {v19:.2f} m/s ; caduta libera stessa v -> h = v^2/2g = {v19**2/(2*g):.2f} m")
