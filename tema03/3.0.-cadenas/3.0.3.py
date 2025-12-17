def cuenta(palabra, letra_buscar):
    contador = 0
    for letra in palabra:
        if letra == letra_buscar:
            contador = contador + 1
    print(contador)

numero_de_os = cuenta("consuelo","o") # Resultado debe ser 2