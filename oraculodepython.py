def iniciar_oraculo():
    print("Sea bienvenido al grandioso oraculo de Python, ¿Deseas conocer tu destino?")
iniciar_oraculo = int(input("""
1. Si
2. No
"""))
while iniciar_oraculo == 1:
    Nombre = (input("Ingresa tu nombre:"))
    print("Asi que te llamas", Nombre, "Bien...")
    Nacimiento = int(input("Ingresa tu año de nacimiento:"))
    def calcular_elemento(Nacimiento):
        Elementocalculado = Nacimiento % 10
        return Elementocalculado
    def asignarme_un_elemento(Elementocalculado):
        if Elementocalculado == 0 or 1:
            Elemento = ("Metal")
        elif Elementocalculado == 2 or 3:
            Elemento = ("Agua")
        elif Elementocalculado == 4 or 5:
            Elemento = ("Madera")
        elif Elementocalculado == 6 or 7:
            Elemento = ("Fuego")
        elif Elementocalculado == 8 or 9:
            Elemento = ("Tierra")
        return print(Elemento)
    print("Bien ahora elige tu numero de la suerte del 1 a 4")
    Numero_de_suerte = int(input("""
    1. Elegir el Num 1
    2. Elegir el Num 2
    3. Elegir el Num 3
    4. Elegir el Num 4
    """))
    def generar_prediccion(Nombrepara, Elementopara):
        Elemento = ()
        Nombrepara == Nombre
        Elementopara == Elemento
        match Numero_de_suerte:
            case 1:
                print(f"Felicitaciones", {Nombre}, "la conexion que tienes con el elemento...", {Elemento}, "Es demasiado poderosa, seras una peesona bastante sabia!☄")
            case 2:
                print(f"Muy bien", {Nombre}, "tu conexion con el elemento", {Elemento}, "Trasciende mas de lo que alguien comun se esperaria, sigue asi☄")
            case 3:
                print(f"Tu camino es uno muy dificil de recorrer", {Nombre}, "pero alguien con tu elemento como lo es el...", {Elemento}, "tiene un futuro brillante☄")
            case 4:
                print(f"Vaya", {Nombre}, "Tu futuro se ve realmente esperanzador, no me sorprende pues despues de todo posees el elemento", {Elemento}, "☄")
    print("¿Deseas conocer tu destino? (De nuevo)")
    iniciar_oraculo = int(input("""
    1. Si
    2. No
    """))
    break