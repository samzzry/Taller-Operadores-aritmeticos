#precio articulo

def definir_precio():
    precio = float(input("Ingrese el precio del articulo: "))
    return precio

def calcular_descuento(precio):
    descuento = precio * 0.10
    return descuento

def imprimir_datos(precio):
    print("Precio del articulo:", precio)

def imprimir_resultado(descuento):
    print("El descuento del 10 por ciento es:", descuento)

    #codigo principal


precio = definir_precio()
descuento = calcular_descuento(precio)

imprimir_datos(precio)
imprimir_resultado(descuento)