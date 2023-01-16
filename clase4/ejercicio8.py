def add(DB: dict, id=None):
    def addTel() -> dict:
        d = {}

        while True:
            i = input("tel indetificador: ")
            if not i or i == 'quit':
                break

            d[i] = input("num de tel: ")

        return d

    if not id:
        id = input("identificador: ")
    nombre = input("nombre: ")
    apellido = input("apellido: ")
    tel = addTel()
    email = input("email: ")

    n_contacto = {
        "id": id,
        "nombre": nombre,
        "apellido": apellido,
        "telefonos": tel,
        "email": email
    }

    if not id:
        DB.append(n_contacto)

    return n_contacto


def printContactos(l: dict | list[dict]) -> None:
    print('--------------------')
    if isinstance(l, dict):
        for k, v in l.items():
            print(f"{k}: {v}")
        print('--------------------')
    else:
        for i in l:
            for k, v in i.items():
                print(f"{k}: {v}")
            print('--------------------')


def buscar(DB: list[dict], s: str):
    mach = []
    for i in DB:
        if s in [i['nombre'], i["apellido"], i['id']]:
            mach.append(i)

    if len(mach) == 1:
        mach = mach[0]

    return mach


def modificar(DB: list[dict], s: str):
    l = buscar(DB, s)

    printContactos(l)
    p_id = input("seleccione el id del contato a modificar: ")
    DB[DB.index(buscar(DB, p_id))] = add(DB, id=p_id)


def eliminar(DB: list[dict], s: str):
    l = buscar(DB, s)

    printContactos(l)
    p_id = input("seleccione el id del contato a elimiar: ")
    res = input("seguro que desea eliminar el contaco?[s][n]")
    if res == 's':
        DB.remove(buscar(DB, p_id))
    else:
        print('operacion cancelada')


def ejercicio8():
    DB = \
        [
            {
                "id": '1',
                "nombre": 'Tomas',
                "apellido": 'Maggi',
                "telefonos": {'trabajo': "3564656314"},
                "email": 'tm82945g@gmail.com'
            },
            {
                "id": '2',
                "nombre": 'Jose',
                "apellido": 'juan',
                "telefonos": {'trabajo': "1231242351"},
                "email": 'gg@sgmail.com'
            }
        ]

    while True:
        print("Agenda: ", end="\n\n")
        print("opciones:")
        print("1. agregar contacto")
        print("2. modificar contacto")
        print("3. buscar contacto")
        print("4. elminar contacto")
        print("5. listar contactos")
        print("6. salir")

        op = int(input("seleccione su opcion:  "))
        match(op):
            case 1:
                printContactos(add(DB))
            case 2:
                s = input(
                    "escriba el nombre, apellido o identificador a modificar")
                modificar(DB, s)
            case 3:
                s = input("escriba el nombre, apellido o identificador a buscar")
                printContactos(buscar(DB, s))
            case 4:
                s = input(
                    "escriba el nombre, apellido o identificador a eliminar")
                eliminar(DB, s)
            case 5:
                printContactos(DB)
            case 6:
                break
            case _:
                continue


if __name__ == "__main__":
    ejercicio8()
