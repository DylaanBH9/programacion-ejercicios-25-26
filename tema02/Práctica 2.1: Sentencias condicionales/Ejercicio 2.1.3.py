def pedir_numeros() -> list[str]:
    numeros = input(">> ¿Que numeros quieres dividir?: ")
    return numeros.split()

def comprobar_numeros(numero1:str, numero2:str) -> tuple[int, int] | None:
    if not numero1.isdigit():
        print("El primer termino debe ser un numero")
        return None
    if not numero2.isdigit():
        print("El segundo termino debe ser un numero")
        return None
    if numero2 == "0":
        print("El divisor no puede ser 0")
        return None

    return int(numero1), int(numero2)

def calculo(numero1, numero2) -> None:
    print(f"{numero1 / numero2 = }")

def main() -> None:
    global numero1, numero2
    try:
        numero1, numero2 = pedir_numeros()
    except ValueError:
        print("Debes introducir dos números separados por un espacio.")
        return
    numeros_validados = comprobar_numeros(numero1, numero2)
    if numeros_validados is not None:
        numero1_comprobado, numero2_comprobado = numeros_validados
        calculo(numero1_comprobado, numero2_comprobado)

if __name__ == '__main__':
    main()