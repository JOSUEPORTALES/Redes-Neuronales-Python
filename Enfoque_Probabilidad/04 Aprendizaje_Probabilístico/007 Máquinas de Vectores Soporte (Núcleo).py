# Importamos las librerias necesarias
from sklearn.datasets import make_moons
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
import matplotlib.pyplot as plt
import numpy as np

# ------------------------------------------
# GENERAMOS UN CONJUNTO DE DATOS DE EJEMPLO
# ------------------------------------------

# Creamos datos simulados en forma de "lunas"
# Esto representa un caso donde las clases no se pueden separar con una línea recta
caracteristicas, etiquetas = make_moons(n_samples=200, noise=0.2, random_state=42)

# Dividimos los datos en entrenamiento y prueba
carac_entrenamiento, carac_prueba, etiquetas_entrenamiento, etiquetas_prueba = train_test_split(
    caracteristicas, etiquetas, test_size=0.3, random_state=42)

# ------------------------------------------
# CREAMOS Y ENTRENAMOS UNA SVM CON NUCLEO
# ------------------------------------------

# Creamos el clasificador SVM usando un núcleo de tipo "rbf" (función de base radial)
# Este núcleo permite separar datos que no son separables con una línea recta
clasificador_svm = SVC(kernel='rbf', C=1.0, gamma='scale')

# Entrenamos el clasificador con los datos de entrenamiento
clasificador_svm.fit(carac_entrenamiento, etiquetas_entrenamiento)

# ------------------------------------------
# PREDICCIONES Y RESULTADOS
# ------------------------------------------

# Hacemos predicciones con los datos de prueba
predicciones = clasificador_svm.predict(carac_prueba)

# Mostramos algunas predicciones
print("Ejemplo de clasificación con SVM y núcleo:")
for i in range(5):
    print(f"Dato real: {etiquetas_prueba[i]}, Dato predicho: {predicciones[i]}")

# ------------------------------------------
# VISUALIZACION DE LA FRONTERA DE DECISION
# ------------------------------------------

# Creamos una malla de puntos para visualizar la frontera de decisión
x_min, x_max = caracteristicas[:, 0].min() - 0.5, caracteristicas[:, 0].max() + 0.5
y_min, y_max = caracteristicas[:, 1].min() - 0.5, caracteristicas[:, 1].max() + 0.5
xx, yy = np.meshgrid(np.linspace(x_min, x_max, 500),
                     np.linspace(y_min, y_max, 500))

# Usamos el modelo para predecir sobre cada punto de la malla
Z = clasificador_svm.predict(np.c_[xx.ravel(), yy.ravel()])
Z = Z.reshape(xx.shape)

# Mostramos el resultado
plt.contourf(xx, yy, Z, cmap=plt.cm.coolwarm, alpha=0.8)
plt.scatter(caracteristicas[:, 0], caracteristicas[:, 1], c=etiquetas, cmap=plt.cm.coolwarm, edgecolors='k')
plt.xlabel("Caracteristica 1")
plt.ylabel("Caracteristica 2")
plt.title("Clasificación con SVM y núcleo RBF")
plt.show()
