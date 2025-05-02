import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

# ---------------------------------------------
# 1. DATOS DE EJEMPLO
# ---------------------------------------------

# Cada fruta tiene dos características: tamaño y peso
# No sabemos qué tipo de fruta es, solo sus medidas

datos = np.array([
    [5, 100],   # fruta pequeña y ligera
    [6, 120],
    [5.5, 110],
    [15, 500],  # fruta grande y pesada
    [16, 520],
    [14.5, 510],
    [10, 300],  # fruta mediana
    [10.5, 310],
    [9.5, 295],
])

# ---------------------------------------------
# 2. AGRUPAMIENTO CON K-MEANS
# ---------------------------------------------

# Creamos el modelo KMeans para agrupar en 3 grupos
modelo = KMeans(n_clusters=3, random_state=0)

# Ajustamos el modelo a los datos
modelo.fit(datos)

# Obtenemos las etiquetas de grupo para cada fruta
etiquetas = modelo.labels_

# Obtenemos los centros de cada grupo (media de cada grupo)
centros = modelo.cluster_centers_

# ---------------------------------------------
# 3. VISUALIZACION DE RESULTADOS
# ---------------------------------------------

# Asignamos colores por grupo
colores = ['red', 'green', 'blue']
for i in range(3):
    grupo = datos[etiquetas == i]
    plt.scatter(grupo[:, 0], grupo[:, 1], color=colores[i], label=f'Grupo {i+1}')

# Dibujamos los centros de los grupos
plt.scatter(centros[:, 0], centros[:, 1], color='black', marker='x', s=100, label='Centro de grupo')

plt.title('Agrupamiento de frutas por tamaño y peso')
plt.xlabel('Tamaño (cm)')
plt.ylabel('Peso (g)')
plt.legend()
plt.grid(True)
plt.show()

# ---------------------------------------------
# 4. MOSTRAMOS LOS GRUPOS
# ---------------------------------------------
print("Etiquetas asignadas a cada fruta (grupo):")
for i, fruta in enumerate(datos):
    print(f"Fruta {i+1} con tamaño {fruta[0]} y peso {fruta[1]} -> Grupo {etiquetas[i] + 1}")
