#Ejercicio 8.

if __name__ == '__main__':
	edad = int()
	respuesta = int()
	precio = float()
	descuento = float()
	categoria1 = float()
	categoria2 = float()
	categoria3 = float()
	categoria4 = float()
	categoria5 = float()
	total = float()
	categoria1 = 0
	categoria2 = 0
	categoria3 = 0
	categoria4 = 0
	categoria5 = 0
	total = 0
	print ("Ingresa el precio del boleto")
	precio = float(raw_input())
	while True:# no hay 'repetir' en python
		print ("Ingresa la edad")
		edad = int(raw_input())
		if edad<5:
			print ("No se permiten menores de 5 años")
			if edad<=14:
				descuento = (precio*.35)
				categoria1 = categoria1+descuento
			else:
				if edad<=19:
					descuento = (precio*.25)
					categoria2 = categoria2+descuento
				else:
					if edad<=45:
						descuento = (precio*.10)
						categoria3 = categoria3+descuento
					else:
						if edad<=65:
							descuento = (precio*.25)
							categoria4 = categoria4+descuento
						else:
							descuento = (precio*.35)
							categoria5 = categoria5+descuento
			total = total+descuento
			print ("El descuento aplicado es: $"),descuento
		print ("Desea continuar: 1 = salir - otro numero para continuar")
		respuesta = int(raw_input())
		if respuesta==1: break
	print ("El descuento total en la categoria 1 es: $"),categoria1
	print ("El descuento total en la categoria 2 es: $"),categoria2
	print ("El descuento total en la categoria 3 es: $"),categoria3
	print ("El descuento total en la categoria 4 es: $"),categoria4
	print ("El descuento total en la categoria 5 es: $"),categoria5
	print ("El descuento total es: $"),total