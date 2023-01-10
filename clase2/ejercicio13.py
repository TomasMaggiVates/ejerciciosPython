def ejercico13():
    a = 12
    b = 44

    n = min([a, b])
    max = 0

    for i in range(1, n):
        if a % i == 0 and b % i == 0:
            max = i

    print(f"el maximo comun denominador de {a} y {b} es: {max}")


if __name__ == "__main__":
    ejercico13()
