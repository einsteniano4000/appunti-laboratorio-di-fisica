import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 10)
y = np.sin(x)
yerr = 0.2

plt.errorbar(x, y, yerr=yerr, fmt='-o')
plt.title("Grafico con Barre di Errore")
plt.xlabel("X")
plt.ylabel("Y")
plt.savefig('grafico_barre_errore.png')
plt.show()
