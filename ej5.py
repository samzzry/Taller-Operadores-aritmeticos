# EJERCICIO 5 - Área de un círculo

def definir_radio():
    radio = float(input("Ingrese el radio del círculo: "))
    return radio

def calcular_area(radio):
    area = 3.1416 * (radio ** 2)
    return area

def imprimir_datos(radio):
    print("El radio es:", radio)

def imprimir_resultado(area):
    print("El área del círculo es:", area)


# Programa principal
radio = definir_radio()
area = calcular_area(radio)

imprimir_datos(radio)
imprimir_resultado(area)