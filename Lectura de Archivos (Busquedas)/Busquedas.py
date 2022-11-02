ruta_archivo = "canales.txt"

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
print(len(lineas))

# Buscar un elemento.
print("Joshue Games" in lineas)
print(lineas.index("Joshue Games")) # Retornar la posicion donde se encuentra.
print(lineas.count("Joshue Games")) # Si encuentra una coincidencia (cantidad).
