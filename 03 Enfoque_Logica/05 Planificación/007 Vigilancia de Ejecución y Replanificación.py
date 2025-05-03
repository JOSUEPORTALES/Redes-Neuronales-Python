# Simulacion de vigilancia de ejecucion y replanificacion

# Estado inicial: el robot esta en la habitacion A
estado_inicial = {
    "robot_en_A": True,
    "robot_en_B": False,
    "obstaculo_en_B": False  # Esto puede cambiar en tiempo de ejecucion
}

# Estado objetivo: el robot debe estar en la habitacion B
estado_objetivo = {
    "robot_en_B": True
}

# Definimos las acciones posibles
acciones = [
    {
        "nombre": "mover_A_a_B",
        "precondiciones": {"robot_en_A", "obstaculo_en_B == False"},
        "efectos": {"robot_en_A": False, "robot_en_B": True}
    },
    {
        "nombre": "mover_B_a_A",
        "precondiciones": {"robot_en_B"},
        "efectos": {"robot_en_B": False, "robot_en_A": True}
    }
]

# Verifica si las precondiciones se cumplen
def verificar_precondiciones(estado, precondiciones):
    for precondicion in precondiciones:
        if "==" in precondicion:
            clave, valor = precondicion.split("==")
            clave = clave.strip()
            valor = valor.strip() == "True"
            if estado.get(clave, False) != valor:
                return False
        else:
            if not estado.get(precondicion, False):
                return False
    return True

# Aplica los efectos de una accion al estado
def aplicar_efectos(estado, efectos):
    nuevo_estado = estado.copy()
    for clave, valor in efectos.items():
        nuevo_estado[clave] = valor
    return nuevo_estado

# Función de planificación simple
def planificar(estado, objetivo, acciones):
    plan = []
    estado_actual = estado.copy()

    for paso in range(5):  # maximo 5 pasos para evitar bucles
        if all(estado_actual.get(k, False) == v for k, v in objetivo.items()):
            return plan

        for accion in acciones:
            if verificar_precondiciones(estado_actual, accion["precondiciones"]):
                estado_actual = aplicar_efectos(estado_actual, accion["efectos"])
                plan.append(accion["nombre"])
                break
        else:
            break

    if all(estado_actual.get(k, False) == v for k, v in objetivo.items()):
        return plan
    else:
        return None

# Funcion de ejecucion con vigilancia y replanificacion si hay fallos
def ejecutar_plan_con_vigilancia(estado, objetivo, acciones):
    plan = planificar(estado, objetivo, acciones)
    if not plan:
        print("No se pudo generar un plan inicial.")
        return

    estado_actual = estado.copy()
    print("Iniciando ejecucion del plan...")
    for paso in plan:
        print("Intentando ejecutar:", paso)

        # Simulamos un cambio en el mundo: aparece un obstaculo
        if paso == "mover_A_a_B":
            estado_actual["obstaculo_en_B"] = True
            print("Obstaculo inesperado detectado en B. Replanificando...")

            # Intentamos replanificar con el nuevo estado
            nuevo_plan = planificar(estado_actual, objetivo, acciones)
            if nuevo_plan:
                print("Nuevo plan generado:", nuevo_plan)
                return
            else:
                print("No se pudo replanificar. Fin del intento.")
                return
        else:
            for accion in acciones:
                if accion["nombre"] == paso:
                    if verificar_precondiciones(estado_actual, accion["precondiciones"]):
                        estado_actual = aplicar_efectos(estado_actual, accion["efectos"])
                        print("Accion ejecutada con exito.")
                    else:
                        print("Fallo al ejecutar accion:", paso)
                        return

    print("Plan ejecutado completamente.")

# Ejecutamos todo el proceso
ejecutar_plan_con_vigilancia(estado_inicial, estado_objetivo, acciones)
