# Clase que representa una accion con sus precondiciones y efectos
class Accion:
    def __init__(self, nombre, precondiciones, efectos):
        self.nombre = nombre
        self.precondiciones = set(precondiciones)
        self.efectos = set(efectos)

# Función que determina si una accion puede ser aplicada en el estado actual
def accion_aplicable(accion, estado_actual):
    return accion.precondiciones.issubset(estado_actual)

# Funcion principal que realiza una planificación de orden parcial simple
def planificacion_orden_parcial(acciones, estado_inicial, objetivos):
    estado = estado_inicial.copy()
    plan = []
    acciones_pendientes = acciones.copy()

    while not objetivos.issubset(estado):
        progreso = False
        for accion in acciones_pendientes:
            if accion_aplicable(accion, estado):
                # Aplicamos la accion
                print(f"Ejecutando: {accion.nombre}")
                estado |= accion.efectos
                plan.append(accion.nombre)
                acciones_pendientes.remove(accion)
                progreso = True
                break
        if not progreso:
            print("No se puede continuar con la planificación. Faltan precondiciones.")
            return None

    return plan

# Estado inicial: el usuario no tiene nada listo
estado_inicial = set()

# Objetivo: sándwich preparado
objetivos = {"sandwich_preparado"}

# Lista de acciones disponibles (sin orden específico)
acciones = [
    Accion(
        nombre="sacar_pan",
        precondiciones=set(),
        efectos={"pan_listo"}
    ),
    Accion(
        nombre="sacar_jamon",
        precondiciones=set(),
        efectos={"jamon_listo"}
    ),
    Accion(
        nombre="poner_jamon_en_pan",
        precondiciones={"pan_listo", "jamon_listo"},
        efectos={"sandwich_preparado"}
    )
]

# Ejecutar la planificación
plan = planificacion_orden_parcial(acciones, estado_inicial, objetivos)

# Mostrar resultado
if plan:
    print("\nPlan generado:")
    for paso in plan:
        print("-", paso)
else:
    print("\nNo fue posible generar un plan.")
