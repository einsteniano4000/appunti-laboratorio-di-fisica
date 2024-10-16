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
#GRAFICO
fig, ax = plt.subplots(figsize=(8,8))
ax.set_title("Misure del periodo T di un pendolo semplice al variare della lunghezza l")
ax.errorbar(misure_x, misure_y, xerr=errori_x, yerr=errori_y, ecolor="black", elinewidth=0.5,
            capsize=3, marker="o", linestyle=" ")
ax.set_xlabel("l(m)")
ax.set_ylabel("T(s)")
ax.grid("both")
plt.show()
#===========================================================================================================