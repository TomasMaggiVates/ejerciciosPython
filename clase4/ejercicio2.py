import math


def areaCirculo(r: float) -> float:
    # A = π r²
    return math.pi * r ** 2


def AreaCilindro(b: float, h: float) -> float:
    # V = Π h r²
    return areaCirculo(b) * h


def ejercicio2():
    # base del cilindro
    b = 5

    # altura del cilindro
    h = 10

    print(f"area del cilindro: {AreaCilindro(b,h):.2f} cm3")


if __name__ == "__main__":
    ejercicio2()
