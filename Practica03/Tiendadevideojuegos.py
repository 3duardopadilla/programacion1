Info_de_Tienda = ("¡Videogames are so fun!", "2015")
Inventario_de_juegos = {
    'Super Mario Bros Wonder': {"Precio": 1600, "stock": 200},
    'The Legend of Zelda: Breath of the wild': {"Precio": 1400, "stock": 350},
    'Mario Kart World': {"Precio": 1800, "stock": 500}
}
print(f"El precio de The Legend of Zelda es:", Inventario_de_juegos['The Legend of Zelda: Breath of the wild']['Precio'])
Inventario_de_juegos['Super Mario Bros Wonder']['stock'] -=1
print("¡Gracias por su compra!, ahora asi quedo nuestro Stock:", Inventario_de_juegos['Super Mario Bros Wonder']['stock'])