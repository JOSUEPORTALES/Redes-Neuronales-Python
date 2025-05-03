# Definimos una funcion de encadenamiento hacia adelante
def encadenamiento_adelante(hechos, reglas):
    nuevos = True
    while nuevos:
        nuevos = False
        for antecedente, consecuente in reglas:
            if antecedente in hechos and consecuente not in hechos:
                hechos.add(consecuente)
                print(f"[Hacia adelante] Se deduce: {consecuente}")
                nuevos = True
    return hechos

# Definimos una funcion de encadenamiento hacia atras
def encadenamiento_atras(meta, hechos, reglas):
    if meta in hechos:
        print(f"[Hacia atras] {meta} ya es un hecho.")
        return True
    for antecedente, consecuente in reglas:
        if consecuente == meta:
            print(f"[Hacia atras] Para demostrar {meta}, se necesita demostrar {antecedente}")
            if encadenamiento_atras(antecedente, hechos, reglas):
                hechos.add(meta)
                print(f"[Hacia atras] Se demuestra: {meta}")
                return True
    print(f"[Hacia atras] No se puede demostrar {meta}")
    return False

# --------------------------
# Hechos conocidos inicialmente
hechos = set(["llueve"])

# Reglas del tipo (si A entonces B)
# Representadas como tuplas: (antecedente, consecuente)
reglas = [
    ("llueve", "suelo mojado"),
    ("suelo mojado", "hay charcos"),
    ("hay charcos", "se moja la ropa")
]

# Ejemplo 1: Encadenamiento hacia adelante
print("\n--- Encadenamiento hacia adelante ---")
hechos_deducidos = encadenamiento_adelante(set(hechos), reglas)

# Ejemplo 2: Encadenamiento hacia atras
print("\n--- Encadenamiento hacia atras ---")
meta = "se moja la ropa"
exito = encadenamiento_atras(meta, set(hechos), reglas)

if exito:
    print(f"✅ La meta '{meta}' fue demostrada.")
else:
    print(f"❌ No se pudo demostrar la meta '{meta}'.")
