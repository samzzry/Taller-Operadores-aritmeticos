def definir_longitud():
    longitud = float(input("Ingrese la longitud: "))
    return longitud

def definir_ancho():
    ancho = float(input("Ingrese el ancho: "))
    return ancho

def calcular_area(longitud, ancho):
    area = longitud * ancho
    return area

def imprimir_datos(longitud, ancho):
    print("Longitud:", longitud)
    print("Ancho:", ancho)

def imprimir_resultado(area):
    print("El area del rectangulo es:", area)


longitud = definir_longitud()
ancho = definir_ancho()
area = calcular_area(longitud, ancho)

imprimir_datos(longitud, ancho)
imprimir_resultado(area)