import matplotlib.pyplot as plt
import numpy as np
x = np.random.rand(50)
y = np.random.rand(50)

plt.scatter(x, y)
plt.title("Grafico a Dispersione")
plt.xlabel("X")
plt.ylabel("Y")
plt.savefig('grafico_dispersione.png') 
plt.show()
