def eje_16():
    def validate():
        while True:
            try:
                i = int(input("Introduzca un numero: "))
                return i
            except:
                print("entrada invalida")

    num = 87
    intentos = 1

    while True:
        entrada = validate()

        if entrada == num:
            break

        intentos += 1

        if entrada < num:
            print("mayor")
        else:
            print("menor")

    print(f"numero {num} encontrado en {intentos} intentos")


if __name__ == "__main__":
    eje_16()
