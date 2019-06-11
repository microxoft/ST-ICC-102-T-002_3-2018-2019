Algoritmo potenciaIterativa
	base = -1
	exponente = -1
	Mientras base<=0 o exponente<=0 Hacer
		Escribir "Digite la base: "
		Leer base
		Escribir "Digite el exponente: "
		Leer exponente
		Si base<=0 o exponente<=0 Entonces
			Escribir "Sólo positivos"
		FinSi
	FinMientras
	potencia = CalcularPotencia(base, exponente)
	Escribir potencia
FinAlgoritmo

Funcion acumulado <- CalcularPotencia(b, e)
	acumulado = 1
	Mientras e>0 Hacer
		acumulado = acumulado * b
		e = e - 1
	FinMientras
FinFuncion

