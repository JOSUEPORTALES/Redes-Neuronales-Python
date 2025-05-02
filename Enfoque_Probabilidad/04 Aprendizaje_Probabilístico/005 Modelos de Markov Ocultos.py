import numpy as np
from hmmlearn import hmm

# -----------------------------------------
# 1. DEFINICION DE LOS COMPONENTES DEL HMM
# -----------------------------------------

# Definimos los estados ocultos (emociones)
estados = ['feliz', 'triste']
n_estados = len(estados)

# Definimos los posibles simbolos que observamos
observaciones_posibles = ['jaja', 'meh', 'buuu']
n_observaciones = len(observaciones_posibles)

# Codificamos las observaciones como números para el modelo
diccionario_observaciones = {'jaja': 0, 'meh': 1, 'buuu': 2}

# -----------------------------------------
# 2. CREAMOS EL MODELO HMM
# -----------------------------------------

modelo = hmm.MultinomialHMM(n_components=n_estados, random_state=42)

# Definimos las probabilidades de inicio para cada estado
modelo.startprob_ = np.array([0.6, 0.4])  # más probable que comience feliz

# Matriz de transiciones entre estados (de uno a otro)
modelo.transmat_ = np.array([
    [0.7, 0.3],  # de feliz a feliz o triste
    [0.4, 0.6],  # de triste a feliz o triste
])

# Matriz de emisiones: probabilidad de decir algo según el estado emocional
modelo.emissionprob_ = np.array([
    [0.6, 0.3, 0.1],  # si está feliz: alta probabilidad de decir "jaja"
    [0.1, 0.4, 0.5],  # si está triste: más probable "buuu"
])

# -----------------------------------------
# 3. DEFINIMOS UNA SECUENCIA OBSERVADA
# -----------------------------------------

# Secuencia de frases escuchadas
secuencia_frases = ['jaja', 'meh', 'meh', 'buuu', 'jaja']

# Convertimos las frases a números
secuencia_numerica = np.array([[diccionario_observaciones[frase]] for frase in secuencia_frases])

# -----------------------------------------
# 4. USAMOS EL ALGORITMO DE VITERBI
# -----------------------------------------

# El algoritmo Viterbi encuentra la secuencia de estados más probable
log_prob, secuencia_estados = modelo.decode(secuencia_numerica, algorithm="viterbi")

# -----------------------------------------
# 5. MOSTRAMOS LOS RESULTADOS
# -----------------------------------------

print("Frases observadas:")
print(secuencia_frases)
print("\nSecuencia de emociones estimada (estados ocultos):")
for i, estado in enumerate(secuencia_estados):
    print(f"{secuencia_frases[i]} --> {estados[estado]}")
