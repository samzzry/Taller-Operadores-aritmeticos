#area de un trapecio
def definir_base_mayor():
    B = float(input("Ingrese la base mayor del trapecio: "))
    return B
def definir_base_menor():
    b = float(input("Ingrese la base menor del trapecio: "))
    return b
def definir_altura():
    h = float(input("Ingrese la altura del trapecio: "))
    return h
def calcular_area(B, b, h):
    area = ((B + b) * h) / 2
    return area
def imprimir_datos(B, b, h):
    print("Base mayor:", B)
    print("Base menor:", b)
    print("Altura:", h)
def imprimir_resultado(area):
    print("El área del trapecio es:", area)
# Programa principal
B = definir_base_mayor()
b = definir_base_menor()
h = definir_altura()
area = calcular_area(B, b, h)
imprimir_datos(B, b, h)
imprimir_resultado(area)