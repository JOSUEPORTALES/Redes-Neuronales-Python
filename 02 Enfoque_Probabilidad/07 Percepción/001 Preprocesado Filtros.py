import cv2
import numpy as np
import matplotlib.pyplot as plt

# 1. Cargar una imagen en escala de grises
# Usamos una imagen de muestra que se incluye con OpenCV o puedes usar cualquier imagen local
imagen = cv2.imread(cv2.samples.findFile('oct.jpg'), cv2.IMREAD_GRAYSCALE)

# Verificamos si se cargo correctamente la imagen
if imagen is None:
    print("No se pudo cargar la imagen. Asegurate de tener 'lena.jpg' o una imagen local.")
    exit()

# 2. Definir un filtro (máscara) para detección de bordes horizontales (filtro de Sobel)
filtro_bordes = np.array([[-1, -2, -1],
                          [ 0,  0,  0],
                          [ 1,  2,  1]])

# 3. Aplicar el filtro a la imagen usando convolución
# Esto nos permite ver cómo la imagen cambia al resaltar los bordes
imagen_filtrada = cv2.filter2D(imagen, -1, filtro_bordes)

# 4. Mostrar la imagen original y la imagen filtrada
# Esto nos ayudará a visualizar el efecto del filtro
plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.title("Imagen Original")
plt.imshow(imagen, cmap='gray')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.title("Imagen con Filtro de Bordes")
plt.imshow(imagen_filtrada, cmap='gray')
plt.axis('off')

plt.tight_layout()
plt.show()
