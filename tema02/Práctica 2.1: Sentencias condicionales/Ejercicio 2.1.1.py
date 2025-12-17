def pedir_edad() -> int | bool:
    edad = input(">> ¿Cuantos años tienes?: ")
    if not edad.isdigit():
        print("La edad debe ser un numero")
        return False
    elif int(edad) < 0 :
        print("No puede ser negativa la edad")
        return False
    elif int(edad) > 110:
        print("No puede ser tan viejo")
        return False
    else:
        return int(edad)

def comprobar_edad(edad: int):
    if edad >= 18:
        print("Eres mayor de edad")
    else:
        print("Eres menor de edad")

def main() ->  None:
    edad = pedir_edad()
    if edad:
        comprobar_edad(edad)

if __name__ == '__main__':
    main()
