from collections import deque
"""
Este programa implementa un algoritmo de búsqueda en anchura (BFS) para encontrar un camino entre dos nodos en un grafo no dirigido.
El grafo representa conexiones entre ciudades, y el objetivo es determinar un camino desde una ciudad inicial hasta una ciudad objetivo.
Funciones:
- busqueda_anchura(grafo, inicio, objetivo): Realiza la búsqueda en anchura en el grafo dado, devolviendo el camino encontrado
    entre el nodo inicial y el nodo objetivo, o None si no existe un camino.
- imprimir_grafo(grafo): Imprime en consola las conexiones del grafo en un formato legible.
Variables principales:
- grafo_ciudades: Un diccionario que define las conexiones entre ciudades.
- ciudad_inicial: La ciudad desde donde comienza la búsqueda.
- ciudad_objetivo: La ciudad que se desea alcanzar.
El programa imprime el grafo, ejecuta la búsqueda en anchura y muestra el camino encontrado, si existe.
"""





# Funcion para realizar la busqueda en anchura (BFS)
def busqueda_anchura(grafo, inicio, objetivo):
    # Cola para guardar los caminos a explorar
    cola = deque()
    # Inicializamos la cola con el nodo inicial como unico camino
    cola.append([inicio])
    
    # Conjunto para llevar registro de nodos visitados
    visitados = set()

    while cola:
        # Obtenemos el primer camino en la cola
        camino = cola.popleft()
        # Obtenemos el ultimo nodo del camino actual
        nodo = camino[-1]

        # Si el nodo es el objetivo, devolvemos el camino encontrado
        if nodo == objetivo:
            return camino

        # Si el nodo no ha sido visitado, lo marcamos como visitado
        if nodo not in visitados:
            visitados.add(nodo)
            # Recorremos los vecinos del nodo actual
            for vecino in grafo.get(nodo, []):
                # Creamos un nuevo camino con el vecino agregado
                nuevo_camino = list(camino)
                nuevo_camino.append(vecino)
                # Agregamos el nuevo camino a la cola
                cola.append(nuevo_camino)
    
    # Si no se encuentra un camino, devolvemos None
    return None

# Funcion para imprimir el grafo en consola
def imprimir_grafo(grafo):
    print("GRAFO DE CONEXIONES ENTRE CIUDADES:")
    for ciudad, vecinos in grafo.items():
        print(f"{ciudad} -> {', '.join(vecinos)}")
    print("\n")

# Definimos un grafo simple como ejemplo
grafo_ciudades = {
    "Monterrey": ["Saltillo", "Reynosa"],
    "Saltillo": ["Monterrey", "Zacatecas"],
    "Reynosa": ["Monterrey", "Tampico"],
    "Zacatecas": ["Saltillo", "SanLuis"],
    "SanLuis": ["Zacatecas", "Tampico"],
    "Tampico": ["Reynosa", "SanLuis"]
}

# Imprimimos el grafo
imprimir_grafo(grafo_ciudades)

# Definimos ciudad de inicio y objetivo
ciudad_inicial = "Monterrey"
ciudad_objetivo = "Tampico"

# Ejecutamos la busqueda
camino_encontrado = busqueda_anchura(grafo_ciudades, ciudad_inicial, ciudad_objetivo)

# Mostramos el resultado
if camino_encontrado:
    print(f"Camino encontrado desde {ciudad_inicial} hasta {ciudad_objetivo}:")
    print(" -> ".join(camino_encontrado))
else:
    print("No se encontro un camino entre las ciudades.")
