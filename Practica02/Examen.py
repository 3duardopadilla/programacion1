#Examen

print("Acontinuacion se llevara acabo un examen de programacion 1")
print("Primera pregunta: ¿Que estructura de control es mas adecuada para itear sobre \n una secuencia de elementos un numero de veces conocido de antemano")

opcion01 = int(input("""
1. A) Bucle 'para'
2. B) Sentencia condicional 'si'
3. C) Bucle 'repetir'
4. D) Bucle 'mientras'
"""))

match opcion01:
    case 1:
        print("Se ha recolectado la respuesta A")
    case 2:
         print("Se ha recolectado la respuesta B")
    case 3:
        print("Se ha recolectado la respuesta C")
    case 4:
        print("Se ha recolectado la respuesta D")
    case _:
        print("Una pregunta sin responder")

print("Segunda pregunta: ¿Que es un \n algoritmo ")

opcion02 = int(input("""
1. A) Un conjunto de instrucciones escritas en codigo binario
2. B) Un lenguaje de programacion epecifico
3. C) El codigo fuente de un programa de computadora
4. D) Una secuencia de pasos finitos y bien definidos para resolver un problema
"""))

match opcion02:
    case 1:
        print("Se ha recolectado la respuesta A")
    case 2:
         print("Se ha recolectado la respuesta B")
    case 3:
        print("Se ha recolectado la respuesta C")
    case 4:
        print("Se ha recolectado la respuesta D")
    case _:
        print("Una pregunta sin responder")

print("Tercera pregunta: ¿El lenguaje maquina esta compuesto \n por ")

opcion03 = int(input("""
1. A) Simbolos logicos y matematicos
2. B) Pseudocodigo
3. C) Instrucciones en ingles abreviado
4. D) Codigo binario
"""))

match opcion03:
    case 1:
        print("Se ha recolectado la respuesta A")
    case 2:
         print("Se ha recolectado la respuesta B")
    case 3:
        print("Se ha recolectado la respuesta C")
    case 4:
        print("Se ha recolectado la respuesta D")
    case _:
        print("Una pregunta sin responder")

print("Cuarta pregunta: ¿Cual de los siguientes componentes NO es parte fundamental de la \n arquitectura de Von Neumann? ")

opcion04 = int(input("""
1. A) Sistema de entrada/salida
2. B) CPU
3. C) Tarjeta grafica
4. D) Memoria principal
"""))

match opcion04:
    case 1:
        print("Se ha recolectado la respuesta A")
    case 2:
         print("Se ha recolectado la respuesta B")
    case 3:
        print("Se ha recolectado la respuesta C")
    case 4:
        print("Se ha recolectado la respuesta D")
    case _:
        print("Una pregunta sin responder")

print("Quinta pregunta: Un lenguaje de programacion de alto nivel \n se caracteriza por ")

opcion05 = int(input("""
1. A) Ser muy dificil de aprender y leer
2. B) Ser el mas rapido en tiempo de ejecucion
3. C) Tener un control directo y preciso sobre el hardware
4. D) Ser independiente de la arquitectura de la computadora
"""))

match opcion05:
    case 1:
        print("Se ha recolectado la respuesta A")
    case 2:
         print("Se ha recolectado la respuesta B")
    case 3:
        print("Se ha recolectado la respuesta C")
    case 4:
        print("Se ha recolectado la respuesta D")
    case _:
        print("Una pregunta sin responder")

print("Gracias por tus respuestas, el examen ha finalizado")