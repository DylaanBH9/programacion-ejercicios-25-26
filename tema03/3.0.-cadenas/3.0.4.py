def cuenta(palabra):
    for letra in palabra:
        contador = palabra.find(letra)
        print(letra, contador)

numero_de_os = cuenta("banana")