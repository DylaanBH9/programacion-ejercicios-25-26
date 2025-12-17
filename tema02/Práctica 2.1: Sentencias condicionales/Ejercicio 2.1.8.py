def main():
    puntuacion: str = input("¿Cual es tu puntuación?: ")
    puntuacion_float: float = float(puntuacion)
    niveles_sueldos(puntuacion_float)


def niveles_sueldos(puntuacion_float: float):
    if puntuacion_float < 0:
        print("La puntuación no puede ser negativa")
    elif puntuacion_float == 0.0:
        print("Nivel: Inaceptable")
        print("Sueldo: 2400€")
    elif puntuacion_float < 0.4:
        print("Nivel: Inaceptable")
        print(f"Sueldo: 2400€ {2400 * (1 + puntuacion_float)}€")
    elif 0.4 <= puntuacion_float < 0.6:
        print("Nivel: Aceptable")
        print(f"Sueldo: {2400 * (1 + puntuacion_float)}€")
    else:
        print("Nivel: Meritorio")
        print(f"Sueldo: {2400 * (1 + puntuacion_float)}€")


if __name__ == '__main__':
    main()