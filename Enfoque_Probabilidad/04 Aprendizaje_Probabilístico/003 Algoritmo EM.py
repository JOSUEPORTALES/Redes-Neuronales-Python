import numpy as np
import matplotlib.pyplot as plt

# ----------------------------
# 1. DATOS SIMULADOS
# ----------------------------

# Creamos dos grupos de datos de forma oculta (no sabremos de cuál viene cada punto)
np.random.seed(0)

grupo1 = np.random.normal(0, 1, 100)   # grupo centrado en 0
grupo2 = np.random.normal(5, 1, 100)   # grupo centrado en 5

# Mezclamos los datos sin saber de qué grupo vienen (esto es lo que vería el algoritmo)
datos = np.hstack([grupo1, grupo2])

# ----------------------------
# 2. INICIALIZACION
# ----------------------------

# Supongamos dos componentes gaussianas
media1 = np.random.choice(datos)
media2 = np.random.choice(datos)
var1 = 1
var2 = 1
peso1 = 0.5
peso2 = 0.5

# ----------------------------
# 3. FUNCIONES AUXILIARES
# ----------------------------

# Funcion para calcular la probabilidad de un valor en una normal
def normal(valor, media, varianza):
    coef = 1.0 / np.sqrt(2 * np.pi * varianza)
    exponente = np.exp(- ((valor - media) ** 2) / (2 * varianza))
    return coef * exponente

# ----------------------------
# 4. ALGORITMO EM
# ----------------------------

for iteracion in range(20):  # Repetimos varias veces para que el algoritmo converja

    # E-step: calcular responsabilidades (probabilidades de pertenencia)
    responsabilidades1 = peso1 * normal(datos, media1, var1)
    responsabilidades2 = peso2 * normal(datos, media2, var2)
    suma_total = responsabilidades1 + responsabilidades2

    # Normalizamos para que las probabilidades sumen 1
    gamma1 = responsabilidades1 / suma_total
    gamma2 = responsabilidades2 / suma_total

    # M-step: actualizar parámetros con los valores esperados
    peso1 = np.mean(gamma1)
    peso2 = np.mean(gamma2)

    media1 = np.sum(gamma1 * datos) / np.sum(gamma1)
    media2 = np.sum(gamma2 * datos) / np.sum(gamma2)

    var1 = np.sum(gamma1 * (datos - media1)**2) / np.sum(gamma1)
    var2 = np.sum(gamma2 * (datos - media2)**2) / np.sum(gamma2)

# ----------------------------
# 5. RESULTADOS
# ----------------------------

print("Parametros estimados:")
print(f"Componente 1 -> media: {media1:.2f}, varianza: {var1:.2f}, peso: {peso1:.2f}")
print(f"Componente 2 -> media: {media2:.2f}, varianza: {var2:.2f}, peso: {peso2:.2f}")

# ----------------------------
# 6. GRAFICO
# ----------------------------

# Graficamos los datos originales
plt.hist(datos, bins=30, density=True, alpha=0.5, label="Datos observados")

# Graficamos las distribuciones gaussianas aprendidas
x = np.linspace(min(datos), max(datos), 1000)
gauss1 = peso1 * normal(x, media1, var1)
gauss2 = peso2 * normal(x, media2, var2)

plt.plot(x, gauss1, label="Componente 1", color="red")
plt.plot(x, gauss2, label="Componente 2", color="blue")
plt.title("Ajuste por EM: mezcla de gaussianas")
plt.legend()
plt.xlabel("Valor")
plt.ylabel("Densidad")
plt.show()
