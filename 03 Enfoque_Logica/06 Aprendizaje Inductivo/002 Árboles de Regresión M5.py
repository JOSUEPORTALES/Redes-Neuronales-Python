import numpy as np
from sklearn.linear_model import LinearRegression

# Definimos los datos de entrenamiento (cada dato es una casa con atributos)
# Cada casa tiene metros, habitaciones y precio
datos_entrenamiento = [
    {'metros': 50, 'habitaciones': 1, 'precio': 100000},
    {'metros': 60, 'habitaciones': 2, 'precio': 120000},
    {'metros': 80, 'habitaciones': 2, 'precio': 150000},
    {'metros': 100, 'habitaciones': 3, 'precio': 200000},
    {'metros': 120, 'habitaciones': 4, 'precio': 250000},
    {'metros': 150, 'habitaciones': 5, 'precio': 300000}
]

# Funcion para construir el arbol de regresion de forma recursiva
def construir_arbol(datos, profundidad=0, profundidad_max=2):
    # Si ya alcanzamos la profundidad maxima, aplicamos regresion lineal
    if profundidad == profundidad_max or len(datos) < 2:
        modelo = LinearRegression()
        X = np.array([[d['metros'], d['habitaciones']] for d in datos])
        y = np.array([d['precio'] for d in datos])
        modelo.fit(X, y)
        return {'modelo': modelo}

    # Elegimos el mejor punto para dividir (en este ejemplo fijo: 100 m²)
    punto_corte = 100
    datos_izquierda = [d for d in datos if d['metros'] <= punto_corte]
    datos_derecha = [d for d in datos if d['metros'] > punto_corte]

    # Si no podemos dividir, entrenamos un modelo
    if not datos_izquierda or not datos_derecha:
        modelo = LinearRegression()
        X = np.array([[d['metros'], d['habitaciones']] for d in datos])
        y = np.array([d['precio'] for d in datos])
        modelo.fit(X, y)
        return {'modelo': modelo}

    # Si podemos dividir, construimos ramas recursivamente
    return {
        'atributo': 'metros',
        'valor': punto_corte,
        'izquierda': construir_arbol(datos_izquierda, profundidad + 1, profundidad_max),
        'derecha': construir_arbol(datos_derecha, profundidad + 1, profundidad_max)
    }

# Funcion para predecir el precio usando el arbol construido
def predecir(arbol, ejemplo):
    if 'modelo' in arbol:
        entrada = np.array([[ejemplo['metros'], ejemplo['habitaciones']]])
        return arbol['modelo'].predict(entrada)[0]
    else:
        if ejemplo[arbol['atributo']] <= arbol['valor']:
            return predecir(arbol['izquierda'], ejemplo)
        else:
            return predecir(arbol['derecha'], ejemplo)

# Construimos el arbol
arbol_regresion = construir_arbol(datos_entrenamiento)

# Ejemplo: predecimos el precio de una casa nueva
casa_nueva = {'metros': 110, 'habitaciones': 3}
precio_estimado = predecir(arbol_regresion, casa_nueva)

# Mostramos el resultado
print("Precio estimado para la casa:", round(precio_estimado))
