# Creamos una clase para representar un concepto en la ontologia
class Concepto:
    def __init__(self, nombre):
        self.nombre = nombre                    # Nombre del concepto, por ejemplo: "Gato"
        self.propiedades = {}                  # Diccionario de propiedades como {"color": "gris"}
        self.subclases = []                    # Lista de conceptos hijos (subclases)
        self.superclase = None                 # Referencia al concepto padre (superclase)

    # Asignamos una propiedad al concepto
    def agregar_propiedad(self, clave, valor):
        self.propiedades[clave] = valor

    # Asignamos la relacion de herencia (subclase)
    def establecer_superclase(self, padre):
        self.superclase = padre
        padre.subclases.append(self)

    # Mostramos toda la informacion del concepto
    def mostrar_info(self):
        print(f" Concepto: {self.nombre}")
        if self.superclase:
            print(f"   Es un tipo de: {self.superclase.nombre}")
        if self.propiedades:
            print("   Propiedades:")
            for clave, valor in self.propiedades.items():
                print(f"     - {clave}: {valor}")
        if self.subclases:
            print("   Subclases:")
            for sub in self.subclases:
                print(f"     - {sub.nombre}")
        print()

# --- Ejemplo práctico: Ontología de animales ---

# Creamos los conceptos principales
animal = Concepto("Animal")
mamifero = Concepto("Mamifero")
ave = Concepto("Ave")

# Establecemos jerarquia: mamifero y ave son animales
mamifero.establecer_superclase(animal)
ave.establecer_superclase(animal)

# Creamos ejemplos concretos
gato = Concepto("Gato")
pingüino = Concepto("Pinguino")

# Definimos jerarquia: gato es un mamifero, pinguino es un ave
gato.establecer_superclase(mamifero)
pingüino.establecer_superclase(ave)

# Agregamos propiedades específicas
gato.agregar_propiedad("numero_de_patas", 4)
gato.agregar_propiedad("sonido", "maulla")

pingüino.agregar_propiedad("numero_de_patas", 2)
pingüino.agregar_propiedad("puede_volar", False)

# Mostramos la ontología
print(" Ontología del dominio 'Animales':\n")
animal.mostrar_info()
mamifero.mostrar_info()
ave.mostrar_info()
gato.mostrar_info()
pingüino.mostrar_info()
