num = ""
while not num.isdigit():
	num = input("¿Qué  numero quieres saber si es primo?: ")
num = int(num)
if num  <= 1:
	print(f"El numero {num} no es primo")
else:
	cont_divisiones = 0
	num_divisor = 1
	while num_divisor <= num:
		if (num % num_divisor == 0):
			cont_divisiones += 1
		num_divisor += 1
	if (cont_divisiones == 2):
		print(f"El numero {num} es primo")
	else:
		print(f"El numero {num} no es primo")
