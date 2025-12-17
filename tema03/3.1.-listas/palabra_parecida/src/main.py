from wordfreq import top_n_list
import random

def generar_palabras() -> list[str]:
    # "en" o "es" según idioma; 5000 -> tamaño de la lista de las más frecuentes
    words = top_n_list("es", 5000)  # cambia a "en" si quieres inglés
    candidates = [w for w in words if w.isalpha() and 4 <= len(w) <= 8]
    word_list = []
    for _ in range(10):
        word_list.append(random.choice(candidates).lower())
    return word_list


def quitar_tildes(lista_palabras):
    lista_palabras_sin_tildes = []
    for palabra_original in lista_palabras:
        lista_caracteres = list(palabra_original)
        for posicion, caracter in enumerate(palabra_original):
            if caracter == 'á':
                lista_caracteres[posicion] = 'a'
            elif caracter == 'é':
                lista_caracteres[posicion] = 'e'
            elif caracter == 'í':
                lista_caracteres[posicion] = 'i'
            elif caracter == 'ó':
                lista_caracteres[posicion] = 'o'
            elif caracter == 'ú':
                lista_caracteres[posicion] = 'u'

        palabra_sin_tildes = "".join(lista_caracteres)
        lista_palabras_sin_tildes.append(palabra_sin_tildes)

    return lista_palabras_sin_tildes

def solicitar_palabra() -> str:
    palabra = input(">> Introduzca una palabra: ").lower()
    return palabra

def contar_letras(lista_palabras: list[str], palabra_usuario: str):
    contador_letras = None
    lista_resultados = []
    for palabra_lista in lista_palabras:
        contador_letras = 0
        for caracter_usuario in palabra_usuario:
            for caracter_palabra in palabra_lista:
                if caracter_usuario == caracter_palabra:
                    contador_letras += 1
        lista_resultados.append([palabra_lista, contador_letras])
    return lista_resultados

def ordenar_lista(lista_original):
    lista_ordenada = lista_original.copy()
    longitud_lista = len(lista_ordenada)
    for contador in range(longitud_lista):
        for numero_actual in range(longitud_lista - contador - 1):
            if lista_ordenada[numero_actual][1] < lista_ordenada[numero_actual + 1][1]:
                num1 = lista_ordenada[numero_actual]
                num2 = lista_ordenada[numero_actual + 1]
                lista_ordenada[numero_actual + 1] = num1
                lista_ordenada[numero_actual] = num2
    return lista_ordenada

def mostrar_resultado(lista_ordenada, palabra_usuario: str):
    print(f'\nLISTA DE PALABRAS CON MAS COINCIDENCIAS CON "{palabra_usuario.upper()}": ')
    indice = 0
    for palabra, contador in lista_ordenada:
        indice += 1
        print(f"{indice}. {palabra.upper()}: {contador}")

def main():
    lista_palabras = generar_palabras()
    lista_palabras_sin_tildes = quitar_tildes(lista_palabras)
    palabra_usuario = solicitar_palabra()
    lista_resultados = contar_letras(lista_palabras_sin_tildes, palabra_usuario)
    lista_ordenada = ordenar_lista(lista_resultados)
    mostrar_resultado(lista_ordenada, palabra_usuario)

if __name__ == "__main__":
    main()