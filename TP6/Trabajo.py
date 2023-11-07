from Clases.grafo import Grafo
from random import randint

# 14. Implementar sobre un grafo no dirigido los algoritmos necesario para dar solución a las siguientes
# tareas:
# a. cada vértice representar un ambiente de una casa: cocina, comedor, cochera, quincho,
# baño 1, baño 2, habitación 1, habitación 2, sala de estar, terraza, patio;
# b. cargar al menos tres aristas a cada vértice, y a dos de estas cárguele cinco, el peso de la arista
# es la distancia entre los ambientes, se debe cargar en metros;
# c. obtener el árbol de expansión mínima y determine cuantos metros de cables se necesitan
# para conectar todos los ambientes;
# d. determinar cuál es el camino más corto desde la habitación 1 hasta la sala de estar para
# determinar cuántos metros de cable de red se necesitan para conectar el router con el
# Smart Tv.
print("\nEJERCICIO 14:")
grafo = Grafo(dirigido=False)
print("\nA")
grafo.insert_vertice("banioUno")#
grafo.insert_vertice("banioDos")#
grafo.insert_vertice("cochera")#
grafo.insert_vertice("cocina")#
grafo.insert_vertice("comedor")
grafo.insert_vertice("habitacionUno")#
grafo.insert_vertice("habitacionDos")#
grafo.insert_vertice("patio")#
grafo.insert_vertice("salaDeEstar")#
grafo.insert_vertice("terraza")#
grafo.insert_vertice("quincho")#
print("Cargados")

print("\nB:")
grafo.insert_arist("banioUno", "banioDos", randint(1, 30))
grafo.insert_arist("banioUno", "habitacionUno", randint(1, 15)) #tres
grafo.insert_arist("banioUno", "salaDeEstar", randint(1, 20))

grafo.insert_arist("banioDos", "habitacionDos", randint(1, 20)) #dos + 1 que tiene con banioUno
grafo.insert_arist("banioDos", "terraza", randint(1, 10))

grafo.insert_arist("habitacionUno", "salaDeEstar", randint(1, 15)) #cuatro + 1 que tiene con banioUno
grafo.insert_arist("habitacionUno", "habitacionDos", randint(1, 30))
grafo.insert_arist("habitacionUno", "comedor", randint(1, 20))
grafo.insert_arist("habitacionUno", "habitacionDos", randint(1, 30))


grafo.insert_arist("habitacionDos", "terraza", randint(1, 15))
grafo.insert_arist("habitacionDos", "quincho", randint(1, 35))    #tres + 2 que tiene en (1 en habitacionUno, 1 en banioDos)
grafo.insert_arist("habitacionDos", "patio", randint(1, 30))


grafo.insert_arist("salaDeEstar", "patio", randint(1, 15)) #uno + 2 que tiene en (1 en habitacionUno y 1 en banioUno)


grafo.insert_arist("patio", "quincho", randint(1, 10)) #uno + 2 que tiene en (1 en salaDeEstar y 1 en habitacionDos)

grafo.insert_arist("quincho", "cochera", randint(1, 30)) #uno + 2 que tiene en (1 en habitacionDos y 1 en patio)


grafo.insert_arist("terraza", "cochera", randint(1, 30)) #uno + 2 que tiene en (1 en banioDos y 1 en habitacionDos)

grafo.insert_arist("cochera", "comedor", randint(1, 20)) #uno + 2 que tiene en (1 en terraza, 1 en quincho) 

grafo.insert_arist("cocina", "patio", randint(1, 20))
grafo.insert_arist("cocina", "comedor", randint(1, 10)) #tres
grafo.insert_arist("cocina", "salaDeEstar", randint(1, 20))

                            #comedor ya tiene 3 (1 en cocina, 1 en cochera, 1 en habitacionUno)

print("Cargados")

acu = 0
for arbol in grafo.kruskal():
    for nodo in arbol.split(';'):
        acu += int(nodo.split('-')[-1])

print(f"Se necesitaran {acu} metros.")

print("\nD:")
ori = 'habitacionUno'
des = 'salaDeEstar'
origen = grafo.search_vertice(ori)
destino = grafo.search_vertice(des)
camino_mas_corto = None
if(origen is not None and destino is not None):
    if(grafo.has_path(ori, des)):
        camino_mas_corto = grafo.dijkstra(ori, des)
        fin = des
        while camino_mas_corto.size() > 0:
            value = camino_mas_corto.pop()
            if fin == value[0]:
                print(value[0], value[1])
                fin = value[2]


print("\EJERCICIO 15:")
# 15. Se requiere implementar un grafo para almacenar las siete maravillas arquitectónicas modernas
# y naturales del mundo, para lo cual se deben tener en cuenta las siguientes actividades:
# a. de cada una de las maravillas se conoce su nombre, país de ubicación (puede ser más de
# uno en las naturales) y tipo (natural o arquitectónica);
# b. cada una debe estar relacionada con las otras seis de su tipo, para lo que se debe almacenar
# la distancia que las separa;
# c. hallar el árbol de expansión mínimo de cada tipo de las maravillas;
# d. determinar si existen países que dispongan de maravillas arquitectónicas y naturales;
# e. determinar si algún país tiene más de una maravilla del mismo tipo;
# f. deberá utilizar un grafo no dirigido.


grafo_maravillas_a = Grafo(dirigido=False)
grafo_maravillas_n = Grafo(dirigido=False)

MARAVILLAS_N = grafo_maravillas_n
MARAVILLAS_A = grafo_maravillas_a

print("\nA:")


maravilla = [
    {"nombre":"Amazonas", "pais":["Argentina", "Bolivia", "Brasil", "Colombia", "Ecuador", "Guayana Francesa", "Guyana", "Peru", "Surinam", "Venezuela"], "tipo": "Natural"},
    {"nombre":"Bahia de Ha-Long", "pais": "Vietnam", "tipo": "Natural"},
    {"nombre":"Cataratas del Iguazu", "pais": ["Argentina", "Brasil"], "tipo": "Natural"},
    {"nombre":"Chichen Itza", "pais": "Mexico", "tipo": "Arquitectonica"},
    {"nombre":"Coliseo de Roma", "pais": "Italia", "tipo": "Arquitectonica"},
    {"nombre":"Cristo Redentor", "pais": "Brasil", "tipo": "Arquitectonica"},
    {"nombre":"Gran Muralla China", "pais": "China", "tipo": "Arquitectonica"},
    {"nombre":"Isla Jeju", "pais": "Corea del Sur", "tipo": "Natural"},
    {"nombre":"Machu Picchu", "pais": "Peru", "tipo": "Arquitectonica"},
    {"nombre":"Montania de la Mesa", "pais": "Sudafrica", "tipo": "Natural"},
    {"nombre":"Parque de Komodo", "pais": "Indonesia", "tipo": "Natural"},
    {"nombre":"Petra", "pais": "Jordania", "tipo": "Arquitectonica"},
    {"nombre":"Rio de Puerto Princesa", "pais": "Filipinas", "tipo": "Natural"},
    {"nombre":"Taj Mahal", "pais": "India", "tipo": "Arquitectonica"}
]

for i in maravilla:
    if i["tipo"] == "Natural":
        MARAVILLAS_N.insert_vertice(i["nombre"], i["pais"])
    else:
        MARAVILLAS_A.insert_vertice(i["nombre"], i["pais"])


print("\nB:")
MARAVILLAS_N.insert_arist("Amazonas", "Bahia de Ha-Long", randint(1000, 500000))
MARAVILLAS_N.insert_arist("Amazonas", "Cataratas del Iguazu", randint(1000, 500000))
MARAVILLAS_N.insert_arist("Amazonas", "Isla Jeju", randint(1000, 500000))
MARAVILLAS_N.insert_arist("Amazonas", "Montania de la Mesa", randint(1000, 500000))
MARAVILLAS_N.insert_arist("Amazonas", "Parque de Komodo", randint(1000, 500000))
MARAVILLAS_N.insert_arist("Amazonas", "Rio de Puerto Princesa", randint(1000, 500000))

MARAVILLAS_N.insert_arist("Bahia de Ha-Long", "Cataratas del Iguazu", randint(1000, 500000))
MARAVILLAS_N.insert_arist("Bahia de Ha-Long", "Isla Jeju", randint(1000, 500000))
MARAVILLAS_N.insert_arist("Bahia de Ha-Long", "Montania de la Mesa", randint(1000, 500000))
MARAVILLAS_N.insert_arist("Bahia de Ha-Long", "Parque de Komodo", randint(1000, 500000))
MARAVILLAS_N.insert_arist("Bahia de Ha-Long", "Rio de Puerto Princesa", randint(1000, 500000))

MARAVILLAS_N.insert_arist("Cataratas del Iguazu", "Isla Jeju", randint(1000, 500000))
MARAVILLAS_N.insert_arist("Cataratas del Iguazu", "Montania de la Mesa", randint(1000, 500000))
MARAVILLAS_N.insert_arist("Cataratas del Iguazu", "Parque de Komodo", randint(1000, 500000))
MARAVILLAS_N.insert_arist("Cataratas del Iguazu", "Rio de Puerto Princesa", randint(1000, 500000))

MARAVILLAS_N.insert_arist("Isla Jeju", "Montania de la Mesa", randint(1000, 500000))
MARAVILLAS_N.insert_arist("Isla Jeju", "Parque de Komodo", randint(1000, 500000))
MARAVILLAS_N.insert_arist("Isla Jeju", "Rio de Puerto Princesa", randint(1000, 500000))

MARAVILLAS_N.insert_arist("Montania de la Mesa", "Parque de Komodo", randint(1000, 500000))
MARAVILLAS_N.insert_arist("Montania de la Mesa", "Rio de Puerto Princesa", randint(1000, 500000))

MARAVILLAS_N.insert_arist("Parque de Komodo", "Rio de Puerto Princesa", randint(1000, 500000))

MARAVILLAS_A.insert_arist("Chichen Itza", "Coliseo de Roma", randint(1000, 500000))
MARAVILLAS_A.insert_arist("Chichen Itza", "Cristo Redentor", randint(1000, 500000))
MARAVILLAS_A.insert_arist("Chichen Itza", "Gran Muralla China", randint(1000, 500000))
MARAVILLAS_A.insert_arist("Chichen Itza", "Machu Picchu", randint(1000, 500000))
MARAVILLAS_A.insert_arist("Chichen Itza", "Petra", randint(1000, 500000))
MARAVILLAS_A.insert_arist("Chichen Itza", "Taj Mahal", randint(1000, 500000))

MARAVILLAS_A.insert_arist("Coliseo de Roma", "Cristo Redentor", randint(1000, 500000))
MARAVILLAS_A.insert_arist("Coliseo de Roma", "Gran Muralla China", randint(1000, 500000))
MARAVILLAS_A.insert_arist("Coliseo de Roma", "Machu Picchu", randint(1000, 500000))
MARAVILLAS_A.insert_arist("Coliseo de Roma", "Petra", randint(1000, 500000))
MARAVILLAS_A.insert_arist("Coliseo de Roma", "Taj Mahal", randint(1000, 500000))

MARAVILLAS_A.insert_arist("Gran Muralla China", "Machu Picchu", randint(1000, 500000))
MARAVILLAS_A.insert_arist("Gran Muralla China", "Petra", randint(1000, 500000))
MARAVILLAS_A.insert_arist("Gran Muralla China", "Taj Mahal", randint(1000, 500000))


MARAVILLAS_A.insert_arist("Machu Picchu", "Petra", randint(1000, 500000))
MARAVILLAS_A.insert_arist("Machu Picchu", "Taj Mahal", randint(1000, 500000))

MARAVILLAS_A.insert_arist("Petra", "Taj Mahal", randint(1000, 500000))

print("\nC:")
for vertice in MARAVILLAS_N.kruskal():
    for nodo in vertice.split(";"):
        print(nodo)   
print()
for vertice in MARAVILLAS_A.kruskal():
    for nodo in vertice.split(";"):
        print(nodo)

print("\nD:")