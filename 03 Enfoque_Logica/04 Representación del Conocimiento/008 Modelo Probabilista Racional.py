# Importamos la libreria necesaria para trabajar con probabilidades
import random

# Definimos una clase para el modelo probabilista racional
class ModeloProbabilistaRacional:
    def __init__(self):
        # Base de conocimiento probabilistica: enfermedad -> probabilidad de ocurrencia
        self.enfermedades = {
            "gripe": 0.5,
            "resfriado": 0.3,
            "covid": 0.2
        }

        # Probabilidades condicionales de sintomas dado la enfermedad
        self.condicionales = {
            "fiebre": {"gripe": 0.8, "resfriado": 0.2, "covid": 0.9},
            "tos": {"gripe": 0.7, "resfriado": 0.6, "covid": 0.9},
            "dolor muscular": {"gripe": 0.6, "resfriado": 0.1, "covid": 0.7}
        }

    # Metodo para calcular la probabilidad posterior usando la regla de Bayes simplificada
    def inferir_enfermedad(self, sintomas_observados):
        probabilidades = {}

        # Para cada enfermedad, calculamos una puntuacion de probabilidad
        for enfermedad in self.enfermedades:
            probabilidad = self.enfermedades[enfermedad]

            # Multiplicamos la probabilidad por la de cada sintoma dado la enfermedad
            for sintoma in sintomas_observados:
                if sintoma in self.condicionales:
                    probabilidad *= self.condicionales[sintoma].get(enfermedad, 0.01)  # Valor por defecto si no está

            probabilidades[enfermedad] = probabilidad

        # Mostramos los resultados
        print("Probabilidades calculadas:")
        for enfermedad, prob in probabilidades.items():
            print(f"{enfermedad}: {round(prob, 4)}")

        # Elegimos la enfermedad con mayor probabilidad
        mejor = max(probabilidades, key=probabilidades.get)
        print("\nDiagnostico mas probable:", mejor)

# Creamos el modelo
modelo = ModeloProbabilistaRacional()

# Definimos sintomas que observamos en una persona
sintomas_usuario = ["fiebre", "tos"]

# Ejecutamos la inferencia probabilista
modelo.inferir_enfermedad(sintomas_usuario)
