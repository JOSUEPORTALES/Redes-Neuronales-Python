import numpy as np

# Funcion para calcular la distancia euclidiana entre dos vectores
def distancia(vector1, vector2):
    return np.sqrt(np.sum((vector1 - vector2)**2))

# Clase para representar el Mapa Autoorganizado
class MapaKohonen:
    def __init__(self, forma_mapa, dimensiones_entrada, tasa_aprendizaje):
        self.filas, self.columnas = forma_mapa
        self.dimensiones_entrada = dimensiones_entrada
        self.tasa_aprendizaje = tasa_aprendizaje

        # Inicializamos los pesos aleatoriamente
        self.mapa = np.random.rand(self.filas, self.columnas, dimensiones_entrada)

    # Encontrar la neurona ganadora (la mas parecida a la entrada)
    def encontrar_ganadora(self, entrada):
        menor_distancia = float('inf')
        posicion_ganadora = (0, 0)
        for i in range(self.filas):
            for j in range(self.columnas):
                peso = self.mapa[i, j]
                dist = distancia(entrada, peso)
                if dist < menor_distancia:
                    menor_distancia = dist
                    posicion_ganadora = (i, j)
        return posicion_ganadora

    # Entrenamiento del mapa
    def entrenar(self, entradas, epocas):
        for epoca in range(epocas):
            for entrada in entradas:
                i, j = self.encontrar_ganadora(entrada)
                # Ajustamos solo la neurona ganadora
                self.mapa[i, j] += self.tasa_aprendizaje * (entrada - self.mapa[i, j])
            if epoca % 10 == 0:
                print(f"Epoca {epoca} completada")

    # Mostrar los pesos finales
    def mostrar_pesos(self):
        for i in range(self.filas):
            for j in range(self.columnas):
                print(f"Neurona [{i},{j}]: {self.mapa[i,j]}")

# === Datos de ejemplo: colores rojo, verde y azul ===
colores = np.array([
    [1, 0, 0],  # rojo
    [0, 1, 0],  # verde
    [0, 0, 1],  # azul
    [1, 1, 0],  # amarillo (rojo + verde)
])

# Creamos el mapa (2x2 neuronas), cada color tiene 3 valores (R,G,B)
mapa = MapaKohonen(forma_mapa=(2, 2), dimensiones_entrada=3, tasa_aprendizaje=0.3)

# Entrenamos el mapa durante 100 epocas
mapa.entrenar(colores, epocas=100)

# Mostramos los pesos finales
print("\n=== Pesos finales del mapa ===")
mapa.mostrar_pesos()
