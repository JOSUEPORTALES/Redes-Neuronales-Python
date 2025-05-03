# Definimos una tarea que puede ser primitiva (accion ejecutable) o compuesta (necesita descomposición)
class Tarea:
    def __init__(self, nombre, subtareas=None):
        self.nombre = nombre
        # Si no hay subtareas, es una tarea primitiva
        self.subtareas = subtareas or []

# Funcion que realiza la descomposicion de una tarea jerarquica
def ejecutar_tarea(tarea):
    if not tarea.subtareas:
        # Si no hay subtareas, es una tarea primitiva y se ejecuta directamente
        print(f"Ejecutando tarea: {tarea.nombre}")
    else:
        # Si hay subtareas, se descompone en partes más simples
        print(f"Descomponiendo tarea: {tarea.nombre}")
        for subtarea in tarea.subtareas:
            ejecutar_tarea(subtarea)

# Ejemplo: organizar una fiesta

# Subtareas para comprar comida
comprar_comida = Tarea("comprar comida", [
    Tarea("hacer lista del supermercado"),
    Tarea("ir al supermercado"),
    Tarea("comprar bebidas"),
    Tarea("comprar botanas")
])

# Subtareas para limpiar la casa
limpiar_casa = Tarea("limpiar la casa", [
    Tarea("barrer"),
    Tarea("trapear"),
    Tarea("limpiar baño")
])

# Subtareas para invitar amigos
invitar_amigos = Tarea("invitar amigos", [
    Tarea("escribir mensajes"),
    Tarea("enviar mensajes")
])

# Tarea principal
organizar_fiesta = Tarea("organizar fiesta", [
    comprar_comida,
    limpiar_casa,
    invitar_amigos
])

# Ejecutamos la tarea principal, que se descompone en subtareas
ejecutar_tarea(organizar_fiesta)
