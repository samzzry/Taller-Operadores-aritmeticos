#la raiz cuadrada

def definir_numero():
    num = float(input("Ingrese un número: "))
    return num
def calcular_raiz(num):
    raiz = num ** 0.5
    return raiz
def imprimir_datos(num):
    print("el número ingresado es:", num)

def imprimir_resultado(raiz):
    print("la raíz cuadrada es:", raiz)
# Programa principal
numero = definir_numero()
resultado = calcular_raiz(numero)





imprimir_datos(numero)
imprimir_resultado(resultado)