def transponer(matriz):
    matriz_transpuesta = []
    filas = len(matriz)
    columnas = len(matriz[0])
    for columna in range(columnas):
        nueva_fila = []
        for fila in range(filas):
            nueva_fila.append(matriz[fila][columna])
        matriz_transpuesta.append(nueva_fila)

    return matriz_transpuesta


if __name__ == '__main__':
    print(transponer([[1, 2, 3],
                      [4, 5, 6]]))