# Lista de personas que representan nuestra base de conocimiento
personas = [
    {"nombre": "Ana", "es_humana": True, "es_mortal": True},
    {"nombre": "Luis", "es_humana": True, "es_mortal": True},
    {"nombre": "Robo", "es_humana": False, "es_mortal": False}
]

# Funcion que representa el cuantificador universal (∀)
# Verifica si TODOS los humanos son mortales
def todos_los_humanos_son_mortales(personas):
    for persona in personas:
        if persona["es_humana"] and not persona["es_mortal"]:
            return False  # Encontramos un humano que no es mortal
    return True  # Todos los humanos fueron mortales

# Funcion que representa el cuantificador existencial (∃)
# Verifica si existe al menos un humano en la lista
def existe_un_humano(personas):
    for persona in personas:
        if persona["es_humana"]:
            return True  # Encontramos al menos un humano
    return False  # No hay ningun humano

# ----------------------------------
# Ejecucion del programa

# Verificamos si todos los humanos son mortales
resultado_universal = todos_los_humanos_son_mortales(personas)
print("¿Todos los humanos son mortales?", resultado_universal)

# Verificamos si existe al menos un humano
resultado_existencial = existe_un_humano(personas)
print("¿Existe al menos un humano?", resultado_existencial)
