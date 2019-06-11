Algoritmo InvertirNumero
	valor = -1
	Mientras valor <= 0 Hacer
		Escribir "Digite un valor: "
		Leer valor
		Si valor<=0 Entonces
			Escribir "Sólo positivos"
		FinSi
	FinMientras
	invertido = Invertir(valor)
	Escribir invertido
FinAlgoritmo

Funcion acumulado <- Invertir(num)
	acumulado = 0
	Mientras num>0 Hacer
		acumulado = acumulado * 10 + (num%10)
		num = trunc(num / 10)
	FinMientras
FinFuncion

