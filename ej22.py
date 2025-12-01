# resta de dos números

def definir_num1():
    num1 = float(input("Ingrese el primer número: "))
    return num1
def definir_num2():
    num2 = float(input("Ingrese el segundo número: "))
    return num2
def calcular_resta(num1, num2):
    resta = num1 - num2
    return resta
def imprimir_datos(num1, num2):
    print("Primer número:", num1)
    print("Segundo número:", num2)
def imprimir_resultado(resta):
    print("La resta es:", resta)











# Programa principal
num1 = definir_num1()
num2 = definir_num2()
resta = calcular_resta(num1, num2)
imprimir_datos(num1, num2)
imprimir_resultado(resta)
