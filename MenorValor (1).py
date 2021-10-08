#Ejercicio 5.

if __name__ == '__main__':
	x = int()
	n = int()
	total = int()
	numero_menor = int()
	print ("Escribe el total de numeros a calcular")
	total = int(raw_input())
	x = 1
	while x<=total:
		print ("Escribe un nuemro")
		n = int(raw_input())
		if x==1:
			numero_menor = n
		else:
			if n<numero_menor:
				numero_menor = n
		x = x+1
	print ("El numero menor es: "), numero_menor