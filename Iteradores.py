#Titulo Programa: Iteradores
#Fecha: 03-Septiembre-2022
#Autor: Renteria Arriaga Josue

#Definicion de la Lista o Arreglo.
comidas = ['manzanas', 'pan', 'leche', 'queso']

#----------------BUCLE FOR----------------
#Declaracion del For.
for comida in comidas:
    if comida == 'leche':
        print(f"Compra {comida}.")
        break #Rompe el Bucle for.
    elif comida == 'manzanas':
        continue #Ya no muestra este valor y sigue en el Bucle.
    print(comida)


#Recorrer rangos (number es la nueva variable que se crea y se ocupa para ir mostrando variable por variable).
for number in range(1, 8):
    print(number)

#Recorrer cada letra de una cadena.
for letra in "Hello":
    print(letra)

#----------------BUCLE WHILE----------------
#Declaracion del While.
count = 4
while count <= 10:
    print(count)
    count = count + 1