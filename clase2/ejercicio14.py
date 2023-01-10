def ejercicio14():
    def f(x):
        return x**2 - 6*x + 3

    menorx = 99999999
    menory = 99999999

    for i in range(-9, 9):
        min = f(i)
        if min < menory:
            menory = min
            menorx = i

    print(f"menor x: {menorx}, menor y: {menory}")


if __name__ == "__main__":
    ejercicio14()
