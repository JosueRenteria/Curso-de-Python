#Titulo Programa: Condicionales
#Fecha: 03-Septiembre-2022
#Autor: Renteria Arriaga Josue

#Condicionales en Python (<, >, ==, >=, <=).
x = 20
    # x = input("Ingresa un Numero: ")
    # x_numerico = int(x)
if x < 30:
    print("x es menor que 30")
elif x == 0:
    print("x es igual a 0")
else:
    print("x es mayor que 30")

#If Anidados.
nombre, apellido = "Josue", "Renteria"
if nombre == "Josue":
    if apellido == "Renteria":
        print("Bienvenido " + nombre + ".")
    else:
        print("Tu Apellido no Coincide.")
else:
    print("Tu no Eres Josue.")

#Ocupar operadores logicos para simplificar algunos if anidados (and, or, not). 
if nombre == "Josue" and apellido == "Renteria":
    print("Hola " + nombre + " " + apellido)
    