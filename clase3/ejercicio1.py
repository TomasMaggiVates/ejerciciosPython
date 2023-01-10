def ejercicio1():
    s = "lumberjacks"
    esIsograma = True
    h = {}

    for i in s:
        if i in h.keys():
            esIsograma = False
        h[i] = None

    print(f"{s} es isograma? {'si' if esIsograma else 'no'}")


if __name__ == "__main__":
    ejercicio1()
