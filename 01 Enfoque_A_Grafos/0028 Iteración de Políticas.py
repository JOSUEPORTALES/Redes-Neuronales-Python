import numpy as np
"""
Este programa implementa el algoritmo de Iteración de Políticas para resolver problemas de decisión en un entorno
representado como un grafo en forma de cuadrícula. El objetivo es encontrar la política óptima (la mejor acción a tomar
en cada estado) y los valores asociados a cada estado, maximizando las recompensas acumuladas.
El programa consta de las siguientes partes principales:
1. Definición del entorno: Se define una cuadrícula con recompensas específicas para cada celda.
2. Evaluación de políticas: Calcula los valores de cada estado dado una política fija.
3. Mejora de políticas: Ajusta la política para maximizar los valores de los estados.
4. Iteración de políticas: Combina la evaluación y mejora de políticas hasta que la política sea estable (óptima).
Funciones principales:
- `evaluar_politica`: Evalúa los valores de los estados para una política dada.
- `mejorar_politica`: Mejora la política basada en los valores actuales de los estados.
- `iteracion_politica`: Ejecuta el ciclo de evaluación y mejora de políticas hasta converger.
Parámetros clave:
- `filas`, `columnas`: Dimensiones del entorno (cuadrícula).
- `recompensas`: Matriz que define las recompensas para cada celda.
- `movimientos`: Diccionario que define las posibles acciones y sus efectos en la posición.
- `descuento`: Factor de descuento para calcular el valor presente de recompensas futuras.
- `epsilon`: Umbral para determinar la convergencia en la evaluación de políticas.
Resultados:
- Imprime la política óptima (dirección a tomar en cada celda).
- Imprime los valores finales asociados a cada estado.
"""





# Tamaño del entorno (grafo en forma de cuadrícula)
filas, columnas = 3, 3

# Definimos las recompensas del entorno (solo el estado final tiene una recompensa alta)
recompensas = np.array([
    [0, 0, 0],
    [0, -1, 0],
    [0, 0, 10]
])

# Definimos los posibles movimientos: (direccion, cambio en fila, cambio en columna)
movimientos = {
    '↑': (-1, 0),
    '↓': (1, 0),
    '←': (0, -1),
    '→': (0, 1)
}

# Inicializamos la politica: todas las celdas tienen una accion al azar inicialmente
politica = np.full((filas, columnas), '→')

# Inicializamos los valores de cada estado en cero
valores = np.zeros((filas, columnas))

# Parametros del algoritmo
descuento = 0.9
epsilon = 0.01

# Funcion para evaluar una politica actual
def evaluar_politica(politica, valores, recompensas, descuento, epsilon):
    while True:
        delta = 0
        for fila in range(filas):
            for columna in range(columnas):
                # Saltamos el estado terminal
                if (fila, columna) == (2, 2):
                    continue

                direccion = politica[fila][columna]
                mov_fila, mov_columna = movimientos[direccion]

                nueva_fila = fila + mov_fila
                nueva_columna = columna + mov_columna

                # Si el movimiento es valido (dentro del mapa)
                if 0 <= nueva_fila < filas and 0 <= nueva_columna < columnas:
                    valor_nuevo_estado = valores[nueva_fila][nueva_columna]
                else:
                    valor_nuevo_estado = valores[fila][columna]  # Quedarse en el mismo lugar

                valor_actual = recompensas[fila][columna] + descuento * valor_nuevo_estado
                delta = max(delta, abs(valor_actual - valores[fila][columna]))
                valores[fila][columna] = valor_actual

        if delta < epsilon:
            break

# Funcion para mejorar la politica basada en los valores actuales
def mejorar_politica(politica, valores, recompensas, descuento):
    politica_estable = True

    for fila in range(filas):
        for columna in range(columnas):
            if (fila, columna) == (2, 2):
                continue

            mejores_valores = []
            mejores_direcciones = []

            for direccion, (df, dc) in movimientos.items():
                nueva_fila = fila + df
                nueva_columna = columna + dc

                if 0 <= nueva_fila < filas and 0 <= nueva_columna < columnas:
                    valor = recompensas[fila][columna] + descuento * valores[nueva_fila][nueva_columna]
                else:
                    valor = recompensas[fila][columna] + descuento * valores[fila][columna]

                mejores_valores.append(valor)
                mejores_direcciones.append(direccion)

            mejor_indice = np.argmax(mejores_valores)
            mejor_direccion = mejores_direcciones[mejor_indice]

            if politica[fila][columna] != mejor_direccion:
                politica_estable = False
                politica[fila][columna] = mejor_direccion

    return politica_estable

# Funcion principal que combina la evaluacion y mejora de politica
def iteracion_politica(politica, valores, recompensas, descuento, epsilon):
    while True:
        evaluar_politica(politica, valores, recompensas, descuento, epsilon)
        estable = mejorar_politica(politica, valores, recompensas, descuento)
        if estable:
            break
    return politica, valores

# Ejecutamos el algoritmo
politica_final, valores_finales = iteracion_politica(politica, valores, recompensas, descuento, epsilon)

# Mostramos la politica final
print("POLITICA OPTIMA (direccion a tomar en cada celda):")
for fila in politica_final:
    print(" ".join(fila))

# Mostramos los valores finales por estado
print("\nVALORES FINALES POR ESTADO:")
for fila in valores_finales:
    print(["{0:>6.2f}".format(v) for v in fila])
