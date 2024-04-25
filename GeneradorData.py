
#Librería Random para seleccionar aleatoriamente.
import random as rd
#Librería json para leer y escribir el formato json en nuestro dataset.
import json

#Opciones de selección aleatoria para datos de Videojuegos, Generos y Plataformas.
#TODO: Agregar más datos para obtener más datos aleatorios y variados.
videojuegos = ["The Witcher 3", "Civilization VI", "Stardew Valley", "FIFA 22", "NBA 2K22", "Age of Empires II", "Total War: Rome II", "Super Mario Bros", "Pac-Man", "Uncharted 4", "Tomb Raider"]
generos = ["RPG", "Estrategia", "Simulación", "Deportes", "Acción", "Arcade", "Plataforma", "Aventura"]
plataformas = ["PC", "Nintendo Switch", "PS5", "Xbox One", "NES", "Arcade", "PS4"]

#Funcion generar usuario según un ID
def generarUsuario(id):
    #Genera un usuario con nombre "User + Parámetro(Id)" y con datos aleatorios de la lista predefinida.
    nombre_usuario = "User" + str(id)
    #Asigna a cada dato, una lista de videojuegos, generos y/o plataformas. 
    videojuegos_favoritos = rd.sample(videojuegos, rd.randint(1, 5))
    generos_preferidos = rd.sample(generos, rd.randint(1, 5))
    plataformas_juego = rd.sample(plataformas, rd.randint(1, 5))
    
    #Se retorna un diccionario de python con los datos.
    return {
        "id": str(id).zfill(3),
        "nombreUsuario": nombre_usuario,
        "videojuegosFavoritos": videojuegos_favoritos,
        "generosPreferidos": generos_preferidos,
        "plataformasJuego": plataformas_juego
    }

#Funcion para generar N usuarios, cada participante deberá usar esta función para generar nuestros 500 datos.
def generarUsuarios(n):
    #Retorna una lista de diccionarios que será agregado al data set de json.
    return [generarUsuario(i) for i in range(1, n + 1)]


#TODO: Realizar agregación de datos por cada uno.

# Generación y adición de sus datos para Fernando Daniel Quispe Condori
usuarios = generarUsuarios(500)

with open('dataset.json', 'w') as f:
    json.dump(usuarios, f, indent=4)
