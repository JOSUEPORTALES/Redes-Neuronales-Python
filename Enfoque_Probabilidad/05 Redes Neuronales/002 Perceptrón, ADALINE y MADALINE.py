import numpy as np

# Funcion de activacion escalon para el perceptron
def funcion_escalon(valor):
    return 1 if valor >= 0 else 0

# Funcion de activacion lineal para ADALINE
def funcion_lineal(valor):
    return valor

# Entrenamiento de un perceptron
def entrenar_perceptron(entradas, salidas_esperadas, tasa_aprendizaje, epocas):
    pesos = np.zeros(entradas.shape[1])
    sesgo = 0

    for epoca in range(epocas):
        print(f"Epoca {epoca+1}")
        for i in range(len(entradas)):
            suma = np.dot(entradas[i], pesos) + sesgo
            salida = funcion_escalon(suma)
            error = salidas_esperadas[i] - salida
            pesos += tasa_aprendizaje * error * entradas[i]
            sesgo += tasa_aprendizaje * error
            print(f"Entrada: {entradas[i]}, Esperado: {salidas_esperadas[i]}, Salida: {salida}, Error: {error}")
        print(f"Pesos: {pesos}, Sesgo: {sesgo}\n")
    
    return pesos, sesgo

# Entrenamiento de ADALINE
def entrenar_adaline(entradas, salidas_esperadas, tasa_aprendizaje, epocas):
    pesos = np.zeros(entradas.shape[1])
    sesgo = 0

    for epoca in range(epocas):
        print(f"Epoca {epoca+1}")
        for i in range(len(entradas)):
            salida = funcion_lineal(np.dot(entradas[i], pesos) + sesgo)
            error = salidas_esperadas[i] - salida
            pesos += tasa_aprendizaje * error * entradas[i]
            sesgo += tasa_aprendizaje * error
            print(f"Entrada: {entradas[i]}, Esperado: {salidas_esperadas[i]}, Salida: {salida:.2f}, Error: {error:.2f}")
        print(f"Pesos: {pesos}, Sesgo: {sesgo}\n")
    
    return pesos, sesgo

# Datos de entrenamiento (puerta logica OR)
entradas = np.array([
    [0, 0],
    [0, 1],
    [1, 0],
    [1, 1]
])
salidas_or = np.array([0, 1, 1, 1])

# Entrenamiento y pruebas
print("=== PERCEPTRON ===")
pesos_p, sesgo_p = entrenar_perceptron(entradas, salidas_or, tasa_aprendizaje=0.1, epocas=5)

print("=== ADALINE ===")
pesos_a, sesgo_a = entrenar_adaline(entradas, salidas_or, tasa_aprendizaje=0.1, epocas=5)

# MADALINE: es una red con multiples ADALINE organizadas en capas, su implementacion completa requiere arquitectura multicapa.
print("Nota: MADALINE es una red neuronal con multiples unidades ADALINE. Se usa para problemas no lineales y requiere estructuras mas complejas.\n")
