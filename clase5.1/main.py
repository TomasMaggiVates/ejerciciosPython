from alumno_class import Alumno
from maestro_class import Maestro
from grado_class import Grado
from materia_class import Materia
from libreta_class import Libreta

if __name__ == "__main__":
    """
    • Cargar un Alumno
    • Asignar una libreta a cada alumno, ya sea de 1ro, 2do o 3er grado
    • Cargar las notas de cada alumno para cada materia y por cada semestre
    • Consultar la libreta de cada alumno indicando su legajo
    • Consultar el alumno con mejor promedio por grado
    • Consultar qué materias dicta cada maestro
    • Consultar cuántos alumnos tiene cada materia.
    • Consultar cuántos alumnos en total tiene cada maestro
    """

    """
    Nombre       Apellido       Legajo      Grado
    Martín      Dominguez       10              1
    Marcela     Morelo          20              2
    Eduardo     Verti           30              1
    Mirta       Ledezma         40              3
    Jeremías    Navarro         50              1
    Silvina     Saires          60              3
    Miguel      Carrizo         70              2
    Nora        Morales         80              1
    Virginia    López           90              3
    Guillermo   Brito           100             2
    Martina     Torres          110             1
    Bart        Simpson         120             3
    """

    """
    Grado       Materia                 Maestro             Legajo
    1           Artes               Augusto Gutierres       M10
    1           Matemática          Cecilia Peña            M20
    1           Geografía           Sandra Almada           M30
    2           Educación           Física Hugo Carrizo     M40
    2           Ciencias Naturales  Cecilia Peña            M20
    2           Lengua              Sandra Almada           M30
    3           Historia            Augusto Gutierres       M10
    3           Formación Cívica    Sandra Almada           M30
    3           Inglés              Sandra Almada           M30
    """

    datos_alumnos = \
        {
            {
                'legajo': '10',
                'nombre': 'Martin',
                'apellido': 'Dominguez',
                'grado': '1',
                'libreta': Libreta(['Artes', 'Matemática', 'Geografía'])
            },
            {
                'legajo': '20',
                'nombre': 'Marcela',
                'apellido': 'Morelo',
                'grado': '2',
                'libreta': Libreta(['Educación', 'Ciencias Naturales', 'Lengua'])
            },
            {
                'legajo': '30',
                'nombre': 'Eduardo',
                'apellido': 'Verti',
                'grado': '1',
                'libreta': Libreta(['Artes', 'Matemática', 'Geografía'])
            },
            {
                'legajo': '40',
                'nombre': 'Mirta',
                'apellido': 'Ledezma',
                'grado': '3',
                'libreta': Libreta(['Historia', 'Formación Cívica', 'Inglés'])
            }
        }

    datos_grado = \
        {
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
        }
