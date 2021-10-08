#Ejercicio 7.

if __name__ == '__main__':
	cantidad = int()
	total = float()
	precio = float()
	respuesta = str()
	total = 0
	respuesta = ""
	while True:# no hay 'repetir' en python
		print ("Ingresa la cantidad de articulos")
		cantidad = int(raw_input())
		print ("Ingresa el precio del articulo")
		precio = float(raw_input())
		total = total+(cantidad*precio)
		print ("Desea finalizar la compra:")
		respuesta = raw_input()
		if respuesta=="si" or respuesta=="SI": break
	print ("El total a pagar por los articulos es: $"),total