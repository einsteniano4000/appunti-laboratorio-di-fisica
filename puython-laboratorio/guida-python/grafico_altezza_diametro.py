import matplotlib.pyplot as plt
import numpy as np

# Costanti
volume = 1000  # Volume costante del cilindro in m³

# Diametro della base
diametro = np.linspace(1, 10, 100)  # Diametro varia da 1 a 10 metri

# Calcolo dell'altezza
# Volume = Area base × Altezza
# Area base = π × (Diametro / 2)²
# Altezza = Volume / (π × (Diametro / 2)²)
altezza = volume / (np.pi * (diametro / 2)**2)

# Creazione del grafico
plt.figure(figsize=(12, 6))
plt.plot(diametro, altezza, label='Altezza = Volume / (π × (Diametro / 2)²)', color='green')
plt.title("Grafico dell'Altezza in Funzione del Diametro di Base (Volume Fisso)")
plt.xlabel("Diametro della Base (m)")
plt.ylabel("Altezza (m)")
plt.grid(True)
plt.legend()
plt.savefig('grafico_altezza_diametro.png')
plt.show()
