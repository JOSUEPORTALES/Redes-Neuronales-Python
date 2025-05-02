from collections import defaultdict

# Paso 1: corpus paralelo (frases en ingles y español alineadas)
corpus_ingles = [
    "the dog eats",
    "the cat eats",
    "a dog runs",
    "a cat sleeps"
]

corpus_espanol = [
    "el perro come",
    "el gato come",
    "un perro corre",
    "un gato duerme"
]

# Paso 2: contar alineaciones palabra a palabra
# Vamos a contar cada vez que una palabra inglesa aparece con una española en la misma posicion
frecuencias = defaultdict(lambda: defaultdict(int))

for frase_ing, frase_esp in zip(corpus_ingles, corpus_espanol):
    palabras_ing = frase_ing.split()
    palabras_esp = frase_esp.split()
    
    for palabra_ing, palabra_esp in zip(palabras_ing, palabras_esp):
        frecuencias[palabra_ing][palabra_esp] += 1

# Paso 3: convertir a probabilidades (normalizar)
modelo_probabilidades = {}

for palabra_ing, traducciones in frecuencias.items():
    total = sum(traducciones.values())
    modelo_probabilidades[palabra_ing] = {palabra_esp: conteo / total for palabra_esp, conteo in traducciones.items()}

# Paso 4: funcion de traduccion palabra por palabra
def traducir_frase(frase_ingles):
    palabras = frase_ingles.split()
    traduccion = []
    for palabra in palabras:
        if palabra in modelo_probabilidades:
            # Tomamos la traduccion mas probable
            palabra_esp = max(modelo_probabilidades[palabra], key=modelo_probabilidades[palabra].get)
            traduccion.append(palabra_esp)
        else:
            traduccion.append(palabra)  # palabra desconocida
    return ' '.join(traduccion)

# Ejemplos de traduccion
print("Ejemplos de traduccion automatica estadistica:")
frases_prueba = [
    "the dog eats",
    "a cat sleeps",
    "a dog runs"
]

for frase in frases_prueba:
    print(f"Ingles: {frase} → Espanol: {traducir_frase(frase)}")
