

# Probabilidad de lluvia
"""
Este programa calcula la utilidad esperada de dos decisiones posibles (llevar paraguas o no llevarlo) 
basándose en la probabilidad de lluvia y una tabla de utilidad que asigna valores a cada combinación 
de decisión y condición climática. Finalmente, determina cuál es la mejor decisión según la utilidad 
esperada máxima.
Funciones principales del programa:
1. Define las probabilidades de lluvia y no lluvia.
2. Establece las opciones de decisión y una tabla de utilidad asociada.
3. Calcula la utilidad esperada para cada decisión considerando las probabilidades.
4. Muestra las utilidades esperadas y selecciona la decisión con mayor utilidad esperada.
"""
prob_lluvia = 0.4
prob_no_lluvia = 1 - prob_lluvia

# Opciones de decisión
decisiones = ["llevar_paraguas", "no_llevar"]

# Tabla de utilidad: (decisión, lluvia) → utilidad
utilidad = {
    ("llevar_paraguas", True): 7,
    ("llevar_paraguas", False): 3,
    ("no_llevar", True): -5,
    ("no_llevar", False): 10
}

# Calcular utilidad esperada para cada decisión
utilidad_esperada = {}
for decision in decisiones:
    u_lluvia = utilidad[(decision, True)] * prob_lluvia
    u_no_lluvia = utilidad[(decision, False)] * prob_no_lluvia
    utilidad_esperada[decision] = u_lluvia + u_no_lluvia

# Mostrar los resultados
print("Utilidad esperada por decisión:")
for decision, utilidad in utilidad_esperada.items():
    print(f"- {decision}: {utilidad}")

# Elegir la mejor decisión
mejor_decision = max(utilidad_esperada, key=utilidad_esperada.get)
print("\n🟢 Mejor decisión:", mejor_decision)
print("🔢 Utilidad esperada máxima:", utilidad_esperada[mejor_decision])
