# Importamos itertools para generar todas las combinaciones posibles de valores de verdad
import itertools

# Definimos la funcion para la implicacion logica (p → q)
def implicacion(p, q):
    # La implicacion solo es falsa si p es verdadero y q es falso
    return (not p) or q

# Definimos la funcion para evaluar la equivalencia, validez y satisfacibilidad
def analizar_logica():
    # Lista para almacenar combinaciones de valores de verdad
    combinaciones = list(itertools.product([True, False], repeat=2))

    # Listas para guardar los resultados de cada expresion
    resultados_1 = []
    resultados_2 = []

    print("llueve | calle_mojada | ¬llueve ∨ calle_mojada | llueve → calle_mojada")
    print("---------------------------------------------------------------")

    # Recorremos todas las combinaciones posibles de valores
    for llueve, calle_mojada in combinaciones:
        # expresion_1: ¬p ∨ q
        expresion_1 = (not llueve) or calle_mojada

        # expresion_2: p → q
        expresion_2 = implicacion(llueve, calle_mojada)

        # Guardamos los resultados
        resultados_1.append(expresion_1)
        resultados_2.append(expresion_2)

        # Mostramos la fila de la tabla
        print(f"{llueve!s:^7} | {calle_mojada!s:^13} | {expresion_1!s:^23} | {expresion_2!s:^23}")

    print("\n--- Analisis ---")

    # Equivalencia: las dos expresiones son equivalentes si todos sus resultados son iguales
    equivalentes = resultados_1 == resultados_2
    print(f"¿Son equivalentes? {'Sí' if equivalentes else 'No'}")

    # Validez: una expresion es valida si es verdadera en todos los casos
    es_valida_1 = all(resultados_1)
    es_valida_2 = all(resultados_2)
    print(f"¿Expresion 1 es valida? {'Sí' if es_valida_1 else 'No'}")
    print(f"¿Expresion 2 es valida? {'Sí' if es_valida_2 else 'No'}")

    # Satisfacibilidad: una expresion es satisfacible si al menos una combinacion da True
    es_satisfacible_1 = any(resultados_1)
    es_satisfacible_2 = any(resultados_2)
    print(f"¿Expresion 1 es satisfacible? {'Sí' if es_satisfacible_1 else 'No'}")
    print(f"¿Expresion 2 es satisfacible? {'Sí' if es_satisfacible_2 else 'No'}")

# Llamamos a la funcion principal
analizar_logica()
