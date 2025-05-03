# ============================================
# EJEMPLO DE PROGRAMACION LOGICA INDUCTIVA (FOIL SIMPLIFICADO)
# ============================================
# Este programa simula un enfoque básico de FOIL (First Order Inductive Learner),
# que genera reglas lógicas a partir de ejemplos positivos y negativos.
# FOIL busca construir hipótesis lógicas de primer orden que expliquen los ejemplos positivos
# sin cubrir los negativos. Aquí mostramos una forma simplificada del algoritmo con reglas tipo "si-entonces".

# Conjunto de ejemplos positivos y negativos
ejemplos_positivos = [
    {"animal": "gato", "tiene_pelo": True, "da_leche": True},
    {"animal": "perro", "tiene_pelo": True, "da_leche": True},
    {"animal": "vaca", "tiene_pelo": True, "da_leche": True},
]

ejemplos_negativos = [
    {"animal": "serpiente", "tiene_pelo": False, "da_leche": False},
    {"animal": "cocodrilo", "tiene_pelo": False, "da_leche": False},
    {"animal": "pollo", "tiene_pelo": False, "da_leche": False},
]

# Funcion que genera reglas basicas a partir de los ejemplos
def generar_regla_foil(ejemplos_positivos, ejemplos_negativos):
    # Inicializamos una lista para guardar las condiciones candidatas
    condiciones = []

    # Revisamos todos los atributos del primer ejemplo positivo
    for atributo in ejemplos_positivos[0]:
        if atributo == "animal":
            continue  # Saltamos el atributo "animal" porque solo es identificador

        # Verificamos si el valor de este atributo es el mismo en todos los ejemplos positivos
        valor_posible = all(ejemplo[atributo] == ejemplos_positivos[0][atributo] for ejemplo in ejemplos_positivos)
        
        # Verificamos si ese valor no aparece en los ejemplos negativos
        valor_exclusivo = all(ejemplo[atributo] != ejemplos_positivos[0][atributo] for ejemplo in ejemplos_negativos)

        # Si se cumple en todos los positivos y en ninguno de los negativos, es una buena regla
        if valor_posible and valor_exclusivo:
            condiciones.append((atributo, ejemplos_positivos[0][atributo]))

    return condiciones

# Funcion que imprime la regla en forma comprensible
def imprimir_regla(condiciones):
    if not condiciones:
        print("No se encontraron condiciones que distingan los positivos de los negativos.")
        return

    regla = "SI "
    regla += " Y ".join([f"{atributo} = {valor}" for atributo, valor in condiciones])
    regla += " ENTONCES el animal es un mamifero"
    print("Regla aprendida por FOIL (simplificada):")
    print(regla)

# Ejecutamos el algoritmo FOIL simplificado
condiciones_encontradas = generar_regla_foil(ejemplos_positivos, ejemplos_negativos)
imprimir_regla(condiciones_encontradas)
# ============================================
# Este es un ejemplo básico y simplificado de cómo se puede implementar un enfoque inductivo