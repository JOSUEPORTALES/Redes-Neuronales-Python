# Esta funcion compara dos expresiones logicas simples y trata de unificarlas
# Cada expresion se representa como una tupla con nombre del predicado y argumentos
def unificar(expresion1, expresion2):
    sustituciones = {}  # Diccionario para guardar las igualdades encontradas

    # Si los predicados son distintos, no se pueden unificar
    if expresion1[0] != expresion2[0]:
        return None

    # Obtenemos los argumentos de ambas expresiones
    argumentos1 = expresion1[1]
    argumentos2 = expresion2[1]

    # Si tienen distinta cantidad de argumentos, no se pueden unificar
    if len(argumentos1) != len(argumentos2):
        return None

    # Recorremos los argumentos y buscamos coincidencias o sustituciones posibles
    for arg1, arg2 in zip(argumentos1, argumentos2):
        if arg1 == arg2:
            continue  # Si son iguales, no hay nada que hacer
        elif es_variable(arg1):  # Si el primero es variable, lo sustituimos
            sustituciones[arg1] = arg2
        elif es_variable(arg2):  # Si el segundo es variable, lo sustituimos
            sustituciones[arg2] = arg1
        else:
            return None  # Si ambos son constantes distintas, falla la unificacion

    return sustituciones  # Devolvemos el conjunto de sustituciones

# Funcion que determina si un valor es una variable (iniciando en minuscula)
def es_variable(simbolo):
    return simbolo[0].islower()

# --------------------------------------
# EJEMPLO PRACTICO

# Queremos unificar: padre(juan, X) con padre(juan, pedro)
expresion_a = ("padre", ["juan", "X"])
expresion_b = ("padre", ["juan", "pedro"])

# Ejecutamos la unificacion
resultado = unificar(expresion_a, expresion_b)

# Mostramos el resultado
if resultado is None:
    print("No fue posible unificar las expresiones.")
else:
    print("Sustituciones encontradas para la unificacion:")
    for variable, valor in resultado.items():
        print(f"{variable} = {valor}")

'''
Cada predicado (como padre) tiene argumentos.

Las variables se representan como cadenas que inician con minúsculas ("X", "y").

La unificación busca qué valor le podemos dar a una variable para que dos expresiones sean iguales.

En el ejemplo, la variable "X" se puede reemplazar por "pedro" para que padre(juan, X) sea igual a padre(juan, pedro).
'''
# Fin del código
# -------------------------------------- 