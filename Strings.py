#Titulo Programa: Strings
#Fecha: 03-Septiembre-2022
#Autor: Renteria Arriaga Josue

#Declaracion de variables.
from msilib import MSIMODIFY_UPDATE
from re import M


myStr = "Hola Mundo"

#mostrar que podemos hacer con un tipo de variables, optecion de los metodos.
    # print(dir(myStr))

#Utlizacion de metodos para los Strings.
print(myStr.upper()) #Mayusculas.
print(myStr.lower()) #Minusculas.
print(myStr.swapcase()) #Cambia el tamaño de las letras.
print(myStr.capitalize()) #Primera letra de cada palabra en mayuscula.
print(myStr.replace("Hola", "Adios")) #Remplaza los textos

#Aplicar Metos tras Metodos (Metodos Encadenados).
print(myStr.replace("Hola", "Adios").upper())

print(myStr.count('l')) #Ver cuantas letras hay en  un String.
print(myStr.startswith('Hola')) #Ver si la cadena inicia con estra palabra o caracter.
print(myStr.endswith("Mundo")) #Ver si la cadena termina con estra palabra o caracter.

#Dividir la cadena en dos variables (se crea una lista y agruparlos).
myStr2 = "Hola,Mundo"
print(myStr.split()) #Lo separa por espacios (por defecto).
print(myStr2.split(',')) #Lo separa donde este una ,
print(myStr.split('o')) #Separar por letras

#Buscar la pocicion donde se encuentra el primer caracter (Indice).
print(myStr.find('o'))
print(len(myStr)) #Longuitud del String.
print(myStr.index('o')) #Tambien Buscar el indice (recibir entradas de usuarios).

#Saber el Tipo de Dato del String.
print(myStr.isnumeric())
print(myStr.isalpha())

#Mostrar solo el caracter de esa posicion.
print(myStr[3])
print(myStr[-1]) #En vez de los negativos te muestra de atras a adelante.

#Para concatenar con variables.
print("My name is:" + " " + myStr)
print(f"My Name is: {myStr}") #Dentro del texto hay una variable (Python 3.6+).
print("My Name is: {0}".format(myStr))