# Importamos la biblioteca itertools que nos permite generar combinaciones de valores
import itertools

# Definimos una funcion para calcular el valor de verdad de una implicacion (p → q)
def implicacion(p, q):
    # En logica proposicional, p → q es falso solo si p es verdadero y q es falso
    return (not p) or q

# Definimos una funcion para imprimir la tabla de verdad
def mostrar_tabla_verdad():
    # Creamos las variables: 'llueve' (p) y 'calle_mojada' (q)
    # Cada una puede tomar los valores True (Verdadero) o False (Falso)
    
    # itertools.product genera todas las combinaciones posibles de valores para p y q
    combinaciones = list(itertools.product([True, False], repeat=2))

    # Imprimimos los encabezados de la tabla
    print("llueve | calle_mojada | llueve -> calle_mojada")
    print("-----------------------------------------------")

    # Recorremos todas las combinaciones posibles
    for llueve, calle_mojada in combinaciones:
        # Calculamos el resultado de la implicacion
        resultado = implicacion(llueve, calle_mojada)

        # Mostramos la fila correspondiente de la tabla de verdad
        print(f"{llueve!s:^7} | {calle_mojada!s:^13} | {resultado!s:^25}")

# Llamamos a la funcion para mostrar la tabla de verdad
mostrar_tabla_verdad()
