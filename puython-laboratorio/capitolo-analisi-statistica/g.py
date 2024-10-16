import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

# Dati sperimentali
tempo = np.array([1.0, 2.0, 3.0, 4.0, 5.0])
distanza = np.array([4.9, 19.6, 44.1, 78.4, 122.5])
error_distanza = np.array([0.1, 0.1, 0.1, 0.1, 0.1])

# Calcolo di t^2
tempo_squared = tempo**2

# Definizione della funzione di modello lineare senza intercetta
def linear_model(t_squared, g_over_2):
    return g_over_2 * t_squared

# Regressione lineare forzata attraverso l'origine
params, covariance = curve_fit(linear_model, tempo_squared, distanza, sigma=error_distanza, absolute_sigma=True)
g_over_2 = params[0]

# Calcolo dell'accelerazione di gravità
g = 2 * g_over_2

# Calcolo dell'errore associato
std_err = np.sqrt(np.diag(covariance))
g_error = 2 * std_err[0]


print(f"Accelerazione di gravità (g): {g:.2f} ± {g_error:.2f} m/s^2")

# Creazione del grafico
plt.figure(figsize=(8, 6))
plt.errorbar(tempo_squared, distanza, yerr=error_distanza, fmt='o', label='Dati sperimentali', capsize=5)
plt.plot(tempo_squared, linear_model(tempo_squared, *params), 'r-', label='Retta di regressione')
plt.title('Misurazione dell\'Accelerazione di Gravità')
plt.xlabel('Tempo al quadrato (s^2)')
plt.ylabel('Distanza (m)')
plt.legend()
plt.grid(True)
plt.show()
