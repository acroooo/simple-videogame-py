import random


def main():
    num_aleatorio = random.randint(1, 101)
    num_usuario = int(input("Adivina el número (entre 1 y 100): "))
    while num_usuario != num_aleatorio:
        if num_usuario < num_aleatorio:
            print("El número es mayor")
        else:
            print("El número es menor")
        num_usuario = int(input("Adivina el número (entre 1 y 100): "))
    print("¡Has acertado!")


if __name__ == "__main__":
    main()
