import heapq  # Librería para implementar la cola de prioridad (mínimo costo)

# Clase para representar un Grafo
class Grafo:
    def __init__(self):
        # Diccionario para guardar nodos y sus conexiones (vecinos)
        self.grafo = {}

    # Método para agregar una arista con costo
    def agregar_arista(self, origen, destino, costo):
        if origen not in self.grafo:
            self.grafo[origen] = []
        self.grafo[origen].append((destino, costo))

    # Búsqueda de Costo Uniforme
    def ucs(self, inicio, objetivo):
        # Cola de prioridad: (costo acumulado, nodo actual, camino recorrido)
        frontera = []
        heapq.heappush(frontera, (0, inicio, [inicio]))

        # Conjunto de nodos visitados
        visitados = set()

        while frontera:
            costo_actual, nodo_actual, camino = heapq.heappop(frontera)

            # Si llegamos al objetivo, devolvemos el camino y el costo
            if nodo_actual == objetivo:
                print(f"Camino encontrado: {camino} con costo total: {costo_actual}")
                return camino, costo_actual

            # Si ya visitamos este nodo, lo ignoramos
            if nodo_actual in visitados:
                continue

            visitados.add(nodo_actual)

            # Exploramos los vecinos
            for vecino, costo in self.grafo.get(nodo_actual, []):
                if vecino not in visitados:
                    costo_total = costo_actual + costo
                    heapq.heappush(frontera, (costo_total, vecino, camino + [vecino]))

        print("No se encontró un camino.")
        return None, float('inf')


# Ejemplo de uso
grafo = Grafo()
grafo.agregar_arista('A', 'B', 2)
grafo.agregar_arista('A', 'C', 5)
grafo.agregar_arista('B', 'D', 4)
grafo.agregar_arista('C', 'D', 1)
grafo.agregar_arista('D', 'E', 3)

print("Búsqueda de Costo Uniforme de A hasta E:\n")
camino, costo = grafo.ucs('A', 'E')
