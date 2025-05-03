# Creamos una clase para representar una Categoria general
class Categoria:
    def __init__(self, nombre):
        self.nombre = nombre
        self.subcategorias = []
        self.objetos = []

    # Metodo para agregar una subcategoria
    def agregar_subcategoria(self, subcategoria):
        self.subcategorias.append(subcategoria)

    # Metodo para agregar un objeto a esta categoria
    def agregar_objeto(self, objeto):
        self.objetos.append(objeto)

    # Metodo para mostrar la estructura jerarquica
    def mostrar_taxonomia(self, nivel=0):
        sangria = "  " * nivel  # sangría visual para representar jerarquia
        print(f"{sangria}- {self.nombre}")
        for objeto in self.objetos:
            print(f"{sangria}  • {objeto}")
        for subcat in self.subcategorias:
            subcat.mostrar_taxonomia(nivel + 1)

# Creamos categorias generales
animal = Categoria("Animal")
vegetal = Categoria("Vegetal")

# Subcategorias de Animal
mamifero = Categoria("Mamifero")
ave = Categoria("Ave")
animal.agregar_subcategoria(mamifero)
animal.agregar_subcategoria(ave)

# Objetos dentro de las subcategorias
mamifero.agregar_objeto("Perro")
mamifero.agregar_objeto("Gato")
ave.agregar_objeto("Aguila")
ave.agregar_objeto("Paloma")

# Subcategoria de Vegetal
fruta = Categoria("Fruta")
vegetal.agregar_subcategoria(fruta)
fruta.agregar_objeto("Manzana")
fruta.agregar_objeto("Banano")

# Mostramos toda la taxonomia
print("📚 Taxonomia de categorias y objetos:")
animal.mostrar_taxonomia()
vegetal.mostrar_taxonomia()
