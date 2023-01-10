def ejercicio2():
    date = '3/30/20'

    r = date.split('/')
    mes = r[0]
    dia = r[1]
    año = '20' + r[2]

    new_date = f'{dia}-{mes}-{año}'

    print(new_date)


if __name__ == "__main__":
    ejercicio2()
