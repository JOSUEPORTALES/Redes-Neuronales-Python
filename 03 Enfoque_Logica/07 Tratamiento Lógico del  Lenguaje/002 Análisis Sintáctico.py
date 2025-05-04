# Este programa realiza un análisis sintáctico simple de oraciones usando una gramática libre de contexto.
# El análisis sintáctico permite verificar si una oración tiene una estructura gramatical válida,
# lo cual es fundamental en el procesamiento del lenguaje natural dentro de la Inteligencia Artificial.
# Se utiliza la librería nltk para definir una gramática y construir un analizador sintáctico descendente.


# Importamos las librerías necesarias
import nltk
from nltk import CFG

# Descargamos los recursos necesarios de nltk si no están instalados
nltk.download('punkt')

# Definimos una gramática libre de contexto (CFG)
# Esta gramática define cómo se forma una oración simple en español
gramatica = CFG.fromstring("""
    S -> SN SV
    SN -> Det N
    SV -> V SN | V
    Det -> 'el' | 'la'
    N -> 'gato' | 'perro' | 'niña' | 'pelota'
    V -> 'come' | 've' | 'patea'
""")

# Creamos un analizador sintáctico descendente con la gramática
analizador = nltk.ChartParser(gramatica)

# Definimos una lista de oraciones de ejemplo para analizar
oraciones = [
    "el gato come",
    "la niña ve el perro",
    "el perro patea la pelota",
    "el gato patea",
    "la pelota come el perro",  # esta no tiene sentido, pero es sintácticamente válida
    "el gato salta"  # esta no es válida porque "salta" no está en la gramática
]

# Analizamos cada oración
for oracion in oraciones:
    print(f"\nOracion: '{oracion}'")
    
    # Tokenizamos la oración en palabras
    palabras = oracion.split()
    
    # Intentamos generar el árbol sintáctico con la gramática definida
    try:
        generador = analizador.parse(palabras)
        generado = False
        for arbol in generador:
            generado = True
            print("Estructura sintactica valida:")
            arbol.pretty_print()
        if not generado:
            print("La oracion no es sintacticamente valida segun la gramatica.")
    except ValueError as e:
        print(f"Error en el analisis: {e}")
