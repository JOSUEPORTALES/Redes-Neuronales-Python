# Clase para representar un nodo con su estado y su padre (para reconstruir el camino)
class Nodo:
    def __init__(self, estado, padre=None):
        self.estado = estado
        self.padre = padre

# Función para reconstruir el camino desde el nodo objetivo hasta el inicial
def reconstruir_camino(nodo):
    camino = []
    while nodo is not None:
        camino.append(nodo.estado)
        nodo = nodo.padre
    return list(reversed(camino))  # Invertimos para que el camino sea de inicio a fin

# Función de búsqueda en profundidad limitada (DLS), reutilizada por IDDFS
def busqueda_profundidad_limitada(nodo, objetivo, grafo, limite):
    print(f"Explorando {nodo.estado} a profundidad {limite}")
    
    if nodo.estado == objetivo:
        return nodo
    if limite <= 0:
        return None

    for vecino in grafo.get(nodo.estado, []):
        hijo = Nodo(vecino, nodo)
        resultado = busqueda_profundidad_limitada(hijo, objetivo, grafo, limite - 1)
        if resultado is not None:
            return resultado
    return None

# Búsqueda en profundidad iterativa
def busqueda_profundidad_iterativa(inicio, objetivo, grafo, limite_maximo):
    for limite in range(limite_maximo + 1):  # Se va aumentando el límite de forma iterativa
        print(f"\nIntentando con límite: {limite}")
        nodo_inicio = Nodo(inicio)
        resultado = busqueda_profundidad_limitada(nodo_inicio, objetivo, grafo, limite)
        if resultado:
            return reconstruir_camino(resultado)
    return None  # Si no se encuentra el objetivo con ningún límite

# Ejemplo de uso
if __name__ == "__main__":
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
    limite_maximo = 5

    resultado = busqueda_profundidad_iterativa(inicio, objetivo, grafo, limite_maximo)

    if resultado:
        print("\nCamino encontrado:", resultado)
    else:
        print("\nNo se encontró un camino dentro del límite máximo.")
