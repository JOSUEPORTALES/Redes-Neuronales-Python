# Programa para ilustrar dos tipos de gramáticas de la Jerarquía de Chomsky:
# - Una gramática regular (Tipo 3), que genera cadenas con 'a' seguidas de 'b'
# - Una gramática libre de contexto (Tipo 2), que genera cadenas balanceadas con 'a' y 'b'
# El objetivo es mostrar cómo se puede representar el conocimiento del lenguaje formal
# usando gramáticas, y cómo esto se relaciona con el procesamiento del lenguaje en IA.

import re

# ----------------------------
# GRAMATICA REGULAR (Tipo 3)
# ----------------------------

# Esta funcion verifica si una cadena pertenece a un lenguaje regular definido como:
# L = { a^n b^n | n >= 1 }, pero limitado a patrones simples con una sola a y b.
# Por ejemplo: "ab", "aab", "aaabbb" NO es aceptado por esta gramatica regular.
def es_cadena_valida_regular(cadena):
    patron = r"^a+b$"  # al menos una 'a' seguida de al menos una 'b'
    return re.match(patron, cadena) is not None


# ----------------------------
# GRAMATICA LIBRE DE CONTEXTO (Tipo 2)
# ----------------------------

# Esta funcion verifica si una cadena pertenece a una gramatica que genera cadenas
# con el mismo numero de 'a' y 'b', en forma balanceada (por ejemplo: 'aabb', 'aaabbb')
# Es un lenguaje clasico que requiere un autómata de pila, ya que necesita memoria.
def es_cadena_valida_libre_contexto(cadena):
    contador = 0
    for simbolo in cadena:
        if simbolo == 'a':
            contador += 1
        elif simbolo == 'b':
            contador -= 1
        else:
            return False  # solo se permiten 'a' y 'b'
        if contador < 0:
            return False  # más 'b' que 'a', no balanceado
    return contador == 0  # solo es valido si se balancea exactamente


# ----------------------------
# EJEMPLOS Y RESULTADOS
# ----------------------------

# Lista de cadenas de ejemplo
cadenas = ["ab", "aab", "aaabbb", "aabb", "abb", "aaaabbbb", "aabbb", "bbaa"]

print("Evaluacion de cadenas con gramatica REGULAR (Tipo 3):")
for c in cadenas:
    print(f"{c}: {'valida' if es_cadena_valida_regular(c) else 'no valida'}")

print("\nEvaluacion de cadenas con gramatica LIBRE DE CONTEXTO (Tipo 2):")
for c in cadenas:
    print(f"{c}: {'valida' if es_cadena_valida_libre_contexto(c) else 'no valida'}")
