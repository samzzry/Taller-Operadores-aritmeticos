

def definir_longitud():
    longitud = float(input("Ingrese la longitud del prisma: "))
    return longitud

def definir_ancho():
    ancho = float(input("Ingrese el ancho del prisma: "))
    return ancho

def definir_altura():
    altura = float(input("Ingrese la altura del prisma: "))
    return altura

def calcular_volumen(longitud, ancho, altura):
    volumen = longitud * ancho * altura
    return volumen

def imprimir_datos(longitud, ancho, altura):
    print("La longitud es:", longitud)
    print("El ancho es:", ancho)
    print("La altura es:", altura)

def imprimir_resultado(volumen):
    print("El volumen del prisma rectangular es:", volumen)


# Programa principal
longitud = definir_longitud()
ancho = definir_ancho()
altura = definir_altura()

volumen = calcular_volumen(longitud, ancho, altura)

imprimir_datos(longitud, ancho, altura)
imprimir_resultado(volumen)
