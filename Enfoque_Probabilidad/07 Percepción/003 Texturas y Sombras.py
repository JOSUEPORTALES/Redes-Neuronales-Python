import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm

# Paso 1: crear una textura tipo ladrillo usando una funcion sinusoidal
def generar_textura(tamano):
    filas, columnas = tamano
    textura = np.zeros((filas, columnas))

    for fila in range(filas):
        for columna in range(columnas):
            # Creamos un patron repetitivo simulando ladrillos
            textura[fila, columna] = (
                np.sin(fila * 0.3) + np.cos(columna * 0.3)
            )
    
    return textura

# Paso 2: aplicar una "sombra" a la textura simulando luz en diagonal
def aplicar_sombra(textura):
    # Creamos un filtro de sombra diagonal (matriz de atenuacion)
    sombra = np.linspace(1.0, 0.4, textura.shape[0]).reshape(-1, 1)
    imagen_con_sombra = textura * sombra
    return imagen_con_sombra

# Paso 3: mostrar la imagen con sombra (percepcion de profundidad)
def mostrar_imagen(imagen, titulo):
    plt.imshow(imagen, cmap=cm.viridis)  # colormap viridis para mejor contraste
    plt.title(titulo)
    plt.axis('off')
    plt.colorbar()
    plt.show()

# Simulamos el proceso completo
tamano_imagen = (100, 100)

print("Generando textura base...")
textura = generar_textura(tamano_imagen)
mostrar_imagen(textura, "Textura sin sombra")

print("Aplicando sombra para simular profundidad...")
imagen_sombreada = aplicar_sombra(textura)
mostrar_imagen(imagen_sombreada, "Textura con sombra (simulacion de volumen)")

# Paso 4: deteccion probabilistica de sombra
def detectar_sombra(imagen, umbral=0.5):
    # Esta funcion detecta las zonas oscuras (valores bajos)
    mascara_sombra = imagen < umbral
    return mascara_sombra

# Detectamos sombra
sombra_detectada = detectar_sombra(imagen_sombreada)
mostrar_imagen(sombra_detectada, "Zonas detectadas como sombra (probabilidad alta de profundidad)")
