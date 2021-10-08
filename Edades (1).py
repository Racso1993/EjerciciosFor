# Ejercicio 4.

if __name__ == '__main__':
	total = int()
	edad = int()
	suma = int()
	promedio = float()
	print ("Ingresa el total de alumnos")
	total = int(raw_input())
	x = 1
	suma = 0
	while x<=total:
		print ("Ingresa tu edad")
		edad = int(raw_input())
		suma = suma+edad
		x = x+1
	print ("El promedio de edades de todo el grupo es: "), suma/total