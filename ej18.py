# are hexágono regular

import math

def definir_lado():
    lado = float(input("Ingrese el lado del hexágono: "))
    return lado
def calcular_area(lado):
    area = (3 * math.sqrt(3) / 2) * (lado ** 2)
    return area
def imprimir_datos(lado):
    print("El lado del hexágono es:", lado)
def imprimir_resultado(area):
    print("El área del hexágono es:", area)
# Programa principal
lado = definir_lado()
area = calcular_area(lado)
imprimir_datos(lado)
imprimir_resultado(area)