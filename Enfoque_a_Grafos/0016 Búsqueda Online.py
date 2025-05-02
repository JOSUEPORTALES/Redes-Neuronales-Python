import random

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
