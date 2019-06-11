from math import sqrt

def esPar(num):
    return num%2 == 0

def esPositivo(num):
    if num > 0:
        print("Es positivo.")
    elif num < 0:
        print("Es negativo.")
    else:
        print("Es cero.")

def esPrimo(num):
    k = 2

    while num % k != 0 and k <= sqrt(num):
        k += 1

    return k > sqrt(num)# ó: num % k != 0

bandera = 's'
cantidad = 0
suma = 0
cantidadPrimos = 0
sumaPrimos = 0

while bandera == 's':
    num = int(input("Digite un valor: "))
    cantidad += 1
    suma += num

    if(esPar(num)):
        print("Es par.")
    else:
        print("Impar.")

    esPositivo(num)

    if cantidad == 1:
        mayor = num
        menor = num
    elif num > mayor:
        mayor = num
    elif num < menor:
        menor = num

    if esPrimo(num):
        cantidadPrimos += 1
        sumaPrimos += num        

    bandera = input("Digite s para otro valor:").lower()

print("El mayor es: {0} y el menor es: {1}".format(mayor, menor))
print("Se capturaron {} números.".format(cantidad))
print("La suma es: {}".format(suma))
print("El promedio de los primos es: {0}".format(sumaPrimos / cantidadPrimos))








