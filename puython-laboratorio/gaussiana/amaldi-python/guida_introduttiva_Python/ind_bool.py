import numpy as np

x = np.random.uniform(-1,1,4)
print(x)
print(x>0)
print(np.count_nonzero(x>0))
print(x[x>0])


