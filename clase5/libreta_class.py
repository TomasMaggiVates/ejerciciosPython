class Libreta:
    # grado
    # lista de materias
    # nota de semestre 1
    # nota de semestre 2
    # promedio por materia
    # promedio general
    def __init__(self, grado, lista_materias) -> None:
        self.grado = grado
        self.materias = {}

        for materia in lista_materias:
            self.materias[materia] = {'1': None, '2': None}

    def agregarNotasMateria(self, materia, semestre, nota) -> None:
        self.materias[materia][semestre] = nota

    def promedioMateria(self, materia) -> float:
        return (self.materias[materia]['1'] + self.materias[materia]['2']) / 2

    def promedioGeneral(self) -> float:
        s = 0
        l = len(list(self.materias.keys()))
        for key in self.materias.keys():
            s += self.promedioMateria(key)

        return s / l

    def __eq__(self, another):
        return hasattr(another, 'grado') and hasattr(another, 'materia') \
            and self.grado == another.grado and self.materia == another.materia

    def __hash__(self):
        return hash(self.grado)
