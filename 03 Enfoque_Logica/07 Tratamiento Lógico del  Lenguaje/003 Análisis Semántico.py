# ============================================================
# ANALISIS SEMANTICO - EJEMPLO EN PYTHON
# ============================================================
# Este programa realiza un analisis semantico basico, es decir,
# intenta comprender el significado de una oracion sencilla.
# Utilizaremos un diccionario de sinonimos para interpretar
# si una palabra o frase tiene un significado similar a otra.
# El analisis semantico es una parte del tratamiento del lenguaje
# que busca interpretar lo que realmente quiere decir una oracion,
# mas alla de solo dividirla en palabras.



# Diccionario de sinonimos para algunas palabras comunes
diccionario_sinonimos = {
    "feliz": ["contento", "alegre", "satisfecho"],
    "triste": ["deprimido", "melancolico", "infeliz"],
    "correr": ["trotar", "sprintar", "moverse_rapido"],
    "comer": ["alimentarse", "degustar", "consumir"]
}

# Funcion que busca el significado (sinonimos) de una palabra
def obtener_significado(palabra):
    for clave, sinonimos in diccionario_sinonimos.items():
        if palabra == clave or palabra in sinonimos:
            return f"La palabra '{palabra}' significa o esta relacionada con '{clave}'."
    return f"No se encontro un significado claro para la palabra '{palabra}'."

# Funcion de analisis semantico de una oracion
def analisis_semantico(oracion):
    # Dividimos la oracion en palabras
    palabras = oracion.lower().split()

    # Analizamos cada palabra buscando su significado
    for palabra in palabras:
        significado = obtener_significado(palabra)
        print(significado)

# === Ejemplo de uso ===

oracion_ejemplo = "El niño esta contento y le gusta correr y comer."

print("Resultado del analisis semantico:\n")
analisis_semantico(oracion_ejemplo)
