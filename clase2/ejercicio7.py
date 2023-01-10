def ejercicio7():
    n = 11
    esPrimo = True

    for i in range(2, n):
        if n % i == 0:
            esPrimo = False

    if esPrimo:
        print("Primo")
    else:
        print("No es primo")


if __name__ == "__main__":
    ejercicio7()
