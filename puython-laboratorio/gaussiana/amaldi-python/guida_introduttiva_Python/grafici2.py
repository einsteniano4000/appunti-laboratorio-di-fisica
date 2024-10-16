import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0,1,10)
y = x**2
z = 2*x

fig, grafici = plt.subplots(nrows=2, ncols=1, figsize=(10,6), sharex=True)
grafici[0].plot(x, y)
grafici[1].plot(x, z)
plt.show()


