import numpy as np

t = np.linspace(0, 10, 11)
v = 2.0
s1 = v*t

a = 9.81
s2 = v*t + 0.5*a*t**2

print(s1)
print(s2)

