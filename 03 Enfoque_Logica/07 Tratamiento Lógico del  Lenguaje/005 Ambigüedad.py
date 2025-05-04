# =============================================================
# AMBIGÜEDAD EN EL LENGUAJE NATURAL - SIMULACION EN PYTHON
# =============================================================
# Este programa muestra como una oracion puede tener multiples
# significados (ambiguedad) dependiendo de la forma en que se interpreta.
# No usamos librerías externas, solo listas y condicionales.
# El objetivo es demostrar que una misma frase puede entenderse
# de distintas maneras, lo que es un problema importante para la IA.



# Definimos una oracion ambigua
oracion = "Vi al hombre con el telescopio"

# Mostramos la oracion original
print("Oracion original:")
print(oracion)
print()

# Simulamos las dos posibles interpretaciones de la oracion
interpretaciones = [
    {
        "descripcion": "Use un telescopio para ver al hombre",
        "explicacion": "La frase 'con el telescopio' se refiere a como vi al hombre (instrumento usado)."
    },
    {
        "descripcion": "Vi a un hombre que tenia un telescopio",
        "explicacion": "La frase 'con el telescopio' describe al hombre (atributo del sujeto)."
    }
]

# Mostramos las interpretaciones
print("Posibles interpretaciones de la oracion:")
for i, interpretacion in enumerate(interpretaciones, start=1):
    print(f"Interpretacion {i}: {interpretacion['descripcion']}")
    print(f"  Explicacion: {interpretacion['explicacion']}")
    print()

# Explicacion general:
# En el lenguaje natural, muchas oraciones tienen ambiguedad.
# Esto significa que se pueden entender de varias maneras.
# Los humanos entendemos el significado por el contexto,
# pero una computadora necesita reglas o informacion adicional
# para saber cual es la interpretacion correcta.

