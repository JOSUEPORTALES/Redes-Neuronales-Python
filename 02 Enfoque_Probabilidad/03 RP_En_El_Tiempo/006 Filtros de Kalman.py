import numpy as np
import matplotlib.pyplot as plt

# ------------------------------
# CONFIGURACION DEL SISTEMA
# ------------------------------

# Numero de pasos de tiempo que vamos a simular
pasos = 30

# Posicion inicial verdadera del robot
posicion_real = 0.0

# Velocidad constante (el robot se mueve 1 unidad por paso)
velocidad = 1.0

# Incertidumbre del movimiento (ruido del proceso)
ruido_movimiento = 0.2

# Incertidumbre de las mediciones (ruido del sensor)
ruido_medicion = 1.0

# Creamos listas para guardar la posicion real, medidas y estimaciones
posiciones_reales = []
mediciones = []
estimaciones = []

# ------------------------------
# PARAMETROS DEL FILTRO DE KALMAN
# ------------------------------

# Estimacion inicial del estado (posicion)
estimacion_actual = 0.0

# Incertidumbre inicial en la estimacion
incertidumbre_actual = 1.0

# Matriz de transicion del estado (en este caso simple: se suma velocidad)
F = 1.0  # matriz del sistema

# Matriz de control (cuanto afecta la velocidad al estado)
B = 1.0  # control

# Matriz de observacion (relacion entre estado y lo que medimos)
H = 1.0  # medicion directa de la posicion

# Varianza del ruido del proceso (incertidumbre en movimiento)
Q = ruido_movimiento ** 2

# Varianza del ruido de la medicion (incertidumbre en sensor)
R = ruido_medicion ** 2

# ------------------------------
# BUCLE PRINCIPAL DE SIMULACION
# ------------------------------

for paso in range(pasos):
    # ------ VERDADERO MOVIMIENTO DEL ROBOT ------
    # El robot se mueve con un poco de error (ruido)
    posicion_real += velocidad + np.random.normal(0, ruido_movimiento)
    posiciones_reales.append(posicion_real)

    # ------ MEDICION CON SENSOR RUIDOSO ------
    medicion = posicion_real + np.random.normal(0, ruido_medicion)
    mediciones.append(medicion)

    # ------ PREDICCION DEL FILTRO DE KALMAN ------
    prediccion_estado = F * estimacion_actual + B * velocidad
    prediccion_incertidumbre = F * incertidumbre_actual * F + Q

    # ------ ACTUALIZACION CON LA MEDICION ------
    # Ganancia de Kalman (cuanto confiamos en el sensor)
    ganancia_kalman = prediccion_incertidumbre * H / (H * prediccion_incertidumbre * H + R)

    # Corregimos la prediccion con la nueva medicion
    estimacion_actual = prediccion_estado + ganancia_kalman * (medicion - H * prediccion_estado)

    # Actualizamos la incertidumbre
    incertidumbre_actual = (1 - ganancia_kalman * H) * prediccion_incertidumbre

    # Guardamos la estimacion actual
    estimaciones.append(estimacion_actual)

# ------------------------------
# GRAFICAMOS LOS RESULTADOS
# ------------------------------
plt.figure(figsize=(12, 6))
plt.plot(posiciones_reales, label='Posicion Real', color='green', linestyle='--')
plt.plot(mediciones, label='Mediciones con Ruido', color='red', linestyle=':')
plt.plot(estimaciones, label='Estimacion por Kalman', color='blue')
plt.xlabel('Paso de Tiempo')
plt.ylabel('Posicion')
plt.title('Filtro de Kalman - Seguimiento de un Robot en 1D')
plt.legend()
plt.grid(True)
plt.show()
