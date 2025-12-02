# par
def definir_numero():
    num = int(input("Ingrese un número: "))
    return num
def calcular_paridad(num):
    if num % 2 == 0:
      palaridad="par"
    else:
        palaridad="impar"
        return palaridad
def imprimir_datos(num):
    print("numero ingresado:", num)
    
def imprimir_resultado(polaridad):
    print("el numero es", polaridad)
#programa principal
numero= definir_numero()
resultado = imprimir_resultado()
imprimir_datos(numero)
imprimir_resultado(resultado)