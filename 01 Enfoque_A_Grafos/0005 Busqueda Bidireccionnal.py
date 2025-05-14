from collections import deque
# La librería 'collections' proporciona contenedores especializados como 'deque',
# que es una cola de doble extremo eficiente para operaciones de inserción y eliminación
# en ambos extremos. Aquí se utiliza para implementar las fronteras de búsqueda.

# Función para reconstruir el camino completo desde inicio hasta objetivo
def reconstruir_camino(nodo_desde_inicio, nodo_desde_objetivo):
    # Convertimos ambos caminos en listas
    camino_inicio = []
    while nodo_desde_inicio:
        camino_inicio.append(nodo_desde_inicio[0])
        nodo_desde_inicio = nodo_desde_inicio[1]
    camino_inicio = camino_inicio[::-1]  # Invertimos para ir desde el inicio

    camino_objetivo = []
    while nodo_desde_objetivo:
        camino_objetivo.append(nodo_desde_objetivo[0])
        nodo_desde_objetivo = nodo_desde_objetivo[1]

    # Unimos ambos caminos (omitimos el nodo duplicado en el medio)
    return camino_inicio + camino_objetivo[1:]

# Búsqueda bidireccional
def busqueda_bidireccional(inicio, objetivo, grafo):
    if inicio == objetivo:
        return [inicio]

    # Cola para búsqueda desde el inicio
    frontera_inicio = deque([(inicio, None)])
    # Cola para búsqueda desde el objetivo
    frontera_objetivo = deque([(objetivo, None)])

    # Visitados con referencias a sus padres para ambos lados
    visitados_inicio = {inicio: (inicio, None)}
    visitados_objetivo = {objetivo: (objetivo, None)}

    while frontera_inicio and frontera_objetivo:
        # Expandimos desde el lado del inicio
        actual_inicio, padre = frontera_inicio.popleft()
        for vecino in grafo.get(actual_inicio, []):
            if vecino not in visitados_inicio:
                visitados_inicio[vecino] = (vecino, visitados_inicio[actual_inicio])
                frontera_inicio.append((vecino, visitados_inicio[actual_inicio]))
                if vecino in visitados_objetivo:
                    # Punto de encuentro encontrado
                    return reconstruir_camino(visitados_inicio[vecino], visitados_objetivo[vecino])

        # Expandimos desde el lado del objetivo
        actual_objetivo, padre = frontera_objetivo.popleft()
        for vecino in grafo.get(actual_objetivo, []):
            if vecino not in visitados_objetivo:
                visitados_objetivo[vecino] = (vecino, visitados_objetivo[actual_objetivo])
                frontera_objetivo.append((vecino, visitados_objetivo[actual_objetivo]))
                if vecino in visitados_inicio:
                    # Punto de encuentro encontrado
                    return reconstruir_camino(visitados_inicio[vecino], visitados_objetivo[vecino])

    return None  # Si no se encuentra camino

# Ejemplo de uso
if __name__ == "__main__":
    grafo = {
        'A': ['B', 'C'],
        'B': ['A', 'D', 'E'],
        'C': ['A', 'F'],
        'D': ['B'],
        'E': ['B', 'G'],
        'F': ['C'],
        'G': ['E']
    }

    inicio = 'A'
    objetivo = 'G'

    resultado = busqueda_bidireccional(inicio, objetivo, grafo)

    if resultado:
        print("Camino encontrado:", resultado)
    else:
        print("No se encontró un camino.")
