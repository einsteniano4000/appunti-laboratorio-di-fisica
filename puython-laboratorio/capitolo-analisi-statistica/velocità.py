import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

# Dati sperimentali
tempo = np.array([1.0, 2.0, 3.0, 4.0, 5.0])
spazio = np.array([2.1, 4.2, 6.1, 8.0, 10.1])
error_spazio = np.array([0.1, 0.1, 0.1, 0.1, 0.1])  


# Definizione della funzione di modello lineare
def linear_model(t, s0, v):
    return s0 + v * t

# Regressione lineare
params, covariance = curve_fit(linear_model, tempo, spazio)
s0 = params[0]
v = params[1]
std_err = np.sqrt(np.diag(covariance))

# Calcolo dell'errore sulla velocità
v_error = std_err[1]
print(f"Velocità (v): {v:.2f} +- {v_error:.2f} m/s")

# Creazione del grafico
plt.figure(figsize=(8, 6))
plt.errorbar(tempo, spazio, yerr=error_spazio, fmt='o', label='Dati sperimentali', capsize=5)
plt.plot(tempo, linear_model(tempo, *params), 'r-', label='Retta di regressione')
plt.title('Moto Rettilineo Uniforme')
plt.xlabel('Tempo (s)')
plt.ylabel('Spazio (m)')
plt.legend()
plt.grid(True)
plt.show()
