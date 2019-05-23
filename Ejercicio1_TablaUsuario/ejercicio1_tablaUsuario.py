def MostrarTabla(tablaMultiplicar):
    multiplicando = 1
    suma = 0

    while multiplicando <= 12:
        nuevoValor = tablaMultiplicar * multiplicando
        print("{0}*{1}={2}".format(tablaMultiplicar, multiplicando, nuevoValor))
        multiplicando = multiplicando + 1
        suma = suma + nuevoValor

    return suma

tabla = int(input("Digite la tabla que desea: "))

resultado = MostrarTabla(tabla)

print(resultado)
