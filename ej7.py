#  Convertir Celsius a Fahrenheit

def definir_celsius():
    c = float(input("Ingrese los grados Celsius: "))
    return c
def convertir_fahrenheit(c):
    f = (c * 9/5) + 32
    return f
def imprimir_datos(c):
    print("Los grados Celsius ingresados son:", c)
def imprimir_resultado(f):
    print("Equivalen a", f, "grados Fahrenheit")
# Programa principal
c = definir_celsius()
f = convertir_fahrenheit(c)
imprimir_datos(c)
imprimir_resultado(f)