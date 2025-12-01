# paralelogramo

def definir_base():
    base = float(input("Ingrese la base del paralelogramo: "))
    return base
def definir_altura():
    altura = float(input("Ingrese la altura del paralelogramo: "))
    return altura
def calcular_area(base, altura):
    area = base * altura
    return area
def imprimir_datos(base, altura):
    print("La base es:", base)
    print("La altura es:", altura)
def imprimir_resultado(area):
    print("El área del paralelogramo es:", area)

# Programa principal
base = definir_base()
altura = definir_altura()
area = calcular_area(base, altura)
imprimir_datos(base, altura)
imprimir_resultado(area)
