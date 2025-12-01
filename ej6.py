# cono

def definir_radio():
    radio = float(input("Ingrese el radio del cono: "))
    return radio
def definir_altura():
    altura = float(input("Ingrese la altura del cono: "))
    return altura
def calcular_volumen(radio, altura):
    volumen = (3.1416 * (radio ** 2) * altura) / 3
    return volumen

def imprimir_datos(radio, altura):
    print("El radio es:", radio)
    print("La altura es:", altura)
def imprimir_resultado(volumen):
    print("El volumen del cono es:", volumen)
# Programa principal
radio = definir_radio()
altura = definir_altura()
volumen = calcular_volumen(radio, altura)
imprimir_datos(radio, altura)
imprimir_resultado(volumen)