import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0,1,10)
y = x**2

figura, grafico = plt.subplots(figsize=(10,6))
grafico.plot(x, y)
plt.show()


