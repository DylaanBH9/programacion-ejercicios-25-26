def entrada_teclado():
    try:
        return input()
    except EOFError:
        return "0"


def procesamiento(cantidad_piedras: int, linea_guijarros: str):
    """
    Procesa un caso de prueba para ver si los guijarros se pueden equilibrar.
    Esta versión USA BUCLES y no recursión.
    """
    # 1. Preparar los datos
    lista_guijarros = list(map(int, linea_guijarros.split()))
    peso_total = sum(lista_guijarros)

    # 2. Comprobación rápida
    if peso_total % 2 != 0:
        return "NO"

    peso_objetivo = peso_total // 2

    # 3. La búsqueda con bucles (Bitmasking)
    solucion_encontrada = False

    # El número total de combinaciones es 2 elevado a la cantidad de piedras.
    # Por ejemplo, para 3 piedras, hay 2^3 = 8 combinaciones (del 0 al 7).
    numero_combinaciones = 2**cantidad_piedras  # Esto es lo mismo que 2**cantidad_piedras

    # Bucle principal: recorre cada combinación posible, de 0 a (2^n - 1)
    for i in range(numero_combinaciones):
        suma_actual = 0

        # Bucle secundario: para la combinación 'i', revisamos qué piedras incluye.
        for j in range(cantidad_piedras):
            # Esta es la magia de los bits:
            # Comprueba si el j-ésimo bit de 'i' está encendido (es 1).
            # Si lo está, significa que debemos incluir la j-ésima piedra.
            if (i >> j) & 1:
                suma_actual += lista_guijarros[j]

        # Después de sumar todas las piedras de la combinación 'i', comprobamos
        if suma_actual == peso_objetivo:
            solucion_encontrada = True

    # 4. Devolver el resultado final
    if solucion_encontrada:
        return "SI"
    else:
        return "NO"


def mostrar_resultado(resultado_final):
    """Imprime en la pantalla lo que le pasen."""
    print(resultado_final)


def main():
    """Función principal que controla el flujo del programa."""
    entrada = entrada_teclado()
    while entrada and entrada != "0":
        n_piedras = int(entrada)
        entrada_guijarros = entrada_teclado()
        resultado = procesamiento(n_piedras, entrada_guijarros)
        mostrar_resultado(resultado)
        entrada = entrada_teclado()


if __name__ == '__main__':
    main()

    while suma_total != peso_objetivo or suma_total >peso_objetivo:
        for i in range(n_combinaciones_totales):
