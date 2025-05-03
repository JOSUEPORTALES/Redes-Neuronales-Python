# Funcion que representa una accion de salir de casa dependiendo del clima
def salir_de_casa(llueve):
    # Evaluamos la condicion: ¿está lloviendo?
    if llueve:
        # Si llueve, seguimos este plan
        print("Está lloviendo. Tomar paraguas.")
        print("Ponerse zapatos.")
        print("Salir de casa con paraguas.")
    else:
        # Si no llueve, seguimos otro plan
        print("No está lloviendo.")
        print("Ponerse zapatos.")
        print("Salir de casa sin paraguas.")

# Simulamos el estado del clima con una variable
# Cambia este valor a True o False para probar ambos escenarios
llueve = True

# Ejecutamos el plan condicional
salir_de_casa(llueve)
