# Definimos un conjunto de estudiantes con propiedades
estudiantes = [
    {"nombre": "Ana", "edad": 20, "tiene_beca": True},
    {"nombre": "Luis", "edad": 22, "tiene_beca": True},
    {"nombre": "Carlos", "edad": 21, "tiene_beca": True}
]

# Definimos una lista de propiedades (predicados) como funciones
def es_mayor_de_edad(estudiante):
    return estudiante["edad"] >= 18

def tiene_beca(estudiante):
    return estudiante["tiene_beca"]

def nombre_empieza_con_a(estudiante):
    return estudiante["nombre"].startswith("A")

# Lista de propiedades que probaremos
propiedades = [es_mayor_de_edad, tiene_beca, nombre_empieza_con_a]

# Funcion que simula la cuantificacion ∃P ∀x (P(x)) usando programación
def existe_una_propiedad_que_cumplen_todos(estudiantes, propiedades):
    for propiedad in propiedades:
        if all(propiedad(estudiante) for estudiante in estudiantes):
            return propiedad  # Devolvemos la propiedad que cumple la condicion
    return None

# Ejecutamos la simulacion
propiedad_cumplida = existe_una_propiedad_que_cumplen_todos(estudiantes, propiedades)

# Mostramos los resultados
print("🧾 Evaluando propiedades sobre estudiantes...\n")
for estudiante in estudiantes:
    print(f"- {estudiante}")

print("\n🔍 Buscando una propiedad que todos cumplen...")

if propiedad_cumplida:
    print(f"\n✅ Todos los estudiantes cumplen la propiedad: {propiedad_cumplida.__name__}")
else:
    print("\n❌ No existe una propiedad en la lista que todos los estudiantes cumplan.")
