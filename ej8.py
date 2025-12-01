# convertir euros a dolares
def definir_dolares():
    dolares = float(input("Ingrese la cantidad de dólares: "))
    return dolares

def definir_tasa():
    tasa = float(input("Ingrese la tasa de cambio (1 dólar = cuántos euros): "))
    return tasa

def convertir_euros(dolares, tasa):
    euros = dolares * tasa
    return euros

def imprimir_datos(dolares, tasa):
    print("Dólares ingresados:", dolares)
    print("Tasa de cambio:", tasa)

def imprimir_resultado(euros):
    print("Equivalen a", euros, "euros")


# Programa principal
dolares = definir_dolares()
tasa = definir_tasa()
euros = convertir_euros(dolares, tasa)

imprimir_datos(dolares, tasa)
imprimir_resultado(euros)