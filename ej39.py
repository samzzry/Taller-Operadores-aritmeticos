def definir_numero1():
    num1 = float(input("Ingrese el primer numero: "))
    return num1

def definir_numero2():
    num2 = float(input("Ingrese el segundo numero: "))
    return num2

def calcular_promedio(num1, num2):
    promedio = (num1 + num2) / 2
    return promedio

def imprimir_datos(num1, num2):
    print("Primer numero:", num1)
    print("Segundo numero:", num2)

def imprimir_resultado(promedio):
    print("El promedio es:", promedio)


num1 = definir_numero1()
num2 = definir_numero2()

promedio = calcular_promedio(num1, num2)

imprimir_datos(num1, num2)
imprimir_resultado(promedio)