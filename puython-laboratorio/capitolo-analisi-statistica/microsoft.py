import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# Parametri della distribuzione
mu = 4
sigma = 1

# Generazione dei dati
x = np.linspace(mu - 3*sigma, mu + 3*sigma, 1000)
y = norm.pdf(x, mu, sigma)

# Creazione del grafico
plt.plot(x, y, label='Gaussian Curve')

# Punti significativi
significant_points = [mu - sigma, mu, mu + sigma]
plt.axvline(mu -sigma, color='red', linestyle='dashed')
plt.axvline(mu, color='red', linestyle='dashed')
plt.axvline(mu +sigma, color='red', linestyle='dashed')
plt.text(mu -sigma,0, f'$\mu { "-"} \sigma$', horizontalalignment='center', verticalalignment='bottom')
plt.text(mu,0, f'$\mu$', horizontalalignment='center', verticalalignment='bottom')
plt.text(mu +sigma,0, f'$\mu { "+"} \sigma$', horizontalalignment='center', verticalalignment='bottom')

# Rimozione dei numeri sull'asse x
plt.xticks([])

# Etichette e titolo
plt.xlabel('x')
plt.ylabel('PDF')
plt.title('Gaussian Curve with Significant Points')
plt.legend()

# Mostra il grafico
plt.show()
