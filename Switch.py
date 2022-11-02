# En Python es diferente esta sentencia y se hace con diccionarios.
# Ejemplo: El usuario nos da el numero del mes y pasamos a letra.

def Mes(numero):
    seleccion = {
        1: "Enero",
        2: "Febrero",
        3: "Marzo",
        4: "Abril",
        5: "Mayo",
        6: "Junio"
    }
    return seleccion.get(numero, "No valido")

print(Mes(2))