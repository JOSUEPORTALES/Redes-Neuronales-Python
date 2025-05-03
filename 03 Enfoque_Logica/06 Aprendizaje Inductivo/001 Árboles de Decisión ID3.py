import math
from collections import Counter

# Definimos la base de datos como una lista de diccionarios
# Cada ejemplo tiene atributos y una clase (jugar)
datos_entrenamiento = [
    {'clima': 'soleado', 'temperatura': 'caliente', 'jugar': 'no'},
    {'clima': 'soleado', 'temperatura': 'caliente', 'jugar': 'no'},
    {'clima': 'nublado', 'temperatura': 'caliente', 'jugar': 'si'},
    {'clima': 'lluvioso', 'temperatura': 'templado', 'jugar': 'si'},
    {'clima': 'lluvioso', 'temperatura': 'fria', 'jugar': 'si'},
    {'clima': 'lluvioso', 'temperatura': 'fria', 'jugar': 'no'},
    {'clima': 'nublado', 'temperatura': 'fria', 'jugar': 'si'},
    {'clima': 'soleado', 'temperatura': 'templado', 'jugar': 'no'},
    {'clima': 'soleado', 'temperatura': 'fria', 'jugar': 'si'},
    {'clima': 'lluvioso', 'temperatura': 'templado', 'jugar': 'si'}
]

# Funcion para calcular la entropia (cuanto desorden hay en los datos)
def calcular_entropia(datos):
    total = len(datos)
    conteo_clases = Counter([ejemplo['jugar'] for ejemplo in datos])
    entropia = 0
    for clase in conteo_clases:
        probabilidad = conteo_clases[clase] / total
        entropia -= probabilidad * math.log2(probabilidad)
    return entropia

# Funcion para calcular la ganancia de informacion de un atributo
def ganancia_informacion(datos, atributo):
    total = len(datos)
    valores = set([ejemplo[atributo] for ejemplo in datos])
    entropia_total = calcular_entropia(datos)
    entropia_atributo = 0
    for valor in valores:
        subconjunto = [ejemplo for ejemplo in datos if ejemplo[atributo] == valor]
        entropia_valor = calcular_entropia(subconjunto)
        entropia_atributo += (len(subconjunto) / total) * entropia_valor
    return entropia_total - entropia_atributo

# Funcion para construir el arbol usando ID3
def id3(datos, atributos):
    clases = [ejemplo['jugar'] for ejemplo in datos]
    if clases.count(clases[0]) == len(clases):
        # Si todos los ejemplos son de la misma clase, devolvemos esa clase
        return clases[0]
    if not atributos:
        # Si ya no hay atributos que usar, devolvemos la clase mayoritaria
        return Counter(clases).most_common(1)[0][0]

    # Elegimos el mejor atributo (el que tiene mayor ganancia)
    mejor_atributo = max(atributos, key=lambda a: ganancia_informacion(datos, a))
    arbol = {mejor_atributo: {}}
    valores = set([ejemplo[mejor_atributo] for ejemplo in datos])

    for valor in valores:
        subconjunto = [ejemplo for ejemplo in datos if ejemplo[mejor_atributo] == valor]
        if not subconjunto:
            # Si no hay datos para este valor, usamos la clase mayoritaria
            arbol[mejor_atributo][valor] = Counter(clases).most_common(1)[0][0]
        else:
            # Construimos el subarbol de forma recursiva
            nuevos_atributos = [a for a in atributos if a != mejor_atributo]
            arbol[mejor_atributo][valor] = id3(subconjunto, nuevos_atributos)

    return arbol

# Construimos el arbol con los atributos disponibles
atributos_disponibles = ['clima', 'temperatura']
arbol_decision = id3(datos_entrenamiento, atributos_disponibles)

# Mostramos el arbol generado
print("Arbol de decision generado:")
print(arbol_decision)
