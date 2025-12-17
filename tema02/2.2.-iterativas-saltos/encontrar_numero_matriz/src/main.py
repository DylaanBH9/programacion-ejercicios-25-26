def main_for():
    matriz = [[1 , 2 ,3], [4, 5, 6], [7, 8, 9]]
    numero = int(input(">> "))
    fila_resultado = 0
    columna_resultado = 0
    encontrado = False
    for filas in range(len(matriz)):
        for columnas in range(len(matriz[filas])):
            if matriz[filas][columnas] == numero:
                fila_resultado = filas
                columna_resultado = columnas
                encontrado = True

    if encontrado:
        print(f"Elemento encontrado en fila: {fila_resultado}, columna: {columna_resultado}.")
    else:
        print("Elemento no encontrado")

def main_while():
    matriz = [[1 , 2 ,3], [4, 5, 6], [7, 8, 9]]
    numero = int(input(">> "))
    fila_resultado = 0
    columna_resultado = 0
    filas = 0
    columnas = 0
    encontrado = False
    filas_matriz = len(matriz)
    columnas_matriz = len(matriz[filas_matriz -1])
    while not encontrado and filas < filas_matriz:
        while not encontrado and columnas < columnas_matriz:
            if matriz[filas][columnas] == numero:
                fila_resultado = filas
                columna_resultado = columnas
                encontrado = True
            columnas += 1
        filas += 1
        #REINICIO COLUMNAS
        columnas = 0

    if encontrado:
        print(f"Elemento encontrado en fila: {fila_resultado}, columna: {columna_resultado}.")
    else:
        print("Elemento no encontrado")

if __name__ == "__main__":
    main_while()