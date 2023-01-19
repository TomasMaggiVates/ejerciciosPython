class Alumno:
    # legajo
    # nombre
    # apellido
    def __init__(self, nombre, apellido, legajo) -> None:
        self.nombre = nombre
        self.apellido = apellido
        self.legajo = legajo
        self.libreta = None

    def __eq__(self, another):
        return hasattr(another, 'nombre') and hasattr(another, 'apellido') and hasattr(another, 'legajo') and hasattr(another, 'libreta')\
            and self.nombre == another.nombre and self.apellido == another.apellido and self.legajo == another.legajo and self.libreta == another.libreta

    def __hash__(self):
        return hash(self.legajo)


a = Alumno('ahfe', 'fhraeofasw', 20)

print(a)
