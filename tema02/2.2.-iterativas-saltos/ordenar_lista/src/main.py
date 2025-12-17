def main():
    lista_original = [3, 7, 2, 9, 4 ,1]
    lista_ordenada = lista_original.copy()
    longitud_lista = len(lista_ordenada)
    for contador in range(longitud_lista):
        for numero_actual in range(longitud_lista - contador - 1):
            if lista_ordenada[numero_actual] > lista_ordenada[numero_actual + 1]:
                num1 = lista_ordenada[numero_actual]
                num2 = lista_ordenada[numero_actual + 1]
                lista_ordenada[numero_actual + 1] = num1
                lista_ordenada[numero_actual] = num2
    print(lista_ordenada)

if __name__ == '__main__':
    main()
