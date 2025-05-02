import numpy as np

# --------------------------------------------
# MODELO DE MARKOV OCULTO (HMM) - desde cero
# Tema: Introducción a la I.A.
# Subtema: Enfoque Probabilístico - Aprendizaje Probabilístico
# --------------------------------------------

# --------------------------------------------
# 1. DEFINIMOS LOS ELEMENTOS DEL MODELO
# --------------------------------------------

# Estados ocultos (emociones): no se observan directamente
estados = ['feliz', 'triste']
numero_estados = len(estados)

# Observaciones posibles (frases que oímos)
observaciones_posibles = ['jaja', 'meh', 'buuu']
numero_observaciones = len(observaciones_posibles)

# Diccionario para convertir frases a índices
diccionario_observaciones = {'jaja': 0, 'meh': 1, 'buuu': 2}

# Secuencia de frases que escuchamos
frases_observadas = ['jaja', 'meh', 'meh', 'buuu', 'jaja']
secuencia_observada = [diccionario_observaciones[frase] for frase in frases_observadas]

# Probabilidad de empezar en cada estado
prob_inicio = [0.6, 0.4]  # más probable comenzar feliz

# Matriz de transición entre estados
# Ejemplo: de feliz a feliz o triste
prob_transicion = [
    [0.7, 0.3],  # desde feliz
    [0.4, 0.6]   # desde triste
]

# Matriz de emisión (probabilidad de decir una frase dado el estado)
# Cada fila es un estado, cada columna una frase
prob_emision = [
    [0.6, 0.3, 0.1],  # feliz: más probable decir "jaja"
    [0.1, 0.4, 0.5]   # triste: más probable decir "buuu"
]

# --------------------------------------------
# 2. ALGORITMO DE VITERBI (hecho desde cero)
# --------------------------------------------

def viterbi(secuencia, prob_inicio, prob_transicion, prob_emision):
    T = len(secuencia)           # longitud de la secuencia observada
    N = len(prob_inicio)         # número de estados
    V = np.zeros((N, T))         # matriz de probabilidades
    camino = np.zeros((N, T), dtype=int)  # para guardar los caminos

    # Paso 1: inicialización con la primera observación
    for estado in range(N):
        V[estado, 0] = prob_inicio[estado] * prob_emision[estado][secuencia[0]]
        camino[estado, 0] = 0

    # Paso 2: iteración sobre el tiempo
    for t in range(1, T):
        for estado_actual in range(N):
            probabilidades = []
            for estado_anterior in range(N):
                prob = V[estado_anterior, t-1] * prob_transicion[estado_anterior][estado_actual] * prob_emision[estado_actual][secuencia[t]]
                probabilidades.append(prob)
            V[estado_actual, t] = max(probabilidades)
            camino[estado_actual, t] = np.argmax(probabilidades)

    # Paso 3: reconstruir la mejor secuencia de estados
    estados_optimos = np.zeros(T, dtype=int)
    estados_optimos[T-1] = np.argmax(V[:, T-1])
    for t in range(T-2, -1, -1):
        estados_optimos[t] = camino[estados_optimos[t+1], t+1]

    return estados_optimos

# --------------------------------------------
# 3. EJECUTAMOS Y MOSTRAMOS RESULTADOS
# --------------------------------------------

# Ejecutamos Viterbi
estados_estimados = viterbi(secuencia_observada, prob_inicio, prob_transicion, prob_emision)

# Imprimimos resultados
print("Frases observadas:")
print(frases_observadas)

print("\nSecuencia estimada de estados emocionales:")
for i, estado in enumerate(estados_estimados):
    print(f"{frases_observadas[i]} --> {estados[estado]}")
