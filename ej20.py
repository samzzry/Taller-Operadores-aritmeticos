# cpnvertir litros a galones

def definir_litros():
    litros = float(input("Ingrese los litros a convertir: "))
    return litros
def convertir_galones(litros):
    galones = litros * 0.264172
    return galones
def imprimir_datos(litros):
    print("Litros ingresados:", litros)
def imprimir_resultado(galones):
    print("Equivalente en galones:", galones)
# Programa principal
litros = definir_litros()
galones = convertir_galones(litros)
imprimir_datos(litros)
imprimir_resultado(galones)
