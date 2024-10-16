import matplotlib.pyplot as plt
import numpy as np

# Dati di esempio
data = np.random.randn(1000)

# Creazione della figura e dell'asse
fig, ax = plt.subplots()

# Creazione dell'istogramma
n, bins, patches = ax.hist(data, bins=30, color='skyblue', edgecolor='black', alpha=0.7)

# Aggiunta di etichette agli assi
ax.set_xlabel('Valori')
ax.set_ylabel('Frequenza')

# Aggiunta di un titolo
ax.set_title('Istogramma dei Valori')

# Aggiunta di una legenda
ax.legend(['Dati'])

# Aggiunta di una griglia
ax.grid(True)

# Mostra il grafico
plt.show()
