# area de un triagulo
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
    print("La base es:", base)
    print("La altura es:", altura)
def imprimir_resultado(area):
    print("El área del triángulo es:", area)
# Progrma principal
base = definir_base()
altura = definir_altura()
area = calcular_area(base, altura)
imprimir_datos(base, altura)
imprimir_resultado(area)


