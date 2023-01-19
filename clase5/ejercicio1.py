from alumno_class import Alumno
from maestro_class import Maestro
from grado_class import Grado
from materia_class import Materia
from libreta_class import Libreta


class Institucion:
    # cargar Alumnos
    # asignar libreta a alumno
    # cargar notas a cada alumno por materia por semestre
    # conseguir libreta de alumno por legajo
    # mejor promedio por grado
    # materias de cada maestro
    # alumnos de cada materia
    # alumnos de cada maestro

    pass


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
