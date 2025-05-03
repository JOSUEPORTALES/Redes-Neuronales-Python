import cv2
import matplotlib.pyplot as plt

# 1. Cargar una imagen en escala de grises
imagen = cv2.imread(cv2.samples.findFile('oct.jpg'), cv2.IMREAD_GRAYSCALE)

# Verificamos si se cargo correctamente la imagen
if imagen is None:
    print("No se pudo cargar la imagen. Usa una imagen local.")
    exit()

# 2. Deteccion de aristas usando el algoritmo de Canny
# Este metodo detecta bordes importantes en la imagen
imagen_aristas = cv2.Canny(imagen, 100, 200)

# 3. Segmentacion simple usando umbral (thresholding)
# Separamos los pixeles en dos grupos: los claros y los oscuros
valor_umbral = 127
valor_maximo = 255
_, imagen_segmentada = cv2.threshold(imagen, valor_umbral, valor_maximo, cv2.THRESH_BINARY)

# 4. Mostrar la imagen original, con bordes y segmentada
plt.figure(figsize=(12, 4))

plt.subplot(1, 3, 1)
plt.title("Imagen Original")
plt.imshow(imagen, cmap='gray')
plt.axis('off')

plt.subplot(1, 3, 2)
plt.title("Aristas (Canny)")
plt.imshow(imagen_aristas, cmap='gray')
plt.axis('off')

plt.subplot(1, 3, 3)
plt.title("Segmentacion (Umbral)")
plt.imshow(imagen_segmentada, cmap='gray')
plt.axis('off')

plt.tight_layout()
plt.show()
