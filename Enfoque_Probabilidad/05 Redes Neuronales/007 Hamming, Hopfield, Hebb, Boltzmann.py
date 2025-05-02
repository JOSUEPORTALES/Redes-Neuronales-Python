import numpy as np

# Regla de Hebb: "las neuronas que se activan juntas, se conectan juntas"
# Entrenamos una red muy simple con patrones binarios

# Entradas: patrones binarios (0, 1), convertidos a (-1, 1)
entradas = np.array([[1, -1], [-1, 1]])
# Salidas esperadas
salidas = np.array([[1], [-1]])

# Inicializamos pesos en cero
pesos = np.zeros((2, 1))

# Aplicamos la regla de Hebb: sumamos entrada * salida para cada par
for i in range(len(entradas)):
    pesos += np.outer(entradas[i], salidas[i])

print("Pesos aprendidos por Hebb:")
print(pesos)
