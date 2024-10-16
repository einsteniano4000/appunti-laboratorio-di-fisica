import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress

# Dati sperimentali
tempo = np.array([0, 1, 2, 3, 4])
velocita = np.array([0, 2, 4, 6, 8])

# Aggiunta degli errori di misura
errori_tempo = np.array([0.1, 0.1, 0.1, 0.1, 0.1])
errori_velocita = np.array([0.2, 0.2, 0.2, 0.2, 0.2])

# Calcolo della regressione lineare
slope, intercept, r_value, p_value, std_err = linregress(tempo, velocita)

# Stampa dei risultati
print(f"Coefficiente angolare (velocità): {slope:.2f} m/s")
print(f"Intercetta: {intercept:.2f} m")
print(f"R-quadrato: {r_value**2:.2f}")

# Grafico dei dati e della retta di regressione con barre di errore
plt.errorbar(tempo, velocita, xerr=errori_tempo, yerr=errori_velocita, fmt='o', label='Dati sperimentali')
plt.plot(tempo, slope*tempo + intercept, color='red', label='Retta di regressione')
plt.xlabel('Tempo (s)')
plt.ylabel('Velocità (m/s)')
plt.legend()
plt.title('Regressione Lineare della Velocità in Funzione del Tempo con Barre di Errore')
plt.show()

