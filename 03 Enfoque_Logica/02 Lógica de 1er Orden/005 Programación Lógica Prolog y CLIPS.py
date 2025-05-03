# Creamos una clase para representar la base de conocimiento
class BaseConocimiento:
    def __init__(self):
        # Diccionario donde cada clave es un predicado y su valor es una lista de tuplas con argumentos
        self.hechos = {
            "es_padre": [],
            "es_madre": []
        }

    def agregar_hecho(self, predicado, argumento1, argumento2):
        # Agrega un hecho a la base de conocimiento
        if (argumento1, argumento2) not in self.hechos[predicado]:
            self.hechos[predicado].append((argumento1, argumento2))

    def consultar(self, predicado, argumento1=None, argumento2=None):
        # Consulta hechos según el predicado y argumentos opcionales
        resultados = []
        for a1, a2 in self.hechos.get(predicado, []):
            if (argumento1 is None or a1 == argumento1) and (argumento2 is None or a2 == argumento2):
                resultados.append((a1, a2))
        return resultados

# Función para deducir abuelos: si A es padre de B y B es padre o madre de C => A es abuelo/a de C
def deducir_abuelos(base):
    abuelos = set()
    for padre, hijo in base.consultar("es_padre"):
        for padre2, nieto in base.consultar("es_padre"):
            if padre2 == hijo:
                abuelos.add((padre, nieto))
        for madre2, nieto in base.consultar("es_madre"):
            if madre2 == hijo:
                abuelos.add((padre, nieto))
    return abuelos

# Creamos la base de conocimiento
base = BaseConocimiento()

# Agregamos hechos de ejemplo
base.agregar_hecho("es_padre", "carlos", "juan")
base.agregar_hecho("es_padre", "juan", "pedro")
base.agregar_hecho("es_madre", "ana", "pedro")
base.agregar_hecho("es_padre", "carlos", "laura")
base.agregar_hecho("es_madre", "laura", "sofia")

# Mostramos todos los hechos
print(" Hechos en la base de conocimiento:")
for predicado in base.hechos:
    for a1, a2 in base.hechos[predicado]:
        print(f"- {predicado}({a1}, {a2})")

# Aplicamos la regla para deducir quién es abuelo
abuelos = deducir_abuelos(base)

# Mostramos los abuelos deducidos
print("\n Deducciones: Relaciones de abuelo")
for abuelo, nieto in abuelos:
    print(f"- {abuelo} es abuelo de {nieto}")
