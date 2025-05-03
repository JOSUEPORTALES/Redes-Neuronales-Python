# Definimos la clase que simula un sistema experto simple para diagnóstico médico
class SistemaExpertoDiagnostico:
    def __init__(self):
        # Base de conocimiento: hechos y reglas
        self.sintomas = []  # Lista vacía que se llenará con los síntomas que el usuario reporta
        self.diagnostico = None  # Aquí guardaremos la posible enfermedad diagnosticada

    # Metodo para agregar un sintoma reportado por el usuario
    def agregar_sintoma(self, sintoma):
        self.sintomas.append(sintoma)

    # Metodo que realiza la inferencia (reglas del experto)
    def analizar(self):
        # Reglas simples del sistema experto
        if "fiebre" in self.sintomas and "tos" in self.sintomas and "dolor de garganta" in self.sintomas:
            self.diagnostico = "gripe"
        elif "dolor de cabeza" in self.sintomas and "nauseas" in self.sintomas:
            self.diagnostico = "migraña"
        elif "dolor estomacal" in self.sintomas and "diarrea" in self.sintomas:
            self.diagnostico = "intoxicacion alimentaria"
        else:
            self.diagnostico = "sintomas insuficientes para un diagnostico"

    # Metodo para mostrar el resultado del diagnostico
    def mostrar_diagnostico(self):
        print("Diagnostico del sistema experto:", self.diagnostico)

# Ejemplo de uso del sistema experto

# Creamos una instancia del sistema
sistema = SistemaExpertoDiagnostico()

# Simulamos la entrada del usuario (sintomas que se presentan)
sistema.agregar_sintoma("fiebre")
sistema.agregar_sintoma("tos")
sistema.agregar_sintoma("dolor de garganta")

# Analizamos los sintomas usando reglas lógicas simples
sistema.analizar()

# Mostramos el resultado del diagnostico
sistema.mostrar_diagnostico()
