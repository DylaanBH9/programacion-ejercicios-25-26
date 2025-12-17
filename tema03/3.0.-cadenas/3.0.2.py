'''
    Si me dan variable "fruta" que es de tipo string y seguido se ponen dos corchetes con dos puntos "[:]" se está
    haciendo un slicing de la cadena y al no especificar ningún parametro devuelve la cadena entera igual que la original.
'''

def main():
    fruta = "fruta"
    print(fruta)
    print(fruta[:])

if __name__ == '__main__':
    main()