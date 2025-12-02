# Residuo de una disvision
def definir_numero1():
    num1 = float(input("Ingrese el primer número: "))
    return num1
def definir_numero2():
    num2 = float(input("Ingrese el segundo número: "))
    return num2
def calcular_residuo(num1, num2):
    residuo = num1 % num2
    return residuo
def imprimir_datos(num1, num2):
    print("Primer número:", num1)
    print("Segundo número:", num2)
def imprimir_resultado(residuo):
    print("El residuo de la división es:", residuo)
# Programa principal
numero1 = definir_numero1()
numero2 = definir_numero2()
resultado = calcular_residuo(numero1, numero2)
imprimir_datos(numero1, numero2)
imprimir_resultado(resultado)