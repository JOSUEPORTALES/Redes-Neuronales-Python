# Definimos una clase para representar un Agente que tiene creencias
class Agente:
    def __init__(self, nombre):
        self.nombre = nombre                    # Nombre del agente, por ejemplo: "juan"
        self.creencias = {}                     # Diccionario que almacena sus creencias

    # Metodo para agregar una creencia al agente
    def agregar_creencia(self, hecho, valor):
        self.creencias[hecho] = valor

    # Metodo para mostrar todas las creencias actuales del agente
    def mostrar_creencias(self):
        print(f"\n Creencias de {self.nombre.capitalize()}:")
        if not self.creencias:
            print("   No tiene creencias registradas.")
        for hecho, valor in self.creencias.items():
            print(f"   Cree que '{hecho}' es {valor}")

    # Metodo para actualizar una creencia, por ejemplo si recibe nueva informacion
    def actualizar_creencia(self, hecho, nuevo_valor):
        if hecho in self.creencias:
            print(f" Actualizando creencia sobre '{hecho}' para {self.nombre}")
        else:
            print(f" Agregando nueva creencia sobre '{hecho}' para {self.nombre}")
        self.creencias[hecho] = nuevo_valor

    # Metodo para eliminar una creencia si el agente deja de creer en algo
    def eliminar_creencia(self, hecho):
        if hecho in self.creencias:
            print(f" Eliminando creencia: '{hecho}' de {self.nombre}")
            del self.creencias[hecho]

# --- Ejemplo práctico: Un agente llamado juan y sus creencias ---

# Creamos un agente
juan = Agente("juan")

# Juan cree inicialmente que 'el cielo es azul' y que 'los gatos pueden volar'
juan.agregar_creencia("el cielo es azul", True)
juan.agregar_creencia("los gatos pueden volar", True)

# Mostramos sus creencias iniciales
juan.mostrar_creencias()

# Juan recibe nueva informacion: los gatos no pueden volar
juan.actualizar_creencia("los gatos pueden volar", False)

# Juan deja de tener una opinion sobre 'el cielo es azul'
juan.eliminar_creencia("el cielo es azul")

# Mostramos sus creencias finales
juan.mostrar_creencias()
