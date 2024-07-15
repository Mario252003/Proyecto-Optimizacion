import numpy as np
import matplotlib.pyplot as plt

# Definición de las funciones matemáticas
def caja(l):
    return -1 * (4 * (l)**3 - 60 * (l)**2 + 200 * l)

def lata(r):
    return 2 * np.pi * (r**2) + 500 / r

def f1(x):
    return ((x)**2) + 54 / x

def f3(x):
    return ((x)**4) + ((x)**2) - 33

def f4(x):
    return (3 * ((x)**4)) - (8 * ((x)**3)) - (6 * ((x)**2)) + 12 * (x)

# Método de la secante ajustado con delta y epsilon
def met_secante(a, b, epsilon, f):
    x1, x2 = a, b
    delta = lambda x: 0.01 * abs(x) if abs(x) > 0.01 else 0.0001
    z = x2 - (derivada(f, x2, delta(x2)) / (derivada(f, x2, delta(x2)) - derivada(f, x1, delta(x1)) / (x2 - x1)))
    while abs(derivada(f, z, delta(z))) > epsilon:
        z = x2 - (derivada(f, x2, delta(x2)) / (derivada(f, x2, delta(x2)) - derivada(f, x1, delta(x1)) / (x2 - x1)))
        if derivada(f, z, delta(z)) < 0:
            x1 = z
        else:
            x2 = z
    return z  

# Función para calcular la derivada numérica
def derivada(f, x, delta):
    return (f(x + delta) - f(x - delta)) / (2 * delta)

# Generación de rangos para cada función
limites_lata = np.linspace(0.5, 8, 100)
limites_caja = np.linspace(2, 3, 100)
limites_f1 = np.linspace(0, 10, 100)
limites_f3 = np.linspace(-2.5, 2.5, 100)
limites_f4 = np.linspace(-1.5, 3, 100)

# Generación de puntos para cada función usando el método de la secante con diferentes epsilons
puntos_lata1 = met_secante(0.6, 5, 0.5, lata)
puntos_lata2 = met_secante(0.6, 5, 0.1, lata)
puntos_lata3 = met_secante(0.6, 5, 0.01, lata)
puntos_lata4 = met_secante(0.6, 5, 0.0001, lata)

puntos_caja1 = met_secante(2, 3, 0.5, caja)
puntos_caja2 = met_secante(2, 3, 0.1, caja)
puntos_caja3 = met_secante(2, 3, 0.01, caja)
puntos_caja4 = met_secante(2, 3, 0.0001, caja)

puntos_f11 = met_secante(0.6, 5, 0.5, f1)
puntos_f12 = met_secante(0.6, 5, 0.1, f1)
puntos_f13 = met_secante(0.6, 5, 0.01, f1)
puntos_f14 = met_secante(0.6, 5, 0.0001, f1)

puntos_f31 = met_secante(-2, 2.5, 0.5, f3)
puntos_f32 = met_secante(-2, 2.5, 0.1, f3)
puntos_f33 = met_secante(-2, 2.5, 0.01, f3)
puntos_f34 = met_secante(-2, 2.5, 0.0001, f3)

puntos_f41 = met_secante(-1.8, 2.5, 0.5, f4)
puntos_f42 = met_secante(-1.8, 2.5, 0.1, f4)
puntos_f43 = met_secante(-1.8, 2.5, 0.01, f4)
puntos_f44 = met_secante(-1.8, 2.5, 0.0001, f4)

# Gráficos de las funciones y sus puntos encontrados

# Función lata
plt.figure(figsize=(8, 6))
plt.plot(limites_lata, lata(limites_lata), label='Función Lata')
plt.scatter(puntos_lata1, lata(puntos_lata1), label='Epsilon=0.5', marker='o')
plt.scatter(puntos_lata2, lata(puntos_lata2), label='Epsilon=0.1', marker='o')
plt.scatter(puntos_lata3, lata(puntos_lata3), label='Epsilon=0.01', marker='o')
plt.scatter(puntos_lata4, lata(puntos_lata4), label='Epsilon=0.0001', marker='o')
plt.xlabel('Valores de x')
plt.ylabel('Valores de y')
plt.title('Función Lata')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# Función caja
plt.figure(figsize=(8, 6))
plt.plot(limites_caja, caja(limites_caja), label='Función Caja')
plt.scatter(puntos_caja1, caja(puntos_caja1), label='Epsilon=0.5', marker='o')
plt.scatter(puntos_caja2, caja(puntos_caja2), label='Epsilon=0.1', marker='o')
plt.scatter(puntos_caja3, caja(puntos_caja3), label='Epsilon=0.01', marker='o')
plt.scatter(puntos_caja4, caja(puntos_caja4), label='Epsilon=0.0001', marker='o')
plt.xlabel('Valores de x')
plt.ylabel('Valores de y')
plt.title('Función Caja')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# Función f1
plt.figure(figsize=(8, 6))
plt.plot(limites_f1, f1(limites_f1), label='Función f1')
plt.scatter(puntos_f11, f1(puntos_f11), label='Epsilon=0.5', marker='o')
plt.scatter(puntos_f12, f1(puntos_f12), label='Epsilon=0.1', marker='o')
plt.scatter(puntos_f13, f1(puntos_f13), label='Epsilon=0.01', marker='o')
plt.scatter(puntos_f14, f1(puntos_f14), label='Epsilon=0.0001', marker='o')
plt.xlabel('Valores de x')
plt.ylabel('Valores de y')
plt.title('Función f1')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# Función f3
plt.figure(figsize=(8, 6))
plt.plot(limites_f3, f3(limites_f3), label='Función f3')
plt.scatter(puntos_f31, f3(puntos_f31), label='Epsilon=0.5', marker='o')
plt.scatter(puntos_f32, f3(puntos_f32), label='Epsilon=0.1', marker='o')
plt.scatter(puntos_f33, f3(puntos_f33), label='Epsilon=0.01', marker='o')
plt.scatter(puntos_f34, f3(puntos_f34), label='Epsilon=0.0001', marker='o')
plt.xlabel('Valores de x')
plt.ylabel('Valores de y')
plt.title('Función f3')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# Función f4
plt.figure(figsize=(8, 6))
plt.plot(limites_f4, f4(limites_f4), label='Función f4')
plt.scatter(puntos_f41, f4(puntos_f41), label='Epsilon=0.5', marker='o')
plt.scatter(puntos_f42, f4(puntos_f42), label='Epsilon=0.1', marker='o')
plt.scatter(puntos_f43, f4(puntos_f43), label='Epsilon=0.01', marker='o')
plt.scatter(puntos_f44, f4(puntos_f44), label='Epsilon=0.0001', marker='o')
plt.xlabel('Valores de x')
plt.ylabel('Valores de y')
plt.title('Función f4')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
