# circunferencia de un círculo

def definir_radio():
    radio = float(input("Ingrese el radio del círculo: "))
    return radio
def calcular_circunferencia(radio):
    circunferencia = 2 * 3.1416 * radio
    return circunferencia
def imprimir_datos(radio):
    print("Radio:", radio)
def imprimir_resultado(circunferencia):
    print("La circunferencia del círculo es:", circunferencia)
# Programa principal
radio = definir_radio()
resultado = calcular_circunferencia(radio)
imprimir_datos(radio)
imprimir_resultado(resultado)