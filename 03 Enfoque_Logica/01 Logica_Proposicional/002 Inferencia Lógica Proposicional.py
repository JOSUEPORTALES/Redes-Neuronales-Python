# Importamos las herramientas necesarias de sympy
from sympy import symbols
from sympy.logic.boolalg import Implies, And, Not
from sympy.logic.inference import satisfiable

# Paso 1: definimos nuestras proposiciones
# P: "Pedro estudia"
# Q: "Pedro aprueba el examen"
# R: "Pedro recibe una beca"

P, Q, R = symbols('P Q R')

# Paso 2: definimos las reglas del sistema (base de conocimiento)
# Regla 1: Si Pedro estudia, entonces aprueba el examen (P → Q)
# Regla 2: Si Pedro aprueba el examen, entonces recibe una beca (Q → R)
# Hecho conocido: Pedro estudia (P es verdadero)

base_conocimiento = [
    Implies(P, Q),  # Regla 1
    Implies(Q, R),  # Regla 2
    P               # Hecho conocido
]

# Paso 3: combinamos todas las reglas y hechos con una conjuncion (AND)
base_total = And(*base_conocimiento)

# Paso 4: queremos saber si se puede inferir que Pedro recibe beca (R)
# Para eso intentamos negar R y ver si eso lleva a una contradiccion
es_posible_no_R = satisfiable(And(base_total, Not(R)))

# Paso 5: mostramos el resultado
if es_posible_no_R == False:
    print("El sistema deduce que Pedro recibe una beca (R es verdadero).")
else:
    print("No se puede deducir con certeza que Pedro recibe una beca.")
