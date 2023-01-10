def ejercicio5():
    def getKeysIterable(dic: dict):
        for key in dic.keys():
            yield (key)

    uglstr =\
        "dni;nombre;email;teléfono;descuento\n\
    01234567L;LuisGonzález;luisgonzalez@mail.com;656343576;12.5\n\
    71476342J;Macarena Ramírez;macarena@mail.com;692839321;8\n\
    63823376M;Juan JoséMartínez;juanjo@mail.com;664888233;5.2\n\
    98376547F;Carmen Sánchez;carmen@mail.com;667677855;15.7"

    l = uglstr.split("\n")
    l = [i.split(";") for i in l]

    info = {}

    for i in l[0]:
        info[i] = []

    l.remove(l[0])

    for i in l:
        for key, j in info.keys(), i:
            print(key, j)

    print(getKeysIterable(info))


if __name__ == "__main__":
    ejercicio5()
