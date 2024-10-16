print("")#imprime espacio en blanco 
print("Martinez Tagle Luis Angel 3w 1196 Este programa de calcular y tomar el precio de las frutas   ")#imprime el titulo y nombre 
print("")#imprime el espacio en blanco 


# Diccionario con precios de frutas
precios_frutas = {
    'manzana': 3.0,
    'guanabana ': 2.5,
    'granada': 4.0,
    'kiwi': 5.0
}

# Solicitar fruta y kilos al usuario
fruta = input("Introduce una fruta (manzana, guanabana, granada,kiwi): ").lower()
kilos = float(input("Introduce el número de kilos: "))

# Calcular y mostrar el precio si la fruta está en el diccionario
if fruta in precios_frutas:
    precio_total = precios_frutas[fruta] * kilos
    print(f"El precio de {kilos} kilos de {fruta} es: €{precio_total:.2f}")
else:
    print("La fruta no está disponible.")
