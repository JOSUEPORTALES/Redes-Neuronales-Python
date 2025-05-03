# Creamos una clase para manejar una base de conocimientos simple
class BaseConocimiento:
    def __init__(self):
        # Lista de hechos conocidos (predicados como strings)
        self.hechos = set()

    def agregar_hecho(self, hecho):
        # Agrega un nuevo hecho si no está ya presente
        self.hechos.add(hecho)

    def tiene_hecho(self, hecho):
        # Verifica si un hecho ya está en la base
        return hecho in self.hechos

    def mostrar_hechos(self):
        # Imprime todos los hechos conocidos
        print("📚 Hechos en la base de conocimiento:")
        for hecho in sorted(self.hechos):
            print(f"- {hecho}")

# Función para aplicar reglas de inferencia
def aplicar_reglas(base):
    nuevos_hechos = set()

    # Recorremos los hechos para aplicar una regla lógica:
    # Si una persona es estudiante y estudia IA, entonces es aprendiz_IA
    for hecho1 in base.hechos:
        if hecho1.startswith("es_estudiante("):
            # Extraemos el nombre de la persona
            persona = hecho1[len("es_estudiante("):-1]

            # Creamos el hecho correspondiente que buscamos para completar la regla
            hecho2 = f"estudia_ia({persona})"

            # Si también existe este hecho, inferimos uno nuevo
            if base.tiene_hecho(hecho2):
                nuevo_hecho = f"es_aprendiz_ia({persona})"
                nuevos_hechos.add(nuevo_hecho)

    # Agregamos todos los nuevos hechos inferidos
    for nuevo in nuevos_hechos:
        if not base.tiene_hecho(nuevo):
            print(f"🔍 Regla aplicada: Se ha inferido -> {nuevo}")
            base.agregar_hecho(nuevo)

# Creamos la base de conocimiento
base = BaseConocimiento()

# Agregamos algunos hechos (representación de conocimiento experto)
base.agregar_hecho("es_estudiante(juan)")
base.agregar_hecho("es_estudiante(maria)")
base.agregar_hecho("estudia_ia(juan)")
base.agregar_hecho("estudia_ia(luis)")  # Luis estudia IA, pero no sabemos si es estudiante

# Mostramos los hechos actuales
base.mostrar_hechos()

# Aplicamos reglas para inferir nuevos hechos
aplicar_reglas(base)

# Mostramos los hechos luego de la inferencia
print("\n📘 Hechos luego de aplicar reglas:")
base.mostrar_hechos()
