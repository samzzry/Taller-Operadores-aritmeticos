# eej horas a minutos

def definir_horas():
    horas = float(input("Ingrese número de horas: "))
    return horas

def calcular_minutos(horas):
    minutos = horas * 60
    return minutos

def imprimir_datos(horas):
    print("Horas ingresadas:", horas)

def imprimir_resultado(minutos):
    print("Equivalen a:", minutos, "minutos")


# Programa principal
horas = definir_horas()
resultado = calcular_minutos(horas)

imprimir_datos(horas)
imprimir_resultado(resultado)