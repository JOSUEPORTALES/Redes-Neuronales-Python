# --------------------------------------------
# APRENDIZAJE PROFUNDO (SIN LIBRERÍAS EXTERNAS)
# Tema: Introducción a la I.A. - Aprendizaje Probabilístico
# --------------------------------------------

import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelBinarizer

# --------------------------------------------
# FUNCIONES DE ACTIVACION Y DERIVADAS
# --------------------------------------------

def sigmoide(x):
    return 1 / (1 + np.exp(-x))

def derivada_sigmoide(x):
    return sigmoide(x) * (1 - sigmoide(x))

def softmax(x):
    exp_x = np.exp(x - np.max(x))  # para evitar overflow
    return exp_x / np.sum(exp_x, axis=1, keepdims=True)

# --------------------------------------------
# FUNCION DE PERDIDA: ENTROPÍA CRUZADA
# --------------------------------------------

def perdida(entrenamiento, prediccion):
    n = entrenamiento.shape[0]
    return -np.sum(entrenamiento * np.log(prediccion + 1e-9)) / n  # evitar log(0)

# --------------------------------------------
# CARGA DE DATOS
# --------------------------------------------

datos = load_iris()
entradas = datos.data  # 4 características por flor
etiquetas = datos.target  # clases: 0, 1 o 2

# Convertimos etiquetas a codificacion one-hot
codificador = LabelBinarizer()
etiquetas_codificadas = codificador.fit_transform(etiquetas)

# Dividimos en entrenamiento y prueba
x_entrenamiento, x_prueba, y_entrenamiento, y_prueba = train_test_split(
    entradas, etiquetas_codificadas, test_size=0.2, random_state=42
)

# --------------------------------------------
# PARAMETROS DEL MODELO
# --------------------------------------------

# Cantidad de neuronas
entrada_dim = 4
oculto_dim = 6
salida_dim = 3

# Inicializacion aleatoria de pesos
np.random.seed(42)
pesos_entrada_oculta = np.random.randn(entrada_dim, oculto_dim)
bias_oculta = np.zeros((1, oculto_dim))

pesos_oculta_salida = np.random.randn(oculto_dim, salida_dim)
bias_salida = np.zeros((1, salida_dim))

# Tasa de aprendizaje
tasa_aprendizaje = 0.05

# --------------------------------------------
# ENTRENAMIENTO DEL MODELO
# --------------------------------------------

for epoca in range(5000):
    # ----- PROPAGACION HACIA ADELANTE -----
    capa_oculta = sigmoide(np.dot(x_entrenamiento, pesos_entrada_oculta) + bias_oculta)
    salida = softmax(np.dot(capa_oculta, pesos_oculta_salida) + bias_salida)

    # ----- CALCULO DEL ERROR -----
    error = salida - y_entrenamiento

    # ----- PROPAGACION HACIA ATRAS -----
    gradiente_salida = error / x_entrenamiento.shape[0]
    gradiente_pesos_oculta_salida = np.dot(capa_oculta.T, gradiente_salida)
    gradiente_bias_salida = np.sum(gradiente_salida, axis=0, keepdims=True)

    error_oculta = np.dot(gradiente_salida, pesos_oculta_salida.T) * derivada_sigmoide(np.dot(x_entrenamiento, pesos_entrada_oculta) + bias_oculta)
    gradiente_pesos_entrada_oculta = np.dot(x_entrenamiento.T, error_oculta)
    gradiente_bias_oculta = np.sum(error_oculta, axis=0, keepdims=True)

    # ----- ACTUALIZAMOS LOS PESOS -----
    pesos_oculta_salida -= tasa_aprendizaje * gradiente_pesos_oculta_salida
    bias_salida -= tasa_aprendizaje * gradiente_bias_salida
    pesos_entrada_oculta -= tasa_aprendizaje * gradiente_pesos_entrada_oculta
    bias_oculta -= tasa_aprendizaje * gradiente_bias_oculta

    # Mostramos el error cada 500 iteraciones
    if epoca % 500 == 0:
        perdida_actual = perdida(y_entrenamiento, salida)
        print(f"Epoca {epoca}, perdida: {perdida_actual:.4f}")

# --------------------------------------------
# EVALUACION CON DATOS DE PRUEBA
# --------------------------------------------

# Propagacion hacia adelante con datos nuevos
capa_oculta_prueba = sigmoide(np.dot(x_prueba, pesos_entrada_oculta) + bias_oculta)
salida_prueba = softmax(np.dot(capa_oculta_prueba, pesos_oculta_salida) + bias_salida)

# Comparamos predicciones
predicciones = np.argmax(salida_prueba, axis=1)
reales = np.argmax(y_prueba, axis=1)
precision = np.mean(predicciones == reales)
print(f"\nPrecisión sobre datos de prueba: {precision:.2f}")
