import matplotlib.pyplot as plt
import numpy as np

#=============================================================================================================================
#DATI INIZIALI
tempo_iniziale = 5.0 #s
tempo_finale = 10.0 #s
posizione_iniziale = 0.0 #m
velocita_iniziale = 10.0 #m/s
accelerazione = -4.5 #m/s^2
numero_istanti = 21 #numero di istanti presenti sull'asse del tempo
t = np.linspace(tempo_iniziale,tempo_finale,numero_istanti) #s
#=============================================================================================================================

#=============================================================================================================================
#LEGGE ORARIA DEL MOTO RETTILINEO UNIFORME
velocita = velocita_iniziale + accelerazione * (t - tempo_iniziale)
posizione = posizione_iniziale + velocita_iniziale * (t-tempo_iniziale) + 1/2 *accelerazione * (t-tempo_iniziale)**2
#=============================================================================================================================

#=============================================================================================================================
#CREAZIONE DEL GRAFICO
fig, grafici = plt.subplots(nrows=2, ncols=1, figsize=(10,6), sharex=True)
grafici[0].plot(t, velocita, color='r', linestyle='-', linewidth=3.0)
grafici[0].set_ylabel("velocità (m/s)")
grafici[0].set_title("Grafico velocità-tempo")
grafici[0].minorticks_on()
grafici[0].grid(which='major', axis='both', linewidth=1.0)
grafici[0].grid(which='minor', axis='both', linestyle ="--", linewidth=0.2)
grafici[1].plot(t, posizione, linewidth=3.0)
grafici[1].set_xlabel("tempo (s)")
grafici[1].set_ylabel("posizione (m)")
grafici[1].set_title("Grafico spazio-tempo")
grafici[1].minorticks_on()
grafici[1].grid(which='major', axis='both', linewidth=1.0)
grafici[1].grid(which='minor', axis='both', linestyle ="--", linewidth=0.2)
plt.show()
#=============================================================================================================================