# Evolumen de una pirámide

def definir_largo():
    largo = float(input("Ingrese el largo de la base: "))
    return largo
def definir_ancho():
    ancho = float(input("Ingrese el ancho de la base: "))
    return ancho
def definir_altura():
    altura = float(input("Ingrese la altura de la pirámide: "))
    return altura
def calcular_volumen(largo, ancho, altura):
    area_base = largo * ancho
    volumen = (area_base * altura) / 3
    return volumen
def imprimir_datos(largo, ancho, altura):
    print("Largo de la base:", largo)
    print("Ancho de la base:", ancho)
    print("Altura:", altura)
def imprimir_resultado(volumen):
    print("El volumen de la pirámide es:", volumen)
# rograma principal
largo = definir_largo()
ancho = definir_ancho()
altura = definir_altura()

volumen = calcular_volumen(largo, ancho, altura)

imprimir_datos(largo, ancho, altura)
imprimir_resultado(volumen)
