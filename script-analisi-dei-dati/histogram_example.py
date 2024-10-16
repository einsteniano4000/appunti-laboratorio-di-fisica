import matplotlib.pyplot as plt
import numpy as np

# Generazione di dati casuali
data = np.random.randn(1000)

# Creazione dell'istogramma
plt.hist(data, bins=30, edgecolor='black')

# Aggiunta di titolo e etichette
plt.title('Esempio di Istogramma')
plt.xlabel('Valore')
plt.ylabel('Frequenza')

# Salvataggio dell'istogramma
plt.savefig('histogram_example.png')
plt.show()
