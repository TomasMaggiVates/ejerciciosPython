def ejercicioStr2():
    ruta = "//1.1.1.1/eoi/python"
    ruta = ruta.replace("//", "")

    host = ruta.split("/", 1)[0]
    path = ruta.split("/", 1)[1]

    print(f"host={host}  path={path}")


if __name__ == "__main__":
    ejercicioStr2()
