def entrada_teclado() -> int:
    return int(input())

def mostrar_resultado(filas: int):
    for fila in range (1, filas + 1):
        print("*" * fila)

def main():
    n_filas = entrada_teclado()
    mostrar_resultado(n_filas)

if __name__ == "__main__":
    main()