# Importamos librerias necesarias
import numpy as np

# ------------------------------------------
# FUNCIONES DE ACTIVACION Y DERIVADAS
# ------------------------------------------

# Funcion sigmoide para la activacion de las neuronas
def sigmoide(x):
    return 1 / (1 + np.exp(-x))

# Derivada de la funcion sigmoide (necesaria para retropropagacion)
def derivada_sigmoide(x):
    return x * (1 - x)

# ------------------------------------------
# DATOS DE ENTRENAMIENTO (FUNCION AND)
# ------------------------------------------

# Entradas posibles para la funcion AND (2 variables de entrada)
entradas = np.array([
    [0, 0],
    [0, 1],
    [1, 0],
    [1, 1]
])

# Salidas esperadas de la funcion AND
# Solo es 1 cuando ambas entradas son 1
salidas_esperadas = np.array([[0], [0], [0], [1]])

# Semilla para resultados reproducibles
np.random.seed(1)

# ------------------------------------------
# INICIALIZAMOS PESOS ALEATORIOS
# ------------------------------------------

# Pesos entre capa de entrada y capa oculta (2 neuronas en capa oculta)
pesos_entrada_oculta = 2 * np.random.random((2, 2)) - 1

# Pesos entre capa oculta y capa de salida (1 sola neurona en la salida)
pesos_oculta_salida = 2 * np.random.random((2, 1)) - 1

# ------------------------------------------
# ENTRENAMIENTO DE LA RED
# ------------------------------------------

# Numero de veces que entrenaremos la red
epocas = 10000

for epoca in range(epocas):
    # PASO 1: Propagacion hacia adelante

    # Capa de entrada -> capa oculta
    capa_oculta = sigmoide(np.dot(entradas, pesos_entrada_oculta))

    # Capa oculta -> salida
    salida_calculada = sigmoide(np.dot(capa_oculta, pesos_oculta_salida))

    # PASO 2: Calculo del error
    error_salida = salidas_esperadas - salida_calculada

    # PASO 3: Retropropagacion del error

    # Calculamos ajuste para pesos entre capa oculta y salida
    ajuste_salida = error_salida * derivada_sigmoide(salida_calculada)

    # Calculamos error que viene desde la salida hacia la capa oculta
    error_oculta = ajuste_salida.dot(pesos_oculta_salida.T)

    # Ajuste para los pesos entre entrada y capa oculta
    ajuste_oculta = error_oculta * derivada_sigmoide(capa_oculta)

    # PASO 4: Ajuste de pesos
    pesos_oculta_salida += capa_oculta.T.dot(ajuste_salida)
    pesos_entrada_oculta += entradas.T.dot(ajuste_oculta)

# ------------------------------------------
# RESULTADO FINAL
# ------------------------------------------

print("Resultado de la red neuronal entrenada (funcion AND):")
for i in range(len(entradas)):
    entrada = entradas[i]
    # Pasamos la entrada por la red entrenada
    capa_oculta = sigmoide(np.dot(entrada, pesos_entrada_oculta))
    salida = sigmoide(np.dot(capa_oculta, pesos_oculta_salida))
    print(f"Entrada: {entrada} -> Salida: {round(float(salida), 3)}")
