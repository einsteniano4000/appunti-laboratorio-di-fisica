import matplotlib.pyplot as plt
import numpy as np

# Dati
tempi = [0, 2, 5, 8, 10]
velocita = [2, 2, 4, 4, 6]

# Creazione del grafico
plt.figure(figsize=(12, 6))
plt.step(tempi, velocita, where='post', marker='o')
plt.title("Grafico Velocità-Tempo per Moto Uniforme a Tratti")
plt.xlabel("Tempo (s)")
plt.ylabel("Velocità (m/s)")
plt.grid(True)
plt.savefig('grafico_velocita_temporale.png')
plt.show()
