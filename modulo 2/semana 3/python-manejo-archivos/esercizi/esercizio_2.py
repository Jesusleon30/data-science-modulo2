# usando el with no es necesario cerrar basta que este dentro la function

with open('file.txt', 'w') as file: 
    while True:
        linea = input("escribe una linea (o 'salir' para terminar) :")
        if linea == "salir":
            break
        file.write(linea + '\n') # un salto de linea uno debajo de otro
        # file.write(linea + ' ') # un spazio vacio para separar las palabras
