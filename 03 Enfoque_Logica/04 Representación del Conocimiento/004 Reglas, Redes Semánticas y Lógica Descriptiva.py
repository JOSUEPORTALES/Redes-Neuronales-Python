# Clase para representar un nodo de la red semántica
class NodoConcepto:
    def __init__(self, nombre):
        self.nombre = nombre              # Nombre del concepto, por ejemplo "gato"
        self.propiedades = {}            # Propiedades como "tiene_pelos": True
        self.relaciones = {}             # Relaciones como "es_un": "animal"

    # Agregar una propiedad al concepto
    def agregar_propiedad(self, propiedad, valor):
        self.propiedades[propiedad] = valor

    # Agregar una relacion con otro concepto
    def agregar_relacion(self, tipo_relacion, objetivo):
        self.relaciones[tipo_relacion] = objetivo

    # Mostrar la informacion del concepto
    def mostrar_info(self):
        print(f"\n🔹 Concepto: {self.nombre}")
        print("  Propiedades:")
        for prop, val in self.propiedades.items():
            print(f"    - {prop}: {val}")
        print("  Relaciones:")
        for tipo, obj in self.relaciones.items():
            print(f"    - {tipo} → {obj}")

# Creamos una red semántica simple
# Creamos nodos (conceptos)
gato = NodoConcepto("gato")
animal = NodoConcepto("animal")
ser_vivo = NodoConcepto("ser vivo")

# Definimos propiedades y relaciones
gato.agregar_propiedad("tiene_pelos", True)
gato.agregar_relacion("es_un", "animal")

animal.agregar_propiedad("puede_moverse", True)
animal.agregar_relacion("es_un", "ser vivo")

ser_vivo.agregar_propiedad("necesita_energia", True)

# Función para aplicar una regla de inferencia simple
# Regla: Si un concepto "A" es un "B", y "B" tiene una propiedad, entonces "A" también la hereda.
def aplicar_herencia_propiedades(conceptos):
    print("\n Aplicando reglas de herencia lógica...")
    for concepto in conceptos:
        relaciones = concepto.relaciones
        if "es_un" in relaciones:
            padre = relaciones["es_un"]
            # Buscamos el nodo padre en la lista
            for otro in conceptos:
                if otro.nombre == padre:
                    for prop, val in otro.propiedades.items():
                        if prop not in concepto.propiedades:
                            concepto.propiedades[prop] = val
                            print(f" '{concepto.nombre}' hereda '{prop}: {val}' de '{padre}'")

# Lista de todos los conceptos
conceptos = [gato, animal, ser_vivo]

# Mostrar informacion antes de aplicar reglas
print("\nInformación antes de aplicar reglas:")
for c in conceptos:
    c.mostrar_info()

# Aplicamos la regla de herencia de propiedades
aplicar_herencia_propiedades(conceptos)

# Mostrar informacion después de aplicar reglas
print("\n Información después de aplicar reglas:")
for c in conceptos:
    c.mostrar_info()
