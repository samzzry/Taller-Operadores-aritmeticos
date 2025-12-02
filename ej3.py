# area rectangulo
def definir_longitud():
    longitud = float(input("Ingrese la longitud del rectángulo: "))
    return longitud
def definir_ancho():
    ancho = float(input("Ingrese el ancho del rectángulo: "))
    return ancho
def calcular_area(longitud, ancho):
    area = longitud * ancho
    return area
def imprimir_datos(longitud, ancho):
    print("La longitud es:", longitud)
    print("El ancho es:", ancho)
def imprimir_resultado(area):
    print("El área del rectángulo es:", area)
# Programa principal
longitud = definir_longitud()
ancho = definir_ancho()
area = calcular_area(longitud, ancho)
imprimir_datos(longitud, ancho)
imprimir_resultado(area)
