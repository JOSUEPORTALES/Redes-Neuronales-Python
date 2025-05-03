# Ejemplo simple de conjuntos difusos

# Funcion de pertenencia difusa para temperatura "caliente"
def pertenencia_caliente(temperatura):
    if temperatura <= 20:
        return 0.0  # no es caliente
    elif temperatura >= 30:
        return 1.0  # totalmente caliente
    else:
        # entre 20 y 30 la pertenencia aumenta linealmente
        return (temperatura - 20) / 10

# Probar con diferentes temperaturas
temperaturas = [15, 22, 25, 28, 35]

print("Conjunto difuso: Caliente")
for t in temperaturas:
    print(f"Temperatura {t}° tiene pertenencia: {pertenencia_caliente(t):.2f}")


# Inferencia difusa basada en una regla simple

# Funcion de pertenencia para velocidad del ventilador segun temperatura caliente
def velocidad_ventilador(temperatura):
    grado_calor = pertenencia_caliente(temperatura)  # reutilizamos la funcion anterior
    # Suponemos que la velocidad es proporcional al grado de calor
    velocidad = grado_calor * 100  # 0 a 100%
    return velocidad

print("\nInferencia difusa para velocidad del ventilador:")
for t in temperaturas:
    velocidad = velocidad_ventilador(t)
    print(f"Temperatura {t}° -> velocidad ventilador: {velocidad:.1f}%")


# Simulacion simple de una regla fuzzy tipo CLIPS

# Funcion de pertenencia difusa para "humedad alta"
def pertenencia_humedad_alta(humedad):
    if humedad <= 40:
        return 0.0
    elif humedad >= 80:
        return 1.0
    else:
        return (humedad - 40) / 40

# Simulacion de regla fuzzy:
# SI temperatura ES caliente Y humedad ES alta ENTONCES ventilador fuerte

def regla_fuzzy(temperatura, humedad):
    grado_calor = pertenencia_caliente(temperatura)
    grado_humedad = pertenencia_humedad_alta(humedad)

    # Usamos el operador AND (minimo) para la inferencia difusa
    grado_regla = min(grado_calor, grado_humedad)

    # El resultado afecta la intensidad del ventilador
    intensidad = grado_regla * 100  # porcentaje
    return intensidad

# Probar con varios casos
casos = [(25, 50), (28, 85), (22, 70), (30, 90)]

print("\nSimulacion Fuzzy CLIPS (regla difusa combinada):")
for temp, hum in casos:
    intensidad = regla_fuzzy(temp, hum)
    print(f"Temp: {temp}°, Humedad: {hum}% -> Ventilador: {intensidad:.1f}%")
