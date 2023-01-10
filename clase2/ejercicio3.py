def ejercicio3():
    def validate_input(msg):
        s = ""
        while s not in opciones:
            s = input(msg)
        return s

    opciones = ["piedra", "papel", "tijera"]
    frases = ["papel envuelve piedra",
              "tijera corta papel", "piedra rompe tijeras"]

    p1 = validate_input("jugador 1: ")
    p2 = validate_input("jugador 2: ")

    if p1 == p2:
        print("empate")

    if (opciones.index(p1) > opciones.index(p2)) or (opciones.index(p1) == 1 and opciones.index(p2) == 3):
        print(f"p1 gana {frases[opciones.index(p2)]}")
    else:
        print(f"p2 gana {frases[opciones.index(p1)]}")


if __name__ == "__main__":
    ejercicio3()
