# area de un triángulo

def definir_base():
    base = float(input("Ingrese la base del triángulo: "))
    return base

def definir_altura():
    altura = float(input("Ingrese la altura del triángulo: "))
    return altura
def calcular_area(base, altura):
    area = (base * altura) / 2
    return area
def imprimir_datos(base, altura):
    print("base:", base)
    print("altura:", altura)
def imprimir_resultado(area):
    print("e area del triángulo es:", area)
# Programa principal
base = definir_base()
altura = definir_altura()
resultado = calcular_area(base, altura)
imprimir_datos(base, altura)
imprimir_resultado(resultado)