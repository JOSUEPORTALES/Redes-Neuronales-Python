import numpy as np
import cv2
import matplotlib.pyplot as plt

# Paso 1: crear una imagen con un cuadrado en cierta posicion
def crear_imagen(tamano, posicion_cuadro):
    imagen = np.zeros(tamano, dtype=np.uint8)
    fila, columna = posicion_cuadro
    cv2.rectangle(imagen, (columna, fila), (columna + 20, fila + 20), 255, -1)
    return imagen

# Paso 2: detectar el movimiento entre dos imagenes
def detectar_movimiento(imagen_1, imagen_2, umbral=25):
    # Restamos los pixeles de ambas imagenes
    diferencia = cv2.absdiff(imagen_1, imagen_2)
    # Aplicamos un umbral para marcar solo los cambios grandes (movimiento)
    _, movimiento = cv2.threshold(diferencia, umbral, 255, cv2.THRESH_BINARY)
    return movimiento

# Paso 3: mostrar las imagenes
def mostrar_imagen(imagen, titulo):
    plt.imshow(imagen, cmap='gray')
    plt.title(titulo)
    plt.axis('off')
    plt.show()

# Simulamos dos momentos: cuadro en una posicion y luego desplazado
tamano_imagen = (100, 100)

print("Creando imagen 1 (cuadro en posicion inicial)...")
imagen_1 = crear_imagen(tamano_imagen, (40, 10))
mostrar_imagen(imagen_1, "Imagen 1: Posicion inicial")

print("Creando imagen 2 (cuadro desplazado)...")
imagen_2 = crear_imagen(tamano_imagen, (40, 30))  # Se mueve hacia la derecha
mostrar_imagen(imagen_2, "Imagen 2: Cuadro desplazado")

print("Detectando movimiento entre las dos imagenes...")
imagen_movimiento = detectar_movimiento(imagen_1, imagen_2)
mostrar_imagen(imagen_movimiento, "Movimiento detectado (zona blanca)")
