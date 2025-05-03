# Creamos una clase que representa un marco general (una situacion o evento)
class Marco:
    def __init__(self, nombre, ranuras):
        self.nombre = nombre              # Nombre del marco, como "visita_restaurante"
        self.ranuras = ranuras            # Diccionario con ranuras y valores

    # Metodo para actualizar una ranura (atributo del marco)
    def actualizar_ranura(self, clave, valor):
        self.ranuras[clave] = valor

    # Metodo para mostrar el contenido del marco
    def mostrar(self):
        print(f"🔹 Marco: {self.nombre}")
        for clave, valor in self.ranuras.items():
            print(f"  - {clave}: {valor}")
        print()

# Creamos un marco para una situacion comun: visitar un restaurante
marco_restaurante = Marco("visita_restaurante", {
    "lugar": "restaurante",
    "cliente": "persona",
    "mesero": "persona",
    "acciones": ["entrar", "ordenar", "comer", "pagar", "salir"],
    "menu": ["hamburguesa", "ensalada", "agua"]
})

# Mostramos el marco
marco_restaurante.mostrar()

# Simulamos una instancia del marco con valores concretos
print("🔸 Simulacion de un evento real con este marco:")
marco_restaurante.actualizar_ranura("cliente", "Ana")
marco_restaurante.actualizar_ranura("mesero", "Carlos")
marco_restaurante.actualizar_ranura("orden", "hamburguesa y agua")

# Agregamos una nueva accion a la lista de acciones realizadas
marco_restaurante.ranuras["acciones"].append("dejar_propina")

# Mostramos nuevamente el marco actualizado con la situacion especifica
marco_restaurante.mostrar()
