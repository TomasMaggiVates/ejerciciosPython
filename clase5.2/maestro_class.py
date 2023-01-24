class Maestro:
    # nombre
    # apellido
    # legajo
    def __init__(self, nombre, legajo) -> None:
        self.nombre = nombre
        self.legajo = legajo
        self.materias = []

    def __eq__(self, another):
        return hasattr(another, 'nombre') and hasattr(another, 'legajo')\
            and self.nombre == another.nombre and self.legajo == another.legajo

    def __hash__(self):
        return hash(self.legajo)
