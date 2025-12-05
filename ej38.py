def definir_numero1():
    num1 = float(input("Ingrese el primer numero: "))
    return num1

def definir_numero2():
    num2 = float(input("Ingrese el segundo numero: "))
    return num2

def calcular_mayor(num1, num2):
    if num1 > num2:
        mayor = num1
    else:
        mayor = num2
    return mayor

def imprimir_datos(num1, num2):
    print("Primer numero:", num1)
    print("Segundo numero:", num2)

def imprimir_resultado(mayor):
    print("El numero mayor es:", mayor)


num1 = definir_numero1()
num2 = definir_numero2()

mayor = calcular_mayor(num1, num2)

imprimir_datos(num1, num2)
imprimir_resultado(mayor)