def entrada_teclado():
    return input(">> Introduzca una palabra: ")

def procesamiento(palabra):
    longitud = len(palabra)
    contador = longitud -1
    while contador >= 0:
        print(palabra[contador])
        contador -= 1

def main():
    entrada = entrada_teclado()
    procesamiento(entrada)

if __name__ == '__main__':
    main()