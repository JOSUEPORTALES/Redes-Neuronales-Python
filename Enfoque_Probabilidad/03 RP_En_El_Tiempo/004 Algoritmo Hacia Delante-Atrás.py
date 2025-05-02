import numpy as np
import matplotlib.pyplot as plt

# Estados ocultos posibles
estados = ['lluvia', 'sol']

# Observaciones posibles
observaciones_posibles = ['paraguas', 'sin_paraguas']

# Probabilidad inicial de cada estado
probabilidad_inicial = {
    'lluvia': 0.6,
    'sol': 0.4
}

# Matriz de transicion entre estados
transicion = {
    'lluvia': {'lluvia': 0.7, 'sol': 0.3},
    'sol': {'lluvia': 0.4, 'sol': 0.6}
}

# Matriz de emision: probabilidad de observacion dado el estado
emision = {
    'lluvia': {'paraguas': 0.9, 'sin_paraguas': 0.1},
    'sol': {'paraguas': 0.2, 'sin_paraguas': 0.8}
}

# Observaciones realizadas (por ejemplo, durante 5 dias)
secuencia_observada = ['paraguas', 'paraguas', 'sin_paraguas', 'paraguas', 'paraguas']

# ------------------- FUNCION ADELANTE -------------------
def adelante(observaciones, estados, prob_ini, trans, emis):
    paso_adelante = []

    # Paso inicial: aplicar probabilidad inicial y de emision
    estado_actual = {
        estado: prob_ini[estado] * emis[estado][observaciones[0]] for estado in estados
    }

    # Normalizamos (para que las probabilidades sumen 1)
    normalizador = sum(estado_actual.values())
    for estado in estado_actual:
        estado_actual[estado] /= normalizador

    paso_adelante.append(estado_actual.copy())

    # Para cada observacion posterior, aplicamos el paso hacia adelante
    for observacion in observaciones[1:]:
        nuevo_estado = {}
        for estado in estados:
            suma = sum(
                paso_adelante[-1][estado_anterior] * trans[estado_anterior][estado]
                for estado_anterior in estados
            )
            nuevo_estado[estado] = emis[estado][observacion] * suma
        # Normalizamos
        normalizador = sum(nuevo_estado.values())
        for estado in nuevo_estado:
            nuevo_estado[estado] /= normalizador
        paso_adelante.append(nuevo_estado.copy())

    return paso_adelante

# ------------------- FUNCION ATRAS -------------------
def atras(observaciones, estados, trans, emis):
    n = len(observaciones)
    paso_atras = [{} for _ in range(n)]

    # Paso inicial: al final todas las probabilidades hacia adelante son 1
    for estado in estados:
        paso_atras[-1][estado] = 1.0

    # Recorremos hacia atras
    for t in reversed(range(n - 1)):
        for estado in estados:
            suma = sum(
                trans[estado][estado_siguiente] *
                emis[estado_siguiente][observaciones[t + 1]] *
                paso_atras[t + 1][estado_siguiente]
                for estado_siguiente in estados
            )
            paso_atras[t][estado] = suma

        # Normalizamos
        normalizador = sum(paso_atras[t].values())
        for estado in paso_atras[t]:
            paso_atras[t][estado] /= normalizador

    return paso_atras

# ------------------- FUNCION HACIA ADELANTE-ATRAS -------------------
def hacia_adelante_atras(observaciones, estados, prob_ini, trans, emis):
    paso_adelante = adelante(observaciones, estados, prob_ini, trans, emis)
    paso_atras = atras(observaciones, estados, trans, emis)

    # Combinar ambos para obtener la probabilidad posterior
    posterior = []
    for t in range(len(observaciones)):
        posterior_t = {}
        for estado in estados:
            posterior_t[estado] = paso_adelante[t][estado] * paso_atras[t][estado]
        # Normalizamos
        normalizador = sum(posterior_t.values())
        for estado in posterior_t:
            posterior_t[estado] /= normalizador
        posterior.append(posterior_t)
    return posterior

# ------------------- FUNCION PARA GRAFICAR -------------------
def graficar_resultados(titulo, posterior):
    plt.figure(figsize=(10, 5))
    for estado in estados:
        prob = [p[estado] for p in posterior]
        plt.plot(range(len(prob)), prob, marker='o', label=estado)
    plt.title(f"Probabilidad posterior por dia - {titulo}")
    plt.xlabel("Dia")
    plt.ylabel("Probabilidad")
    plt.xticks(range(len(posterior)))
    plt.legend()
    plt.grid(True)
    plt.show()

# ------------------- PROGRAMA PRINCIPAL -------------------
if __name__ == "__main__":
    print("Algoritmo Hacia Adelante-Atras para inferencia de estados ocultos\n")

    resultado_posterior = hacia_adelante_atras(secuencia_observada, estados, probabilidad_inicial, transicion, emision)

    # Mostramos los resultados por dia
    for i, distribucion in enumerate(resultado_posterior):
        print(f"Dia {i+1}:")
        for estado in distribucion:
            print(f"  {estado}: {distribucion[estado]:.4f}")

    # Graficamos
    graficar_resultados("Algoritmo Hacia Adelante-Atras", resultado_posterior)
