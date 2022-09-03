#Titulo Programa: Listas
#Fecha: 03-Septiembre-2022
#Autor: Renteria Arriaga Josue

#Formas de Construir una Lista.
from operator import truediv


lista_demo = [1, "Hola Mundo", True, [1, 2, 3]]
colores = ['Rojo', 'Azul', 'Rojo', 'Amarillo']

#Utilizacion de un constructor para definir listas.
lista_numeros = list((1, 2, 3, 4)) #Veamos que se ocupa una Tuple para crear la lista.
print(lista_numeros)
print(type(lista_numeros))

#Crear una lista basada en un rango.
rango_lista = list(range(1, 11)) #Range es un rango dependiendo de los parametros.
print(rango_lista)

#Obtener informacion de una lista.
print("Saber informacion de la Lista Colores:")
print(type(colores))
    # print(dir(colores))
print(len(colores)) #Tamaño de la lista.
print(colores[1]) #Ver la posicion de la lista (tambien indices inversos).
print("verde" in colores) #Ver si un dato esta en la lista.

#Reasignar valores de una lista.
print(colores)
colores[1] = "Cafe"
print(colores)

#Agregar un elemento a la lista.
colores.append("Violeta")
colores.extend(["Negro", "Blanco"]) #Para agregar dos o mas se hace con Extend.
colores.extend(("Rosa", "Purpura")) #Utilizando una Tuples.
print(colores)

#Insertar un elemento despues de otro elemento.
colores.insert(4, "Plateado") #Tambien se puede en inverso con el -1.
print(colores)
colores.insert(len(colores), "Dorado") #Agregar al final de la lista.
print(colores)

#Remover elementos de una Lista.
colores.pop() #Este es para sacar el ultimo de la lista.
print(colores)
colores.remove("Plateado") #Quitar por el nombre del color.
print(colores)
colores.pop(2) #Por un indice
print(colores)

#Para ordenar los Datos de la Lista.
colores.sort() #Ordena Alfabeticamente la Lista.
print(colores)
colores.sort(reverse = True) #Ordena Alfabeticamente la Lista, pero, Inversamente.
print(colores)
print(colores.index("Rojo")) #Optener Indices de los Datos de las Listas.
print(colores.count("Rojo")) #Contar las veces que se repite un Dato en la Lista.

#Para limpiar o borrar todos los datos de las Listas (Lista Vacia).
colores.clear()
print(colores)