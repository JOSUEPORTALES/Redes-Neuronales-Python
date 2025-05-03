# Definimos una base de hechos: sintomas observados en un paciente
hechos = {
    "tiene_fiebre": True,
    "tiene_tos": True,
    "tiene_dolor_garganta": True,
    "tiene_dolor_cabeza": False,
    "tiene_erupciones": False
}

# Reglas causales: si se cumple una causa, se puede deducir un efecto
reglas_causales = [
    {"causa": "tiene_gripe", "efectos": ["tiene_fiebre", "tiene_tos", "tiene_dolor_garganta"]},
    {"causa": "tiene_sarampion", "efectos": ["tiene_fiebre", "tiene_erupciones"]},
    {"causa": "tiene_resfriado", "efectos": ["tiene_tos", "tiene_dolor_garganta"]},
]

# Esta funcion revisa si una enfermedad puede ser la causa de los sintomas observados
def diagnosticar(hechos, reglas):
    posibles_diagnosticos = []

    # Recorremos todas las reglas
    for regla in reglas:
        efectos = regla["efectos"]
        # Verificamos si todos los efectos (sintomas) estan presentes en los hechos
        si_coincide = all(hechos.get(efecto, False) for efecto in efectos)
        if si_coincide:
            posibles_diagnosticos.append(regla["causa"])
    
    return posibles_diagnosticos

# Ejecutamos el razonamiento para obtener diagnosticos posibles
diagnosticos = diagnosticar(hechos, reglas_causales)

# Mostramos los resultados al usuario
print("✔ Hechos observados:")
for hecho, valor in hechos.items():
    if valor:
        print(f"- {hecho.replace('_', ' ')}")

print("\n🔎 Posibles diagnosticos segun los sintomas:")
for diagnostico in diagnosticos:
    print(f"- {diagnostico.replace('_', ' ')}")

# Si no hay diagnosticos posibles
if not diagnosticos:
    print("No se encontraron causas conocidas para los sintomas.")
