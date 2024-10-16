import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0,1,10)
y = x**2

figura, grafico = plt.subplots(figsize=(10,6))
grafico.plot(x, y, label="x**2")
grafico.set_xlabel("Etichetta asse x")
grafico.set_ylabel("Etichetta asse x")
grafico.set_title("Titolo del grafico")
grafico.minorticks_on()
grafico.grid(which='major', axis='both', linewidth=1.0)
grafico.grid(which='minor', axis='both', linestyle ="--", linewidth=0.2)
grafico.set_aspect("equal")
grafico.legend()
plt.show()





