
def ejercicioStr1():
    s = "Gerundio omar, julian alvaro"
    s = s.split(", ")[::-1]

    ns = ''
    for w in s:
        ns += w + " "

    print(ns)


if __name__ == "__main__":
    ejercicioStr1()
