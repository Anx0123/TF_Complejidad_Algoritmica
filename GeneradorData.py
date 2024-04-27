
#Librería Random para seleccionar aleatoriamente.
import random as rd
#Librería json para leer y escribir el formato json en nuestro dataset.
import json
import os

#Opciones de selección aleatoria para datos de Videojuegos, Generos y Plataformas.
#TODO: Agregar más datos para obtener más datos aleatorios y variados.
videojuegos = ["The Witcher 3", "Civilization VI", "Stardew Valley", "FIFA 22", "NBA 2K22", "Age of Empires II", "Total War: Rome II", "Super Mario Bros", "Pac-Man", "Uncharted 4", "Tomb Raider"]
generos = ["RPG", "Estrategia", "Simulación", "Deportes", "Acción", "Arcade", "Plataforma", "Aventura"]
plataformas = ["PC", "Nintendo Switch", "PS5", "Xbox One", "NES", "Arcade", "PS4"]

#Lista de videojuegos, plataformas y generos "raros" así evitamos intereses comunes muy fácilmente relacionados en el grafo.
videojuegos_raros = ["Juego Indie 1", "Juego Retro 1"]
generos_raros = ["Visual Novel", "Text Adventure"]
plataformas_raras = ["Linux", "Mac"]

# Funcion para agregar intereses raros a cada usuario
def agregarInteresesRaros(intereses, raros):
    if not set(intereses).intersection(set(raros)):
        intereses.append(rd.choice(raros))
    return intereses

#Eventos externos que pueden influir en los intereses de los usuarios
eventos = ["Lanzamiento de nuevo juego", "Popularidad de un género", "Ofertas en una plataforma"]

# Funcion para aplicar un evento externo aleatorio a los intereses de los usuarios
def aplicarEventoAleatorio(usuario):
    evento = rd.choice(eventos)
    if evento == "Lanzamiento de nuevo juego":
        nuevo_juego = "Nuevo Juego AAA"
        if nuevo_juego not in usuario["videojuegosFavoritos"]:
            usuario["videojuegosFavoritos"].append(nuevo_juego)
    elif evento == "Popularidad de un género":
        nuevo_genero = "Battle Royale"
        if nuevo_genero not in usuario["generosPreferidos"]:
            usuario["generosPreferidos"].append(nuevo_genero)
    elif evento == "Ofertas en una plataforma":
        nueva_plataforma = "Steam"
        if nueva_plataforma not in usuario["plataformasJuego"]:
            usuario["plataformasJuego"].append(nueva_plataforma)

#Funcion generar usuario según un ID
def generarUsuario(id):
    #Genera un usuario con nombre "User + Parámetro(Id)" y con datos aleatorios de la lista predefinida.
    nombre_usuario = "User" + str(id)
    #Asigna a cada dato, una lista de videojuegos, generos y/o plataformas. 
    videojuegos_favoritos = rd.sample(videojuegos, rd.randint(1, 3))
    generos_preferidos = rd.sample(generos, rd.randint(1, 3))
    plataformas_juego = rd.sample(plataformas, rd.randint(1, 3))
    
    # Asegurar que cada usuario tenga al menos un interés raro
    videojuegos_favoritos = agregarInteresesRaros(videojuegos_favoritos, videojuegos_raros)
    generos_preferidos = agregarInteresesRaros(generos_preferidos, generos_raros)
    plataformas_juego = agregarInteresesRaros(plataformas_juego, plataformas_raras)

    #Se retorna un diccionario de python con los datos.
    return {
        "id": str(id).zfill(3),
        "nombreUsuario": nombre_usuario,
        "videojuegosFavoritos": videojuegos_favoritos,
        "generosPreferidos": generos_preferidos,
        "plataformasJuego": plataformas_juego
    }

# Funcion para generar N usuarios
def generarUsuarios(n, start_id):
    return [generarUsuario(i) for i in range(start_id, start_id + n)]

# Leer datos existentes y agregar nuevos usuarios
def agregarUsuariosAlJson(n):
    filename = 'dataset.json'
    usuarios_existentes = []
    start_id = 1
    
    # Verificar si el archivo ya existe para leer los datos existentes
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            usuarios_existentes = json.load(file)
            # Determinar el nuevo ID de inicio basado en la cantidad existente de usuarios
            if usuarios_existentes:
                start_id = int(usuarios_existentes[-1]["id"]) + 1
    
    # Generar nuevos usuarios
    nuevos_usuarios = generarUsuarios(n, start_id)
    
    # Combinar listas de usuarios existentes y nuevos
    usuarios_actualizados = usuarios_existentes + nuevos_usuarios
    
    # Escribir la lista actualizada de usuarios en el archivo
    with open(filename, 'w') as file:
        json.dump(usuarios_actualizados, file, indent=4)

# Ejemplo de uso: agregar 2 nuevos usuarios al JSON
agregarUsuariosAlJson(2)