limS = 11
limI = 0

intento = int(input())
respuesta = input()
while respuesta != "correcto":
    if respuesta == "muy alto" and limS > intento:
        limS = intento - 1
    elif respuesta == "muy bajo" and limI < intento:
        limI = intento + 1

    intento = int(input())
    respuesta = input()

if intento < limI or intento > limS:
    print("María es deshonesta")
elif limI > limS:
    print("María es deshonesta")
else:
    print("María es honesta")
