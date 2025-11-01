def agregarAlumno():
    alumno = {
             "nombre": input("Introduce su nombre"),
             "edad": input("Introduce su edad"),
             "semestre": input("Introduce a que semestre asiste"),
             "carrera": input("Introduce la carrera del alumno")
            }
    return alumno

def dardebajaAlumno(curso):
    IdAlumno = int(input("Dame el Id del Alumno al que quieras dar de baja"))
    if 0 <= IdAlumno < len(curso):
        AlumnoEliminado = curso.pop(IdAlumno)
        print(f"El Alumno {AlumnoEliminado["nombre"]} fue dado de baja con exito")
    else:
        print("ID no valido o no identificado")
    return curso

def mostrarlistadeAlumnos(curso):
    if len(curso) == 0:
        print("====== NO HAY ALUMNOS REGISTRADOS ======")
    else:
        print("=========LISTA DE ALUMNADO=========")
        for i, alumno in enumerate(curso):
            print(f"ID: {i}")
            print(f"Nombre: {alumno['nombre']}")
            print(f"Edad: {alumno['edad']}")
            print(f"Semestre: {alumno['semestre']}")
            print(f"Carrera: {alumno['carrera']}\n")
