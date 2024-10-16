import matplotlib.pyplot as plt
import numpy as np

#=============================================================================================================================
#DATI INIZIALI
g = 9.81 #m/s^2
alfa = 45*np.pi/180 #rad

mu_A = 0.05 
x0_A = 0.00 #m
v0_A = 0.0001 #m/s

mu_B = 0.30
x0_B = 1.00 #m
v0_B = 0.0001 #m/s

durata = 2.50 #s
numero_istanti = 100 #numero di istanti in cui è suddiviso l'asse del tempo
t = np.linspace(0.00,durata,numero_istanti) #s
#=============================================================================================================================

#=============================================================================================================================
#FISICA DELLO SCIVOLAMENTO CON ATTRITO RADENTE
#accelerazioni dei due corpi
if (v0_A <= 0) or (v0_B <= 0):
    print("Le velocità iniziali devono essere maggiori o uguali a 0 m/s.")
    exit()
    
a_A = g*(np.sin(alfa) - mu_A*np.cos(alfa))
a_B = g*(np.sin(alfa) - mu_B*np.cos(alfa))

if (a_A < 0):
    print("La forza di attrito tra il corpo A e il piano è così elevata che il corpo A si fermerà, \
diminuisci mu_A oppure aumenta l'inclinazione del piano.")
    exit()
if (a_B < 0):
    print("La forza di attrito tra il corpo B e il piano è così elevata che il corpo B si fermerà, \
diminuisci mu_B oppure aumenta l'inclinazione del piano.")
    exit()
    
#posizioni dei due corpi
x_A = x0_A + v0_A*t + 1/2*a_A*t**2
x_B = x0_B + v0_B*t + 1/2*a_B*t**2
#=============================================================================================================================

#=============================================================================================================================
#CREAZIONE DEL GRAFICO
fig, grafico = plt.subplots(figsize=(10,6), sharex=True)
grafico.plot(t, x_A, color='blue', linestyle='-', linewidth=3.0, label="corpo A")
grafico.plot(t, x_B, color='red', linestyle='-', linewidth=3.0, label="corpo B")
grafico.set_xlabel("t (s)")
grafico.set_ylabel("posizione (m)")
grafico.set_title("Grafico spazio-tempo per i due corpi")
grafico.legend()
grafico.minorticks_on()
grafico.grid(which='major', axis='both', linewidth=1.0)
grafico.grid(which='minor', axis='both', linestyle ="--", linewidth=0.2)
plt.show()
#=============================================================================================================================