# ============================================================
# ANALISIS LEXICO - EJEMPLO EN PYTHON
# ============================================================
# Este programa realiza un análisis léxico simple, es decir,
# toma una cadena de texto (una oración) y la divide en "tokens".
# Los tokens son palabras o símbolos individuales que pueden luego
# clasificarse como sustantivos, verbos, números, signos, etc.
# El análisis léxico es el primer paso del procesamiento de lenguaje natural
# y permite identificar los componentes básicos del lenguaje para su posterior análisis.


import re

# Funcion para analizar lexico de una oracion
def analisis_lexico(oracion):
    # Expresion regular para separar palabras, numeros y signos
    patron = r'\w+|[^\w\s]'
    
    # Aplicamos el patron a la oracion para extraer tokens
    tokens = re.findall(patron, oracion)

    # Lista donde almacenaremos los tokens clasificados
    tokens_clasificados = []

    for token in tokens:
        if token.isdigit():
            tipo = "numero"
        elif token.isalpha():
            tipo = "palabra"
        elif token in [".", ",", ":", ";", "!", "?"]:
            tipo = "signo_puntuacion"
        else:
            tipo = "otro"

        tokens_clasificados.append((token, tipo))

    return tokens_clasificados

# === Ejemplo de uso del analizador lexico ===

# Oracion de entrada
oracion_ejemplo = "El perro corre rapido, pero el gato duerme. Tiene 2 años."

# Ejecutamos el analisis lexico
resultado = analisis_lexico(oracion_ejemplo)

# Mostramos los tokens y sus tipos
print("Resultado del analisis lexico:\n")
for token, tipo in resultado:
    print(f"Token: '{token}' -> Tipo: {tipo}")
