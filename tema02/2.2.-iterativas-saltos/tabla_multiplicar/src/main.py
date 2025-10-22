def main():
    entrada = int(input("¿De que numero quieres la tabla de multiplicar?: "))
    for i in range(1, 11):
        multiplicacion = entrada * i
        print(f"{entrada} * {i} = {multiplicacion}")

if __name__ == '__main__':
    main()
