def sumarUno(i: int) -> int:
    return i + 1


def aumentar(l: list, f: callable) -> list:
    for i in range(len(l)):
        l[i] = f(l[i])

    return l


def ejercicio1():
    l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

    l = aumentar(l, sumarUno)

    print(l)


if __name__ == "__main__":
    ejercicio1()
