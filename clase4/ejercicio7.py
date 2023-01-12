import datetime
import copy


def getPropiedades(inm: list, lim: float) -> list:
    r = []

    for i in inm:
        precio = calcPrecio(i)
        if precio <= lim:
            i['precio'] = formatPrecio(precio)
            r.append(i)
    return r


def calcPrecio(d: dict) -> float:
    precio = 0
    if d['zona'] == 'A':
        #  precio = (metros * 1000 + habitaciones * 5000 + garaje * 15000) * (1-antiguedad/100)
        precio = \
            (d['metros'] * 1000 + d['habitaciones'] * 5000 + d['garaje'] * 15000)\
            * \
            (1 - (datetime.date.today().year - d['año']) / 100)
    else:
        #  precio = (metros * 1000 + habitaciones * 5000 + garaje * 15000) * (1-antiguedad/100) * 1.5
        precio = \
            (d['metros'] * 1000 + d['habitaciones'] * 5000 + d['garaje'] * 15000)\
            * \
            (1 - (datetime.date.today().year - d['año']) / 100)

    return precio


def formatPrecio(s: float) -> str:
    return f"{s:.2f} $"


def ejercicio7():
    def printInmuebles(l: list[dict]) -> None:
        for i in l:
            for k, v in i.items():
                print(f"{k}: {v}")
            print('--------------------')

    INMUEBLES = [
        {'año': 2000, 'metros': 100, 'habitaciones': 3, 'garaje': True, 'zona': 'A'},
        {'año': 2012, 'metros': 60, 'habitaciones': 2, 'garaje': True, 'zona': 'B'},
        {'año': 1980, 'metros': 120, 'habitaciones': 4, 'garaje': False, 'zona': 'A'},
        {'año': 2005, 'metros': 75, 'habitaciones': 3, 'garaje': True, 'zona': 'B'},
        {'año': 2015, 'metros': 90, 'habitaciones': 2, 'garaje': False, 'zona': 'A'}
    ]

    limite = 100000

    l = getPropiedades(copy.deepcopy(INMUEBLES), limite)

    printInmuebles(l)


if __name__ == "__main__":
    ejercicio7()
