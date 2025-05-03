# Base de conocimiento con hechos y reglas
base_conocimiento = {
    "es_pajaro": ["tucan", "pingüino"],
    "puede_volar": ["tucan"]
}

# Funcion para inferir si un animal puede volar, basandonos en reglas actuales
def puede_volar(animal, base):
    # Si el animal esta en la lista de los que pueden volar, devolvemos True
    if animal in base["puede_volar"]:
        return True
    # Si el animal es un pajaro pero no esta en la lista de vuelo, asumimos que puede volar
    elif animal in base["es_pajaro"]:
        return True
    else:
        return False

# Evaluamos antes de agregar nueva informacion
print("🧠 Conocimiento inicial:")
for animal in base_conocimiento["es_pajaro"]:
    resultado = puede_volar(animal, base_conocimiento)
    print(f"¿Puede volar {animal}? {'Sí' if resultado else 'No'}")

# Ahora agregamos nueva informacion que cambia nuestras conclusiones
# Añadimos una regla de excepcion: los pinguinos no pueden volar
def actualizar_conocimiento_para_excepciones(base):
    if "pingüino" in base["puede_volar"]:
        base["puede_volar"].remove("pingüino")  # eliminamos si estaba ahi
    base["no_puede_volar"] = ["pingüino"]  # nueva regla: pinguino no vuela

# Aplicamos la actualizacion
actualizar_conocimiento_para_excepciones(base_conocimiento)

# Funcion actualizada para manejar excepciones
def puede_volar_con_excepciones(animal, base):
    if "no_puede_volar" in base and animal in base["no_puede_volar"]:
        return False
    return puede_volar(animal, base)

# Evaluamos despues de agregar excepciones
print("\n🔄 Conocimiento actualizado con excepciones:")
for animal in base_conocimiento["es_pajaro"]:
    resultado = puede_volar_con_excepciones(animal, base_conocimiento)
    print(f"¿Puede volar {animal}? {'Sí' if resultado else 'No'}")
