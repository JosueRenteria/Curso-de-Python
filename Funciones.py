#Titulo Programa: Funciones.
#Fecha: 03-Septiembre-2022
#Autor: Renteria Arriaga Josue

#Porcion de codigo que noscpuede devuelve algo (Datos).
def Hola(nombre = ""): #def hace referencia que es una Definicion de Funcion.
    print("Hola Mundo " + nombre)

#Llamar la funcion para que se ejecute.
Hola("Josue")
Hola("Paco")

#Para utilizar la funcion sin ningun parametro, aunque lo pida hay que definir uno por default.
Hola() #Parametros por defecto

#Funcion que retorne algo.
def suma(x, y):
    return x + y

#Utilizacion de la Funcion de Suma.
valor = suma(10, 1)
print(valor)
print(suma(11, 1))

#--------------FUNCIONES LAMBDA (Sin nombre)--------------
add = lambda numero1, numero2: numero1 + numero2
print(add(20, 21))

