valores = [int(x) for x in input().split()]

sumatoriaMax = 0
cantidadMax = 0
sumatoria = valores[0]
cantidad = 1
i = 1
potencia2 = 0

while i < len(valores):
    if valores[i-1] - 2**potencia2 == valores[i]:
        cantidad += 1
        sumatoria += valores[i]
        potencia2+=1
    else:
        if sumatoria > sumatoriaMax or cantidadMax == 0:
            sumatoriaMax = sumatoria
            cantidadMax = cantidad
        sumatoria = valores[i]
        cantidad = 1
        potencia2 = 0
    
    i+=1

print(sumatoriaMax / cantidadMax)
