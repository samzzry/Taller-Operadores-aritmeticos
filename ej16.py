# Volumen de un cubo

def definir_lado():
    lado = float(input("Ingrese la longitud del lado del cubo: "))
    return lado

def calcular_volumen(lado):
    volumen = lado ** 3
    return volumen

def imprimir_datos(lado):
    print("El lado del cubo es:", lado)

def imprimir_resultado(volumen):
    print("El volumen del cubo es:", volumen)


# Programa principal
lado = definir_lado()
volumen = calcular_volumen(lado)

imprimir_datos(lado)
imprimir_resultado(volumen)
