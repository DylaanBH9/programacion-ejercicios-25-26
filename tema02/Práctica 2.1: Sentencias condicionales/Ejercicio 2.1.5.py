def main():
    edad, ingresos = entrada_datos()
    procesamiento(edad, ingresos)

def procesamiento(edad: str, ingresos: str):
    if int(edad) >= 16 and int(ingresos) >= 1000:
        print("Debe tributar")
    else:
        print("No debe tributar")

def entrada_datos() -> tuple[str, str]:
    edad = input(">> ¿Cuantos años tienes?: ")
    ingresos = input(">> ¿Cuales son tus ingresos mensuales?: ")
    return edad, ingresos

if __name__ == '__main__':
    main()