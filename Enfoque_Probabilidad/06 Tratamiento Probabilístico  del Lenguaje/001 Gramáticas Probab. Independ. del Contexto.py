import random

# Definimos una gramática probabilística simple
gramatica = {
    'S': [('NP VP', 1.0)],  # Oración = Sintagma nominal + verbal

    'NP': [('articulo sustantivo', 0.6), ('nombre', 0.4)],
    'VP': [('verbo NP', 1.0)],

    'articulo': [('el', 0.5), ('la', 0.5)],
    'sustantivo': [('gato', 0.5), ('perra', 0.5)],
    'verbo': [('ve', 1.0)],
    'nombre': [('juan', 1.0)]
}

# Funcion para elegir una expansion basada en probabilidad
def elegir_expansion(opciones):
    total = sum(prob for _, prob in opciones)
    r = random.uniform(0, total)
    acumulado = 0
    for opcion, prob in opciones:
        acumulado += prob
        if r <= acumulado:
            return opcion

# Funcion recursiva que genera la oracion
def generar_oracion(simbolo):
    if simbolo not in gramatica:
        return simbolo  # Es una palabra terminal
    expansion = elegir_expansion(gramatica[simbolo])
    partes = expansion.split()
    return ' '.join([generar_oracion(p) for p in partes])

# Generamos varias oraciones de ejemplo
print("Oraciones generadas con la gramática probabilística:")
for _ in range(5):
    print(generar_oracion('S'))
