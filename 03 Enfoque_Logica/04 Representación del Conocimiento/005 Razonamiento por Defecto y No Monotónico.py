# Creamos una clase para representar animales y su comportamiento por defecto
class Animal:
    def __init__(self, nombre, tipo):
        self.nombre = nombre          # Nombre del animal (ej: "piolin", "pingu")
        self.tipo = tipo              # Tipo de animal (ej: "ave", "murcielago")
        self.puede_volar = None       # No sabemos al principio si puede volar

    # Metodo para razonar si el animal puede volar segun su tipo
    def razonar_vuelo(self):
        # Razonamiento por defecto:
        if self.tipo == "ave":
            self.puede_volar = True   # Suponemos que todas las aves vuelan (por defecto)
        elif self.tipo == "murcielago":
            self.puede_volar = True   # Tambien los murcielagos
        else:
            self.puede_volar = False  # Por defecto, otros animales no vuelan

    # Metodo para anular el razonamiento por defecto (cuando hay excepcion)
    def anular_vuelo(self):
        self.puede_volar = False      # Cambiamos la conclusion si hay una excepcion

    # Metodo para mostrar informacion
    def mostrar(self):
        estado_vuelo = "si" if self.puede_volar else "no"
        print(f"{self.nombre} es un(a) {self.tipo} y {estado_vuelo} puede volar.")

# Creamos dos animales
ave_normal = Animal("piolin", "ave")
ave_rara = Animal("pingu", "ave")         # Es un pinguino

# Aplicamos el razonamiento por defecto
ave_normal.razonar_vuelo()
ave_rara.razonar_vuelo()

# Pero nos damos cuenta de que el pinguino no vuela (excepcion)
ave_rara.anular_vuelo()

# Mostramos los resultados
ave_normal.mostrar()
ave_rara.mostrar()
