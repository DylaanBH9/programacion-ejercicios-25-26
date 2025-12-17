def pedir_contrasena() -> str:
    contrasena = input(">> ¿Cual es la contraseña?: ")
    return contrasena

def comprobar_contrasena(contrasena, contrasena_usuario) -> None:
    if contrasena.lower() == contrasena_usuario.lower():
        print("La contraseña es correcta")
    else:
        print("La contraseña no es correcta")

def main() -> None:
    contrasena: str = "contraseña"
    contrasena_usuario = pedir_contrasena()
    comprobar_contrasena(contrasena, contrasena_usuario)

if __name__ == '__main__':
    main()