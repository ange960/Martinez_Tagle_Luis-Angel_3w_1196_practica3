print("")#imprime espacio en blanco 
print("Martinez Tagle Luis Angel 3w 1196 Este programa solicita e imprime la divisa ")#imprime el titulo y nombre 
print("")#imprime el espacio en blanco 
# Diccionario de divisas con sus símbolos
divisas = {'Euro': '€', 'Dollar': '$', 'Yen': '¥'}


# Diccionario de divisas
divisas = {'Euro': '€', 'Dollar': '$', 'Yen': '¥'}

while True:
    # Solicitar divisa al usuario
    entrada = input("Introduce una divisa (Euro, Dollar, Yen) o 'salir': ")
    
    # Salir del programa si el usuario lo desea
    if entrada == 'salir':
        break
    
    # Mostrar el símbolo de la divisa o un mensaje de error
    print(divisas.get(entrada, "La divisa no está en el diccionario."))

