from Clases.cola import Cola
from Clases.cola_prioridad import ColaPrioridad
from Clases.pila import Pila

# EJERCICIO 10  Dada una cola con las notificaciones de las aplicaciones de redes sociales de un Smartphone,
#               de las cual se cuenta con la hora de la notificación, la aplicación que la emitió y el mensaje,
#               resolver las siguientes actividades:
#               a. escribir una función que elimine de la cola todas las notificaciones de Facebook;
#               b. escribir una función que muestre todas las notificaciones de Twitter, cuyo mensaje incluya
#               la palabra ‘Python’, si perder datos en la cola;
#               c. utilizar una pila para almacenar temporáneamente las notificaciones producidas entre las
#               11:43 y las 15:57, y determinar cuántas son.

print("\nEJERCICIO 10")

pila = Pila()
cola = Cola()
cola_new = Cola()
con = 0

notificaciones = [
    {"hora": 1145, "aplicacion": "Facebook", "mensaje": "Carlos le dio me gusta a tu publicacion: 'cursos de Python gratis!'"},
    {"hora": 1500, "aplicacion": "Twitter", "mensaje": "Guido van Rossum compartio tu mensaje 'practicando en Python!'"},
    {"hora": 1640, "aplicacion": "Instagram", "mensaje": "Mark Zuckerberg solicito seguirte. Opciones: Aceptar-Aceptar"},
    {"hora": 1322, "aplicacion": "Twitter", "mensaje": "Has recibido una solicitud de seguimiento."},
    {"hora": 1100, "aplicacion": "Twitter", "mensaje": "Guido van Rossum te ha mandado un mensaje privado: 'Necesito ayuda en Python'"},
    {"hora": 1912, "aplicacion": "Facebook", "mensaje": "Mark Zuckerberg te ha enviado un mensaje: 'Por favor prueba Meta, gastamos como 10 mil millones"}
]

for noti in notificaciones:
    cola.arrive(noti)

while cola.size() > 0:
    dato = cola.attention()
    if ((dato["aplicacion"]) != "Facebook"):
        cola_new.arrive(dato)
    if ((dato["aplicacion"]) == "Twitter" and (dato["mensaje"]).__contains__("Python")):
        print(dato["mensaje"])
    if ((dato["hora"]) >= 1143 and dato["hora"] <= 1557):
        pila.push(dato)
        con += 1

print("Existen", con, "notificaciones que fueron recibidas entre las 11:43 y las 15:57")

# def borrar_facebook(cola):
#     while cola.size() > 0:
#         dato = cola.attention()
#         if ((dato["aplicacion"]) != "Facebook"):
#             cola_new.arrive(dato)



# def borrar_twitter_python(cola, cola_new):
#     while cola.size() > 0:
#         dato = cola.attention()
#         if ((dato["aplicacion"] == "Twitter" and not dato["mensaje"].__contains__("Python"))):
#             cola_new.arrive()

# for noti in notificaciones:
#     dato = cola.attention()
#     if (dato["hora"] >= 1143 and dato["hora"] <= 1557):
#         pila.push(noti)


# EJERCICIO 16

     # Utilice cola de prioridad, para atender la cola de impresión tomando en cuenta el siguiente
     # criterio (1- empleados, 2- staff de tecnologías de la información “TI”, 3- gerente), y resuelva la
     # siguiente situación:
     # a. cargue tres documentos de empleados (cada documento se representa solamente con
     # un nombre).
     # b. imprima el primer documento de la cola (solamente mostrar el nombre de este por pantalla).
     # c. cargue dos documentos del staff de TI.
     # d. cargue un documento del gerente.
     # e. imprima los dos primeros documentos de la cola.
     # f. cargue dos documentos de empleados y uno de gerente.
     # g. imprima todos los documentos de la cola de impresión.

print("\nEJERCICIO 16\n")

cola_p = ColaPrioridad()

print("\nA:")
empresa = [
    {"nombre":"Carlos", "prioridad":1},
    {"nombre":"Jose", "prioridad":1},
    {"nombre":"Maria", "prioridad":1},
]

for i in empresa:
    cola_p.arrive(i["nombre"], i["prioridad"])



print("\nB:")
print(cola_p.attention()[1])


print("\nC:")
empresa = [
    {"nombre":"Ana", "prioridad":2},
    {"nombre":"Pedro", "prioridad":2},
]

for i in empresa:
    cola_p.arrive(i["nombre"], i["prioridad"])

print("\nD:")
empresa = [
    {"nombre":"Ernesto", "prioridad":3},
]

for i in empresa:
    cola_p.arrive(i["nombre"], i["prioridad"])

print("\nE:")
for i in range(2):
    print(cola_p.attention()[1])

print("\nF:")

empresa = [
    {"nombre":"Jose", "prioridad":1},
    {"nombre":"Adrian", "prioridad":1},
    {"nombre":"Juan", "prioridad":3},
]

for i in empresa:
    cola_p.arrive(i["nombre"], i["prioridad"])

print("\nG:")
while cola_p.size() > 0:
    print(cola_p.attention()[1])


# EJERCICIO 22

    # Se tienen una cola con personajes de Marvel Cinematic Universe (MCU), de los cuales se conoce
    # el nombre del personaje, el nombre del superhéroe y su género (Masculino M y Femenino
    # F) –por ejemplo {Tony Stark, Iron Man, M}, {Steve Rogers, Capitán América, M}, {Natasha Romanoff,
    # Black Widow, F}, etc., desarrollar un algoritmo que resuelva las siguientes actividades:
    # a. determinar el nombre del personaje de la superhéroe Capitana Marvel;
    # b. mostrar los nombre de los superhéroes femeninos;
    # c. mostrar los nombres de los personajes masculinos;
    # d. determinar el nombre del superhéroe del personaje Scott Lang;
    # e. mostrar todos datos de los superhéroes o personaje cuyos nombres comienzan
    # con la letra S;
    # f. determinar si el personaje Carol Danvers se encuentra en la cola e indicar su nombre
    # de superhéroes.
print("\nEJERCICIO 22")
cola = Cola()

personajes = [
    {"nombre": "Stephen Strange", "superheroe": "Doctor Strange", "genero": "M"},
    {"nombre": "Tony Stark", "superheroe": "Iron Man", "genero": "M"},
    {"nombre": "Steve Rogers", "superheroe": "Captain America", "genero": "M"},
    {"nombre": "Natasha Romanoff", "superheroe": "Black Widow", "genero": "F"},
    {"nombre": "Wanda Maximoff", "superheroe": "Scarlet Witch", "genero": "F"},
    {"nombre": "Peter Quill", "superheroe": "Star-Lord", "genero": "M"},
    {"nombre": "Carol Danvers", "superheroe": "Captain Marvel", "genero": "F"},
    {"nombre": "Scott Lang", "superheroe": "Ant-Man", "genero": "M"}
]

for perso in personajes:
    cola.arrive(perso)

while cola.size() > 0:
    dato = cola.attention()
    if (dato["superheroe"] == "Captain Marvel"):
        print("El nombre de Capitana Marvel es "+ dato["nombre"]+ "\n")
    if (dato["genero"] == "F"):
        print(dato["superheroe"]+ " es un superheroe femenino.\n")
    if (dato["genero"] == "M"):
        print(dato["nombre"]+ " es un personaje masculino.\n")
    if (dato["nombre"] == "Scott Lang"):
        print("El nombre de superheroe de Scott Lang es " + dato["superheroe"], "\n")
    if (dato["nombre"].startswith('S') or dato["superheroe"].startswith('S')):
        print("El nombre de superheroe o personaje de " + dato["nombre"]+ " empieza con la letra S.\n")
    if (dato["nombre"] == "Carol Danvers"):
        print("Carol Danvers se encuentra en la cola y su nombre de superheroe es: " + dato["superheroe"])