ruta_archivo = "lorem.txt"

with open(ruta_archivo) as archivo:
    # Aqui leemos el archivo y lo guaradamos.
    contenido = archivo.read()

    # Quitamos los saltos de linea.
    lineas = contenido.split("\n")

# Mostrar los elementos.
print(contenido)
print(lineas)

for l in lineas:
    print(l)

# Contar las lineas del archivo.
print(l[:50] + "...")

# Contar las lineas del archivo.
print(len(lineas))
