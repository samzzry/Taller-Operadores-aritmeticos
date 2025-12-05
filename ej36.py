def definir_numero1():
    num1 = int(input("Ingrese el primer numero: "))
    return num1

def definir_numero2():
    num2 = int(input("Ingrese el segundo numero: "))
    return num2

def calcular_cociente(num1, num2):
    cociente = num1 // num2
    return cociente

def imprimir_datos(num1, num2):
    print("Primer numero:", num1)
    print("Segundo numero:", num2)

def imprimir_resultado(cociente):
    print("El cociente entero es:", cociente)


num1 = definir_numero1()
num2 = definir_numero2()

cociente = calcular_cociente(num1, num2)

imprimir_datos(num1, num2)
imprimir_resultado(cociente)