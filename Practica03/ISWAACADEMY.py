def AgregarAlumno():
    alumno = input("Dime el nombre del alumno que introduciras")
    return alumno
def EliminarAlumno(curso, IdAlumno):
    curso.pop(IdAlumno)
    return curso

def MostrarAlumnos (curso):
    alumnos = curso[-1]
    print(f"======[{curso[0]}]======")
    for i in enumerate(len(alumnos)):
        print(f"ID:{i}-¨{alumnos[i]}")      
cursos =[] 
while True:
     Op1 = input("Deseas agregar un curso?, se te mostrara un menu acontinuacion (si/no)").lower()
     if(Op1 == "no"):
         break
     Curso = ["Programacion I", "Jorge Norzagaray",423,[]]
     cursos.append(Curso)
     alumnos = []
     while True:
        nombredelusuario = input("¿Cual es tu nombre?")
        print("Muy bien", nombredelusuario, "Dime que quieres hacer con los cursos.")
        print("*****  AGREGAR ALUMNO *****")
        print("****  DAR DE BAJA A UN ALUMNO ****")
        print("***** MOSTRAR LISTA DE ALUMNADO *****")
        print("*****    SALIR   *****")
        Op2 = int(input("""
        1. Agregar.
        2. Dar_de_baja.
        3. Ver_lista.
        4. Salir. 
        """))
        match Op2:
            case 1:
                alumno = AgregarAlumno()    
                cursos[0].append(alumno)
                print("Tu alumno fue agregado exitosamente")
            case 2:
                MostrarAlumnos(cursos[0])
                IdAlumno = int(input("digite el ID del alumno al cual se le dara de baja"))
                cursoEditado = EliminarAlumno(cursos[0], IdAlumno)
                cursos[0] = cursoEditado
                print("Se ha dado de baja al alumno satisfactoriamente")
            case 3:
                mostrarCursos = (cursos)
                IdCurso = int(input("digite el ID del curso a mostrar"))
                MostrarAlumnos(cursos[IdCurso])
            case _:
                break