#Ejercicio 6.

if __name__ == '__main__':
	x = int()
	a = int()
	peso_anterior = float()
	peso = float()
	suma = float()
	for x in range(1,6):
		print ("Persona"), x
		print ("Ingresa tu peso anterior")
		peso_anterior = float(raw_input())
		suma = 0
		for a in range(1,11):
			print ("Ingresa el peso"), a
			peso = float(raw_input())
			suma = suma+peso
		if suma/10==peso_anterior:
			print ("La persona ",x," se mantiene en el peso")
		else:
			if suma/10>peso_anterior:
				print ("La persona ",x," Subio")
			else:
				print ("La persona ",x," bajo")
		print ("")