#convertir pulgadas a centímetros

def definir_pulgadas():
    pulgadas = float(input("Ingrese las pulgadas: "))
    return pulgadas
def convertir_cm(pulgadas):
    cm = pulgadas * 2.54
    return cm
def imprimir_datos(pulgadas):
    print("Pulgadas ingresadas:", pulgadas)







def imprimir_resultado(cm):
    print("Equivalente en centímetros:", cm)

# Programa principal
pulgadas = definir_pulgadas()
cm = convertir_cm(pulgadas)

imprimir_datos(pulgadas)
imprimir_resultado(cm)
