# el area de un cuadrado

def definir_lado():
    lado = float(input("Ingrese el lado del cuadrado: "))
    return lado

def calcular_area(lado):
    area = lado * lado
    return area

def imprimir_datos(lado):
    print("El lado del cuadrado es:", lado)

def imprimir_resultado(area):
    print("El área del cuadrado es:", area)


# Programa principal
lado = definir_lado()
area = calcular_area(lado)

imprimir_datos(lado)
imprimir_resultado(area)
