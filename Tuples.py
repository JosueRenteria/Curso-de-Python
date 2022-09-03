#Titulo Programa: Tuples
#Fecha: 03-Septiembre-2022
#Autor: Renteria Arriaga Josue
#Nos sirven para definir un conjunto de Datos pero estos no se pueden Modificar (Datos Inmutables).

#Formar para crear una Tuples.
x = (1, 2, 3) #Tuples con un solo Dato no se considera una Tuple.
print(x)
y = tuple((2, 3, 4)) #A partir de un constructor al igual que en las listas. 
print(y)
    # print(dir(x))

#Ocupar o Mostrar algun elemento de la Tuples.
x = (1, 2, 3, 4, 5)
print(x[0])

#Eliminar una Tuple. 
del x

#Diccionarios de Localizaciones (Implementacion de Tuples).
locations = {
    (35.1231, 39.45): "Tokio",
    (35.124, 32.245): "New York"
}