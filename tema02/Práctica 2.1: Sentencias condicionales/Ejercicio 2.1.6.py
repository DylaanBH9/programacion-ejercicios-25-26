def main():
    nombre, sexo = pedir_nombre_sexo()
    letra = nombre[0]
    if not nombre.isalpha():
        print("Tiene que introducir un nombre válido (solo letras).")
        return
    clasificador_alumnos(letra, sexo)

def clasificador_alumnos(letra: str, sexo: str):
    if sexo.lower() == "mujer":
        if letra.lower() < "m":
            print("Perteneces al grupo A")
        else:
            print("Perteneces al grupo B")
    elif sexo.lower() == "hombre":
        if letra.lower() > "n":
            print("Perteneces al grupo A")
        else:
            print("Perteneces al grupo B")
    else:
        print("Su sexo debe ser 'hombre' o 'mujer'")


def pedir_nombre_sexo() -> tuple[str, str]:
    nombre = input(">> ¿Como te llamas?: ")
    sexo = input(">> ¿De que sexo eres?: ")
    return nombre, sexo


if __name__ == '__main__':
    main()