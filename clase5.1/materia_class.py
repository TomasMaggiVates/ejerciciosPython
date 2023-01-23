class Materia:
    # nombre
    # maestro
    def __init__(self, nombre, maestro) -> None:
        self.nombre = nombre
        self.maestro = maestro

    def __eq__(self, another):
        return hasattr(another, 'nombre') and hasattr(another, 'maestro') \
            and self.nombre == another.nombre and self.maestro == another.maestro

    def __hash__(self):
        return hash(self.nombre)
