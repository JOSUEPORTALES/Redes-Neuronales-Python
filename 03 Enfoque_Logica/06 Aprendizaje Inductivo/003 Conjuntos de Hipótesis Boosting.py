# Importamos las librerías necesarias
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import AdaBoostClassifier
from sklearn.metrics import accuracy_score

# Cargamos los datos del conjunto "iris"
datos = load_iris()

# Separamos las variables predictoras (caracteristicas) y la clase (tipo de flor)
caracteristicas = datos.data
clases = datos.target

# Dividimos los datos en entrenamiento y prueba (70% y 30%)
carac_entrenamiento, carac_prueba, clases_entrenamiento, clases_prueba = train_test_split(
    caracteristicas, clases, test_size=0.3, random_state=1
)

# Creamos un clasificador debil: un arbol de decision pequeño
clasificador_debil = DecisionTreeClassifier(max_depth=1)

# Creamos el clasificador boosting (AdaBoost) usando clasificadores debiles
modelo_boosting = AdaBoostClassifier(
    estimator=clasificador_debil,  # Clasificador debil base
    n_estimators=10,
    learning_rate=1.0,
    random_state=1
)

# Entrenamos el modelo con los datos de entrenamiento
modelo_boosting.fit(carac_entrenamiento, clases_entrenamiento)

# Usamos el modelo entrenado para predecir con los datos de prueba
clases_predichas = modelo_boosting.predict(carac_prueba)

# Evaluamos la precision del modelo
precision = accuracy_score(clases_prueba, clases_predichas)

# Mostramos el resultado
print("Precision del modelo Boosting:", precision)

# Mostramos las clases reales y las predichas para entender el rendimiento
print("Clases reales:   ", clases_prueba)
print("Clases predichas:", clases_predichas)
