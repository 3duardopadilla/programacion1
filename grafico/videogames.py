import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Fuente 1: Ventas internas
sales_data = {
    "GameID": ["G1", "G2","G3","G4","G5","G6"],
    "Title": ["GTA VI", "The Sims 4",
              "Super Mario Galaxy","Cooking Mama",
              "Minecraft Bedrock","Super Princess Peach"],
    "Genre": ["Action", "Life Sim",
              "Adventure","Cooking game",
              "Sandbox","Adventure"],
    "Publisher": ["Rockstar", "EA",
              "Nintendo","Nintendo",
              "Microsoft","Nintendo"],
    "Units_Sold_Millions": [15.5, 20.1,
              8.0, 12.3,
              18.2, 19.6]
}

sales_df = pd.DataFrame(sales_data)

#Fuente 2: Reseñas de criticos (externo)
reviews_data= {
    "GameID": ["G1", "G2","G3","G4","G5","G7"], #Nota. G6 falta y G7 sobra.
    "Critic_Score": [7.5, 9.5, 8.8, 9.7, 6.1, 8.0],
    "User_Score": [5.1, 9.1, 8.5, 9.2, np.nan, 7.5] #Un Nan! Alguien olvido puntuar Minecraft Bedrock
} 

reviews_df = pd.DataFrame(reviews_data)

print("--- Datos de Ventas (crudos) ---")
print(sales_df)
print("---Datos de Reseñas (crudos) ---")
print(reviews_df)

# Limpieza de datos y preparacion
# desicion: Rellenaremos el User_Score que falta con el promedio (MC Bedrock)
mean_user_score = reviews_df["User_Score"].mean()#Promedio de calificaciones de los usuarios
reviews_df["User_Score"] = reviews_df["User_Score"].fillna(mean_user_score)

print(f"\n--- Reseñas (Limpias, Nan rellenado con {mean_user_score})---")
print(reviews_df)

#Fusion de tablas (merge)
#Fusionar la tabla de ventas con reseñas, Game ID como llave
#INNER JOIN, Nos quedamos con los juegos que existen en ambas tablas
#G6 va a desaparecer, G7 desaparecera
df = pd.merge(sales_df, reviews_df, on="GameID", how="inner")

print("\n----- Tabla fusionada de ventas + reseñas -----")
print(df)

#Crear nuevas columnas que nos den mas informacion
#Columna que nos de Estimacion de ingresos (Asumiendo que valen $50 cada juego)
df["Revenue_Estimate_Billions"] = (df["Units_Sold_Millions"]*50)/1000

#Columna de la brecha que hay entre reseñas de criticos y los usuarios
df["Score_Gap"] = df["Critic_Score"]-df["User_Score"]

#Columna Estandar puntuacion de los criticos (a 100)
df["Critic_Score_100"] = df["Critic_Score"] * 10

print("\n----- Tabla Transformada (Con nuevas columnas) -----")
print(df)

#Agrupacion por genero y vamos a ver las ventas por millon.
genre_sales = df.groupby("Genre")["Units_Sold_Millions"].sum().sort_values(ascending=False)
print(genre_sales)

#Mostrar una grafica con matplotlib
plt.bar(genre_sales.keys(),genre_sales)
plt.title("Ventas totales por Genero")
plt.ylabel("Unidades vendidas (En millones)")
plt.xlabel("Genero")
plt.grid(axis="y", linestyle="dotted", alpha=0.7)
plt.tight_layout()
plt.show()
