def ejercicio4():
    def validateInput(msg: str):
        while True:
            try:
                s = int(input(msg).strip())
                return s
            except:
                print("entrada invalida")

    def getPersona():
        while True:
            try:
                nombre = input("nombre: ").lower().strip().capitalize()
                apellido = input("apellido: ").lower().strip().capitalize()
                edad = int(input("edad:").lower().strip())
                email = input("email:").lower().strip()
                return {
                    "nombre": nombre,
                    "apellido": apellido,
                    "edad": edad,
                    "email": email
                }
            except:
                print("datos invalidos, intente denuevo")

    def printPersonas(dic: dict[str, list]):
        keys = list(dic.keys())

        for i in range(len(dic[keys[0]])):
            print(f"persona {i+1}:")
            for key in keys:
                print(f"{key}: {dic[key][i]}")
            print("-------------")

    def addPersona(persona, dic):
        for i in dic.keys():
            dic[i].append(persona[i])

    personas = {
        "nombre": ["Emilia", "Gustavo Andres"],
        "apellido": ['Cabrera', "Peralta"],
        "edad": [23, 26],
        "email": ["ecabrera@curso.com", "gperalta@curso.com"]
    }

    print(
        """
Menu:

1. agregar persona
2. imprimir lista de personas
3. salir
"""
    )

    while True:
        op = validateInput('seleccione su opcion: ')

        match op:
            case 1:
                persona = getPersona()
                addPersona(persona, personas)
            case 2:
                printPersonas(personas)
            case 3:
                break
            case _:
                print("opcion invalida, intente denuevo")


if __name__ == "__main__":
    ejercicio4()
