def ejercicio2():
    año = 2008

    if (año % 4 == 0 and año % 10 != 0) or (año % 40 == 0):
        print("Bisiesto")
    else:
        print("año no Bisiesto")


if __name__ == "__main__":
    ejercicio2()
