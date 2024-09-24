"""
Abrir un archivo y pedir al usuario que escriba una linea (escribir en el archivo),
en caso escriba "salir", que termine el programa
"""

file = open("file", "w")

while True:
    linea = input("escribe una linea (o 'salir' para terminar) :")
    
    if linea == "salir":
        break

    file.write(linea) # escribir dentro il file creado

file.close()
