def factorial(num: int) -> int:
    factorial = 1
    if num > 0:
        for i in range(num, 1, -1):
            factorial *= i
    elif num < 0:
        raise ValueError("solo numeros mayores o iguales a 0")
    return factorial


def ejercicio1():
    print(f"factorial de -10: {factorial(-1)}")


if __name__ == "__main__":
    ejercicio1()
