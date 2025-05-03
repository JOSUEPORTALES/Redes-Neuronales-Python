# Definimos el tamaño del mundo: una cuadricula de 3x3
tamaño_mapa = 3

# Representamos los movimientos posibles como desplazamientos en X y Y
movimientos = {
    "arriba": (-1, 0),
    "abajo": (1, 0),
    "izquierda": (0, -1),
    "derecha": (0, 1)
}

# Funcion para verificar si una posicion es valida dentro del mapa
def es_posicion_valida(posicion):
    x, y = posicion
    return 0 <= x < tamaño_mapa and 0 <= y < tamaño_mapa

# Funcion para obtener todos los posibles estados desde una posicion dada
def obtener_sucesores(posicion_actual):
    sucesores = []
    for accion, (dx, dy) in movimientos.items():
        nueva_posicion = (posicion_actual[0] + dx, posicion_actual[1] + dy)
        if es_posicion_valida(nueva_posicion):
            sucesores.append((accion, nueva_posicion))
    return sucesores

# Funcion para explorar el espacio de estados usando busqueda en anchura
def buscar_camino(estado_inicial, estado_objetivo):
    from collections import deque

    cola = deque()
    cola.append((estado_inicial, []))  # Cada elemento tiene (estado, camino)
    visitados = set()

    while cola:
        estado_actual, camino = cola.popleft()

        if estado_actual == estado_objetivo:
            return camino

        if estado_actual in visitados:
            continue
        visitados.add(estado_actual)

        for accion, nuevo_estado in obtener_sucesores(estado_actual):
            if nuevo_estado not in visitados:
                nueva_ruta = camino + [(accion, nuevo_estado)]
                cola.append((nuevo_estado, nueva_ruta))
    
    return None  # Si no se encuentra camino

# Definimos el estado inicial y el objetivo
estado_inicial = (0, 0)
estado_objetivo = (2, 2)

# Ejecutamos la busqueda
camino_encontrado = buscar_camino(estado_inicial, estado_objetivo)

# Mostramos el resultado paso a paso
print("Camino encontrado del estado inicial al objetivo:")
for paso in camino_encontrado:
    accion, posicion = paso
    print(f"Accion: {accion}, Nueva posicion: {posicion}")
