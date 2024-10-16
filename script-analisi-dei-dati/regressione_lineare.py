import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
# Dati sperimentali
tempo = np.array([1.0, 2.0, 3.0, 4.0, 5.0])
spazio = np.array([1.9, 4.1, 6.0, 7.7, 12.0])

# Definizione della funzione di modello lineare
def linear_model(x, a, b):
    return a * x + b

# Fitting dei dati
params, params_covariance = curve_fit(linear_model, tempo, spazio)

# Estrazione dei parametri
pendenza, intercetta = params
pendenza_error, intercetta_error = np.sqrt(np.diag(params_covariance))

print(f"Pendenza: {pendenza:.3f} ± {pendenza_error:.3f}")
print(f"Intercetta: {intercetta:.3f} ± {intercetta_error:.3f}")

# Creazione del grafico
plt.figure(figsize=(8, 6))
plt.scatter(tempo, spazio, label='Dati sperimentali')
plt.plot(tempo, linear_model(tempo, *params), 'r-', label='Retta di regressione')
plt.xlabel('Tempo (s)')
plt.ylabel('Spazio (m)')
plt.title('Fitting Lineare')
plt.legend()
plt.grid(True)
plt.savefig('regressione_lineare.png')  # Salvataggio dell'immagine
plt.show()
