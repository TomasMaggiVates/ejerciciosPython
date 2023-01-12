import math


def calVar(l: list[float], avg: float) -> float:
    # Var (X) = (x1 – x’)2 + (x2 – x’)2 + … + (xn – x’) / N
    sum = 0
    for i in l:
        sum += (i - avg) * 2
    return sum / len(l)


def calDes(l: list[float], avg: float) -> float:
    # Des(x) = sqrt(sum(|x - avg|^2)) / N
    sum = 0
    for i in l:
        sum += abs(i - avg) ** 2

    des = math.sqrt(sum) / len(l)
    return des


def calc(l: list[float]) -> dict:
    avg = max(l) / len(l)
    var = calVar(l, avg)
    des = calDes(l, avg)

    return {
        'avg': avg,
        'var': var,
        'des': des
    }


def ejercicio3():
    l = [1, 2, 3, 4, 5, 6]

    r = calc(l)

    print(f'promedio: {r["avg"]}, variacion: {r["var"]},  desviacion: {r["des"]:.2f}')


if __name__ == "__main__":
    ejercicio3()
