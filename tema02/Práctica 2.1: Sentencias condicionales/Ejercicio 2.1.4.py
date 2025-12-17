def main() -> None:
    numero = pedir_numero()
    comprobar_numero(numero)

def comprobar_numero(numero: str):
    if not numero.isdigit():
        print("El numero debe ser un digito")
    else:
        par_impar(numero)

def pedir_numero() -> str:
    numero = input(">> Escribe un numero: ")
    return numero

def par_impar(numero: str):
    if int(numero) % 2 == 0:
        print("El numero es par")
    else:
        print("El numero es impar")

if __name__ == '__main__':
    main()