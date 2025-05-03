# Definimos ejemplos de frutas
# Cada fruta tiene tres atributos y una etiqueta que indica si es dulce o no
ejemplos = [
    (["roja", "grande", "lisa"], "si"),
    (["roja", "grande", "rugosa"], "si"),
    (["verde", "grande", "lisa"], "no"),
    (["roja", "pequeña", "lisa"], "si"),
]

# Inicializamos la mejor hipotesis con los valores mas generales posibles
# Cada "?" significa que no sabemos nada aún
mejor_hipotesis = ["?", "?", "?"]

# Recorremos cada ejemplo del conjunto de entrenamiento
for atributos, etiqueta in ejemplos:
    # Solo nos interesan los ejemplos positivos (etiqueta "si")
    if etiqueta == "si":
        # Si la hipotesis es general (?), la reemplazamos por el primer ejemplo positivo
        if mejor_hipotesis == ["?", "?", "?"]:
            mejor_hipotesis = atributos.copy()
        else:
            # Comparamos cada atributo con la hipótesis actual
            for i in range(len(atributos)):
                # Si el valor es diferente al de la hipótesis, lo generalizamos a "?"
                if mejor_hipotesis[i] != atributos[i]:
                    mejor_hipotesis[i] = "?"

# Mostramos la mejor hipótesis final
print("Mejor hipotesis actual:", mejor_hipotesis)
