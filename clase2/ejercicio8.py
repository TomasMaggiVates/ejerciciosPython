def ejercicio8():
    n = 45
    r = []
    sum = 0
    for i in range(0, n, 3):
        if sum + i <= n:
            sum += i
            r.append(i)

    print(r)


if __name__ == "__main__":
    ejercicio8()
