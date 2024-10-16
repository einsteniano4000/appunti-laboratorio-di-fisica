import matplotlib.pyplot as plt

# Dati sperimentali
dati_sperimentali = [45.1, 47.2, 49.3, 50.5, 52.6, 54.7, 48.3, 46.9, 51.2, 53.8, 
                     50.0, 49.9, 48.7, 51.5, 52.1, 47.6, 46.3, 50.9, 51.8, 48.0, 
                     49.5, 50.3, 47.0, 46.5, 52.4, 48.8, 49.2, 51.3, 47.8, 50.7]

# Crea l'istogramma
plt.figure(figsize=(10, 6))
plt.hist(dati_sperimentali, bins=8, edgecolor='black', alpha=0.7)

# Aggiungi titolo e etichette
plt.title('Istogramma dei dati sperimentali')
plt.xlabel('Misura (cm)')
plt.ylabel('Frequenza')

# Mostra l'istogramma
plt.savefig('istogramma2.png')  # Salva l'immagine come istogramma2.png
plt.show()
