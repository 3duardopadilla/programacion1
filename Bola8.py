import random
Nombre = input("¿Cual es tu nombre?")
def iniciar_bola_magica_8():
    respuestas = [
        "Es cierto",
        "Es decididamente así",
        "Sin lugar a dudas",
        "Sí, definitivamente",
        "Puedes confiar en ello.",
        "Respuesta confusa, vuelve a intentarlo",
        "Vuelve a preguntar más tarde",
        "No se puede predecir ahora",
        "Concéntrate y vuelve a preguntar.",
        "No cuentes con ello",
        "Mi respuesta es no",
        "Mis fuentes dicen que no",
        "Las perspectivas no son muy buenas",
        "Muy dudoso."
    ]
    print("Bienvenido a la bola magica 8.... Hazme cualquier pregunta y te dare la respuesta.")
    input("presiona enter para continuar")

    while True:
        pregunta = input("Hazme la pregunta (O escribe 'no' para terminar)").lower()
        if pregunta.lower() == 'no':
            print("Bien, no todos estan hechos para saber la verdad ni la de ellos mismos.")
            break
        respuestaSeleccionada = random.choice(respuestas)
        print(f"Mi respuesta ante tu pregunta es: {respuestaSeleccionada}\n")

iniciar_bola_magica_8()