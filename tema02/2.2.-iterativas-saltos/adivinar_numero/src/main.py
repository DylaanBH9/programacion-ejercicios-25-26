import random

def main():
    numero_adivinar = random.randint(1, 100)
    print(numero_adivinar)
    encontrado = False
    intentos = 6
    print(f"Tienes {intentos} intentos para adivinar el numero.")
    contador = 0
    while not encontrado and contador < intentos:
        contador += 1
        intento = int(input("Adivina el numero entre 0 y 100: "))
        encontrado = intento == numero_adivinar
        if numero_adivinar > intento and contador != intentos:
            print("El numero es mayor.")
        elif numero_adivinar < intento and contador != intentos:
            print("El numero es menor.")

    if not encontrado:
        print(f"Has fallado! \nEl numero era {numero_adivinar}.")
    else:
        print("Has adivinado el numero.")

if __name__ == "__main__":
    main()