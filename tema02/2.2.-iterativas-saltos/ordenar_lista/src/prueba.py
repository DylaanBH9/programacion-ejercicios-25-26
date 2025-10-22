def ordenamiento_burbuja(lista):
    """
    Ordena una lista de números utilizando el algoritmo de burbuja.
    """
    n = len(lista)  # Obtenemos la cantidad de elementos en la lista

    # Recorremos todos los elementos de la lista
    for i in range(n):   # El último i elementos ya están en su lugar, por eso el -i-1
        for j in range(0, n - 1):

                # Comparamos el elemento actual con el siguiente
            if lista[j] > lista[j + 1]:
                    # Si el elemento actual es mayor que el siguiente, los intercambiamos
                lista[j], lista[j + 1] = lista[j + 1], lista[j]


# --- Ejemplo de uso ---

# 1. Creamos una lista desordenada
mi_lista = [64, 34, 25, 12, 22, 11, 90]

print("Lista original:", mi_lista)

# 2. Llamamos a nuestra función para que la ordene
ordenamiento_burbuja(mi_lista)

# 3. Imprimimos el resultado
print("Lista ordenada:", mi_lista)