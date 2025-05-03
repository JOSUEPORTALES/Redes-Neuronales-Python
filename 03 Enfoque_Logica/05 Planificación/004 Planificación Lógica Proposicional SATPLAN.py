# Planificación Lógica Proposicional - SATPLAN
# Ejemplo: Mover una caja de A a B

# Estado inicial: La caja está en A
estado_inicial = {
    "caja_en_A": True,
    "caja_en_B": False
}

# Estado objetivo: La caja debe estar en B
estado_objetivo = {
    "caja_en_B": True
}

# Definimos las acciones posibles
acciones = [
    {
        "nombre": "mover_A_a_B",
        "precondiciones": {"caja_en_A"},
        "efectos": {"caja_en_A": False, "caja_en_B": True}
    },
    {
        "nombre": "mover_B_a_A",
        "precondiciones": {"caja_en_B"},
        "efectos": {"caja_en_B": False, "caja_en_A": True}
    }
]

# Función que verifica si todas las precondiciones de una acción se cumplen en el estado actual
def verificar_precondiciones(estado, precondiciones):
    for precondicion in precondiciones:
        if not estado.get(precondicion, False):
            return False
    return True

# Función que aplica los efectos de una acción al estado actual y devuelve un nuevo estado
def aplicar_efectos(estado, efectos):
    nuevo_estado = estado.copy()
    for clave, valor in efectos.items():
        nuevo_estado[clave] = valor
    return nuevo_estado

# Función principal de planificación
def planificar(estado_inicial, estado_objetivo, acciones, max_pasos=5):
    estado_actual = estado_inicial.copy()
    plan = []

    for _ in range(max_pasos):  # Evita ciclos infinitos
        # Verificamos si ya alcanzamos el objetivo
        if all(estado_actual.get(clave, False) == valor for clave, valor in estado_objetivo.items()):
            return plan

        # Buscamos una acción que podamos ejecutar
        for accion in acciones:
            if verificar_precondiciones(estado_actual, accion["precondiciones"]):
                estado_actual = aplicar_efectos(estado_actual, accion["efectos"])
                plan.append(accion["nombre"])
                break
        else:
            # Si ninguna acción es aplicable, terminamos
            break

    if all(estado_actual.get(clave, False) == valor for clave, valor in estado_objetivo.items()):
        return plan
    else:
        return None

# Ejecutamos el planificador
plan = planificar(estado_inicial, estado_objetivo, acciones)

# Mostramos el resultado
if plan:
    print("Plan encontrado:")
    for paso in plan:
        print("-", paso)
else:
    print("No se pudo encontrar un plan.")
