def ejercicio3():
    frutas = {
        "banana": 1.35,
        "manzana": 0.80,
        "pera": 0.85,
        "naranja": 0.70
    }

    print("seleccione una fruta para consultar su precio:\n")
    for i in frutas.keys():
        print(f"* {i}")

    print("")

    try:
        op = input("opcion: ").lower().strip()
        print(f"{op}: ${frutas[op]}")
    except:
        print("opcion no valida")


if __name__ == "__main__":
    ejercicio3()
