# Importamos la biblioteca OpenCV para trabajar con imágenes
import cv2

# Importamos la biblioteca numpy para manejar arreglos de números (matrices)
import numpy as np

# Creamos una imagen en negro de 400x400 píxeles, con 3 canales de color (RGB)
imagen = np.zeros((400, 400, 3), dtype=np.uint8)

# Dibujamos un círculo blanco en la imagen
cv2.circle(imagen, (100, 100), 40, (255, 255, 255), -1)

# Dibujamos un rectángulo blanco en la imagen
cv2.rectangle(imagen, (200, 50), (300, 150), (255, 255, 255), -1)

# Dibujamos un triángulo blanco (polígono con 3 puntos)
puntos_triangulo = np.array([[150, 300], [100, 200], [200, 200]], np.int32)
cv2.fillPoly(imagen, [puntos_triangulo], (255, 255, 255))

# Convertimos la imagen a escala de grises
imagen_grises = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)

# Aplicamos detección de bordes (Canny)
bordes = cv2.Canny(imagen_grises, 50, 150)

# Encontramos los contornos (bordes cerrados) en la imagen
contornos, _ = cv2.findContours(bordes, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Recorremos cada contorno detectado
for contorno in contornos:
    # Aproximamos el contorno a una forma más simple (menos puntos)
    aproximacion = cv2.approxPolyDP(contorno, 0.04 * cv2.arcLength(contorno, True), True)

    # Obtenemos el centro del contorno para escribir el nombre de la figura
    momento = cv2.moments(contorno)
    if momento["m00"] != 0:
        cx = int(momento["m10"] / momento["m00"])
        cy = int(momento["m01"] / momento["m00"])
    else:
        cx, cy = 0, 0

    # Clasificamos la forma según el número de lados
    if len(aproximacion) == 3:
        figura = "Triangulo"
    elif len(aproximacion) == 4:
        figura = "Rectangulo"
    elif len(aproximacion) > 4:
        figura = "Circulo"
    else:
        figura = "Desconocido"

    # Dibujamos el contorno y escribimos el nombre de la figura
    cv2.drawContours(imagen, [contorno], -1, (0, 255, 0), 2)
    cv2.putText(imagen, figura, (cx - 40, cy), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)

# Mostramos la imagen con las figuras detectadas
cv2.imshow("Reconocimiento de Formas", imagen)
cv2.waitKey(0)
cv2.destroyAllWindows()
