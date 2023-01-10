def ejercicio2_3():

    a = 2
    b = -3
    c = 4

    delta = b**2 - (4 * a * c)

    x1 = (-1*b + (delta)**(1/2))/(2*a)
    x2 = (-1*b - (delta)**(1/2))/(2*a)

    # 3
    print(2*x1**2 - 3*x1 + 4 == 0)
    print(2*x2**2 - 3*x2 + 4 == 0)


if __name__ == "__main__":
    ejercicio2_3()
