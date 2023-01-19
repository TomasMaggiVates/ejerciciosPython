class Maestro:
    # nombre
    # apellido
    # legajo
    def __init__(self, nombre, apellido, legajo) -> None:
        self.nombre = nombre
        self.apellido = apellido
        self.legajo = legajo

    def __eq__(self, another):
        return hasattr(another, 'nombre') and hasattr(another, 'apellido') and hasattr(another, 'legajo')\
            and self.nombre == another.nombre and self.apellido == another.apellido and self.legajo == another.legajo

    def __hash__(self):
        return hash(self.legajo)
