class Grado:
    # maestro
    # lista de alumnos
    # lista de materias
    def __init__(self, maestro, alumnos, materias) -> None:
        self.maestro = maestro
        self.lista_alumnos = alumnos
        self.lista_materias = materias

    def __eq__(self, another):
        return hasattr(another, 'maestro') and hasattr(another, 'lista_alumnos') and hasattr(another, 'lista_materias')\
            and self.nombre == another.nombre and self.lista_alumnos == another.lista_alumnos and self.lista_materias == another.lista_materias

    def __hash__(self):
        return hash(self.maestro)
