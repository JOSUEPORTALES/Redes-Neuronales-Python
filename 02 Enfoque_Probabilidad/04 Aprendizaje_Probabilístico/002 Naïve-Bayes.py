from collections import defaultdict

# --------------------------
# DATOS DE ENTRENAMIENTO
# --------------------------

# Cada correo tiene palabras y una clase: 'spam' o 'no_spam'
correos = [
    {'palabras': ['oferta', 'dinero', 'gratis'], 'clase': 'spam'},
    {'palabras': ['gana', 'dinero', 'rapido'], 'clase': 'spam'},
    {'palabras': ['hola', 'amigo', 'cena'], 'clase': 'no_spam'},
    {'palabras': ['trabajo', 'informe', 'adjunto'], 'clase': 'no_spam'},
    {'palabras': ['dinero', 'oferta', 'trabajo'], 'clase': 'spam'},
]

# --------------------------
# ENTRENAMIENTO NAÏVE BAYES
# --------------------------

# Conteo de palabras por clase y total de correos por clase
conteo_palabras = defaultdict(lambda: defaultdict(int))
conteo_correos_por_clase = defaultdict(int)
total_correos = len(correos)

# Contamos palabras y clases
for correo in correos:
    clase = correo['clase']
    conteo_correos_por_clase[clase] += 1
    for palabra in correo['palabras']:
        conteo_palabras[clase][palabra] += 1

# Obtenemos el vocabulario total
vocabulario = set()
for clase in conteo_palabras:
    for palabra in conteo_palabras[clase]:
        vocabulario.add(palabra)

# --------------------------
# FUNCION PARA CLASIFICAR UN NUEVO CORREO
# --------------------------

def clasificar(correo_nuevo):
    probabilidades = {}
    for clase in conteo_correos_por_clase:
        # Calculo de la probabilidad a priori P(clase)
        prob_clase = conteo_correos_por_clase[clase] / total_correos

        # Inicializamos la probabilidad total con la probabilidad de la clase
        prob_total = prob_clase

        # Conteo total de palabras en la clase actual
        total_palabras_en_clase = sum(conteo_palabras[clase].values())

        for palabra in correo_nuevo:
            # Conteo de la palabra en la clase (con suavizado de Laplace)
            conteo = conteo_palabras[clase][palabra] + 1  # +1 para evitar ceros
            prob_palabra = conteo / (total_palabras_en_clase + len(vocabulario))
            prob_total *= prob_palabra  # aplicamos Naïve Bayes: producto de las probabilidades

        probabilidades[clase] = prob_total

    # Devolvemos la clase con mayor probabilidad
    clase_estimada = max(probabilidades, key=probabilidades.get)
    return clase_estimada, probabilidades

# --------------------------
# EJEMPLO DE USO
# --------------------------

correo_prueba = ['dinero', 'gratis', 'trabajo']

clase, probabilidades = clasificar(correo_prueba)

print("Correo a clasificar:", correo_prueba)
print("Probabilidades por clase:", probabilidades)
print("Clase estimada:", clase)
