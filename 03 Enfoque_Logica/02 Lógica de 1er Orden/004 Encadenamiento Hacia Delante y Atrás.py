# Sistema de encadenamiento logico simple
# Las reglas y hechos se representan como listas de cadenas

# FUNCION: ENCANDENAMIENTO HACIA ADELANTE
def encadenamiento_adelante(reglas, hechos, meta):
    hechos = set(hechos)  # Convertimos los hechos a un conjunto para acceso rapido

    while True:
        nuevos = set()
        for antecedente, consecuente in reglas:
            # Si todos los antecedentes estan en los hechos actuales
            if all(premisa in hechos for premisa in antecedente):
                if consecuente not in hechos:
                    nuevos.add(consecuente)
        # Si no hay hechos nuevos, terminamos
        if not nuevos:
            break
        hechos.update(nuevos)  # Agregamos los nuevos hechos
        if meta in hechos:
            return True
    return meta in hechos

# FUNCION: ENCANDENAMIENTO HACIA ATRAS
def encadenamiento_atras(reglas, hechos, meta):
    if meta in hechos:
        return True

    # Buscamos reglas que produzcan la meta
    for antecedente, consecuente in reglas:
        if consecuente == meta:
            # Verificamos que todos los antecedentes puedan probarse
            if all(encadenamiento_atras(reglas, hechos, submeta) for submeta in antecedente):
                return True
    return False

# ---------------------------
# DATOS DE EJEMPLO

# Conjunto de hechos conocidos
hechos = ["llueve", "tengo_paraguas"]

# Conjunto de reglas representadas como: ([premisas], conclusion)
reglas = [
    (["llueve", "tengo_paraguas"], "no_me_mojo"),
    (["no_me_mojo"], "estoy_feliz"),
]

# Meta deseada: ¿puedo estar feliz?
meta = "estoy_feliz"

# ---------------------------
# PRUEBA DE ENCANDENAMIENTO HACIA ADELANTE
print("Encadenamiento hacia adelante:")
if encadenamiento_adelante(reglas, hechos, meta):
    print(f"✓ Se puede probar que '{meta}' es verdadero.")
else:
    print(f"✗ No se pudo probar que '{meta}' es verdadero.")

# ---------------------------
# PRUEBA DE ENCANDENAMIENTO HACIA ATRAS
print("\nEncadenamiento hacia atras:")
if encadenamiento_atras(reglas, hechos, meta):
    print(f"✓ Se puede probar que '{meta}' es verdadero.")
else:
    print(f"✗ No se pudo probar que '{meta}' es verdadero.")
