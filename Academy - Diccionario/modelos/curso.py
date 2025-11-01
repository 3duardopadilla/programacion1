def agregarCurso():
    curso = {   
        "Instructor": {
            "nombre": input("Introduce el nombre del instructor"),
            "titulo": input("Introduce cual es su titulo"),
            "edad": input("Introduce la edad")
        },
        "aula": input("Introduce el aula"),
        "Alumnos": {}
        }
    return curso

def mostrarCurso(cursos):
    print("===MOSTRANDO CURSO===")
    print(f"Instructor: {cursos['Instructor']['nombre']}")
    print(f"Titulo: {cursos['Instructor']['titulo']}")
    print(f"Edad: {cursos['Instructor']['edad']}")
    print(f"Aula: {cursos['aula']}")
    print("==LISTA DE ALUMNADO==")
    if len(cursos["Alumnos"]) == 0:
        print("====== NO HAY ALUMNOS REGISTRADOS ======")
    else:
        print("=========LISTA DE ALUMNADO=========")
        for i, alumno in enumerate(cursos["Alumnos"]):
            print(f"ID: {i}")
            print(f"Nombre: {alumno['nombre']}")
            print(f"Edad: {alumno['edad']}")
            print(f"Semestre: {alumno['semestre']}")
            print(f"Carrera: {alumno['carrera']}\n")