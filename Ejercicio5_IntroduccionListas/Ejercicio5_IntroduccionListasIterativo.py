def UnirListas(lista, sublista, enCola):
    posicion = len(lista) if enCola else 0

    for valor in sublista:
        lista.insert(posicion, valor)
        posicion += 1


listaVieja = [50, 60, 70, 80]

print(listaVieja)

subLista = []

respuesta = 's'
while respuesta == 's':
    subLista.append(int(input()))
    respuesta = input("Digite 'S' para otro valor").lower()

UnirListas(listaVieja, subLista, False if input("Digite 1 para agregar al inicio: ").lower() == "1" else True)

print(listaVieja)

# Eliminando una posicion:
pos = int(input("Digite la posición a eliminar: "))

'''
i = 0
copiaLista = listaVieja.copy() #list(listaVieja)
for valor in copiaLista:
    i+=1
    if i == pos:
        del copiaLista[i]
        break

print(copiaLista)
'''
copiaLista = []
for i, valor in enumerate(listaVieja):
    if i != pos:
        copiaLista.append(valor)


print(copiaLista)
listaVieja = copiaLista.copy()


valorEliminar = int(input("Digite el valor a eliminar: "))

YaEliminado = False
copiaLista = []
for i, valor in enumerate(listaVieja):
    if valor != valorEliminar or YaEliminado == True:
        copiaLista.append(valor)
    else:
        YaEliminado = True


print(copiaLista)
