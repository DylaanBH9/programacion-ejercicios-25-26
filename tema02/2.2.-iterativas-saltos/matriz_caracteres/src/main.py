def main():
    numero_caracteres = int(input(">> "))
    for linea in range(1, numero_caracteres + 1):
        for columna in range(linea):
            print("*", end="")
        print("\n")

if __name__ == "__main__":
    main()