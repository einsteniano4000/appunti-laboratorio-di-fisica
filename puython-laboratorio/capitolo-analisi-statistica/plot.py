import numpy as np
from scipy.stats import linregress
import matplotlib.pyplot as plt

# Dati sperimentali
tempo = np.array([1.0, 2.0, 3.0, 4.0, 5.0])
distanza = np.array([4.900, 19.600, 44.100, 78.400, 122.500])
error_distanza = np.array([0.001] * len(distanza))

# Calcolo di t^2
tempo_squared = tempo**2

# Regressione lineare su distanza vs. t^2
slope, intercept, r_value, p_value, std_err = linregress(tempo_squared, distanza)

# Calcolo dell'accelerazione di gravit\'a
g = 2 * slope  # dato che d = 1/2 * g * t^2
g_error = 2 * std_err

print(f"Accelerazione di gravit\'a (g): {g:.3f}") 
print(f"Errore su g:  {g_error:.3f} ")


# Creazione del grafico
plt.figure(figsize=(8, 6))
plt.errorbar(tempo_squared, distanza, yerr=error_distanza, fmt='o', label='Dati sperimentali', capsize=5)
plt.plot(tempo_squared, slope*tempo_squared + intercept, 'r-', label='Retta di regressione')
plt.title('Misurazione dell\'Accelerazione di Gravità')
plt.xlabel('Tempo secondi al quadrato ')
plt.ylabel('Distanza (metri)')
plt.legend()
plt.grid(True)
plt.show()
