# ============================================================
# GRAMATICA CAUSAL DEFINIDA (DCG) - EJEMPLO EN PYTHON
# ============================================================
# Este programa simula una gramatica causal definida simple,
# que permite analizar si una oracion sigue una estructura valida.
# Las gramaticas causales definidas se usan para representar
# la estructura sintactica de un lenguaje natural de manera logica.
# Se definen reglas que describen como se forma una oracion,
# y se puede comprobar si una oracion es gramaticalmente correcta.



# Definimos una funcion para verificar si una oracion es valida
# segun una gramatica causal definida simple

# Nuestra gramatica permitira oraciones como:
# "el gato come pescado", "la niña lee libro", etc.

# Reglas gramaticales definidas manualmente

def es_articulo(palabra):
    return palabra in ["el", "la"]

def es_sustantivo(palabra):
    return palabra in ["gato", "perro", "pescado", "niña", "libro"]

def es_verbo(palabra):
    return palabra in ["come", "lee", "muerde", "mira"]

# Funcion que representa una oracion como una estructura: Sujeto + Verbo + Objeto
def es_oracion_valida(oracion):
    # Dividimos la oracion en palabras
    palabras = oracion.lower().split()

    # La estructura valida es de 4 palabras: articulo + sustantivo + verbo + sustantivo
    if len(palabras) != 4:
        return False

    # Se separan las partes de la oracion
    articulo_sujeto, sustantivo_sujeto, verbo, sustantivo_objeto = palabras

    # Verificamos si cada parte es valida segun nuestra gramatica
    if (es_articulo(articulo_sujeto) and
        es_sustantivo(sustantivo_sujeto) and
        es_verbo(verbo) and
        es_sustantivo(sustantivo_objeto)):
        return True
    else:
        return False

# === Ejemplo de uso ===

oracion_1 = "el gato come pescado"
oracion_2 = "la niña lee libro"
oracion_3 = "niña come pescado"  # Esta es incorrecta porque le falta el articulo

print("Resultado del analisis gramatical:\n")

for oracion in [oracion_1, oracion_2, oracion_3]:
    if es_oracion_valida(oracion):
        print(f"La oracion '{oracion}' es gramaticalmente valida.")
    else:
        print(f"La oracion '{oracion}' NO es gramaticalmente valida.")
