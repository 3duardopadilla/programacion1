#Crear un analizador de textos
#Texto: GRACIAS A LAS NUEVAS TECNOLOGIAS, USAR PYTHON ES CADA VEZ MAS FACIL
#Letras: A, T y O
print("Bienvenido a tu analizador de textos, por favor introduzca el texto que desea que sea analizado")
Texto = input("Introduce el texto: ").lower()
print("Ahora introduzca las tres letras solicitadas")
Letra01 = input("Introduce la primera letra: ").lower()
Letra02 = input("Introduce la segunda letra: ").lower()
Letra03 = input("Introduce la segunda letra: ").lower()
print("¿Cuantas veces aparecen cada una de las letras elegidas?")
count_letra1 = Texto.count(Letra01)
count_letra2 = Texto.count(Letra02)
count_letra3 = Texto.count(Letra03)
for Primeraletra in Texto:
        if Primeraletra == Letra01:
                print("La primera letra aparece un total de:", count_letra1, "veces")
                break     
for Segundaletra in Texto:
        if Segundaletra == Letra02:
                print("La segunda letra aparece un total de:", count_letra2, "veces")
                break
for Tercerletra in Texto:
        if Tercerletra == Letra03:
                print("La tercer letra aparece un total de:", count_letra3, "veces")
                break
print("¿Cuantas palabras hay en el texto?")
contar_palabras =  len(Texto.split())  
print(f"Tu numero de palabras es: {contar_palabras}")
print("¿Cual es la primera y ultima letra del texto?")
Primera_Letra = Texto[0:1]
Ultima_Letra = Texto[66:67]
print("La primera letra de tu texto es:", Primera_Letra)
print("La ultima letra de tu texto es:", Ultima_Letra)
print("¿Y como seria el texto al reves?")
Texto_al_reves = ''.join(reversed(Texto))
print(Texto_al_reves)
print("La palabra Python se encuentra en este texto?...")
if "python" in Texto:
        print("Si, la palabra Python esta en este texto.")
else:
        print("No, la palabra no se encuentra en ningun lado")
