#Titulo Programa: Numeros
#Fecha: 03-Septiembre-2022
#Autor: Renteria Arriaga Josue

#Operaciones en Python
print(1 + 1)
print(1.15 + 29) #Devuelve un flotante.
print(2**3) #Para la exponencial
print(3 // 2 ) #Operador de Modulo.
print(3 % 2) #Residuo de la Operacion.

#Tabla de Presedencia.
print(20 - 10 / 5 * 3**2)
print((20 - 10) / (5 * 3)**2)

#Programa que pide Datos Al usuario, input() para resivir datos.
edad = input("Inserte su Edad: ") #Todo lo que se resive es un String.
print(type(edad))
print(type(int(edad)))
nueva_edad = int(edad) * 2 #Convertimos edad a un numero.
print(nueva_edad)