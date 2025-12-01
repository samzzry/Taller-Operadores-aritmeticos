# volumen de un prisma triangular

def definir_base():
    base = float(input("Ingrese la base del triángulo: "))
    return base

def definir_altura():
    altura = float(input("Ingrese la altura del triángulo: "))
    return altura

def definir_largo():
    largo = float(input("Ingrese el largo del prisma: "))
    return largo

def calcular_volumen(base, altura, largo):
    area_triangulo = (base * altura) / 2
    volumen = area_triangulo * largo
    return volumen

def imprimir_datos(base, altura, largo):
    print("Base:", base)
    print("Altura:", altura)
    print("Largo del prisma:", largo)

def imprimir_resultado(volumen):
    print("El volumen del prisma triangular es:", volumen)






# Programa principal
base = definir_base()
altura = definir_altura()
largo = definir_largo()

volumen = calcular_volumen(base, altura, largo)

imprimir_datos(base, altura, largo)
imprimir_resultado(volumen)
