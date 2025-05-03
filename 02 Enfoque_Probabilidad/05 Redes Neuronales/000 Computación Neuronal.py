# --------------------------------------------
# COMPUTACION NEURONAL - Red neuronal simple
# Tema: Introduccion a la I.A. - Enfoque: Redes Neuronales
# --------------------------------------------

import numpy as np  # Importamos numpy para manejo de matrices y funciones matematicas

# --------------------------------------------
# FUNCION DE ACTIVACION
# --------------------------------------------

# Esta funcion transforma valores a un rango entre 0 y 1
# Util para representar probabilidades
def sigmoide(x):
    return 1 / (1 + np.exp(-x))

# Derivada de la funcion sigmoide, necesaria para ajustar los pesos durante el aprendizaje
def derivada_sigmoide(x):
    return x * (1 - x)

# --------------------------------------------
# DATOS DE ENTRADA Y SALIDA ESPERADA
# --------------------------------------------

# Entradas: cada fila representa una persona con [horas de estudio, nivel de comprension]
entradas = np.array([
    [2, 0.5],   # poco estudio, comprension media
    [4, 0.4],   # estudio regular, comprension baja
    [6, 0.8],   # estudio alto, comprension buena
    [1, 0.2],   # poco estudio, baja comprension
    [5, 0.7],   # buen estudio, buena comprension
    [3, 0.3]    # promedio general
])

# Salidas esperadas: 1 = aprueba, 0 = reprueba
salidas = np.array([[0], [0], [1], [0], [1], [0]])

# --------------------------------------------
# INICIALIZAMOS PESOS Y PARAMETROS
# --------------------------------------------

np.random.seed(42)  # Semilla para que los resultados sean repetibles

# Creamos pesos aleatorios para la capa oculta (2 entradas -> 3 neuronas ocultas)
pesos_capa_oculta = np.random.rand(2, 3)

# Creamos pesos para la capa de salida (3 neuronas ocultas -> 1 salida)
pesos_capa_salida = np.random.rand(3, 1)

# Bias para cada capa
bias_capa_oculta = np.random.rand(1, 3)
bias_capa_salida = np.random.rand(1, 1)

# Tasa de aprendizaje: cuanto se ajustan los pesos en cada iteracion
tasa_aprendizaje = 0.1

# --------------------------------------------
# ENTRENAMIENTO DE LA RED NEURONAL
# --------------------------------------------

for epoca in range(10000):
    # FORWARD PASS (propagacion hacia adelante)
    entrada_oculta = np.dot(entradas, pesos_capa_oculta) + bias_capa_oculta
    salida_oculta = sigmoide(entrada_oculta)

    entrada_final = np.dot(salida_oculta, pesos_capa_salida) + bias_capa_salida
    salida_final = sigmoide(entrada_final)

    # CALCULO DEL ERROR
    error = salidas - salida_final

    # BACKPROPAGATION (ajuste de pesos)
    delta_salida = error * derivada_sigmoide(salida_final)
    delta_oculta = delta_salida.dot(pesos_capa_salida.T) * derivada_sigmoide(salida_oculta)

    # ACTUALIZAMOS PESOS Y BIAS
    pesos_capa_salida += salida_oculta.T.dot(delta_salida) * tasa_aprendizaje
    bias_capa_salida += np.sum(delta_salida, axis=0, keepdims=True) * tasa_aprendizaje

    pesos_capa_oculta += entradas.T.dot(delta_oculta) * tasa_aprendizaje
    bias_capa_oculta += np.sum(delta_oculta, axis=0, keepdims=True) * tasa_aprendizaje

    # Mostramos el error promedio cada 2000 iteraciones
    if epoca % 2000 == 0:
        error_promedio = np.mean(np.abs(error))
        print(f"Epoca {epoca} - Error promedio: {error_promedio:.4f}")

# --------------------------------------------
# PRUEBA DE LA RED ENTRENADA
# --------------------------------------------

print("\n--- PRUEBAS DE LA RED ENTRENADA ---")

# Nuevos datos para predecir
nuevos_datos = np.array([
    [5, 0.6],   # buen estudio y comprension
    [2, 0.1],   # poco estudio y comprension baja
    [6, 0.9]    # excelente estudio y comprension
])

# Hacemos predicciones
salida_oculta = sigmoide(np.dot(nuevos_datos, pesos_capa_oculta) + bias_capa_oculta)
salida_final = sigmoide(np.dot(salida_oculta, pesos_capa_salida) + bias_capa_salida)

# Mostramos resultados
for i, resultado in enumerate(salida_final):
    estado = "APRUEBA" if resultado > 0.5 else "REPRUEBA"
    print(f"Entrada: {nuevos_datos[i]} -> Probabilidad: {resultado[0]:.2f} -> Resultado: {estado}")
