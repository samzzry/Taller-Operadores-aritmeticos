# Volumen de una esfera

def definir_radio():
    radio = float(input("Ingrese el radio de la esfera: "))
    return radio

def calcular_volumen(radio):
    volumen = (4/3) * 3.1416 * (radio ** 3)
    return volumen

def imprimir_datos(radio):
    print("El radio es:", radio)

def imprimir_resultado(volumen):
    print("El volumen de la esfera es:", volumen)


# Programa principal
radio = definir_radio()
volumen = calcular_volumen(radio)

imprimir_datos(radio)
imprimir_resultado(volumen)
