import random

# Esta funcion evalua cuantas clausulas son verdaderas segun una asignacion de valores
def evaluar(clausulas, asignacion):
    total = 0
    for clausula in clausulas:
        verdadera = False
        for literal in clausula:
            if literal.startswith("¬"):
                simbolo = literal[1:]
                valor = not asignacion[simbolo]
            else:
                simbolo = literal
                valor = asignacion[simbolo]
            if valor:
                verdadera = True
                break
        if verdadera:
            total += 1
    return total

# Funcion principal que implementa el algoritmo de busqueda local por subida de colina
def subida_de_colina(clausulas, simbolos, max_intentos=100):
    # Crear una asignacion aleatoria inicial de verdadero/falso para cada simbolo
    asignacion = {s: random.choice([True, False]) for s in simbolos}

    # Evaluar cuantas clausulas se cumplen con la asignacion inicial
    mejor_valor = evaluar(clausulas, asignacion)

    print("Asignacion inicial:", asignacion)
    print("Clausulas verdaderas:", mejor_valor)

    # Intentamos mejorar la asignacion hasta llegar al maximo de intentos
    for _ in range(max_intentos):
        vecino_mejor = None
        valor_mejor = mejor_valor

        # Exploramos cambiar cada simbolo individualmente
        for simbolo in simbolos:
            nueva_asignacion = asignacion.copy()
            nueva_asignacion[simbolo] = not nueva_asignacion[simbolo]  # cambiamos su valor

            nuevo_valor = evaluar(clausulas, nueva_asignacion)

            # Si mejora el resultado, lo guardamos
            if nuevo_valor > valor_mejor:
                vecino_mejor = nueva_asignacion
                valor_mejor = nuevo_valor

        # Si encontramos una mejor asignacion, la usamos
        if vecino_mejor:
            asignacion = vecino_mejor
            mejor_valor = valor_mejor
            print("Mejorado:", asignacion, "| Clausulas verdaderas:", mejor_valor)
        else:
            # Si no encontramos mejora, nos detenemos
            break

    print("\n✔ Asignacion final encontrada:")
    print(asignacion)
    print("Clausulas satisfechas:", mejor_valor)

# Ejemplo de uso

# Clausulas en Forma Normal Conjuntiva (FNC)
# (p ∨ ¬q) ∧ (¬p ∨ r) ∧ (q ∨ r)
clausulas = [
    ["p", "¬q"],
    ["¬p", "r"],
    ["q", "r"]
]

# Lista de simbolos usados en las clausulas
simbolos = ["p", "q", "r"]

# Ejecutamos el algoritmo de busqueda local
subida_de_colina(clausulas, simbolos)
