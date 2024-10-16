import matplotlib.pyplot as plt
import numpy as np

# Dati di esempio assegnati esplicitamente
x = np.array([0, 1.11, 2.22, 3.33, 4.44, 5.55, 6.66, 7.77, 8.88, 10])
y = np.array([0.5, 3.1, 5.2, 8.3, 11.1, 13.9, 16.5, 19.4, 22.1, 25.3])
yerr = np.array([0.6, 0.4, 0.5, 0.3, 0.7, 0.2, 0.4, 0.6, 0.5, 0.3])  # Assicurarsi che yerr sia positivo

# Creazione della figura e dell'asse
fig, ax = plt.subplots()

# Creazione del grafico con barre di errore
ax.errorbar(x, y, yerr=yerr, fmt='o', ecolor='red', capsize=5, label='Misure sperimentali')

# Aggiunta di etichette agli assi
ax.set_xlabel('Variabile indipendente')
ax.set_ylabel('Variabile dipendente')

# Aggiunta di un titolo
ax.set_title('Grafico delle Misure Sperimentali con Barre di Errore')

# Aggiunta di una legenda
ax.legend()

# Aggiunta di una griglia
ax.grid(True)

# Mostra il grafico
plt.show()
