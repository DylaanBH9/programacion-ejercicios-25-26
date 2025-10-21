def entrada_teclado():
	entrada = input("Introduzca un número: ")
	return entrada
	
def comprobar_entrada(total:int, cantidad:int) -> int:
	entrada = entrada_teclado()
	while entrada.lower() != "fin":
		if not entrada.isdigit():
			print("Entrada inválida")
		else: 
			total += int(entrada)
			cantidad += 1
		entrada = entrada_teclado()
	return total, cantidad
	
def procesamiento():
	total = 0
	cantidad = 0
	media = 0
	total, cantidad = comprobar_entrada(total, cantidad)
	if not cantidad == 0:
		media = (total / cantidad)
	print(f"{total} {cantidad} {media}")

if __name__ == "__main__":
	procesamiento()
