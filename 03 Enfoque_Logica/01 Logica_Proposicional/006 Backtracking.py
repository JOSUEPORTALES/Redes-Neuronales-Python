# Funcion que verifica si una reina puede colocarse en la posicion actual
def es_valido(tablero, fila, columna):
    for i in range(fila):
        # Verifica misma columna
        if tablero[i] == columna:
            return False
        # Verifica diagonales
        if abs(tablero[i] - columna) == abs(i - fila):
            return False
    return True

# Funcion principal que utiliza backtracking para resolver el problema
def resolver_reinas(fila, tablero, soluciones):
    if fila == len(tablero):
        soluciones.append(tablero[:])  # Se guarda una copia de la solucion encontrada
        return
    
    for columna in range(len(tablero)):
        if es_valido(tablero, fila, columna):
            tablero[fila] = columna  # Coloca la reina
            resolver_reinas(fila + 1, tablero, soluciones)  # Intenta en la siguiente fila
            # No se necesita "quitar" explícitamente la reina porque se sobreescribirá

# Funcion que imprime el tablero de forma visual
def imprimir_tablero(tablero):
    for fila in tablero:
        linea = ""
        for i in range(len(tablero)):
            if i == fila:
                linea += "👑 "
            else:
                linea += ". "
        print(linea)
    print("\n")

# ----------------------------
# Tamaño del tablero (4x4)
n = 4

# Representacion del tablero: lista donde el indice representa la fila
# y el valor en esa posicion representa la columna de la reina
tablero = [-1] * n

# Lista para guardar todas las soluciones encontradas
soluciones = []

# Ejecutamos el algoritmo
resolver_reinas(0, tablero, soluciones)

# Mostramos los resultados
print(f"Se encontraron {len(soluciones)} soluciones posibles para {n} reinas.\n")
for solucion in soluciones:
    imprimir_tablero(solucion)
