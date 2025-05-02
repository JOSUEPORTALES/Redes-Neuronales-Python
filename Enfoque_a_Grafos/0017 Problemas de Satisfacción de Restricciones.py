import networkx as nx

# Importamos la biblioteca necesaria para trabajar con grafos y dibujarlos
import matplotlib.pyplot as plt

# Definimos el problema de satisfacción de restricciones (CSP)
# En este caso, el problema es colorear un mapa
def resolver_coloreo_mapa():
    # Definimos las regiones del mapa como nodos de un grafo
    regiones = ['A', 'B', 'C', 'D', 'E']

    # Definimos las conexiones entre regiones (aristas del grafo)
    conexiones = [
        ('A', 'B'),
        ('A', 'C'),
        ('B', 'C'),
        ('B', 'D'),
        ('C', 'D'),
        ('C', 'E'),
        ('D', 'E')
    ]

    # Creamos un grafo utilizando NetworkX
    grafo = nx.Graph()
    grafo.add_nodes_from(regiones)
    grafo.add_edges_from(conexiones)

    # Definimos los colores disponibles
    colores_disponibles = ['red', 'green', 'blue']

    # Creamos un diccionario para almacenar el color asignado a cada región
    asignacion_colores = {}

    # Función para verificar si un color es válido para una región
    def es_color_valido(region, color):
        for vecino in grafo.neighbors(region):
            if vecino in asignacion_colores and asignacion_colores[vecino] == color:
                return False
        return True

    # Algoritmo de búsqueda para asignar colores a las regiones
    def asignar_colores(region_actual):
        # Si hemos asignado colores a todas las regiones, terminamos
        if region_actual == len(regiones):
            return True

        # Obtenemos la región actual
        region = regiones[region_actual]

        # Probamos cada color disponible
        for color in colores_disponibles:
            if es_color_valido(region, color):
                # Asignamos el color a la región
                asignacion_colores[region] = color

                # Llamamos recursivamente para asignar colores a las siguientes regiones
                if asignar_colores(region_actual + 1):
                    return True

                # Si no se puede continuar, deshacemos la asignación
                del asignacion_colores[region]

        # Si no se puede asignar ningún color válido, devolvemos False
        return False

    # Iniciamos el proceso de asignación de colores
    if asignar_colores(0):
        print("Solución encontrada:")
        for region, color in asignacion_colores.items():
            print(f"Region {region}: {color}")
    else:
        print("No se encontró solución.")

    # Dibujamos el grafo con los colores asignados
    colores_nodos = [asignacion_colores[region] for region in regiones]
    nx.draw(grafo, with_labels=True, node_color=colores_nodos, node_size=500, font_color='white')
    plt.show()

# Llamamos a la función para resolver el problema
resolver_coloreo_mapa()



