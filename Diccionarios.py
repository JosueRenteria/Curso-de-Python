#Titulo Programa: Diccionarios
#Fecha: 03-Septiembre-2022
#Autor: Renteria Arriaga Josue

#Formas para definir un Diccionario.
from unicodedata import name


productos = {
    "nombre": "libro",
    "cantidad": 3,
    "precio": 4.99
}

#Definir objetos de la vida Real.
persona = {
    "Nombre": "Josue",
    "Apellido": "Renteria"
}

#Observar su tipo de Dato y sus Metodos.
print(type(persona))
    # print(dir(persona))

#Ejemplos de Algunos metodos que se pueden usar para los Diccionarios.
print(persona.keys()) #Valores de las Llaves.
print(persona.items()) #Obtener los Datos.

#Limpiar el Diccionario.
persona.clear()
print(persona)

#Eliminar el Diccionario.
del persona

#Diccionarios dentro de una Lista
productos = [
    {"name": "libro", "precio": 34},
    {"name": "laptop"}
]
print(productos)
