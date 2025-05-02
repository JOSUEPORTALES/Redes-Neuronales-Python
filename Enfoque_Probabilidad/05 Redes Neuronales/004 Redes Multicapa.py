import numpy as np

# Funcion sigmoide para activacion (convierte valores a un rango entre 0 y 1)
def sigmoide(valor):
    return 1 / (1 + np.exp(-valor))

# Derivada de la funcion sigmoide (para ajustar pesos)
def derivada_sigmoide(valor):
    return valor * (1 - valor)

# Entrenamiento de una red neuronal multicapa
def entrenar_red(entradas, salidas_esperadas, epocas, tasa_aprendizaje):
    # Semilla para resultados reproducibles
    np.random.seed(1)

    # Cantidad de neuronas en la capa de entrada (2), oculta (4), y salida (1)
    pesos_entrada_oculta = 2 * np.random.random((2, 4)) - 1
    pesos_oculta_salida = 2 * np.random.random((4, 1)) - 1

    for epoca in range(epocas):
        # Propagacion hacia adelante
        capa_entrada = entradas
        suma_oculta = np.dot(capa_entrada, pesos_entrada_oculta)
        capa_oculta = sigmoide(suma_oculta)

        suma_salida = np.dot(capa_oculta, pesos_oculta_salida)
        capa_salida = sigmoide(suma_salida)

        # Calculo del error
        error_salida = salidas_esperadas - capa_salida

        # Retropropagacion del error
        ajuste_salida = error_salida * derivada_sigmoide(capa_salida)
        error_oculta = ajuste_salida.dot(pesos_oculta_salida.T)
        ajuste_oculta = error_oculta * derivada_sigmoide(capa_oculta)

        # Actualizar pesos
        pesos_oculta_salida += capa_oculta.T.dot(ajuste_salida) * tasa_aprendizaje
        pesos_entrada_oculta += capa_entrada.T.dot(ajuste_oculta) * tasa_aprendizaje

        if epoca % 1000 == 0:
            print(f"Epoca {epoca}, Error promedio: {np.mean(np.abs(error_salida)):.4f}")

    return pesos_entrada_oculta, pesos_oculta_salida

# Funcion para probar la red una vez entrenada
def predecir_red(entrada, pesos_entrada_oculta, pesos_oculta_salida):
    capa_oculta = sigmoide(np.dot(entrada, pesos_entrada_oculta))
    capa_salida = sigmoide(np.dot(capa_oculta, pesos_oculta_salida))
    return capa_salida

# Datos para resolver la compuerta XOR
entradas = np.array([
    [0, 0],
    [0, 1],
    [1, 0],
    [1, 1]
])

salidas_esperadas = np.array([[0], [1], [1], [0]])

# Entrenamos la red
pesos_ocultos, pesos_finales = entrenar_red(entradas, salidas_esperadas, epocas=10000, tasa_aprendizaje=0.1)

# Probamos la red ya entrenada
print("\n=== RESULTADOS DE LA RED ===")
for entrada in entradas:
    salida = predecir_red(entrada, pesos_ocultos, pesos_finales)
    print(f"Entrada: {entrada}, Salida aproximada: {salida[0]:.4f}")
