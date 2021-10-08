#Ejercicio 2.

if __name__ == '__main__':
	x = float()
	n = float()
	total = float()
	edad = float()
	categoria1 = float()
	categoria2 = float()
	categoria3 = float()
	animal = str()
	categoria1 = 0
	categoria2 = 0
	categoria3 = 0
	print ("Selecciona un animal")
	print ("1 = Elefantes")
	print ("2 = Jirafas")
	print ("3 = Chimpances")
	n = float(raw_input())
	if n>0 and n<4:
		if n==1:
			animal = "Elefantes"
			total = 20
		else:
			if n==2:
				animal = "Jirafas"
				total = 15
			else:
				animal = "Chimpances"
				total = 40
		for x in range(1,total+1):
			print ("Ingresa la edad: "), x
			edad = float(raw_input())
			if edad>=0 and edad<=1:
				categoria1 = categoria1+1
			else:
				if edad<3:
					categoria2 = categoria2+1
				else:
					categoria3 = categoria3+1
		print ("Porcentaje de edades de: "), animal
		print (categoria1/total)*100,"%: de 0 a 1 año "
		print (categoria2/total)*100,"%: de mas de 1 año y menos de 3 años "
		print (categoria3/total)*100,"%: de 3 años o mas "
	else:
		print ("Ingresa un animal correcto")