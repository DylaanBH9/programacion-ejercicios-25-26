def main():
    renta_anual = entrada_renta()
    renta_anual_int: int = int(renta_anual)
    clasificacion_renta(renta_anual_int)

def clasificacion_renta(renta_anual_int: int):
    if renta_anual_int < 0:
        print("La renta anual no puede ser negativa")
    elif renta_anual_int <= 10000:
        print("Tipo impositivo del: 5%")
    elif renta_anual_int > 10000 and renta_anual_int <= 20000:
        print("Tipo impositivo del: 15%")
    elif renta_anual_int > 20000 and renta_anual_int <= 35000:
        print("Tipo impositivo del: 20%")
    elif renta_anual_int > 35000 and renta_anual_int <= 60000:
        print("Tipo impositivo del: 30%")
    else:
        print("Tipo impositivo del: 40%")

def entrada_renta() -> str:
    renta_anual: str = input(">> ¿Cual es tu renta anual?: ")
    return renta_anual

if __name__ == '__main__':
    main()