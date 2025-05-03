import random

# Definimos el corpus de texto: un conjunto de frases o palabras
corpus = """
el perro corre rapido
el gato duerme tranquilo
el perro duerme en el sofa
la gata juega con el perro
"""

# 1. Preprocesamos el corpus para obtener una lista de palabras
# Convertimos todo a minúsculas y lo dividimos en palabras
palabras = corpus.lower().split()

# 2. Creamos el modelo de bigramas
# Un bigrama es un par de palabras consecutivas
bigramas = {}

# Generamos los bigramas, recorriendo la lista de palabras
for i in range(len(palabras) - 1):
    # Creamos un par de palabras consecutivas
    palabra_actual = palabras[i]
    palabra_siguiente = palabras[i + 1]
    
    # Si ya existe el bigrama, aumentamos su contador
    if (palabra_actual, palabra_siguiente) in bigramas:
        bigramas[(palabra_actual, palabra_siguiente)] += 1
    else:
        # Si no existe, lo agregamos con valor 1
        bigramas[(palabra_actual, palabra_siguiente)] = 1

# 3. Calculamos las probabilidades de los bigramas
probabilidades = {}
for (palabra_actual, palabra_siguiente), frecuencia in bigramas.items():
    # La probabilidad es la frecuencia del bigrama dividido por la frecuencia de la primera palabra
    frecuencia_palabra_actual = palabras.count(palabra_actual)
    probabilidad = frecuencia / frecuencia_palabra_actual
    probabilidades[(palabra_actual, palabra_siguiente)] = probabilidad

# 4. Función para generar texto aleatorio basado en las probabilidades
def generar_texto(semilla, longitud=10):
    palabra_actual = semilla
    texto_generado = [palabra_actual]
    
    for _ in range(longitud - 1):
        # Seleccionamos las siguientes palabras posibles basadas en la probabilidad
        opciones = [(palabra_actual, palabra_siguiente) for (palabra_actual, palabra_siguiente) in probabilidades.keys() if palabra_actual == palabra_actual]
        
        # Elegimos la palabra siguiente con mayor probabilidad
        siguiente_palabra = random.choices(opciones, weights=[probabilidades[(palabra_actual, palabra_siguiente)] for (palabra_actual, palabra_siguiente) in opciones])[0][1]
        
        # Añadimos la palabra al texto generado
        texto_generado.append(siguiente_palabra)
        
        # Actualizamos la palabra actual
        palabra_actual = siguiente_palabra
    
    return ' '.join(texto_generado)

# 5. Mostrar el modelo de probabilidades
print("Probabilidades de los bigramas:")
for bigrama, probabilidad in probabilidades.items():
    print(f"P({bigrama[1]} | {bigrama[0]}) = {probabilidad:.4f}")

# 6. Generar texto aleatorio a partir de una semilla
semilla = "el"
texto_generado = generar_texto(semilla, longitud=10)
print("\nTexto generado a partir de la semilla '{}':".format(semilla))
print(texto_generado)
