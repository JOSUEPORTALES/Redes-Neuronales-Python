# Simulacion basica de logica modal
# Explicaremos las modalidades de "posible" (◇) y "necesario" (□)

# Creamos un entorno con diferentes mundos posibles
# Cada mundo tiene un conjunto de hechos verdaderos
mundos = {
    "mundo_1": {"llueve", "nublado"},
    "mundo_2": {"nublado"},
    "mundo_3": {"sol"},
}

# Funcion que simula la modalidad "posible"
# Devuelve True si en al menos un mundo el hecho es verdadero
def es_posible(hecho, mundos):
    for nombre, hechos in mundos.items():
        if hecho in hechos:
            return True
    return False

# Funcion que simula la modalidad "necesario"
# Devuelve True si en todos los mundos el hecho es verdadero
def es_necesario(hecho, mundos):
    for nombre, hechos in mundos.items():
        if hecho not in hechos:
            return False
    return True

# -----------------------------------
# EJEMPLOS DE USO

print("¿Es posible que llueva?")
print(es_posible("llueve", mundos))  # Debe ser True

print("\n¿Es necesario que este nublado?")
print(es_necesario("nublado", mundos))  # False, porque no todos los mundos tienen "nublado"

print("\n¿Es necesario que haya sol?")
print(es_necesario("sol", mundos))  # False

print("\n¿Es posible que haya sol?")
print(es_posible("sol", mundos))  # True
