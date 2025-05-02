import networkx as nx
import matplotlib.pyplot as plt
import random

# Definimos los eventos posibles y sus probabilidades a priori
# Estos valores deben sumar 1.0
eventos_probabilidades = {
    'Lluvia': 0.3,
    'Soleado': 0.5,
    'Nublado': 0.2
}

# Esta funcion elige un evento aleatoriamente segun su probabilidad a priori
def elegir_evento_apriori(eventos):
    nombres_eventos = list(eventos.keys())  # Nombres como 'Lluvia', 'Soleado', etc.
    probabilidades = list(eventos.values())  # Valores como 0.3, 0.5, 0.2

    # Seleccionamos un evento segun su probabilidad
    evento_elegido = random.choices(nombres_eventos, weights=probabilidades, k=1)[0]
    return evento_elegido

# Esta funcion crea y muestra un grafo simple con los eventos y sus probabilidades
def dibujar_eventos_probabilidad(eventos, evento_seleccionado=None):
    G = nx.DiGraph()

    for evento, probabilidad in eventos.items():
        G.add_node(evento, prob=probabilidad)

    # Conectamos todos con un nodo central "Clima"
    G.add_node("Clima")
    for evento in eventos:
        G.add_edge("Clima", evento)

    # Posiciones fijas para el grafo
    pos = nx.spring_layout(G, seed=42)

    # Dibujamos los nodos y las aristas
    colores = ['lightblue' if evento != evento_seleccionado else 'orange' for evento in G.nodes()]
    nx.draw(G, pos, with_labels=True, node_size=1500, node_color=colores, font_weight='bold')

    # Etiquetas con probabilidades
    etiquetas_nodos = {nodo: f"{nodo}\nP={eventos[nodo]:.1f}" if nodo in eventos else nodo for nodo in G.nodes()}
    nx.draw_networkx_labels(G, pos, labels=etiquetas_nodos)

    plt.title("Probabilidades a Priori de Eventos")
    plt.show()


# Elegimos un evento basado en las probabilidades a priori
evento_elegido = elegir_evento_apriori(eventos_probabilidades)

# Mostramos el evento seleccionado
print(f"Evento elegido segun probabilidad a priori: {evento_elegido}")

# Dibujamos el grafo resaltando el evento elegido
dibujar_eventos_probabilidad(eventos_probabilidades, evento_elegido)
