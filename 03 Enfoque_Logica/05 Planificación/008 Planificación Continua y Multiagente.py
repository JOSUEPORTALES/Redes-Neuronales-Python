import random
import time

# Definimos el entorno como una cuadrícula de 3x3
espacio = [
    ["vacio", "pieza", "vacio"],
    ["vacio", "vacio", "pieza"],
    ["pieza", "vacio", "vacio"]
]

# Cada robot tiene su posicion y si lleva una pieza
robots = {
    "robot_1": {"posicion": [0, 0], "tiene_pieza": False},
    "robot_2": {"posicion": [2, 2], "tiene_pieza": False}
}

# Objetivo: cada robot debe recolectar una pieza
objetivos = {
    "robot_1": True,
    "robot_2": True
}

# Funcion para imprimir el estado actual
def imprimir_estado():
    print("\nEstado del entorno:")
    for i in range(3):
        fila = ""
        for j in range(3):
            celda = espacio[i][j]
            simbolo = "."
            for nombre, datos in robots.items():
                if datos["posicion"] == [i, j]:
                    simbolo = nombre[-1]  # Muestra 1 o 2
            if celda == "pieza":
                simbolo = "P"
            fila += simbolo + " "
        print(fila)
    print("Estado de los robots:")
    for nombre, datos in robots.items():
        print(nombre, "posicion:", datos["posicion"], "| tiene_pieza:", datos["tiene_pieza"])

# Funcion para mover el robot
def mover_robot(nombre_robot):
    robot = robots[nombre_robot]
    if robot["tiene_pieza"]:
        return  # Ya tiene la pieza, no hace nada

    x, y = robot["posicion"]

    # Buscar pieza cercana
    for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
        nx, ny = x + dx, y + dy
        if 0 <= nx < 3 and 0 <= ny < 3:
            if espacio[nx][ny] == "pieza":
                # Mover al robot
                robot["posicion"] = [nx, ny]
                robot["tiene_pieza"] = True
                espacio[nx][ny] = "vacio"
                print(nombre_robot, "recolecto una pieza en", [nx, ny])
                return
    
    # Si no hay pieza cerca, moverse aleatoriamente
    direcciones = [(-1,0),(1,0),(0,-1),(0,1)]
    random.shuffle(direcciones)
    for dx, dy in direcciones:
        nx, ny = x + dx, y + dy
        if 0 <= nx < 3 and 0 <= ny < 3:
            # Evitar colision con otro robot
            colision = False
            for otro, datos in robots.items():
                if otro != nombre_robot and datos["posicion"] == [nx, ny]:
                    colision = True
            if not colision:
                robot["posicion"] = [nx, ny]
                return

# Bucle de planificación continua
def planificacion_continua():
    pasos = 0
    while True:
        pasos += 1
        print(f"\n--- Paso {pasos} ---")

        # Simulamos que puede aparecer una nueva pieza
        if random.random() < 0.2:
            x, y = random.randint(0,2), random.randint(0,2)
            if espacio[x][y] == "vacio":
                espacio[x][y] = "pieza"
                print("Aparecio una nueva pieza en", [x, y])

        # Cada robot planifica su siguiente accion
        for nombre_robot in robots:
            mover_robot(nombre_robot)

        imprimir_estado()

        # Verificamos si ambos lograron su objetivo
        if all(robots[nombre]["tiene_pieza"] == objetivo for nombre, objetivo in objetivos.items()):
            print("\nTodos los robots cumplieron su objetivo.")
            break

        time.sleep(1)

# Iniciar el proceso
planificacion_continua()
