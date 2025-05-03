# Definimos una funcion para combinar factores de certeza
# Esta es una version simplificada del metodo de MYCIN (sistema experto)
def combinar_factores(fc1, fc2):
    if fc1 > 0 and fc2 > 0:
        # Cuando ambos son positivos
        return fc1 + fc2 * (1 - fc1)
    elif fc1 < 0 and fc2 < 0:
        # Cuando ambos son negativos
        return fc1 + fc2 * (1 + fc1)
    else:
        # Cuando hay conflicto entre evidencias
        return (fc1 + fc2) / (1 - min(abs(fc1), abs(fc2)))

# Regla simple: si hay fiebre (0.8) y dolor muscular (0.6), entonces puede haber gripe con cierto FC
# Simularemos una inferencia lógica con incertidumbre

# Hechos conocidos con factores de certeza
fiebre_fc = 0.8            # Estoy casi seguro de que hay fiebre
dolor_muscular_fc = 0.6    # Confianza moderada en que hay dolor muscular

# Confianza de la regla: "si fiebre Y dolor muscular → entonces gripe"
fc_regla = 0.9             # Alta confianza en la regla

# Primero, combinamos los factores de certeza de los hechos (fiebre y dolor muscular)
fc_hechos = min(fiebre_fc, dolor_muscular_fc)

# Aplicamos la regla multiplicando la certeza de los hechos por la certeza de la regla
fc_gripe = fc_hechos * fc_regla

# Mostramos los resultados
print("\n Diagnóstico con incertidumbre:")
print(f"- Fiebre: {fiebre_fc}")
print(f"- Dolor muscular: {dolor_muscular_fc}")
print(f"- FC de la regla: {fc_regla}")
print(f"=> FC de tener gripe: {fc_gripe:.2f}")

# Ahora supongamos que hay otra fuente que dice que NO hay gripe con certeza 0.4
fc_no_gripe = -0.4

# Combinamos ambas fuentes para obtener un resultado final
fc_final = combinar_factores(fc_gripe, fc_no_gripe)

print(f"\n Combinando evidencias contradictorias...")
print(f"- FC de tener gripe (positivo): {fc_gripe:.2f}")
print(f"- FC de no tener gripe (negativo): {fc_no_gripe}")
print(f"=> FC final de gripe: {fc_final:.2f}")
