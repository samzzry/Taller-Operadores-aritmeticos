def definir_numero1():
    num1 = int(input("Ingrese el primer numero: "))
    return num1

def definir_numero2():
    num2 = int(input("Ingrese el segundo numero: "))
    return num2

def calcular_multiplo(num1, num2):
    if num1 % num2 == 0:
        resultado = "El numero es multiplo."
    else:
        resultado = "El numero no es multiplo."
    return resultado

def imprimir_datos(num1, num2):
    print("Primer numero:", num1)
    print("Segundo numero:", num2)

def imprimir_resultado(resultado):
    print(resultado)


num1 = definir_numero1()
num2 = definir_numero2()

resultado = calcular_multiplo(num1, num2)

imprimir_datos(num1, num2)
imprimir_resultado(resultado)