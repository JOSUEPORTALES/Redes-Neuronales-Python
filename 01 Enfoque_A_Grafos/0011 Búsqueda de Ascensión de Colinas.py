import random
"""
Este programa implementa el algoritmo de Búsqueda de Ascensión de Colinas para encontrar el máximo local
de una función objetivo. La función objetivo utilizada en este caso es f(x) = -x^2 + 5x + 2, una parábola
invertida. El algoritmo comienza desde un punto inicial aleatorio y se mueve hacia soluciones vecinas
que mejoren el valor de la función objetivo. Si no se encuentra una mejora, el algoritmo concluye que
ha alcanzado un máximo local.
Funciones:
- funcion_objetivo(x): Calcula el valor de la función objetivo para un valor dado de x.
- busqueda_ascension_colinas(funcion_objetivo, inicio, paso, max_iteraciones): Implementa el algoritmo
    de Búsqueda de Ascensión de Colinas. Recibe como parámetros la función objetivo, el punto inicial,
    el tamaño del paso y el número máximo de iteraciones.
Parámetros de ejecución:
- inicio: Punto inicial aleatorio entre -10 y 10.
- paso: Tamaño del paso para explorar soluciones vecinas.
- max_iteraciones: Número máximo de iteraciones permitidas.
Salida:
- Imprime el progreso del algoritmo en cada iteración, indicando el movimiento hacia una mejor solución
    o la detención al alcanzar un máximo local.
- Al final, muestra la solución final encontrada y el valor correspondiente de la función objetivo.
"""



# Definir la función a maximizar (en este caso, f(x) = -x^2 + 5x + 2)
def funcion_objetivo(x):
    return -x**2 + 5*x + 2

# Función para la Búsqueda de Ascensión de Colinas
def busqueda_ascension_colinas(funcion_objetivo, inicio, paso, max_iteraciones):
    # Comenzamos desde una solución inicial
    solucion_actual = inicio
    valor_actual = funcion_objetivo(solucion_actual)
    
    for i in range(max_iteraciones):
        # Generar soluciones vecinas (en este caso, moverse hacia la izquierda o derecha)
        vecinos = [solucion_actual + paso, solucion_actual - paso]
        
        # Evaluar la función en las soluciones vecinas
        vecino_mejor = max(vecinos, key=funcion_objetivo)
        
        # Si el vecino es mejor, nos movemos hacia él
        if funcion_objetivo(vecino_mejor) > valor_actual:
            solucion_actual = vecino_mejor
            valor_actual = funcion_objetivo(solucion_actual)
            print(f"Iteración {i+1}: Moverse a {solucion_actual} con valor {valor_actual}")
        else:
            # Si no hay mejora, hemos llegado a un máximo local
            print(f"Iteración {i+1}: No hay mejora, hemos alcanzado el máximo local.")
            break
    
    return solucion_actual, valor_actual

# Parámetros de ejecución
inicio = random.uniform(-10, 10)  # Solución inicial aleatoria entre -10 y 10
paso = 0.1  # Paso de búsqueda
max_iteraciones = 100  # Número máximo de iteraciones

# Ejecutar la Búsqueda de Ascensión de Colinas
solucion_final, valor_final = busqueda_ascension_colinas(funcion_objetivo, inicio, paso, max_iteraciones)

print(f"\nSolución final encontrada: x = {solucion_final}, f(x) = {valor_final}")
