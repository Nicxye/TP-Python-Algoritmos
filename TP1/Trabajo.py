# Ejercicio 1 - Desarrollar una función que permita convertir un número romano en un número decimal.

print("EJERCICIO 1")

romanos = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

numero = "MMXXIII"

def romano_a_decimal(numero_romano):
    if len(numero_romano) == 1:
        return romanos[numero_romano]
    else:
        if romanos[numero_romano[0]] >= romanos[numero_romano[1]]:
            return romanos[numero_romano[0]] + romano_a_decimal(numero_romano[1:])
        else:
            return romano_a_decimal(numero_romano[1:]) - romanos[numero_romano[0]] 

print(f"{numero} en decimal es {romano_a_decimal(numero)}\n")

# Ejercicio 2 - El problema de la mochila Jedi. Suponga que un Jedi (Luke Skywalker, Obi-Wan Kenobi, Rey u
#               otro, el que más le guste) está atrapado, pero muy cerca está su mochila que contiene muchos
#               objetos. Implementar una función recursiva llamada “usar la fuerza” que le permita al Jedi “con
#               ayuda de la fuerza” realizar las siguientes actividades:

#               a. sacar los objetos de la mochila de a uno a la vez hasta encontrar un sable de luz o que no
#               queden más objetos en la mochila;

#               b. determinar si la mochila contiene un sable de luz y cuantos objetos fueron necesarios sacar
#               para encontrarlo;

#               c. Utilizar un vector para representar la mochila.

print("EJERCICIO 2")

def usar_la_fuerza(contenedor, tamanio):
    if (contenedor[0] != "Lightsaber"):
        if (contenedor[0] == "Yoda"):
            print("Eso no era un sable de luz, era Yoda. Probablemente el podria ayudarnos, pero no es lo que pide el ejercicio. Buscando...")
        else:
            print(f"Eso no era un sable de luz, era un/a {contenedor[0]}. Buscando...")

        contenedor.pop(0)
        return usar_la_fuerza(contenedor, tamanio)
    
    if (contenedor[0] == "Lightsaber"):
        return f"Este es el sable! El Jedi ha encontrado su sable en su intento {tamanio - len(contenedor) + 1}."

mochila = ["Guantes", "Cantimplora", "Blaster", "Brujula", "Mapa", "Yoda", "Lightsaber", "Kit médico", "Botas", "Cabeza de C3PO"]
tamanio = len(mochila)
print(usar_la_fuerza(mochila, tamanio))