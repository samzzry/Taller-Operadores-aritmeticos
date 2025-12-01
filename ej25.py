#  division entre dos números

def definir_num1():
    num1 = float(input("Ingrese el primer número: "))
    return num1

def definir_num2():
    num2 = float(input("Ingrese el segundo número: "))
    return num2

def calcular_division(num1, num2):
    division = num1 / num2
    return division

def imprimir_datos(num1, num2):
    print("Primer número:", num1)
    print("Segundo número:", num2)

def imprimir_resultado(division):
    print("El resultado de la división es:", division)


# Programa principal
num1 = definir_num1()
num2 = definir_num2()

division = calcular_division(num1, num2)

imprimir_datos(num1, num2)
imprimir_resultado(division)
