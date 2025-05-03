# AGENTE LOGICO SIMPLE
# Simula un agente que razona con reglas para decidir moverse o no.

# Hechos que el agente percibe
hechos = set()

# Reglas lógicas representadas como: (condiciones, accion)
reglas = [
    (["brisa", "no_hay_oro"], "no_moverse"),      # Si hay brisa y no hay oro, es peligroso
    (["no_brisa", "oro_visible"], "moverse"),     # Si no hay brisa y ve oro, se mueve
    (["oro_visible"], "recoger_oro"),             # Si ve oro, lo recoge
    (["brisa"], "posible_trampa"),                # Si hay brisa, puede haber trampa
]

# FUNCION PARA INFERIR ACCION A PARTIR DE HECHOS Y REGLAS
def inferir_accion(hechos, reglas):
    acciones = []
    for condiciones, accion in reglas:
        # Si todas las condiciones de la regla están presentes en los hechos
        if all(condicion in hechos for condicion in condiciones):
            acciones.append(accion)
    return acciones

# ---------------------------
# EJEMPLO 1: Hay brisa pero no hay oro
print("Ejemplo 1:")
hechos = {"brisa", "no_hay_oro"}
acciones = inferir_accion(hechos, reglas)
print(f"Hechos percibidos: {hechos}")
print(f"Acciones inferidas por el agente: {acciones}")

# ---------------------------
# EJEMPLO 2: No hay brisa y se ve oro
print("\nEjemplo 2:")
hechos = {"no_brisa", "oro_visible"}
acciones = inferir_accion(hechos, reglas)
print(f"Hechos percibidos: {hechos}")
print(f"Acciones inferidas por el agente: {acciones}")
