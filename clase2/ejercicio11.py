def ejercicio11():
    x_actual = 0
    y_actual = 0

    x_objetivo = 8
    y_objetivo = 7

    flag = False

    while True:
        if x_actual == x_objetivo and y_actual == y_objetivo:
            break

        if flag:
            x_actual += 1
            y_actual += 2
        else:
            x_actual += 2
            y_actual += 1

        flag = not flag

        print(f"({x_actual},{y_actual})")


if __name__ == "__main__":
    ejercicio11()
