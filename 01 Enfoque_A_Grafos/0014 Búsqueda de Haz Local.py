import heapq
"""
Este programa implementa la búsqueda de haz local (Local Beam Search) en un grafo no dirigido. 
El objetivo es encontrar el camino de menor costo entre un nodo inicial y un nodo objetivo, 
explorando múltiples caminos simultáneamente y manteniendo solo los mejores k caminos en cada iteración.
Clases:
- Grafo: Representa un grafo no dirigido con métodos para agregar aristas y obtener vecinos de un nodo.
Funciones:
- calcular_costo(camino, grafo): Calcula el costo total de un camino en el grafo.
- busqueda_haz_local(grafo, inicio, objetivo, k=2, max_iteraciones=50): Implementa el algoritmo de búsqueda de haz local.
Parámetros de `busqueda_haz_local`:
- grafo: Instancia de la clase Grafo que representa el grafo a explorar.
- inicio: Nodo inicial desde donde comienza la búsqueda.
- objetivo: Nodo objetivo al que se desea llegar.
- k: Número de caminos que se mantienen en cada iteración (tamaño del haz).
- max_iteraciones: Número máximo de iteraciones permitidas.
El programa incluye un ejemplo de uso donde se crea un grafo, se definen las aristas con sus pesos, 
y se ejecuta la búsqueda de haz local desde un nodo inicial hasta un nodo objetivo. 
Al final, se imprime el mejor camino encontrado junto con su costo, o un mensaje indicando que no se encontró un camino.
"""



class Grafo:
    def __init__(self):
        self.grafo = {}

    def agregar_arista(self, nodo1, nodo2, peso):
        if nodo1 not in self.grafo:
            self.grafo[nodo1] = []
        if nodo2 not in self.grafo:
            self.grafo[nodo2] = []
        self.grafo[nodo1].append((nodo2, peso))
        self.grafo[nodo2].append((nodo1, peso))  # Grafo no dirigido

    def obtener_vecinos(self, nodo):
        return self.grafo.get(nodo, [])

def calcular_costo(camino, grafo):
    costo = 0
    for i in range(len(camino) - 1):
        for vecino, peso in grafo.obtener_vecinos(camino[i]):
            if vecino == camino[i + 1]:
                costo += peso
                break
    return costo

def busqueda_haz_local(grafo, inicio, objetivo, k=2, max_iteraciones=50):
    # Inicializar el haz con un solo camino: el nodo inicial
    haz = [[inicio]]
    historial = []

    for iteracion in range(max_iteraciones):
        nuevos_caminos = []

        # Expandir cada camino del haz actual
        for camino in haz:
            ultimo_nodo = camino[-1]
            vecinos = grafo.obtener_vecinos(ultimo_nodo)

            for vecino, peso in vecinos:
                if vecino not in camino:  # Evita ciclos
                    nuevo_camino = camino + [vecino]
                    nuevos_caminos.append(nuevo_camino)

        if not nuevos_caminos:
            break

        # Calcular costos de todos los caminos nuevos
        caminos_con_costos = [(calcular_costo(cam, grafo), cam) for cam in nuevos_caminos]

        # Seleccionar los k mejores caminos (con menor costo)
        caminos_con_costos.sort(key=lambda x: x[0])
        haz = [cam for _, cam in caminos_con_costos[:k]]

        # Agregar al historial
        for costo, camino in caminos_con_costos[:k]:
            historial.append((camino, costo))

        # Verificar si se alcanzó el objetivo en algún camino
        for camino in haz:
            if camino[-1] == objetivo:
                print("\nHistorial de soluciones:")
                for i, (cam, cost) in enumerate(historial):
                    print(f"Iteración {i+1}: Camino: {cam} - Costo: {cost}")
                return camino, calcular_costo(camino, grafo)

    print("\nHistorial de soluciones:")
    for i, (cam, cost) in enumerate(historial):
        print(f"Iteración {i+1}: Camino: {cam} - Costo: {cost}")
    return None, None


# Crear un grafo de ejemplo
grafo = Grafo()
grafo.agregar_arista("A", "B", 1)
grafo.agregar_arista("B", "C", 2)
grafo.agregar_arista("A", "C", 3)
grafo.agregar_arista("C", "D", 1)
grafo.agregar_arista("B", "D", 4)

# Ejecutar Búsqueda de Haz Local desde A hasta D
mejor_camino, mejor_costo = busqueda_haz_local(grafo, "A", "D", k=2)

if mejor_camino:
    print(f"\nMejor camino encontrado: {mejor_camino} con costo: {mejor_costo}")
else:
    print("\nNo se encontró un camino al objetivo.")

