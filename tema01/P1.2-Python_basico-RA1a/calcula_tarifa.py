horas_trabajadas = ""
tarifa = ""

while not horas_trabajadas.isdigit():
	horas_trabajadas = input("¿Cuantas horas has trabajado?: ")

while not tarifa.isdigit():
	tarifa = input("¿Cual es tu tarifa?: ")

salario = int(horas_trabajadas) * int(tarifa)

print(f"Tu salario es {salario}€")
