#Definimos el nombre del archivo
file_name = "my_notes.txt"

#Modo de apertura: "r" para lectura (read)
#Abrimos el archivo que acabamos de crear
archivo = open(file_name, "r")

#Leemos el contenido e imprimimos
#contenido = archivo.read()

for Pasatiempo in archivo:
    print(Pasatiempo)

#Cerramos el archivo
archivo.close()