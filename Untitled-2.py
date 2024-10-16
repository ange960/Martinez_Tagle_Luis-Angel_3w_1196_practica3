print("")#imprime espacio en blanco 
print("Martinez Tagle Luis Angel 3w 1196 Este programa introduce tu informacion personal  ")#imprime el titulo y nombre 
print("")#imprime el espacio en blanco 
# Solicitar información al usuario
nombre = input("Introduce tu nombre: ")
edad = input("Introduce tu edad: ")
direccion = input("Introduce tu dirección: ")
telefono = input("Introduce tu número de teléfono: ")

# Guardar la información en un diccionario
usuario = {
    'nombre': nombre,
    'edad': edad,
    'direccion': direccion,
    'telefono': telefono
}

# Mostrar la información en el formato deseado
print(f"{usuario['nombre']} tiene {usuario['edad']} años,")#esta linea imprime tu informacion 
print(f"vive en {usuario['direccion']} y su número de teléfono es {usuario['telefono']}.")#esta liena imprime el numero 
