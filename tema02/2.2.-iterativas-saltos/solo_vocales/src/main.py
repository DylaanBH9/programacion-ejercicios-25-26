def entrada_teclado():
    entrada = input()
    return entrada

def saca_vocales(linea: str) -> str:
    lista_vocales = []
    vocales = "aeiouáéíóú"
    for letra in linea.lower():
        if letra in vocales:
            lista_vocales.append(letra)
    cadena_vocales = "".join(lista_vocales)
    return cadena_vocales

def main():
    entrada = entrada_teclado()
    resultado = saca_vocales(entrada)
    print(resultado)

if __name__ == '__main__':
    main()