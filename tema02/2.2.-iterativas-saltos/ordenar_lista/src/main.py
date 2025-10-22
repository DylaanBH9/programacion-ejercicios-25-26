def main():
    lista_original = [3, 7, 2, 9, 4 ,11]
    lista_ordenada = lista_original.copy()
    n = len(lista_ordenada)
    for contador in range(n):
        for numero_actual in range(n - 1):
            if lista_ordenada[numero_actual] > lista_ordenada[numero_actual + 1]:
                lista_ordenada[numero_actual], lista_ordenada[numero_actual + 1] = lista_ordenada[numero_actual + 1], lista_ordenada[numero_actual]
    print(lista_ordenada)

if __name__ == '__main__':
    main()
