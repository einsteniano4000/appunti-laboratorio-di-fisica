import matplotlib.pyplot as plt
import numpy as np

# Dati
densita = 5  # densità costante (ad esempio 5 kg/m³)
volume = np.linspace(0, 10, 100)  # Genera 100 punti tra 0 e 10

# Calcolo della massa
massa = densita * volume

# Creazione del grafico
plt.figure(figsize=(12, 6))
plt.plot(volume, massa, label='m = densità × V', color='blue')
plt.title("Grafico della Massa in Funzione del Volume")
plt.xlabel("Volume (m³)")
plt.ylabel("Massa (kg)")
plt.grid(True)
plt.legend()
plt.savefig('grafico_massa_volume.png')
plt.show()
