# Búsqueda en Profundidad (DFS) en un Grafo no dirigido

# Creamos una clase para representar el Grafo
class Grafo:
    def __init__(self):
        # Diccionario para almacenar los nodos y sus conexiones (vecinos)
        self.grafo = {}

    # Método para agregar una conexión (arista) entre dos nodos
    def agregar_arista(self, origen, destino):
        if origen not in self.grafo:
            self.grafo[origen] = []
        if destino not in self.grafo:
            self.grafo[destino] = []
        self.grafo[origen].append(destino)
        self.grafo[destino].append(origen)  # Porque es un grafo no dirigido

    # Búsqueda en Profundidad (DFS) recursiva
    def dfs(self, inicio, objetivo, visitados=None, camino=None):
        if visitados is None:
            visitados = set()  # Para evitar ciclos y no visitar un nodo dos veces

        if camino is None:
            camino = []  # Para almacenar el camino recorrido

        visitados.add(inicio)  # Marcamos el nodo actual como visitado
        camino.append(inicio)  # Agregamos el nodo actual al camino

        # Si llegamos al objetivo, mostramos el camino encontrado
        if inicio == objetivo:
            print(f"Camino encontrado: {camino}")
            return camino

        # Exploramos todos los vecinos (nodos conectados)
        for vecino in self.grafo.get(inicio, []):
            if vecino not in visitados:
                resultado = self.dfs(vecino, objetivo, visitados, camino)
                if resultado:  # Si encontramos el objetivo
                    return resultado

        # Si no encontramos el objetivo desde este nodo, hacemos backtracking
        camino.pop()
        return None


# Ejemplo de uso del código

# Creamos el grafo
grafo = Grafo()
grafo.agregar_arista('A', 'B')
grafo.agregar_arista('A', 'C')
grafo.agregar_arista('B', 'D')
grafo.agregar_arista('C', 'E')
grafo.agregar_arista('D', 'F')
grafo.agregar_arista('E', 'F')

# Mostramos el recorrido desde A hasta F usando DFS
print("Búsqueda en Profundidad (DFS) desde A hasta F:\n")
grafo.dfs('A', 'F')
