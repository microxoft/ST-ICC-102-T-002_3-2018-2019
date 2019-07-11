t = int(input())
while(t>0):
    t-=1
    valores = input().split()
    primeraPalabra = list(valores[0] if len(valores[0]) > len(valores[1]) else valores[1])
    segundaPalabra = list(valores[1] if len(valores[0]) > len(valores[1]) else valores[0])
    palabraModificada = segundaPalabra.copy()
    cambiosModificada = 0
    cambios = 0

    i=0
    for i in range(len(primeraPalabra)):
        if i >= len(palabraModificada):
            cambiosModificada += 1
        elif primeraPalabra[i] != palabraModificada[i]:
            cambiosModificada += 1
            
        if i >= len(segundaPalabra):
            segundaPalabra.insert(i, primeraPalabra[i])
            cambios+=1
        if primeraPalabra[i] == segundaPalabra[i]:
            continue
        #Probando insertar:
        segundaPalabra.insert(i, primeraPalabra[i])
        cambios+=1
    if(len(primeraPalabra) != len(segundaPalabra) and cambiosModificada > 1):
        print("No")
    else:
        print(cambios)
        print(primeraPalabra)
        print(segundaPalabra)
        print("Si" if (cambios <= 1 or cambiosModificada <= 1) else "No")
        
