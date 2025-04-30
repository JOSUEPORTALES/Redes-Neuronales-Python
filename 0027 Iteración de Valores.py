# Importamos librerías necesarias
import numpy as np

# Definimos el entorno como una cuadrícula de 3x3 (grafo)
# Cada celda representa un estado. Usamos una matriz para representar los valores.
valores = np.zeros((3, 3))  # Todos los valores iniciales son 0

# Definimos las recompensas del entorno (solo el destino tiene recompensa positiva)
recompensas = np.array([
    [0, 0, 0],
    [0, -1, 0],
    [0, 0, 10]  # La recompensa de llegar al estado (2,2)
])

# Definimos los posibles movimientos: arriba, abajo, izquierda, derecha
movimientos = {
    'arriba': (-1, 0),
    'abajo': (1, 0),
    'izquierda': (0, -1),
    'derecha': (0, 1)
}

# Configuramos parametros
descuento = 0.9  # Factor de descuento (gamma), cuanto valen las recompensas futuras
epsilon = 0.01   # Umbral para detener la iteracion cuando los valores convergen

# Iteracion de valores
def iterar_valores(valores, recompensas, descuento, epsilon):
    # Copiamos la matriz para no modificarla mientras actualizamos
    nuevo_valores = valores.copy()

    # Bucle hasta que la diferencia entre iteraciones sea pequeña
    while True:
        delta = 0  # Almacena el mayor cambio en esta iteración
        for fila in range(3):
            for columna in range(3):
                # Saltamos si es un estado terminal (donde hay recompensa final)
                if (fila, columna) == (2, 2):
                    continue

                mejores_valores = []

                # Probamos todos los movimientos posibles
                for movimiento in movimientos.values():
                    nueva_fila = fila + movimiento[0]
                    nueva_columna = columna + movimiento[1]

                    # Verificamos que el movimiento no salga del mapa
                    if 0 <= nueva_fila < 3 and 0 <= nueva_columna < 3:
                        # Obtenemos el valor del nuevo estado
                        valor_nuevo_estado = valores[nueva_fila][nueva_columna]
                        # Calculamos el valor estimado usando la recompensa y el valor futuro
                        valor_total = recompensas[fila][columna] + descuento * valor_nuevo_estado
                        mejores_valores.append(valor_total)

                # Actualizamos el valor del estado con el mejor de los posibles movimientos
                mejor_valor = max(mejores_valores)
                delta = max(delta, abs(mejor_valor - nuevo_valores[fila][columna]))
                nuevo_valores[fila][columna] = mejor_valor

        # Si el cambio entre valores es pequeño, salimos del bucle
        if delta < epsilon:
            break

    return nuevo_valores

# Ejecutamos la iteracion de valores
valores_finales = iterar_valores(valores, recompensas, descuento, epsilon)

# Imprimimos los resultados
print("VALORES FINALES POR ESTADO (tras iteracion de valores):")
for fila in valores_finales:
    print(["{0:>6.2f}".format(v) for v in fila])
