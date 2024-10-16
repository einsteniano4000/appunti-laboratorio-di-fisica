import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# Altezze di 100 persone (in cm)
heights = [170, 165, 180, 175, 160, 155, 178, 172, 168, 169, 
           174, 167, 166, 171, 173, 177, 182, 181, 176, 179, 
           164, 163, 162, 161, 159, 158, 157, 156, 154, 153, 
           152, 151, 150, 149, 148, 147, 146, 145, 144, 143,
           150, 155, 160, 165, 170, 175, 180, 185, 190, 195,
           172, 177, 182, 187, 192, 197, 162, 167, 172, 177,
           180, 175, 170, 165, 160, 155, 150, 145, 140, 135,
           142, 147, 152, 157, 162, 167, 172, 177, 182, 187,
           165, 170, 175, 180, 185, 190, 195, 200, 205, 210]

# Stima di media, deviazione standard e deviazione standard della media
mu = np.mean(heights)
sigma = np.std(heights, ddof=1)
sigma_x_mean = sigma / np.sqrt(len(heights))

# Arrotonda la deviazione standard della media e la media alle unità
sigma_x_mean_rounded = round(sigma_x_mean)
mu_rounded = round(mu)

print(f"Media delle altezze: {mu_rounded} cm")
print(f"Deviazione standard delle altezze: {sigma:.2f} cm")
print(f"Deviazione standard della media: {sigma_x_mean_rounded} cm")

# Creazione dell'istogramma
count, bins, ignored = plt.hist(heights, bins=6, density=True, alpha=0.6, color='g', edgecolor='black')

# Sovrapposizione della curva gaussiana
xmin, xmax = plt.xlim()
x = np.linspace(xmin, xmax, 100)
p = norm.pdf(x, mu, sigma)
plt.plot(x, p, 'k', linewidth=2)
title = "Istogramma delle Altezze e Curva Gaussiana"
plt.title(title)

# Visualizzazione di media e deviazione standard
plt.axvline(mu, color='r', linestyle='dashed', linewidth=1)
plt.text(mu + mu/10, max(p), f'Media: {mu_rounded} cm', color='r')
plt.axvline(mu + sigma, color='b', linestyle='dashed', linewidth=1)
plt.axvline(mu - sigma, color='b', linestyle='dashed', linewidth=1)
plt.text(mu + sigma + mu/10, max(p)/2, f'Sigma: {sigma:.2f} cm', color='b')
plt.text(mu - sigma - mu/10, max(p)/2, f'Sigma: {sigma:.2f} cm', color='b')

# Impostazione dei valori sui bins come etichette sull'asse x
bin_labels = [f"{int(bins[i])}" for i in range(len(bins))]
plt.xticks(bins, labels=bin_labels, rotation=45)

# Migliora la disposizione dei sottotitoli e delle etichette
plt.tight_layout()

plt.savefig('istogramma.png')
plt.show()

# Risultato finale, arrotondato a due cifre significative
print(f"Altezza = ({mu_rounded} ± {sigma_x_mean_rounded}) cm")
