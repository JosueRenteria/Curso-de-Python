# Declaracion de las variables.
variable = "Dia"
variable2 = 200

# Declaracion de la Funcion Match.
match variable:
    case "Dia":
        print("Hola Buenos Dias.")
    case "Tarde":
        print("Hola Buenas Tardes.")
    case "Noche":
        print("Hola Buenas Noches")
    # El caso por defecto.
    case _:
        print("Mensaje Erroneo.")


# Para reducir el codigo (Cuando se repiten casos).
match variable:
    case "Dia" | "Tarde" | "Noche":
        print("Hola Buenos ", variable)
    case _:
        print("Mensaje Erroneo.")

# Para numeros (Con condiciones).
match variable2:
    case variable2 if (variable2 > 200):
        print(variable2, " Es un numero mayor a 200.")
    case variable2 if (variable2 < 200):
        print(variable2, " Es un numero menor a 200.")
    case _:
        print(variable2, " Es igual a 200.")