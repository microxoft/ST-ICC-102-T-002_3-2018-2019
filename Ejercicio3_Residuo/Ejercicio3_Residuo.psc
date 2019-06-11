Algoritmo ModuloIterativo
	divisor = -1
	dividendo = -1
	Mientras divisor < 0 o dividendo < 0 Hacer
		Escribir "Digite el divisor: "
		Leer divisor
		Escribir "Digite el dividendo: "
		Leer dividendo
		Si divisor > 0 y dividendo > 0 Entonces
			resultado = CalcularResiduo(divisor, dividendo)
		SiNo
			Escribir "Sólo positivos."
		FinSi
	FinMientras
	Escribir resultado
FinAlgoritmo

Funcion divisor <- CalcularResiduo(divisor, dividendo)
	Mientras divisor > dividendo Hacer
		divisor = divisor - dividendo
	FinMientras
FinFuncion

