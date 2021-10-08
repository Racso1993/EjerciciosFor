#Ejercicio 3.

if __name__ == '__main__':
	x = int()
	n = int()
	horas = int()
	hora_extra = int()
	salario = float()
	print ("Escribe el numero de trabajadores")
	n = int(raw_input())
	x = 1
	while x<=n:
		print ("Escribe el numero de horas trabajadas")
		horas = int(raw_input())
		if horas<=40:
			salario = horas*20
		else:
			hora_extra = horas-40
			salario = 40*20+(hora_extra*25)
		print ("El salario del trabajador ",x," es: $"), salario
		x = x+1