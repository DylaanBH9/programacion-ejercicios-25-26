def entrada_teclado():
    entrada = input()
    return entrada

def procesamiento(linea: str) -> int:
    ano = int(linea)
    if ano % 400 == 0:
        return 29
    elif ano % 4 == 0 and ano % 100 != 0:
        return 29
    else:
        return 28

def main():
    n_comprobaciones = int(entrada_teclado())
    while n_comprobaciones > 0:
        entrada = entrada_teclado()
        resultado = procesamiento(entrada)
        print(resultado)
        n_comprobaciones -= 1

if __name__ == "__main__":
    main()