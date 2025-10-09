#if else elif
edad = 25 #int(input("dime tu edad"))

if edad >= 10 and edad <18:
    print("eres un adolescente")
elif edad >= 18:  
    print("Eres un adulto") 
    print("Tienes que trabajar")
else:
    print("Todavia eres un niño")    
print("Fin del programa")

#match

opcion = int(input("""
1. Agregar
2. Editar
3. Eliminar
4. Leer
5. Finalizar
"""))


match opcion:
    case 1:
        print("Se ha agregado \n correctamente")
    case 2:
         print("Se ha modificado correctamente")
    case 3:
        print("Se ha eliminado correctamente")
    case 4:
        print("El usuario ha sido registrado, se llama Eduardo")
    case _:
        print("Se finalizara el programa")

