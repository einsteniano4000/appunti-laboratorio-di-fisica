import matplotlib.pyplot as plt
import numpy as np

# Dati
tempi = [0, 2, 5, 8, 10]
posizioni = [0, 4, 16, 28, 40]

# Creazione del grafico
plt.figure(figsize=(12, 6))
plt.plot(tempi, posizioni, marker='o')
plt.title("Grafico Spazio-Tempo per Moto Uniforme a Tratti")
plt.xlabel("Tempo (s)")
plt.ylabel("Posizione (m)")
plt.grid(True)
plt.savefig('grafico_spazio_temporale.png')
plt.show()
