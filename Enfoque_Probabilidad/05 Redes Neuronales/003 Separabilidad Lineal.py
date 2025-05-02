# Importamos librerias necesarias
import matplotlib.pyplot as plt
import numpy as np
from sklearn.datasets import make_classification

# ------------------------------------------
# CASO 1: DATOS SEPARABLES LINEALMENTE
# ------------------------------------------

# Creamos un conjunto de datos con dos clases claramente separadas
# n_features=2 -> dos variables (x, y)
# n_redundant=0 -> sin variables repetidas
# n_clusters_per_class=1 -> cada clase en un solo grupo
datos_lineales, etiquetas_lineales = make_classification(n_samples=100, n_features=2,
                                                          n_redundant=0, n_clusters_per_class=1,
                                                          class_sep=2.0, random_state=1)

# ------------------------------------------
# CASO 2: DATOS NO SEPARABLES LINEALMENTE
# ------------------------------------------

# Creamos otro conjunto de datos donde las clases están mezcladas
datos_no_lineales, etiquetas_no_lineales = make_classification(n_samples=100, n_features=2,
                                                                n_redundant=0, n_clusters_per_class=1,
                                                                class_sep=0.5, random_state=1)

# ------------------------------------------
# GRAFICAMOS LOS DOS CASOS
# ------------------------------------------

plt.figure(figsize=(12, 5))

# Caso 1: Separable linealmente
plt.subplot(1, 2, 1)
plt.scatter(datos_lineales[:, 0], datos_lineales[:, 1], c=etiquetas_lineales, cmap='bwr', edgecolors='k')
plt.title("Datos separables linealmente")
plt.xlabel("Caracteristica 1")
plt.ylabel("Caracteristica 2")

# Caso 2: No separable linealmente
plt.subplot(1, 2, 2)
plt.scatter(datos_no_lineales[:, 0], datos_no_lineales[:, 1], c=etiquetas_no_lineales, cmap='bwr', edgecolors='k')
plt.title("Datos NO separables linealmente")
plt.xlabel("Caracteristica 1")
plt.ylabel("Caracteristica 2")

# Mostrar los graficos
plt.tight_layout()
plt.suptitle("Ejemplo de Separabilidad Lineal", fontsize=16, y=1.05)
plt.show()
