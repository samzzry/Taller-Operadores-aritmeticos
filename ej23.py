# producto de dos números

def definir_num1():
    num1 = float(input("Ingrese el primer número: "))
    return num1

def definir_num2():
    num2 = float(input("Ingrese el segundo número: "))
    return num2

def calcular_producto(num1, num2):
    producto = num1 * num2
    return producto

def imprimir_datos(num1, num2):
    print("Primer número:", num1)
    print("Segundo número:", num2)

def imprimir_resultado(producto):
    print("El producto de los números es:", producto)
# Programa principal
num1 = definir_num1()
num2 = definir_num2()
producto = calcular_producto(num1, num2)
imprimir_datos(num1, num2)
imprimir_resultado(producto)
