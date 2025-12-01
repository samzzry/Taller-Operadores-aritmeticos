# convertir libras a kilogramos

def definir_libras():
    libras = float(input("Ingrese las libras a convertir: "))
    return libras

def convertir_kilos(libras):
    kilos = libras * 0.453592
    return kilos

def imprimir_datos(libras):
    print("Libras ingresadas:", libras)

def imprimir_resultado(kilos):
    print("Equivalente en kilogramos:", kilos)


# Programa principal
libras = definir_libras()
kilos = convertir_kilos(libras)

imprimir_datos(libras)
imprimir_resultado(kilos)
