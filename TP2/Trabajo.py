from pila import Pila

# EJERCICIO 1 -   Dada una pila de películas de las que se conoce su título, estudio cinematográfico y año de estreno,
#                 desarrollar las funciones necesarias para resolver las siguientes actividades:

#                 a. mostrar los nombre películas estrenadas en el año 2014;

#                 b. indicar cuántas películas se estrenaron en el año 2018;

#                 c. mostrar las películas de Marvel Studios estrenadas en el año 2016.

pila = Pila()

peliculas = [
            {"title": "Iron Man", "year": 2008, "studio": "Marvel Studios"},
            {"title": "Inception", "year": 2010, "studio": "Warner Bros."},
            {"title": "Capitan America 2", "year": 2014, "studio": "Marvel Studios"},
            {"title": "Jurassic Park", "year": 1993, "studio": "Amblin"},
            {"title": "Ready Player One", "year": 2018, "studio": "Amblin"},
            {"title": "Avengers Infinity War", "year": 2018, "studio": "Marvel Studios"},
            {"title": "Green Book", "year": 2018, "studio": "Dreamworks"},
            {"title": "Doctor Strange", "year": 2016, "studio": "Marvel Studios"},
            {"title": "El Hobbit 3", "year": 2014, "studio": "Metro-Goldwyn-Mayer"},
            {"title": "GOTG", "year": 2014, "studio": "Marvel Studios"},
            ]

for pelis in peliculas:
    pila.push(pelis)

con = 0

while (pila.size() > 0):
    dato = pila.pop()
    if (dato["year"] == 2014):
        print("\n", dato["title"], "se estreno en 2014.")
    if (dato["year"] == 2018):
        con += 1
    if (dato["year"] == 2016 and dato["studio"] == "Marvel Studios"):
        print("\n", dato["title"], "se estreno en 2016 por Marvel Studios.")

print(f"\n En 2018 se estrenaron {con} peliculas.")

# EJERCICIO 2 -   Dada una pila de personajes de Marvel Cinematic Universe (MCU), de los cuales se dispone de
#                 su nombre y la cantidad de películas de la saga en la que participó, implementar las funciones
#                 necesarias para resolver las siguientes actividades:

#                 a. determinar en qué posición se encuentran Rocket Raccoon y Groot, tomando como posición
#                 uno la cima de la pila;

#                 b. determinar los personajes que participaron en más de 5 películas de la saga, además indicar
#                 la cantidad de películas en la que aparece;

#                 c. determinar en cuantas películas participo la Viuda Negra (Black Widow);

#                 d. mostrar todos los personajes cuyos nombre empiezan con C, D y G.