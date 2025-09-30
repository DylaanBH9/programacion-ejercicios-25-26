num = ""
while not num.isdigit():
	num = input("Introduce el numero que quieres multiplicar del 1 al 10: ")
cont_multiplicacion = 1
num = int(num)
while cont_multiplicacion  <= 10:
	print(f" {num} * {cont_multiplicacion} = {num * cont_multiplicacion}")
	cont_multiplicacion += 1
