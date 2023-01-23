from alumno_class import Alumno
from maestro_class import Maestro
from grado_class import Grado
from materia_class import Materia
from libreta_class import Libreta


class Institucion:

    def __init__(self) -> None:
        self.alumnos = []
        self.maestros = []
        self.materias = []
        self.grados = []

    def agregarAlumno(self, nombre: str, apellido: str, legajo: str) -> Alumno:
        # cargar Alumnos
        a = Alumno(nombre, apellido, legajo)
        self.alumnos.append(a)
        return a

    def agregaMaestro(self, nombre: str, apellido: str, legajo: str) -> Maestro:
        m = Maestro(nombre, apellido, legajo)
        self.maestros.append(m)
        return m

    def agregarMateria(self, nombre: str, maestro: Maestro) -> None:
        self.materias.append(Materia(nombre, maestro))

    def agregarGrado(self, maestro: Maestro, alumnos: list[Alumno], materias: list[Materia]) -> None:
        self.alumnos.append(Grado(maestro, alumnos, materias))

    def agregarLibreta(self, grado: Grado, materias: list[Materia], alumno: Alumno) -> None:
        # asignar libreta a alumno
        alumno.libreta = Libreta(grado, materias)

    def getLibretaPorLegajo(self, legajo) -> Alumno:
        # conseguir alumno por legajo
        for alumno in self.alumnos:
            if alumno.legajo == legajo:
                return alumno

    def mejorPromedioPorGrado(self) -> dict:
        # conseguir mejor promedio por grado
        d = {}
        for grado in self.grados:
            d[grado]
            for alumno in self.alumnos:
                if alumno.libreta.promedioGeneral() > d[grado].alumno.libreta.promedioGeneral() or not d[grado]:
                    d[grado] = alumno
        return d

    def materiasPorMaestro(self) -> dict:
        # materias de cada maestro
        d = {}
        for maestro in self.maestros:
            d[maestro] = []
            for materia in self.materias:
                if materia.maestro == maestro:
                    d[maestro].append(materia)
        return d

    def alumnosPorMateria(self) -> dict:
        # alumnos de cada materia
        d = {}
        for materia in self.materias:
            d[materia] = []
            for alumno in self.alumnos:
                if alumno.libreta.materias[materia]:
                    d[materia].append(alumno)
        return d

    def alumnosPorMaestro(self) -> dict:
        # alumnos de cada maestro
        d = {}
        for maestro, alumnos, materias in zip(self.grados):
            d[maestro] = alumnos
        return d


def main():
    NOMBRE = "nombre"
    APELLIDO = "apellido"
    GRADO = "grado"
    NOMBRE_MATERIA = "nombre materia"
    LEGAJO = "legajo"

    datos_alumno = \
        {
            "10": {NOMBRE: "Martin", APELLIDO: "Domingez", GRADO: 1},
            "20": {NOMBRE: "Marcela", APELLIDO: "Morelo", GRADO: 2},
            "30": {NOMBRE: "Eduardo", APELLIDO: "Verti", GRADO: 1},
            "40": {NOMBRE: "Mirta", APELLIDO: "Ledesma", GRADO: 3},
            "50": {NOMBRE: "Jeremias", APELLIDO: "Navarro", GRADO: 1},
            "60": {NOMBRE: "Silvina", APELLIDO: "Saires", GRADO: 3},
            "70": {NOMBRE: "Martin", APELLIDO: "Domingez", GRADO: 1},
            "80": {NOMBRE: "Martin", APELLIDO: "Domingez", GRADO: 1},
            "90": {NOMBRE: "Martin", APELLIDO: "Domingez", GRADO: 1},
            "100": {NOMBRE: "Martin", APELLIDO: "Domingez", GRADO: 1},
            "110": {NOMBRE: "Martin", APELLIDO: "Domingez", GRADO: 1},
            "120": {NOMBRE: "Martin", APELLIDO: "Domingez", GRADO: 1}
        }

    datos_profesores = \
        {
            1: {NOMBRE_MATERIA: "Artes", NOMBRE: "Augusto", APELLIDO: "Gutierres", LEGAJO: "M10"},
            1: {NOMBRE_MATERIA: "Matemática", NOMBRE: "Cecilia", APELLIDO: "Peña", LEGAJO: "M20"},
            1: {NOMBRE_MATERIA: "Geografía", NOMBRE: "Sandra", APELLIDO: "Almada", LEGAJO: "M30"},
            2: {NOMBRE_MATERIA: "Educación Física", NOMBRE: "Hugo", APELLIDO: "Carrizo", LEGAJO: "M40"},
            2: {NOMBRE_MATERIA: "Ciencias Naturales", NOMBRE: "Cecilia", APELLIDO: "Peña", LEGAJO: "M20"},
            2: {NOMBRE_MATERIA: "Lengua", NOMBRE: "Sandra", APELLIDO: "Almada", LEGAJO: "M30"},
            3: {NOMBRE_MATERIA: "Historia", NOMBRE: "Augusto", APELLIDO: "Gutierres", LEGAJO: "M10"},
            3: {NOMBRE_MATERIA: "Formación Cívica", NOMBRE: "Sandra", APELLIDO: "Almada", LEGAJO: "M30"},
            3: {NOMBRE_MATERIA: "Inglés", NOMBRE: "Sandra", APELLIDO:  "Almada", LEGAJO: "M30"}
        }
