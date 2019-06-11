def DivisionIterativa(divisor, dividendo):
    resultado = 0

    while divisor > 0:
        resultado = resultado + 1
        divisor = divisor - dividendo

    return resultado

divisor = -1
dividendo = -1

while divisor <= 0 or dividendo <= 0:
    divisor = int(input("Digite el divisor: "))
    dividendo = int(input("Digite Dividendo: "))

    if divisor > 0 and dividendo > 0:
        resultado = DivisionIterativa(divisor, dividendo)
        print(resultado)
    else:
        print("Sólo positivos.")
