# Importamos las librerías necesarias
from sklearn.tree import DecisionTreeClassifier, export_text
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report

# Cargamos un conjunto de datos simple: el conjunto de flores iris
# Este conjunto tiene flores con distintos atributos (largo de pétalos, etc.)
# y queremos predecir la especie de flor.
datos = load_iris()

# Dividimos los datos en conjunto de entrenamiento y prueba
entradas_entrenamiento, entradas_prueba, salidas_entrenamiento, salidas_prueba = train_test_split(
    datos.data, datos.target, test_size=0.3, random_state=42
)

# Creamos un clasificador de árbol de decisión
modelo = DecisionTreeClassifier(random_state=42)

# Entrenamos el modelo con los datos de entrenamiento
modelo.fit(entradas_entrenamiento, salidas_entrenamiento)

# Hacemos predicciones con el modelo usando los datos de prueba
predicciones = modelo.predict(entradas_prueba)

# Mostramos un reporte de cómo de bien funcionó el modelo
print("REPORTE DE CLASIFICACION:")
print(classification_report(salidas_prueba, predicciones, target_names=datos.target_names))

# Explicamos el modelo como texto que una persona puede leer
# Mostramos las decisiones que toma el modelo para clasificar
print("\nEXPLICACION DEL ARBOL DE DECISION:")
arbol_texto = export_text(modelo, feature_names=datos.feature_names)
print(arbol_texto)

# Mostramos que tan importante fue cada atributo para tomar decisiones
importancias = modelo.feature_importances_
print("\nIMPORTANCIA DE LOS ATRIBUTOS (informacion relevante):")
for nombre, importancia in zip(datos.feature_names, importancias):
    print(f"- {nombre}: {importancia:.2f}")
