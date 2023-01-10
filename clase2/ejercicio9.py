def ejercicio9():
    s = '1'

    for i in range(9):
        print(f"{s} * {s} = {int(s) * int(s)}")
        s += '1'


if __name__ == "__main__":
    ejercicio9()
