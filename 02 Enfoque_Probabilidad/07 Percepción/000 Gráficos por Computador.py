import matplotlib.pyplot as plt
import numpy as np
import random

# Funcion para dibujar una figura dependiendo del nombre
def dibujar_figura(nombre_figura):
    if nombre_figura == 'circulo':
        circulo = plt.Circle((0.5, 0.5), 0.3, fill=True, color='skyblue')
        plt.gca().add_patch(circulo)
    elif nombre_figura == 'cuadrado':
        cuadrado = plt.Rectangle((0.2, 0.2), 0.6, 0.6, fill=True, color='lightgreen')
        plt.gca().add_patch(cuadrado)
    elif nombre_figura == 'triangulo':
        triangulo = plt.Polygon([[0.5, 0.8], [0.2, 0.2], [0.8, 0.2]], fill=True, color='salmon')
        plt.gca().add_patch(triangulo)
    
    # Ajustes visuales
    plt.gca().set_aspect('equal')
    plt.axis('off')
    plt.title(f"Figura: {nombre_figura}")
    plt.show()

# Supongamos que nuestro "modelo IA" tiene ciertas probabilidades de ver cada figura
# Por ejemplo, basado en contexto o entrenamiento previo
modelo_probabilidades = {
    'circulo': 0.5,
    'cuadrado': 0.6,
    'triangulo': 0.2
}

# Elegimos una figura segun las probabilidades (simulando percepcion probabilistica)
def elegir_figura(probabilidades):
    figuras = list(probabilidades.keys())
    valores = list(probabilidades.values())
    figura_elegida = random.choices(figuras, valores)[0]
    return figura_elegida

# Simulacion: la IA percibe una figura
print("Simulacion de percepcion: la IA 've' una figura segun probabilidades...")

figura = elegir_figura(modelo_probabilidades)
print(f"La figura percibida es: {figura}")

# Dibujamos la figura que la IA 'percibio'
dibujar_figura(figura)
