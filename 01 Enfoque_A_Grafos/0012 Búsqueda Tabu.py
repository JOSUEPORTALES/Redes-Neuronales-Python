import random
"""
Este programa implementa la búsqueda tabú para encontrar el camino más corto en un grafo no dirigido.
La búsqueda tabú es una técnica de optimización que utiliza una memoria tabú para evitar ciclos y
explorar soluciones más prometedoras. El programa incluye las siguientes funcionalidades:
1. Clase `Grafo`:
    - Permite crear un grafo no dirigido.
    - Métodos para agregar aristas y obtener vecinos de un nodo.
2. Función `busqueda_tabú`:
    - Implementa el algoritmo de búsqueda tabú.
    - Encuentra el camino más corto desde un nodo inicial hasta un nodo objetivo.
    - Utiliza una memoria tabú para evitar caminos ya explorados.
    - Registra un historial de soluciones intermedias para análisis.
3. Ejemplo de uso:
    - Se crea un grafo con nodos y aristas.
    - Se ejecuta la búsqueda tabú para encontrar el camino más corto entre dos nodos.
    - Se imprime el historial de soluciones y el mejor camino encontrado.
Parámetros principales:
- `grafo`: Objeto de la clase `Grafo` que representa el grafo.
- `nodo_inicio`: Nodo desde donde comienza la búsqueda.
- `nodo_objetivo`: Nodo al que se desea llegar.
- `iteraciones`: Número máximo de iteraciones para la búsqueda.
- `tamano_memoria`: Tamaño máximo de la memoria tabú.
Salida:
- El mejor camino encontrado y su costo asociado.
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

def busqueda_tabú(grafo, nodo_inicio, nodo_objetivo, iteraciones=100, tamano_memoria=10):
    # Inicialización
    mejor_solucion = [nodo_inicio]
    mejor_costo = 0
    solucion_actual = [nodo_inicio]
    costo_actual = 0
    memoria_tabú = []  # Almacena los caminos ya explorados
    historial_soluciones = []  # Lista para almacenar el historial de soluciones

    while solucion_actual[-1] != nodo_objetivo and iteraciones > 0:
        iteraciones -= 1
        
        # Generar los vecinos del último nodo en la solución actual
        ultimo_nodo = solucion_actual[-1]
        vecinos = grafo.obtener_vecinos(ultimo_nodo)
        
        # Generar posibles caminos (vecinos)
        vecinos_posibles = []
        for vecino, peso in vecinos:
            if vecino not in solucion_actual:  # Evitar ciclos
                vecinos_posibles.append((vecino, peso))
        
        # Si no hay vecinos disponibles, terminar
        if not vecinos_posibles:
            break
        
        # Seleccionar el mejor vecino no tabú
        mejor_vecino = None
        mejor_valor = float('inf')
        for vecino, peso in vecinos_posibles:
            if (vecino not in memoria_tabú) and (costo_actual + peso < mejor_valor):
                mejor_vecino = vecino
                mejor_valor = costo_actual + peso
        
        # Actualizar la solución
        if mejor_vecino is not None:
            solucion_actual.append(mejor_vecino)
            costo_actual = mejor_valor
            if costo_actual < mejor_costo:
                mejor_costo = costo_actual
                mejor_solucion = solucion_actual[:]
        
        # Agregar la solución actual a la memoria tabú
        memoria_tabú.append(solucion_actual[:])
        
        # Limitar el tamaño de la memoria tabú
        if len(memoria_tabú) > tamano_memoria:
            memoria_tabú.pop(0)  # Eliminar el camino más antiguo
        
        # Guardar el historial de soluciones intermedias
        historial_soluciones.append((list(solucion_actual), costo_actual))

    # Mostrar el historial de soluciones
    print("\nHistorial de soluciones:")
    for i, (camino, costo) in enumerate(historial_soluciones):
        print(f"Iteración {i+1}: Camino: {camino} - Costo: {costo}")
    
    return mejor_solucion, mejor_costo

# Crear un grafo de ejemplo
grafo = Grafo()
grafo.agregar_arista("A", "B", 1)
grafo.agregar_arista("B", "C", 2)
grafo.agregar_arista("A", "C", 3)
grafo.agregar_arista("C", "D", 1)
grafo.agregar_arista("B", "D", 4)

# Ejecutar la búsqueda tabú para encontrar el camino de A a D
mejor_camino, mejor_costo = busqueda_tabú(grafo, "A", "D")
print(f"\nMejor camino encontrado: {mejor_camino} con costo: {mejor_costo}")
