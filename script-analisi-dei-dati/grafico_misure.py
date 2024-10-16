import numpy as np
import numpy as np
import matplotlib.pyplot as plt

# Dati sperimentali
tempo = np.array([1.0, 2.0, 3.0, 4.0, 5.0])
distanza = np.array([4.900, 19.600, 44.100, 78.400, 122.500])
error_distanza = np.array([1, 2, 3, 1, 4])  # Errori aumentati
error_t2 = np.array([1, 1, 1, 1, 1])

# Configurazione per usare LaTeX in Matplotlib


# Creazione del grafico con dimensioni maggiori e punti più piccoli
plt.figure(figsize=(12, 9))  # Dimensioni della figura
plt.errorbar(tempo**2, distanza, yerr=error_distanza, xerr=error_t2, fmt='o', label='Dati sperimentali', capsize=5, elinewidth=2, markersize=6)
plt.title(r"Misurazione dell'Accelerazione di gravità", fontsize=16)
plt.xlabel(r'Tempo al quadrato $(s^2)$', fontsize=14)
plt.ylabel(r'Distanza (m)', fontsize=14)
plt.legend()
plt.grid(True)
plt.savefig('grafico_misure.png')  # Salvataggio dell'immagine
plt.show()
