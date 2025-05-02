# Cargamos librerias necesarias
from collections import defaultdict
import math

# --------------------------
# DATOS DE ENTRENAMIENTO
# --------------------------
# Cada fruta tiene: color, forma y etiqueta (clase)
frutas = [
    {'color': 'rojo', 'forma': 'redonda', 'clase': 'manzana'},
    {'color': 'rojo', 'forma': 'alargada', 'clase': 'manzana'},
    {'color': 'naranja', 'forma': 'redonda', 'clase': 'naranja'},
    {'color': 'naranja', 'forma': 'redonda', 'clase': 'naranja'},
    {'color': 'rojo', 'forma': 'redonda', 'clase': 'manzana'},
]

# --------------------------
# ENTRENAMIENTO BAYESIANO
# --------------------------

# Contadores para clases y atributos
conteo_clases = defaultdict(int)
conteo_atributos = defaultdict(lambda: defaultdict(int))
total_ejemplos = len(frutas)

# Contamos frecuencias
for fruta in frutas:
    clase = fruta['clase']
    conteo_clases[clase] += 1
    for atributo, valor in fruta.items():
        if atributo != 'clase':
            conteo_atributos[atributo + '=' + valor][clase] += 1

# --------------------------
# FUNCION PARA CLASIFICAR
# --------------------------
def clasificar(nueva_fruta):
    probabilidades = {}
    
    for clase in conteo_clases:
        # Probabilidad a priori P(clase)
        prob = conteo_clases[clase] / total_ejemplos
        
        # Multiplicamos por la probabilidad condicional de cada atributo
        for atributo, valor in nueva_fruta.items():
            clave = atributo + '=' + valor
            prob *= conteo_atributos[clave][clase] / conteo_clases[clase]
        
        probabilidades[clase] = prob
    
    # Devolvemos la clase con mayor probabilidad
    clase_estimacion = max(probabilidades, key=probabilidades.get)
    return clase_estimacion, probabilidades

# --------------------------
# EJEMPLO DE USO
# --------------------------

# Nueva fruta que queremos clasificar
fruta_nueva = {'color': 'rojo', 'forma': 'redonda'}

# Clasificamos usando el modelo bayesiano aprendido
clase_estimada, probabilidades = clasificar(fruta_nueva)

print("Fruta nueva:", fruta_nueva)
print("Probabilidades estimadas:", probabilidades)
print("Clase predicha:", clase_estimada)
