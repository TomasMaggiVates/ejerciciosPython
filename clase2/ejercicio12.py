def ejercicio12():
    s1 = "0001010011101"
    s2 = "0000110010001"

    distancia = 0

    for i in range(len(s1)):
        if s1[i] != s2[i]:
            distancia += 1

    print(distancia)


if __name__ == "__main__":
    ejercicio12()
