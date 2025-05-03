# Lista de ejemplos de entrenamiento
# Cada fruta tiene una lista de atributos y una etiqueta "si" (es dulce) o "no" (no es dulce)
ejemplos = [
    (["roja", "grande", "lisa"], "si"),
    (["roja", "grande", "rugosa"], "si"),
    (["verde", "grande", "lisa"], "no"),
    (["roja", "pequeña", "lisa"], "si")
]

# Inicializamos S (hipótesis más específica) con el primer ejemplo positivo
hipotesis_especifica = None
for atributos, etiqueta in ejemplos:
    if etiqueta == "si":
        hipotesis_especifica = atributos.copy()
        break

# Inicializamos G (hipótesis más generales) con todos los signos de "?"
hipotesis_general = [["?" for _ in hipotesis_especifica]]

# Recorremos cada ejemplo para actualizar S y G
for atributos, etiqueta in ejemplos:
    if etiqueta == "si":
        # Actualizamos la hipótesis específica
        for i in range(len(atributos)):
            if hipotesis_especifica[i] != atributos[i]:
                hipotesis_especifica[i] = "?"
        
        # Eliminamos de G las hipótesis que no cubren este positivo
        hipotesis_general = [h for h in hipotesis_general if all(h[i] == "?" or h[i] == atributos[i] for i in range(len(h)))]
    
    elif etiqueta == "no":
        # Generalizamos G para que no cubra este ejemplo negativo
        nuevas_hipotesis = []
        for h in hipotesis_general:
            for i in range(len(h)):
                if h[i] == "?":
                    if atributos[i] != hipotesis_especifica[i]:
                        nueva = h.copy()
                        nueva[i] = hipotesis_especifica[i]
                        nuevas_hipotesis.append(nueva)
        hipotesis_general += nuevas_hipotesis

# Mostramos las hipótesis finales
print("Hipotesis especifica (S):", hipotesis_especifica)
print("Hipotesis general (G):")
for h in hipotesis_general:
    print(h)
