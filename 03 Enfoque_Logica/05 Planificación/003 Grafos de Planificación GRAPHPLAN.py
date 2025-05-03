# Definimos el estado del mundo en términos de predicados
# Estos son los estados iniciales y objetivos de los predicados
estado_inicial = {
    "en(caja, A)",  # La caja está en A
    "no_en(caja, B)" # La caja no está en B
}

estado_objetivo = {
    "en(caja, B)"  # Queremos que la caja esté en B
}

# Acciones posibles
acciones = [
    {
        "nombre": "recoger_caja",  # Acción de recoger la caja
        "precondiciones": {"en(caja, A)"},  # La caja debe estar en A
        "efectos": {"no_en(caja, A)", "en(caja, B)"}  # Después de la acción, la caja estará en B
    },
    {
        "nombre": "dejar_caja",  # Acción de dejar la caja
        "precondiciones": {"en(caja, B)"},
        "efectos": {"no_en(caja, B)", "en(caja, A)"}
    }
]

# Función que verifica si las precondiciones de una acción son satisfechas en un estado dado
def precondiciones_satisfechas(estado, accion):
    return accion["precondiciones"].issubset(estado)

# Función para aplicar una acción a un estado, generando un nuevo estado
def aplicar_accion(estado, accion):
    if precondiciones_satisfechas(estado, accion):
        # Se aplican los efectos de la acción
        nuevo_estado = estado.copy()
        nuevo_estado.update(accion["efectos"])
        return nuevo_estado
    return None

# Función de búsqueda de planificación, utilizando GRAPHPLAN
def planificar(estado_inicial, estado_objetivo, acciones):
    nivel = 0  # Inicializamos el primer nivel
    plan = []  # El plan final
    estados = [estado_inicial]  # Estado actual
    while estados:
        nivel += 1
        nuevos_estados = []  # Para almacenar nuevos estados
        for estado in estados:
            if estado_objetivo.issubset(estado):  # Si hemos alcanzado el objetivo, hemos terminado
                return plan
            for accion in acciones:
                # Aplicamos la acción si es posible
                nuevo_estado = aplicar_accion(estado, accion)
                if nuevo_estado:
                    nuevos_estados.append(nuevo_estado)
                    plan.append(accion["nombre"])  # Agregamos la acción al plan
        estados = nuevos_estados  # Actualizamos el conjunto de estados
    return None  # Si no encontramos solución

# Ejecutamos la planificación
plan_generado = planificar(estado_inicial, estado_objetivo, acciones)

# Mostramos el plan generado paso a paso
if plan_generado:
    print("Plan encontrado para alcanzar el objetivo:")
    for paso in plan_generado:
        print(paso)
else:
    print("No se pudo encontrar un plan.")
