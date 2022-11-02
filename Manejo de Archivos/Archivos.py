# EJEMPLO 1
"""
# Funcion para abir y leer archivos ('r' = Metodo de Lectura).
file = open("data1.txt", 'r')

# Este prin nos nuestra la informacion general del archivo.
print(file)

# Leer su contenido (Crea una lista de elementos por lineas).
lineas = file.readlines()
print(lineas)

# Cerramos nuestro Archivo (para que no este desprotegido).
file.close()
"""

# EJEMPLO 2
"""
# Indica que con este archivo abierto lo vamos a ocupar con un alias.
# La diferencia es que el archivo se cerrara al terminar la consulta.
with open("data2.txt", "r") as archivo:
    lineas = archivo.readlines()
    print(lineas)

# Podemos ocupar las variables que creamos, pero, ya no hacer nada con el archivo.
print(lineas)

# Mostramos las lineas por separado.
for l in lineas:
    # Quitamos el \n que se genera automaticamente.
    print(l.replace("\n", ""))
"""

# Ejemplo 3
""" 
with open("data2.txt", "r") as archivo:
    # Aqui leemos el archivo y lo guaradamos.
    contenido = archivo.read()
    # Quitamos los saltos de linea.
    lineas = contenido.split("\n")
    print(lineas)
"""

# Ejemplo 4
""" 
with open("data2.txt", "r") as archivo:
    # Aqui leemos el archivo y lo guaradamos.
    contenido = archivo.read()

    # Quitamos los saltos de linea.
    lineas = contenido.split("\n")

    # Saber la posicion que nos encontramos del archivo.
    posicion = archivo.tell()

    # Mostramos el tamaño de la longuitud
    print(posicion)
    print("El archivo tiene {0} caracteres de longuitud".format(posicion))
""" 

# Ejemplo 5
""" 
with open("data2.txt", "r") as archivo:
    # Ubica la lectura en una posicion en especifico.
    archivo.seek(7)

    # Saber la posicion que nos encontramos del archivo.
    posicion = archivo.tell()

    # Mostramos el tamaño de la longuitud
    print(posicion)

    # Aqui leemos el archivo y lo guaradamos.
    contenido = archivo.read()

    # Quitamos los saltos de linea.
    lineas = contenido.split("\n")

    print(lineas)
""" 

# Ejemplo 6
""" 
with open("data2.txt", "r") as archivo:
    # Solo nos muestra los caracteres que se indicaron.
    siguientes4 = archivo.read(10) # Caracteres a leer.
    print(siguientes4)
""" 

# Ejemplo 7
""" 
with open("data2.txt", "r") as archivo:
    print(type(archivo.read())) # Deberia mostrar un String.

with open("data2.txt", "rb") as archivo:
    print(type(archivo.read())) # Deberia mostrar que lo lee en bytes.
""" 

# Ejemplo 8
""" 
# Este metodo crea y escribe en un archivo.
with open("data3.txt", "w") as archivo:
    # Si se corre 2 veces se sobreescribe.
    archivo.write("Josue\nRenteria\nArriaga123")
""" 

# Este metodo crea y escribe en un archivo.
with open("data3.txt", "a") as archivo:
    # Si se corre 2 veces al final se escribe de nuevo el contenido.
    archivo.write("Josue\nRenteria\nArriaga123\ncls")