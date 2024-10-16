import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

# Dati sperimentali
tempo = np.array([1.0, 2.0, 3.0, 4.0, 5.0])
distanza = np.array([4.900, 19.600, 44.100, 78.400, 122.500])
error_distanza = np.array([0.001] * len(distanza))

# Calcolo di t^2
tempo_squared = tempo**2

# Definizione della funzione di modello lineare
def linear_model(x, a, b):
    return a * x + b

# Regressione lineare su distanza vs. t^2
params, covariance = curve_fit(linear_model, tempo_squared, distanza)
slope = params[0]
intercept = params[1]
std_err = np.sqrt(np.diag(covariance))

# Calcolo dell'accelerazione di gravità
g = 2 * slope  # dato che d = 1/2 * g * t^2
g_error = 2 * std_err[0]

print(f"Accelerazione di gravità (g): {g:.3f} ± {g_error:.3f} m/s²")

# Creazione del grafico
plt.figure(figsize=(8, 6))
plt.errorbar(tempo_squared, distanza, yerr=error_distanza, fmt='o', label='Dati sperimentali', capsize=5)
plt.plot(tempo_squared, linear_model(tempo_squared, *params), 'r-', label='Retta di regressione')
plt.title('Misurazione dell\'Accelerazione di Gravità')
plt.xlabel('Tempo al quadrato (s²)')
plt.ylabel('Distanza (m)')
plt.legend()
plt.grid(True)
plt.show()
