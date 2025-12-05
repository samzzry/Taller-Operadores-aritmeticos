def definir_cantidad():
    cantidad = float(input("Ingrese la cantidad de dinero: "))
    return cantidad

def calcular_interes(cantidad):
    interes = cantidad * 0.05
    return interes

def imprimir_datos(cantidad):
    print("Cantidad ingresada:", cantidad)

def imprimir_resultado(interes):
    print("El interes del 5 por ciento es:", interes)


cantidad = definir_cantidad()
interes = calcular_interes(cantidad)

imprimir_datos(cantidad)
imprimir_resultado(interes)