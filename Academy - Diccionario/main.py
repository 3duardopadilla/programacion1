import modelos.curso
from modelos.curso import agregarCurso
from modelos.alumno import agregarAlumno
from modelos.curso import mostrarCurso
from modelos.alumno import dardebajaAlumno
from modelos.alumno import mostrarlistadeAlumnos


cursos = {}

while True:
    nombredelusuario = input("¿Cual es tu nombre?")
    print("Muy bien", nombredelusuario, "Dime que quieres hacer con los cursos.")
    print("*****  AGREGAR CURSO *****")
    print("****  DAR DE BAJA A UN ALUMNO ****")
    print("****  AGREGAR A UN ALUMNO ****")
    print("***** MOSTRAR LISTA DE ALUMNADO *****")
    print("*****    SALIR   *****")
    break
while True:
    Op2 = int(input("""
    1. Agregar Curso.
    2. Agregar un Alumno.
    3. Dar de baja un Alumno.
    4. Mostrar lista
    5. Salir
    """))
    match Op2:
        case 1:
            nombre = input("Nombre de tu curso nuevo")
            cursonuevo = agregarCurso()
            cursos[nombre] = cursonuevo
        case 2:
            nombre = input("Dame el nombre del curso que deseas modificar")
            IdAlumno = input("Dame el Id del Alumno")
            nuevoAlumno = agregarAlumno()
            cursos[nombre]["Alumnos"]
        case 3:
            nombre = input("Dame el nombre del curso que deseas modificar")
            Alumnoexpulsado = dardebajaAlumno(cursos)
            cursos[nombre]["Alumnos"] = Alumnoexpulsado
        case 4:
            mostrarCurso()
        case _:
            break