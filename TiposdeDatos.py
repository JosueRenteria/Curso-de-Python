#Titulo Programa: Tipos de Datos
#Fecha: 03-Septiembre-2022
#Autor: Renteria Arriaga Josue

#Tipo de Dato String (La palabra print es una funcion para mostrar cadenas).
print("Hola Mundo")
print('Hola Mundo')
print('''Hola Mundo''')
print("""Hola Mundo""")

#Para saber el tipo de dato (type es una funcion).
print(type("Hola Mundo"))

#Para unir cadena o concatenacion.
print("Hola" + " " + "Adios")

#Tipo de Datos Enteros y Flotantes
print(30)
print(type(30))
print(30.5)
print(type(30.5))

#Tipos de Datos Boolean
print(True)
print(False)

#Listas, las listas estan compuestos por elementos (se pueden cambiar los datos).
[10, 20, 30, 35]
["Hola", "Adios", "Bye"]
print(type([10, "Hola", "30.5"]))
[] #Lista Vacia.

#Utilizacion de Tuples (listas que no pueden cambiar). Inmutable.
(10, 20, 30, 45)
() #Tuple Vacia.
print(type((10, 20, 30)))

#Diccionarios, permiten agrupar datos de una misma identidad.
{
    "nombre": "Josue",
    "apellido": "Renteria",
    "apodo": "Joshue",
    "edad": 17
}
{} #Diccionario Vacio.
print(type({
    "nombre": "Josue",
    "apellido": "Renteria",
    "apodo": "Joshue",
    "edad": 17
}))

#Tipo de Dato que no esta Definido.
None
print(None)
print(type(None))
