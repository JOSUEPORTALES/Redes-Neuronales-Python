class Accion:
    def __init__(self, nombre, precondiciones, efectos_agregar, efectos_eliminar):
        self.nombre = nombre
        self.precondiciones = set(precondiciones)
        self.efectos_agregar = set(efectos_agregar)
        self.efectos_eliminar = set(efectos_eliminar)

def precondiciones_satisfechas(accion, estado):
    return accion.precondiciones.issubset(estado)

def aplicar_accion(accion, estado):
    nuevo_estado = estado.copy()
    nuevo_estado -= accion.efectos_eliminar
    nuevo_estado |= accion.efectos_agregar
    return nuevo_estado

def planificar(estado_inicial, meta, acciones, pasos_maximos=20):
    estado = estado_inicial.copy()
    plan = []
    pasos = 0
    
    while not meta.issubset(estado):
        pasos += 1
        if pasos > pasos_maximos:
            print("Se ha alcanzado el limite de pasos. Posible bucle infinito.")
            return None
        
        accion_aplicada = False
        for accion in acciones:
            if precondiciones_satisfechas(accion, estado):
                nuevo_estado = aplicar_accion(accion, estado)
                if nuevo_estado != estado:
                    print(f"Aplicando accion: {accion.nombre}")
                    plan.append(accion.nombre)
                    estado = nuevo_estado
                    accion_aplicada = True
                    break
        if not accion_aplicada:
            print("No hay acciones aplicables. Plan fallido.")
            return None
    
    return plan

# Estado inicial
estado_inicial = {
    "robot_en_sala1",
    "caja_en_sala1",
    "manos_vacias"
}

# Meta
meta = {
    "caja_en_sala2"
}

# Acciones
acciones = [
    Accion(
        nombre="moverse_a_sala2",
        precondiciones={"robot_en_sala1"},
        efectos_agregar={"robot_en_sala2"},
        efectos_eliminar={"robot_en_sala1"}
    ),
    Accion(
        nombre="moverse_a_sala1",
        precondiciones={"robot_en_sala2"},
        efectos_agregar={"robot_en_sala1"},
        efectos_eliminar={"robot_en_sala2"}
    ),
    Accion(
        nombre="tomar_caja",
        precondiciones={"robot_en_sala1", "caja_en_sala1", "manos_vacias"},
        efectos_agregar={"robot_tiene_caja"},
        efectos_eliminar={"caja_en_sala1", "manos_vacias"}
    ),
    Accion(
        nombre="dejar_caja_en_sala2",
        precondiciones={"robot_en_sala2", "robot_tiene_caja"},
        efectos_agregar={"caja_en_sala2", "manos_vacias"},
        efectos_eliminar={"robot_tiene_caja"}
    )
]

# Ejecutar el planificador
plan = planificar(estado_inicial, meta, acciones)

# Mostrar resultado
if plan:
    print("\nPlan encontrado:")
    for paso in plan:
        print("-", paso)
else:
    print("\nNo se pudo encontrar un plan.")
