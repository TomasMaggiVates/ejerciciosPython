def getPares(l: list[int]) -> list[int]:
    return [x for x in l if x % 2 == 0]


def ejercicio4():
    l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

    l = getPares(l)

    print(l)


if __name__ == "__main__":
    ejercicio4()
