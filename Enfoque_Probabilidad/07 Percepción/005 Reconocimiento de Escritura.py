# Importamos librerías necesarias
from sklearn.datasets import load_digits         # Carga de datos de dígitos escritos a mano
from sklearn.model_selection import train_test_split  # Para dividir los datos en entrenamiento y prueba
from sklearn.linear_model import LogisticRegression   # Clasificador simple pero eficaz
import matplotlib.pyplot as plt                    # Para mostrar imágenes
import numpy as np

# Cargamos el conjunto de datos de dígitos (imágenes 8x8)
datos = load_digits()

# Mostramos una de las imágenes como ejemplo
plt.gray()
plt.matshow(datos.images[0])  # Muestra la primera imagen
plt.title(f'Digito real: {datos.target[0]}')
plt.show()

# Las imágenes se representan como matrices 8x8. Necesitamos convertirlas a vectores para el modelo.
imagenes = datos.images.reshape((len(datos.images), -1))

# Dividimos los datos en entrenamiento (80%) y prueba (20%)
imagenes_entrenamiento, imagenes_prueba, etiquetas_entrenamiento, etiquetas_prueba = train_test_split(
    imagenes, datos.target, test_size=0.2, random_state=42
)

# Creamos un modelo de regresión logística (clasificador)
modelo = LogisticRegression(max_iter=10000)  # max_iter grande para asegurar convergencia

# Entrenamos el modelo con las imágenes y etiquetas
modelo.fit(imagenes_entrenamiento, etiquetas_entrenamiento)

# Probamos el modelo con una imagen de prueba
indice_prueba = 10
imagen_prueba = imagenes_prueba[indice_prueba]
etiqueta_real = etiquetas_prueba[indice_prueba]

# Mostramos la imagen que vamos a predecir
plt.matshow(imagen_prueba.reshape(8, 8))
plt.title(f'Digito real: {etiqueta_real}')
plt.show()

# El modelo predice la clase del dígito
prediccion = modelo.predict([imagen_prueba])
print(f'Prediccion del modelo: {prediccion[0]}')

# Mostramos la probabilidad asociada a cada clase
probabilidades = modelo.predict_proba([imagen_prueba])
print("Probabilidades para cada digito del 0 al 9:")
for i, prob in enumerate(probabilidades[0]):
    print(f"{i}: {prob:.3f}")
