class Alumno:
    # legajo
    # nombre
    # apellido
    # libreta
    pass


class Maestro:
    # nombre
    # apellido
    # legajo
    pass


class Materia:
    # nombre
    # maestro
    pass


class Libreta:
    # grado
    # lista de materias
    # nota de semestre 1
    # nota de semestre 2
    # promedio por materia
    # promedio general
    pass


class Grado:
    # maestro
    # lista de alumnos
    # lista de materias
    pass


class Institucion:
    # lista de profesores
    # lista de alumnos
    pass


def main():
    NOMBRE = "nombre"
    APELLIDO = "apellido"
    GRADO = "grado"

    datos = {
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
