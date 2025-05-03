# Este programa trabaja con clausulas en Forma Normal Conjuntiva (FNC)
# y aplica la tecnica de resolucion para deducir si una conclusion es logica

# Definimos una funcion para aplicar la resolucion entre dos clausulas
def resolver(clausula1, clausula2):
    # Creamos una nueva lista para guardar los posibles resultados de resolucion
    resolventes = []

    # Recorremos cada literal de ambas clausulas
    for literal in clausula1:
        if f"¬{literal}" in clausula2:
            # Creamos una nueva clausula eliminando el literal y su negacion
            nueva = list(set(clausula1 + clausula2))
            nueva.remove(literal)
            nueva.remove(f"¬{literal}")
            resolventes.append(nueva)
        elif literal.startswith("¬") and literal[1:] in clausula2:
            nueva = list(set(clausula1 + clausula2))
            nueva.remove(literal)
            nueva.remove(literal[1:])
            resolventes.append(nueva)
    return resolventes

# Funcion principal para demostrar si se puede derivar la conclusion
def aplicar_resolucion():
    # Clausulas en Forma Normal Conjuntiva (lista de listas)
    # p: llueve, q: calle mojada

    # Base de conocimiento (premisas)
    base = [
        ["p"],           # Clausula 1: llueve
        ["¬p", "q"]      # Clausula 2: si llueve entonces calle mojada (¬p ∨ q)
    ]

    # Negamos la conclusion que queremos probar (¬q) para aplicar refutacion
    conclusion_negada = ["¬q"]
    base += [conclusion_negada]

    # Creamos un conjunto para guardar todas las clausulas
    clausulas = [clausula for clausula in base]

    print("Clausulas iniciales (FNC):")
    for c in clausulas:
        print(c)

    print("\n--- Aplicando resolucion ---")

    # Vamos generando nuevas clausulas por resolucion
    nuevas = []
    while True:
        n = len(clausulas)
        # Revisamos todas las combinaciones posibles de clausulas
        for i in range(n):
            for j in range(i+1, n):
                resolventes = resolver(clausulas[i], clausulas[j])
                for resolvente in resolventes:
                    if resolvente == []:
                        print(f"Resolucion exitosa: {clausulas[i]} y {clausulas[j]} → []")
                        print("\n✔ La conclusion 'q' es logicamente deducible.")
                        return
                    if resolvente not in clausulas and resolvente not in nuevas:
                        nuevas.append(resolvente)
                        print(f"Nueva clausula obtenida: {resolvente}")

        if not nuevas:
            print("\n✘ No se pudo deducir la conclusion.")
            return

        # Agregamos las nuevas clausulas a la base
        clausulas += nuevas
        nuevas = []

# Ejecutamos el programa
aplicar_resolucion()
