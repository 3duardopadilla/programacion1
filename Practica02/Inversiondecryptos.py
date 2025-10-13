Totaldesaldo = 0
Cripto = 0
Montoagastar = 0
terminar = False
#    Saldo    I     Cripto  I  Promedio gastado   I
#     500            400            400
print("¿Cuanto vas a gastar en criptos?")
Totaldesaldo = int(input("Vas a gastar: "))
while terminar == False:
    print("¿Cuanto se va a gastar en criptos?")
    Montoagastar = int(input("Lo que se gastara: "))
    Totaldecomprasexitosas = + 1
    Totaldesaldo = Totaldesaldo - Montoagastar
    if Montoagastar <= Totaldesaldo:
        print("La compra ha sido exitosa")
        if Totaldesaldo == 0:
            print("Se agoto tu saldo")
            terminar = True
    elif Montoagastar >= Totaldesaldo:
            print("¿Deseas realizar otra compra?")
            terminar = False
            if Montoagastar <= Totaldesaldo:
                terminar = True
                print("Lo sentimos no cuentas con mas fondos")
            else:
                print("El dinero que le sobra es...", Totaldesaldo) 
                print ("Sus cripto compradas son...", Totaldecomprasexitosas)