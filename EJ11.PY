# kilómetros a millas

def definir_kilometros():
    km = float(input("Ingrese los kilómetros a convertir: "))
    return km

def convertir_millas(km):
    millas = km * 0.621371
    return millas

def imprimir_datos(km):
    print("Los kilómetros ingresados son:", km)

def imprimir_resultado(millas):
    print("Equivalente en millas:", millas)


# Programa principal
km = definir_kilometros()
millas = convertir_millas(km)

imprimir_datos(km)
imprimir_resultado(millas)
