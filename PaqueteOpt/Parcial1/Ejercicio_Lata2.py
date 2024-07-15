import matplotlib.pyplot as plt
import numpy as np

r = np.linspace(0.5, 8, 100)

def calcular_lata(r):
    s = (2 * np.pi * r ** 2) + (500 / r)
    return s

Sr = (500 / (4 * np.pi)) ** (1 / 3)

vH = 250 / (np.pi * Sr ** 2)
print(vH)

s_values = calcular_lata(r)

plt.plot(r, s_values)
plt.show()
