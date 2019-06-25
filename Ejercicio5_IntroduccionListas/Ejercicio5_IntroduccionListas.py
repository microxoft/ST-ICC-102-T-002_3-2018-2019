def MostrarMenu():
    opcion = -1

    while opcion < 0 or opcion > 7:
        print("Seleccione una opción del menú:\n\n")
        print("\t1: Capturar una lista.")
        print("\t*2: Sacar los últimos J valores.")
        print("\t*3: Invertir lista.")
        print("\t*4: Mostrar sub-conjunto.")
        print("\t5: Mostrar elemento dada una posición.")
        print("\t*6: Buscar un elemento.")
        print("\t7: Modificar la lista.")
        print("\n\n\t0: Salir.")

        opcion = int(input("Opción: "))

    return opcion

def MostrarSubMenu():
    opcion = -1

    while opcion < 0 or opcion > 6:
        print("Seleccione una opción del submenú:\n\n")
        print("\t*1: Agregar elemento al final de la lista.")
        print("\t*2: Agregar elemento al inicio de la lista.")
        print("\t*3: Agregar elemento en una posición dada.")
        print("\t*4: Agregar una nueva lista.")
        print("\t5: Eliminar un elemento de una posición dada.")
        print("\t*6: Buscar y eliminar un elemento.")
        print("\n\n\t0: Volver al menú anterior.")

        opcion = int(input("Opción: "))

    return opcion

def CapturarLista():
    nuevaLista = []
    
    #for valorActual in input().split():
    #    nuevaLista.append(int(valorActual))
    
    #nuevaLista = (list(map(int, input().split())))

    nuevaLista = [int(valor) for valor in input().split()]

    return nuevaLista

def SacarValores(lista, j):
    while j>0:
        print(lista.pop())
        j-=1

    return lista

def InvertirLista(lista):
    return lista[::-1]

def SubConjunto(lista, d, h, s):
    return lista[d:h:s]

def ObtenerElemento(lista, posicion):
    return lista[posicion]

def BusquedaSecuencial(lista, valor):
    return lista.index(valor)
    #for (indice, valorActual) in enumerate(lista):
    #    if valorActual == valor:
    #        return indice
    #return -1

def AgregarElemento(lista, elemento, posicion):
    lista.insert(posicion, elemento)

def AgregarNuevaLista(lista, alFinal):
    nuevaLista = CapturarLista()

    return lista + nuevaLista if alFinal else nuevaLista + lista
    """if alFinal:
        return lista.extend(nuevaLista)
    else:
        return nuevaLista.extend(lista)"""

def EliminarPosicion(lista, posicion):
    del lista[posicion]

def EliminarElemento(lista, elemento):
    try:
        lista.remove(elemento)
    except:
        print("{0} no está en la lista.".format(elemento))
        
listado = []
seleccion = -1

while seleccion != 0:
    print("La lista es: {0}, y su longitud {1}".format(listado, len(listado)))
    seleccion = MostrarMenu()

    if seleccion == 1:
        listado = CapturarLista()
    elif seleccion == 2:
        nuevaEntrada = int(input("Digite la cantidad de valores a sacar: "))
        listado = SacarValores(listado, nuevaEntrada)
    elif seleccion == 3:
        print(InvertirLista(listado))
    elif seleccion == 4:
        desde = int(input("Desde: "))
        hasta = int(input("Hasta: "))
        step = int(input("Step: "))
        SubConjunto(listado, desde, hasta, step)
    elif seleccion == 5:
        pos = int(input("Digite la posición: "))
        print(ObtenerElemento(listado, pos))
    elif seleccion == 6:
        val = int(input("Digite el valor: "))
        print(BusquedaSecuencial(listado, val))
    elif seleccion == 7:
        nuevaSeleccion = -1

        while nuevaSeleccion != 0:
            nuevaSeleccion = MostrarSubMenu()

            if nuevaSeleccion == 1:
                AgregarElemento(listado, int(input("Digite el nuevo valor: ")), len(listado))
            elif nuevaSeleccion == 2:
                AgregarElemento(listado, int(input("Digite el nuevo valor: ")), 0)
            elif nuevaSeleccion == 3:
                AgregarElemento(listado, int(input("Digite el nuevo valor: ")), int(input("Indique la posición: ")))
            elif nuevaSeleccion == 4:
                alFinal = input("Digite 1 para agregar al inicio, o 2 para agregar al final.") == "2"
                listado = AgregarNuevaLista(listado, alFinal)
            elif nuevaSeleccion == 5:
                EliminarPosicion(listado, int(input("Digite la posición a eliminar: ")))
            elif nuevaSeleccion == 6:
                EliminarElemento(listado, int(input("Digite el elemento a eliminar: ")))






        
