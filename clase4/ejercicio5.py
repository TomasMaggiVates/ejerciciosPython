def quitarAcentos(s: str) -> str:
    d = {
        'á': 'a',
        'é': 'e',
        'í': 'i',
        'ó': 'o',
        'ú': 'u'
    }
    return d[s] if s in d.keys() else s


def getFrecuencia(s: str) -> dict[str, int]:
    info = {}
    # limpiamos el str de caracteres que no sean letras o numeros
    s = list(s.replace(',', '').replace('.', '').replace('\n', '').split(' '))

    for i in s:

        # normalizamos y quitamos los caracteres de cada letra de la palabra
        r = ''.join([quitarAcentos(j.lower()) for j in i])

        # evitamos contar espacios vacios
        if r in [' ', '']:
            continue
        elif r in list(info.keys()):
            info[r] += 1
        else:
            info[r] = 1
    return info


def mayorFrecuencia(d: dict[str, int]) -> tuple:
    mayor = 0
    keys = []

    for k, v in d.items():
        if v == mayor:
            mayor = v
            keys.append(k)

        if v > mayor:
            mayor = v
            keys = [k]

    return (keys, mayor)


def ejercicio5():
    s = "Éscribir un programa que  reciba una cadena de caracteres y devuelva un diccionario con\
cada palabra que contiene y su frecuencia"

    d = getFrecuencia(s)
    t = mayorFrecuencia(d)

    l = len(t[0])
    print(f"Palabra{'s' if l > 2 else ''} mas usada{'s' if l > 2 else ''}: ")
    for i in t[0]:
        print(f"* {i}")

    print(f"que se repite{'n' if l > 2 else ''} un total de: {t[1]} veces")


if __name__ == "__main__":
    ejercicio5()
