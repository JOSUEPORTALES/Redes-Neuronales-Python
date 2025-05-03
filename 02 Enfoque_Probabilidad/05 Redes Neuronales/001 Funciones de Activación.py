# Importamos las librerias necesarias
import numpy as np
import matplotlib.pyplot as plt

# Creamos un conjunto de valores de entrada (de -10 a 10)
# Simulan los valores que llegarían a una neurona en una red neuronal
entradas = np.linspace(-10, 10, 400)

# ------------------------------------------------------
# DEFINIMOS DIFERENTES FUNCIONES DE ACTIVACION
# ------------------------------------------------------

# Funcion Sigmoide: Aplana los valores entre 0 y 1
def funcion_sigmoide(x):
    return 1 / (1 + np.exp(-x))

# Funcion ReLU: Pasa los valores positivos y elimina los negativos (los pone en cero)
def funcion_relu(x):
    return np.maximum(0, x)

# Funcion TanH: Aplana los valores entre -1 y 1
def funcion_tanh(x):
    return np.tanh(x)

# Funcion Escalon: Devuelve 1 si la entrada es positiva, y 0 si es negativa o cero
def funcion_escalon(x):
    return np.where(x > 0, 1, 0)

# ------------------------------------------------------
# CALCULAMOS LAS SALIDAS PARA CADA FUNCION
# ------------------------------------------------------

salida_sigmoide = funcion_sigmoide(entradas)
salida_relu = funcion_relu(entradas)
salida_tanh = funcion_tanh(entradas)
salida_escalon = funcion_escalon(entradas)

# ------------------------------------------------------
# MOSTRAMOS EN GRAFICAS CADA FUNCION DE ACTIVACION
# ------------------------------------------------------

plt.figure(figsize=(10, 8))

# Graficamos la funcion sigmoide
plt.subplot(2, 2, 1)
plt.plot(entradas, salida_sigmoide, color='blue')
plt.title("Funcion Sigmoide")
plt.xlabel("Entrada")
plt.ylabel("Salida")

# Graficamos la funcion ReLU
plt.subplot(2, 2, 2)
plt.plot(entradas, salida_relu, color='green')
plt.title("Funcion ReLU")
plt.xlabel("Entrada")
plt.ylabel("Salida")

# Graficamos la funcion tanh
plt.subplot(2, 2, 3)
plt.plot(entradas, salida_tanh, color='red')
plt.title("Funcion TanH")
plt.xlabel("Entrada")
plt.ylabel("Salida")

# Graficamos la funcion escalon
plt.subplot(2, 2, 4)
plt.plot(entradas, salida_escalon, color='purple')
plt.title("Funcion Escalon")
plt.xlabel("Entrada")
plt.ylabel("Salida")

# Mostramos todas las graficas
plt.tight_layout()
plt.suptitle("Funciones de Activacion en Redes Neuronales", fontsize=16, y=1.02)
plt.show()
