import cv2  # Libreria para procesamiento de imagenes
import numpy as np
import matplotlib.pyplot as plt

# Paso 1: crear una imagen con varias lineas
def crear_imagen_lineas(tamano=(200, 200)):
    imagen = np.zeros(tamano, dtype=np.uint8)

    # Dibujamos varias lineas con diferentes direcciones
    cv2.line(imagen, (10, 10), (190, 10), 255, 2)     # Horizontal
    cv2.line(imagen, (10, 10), (10, 190), 255, 2)     # Vertical
    cv2.line(imagen, (10, 190), (190, 10), 255, 2)    # Diagonal negativa
    cv2.line(imagen, (10, 10), (190, 190), 255, 2)    # Diagonal positiva

    return imagen

# Paso 2: detectar lineas usando el algoritmo de Canny y Hough
def detectar_lineas(imagen):
    bordes = cv2.Canny(imagen, 50, 150)  # Detecta los bordes
    lineas = cv2.HoughLinesP(bordes, 1, np.pi / 180, threshold=50, minLineLength=20, maxLineGap=5)
    return lineas

# Paso 3: etiquetar lineas segun su orientacion
def etiquetar_lineas(imagen, lineas):
    imagen_color = cv2.cvtColor(imagen, cv2.COLOR_GRAY2BGR)

    for linea in lineas:
        x1, y1, x2, y2 = linea[0]
        # Calculamos el angulo de la linea
        angulo = np.arctan2(y2 - y1, x2 - x1) * 180 / np.pi

        # Etiquetamos segun orientacion
        if -10 <= angulo <= 10:
            color = (255, 0, 0)  # Azul: horizontal
        elif 80 <= abs(angulo) <= 100:
            color = (0, 255, 0)  # Verde: vertical
        else:
            color = (0, 0, 255)  # Rojo: diagonal

        cv2.line(imagen_color, (x1, y1), (x2, y2), color, 2)

    return imagen_color

# Paso 4: mostrar la imagen
def mostrar_imagen(imagen, titulo):
    plt.imshow(cv2.cvtColor(imagen, cv2.COLOR_BGR2RGB))
    plt.title(titulo)
    plt.axis('off')
    plt.show()

# Simulacion completa
print("Creando imagen con lineas...")
imagen_base = crear_imagen_lineas()

print("Detectando lineas en la imagen...")
lineas_detectadas = detectar_lineas(imagen_base)

print("Etiquetando lineas segun orientacion...")
imagen_etiquetada = etiquetar_lineas(imagen_base, lineas_detectadas)

mostrar_imagen(imagen_etiquetada, "Lineas etiquetadas por orientacion")
