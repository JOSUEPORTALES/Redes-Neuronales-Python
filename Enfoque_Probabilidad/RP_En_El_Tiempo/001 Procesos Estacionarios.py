import numpy as np
import matplotlib.pyplot as plt

# ----------------------------------------
# Funcion para generar un proceso estacionario
# ----------------------------------------

def generar_proceso_estacionario(num_puntos):
    """
    Genera una secuencia de numeros aleatorios con media constante (ruido blanco).
    Es un proceso estacionario porque sus propiedades no cambian en el tiempo.
    """
    media = 0
    desviacion = 1
    # Generamos 'num_puntos' valores aleatorios de una distribucion normal
    datos = np.random.normal(media, desviacion, num_puntos)
    return datos

# ----------------------------------------
# Funcion para generar un proceso no estacionario
# ----------------------------------------

def generar_proceso_no_estacionario(num_puntos):
    """
    Genera una secuencia de datos con una tendencia lineal (no estacionario).
    La media cambia con el tiempo.
    """
    tendencia = np.linspace(0, 10, num_puntos)
    ruido = np.random.normal(0, 1, num_puntos)
    datos = tendencia + ruido
    return datos

# ----------------------------------------
# Graficar ambos procesos para compararlos
# ----------------------------------------

def graficar_procesos():
    puntos = 200

    estacionario = generar_proceso_estacionario(puntos)
    no_estacionario = generar_proceso_no_estacionario(puntos)

    # Creamos una figura con dos graficas
    plt.figure(figsize=(12, 6))

    # Grafica del proceso estacionario
    plt.subplot(1, 2, 1)
    plt.plot(estacionario, label="Proceso Estacionario", color="blue")
    plt.title("Proceso Estacionario (Ruido Blanco)")
    plt.xlabel("Tiempo")
    plt.ylabel("Valor")
    plt.grid(True)
    plt.legend()

    # Grafica del proceso no estacionario
    plt.subplot(1, 2, 2)
    plt.plot(no_estacionario, label="Proceso No Estacionario", color="red")
    plt.title("Proceso No Estacionario (Tendencia)")
    plt.xlabel("Tiempo")
    plt.ylabel("Valor")
    plt.grid(True)
    plt.legend()

    plt.suptitle("Comparacion de Procesos Estacionario vs No Estacionario")
    plt.tight_layout()
    plt.show()

# Llamamos a la funcion para graficar
graficar_procesos()
