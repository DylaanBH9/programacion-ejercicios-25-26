def procesamiento(linea: str) -> int:
    entrada_h = int(linea[:2])
    entrada_min = int(linea[3:])
    horas_restantes = 23 - entrada_h
    minutos_restantes_h = horas_restantes * 60
    minutos_restantes_min = 60 - entrada_min
    minutos_restantes_totales = minutos_restantes_h + minutos_restantes_min
    return minutos_restantes_totales

def main():
    linea = input()
    while linea != "00:00":
        resultado = procesamiento(linea)
        print(f"Faltan {resultado} minutos para medianoche.")
        linea = input()


if __name__ == "__main__":
    main()