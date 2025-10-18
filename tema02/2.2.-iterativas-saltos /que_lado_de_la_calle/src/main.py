def procesamiento(linea: str) -> str:
    if (linea % 2 == 0):
        return "DERECHA"
    else:
        return "IZQUIERDA"

def main():
    linea = input()
    while linea != "0":
        lado_calle = procesamiento(linea)
        print(lado_calle)
        linea = input()
if __name__ == "__main__":
    main()