from sympy import symbols
from sympy.logic.boolalg import Implies, And, Or, Not
from sympy.logic.inference import satisfiable


# Paso 1: definimos nuestras proposiciones (hechos logicos)
# Supongamos:
# A = "Esta lloviendo"
# B = "Hay nubes"
# C = "El suelo esta mojado"

A, B, C = symbols('A B C')  # Creamos las proposiciones logicas

# Paso 2: definimos la base de conocimiento (conjunto de reglas y hechos)
# Si llueve, entonces el suelo esta mojado: A → C
# Si hay nubes, entonces puede llover: B → A
# Sabemos que hay nubes: B es verdadero

base_conocimiento = [
    Implies(A, C),   # Regla 1
    Implies(B, A),   # Regla 2
    B                # Hecho conocido
]

# Paso 3: combinamos todo usando una conjuncion logica (AND)
base_total = And(*base_conocimiento)

# Paso 4: preguntamos al sistema si se puede deducir que el suelo esta mojado (C)
# Lo hacemos probando si la base + Not(C) es inconsistente (no tiene solucion)
es_posible_no_C = satisfiable(And(base_total, Not(C)))

# Paso 5: mostramos el resultado
if es_posible_no_C == False:
    print("El sistema deduce que el suelo esta mojado (C es verdadero).")
else:
    print("No se puede garantizar que el suelo este mojado con la informacion actual.")
