import numpy as np
import matplotlib.pyplot as plt

# ------------------------------------------
# Definimos los estados posibles del clima
# ------------------------------------------
estados = ['soleado', 'lluvioso']

# ------------------------------------------
# Definimos las evidencias posibles (lo que observamos)
# ------------------------------------------
evidencias = ['sin_paraguas', 'con_paraguas']

# ------------------------------------------
# Matriz de transición de estados (probabilidades de pasar de un clima a otro)
# Por ejemplo, si ayer fue soleado, hay un 70% de que hoy también lo sea
matriz_transicion = np.array([
    [0.7, 0.3],  # De soleado a [soleado, lluvioso]
    [0.3, 0.7]   # De lluvioso a [soleado, lluvioso]
])

# ------------------------------------------
# Matriz de observación (probabilidad de ver un paraguas dependiendo del clima)
# Por ejemplo, si es soleado, hay un 10% de ver a alguien con paraguas
matriz_observacion = np.array([
    [0.9, 0.1],  # Clima soleado -> [sin_paraguas, con_paraguas]
    [0.2, 0.8]   # Clima lluvioso -> [sin_paraguas, con_paraguas]
])

# ------------------------------------------
# Estado inicial (no sabemos, así que asumimos distribución uniforme)
# ------------------------------------------
estado_inicial = np.array([0.5, 0.5])  # 50% soleado, 50% lluvioso

# ------------------------------------------
# Observaciones que obtenemos en una semana (1 = con paraguas, 0 = sin paraguas)
# ------------------------------------------
observaciones = [1, 1, 0, 1, 1, 0, 0]  # ejemplo: lunes a domingo

# ------------------------------------------
# FILTRADO: calcular la probabilidad de los estados dado lo observado hasta hoy
# ------------------------------------------
def filtrar(observaciones, estado_inicial, matriz_transicion, matriz_observacion):
    historial = []
    estado_actual = estado_inicial

    for dia, obs in enumerate(observaciones):
        # Paso 1: estimar el nuevo estado con la transición
        estado_predicho = np.dot(estado_actual, matriz_transicion)

        # Paso 2: aplicar la evidencia (observación)
        estado_filtrado = estado_predicho * matriz_observacion[:, obs]

        # Paso 3: normalizar para que sea una distribución de probabilidad válida
        estado_filtrado = estado_filtrado / np.sum(estado_filtrado)

        # Guardamos el estado estimado
        historial.append(estado_filtrado)

        # Este estado filtrado se usará para el siguiente día
        estado_actual = estado_filtrado

    return np.array(historial)

# ------------------------------------------
# PREDICCIÓN: predecimos los estados futuros sin nuevas observaciones
# ------------------------------------------
def predecir(estado_actual, matriz_transicion, pasos):
    predicciones = []
    for _ in range(pasos):
        estado_actual = np.dot(estado_actual, matriz_transicion)
        predicciones.append(estado_actual)
    return np.array(predicciones)

# ------------------------------------------
# SUAVIZADO: inferimos estados pasados con información futura
# ------------------------------------------
def suavizar(historial_filtrado, matriz_transicion):
    pasos = len(historial_filtrado)
    suavizado = [None] * pasos
    suavizado[-1] = historial_filtrado[-1]

    # Variable para ir calculando hacia atrás
    mensaje = np.ones(len(estados))

    for t in reversed(range(pasos - 1)):
        siguiente = suavizado[t + 1]
        # Ecuación de suavizado (hacia atrás)
        mensaje = np.dot(matriz_transicion, matriz_observacion[:, observaciones[t + 1]] * mensaje)
        estado_suavizado = historial_filtrado[t] * mensaje
        estado_suavizado /= np.sum(estado_suavizado)
        suavizado[t] = estado_suavizado

    return np.array(suavizado)

# Ejecutamos el filtrado
historial_filtrado = filtrar(observaciones, estado_inicial, matriz_transicion, matriz_observacion)

# Ejecutamos la predicción para 3 días después de la semana
estado_final = historial_filtrado[-1]
predicciones = predecir(estado_final, matriz_transicion, 3)

# Ejecutamos el suavizado
historial_suavizado = suavizar(historial_filtrado, matriz_transicion)

# ------------------------------------------
# Graficamos los resultados
# ------------------------------------------
dias = ['Lun', 'Mar', 'Mie', 'Jue', 'Vie', 'Sab', 'Dom']
dias_prediccion = ['Lun+', 'Mar+', 'Mie+']

plt.figure(figsize=(12, 6))

# Filtrado
plt.subplot(1, 3, 1)
plt.title("Filtrado (estado actual)")
plt.plot(historial_filtrado[:, 0], label='Soleado')
plt.plot(historial_filtrado[:, 1], label='Lluvioso')
plt.xticks(range(len(dias)), dias)
plt.ylim(0, 1)
plt.legend()

# Suavizado
plt.subplot(1, 3, 2)
plt.title("Suavizado (ajuste pasado)")
plt.plot(historial_suavizado[:, 0], label='Soleado')
plt.plot(historial_suavizado[:, 1], label='Lluvioso')
plt.xticks(range(len(dias)), dias)
plt.ylim(0, 1)
plt.legend()

# Predicción
plt.subplot(1, 3, 3)
plt.title("Predicción (futuro)")
plt.plot(predicciones[:, 0], label='Soleado')
plt.plot(predicciones[:, 1], label='Lluvioso')
plt.xticks(range(len(dias_prediccion)), dias_prediccion)
plt.ylim(0, 1)
plt.legend()

plt.tight_layout()
plt.show()

