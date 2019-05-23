Algoritmo tablaUsuario
	Escribir 'Digite la tabla que desea: '
	Leer tabla
	multiplicando <- 1
	suma = 0
	Mientras multiplicando<=12 Hacer
		nuevoValor <- tabla*multiplicando
		Escribir tabla,'*',multiplicando,'=',nuevoValor
		multiplicando <- multiplicando+1
		suma = suma+nuevoValor
	FinMientras
	Escribir suma
FinAlgoritmo

