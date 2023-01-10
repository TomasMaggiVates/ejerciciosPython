def ejercicioStr5():
    s = "Órdenador"

    c = len(s)
    v = 0

    for ch in s:
        if ch.lower() in ['a', 'e', 'i', 'o', 'u', 'á', 'é', 'í', 'ó', 'ú']:
            v += 1

    metrica = c * v

    print(metrica)


if __name__ == "__main__":
    ejercicioStr5()
