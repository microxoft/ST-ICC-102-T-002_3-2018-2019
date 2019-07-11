import random

def BusquedaLineal(lista, valor):
    for posActual in range(len(lista)):
        if lista[posActual] == valor:
            return posActual
    return -1

def BusquedaBinaria(lista, valor):
    limI = 0
    limS = len(lista) - 1
    while limI<limS:
        posCentral = int(limI/2 + limS/2)
        if lista[posCentral] == valor:
            return posCentral
        elif lista[posCentral] > valor:
            limS = posCentral - 1
        else:
            limI = posCentral + 1
    return -1

def GenerarAleatorios(cantidad):
    nuevaLista = []
    while cantidad > 0:
        cantidad -= 1
        nuevaLista.append(random.randrange(100, 1000))

    return nuevaLista

def OrdenarBurbuja(lista):
    for i in range(len(lista)):
        for j in range(len(lista)-1-i):
            if lista[j] > lista[j+1]:
                aux = lista[j]
                lista[j] = lista[j+1]
                lista[j+1] = aux

def OrdenarSeleccion(lista):
    for i in range(len(lista)):
        minimo = i
        for j in range(i+1, len(lista)):
            if lista[j] < lista[minimo]:
                minimo = j
        aux = lista[i]
        lista[i] = lista[minimo]
        lista[minimo] = aux

def OrdenarInsercion(lista):
    for i in range(1, len(lista)):
        valorActual = lista[i]
        j = i - 1
        while j >= 0 and lista[j]>valorActual:
            lista[j+1] = lista[j]
            j = j - 1
        lista[j+1] = valorActual

#valores = [float(x) for x in input().split()]
valores = GenerarAleatorios(100)
valores2 = list(valores)
valores3 = list(valores)
print(valores)
print("Ordenados:")
OrdenarInsercion(valores)
OrdenarBurbuja(valores2)
OrdenarSeleccion(valores3)
print(valores)
print(valores2)
print(valores3)
destino = float(input())
#resultado = BusquedaLineal(valores, destino)
#print("No encontró el valor" if resultado < 0 else "El valor está en {0}".format(resultado))
resultado = BusquedaBinaria(valores, destino)
print("No encontró el valor" if resultado < 0 else "El valor está en {0}".format(resultado))
