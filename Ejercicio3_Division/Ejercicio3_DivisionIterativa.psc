Algoritmo Division
	divisor <- -1
	dividendo <- -1
	Mientras divisor<=0 O dividendo<=0 Hacer
		Escribir 'Digite el divisor: '
		Leer divisor
		Escribir 'Digite el dividendo: '
		Leer dividendo
		Si divisor>0 Y dividendo>0 Entonces
			resultado <- DivisionIterativa(divisor, dividendo)
			Escribir resultado
		SiNo
			Escribir 'Sólo positivos'
		FinSi
	FinMientras
FinAlgoritmo

Funcion resultado <- DivisionIterativa(divisor, dividendo)
	resultado = 0
	Mientras divisor>0 Hacer
		resultado = resultado + 1
		divisor = divisor - dividendo
	FinMientras
FinFuncion

