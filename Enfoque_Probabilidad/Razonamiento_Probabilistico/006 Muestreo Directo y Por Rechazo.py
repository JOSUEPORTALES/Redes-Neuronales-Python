import numpy as np
import matplotlib.pyplot as plt

# -------------------------
# Función de la distribución de interés
# -------------------------
def distribucion_interes(x):
    """
    Esta es una distribución arbitraria de interés. Para este ejemplo,
    usaremos una distribución de tipo 'normal' para muestreo directo y
    la utilizaremos también como distribución objetivo para el muestreo por rechazo.
    """
    return (1 / np.sqrt(2 * np.pi)) * np.exp(-0.5 * x**2)

# -------------------------
# Función de Muestreo Directo
# -------------------------
def muestreo_directo(n):
    """
    Muestrea directamente de una distribución normal estándar (media 0 y varianza 1).
    Utilizamos numpy para generar las muestras.
    """
    muestras = np.random.normal(0, 1, n)  # Muestras de una normal estándar
    return muestras

# -------------------------
# Función de Muestreo por Rechazo
# -------------------------
def muestreo_por_rechazo(n):
    """
    Muestreo por rechazo usando una distribución uniforme como propuesta.
    Rechazamos las muestras que no cumplan con la condición de aceptación.
    """
    muestras_aceptadas = []
    while len(muestras_aceptadas) < n:
        # Muestreo de la distribución propuesta (uniforme)
        propuesta = np.random.uniform(-5, 5)
        
        # Muestreo de la distribución objetivo (normal)
        prob_objetivo = distribucion_interes(propuesta)
        
        # Muestreo de la distribución de propuesta (uniforme), que tiene una altura máxima de 1/10
        prob_propuesta = 1 / 10  # Esto se refiere a la altura de la distribución uniforme
        
        # Condición de aceptación
        if np.random.uniform(0, 1) < prob_objetivo / prob_propuesta:
            muestras_aceptadas.append(propuesta)
    
    return np.array(muestras_aceptadas)

# -------------------------
# Ejecución de ambos métodos
# -------------------------

# Número de muestras que queremos generar
n_muestras = 1000

# Muestreo directo de la distribución normal
muestras_directas = muestreo_directo(n_muestras)

# Muestreo por rechazo
muestras_rechazo = muestreo_por_rechazo(n_muestras)

# -------------------------
# Visualización de los resultados
# -------------------------

# Graficamos ambas distribuciones y las muestras obtenidas
x = np.linspace(-5, 5, 1000)
plt.figure(figsize=(12, 6))

# Gráfico de la distribución de interés
plt.plot(x, distribucion_interes(x), label="Distribución de interés (normal)", color='blue', linewidth=2)

# Histograma de muestras directas
plt.hist(muestras_directas, bins=30, density=True, alpha=0.6, color='red', label="Muestras Directas", edgecolor='black')

# Histograma de muestras por rechazo
plt.hist(muestras_rechazo, bins=30, density=True, alpha=0.6, color='green', label="Muestras por Rechazo", edgecolor='black')

# Configuración de la gráfica
plt.title("Muestreo Directo vs Muestreo por Rechazo")
plt.xlabel("Valor")
plt.ylabel("Densidad de probabilidad")
plt.legend()

# Mostrar la gráfica
plt.show()
