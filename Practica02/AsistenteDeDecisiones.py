print("Asistente de decisiones Activado")
print("¿Que dia de la semana es hoy?")

dia = int(input("""
1. Lunes.
2. Martes.
3. Miercoles.
4. Jueves.
5. Viernes.
6. Sabado.
7. Domingo.
"""))

match dia:
    case 1:
        print("Haz seleccionado el dia lunes")
        print("¿Como esta el clima?")
        opciondeclima = int(input("""
        1. Soleado
        2. Lluvioso
        3. Nublado
        """))

        if opciondeclima == 1:
            print("Deberias salir a correr, no olvides hidratarte!")
        elif opciondeclima == 2 and 3:
            print("No deberias salir con este clima, quedate adentro y lee un libro")
            print("Espera que el clima mejore")
        else:
            print("Deberias resguardarte")
    case 2:
        print("Haz seleccionado el dia martes")
        print("¿Como esta el clima?")
        opciondeclima = int(input("""
        1. Soleado
        2. Lluvioso
        3. Nublado
        """))

        if opciondeclima == 1:
            print("Deberias salir a correr, no olvides hidratarte!")
        elif opciondeclima == 2 and 3:
            print("Quiza puedas quedarte leyendo en casa")
            print("Espera que el clima mejore")
        else:
            print("Deberias resguardarte")
    case 3:
        print("Haz seleccionado el dia miercoles")
        print("¿Como esta el clima?")
        opciondeclima = int(input("""
        1. Soleado
        2. Lluvioso
        3. Nublado
        """))
    
    
        if opciondeclima == 1:
            print("Deberias ir al parque, el clima esta agradable!")
        elif opciondeclima == 2 and 3:
             print("No deberias salir con este clima, quedate adentro y lee un libro")
             print("Espera que el clima mejore")
        else:
             print("Deberias resguardarte")
    case 4:
        print("Haz seleccionado el dia jueves")
        print("¿Como esta el clima?")
        opciondeclima = int(input("""
        1. Soleado
        2. Lluvioso
        3. Nublado
        """))

        if opciondeclima == 1:
            print("Deberias salir a correr, no olvides hidratarte!")
        elif opciondeclima == 2 and 3:
            print("Ve a jugar un poco en la lluvia, el agua esta fresquita")
            print("El clima no esta tan mal")
        else:
            print("Quedate en casa a reponerte")
    case 5:
        print("Haz seleccionado el dia viernes")
        print("¿Como esta el clima?")
        opciondeclima = int(input("""
        1. Soleado
        2. Lluvioso
        3. Nublado
        """))

        if opciondeclima == 1:
            print("Deberias de hacer una rutina de ejercicios, no olvides hidratarte!")
        elif opciondeclima == 2 and 3:
            print("No deberias salir con este clima tan espantoso, quedate adentro y lee un libro")
            print("Espera que el clima mejore y quedate seguro")
        else:
            print("Deberias resguardarte")
