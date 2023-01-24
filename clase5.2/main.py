from alumno_class import Alumno
from maestro_class import Maestro
from grado_class import Grado
from materia_class import Materia
from libreta_class import Libreta

"""
institucion
    |->grado[]
        |->maestro[]
        |    |->materia[]
        |->alumnos[]
        |    |->libreta
        |->materia[]
"""


class institucion:
    '''
    manejamos las funciones requeridas por el ejercicio

    • Cargar un Alumno
    • Asignar una libreta a cada alumno, ya sea de 1ro, 2do o 3er grado
    • Cargar las notas de cada alumno para cada materia y por cada semestre
    • Consultar la libreta de cada alumno indicando su legajo
    • Consultar el alumno con mejor promedio por grado
    • Consultar qué materias dicta cada maestro
    • Consultar cuántos alumnos tiene cada materia.
    • Consultar cuántos alumnos en total tiene cada maestro
    '''

    def __init__(self):
        self.grados = {}

    # cargamos la info desde las tablas del pdf
    def cargarDesdeDict(self, d1: dict, d2: dict):
        tmp_grados = \
            {
                1: {
                    'maestros': [],
                    'alumnos': [],
                    'materias': []
                },
                2: {
                    'maestros': [],
                    'alumnos': [],
                    'materias': []
                },
                3: {
                    'maestros': [],
                    'alumnos': [],
                    'materias': []
                }
            }

        tmp_maestros = []

        # cargamos los maestros
        for i in d2:
            tmp = Maestro(i['maestro'], i['legajo'])
            tmp_maestros.append(tmp)
            tmp_grados[int(i['grado'])]['maestros'].append(tmp)

        # cargamos las materias y los referenciamos entre si con los maestros segun su legajo
        for i in d2:
            for j in tmp_maestros:
                if i['legajo'] == j.legajo:
                    tmp = Materia(i['legajo'], j)
                    j.materias.append(tmp)
                    tmp_grados[int(i['grado'])]['materias'].append(tmp)

        tmp_alumnos = []

        # cargamos alumnos
        for i in d1:
            tmp = Alumno(i['nombre'], i['apellido'], i['legajo'])
            tmp_alumnos.append(tmp)
            tmp_grados[int(i['grado'])]['alumnos'].append(tmp)

        def pretty(d, indent=0):
            for key, value in d.items():
                print('\t' * indent + str(key))
                if isinstance(value, dict):
                    pretty(value, indent+1)
                else:
                    print('\t' * (indent+1) + str(value))

        # pretty(tmp_grados)

        for i in tmp_grados.values():
            for j in i['alumnos']:
                j.libreta = Libreta(i['materias'])

        # print(tmp_grados[1]['alumnos'][0].libreta.materias)
        self.grados = tmp_grados.copy()

    # metodos para el ejercicio

    def agregarAlumno(self, grado, a: Alumno):
        self.grados[grado].append(a)
        return

    def asignarLibreta(self, legajo: str, libreta: Libreta):
        a = self.alumnoPorlegajo(legajo)
        a.libreta = libreta
        return

    def cargarNotas(self):

    def getLibretaPorLegajo(self, legajo):
        pass

    def getmejorPromedioPorGrado(self):
        pass

    def materiasPorMaestro(self):
        pass

    def alumnosPorMateria(self):
        pass

    def alumnosPorMateria(self):
        pass

    # metodos de ayuda

    def alumnoPorlegajo(self, legajo) -> Alumno:
        for k in self.grados.keys():
            for alumno in self.grados[k]['alumnos']:
                if int(alumno.legajo) == legajo:
                    return alumno


if __name__ == "__main__":
    datos_alumnos = \
        [
            {
                'legajo': '10',
                'nombre': 'Martin',
                'apellido': 'Dominguez',
                'grado': '1'
            },
            {
                'legajo': '20',
                'nombre': 'Marcela',
                'apellido': 'Morelo',
                'grado': '2'
            },
            {
                'legajo': '30',
                'nombre': 'Eduardo',
                'apellido': 'Verti',
                'grado': '1'
            },
            {
                'legajo': '40',
                'nombre': 'Mirta',
                'apellido': 'Ledezma',
                'grado': '3'
            }
        ]
    datos_grado = \
        [
            {
                'grado': '1',
                'legajo': 'M10',
                'materia': 'Artes',
                'maestro': 'Augusto Guitierres'
            },
            {
                'grado': '1',
                'legajo': 'M20',
                'materia': 'Matemática',
                'maestro': 'Cecilia Peña'

            },
            {
                'grado': '1',
                'legajo': 'M30',
                'materia': 'Geografía',
                'maestro': 'Sandra Almada'

            },
            {
                'grado': '2',
                'legajo': 'M40',
                'materia': 'Educación Física',
                'maestro': 'Hugo Carrizo'
            }
        ]

    i = institucion()
    i.cargarDesdeDict(datos_alumnos, datos_grado)
    print(i.alumnoPorlegajo(10).legajo)
