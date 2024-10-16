import matplotlib.pyplot as plt
import numpy as np

#===========================================================================================================
#MISURE
misure_x = np.array([0.30,0.50,0.70,0.90,1.10,1.30,1.50])
errori_x = np.array([0.02,0.02,0.02,0.02,0.02,0.02,0.02])
misure_y = np.array([1.1,1.4,1.6,1.9,2.1,2.2,2.4])
errori_y = np.array([0.2,0.2,0.1,0.1,0.1,0.1,0.1])
#===========================================================================================================

#===========================================================================================================
#GRANDEZZE DERIVATE
misure_y_2 = misure_y**2
errori_y_2 = 2*errori_y*misure_y
#===========================================================================================================

#===========================================================================================================
#GRAFICO
fig, ax = plt.subplots(figsize=(8,8))
ax.set_title("Misure del periodo T^2 di un pendolo semplice al variare della lunghezza l")
ax.errorbar(misure_x, misure_y_2, xerr=errori_x, yerr=errori_y_2, ecolor="red", elinewidth=0.5,
            capsize=3, marker="o", linestyle=" ")
ax.set_xlabel("l(m)")
ax.set_ylabel("T^2(s)")
ax.grid("both")
plt.show()
#===========================================================================================================