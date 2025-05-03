# Base de conocimiento inicial
base_conocimiento = {
    "es_pajaro": ["tucan", "pingüino", "sparrow"],
    "puede_volar": ["tucan", "sparrow"],  # Por defecto asumimos que pueden volar
}

# Funcion que determina si un animal puede volar, usando lógica por defecto
def puede_volar(animal, base):
    # Si el animal está en la lista de "puede_volar", asumimos que puede volar
    if animal in base["puede_volar"]:
        return True
    # Si el animal es un pájaro, pero no está explícitamente en la lista de "puede_volar", 
    # asumimos que **por defecto** puede volar.
    elif animal in base["es_pajaro"]:
        return True
    else:
        return False

# Evaluamos antes de modificar las excepciones
print("🧠 Conocimiento inicial (por defecto):")
for animal in base_conocimiento["es_pajaro"]:
    resultado = puede_volar(animal, base_conocimiento)
    print(f"¿Puede volar {animal}? {'Sí' if resultado else 'No'}")

# Ahora agregamos una excepción, por ejemplo: los pingüinos no pueden volar
def actualizar_conocimiento_para_excepciones(base):
    if "pingüino" in base["puede_volar"]:
        base["puede_volar"].remove("pingüino")  # Eliminamos el pingüino de la lista
    base["no_puede_volar"] = ["pingüino"]  # Establecemos la excepción: el pingüino no vuela

# Aplicamos la actualización
actualizar_conocimiento_para_excepciones(base_conocimiento)

# Evaluamos después de agregar la excepción para el pingüino
print("\n🔄 Conocimiento actualizado (con excepción para pingüinos):")
for animal in base_conocimiento["es_pajaro"]:
    resultado = puede_volar(animal, base_conocimiento)
    print(f"¿Puede volar {animal}? {'Sí' if resultado else 'No'}")
