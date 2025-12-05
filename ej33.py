def definir_kilometros():
    km = float(input("Ingrese distancia en kilometros: "))
    return km

def convertir_millas(km):
    millas = km * 0.621371
    return millas

def imprimir_datos(km):
    print("Kilometros ingresados:", km)

def imprimir_resultado(millas):
    print("Equivale a", millas, "millas")


km = definir_kilometros()
millas = convertir_millas(km)

imprimir_datos(km)
imprimir_resultado(millas)