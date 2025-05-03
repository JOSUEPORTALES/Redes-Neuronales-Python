# Ejemplo de Listas de Decisión: K-DL y K-DT
# Tema: Introducción a la I.A. - Aprendizaje Inductivo - Listas de Decisión

# En este ejemplo mostraremos como se comportan una lista de decisión (K-DL)
# y un arbol de decisión (K-DT) usando un conjunto de datos simple

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, export_text
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import numpy as np

# Cargamos el conjunto de datos Iris
conjunto = load_iris()
caracteristicas = conjunto.data
clases = conjunto.target

# Usamos solo dos clases (por simplicidad) y dos caracteristicas
filtro = clases != 2
caracteristicas = caracteristicas[filtro][:, :2]  # solo tomamos 2 caracteristicas
clases = clases[filtro]

# Dividimos el conjunto en entrenamiento y prueba
carac_entrenamiento, carac_prueba, clases_entrenamiento, clases_prueba = train_test_split(
    caracteristicas, clases, test_size=0.3, random_state=0
)

# ----- K-DT: Arbol de decision -----

# Creamos un arbol de decision de profundidad 1 (k = 1)
arbol = DecisionTreeClassifier(max_depth=1)
arbol.fit(carac_entrenamiento, clases_entrenamiento)

# Predecimos y evaluamos
predicciones_arbol = arbol.predict(carac_prueba)
precision_arbol = accuracy_score(clases_prueba, predicciones_arbol)

print("\n--- Arbol de Decision (K-DT) ---")
print("Precision:", precision_arbol)
print(export_text(arbol, feature_names=conjunto.feature_names[:2]))

# ----- K-DL: Lista de decision -----

# Simularemos una lista de decision usando regresion logistica escalonada
# Esto es una aproximacion simple a una lista de reglas secuenciales

# Creamos dos clasificadores logisticos secuenciales (simula una lista)
clasificador1 = LogisticRegression().fit(carac_entrenamiento, clases_entrenamiento)

# La salida se transforma a 0 o 1 segun la prediccion
prediccion_dl = clasificador1.predict(carac_prueba)
precision_dl = accuracy_score(clases_prueba, prediccion_dl)

print("\n--- Lista de Decision (K-DL aproximado) ---")
print("Precision:", precision_dl)

# Mostramos algunas predicciones
for i in range(5):
    print("Entrada:", carac_prueba[i], "- Clase real:", clases_prueba[i], "- Predicho:", prediccion_dl[i])
