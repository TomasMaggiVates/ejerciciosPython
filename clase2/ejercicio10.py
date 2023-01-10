def ejercicio10():
    str1 = ["a", "b", "c"]
    str2 = ["1", "2"]
    str3 = []

    for i in str1:
        for j in str2:
            str3.append([i, j])

    print(str3)


if __name__ == "__main__":
    ejercicio10()
