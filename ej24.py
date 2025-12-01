# cuadrado de un número

def definir_numero():
    num = float(input("Ingrese un número: "))
    return num
def calcular_cuadrado(num):
    cuadrado = num * num
    return cuadrado
def imprimir_datos(num):
    print("Número ingresado:", num)
def imprimir_resultado(cuadrado):
    print("El cuadrado del número es:", cuadrado)
# Programa principal
num = definir_numero()
cuadrado = calcular_cuadrado(num)

imprimir_datos(num)
imprimir_resultado(cuadrado)
