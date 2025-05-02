import random

# Gramática lexicalizada: cada regla incluye una palabra 'cabeza'
# Estructura: lado izquierdo -> lista de (expansion, palabra cabeza, probabilidad)
gramatica = {
    'S': [
        ('NP VP', 'verbo', 1.0)  # El verbo es la palabra más importante de la oración
    ],
    'NP': [
        ('articulo sustantivo', 'sustantivo', 1.0)
    ],
    'VP': [
        ('verbo NP', 'verbo', 1.0)
    ],
    'articulo': [
        ('el', 'el', 0.5), ('la', 'la', 0.5)
    ],
    'sustantivo': [
        ('gato', 'gato', 0.5), ('perro', 'perro', 0.5)
    ],
    'verbo': [
        ('persigue', 'persigue', 0.5), ('mira', 'mira', 0.5)
    ]
}

# Funcion para elegir una expansion aleatoriamente segun probabilidad
def elegir_expansion(opciones):
    total = sum(prob for _, _, prob in opciones)
    r = random.uniform(0, total)
    acumulado = 0
    for expansion, cabeza, prob in opciones:
        acumulado += prob
        if r <= acumulado:
            return expansion, cabeza

# Funcion recursiva que genera la oracion y asocia palabras cabeza
def generar_oracion(simbolo):
    if simbolo not in gramatica:
        # Es un terminal, retornamos la palabra y ella misma como cabeza
        return simbolo, simbolo

    expansion, cabeza = elegir_expansion(gramatica[simbolo])
    partes = expansion.split()
    
    palabras = []
    cabeza_final = None
    
    for parte in partes:
        palabra, cabeza_sub = generar_oracion(parte)
        palabras.append(palabra)
        if parte == cabeza:
            cabeza_final = cabeza_sub
    
    return ' '.join(palabras), cabeza_final

# Generar varias oraciones con sus palabras cabeza
print("Oraciones generadas con sus cabezas léxicas:")
for _ in range(5):
    oracion, cabeza = generar_oracion('S')
    print(f"Oracion: '{oracion}' | Palabra cabeza: '{cabeza}'")
