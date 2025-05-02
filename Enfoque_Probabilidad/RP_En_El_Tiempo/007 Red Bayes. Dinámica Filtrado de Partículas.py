import numpy as np
import matplotlib.pyplot as plt

# --------------------------
# CONFIGURACION DEL SISTEMA
# --------------------------

# Largo del pasillo (posiciones posibles de la persona)
largo_pasillo = 100

# Numero de pasos de tiempo
pasos = 30

# Numero de particulas que usaremos
num_particulas = 500

# Ruido en el movimiento (la persona no siempre avanza exactamente 1 unidad)
ruido_movimiento = 1.0

# Ruido en la medicion del sensor
ruido_sensor = 5.0

# Posicion inicial real
posicion_real = 20

# Listas para guardar valores
posiciones_reales = []
mediciones = []
estimaciones = []

# --------------------------
# INICIALIZAMOS PARTICULAS
# --------------------------
# Cada particula representa una suposicion sobre la posicion de la persona
particulas = np.random.uniform(0, largo_pasillo, num_particulas)

# Cada particula tiene un peso inicial igual
pesos = np.ones(num_particulas) / num_particulas

# --------------------------
# FUNCION PARA RE-MUESTREO
# --------------------------
def remuestreo(particulas, pesos):
    indices = np.random.choice(len(particulas), size=len(particulas), p=pesos)
    return particulas[indices]

# --------------------------
# FILTRADO DE PARTICULAS
# --------------------------
for paso in range(pasos):
    # --------------------------
    # MOVIMIENTO REAL DE LA PERSONA (DESCONOCIDO PARA NOSOTROS)
    posicion_real += np.random.normal(1.0, ruido_movimiento)
    posicion_real = np.clip(posicion_real, 0, largo_pasillo)  # Limitar dentro del pasillo
    posiciones_reales.append(posicion_real)

    # --------------------------
    # SENSOR LEE LA POSICION CON RUIDO
    medicion = posicion_real + np.random.normal(0.0, ruido_sensor)
    medicion = np.clip(medicion, 0, largo_pasillo)
    mediciones.append(medicion)

    # --------------------------
    # PREDICCION: mover cada particula segun el modelo de movimiento
    particulas += np.random.normal(1.0, ruido_movimiento, size=num_particulas)
    particulas = np.clip(particulas, 0, largo_pasillo)

    # --------------------------
    # ACTUALIZACION: calcular pesos segun la probabilidad de la medicion
    # Usamos una distribucion normal para dar mas peso a particulas cercanas a la medicion
    pesos = (1.0 / (np.sqrt(2 * np.pi) * ruido_sensor)) * \
            np.exp(-0.5 * ((medicion - particulas) ** 2) / (ruido_sensor ** 2))

    # Normalizamos los pesos
    pesos += 1e-300  # para evitar dividir por cero
    pesos /= np.sum(pesos)

    # --------------------------
    # ESTIMACION: posicion promedio de las particulas con peso
    estimacion = np.sum(particulas * pesos)
    estimaciones.append(estimacion)

    # --------------------------
    # RE-MUESTREO: seleccionamos nuevas particulas segun los pesos
    particulas = remuestreo(particulas, pesos)

# --------------------------
# GRAFICO DE RESULTADOS
# --------------------------
plt.figure(figsize=(12, 6))
plt.plot(posiciones_reales, label='Posicion Real', color='green', linestyle='--')
plt.plot(mediciones, label='Mediciones Ruidosas', color='red', linestyle=':')
plt.plot(estimaciones, label='Estimacion por Particulas', color='blue')
plt.xlabel('Paso de Tiempo')
plt.ylabel('Posicion en el Pasillo')
plt.title('Filtrado de Particulas - Seguimiento de una Persona en un Pasillo')
plt.legend()
plt.grid(True)
plt.show()
