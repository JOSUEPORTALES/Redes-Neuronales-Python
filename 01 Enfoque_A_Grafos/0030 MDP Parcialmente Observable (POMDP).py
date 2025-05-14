import numpy as np
"""
Este programa implementa un modelo de decisión parcialmente observable (POMDP) para un agente que opera en un entorno incierto.
El agente tiene una creencia inicial sobre su estado, que se actualiza a medida que toma acciones y recibe observaciones.
El flujo principal del programa es el siguiente:
1. Se define un conjunto de estados, acciones y observaciones posibles.
2. Se especifican las matrices de transición y observación que modelan el comportamiento del entorno.
3. El agente comienza con una creencia inicial uniforme sobre los estados.
4. Se implementan funciones para:
    - Actualizar la creencia del agente con base en una observación recibida.
    - Predecir la nueva creencia tras realizar una acción.
    - Seleccionar una acción basada en una política simple.
5. Se simula un paso del POMDP:
    - El agente selecciona una acción según su política.
    - Se predice la nueva creencia tras la acción.
    - Se recibe una observación y se actualiza la creencia del agente.
Funciones principales:
- `actualizar_creencia(creencia, observacion)`: Actualiza la creencia del agente con base en una observación recibida.
- `predecir_creencia(creencia, accion)`: Predice la nueva creencia del agente tras realizar una acción.
- `politica(creencia)`: Define una política simple para seleccionar acciones basadas en la creencia actual.
El programa ilustra cómo un agente puede razonar y tomar decisiones en un entorno incierto utilizando un modelo POMDP.
"""





# Estados posibles (el agente no sabe en cuál está exactamente)
estados = ['bueno', 'regular', 'malo']

# Acciones posibles
acciones = ['esperar', 'mover']

# Observaciones posibles que recibe el agente (indirectas)
observaciones = ['brillante', 'oscuro']

# Matriz de transición: probabilidad de pasar de un estado a otro dado una accion
# transicion[accion][estado_actual][estado_siguiente]
transicion = {
    'esperar': [
        [0.8, 0.2, 0.0],  # desde 'bueno'
        [0.1, 0.8, 0.1],  # desde 'regular'
        [0.0, 0.3, 0.7]   # desde 'malo'
    ],
    'mover': [
        [0.6, 0.3, 0.1],
        [0.2, 0.6, 0.2],
        [0.1, 0.4, 0.5]
    ]
}

# Matriz de observación: probabilidad de recibir una observacion dado el estado real
# observacion[estado][observacion]
prob_observacion = {
    'bueno': {'brillante': 0.9, 'oscuro': 0.1},
    'regular': {'brillante': 0.5, 'oscuro': 0.5},
    'malo': {'brillante': 0.2, 'oscuro': 0.8}
}

# Inicialmente, el agente no sabe dónde está (creencia uniforme)
creencia = np.array([1/3, 1/3, 1/3])  # probabilidades sobre ['bueno', 'regular', 'malo']

# Funcion para actualizar la creencia con una observacion
def actualizar_creencia(creencia, observacion):
    nueva_creencia = np.zeros(len(estados))
    for i, estado in enumerate(estados):
        prob = prob_observacion[estado][observacion]
        nueva_creencia[i] = creencia[i] * prob

    # Normalizamos la creencia para que sea una distribución de probabilidad
    suma = sum(nueva_creencia)
    if suma > 0:
        nueva_creencia /= suma
    return nueva_creencia

# Funcion para predecir nueva creencia tras una accion
def predecir_creencia(creencia, accion):
    nueva_creencia = np.zeros(len(estados))
    for i, prob_estado in enumerate(creencia):
        for j in range(len(estados)):
            nueva_creencia[j] += prob_estado * transicion[accion][i][j]
    return nueva_creencia

# Politica simple basada en creencia:
# si se cree que estamos más cerca de 'malo', mejor moverse
def politica(creencia):
    indice_mayor = np.argmax(creencia)
    if estados[indice_mayor] == 'malo':
        return 'mover'
    else:
        return 'esperar'

# Simulacion paso a paso
print("Creencia inicial:", dict(zip(estados, creencia.round(2))))

# Paso 1: aplicar politica y accion
accion = politica(creencia)
print("\nAccion tomada:", accion)

# Paso 2: predecimos nueva creencia (transicion)
creencia = predecir_creencia(creencia, accion)
print("Creencia despues de transicion:", dict(zip(estados, creencia.round(2))))

# Paso 3: recibimos una observacion
observacion_recibida = 'oscuro'  # simulemos que se observa un ambiente oscuro
print("Observacion recibida:", observacion_recibida)

# Paso 4: actualizamos creencia con la observacion
creencia = actualizar_creencia(creencia, observacion_recibida)
print("Creencia actualizada con observacion:", dict(zip(estados, creencia.round(2))))
