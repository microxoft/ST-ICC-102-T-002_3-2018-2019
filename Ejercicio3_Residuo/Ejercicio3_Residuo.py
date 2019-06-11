def CalcularResiduo(divisor, dividendo):
    while divisor > dividendo:
        divisor = divisor - dividendo

    return divisor

divisor = -1
dividendo = -1

while divisor < 0 or dividendo < 0:
    divisor = int(input("Digite el divisor: "))
    dividendo = int(input("Digite el dividendo: "))

    if divisor < 0 or dividendo < 0:
        print("Sólo positivos.")
    else:
        resultado = CalcularResiduo(divisor, dividendo)
print(resultado)
