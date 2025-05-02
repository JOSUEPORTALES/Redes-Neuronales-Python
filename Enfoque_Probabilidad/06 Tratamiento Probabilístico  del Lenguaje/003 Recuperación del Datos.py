import math

# 1. Definir un conjunto de documentos (corpus)
# Los documentos son simplemente textos que simulan artículos o párrafos.
documentos = [
    "el perro corre rapido",
    "el gato duerme tranquilo",
    "el perro duerme en el sofa",
    "la gata juega con el perro"
]

# 2. Definir la consulta de búsqueda
consulta = "perro duerme"

# 3. Preprocesar los documentos y la consulta
# Convertimos todo a minúsculas para evitar diferencias por mayúsculas/minúsculas
documentos_procesados = [doc.lower().split() for doc in documentos]
consulta_procesada = consulta.lower().split()

# 4. Contar la frecuencia de cada palabra en los documentos
# Esto nos ayudará a calcular la probabilidad de ocurrencia de una palabra
def contar_palabras(documentos):
    contador = {}
    for doc in documentos:
        for palabra in doc:
            if palabra in contador:
                contador[palabra] += 1
            else:
                contador[palabra] = 1
    return contador

# 5. Calcular la probabilidad de relevancia de cada documento con respecto a la consulta
# Utilizaremos la fórmula simplificada de "Modelo de Recuperación Probabilística"
# P(relevancia | documento) es proporcional a la probabilidad de que las palabras de la consulta ocurran en el documento

# 6. Función para calcular la probabilidad de relevancia
def calcular_probabilidad_relevancia(documento, consulta, contador_palabras, total_documentos):
    probabilidad = 1
    for palabra in consulta:
        # Calculamos la probabilidad de cada palabra en el documento
        frecuencia_palabra = documento.count(palabra)
        frecuencia_palabra_en_corpus = contador_palabras.get(palabra, 0)  # Número de documentos que contienen la palabra
        
        # Aplicamos la fórmula simplificada de probabilidad de relevancia
        if frecuencia_palabra_en_corpus > 0:
            probabilidad_palabra = (frecuencia_palabra + 1) / (frecuencia_palabra_en_corpus + total_documentos)
            probabilidad *= probabilidad_palabra
        else:
            probabilidad *= 0.0001  # Si no existe la palabra en el corpus, su probabilidad es muy baja
    return probabilidad

# 7. Función para recuperar documentos más relevantes basados en la consulta
def recuperar_documentos(consulta, documentos, contador_palabras):
    probabilidad_documentos = []
    total_documentos = len(documentos)
    
    for i, documento in enumerate(documentos_procesados):
        probabilidad = calcular_probabilidad_relevancia(documento, consulta_procesada, contador_palabras, total_documentos)
        probabilidad_documentos.append((i, probabilidad))
    
    # Ordenamos los documentos por la probabilidad de relevancia (de mayor a menor)
    probabilidad_documentos.sort(key=lambda x: x[1], reverse=True)
    
    # Mostramos los documentos ordenados por relevancia
    for i, probabilidad in probabilidad_documentos:
        print(f"Documento {i + 1} (Probabilidad de relevancia: {probabilidad:.4f}):")
        print(" ".join(documentos[i]))
        print("-" * 50)

# 8. Preprocesamos el corpus y calculamos la frecuencia de las palabras
contador_palabras = contar_palabras([doc.split() for doc in documentos])

# 9. Recuperar los documentos más relevantes para la consulta
print(f"Consulta: '{consulta}'\n")
recuperar_documentos(consulta, documentos, contador_palabras)
