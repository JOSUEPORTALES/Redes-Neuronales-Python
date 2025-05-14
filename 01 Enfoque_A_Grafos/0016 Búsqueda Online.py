import random
"""
Este programa implementa un algoritmo de búsqueda online en un grafo parcialmente desconocido.
El grafo se construye dinámicamente y los nodos vecinos se descubren a medida que se exploran.
Se utiliza una estrategia de búsqueda "greedy" o aleatoria para encontrar un camino desde un nodo inicial hasta un nodo objetivo.
Clases:
--------
- GrafoDesconocido:
    Representa un grafo parcialmente desconocido. Permite agregar aristas y descubrir vecinos de un nodo.
Funciones:
----------
- busqueda_online(grafo, inicio, objetivo, estrategia="greedy"):
    Realiza una búsqueda online en el grafo desde un nodo inicial hasta un nodo objetivo.
    Parámetros:
        - grafo (GrafoDesconocido): El grafo sobre el cual se realiza la búsqueda.
        - inicio (str): Nodo inicial.
        - objetivo (str): Nodo objetivo.
        - estrategia (str): Estrategia de búsqueda ("greedy" o aleatoria).
    Retorna:
        - camino (list): Lista de nodos que forman el camino encontrado.
        - costo_total (int): Costo total del camino encontrado.
Ejemplo de uso:
---------------
1. Crear un grafo y agregar aristas.
2. Ejecutar la función `busqueda_online` para encontrar un camino entre dos nodos.
3. Imprimir el historial de exploración y el camino encontrado.
"""



# -------------------------------
# Clase del grafo parcialmente desconocido
# -------------------------------
class GrafoDesconocido:
    def __init__(self):
        self.grafo_completo = {}
        self.grafo_descubierto = {}

    def agregar_arista(self, nodo1, nodo2, peso):
        if nodo1 not in self.grafo_completo:
            self.grafo_completo[nodo1] = []
        if nodo2 not in self.grafo_completo:
            self.grafo_completo[nodo2] = []
        self.grafo_completo[nodo1].append((nodo2, peso))
        self.grafo_completo[nodo2].append((nodo1, peso))  # Grafo no dirigido

    def descubrir_vecinos(self, nodo):
        if nodo not in self.grafo_descubierto:
            self.grafo_descubierto[nodo] = self.grafo_completo.get(nodo, [])
        return self.grafo_descubierto[nodo]

# -------------------------------
# Función de búsqueda online
# -------------------------------
def busqueda_online(grafo, inicio, objetivo, estrategia="greedy"):
    actual = inicio
    camino = [actual]
    costo_total = 0
    historial = []

    while actual != objetivo:
        vecinos = grafo.descubrir_vecinos(actual)

        # Solo vecinos que aún no están en el camino
        opciones = [(vec, peso) for vec, peso in vecinos if vec not in camino]

        if not opciones:
            print(f"\n❌ No hay más nodos por explorar desde {actual}")
            return None, None

        if estrategia == "greedy":
            siguiente, costo = min(opciones, key=lambda x: x[1])
        else:
            siguiente, costo = random.choice(opciones)

        camino.append(siguiente)
        costo_total += costo
        historial.append((list(camino), costo_total))
        actual = siguiente

    # Mostrar historial
    print("\n🧭 Historial de exploración:")
    for i, (cam, cost) in enumerate(historial):
        print(f"Paso {i+1}: Camino: {cam} - Costo acumulado: {cost}")

    return camino, costo_total

# -------------------------------
# Ejemplo de uso
# -------------------------------
if __name__ == "__main__":
    grafo = GrafoDesconocido()

    # Aristas del grafo
    grafo.agregar_arista("A", "B", 2)
    grafo.agregar_arista("A", "C", 1)
    grafo.agregar_arista("B", "D", 3)
    grafo.agregar_arista("C", "D", 1)
    grafo.agregar_arista("D", "E", 4)

    print("🔗 Grafo completo:")
    for nodo in grafo.grafo_completo:
        print(f"{nodo} -> {grafo.grafo_completo[nodo]}")

    # Ejecutar búsqueda
    camino, costo = busqueda_online(grafo, "A", "E", estrategia="greedy")

    if camino:
        print(f"\n Camino encontrado: {camino} con costo total: {costo}")
    else:
        print("\n No se encontró un camino.")
