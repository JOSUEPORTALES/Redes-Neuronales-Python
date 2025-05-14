

import heapq  # Librería para implementar la cola de prioridad (mínimo costo)
"""
Este programa implementa la Búsqueda de Costo Uniforme (UCS) en un grafo dirigido ponderado.
La UCS es un algoritmo de búsqueda que expande siempre el nodo con el menor costo acumulado,
asegurando encontrar el camino más corto en términos de costo desde un nodo inicial hasta un nodo objetivo.
Clases y Métodos:
- Clase `Grafo`: Representa un grafo dirigido ponderado.
    - `__init__`: Inicializa el grafo como un diccionario vacío.
    - `agregar_arista(origen, destino, costo)`: Agrega una arista dirigida con un costo asociado entre dos nodos.
    - `ucs(inicio, objetivo)`: Implementa la Búsqueda de Costo Uniforme para encontrar el camino de menor costo
        desde el nodo `inicio` hasta el nodo `objetivo`.
Funcionamiento del Método `ucs`:
1. Utiliza una cola de prioridad (heap) para almacenar los nodos a explorar, ordenados por costo acumulado.
2. Mantiene un conjunto de nodos visitados para evitar ciclos y redundancias.
3. En cada iteración, extrae el nodo con el menor costo acumulado de la cola de prioridad.
4. Si el nodo actual es el objetivo, devuelve el camino y el costo total.
5. Si no, explora los vecinos del nodo actual, actualizando el costo acumulado y el camino recorrido.
6. Si no se encuentra un camino al objetivo, devuelve `None` y un costo infinito.
Ejemplo de Uso:
El programa incluye un ejemplo donde se define un grafo con nodos y aristas ponderadas.
Se realiza una búsqueda UCS desde el nodo 'A' hasta el nodo 'E', mostrando el camino encontrado y su costo total.
"""

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
