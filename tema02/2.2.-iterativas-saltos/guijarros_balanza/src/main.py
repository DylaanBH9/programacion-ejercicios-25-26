def entrada_teclado():
    entrada = input()
    return entrada

def procesamiento(cantidad_piedras: int, linea: str):
    n_combinaciones_totales = 2**cantidad_piedras
    lista_guijarros = [int(num) for num in linea.split()]
    peso_total = sum(lista_guijarros)
    peso_objetivo = peso_total / 2
    suma_total = 0
    l_lista = len(lista_guijarros)
    for j in range(0, l_lista - 1):
        guijarro_actual = lista_guijarros.pop(j)
        suma_total += guijarro_actual
        if suma_total == peso_objetivo:
            return "SI"
        elif suma_total != peso_objetivo:

        elif suma_total != peso_objetivo:



def mostrar_resultado(resultado_final):
    print(resultado_final)

def main():
    entrada = entrada_teclado()
    while entrada != "0":
        n_piedras = int(entrada)
        entrada_guijarros = entrada_teclado()
        resultado = procesamiento(n_piedras, entrada_guijarros)
        mostrar_resultado(resultado)
        entrada = entrada_teclado()

if __name__ == '__main__':
    main()