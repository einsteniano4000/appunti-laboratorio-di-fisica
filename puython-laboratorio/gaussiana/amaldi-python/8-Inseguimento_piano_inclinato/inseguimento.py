import matplotlib.pyplot as plt
import numpy as np

#=============================================================================================================================
#DATI INIZIALI
g = 9.81 #m/s^2
alfa = 30*np.pi/180 #rad

y0 = 0.5 #m
v0 = 50 #m/s

v0_x = v0*np.cos(alfa) #m/s
v0_y = v0*np.sin(alfa) #m/s

durata = 5.00 #s
numero_istanti = 100 #numero di istanti in cui è suddiviso l'asse del tempo
t = np.linspace(0.00,durata,numero_istanti) #s
#=============================================================================================================================

#=============================================================================================================================
#LEGGI ORARIE
x = v0_x*t
y = y0 + v0_y*t - 1/2*g*t**2
#=============================================================================================================================

#=============================================================================================================================
#CREAZIONE DEL GRAFICO
fig, grafico = plt.subplots(figsize=(10,6), sharex=True)
grafico.plot(x, y, color='blue', linestyle='-', linewidth=3.0)
grafico.set_xlabel("x (m)")
grafico.set_ylabel("y (m)")
grafico.set_title("Traiettoria del moto")
grafico.legend()
grafico.minorticks_on()
grafico.grid(which='major', axis='both', linewidth=1.0)
grafico.grid(which='minor', axis='both', linestyle ="--", linewidth=0.2)
plt.show()
#=============================================================================================================================