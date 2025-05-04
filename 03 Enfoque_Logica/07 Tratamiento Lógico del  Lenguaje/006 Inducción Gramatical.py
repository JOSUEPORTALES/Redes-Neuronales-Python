# ===============================================================
# INDUCCION GRAMATICAL - EJEMPLO SIMPLE EN PYTHON
# ===============================================================
# Este programa muestra como una IA puede inducir (aprender) una
# regla gramatical simple a partir de ejemplos positivos.
# Se analizan frases con estructura sujeto-verbo-objeto (SVO)
# para identificar una regla comun y luego verificar si nuevas
# frases cumplen esa misma estructura.
# No se usa ninguna libreria externa, solo estructuras basicas.


# Lista de frases correctas que el programa usará para inducir una regla
frases_entrenamiento = [
    "juan come manzana",
    "ana lee libro",
    "maria compra flores",
    "pedro bebe agua"
]

# Suponemos que cada frase esta estructurada como:
# sujeto (nombre) + verbo + objeto (sustantivo)

# Creamos listas simples para simular las clases gramaticales
nombres = ["juan", "ana", "maria", "pedro"]
verbos = ["come", "lee", "compra", "bebe"]
sustantivos = ["manzana", "libro", "flores", "agua"]

# Funcion que verifica si una frase sigue la estructura SVO
def es_frase_valida(frase):
    palabras = frase.split()
    
    if len(palabras) != 3:
        return False  # La frase debe tener exactamente 3 palabras
    
    sujeto, verbo, objeto = palabras
    
    # Verificamos si cada palabra esta en la clase correcta
    if sujeto in nombres and verbo in verbos and objeto in sustantivos:
        return True
    else:
        return False

# Frases nuevas para verificar si cumplen la regla inducida
frases_prueba = [
    "juan lee libro",         # valida
    "ana come flores",        # valida
    "libro lee juan",         # invalida
    "pedro corre rapido"      # invalida
]

# Mostrar resultados de prueba
print("Evaluacion de frases usando la regla inducida (SVO):\n")
for frase in frases_prueba:
    if es_frase_valida(frase):
        print(f'"{frase}" -> Frase valida (estructura SVO reconocida)')
    else:
        print(f'"{frase}" -> Frase invalida (estructura no reconocida)')

# Comentario final:
# Este ejemplo demuestra como una IA puede inducir una "regla gramatical"
# basica observando patrones comunes en frases correctas.
# En la vida real, esto se usa para aprender la sintaxis de un idioma.
