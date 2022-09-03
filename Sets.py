#Titulo Programa: Sets
#Fecha: 03-Septiembre-2022
#Autor: Renteria Arriaga Josue

#Coleccion Desordenada sin Indices (Estructura).
colores = {'Rojo', 'Verde', 'Azul'}
print(colores)
print(type(colores))

#Mostrar o Decir si un Dato esta en el Set (Forma Boolean).
print('Rojo' in colores)

#Agregar Datos al Set, pero, este se agrega al azar.
colores.add('Violeta')
print(colores)

#Para remover un Dato del Set.
colores.remove('Rojo')
print(colores)

#Limpiar o Borrar el set.
colores.clear()
print(colores)
del colores #Eliminar la Variable o el Set.