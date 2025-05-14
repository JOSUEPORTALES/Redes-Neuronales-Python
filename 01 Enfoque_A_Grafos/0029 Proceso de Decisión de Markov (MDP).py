# Importamos librerías necesarias
"""
Este programa implementa el algoritmo de Iteración de Valores para resolver un Proceso de Decisión de Markov (MDP). 
El objetivo es encontrar los valores óptimos para cada estado y la política óptima (la mejor acción a tomar en cada estado) 
dado un conjunto de estados, acciones, transiciones, y parámetros de descuento y convergencia.
Funciones:
-----------
iteracion_valores_mdp(estados, acciones, transiciones, descuento, epsilon):
    Aplica el algoritmo de Iteración de Valores para calcular los valores óptimos de los estados y la política óptima.
    - estados: Lista de estados del MDP.
    - acciones: Lista de acciones disponibles.
    - transiciones: Diccionario que define las transiciones del MDP en forma de (estado_actual, accion) -> [(probabilidad, estado_siguiente, recompensa)].
    - descuento: Factor de descuento para recompensas futuras (valor entre 0 y 1).
    - epsilon: Criterio de convergencia para detener el algoritmo.
Retorna:
    - valores: Diccionario con los valores óptimos para cada estado.
    - politica: Diccionario con la mejor acción a tomar desde cada estado.
El programa inicializa los valores de los estados en 0 y ejecuta el algoritmo hasta que los valores converjan 
(según el criterio epsilon). Finalmente, imprime los valores finales de cada estado y la política óptima.
"""
import numpy as np




# Definimos los estados de nuestro grafo
estados = ['A', 'B', 'C', 'D']

# Definimos las acciones disponibles en cada estado
acciones = ['ir_a_B', 'ir_a_C', 'ir_a_D']

# Definimos las transiciones como: (estado_actual, accion) -> [(probabilidad, estado_siguiente, recompensa)]
transiciones = {
    ('A', 'ir_a_B'): [(1.0, 'B', 5)],
    ('A', 'ir_a_C'): [(1.0, 'C', 10)],
    ('B', 'ir_a_D'): [(1.0, 'D', 2)],
    ('C', 'ir_a_D'): [(1.0, 'D', 4)],
    ('D', 'ir_a_A'): [(1.0, 'A', 0)],  # Ciclo que vuelve al inicio
}

# Creamos una tabla de valores iniciales para cada estado
valores = {estado: 0.0 for estado in estados}

# Parametros del algoritmo
descuento = 0.9   # Cuanto valen las recompensas futuras
epsilon = 0.01    # Criterio de convergencia

# Funcion para aplicar la iteracion de valores a este MDP
def iteracion_valores_mdp(estados, acciones, transiciones, descuento, epsilon):
    valores = {estado: 0.0 for estado in estados}
    politica = {estado: None for estado in estados}

    while True:
        delta = 0
        nuevos_valores = valores.copy()

        for estado in estados:
            mejores_valores = []
            mejores_acciones = []

            # Probamos cada accion posible desde este estado
            for accion in acciones:
                if (estado, accion) in transiciones:
                    valor_total = 0
                    for probabilidad, estado_siguiente, recompensa in transiciones[(estado, accion)]:
                        valor_total += probabilidad * (recompensa + descuento * valores[estado_siguiente])
                    mejores_valores.append(valor_total)
                    mejores_acciones.append(accion)

            if mejores_valores:
                mejor_valor = max(mejores_valores)
                mejor_accion = mejores_acciones[np.argmax(mejores_valores)]

                nuevos_valores[estado] = mejor_valor
                politica[estado] = mejor_accion
                delta = max(delta, abs(valores[estado] - mejor_valor))

        valores = nuevos_valores

        if delta < epsilon:
            break

    return valores, politica

# Ejecutamos el algoritmo
valores_finales, politica_optima = iteracion_valores_mdp(estados, acciones, transiciones, descuento, epsilon)

# Imprimimos los valores de cada estado
print("VALORES FINALES POR ESTADO:")
for estado, valor in valores_finales.items():
    print(f"Estado {estado}: {valor:.2f}")

# Imprimimos la mejor accion desde cada estado (la politica optima)
print("\nPOLITICA OPTIMA:")
for estado, accion in politica_optima.items():
    print(f"Desde el estado {estado}: tomar accion -> {accion}")
