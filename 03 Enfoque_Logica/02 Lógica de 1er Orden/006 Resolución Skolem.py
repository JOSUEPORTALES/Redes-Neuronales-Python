# Clase que representa una formula lógica con cuantificadores
class FormulaLogica:
    def __init__(self, cuantificador, variable, cuerpo):
        # Guardamos el tipo de cuantificador: 'para_todo' o 'existe'
        self.cuantificador = cuantificador
        self.variable = variable  # variable ligada por el cuantificador
        self.cuerpo = cuerpo      # el contenido de la formula, en forma de texto

    def __str__(self):
        # Formato de impresión amigable
        simbolo = "∀" if self.cuantificador == "para_todo" else "∃"
        return f"{simbolo}{self.variable}: {self.cuerpo}"

# Funcion para skolemizar una formula con cuantificadores
def skolemizar(formula, variables_para_todo):
    """
    Transforma una formula con cuantificador existencial en una sin ∃,
    usando funciones o constantes de Skolem.
    """
    if formula.cuantificador == "existe":
        if variables_para_todo:
            # Si hay variables universales, usamos una funcion de Skolem
            nombre_funcion = f"f_skolem_{formula.variable}"
            nuevos_valores = ", ".join(variables_para_todo)
            cuerpo_transformado = formula.cuerpo.replace(formula.variable, f"{nombre_funcion}({nuevos_valores})")
        else:
            # Si no hay variables universales, usamos una constante de Skolem
            nombre_constante = f"c_skolem_{formula.variable}"
            cuerpo_transformado = formula.cuerpo.replace(formula.variable, nombre_constante)
        return cuerpo_transformado
    else:
        # Si es 'para_todo', agregamos su variable a la lista de variables universales
        variables_para_todo.append(formula.variable)
        return f"para_todo {formula.variable}: {formula.cuerpo}"

# --- EJEMPLO PRÁCTICO ---

# Creamos una fórmula lógica: ∀x (Estudiante(x) → ∃y Toma(x, y))
formula_existencial = FormulaLogica("existe", "y", "Toma(x, y)")
formula_universal = FormulaLogica("para_todo", "x", f"Estudiante(x) → {str(formula_existencial)}")

# Mostramos la fórmula original
print("🧾 Fórmula original con cuantificadores:")
print(formula_universal)

# Proceso de Skolemización
print("\n⚙️ Aplicando Skolemización...")
variables_para_todo = [formula_universal.variable]  # x es la variable universal
formula_skolemizada = skolemizar(formula_existencial, variables_para_todo)

# Mostrar la fórmula transformada
print("\n✅ Fórmula después de skolemizar:")
print(f"para_todo x: Estudiante(x) → {formula_skolemizada}")
