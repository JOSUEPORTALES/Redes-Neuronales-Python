# Simulacion sencilla de logica temporal
# Supondremos una secuencia de estados en el tiempo (pasado y futuro)

# Lista que representa el clima en diferentes momentos (de pasado a futuro)
# Cada elemento es un conjunto de condiciones verdaderas en ese tiempo
# Tiempo 0: pasado, Tiempo 3: futuro
tiempo = [
    {"llueve"},                # tiempo 0
    {"nublado"},               # tiempo 1
    {"sol"},                   # tiempo 2
    {"nublado", "sol"},        # tiempo 3
]

# Funcion: fue_verdadero (Pasado)
# Verifica si un hecho fue verdadero en algun momento anterior
def fue_verdadero(hecho, tiempo_actual, linea_tiempo):
    for t in range(0, tiempo_actual):
        if hecho in linea_tiempo[t]:
            return True
    return False

# Funcion: sera_verdadero (Futuro)
# Verifica si un hecho sera verdadero en algun momento despues del actual
def sera_verdadero(hecho, tiempo_actual, linea_tiempo):
    for t in range(tiempo_actual + 1, len(linea_tiempo)):
        if hecho in linea_tiempo[t]:
            return True
    return False

# Funcion: siempre_futuro (Siempre G)
# Verifica si el hecho sera siempre verdadero desde ahora en adelante
def siempre_futuro(hecho, tiempo_actual, linea_tiempo):
    for t in range(tiempo_actual, len(linea_tiempo)):
        if hecho not in linea_tiempo[t]:
            return False
    return True

# Funcion: siguiente (X)
# Verifica si un hecho sera verdad en el siguiente tiempo
def siguiente(hecho, tiempo_actual, linea_tiempo):
    if tiempo_actual + 1 < len(linea_tiempo):
        return hecho in linea_tiempo[tiempo_actual + 1]
    return False

# -----------------------------------
# EJEMPLOS DE USO

tiempo_actual = 1  # estamos en el tiempo 1 (nublado)

print("¿Fue llueve verdadero en el pasado?")
print(fue_verdadero("llueve", tiempo_actual, tiempo))  # True

print("\n¿Sera sol verdadero en el futuro?")
print(sera_verdadero("sol", tiempo_actual, tiempo))  # True

print("\n¿Sera nublado siempre verdadero desde ahora?")
print(siempre_futuro("nublado", tiempo_actual, tiempo))  # True

print("\n¿Sera sol verdadero en el siguiente momento?")
print(siguiente("sol", tiempo_actual, tiempo))  # True
