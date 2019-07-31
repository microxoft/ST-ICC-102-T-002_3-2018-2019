import time

factores = [2520, 11, 13, 16, 17, 19]
bandera = True
proximoIntento = 2521
tiempoDesde = time.perf_counter()

while(bandera):
    bandera = False
    for factorActual in factores:
        if proximoIntento % factorActual != 0:
            bandera = True

    if not bandera:
        tiempoHasta = time.perf_counter()
        print(tiempoHasta - tiempoDesde)
        print(proximoIntento) # 232792560
        
    proximoIntento+=1

