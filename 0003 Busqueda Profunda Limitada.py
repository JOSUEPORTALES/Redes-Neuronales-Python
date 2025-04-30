# Definimos una clase para representar un nodo en el grafo
class Nodo:
    def __init__(self, estado, padre=None):
        self.estado = estado  # Estado actual del nodo
        self.padre = padre    # Nodo padre desde el que se llegó a este

# Función para reconstruir el camino desde el nodo inicial hasta el objetivo
def reconstruir_camino(nodo):
    camino = []
    while nodo is not None:
        camino.append(nodo.estado)
        nodo = nodo.padre
    return list(reversed(camino))  # Invertimos para que vaya del inicio al fin

# Búsqueda en profundidad limitada
def busqueda_profundidad_limitada(inicio, objetivo, grafo, limite):
    # Función recursiva auxiliar que realiza la búsqueda
    def dls_recursivo(nodo, profundidad):
        print(f"Visitando: {nodo.estado}, profundidad: {profundidad}")

        # Si se encuentra el objetivo, se retorna el nodo
        if nodo.estado == objetivo:
            return nodo
        
        # Si alcanzamos el límite de profundidad, no seguimos explorando
        if profundidad >= limite:
            return None

        # Se exploran los vecinos del nodo actual
        for vecino in grafo.get(nodo.estado, []):
            hijo = Nodo(vecino, nodo)
            resultado = dls_recursivo(hijo, profundidad + 1)
            if resultado is not None:
                return resultado
        
        return None  # No se encontró el objetivo en este camino

    # Creamos el nodo inicial
    nodo_inicio = Nodo(inicio)
    resultado = dls_recursivo(nodo_inicio, 0)

    # Si se encontró el objetivo, devolvemos el camino
    if resultado:
        return reconstruir_camino(resultado)
    else:
        return None  # No se encontró el objetivo

# Ejemplo de uso
if __name__ == "__main__":
    # Grafo de ejemplo representado como diccionario (lista de adyacencia)
    grafo = {
        'A': ['B', 'C'],
        'B': ['D', 'E'],
        'C': ['F'],
        'D': [],
        'E': ['G'],
        'F': [],
        'G': []
    }

    inicio = 'A'
    objetivo = 'G'
    limite = 3  # Límite de profundidad

    resultado = busqueda_profundidad_limitada(inicio, objetivo, grafo, limite)

    if resultado:
        print("Camino encontrado:", resultado)
    else:
        print("No se encontró un camino dentro del límite de profundidad.")
