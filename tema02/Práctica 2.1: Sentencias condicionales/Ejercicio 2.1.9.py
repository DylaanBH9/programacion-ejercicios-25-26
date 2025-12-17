def main():
    edad_cliente: str = input(">> ¿Cuantos años tienes?: ")
    edad_cliente_int: int = int(edad_cliente)
    if not edad_cliente.isdigit():
        print("La edad del cliente debe ser un numero")
    elif edad_cliente_int < 4:
        ...

if __name__ == '__main__':
    main()