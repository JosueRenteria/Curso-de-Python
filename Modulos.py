#Titulo Programa: Modulos.
#Fecha: 03-Septiembre-2022
#Autor: Renteria Arriaga Josue

#Para Aplicaciones reales y ocupar algo ya hecho (Evitar repeticiones).
#Modulos Creados.
#Modulos Descargados.
#Modulos de Python.

#pagina para importar modulos de la comunidad https://pypi.org

#Importar los Modulos.
import datetime
from lib2to3.pytree import convert
print(datetime.date.today())
print(datetime.timedelta(minutes = 70))

#Importar solo el metodo del Modulo. 
from datetime import timedelta, date 
print(date.today())

#Crear nuestro propio Modulo.
import fmath
fmath.add(10, 1)
fmath.substract(10, 2)

#Importar solo el metodo del Modulo. 
from fmath import add, substract 
add(13, 45)
substract(123, 27)
