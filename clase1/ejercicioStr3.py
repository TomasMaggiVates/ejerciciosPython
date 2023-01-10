def ejercicioStr3():
    dni = '12345678'
    r = int(dni) % 23
    l = ''

    match r:
        case 0:
            l = 'T'
        case 1:
            l = 'R'
        case 2:
            l = 'W'
        case 3:
            l = 'A'
        case 4:
            l = 'G'
        case 5:
            l = 'M'
        case 6:
            l = 'Y'
        case 7:
            l = 'F'
        case 8:
            l = 'P'
        case 9:
            l = 'D'
        case 10:
            l = 'X'
        case 11:
            l = 'B'
        case 12:
            l = 'N'
        case 13:
            l = 'J'
        case 14:
            l = 'Z'
        case 15:
            l = 'S'
        case 16:
            l = 'Q'
        case 17:
            l = 'V'
        case 18:
            l = 'H'
        case 19:
            l = 'L'
        case 20:
            l = 'C'
        case 21:
            l = 'K'
        case 22:
            l = 'E'

    print(dni + l)


if __name__ == "__main__":
    ejercicioStr3()
