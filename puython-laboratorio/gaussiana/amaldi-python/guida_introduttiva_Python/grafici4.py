import matplotlib.pyplot as plt
import numpy as np


figura, grafico = plt.subplots(figsize=(10,6))
rettangolo = plt.Rectangle((0.2,0.2),0.3,0.5,color="red")
cerchio = plt.Circle((0.6, 0.4), 0.2, color="blue")
grafico.add_artist(rettangolo)
grafico.add_artist(cerchio)
grafico.set_aspect("equal")
plt.show()





