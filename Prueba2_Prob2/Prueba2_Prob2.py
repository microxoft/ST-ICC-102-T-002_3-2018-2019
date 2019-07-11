t = int(input())

while t > 0:
    t -= 1

    textoEntrada = input()
    textoNuevo = []

    for letraActual in textoEntrada:
        if letraActual.lower() >= 'a' and letraActual.lower() <= 'z':
            textoNuevo.append(letraActual.lower())

    if textoNuevo == textoNuevo[::-1]:
        print("Si")
    else:
        print("No")
