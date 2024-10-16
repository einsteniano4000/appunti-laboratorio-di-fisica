import matplotlib.pyplot as plt
import numpy as np

#=============================================================================================================================
#DATI INIZIALI
g = 9.81 #m/s^2
alfa = 45.00*np.pi/180 #rad

y0 = 1.00 #m
v0 = 20.00 #m/s

v0_x = v0*np.cos(alfa) #m/s
v0_y = v0*np.sin(alfa) #m/s

durata = 4.14 #s
numero_istanti = 500 #numero di istanti in cui è suddiviso l'asse del tempo
t = np.linspace(0,durata,numero_istanti) #s
#=============================================================================================================================

#=============================================================================================================================
#EQUAZIONI DEL MOTO
x = v0_x*t
y = y0 + v0_y*t - 1/2*g*t**2
#=============================================================================================================================

#=============================================================================================================================
#CREAZIONE DEL GRAFICO
fig, grafico = plt.subplots(figsize=(10,6))
grafico.plot(x, y, color='blue')
grafico.set_xlabel("x (m)")
grafico.set_ylabel("y (m)")
grafico.set_title("Traiettoria del moto")
grafico.minorticks_on()
grafico.grid(which='major', axis='both', linewidth=1.0)
grafico.grid(which='minor', axis='both', linestyle ="--", linewidth=0.2)
plt.show()
#=============================================================================================================================