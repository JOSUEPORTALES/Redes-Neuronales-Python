# Importamos las librerias necesarias
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import numpy as np

# Cargamos un conjunto de datos muy conocido llamado "iris"
# Contiene datos de flores con diferentes medidas y sus tipos
datos = load_iris()
caracteristicas = datos.data  # Esto contiene medidas como el largo del pétalo, ancho del sépalo, etc.
etiquetas = datos.target      # Esto indica a qué tipo de flor pertenece (0, 1 o 2)

# Dividimos los datos en entrenamiento y prueba
# Entrenamiento: para aprender
# Prueba: para verificar si lo aprendido fue correcto
carac_entrenamiento, carac_prueba, etiquetas_entrenamiento, etiquetas_prueba = train_test_split(
    caracteristicas, etiquetas, test_size=0.3, random_state=42)

# ----------------------------------
# PARTE 1: Clasificación usando k-NN
# ----------------------------------

# Creamos un clasificador k-NN con k=3 (toma los 3 vecinos más cercanos)
clasificador_knn = KNeighborsClassifier(n_neighbors=3)

# Entrenamos el modelo con los datos de entrenamiento
clasificador_knn.fit(carac_entrenamiento, etiquetas_entrenamiento)

# Probamos con los datos de prueba
predicciones = clasificador_knn.predict(carac_prueba)

# Mostramos algunas predicciones y sus etiquetas reales
print("Ejemplo de clasificación con k-NN:")
for i in range(5):
    print(f"Flor real: {etiquetas_prueba[i]}, Flor predicha: {predicciones[i]}")

# ----------------------------------
# PARTE 2: Agrupamiento con k-Medias
# ----------------------------------

# Creamos un modelo de k-Medias para hacer clustering (agrupamiento)
# En este caso, queremos dividir los datos en 3 grupos (porque hay 3 tipos de flores)
modelo_kmedias = KMeans(n_clusters=3, random_state=42)

# Aplicamos el modelo a los datos
modelo_kmedias.fit(caracteristicas)

# Obtenemos a qué grupo fue asignada cada flor
grupos = modelo_kmedias.labels_

# Mostramos los primeros resultados
print("\nEjemplo de agrupamiento con k-Medias:")
for i in range(5):
    print(f"Flor {i} asignada al grupo: {grupos[i]}")

# ----------------------------------
# PARTE 3: Visualización del resultado del clustering
# ----------------------------------

# Convertimos las primeras dos características en coordenadas (x, y) para graficar
x = caracteristicas[:, 0]  # largo del sepalo
y = caracteristicas[:, 1]  # ancho del sepalo

# Creamos un gráfico donde el color indica el grupo asignado por k-Medias
plt.scatter(x, y, c=grupos, cmap='viridis')
plt.xlabel("Largo del sepalo")
plt.ylabel("Ancho del sepalo")
plt.title("Agrupamiento de flores con k-Medias")
plt.show()
