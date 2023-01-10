def ejercicio1():
    def str_ingredientes(l):
        s = ''
        for i in l:
            s += f"{l.index(i)}. {i}\n"
        return s

    def str_pizza(l):
        s = ''
        for i in l:
            if i == l[-1]:
                s = s[:-2]
                s += f' y {i}'
            else:
                s += f'{i}, '
        return s

    ingredientes_veg = ["pimiento", "tofu"]
    ingredientes_nov = ["peperoni", "salmon", "jamon"]
    ingredientes_default = ["mozzarella", "tomate"]

    menu = """
Bienvenido a la pizzeria Bella Napoli.
Tipos de pizza
1- Vegetariana
2- No vegetariana
"""

    print(menu)

    op = ""
    while not op in ["1", "2"]:
        op = input("seleccione una opcion: ")

    # vegano
    if op == "1":
        print("Ingredientes de pizzas vegetarianas")
        print(str_ingredientes(ingredientes_veg))
        ing = int(input("seleccione ingrediente: "))
        print("Pizza vegetarina con ", end="")

        ingredientes_default.append(ingredientes_veg[ing])
        print(str_pizza(ingredientes_default))

    # no vegano
    else:
        print("Ingredientes de pizzas no vegetarianas")
        print(str_ingredientes(ingredientes_nov))
        ing = int(input("seleccione ingrediente: "))
        print("Pizza no vegetarina con ", end="")

        ingredientes_default.append(ingredientes_nov[ing])
        print(str_pizza(ingredientes_default))


if __name__ == "__main__":
    ejercicio1()
